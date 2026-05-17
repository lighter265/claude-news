# 毎朝ローカルで実行: サーバーが push した feed.md を pull してメール送信する。
$ErrorActionPreference = "Stop"
$repo = Split-Path -Parent $PSScriptRoot
$log  = Join-Path $repo "local\daily_local.log"

function Log($m) {
    "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')  $m" | Tee-Object -FilePath $log -Append
}

try {
    Set-Location $repo
    Log "git pull --rebase 開始"
    git pull --rebase 2>&1 | ForEach-Object { Log $_ }
    Log "メール送信開始"
    python "$repo\local\send_mail.py" 2>&1 | ForEach-Object { Log $_ }
    Log "完了"
} catch {
    Log "エラー: $_"
    exit 1
}
