# claude-news

毎朝の技術ニュースを自動取得・AI 要約し、メールで受け取る仕組み。

5 ソース(GitHub Trending / Hacker News / Reddit / Zenn / Qiita)を取得し、Claude Code が
要約付きの `feed.md` を生成する。参考: Qiita @iineineno03k の2記事を Windows 向けに再構築。

## アーキテクチャ(サーバー+ローカル2段)

```
[サーバー: Claude Code routine]  毎朝 4:30 JST
  1. python scripts/fetch_all.py   → raw/*.json 生成
  2. routine(Claude)が raw を読み要約 → feed.md 生成
  3. git add feed.md && commit && push
        │ git(feed.md の受け渡し)
        ▼
[ローカル: Windows タスクスケジューラ]  毎朝 5:00 JST + ログオン時
  1. git pull --rebase
  2. python local/send_mail.py     → info@blueskyjp.com へ送信
```

AI が必要な処理(要約)をサーバー、AI 不要な処理(メール送信)をローカルに分離。
ローカル側は git と Python のみで完結し、Claude CLI の OAuth 失効の影響を受けない。

## ディレクトリ

| パス | 役割 |
|------|------|
| `scripts/fetch_*.py` | 各ソースの取得スクリプト(標準ライブラリのみ) |
| `scripts/fetch_all.py` | 5 ソースを順次取得。1 ソース失敗でも継続 |
| `scripts/common.py` | 取得共通ヘルパ |
| `routine_prompt.md` | サーバー routine に渡す要約指示 |
| `local/send_mail.py` | feed.md をメール送信 |
| `local/daily_local.ps1` | git pull → send_mail を実行(タスクスケジューラ用) |
| `raw/` | 生データ出力先(git 管理外) |
| `feed.md` | 要約結果(routine が生成・commit) |

## セットアップ

### 1. Gmail アプリパスワード

`info@blueskyjp.com`(Google Workspace)で2段階認証を有効化し、アプリパスワードを発行する。
発行した16桁を `local/.env` に記入(`local/.env.example` をコピー):

```
GMAIL_APP_PASSWORD=xxxxxxxxxxxxxxxx
```

`local/.env` は `.gitignore` 対象。

### 2. サーバー routine 登録

Claude Code の `/schedule` で routine を作成する。

- 対象リポジトリ: この GitHub リポジトリ
- トリガー: schedule、毎朝 4:30 JST = cron `30 19 * * *`(UTC)
- プロンプト: 「リポジトリの routine_prompt.md を読み手順に従え」
- モデル: `claude-opus-4-7`

**ネットワーク許可(必須)**: routine 環境はデフォルト(Trusted)だと GitHub 系しか
通らず、ニュース API が 403 になる。環境設定の Network access を **Custom** にして
Allowed domains に以下を追加し、「Also include default list of common package managers」
を必ずチェックする(外すと GitHub も切れて clone に失敗する):

```
hn.algolia.com
www.reddit.com
zenn.dev
qiita.com
```

GitHub Trending は `mshibanami.github.io`(GitHub 系)のため Trusted で既に通る。
Network access を **Full** にすれば個別指定は不要。

**push 先**: Claude Code on the web はセッションごとに作業ブランチを切るため、
`routine_prompt.md` では `git push origin HEAD:main` で main へ直接 push する。

### 3. ローカル タスクスケジューラ登録

PowerShell(管理者)で:

```powershell
$repo = "C:\Users\info\repo\claude_news"
$action  = New-ScheduledTaskAction -Execute "powershell.exe" `
    -Argument "-NoProfile -ExecutionPolicy Bypass -File `"$repo\local\daily_local.ps1`""
$daily   = New-ScheduledTaskTrigger -Daily -At 5:00am
$logon   = New-ScheduledTaskTrigger -AtLogOn
Register-ScheduledTask -TaskName "claude-news-daily" `
    -Action $action -Trigger $daily,$logon -Description "技術ニュース要約メール送信"
```

`-AtLogOn` は朝の実行時刻に PC がオフだった場合の救済。

## 手動実行・検証

```powershell
python scripts\fetch_all.py          # 取得のみ(raw/ に出力)
python local\send_mail.py            # feed.md をメール送信
powershell -File local\daily_local.ps1   # pull + 送信(タスクと同じ)
```

routine 側はサーバーで `/schedule` から手動トリガーして feed.md の push を確認する。
