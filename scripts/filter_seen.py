"""DB参照でraw/*.jsonから既出URLを除去する。DBは変更しない。"""
import glob
import json
import os
import sqlite3
from datetime import date

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(REPO, "local", "seen_urls.db")
RAW_DIR = os.path.join(REPO, "raw")

# 既出でも除去せず、``seen_before`` を付けて新規/継続を分けて表示するソース。
ANNOTATE_ONLY_SOURCES = {"reddit_local_llm"}

SCORE_INCREASE_RATIO = 1.3   # 前回比 +30%
COMMENT_INCREASE_DELTA = 20  # 前回比 +20件


def init_db(conn):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS seen_urls (
            url           TEXT PRIMARY KEY,
            source        TEXT,
            first_seen    TEXT,
            last_seen     TEXT,
            last_score    INTEGER,
            last_comments INTEGER,
            times_shown   INTEGER DEFAULT 0
        )
    """)
    conn.commit()


def load_seen(conn):
    cur = conn.execute("SELECT url, last_score, last_comments FROM seen_urls")
    return {row[0]: {"score": row[1], "comments": row[2]} for row in cur}


def parse_comments(extra):
    if not extra:
        return 0
    for part in extra.split(","):
        part = part.strip()
        if part.lower().startswith("comments:"):
            try:
                return int(part.split(":", 1)[1].strip())
            except (ValueError, IndexError):
                pass
    return 0


def should_show(item, seen):
    url = item.get("url", "")
    if not url or url not in seen:
        return True
    prev = seen[url]
    cur_score = item.get("score") or 0
    cur_comments = parse_comments(item.get("extra"))
    prev_score = prev["score"] or 0
    prev_comments = prev["comments"] or 0
    if prev_score > 0 and cur_score >= prev_score * SCORE_INCREASE_RATIO:
        return True
    if cur_comments >= prev_comments + COMMENT_INCREASE_DELTA:
        return True
    return False


def main():
    # CIFS filesystem では fcntl locking 非対応のため nolock=1 を使用
    conn = sqlite3.connect(f"file://{DB_PATH}?nolock=1", uri=True)
    init_db(conn)

    # 登録後4日経過した既出URLを削除
    cursor = conn.cursor()
    cursor.execute("DELETE FROM seen_urls WHERE first_seen <= date('now', '-4 days')")
    deleted_count = cursor.rowcount
    if deleted_count > 0:
        conn.commit()
        print(f"[filter] Deleted {deleted_count} expired seen URL(s) (older than 4 days)")

    seen = load_seen(conn)
    seen_before_today = {
        row[0] for row in conn.execute(
            "SELECT url FROM seen_urls WHERE first_seen < ?", (date.today().isoformat(),)
        )
    }
    conn.close()

    total_before = total_after = 0
    for path in sorted(glob.glob(os.path.join(RAW_DIR, "*.json"))):
        if os.path.basename(path).startswith("section_"):
            continue
        with open(path, encoding="utf-8") as f:
            items = json.load(f)
        if os.path.basename(path)[:-len(".json")] in ANNOTATE_ONLY_SOURCES:
            # 48時間窓のため前日掲載分と重なる。落とさず「前日にも掲載済みか」を付与する。
            # 当日の再実行でも結果が変わらないよう、登録日が今日より前のものだけを既出とする。
            for item in items:
                item["seen_before"] = item.get("url", "") in seen_before_today
            filtered = items
        else:
            filtered = [item for item in items if should_show(item, seen)]
        total_before += len(items)
        total_after += len(filtered)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(filtered, f, ensure_ascii=False, indent=2)
        print(f"[filter] {os.path.basename(path)}: {len(items)} → {len(filtered)} items")

    print(f"--- filter done. {total_before} → {total_after} items total ---")


if __name__ == "__main__":
    main()
