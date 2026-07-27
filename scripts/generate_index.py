#!/usr/bin/env python3
"""docs/pages/*.html をスキャンして:
  - docs/index.html       トップ (月別カード, 年別グルーピング)
  - docs/YYYY-MM.html     月別ページ (日次一覧 + 前月/翌月ナビ)
  を生成する。
"""
import re
from collections import OrderedDict
from pathlib import Path
from datetime import datetime

REPO = Path(__file__).resolve().parent.parent
PAGES_DIR = REPO / "docs" / "pages"
INDEX_HTML = REPO / "docs" / "index.html"

# 日本語の月名
MONTH_NAMES = {
    1: "1月", 2: "2月", 3: "3月", 4: "4月",
    5: "5月", 6: "6月", 7: "7月", 8: "8月",
    9: "9月", 10: "10月", 11: "11月", 12: "12月",
}


def collect_pages() -> list[dict]:
    """日付htmlファイルを収集し、タイトルを抽出"""
    pages = []
    for f in sorted(PAGES_DIR.glob("*.html")):
        date_str = f.stem  # e.g. "2026-06-13"
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", date_str):
            continue
        try:
            text = f.read_text(encoding="utf-8")
            m = re.search(r"<title>(.+?)</title>", text)
            title = m.group(1) if m else date_str
        except Exception:
            title = date_str
        pages.append({
            "date": date_str,
            "title": title,
            "filename": f.name,
            "year": int(date_str[:4]),
            "month": int(date_str[5:7]),
            "day": int(date_str[8:10]),
        })
    return pages


def group_by_year_month(pages: list[dict]) -> OrderedDict:
    """年・月でグルーピング。降順 (新しい順)。"""
    groups: OrderedDict[str, list[dict]] = OrderedDict()
    for p in sorted(pages, key=lambda x: x["date"], reverse=True):
        key = f'{p["year"]}-{p["month"]:02d}'
        groups.setdefault(key, []).append(p)
    return groups


