# claude-news

毎朝の技術ニュースを自動取得・AI 要約し、静的サイト(`docs/`)として公開する仕組み。

7 ソース(GitHub Trending / Hacker News / InfoQ Japan / はてなブックマーク (tech) / Zenn / Qiita / Reddit r/LocalLLaMA)を Linux サーバーで取得し、Claude CLI が
要約付きの `feed.md` とローカルLLM専用の `feed-local-llm.md` を生成する。

## アーキテクチャ

```
[Linux サーバー: cron]  毎朝 5:00 JST (= 20:00 UTC 前日)
  1. bash execute.sh
  2. git pull --rebase origin master
  3. python3 scripts/fetch_all.py       → raw/*.json 生成（RedditはAtom RSS）
  4. claude --model opus -p <要約指示>  → feed.md / feed-local-llm.md 生成
  5. python3 scripts/generate_html.py   → docs/pages/YYYY-MM-DD.html 生成
  6. git add feed*.md docs/ && commit && push  → master に履歴保存
```

Claude CLI は要約生成だけを担当し、fetch・Git 操作・HTML 生成は `execute.sh` が制御する。
多重起動防止には `flock` を使用。

## ディレクトリ

| パス | 役割 |
|------|------|
| `execute.sh` | fetch → Claude 要約 → HTML 生成 → commit/push を実行 |
| `feed-format.md` | Claude CLI に渡す `feed.md` の出力形式と要約ルール |
| `scripts/fetch_*.py` | 各ソースの取得スクリプト(標準ライブラリのみ) |
| `scripts/fetch_all.py` | 7 ソースを並列取得。1 ソース失敗でも継続 |
| `scripts/common.py` | 取得共通ヘルパ |
| `scripts/generate_html.py` | feed.md / feed-local-llm.md から日別ページ `docs/pages/*.html` を生成 |
| `raw/` | 生データ出力先(git 管理外) |
| `feed.md` | 要約結果(`execute.sh` が commit/push) |
| `feed-local-llm.md` | GitHub Trending抽出とReddit r/LocalLLaMAを別セクションで要約 |
| `archive/windows/` | 旧 Windows 向けスクリプト(参照用) |

### Reddit r/LocalLLaMA の取得範囲

- 認証不要の Atom RSS `https://www.reddit.com/r/LocalLLaMA/new/.rss?limit=100` を使用する。
- 投稿日時が実行時刻から直近48時間以内のエントリを全件対象にする。RSSは1ページ100件までのため、`after` で最大 `MAX_PAGES` ページ遡って取得する（2ページ目以降の失敗は取得済み分で続行）。
- `filter_seen.py` はこのソースだけ既出URLを除去せず `seen_before`（前日までにDB登録済みか）を付与する。`feed-local-llm.md` では「新着」と「前日にも掲載」の2セクションに分けて表示する。
- RSS取得・XML解析・日付範囲は [scripts/fetch_reddit_local_llm.py](scripts/fetch_reddit_local_llm.py) の `REDDIT_RSS_LIMIT`、`RECENT_WINDOW_HOURS`、`DESCRIPTION_MAX_CHARS` で調整できる（URLのlimitも定数から組み立てる）。
- Reddit専用の識別User-Agentを付け、HTTP 429/5xxだけを最大2回リトライする。`Retry-After` があれば優先し、無ければ指数バックオフを使う。
- 取得結果は `raw/reddit_local_llm.json` に保存し、`raw/local_llm_github.json` とは混ぜない。本文はHTMLをプレーンテキスト化し、要約用に500文字（`DESCRIPTION_MAX_CHARS`）まで保持する。
- Reddit取得失敗時は空のrawを保存して前回の投稿を再利用せず、GitHub分のローカルLLM要約を継続する。

### 日別ページの表示

- 日別ページ(`docs/pages/YYYY-MM-DD.html`)は、開いた時点では📌3行サマリとソース名だけが見える。
- ソース名の行をクリック(タップ)すると、そのソースの記事一覧が開閉する。JS 無効時は全展開で表示される。

## セットアップ

### 1. 前提ソフトウェア

```bash
# Python 3
python3 --version

# Git（SSH 鍵設定済みで push が対話なしで通ること）
git push origin master --dry-run

# Claude CLI
npm install -g @anthropic-ai/claude-code
claude --version
claude login   # API キー認証
```

### 2. リポジトリのクローン

```bash
git clone git@github.com:lighter265/claude-news.git
cd claude-news
```

### 3. 動作確認（手動実行）

```bash
bash execute.sh
```

成功すると `feed.md` が当日分に更新され、日別ページを生成し、差分がある場合だけ commit/push する。
ログは `local/execute.log` に追記される。

### 4. cron 登録

```bash
crontab -e
```

以下を追記（サーバーのタイムゾーンが UTC の場合）:

```
0 20 * * * /path/to/claude-news/execute.sh >> /path/to/claude-news/local/execute.log 2>&1
```

JST のサーバー（`TZ=Asia/Tokyo`）の場合:

```
0 5 * * * /path/to/claude-news/execute.sh >> /path/to/claude-news/local/execute.log 2>&1
```

cron 実行時は PATH が限られるため、`which claude` / `which python3` の絶対パスを使う方が確実:

```
0 20 * * * PATH=/usr/local/bin:/usr/bin:/bin /path/to/claude-news/execute.sh >> /path/to/claude-news/local/execute.log 2>&1
```

### 5. systemd timer（cron の代替）

`/etc/systemd/system/claude-news.service`:

```ini
[Unit]
Description=claude-news daily run

[Service]
Type=oneshot
User=youruser
WorkingDirectory=/path/to/claude-news
ExecStart=/path/to/claude-news/execute.sh
```

`/etc/systemd/system/claude-news.timer`:

```ini
[Unit]
Description=claude-news daily timer

[Timer]
OnCalendar=*-*-* 20:00:00 UTC
Persistent=true

[Install]
WantedBy=timers.target
```

```bash
sudo systemctl enable --now claude-news.timer
```

## トラブルシューティング

- **`claude: command not found`** — `npm install -g @anthropic-ai/claude-code` 後、`which claude` でパスを確認して cron の PATH に追加する
- **`git push` が失敗** — SSH 鍵がサーバーに設定されているか確認: `ssh -T git@github.com`
- **feed.md が空 / タイトルなし** — Claude CLI の認証切れの可能性。`claude login` を再実行する
- **ログ確認** — `tail -f local/execute.log`
