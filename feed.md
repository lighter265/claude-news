# 技術ニュース要約 — 2026-07-15

## GitHub Trending

| # | タイトル | 要約 | URL |
|---|----------|------|-----|
| 1 | オープンソースの動画編集ソフト「OpenCut」が全面リライト中 | CapCut の代替を目指す無料・オープンソースの動画エディタ。Web・デスクトップ・モバイルを 1 つのコードベースから提供する方針で、現在は Rust コアを中心にゼロから作り直しが進んでいる。編集用 API、サードパーティ製プラグイン、AI エージェント向けの MCP サーバー、自動化やバッチレンダリング用のヘッドレスモード、エディタ内スクリプトタブなどが今後の予定として挙げられている。 | https://github.com/OpenCut-app/OpenCut |
| 2 | 実際に動かせる 100 種類超の AI エージェント／RAG アプリ集「awesome-llm-apps」 | クローンしてカスタマイズし、そのまま動かせる AI エージェントと RAG アプリを 100 以上集めたリポジトリ。AI エージェント、常駐エージェント、マルチエージェント構成、MCP エージェント、音声エージェント、ファインチューニングなど幅広い題材を扱う。Claude・Gemini・OpenAI・xAI・Qwen・Llama など複数モデルに対応し、ステップバイステップのチュートリアルも用意されている。 | https://github.com/Shubhamsaboo/awesome-llm-apps |
| 3 | 仕様駆動開発を始めるためのツールキット「Spec Kit」 | いわゆる「vibe coding」で場当たり的に書くのではなく、製品シナリオと予測可能な成果に集中するための仕様駆動開発（Spec-Driven Development）を支援するオープンソースツールキット。Specify CLI を中心に、拡張やプリセット、役割別のバンドル設定などを備える。複数の AI コーディングエージェントとの統合に対応している。 | https://github.com/github/spec-kit |
| 4 | AI らしさを排除するデザインスキル「Hallmark」 | Claude Code・Cursor・Codex 向けに、生成物が「いかにも AI 製」に見えないことを狙ったデザインスキル。ブリーフに応じてマクロ構造を選び、20 種類のテーマのいずれかを適用し、57 個の「slop テスト」ゲートと出力前の自己批評を通すことで、LLM が学習しがちな定番デザインを避けるという。Together AI が公開している。 | https://github.com/Nutlope/hallmark |
| 5 | コードや資料をクエリ可能な知識グラフに変える「graphify」 | Claude Code・Codex・Cursor・Gemini CLI などのコーディングエージェント向けスキル。コード、SQL スキーマ、R やシェルスクリプト、ドキュメント、論文、画像、動画などを含むフォルダを、まとめて問い合わせできる知識グラフに変換する。アプリのコード・データベーススキーマ・インフラを 1 つのグラフ上で扱えることを特徴として掲げている。 | https://github.com/Graphify-Labs/graphify |
| 6 | Windows を軽量化する PowerShell スクリプト「Win11Debloat」 | プリインストールアプリの削除やテレメトリの無効化など、Windows の整理・カスタマイズを手軽に行える軽量な PowerShell スクリプト。Windows 10 と Windows 11 の両方で動作し、インストール不要で利用できる。デフォルト状態の煩雑さを減らしたいユーザーを対象としている。 | https://github.com/Raphire/Win11Debloat |
| 7 | 自己ホスト型の AI コンパニオン「AIRI」 | 自分で所有・運用できるセルフホスト型の AI キャラクター（バーチャルキャラクター）コンテナ。Neuro-sama から着想を得ており、リアルタイム音声チャットに加え、Minecraft や Factorio のプレイにも対応するとしている。Web・macOS・Windows で動作する。 | https://github.com/moeru-ai/airi |

## Hacker News

