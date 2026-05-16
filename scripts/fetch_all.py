"""5 ソースを順次取得し raw/ に保存。1 ソース失敗でも残りは継続する。"""
import importlib
import traceback

from common import save_raw

SOURCES = ["github_trending", "hackernews", "reddit", "zenn", "qiita"]


def main():
    total = 0
    failures = []
    for name in SOURCES:
        try:
            mod = importlib.import_module("fetch_" + name)
            items = mod.fetch()
            path = save_raw(name, items)
            print(f"[OK]   {name}: {len(items)} items -> {path}")
            total += len(items)
        except Exception as e:
            failures.append(name)
            print(f"[FAIL] {name}: {e}")
            traceback.print_exc()
    print(f"--- done. {total} items, {len(failures)} source(s) failed: {failures or 'none'} ---")


if __name__ == "__main__":
    main()
