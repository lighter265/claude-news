# リポジトリ分析レポート — claude-news

- 対象: `claude-news`（技術ニュース自動要約 bot）
- 分析日: 2026-08-09
- スコープ: `execute.sh`、`scripts/*.py`、`local/send_mail.py`、`feed-format.md` / `local-llm-format.md` 等の現状コード
- 方針: リポジトリの「何をしているか」「不具合」「脆弱性の可能性」「高速化の余地」を検討

---

## 1. このリポジトリは何をしているか

毎朝決まった時刻に **9 つの情報源**から技術ニュースを取得し、Claude CLI で日本語要約を生成してメール/GitHub Pages で配信する bot です。

1. `execute.sh` が `cron`（または systemd timer）から呼ばれ、一連の処理を制御する。
2. `scripts/fetch_all.py` が 9 ソースを **ThreadPoolExecutor で並列取得**し `raw/*.json` に保存する。
   - GitHub Trending (RSS) / Hacker News (Algolia API) / Anthropic (スクレイピング) / OpenAI (RSS) / InfoQ Japan (RSS) / はてなブックマーク it (RDF) / Zenn (API) / Qiita (API) / Reddit r/LocalLLaMA (Atom RSS)
3. `scripts/filter_seen.py` が SQLite (`local/seen_urls.db`) を参照し、直近で既出の URL を `raw/*.json` から除去する（スコア/コメント増加は再掲載）。
4. `claude --model opus -p <要約指示>` が `feed.md` を生成（テーブル形式）。Reddit データは明示的に除外。
5. `scripts/extract_local_llm.py` が GitHub Trending からローカルLLM関連を抽出し、2 回目の `claude` 呼び出しで `feed-local-llm.md` を生成（GitHub と Reddit を別セクション）。
6. `scripts/register_seen.py` が掲載済み URL を DB へ登録。
7. `scripts/generate_html.py` / `scripts/generate_index.py` が `docs/pages/*.html`、`docs/index.html`、`docs/YYYY-MM.html` を生成。
8. `git commit/push` して履歴を残し、`local/send_mail.py`（Gmail SMTP）でメール送信（現在は `execute.sh` 内でコメントアウト）。

アーキテクチャはシンプルで、取得・Git・メールはシェル/標準ライブラリのみ、要約だけを Claude に任せる設計。標準ライブラリのみで完結している点は良い。

---

## 2. 不具合（バグ）の可能性

### 2.1 【中】`execute.sh` に `git pull --rebase` が無い（README と実装の乖離）
README のアーキテクチャ図には「2. `git pull --rebase origin master`」とあるが、`execute.sh` は **pull を行わずに直接 `git add ... && git commit && git push origin HEAD:master`** する。

- リモート `master` に他のコミット（PR マージ、他マシンからの push、手編集した `docs/`）が 1 つでもあると、push は non-fast-forward で失敗する。
- `set -e` により push 失敗でスクリプトは中断するが、すでにローカルに commit 済み。次回の cron でも再度 commit → push 失敗が繰り返され、ローカルに commit が蓄積する。
- 特に `docs/` を commit 対象に含めているため、`docs/` 側の差分があれば確実に衝突する。

**修正案:** commit 直前（または push 前）に `git pull --rebase --autostash origin master` を入れる。あるいは push に `--force-with-lease` を使う（ただし force は慎重に）。

### 2.2 【中】`fetch_qiita.py` が外部 `curl` に依存し、他スクリプトと非互換
README には「取得スクリプト（標準ライブラリのみ）」とあるが、`fetch_qiita.py` だけ `subprocess.run(["curl", ...])` を使っている。

- `curl` が無い環境（最小化コンテナ等）では `FileNotFoundError` で取得失敗（source ごと継続扱いなので全体は止まらないが、Qiita が欠落する）。
- `json.loads(result.stdout)` に例外処理が無く、curl がエラー HTML を返した場合そのままクラッシュする。
- `common.http_get()` を使う他の 8 スクリプトと一貫しない。

**修正案:** `http_get_json()`（他と同じ）に置き換え、取得失敗時は `[]` を返す他ソースと同じ挙動にする。

### 2.3 【低】`generate_html.py` が「表でも箇条書きでもない本文」を破棄する
`parse_feed()` は `## ` セクションのうち、📌 セクションの箇条書きとテーブル行のみを収集し、それ以外の自由文は無視する。

- 例: `feed-local-llm.md` の「ローカルLLM関連リポジトリ」が 0 件の日は `## ローカルLLM関連リポジトリ` の下に「該当記事なし（…）」という**自由文**だけが書かれるが、HTML では空セクションとして丸ごと消え、その説明文が失われる。
- 要約が表形式でない（旧形式の `### 見出し` + 段落）場合も情報が落ちる。

**修正案:** セクション本文の非表・非箇条書きテキストを段落として保持・レンダリングする。あるいは「該当記事なし」等の注記は専用パース処理とする。

