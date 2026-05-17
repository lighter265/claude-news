# claude-news

毎朝の技術ニュースを自動取得・AI 要約し、メールで受け取る仕組み。

5 ソース(GitHub Trending / Hacker News / Reddit / Zenn / Qiita)を Linux サーバーで取得し、Claude CLI が
要約付きの `feed.md` を生成する。

## アーキテクチャ

```
[Linux サーバー: cron]  毎朝 5:00 JST (= 20:00 UTC 前日)
  1. bash execute.sh
  2. git pull --rebase origin master
  3. python3 scripts/fetch_all.py       → raw/*.json 生成
  4. claude --model opus -p <要約指示>  → feed.md 生成
  5. git add feed.md && commit && push  → master に履歴保存
  6. python3 local/send_mail.py         → メール送信
```

Claude CLI は要約生成だけを担当し、fetch・Git 操作・メール送信は `execute.sh` が制御する。
多重起動防止には `flock` を使用。

## ディレクトリ

| パス | 役割 |
|------|------|
| `execute.sh` | fetch → Claude 要約 → commit/push → メール送信を実行 |
| `feed-format.md` | Claude CLI に渡す `feed.md` の出力形式と要約ルール |
| `scripts/fetch_*.py` | 各ソースの取得スクリプト(標準ライブラリのみ) |
| `scripts/fetch_all.py` | 5 ソースを順次取得。1 ソース失敗でも継続 |
| `scripts/common.py` | 取得共通ヘルパ |
| `local/send_mail.py` | feed.md をメール送信 |
| `raw/` | 生データ出力先(git 管理外) |
| `feed.md` | 要約結果(`execute.sh` が commit/push) |
| `archive/windows/` | 旧 Windows 向けスクリプト(参照用) |

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

### 3. Gmail アプリパスワード

`local/.env.example` をコピーして編集:

```bash
cp local/.env.example local/.env
```

`local/.env` に Gmail アプリパスワード(16 桁)を記入:

```
GMAIL_APP_PASSWORD=xxxxxxxxxxxxxxxx
```

`local/.env` は `.gitignore` 対象。

### 4. 動作確認（手動実行）

```bash
bash execute.sh
```

成功すると `feed.md` が当日分に更新され、差分がある場合だけ commit/push してからメール送信する。
ログは `local/execute.log` に追記される。

### 5. cron 登録

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

### 6. systemd timer（cron の代替）

`/etc/systemd/system/claude-news.service`:

```ini
[Unit]
Description=claude-news daily run

[Service]
Type=oneshot
User=youruser
WorkingDirectory=/path/to/claude-news
ExecStart=/path/to/claude-news/execute.sh
EnvironmentFile=/path/to/claude-news/local/.env
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
