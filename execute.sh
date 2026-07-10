#!/usr/bin/env bash
# Linux entry point: fetch news, generate feed.md via Claude CLI, commit/push, send mail.
set -euo pipefail

TRY_MODE=false
NO_FILTER_MODE=false

while [[ $# -gt 0 ]]; do
    case "$1" in
        --try)
            TRY_MODE=true
            shift
            ;;
        --no-filter)
            NO_FILTER_MODE=true
            shift
            ;;
        *)
            echo "Unknown option: $1" >&2
            exit 1
            ;;
    esac
done

# cronはPATHが最小限のためclaudeが見つからない場合がある
export PATH="/home/lighter/.local/bin:/home/lighter/.opencode/bin:$PATH"

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
    "$@" 9>&- 2>&1 | while IFS= read -r line; do log "$line"; done
}

assert_command() {
    command -v "$1" >/dev/null 2>&1 || { log "Required command not found in PATH: $1"; exit 1; }
}

assert_file() {
    [[ -f "$1" ]] || { log "Required file missing: $1"; exit 1; }
}

main() {
    cd "$REPO"
    # .env 読み込み
    if [[ -f "$REPO/local/.env" ]]; then
        set -a
        source "$REPO/local/.env"
        set +a
    fi
    local init_msg="開始"
    if [[ "$TRY_MODE" == true ]]; then
        init_msg="$init_msg [TRY-MODE: git commit/push/mail スキップ]"
    fi
    if [[ "$NO_FILTER_MODE" == true ]]; then
        init_msg="$init_msg [NO-FILTER-MODE: 既出URLフィルタースキップ]"
    fi
    log "$init_msg"

    assert_command git
    assert_command python3
    assert_command claude #opencode #claude

    assert_file "scripts/fetch_all.py"
    assert_file "feed-format.md"
    assert_file "local/send_mail.py"

    log "ニュース取得開始"
    run python3 scripts/fetch_all.py

    if [[ "$NO_FILTER_MODE" == true ]]; then
        log "既出URLフィルタスキップ (--no-filter)"
    else
        log "既出URLフィルタ開始"
        run python3 scripts/filter_seen.py
    fi

    local raw_count
    raw_count=$(find "$REPO/raw" -name "*.json" -size +2c 2>/dev/null | wc -l || echo 0)
    if [[ "$raw_count" -eq 0 ]]; then
        log "raw/ に有効な JSON ファイルが生成されませんでした。"
        exit 1
    fi
    log "raw JSON: ${raw_count} ファイル"

    local prompt="raw/*.json を読み、feed-format.md の要約ルール・記法に従って生成し、feed.md へ上書きしてください。"
    log "要約生成開始"

    #run timeout 1800 claude -p "$prompt"
    run timeout 1800 claude --model opus --dangerously-skip-permissions -p "$prompt"
    #run timeout 1800 opencode run "$prompt"

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

    log "HTML生成"
    run python3 scripts/generate_html.py
    run python3 scripts/generate_index.py

    if [[ "$TRY_MODE" == false ]]; then
        log "Git commit & push"
        git add feed.md docs/
        if git diff --cached --quiet; then
            log "差分なし、pushスキップ"
        else
            git commit -m "feed: $today の技術ニュース要約"
            git push origin HEAD:master
        fi

        #log "メール送信開始"
        #run python3 local/send_mail.py

        #log "Slack通知"
        #if [[ -n "${SLACK_WEBHOOK_URL:-}" ]]; then
        ##    run python3 scripts/slack_notify.py
        #else
        #    log "SLACK_WEBHOOK_URL未設定、Slack通知スキップ"
        #fi
    else
        log "[TRY MODE] commit/push/mail/slack をスキップ"
    fi

    log "完了"
}

(
    flock -n 9 || { log "別の execute.sh が実行中です。スキップします。 (保持PID: $(fuser "$LOCKFILE" 2>/dev/null || echo '不明'))"; exit 0; }
    main
) 9>"$LOCKFILE"
