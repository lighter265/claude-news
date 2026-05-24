# 技術ニュース要約 — 2026-05-25

## GitHub Trending

### AIエージェント向けサイバーセキュリティスキルライブラリ — 754件・5フレームワーク対応
MITRE ATT&CK、NIST CSF 2.0、MITRE ATLAS、D3FEND、NIST AI RMF の5つの標準フレームワークにマッピングされた754件のサイバーセキュリティスキルをまとめたオープンソースリポジトリ。26のセキュリティドメインをカバーし、Claude Code・GitHub Copilot・Cursor・Gemini CLI など20以上のAIプラットフォームで利用できる。Apache 2.0ライセンスで公開されており、agentskills.io 標準に準拠している。AIエージェントにセキュリティ知識を体系的に組み込むための基盤として活用できる。
https://github.com/mukul975/Anthropic-Cybersecurity-Skills

### Gamma・Beautiful AIに代わるオープンソースのAIプレゼン生成ツール「Presenton」
SaaS型プレゼン生成サービス（Gamma、Beautiful AI、Decktopus）のオープンソース代替として開発されたAIプレゼンテーションジェネレーター。Docker経由でのセルフホストとデスクトップアプリ（Mac・Windows・Linux）の両方に対応している。OpenAI、Gemini、Vertex AI、Azure OpenAI、Amazon Bedrockなど主要なLLMプロバイダーを選択でき、データをローカルに留めたままAIプレゼン生成が可能。ベンダーロックインを嫌うチームや、データ管理を自社で完結させたい企業向けの選択肢となっている。
https://github.com/presenton/presenton

### NVIDIA発・NVFP4量子化と並列処理で長尺動画生成を45.7 FPSに高速化「LongLive 2.0」
NVIDIAが開発した長尺動画生成向けの並列インフラ「LongLive 2.0」。NVFP4量子化と並列処理を組み合わせ、トレーニングから推論まで一貫した高速化を実現している。AR学習・DMDディスティレーション・推論の各工程に対応し、推論時は45.7 FPSを達成。また TriAttention を用いたKVキャッシュ圧縮も搭載しており、KVメモリを50%削減しながら品質を維持する。長尺動画の研究・生成コストを大幅に下げることが期待される。
https://github.com/NVlabs/LongLive

### プロセスの実行トレースを高解像度で可視化するデバッグツール「magic-trace」
Jane Street が開発した、実行中プロセスの高解像度トレースを収集・表示するOSSツール。本番環境で一部リクエストだけ遅延するような問題や、「コードが実際に何をしているか」を事後確認するユースケースに活用できる。クラッシュ前の動作履歴を後から追える点が特徴で、Perfettoベースのビューアで視覚的に確認可能。gdbのような割り込みなしに稼働中プロセスをインスペクトできるため、本番デバッグの選択肢として注目されている。
https://github.com/janestreet/magic-trace

## Hacker News

### オーストラリア週4日勤務の実証実験、生産性向上のデータが明らかに
オーストラリアで実施された週4日勤務の試験導入に関する研究報告。データによれば、労働時間短縮にもかかわらず生産性は維持または向上したと報告されている。従業員のウェルビーイング改善や離職率低下も確認されており、「労働時間と生産性は比例する」という従来の前提に疑問を呈する結果となった。国際的に広がる週4日勤務の議論に実証的な根拠を加える内容として注目を集め、30件のコメントが寄せられている。
https://scienceaim.com/australia-just-proved-the-four-day-work-week-works-here-is-what-the-data-actually-says/

### 米CBP、国境における電子機器の強制検索に関する指令3340-049Bを公開
米国税関・国境警備局（CBP）が公開した、国境での電子機器検索に関する公式指令文書。令状なしに端末のデータを調べる権限の範囲や手続きを規定しており、プライバシー権との緊張関係が議論されている。入国者・帰国市民問わず対象となる可能性があり、特に機密情報を扱うビジネスパーソンや渡航者にとって実務的な影響がある。スコア48と高い注目度を集め、国境でのデジタルプライバシーに関心を持つ層を中心に共有されている。
https://www.cbp.gov/document/directives/cbp-directive-no-3340-049b-border-search-electronic-devices

