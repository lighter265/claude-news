# Context

現在 `execute.ps1` を Windows タスクスケジューラで毎朝 5:00 JST に起動する構成。
問題：ログインセッションなし（未ログイン状態）だとタスクが動かない／不安定な場合がある。
目的：「ログイン不要で確実に毎日実行」を実現する手段を比較し、最適案を選ぶ。

---

# 現状の構成

| レイヤー | 技術 |
|--------|------|
| スケジューラ | Windows タスクスケジューラ |
| オーケストレーション | PowerShell (`execute.ps1`) |
| ニュース取得 | Python 3.x (stdlib only) |
| AI 要約 | Claude CLI (`claude --model opus`) |
| 配信 | smtplib + Gmail SMTP |
| 出力 | `feed.md` → GitHub にコミット＋プッシュ |

---

# 比較検討

## Option A: Windows のまま修正（タスクスケジューラ設定強化）

### 対処法
1. **「ユーザーがログオンしているかどうかにかかわらず実行する」に変更**
   - タスクスケジューラ GUI → 全般タブ → "Run whether user is logged on or not"
   - `SYSTEM` アカウントまたは専用サービスアカウントで実行
   - `Register-ScheduledTask` に `-RunLevel Highest -LogonType S4U` または `-LogonType Password` を指定
2. **パスワードを保存して実行**（`-LogonType Password` ＋ パスワード入力）
3. **NSSM / WinSW でサービス化**（スケジューラ依存を排除）
   - NSSM: `nssm install claude-news powershell.exe -File execute.ps1`

### 制約・注意点
- Claude CLI がユーザープロファイル依存（認証トークン、PATH）の場合、SYSTEM 実行では認証が見えない可能性あり
- `Stop-Computer` (シャットダウン) は SYSTEM 権限でも動くが要確認
- Windows Update や再起動後のタスク状態に注意

### コスト・工数
- 追加費用なし
- 設定変更のみ（30分〜2時間）

---

## Option B: Linux サーバーへ移行（VPS / ラズパイ等）

### 構成案
- VPS（Hetzner CX22 等: ~€4/月）または自宅 Raspberry Pi
- `cron` でスケジュール → シェルスクリプト or Python スクリプト
- PowerShell の処理を bash + Python に書き換え
- Claude CLI は Linux 対応済み（`npm install -g @anthropic-ai/claude-code` or 公式バイナリ）

### 書き換え範囲
| 現行 | 移行後 |
|------|--------|
| `execute.ps1` (PowerShell) | `execute.sh` (bash) |
| `Register-ScheduledTask` | `crontab -e` / `systemd timer` |
| `Global\` mutex | `flock` コマンド |
| `Stop-Computer` | 不要（サーバーは常時稼働）|
| `local/.env` | `.env` そのまま or `systemd` EnvironmentFile |

### Python スクリプト群（`scripts/`, `local/send_mail.py`）
- **変更不要**（stdlib only で OS 非依存）

### メリット
- ログイン不要問題が根本解決
- `cron` は枯れた技術で信頼性が高い
- 常時稼働なのでシャットダウンロジックが不要になりシンプル化

### デメリット
- 月額費用（VPS の場合）
- bash 書き換え工数（execute.ps1 が約 200 行 → bash 換算で同程度）
- Claude CLI の認証を Linux 環境でセットアップする必要あり

### コスト・工数
- VPS: ~€4〜6/月
- 移行工数: 半日〜1日

---

## Option C: GitHub Actions（クラウド実行）

### 構成案
- `.github/workflows/daily.yml` を追加
- `schedule: cron: '0 20 * * *'` (UTC 20:00 = JST 05:00)
- ジョブ内で Python fetch → Claude API 呼び出し → feed.md 更新 → push → メール送信

### Claude 呼び出し方法
- CLI ではなく **Anthropic API** (`anthropic` Python SDK) を使用
- `ANTHROPIC_API_KEY` を GitHub Secrets に登録

### メリット
- サーバー管理不要・費用なし（パブリックリポジトリなら無制限、プライベートは 2000分/月無料）
- ログイン不要問題が完全解消
- `execute.ps1` のほとんどのロジックが不要（GitHub Actions がオーケストレーション担当）

### 書き換え範囲
| 現行 | 移行後 |
|------|--------|
| `execute.ps1` | `.github/workflows/daily.yml` |
| `claude --model opus` CLI | Python `anthropic` SDK（`claude-opus-4-x`）|
| Gmail SMTP 送信 | `send_mail.py` そのまま利用可（Actions secrets で認証）|
| `git commit` / `git push` | `actions/checkout` + `git push` in workflow |

### デメリット
- Claude CLI → API SDK へのコード変更が必要（プロンプト渡し方を調整）
- GitHub Actions の実行時間が保証されない（最大数十分の遅延あり）
- プライベートリポジトリの場合、月次制限に注意

### コスト・工数
- 費用: 基本無料
- 工数: 半日（YAML + Python SDK 化）

---

## Option D: その他クラウドサービス

| サービス | 概要 | 費用 |
|--------|------|------|
| **AWS Lambda + EventBridge** | Cron でコンテナ実行 | ~$0/月（無料枠内） |
| **Google Cloud Run Jobs** | スケジュールジョブ | ~$0/月（無料枠内） |
| **Render.com Cron Jobs** | 無料プランあり | 無料〜$7/月 |
| **fly.io** | 軽量 VM、Machines API | ~$2/月 |

これらは Option C（GitHub Actions）と同様、Claude CLI の代わりに API SDK が必要になる。

---

# 推奨案の整理

| 観点 | A: Windows修正 | B: Linux VPS | C: GitHub Actions |
|-----|--------------|-------------|-----------------|
| 確実性 | △（設定次第） | ◎ | ◎ |
| 費用 | 無料 | €4〜6/月 | 無料 |
| 移行コスト | 低（設定のみ） | 中（bash書き換え）| 中（workflow+SDK）|
| 管理コスト | 低 | 中（OS管理） | 低 |
| Claude CLI 継続 | ◎ | ◎ | ✗（SDK化必要）|
| 停止後シャットダウン | ◎ | 不要 | 不要 |

**最も低コスト・低リスクな順**: A → C → B → D

---

# 実装方針（選択後）

選択肢が決まり次第、以下を実装：

### A を選ぶ場合
- `execute.ps1` は変更なし
- タスクスケジューラの登録コマンドを更新（`-LogonType S4U` or サービスアカウント）
- README に設定手順を追記

### B を選ぶ場合
- `execute.sh` を新規作成（`execute.ps1` の bash 移植）
- `systemd` timer または `crontab` の設定例を追加
- README に Linux セットアップ手順を追記
- `execute.ps1` / `local/daily_local.ps1` は削除またはアーカイブ

### C を選ぶ場合
- `.github/workflows/daily.yml` を新規作成
- `scripts/run_claude.py` を新規作成（`anthropic` SDK でプロンプト送信）
- `local/send_mail.py` はそのまま流用
- `execute.ps1` は削除またはアーカイブ

---

# 検証方法

- **A**: タスクスケジューラからログアウト状態でテスト実行し `execute.log` を確認
- **B**: VPS で手動実行 → cron で翌日自動実行確認 → `feed.md` のコミットとメール受信確認
- **C**: `workflow_dispatch` で手動トリガー → Actions ログ確認 → `feed.md` PR/コミット確認 → メール受信確認