| # | タイトル | 要約 | URL |
|---|----------|------|-----|
| 1 | StubHub の「ファンのためのマーケット」運営者が大規模転売業者だと SEC 提出書類で判明 | チケット再販プラットフォーム StubHub を「ファンのためのマーケットプレイス」と位置づける一方で、その運営に大規模なスキャルパー（転売業者）が関与していることが、SEC への提出書類から明らかになったと報じる記事。集団訴訟にも触れており、プラットフォームの建前と実態の乖離が論点となっている。 | https://www.cbc.ca/news/world/stubhub-ceo-class-action-scalping-9.7268987 |
| 2 | 掲示板サイト Lobste.rs が SQLite で稼働するように | 技術系リンク共有コミュニティ Lobste.rs が、データベースを SQLite に移行して運用していることを報告する投稿。大規模な RDBMS ではなく SQLite でも十分にサービスを支えられるという実例として、コミュニティで話題になっている。 | https://lobste.rs/s/ko1ji1/lobste_rs_is_now_running_on_sqlite |
| 3 | Apple が可観測性スタートアップ SigScalr を買収 | Apple がオブザーバビリティ（可観測性）分野のスタートアップ SigScalr を買収したと報じられている。ログやメトリクスなどの監視基盤に関わる技術・人材の取り込みを狙った動きとみられる。買収の詳細な条件は明らかにされていない。 | https://9to5mac.com/2026/07/13/apple-acquires-observability-startup-sigscalr/ |
| 4 | PostgreSQL で RE2 による高速な正規表現を使える拡張「pg_re2」 | Google の RE2 エンジンを利用し、PostgreSQL 上で高速な正規表現マッチングを可能にする拡張機能。RE2 は最悪計算量の爆発を避ける設計で知られ、標準の正規表現よりも安定した性能が期待できる。ClickHouse のブログで紹介されている。 | https://clickhouse.com/blog/introducing-pg_re2-regex-in-postgres |
| 5 | OpenAI の初のデバイスは画面のない可搬型スピーカー | OpenAI が開発中とされる最初のハードウェア製品は、持ち運び可能で画面を持たないスピーカー型の「AI コンパニオン」だと報じられている。ディスプレイに依存しない対話型のデバイスとして構想されているとされ、AI を日常的に使う新しい形として注目されている。 | https://www.bloomberg.com/news/articles/2026-07-14/openai-s-first-device-will-be-moveable-screenless-speaker-built-as-ai-companion |
| 6 | IBM の AI に関する警告が業界に波紋 | IBM が発した AI に関する警告が、テック業界に「衝撃」を与えたと伝える記事。AI の導入や雇用・事業への影響をめぐる見解が話題となっている。見出しは強い表現だが、実際の内容は IBM 側の見通しや懸念の表明にとどまる点に留意が必要。 | https://www.msn.com/en-us/money/other/ibm-sends-shockwave-through-tech-industry-with-ai-warning/ar-AA27TcGM |
| 7 | DeepSeek が年内にも IPO 申請を準備との報道 | 中国の AI 企業 DeepSeek が、早ければ年内にも新規株式公開（IPO）の申請を準備していると報じられている。70 億ドル規模の資金調達からわずか数週間後の動きとされ、新たな資金調達も検討しているという。生成 AI 分野の資本市場での存在感が改めて注目される。 | https://www.bloomberg.com/news/articles/2026-07-14/deepseek-mulls-new-funding-weeks-after-7-billion-round-ft-says |
| 8 | Dependabot のバージョン更新にデフォルトの「クールダウン」期間が導入 | GitHub の Dependabot に、依存パッケージの更新提案を一定期間見送る「パッケージのクールダウン」がデフォルトで導入された。新しくリリースされたバージョンをすぐには適用せず一定期間待つことで、リリース直後に見つかる不具合や悪意ある更新の影響を受けにくくする狙いがある。 | https://github.blog/changelog/2026-07-14-dependabot-version-updates-introduce-default-package-cooldown/ |

## Zenn

| # | タイトル | 要約 | URL |
|---|----------|------|-----|
| 1 | Cloudflare だけで独自ドメインメールを Gmail から送受信する | 独自ドメインのメールを、Cloudflare の機能だけで Gmail から送受信できるようになっていたことを紹介する記事。従来は別途メールサーバーやサービスが必要だった構成を、Cloudflare の Email Routing などを使って簡素化する手順を解説している。個人ドメインでのメール運用を手軽にしたい人向けの内容。 | https://zenn.dev/9m/articles/d08dcc093e1bbf |
| 2 | GitHub Actions の並列化でデプロイ 8 分→3 分、CI コスト 3 割減 | GitHub Actions のステップを parallel（並列）実行することで、デプロイ時間を 8 分から 3 分に短縮し、CI のコストも約 3 割削減できたという実践記録。どの処理を並列化したか、どのようにワークフローを組み替えたかを具体的に説明している。CI/CD のボトルネック解消を検討している開発者に参考になる。 | https://zenn.dev/hatsu/articles/github-actions-steps-parallel |
| 3 | Cursor に「不要なブランチを整理して」と頼んだら D ドライブが消えた | AI コーディングエージェント Cursor に不要な Git ブランチの整理を依頼したところ、想定外の動作で D ドライブの内容が消えてしまったという体験談。AI エージェントに破壊的な操作を任せる際のリスクや、権限・確認の重要性を実例を通して示している。エージェント運用の注意喚起として読まれている。 | https://zenn.dev/iwaken71/articles/cursor-agent-d-drive-deleted |
| 4 | 「AI 臭」は語彙よりリズムに出る — 7 モデル×406 本の実測 | AI が生成した日本語の不自然さ（AI 臭）は、使われる語彙よりも文のリズムに現れるという仮説を、7 モデル・406 本のテキストを実測して検証した記事。より自然な日本語を書かせるための Agent Skill を作成し、その効果を定量的に評価している。文章の自然さを改善したい人向けの実践的な内容。 | https://zenn.dev/coji/articles/natural-japanese-ai-smell-lint |
| 5 | 情報漏洩に敏感な金融機関で Claude・Gemini・ChatGPT を導入した話 | 情報漏洩リスクに厳しい金融機関において、Claude・Gemini・ChatGPT といった生成 AI をどのように導入していったかをまとめた記事。セキュリティやガバナンス上の制約をどうクリアしたか、利用ルールや体制づくりの観点から経験を共有している。規制の厳しい業界での AI 導入を検討する担当者に参考になる。 | https://zenn.dev/seiuchi3939/articles/b12d6746d9f187 |
| 6 | Markdown を push するだけで社内資料 PDF を常に最新に | Markdown を Git に push するだけで、社内資料の PDF を自動生成・配信して常に最新状態に保つ仕組みを解説する記事。Workload Identity Federation（WIF）と Google Drive を組み合わせ、サービスアカウントの鍵を持たない「鍵レス」な自動配信を実現している。ドキュメント運用の自動化とセキュリティ両立の事例。 | https://zenn.dev/o2wsu9/articles/36dea065f5d73c |
| 7 | 2026 年に相次いだ Excel/VBA とモダン開発をつなぐツール群 | Excel/VBA と現代的な開発環境の「あいだ」を埋めるツールとして、2026 年に登場した XLIDE・xlflow・xlsm_devkit などを紹介する記事。VBA の資産を活かしつつ、バージョン管理やモダンな開発フローを取り入れる動きを整理している。Excel 業務を抱える現場のモダナイズを考える際の見取り図となる。 | https://zenn.dev/minipoisson/articles/excel-vba-modern-dev |