### 米国の健康アウトカムが政治的二極化と相関、Nature誌に掲載
自然科学誌Natureに掲載された研究で、米国における健康アウトカム（平均寿命・疾病率など）が政治的傾向と有意な相関を持つことが報告された。共和党・民主党支持地域の間で健康指標に差が広がっており、単純な経済格差だけでは説明できない構造的な要因が示唆されている。医療アクセス・政策・生活習慣など複合的な要因が絡み合うとされ、公衆衛生と政治の関係についての議論を呼んでいる。
https://www.nature.com/articles/s41562-026-02474-9

### Gitの厳格な運用疲れを「Jujutsu」で解消する方法
GitのコミットやブランチモデルによるCLI操作の煩雑さに疲弊した開発者向けに、代替バージョン管理ツール「Jujutsu（jj）」を活用した改善例を紹介する記事。Jujutsuは変更セット（Change）を第一級概念として扱い、コミットの書き換えやrebaseを安全かつ直感的に行える設計になっている。Gitと互換性を持ちながら操作モデルが異なるため、既存のリモートリポジトリをそのまま使い続けられる点が特徴。Gitの運用ルールに縛られたチームの代替案として検討価値がある。
https://ikesau.co/blog/defeating-git-rigour-fatigue-with-jujutsu/

### ホワイトハウス、情報機関のAI整備に90億ドルを承認
米ホワイトハウスが、CIA・NSAなどの諜報機関がAIの活用で民間に後れを取らないよう、AIチップや関連インフラの整備に90億ドルを承認したと報じられた。GPU不足が情報機関のAI導入を妨げていた背景があり、安全保障分野でのAI競争力強化が目的とされている。民間テック企業との人材・計算資源の獲得競争が激化する中、国家レベルでのAI投資が政策として明確化された形となる。
https://www.nytimes.com/2026/05/22/us/politics/spy-agencies-ai-chips-shortage.html

### WebAuthnのcredentialProtectionPolicyを丁寧に解説
WebAuthnに用意されているが理解されにくい拡張機能「credentialProtectionPolicy」の仕組みを解説した記事。デバイス上のパスキーが「PIN/生体認証なしでも使えてしまう」問題を防ぐためのポリシー設定で、セキュリティレベルを3段階で制御できる。実装側の考慮事項と、ユーザー体験とのトレードオフについても論じており、パスキー実装者にとって実用的な内容となっている。
https://pilcrowonpaper.com/blog/16

## Reddit

### Chrome、宣言的な部分更新APIを新たに提案 — HTMLの差分更新を標準化へ
Googleが、JavaScriptを使わずにHTMLの一部をサーバー側から差分更新できる「Declarative Partial Updates」APIをChrome向けに提案した。現在はJavaScriptやHTMXなどのライブラリで実現されているHTMLの部分更新を、ブラウザネイティブの仕組みで標準化しようとする試み。サーバーサイドレンダリングとの親和性が高く、フルページリロードなしの画面更新を軽量に実現できる可能性がある。r/programmingで331スコアを獲得し、77件のコメントが寄せられるなど大きな注目を集めた。
https://developer.chrome.com/blog/declarative-partial-updates

### C++標準ライブラリは15年かけて自己否定を繰り返してきた — 公開記録を読む
C++標準ライブラリの歴史を振り返り、追加された機能が後の改訂で非推奨・削除・変更された事例を公開されている委員会文書から整理した記事。`std::auto_ptr`・`std::random_shuffle`・例外仕様など、設計判断が覆されてきた積み重ねを「後退の記録」として可視化している。言語設計の難しさや、標準化プロセスの長期的な影響を考える上で示唆が多い内容で、r/programmingで278スコア・202コメントを集めた。
https://hftuniversity.com/post/the-c-standard-library-has-been-walking-itself-back-for-fifteen-years-and-the-receipts-are-public

