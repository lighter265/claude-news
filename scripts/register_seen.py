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
            line = line.strip()
            if re.match(r"^https?://\S+$", line):
                urls.append(line)
    return urls


def main():
    if not os.path.exists(FEED_PATH):
        print("[register] feed.md not found, skip.")
        return

    # CIFS filesystem では fcntl locking 非対応のため nolock=1 を使用
    conn = sqlite3.connect(f"file://{DB_PATH}?nolock=1", uri=True)
    init_db(conn)

    raw_index = load_raw_index()
    urls = extract_urls(FEED_PATH)
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
