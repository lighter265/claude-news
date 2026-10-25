# 技術ニュース要約 — 2026-10-26

## 📌 今日の3行サマリ

- Moderna と Merck の mRNA がんワクチンが、メラノーマの患者で死亡と再発のリスクを 42% 下げたと Ars Technica が報じた。Hacker News では 95 ポイントで、今回取得分の中で最多だった。
- 盗んだ GitHub のトークンを使ってリポジトリに秘密情報を抜き出すワークフローを仕込む攻撃「Gheist」を、Wiz が報告した。GitHub CLI の短命トークンや、devcontainer で GH_TOKEN を守る工夫など、トークンの扱いを見直す記事も目立った。
- LLM の利用料を抑える話題が続いている。Hacker News には「OpenAI と Anthropic が数か月で LLM の価格を最大 80% 下げた理由」を考える記事が投稿された。Qiita では、プロンプトキャッシュや資料の渡し方を工夫してトークン代を減らす実測の記事が読まれている。

## GitHub Trending

| # | タイトル | 要約 | URL |
|---|----------|------|-----|
| 1 | Gemini CLI — ターミナルで Gemini を使うオープンソースの AI エージェント — (原文: google-gemini/gemini-cli) | • Google が公開している、ターミナルから Gemini を使えるオープンソースの AI エージェント。<br>• README によると、無料枠と Google One の利用者向けには、2026 年 6 月 18 日に Antigravity CLI へ切り替わった。<br>• Gemini CLI は最新の Gemini モデル（Gemini 4 Argon など）向けには最適化されておらず、それらには Antigravity CLI を使うよう案内している。<br><br>Google のコーディング用 CLI は、Antigravity CLI へ移りつつあるようだ。Gemini CLI を使い続けている場合は、自分の契約の形でどちらを使うべきかを確かめたい。 | https://github.com/google-gemini/gemini-cli |
| 2 | Cindy — 入れてすぐ使えるオープンソースの AI エージェント — (原文: makecindy/cindy) | • 「入れてすぐ使える」ことをうたう、オープンソースの AI エージェント。英語と中国語で案内している。<br>• 複数のハーネス、モデル、ツールを 1 つのエージェントにまとめ、プロジェクトやアプリの実際の作業を終わらせることを目指す。<br>• 手元のマシンで動き、自分のファイルやログイン済みのアプリをそのまま使う。最初に対応するハーネスには Claude Code などが含まれるとみられる。<br><br>既存のコーディングエージェントを束ねて使う道具が増えている。手元のファイルやログイン中のアプリに触れるため、どこまで権限を渡すかを決めてから使いたい。 | https://github.com/makecindy/cindy |
| 3 | Agent Toolkit for AWS — AI エージェント向けの AWS 公式ツール群 — (原文: aws/agent-toolkit-for-aws) | • AWS が公式に支える、AI エージェント向けの MCP サーバー、スキル、プラグインの集まり。<br>• AI のコーディングエージェントが AWS 上でアプリを作り、デプロイし、管理するための道具、知識、ガードレールを与える。<br>• Claude Code、Codex、Cursor、Devin、Kiro などに対応し、AWS CLI からも使える。<br><br>クラウドの大手が、エージェント向けの公式の入り口を整える流れが続いている。本番の環境に触らせる場合は、ガードレールの範囲と権限の設定を確かめる必要がある。 | https://github.com/aws/agent-toolkit-for-aws |
| 4 | Microduck — 強化学習で歩く小さなアヒル型の二足ロボット — (原文: pollen-robotics/microduck) | • Pollen Robotics の、高さ約 25 cm、重さ 800 g の小さな二足歩行ロボット。<br>• 強化学習で作った方策で動き、Rockchip RK3566 の上で 50 Hz の制御ループが 15 個のサーボを動かす。<br>• このリポジトリはロボットの「頭脳」にあたるソフトで、無線やカメラ、ソフトの更新の仕組みも含む。<br><br>学習した方策で実機を動かす試みが、小さく手ごろなロボットでもできるようになってきた。研究や教育の題材として使いやすそうだ。 | https://github.com/pollen-robotics/microduck |
| 5 | Hallmark — AI が作ったように見えないデザインにするスキル — (原文: Nutlope/hallmark) | • Claude Code、Codex、Cursor、OpenCode で使える、デザイン用のスキル。Together AI が作った。<br>• 48 種類の素材のカタログから 3 つのテーマを選び、訪問者の目的に合わせてページを組み立てる。<br>• できあがった結果を lint で点検し、「AI っぽい」見た目になるのを避けることを狙う。<br><br>AI が作る画面が似通いやすいという不満から、こうしたデザイン用のスキルが増えている。見た目の質をどこまで自動で保てるかが、今後の注目点になる。 | https://github.com/Nutlope/hallmark |
| 6 | 電子書籍ダウンロードの宝庫 — 電子書籍のダウンロードリンク集 — (原文: jbiaojerry/ebook-treasure-chest) | • 中国の読書アプリなどにある電子書籍のダウンロードリンクを集め、タグで分けたリポジトリ。<br>• 各書籍に epub、mobi、azw3 の 3 形式があると説明している。<br>• GitHub Pages で、複数のキーワードで探せる検索ページも用意している。<br><br>リンク先の書籍が正しく許諾されたものかは、README からは確かめられない。著作権の扱いがはっきりしないものを使わないよう注意が要る。 | https://github.com/jbiaojerry/ebook-treasure-chest |

