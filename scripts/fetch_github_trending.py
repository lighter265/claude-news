"""GitHub Trending を mshibanami/GitHubTrendingRSS の RSS から取得。

XML パーサは標準の ElementTree を使う(awk/sed のような手作業パース不要)。
RSS 2.0 / Atom の両形式に対応。
"""
import html
import re
import xml.etree.ElementTree as ET

from common import http_get, article, save_raw

FEED_URL = "https://mshibanami.github.io/GitHubTrendingRSS/daily/all.xml"
ATOM = "{http://www.w3.org/2005/Atom}"


def _strip_html(s):
    s = re.sub(r"<[^>]+>", " ", s or "")
    return html.unescape(re.sub(r"\s+", " ", s)).strip()


def fetch(limit=25):
    raw = http_get(FEED_URL).decode("utf-8", "replace")
    root = ET.fromstring(raw)
    items = []

    # RSS 2.0: <channel><item>
    for it in root.iter("item"):
        items.append(article(
            "github_trending",
            it.findtext("title"),
            it.findtext("link"),
            extra=_strip_html(it.findtext("description"))[:500],
        ))

    # Atom fallback: <entry>
    if not items:
        for e in root.iter(ATOM + "entry"):
            link_el = e.find(ATOM + "link")
            items.append(article(
                "github_trending",
                e.findtext(ATOM + "title"),
                link_el.get("href") if link_el is not None else None,
                extra=_strip_html(e.findtext(ATOM + "content"))[:500],
            ))

    return items[:limit]


if __name__ == "__main__":
    print(save_raw("github_trending", fetch()))
