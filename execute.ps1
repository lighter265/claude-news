# Windows Task Scheduler entry point for the local news routine.
# It fetches raw data, asks Claude CLI to generate feed.md, commits/pushes it, then sends mail.
# Pass -Scheduled when invoked from Task Scheduler to trigger shutdown on completion.
#requires -Version 5.1
param(
    [switch]$Scheduled
)

$ErrorActionPreference = "Stop"

$repo = Split-Path -Parent $PSCommandPath
$log = Join-Path $repo "local\execute.log"
$mutexName = "Global\claude-news-execute"
$mutex = $null
$hasMutex = $false

function Write-Log {
    param([string]$Message)
    $line = "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')  $Message"
    Write-Host $line
    Add-Content -Path $log -Value $line -Encoding UTF8
}

function Invoke-Native {
    param(
        [Parameter(Mandatory = $true)][string]$FilePath,
        [string[]]$ArgumentList = @()
    )

    Write-Log "> $FilePath $($ArgumentList -join ' ')"
    & $FilePath @ArgumentList 2>&1 | ForEach-Object { Write-Log ([string]$_) }
    if ($LASTEXITCODE -ne 0) {
        throw "Command failed with exit code ${LASTEXITCODE}: $FilePath $($ArgumentList -join ' ')"
    }
}

function Assert-CommandExists {
    param([Parameter(Mandatory = $true)][string]$Name)
    if (-not (Get-Command $Name -ErrorAction SilentlyContinue)) {
        throw "Required command is not available in PATH: $Name"
    }
}

function Assert-FileExists {
    param([Parameter(Mandatory = $true)][string]$Path)
    if (-not (Test-Path -LiteralPath $Path)) {
        throw "Required file is missing: $Path"
    }
}

function Assert-CleanWorkTree {
    $changes = & git status --porcelain
    if ($LASTEXITCODE -ne 0) {
        throw "git status failed."
    }
    if ($changes) {
        throw "Working tree is not clean. Commit or remove local changes before running execute.ps1."
    }
}

try {
    Set-Location $repo

    [bool]$createdNew = $false
    $mutex = [System.Threading.Mutex]::new($false, $mutexName, [ref]$createdNew)
    if (-not $mutex.WaitOne(0)) {
        Write-Log "Another execute.ps1 instance is already running. Exiting."
        exit 0
    }
    $hasMutex = $true

    Write-Log "開始"

    Assert-CommandExists "git"
    Assert-CommandExists "python"
    Assert-CommandExists "claude"

    Assert-FileExists (Join-Path $repo "scripts\fetch_all.py")
    Assert-FileExists (Join-Path $repo "feed-format.md")
    Assert-FileExists (Join-Path $repo "local\send_mail.py")

    $branch = (& git rev-parse --abbrev-ref HEAD).Trim()
    if ($LASTEXITCODE -ne 0) {
        throw "git rev-parse failed."
    }
    if ($branch -ne "master") {
        throw "execute.ps1 must run on the master branch. Current branch: $branch"
    }

    Assert-CleanWorkTree

    Write-Log "git pull --rebase origin master 開始"
    Invoke-Native "git" @("pull", "--rebase", "origin", "master")

    Write-Log "ニュース取得開始"
    Invoke-Native "python" @("scripts\fetch_all.py")

    $rawDir = Join-Path $repo "raw"
    $rawFiles = Get-ChildItem -LiteralPath $rawDir -Filter "*.json" -ErrorAction SilentlyContinue | Where-Object { $_.Length -gt 2 }
    if (-not $rawFiles) {
        throw "No non-empty raw JSON files were generated in raw/."
    }
    Write-Log "raw JSON: $($rawFiles.Count) file(s)"

    $prompt = @"
raw/*.json は既に生成済みです。
fetch、commit、push、メール送信は行わないでください。
raw/*.json を読み、feed.md を feed-format.md の記法に従って生成し、上書きしてください。
要約ルールも feed-format.md に従ってください。
"@

    Write-Log "Claude 要約生成開始"
    Invoke-Native "claude" @("--model", "opus", "-p", $prompt)

    $feed = Join-Path $repo "feed.md"
    Assert-FileExists $feed
    $feedBody = Get-Content -LiteralPath $feed -Raw -Encoding UTF8
    if (-not $feedBody.Trim()) {
        throw "feed.md is empty."
    }

    $today = Get-Date -Format "yyyy-MM-dd"
    $expectedTitle = "# 技術ニュース要約 — $today"
    if (-not $feedBody.Contains($expectedTitle)) {
        throw "feed.md does not contain today's title: $expectedTitle"
    }
    if ($feedBody -notmatch "(?m)^## ") {
        throw "feed.md does not contain any source section headings."
    }
    if ($feedBody -notmatch "https?://") {
        throw "feed.md does not contain any URL."
    }

    & git diff --quiet -- feed.md
    $diffExit = $LASTEXITCODE
    if ($diffExit -eq 0) {
        Write-Log "feed.md に差分がありません。commit/push/mail をスキップします。"
        exit 0
    }
    if ($diffExit -ne 1) {
        throw "git diff failed with exit code $diffExit."
    }

    Write-Log "commit/push 開始"
    Invoke-Native "git" @("add", "feed.md")
    Invoke-Native "git" @("commit", "-m", "feed: $today の技術ニュース要約")
    Invoke-Native "git" @("push", "origin", "HEAD:master")

    Write-Log "メール送信開始"
    Invoke-Native "python" @("local\send_mail.py")

    Write-Log "完了"
    if ($Scheduled) {
        Write-Log "スケジューラ実行 → シャットダウン"
        Stop-Computer -Force
    }
} catch {
    Write-Log "エラー: $_"
    exit 1
} finally {
    if ($hasMutex -and $mutex) {
        $mutex.ReleaseMutex() | Out-Null
    }
    if ($mutex) {
        $mutex.Dispose()
    }
}
