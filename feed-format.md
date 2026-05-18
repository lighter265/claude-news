# feed.md 生成形式

このファイルは、Claude CLI に `feed.md` の出力形式を伝えるための仕様です。
`raw/*.json` は生成済みである前提で読み込み、`feed.md` 全体を上書きしてください。

## 実行範囲

- `raw/*.json` を読み、技術ニュース要約として `feed.md` を生成する。
- `feed.md` は必ず全体を上書きする。
- fetch、commit、push、メール送信は行わない。

## 出力形式

```markdown
# 技術ニュース要約 — YYYY-MM-DD

## GitHub Trending
### <内容がわかる日本語見出し>
<人に説明できるレベルの要約。3〜5文。>
<一次ソース URL>

### ...

## Hacker News
（同様）

## Reddit
（同様）

## Zenn
（同様）

## Qiita
（同様）
```

## セクションルール

- セクション順は GitHub Trending、Hacker News、Reddit、Zenn、Qiita とする。
- 各ソースから、注目度(score)の高いものを中心に 5〜8 件ずつ選ぶ。
- 取得できなかったソース、または有用な項目がないソースは見出しごと省略してよい。
- 各記事は「日本語見出し」「要約」「一次ソース URL」の順に書く。
- URL は各項目の末尾に単独行で置く。

## 要約ルール

1. タイトルは内容がわかる日本語見出しにする。原題の直訳ではなく、記事の要点が伝わるように意訳する。
2. 要約は記事の内容を十分に説明する。リンク先を開かなくても、人に説明できるレベルで要点が分かるようにする。
3. 要約は 3〜5 文を目安にし、短すぎる箇条書きにはしない。
4. 一次ソース URL は raw の URL を優先する。
5. 客観的・中立に書く。誇張、煽り、断定しすぎる表現を避ける。
6. raw の `extra` にタグ、コメント数、説明文などがある場合は、要約の判断材料として使ってよい。

## サブエージェント分担

`feed.md` の生成はソース単位でサブエージェントに分担できる。各サブエージェントは
1 つの `raw/<source>.json` だけを読み、対応するセクションを単独で生成する。
メインエージェントは各サブエージェントの出力を集約して `feed.md` を組み立てる。

### source とセクション・出力ファイルの対応

| source 値 | セクション見出し | 出力ファイル |
|---|---|---|
| `github_trending` | `## GitHub Trending` | `raw/section_github_trending.md` |
| `hackernews` | `## Hacker News` | `raw/section_hackernews.md` |
| `reddit` | `## Reddit` | `raw/section_reddit.md` |
| `zenn` | `## Zenn` | `raw/section_zenn.md` |
| `qiita` | `## Qiita` | `raw/section_qiita.md` |

### per-source セクション生成ルール（サブエージェント）

- 入力は単一の `raw/<source>.json`。出力は `raw/section_<source>.md`（全体上書き）。
- 出力内容は `## <セクション見出し>` から始め、その下に各記事を
  「日本語見出し（`### ...`）」「要約」「一次ソース URL（単独行）」の順で並べる。
- 上記の「セクションルール」「要約ルール」を 1 ソース分に適用する
  （注目度の高いものを中心に 5〜8 件、URL は各項目末尾に単独行など）。
- 有用な項目が 1 件もない場合は、`## <セクション見出し>` の行だけを書くか空ファイルにし、
  メイン側で省略できるようにする。

### メインエージェントの組み立てルール

- 先頭に `# 技術ニュース要約 — YYYY-MM-DD`（当日の日付）を置く。
- セクション順は GitHub Trending → Hacker News → Reddit → Zenn → Qiita。
- 各 `raw/section_<source>.md` の内容をこの順に連結して `feed.md` を全体上書きする。
- 存在しない、空、または記事が 1 件もない `section_<source>.md` は省略する。
