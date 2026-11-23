"""r/LocalLLaMA の新着投稿を donsetch 経由で取得する。

旧実装は Atom RSS（2026-11-13 で Reddit が RSS を廃止）だったが、
donsetch の api.reddit.com ルートなら未認証でも一覧と本文が取れる。
取得した記事は旧スキーマの ``article()`` で ``raw/reddit_local_llm.json`` に保存する
（下流の filter_seen / 要約 / register_seen は変更しない）。

フロー:
  1. donsetch fetch 'api.reddit.com/r/LocalLLaMA/new?limit=N' --links --json
     → permalink（1y... 形式）入りの一覧をパース。
  2. permalink を最大 BATCH_SIZE 件ずつ donsetch fetch <urls...> --json
     → OP 本文を ``extra`` にマッピング。
  3. 旧 article() スキーマで save_raw(...)。失敗時は .failed マーカーを置き、
     raw は上書きしない（2026-10-27 の事故再発防止）。
"""
import json
import os
import re
import subprocess
import time
from datetime import datetime, timedelta, timezone

from common import article, save_raw

# donsetch のバイナリ（cron の最小 PATH でも動くよう絶対パスを既定にする）。
DONSETCH_BIN = os.environ.get(
    "DONSETCH_BIN",
    "/home/lighter/.nvm/versions/node/v24.22.2/lib/node_modules/donsetch/binaries/donsetch",
)
# new の一覧は最大40件まで。直近48時間で24件程度なので40で十分カバーできる。
LIST_URL = "https://api.reddit.com/r/LocalLLaMA/new?limit=40"
RECENT_WINDOW_HOURS = 48
DESCRIPTION_MAX_CHARS = 500
# サーバー過負荷とIP BANを避けるため1件ずつ読む（donsetch自体は12件並列だが使わない）。
BATCH_SIZE = 1
FETCH_INTERVAL_SECONDS = 2.0
FETCH_TIMEOUT_SECONDS = 120

# 一覧行: "- [title](url) — (domain) · N pts · u/name · N comments"
LIST_ROW = re.compile(
    r"^- \[(?P<title>.*?)\]\((?P<url>https://www\.reddit\.com/r/LocalLLaMA/comments/[^\s)]+)\)"
    r"(?P<rest>.*)$"
)
SCORE_RE = re.compile(r"(?P<n>[\d,]+)\s+pts?\b")
COMMENTS_RE = re.compile(r"(?P<n>[\d,]+)\s+comments?\b")
# 本文のメタ行: "u/name · 2 pts · 3h · 27 comments · r/LocalLLaMA"
RELATIVE_TIME_RE = re.compile(r"(?<![\d.])(?P<n>\d+)\s*(?P<unit>s|m|h|d|mo|y)\b")
CHANGED_HEADER_RE = re.compile(r"^\*\[changed since last fetch.*?\*\s*$", re.MULTILINE)


def _run_donsetch(args):
    """donsetch をsubprocessで呼び、JSON envelope を返す。"""
    cmd = [DONSETCH_BIN] + args + ["--json"]
    proc = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=FETCH_TIMEOUT_SECONDS,
        check=False,
    )
    if proc.returncode != 0:
        raise RuntimeError(
            f"donsetch exited {proc.returncode}: {proc.stderr.decode('utf-8', 'replace')[:400]}"
        )
    try:
        return json.loads(proc.stdout.decode("utf-8", "replace"))
    except json.JSONDecodeError as error:
        raise RuntimeError(f"donsetch returned non-JSON: {error}") from error


def _parse_list(content):
    """一覧の markdown から記事の素情報を取り出す。"""
    content = CHANGED_HEADER_RE.sub("", content)
    items = []
    for line in content.splitlines():
        match = LIST_ROW.match(line.strip())
        if not match:
            continue
        rest = match.group("rest")
        score_match = SCORE_RE.search(rest)
        comments_match = COMMENTS_RE.search(rest)
        items.append({
            "title": match.group("title"),
            "url": match.group("url"),
            "score": int(score_match.group("n").replace(",", "")) if score_match else None,
            "num_comments": int(comments_match.group("n").replace(",", "")) if comments_match else 0,
        })
    return items


def _parse_thread(content, url):
    """スレッド本文から (著者, 相対時刻, スコア, 本文テキスト) を取り出す。"""
    content = CHANGED_HEADER_RE.sub("", content)
    lines = content.splitlines()

    # タイトル行(# ...)と URL 行を飛ばし、メタ行を探す。
    meta = None
    body_start = 0
    for index, line in enumerate(lines):
        if line.startswith("u/") and "·" in line:
            meta = line
            body_start = index + 1
            break
    if meta is None:
        return None

    score_match = SCORE_RE.search(meta)
    relative_match = RELATIVE_TIME_RE.search(meta)
    body_lines = []
    for line in lines[body_start:]:
        if line.strip() == "---":
            break
        body_lines.append(line)
    body = "\n".join(body_lines).strip()
    if len(body) > DESCRIPTION_MAX_CHARS:
        body = body[:DESCRIPTION_MAX_CHARS].rstrip() + "…"

    return {
        "score": int(score_match.group("n").replace(",", "")) if score_match else None,
        "relative": relative_match.group(0) if relative_match else "",
        "extra": body,
    }


