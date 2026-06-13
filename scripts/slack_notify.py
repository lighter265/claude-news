#!/usr/bin/env python3
"""feed.md の要約をSlackに投稿する。SLACK_WEBHOOK_URL 環境変数が必要。"""
import os
import re
import json
import sys
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
FEED_MD = REPO / "feed.md"

# GitHub Pages用URL (要設定)
PAGES_URL = os.environ.get(
    "CLAUDE_NEWS_URL",
    "https://lighter265.github.io/claude-news/"
)


def parse_sections(md_text: str) -> list[dict]:
    """セクションとそのアイテム数を抽出"""
    sections = []
    for m in re.finditer(r"^## (.+)", md_text, re.MULTILINE):
        sections.append({"name": m.group(1).strip(), "count": 0})

    # 各セクションの記事数カウント
    for i, sec in enumerate(sections):
        start = md_text.find(f"## {sec['name']}")
        end = len(md_text)
        if i + 1 < len(sections):
            end = md_text.find(f"## {sections[i+1]['name']}")
        # テーブル行 (| 1 | ...) をカウント
        sec["count"] = len(re.findall(r"^\| \d+ \|", md_text[start:end], re.MULTILINE))

    return sections


def send_slack(blocks: list[dict]) -> bool:
    webhook_url = os.environ.get("SLACK_WEBHOOK_URL", "")
    if not webhook_url:
        print("SLACK_WEBHOOK_URL not set, skipping Slack notification", file=sys.stderr)
        return False

    payload = json.dumps({"blocks": blocks}).encode("utf-8")
    req = urllib.request.Request(
        webhook_url,
        data=payload,
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            body = resp.read().decode()
            print(f"Slack response: {body}")
            return resp.status == 200
    except Exception as e:
        print(f"Slack webhook failed: {e}", file=sys.stderr)
        return False


def main():
    if not FEED_MD.exists():
        print(f"feed.md not found at {FEED_MD}", file=sys.stderr)
        sys.exit(1)

    md_text = FEED_MD.read_text(encoding="utf-8")
    date_match = re.search(r"(\d{4}-\d{2}-\d{2})", md_text)
    date_str = date_match.group(1) if date_match else ""

    sections = parse_sections(md_text)
    total_items = sum(s["count"] for s in sections)
    section_lines = [f"• *{s['name']}*: {s['count']}件" for s in sections if s["count"] > 0]

    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f"📰 技術ニュース要約 — {date_str}",
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    f"今朝の技術ニュース（全{total_items}件）をお届けします 🐝\n"
                    + "\n".join(section_lines)
                ),
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"👉 <{PAGES_URL}|全文を開く>",
            }
        },
        {"type": "divider"},
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": f"🤖 claude-news · {date_str} · 自動投稿",
                }
            ],
        },
    ]

    send_slack(blocks)


if __name__ == "__main__":
    main()
