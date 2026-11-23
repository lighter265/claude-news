"""6 ソースを並列取得し raw/ に保存。1 ソース失敗でも残りは継続する。

reddit_local_llm は donsetch を使うため並列から外し、
execute.sh で fetch_all の後に個別に取得する（並列だと donsetch が exit 3 になる）。
"""
import importlib
import traceback
from concurrent.futures import ThreadPoolExecutor, as_completed

from common import save_raw

SOURCES = [
    "github_trending",
    "hackernews",
    "infoq_jp",
    "hatena",
    "zenn",
    "qiita",
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

    print(f"--- done. {total} items, {len(failures)} source(s) failed: {failures or 'none'} ---")


if __name__ == "__main__":
    main()
