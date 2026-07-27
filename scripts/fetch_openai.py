"""OpenAI 公式ニュースを RSS 2.0 から取得。"""
import email.utils
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone

from common import http_get, article, save_raw

FEED_URL = "https://openai.com/news/rss.xml"


def _parse_timestamp(pub_date):
    """RFC 2822 → UNIX 秒。パース不能なら None。"""
    if not pub_date:
        return None
    try:
        dt = email.utils.parsedate_to_datetime(pub_date)
        return dt.timestamp()
    except Exception:
        return None


def _recent_enough(timestamp, days=7):
    """タイムスタンプが指定日数以内か。None（日付不明）なら通す。"""
    if timestamp is None:
        return True
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    return timestamp >= cutoff.timestamp()


def fetch(limit=20):
    raw = http_get(FEED_URL).decode("utf-8", "replace")
    root = ET.fromstring(raw)
    items = []

    for it in root.iter("item"):
        title = it.findtext("title")
        link = it.findtext("link")
        pub_date = it.findtext("pubDate")

        # 最初の <category> テキストを利用
        cat_el = it.find("category")
        cat = cat_el.text.strip() if cat_el is not None and cat_el.text else None

        ts = _parse_timestamp(pub_date)

        if not _recent_enough(ts):
            continue

        extra = f"category: {cat}" if cat else None

        items.append(article(
            "openai",
            title,
            link,
            score=None,
            timestamp=ts,
            extra=extra,
        ))

        if len(items) >= limit:
            break

    return items


if __name__ == "__main__":
    print(save_raw("openai", fetch()))
