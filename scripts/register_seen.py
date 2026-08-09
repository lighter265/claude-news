"""feed.md のURLをDBへ登録/更新する。rawからスコア等を補完する。"""
import glob
import json
import os
import re
import sqlite3
from datetime import date

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(REPO, "local", "seen_urls.db")
RAW_DIR = os.path.join(REPO, "raw")
FEED_PATH = os.path.join(REPO, "feed.md")
FEED_LLM_PATH = os.path.join(REPO, "feed-local-llm.md")
FEED_PATHS = (FEED_PATH, FEED_LLM_PATH)


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


def load_raw_index():
    index = {}
    for path in glob.glob(os.path.join(RAW_DIR, "*.json")):
        if os.path.basename(path).startswith("section_"):
            continue
        with open(path, encoding="utf-8") as f:
            items = json.load(f)
        for item in items:
            url = item.get("url", "")
            if url:
                index[url] = item
    return index


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


def extract_urls(feed_path):
    urls = []
    with open(feed_path, encoding="utf-8") as f:
        for line in f:
            # 行全体がURLのケース（旧形式）とテーブル行内のURL（新形式）の両対応
            for m in re.finditer(r"https?://[^\s|)]+", line):
                urls.append(m.group(0))
    return urls


def main():
    existing_feed_paths = [path for path in FEED_PATHS if os.path.exists(path)]
    if not existing_feed_paths:
        print("[register] feed.md/feed-local-llm.md not found, skip.")
        return

    # CIFS filesystem では fcntl locking 非対応のため nolock=1 を使用
    conn = sqlite3.connect(f"file://{DB_PATH}?nolock=1", uri=True)
    init_db(conn)

    raw_index = load_raw_index()
    # 通常ニュースに加え、feed-local-llm.md のReddit/GitHub記事も登録する。
    # 同一URLが両方のフィードに出る場合は1回だけ更新する。
    urls = list(dict.fromkeys(
        url
        for path in existing_feed_paths
        for url in extract_urls(path)
    ))
    today = date.today().isoformat()

    for url in urls:
        item = raw_index.get(url, {})
        source = item.get("source")
        score = item.get("score")
        comments = parse_comments(item.get("extra"))
        conn.execute(
            """
            INSERT INTO seen_urls
                (url, source, first_seen, last_seen, last_score, last_comments, times_shown)
            VALUES (?, ?, ?, ?, ?, ?, 1)
            ON CONFLICT(url) DO UPDATE SET
                last_seen     = excluded.last_seen,
                last_score    = excluded.last_score,
                last_comments = excluded.last_comments,
                times_shown   = times_shown + 1
            """,
            (url, source, today, today, score, comments),
        )

    conn.commit()
    conn.close()
    print(f"[register] {len(urls)} URLs registered from feed.md")


if __name__ == "__main__":
    main()
