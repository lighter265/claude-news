# 技術ニュース要約 — 2026-08-02

## 📌 今日の3行サマリ

- 中国発「DeepSeek V4 Flash」正式版が無償公開され、最小82GB台の軽量構成でローカル実行の裾野が広がる。
- MCP（Model Context Protocol）が2026-07-28に大型アップデート。ステートレス設計への注目が高まり、TypeScript SDK v2で検証が進む。
- GitHubが「Copilot SDK」を公開。Copilot CLIと同じエージェントランタイムを多言語からプログラム的に呼び出せるようになった。

## GitHub Trending

| # | タイトル | 要約 | URL |
|---|----------|------|-----|
| 1 | GitHub、Copilotエージェントを組み込む「Copilot SDK」を公開 — (原文: github/copilot-sdk) | • Copilot CLIと同じエージェントランタイムをSDK経由で提供<br>• Python / TypeScript / Go / .NET / Java / Rust の多言語に対応<br>• プランニングやツール実行はCopilot側が担い、独自オーケストレーション不要<br><br>アプリやサービスにエージェント的ワークフローを直接埋め込めるようになり、自前でエージェント基盤を構築する負担を減らせる。各社の開発ツールへのCopilot統合が進む契機になりそうだ。 | https://github.com/github/copilot-sdk |
| 2 | 体系的トレーディングの厳選リンク集 — (原文: paperswithbacktest/awesome-systematic-trading) | • 定量取引の研究・実運用向けライブラリ/パッケージを97件収録<br>• 機関投資家・研究者による40以上の戦略を解説<br>• 初心者から専門家向けまで書籍55冊、動画23本も整理<br><br>システマティックトレーディング（クオンツ取引）の戦略発見・開発・運用に必要な資料を一望できるキュレーション。中国語版も用意され、金融×プログラミングの入門・参照資料として広く使える。 | https://github.com/paperswithbacktest/awesome-systematic-trading |
| 3 | 必要な機能だけのオープンソースPM「Kaneo」 — (原文: usekaneo/kaneo) | • 肥大化したプロジェクト管理ツールへの反省から誕生<br>• 「機能が足りない」ではなく「多すぎる」問題を解決する方針<br>• 通知や不要なボタンを削り、開発そのものへの集中を重視<br><br>シンプルさを設計思想の中心に据えたセルフホスト型のプロジェクト管理ツール。クラウド版やDiscordコミュニティも用意され、軽量な代替ツールを探すチームの選択肢になる。 | https://github.com/usekaneo/kaneo |
| 4 | ディープラーニングによる顔交換ツール「FaceSwap」 — (原文: deepfakes/faceswap) | • 画像・動画内の顔を認識して入れ替えるオープンソースツール<br>• 複数の学習モデル（Phaze-A、Villainなど）を提供<br>• 導入前にINSTALL.mdの確認を推奨<br><br>ディープフェイク生成の代表的なOSSとして継続的に注目を集める。技術的な学習素材である一方、悪用リスクや倫理面の議論も伴うため、利用には配慮が求められる。 | https://github.com/deepfakes/faceswap |
| 5 | RAM効率を掲げるコーディングハーネス「jcode」 — (原文: 1jehuang/jcode) | • 「最もRAM効率が良いハーネス」を標榜するコーディング支援ツール<br>• macOS / Linux / Windows 11 向けのワンライナー導入を用意<br>• Homebrewやソースビルド、プロバイダ設定にも対応<br><br>省リソースを売りにしたAIコーディング用ハーネス。エージェントによるセットアップ支援も想定され、軽量な開発環境を求める層に向けた新興プロジェクトとして話題になっている。 | https://github.com/1jehuang/jcode |

## Hacker News

