# 毎朝の技術ニュース要約 routine

このリポジトリで、技術ニュースを取得して要約フィードを生成し、push してください。

## 手順

1. **生データ取得**

   ```
   python scripts/fetch_all.py
   ```

   `raw/` に各ソースの JSON が出力される。1 ソース失敗してもエラーにせず、取得できた分で続行する。

2. **要約フィード生成** — `raw/*.json` をすべて読み、`feed-format.md` の形式と要約ルールに従って `feed.md` を新規生成(全体を上書き)する。

3. **コミット & main へプッシュ**

   ```
   git add feed.md
   git commit -m "feed: <YYYY-MM-DD> の技術ニュース要約"
   git push origin HEAD:master
   ```

   - `feed.md` に差分が無い場合はコミットしない。
   - **必ず `main` ブランチへ push する**(`git push origin HEAD:master`)。
     Claude Code on the web はセッションごとに作業ブランチを切るが、ローカル側は
     `main` を pull して受け取るため、作業ブランチへの push では運用が成立しない。

## feed.md の形式と要約ルール

`feed-format.md` に従う。テーブル形式で出力すること。
