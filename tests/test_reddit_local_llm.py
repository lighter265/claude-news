import json
import sqlite3
import sys
import unittest
import urllib.error
from datetime import datetime, timedelta, timezone
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch


REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))

import fetch_reddit_local_llm as reddit  # noqa: E402
import register_seen  # noqa: E402


class RedditFetchTest(unittest.TestCase):
    def test_fetch_filters_by_post_time_and_keeps_safe_plaintext(self):
        now = datetime(2026, 8, 9, 12, 0, tzinfo=timezone.utc)
        boundary = (now - timedelta(hours=36)).isoformat().replace("+00:00", "Z")
        recent = (now - timedelta(hours=1)).isoformat().replace("+00:00", "Z")
        old = (now - timedelta(hours=36, seconds=1)).isoformat().replace("+00:00", "Z")
        future = (now + timedelta(minutes=1)).isoformat().replace("+00:00", "Z")
        long_body = "<p>safe <strong>body</strong></p><script>do_not_keep()</script> " + "x" * 600
        rss = f"""<?xml version="1.0" encoding="UTF-8"?>
        <feed xmlns="http://www.w3.org/2005/Atom">
          <entry>
            <title>Recent &amp; useful</title>
            <published>{recent}</published>
            <link href="https://www.reddit.com/r/LocalLLaMA/comments/recent/post/" />
            <content type="html">{long_body.replace('<', '&lt;').replace('>', '&gt;')}</content>
          </entry>
          <entry>
            <title>Boundary</title>
            <published>{boundary}</published>
            <link href="https://www.reddit.com/r/LocalLLaMA/comments/boundary/post/" />
            <summary>summary &lt;em&gt;text&lt;/em&gt;</summary>
          </entry>
          <entry>
            <title>Old</title><published>{old}</published>
            <link href="https://www.reddit.com/r/LocalLLaMA/comments/old/post/" />
          </entry>
          <entry>
            <title>Future</title><published>{future}</published>
            <link href="https://www.reddit.com/r/LocalLLaMA/comments/future/post/" />
          </entry>
        </feed>""".encode()

        with patch.object(reddit, "http_get", return_value=rss):
            items = reddit.fetch(now=now)

        self.assertEqual([item["title"] for item in items], ["Recent & useful", "Boundary"])
        self.assertEqual(items[0]["source"], "reddit_local_llm")
        self.assertEqual(items[0]["url"], "https://www.reddit.com/r/LocalLLaMA/comments/recent/post/")
        self.assertNotIn("<strong>", items[0]["extra"])
        self.assertNotIn("do_not_keep", items[0]["extra"])
        self.assertLessEqual(len(items[0]["extra"]), reddit.DESCRIPTION_MAX_CHARS + 1)
        self.assertEqual(items[0]["published_at"], recent.replace("Z", "+00:00"))
        self.assertIn("summary text", items[1]["extra"])

    def test_fetch_uses_rss_limit_constant_in_url(self):
        with patch.object(reddit, "http_get", return_value=b"<feed />") as mocked:
            reddit.fetch(now=datetime.now(timezone.utc))
        self.assertEqual(mocked.call_args.args[0], reddit.FEED_URL)
        self.assertIn(f"limit={reddit.REDDIT_RSS_LIMIT}", reddit.FEED_URL)

    def test_retries_429_using_retry_after_and_explicit_user_agent(self):
        rss = b"<feed xmlns=\"http://www.w3.org/2005/Atom\" />"
        rate_limited = urllib.error.HTTPError(
            reddit.FEED_URL, 429, "Too Many Requests", {"Retry-After": "3"}, None
        )
        with patch.object(reddit, "http_get", side_effect=[rate_limited, rss]) as mocked, \
             patch.object(reddit.time, "sleep") as mocked_sleep:
            items = reddit.fetch(now=datetime.now(timezone.utc))

        self.assertEqual(items, [])
        self.assertEqual(mocked.call_count, 2)
        self.assertEqual(mocked.call_args_list[0].kwargs["headers"], {
            "User-Agent": reddit.REDDIT_USER_AGENT,
        })
        mocked_sleep.assert_called_once_with(3.0)

    def test_retries_5xx_with_exponential_backoff_without_real_rss(self):
        rss = b"<feed xmlns=\"http://www.w3.org/2005/Atom\" />"
        server_error = urllib.error.HTTPError(
            reddit.FEED_URL, 503, "Service Unavailable", {}, None
        )
        with patch.object(reddit, "http_get", side_effect=[server_error, server_error, rss]), \
             patch.object(reddit.time, "sleep") as mocked_sleep:
            reddit.fetch(now=datetime.now(timezone.utc))

        self.assertEqual(
            mocked_sleep.call_args_list,
            [unittest.mock.call(1.0), unittest.mock.call(2.0)],
        )


class RegisterSeenTest(unittest.TestCase):
    def test_registers_urls_from_local_llm_feed_too(self):
        with TemporaryDirectory() as temp:
            root = Path(temp)
            raw_dir = root / "raw"
            raw_dir.mkdir()
            reddit_url = "https://www.reddit.com/r/LocalLLaMA/comments/example/post/"
            (raw_dir / "reddit_local_llm.json").write_text(json.dumps([{
                "source": "reddit_local_llm",
                "url": reddit_url,
                "score": None,
                "extra": "post body",
            }]), encoding="utf-8")
            feed_path = root / "feed.md"
            feed_path.write_text("# feed\n\nhttps://example.com/news\n", encoding="utf-8")
            local_feed_path = root / "feed-local-llm.md"
            local_feed_path.write_text(f"# llm\n\n{reddit_url}\n", encoding="utf-8")
            db_path = root / "seen_urls.db"

            with patch.object(register_seen, "DB_PATH", str(db_path)), \
                 patch.object(register_seen, "RAW_DIR", str(raw_dir)), \
                 patch.object(register_seen, "FEED_PATH", str(feed_path)), \
                 patch.object(register_seen, "FEED_LLM_PATH", str(local_feed_path)), \
                 patch.object(register_seen, "FEED_PATHS", (str(feed_path), str(local_feed_path))):
                register_seen.main()

            conn = sqlite3.connect(db_path)
            urls = {row[0] for row in conn.execute("SELECT url FROM seen_urls")}
            conn.close()
            self.assertEqual(urls, {"https://example.com/news", reddit_url})


if __name__ == "__main__":
    unittest.main()