def escape_html(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


# ---------------------------------------------------------------------------
# トップページ (docs/index.html)
# ---------------------------------------------------------------------------

def build_index_html(groups: OrderedDict, total: int) -> str:
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M JST")
    year_sections = ""
    # 年ごとにまとめる
    years: OrderedDict[int, OrderedDict] = OrderedDict()
    for ym, pages in groups.items():
        year = int(ym[:4])
        month = int(ym[5:7])
        years.setdefault(year, OrderedDict())[ym] = pages

    for year, year_groups in years.items():
        year_count = sum(len(ps) for ps in year_groups.values())
        month_cards = ""
        for ym, pages in year_groups.items():
            month = int(ym[5:7])
            month_label = f"{MONTH_NAMES[month]}"
            count = len(pages)
            # 月カード: 左にネイビーの太いボーダー + カウントバッジ
            month_cards += (
                f'<a href="{ym}.html" class="month-card" aria-label="{year}年{month_label} — {count}件">\n'
                f'  <div class="month-name">{escape_html(month_label)}</div>\n'
                f'  <div class="month-badge">{count}件</div>\n'
                f'</a>\n'
            )
        year_sections += (
            f'<section class="year-section">\n'
            f'  <h2 class="year-heading">{year}年</h2>\n'
            f'  <div class="month-grid">\n'
            f'{month_cards}'
            f'  </div>\n'
            f'</section>\n'
        )

    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>📰 claude-news アーカイブ</title>
<style>
  *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    background: #f5f5f5; color: #333; line-height: 1.6;
  }}
  .container {{ max-width: 720px; margin: 0 auto; padding: 32px 16px; }}
  h1 {{ font-size: 1.5rem; text-align: center; padding: 16px 0 8px; color: #1a1a2e; }}
  .count {{ text-align: center; color: #888; font-size: .88rem; margin-bottom: 32px; }}

  /* 年別セクション */
  .year-section {{ margin-bottom: 36px; }}
  .year-heading {{
    font-size: 1.15rem; font-weight: 700; color: #1a1a2e;
    padding-bottom: 8px; margin-bottom: 16px;
    border-bottom: 2px solid #1a1a2e;
  }}

  /* 月カードグリッド */
  .month-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
    gap: 12px;
  }}
  .month-card {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: #fff;
    border-left: 4px solid #1a1a2e;
    border-radius: 8px;
    padding: 16px 18px;
    text-decoration: none;
    color: inherit;
    box-shadow: 0 1px 4px rgba(0,0,0,.08);
    transition: box-shadow .15s, transform .15s;
  }}
  .month-card:hover {{
    box-shadow: 0 3px 12px rgba(0,0,0,.13);
    transform: translateY(-2px);
  }}
  .month-card:focus-visible {{
    outline: 2px solid #2a4f85;
    outline-offset: 2px;
  }}
  .month-name {{
    font-size: 1.1rem;
    font-weight: 700;
    color: #1a1a2e;
  }}
  .month-badge {{
    background: #1a1a2e;
    color: #e8e8e8;
    font-size: .75rem;
    font-weight: 600;
    padding: 3px 10px;
    border-radius: 12px;
    white-space: nowrap;
  }}

  /* レスポンシブ */
  @media (max-width: 480px) {{
    .container {{ padding: 20px 12px; }}
    h1 {{ font-size: 1.3rem; }}
    .month-grid {{ grid-template-columns: 1fr 1fr; gap: 10px; }}
    .month-card {{ padding: 12px 14px; }}
    .month-name {{ font-size: 1rem; }}
    .month-badge {{ font-size: .7rem; padding: 2px 8px; }}
  }}

  footer {{ text-align: center; padding: 32px 0; font-size: .78rem; color: #999; }}
  footer a {{ color: #666; text-decoration: none; }}
</style>
</head>
<body>
<div class="container">
<h1>📰 claude-news アーカイブ</h1>
<p class="count">{total} 件のニュース要約</p>
{year_sections}
<footer>
  Generated by <a href="https://github.com/lighter265/claude-news">claude-news</a>
  · {now_str}
</footer>
</div>
</body>
</html>"""


# ---------------------------------------------------------------------------
# 月別ページ (docs/YYYY-MM.html)
# ---------------------------------------------------------------------------

def build_month_html(ym: str, pages: list[dict], prev_ym: str | None, next_ym: str | None) -> str:
    year = int(ym[:4])
    month = int(ym[5:7])
    month_label = f"{year}年{MONTH_NAMES[month]}"
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M JST")

    # 日次リンク一覧 (新しい順)
    sorted_pages = sorted(pages, key=lambda p: p["date"], reverse=True)
    daily_rows = ""
    for p in sorted_pages:
        daily_rows += (
            f'<a href="pages/{p["filename"]}" class="daily-row">\n'
            f'  <span class="daily-date">{escape_html(p["date"])}</span>\n'
            f'  <span class="daily-title">{escape_html(p["title"])}</span>\n'
            f'</a>\n'
        )

    # 前月/翌月ボタン
    nav_prev = ""
    if prev_ym:
        pv = int(prev_ym[:4])
        pm = int(prev_ym[5:7])
        nav_prev = f'<a href="{prev_ym}.html" class="nav-btn">← {pv}年{MONTH_NAMES[pm]}</a>'
    else:
        nav_prev = '<span class="nav-btn disabled" aria-disabled="true">← 前月なし</span>'

    nav_next = ""
    if next_ym:
        nv = int(next_ym[:4])
        nm = int(next_ym[5:7])
        nav_next = f'<a href="{next_ym}.html" class="nav-btn">{nv}年{MONTH_NAMES[nm]} →</a>'
    else:
        nav_next = '<span class="nav-btn disabled" aria-disabled="true">翌月なし →</span>'

    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape_html(month_label)} — claude-news アーカイブ</title>
<style>
  *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    background: #f5f5f5; color: #333; line-height: 1.6;
  }}
  .container {{ max-width: 720px; margin: 0 auto; padding: 32px 16px; }}

  /* パンくず */
  .breadcrumb {{ display: flex; flex-wrap: wrap; align-items: center; gap: 6px; margin-bottom: 20px; font-size: .85rem; color: #888; }}
  .breadcrumb a {{ color: #2a4f85; text-decoration: none; }}
  .breadcrumb a:hover {{ text-decoration: underline; }}
  .breadcrumb .sep {{ color: #bbb; }}
  .breadcrumb .current {{ color: #555; font-weight: 500; }}

  h1 {{ font-size: 1.5rem; padding: 0 0 6px; color: #1a1a2e; }}
  .month-count {{ color: #888; font-size: .88rem; margin-bottom: 20px; }}

  /* 前月/翌月ナビ */
  .month-nav {{ display: flex; justify-content: space-between; gap: 12px; margin-bottom: 24px; }}
  .nav-btn {{
    display: inline-block;
    padding: 8px 16px;
    background: #fff;
    border: 1px solid #ddd;
    border-radius: 6px;
    color: #2a4f85;
    text-decoration: none;
    font-size: .88rem;
    font-weight: 500;
    box-shadow: 0 1px 3px rgba(0,0,0,.06);
    transition: background .15s, box-shadow .15s;
  }}
  .nav-btn:hover {{ background: #f0f4fa; box-shadow: 0 2px 6px rgba(0,0,0,.1); }}
  .nav-btn:focus-visible {{ outline: 2px solid #2a4f85; outline-offset: 2px; }}
  .nav-btn.disabled {{
    color: #bbb;
    border-color: #eee;
    background: #fafafa;
    cursor: default;
    pointer-events: none;
  }}

  /* 日次リスト */
  .daily-list {{ display: flex; flex-direction: column; gap: 0; }}
  .daily-row {{
    display: flex;
    align-items: baseline;
    gap: 16px;
    padding: 14px 16px;
    background: #fff;
    border-bottom: 1px solid #eee;
    text-decoration: none;
    color: inherit;
    transition: background .12s;
  }}
  .daily-row:first-child {{ border-radius: 8px 8px 0 0; }}
  .daily-row:last-child {{ border-radius: 0 0 8px 8px; border-bottom: none; }}
  .daily-row:hover {{ background: #f8f9fb; }}
  .daily-row:focus-visible {{ outline: 2px solid #2a4f85; outline-offset: -2px; }}
  .daily-date {{
    flex-shrink: 0;
    width: 110px;
    font-family: "SF Mono", "Cascadia Code", "Consolas", monospace;
    font-size: .88rem;
    color: #999;
  }}
  .daily-title {{
    font-weight: 500;
    font-size: .93rem;
    color: #2a4f85;
  }}
  .daily-row:hover .daily-title {{ text-decoration: underline; }}

  /* レスポンシブ */
  @media (max-width: 480px) {{
    .container {{ padding: 20px 12px; }}
    h1 {{ font-size: 1.3rem; }}
    .month-nav {{ flex-direction: column; gap: 8px; }}
    .nav-btn {{ text-align: center; }}
    .daily-row {{ flex-direction: column; gap: 4px; padding: 12px 14px; }}
    .daily-date {{ width: auto; }}
  }}

  footer {{ text-align: center; padding: 32px 0; font-size: .78rem; color: #999; }}
  footer a {{ color: #666; text-decoration: none; }}
</style>
</head>
<body>
<div class="container">
<nav class="breadcrumb" aria-label="パンくずナビ">
  <a href="index.html">トップ</a>
  <span class="sep" aria-hidden="true">›</span>
  <span class="current" aria-current="page">{escape_html(month_label)}</span>
</nav>
<h1>📰 {escape_html(month_label)} のアーカイブ</h1>
<p class="month-count">{len(pages)} 件のニュース要約</p>
<div class="month-nav">
  {nav_prev}
  {nav_next}
</div>
<div class="daily-list">
{daily_rows}
</div>
<footer>
  Generated by <a href="https://github.com/lighter265/claude-news">claude-news</a>
  · {now_str}
</footer>
</div>
</body>
</html>"""


# ---------------------------------------------------------------------------
# daily ページのパンくず差し込み (既存ファイルを再生成)
# ---------------------------------------------------------------------------

def rebuild_daily_pages(pages: list[dict]) -> int:
    """既存の日次ページを読み、パンくずナビを差し込んで上書き。
    既にパンくずがある場合はスキップ。"""
    rebuilt = 0
    for p in pages:
        fpath = PAGES_DIR / p["filename"]
        if not fpath.exists():
            continue
        text = fpath.read_text(encoding="utf-8")
        if "breadcrumb" in text:
            continue  # 既にパンくずあり

        year = p["year"]
        month = p["month"]
        month_label = f"{year}年{MONTH_NAMES[month]}"
        date_str = p["date"]

        breadcrumb = (
            f'<nav class="breadcrumb" aria-label="パンくずナビ">\n'
            f'  <a href="../index.html">トップ</a>\n'
            f'  <span class="sep" aria-hidden="true">›</span>\n'
            f'  <a href="../{year}-{month:02d}.html">{escape_html(month_label)}</a>\n'
            f'  <span class="sep" aria-hidden="true">›</span>\n'
            f'  <span class="current" aria-current="page">{escape_html(date_str)}</span>\n'
            f'</nav>\n'
        )

        # h1 の直後にパンくずを挿入
        new_text = text.replace(
            f'<h1>📰 技術ニュース要約 — {escape_html(date_str)}</h1>',
            f'<h1>📰 技術ニュース要約 — {escape_html(date_str)}</h1>\n{breadcrumb}',
            1,
        )

        # CSS に breadcrumb スタイルを追加 (既存の closing </style> の前に挿入)
        breadcrumb_css = """
  /* breadcrumb */
  .breadcrumb { display: flex; flex-wrap: wrap; align-items: center; gap: 6px; margin-bottom: 20px; font-size: .85rem; color: #888; }
  .breadcrumb a { color: #2a4f85; text-decoration: none; }
  .breadcrumb a:hover { text-decoration: underline; }
  .breadcrumb .sep { color: #bbb; }
  .breadcrumb .current { color: #555; font-weight: 500; }
"""
        if ".breadcrumb" not in new_text:
            new_text = new_text.replace("</style>", f"{breadcrumb_css}</style>", 1)

        fpath.write_text(new_text, encoding="utf-8")
        rebuilt += 1

    return rebuilt


# ---------------------------------------------------------------------------
# メイン
# ---------------------------------------------------------------------------

def main():
    PAGES_DIR.mkdir(parents=True, exist_ok=True)
    pages = collect_pages()
    if not pages:
        print("No daily pages found in", PAGES_DIR)
        return

    groups = group_by_year_month(pages)
    total = len(pages)

    # 1) トップページ生成
    index_html = build_index_html(groups, total)
    INDEX_HTML.write_text(index_html, encoding="utf-8")
    print(f"Generated {INDEX_HTML} ({total} pages, {len(index_html)} bytes)")

    # 2) 月別ページ生成
    ym_keys = list(groups.keys())
    month_count = 0
    for i, ym in enumerate(ym_keys):
        prev_ym = ym_keys[i + 1] if i + 1 < len(ym_keys) else None
        next_ym = ym_keys[i - 1] if i - 1 >= 0 else None
        month_html = build_month_html(ym, groups[ym], prev_ym, next_ym)
        month_file = REPO / "docs" / f"{ym}.html"
        month_file.write_text(month_html, encoding="utf-8")
        month_count += 1
        print(f"Generated {month_file} ({len(groups[ym])} days, {len(month_html)} bytes)")

    # 3) 既存日次ページにパンくず差し込み
    rebuilt = rebuild_daily_pages(pages)
    print(f"Rebuilt {rebuilt} daily pages with breadcrumb navigation")

    print(f"\nDone: {INDEX_HTML.name} + {month_count} month pages + {rebuilt} daily pages updated")


if __name__ == "__main__":
    main()
