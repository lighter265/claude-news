#!/usr/bin/env bash
# Linux entry point: fetch news, generate feed.md via Claude CLI, commit/push, send mail.
set -euo pipefail

# cronはPATHが最小限のためclaudeが見つからない場合がある
export PATH="/home/lighter/.local/bin:$PATH"

REPO="$(cd "$(dirname "$0")" && pwd)"
LOG="$REPO/local/execute.log"
LOCKFILE="$REPO/local/execute.lock"

log() {
    local line
    line="$(date '+%Y-%m-%d %H:%M:%S')  $*"
    echo "$line"
    echo "$line" >> "$LOG"
}

run() {
    log "> $*"
    "$@" 2>&1 | while IFS= read -r line; do log "$line"; done
}

assert_command() {
    command -v "$1" >/dev/null 2>&1 || { log "Required command not found in PATH: $1"; exit 1; }
}

assert_file() {
    [[ -f "$1" ]] || { log "Required file missing: $1"; exit 1; }
}

main() {
    cd "$REPO"
    log "開始"

    assert_command git
    assert_command python3
    assert_command claude

    assert_file "scripts/fetch_all.py"
    assert_file "feed-format.md"
    assert_file "local/send_mail.py"

    local branch
    branch=$(git rev-parse --abbrev-ref HEAD)
    if [[ "$branch" != "master" ]]; then
        log "master ブランチで実行してください。現在: $branch"
        exit 1
    fi

    local changes
    changes=$(git status --porcelain)
    if [[ -n "$changes" ]]; then
        log "作業ツリーが clean ではありません。先にコミットまたはリセットしてください。"
        exit 1
    fi

    log "git pull --rebase origin master 開始"
    run git pull --rebase origin master

    log "ニュース取得開始"
    run python3 scripts/fetch_all.py

    log "既出URLフィルタ開始"
    run python3 scripts/filter_seen.py

    local raw_count
    raw_count=$(find "$REPO/raw" -name "*.json" -size +2c 2>/dev/null | wc -l || echo 0)
    if [[ "$raw_count" -eq 0 ]]; then
        log "raw/ に有効な JSON ファイルが生成されませんでした。"
        exit 1
    fi
    log "raw JSON: ${raw_count} ファイル"

    local prompt
    prompt=$(cat <<'EOF'
raw/ 配下の技術ニュース JSON（github_trending / hackernews / reddit / zenn / qiita の
各 raw/<source>.json。section_*.md などは対象外）から feed.md を生成してください。

手順:
1. まず feed-format.md を読み、「サブエージェント分担」「per-source セクション生成ルール」
   「メインエージェントの組み立てルール」を把握する。
2. raw/ に存在する各 raw/<source>.json に対し、1 ソースにつき 1 つサブエージェントを
   並列に dispatch する（全ソース分を同時に起動する）。各サブエージェントには次を指示する:
   「raw/<source>.json と feed-format.md を読み、per-source セクション生成ルールに従って
   当該ソースのセクションを生成し、raw/section_<source>.md に全体上書きで書き出す。
   feed.md 本体やほかのファイルは編集しない。」
3. 全サブエージェントの完了後、今回 dispatch したサブエージェントが書き出した
   raw/section_<source>.md のみを読み込み、feed-format.md の組み立てルールに従って
   feed.md を全体上書きで生成する。前回実行の古い section ファイルが残っていても、
   今回処理したソースの分だけを使うこと。
4. fetch、commit、push、メール送信は行わない。
EOF
)

    log "Claude 要約生成開始"
    #run claude -p "$prompt"
    run claude --model opus -p "$prompt"

    assert_file "feed.md"

    local feed_body
    feed_body=$(cat feed.md)
    if [[ -z "${feed_body// }" ]]; then
        log "feed.md が空です。"
        exit 1
    fi

    local today
    today=$(date '+%Y-%m-%d')
    local expected_title="# 技術ニュース要約 — $today"
    if [[ "$feed_body" != *"$expected_title"* ]]; then
        log "feed.md に本日のタイトルがありません: $expected_title"
        exit 1
    fi
    if ! grep -qm1 '^## ' feed.md; then
        log "feed.md にセクション見出しがありません。"
        exit 1
    fi
    if ! grep -qEm1 'https?://' feed.md; then
        log "feed.md に URL がありません。"
        exit 1
    fi

    log "掲載URLをDBへ登録"
    run python3 scripts/register_seen.py

    if git diff --quiet -- feed.md; then
        log "feed.md に差分なし。commit/push/mail をスキップします。"
        exit 0
    fi

    log "commit/push 開始"
    run git add feed.md
    run git commit -m "feed: ${today} の技術ニュース要約"
    run git push origin HEAD:master

    log "メール送信開始"
    run python3 local/send_mail.py

    log "完了"
}

(
    flock -n 9 || { log "別の execute.sh が実行中です。スキップします。"; exit 0; }
    main
) 9>"$LOCKFILE"
