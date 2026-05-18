# 既出URL重複排除 — 設計・決定事項

## 目的

`feed.md` に一度掲載したURLを翌日以降の取得結果からフィルタし、
スコアやコメント数が大幅に増加した場合のみ再掲する。

## 決定案: A+D ハイブリッド

- **案A**: SQLite DB + filter スクリプトでClaude前にraw JSONを浄化
- **案D** の要素追加: 「feed.mdに実際に掲載されたURL」のみDBへ登録（rawを通過したがClaudeが落とした記事は追跡しない）

## パイプライン

```
fetch_all.py
  ↓ raw/*.json（全URL含む）
filter_seen.py        ← DB参照のみ・rawを上書き（既出URL除去）
  ↓ raw/*.json（新規 or 再表示条件を満たすURLのみ）
claude --model opus   ← クリーンなrawを処理
  ↓ feed.md
register_seen.py      ← feed.mdのURLをDBへ登録/更新
  ↓ DB更新
git commit / push / email
```

## DBスキーマ

```sql
-- local/seen_urls.db（gitignore対象）
CREATE TABLE IF NOT EXISTS seen_urls (
    url           TEXT PRIMARY KEY,
    source        TEXT,
    first_seen    TEXT,   -- ISO date
    last_seen     TEXT,   -- ISO date
    last_score    INTEGER,
    last_comments INTEGER,
    times_shown   INTEGER DEFAULT 0
);
```

## 再表示条件（filter_seen.py）

| 条件 | 閾値 |
|------|------|
| score 増加率 | 前回比 +30% 以上 |
| comments 増加数 | 前回比 +20 件以上 |

新規URL（DB未登録）は無条件に通過。

## 新規ファイル

| ファイル | 役割 |
|----------|------|
| `scripts/filter_seen.py` | DB参照→raw JSON浄化（DB書き込みなし） |
| `scripts/register_seen.py` | feed.mdパース→DB upsert |

## execute.sh への変更点

```bash
# fetch_all.py の直後に追加
run python3 scripts/filter_seen.py

# feed.md バリデーション通過後・git add の直前に追加
run python3 scripts/register_seen.py
```

## .gitignore への追加

```
local/seen_urls.db
```
