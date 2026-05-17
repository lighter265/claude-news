#!/usr/bin/env bash
# Linux entry point: fetch news, generate feed.md via Claude CLI, commit/push, send mail.
set -euo pipefail

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

    local raw_count
    raw_count=$(find "$REPO/raw" -name "*.json" -size +2c 2>/dev/null | wc -l || echo 0)
    if [[ "$raw_count" -eq 0 ]]; then
        log "raw/ に有効な JSON ファイルが生成されませんでした。"
        exit 1
    fi
    log "raw JSON: ${raw_count} ファイル"

    local prompt="raw/*.json は既に生成済みです。
fetch、commit、push、メール送信は行わないでください。
raw/*.json を読み、feed.md を feed-format.md の記法に従って生成し、上書きしてください。
要約ルールも feed-format.md に従ってください。"

    log "Claude 要約生成開始"
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
