"""取得スクリプト共通ヘルパ。標準ライブラリのみ。"""
import json
import os
import urllib.request

RAW_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "raw")
USER_AGENT = "claude-news/1.0 (tech news digest bot)"


def http_get(url, headers=None, timeout=30):
    h = {"User-Agent": USER_AGENT}
    if headers:
        h.update(headers)
    req = urllib.request.Request(url, headers=h)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def http_get_json(url, headers=None, timeout=30):
    return json.loads(http_get(url, headers, timeout).decode("utf-8"))


def article(source, title, url, score=None, timestamp=None, extra=None):
    """正規化した記事レコード。score は star/point/like 等、timestamp は UNIX 秒。"""
    return {
        "source": source,
        "title": (title or "").strip(),
        "url": url,
        "score": score,
        "timestamp": timestamp,
        "extra": (extra or "").strip() if extra else None,
    }


def save_raw(name, items):
    os.makedirs(RAW_DIR, exist_ok=True)
    path = os.path.join(RAW_DIR, name + ".json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=2)
    return path