## Hacker News

| # | タイトル | 要約 | URL |
|---|----------|------|-----|
| 1 | Moderna と Merck の mRNA がんワクチン、死亡と再発を 42% 減らしたと発表 — (原文: Moderna and Merck say their mRNA cancer vaccine cut death, recurrence by 42%) | • Moderna と Merck が、患者ごとに作る mRNA がんワクチンで、死亡と再発のリスクが 42% 下がったと発表したと Ars Technica が報じた。<br>• URL から、対象はメラノーマ（悪性黒色腫）とみられる。<br>• 95 ポイント、コメント 15 件で、今回取得分の中で最多。<br><br>患者ごとに作る mRNA ワクチンは、がん治療の新しい手法として期待されている。対象の範囲や副作用、承認までの道のりは、元の記事や発表で確かめたい。 | https://arstechnica.com/health/2026/10/personalized-mrna-cancer-vaccine-cut-melanoma-death-recurrence-by-42/ |
| 2 | 私がプログラマーである理由 — (原文: Why I Am a Programmer) | • 個人のブログで、筆者がプログラマーであることの理由をつづったエッセイとみられる。<br>• 個人ブログ alfie.wtf のプログラミングのカテゴリーに載った記事。<br>• 42 ポイント、コメント 6 件。<br><br>プログラミングの仕事の意味を問い直す文章は、最近 HN で関心を集めやすい。具体的な主張は本文で確かめたい。 | https://www.alfie.wtf/programming/why-i-am-a-programmer.html |
| 3 | 「Eunice」がもうすぐ登場 — (原文: Eunice is almost here) | • armincat.com に掲載された、「Eunice」という名前の何かがもうすぐ公開されることを伝える記事。<br>• タイトルからは、製品やプロジェクトの予告とみられるが、中身はわからない。<br>• 34 ポイント、コメント 28 件で、点数に比べてコメントが多い。<br><br>コメントの多さから、話題を呼ぶ内容とみられる。何が公開されるのかは、記事を読んで確かめる必要がある。 | https://armincat.com/articles/eunice-is-almost-here |
| 4 | 攻撃キャンペーン「Gheist」、盗んだ GitHub トークンで秘密情報を抜き出すワークフローを仕込む — (原文: Gheist campaign plants secret-dumping workflows using stolen GitHub tokens) | • Wiz が、盗まれた GitHub のトークンを使う攻撃キャンペーン「Gheist」を報告した。<br>• リポジトリに、秘密情報を外へ出すワークフローを仕込む手口とみられる。<br>• URL からは、大規模に悪用しようとして、うまくいかなかった面もあったと読める。26 ポイント。<br><br>CI のワークフローは、権限の強い秘密情報にふれやすい。長く使えるトークンを減らし、ワークフローの変更を見張ることが対策になる。 | https://www.wiz.io/blog/gheist-attempted-scaled-abuse-of-stolen-github-tokens-stumbles |
| 5 | アニメーション映画はどう作られるのか — (原文: What goes into making an animated film?) | • ディズニー・アニメーション・スタジオが、映画を作る工程を紹介するページ。<br>• 企画から完成までの流れを、工程ごとに説明しているとみられる。<br>• 16 ポイント、コメント 6 件。<br><br>CG のアニメーションは、多くの専門の工程とソフトの組み合わせで作られている。技術者にとっても、大きな制作の流れを知る材料になる。 | https://www.disneyanimation.com/process/ |
| 6 | Show HN: CaseCite — 弁護士向けの無料の RAG 判例調査・文書分析ツール — (原文: Show HN: CaseCite – Free RAG caselaw research and document analysis for lawyers) | • 弁護士向けに、判例の調査や文書の分析をする無料のツール。<br>• 検索と生成を組み合わせる RAG の仕組みを使い、GitHub でソースを公開している。<br>• 14 ポイント、コメント 2 件。<br><br>法律の分野では、AI がありもしない判例を示す問題が知られている。出典をたどれる RAG は、その対策の 1 つとして関心を集めている。 | https://github.com/thomasunise/casecite |
| 7 | OpenAI と Anthropic が数か月で LLM の価格を最大 80% 下げた理由 — (原文: OpenAI and Anthropic cut their LLM prices by up to 80% within a few months. Why?) | • minimaxir のブログで、OpenAI と Anthropic が短い期間に LLM の価格を大きく下げた理由を考えた記事。<br>• タイトルから、値下げは最大 80% に及ぶとしている。<br>• 3 ポイント、コメント 0 件。<br><br>価格が下がると、LLM を組み込んだ製品の費用の見積もりも変わる。値下げの背景に何があるのかは、記事の分析で確かめたい。 | https://minimaxir.com/2026/10/cheap-llms/ |
| 8 | .NET の 2026 年 10 月の定例外セキュリティ更新 — (原文: .NET October 2026 Out-of-Band Security Updates) | • Microsoft が、.NET のセキュリティ更新を、定例の日とは別に出したと公式ブログで案内した。<br>• 定例外で出すことから、急いで直すべき脆弱性への対応とみられる。<br>• 3 ポイント、コメント 0 件。<br><br>今月は Node.js や PHP でも急ぎのセキュリティ更新が続いた。.NET を使っている場合は、対象のバージョンを確かめて早めに更新したい。 | https://devblogs.microsoft.com/dotnet/dotnet-october-2026-oob-security-updates/ |

