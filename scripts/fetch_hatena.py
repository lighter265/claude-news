"""はてなブックマーク - 人気エントリー - テクノロジー を RSS 1.0 (RDF) から取得。

xml.etree.ElementTree で名前空間を Clark 記法 ({uri}localname) で扱う。
Hatena 独自拡張 <hatena:bookmarkcount> を含む。
"""
import html
import re
import xml.etree.ElementTree as ET
from datetime import datetime

from common import http_get, article, save_raw

FEED_URL = "https://b.hatena.ne.jp/hotentry/it.rss"

NS_RSS = "{http://purl.org/rss/1.0/}"
NS_DC = "{http://purl.org/dc/elements/1.1/}"
NS_HATENA = "{http://www.hatena.ne.jp/info/xmlns#}"


def fetch(limit=20):
    raw = http_get(FEED_URL).decode("utf-8", "replace")
    root = ET.fromstring(raw)
    items = []

    for it in root.iter(NS_RSS + "item"):
        # title
        title_el = it.find(NS_RSS + "title")
        title = html.unescape(title_el.text or "") if title_el is not None else ""

        # link
        link_el = it.find(NS_RSS + "link")
        url = (link_el.text or "").strip() if link_el is not None else ""

        # description (HTML タグ除去 ＋ エンティティデコード)
        desc_el = it.find(NS_RSS + "description")
        if desc_el is not None and desc_el.text:
            desc = html.unescape(desc_el.text)
            desc = re.sub(r"<[^>]+>", "", desc)
        else:
            desc = ""

        # dc:date → ISO 8601 → UNIX 秒
        date_el = it.find(NS_DC + "date")
        timestamp = None
        if date_el is not None and date_el.text:
            try:
                # Python 3.7+ の fromisoformat は "Z" 非対応なので置換
                dt = datetime.fromisoformat(date_el.text.replace("Z", "+00:00"))
                timestamp = int(dt.timestamp())
            except (ValueError, TypeError):
                pass

        # hatena:bookmarkcount
        bm_el = it.find(NS_HATENA + "bookmarkcount")
        score = int(bm_el.text) if bm_el is not None and bm_el.text else 0

        # dc:subject (タグ) は複数存在するので全て収集
        tags = []
        for subj in it.iter(NS_DC + "subject"):
            if subj.text:
                tags.append(subj.text.strip())
        extra = f"tags: {', '.join(tags)}" if tags else None

        items.append(article(
            "hatena",
            title,
            url,
            score=score,
            timestamp=timestamp,
            extra=extra,
        ))

    items.sort(key=lambda x: x["score"] or 0, reverse=True)
    return items[:limit]


if __name__ == "__main__":
    print(save_raw("hatena", fetch()))
