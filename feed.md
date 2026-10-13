# 技術ニュース要約 — 2026-10-14

## 📌 今日の3行サマリ

- NICT（情報通信研究機構）が、相次ぐ情報漏えいの原因の一つとして「公開アプリを解析してサーバを攻撃する」手口（A2B 攻撃）への注意を呼びかけた。発表ははてなブックマーク 496 を集め、総務省も同じ内容の注意喚起を出している。
- フランスのスーパー数百店舗で冷蔵設備がサイバー攻撃を受け、温度が最高 50 度まで上がって食品を大量に廃棄したと報じられた（はてなブックマーク 474）。IoT 機器への攻撃が現実の被害に直結した例として注目されている。
- OpenAI のオフィスで録音装置が見つかり、FBI が同社の従業員を逮捕したと複数のメディアが報じた。Hacker News では関連投稿が当日最多の 79 ポイントを集め、米司法省も発表を出している。

## GitHub Trending

| # | タイトル | 要約 | URL |
|---|----------|------|-----|
| 1 | rea — アプリの挙動からネイティブバイナリまでエージェントで解析するリバースエンジニアリング用 MCP — (原文: morluto/rea) | • エージェントを使ってリバースエンジニアリングを行うツール。<br>• バイナリ、アプリケーション、実行時の挙動を 1 つの MCP で扱うとしている。<br>• README は日本語を含む多数の言語で用意されている。<br><br>前日に続いてトレンド上位に入った。同日には NICT が「アプリ解析からのサーバ攻撃」への注意を呼びかけており、解析技術を防御と攻撃の両面からどう扱うかが改めて問われている。 | https://github.com/morluto/rea |
| 2 | Context Mode — AI コーディングエージェントのコンテキストウィンドウを節約するツール — (原文: mksglu/context-mode) | • ツールの出力をサンドボックスに隔離し、コンテキストへの流入を 98% 減らすとしている。<br>• セッションのメモリを保持し、MCP とフックで 17 のプラットフォームにまたがるルーティングを強制する。<br>• Playwright のスナップショット 1 回で 56KB を消費するといった具体例で課題を説明している。<br><br>MCP ツールの呼び出し結果がそのままコンテキストを圧迫する問題は、エージェントを長時間使うほど目立つ。削減率は README の主張であり、実際の効果は使い方によって変わる点に注意したい。 | https://github.com/mksglu/context-mode |
| 3 | God's Eye View — 公開データで動くブラウザ上の偵察衛星シミュレーター — (原文: bilawalsidhu/gods-eye-view) | • 写実的な 3D 地球儀上に、公開情報を使った空間情報を表示する。<br>• 航空機、船舶、衛星、地震、交通、公開カメラをリアルタイムに重ねて見られる。<br>• リアルタイム AI エージェントによる音声操作にも対応する。<br><br>オープンソースの空間インテリジェンス（OSINT）を手軽に体験できる点が特徴で、連日トレンドに入っている。公開データだけでどこまで把握できるかを示す例として、プライバシーの観点からも議論の材料になりそうだ。 | https://github.com/bilawalsidhu/gods-eye-view |
| 4 | ArtCraft — アーティスト向けの AI 画像・動画制作 IDE — (原文: storytold/artcraft) | • アーティスト、デザイナー、映像制作者向けの「意図的なクラフト」エンジンを掲げる。<br>• 2D での構図作成と 3D でのシーン配置を組み合わせて AI 画像・動画を作る。<br>• 用途に合わせて生成モデルを選べる構成。<br><br>プロンプトを書くだけの生成から、視覚的な操作で作り込む方向への転換を狙っている。デスクトップアプリとして配布され、ソースからのビルドにも対応する。 | https://github.com/storytold/artcraft |
| 5 | Open WebUI — セルフホスト型の AI チャットプラットフォーム — (原文: open-webui/open-webui) | • 完全オフラインでも動かせる、拡張性の高いセルフホスト型 AI プラットフォーム。<br>• Ollama と OpenAI 互換 API に対応し、ローカルとクラウドのモデルを同じ画面で扱える。<br>• エンタープライズ向けプランも用意している。<br><br>特定のモデル提供元に依存しない UI として定番になっているプロジェクト。社内で AI チャットを運用したい組織の選択肢として、継続的に注目を集めている。 | https://github.com/open-webui/open-webui |
| 6 | diagram-design — コーディングエージェント向けの図版作成スキル — (原文: cathrynlavery/diagram-design) | • Claude Code、Codex、GitHub Copilot、Cursor などで使えるエージェントスキル。<br>• 40 種類以上の図を、単一の HTML + SVG ファイルとして出力する。<br>• 自社ブランドに合わせたデザインに調整できるとしている。<br><br>「影なし」「Mermaid に頼らない」編集デザイン寄りの図を打ち出している。`npx skills add` で導入でき、エージェントの出力物の見た目を整える用途で関心を集めている。 | https://github.com/cathrynlavery/diagram-design |
| 7 | BitNet — Microsoft による 1 ビット LLM の公式推論フレームワーク — (原文: microsoft/BitNet) | • 1 ビット LLM 向けの推論フレームワーク bitnet.cpp を提供する。<br>• 2026 年 7 月に、BitNet の量子化を使う CPU 向けリアルタイム多言語音声認識エンジン VibeASR.cpp を公開した。<br>• 1 ビットの埋め込みモデル BitNet-embedding も Hugging Face で公開している。<br><br>GPU を使わずに CPU だけで実用的な速度を出す方向の取り組みとして注目される。x86（AVX2）と ARM（NEON）の両方に対応しており、エッジ機器での活用が想定される。 | https://github.com/microsoft/BitNet |
| 8 | AirLLM — 4GB の GPU 1 枚で 70B モデルを推論 — (原文: lyogavin/airllm) | • 量子化・蒸留・枝刈りなしで、70B の LLM を 4GB GPU 1 枚で動かせるとしている。<br>• README では 2.8T パラメータ級のモデルを 4GB 未満で動かす例も挙げている。<br>• 小さな VRAM での大規模モデルの学習にも対応したとしている。<br><br>推論時のメモリ使用量を大きく減らす仕組みとして連日トレンドに入っている。メモリを抑える代わりに速度がどの程度落ちるかは用途ごとに確認が必要だ。 | https://github.com/lyogavin/airllm |

