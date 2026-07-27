"""InfoQ Japan の RSS フィードから記事を取得。
リダイレクト対応 (urllib.request が自動追従)。
"""
import email.utils
import html
import re
import xml.etree.ElementTree as ET
from datetime import datetime, timezone, timedelta
from urllib.error import HTTPError

from common import http_get, article, save_raw

FEED_URL = "https://www.infoq.com/jp/feed/"
# dc:creator 名前空間
DC_NS = "http://purl.org/dc/elements/1.1/"


def _strip_and_decode(text):
    if not text:
        return None
    s = re.sub(r"<[^>]+>", "", text)
    s = html.unescape(s)
    return s.strip()


def fetch(limit=15):
    try:
        raw = http_get(FEED_URL).decode("utf-8", "replace")
    except HTTPError:
        return []

    root = ET.fromstring(raw)
    now = datetime.now(timezone.utc)
    cutoff = now - timedelta(days=14)
    items = []

    for it in root.iter("item"):
        title_el = it.find("title")
        link_el = it.find("link")
        desc_el = it.find("description")
        pub_el = it.find("pubDate")
        creator_el = it.find(f"{{{DC_NS}}}creator")

        title = title_el.text if title_el is not None else None
        url = link_el.text if link_el is not None else None
        pub_date = pub_el.text if pub_el is not None else None

        if not title or not url or not pub_date:
            continue

        # RFC 2822 → UNIX timestamp
        try:
            dt = email.utils.parsedate_to_datetime(pub_date)
        except Exception:
            continue

        # 過去 14 日以内のフィルタ
        if dt < cutoff:
            continue

        timestamp = dt.timestamp()

        # description の処理
        raw_desc = desc_el.text if desc_el is not None else None
        description = _strip_and_decode(raw_desc)

        # dc:creator → extra
        creator_raw = creator_el.text if creator_el is not None else None
        extra = None
        if creator_raw:
            creator = creator_raw.strip()
            if creator:
                extra = f"author: {creator}"

        items.append(article(
            "infoq_jp",
            title,
            url,
            timestamp=timestamp,
            extra=extra,
            score=None,
        ))

        if len(items) >= limit:
            break

    return items


if __name__ == "__main__":
    print(save_raw("infoq_jp", fetch()))
