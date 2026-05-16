# claude-news

毎朝の技術ニュースを自動取得・AI 要約し、メールで受け取る仕組み。

5 ソース(GitHub Trending / Hacker News / Reddit / Zenn / Qiita)を Windows ローカルで取得し、Claude CLI が
要約付きの `feed.md` を生成する。参考: Qiita @iineineno03k の2記事を Windows 向けに再構築。

## アーキテクチャ(Windows 単独)

```
[ローカル: Windows タスクスケジューラ]  毎朝 5:00 JST
  1. powershell -File execute.ps1
  2. git pull --rebase origin main
  3. python scripts/fetch_all.py       → raw/*.json 生成
  4. claude -p <要約専用指示>          → feed.md 生成
  5. git add feed.md && commit && push → main に履歴保存
  6. python local/send_mail.py         → info@blueskyjp.com へ送信
```

ニュース API へのアクセスを Windows ローカルから行うため、Claude Code on web routine 側の
外向き通信制限や 403 の影響を受けない。Claude CLI は要約生成だけを担当し、fetch、Git 操作、
メール送信は `execute.ps1` が制御する。

## ディレクトリ

| パス | 役割 |
|------|------|
| `execute.ps1` | fetch → Claude 要約 → commit/push → メール送信を実行(タスクスケジューラ用) |
| `feed-format.md` | Claude CLI に渡す `feed.md` の出力形式と要約ルール |
| `scripts/fetch_*.py` | 各ソースの取得スクリプト(標準ライブラリのみ) |
| `scripts/fetch_all.py` | 5 ソースを順次取得。1 ソース失敗でも継続 |
| `scripts/common.py` | 取得共通ヘルパ |
| `routine_prompt.md` | 旧 Claude Code on web routine 用の指示 |
| `local/send_mail.py` | feed.md をメール送信 |
| `local/daily_local.ps1` | 旧2段構成用。git pull → send_mail を実行 |
| `raw/` | 生データ出力先(git 管理外) |
| `feed.md` | 要約結果(`execute.ps1` が commit/push) |

## セットアップ

### 1. Gmail アプリパスワード

`info@blueskyjp.com`(Google Workspace)で2段階認証を有効化し、アプリパスワードを発行する。
発行した16桁を `local/.env` に記入(`local/.env.example` をコピー):

```
GMAIL_APP_PASSWORD=xxxxxxxxxxxxxxxx
```

`local/.env` は `.gitignore` 対象。

### 2. ローカル実行の前提

同じ Windows ユーザーで、以下が手入力なしで動く状態にする。

- `git pull --rebase origin main`
- `git push origin HEAD:main`
- `python scripts\fetch_all.py`
- `claude -p "test"`
- `python local\send_mail.py`

Claude CLI はタスクスケジューラ実行ユーザーで認証済みにする。Git は SSH 鍵または
Git Credential Manager で、pull/push 時に対話入力が発生しないようにする。

### 3. タスクスケジューラ登録

PowerShell(管理者)で:

```powershell
$repo = "C:\Users\info\repo\claude_news"
$action  = New-ScheduledTaskAction -Execute "powershell.exe" `
  -Argument "-NoProfile -ExecutionPolicy Bypass -File `"$repo\execute.ps1`"" `
  -WorkingDirectory $repo
$daily   = New-ScheduledTaskTrigger -Daily -At 5:00am
$settings = New-ScheduledTaskSettingsSet `
  -StartWhenAvailable `
  -WakeToRun `
  -MultipleInstances IgnoreNew `
  -ExecutionTimeLimit (New-TimeSpan -Hours 1) `
  -RestartCount 3 `
  -RestartInterval (New-TimeSpan -Minutes 15)
Register-ScheduledTask -TaskName "claude-news-daily" `
  -Action $action -Trigger $daily -Settings $settings -Description "技術ニュース要約生成とメール送信"
```

まずは「ユーザーがログオンしているときのみ実行」を推奨。Claude CLI の認証、PATH、
キーチェーンがユーザーセッションに依存するため。

## 手動実行・検証

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\execute.ps1
```

`execute.ps1` は `main` ブランチ上で実行する。成功すると `feed.md` が当日分に更新され、
差分がある場合だけ commit/push してからメール送信する。ログは `local/execute.log` に追記される。

Claude Code on web の routine を登録している場合は、ローカル実行の成功確認後に停止する。