### 2.4 【低】タイムゾーン処理の不整合（naive datetime の `.timestamp()`）
- `fetch_zenn.py` / `fetch_qiita.py` / `fetch_anthropic.py` は `datetime.fromisoformat(...)` または `strptime(...)` で**タイムゾーン情報の無い naive datetime** を作り、`.timestamp()` で UNIX 秒にしている。Python は naive datetime を**サーバーのローカルタイムゾーン**とみなす。
- 一方 `fetch_hatena.py` / `fetch_reddit_local_llm.py` / `fetch_infoq_jp.py` は tz-aware で正しく変換している。
- サーバーが UTC のとき、Zenn/Qiita の `published_at`（例: `+09:00`）が 9 時間ズレたタイムスタンプになる。現状はソート順程度にしか使われていないため影響は小さいが、一貫性のバグ。

**修正案:** すべて `datetime.fromisoformat(s[:19]).replace(tzinfo=timezone.utc)` 等で UTC として扱う（Zenn/Qiita の API は JST 固定なので UTC 変換が正しい）。

### 2.5 【低】`filter_seen.py` と `register_seen.py` で「日付の基準」が UTC / ローカルで混在
- `filter_seen.py` の 4 日経過削除は SQLite の `date('now', '-4 days')`（**UTC**）を使う。
- `register_seen.py` の `first_seen` は `date.today().isoformat()`（**ローカル日付**）を使う。
- ローカルが JST の場合、UTC との 9 時間差で「4 日」の窓が実質的に約 3 日弱にずれる。

**修正案:** 一方に統一（推奨: 両方 UTC の `datetime.now(timezone.utc).date().isoformat()` と SQLite 側も `date('now')` で合わせる）。

### 2.6 【低】`execute.sh` の `run()` のパイプによるエラー"隠蔽"リスク
```bash
"$@" 9>&- 2>&1 | while IFS= read -r line; do log "$line"; done
```
- パイプラインの終了ステータスは最後の `while` ループ（常に 0）になるため、`set -o pipefail` が**無いと**コマンド失敗が握りつぶされる。`execute.sh` は `pipefail` を指定しているので現状は検知されるが、`pipefail` を外すと fetch/claude の失敗が静かに無視される脆弱な構造。
- `9>&-` は子プロセスで fd 9 を閉じるが、ロックは親サブシェルが fd 9 を保持したままなので flock 自体は効いている（並行性ガードは機能する）。ただし意図が分かりにくく、無意味な記述。

**修正案:** `pipefail` への依存をコメントで明記、または `run` の戻り値を明示的にチェックする。

### 2.7 【低】`claude` 途中クラッシュ時の「半端な feed.md」が通過する可能性
`claude` が本日のタイトル行まで書いてからクラッシュした場合、`assert_file` / 空チェック / タイトルチェックは通過し、不完全な内容がコミット・配信される。発生確率は低いが、要約行数やセクション数の最低基準チェックを足すと堅牢になる。

---

## 3. 脆弱性・セキュリティの可能性

### 3.1 【高】`claude --dangerously-skip-permissions` が**信頼できない外部コンテンツ**に対してフル権限で動く
`execute.sh` は次のように起動する:
```bash
claude --model opus --dangerously-skip-permissions -p "$prompt"
```
- 入力には 9 つの外部 feed（特に **Reddit の自由投稿**やスクレイピングした HTML）が含まれ、それらは攻撃者が意図的に細工できる。
- `--dangerously-skip-permissions` 下ではエージェントが任意のコマンド・ファイルアクセスを実行できるため、**プロンプトインジェクション**（feed 内の「指示」っぽい文）によって、`.env`（Gmail アプリパスワード）の読み出しや任意コマンド実行を試みる余地がある。
- 現在は「feed.md を上書きせよ」という狭い指示しか出していないため実害は起きにくいが、仕組み上のリスクは高い。

**修正案（優先順）:**
1. `--dangerously-skip-permissions` をやめ、許可ツールを限定する（例: ファイル書き込みのみ許可、`--permission-mode` / allowed-tools の指定）。
2. シークレット（`.env`）をエージェントが読める環境・ユーザーに置かない（別ユーザー/コンテナ/サンドボックスで実行）。
3. feed 本文をそのままプロンプトに渡すのではなく、要約対象データのみを別ファイルにし、エージェントには「このファイルを読んで書け」とさせる。

### 3.2 【中】`.env`（Gmail アプリパスワード）がプロセス環境に展開される
- `execute.sh` が `set -a; source local/.env` で環境変数化し、`send_mail.py` も再読み込みする。gitignore されていて漏洩元は無いが、3.1 のエージェントプロセスから環境変数・`.env` ファイルを読める状態。
- シークレットと要約エージェントを同じ実行コンテキストに置かないのが望ましい。

### 3.3 【低】`send_mail.py` の `starttls()` に明示的 SSL コンテキストが無い
Python 3.10+ では `starttls()` はデフォルトで証明書検証を行うため実害は小さいが、明示的に `ssl.create_default_context()` を渡す方が安全で意図が明確。

### 3.4 【低】公開リポジトリへの feed コミット
`feed.md` / `feed-local-llm.md`（外部リンクを含む）は**パブリック GitHub リポジトリ**に push される。仕様上問題ないが、3.1 のインジェクションで細工された内容が公開される可能性は意識しておくべき。

