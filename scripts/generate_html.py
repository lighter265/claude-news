#!/usr/bin/env python3
"""feed.md をテーブル形式のHTMLに変換 (index.html 出力)"""
import re
import sys
from pathlib import Path
from datetime import datetime

REPO = Path(__file__).resolve().parent.parent
FEED_MD = REPO / "feed.md"


def parse_feed(md_text: str) -> dict:
    """feed.md をパース。テーブル形式と見出し形式の両対応。"""
    sections = {}
    current_section = None
    in_table = False
    lines = md_text.split("\n")

    for line in lines:
        # セクション見出し
        m = re.match(r"^## (.+)", line)
        if m:
            current_section = m.group(1).strip()
            sections[current_section] = []
            in_table = False
            continue

        if current_section is None:
            continue

        # テーブル区切り行
        if re.match(r"^\|[-| ]+\|$", line.strip()):
            in_table = True
            continue
        if re.match(r"^\| #[ |]", line.strip()):
            # ヘッダ行はスキップ
            in_table = True
            continue

        # テーブル行
        if in_table and line.strip().startswith("|"):
            parts = [p.strip() for p in line.strip().split("|")]
            parts = [p for p in parts if p]  # 空要素除去
            if len(parts) >= 3:
                # | # | タイトル | 要約 | URL |
                idx = parts[0] if parts[0] else ""
                title = parts[1] if len(parts) > 1 else ""
                summary = parts[2] if len(parts) > 2 else ""
                url = parts[-1] if parts[-1].startswith("http") else ""
                if not url and len(parts) > 3:
                    url = parts[-1] if parts[-1].startswith("http") else ""
                sections[current_section].append({
                    "title": title,
                    "summary": summary,
                    "url": url,
                })
            continue

        # 非テーブル行が来たらテーブルモード解除
        if line.strip():
            in_table = False

        # 旧形式: ### 見出しベース
        m = re.match(r"^### (.+)", line)
        if m and current_section:
            current_item = {"title": m.group(1).strip(), "summary": [], "url": ""}
            sections[current_section].append(current_item)
            continue

        # URL行
        if "current_item" in locals() and current_item and re.match(r"^https?://", line.strip()):
            current_item["url"] = line.strip()
            continue

        # 要約本文
        if "current_item" in locals() and current_item and line.strip() and not line.strip().startswith("http"):
            current_item["summary"].append(line.strip())

    # 要約テキストを連結（リスト形式の場合）
    for sec_items in sections.values():
        for item in sec_items:
            if isinstance(item.get("summary"), list):
                item["summary"] = " ".join(s for s in item["summary"] if not s.startswith("http"))

    return sections


def escape_html(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def build_html(sections: dict, date_str: str) -> str:
    tables = ""
    for sec_name, items in sections.items():
        if not items:
            continue
        tables += f'<h2 class="section-title">{escape_html(sec_name)}</h2>\n'
        tables += '<table>\n'
        tables += (
            f'<thead>'
            f'<tr><th class="num">#</th>'
            f'<th>タイトル</th>'
            f'<th class="link-col">🔗</th></tr>'
            f'</thead>\n'
        )
        tables += '<tbody>\n'
        for i, item in enumerate(items, 1):
            link_html = ""
            if item.get("url"):
                link_html = (
                    f'<a href="{escape_html(item["url"])}" '
                    f'target="_blank" rel="noopener" title="元記事を開く">↗</a>'
                )
            tables += (
                f"<tr>"
                f'<td class="num">{i}</td>'
                f'<td class="title">{escape_html(item["title"])}</td>'
                f'<td class="link-col">{link_html}</td>'
                f"</tr>\n"
            )
            if item.get("summary"):
                tables += (
                    f'<tr class="summary-row">'
                    f'<td></td>'
                    f'<td colspan="2" class="summary">{escape_html(item["summary"])}</td>'
                    f"</tr>\n"
                )
        tables += '</tbody>\n</table>\n'

    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>技術ニュース要約 — {escape_html(date_str)}</title>
<style>
  *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    background: #f5f5f5; color: #333; line-height: 1.6;
  }}
  .container {{ max-width: 960px; margin: 0 auto; padding: 24px 16px; }}
  h1 {{ font-size: 1.6rem; text-align: center; padding: 24px 0 16px; color: #1a1a2e; }}
  .section-title {{ font-size: 1.1rem; font-weight: 700; color: #1a1a2e; margin: 28px 0 10px 4px; }}
  table {{ width: 100%; border-collapse: collapse; background: #fff; border-radius: 8px; overflow: hidden; box-shadow: 0 1px 4px rgba(0,0,0,.08); margin-bottom: 32px; }}
  thead th {{ background: #1a1a2e; color: #e0e0e0; font-size: .82rem; font-weight: 600; padding: 10px 14px; border-bottom: 2px solid #16213e; }}
  tbody td {{ padding: 10px 14px; vertical-align: top; }}
  .num {{ width: 36px; text-align: center; color: #999; font-size: .82rem; font-weight: 500; }}
  .title {{ font-weight: 600; font-size: .93rem; color: #222; }}
  .link-col {{ width: 44px; text-align: center; }}
  .link-col a {{ text-decoration: none; font-size: 1rem; color: #4a6fa5; }}
  .link-col a:hover {{ color: #2a4f85; }}
  .summary-row td {{ border-bottom: 1px solid #eee; }}
  .summary {{ font-size: .84rem; color: #555; padding: 2px 0 10px; line-height: 1.65; }}
  tbody tr:hover td {{ background: #f8f9fb; }}
  footer {{ text-align: center; padding: 32px 0; font-size: .78rem; color: #999; }}
  footer a {{ color: #666; text-decoration: none; }}
  footer a:hover {{ text-decoration: underline; }}
</style>
</head>
<body>
<div class="container">
<h1>📰 技術ニュース要約 — {escape_html(date_str)}</h1>
{tables}
<footer>
  Generated by <a href="https://github.com/lighter265/claude-news">claude-news</a>
  · {escape_html(datetime.now().strftime("%Y-%m-%d %H:%M JST"))}
</footer>
</div>
</body>
</html>"""


def main():
    if not FEED_MD.exists():
        print(f"feed.md not found at {FEED_MD}", file=sys.stderr)
        sys.exit(1)

    md_text = FEED_MD.read_text(encoding="utf-8")
    sections = parse_feed(md_text)

    date_match = re.search(r"(\d{4}-\d{2}-\d{2})", md_text)
    date_str = date_match.group(1) if date_match else datetime.now().strftime("%Y-%m-%d")

    out_dir = REPO / "docs" / "pages"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / f"{date_str}.html"

    html = build_html(sections, date_str)
    out_file.write_text(html, encoding="utf-8")
    print(f"Generated {out_file} ({len(html)} bytes)")


if __name__ == "__main__":
    main()