## はてなブックマーク (tech)

| # | タイトル | 要約 | URL |
|---|----------|------|-----|
| 1 | みんなはどのダークパターン広告が好き？ | • ブロガーの orangestar2 氏が、ダークパターンの広告について書いた記事。<br>• 利用者をだまして押させるような広告の例を取り上げているとみられる。<br>• 51 ブックマークで、今回取得分の中で最多。<br><br>ダークパターンは、利用者の信頼を損ねるとして、規制の議論も進んでいる。どこからが問題なのかを考えるきっかけになる。 | https://orangestar2.hatenadiary.com/entry/2026/10/23/163042 |
| 2 | iPod 25 周年 — Apple Music | • Apple Music に、iPod の 25 周年を記念するページが公開された。<br>• タグには Apple、iPod、music が付いている。<br>• 47 ブックマーク。<br><br>iPod は、音楽を持ち歩く習慣を大きく変えた製品だ。25 年の歩みを振り返る企画として関心を集めている。 | https://music.apple.com/jp/ipod |
| 3 | 社内 SE が AI でやらかして、職場が大混乱に陥った | • 社内 SE が AI を使って失敗し、職場が大混乱になったという匿名ダイアリーの投稿。<br>• 具体的に何が起きたのかは、本文で語られているとみられる。<br>• 28 ブックマーク。<br><br>AI を業務で使う場面が広がるにつれ、確認をせずに動かして起きる事故の話も増えている。権限やレビューの仕組みを考える材料になる。 | https://anond.hatelabo.jp/20261024120028 |
| 4 | C 言語を置き換える言語はどうあるべきか | • C 言語の代わりになる言語に何が求められるかを考えた、個人ブログの記事。<br>• タグにはコンピュータが付いている。<br>• 25 ブックマーク。<br><br>メモリの安全性の問題から、C の代わりを探す動きが続いている。Rust や Zig などが知られるなか、何を求めるべきかを整理する材料になる。 | https://blog.miz-ar.info/2026/10/replacing-c-language/ |
| 5 | Ruby で、任意のユーザー入力を渡してはいけないメソッド | • Ruby で、利用者の入力をそのまま渡すと危ないメソッドをまとめた、@znz 氏のブログ記事。<br>• 任意のコードの実行などにつながるメソッドを挙げているとみられる。<br>• 19 ブックマーク。<br><br>入力をそのまま渡す書き方は、脆弱性の原因になりやすい。AI が書いたコードを見直すときの確認項目としても役立ちそうだ。 | https://blog.n-z.jp/blog/2026-10-09-ruby-insecure-methods.html |
| 6 | 顔写真だけでがん患者の余命を診断できる AI モデル、米研究チームが開発 | • 米国の研究チームが、顔写真だけからがん患者の余命を推定する AI モデルを作ったと CNN が報じた。<br>• 顔の見た目から、体の状態を読み取る試みとみられる。<br>• 19 ブックマーク。<br><br>医療の判断を助ける可能性がある一方で、精度や偏り、写真の扱いには慎重な検証が要る。実際の診療で使うまでには課題が多い。 | https://www.cnn.co.jp/fringe/35253896.html |
| 7 | 人間が時間を使うべきところはどこか | • AI が多くの作業をこなす時代に、人が時間を使うべきところを考えた記事。<br>• タグには ai が付いている。<br>• 18 ブックマーク。<br><br>AI に任せる範囲が広がるほど、人が判断すべきところを見極めることが大事になる。働き方を考えるヒントになる。 | https://tellme.tokyo/post/2026/10/24/where-humans-spend-time/ |
| 8 | GitHub CLI が短命トークンに対応しても ghtkn が必要な理由 | • GitHub CLI が短い期限のトークンに対応したあとも、ghtkn を使う理由を説明した Zenn の記事。<br>• 筆者は ghtkn の作者の suzuki-shunsuke 氏とみられ、2 つを比べている。<br>• 18 ブックマーク。<br><br>トークンが盗まれたときの被害を減らすには、期限を短くすることが効く。GitHub トークンを狙う攻撃も報じられており、手元のトークンの扱いを見直す材料になる。 | https://zenn.dev/shunsuke_suzuki/articles/ghtkn-advantage-over-gh-cli-expiring-token |

