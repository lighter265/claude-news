"""Hacker News を Algolia Search API から取得。過去24時間・スコア順。"""
import time

from common import http_get_json, article, save_raw


def fetch(limit=30):
    since = int(time.time()) - 86400
    url = ("https://hn.algolia.com/api/v1/search_by_date"
           f"?tags=story&numericFilters=created_at_i>{since}&hitsPerPage=100")
    data = http_get_json(url)
    items = []
    for h in data.get("hits", []):
        items.append(article(
            "hackernews",
            h.get("title"),
            h.get("url") or f"https://news.ycombinator.com/item?id={h.get('objectID')}",
            score=h.get("points"),
            timestamp=h.get("created_at_i"),
            extra=f"comments: {h.get('num_comments')}",
        ))
    items.sort(key=lambda x: x["score"] or 0, reverse=True)
    return items[:limit]


if __name__ == "__main__":
    print(save_raw("hackernews", fetch()))
