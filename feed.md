# 技術ニュース要約 — 2026-10-27

## 📌 今日の3行サマリ

- 国内で不正アクセスの報道が相次いだ。楽天トラベルでは顧客情報約 260 万件（クレジットカード 3 万件を含む）が流出した可能性があり、Joshin では最大約 600 万件の会員情報が漏えいした可能性がある。GMO にはハッカー集団が 27 日を期限に 100 万ドルを要求していると NHK が報じ、ギフティでもギフト券が最大 5.5 億円分不正に発行された。
- 認証局 eMudhra の中間 CA 証明書をめぐる問題で、Zenn と Qiita の解説記事がよく読まれている。中間 CA の秘密鍵を求める検証や、コンテナや Python 環境が独自に持つ証明書の点検など、開発者が手元で確かめるべき点が整理されつつある。
- 圧縮形式 Brotli の脆弱性「HTTP2Shell」が Microsoft の製品にも影響し、.NET に定例外の更新が出た。Zenn と Qiita にも Node.js の脆弱性への対応記事が出ており、使っているランタイムやライブラリの更新を確かめたい。

## GitHub Trending

| # | タイトル | 要約 | URL |
|---|----------|------|-----|
| 1 | VoiceStudio — 手元で完結する、ElevenLabs の代わりの音声スタジオ — (原文: debpalash/VoiceStudio) | • 音声のクローン、声のデザイン、動画の吹き替え、口述入力、文字起こし、オーディオブック作りをまとめたオープンソースのツール。<br>• README では 646 言語に対応するとしている。<br>• 完全にローカルで動く「ElevenLabs の代替」をうたい、日本語の README も用意している。<br><br>音声生成をクラウドに頼らず手元で動かしたいという需要に応えるものだ。声のクローンは悪用のおそれもあるため、本人の同意など使い方のルールを決めてから使いたい。 | https://github.com/debpalash/VoiceStudio |
| 2 | Impeccable — AI コーディングエージェントのデザイン力を上げるスキル — (原文: pbakaus/impeccable) | • AI コーディングエージェント向けのデザインの指針で、1 つのスキルと 24 のコマンドからなる。<br>• ブラウザで見ながら直す仕組みと、AI が作ったフロントエンドを点検する 62 個の決定的な検出ルールを備える。<br>• `npx impeccable install` で入れ、エージェントの中で `/impeccable init` を実行して使う。<br><br>README は、Anthropic の frontend-design を「Claude 向けで最初に広く使われたデザインスキル」として挙げている。AI が作る画面の「AI っぽさ」を減らす道具が、続けて注目を集めている。 | https://github.com/pbakaus/impeccable |
| 3 | TradingAgents — 複数の LLM エージェントで金融取引をするフレームワーク — (原文: TauricResearch/TradingAgents) | • 複数の LLM エージェントで売買の判断をする金融取引向けのフレームワークで、論文を arXiv で公開している。<br>• 2026 年 10 月に v0.7.0 が出て、ChatGPT Plus や Pro の契約で動かせるようになった。<br>• バックテストは各判断の後の最初の終値から採点するようになり、リリースごとに wheel も添付される。<br><br>LLM で投資判断を試す研究用の枠組みとして関心を集めている。実際のお金で使う場合は、バックテストの成績が将来の成績を保証しないことに注意が要る。 | https://github.com/TauricResearch/TradingAgents |
| 4 | ThinkRail — JetBrains の軽量なエージェント型 IDE — (原文: JetBrains/thinkrail) | • JetBrains が公開した、コーディングエージェント「pi」を中心に組み立てた軽量な IDE。<br>• 作業ごとにワークスペースを分け、「生きた仕様（living specs）」と再利用できるスキルでプロジェクトの知識を保つ。<br>• 使うほどプロジェクトを学び、今後は自分の機能を自分で作れるようにすることを目指すとしている。<br><br>IDE の大手が、エージェントを中心に据えた新しい形の開発環境を試している。既存の IntelliJ 系の IDE とどう使い分けるのかが注目点になる。 | https://github.com/JetBrains/thinkrail |
| 5 | Coolify — 自分のサーバーで動かす、Vercel や Heroku の代わりの PaaS — (原文: coollabsio/coolify) | • Vercel、Heroku、Netlify の代わりとして使える、セルフホスト型のオープンソースの PaaS。<br>• 静的サイト、データベース、フルスタックのアプリのほか、360 以上のサービスをワンクリックで入れられる。<br>• オープンソースでずっと無料とうたい、クラウド版も案内している。<br><br>費用を抑えたい、データを手元に置きたいといった理由で、セルフホストの PaaS が見直されている。運用やバックアップは自分で担う必要がある点に注意したい。 | https://github.com/coollabsio/coolify |
| 6 | security-audit-skill — Cloudflare の、セキュリティ監査をするエージェント用スキル — (原文: cloudflare/security-audit-skill) | • コーディングエージェントをセキュリティの監査役にするスキルで、Cloudflare が公開した。<br>• 偵察、網羅的な探索、候補の検証、構造化した出力、記録の独立した検証、報告の段階を、分けたエージェントで進める。<br>• 見つけた問題は機械で読める形で出す。Cloudflare の脆弱性発見ハーネスの元になったスキルだという。<br><br>AI による脆弱性探しは誤検知が課題とされ、独立した検証の工程を組み込んでいる点が特徴だ。Zenn には、このスキルを個人開発のアプリで試した記事も出ている。 | https://github.com/cloudflare/security-audit-skill |
| 7 | Claude SEO — Claude Code 用の SEO スキル集 — (原文: AgriciDaniel/claude-seo) | • Claude Code の中で SEO の監査をする、無料のオープンソースのスキル。26 のサブスキルと 19 のサブエージェントからなる。<br>• 技術的な SEO、E-E-A-T、構造化データ、GEO/AEO、被リンク、ローカル SEO、EC、多言語の SEO などを扱う。<br>• llms.txt や WebMCP など AI エージェントからの見え方も点検でき、PDF や Excel で報告書を出せる。<br><br>検索エンジンだけでなく、AI 検索で引用されるかを気にする流れが SEO の分野に広がっている。Google の API とつなぐ機能もあるため、認証情報の扱いを確かめてから使いたい。 | https://github.com/AgriciDaniel/claude-seo |

