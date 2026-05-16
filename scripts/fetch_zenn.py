"""Zenn のデイリートレンドを公式 API から取得。

published_at は "+09:00" 付き ISO 形式。先頭19文字を切り出して扱う。
"""
from datetime import datetime

from common import http_get_json, article, save_raw


def _ts(s):
    if not s:
        return None
    try:
        return int(datetime.fromisoformat(s[:19]).timestamp())
    except ValueError:
        return None


def fetch(limit=25):
    data = http_get_json("https://zenn.dev/api/articles?order=daily")
    items = []
    for a in data.get("articles", []):
        items.append(article(
            "zenn",
            a.get("title"),
            "https://zenn.dev" + a.get("path", ""),
            score=a.get("liked_count"),
            timestamp=_ts(a.get("published_at")),
            extra=a.get("article_type"),
        ))
    return items[:limit]


if __name__ == "__main__":
    print(save_raw("zenn", fetch()))
