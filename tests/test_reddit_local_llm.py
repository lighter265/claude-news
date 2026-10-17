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
        boundary = (now - timedelta(hours=48)).isoformat().replace("+00:00", "Z")
        recent = (now - timedelta(hours=1)).isoformat().replace("+00:00", "Z")
        old = (now - timedelta(hours=48, seconds=1)).isoformat().replace("+00:00", "Z")
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

    def test_fetch_paginates_with_after_until_cutoff(self):
        now = datetime(2026, 8, 9, 12, 0, tzinfo=timezone.utc)

        def feed(*entries):
            body = "".join(
                f"<entry><id>t3_{n}</id><title>{n}</title>"
                f"<published>{(now - timedelta(hours=h)).isoformat()}</published>"
                f"<link href=\"https://www.reddit.com/r/LocalLLaMA/comments/{n}/x/\" /></entry>"
                for n, h in entries
            )
            return f'<feed xmlns="http://www.w3.org/2005/Atom">{body}</feed>'.encode()

        pages = [feed(("a", 1), ("b", 30)), feed(("c", 47), ("d", 49))]
        with patch.object(reddit, "http_get", side_effect=pages) as mocked, \
             patch.object(reddit.time, "sleep"):
            items = reddit.fetch(now=now)

        self.assertEqual([i["title"] for i in items], ["a", "b", "c"])
        self.assertEqual(mocked.call_count, 2)
        self.assertTrue(mocked.call_args_list[1].args[0].endswith("&after=t3_b"))

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

    def test_retries_5xx_with_fallback_delay_without_real_rss(self):
        rss = b"<feed xmlns=\"http://www.w3.org/2005/Atom\" />"
        server_error = urllib.error.HTTPError(
            reddit.FEED_URL, 503, "Service Unavailable", {}, None
        )
        with patch.object(reddit, "http_get", side_effect=[server_error, server_error, rss]), \
             patch.object(reddit.time, "sleep") as mocked_sleep:
            reddit.fetch(now=datetime.now(timezone.utc))

        # ヘッダなしなら30秒固定フォールバック。
        self.assertEqual(
            mocked_sleep.call_args_list,
            [unittest.mock.call(30.0), unittest.mock.call(30.0)],
        )

    def test_skips_retry_when_cumulative_wait_would_exceed_100s(self):
        # Retry-Afterが100秒超 → 待たずに即スキップ（例外が伝播）。
        huge_wait = urllib.error.HTTPError(
            reddit.FEED_URL, 429, "Too Many Requests",
            {"Retry-After": "120"}, None
        )
        with patch.object(reddit, "http_get", side_effect=huge_wait) as mocked, \
             patch.object(reddit.time, "sleep") as mocked_sleep:
            with self.assertRaises(urllib.error.HTTPError):
                reddit.fetch(now=datetime.now(timezone.utc))

        self.assertEqual(mocked.call_count, 1)
        mocked_sleep.assert_not_called()

    def test_retries_until_cumulative_budget_is_exhausted(self):
        # 1回目30s（ヘッダなし）＋2回目Retry-After 60s = 累計90sまで待つ。
        # 3回目はさらに30s必要で累計120s → 100s超なのでスキップして例外。
        limited = urllib.error.HTTPError(
            reddit.FEED_URL, 429, "Too Many Requests", {}, None
        )
        limited_again = urllib.error.HTTPError(
            reddit.FEED_URL, 429, "Too Many Requests", {"Retry-After": "60"}, None
        )
        with patch.object(reddit, "http_get", side_effect=[limited, limited_again, limited]), \
             patch.object(reddit.time, "sleep") as mocked_sleep:
            with self.assertRaises(urllib.error.HTTPError):
                reddit.fetch(now=datetime.now(timezone.utc))

        self.assertEqual(
            mocked_sleep.call_args_list,
            [unittest.mock.call(30.0), unittest.mock.call(60.0)],
        )

    def test_uses_x_ratelimit_reset_as_middle_fallback(self):
        # Retry-After が無ければ x-ratelimit-reset を使い、それも無ければ30秒。
        rss = b"<feed xmlns=\"http://www.w3.org/2005/Atom\" />"
        rate_limited = urllib.error.HTTPError(
            reddit.FEED_URL, 429, "Too Many Requests",
            {"X-RateLimit-Reset": "7"}, None
        )
        with patch.object(reddit, "http_get", side_effect=[rate_limited, rss]), \
             patch.object(reddit.time, "sleep") as mocked_sleep:
            reddit.fetch(now=datetime.now(timezone.utc))

        mocked_sleep.assert_called_once_with(7.0)


class FilterSeenTest(unittest.TestCase):
    def test_reddit_items_are_annotated_not_dropped(self):
        import filter_seen
        with TemporaryDirectory() as temp:
            root = Path(temp)
            raw_dir = root / "raw"
            raw_dir.mkdir()
            old, new = "https://r/old", "https://r/new"
            (raw_dir / "reddit_local_llm.json").write_text(json.dumps([
                {"source": "reddit_local_llm", "url": old},
                {"source": "reddit_local_llm", "url": new},
            ]), encoding="utf-8")
            db = root / "seen.db"
            conn = sqlite3.connect(db)
            filter_seen.init_db(conn)
            conn.execute("INSERT INTO seen_urls (url, first_seen) VALUES (?, date('now','-1 day'))", (old,))
            conn.commit()
            conn.close()
            with patch.object(filter_seen, "DB_PATH", str(db)), \
                 patch.object(filter_seen, "RAW_DIR", str(raw_dir)):
                filter_seen.main()
            items = json.loads((raw_dir / "reddit_local_llm.json").read_text(encoding="utf-8"))
        self.assertEqual({i["url"]: i["seen_before"] for i in items}, {old: True, new: False})


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