## Zenn

| # | タイトル | 要約 | URL |
|---|----------|------|-----|
| 1 | prpr — Rust 向けのシンプルで速いパーサージェネレーター | • Rust 向けのパーサージェネレーター「prpr」を紹介する記事。<br>• URL から、packrat パーサーの方式をとるとみられる。筆者は tanakh 氏。<br>• 40 いいね。<br><br>パーサーを手で書くのは手間がかかるため、簡単で速い生成器は言語処理系や設定ファイルの読み込みに役立つ。既存のライブラリとの違いは記事で確かめたい。 | https://zenn.dev/tanakh/articles/prpr-packrat-parser |
| 2 | AI が実装してくれる時代こそ、自分の手で実装しよう | • AI が実装を代わりにしてくれる時代だからこそ、自分の手で書くことを勧める記事。<br>• ログラスの記事で、考えをまとめた「idea」に分類されている。<br>• 30 いいね。<br><br>AI に任せきりにすると、コードを読む力や設計の判断力が育ちにくいという声がある。学び方を考えるうえで参考になる。 | https://zenn.dev/loglass/articles/24b2a4776ce8d4 |
| 3 | コードレビューをなくして見えたもの | • チームでコードレビューをやめてみた経験をまとめた記事。<br>• レビューをなくしたことで見えた良い点や課題を扱っているとみられる。<br>• 25 いいね。<br><br>AI がコードを書く量が増え、人のレビューが追いつかないという悩みが広がっている。レビューのやり方そのものを見直す例として参考になる。 | https://zenn.dev/henteko/articles/b76b15922cdf72 |
| 4 | 600 人規模のイベントを支えたインカムを、学生 1 人で作った話 | • 600 人規模のイベントの運営で使ったインカムを、学生が 1 人で作った記事。<br>• 作ったシステムの仕組みや、本番で使った経験を書いているとみられる。<br>• 16 いいね。<br><br>市販の機器の代わりに自分で作ると、費用を抑えたり、必要な機能に絞ったりできる。本番で使えるところまで仕上げた例として参考になる。 | https://zenn.dev/kodak_20/articles/3b0ba74333b56c |
| 5 | Vue Fes Japan 2026 に参加してきた | • Vue Fes Japan 2026 に参加した感想をまとめた記事。<br>• 聞いた発表の内容や、会場の様子を紹介しているとみられる。<br>• 15 いいね。<br><br>前日のはてなでも Vue Fes の発表資料が多く読まれており、関心の高いイベントだったようだ。参加できなかった人が全体の流れをつかむのに役立つ。 | https://zenn.dev/krz_tech/articles/vuefes_japan_2026 |
| 6 | Xcode 27 で @State がマクロになった理由 | • Xcode 27 で、SwiftUI の @State がマクロになった理由を説明した記事。<br>• 遅延評価が使えるのは private のときだけ、という点や、@StateObject との違いを扱っている。<br>• 5 いいね。<br><br>よく使う機能の仕組みが変わると、思わぬところで動きが変わることがある。移行の前に、違いを押さえておきたい。 | https://zenn.dev/takehito/articles/50145459523321 |
| 7 | 2026 年の国内の情報漏えい 71 件を侵入経路で分類してみた | • 2026 年に国内で起きた情報漏えい 71 件を、侵入の経路ごとに分けた記事。<br>• どの経路からの被害が多いかを整理しているとみられる。<br>• 4 いいね。<br><br>侵入の経路の傾向がわかると、どこから守りを固めるべきかを決めやすくなる。自社の対策の優先順位を考える材料になる。 | https://zenn.dev/blackleg/articles/e9ed8b038bcf48 |
| 8 | Claude Code に gh を使わせても、GH_TOKEN をコンテナの環境変数に置かない devcontainer の構成 | • Claude Code に GitHub CLI（gh）を使わせつつ、GH_TOKEN をコンテナの環境変数に置かない構成を紹介した記事。<br>• URL から、gh をラッパーで包んでトークンを渡す方法とみられる。<br>• 3 いいね。<br><br>環境変数に置いたトークンは、エージェントやほかのプロセスから読まれるおそれがある。エージェントに渡す秘密情報を減らす工夫として参考になる。 | https://zenn.dev/hii_chi/articles/claude-code-gh-token-wrapper |

