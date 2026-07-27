"""Anthropic ブログ/ニュースを https://www.anthropic.com/news からスクレイピング。

公式 RSS が存在しないため、一覧ページ HTML を html.parser.HTMLParser で解析。
カード構造 (Featured / Grid / PublicationList) に対応。1 リクエストで完結。
"""
import re
import time as time_module
from datetime import datetime
from html.parser import HTMLParser

from common import http_get, article, save_raw

NEWS_URL = "https://www.anthropic.com/news"
DATE_PATTERN = re.compile(
    r"^(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d{1,2}, \d{4}$"
)


class _AnthropicParser(HTMLParser):
    """一覧ページから /news/... の記事リストを抽出。"""

    def __init__(self):
        super().__init__()
        self.result = []
        self._seen = set()  # href 重複排除

        # 現在解析中のカード状態
        self._in_news_link = False
        self._href = None
        self._title = None
        self._category = None
        self._date_str = None
        self._in_title_tag = False  # h2/h4 の内側
        self._in_span = False
        self._in_time = False
        self._skip_attrs = False  # 開始タグの属性読み飛ばし用

    def _reset_card(self):
        self._in_news_link = False
        self._href = None
        self._title = None
        self._category = None
        self._date_str = None
        self._in_title_tag = False
        self._in_span = False
        self._in_time = False

    def _flush_card(self):
        """カード内容を result に追加。最低限 title と日付があれば採用。"""
        if not self._href or not self._title or not self._date_str:
            return
        if self._href in self._seen:
            return
        self._seen.add(self._href)

        try:
            ts = int(
                datetime.strptime(self._date_str, "%b %d, %Y").timestamp()
            )
        except (ValueError, OverflowError):
            ts = None

        extra = f"category: {self._category}" if self._category else None

        self.result.append(article(
            source="anthropic",
            title=self._title,
            url=f"https://www.anthropic.com{self._href}",
            score=None,
            timestamp=ts,
            extra=extra,
        ))

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)

        if tag == "a":
            href = attrs_dict.get("href", "")
            if href.startswith("/news/"):
                self._in_news_link = True
                self._href = href
                # 既に見た href ならスキップフラグ
                if href in self._seen:
                    self._skip_attrs = True
            return

        if not self._in_news_link:
            return

        if tag in ("h2", "h4"):
            self._in_title_tag = True
        elif tag == "span":
            self._in_span = True
        elif tag == "time":
            self._in_time = True

    def handle_endtag(self, tag):
        if tag == "a" and self._in_news_link:
            if not self._skip_attrs:
                self._flush_card()
            self._skip_attrs = False
            self._reset_card()
            return

        if not self._in_news_link:
            return

        if tag in ("h2", "h4"):
            self._in_title_tag = False
        elif tag == "span":
            self._in_span = False
        elif tag == "time":
            self._in_time = False

    def handle_data(self, data):
        if not self._in_news_link or self._skip_attrs:
            return

        stripped = data.strip()
        if not stripped:
            return

        if self._in_title_tag:
            if self._title is None:
                self._title = stripped
        elif self._in_time:
            if self._date_str is None and DATE_PATTERN.match(stripped):
                self._date_str = stripped
        elif self._in_span:
            # span は category か title (PublicationList で title が span)
            if DATE_PATTERN.match(stripped):
                # 日付っぽい文字列は category 候補から除外
                pass
            elif self._category is None:
                # 最初の非日付 span を category に
                self._category = stripped
            elif self._title is None:
                # PublicationList: 2 つめの span は title
                self._title = stripped


def fetch(limit=15):
    """Anthropic ニュース一覧から最大 limit 件の記事を返す。"""
    try:
        raw = http_get(NEWS_URL).decode("utf-8", "replace")
    except Exception:
        return []

    parser = _AnthropicParser()
    parser.feed(raw)

    return parser.result[:limit]


if __name__ == "__main__":
    print(save_raw("anthropic", fetch()))