## Hacker News

| # | タイトル | 要約 | URL |
|---|----------|------|-----|
| 1 | 誰かスパムの SMS を止めてほしい — (原文: Somebody please stop the spam texts) | • 個人のブログ notes.npilk.com で、スパムのテキストメッセージが止まらない現状を訴える記事とみられる。<br>• 92 ポイント、コメント 101 件で、今回取得分の中で最多。<br>• ポイントに対してコメントが多く、同じ悩みを抱える人が多いことがうかがえる。<br><br>SMS のスパムや詐欺のメッセージは、対策が追いついていない問題とされる。通信事業者や規制がどう対応すべきかは、本文とコメント欄の議論で確かめたい。 | https://notes.npilk.com/stop-the-spam-texts |
| 2 | Microsoft、従業員の 4 分の 1 に希望退職を提示 — (原文: Microsoft offers voluntary buyouts to a quarter of its workforce) | • シアトルの公共ラジオ KUOW が、Microsoft が従業員のおよそ 4 分の 1 に希望退職を提示したと報じた。<br>• 対象の部門や条件は、タイトルからはわからない。<br>• 26 ポイント、コメント 7 件。<br><br>大手 IT 企業では、人員の見直しが続いている。規模が大きいため、業界の雇用への影響が注目される。 | https://www.kuow.org/technology/2026-10-26/microsoft-offers-voluntary-buyouts-to-a-quarter-of-its-workforce |
| 3 | 画像生成は 2022 年 8 月からここまで進んだ — (原文: Image generation has come a long way since August 2022) | • 個人サイト hbrooks.com で、2022 年 8 月から今までの画像生成 AI の進歩を振り返る記事。<br>• 起点の 2022 年 8 月は、Stable Diffusion が公開されたころにあたる。<br>• 21 ポイント、コメント 3 件。<br><br>数年で画像生成の品質は大きく変わった。はてなでも、無料の画像生成 AI「Moss-Image」を試す記事が今日最も多くブックマークされている。 | https://www.hbrooks.com/writing/image-generation-has-come-a-long-way |
| 4 | 「グランド・セフト AI」— 高速道路でデータセンター機器が数百万ドル分盗まれる — (原文: Grand theft AI: Highway thieves are stealing millions in data center gear) | • NBC News が、輸送中のデータセンター機器を狙った盗難が起きていると報じた。<br>• タイトルによると、被害は数百万ドル分に上る。<br>• 21 ポイント。<br><br>AI 向けのサーバーや GPU は高値で取引されるため、輸送中に狙われやすいとみられる。サプライチェーンの物理的な守りも課題になりつつある。 | https://www.nbcnews.com/tech/security/grand-theft-ai-highway-thieves-are-stealing-millions-data-center-gear-rcna603733 |
| 5 | バッチファイルから実行すると動かないのに、クリックすると動くのはなぜか — (原文: Why a program doesn't work when run from a batch file, but works when clicked) | • Microsoft の開発者ブログ「The Old New Thing」の記事。<br>• バッチファイルから起動したときと、クリックで起動したときで、プログラムの動きが変わる理由を説明しているとみられる。<br>• 20 ポイント。<br><br>作業ディレクトリや環境変数など、起動のしかたで変わる条件はトラブルの元になりやすい。Windows の昔からの挙動を知る手がかりになる。 | https://devblogs.microsoft.com/oldnewthing/20261026-00/?p=112797/ |
| 6 | 英語以外の言語では AI モデルの利用料が高くなる — (原文: AI models cost more when you don't use English) | • Rest of World が、英語以外の言語で AI を使うと費用が高くなる問題を報じた。<br>• URL から、トークナイザーによる「税」と、それが生む不公平を扱った記事とみられる。<br>• 20 ポイント。<br><br>同じ内容でも、言語によってトークン数が変わることは以前から指摘されている。日本語で LLM を使う場合も、費用の見積もりは英語と分けて考えたい。 | https://restofworld.org/2026/ai-tokenizer-tax-non-english-languages-cost-inequity/ |
| 7 | セルフホストの Convex を拡張する: TypeScript の関数を WASM にコンパイル — (原文: Scaling self-hosted Convex: compilation of TypeScript Convex functions into WASM) | • バックエンドの Convex をセルフホストで使うとき、TypeScript で書いた関数を WebAssembly（WASM）にコンパイルする取り組みの記事。<br>• 規模を広げるための工夫として紹介しているとみられる。<br>• 20 ポイント。<br><br>WASM には、隔離した環境で動かせることや起動の速さといった利点がある。本番での効果は、記事の数字で確かめたい。 | https://convex-in-prod.github.io/posts/convex-wasm-compiler/ |
| 8 | warp.dev が侵害を受ける — (原文: warp.dev Breached) | • ターミナルアプリ Warp が侵害を受けたことを伝える、X（旧 Twitter）の投稿。<br>• アカウント名から、Warp の CEO である Zach Lloyd 氏の投稿とみられる。<br>• 12 ポイント、コメント 1 件。<br><br>開発者のターミナルは、認証情報や秘密鍵に触れやすい道具だ。Warp を使っている場合は、公式の発表で影響の範囲と取るべき対応を確かめたい。 | https://twitter.com/zachlloydtweets/status/2114800787716972873 |

## InfoQ Japan

| # | タイトル | 要約 | URL |
|---|----------|------|-----|
| 1 | CircleCI、AI コーディングの流れに CI の検証を組み込む「Chunk Sidecars」を導入 | • CircleCI が、AI コーディングのワークフローに CI の検証機能を直接組み込む「Chunk Sidecars」を導入した。<br>• AI が書いたコードを、作業の途中で CI と同じ検証にかけられるようにするものとみられる。<br>• 記事は Craig Risi 氏による。<br><br>AI エージェントが書くコードが増え、変更を早く確かめる仕組みが求められている。CI を後の工程ではなく作業のそばに置く流れの一例といえる。 | https://www.infoq.com/jp/news/2026/10/circleci-chunk-sidecars/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global |
| 2 | Google の Genkit、TypeScript と Go 向けに Agents API をリリース | • Google の AI アプリ開発フレームワーク Genkit が、TypeScript と Go 向けに Agents API を出した。<br>• 「Detached Turns」と「Human-in-the-Loop」という機能を備える。<br>• URL からは、プレビュー版とみられる。<br><br>人の確認をはさむ機能など、業務向けのエージェントに必要な部品がフレームワークにそろいつつある。Detached Turns の詳しい動きは記事で確かめたい。 | https://www.infoq.com/jp/news/2026/10/genkit-agents-api-preview/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global |
| 3 | Anthropic、Web 版・Claude Code・Cowork での Claude の封じ込め方を詳しく説明 | • Anthropic が、Claude をどう「封じ込め」ているかを詳しく説明した内容を、InfoQ が紹介した。<br>• 対象は Web 版の Claude、Claude Code、Cowork の 3 つ。<br>• エージェントが動ける範囲を制限する仕組みを扱っているとみられる。<br><br>エージェントがファイルやネットワークに触れる場面が増え、どこまで動かせるかの設計が大事になっている。自社でエージェントを動かすときの参考になりそうだ。 | https://www.infoq.com/jp/news/2026/10/anthropic-claude-containment/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global |
| 4 | AWS の請求システムの不具合で兆ドル規模の見積額が表示、コストアラームは作動せず | • AWS の請求システムの不具合で、顧客に兆ドル規模の見積額が表示された。<br>• 一方で、コストアラームは作動しなかったと伝えている。<br>• 記事は Steef-Jan Wiggers 氏による。<br><br>請求の見積もりの異常は、利用者を混乱させるだけでなく、監視の仕組みの盲点も示した。コストアラームだけに頼らず、請求の推移を別の方法でも確かめておきたい。 | https://www.infoq.com/jp/news/2026/10/aws-billing-estimates-incident/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global |

## はてなブックマーク (tech)

| # | タイトル | 要約 | URL |
|---|----------|------|-----|
| 1 | 無料の画像生成 AI「Moss-Image」を試す — 日本語や漫画も生成でき、商用利用もできる | • ASCII が、無料の画像生成 AI「Moss-Image」を試した記事。<br>• 日本語の文字や漫画も生成でき、商用利用もできるとしている。<br>• 311 ブックマークで、今回のはてな取得分で最多。<br><br>無料で商用利用できる画像生成モデルが増え、選べる幅が広がっている。商用で使う場合は、利用規約や生成物の権利の扱いを自分で確かめたい。 | https://ascii.jp/elem/000/004/445/4445534/ |
| 2 | 楽天トラベルに不正アクセス、顧客情報 260 万件が流出か | • 日本経済新聞が、楽天トラベルへの不正アクセスで顧客情報約 260 万件が流出した可能性があると報じた。<br>• クレジットカードの情報も 3 万件含まれるとしている。<br>• 133 ブックマーク。<br><br>旅行予約サイトには、氏名や連絡先、宿泊の予定など多くの個人情報が集まる。利用者はカードの明細を確かめ、不審な連絡に注意したい。 | https://www.nikkei.com/article/DGXZQOUC2686T0W6A021C2000000/ |
| 3 | pixiv の素早い PHP 更新を参考に、Docker Official Image のビルドの仕組みを社内で作った話 | • Classi の開発者ブログで、Docker Official Image を社内でビルドする仕組みを作った経緯を紹介。<br>• pixiv が PHP を素早く更新している取り組みを参考にしたという。<br>• タグには PHP、Ruby、セキュリティが並ぶ。132 ブックマーク。<br><br>公式イメージの更新を待たずに自分たちでビルドできれば、脆弱性への対応を早められる。一方で、ビルドの仕組みを保ち続ける手間は増える。 | https://tech.classi.jp/entry/2026/10/26/163000 |
| 4 | Joshin に不正アクセス、最大約 600 万件の会員情報が漏えいの可能性 | • 家電量販店の Joshin が不正アクセスを受け、最大約 600 万件の会員情報などが漏えいした可能性があると INTERNET Watch が報じた。<br>• NHK も同じ件を報じており、はてなでは両方の記事が読まれている。<br>• 128 ブックマーク（NHK の記事は 57）。<br><br>今回は国内の企業への不正アクセスの報道が特に多かった。会員登録しているサービスでは、パスワードの使い回しをやめ、不審なメールに注意したい。 | https://internet.watch.impress.co.jp/docs/news/2151273.html |
| 5 | GMO への不正アクセス — 「能動的サイバー防御」より先にやるべきこと | • 朝日新聞が、GMO への不正アクセスを受けて、「能動的サイバー防御」より先に取り組むべきことを論じた。<br>• NHK は、ハッカー集団が GMO に 27 日を期限として 100 万ドルを要求し、顧客も脅していると報じた。<br>• 116 ブックマーク（NHK の記事は 102）。<br><br>期限とされた 27 日は今日にあたる。国の積極的な対策の議論とは別に、企業の基本的な守りが問われている。 | https://www.asahi.com/articles/ASVBV1JK7VBVULZU002M.html |
| 6 | Apple、iPad mini に「史上最大」のアップデート | • Apple が日本のニュースルームで、iPad mini に史上最大のアップデートを行うと発表した。<br>• 具体的な変更点は、タイトルからはわからない。<br>• 103 ブックマーク。<br><br>小さなタブレットとして根強い人気がある製品の大きな更新だ。詳しい仕様と価格は発表で確かめたい。 | https://www.apple.com/jp/newsroom/2026/10/apple-gives-ipad-mini-its-biggest-update-ever/ |
| 7 | PSN に新たな脆弱性か — 二段階認証を回避してファミリーメンバーが勝手に追加される | • ゲーム Watch が、PlayStation Network（PSN）で新たな脆弱性が見つかった可能性を報じた。<br>• 二段階認証を回避して、ファミリーメンバーが勝手に追加される被害が起きているという。<br>• 67 ブックマーク。<br><br>ファミリーの機能は支払いや利用の制限にかかわるため、悪用されると影響が大きい。利用者はアカウントの設定や登録メンバーを確かめておきたい。 | https://game.watch.impress.co.jp/docs/news/2151226.html |
| 8 | Brotli の脆弱性「HTTP2Shell」、Microsoft 製品にも影響 — .NET に定例外の更新 | • 圧縮形式 Brotli の脆弱性「HTTP2Shell」が、Microsoft の製品にも影響すると窓の杜が報じた。<br>• .NET に定例外の更新が出たほか、Visual Studio と PowerShell でもセキュリティ更新が出た。<br>• 28 ブックマーク。<br><br>Brotli は Web の圧縮で広く使われているため、影響がさまざまなソフトに及ぶ。Zenn にも Node.js の Brotli 脆弱性を読み解く記事が出ており、使っている環境の更新を確かめたい。 | https://forest.watch.impress.co.jp/docs/news/2151104.html |

## Zenn

| # | タイトル | 要約 | URL |
|---|----------|------|-----|
| 1 | eMudhra の中間 CA 証明書の秘密鍵を求めてみる | • 認証局 eMudhra の中間 CA 証明書について、その秘密鍵を求めることを試みた記事。<br>• 筆者は herumi 氏。URL からは、弱い鍵を探す内容とみられる。<br>• 117 いいねで、今回の Zenn 取得分で最多。<br><br>中間 CA の秘密鍵が知られると、偽の証明書を作れてしまうため影響が大きい。eMudhra の件は Zenn と Qiita で複数の記事が読まれている。 | https://zenn.dev/herumi/articles/search_bad_emudhra_key |
| 2 | バイブコーディングを 6 週間続けたら、Mac の起動に 20 分かかるようになった | • AI に任せてコードを書く「バイブコーディング」を 6 週間続けたら、Mac の起動に 20 分かかるようになった体験談。<br>• 原因の調べ方や対処を書いているとみられる。<br>• 99 いいね。<br><br>AI に作業を任せると、何が入れられたり起動したりしたかを把握しにくくなりやすい。自動で起動する項目や常に動いているプロセスを、ときどき見直したい。 | https://zenn.dev/singularity/articles/vibe-coding-mac-boot-20min |
| 3 | 脆弱性管理の仕組みを整えた | • dress code の開発者ブログで、脆弱性管理の仕組みを整えた取り組みを紹介。<br>• 脆弱性を見つけてから対応するまでの流れを、組織として整えた経緯とみられる。<br>• 90 いいね。<br><br>今回は Brotli や Node.js、eMudhra など、すぐ対応が要る話題が多かった。日ごろから脆弱性を追う仕組みがあれば、こうした場面で素早く動ける。 | https://zenn.dev/dress_code/articles/be5550254695cd |
| 4 | Oxlint と Oxfmt で規約をコード化するモノレポ運用 | • REALITY の技術ブログで、Oxc のリンター Oxlint とフォーマッター Oxfmt を使ったモノレポの運用を紹介。<br>• チームの規約をルールとしてコードに落とし込む方法を扱う。<br>• 62 いいね。<br><br>ESLint や Prettier からの乗り換え先として、速さを売りにする Oxc 系のツールが注目されている。大きなモノレポでの使い勝手を知る材料になる。 | https://zenn.dev/reality_tech/articles/oxc-monorepo-20261006 |
| 5 | 600 人規模のイベント運営を支えたインカムを、学生 1 人で作った話 | • 600 人規模のイベントの運営で使うインカム（業務用の通話の仕組み）を、学生が 1 人で作った経緯。<br>• 自作の通話の仕組みを、実際の現場で使った記録とみられる。<br>• 47 いいね。<br><br>市販の機材の代わりに、手持ちの端末とソフトで現場の道具を作る例といえる。本番の現場で使うまでの工夫が読みどころになりそうだ。 | https://zenn.dev/kodak_20/articles/3b0ba74333b56c |
| 6 | AI の謎な説明文を直すスキル | • Microsoft のメンバーによる Zenn の記事で、AI が書くわかりにくい説明文を直すスキルを紹介。<br>• URL の「explain-before-shorten」から、短くする前にまず説明を補うという考え方とみられる。<br>• 41 いいね。はてなブックマークでも 93 件を集めた。<br><br>AI の書く文章は、短くまとめすぎて意味が伝わらないことがある。文章の質をスキルとして整える試みは、ほかのチームでも応用できそうだ。 | https://zenn.dev/microsoft/articles/explain-before-shorten |
| 7 | AI が実装してくれる時代こそ、自分の手で実装しよう | • ログラスのメンバーによる、AI に実装を任せられる時代だからこそ自分の手で書くことを勧める記事。<br>• 考え方を述べるアイデア記事として投稿されている。<br>• 41 いいね。<br><br>AI に任せるほど、自分で書いて身につける機会は減りやすい。学び方と仕事の進め方をどう分けるかが、多くの開発者の関心事になっている。 | https://zenn.dev/loglass/articles/24b2a4776ce8d4 |
| 8 | 「読みにくい DB」は AI 開発のコストを 1.9 倍にする — Claude Code で検証 | • Claude Code を使って、DB 設計のわかりやすさが AI 開発のコストにどう影響するかを検証した記事。<br>• 読みにくい DB では、コストが 1.9 倍になったとしている。<br>• 27 いいね。<br><br>AI はテーブル名や列名から意味を読み取るため、命名や構造のわかりやすさが結果に効く。人にとって読みやすい設計は、AI にとっても扱いやすいといえる。 | https://zenn.dev/actbe_tech/articles/8b4a9991d5365d |

## Qiita

| # | タイトル | 要約 | URL |
|---|----------|------|-----|
| 1 | 3KB しか使えない！奇妙で素敵なゲームエンジン「Playload」の紹介 | • 3KB しか使えないという制約のあるゲームエンジン「Playload」を紹介する記事。<br>• 筆者は Pyxel の作者の kitao 氏で、タグには JavaScript と Pyxel が並ぶ。<br>• 87 いいねで、今回の Qiita 取得分で最多。<br><br>強い制約の中でゲームを作る遊びは、昔からプログラマーに人気がある。小さく作る工夫を学ぶ題材にもなりそうだ。 | https://qiita.com/kitao/items/7fac93e8a7ad6015b0b0 |
| 2 | eMudhra 事件で Web アプリ開発者が点検すべきこと | • 認証局 eMudhra をめぐる事件を受けて、Web アプリの開発者が点検すべきことをまとめた記事。<br>• タグには証明書、暗号技術、HTTPS が並ぶ。<br>• 83 いいね。<br><br>Zenn では、OS やブラウザが最新でも、コンテナや Python 環境が独自に持つ証明書が偽の証明書を信じていたという報告も出ている。自分の環境の証明書の置き場所を確かめておきたい。 | https://qiita.com/autotaker1984/items/ef99b5791fe799a4ca66 |
| 3 | VS Code 1.142 に Canvas — チャットの横でエージェントと同じ画面を触れる「Interactive Canvases」 | • VS Code 1.142 で、「Interactive Canvases」という機能が入ったことを整理した記事。<br>• チャットの横で、エージェントと同じ画面を人も操作できるという。<br>• 38 いいね。タグには GitHub Copilot が並ぶ。<br><br>エージェントとの作業を、文字のやり取りだけでなく画面の共有で進める流れが広がっている。どこまで実用になるかは、使い込んだ人の評価を待ちたい。 | https://qiita.com/shahin0809/items/81e6a6737b2254bdc6ed |
| 4 | Node.js の重大な脆弱性に対応するセキュリティ更新を安全に当てる方法 | • Node.js の重大な脆弱性に対応するため、セキュリティ更新を安全に当てる手順をまとめた記事。<br>• 初心者向けのタグが付いており、npm を使う環境を想定しているとみられる。<br>• 30 いいね。<br><br>ランタイムの更新は、依存するパッケージの動きを変えることがある。テストを回してから本番に入れる手順を決めておくと、急ぎの対応でも慌てずに済む。 | https://qiita.com/superdora-cloud/items/8cad27487cd0e67d088c |
| 5 | トークン代 9 割減？ プロンプトキャッシュの仕組みと効果の実測 — 保持時間が過ぎるとコスト 11 倍に | • プロンプトキャッシュの仕組みと、トークン代がどれだけ減るかを実測した記事。<br>• うまく使えばトークン代が 9 割減る一方、保持時間が過ぎるとコストが 11 倍になる場合があるとしている。<br>• 12 いいね。タグには Claude と OpenAI が並ぶ。<br><br>キャッシュは保持時間を前提にした仕組みのため、呼び出しの間隔によって効果が大きく変わる。自分の使い方に合うかを数字で確かめるのが大事だ。 | https://qiita.com/songchong/items/7144594b0ad9529a168b |
| 6 | 【書評】『プロフェッショナル AI 駆動開発』を読んだ | • 書籍『プロフェッショナル AI 駆動開発』の書評。<br>• タグには AI 駆動開発、AI エージェント、バイブコーディングが並ぶ。<br>• 10 いいね。<br><br>AI を使った開発のやり方を、本として体系的にまとめる動きが出てきた。書評を手がかりに、自分のチームに合う部分を探すとよさそうだ。 | https://qiita.com/tetsuro731/items/c673cf947c3724cd5493 |
| 7 | 実際に試した Claude の便利な使い方 20 選 | • 筆者が実際に試した Claude の便利な使い方を 20 個まとめた記事。<br>• タグには Claude Code、Terraform、AWS が並び、インフラの作業での使い方も含むとみられる。<br>• 8 いいね。<br><br>使い方のまとめ記事は、自分では気づかなかった使い道を知るきっかけになる。インフラを触らせる場合は、権限の範囲に気をつけたい。 | https://qiita.com/N-Kyo/items/bf4a3a2185db2d28eee5 |
| 8 | 「PHP2Shell」の緊急対策 — 日本国内向けサイトで海外 IP を全部弾く | • 「PHP2Shell」への緊急の対策として、日本国内向けのサイトで海外の IP アドレスからの接続をすべて弾く方法を紹介。<br>• nftables や iptables を使い、WordPress のサイトも想定している。<br>• 8 いいね。<br><br>IP で弾く方法はすぐ効く一方、国内からの攻撃や VPN 経由の接続は防げない。あくまで時間を稼ぐ手段として、本来の修正と組み合わせたい。 | https://qiita.com/Hiro884/items/27a98c86ef17b70df7ed |
