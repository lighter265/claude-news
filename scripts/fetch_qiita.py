"""Qiita を公式 API v2 から取得。ストック数 3 超でフィルタ。"""
import json
import subprocess
from datetime import datetime

from common import USER_AGENT, article, save_raw

def _ts(s):
    if not s:
        return None
    try:
        return int(datetime.fromisoformat(s[:19]).timestamp())
    except ValueError:
        return None


def fetch(limit=30):
    url = f"https://qiita.com/api/v2/items?query=stocks:>3&per_page={limit}"
    result = subprocess.run(
        ["curl", "-s", "-H", f"User-Agent: {USER_AGENT}", url],
        capture_output=True, text=True, timeout=30,
    )
    data = json.loads(result.stdout)
    items = []
    for it in data:
        tags = ", ".join(t.get("name", "") for t in it.get("tags", [])[:5])
        items.append(article(
            "qiita",
            it.get("title"),
            it.get("url"),
            score=it.get("likes_count"),
            timestamp=_ts(it.get("created_at")),
            extra=f"tags: {tags}",
        ))
    return items[:limit]


if __name__ == "__main__":
    print(save_raw("qiita", fetch()))