def _relative_to_timestamp(relative, now):
    """'3h' のような相対時刻を UNIX 秒に変換する。取れなければ None。"""
    match = RELATIVE_TIME_RE.search(relative or "")
    if not match:
        return None
    amount = int(match.group("n"))
    unit = match.group("unit")
    seconds = {
        "s": 1, "m": 60, "h": 3600, "d": 86400,
        "mo": 2592000, "y": 31536000,
    }[unit]
    return int((now - timedelta(seconds=amount * seconds)).timestamp())


def _fetch_list():
    """一覧を取得して記事の素情報を返す。"""
    envelope = _run_donsetch(["fetch", LIST_URL, "--links"])
    if not envelope.get("ok"):
        raise RuntimeError(f"donsetch list fetch failed: {envelope.get('error')}")
    return _parse_list(envelope.get("content", ""))


def _fetch_threads(items):
    """permalink を1件ずつ読み、本文情報を url キーの辞書で返す。

    サーバー負荷とIP BANを避けるため、2件目以降は FETCH_INTERVAL_SECONDS 待つ。
    """
    result = {}
    for start in range(0, len(items), BATCH_SIZE):
        if start:
            time.sleep(FETCH_INTERVAL_SECONDS)
        batch = items[start:start + BATCH_SIZE]
        urls = [item["url"] for item in batch]
        envelope = _run_donsetch(["fetch"] + urls)
        for entry in envelope.get("results", []):
            url = entry.get("url")
            if not entry.get("ok") or not url:
                continue
            parsed = _parse_thread(entry.get("content", ""), url)
            if parsed:
                result[url] = parsed
    return result


def fetch(limit=None, recent_hours=RECENT_WINDOW_HOURS, now=None):
    """donsetch で新着投稿を取得し、旧 article() スキーマのリストを返す。

    ``limit`` は返す最大件数。``recent_hours`` は旧スクリプト互換の引数だが、
    donsetch の一覧には created_utc が無いため、本文の相対時刻で
    48 時間を超えるものを除外する（相対時刻が取れない件は残す）。
    """
    now = now or datetime.now(timezone.utc)
    if now.tzinfo is None:
        now = now.replace(tzinfo=timezone.utc)
    now = now.astimezone(timezone.utc)
    cutoff = int((now - timedelta(hours=recent_hours)).timestamp())

    listed = _fetch_list()
    threads = _fetch_threads(listed)

    items = []
    seen_urls = set()
    for row in listed:
        url = row["url"]
        if not url or url in seen_urls:
            continue
        seen_urls.add(url)
        thread = threads.get(url, {})
        timestamp = _relative_to_timestamp(thread.get("relative"), now)
        if timestamp is not None and timestamp < cutoff:
            continue
        item = article(
            "reddit_local_llm",
            row["title"],
            url,
            score=thread.get("score") or row["score"],
            timestamp=timestamp,
            extra=thread.get("extra"),
        )
        # スレッド側のコメント数を extra に残す（filter_seen.py の parse_comments が読む）。
        if row["num_comments"]:
            comments = f"comments: {row['num_comments']}"
            item["extra"] = f"{comments}\n{item['extra']}" if item["extra"] else comments
        if timestamp is not None:
            item["published_at"] = datetime.fromtimestamp(timestamp, timezone.utc).isoformat()
        items.append(item)

    items.sort(key=lambda item: item["timestamp"] or 0, reverse=True)
    return items[:limit] if limit else items


def _failure_marker_path():
    from common import RAW_DIR
    return os.path.join(RAW_DIR, "reddit_local_llm.failed")


if __name__ == "__main__":
    marker = _failure_marker_path()
    error = None
    # donsetch が直前に別の取得で busy だと一時的に exit 3 を返すことがある。
    # 5秒待って1回だけ再試行する（IP BAN 対策の2秒間隔には影響しない）。
    for attempt in range(2):
        try:
            data = fetch()
            path = save_raw("reddit_local_llm", data)
            if os.path.exists(marker):
                os.remove(marker)
            print(path)
            error = None
            break
        except Exception as caught:
            error = caught
            if attempt == 0:
                print(f"[reddit] attempt 1 failed ({caught}); retry in 5s")
                time.sleep(5.0)
    if error is not None:
        # 空結果で上書きすると「該当記事なし」として静かに公開される事故を防ぐ。
        # raw は触らず、失敗マーカーだけを置く（execute.sh が退避＋明記する）。
        with open(marker, "w", encoding="utf-8") as f:
            f.write(f"{type(error).__name__}: {error}")
        print(f"[reddit] fetch failed: {type(error).__name__}: {error}")
        raise error