### 3.5 【低】`slack_notify.py` は現在未使用（コメントアウト）
`SLACK_WEBHOOK_URL` を env から読み、Webhook へ POST。未使用だが、有効化する際は URL の取り扱い（gitignore / secret 管理）に注意。

---

## 4. 高速化の余地

### 4.1 【高】2 回の `claude` 呼び出しを並列化する
`execute.sh` は `claude`（feed.md 用）と `claude`（feed-local-llm.md 用）を**直列**に実行する。各呼び出しは最大 1800 秒（30 分）で、合計で最大 ~60 分の壁時間になるのが全体の支配的要因。

- 2 回目の要約は `feed.md` には依存せず、`raw/*.json`（＋`extract_local_llm.py` の出力）だけに依存する。
- そこで `extract_local_llm.py` を **fetch_all の直後**に移動し、2 つの `claude` をバックグラウンド＋`wait` で並列実行すれば壁時間を概ね半減できる。

```bash
python3 scripts/fetch_all.py
python3 scripts/extract_local_llm.py
claude ... feed.md 用 ... & PID1=$!
claude ... feed-local-llm.md 用 ... & PID2=$!
wait $PID1 $PID2
```

### 4.2 【中〜高】要約モデルを軽量モデルにする
両方の要約に `opus` を使っている。opus は品質は高いが遅く高価。要約タスクには `sonnet` や `haiku` 程度で十分な場合が多く、切り替えで時間・コストを大きく削減できる。品質が気になるなら feed.md は opus、feed-local-llm.md は sonnet 等の使い分けも可。

### 4.3 【低】`generate_index.py` の `rebuild_daily_pages` は事実上死コード
`generate_html.build_html()` はすでに daily ページにパンくずを埋め込すので、`rebuild_daily_pages` は「breadcrumb が無い」ページのみを対象とし、最新生成ページでは常にスキップされる。それでも毎回全ページを読み込んで `"breadcrumb" in text` をチェックする I/O が発生する。既存ページを再生成しないようにする（または削除）と無駄な読み込みが減る。

### 4.4 【低】`extract_local_llm.py` の正規表現をモジュールロード時に 1 回だけコンパイル
`PATTERNS` / `MODEL_PATTERNS` / `LOCAL_PATTERNS` は呼び出しごとに再構築されている。件数こそ少ないが、モジュールトップレベルに移動すれば毎回の再コンパイルが不要に。

### 4.5 【低】HTTP 取得の接続再利用・リトライ
- `common.http_get()` は呼び出しごとに新しい接続を開き（`urllib`）、一時エラー時のリトライも無い（Reddit だけ専用リトライあり）。9 ソースなので現状は無視できるが、共有 `OpenerDirector` ＋簡易リトライで堅牢性が上がる。
- `fetch_all.py` の `ThreadPoolExecutor(max_workers=len(SOURCES))` による並列取得は良好。変更不要。

### 4.6 【低】`filter_seen` / `register_seen` の DB アクセス
- `filter_seen.load_seen()` は `seen_urls` 全件を辞書に読み込む。`nolock=1` は CIFS 前提の指定で、SQLite 自身のロックを無効化している。単独実行（flock ガード）なら問題ないが、`flock` を迂回して直接実行されると DB 破損の危険がある。併記しておく程度。

---

## 5. その他・運用上の所見

- **テスト網羅が狭い:** `tests/` は `fetch_reddit_local_llm.py` と `register_seen.py` のみ。文字列パースに依存する `generate_html.py`、`filter_seen.py`、`extract_local_llm.py`、`send_mail.py` にテストが無く、`feed.md` の表形式が少し崩れると HTML が壊れる（2.3 の類）リスクがカバーされていない。
- **標準ライブラリのみ**という方針はポータビリティ良好。ただし `claude` CLI は未ピン留めの外部依存。
- **`archive/windows/`** は旧 Windows 向けの複製。メイン処理と乖離しやすいので削除か明確な「参照専用」表記を推奨。
- **シークレット管理は概ね良好:** `local/.env` は gitignore 対象。コミット漏れの監視を継続。

---

## 6. 優先対応サマリ

| 優先度 | 項目 | 種別 |
|---|---|---|
| 高 | 3.1 `claude --dangerously-skip-permissions` の権限・サンドボックス見直し | 脆弱性 |
| 高 | 4.1 2 回の `claude` 呼び出しの並列化 | 高速化 |
| 中 | 2.1 `git pull --rebase` の追加（push 失敗防止） | バグ |
| 中 | 2.2 `fetch_qiita.py` の `curl` 依存排除 | バグ |
| 中 | 4.2 要約モデルの軽量化（sonnet/haiku） | 高速化 |
| 中 | 3.2 シークレットと要約エージェントの実行コンテキスト分離 | 脆弱性 |
| 低 | 2.3 HTML で自由文が消える / 2.4・2.5 タイムゾーン不整合 | バグ |
| 低 | 2.6 `run` の pipefail 依存の明記 / 4.3・4.4 の無駄削減 | 保守性・高速化 |
| 低 | テスト追加（generate_html / filter_seen / extract_local_llm） | 品質 |
