"""7 ソースを並列取得し raw/ に保存。1 ソース失敗でも残りは継続する。"""
import importlib
import os
import traceback
from concurrent.futures import ThreadPoolExecutor, as_completed

from common import RAW_DIR, save_raw

SOURCES = [
    "github_trending",
    "hackernews",
    "infoq_jp",
    "hatena",
    "zenn",
    "qiita",
    "reddit_local_llm",
]


def fetch_source(name):
    mod = importlib.import_module("fetch_" + name)
    items = mod.fetch()
    path = save_raw(name, items)
    return name, len(items), path


def main():
    total = 0
    failures = []

    with ThreadPoolExecutor(max_workers=len(SOURCES)) as executor:
        future_to_name = {executor.submit(fetch_source, name): name for name in SOURCES}
        for future in as_completed(future_to_name):
            name = future_to_name[future]
            try:
                _, count, path = future.result()
                print(f"[OK]   {name}: {count} items -> {path}")
                total += count
            except Exception as e:
                failures.append(name)
                print(f"[FAIL] {name}: {e}")
                traceback.print_exc()
                if name == "reddit_local_llm":
                    # 空結果で上書きすると「取得失敗」が「該当記事なし」として
                    # 静かに公開されてしまう（2026-10-27に発生）。
                    # rawは上書きせず、失敗マーカーだけを置く。古いrawの再利用は
                    # execute.sh 側で退避して防ぐ。
                    marker = os.path.join(RAW_DIR, "reddit_local_llm.failed")
                    with open(marker, "w", encoding="utf-8") as f:
                        f.write(f"{type(e).__name__}: {e}")
                    print(
                        f"[WARN] {name}: {type(e).__name__}: {e}; "
                        f"raw left untouched, failure marker -> {marker}"
                    )

    print(f"--- done. {total} items, {len(failures)} source(s) failed: {failures or 'none'} ---")


if __name__ == "__main__":
    main()