## Hacker News

| # | タイトル | 要約 | URL |
|---|----------|------|-----|
| 1 | OpenAI、オフィス内で録音装置を発見 — (原文: OpenAI finds recording device in one of their offices) | • OpenAI の公式ニュースアカウントが、オフィスで録音装置を見つけたと X で発表した。<br>• 79 ポイントで当日の取得分で最多。<br>• SF Standard、Reuters、米司法省などが、役員会議室を盗聴した疑いで従業員が逮捕されたと報じた。<br><br>関連投稿が複数並び、SF Standard の記事にはコメントが 54 件付いた。AI 企業の機密情報をめぐる内部からの脅威が表に出た事例であり、動機や背景は今後の捜査や裁判で明らかになるとみられる。 | https://twitter.com/OpenAINewsroom/status/2110095403198849132 |
| 2 | 米国の制裁で打撃を受けた Huawei、Kirin チップの出荷が 1 億個を突破 — (原文: Huawei, once hobbled by US sanctions, passes 100M Kirin chip milestone) | • Huawei の自社設計チップ Kirin の累計が 1 億個に達したと SCMP が報じた。<br>• 米国の制裁で一時は大きく制約を受けていた。<br>• 14 ポイントを獲得した。<br><br>制裁下でも中国国内で半導体の供給網を立て直してきたことを示す数字として注目される。製造プロセスの詳細や性能面の比較は原文で確認したい。 | https://www.scmp.com/tech/big-tech/article/3370766/huawei-once-hobbled-us-sanctions-passes-100-million-kirin-chip-milestone |
| 3 | Parsimony — AI モデルが追加するコード量を測るオープンソースのベンチマーク — (原文: Show HN: Parsimony – an open-source benchmark for how much code AI models add) | • AI モデルが課題を解く際に、どれだけのコードを追加するかを測るベンチマーク。<br>• Show HN として公開され、10 ポイントを獲得した。<br>• オープンソースで提供されている。<br><br>正答率だけでなく、変更の小ささや無駄のなさを評価軸にする試み。AI が書くコードが膨らみがちだという問題意識に応えるもので、今後のモデル比較の観点として参考になる。 | https://parsimony.lasu.dev/ |
| 4 | Terence Tao 氏と数学、AI — (原文: The Tao of Tao) | • UCLA の雑誌が数学者 Terence Tao 氏を取り上げた記事。<br>• URL から、数学研究と AI の関わりを扱う内容とみられる。<br>• 8 ポイントを獲得した。<br><br>Tao 氏は AI を数学研究に取り入れる取り組みで知られる。第一線の研究者が AI をどう位置づけているかを知る読み物として注目された。 | https://newsroom.ucla.edu/magazine/terence-tao-math-artificial-intelligence-alpha-research |
| 5 | Trezor のウォレットにも不正な部品が仕込まれていた — (原文: Trezor Wallets Also Compromised with Implants) | • 暗号資産のハードウェアウォレット Trezor にも、不正なインプラントが見つかったとする記事。<br>• セキュリティ記者 Kim Zetter 氏のニュースレターで公開された。<br>• タイトルの「also」から、他製品に続く事例とみられる。<br><br>ハードウェアのサプライチェーンを狙う攻撃は、利用者側での検知が難しい。購入経路の確認など、利用者が取れる対策も含めて原文で確認しておきたい。 | https://www.zetter-zeroday.com/trezor-wallets-also-compromised-with-implants/ |
| 6 | 「会社全体の Claude Enterprise アカウントを停止させてしまった」 — (原文: I just got our entire company's Claude Enterprise account suspended) | • ある利用者が、自分の操作が原因で会社の Claude Enterprise アカウント全体が停止されたと X に投稿した。<br>• 7 ポイントを獲得した。<br>• 停止の理由や経緯は投稿元で確認が必要。<br><br>個人の利用が組織全体のアカウントに影響しうる点で、企業で AI サービスを導入する際の運用ルールを考える材料になる。事実関係は当事者の投稿のみであり、続報を待ちたい。 | https://twitter.com/heinenbros/status/2110081812169162923 |
| 7 | Google Play、誰でも自分専用の「バイブコーディング」アプリを作って Android で動かせるように — (原文: Google Play now lets anyone build private, vibe-coded apps that run on Android) | • Google Play が、自分だけのために作った非公開アプリに対応したと TechCrunch が報じた。<br>• AI との対話でアプリを作る「バイブコーディング」を想定している。<br>• 7 ポイントを獲得した。<br><br>アプリを作る人と使う人が同じという使い方を、プラットフォーム側が正式に支える動き。審査や安全性の担保がどうなるのかは原文で確認したい。 | https://techcrunch.com/2026/10/13/google-play-now-supports-private-vibe-coded-apps-built-just-for-you/ |
| 8 | オランダ税務当局、Microsoft 365 のクラウド導入を中止しオープンソースへ — (原文: Dutch tax authorities cancel Microsoft 365 cloud rollout and turn to open source) | • オランダの税務当局が Microsoft 365 のクラウド導入計画を中止したと ZDNet が報じた。<br>• 代わりにオープンソースのソフトウェアを採用する方針としている。<br>• 6 ポイントを獲得した。<br><br>欧州では、米国企業のクラウドへの依存を見直す「デジタル主権」の議論が続いている。行政機関での具体的な事例として、他国や他機関への波及が注目される。 | https://www.zdnet.com/business/dutch-tax-authorities-cancel-microsoft-365-cloud-rollout/ |

## InfoQ Japan

| # | タイトル | 要約 | URL |
|---|----------|------|-----|
| 1 | jQuery の 20 年：小さなライブラリが Web 開発を一変させた経緯 | • jQuery の 20 年の歩みを振り返る記事。<br>• 小さなライブラリが Web 開発のあり方を大きく変えた経緯を扱う。<br>• 著者は Daniel Curtis 氏。<br><br>ブラウザ間の差異を吸収する役割から始まり、その後の Web 標準やフレームワークにも影響を与えた。現在のフロントエンド開発の成り立ちを理解する読み物として参考になる。 | https://www.infoq.com/jp/news/2026/10/jquery-20-years/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global |
| 2 | Amazon CloudWatch Omni、CloudWatch をエージェント時代へ拡張 | • AWS が CloudWatch の新機能「CloudWatch Omni」を発表した。<br>• AI エージェントが使われる時代に向けて、監視基盤を拡張する内容。<br>• 著者は Sergio De Simone 氏。<br><br>エージェントの動作を観測する需要と、エージェントが監視データを扱う需要の両方が高まっている。具体的な機能範囲は原文で確認したい。 | https://www.infoq.com/jp/news/2026/10/aws-cloudwatchomni-observability/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global |
| 3 | Cloudflare Workers、受信 TCP 接続に対応　最初の対応プロトコルは gRPC | • Cloudflare Workers が、外部からの TCP 接続を受け付けられるようになった。<br>• 最初に対応するプロトコルは gRPC。<br>• 著者は Steef-Jan Wiggers 氏。<br><br>HTTP 中心だったエッジ実行環境の用途が広がる変更。gRPC を使うバックエンドサービスを Workers 上で動かす選択肢が増えることになる。 | https://www.infoq.com/jp/news/2026/10/workers-inbound-tcp-grpc/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global |
| 4 | Cloudflare、AI Search を拡張しカスタムデータの検索を容易に | • Cloudflare が AI Search に新機能を追加した。<br>• エージェントや開発者が独自のデータを検索しやすくする内容。<br>• 著者は Sergio De Simone 氏。<br><br>RAG などで独自データを扱う需要に、マネージドな検索基盤で応える動き。Workers の TCP 対応と合わせ、Cloudflare が AI 向けの開発基盤を広げていることがうかがえる。 | https://www.infoq.com/jp/news/2026/10/cloudflare-ai-search/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global |
| 5 | HashiCorp Packer 1.16、マシンイメージの SLSA Provenance をネイティブに生成・検証 | • Packer 1.16 で、マシンイメージの来歴情報（SLSA Provenance）を生成・検証できるようになった。<br>• 外部ツールなしで、標準機能として扱える。<br>• 著者は Claudio Masolo 氏。<br><br>ソフトウェアサプライチェーンの安全性を確保する取り組みが、コンテナだけでなく VM イメージにも広がっている。イメージの改ざん検知や監査への活用が期待される。 | https://www.infoq.com/jp/news/2026/10/hashicorp-packer-verification/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global |
| 6 | OpenTelemetry、企業向けオブザーバビリティの導入を簡素化する「Blueprints」を開始 | • OpenTelemetry が新たな取り組み「Blueprints」を始めた。<br>• 企業がオブザーバビリティを導入する際の手順を簡素化する狙い。<br>• 著者は Craig Risi 氏。<br><br>OpenTelemetry は標準として普及した一方、導入時の設計の難しさが課題とされてきた。参照構成のようなものが提供されれば、導入のハードルが下がると考えられる。 | https://www.infoq.com/jp/news/2026/10/opentelemetry-blueprints-launch/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global |
| 7 | Amazon Linux 2027、SELinux をデフォルトで強制モードにしてパブリックプレビュー開始 | • Amazon Linux 2027 のパブリックプレビューが始まった。<br>• SELinux がデフォルトで強制（enforcing）モードになる。<br>• 著者は Steef-Jan Wiggers 氏。<br><br>セキュリティを初期設定から強める方針の表れ。既存のアプリケーションが SELinux のポリシーで動かなくなる可能性もあるため、移行前の検証が重要になる。 | https://www.infoq.com/jp/news/2026/10/amazon-linux-2027-preview/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global |
| 8 | スキルとサブエージェントの選択に関する Azure とコミュニティのガイドライン | • AI エージェントの機能を「スキル」と「サブエージェント」のどちらで作るかについてのガイドラインを紹介する。<br>• Azure とコミュニティの双方の見解を扱う。<br>• 著者は Sergio De Simone 氏。<br><br>エージェントの設計で両者の使い分けは迷いやすい論点になっている。Zenn でもサブエージェントの見直しを扱う記事が読まれており、実務上の関心の高さがうかがえる。 | https://www.infoq.com/jp/news/2026/10/choosing-between-subagent-skills/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global |

## はてなブックマーク (tech)

| # | タイトル | 要約 | URL |
|---|----------|------|-----|
| 1 | NICT が注意喚起、相次ぐ情報漏えいの一因は「アプリ解析からのサーバ攻撃」 | • NICT が、公開アプリを解析してサーバを攻撃する手口への注意を呼びかけた。<br>• INTERNET Watch などはこの手口を「A2B 攻撃」と紹介し、Android アプリが一因と伝えている。<br>• 総務省も同じ趣旨の注意喚起を公表した。<br><br>はてなブックマーク 496 で当日最多となり、関連記事も多く読まれた。アプリ内に残った接続先や認証情報が悪用されうるため、アプリを公開している事業者は設計と運用を点検したい。 | https://www.nict.go.jp/press/2026/10/13-1.html |
| 2 | フランスのスーパー数百店舗で冷蔵設備にサイバー攻撃、温度が最高 50 度に上昇し食品を大量廃棄 | • フランスのスーパー数百店舗で、冷蔵設備がサイバー攻撃を受けたと ITmedia が報じた。<br>• 設備内の温度が最高 50 度まで上がったとしている。<br>• 食品が大量に廃棄される被害が出た。<br><br>IoT や設備制御への攻撃が、情報漏えいではなく物理的な損害につながった事例。店舗設備のネットワーク分離など、IT 部門以外の機器の管理も課題になる。 | https://www.itmedia.co.jp/news/article/2610/13/2000002201/ |
| 3 | Anthropic、自己複製 AI の「兆し」を指摘　55 ドルの TV ボックス 15 台で 26B モデルが稼働 | • Anthropic が、AI が自らを複製する能力の「兆し」を指摘したと ITmedia が報じた。<br>• 55 ドルの TV ボックス 15 台で 26B のモデルを動かした例が示されている。<br>• はてなブックマーク 280 を集めた。<br><br>安価な機器を束ねて大きなモデルを動かせる点が、自己複製のリスク評価と結びつけて論じられている。研究の前提や評価の方法は原文で確認したい。 | https://www.itmedia.co.jp/news/article/2610/13/2000002204/ |
| 4 | 楽天モバイルで情報漏えいのおそれ、過去の契約者も対象 | • 楽天モバイルで情報漏えいのおそれがあると ASCII が報じた。<br>• 過去に契約していた人も対象に含まれる。<br>• 楽天モバイルは「支払い証明書が第三者に閲覧された可能性」として公式に告知している。<br><br>同日は自治体の防災メールや「銀のさら」、キャッシュレスサービス「IDARE」など、情報漏えいの報道が相次いだ。該当する利用者は公式の案内を確認したい。 | https://ascii.jp/elem/000/004/442/4442187/ |
| 5 | 米 Getty Images が破産申請へ、AI 画像の台頭で経営が悪化 | • Getty Images が破産を申請する見通しだと ITmedia が報じた。<br>• AI による画像生成の広がりが経営悪化の一因とされる。<br>• 「報道写真」を軸に年内の再建を目指すとしている。<br><br>素材写真の市場が生成 AI の影響を大きく受けていることを示す出来事。著作権をめぐる AI 企業との係争との関係も含め、今後の再建の行方が注目される。 | https://www.itmedia.co.jp/news/article/2610/13/2000002234/ |
| 6 | PayPay 証券で障害、日本株の取引を停止　14 日の予約注文も停止 | • PayPay 証券で障害が起き、日本株の取引が停止したとテレビ朝日が報じた。<br>• 14 日分の予約注文も停止され、報道時点で復旧のめどは立っていない。<br>• NHK は、日本株と ETF の全銘柄が接続先の障害で停止したと伝えた。<br><br>外部の接続先の障害がサービス全体の停止につながった例とみられる。利用者は公式の案内で再開の状況を確認したい。 | https://news.tv-asahi.co.jp/news_economy/articles/000539845.html |
| 7 | 「Python 3.15」正式公開、UTF-8 が標準に　実験的な JIT コンパイラも強化 | • Python 3.15 が正式に公開された。<br>• UTF-8 が標準の文字エンコーディングになった。<br>• 「番兵値」などの新しい言語機能が加わり、実験的な JIT コンパイラも大きく強化された。<br><br>UTF-8 の標準化は、Windows などで起きていた文字コードの問題を減らすと期待される。既存のコードが暗黙のエンコーディングに頼っていないか、移行前に確認しておきたい。 | https://forest.watch.impress.co.jp/docs/news/2147319.html |
| 8 | 「パスキーは将来的にユーザーの自由を奪う可能性がある」との警告、その根拠と反論 | • パスキーが利用者の自由を損なう可能性があるとする警告を GIGAZINE が紹介した。<br>• 警告の根拠と、それに対する反論の両方を取り上げている。<br>• Microsoft のタグが付いており、特定企業のエコシステムへの依存が論点とみられる。<br><br>パスキーは安全性の高い認証方式として普及が進む一方、移行のしやすさや囲い込みへの懸念も指摘されている。賛否の両論を比べて判断する材料になる。 | https://gigazine.net/news/20261013-passkey-are-a-trap/ |

## Zenn

| # | タイトル | 要約 | URL |
|---|----------|------|-----|
| 1 | SQLite 本体にベクトル検索拡張「vec1」が登場 | • SQLite 本体にベクトル検索の拡張「vec1」が加わったことを紹介する記事。<br>• 著者は mattn 氏。<br>• Zenn で当日最多の 127 いいねを集めた。<br><br>組み込みデータベースだけでベクトル検索ができれば、小規模な RAG やローカルアプリの構成を簡単にできる。既存のサードパーティ拡張との違いは原文で確認したい。 | https://zenn.dev/mattn/articles/6e9996319ac099 |
| 2 | Haiku 5.5 を機に、Sonnet 以下で動かしていたサブエージェントの役割を見直した | • Claude Haiku 5.5 の登場をきっかけに、サブエージェントに割り当てるモデルを見直した事例。<br>• これまで Sonnet 以下のモデルで動かしていた役割を整理している。<br>• 71 いいねを獲得した。<br><br>小型モデルの性能が上がると、コストと品質のバランスでモデルを割り当て直す余地が生まれる。InfoQ のスキルとサブエージェントの使い分けの記事と合わせて読むと参考になる。 | https://zenn.dev/genda_jp/articles/haiku-5-5-subagent-roles |
| 3 | 若手エンジニアに必要だと感じた「AI を使う力」 | • 若手エンジニアに求められる「AI を使う力」について考えた記事。<br>• アイデアカテゴリで 71 いいねを獲得した。<br>• 現場での経験をもとにした考察とみられる。<br><br>AI ツールが当たり前になる中で、若手の育成で何を重視するかは多くの組織の課題になっている。教える側・学ぶ側の双方にとって考える材料になる。 | https://zenn.dev/muit_techblog/articles/6ea28887c79457 |
| 4 | Claude の新機能「Claude Motion」を早速使ってみた | • Claude の新機能「Claude Motion」を試した速報記事。<br>• 53 いいねを獲得した。<br>• 実際に使った印象をまとめている。<br><br>新機能の具体的な使い勝手を早く知りたい読者の関心を集めた。機能の正式な仕様や提供範囲は公式情報で確認したい。 | https://zenn.dev/branbran/articles/047821d64590f0 |
| 5 | AI で浮いた時間を「もっと作る」に使っていませんか | • AI で効率化して生まれた時間の使い方を問いかける記事。<br>• 浮いた時間をさらに多くのものを作ることに充てる傾向に疑問を投げかけている。<br>• 40 いいねを獲得した。<br><br>生産性の向上がそのまま仕事量の増加につながる問題は、AI 導入の議論でたびたび指摘される。働き方や開発の優先順位を考え直すきっかけになる内容だ。 | https://zenn.dev/idealog/articles/a3e9cf4299b1cf |
| 6 | 2025 年 10 月から 2026 年 10 月までの Mozc の主な変更 | • オープンソースの日本語入力エンジン Mozc の 1 年間の主な変更をまとめた記事。<br>• 対象期間は 2025 年 10 月から 2026 年 10 月。<br>• 35 いいねを獲得した。<br><br>Mozc は Linux などで広く使われる日本語入力の基盤。利用者や関連ソフトの開発者が、最近の変更をまとめて把握するのに役立つ。 | https://zenn.dev/komatsuh/articles/komatsuh_mozc_updates_from_2025_10 |
| 7 | GitLab を月 500 円で自社運用する、退役 PC と「出島サーバ」の構成 | • 使わなくなった PC を使い、GitLab を月 500 円程度で自社運用する構成を紹介する。<br>• 外部公開用の「出島サーバ」を組み合わせた構成としている。<br>• 24 いいねを獲得した。<br><br>小規模なチームがコストを抑えてソースコード管理を自前で持つための実践例。セキュリティ面の設計やバックアップの方法は原文で確認したい。 | https://zenn.dev/miyanaga/articles/zenn-2026-10-11 |
| 8 | 良いテストを書き、良いテストを見分ける ─『単体テストの考え方/使い方』のエッセンス | • 書籍『単体テストの考え方/使い方』の要点をまとめた記事。<br>• 良いテストの書き方と見分け方を扱う。<br>• 21 いいねを獲得した。<br><br>AI がテストコードを大量に生成できるようになった今、テストの良し悪しを判断する力の重要性は増している。テスト設計の考え方を短時間で確認したい人に向く。 | https://zenn.dev/nexta_/articles/unit-testing-principles-essence |

## Qiita

| # | タイトル | 要約 | URL |
|---|----------|------|-----|
| 1 | すでに Web デザイナーの 8 割は不要である | • 生成 AI の普及により、Web デザイナーの多くが不要になったと主張する記事。<br>• Qiita で当日最多の 128 いいねを集めた。<br>• タグは「#AI」のみで、意見を述べる性格の記事とみられる。<br><br>強い主張のタイトルが関心を集めた一方で、職種の将来をめぐっては異なる見方も多い。同じ著者による AI 時代の開発費についての記事も読まれている。 | https://qiita.com/kotowazaman/items/74621592ace2ff968670 |
| 2 | サイバーセキュリティを勉強するなら今？おすすめリソース紹介 | • サイバーセキュリティを学ぶためのおすすめリソースを紹介する記事。<br>• 118 いいねを獲得した。<br>• AI のタグも付いており、AI 時代の学び方にも触れているとみられる。<br><br>同日は NICT の注意喚起や情報漏えいの報道が相次ぎ、セキュリティへの関心が高まっている。これから学び始める人の入り口として参考になる。 | https://qiita.com/leolui2004/items/226062f17e55202e8c47 |
| 3 | 攻撃者は Web アプリのどこを狙う？ 初心者でもすぐできるセキュリティチェックリスト | • Web アプリで攻撃者に狙われやすい箇所を整理した記事。<br>• 初心者でもすぐ使えるチェックリストの形でまとめている。<br>• 71 いいねを獲得した。<br><br>個人開発や小規模なサービスでも、基本的な対策の抜けが被害につながる。公開前の点検項目として手元に置いておくと役立つ。 | https://qiita.com/Koukyosyumei/items/8aaa44ff15a3b404fd8b |
| 4 | 判断特化型の GraphRAG を Jev で構築（ベクトル未使用） | • ベクトル検索を使わずに、判断に特化した GraphRAG を構築した事例。<br>• Jev と AWS の DynamoDB を使っている。<br>• 47 いいねを獲得した。<br><br>RAG はベクトル検索が定番だが、関係性を重視するグラフ構造で代替する試みは増えている。用途に応じた構成の選択肢として参考になる。 | https://qiita.com/kikuziro/items/6191b5ad83520d181f38 |
| 5 | Microsoft セキュリティ、これをやってください！～ 実践ベストプラクティス | • Microsoft 環境のセキュリティで実施すべき対策をまとめた記事。<br>• Entra ID、Microsoft 365、Windows、パスキーなどを扱う。<br>• 36 いいねを獲得した。<br><br>Microsoft 製品を使う組織の管理者向けの実践的なまとめ。はてなブックマークで話題のパスキーをめぐる議論と合わせて読むと、認証方式を考える材料になる。 | https://qiita.com/carol0226/items/bdb16dbd5c16a2c43ad5 |
| 6 | 「私は Gemini。env の認証情報をうっかりチャットに漏らしました」— AI エージェント内側の告白 | • AI エージェントが環境変数の認証情報をチャットに出力してしまった事例を扱う記事。<br>• エージェント自身の視点で語る形式をとっている。<br>• 16 いいねを獲得した。<br><br>エージェントに環境へのアクセス権を与えると、意図しない形で秘密情報が漏れるおそれがある。同じ著者による API キーの扱いの検証記事と合わせて読みたい。 | https://qiita.com/songchong/items/f80fad42b5a134fa3c14 |
| 7 | AI エージェントに鍵を任せて大丈夫か — API キー操作を Claude Code・Codex・Gemini に 51 回頼んで検証 | • API キーに関わる 5 種類の操作を、Claude Code、Codex、Gemini に計 51 回依頼して比較した。<br>• やり方を「危険」「要注意」「安全」に分けて整理している。<br>• 13 いいねを獲得した。<br><br>エージェントに秘密情報を扱わせる際の具体的な指針を、実際の試行結果から導いている点が特徴。開発環境でエージェントを使う際の運用ルールづくりに役立つ。 | https://qiita.com/songchong/items/0d759f44eb26f332b897 |
| 8 | OpenAI の Decisions API を触ってみた | • OpenAI の「Decisions API」を試した記事。<br>• TypeScript と Node.js で動かしている。<br>• 16 いいねを獲得した。<br><br>新しい API を実際のコードで試した記録として、導入を検討する開発者の参考になる。API の正式な仕様や料金は公式ドキュメントで確認したい。 | https://qiita.com/hiroshi_ito9854/items/ff26fe2e239e23305f26 |
