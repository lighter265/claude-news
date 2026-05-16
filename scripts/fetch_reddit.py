"""Reddit を公式 JSON API から取得。

User-Agent ヘッダ必須。レート制限対策で subreddit 間に 2 秒 sleep。
API が不安定なため、1 つの subreddit が失敗しても残りは続行する。
"""
import time

from common import http_get_json, article, save_raw

SUBS = ["programming", "MachineLearning"]


def fetch(limit_per_sub=15):
    items = []
    for i, sub in enumerate(SUBS):
        if i > 0:
            time.sleep(2)
        try:
            url = f"https://www.reddit.com/r/{sub}/top.json?t=day&limit={limit_per_sub}"
            data = http_get_json(url)
            for c in data.get("data", {}).get("children", []):
                d = c.get("data", {})
                created = d.get("created_utc")
                items.append(article(
                    "reddit",
                    d.get("title"),
                    d.get("url") or ("https://www.reddit.com" + d.get("permalink", "")),
                    score=d.get("score"),
                    timestamp=int(created) if created else None,
                    extra=f"r/{sub}, comments: {d.get('num_comments')}",
                ))
        except Exception as e:
            print(f"  reddit r/{sub} failed: {e}")
    return items


if __name__ == "__main__":
    print(save_raw("reddit", fetch()))
