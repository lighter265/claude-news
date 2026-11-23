"""donsetch の実測レスポンス（fixture）を使った Reddit 取得のテスト。"""
import json
import sys
import unittest
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import patch


REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))

import fetch_reddit_local_llm as reddit  # noqa: E402

FIXTURES = REPO / "tests" / "fixtures"
NOW = datetime(2026, 11, 23, 7, 0, tzinfo=timezone.utc)


def load_fixture(name):
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


class ParseListTest(unittest.TestCase):
    def test_parses_permalinks_score_and_comments(self):
        content = load_fixture("reddit_list.json")["content"]
        items = reddit._parse_list(content)
        self.assertGreater(len(items), 0)
        first = items[0]
        self.assertTrue(first["url"].startswith("https://www.reddit.com/r/LocalLLaMA/comments/1"))
        self.assertIsInstance(first["score"], int)
        self.assertIsInstance(first["num_comments"], int)
        self.assertTrue(first["title"])

    def test_since_last_header_is_stripped(self):
        content = "*[changed since last fetch (minor, 44s ago) : since_last=true returns just the delta]*\n\n" \
                  + load_fixture("reddit_list.json")["content"]
        items = reddit._parse_list(content)
        self.assertGreater(len(items), 0)


class ParseThreadTest(unittest.TestCase):
    def test_extracts_body_score_and_relative_time(self):
        envelope = load_fixture("reddit_threads.json")
        entry = next(r for r in envelope["results"] if r["ok"])
        parsed = reddit._parse_thread(entry["content"], entry["url"])
        self.assertIsNotNone(parsed)
        self.assertTrue(parsed["extra"])
        self.assertNotIn("\n---\n", parsed["extra"])
        self.assertLessEqual(len(parsed["extra"]), reddit.DESCRIPTION_MAX_CHARS + 1)
        self.assertRegex(parsed["relative"], r"^\d+\s*[smhd]$")

    def test_relative_time_to_timestamp(self):
        self.assertEqual(
            reddit._relative_to_timestamp("3h", NOW),
            int((NOW.timestamp() - 3 * 3600)),
        )
        self.assertIsNone(reddit._relative_to_timestamp("", NOW))


class PacingTest(unittest.TestCase):
    def test_fetches_one_at_a_time_with_interval(self):
        items = [
            {"url": f"https://www.reddit.com/r/LocalLLaMA/comments/1y{a:05d}/post/"}
            for a in range(3)
        ]
        envelope = {"results": []}
        with patch.object(reddit, "_run_donsetch", return_value=envelope) as mock_run, \
             patch.object(reddit.time, "sleep") as mock_sleep:
            reddit._fetch_threads(items)
        self.assertEqual(mock_run.call_count, 3)
        self.assertEqual(mock_sleep.call_count, 2)
        mock_sleep.assert_called_with(reddit.FETCH_INTERVAL_SECONDS)

    def test_limit_is_40(self):
        self.assertIn("limit=40", reddit.LIST_URL)


class FetchTest(unittest.TestCase):
    def test_fetch_maps_list_and_threads_into_legacy_schema(self):
        listing = load_fixture("reddit_list.json")
        threads = load_fixture("reddit_threads.json")
        with patch.object(reddit, "_fetch_list", return_value=reddit._parse_list(listing["content"])), \
             patch.object(reddit, "_fetch_threads") as mock_threads:
            thread_map = {}
            for entry in threads["results"]:
                parsed = reddit._parse_thread(entry["content"], entry["url"])
                if parsed:
                    thread_map[entry["url"]] = parsed
            mock_threads.return_value = thread_map
            items = reddit.fetch(now=NOW)

        self.assertGreater(len(items), 0)
        first = items[0]
        for key in ("source", "title", "url", "score", "timestamp", "extra"):
            self.assertIn(key, first)
        self.assertEqual(first["source"], "reddit_local_llm")
        self.assertTrue(any("comments:" in (i["extra"] or "") for i in items))
        self.assertTrue(any("published_at" in i for i in items))

    def test_fetch_propagates_list_failure(self):
        with patch.object(reddit, "_fetch_list", side_effect=RuntimeError("donsetch down")):
            with self.assertRaises(RuntimeError):
                reddit.fetch(now=NOW)


if __name__ == "__main__":
    unittest.main()
