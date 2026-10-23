# 技術ニュース要約 — 2026-10-24

## 📌 今日の3行サマリ

- 国内で個人情報の流出が相次いで報じられた。佐川急便は荷物問い合わせサービスへの不正アクセスで最大 5323 万件が流出した可能性を公表し、タイムズカーは免許証画像など約 146 万人分の流出を受けて 1 人 3000 円の見舞金を出すとした。パナソニック HD では、利用が禁じられた生成 AI に従業員らの情報 33 万人分が送られていたと報じられた。
- PHP の重大な脆弱性「PHP2Shell」の後始末が続いている。GitHub Trending に PHP 本体のリポジトリ（php/php-src）が入り、はてなではコドモンの対応の振り返りが 174 ブックマークを集めた。Ruby の正規表現エンジン Onigmo のリモートコード実行の問題や、Node.js の 10 月のセキュリティリリースへの対応記事も並んだ。
- Hacker News では、Google が Gmail や Google フォトのデータを広告のターゲティングに使う可能性があると報じた記事が 79 ポイントで最多だった。AI まわりでは、LiteLLM v1.107.0 のリリースに絡む攻撃の経緯の公開や、OpenAI が最先端モデルの学習環境の守り方を説明した記事も投稿された。

## GitHub Trending

| # | タイトル | 要約 | URL |
|---|----------|------|-----|
| 1 | php-src — PHP 本体のインタプリタ — (原文: php/php-src) | • Web 開発で広く使われるスクリプト言語 PHP の、インタプリタ本体のソースコード。<br>• 修正 BSD ライセンス（BSD-3-Clause）で配布されている。<br>• README では、ビルド済みのパッケージやバイナリの入手方法などを案内している。<br><br>PHP の重大な脆弱性「PHP2Shell」への対応が続くなか、本体のリポジトリが注目を集めたとみられる。自分で PHP をビルドしている環境では、修正の入ったバージョンになっているかを改めて確かめたい。 | https://github.com/php/php-src |
| 2 | Supabase — Postgres を土台にした開発プラットフォーム — (原文: supabase/supabase) | • 専用の Postgres データベースを用意し、Web、モバイル、AI アプリを作れるようにするプラットフォーム。<br>• Firebase のような機能を、企業向けのオープンソースの道具で作ることを目指している。<br>• 認証と認可、REST や GraphQL の API 自動生成、リアルタイム購読、Edge Functions、ファイル保存などを備える。<br><br>Firebase の代わりとして、自分でホストもできる選択肢として広く使われている。データベースが素の Postgres なので、SQL や既存の道具をそのまま生かしやすい。 | https://github.com/supabase/supabase |
| 3 | FastAPI — Python の型ヒントで API を作る Web フレームワーク — (原文: fastapi/fastapi) | • Python の標準の型ヒントを使って API を作る、モダンな Web フレームワーク。<br>• 高い性能と、学びやすさ、書きやすさ、本番での使いやすさを掲げている。<br>• 性能は NodeJS などに並ぶとうたう。<br><br>Python で API を作るときの定番の一つで、AI アプリのバックエンドとしてもよく使われる。性能の数字は開発元の説明なので、自分の用途で測って確かめたい。 | https://github.com/fastapi/fastapi |
| 4 | claude-howto — 図と例で学ぶ Claude Code のガイド — (原文: luongnv89/claude-howto) | • Claude Code の基本から高度なエージェントの使い方まで、図と例で解説するガイド。<br>• エージェントの連携、フック、スキル、MCP サーバーまでを扱い、コピーして使えるテンプレートを付けている。<br>• 英語、ベトナム語、中国語、ウクライナ語、日本語で読める。<br><br>コーディングエージェントの機能が増え、何から学べばよいか迷う人が増えている。自分の段階に合わせて読み進められる教材として関心を集めたとみられる。 | https://github.com/luongnv89/claude-howto |
| 5 | PCL — Minecraft のランチャー「Plain Craft Launcher」 — (原文: Meloong-Git/PCL) | • Minecraft の起動ツール「Plain Craft Launcher（PCL）」のソースコード。<br>• UI ライブラリ、アニメーション、ダウンロード、Minecraft の起動などのモジュールのほとんどを含む。<br>• コードは常に最新ではなく、PCL の更新が公開されるたびに同期される。<br><br>中国語圏のコミュニティで使われているランチャーで、機能の要望を投票で集める仕組みもある。説明は中国語が中心になっている。 | https://github.com/Meloong-Git/PCL |