| # | タイトル | 要約 | URL |
|---|----------|------|-----|
| 1 | Googleは「Google News」を見捨てたのか — (原文: Google has abandoned Google News?) | • Google Newsが放置状態にあるとの批判記事<br>• 検索・ニュース事業の優先順位低下を指摘<br>• コメント160件超と大きな反響<br><br>大手プラットフォームのニュース配信への姿勢を問う論考。AI検索へのシフトが進む中、従来型ニュースアグリゲーションの位置づけが揺らいでいるとの見方が広がっている。 | https://elgan.com/google-news-is-just-forrest-gumps-shrimp-boat-now |
| 2 | シリコンバレーの「創業者ミンチ機」 — (原文: The Silicon Valley Founder Meat Grinder) | • スタートアップ創業者が消耗していく構造を批判<br>• 過酷な労働文化と投資家との関係を論じる<br>• コメント100件超の議論を呼んだ<br><br>起業家を使い潰すエコシステムへの問題提起。成功神話の裏にある消耗の実態を描き、創業者の心身の健康や持続可能な働き方をめぐる議論を喚起している。 | https://zaksa.zip/blog/silicon-valley-founder-meat-grinder/ |
| 3 | ドキュメント作成の体系「Diátaxis」 — (原文: Diátaxis) | • ドキュメントをチュートリアル/ハウツー/リファレンス/説明の4象限で整理<br>• 目的別に文書を分けることで書き手・読み手の負担を軽減<br>• 多くのOSSプロジェクトで採用が進む<br><br>技術文書の構造化フレームワークとして定評のある方法論。ドキュメント整備に悩むチームにとって、書くべき内容と形式を判断する実践的な指針になる。 | https://diataxis.fr/ |
| 4 | ByteDanceの動画生成モデル「Seedance 2.5」 — (原文: Seedance 2.5) | • ワンテイク生成と柔軟な参照指定に対応<br>• 動画生成の品質と制御性を向上<br>• ByteDance系のクリエイティブAIとして公開<br><br>動画生成分野での中国勢の攻勢を示す最新モデル。参照素材を使った生成の柔軟性が強化され、映像制作へのAI活用がさらに実用段階へ進んでいることをうかがわせる。 | https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5 |
| 5 | Coldcardの3800万ドル超のエクスプロイト、自己管理への信頼を揺るがす — (原文: Coldcard's $38M (so far) exploit shakes faith in self-custody) | • ハードウェアウォレットColdcardで大規模な資金流出<br>• 被害額は判明分だけで3800万ドル超<br>• 自己管理（セルフカストディ）の安全神話に疑問符<br><br>暗号資産の自己保管を支えるハードウェアの信頼性が問われる事例。投資家がETFなど預託型へ回帰する動きを促す可能性があり、セキュリティ設計の重要性を改めて浮き彫りにした。 | https://www.coindesk.com/business/2026/07/31/coldcard-s-usd38-million-so-far-exploit-shakes-faith-in-self-custody-may-push-investors-to-etfs |
| 6 | ステートレスなMCPが再び興味を引く — (原文: Stateless MCP has recaptured my interest) | • Simon Willison氏によるMCP再評価の論考<br>• ステートレス設計がもたらす実装の簡潔さに注目<br>• 直近のMCP仕様アップデートを背景に議論<br><br>AIエージェントとツール連携の標準として広がるMCPについて、状態を持たない設計の利点を論じる。仕様の進化に合わせ、より扱いやすい統合方式への関心が高まっている。 | https://simonwillison.net/2026/Jul/31/stateless-mcp/ |
| 7 | JPEGは一体どうやって動いているのか — (原文: How the Heck Does JPEG Work?) | • JPEG圧縮の仕組みを段階的に解説<br>• 離散コサイン変換など基礎理論を平易に紹介<br>• 画像がどう符号化されるかを可視化<br><br>身近な画像フォーマットの内部動作を丁寧に説明する技術記事。圧縮アルゴリズムの原理を学ぶ入門素材として、エンジニアの関心を集めている。 | https://perthirtysix.com/how-the-heck-does-jpeg-work |

## Anthropic

| # | タイトル | 要約 | URL |
|---|----------|------|-----|
| 1 | Claude Opus 5を発表 — (原文: Introducing Claude Opus 5) | • Anthropicの最上位モデルの新世代「Opus 5」を発表<br>• 高度な推論・分析タスク向けの主力モデル<br>• Productカテゴリの新着として公開<br><br>Claudeファミリーの最上位モデルが更新され、複雑な設計や深い分析を要する用途での性能向上が期待される。企業・開発者のワークフローに与える影響が注目される。 | https://www.anthropic.com/news/claude-opus-5 |
| 2 | Claude Sonnet 5を発表 — (原文: Introducing Claude Sonnet 5) | • バランス型モデル「Sonnet 5」を発表<br>• 標準的なタスク向けの性能と速度を両立<br>• Productカテゴリの新着<br><br>日常的な用途で広く使われるSonnet系の新世代。コストと性能のバランスを重視する多くのアプリケーションで採用が進むと見られる。 | https://www.anthropic.com/news/claude-sonnet-5 |
| 3 | Fable 5の再展開 — (原文: Redeploying Fable 5) | • モデル「Fable 5」の再デプロイを告知<br>• Announcementsカテゴリでの発表<br>• 提供体制の調整に関する内容<br><br>Fable 5の展開に関する運用面のアップデート。モデルの提供状況やアクセスに関わる情報として、利用者向けに周知されている。 | https://www.anthropic.com/news/redeploying-fable-5 |
| 4 | CognizantとAnthropic、提携を拡大しClaudeを企業顧客へ — (原文: Cognizant and Anthropic expand their partnership to bring Claude to enterprise clients) | • 大手ITサービスCognizantとの提携を拡大<br>• 企業顧客へのClaude導入を推進<br>• Announcementsカテゴリの発表<br><br>エンタープライズ領域でのClaude普及を狙った提携強化。SIパートナー経由での導入が進むことで、業務システムへのAI組み込みが加速する可能性がある。 | https://www.anthropic.com/news/cognizant-anthropic |
| 5 | Anthropic Economic IndexをClaudeに質問できるコネクタ — (原文: Ask Claude about the Anthropic Economic Index) | • 経済指標データにClaudeから対話的にアクセス<br>• Anthropic Economic Index連携のコネクタを提供<br>• Productカテゴリの新機能<br><br>AIの経済的影響を分析するデータへ自然言語で問い合わせられる仕組み。データ活用の裾野を広げる試みとして提供される。 | https://www.anthropic.com/news/anthropic-economic-index-connector |
| 6 | 教育者向けの「Claude for Teachers」を発表 — (原文: Introducing Claude for Teachers) | • 教員向けに特化したClaudeの提供を開始<br>• 授業準備や教材作成などの活用を想定<br>• Productカテゴリの新着<br><br>教育現場でのAI活用を後押しするサービス。教員の業務負担軽減や指導の質向上に向けた取り組みとして位置づけられる。 | https://www.anthropic.com/news/claude-for-teachers |

## OpenAI

| # | タイトル | 要約 | URL |
|---|----------|------|-----|
| 1 | 職場でAIが人の仕事の幅を広げる — (原文: How AI is expanding what people do at work) | • AIが業務でこなせる作業の範囲を拡大していると論じる<br>• 仕事の置き換えより「拡張」に焦点<br>• Companyカテゴリの発信<br><br>AI導入によって働き手ができることが広がるという視点を示す。単なる自動化ではなく、人の役割を拡張する方向での活用事例を強調している。 | https://openai.com/index/how-ai-is-expanding-what-people-do-at-work |
| 2 | avatarin、GPT-Realtimeで24時間稼働の小売エージェントを構築 — (原文: How avatarin built a 24/7 retail agent with GPT-Realtime) | • GPT-Realtimeを用いた小売向け対話エージェントの事例<br>• 24時間365日の顧客対応を実現<br>• 日本企業avatarinの導入事例<br><br>リアルタイム音声・対話AIを小売接客に応用した実装例。省人化と顧客体験の両立を狙った取り組みとして紹介されている。 | https://openai.com/index/avatarin |
| 3 | UnivéがAI対応の人材育成を推進 — (原文: Univé builds an AI-ready workforce) | • 保険企業UnivéのAI人材育成の取り組み<br>• 従業員のAI活用スキル向上を推進<br>• 業務変革に向けた組織的な対応<br><br>企業全体でAIを使いこなす体制づくりを進める事例。技術導入だけでなく人材面の準備が競争力を左右することを示している。 | https://openai.com/index/unive |

## InfoQ Japan

| # | タイトル | 要約 | URL |
|---|----------|------|-----|
| 1 | AWS、新「Amazon EKS Capabilities」でワークロード管理を簡素化 | • EKS向けの新機能群を発表<br>• ワークロードオーケストレーションを簡素化<br>• 運用負担の軽減を狙う<br><br>KubernetesマネージドサービスEKSの新機能により、コンテナワークロードの構成・管理が容易になる。運用の複雑さに悩む利用者の負担軽減が期待される。 | https://www.infoq.com/jp/news/2026/07/aws-eks-workload-orchestration/ |
| 2 | Cloudflare、企業のセキュリティ・ガバナンス課題を見据えMCPアーキテクチャを概説 | • MCP導入時のアーキテクチャ設計を解説<br>• セキュリティとガバナンスのリスクに焦点<br>• 企業利用での留意点を整理<br><br>AIエージェント連携の標準MCPを企業で安全に使うための設計指針。ツール接続に伴うリスク管理の重要性を示し、導入検討の参考になる。 | https://www.infoq.com/jp/news/2026/07/cloudflare-mcp/ |
| 3 | Dropbox、過疎ストレージから容量を回収する新コンパクション設計を導入 | • 使用率の低いストレージボリュームを対象<br>• 新しいコンパクション（圧縮・整理）設計を採用<br>• 容量効率の改善を実現<br><br>大規模ストレージの容量を効率的に回収する仕組み。インフラコストの最適化に向けた実装例として、大規模システムの運用者に示唆を与える。 | https://www.infoq.com/jp/news/2026/07/dropbox-tiered-compaction/ |
| 4 | Grafana、Kafkaで再設計したLokiとコーディングエージェント向けCLIを公開 | • ログ基盤LokiをKafkaベースで再設計<br>• コーディングエージェントにオブザーバビリティを提供するCLIをリリース<br>• AIエージェント運用の可観測性を強化<br><br>ログ収集基盤の刷新と、AIコーディングエージェント向け監視ツールの登場。エージェント運用の透明性を高める動きとして注目される。 | https://www.infoq.com/jp/news/2026/07/grafana-loki-ai-agents/ |
| 5 | Kubescape 4.0、Kubernetesに実行時セキュリティとAIエージェントスキャンを追加 | • ランタイムセキュリティ機能を追加<br>• AIエージェントのスキャンに対応<br>• Kubernetesのセキュリティ強化を図る<br><br>クラスタの実行時脅威検知とAIエージェント関連のスキャンを備えた新版。コンテナ環境のセキュリティ対策を包括的に進める動きを示す。 | https://www.infoq.com/jp/news/2026/07/kubescape-40/ |
| 6 | Amazon CloudWatch、OpenTelemetryメトリクス対応をプレビュー公開 | • CloudWatchがOTelメトリクスに対応<br>• プレビュー段階での提供開始<br>• 標準的な計装との親和性を向上<br><br>オープンな計装標準OpenTelemetryとの統合が進む。ベンダー横断的な可観測性の実現に向け、監視データの取り扱いが柔軟になる。 | https://www.infoq.com/jp/news/2026/07/cloudwatch-opentelemetry-metrics/ |
| 7 | AIがソフトウェアライフサイクルの上流へ：コードレビューからPRDガバナンスへ | • AI活用の焦点が下流から上流工程へ移行<br>• コードレビューに加えPRD（要求仕様）の統制へ<br>• 開発プロセス全体でのAI関与を論じる<br><br>AIの適用領域が実装後のレビューから要件定義段階へと広がる潮流を分析。上流での品質・整合性管理にAIを活かす考え方が広がりつつある。 | https://www.infoq.com/jp/news/2026/07/ai-prd-code-review-governance/ |

## はてなブックマーク (tech)

| # | タイトル | 要約 | URL |
|---|----------|------|-----|
| 1 | AIフレンドリーなCLIを開発するテクニック | • AIエージェントが扱いやすいCLI設計の勘所を解説<br>• 出力形式やエラー表現など具体的な工夫を紹介<br>• OSS開発の実践知見に基づく<br><br>AIがコマンドを介してツールを操作する時代に向けたCLI設計論。機械可読性を意識したインターフェースづくりが、エージェント連携の質を左右することを示す。 | https://zenn.dev/shunsuke_suzuki/articles/make-cli-ai-friendly |
| 2 | カンファレンス生態系の変化とCFPの功罪 | • 技術カンファレンスを取り巻く環境の変化を考察<br>• CFP（登壇公募）がもたらす利点と弊害を論じる<br>• コミュニティのあり方に問いを投げかける<br><br>登壇公募文化がカンファレンスの質やコミュニティに与える影響を掘り下げる論考。技術者の学びと交流の場をどう維持するかを考えさせる。 | https://blog.jxck.io/entries/2026-07-31/cfp-over-conference.html |
| 3 | DeepSeekショック再来？「DeepSeek V4 Flash」正式版が無償公開 | • 中国発LLM「DeepSeek V4 Flash」の正式版を無償公開<br>• 公式版は167GB、Unsloth版は最小82GB台<br>• 軽量構成でローカル実行の敷居を下げる<br><br>高性能な中国製オープンモデルの登場が再び波紋を広げる。量子化により手元での実行が現実的になり、オープンLLMの競争が一段と激しくなっている。 | https://pc.watch.impress.co.jp/docs/news/2129807.html |
| 4 | 米Amazon、コーディング作業でClaudeの使い方を誤り予算の8倍超を消費 | • 単純なコーディング作業でClaudeの使い方を誤る<br>• 想定予算の8倍超のコストが発生<br>• AI利用のコスト管理の難しさを露呈<br><br>大企業でもAIの使い方次第でコストが大きく膨らむ事例。エージェントやモデル呼び出しの設計・監視が、運用コストを左右することを改めて示している。 | https://gadget.phileweb.com/post-129954/ |
| 5 | 地理演算でファンタジー地図を自動生成するWebツール「USOMAP」 | • 生成AIを使わず地理演算で地図を自動生成<br>• 水源から町を配置するなどリアルな地形ロジック<br>• 国境線の引き方も自然に見えると話題<br><br>アルゴリズムによる手続き的生成でファンタジー地図を作るツール。AIに頼らない生成手法の面白さが注目され、創作支援としての活用が期待される。 | https://togetter.com/li/2727453 |
| 6 | Web Streams API 入門 ― 基本概念から実践まで | • Web Streams APIの基礎概念を体系的に解説<br>• ストリーム処理の実践的な使い方を紹介<br>• ブラウザでの非同期データ処理に対応<br><br>ブラウザ標準のストリーム処理APIを一から学べる入門記事。大きなデータの逐次処理や効率的なI/Oを扱うフロントエンド開発の参考になる。 | https://zenn.dev/cybozu_frontend/articles/web-streams-api-guide |
| 7 | 高校数学で解き明かす最先端AIの共通構造 | • 最先端AIに共通する構造を高校数学の範囲で解説<br>• 問題設定から学習までを4ステップで整理<br>• 数学的な直観で仕組みを理解<br><br>難解に見えるAIの数理を平易な数学で読み解く連載記事。理論の全体像をつかみたい学習者にとって、入り口となる解説として支持されている。 | https://gihyo.jp/article/2026/07/mathematical-thinking-04 |

## Zenn

| # | タイトル | 要約 | URL |
|---|----------|------|-----|
| 1 | 1日500コミットは、もう読めない ── だからコードレビューをやめた | • AIによる大量コミットでレビューが追いつかない状況を提起<br>• 従来型の全件コードレビューを見直す試み<br>• 開発プロセスの再設計を論じる<br><br>AI駆動開発で生成量が爆発する中、人手レビューの限界と代替策を考える論考。品質保証の仕組みをどう作り直すかという課題を鋭く突いている。 | https://zenn.dev/singularity/articles/stopped-reviewing-my-code |
| 2 | Opus5が思考が浅いように感じる問題への対策 | • Opus 5で推論が浅く感じるケースへの対処法<br>• プロンプトやルール設計の見直しを提案<br>• 実践的な調整の勘所を共有<br><br>新モデルの挙動変化に戸惑う利用者向けの実用ノウハウ。モデル更新に合わせてプロンプト戦略を調整する必要性を具体例で示している。 | https://zenn.dev/u1/articles/claude5-rules-collapse-and-fix |
| 3 | Opus 5では今までのプロンプトが逆効果に。公式プロンプトガイドを読み解く | • Opus 5では従来型プロンプトが逆効果になる場合がある<br>• 「検証して」を消し「簡潔に」と書くべきと解説<br>• 公式プロンプトガイドを踏まえた指針<br><br>モデル世代交代でプロンプトの定石が変わることを示す記事。過剰な指示がかえって性能を損なう可能性を指摘し、書き方の更新を促している。 | https://zenn.dev/little_hand_s/articles/72646a09f49d2a |
| 4 | 「Simple Made Easy」の観点から、UI/UXはどうあるべきか | • Rich Hickeyの講演「Simple Made Easy」を起点に考察<br>• 「単純さ」と「容易さ」を区別してUI/UXを論じる<br>• 設計思想としてのシンプルさを掘り下げる<br><br>ソフトウェア設計の名講演をUI/UX設計に応用する論考。表面的な使いやすさと本質的な単純さの違いを意識した設計の重要性を説く。 | https://zenn.dev/pksha/articles/6cdf19e5fe8065 |
| 5 | 【決着】Claude CodeとCodexの設定ファイルを同期させる | • Claude CodeとCodexの設定を共通化する方法<br>• 両ツールの設定ファイルを同期させる実践手順<br>• 複数AIツール併用時の運用を効率化<br><br>複数のAIコーディングツールを併用する際の設定管理の工夫。ツール間で設定を揃えることで、切り替えの手間や不整合を減らせる。 | https://zenn.dev/explaza/articles/20f7f41cff8428 |
| 6 | MCPの大型アップデート（2026-07-28）で何が変わったか — TypeScript SDK v2で試す | • 2026-07-28のMCP仕様大型アップデートを解説<br>• ステートレス仕様など変更点を整理<br>• TypeScript SDK v2で実際に検証<br><br>MCPの最新仕様変更を実装面から追った記事。SDKの新バージョンを使った検証を通じ、エージェント連携の設計がどう変わるかを具体的に示している。 | https://zenn.dev/komlock_lab/articles/mcp-stateless-spec-2026 |
| 7 | AI時代に感じた危機感と、エンジニアがこれから考えるべきこと | • AIの進化に対するエンジニアの危機感を率直に語る<br>• 今後求められるスキルや役割の変化を考察<br>• キャリアの方向性を問い直す<br><br>AIが開発を大きく変える中でのエンジニアの立ち位置を考えるエッセイ。技術者が何に価値を見出し、どう成長すべきかを問いかけている。 | https://zenn.dev/nabewata/articles/8cef1bd4cbae3f |

## Qiita

| # | タイトル | 要約 | URL |
|---|----------|------|-----|
| 1 | オーダーメイドで九九の計算プリントを作ろう（ローテクAI） | • Geminiを使い子ども向けの九九プリントを生成<br>• 「ローテクAI」として身近な活用例を紹介<br>• 夏休みの学習支援に応用<br><br>生成AIを日常の子育て・学習に活かす親しみやすい事例。高度な用途でなくても、AIが手軽な作業効率化に役立つことを示している。 | https://qiita.com/Kaitou/items/33e9a09af8ea5bdeebeb |
| 2 | リプレイ機能付きオセロを作って、AWS（EC2/RDS）にデプロイしてみた | • オセロゲームにリプレイ機能を実装<br>• AWSのEC2/RDSを使ってデプロイ<br>• 初心者向けのクラウド実践<br><br>ゲーム開発とクラウドデプロイを一通り体験する学習記事。個人開発でAWSの基本構成を試したい初学者の参考になる。 | https://qiita.com/KyosukeTakahagi/items/aae3889fb1dacf6892c8 |
| 3 | 役割を広げたらほんまに強くなれるんかみたいな話 | • エンジニアが担当領域を広げる意義を考察<br>• ドメイン知識やキャリアの観点から論じる<br>• AI時代の働き方への示唆を含む<br><br>専門を越えて役割を広げることの是非を問うエッセイ。AIが技術面を補う中で、人が発揮すべき価値やキャリア戦略を考えさせる内容。 | https://qiita.com/morry_48/items/170fb14f1f9c48f115d5 |
| 4 | Elixir と Livebook で学ぶ LLM / Transformer 入門 | • ElixirとLivebookでLLMの基礎を学ぶ<br>• トークン化からミニGPTの自作学習までを実装<br>• Nxを用いた機械学習の実践<br><br>関数型言語Elixirを使ってTransformerの仕組みを手を動かして学ぶ入門記事。理論と実装を結びつけながらLLMの内部を理解したい人に向く。 | https://qiita.com/RyoWakabayashi/items/ca95db1982c78e40a907 |
| 5 | Google A2AをサポートしたOCI Autonomous Databaseでマルチエージェントを実装 | • OCI Autonomous DatabaseでGoogle A2Aに対応<br>• マルチエージェント連携を実装<br>• エージェント間通信の実践例<br><br>データベース基盤上でエージェント同士を連携させる先進的な実装例。A2A（Agent2Agent）による協調動作を、実サービスで試す手順を示している。 | https://qiita.com/ksonoda/items/d2f2263cf9dc5d2ddd67 |
| 6 | どう頼むかがAIの成果を決める ― 丸投げしないAI協業の「発注の型」 | • AIへの依頼の仕方が成果を左右すると論じる<br>• 丸投げを避けるための「発注の型」を提案<br>• Human-in-the-Loopの実践を重視<br><br>AIと協業する際の依頼設計の重要性を説く記事。適切に分割・指示することで成果の質を高める、実務的なコミュニケーションの型を提示している。 | https://qiita.com/sh-fukaya/items/c1d6c7b0281e8e8afe5c |
| 7 | RAGでマルチシートExcelとWordを壊さず扱うための構造化前処理とChunking | • マルチシートExcelやWordをRAGで扱う課題に対処<br>• 構造を保つ前処理とChunking手法を実装<br>• 文書の情報損失を防ぐ工夫を紹介<br><br>複雑なオフィス文書をRAGに取り込む際の実践的な前処理手法。表構造や書式を壊さずにチャンク分割する工夫が、検索精度の向上に役立つ。 | https://qiita.com/engchina/items/ac600e372fe572fe7457 |