## Qiita

| # | タイトル | 要約 | URL |
|---|----------|------|-----|
| 1 | eMudhra 事件で、Web アプリの開発者が点検すべきこと | • 認証局 eMudhra をめぐる問題を受けて、Web アプリの開発者が確かめるべき点をまとめた記事。<br>• タグには証明書、暗号技術、HTTPS が付いている。<br>• 40 いいねで、今回取得分の中で最多。<br><br>Zenn では、eMudhra の中間 CA 証明書の秘密鍵を求めてみる記事も読まれている。自分のサービスが関係する証明書を使っていないか、確かめておきたい。 | https://qiita.com/autotaker1984/items/ef99b5791fe799a4ca66 |
| 2 | AI に資料を毎回貼らない：ファイル、SKILL、AGENTS.md の活用でトークン代を最大 6 割減らす 6 つの方法を試した | • AI に毎回資料を貼りつける代わりに、ファイル、SKILL、AGENTS.md などを使う 6 つの方法を試した記事。<br>• トークンの課金を最大 6 割減らせるかを確かめている。<br>• 13 いいね。<br><br>同じ資料を何度も送ると、そのたびに費用がかかる。資料の渡し方を工夫するだけで費用を抑えられる可能性がある。 | https://qiita.com/songchong/items/235bed0f8c72f268477e |
| 3 | トークン代 9 割減？ プロンプトキャッシュの仕組みと効果を実測、保持時間を過ぎると費用は 11 倍に | • プロンプトキャッシュの仕組みと、トークン代がどれだけ減るかを測った記事。<br>• キャッシュの保持時間が過ぎると、費用が 11 倍になるという結果を示している。<br>• 2 と同じ筆者で、6 いいね。<br><br>キャッシュが効いているかどうかで、費用は大きく変わる。長い作業では、保持時間を意識して使うと費用を抑えやすい。 | https://qiita.com/songchong/items/7144594b0ad9529a168b |
| 4 | 書評：『プロフェッショナル AI 駆動開発』を読んだ | • 『プロフェッショナル AI 駆動開発』という本の書評。<br>• タグには AI 駆動開発、AI エージェント、VibeCoding が付いている。<br>• 7 いいね。<br><br>AI を使った開発の進め方をまとめた本が増えている。読む前に、どんな内容かをつかむのに役立つ。 | https://qiita.com/tetsuro731/items/c673cf947c3724cd5493 |
| 5 | PHP の緊急メンテナンスで見えた、トップダウンの判断と AI 時代の脆弱性対応 | • PHP の緊急メンテナンスにあたり、「高市さんが言っていたから」と顧客に説明できたことを取り上げた記事。<br>• 上からの判断で対応が進んだことと、AI 時代の脆弱性対応について考えている。<br>• 6 いいね。<br><br>脆弱性への対応は、顧客や上司の理解がないと後回しにされやすい。社会の関心が高いと対応を進めやすいという、現場の視点が読み取れる。 | https://qiita.com/shinkai_/items/a45455b514bf9d32275a |
| 6 | Anthropic 公式の「データアナリスト用スキル」を読み、分析の進め方を 5 段階に整理 | • Anthropic が公開した、データ分析向けのスキルを読み解いた記事。<br>• 分析の進め方を 5 つの段階に整理している。<br>• 5 いいね。<br><br>公式のスキルには、AI に仕事を進めさせる手順が書かれている。人がデータ分析を学ぶ手引きとしても使えそうだ。 | https://qiita.com/ktdatascience/items/8f1756519016c6f64ea0 |
| 7 | PHP2Shell の確認ツール | • PHP2Shell の影響を受けるかどうかを確かめるツールを紹介した記事。<br>• タグには PHP、php2shell、Security が付いている。<br>• 4 いいね。<br><br>PHP2Shell への対応は、今週も続いている。自分のサーバーが対象かを手早く確かめる手段として役立ちそうだ。 | https://qiita.com/hokutoh/items/2beff120afb168bdec1c |