## Hacker News

| # | タイトル | 要約 | URL |
|---|----------|------|-----|
| 1 | Google、Gmail や Google フォトのデータを広告のターゲティングに使う可能性 — (原文: Now Google says it might use your Gmail and Google Photos data to target ads) | • Google が、Gmail や Google フォトのデータを広告のターゲティングに使う可能性があると示した、と The Verge が報じた。<br>• URL からは、「Personal Intelligence」に関わるプライバシーポリシーの更新の話とみられる。<br>• 79 ポイント、コメント 26 件で、今回取得分の中で最多。<br><br>個人のメールや写真が広告に使われるかどうかは、利用者の関心が高い話題だ。実際に何が変わるのか、利用者が設定で止められるのかは、Google の公式の説明で確かめたい。 | https://www.theverge.com/tech/1017600/google-personal-intelligence-privacy-policy-ads-update |
| 2 | ソニー、日本で最後の 4K ブルーレイプレーヤーの販売を終了、残るは PS5 のみ — (原文: Sony Retires Its Last 4K Blu-ray Player in Japan, PS5 Is All That's Left) | • ソニーが、日本で最後に残っていた 4K ブルーレイプレーヤーの販売を終えたと TechPowerUp が報じた。<br>• 同社の製品で 4K ブルーレイを再生できるのは、PS5 だけになるという。<br>• 26 ポイント、コメント 16 件。<br><br>動画配信が広がり、ディスクで映像を見る機会は減っている。手元のディスクを今後どう再生するか、配信に移るかを考えるきっかけになりそうだ。 | https://www.techpowerup.com/354081/sony-retires-its-last-4k-blu-ray-player-in-japan-ps5-is-all-thats-left |
| 3 | Microsoft の新しい AI、病気の診断で医師の 2 倍以上の成績と発表 — (原文: New AI Is More Than Twice as Good at Diagnosing Diseases as Doctors) | • Microsoft が、新しい AI は病気の診断で医師より 2 倍以上よい成績を出したと説明している、と Gizmodo が報じた。<br>• 比べ方や対象の症例などの詳細は、タイトルからはわからない。<br>• 16 ポイント、コメント 10 件。<br><br>医療 AI の成績は、どんな条件で医師と比べたかで意味が大きく変わる。数字は開発元の発表に基づくので、評価の方法や第三者の検証を確かめる必要がある。 | https://gizmodo.com/microsoft-says-its-new-ai-is-more-than-twice-as-good-at-diagnosing-diseases-as-doctors-2000829562 |
| 4 | OpenAI、最先端モデルの学習環境の守り方を説明 — (原文: OpenAI: Securing our frontier model training environment) | • OpenAI が、最先端モデルを学習させる環境のセキュリティについて書いた記事。<br>• 学習環境やモデルの重みなどを、外からの攻撃や内部の不正から守る取り組みを説明したものとみられる。<br>• 14 ポイント、コメント 4 件。<br><br>モデルの能力が上がるほど、重みや学習の仕組みが盗まれたときの影響は大きくなる。AI 企業がどこまで守りを公開するかは、業界全体の基準づくりにも関わる。 | https://openai.com/index/securing-our-frontier-model-training-environment/ |
| 5 | 2 つの州で SNS の利用制限が可能に、これからやるべきこと（EFF） — (原文: Two States Can Now Restrict Social Media Access–Here's What to Do Next) | • 米国の 2 つの州で、SNS の利用を制限できるようになったことを受けた、電子フロンティア財団（EFF）の記事。<br>• タイトルからは、利用者や支援者が次に取れる行動を案内する内容とみられる。<br>• 10 ポイント、コメント 2 件。<br><br>未成年の保護などを理由にした SNS の規制は、年齢確認や表現の自由との関係で議論が続いている。対象の州や制限の中身は、元の記事で確かめたい。 | https://www.eff.org/deeplinks/2026/10/two-states-can-now-restrict-social-media-access-heres-what-do-next |
| 6 | Kimi K3.1 Pro で、オープンソース AI は最先端との差が 1 か月に — (原文: Kimi K3.1 Pro puts open-source AI a month behind the best) | • 中国の公開モデル「Kimi K3.1 Pro」により、オープンソースの AI と最先端のモデルとの差が 1 か月ほどに縮んだ、と論じる記事。<br>• 掲載先は modelcompare.ai のブログで、中国のオープンソース AI を扱っている。<br>• 8 ポイント、コメント 0 件。<br><br>公開モデルの性能が最先端に近づけば、自分の環境で動かす選択肢が広がる。「1 か月」という見積もりは記事の主張なので、比べたベンチマークの中身を確かめたい。 | https://www.modelcompare.ai/blog/china-open-source-ai |
| 7 | Tell HN: Claude CLI が終了しなくなった、Ctrl-C でも止まらない — (原文: Tell HN: Claude CLI doesn't exit anymore, not even with CTRL-C) | • Claude の CLI が終了しなくなり、Ctrl-C を押しても止まらない、と報告する投稿。<br>• 投稿の時点では一人の利用者の報告で、原因や影響の範囲はわからない。<br>• 5 ポイント、コメント 0 件。<br><br>同じ症状が出た場合は、別のターミナルからプロセスを止める方法を知っておくと安心だ。不具合であれば、更新や公式の告知を確かめたい。 | https://news.ycombinator.com/item?id=50214693 |
| 8 | LiteLLM v1.107.0 のリリースを狙った攻撃の経緯 — (原文: The attack chain behind the v1.107.0 LiteLLM release) | • LLM の API をまとめて扱うライブラリ LiteLLM の公式ブログが、v1.107.0 のリリースに絡む攻撃の経緯を説明した記事。<br>• URL からは、2026 年 10 月 21 日のセキュリティ事故についての報告とみられる。<br>• 3 ポイント、コメント 0 件。<br><br>AI アプリの多くが LiteLLM のようなライブラリに頼っており、配布物が狙われると影響が広がりやすい。該当するバージョンを入れていないか、公式の案内に沿って確かめたい。 | https://docs.litellm.ai/blog/security-incident-oct-21-2026-attack-chain |

## InfoQ Japan

| # | タイトル | 要約 | URL |
|---|----------|------|-----|
| 1 | AI を使ったソフトウェア開発：研究の成果を実践に移すチームの構成と能力 | • AI を使ったソフトウェア開発について、研究で得られた成果を現場の実践に移す方法を扱う記事。<br>• タイトルからは、そのために必要なチームの構成や能力を論じているとみられる。<br>• 筆者は Ben Linders。<br><br>AI ツールを入れただけでは、開発の成果が上がるとは限らない。チームの体制やスキルをどう整えるかを考える材料になりそうだ。 | https://www.infoq.com/jp/news/2026/10/AI-research-into-action/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global |
| 2 | Netflix、3 万件以上のストリーミングジョブにオープンソースの Flink オートスケーラーを導入 | • Netflix が、3 万件を超えるストリーミング処理のジョブで、オープンソースの Flink 用オートスケーラーの導入を進めている。<br>• Flink は、流れてくるデータを続けて処理するための仕組み。<br>• 筆者は Leela Kumili。<br><br>大量のジョブの処理能力を手作業で調整するのは難しく、負荷に合わせて自動で増減させる仕組みが欠かせない。大規模な運用の事例として、同じ課題を抱える組織の参考になる。 | https://www.infoq.com/jp/news/2026/10/netflix-flink-autoscaler/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global |
| 3 | Cloudflare Worker Previews：Workers 向けのブランチごとのプレビュー環境 | • Cloudflare が、Workers 向けにブランチごとのプレビュー環境を用意する「Worker Previews」を出した。<br>• ブランチごとに動く環境で、変更を本番に出す前に確かめられるとみられる。<br>• 筆者は Claudio Masolo。<br><br>プルリクエストごとに動作を確かめられると、レビューやテストがしやすくなる。URL には「agent」の語があり、AI エージェントによる開発との関わりも扱っている可能性がある。 | https://www.infoq.com/jp/news/2026/10/cloudflare-worker-agent/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global |

## はてなブックマーク (tech)

| # | タイトル | 要約 | URL |
|---|----------|------|-----|
| 1 | タイムズカーの免許証画像流出、約 146 万人に 1 人 3000 円の見舞金 | • タイムズカーの Web システムへの不正アクセスで、免許証の画像などが流出した問題の続報（第 5 報）。<br>• 約 146 万件で外部に送られた痕跡があり、対象者に 1 人 3000 円の見舞金を出すと報じられた。<br>• 日本経済新聞の記事が 272 ブックマークで最多。公式発表は 64、CNET の記事は 24 ブックマーク。<br><br>免許証の画像は本人確認に使われるため、なりすましに悪用されるおそれがある。対象の人は、身に覚えのない契約や連絡がないか注意したい。 | https://share.timescar.jp/news/2026/1023/1825.html |
| 2 | 佐川急便、流出した個人情報は最大 5300 万件超の可能性 | • 佐川急便の「お荷物問い合わせサービス」への不正アクセスで、最大 5323 万件の個人情報が流出した可能性があると公表された。<br>• 9 月末のサイバー攻撃の続報で、サービスは再開したという。<br>• NHK の記事が 243 ブックマーク。ITmedia（32）や INTERNET Watch（17）も報じた。<br><br>件数の規模が大きく、宅配を装った詐欺のメールや SMS が増えるおそれがある。届いた連絡のリンクをすぐに開かず、公式の窓口で確かめたい。 | https://news.web.nhk/newsweb/na/nd-20261023de64285 |
| 3 | パナソニック HD、利用禁止の生成 AI に従業員らの情報 33 万人分を送出 | • パナソニック HD で、利用が禁じられていた生成 AI に、従業員らの情報 33 万人分が送られていたと日本経済新聞が報じた。<br>• タグには AI、セキュリティ、個人情報などが付いている。<br>• 196 ブックマーク。<br><br>会社が認めていない AI ツールを社員が使う「シャドー AI」は、多くの組織が抱える課題だ。禁止するだけでなく、安全に使える代わりのツールを用意する対策も問われそうだ。 | https://www.nikkei.com/article/DGXZQOUF237Z60T21C26A0000000/ |
| 4 | PHP2Shell への対応を振り返って（コドモン） | • 保育施設向けのサービスを手がけるコドモンが、PHP の脆弱性「PHP2Shell」への対応を振り返った記事。<br>• タグには PHP、セキュリティ、マネジメントなどが付いている。<br>• 174 ブックマーク。<br><br>前日の pixiv の記事に続き、企業が緊急の対応をどう進めたかを公開する流れが続いている。ほかの組織にとっても、次の緊急対応に備える参考になる。 | https://tech.codmon.com/entry/2026/10/23/173909 |
| 5 | Mermaid 図を描ける Markdown エディター「MerMark Editor」が日本語に対応 | • Mermaid の図を描ける Markdown エディター「MerMark Editor」が、v0.8.1 から日本語で使えるようになった。<br>• 日本語化は有志の貢献によるもの。<br>• 91 ブックマーク。<br><br>Mermaid はテキストで図を書けるため、設計書や AI が作る資料でも使われる場面が増えている。日本語の画面で使えるようになり、試しやすくなった。 | https://forest.watch.impress.co.jp/docs/news/2150751.html |
| 6 | Ruby の正規表現エンジン「Onigmo」にリモートコード実行の問題、セキュリティ更新を公開 | • Ruby の正規表現エンジン「Onigmo」に、リモートでコードを実行されるおそれのある問題が見つかった。<br>• 修正版として Ruby v4.0.9、v3.4.12、v3.3.13 が公開された。<br>• GitLab が発見したという。54 ブックマーク。<br><br>Ruby で動く Web サービスは多く、外から受け取った文字列を正規表現で扱う場面も多い。使っているバージョンを確かめ、早めに更新したい。 | https://forest.watch.impress.co.jp/docs/news/2150800.html |
| 7 | 小説家になろう、第三者によるログインの恐れと今後の対応 | • 小説投稿サイト「小説家になろう」の運営ブログが、第三者にログインされた恐れがあることと今後の対応を知らせた。<br>• タイトルに「重要」と付いた告知。<br>• 54 ブックマーク。<br><br>ほかのサービスから流出したパスワードを使い回しで試す攻撃の可能性も考えられる。利用者はパスワードを変え、ほかのサービスと同じものを使わないようにしたい。 | https://blog.syosetu.com/article/view/article_id/5278/ |
| 8 | モスバーガー、流通済みのプリペイドカード情報約 57 万件が流出 | • モスバーガーで、すでに出回っているプリペイドカードの情報、約 57 万件が流出したと NHK が報じた。<br>• タグにはセキュリティなどが付いている。<br>• 39 ブックマーク。<br><br>プリペイドカードの情報が悪用されると、残高を勝手に使われるおそれがある。持っている人は、会社からの案内と残高を確かめたい。 | https://news.web.nhk/newsweb/na/nd-20261023de64388 |

## Zenn

| # | タイトル | 要約 | URL |
|---|----------|------|-----|
| 1 | バイブコーディングを 6 週間続けたら、Mac の起動に 20 分かかるようになった | • AI に任せてコードを書く「バイブコーディング」を 6 週間続けたところ、Mac の起動に 20 分かかるようになった体験を書いた記事。<br>• タイトルからは、原因を調べて直すまでの流れを扱っているとみられる。<br>• 68 いいねで、今回取得分の中で最多。<br><br>エージェントが入れた道具や常駐するプロセスが知らないうちに増えると、開発用のマシンが重くなる。ときどき中身を見直すことの大切さを示す例だ。 | https://zenn.dev/singularity/articles/vibe-coding-mac-boot-20min |
| 2 | 脆弱性管理の仕組みを整えた | • 開発チームで脆弱性を管理する仕組みを整えた経緯を書いた記事。<br>• 筆者は DRESS CODE の開発チーム。<br>• 66 いいね。<br><br>PHP2Shell をはじめ重大な脆弱性が続くなかで、見つけてから直すまでの流れを決めておく重要性が増している。自分のチームの体制を見直す参考になる。 | https://zenn.dev/dress_code/articles/be5550254695cd |
| 3 | セキュリティが心配なら Claude Code にコピペして聞くべき問いかけ 20 選 | • セキュリティが心配なときに、Claude Code にそのまま貼って使える問いかけを 20 個選んだ記事。<br>• AI に自分のコードや設定の危ない点を点検させる使い方とみられる。<br>• 39 いいね。<br><br>AI に点検させると手軽だが、見落としや誤った指摘もありうる。重要な部分は、人の確認や専用のツールと組み合わせたい。 | https://zenn.dev/yuiseki/articles/54b01670841898 |
| 4 | 10 月 21 日、PHP2Shell 対応の後片付けが終わらない | • PHP2Shell への緊急の対応のあと、後片付けが終わらない様子を書いた記事。<br>• タイトルの日付から、対応に追われた現場の記録とみられる。<br>• 12 いいね。<br><br>緊急の更新が済んでも、侵入の痕跡の確認や関係者への説明などの作業が残る。後片付けにかかる手間を見積もる参考になる。 | https://zenn.dev/subara3/articles/1165119ef70e75 |
| 5 | そのProvider、どこから更新する？ Flutter と Riverpod で考える操作完了の通知 | • Flutter の状態管理ライブラリ Riverpod で、操作が終わったことをどこから知らせるかを考える記事。<br>• Provider をどこから更新するのがよいかを扱っている。<br>• 7 いいね。<br><br>状態を更新する場所がばらばらになると、アプリの動きを追いにくくなる。設計の考え方として、Flutter の開発者の参考になる。 | https://zenn.dev/simplex/articles/dc17c45b57af0e |
| 6 | 「読みにくい DB」は AI 開発のコストを 1.9 倍にする — Claude Code で検証した DB 設計の影響 | • データベースの設計が読みにくいと、AI を使った開発のコストが 1.9 倍になった、という検証の記事。<br>• Claude Code を使って、DB の設計による違いを比べている。<br>• 6 いいね。<br><br>AI はテーブル名や列名から意味を読み取るため、わかりやすい設計は人にも AI にも効く。1.9 倍という数字は記事の条件での結果なので、そのまま当てはまるとは限らない。 | https://zenn.dev/actbe_tech/articles/8b4a9991d5365d |
| 7 | Rootless Docker と学ぶ SELinux【初心者向け】 | • root の権限なしで Docker を動かす「Rootless Docker」を題材に、SELinux を学ぶ初心者向けの記事。<br>• SELinux は、Linux でプロセスが触れる範囲を細かく制限する仕組み。<br>• 4 いいね。<br><br>コンテナを安全に動かすには、権限をできるだけ絞ることが大切だ。身近な題材で SELinux に入門できる記事になっている。 | https://zenn.dev/nexryai/articles/afb828d7dda6b7 |

## Qiita

| # | タイトル | 要約 | URL |
|---|----------|------|-----|
| 1 | 「ドパ資料」の作り方 | • 「ドパ資料」と呼ぶ資料の作り方を紹介する記事。<br>• タグには AI、ドパガキ、資料作成などが付いており、AI を使った資料づくりの話とみられる。<br>• 253 いいねで、今回取得分の中で最多。<br><br>AI で資料を作る人が増え、見せ方の工夫にも関心が集まっている。どんな資料を指すかは、元の記事で確かめたい。 | https://qiita.com/kikuziro/items/b6a0743b070d7320c36d |
| 2 | 古くさいと思っていた報連相を、PM になってから考え直した話 | • 古くさいと思っていた「報連相」を、プロジェクトマネージャーになってから考え直した経験を書いた記事。<br>• タグにはマネジメント、コミュニケーション、チーム開発などが付いている。<br>• 72 いいね。<br><br>立場が変わると、情報が届かないことの怖さに気づきやすい。新人や若手の開発者が、チームでの連絡の意味を考えるきっかけになる。 | https://qiita.com/fe1ix/items/d78130c065835a6343a5 |
| 3 | 【2026 年版】AI を駆使した開発手法をざっくりまとめた | • 2026 年時点の、AI を使った開発の手法をおおまかにまとめた記事。<br>• タグには生成 AI、AI エージェント、Claude Code などが付いている。<br>• 28 いいね。<br><br>AI 開発の手法は次々に生まれ、全体像をつかみにくくなっている。手法を見比べて、自分のチームに合うものを選ぶ入り口になる。 | https://qiita.com/kobori_slj/items/b9683ce90f4c26a6e7ae |
| 4 | 「PHP なんて使ってるやつが悪い」と言っている人が一番危ない | • PHP2Shell をきっかけに出た「PHP を使う方が悪い」という意見に反論する記事。<br>• タグには PHP、AI、セキュリティが付いている。<br>• 25 いいね。<br><br>どの言語やソフトにも脆弱性は見つかりうる。言語を責めるより、更新を早く回せる体制を整える方が大切だ、という問題提起とみられる。 | https://qiita.com/kotowazaman/items/aab621d31a8501617eb4 |
| 5 | パスワード管理ツールを調べた（1Password・Bitwarden） | • パスワード管理ツールの 1Password と Bitwarden について調べた記事。<br>• タグにはセキュリティ、パスワード管理が付いている。<br>• 21 いいね。<br><br>流出したパスワードを使い回しで試す攻撃が続くなか、サービスごとに違うパスワードを使うことは基本の対策だ。ツール選びの参考になる。 | https://qiita.com/kozakoza/items/534ca5aadd59bfd1f6b3 |
| 6 | Amazon Linux 2023 の PHP を CVE-2026-109618 の修正版へ先にビルドする | • Amazon Linux 2023 で、PHP の脆弱性 CVE-2026-109618 を直した版を、公式のパッケージを待たずに自分でビルドする方法の記事。<br>• タグには AWS、rpm などが付いている。<br>• 15 いいね。<br><br>OS の公式パッケージが出るまで待てないときの手段として役立つ。ただし自分でビルドした版は、その後の更新も自分で追う必要がある。 | https://qiita.com/amu-kuroneko/items/46f00fbe8b5bac009c1c |
| 7 | 【緊急】Node.js の重大な脆弱性に対応するセキュリティアップデートを安全に適用する方法 | • Node.js の重大な脆弱性に対応する更新を、安全に適用する手順を説明する記事。<br>• タグには npm、初心者などが付いており、慣れていない人向けの手順とみられる。<br>• 11 いいね。<br><br>Zenn にも Node.js の 10 月のセキュリティリリースへの対応記事が出ている。更新の前に、検証環境で動作を確かめたい。 | https://qiita.com/superdora-cloud/items/8cad27487cd0e67d088c |
| 8 | AI の「直しました」に証拠を付けさせる、pstack を Claude Code に入れてみた | • AI が「直しました」と言うときに証拠を付けさせるため、pstack を Claude Code に入れて試した記事。<br>• タグには Cursor、AI エージェントなども付いている。<br>• 11 いいね。<br><br>AI が修正したと言っても、本当に直ったかは確かめる必要がある。確認の手順を仕組みに組み込む試みとして参考になる。 | https://qiita.com/kobayashi-fuuki/items/a7fbba06bb158dae0e11 |