### PapersWithCode、週次アップデートで新機能を複数追加
機械学習の論文・実装・ベンチマークを一覧できるプラットフォーム「PapersWithCode」が、Week 1 の新機能をまとめて公開した。検索・フィルタリング・ランキング表示の改善が含まれており、最新研究の追跡が従来より効率的になるとされている。r/MachineLearningで86スコアを獲得し、ML研究者・実務者から注目されている。定期的な機能更新を継続する姿勢が評価されているようだ。
https://www.reddit.com/r/MachineLearning/comments/1tmawv5/paperswithcode_new_features_week_1_p/

### SQLとNoSQLだけでは足りない — エキゾチックなDBエンジンを分類・比較
グラフDB・時系列DB・ベクトルDB・列指向DBなど、一般的なRDB/NoSQLの枠に収まらない「データベース動物園」を俯瞰する記事。ユースケース別にどのストレージエンジンが向いているかを整理しており、新規システム設計やデータ基盤選定の際の地図として機能する。近年のAI・分析ワークロードの多様化を背景に、DB選択が複雑化していることへの実践的な対応策として参考になる内容。
https://blog.gaborkoos.com/posts/2025-09-19-The-Database-Zoo-Exotic-Data-Storage-Engines/

## Zenn

### 複数集約をまたぐDB処理でトランザクションを使う前に考えるべきこと
DDD（ドメイン駆動設計）において複数の集約にまたがる処理を単一DBトランザクションで括ることの問題点を論じた記事。集約の境界と整合性の単位が一致しない場合に発生する設計上のリスクや、代替手段（イベント、サーガパターン等）の検討材料が示されている。トランザクション設計の前提を丁寧に整理した内容で、スコア121と高い支持を集めている。
https://zenn.dev/j5ik2o/articles/59de072b6728ff

### 日々の開発に組み込まれたClaude Code Skillsの実例集
実際の開発現場でClaude Code Skillsをどのように運用しているかを紹介するアイデア記事。定型作業の自動化・コードレビュー補助・ドキュメント生成など具体的な活用例が共有されており、Claude Codeを業務フローに組み込む際の参考になる。スコア106を記録しており、Claude Code活用に関心を持つ開発者の間で広く読まれている。
https://zenn.dev/remitaid/articles/4f9dc787b6c191

### 「URLを誰にも教えていない」は秘匿性にならない — CT ログを30分監視した実験記録
Certificate Transparency（CT）ログを30分間監視するだけで、公開されていないはずのURLが観測できることを示した実験記事。HTTPSを発行した時点でドメイン・サブドメインがCTログに記録されるため、URLを秘密にしていても第三者がドメインを発見できる仕組みになっている。「隠しURL」による情報保護の限界を実証的に示しており、セキュリティ意識の向上につながる内容。スコア99を獲得している。
https://zenn.dev/tkydev/articles/2026-05-21_ct_log

### Claude Code Skillで社内プロジェクトを仕組み化し、1時間で開発を完了させる
SonicGardenが、Claude Code の Skill 機能を活用して社内プロジェクトの開発プロセスを標準化・自動化した取り組みを紹介。スキルとして手順を定義することで、属人的な判断を減らし再現性のある開発フローを実現している。新メンバーのオンボーディングコスト削減や品質の均一化にも効果があるとされ、スコア78で実践事例として注目されている。
https://zenn.dev/sonicgarden/articles/e5fd7f54433d3d

### TSKaigi 2026 の発表資料まとめ
TypeScriptカンファレンス「TSKaigi 2026」の発表スライドや資料をまとめたインデックス記事。セッション内容を一覧できるため、参加できなかった人や後から振り返りたい人に有用。スコア35を記録しており、TypeScriptコミュニティ内での情報共有の場として機能している。
https://zenn.dev/yasse/articles/a7240304af804c

### Rustで自作した可逆圧縮フォーマット「IVR」がVSCodeスクショでPNG比46%を達成
Rustでゼロからロスレスのカスタムビットマップ圧縮フォーマット「IVR」を実装したという技術記事。特定のVSCodeスクリーンショットにおいて、PNGの46%というファイルサイズを達成したと報告されている。圧縮アルゴリズムの設計から実装詳細まで踏み込んだ内容で、低レベルの画像処理やRustの実装に関心を持つ読者から支持されている（スコア22）。
https://zenn.dev/mugideru/articles/35b209e934ba3e