## Qiita

| # | タイトル | 要約 | URL |
|---|----------|------|-----|
| 1 | 「15 歳と ChatGPT」より、4 万 6812 件が退会させられたシステムを考える | 未成年利用をめぐる議論を入り口に、約 4 万 6812 件が退会（アカウント削除）させられたとされるシステムのあり方を考察する記事。AI サービスにおける年齢確認やアカウント運用、利用者保護の仕組みについて問題提起している。生成 AI とセキュリティ・倫理の交差点を扱った内容。 | https://qiita.com/ZiYuCai1984/items/636c7c15cd666e987a90 |
| 2 | Claude Code、とりあえずこれ読んどけば OK なまとめ（2026 年版） | 2026 年時点の Claude Code の使い方を、初学者向けにまとめた入門記事。基本的な導入から活用のコツまでを一通り押さえ、「まずこれを読めば概要がつかめる」ことを目指している。新卒エンジニアや AI コーディングを始めたい人に向けた総括的な内容。 | https://qiita.com/fuyunoki/items/5818688d20225aa8088a |
| 3 | あなたの技術ブログの「AI 臭さ」を抜くスキルを公開 | 技術ブログの文章から、生成 AI 特有の「AI 臭さ」を取り除くためのスキルを公開する記事。AI が書いたと分かりやすい言い回しや構成をどう見直すか、実際のスキルとして共有している。AI を使いつつも自然で読みやすい文章に仕上げたい書き手に向けた内容。 | https://qiita.com/minorun365/items/699e89544da8b0de300d |
| 4 | Rails で学ぶ暗号化とハッシュ — master.key や Devise は内部で何をしているか | Rails を題材に、暗号化とハッシュの基礎を解説する記事。credentials を守る master.key の役割や、認証ライブラリ Devise が内部でパスワードをどう扱っているかを掘り下げている。フレームワークの「おまかせ」で済ませがちなセキュリティの仕組みを理解したい開発者向け。 | https://qiita.com/akachiryo/items/5a1deaa541d70e11d85f |
| 5 | AWS 東京・大阪を閉域で繋ぐ 3 つの方法、速さはどれくらい違うか | AWS の東京リージョンと大阪リージョンをインターネットを介さない閉域で接続する 3 通りの方法を取り上げ、実際に速度を比較した実験記事。VPC ピアリング、PrivateLink、Transit Gateway といった構成ごとのレイテンシや特性を計測している。マルチリージョン構成のネットワーク設計を検討する際の判断材料になる。 | https://qiita.com/sh_fukatsu/items/541051be6cbd4a90f2a6 |
| 6 | AI と人間が diff 上でコメントを書き合える「hunk」 | AI と人間がコードの diff 上で相互にコメントを書き合える「hunk」という仕組みを紹介する記事。ターミナル上でコードレビューのやり取りを AI と共有でき、Claude Code などと組み合わせた開発フローを想定している。人間と AI の協働レビューを効率化するツールとして注目されている。 | https://qiita.com/kuma_3838/items/14df505c7023f665c585 |
| 7 | 【今更きけない Codex】2026 年 7 月アップデート版の使いどころ | OpenAI の Codex について、2026 年 7 月のアップデートを踏まえ、ChatGPT デスクトップで最初に見るべき機能と使う順番を整理した記事。どの機能から触れば良いか迷いがちな初学者に向け、実用的な導入手順を示している。Codex を使い始める・使い直す際のガイドとなる内容。 | https://qiita.com/TMiyamoto/items/6bd89423d5b38916e48d |
| 8 | ECS と Kubernetes の違いを多方面から徹底比較 | コンテナオーケストレーションの選択肢として、AWS の ECS と Kubernetes を複数の観点から比較する記事。運用の手間、拡張性、エコシステム、セキュリティ（falco・CNAPP など）といった側面から両者の違いを整理している。コンテナ基盤の技術選定を検討しているエンジニア向けの内容。 | https://qiita.com/keitah/items/b35fc1c3b0dd8f6d7052 |
