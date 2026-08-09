"""Reddit r/LocalLLaMA の Atom RSS から最近の投稿を取得する。

Reddit のRSSは認証不要で利用できるため、APIキーやログイン状態には依存しない。
取得対象は日次実行の取りこぼしを吸収できるよう、投稿日時が直近36時間以内のものを
RSSのlimit件数内で全件とする。
"""
import html
import re
import time
import urllib.error
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from html.parser import HTMLParser

from common import http_get, article, save_raw


REDDIT_RSS_BASE_URL = "https://www.reddit.com/r/LocalLLaMA/new/.rss"
REDDIT_RSS_LIMIT = 100
RECENT_WINDOW_HOURS = 36
DESCRIPTION_MAX_CHARS = 500
REDDIT_USER_AGENT = "claude-news/1.0 (personal news digest; contact unavailable)"
RETRY_COUNT = 2  # 初回を含めて最大3試行。日次処理を長時間待たせない。
RETRY_BACKOFF_SECONDS = 1.0
MAX_RETRY_DELAY_SECONDS = 30.0
FEED_URL = f"{REDDIT_RSS_BASE_URL}?limit={REDDIT_RSS_LIMIT}"


class _PlainTextParser(HTMLParser):
    """HTMLをテキストへ変換する最小限の安全なパーサ。"""

    BLOCK_TAGS = {
        "address", "article", "aside", "blockquote", "br", "div", "dl",
        "fieldset", "figcaption", "figure", "footer", "form", "h1", "h2",
        "h3", "h4", "h5", "h6", "header", "hr", "li", "main", "nav",
        "ol", "p", "pre", "section", "table", "tr", "ul",
    }

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self._ignored_depth = 0

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        if tag in ("script", "style", "template"):
            self._ignored_depth += 1
        elif self._ignored_depth == 0 and tag in self.BLOCK_TAGS:
            self.parts.append("\n")

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag in ("script", "style", "template") and self._ignored_depth:
            self._ignored_depth -= 1
        elif self._ignored_depth == 0 and tag in self.BLOCK_TAGS:
            self.parts.append("\n")

    def handle_data(self, data):
        if self._ignored_depth == 0:
            self.parts.append(data)

    def text(self):
        return "".join(self.parts)


def _strip_html(value):
    """HTML/Atom本文をプレーンテキスト化し、空白を整える。"""
    if not value:
        return ""
    parser = _PlainTextParser()
    parser.feed(html.unescape(value))
    parser.close()
    lines = [re.sub(r"[ \t\f\v]+", " ", line).strip()
             for line in parser.text().replace("\r\n", "\n").replace("\r", "\n").split("\n")]
    lines = [line for line in lines if line]
    return "\n".join(lines).strip()


def _parse_datetime(value):
    if not value:
        return None
    value = value.strip()
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(timezone.utc)
    except ValueError:
        try:
            parsed = parsedate_to_datetime(value)
        except (TypeError, ValueError, OverflowError):
            return None
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        return parsed.astimezone(timezone.utc)


def _child_text(element, name):
    """名前空間の有無によらず、entry直下の要素本文を返す。"""
    for child in list(element):
        if child.tag.rsplit("}", 1)[-1] == name:
            return "".join(child.itertext()).strip()
    return ""


def _entry_url(entry):
    for child in list(entry):
        if child.tag.rsplit("}", 1)[-1] != "link":
            continue
        href = child.get("href")
        if href:
            return href.strip()
        if child.text:
            return child.text.strip()
    return ""


def _retry_after_seconds(error):
    """Retry-Afterを秒数またはHTTP日付として解釈する。"""
    value = error.headers.get("Retry-After") if error.headers else None
    if not value:
        return None
    value = value.strip()
    try:
        return max(0.0, float(value))
    except ValueError:
        try:
            retry_at = parsedate_to_datetime(value)
        except (TypeError, ValueError, OverflowError):
            return None
        if retry_at.tzinfo is None:
            retry_at = retry_at.replace(tzinfo=timezone.utc)
        return max(0.0, (retry_at - datetime.now(timezone.utc)).total_seconds())


def _http_get_with_retry(url, sleep=None):
    """Redditのレート制限/一時障害だけを少回数リトライして取得する。"""
    sleep = sleep or time.sleep
    headers = {"User-Agent": REDDIT_USER_AGENT}
    for attempt in range(RETRY_COUNT + 1):
        try:
            return http_get(url, headers=headers)
        except urllib.error.HTTPError as error:
            retryable = error.code == 429 or 500 <= error.code <= 599
            if not retryable or attempt >= RETRY_COUNT:
                raise

            delay = _retry_after_seconds(error)
            if delay is None:
                delay = RETRY_BACKOFF_SECONDS * (2 ** attempt)
            delay = min(delay, MAX_RETRY_DELAY_SECONDS)
            print(
                f"[reddit] HTTP {error.code}; retry "
                f"{attempt + 1}/{RETRY_COUNT} in {delay:g}s"
            )
            sleep(delay)


def fetch(limit=REDDIT_RSS_LIMIT, recent_hours=RECENT_WINDOW_HOURS, now=None):
    """RSSから直近 ``recent_hours`` 時間の投稿を全件返す。

    ``now`` はテストで基準時刻を固定するための引数。通常は現在時刻を使う。
    """
    raw = _http_get_with_retry(FEED_URL).decode("utf-8", "replace")
    root = ET.fromstring(raw)
    now = now or datetime.now(timezone.utc)
    if now.tzinfo is None:
        now = now.replace(tzinfo=timezone.utc)
    now = now.astimezone(timezone.utc)
    cutoff = now - timedelta(hours=recent_hours)

    items = []
    seen_urls = set()
    for entry in root.iter():
        if entry.tag.rsplit("}", 1)[-1] != "entry":
            continue

        published_text = _child_text(entry, "published") or _child_text(entry, "updated")
        published = _parse_datetime(published_text)
        if published is None or published < cutoff or published > now:
            continue

        url = _entry_url(entry)
        if not url or url in seen_urls:
            continue

        # Reddit Atom は通常 content、フィードによっては summary/description。
        body = (_child_text(entry, "content") or _child_text(entry, "summary")
                or _child_text(entry, "description"))
        body = _strip_html(body)
        if len(body) > DESCRIPTION_MAX_CHARS:
            body = body[:DESCRIPTION_MAX_CHARS].rstrip() + "…"

        item = article(
            "reddit_local_llm",
            _child_text(entry, "title"),
            url,
            timestamp=int(published.timestamp()),
            extra=body,
        )
        # timestampは既存スキーマ互換のUNIX秒。ISO形式も保持して可読性を確保する。
        item["published_at"] = published.isoformat()
        items.append(item)
        seen_urls.add(url)

    # RSSの並び順に依存せず、日付の新しい順で安定させる。
    items.sort(key=lambda item: item["timestamp"] or 0, reverse=True)
    return items[:limit]


if __name__ == "__main__":
    print(save_raw("reddit_local_llm", fetch()))