### Claude Codeのスキルを毎日自動改善し続ける仕組みの構築
SonicGardenが、Claude Code のスキルが自己改善ループで日々自動的に更新される仕組みを作った経緯を紹介。実行ログや失敗例を材料にスキルを継続的に洗練させる設計で、人の手を介さずにプロンプトの質が向上していく。スコア18を獲得し、AIエージェントの自律的改善というテーマで注目されている。
https://zenn.dev/sonicgarden/articles/claude-code-self-improving-loop

## Qiita

### 育休中エンジニアがClaude Coworkで「あかちゃんカレンダー」アプリを開発
育児休業中のエンジニアが、Claude の Cowork 機能を活用して赤ちゃんの成長記録カレンダーアプリを個人開発した体験記。育休という限られた時間の中でAIを活用して実装を進めたプロセスが語られており、AIコーディング支援の実用的な活用例として読まれている。スコア38を獲得し、育休×開発というユニークな切り口が共感を集めている。
https://qiita.com/yuzinet/items/323bc76cf2d31d9f4d42

### AIが生成するテストケースが「しょっぱい」理由を真剣に考えた
LLMを使ってテストケースを生成させると、表面的で網羅性の低い「しょっぱい」テストになりがちな問題の原因を分析した記事。コンテキストエンジニアリングの観点から、AIに何を・どのように伝えるかによって生成されるテストの質が大きく変わることを示している。QAエンジニアやAI活用に取り組む開発者にとって実践的な示唆を含む内容で、スコア35を記録。
https://qiita.com/yurizono/items/43a93d8ff3f7046b31e3

### Mac から UTM 上の Ubuntu に SSH 接続すると「Connection closed by port 22」が出る問題の対処法
MacからUTM（仮想化ソフト）上に構築したUbuntu環境へSSH接続しようとした際に発生する「Connection closed by port 22」エラーの原因と解決方法を記録した記事。UTM特有のネットワーク設定やSSHd設定の確認ポイントが整理されており、同様の環境を使っている開発者にとって実用性の高いトラブルシューティング情報。スコア13を獲得している。
https://qiita.com/inorin__62/items/6a15efcf60f954a89373

### フロントエンドパフォーマンス改善の完全ロードマップ総まとめ（第20回）
フロントエンドパフォーマンス改善シリーズの最終回として、JavaScript・TypeScript・Reactにおけるパフォーマンス最適化手法を網羅的にまとめた記事。LCP・INP・TTFBなどのCore Web Vitalsの改善手法からバンドル最適化・コード分割まで体系的に整理されており、フロントエンドエンジニアの実務リファレンスとして活用できる。スコア9を獲得している。
https://qiita.com/tuanphan/items/1feeae0fc6ae30aa709d

### ドキュメントが失われたAWS環境を1日で再現、再構築手順書まで自動生成
Claude Opus 4.7の「infra delegate to」機能を活用し、ドキュメントが残っていないAWS環境を1日でリバースエンジニアリングした事例記事。CloudFormationテンプレートの自動生成から再構築手順書の作成まで、AIエージェントに委任する形で完結させた過程が紹介されている。レガシー環境の棚卸しやインフラのコード化に課題を抱えるチームへの実践的なヒントとなっている（スコア9）。
https://qiita.com/ntaka329/items/b1d961ce5fab8541101f

### Claude CodeだけでKaggleコンペに挑んで惨敗した正直な記録
Claude Codeだけを使ってKaggleコンペに挑戦し、結果的に惨敗した経験を正直にまとめた記事。AIが生成するコードやアプローチの限界、特に特徴量エンジニアリングや仮説設定といった「勝負どころ」でのAIの弱点が浮き彫りになっている。AI活用の過信を戒める内容として、機械学習実務者に参考になる視点を提供している。
https://qiita.com/ktdatascience/items/cad6d18c080aa6ca812c
