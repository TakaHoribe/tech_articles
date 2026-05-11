# 自動運転開発者向け: 他社の製品技術動向おすすめ記事20選

調査日: 2026-05-11  
観点: 研究論文ではなく、商用運行・量産車・量産準備中の自動運転/ADAS製品が実際に採用しているMLモデル、車載アーキテクチャ、SoC/ECU、センサー構成を優先。

## 選定方針

- `index.html` 収録記事も含めるが、研究サーベイや論文中心の記事は除外。
- 公式ブログ、プレスリリース、製品ページを優先し、不足する場合のみ業界メディアを補助的に採用。
- 記事を読む価値は「何を作っているか」より「何を車両・サービスに載せる判断をしたか」に置く。

## 20記事

### 1. Waymo: Beginning fully autonomous operations with the 6th-generation Waymo Driver

- リンク: https://waymo.com/blog/2026/02/ro-on-6th-gen-waymo-driver/
- index.html: 収録済み (#6)
- 第6世代Waymo Driverを完全無人運行に投入する発表で、13カメラ、4 LiDAR、6レーダー、外部音響センサー、17MPカメラ、カスタムシリコンが具体的に説明されている。
- 方針は「センサー種を削らず、各センサーの性能と統合度を上げて個数・コストを下げる」マルチモーダル冗長設計。
- 軽量MLモデルによるセンサーごとの情報抽出、カメラ・LiDAR・イメージングレーダーの統合、車種横断で載せ替えるDriver設計が競合比較の基準になる。

### 2. Tesla: AI & Robotics

- リンク: https://www.tesla.com/AI
- index.html: 追加済み (#101)
- Tesla公式のAIページで、FSD向けAI推論チップ、カメラベースのニューラルネット、BEVネットワーク、車両フリート由来データの学習ループを確認できる。
- 製品としてはLiDAR/レーダーを前提にしないTesla Vision寄りで、カメラと車載AIコンピュータに賭けるアーキテクチャ。
- FSD v13系の詳細はリリースノート系情報も併読が必要だが、公式に確認できる採用思想としては「vision + neural nets + fleet learning + custom inference HW」が中核。

### 3. Wayve: Wayve Advances Embodied AI for Driving with NVIDIA DRIVE AGX Thor

- リンク: https://wayve.ai/thinking/wayve-gen-3/
- index.html: 追加済み (#102)
- WayveのGen 3 robot vehicle platformがNVIDIA DRIVE AGX Thor上に構築されることを示す記事。
- Wayve AI Driverはeyes-off L3とdriverless L4を目標に、E2E/Embodied AIを量産向け計算基盤へ載せる方向に進んでいる。
- WayveはHDマップ依存を下げ、汎化型ファウンデーションモデルを車両フリートで鍛える立場なので、Waymo型マルチセンサー/詳細運用設計との対比に向く。

### 4. Wayve: Driving the World, Sight Unseen: AI-500 Roadshow

- リンク: https://wayve.ai/thinking/ai-500-roadshow-90-cities/
- index.html: 追加済み (#103)
- 「1つのAIモデル、90都市、再学習なし」を掲げ、欧州・北米・アジアの未経験道路で汎化走行を検証した記事。
- 製品観点では、地域ごとのルール実装やHDマップ整備を減らし、単一モデルの汎化性能で展開速度を上げる戦略が見える。
- 意思決定者視点では、ODD拡張を「地図・ルール・都市別チューニング」で解くか「大規模モデルの汎化」で解くかの判断材料になる。

### 5. Wayve: GAIA-3, advancing world models from simulation to evaluation

- リンク: https://wayve.ai/press/wayve-launches-gaia3/
- index.html: 収録済み (#16)
- 15Bパラメータの生成ワールドモデルGAIA-3を、単なる動画生成ではなくE2E driving systemの評価・検証に使う発表。
- 実走で再現しにくい安全クリティカル条件を、制御可能で反復可能なシミュレーションに落とす製品開発パイプラインが主題。
- MLモデル本体だけでなく、評価基盤を生成AI化する流れを知る上で重要。

### 6. Aurora: Seeing with superhuman clarity

- リンク: https://aurora.tech/newsroom/seeing-with-superhuman-clarity-the-physics-and-architecture-behind-the
- index.html: 追加済み (#104)
- Aurora Driverの知覚システム解説で、FirstLight FMCW LiDAR、イメージングレーダー、高解像度カメラ、Mainline Perception、Remainder Explainer、Fault Managementが出てくる。
- 現行FirstLightは450m超、次世代は1000m検出を目指すとされ、高速L4トラックに必要な長距離認識の要件が明確。
- 高速道路トラックは都市ロボタクシーと異なり、遠距離・低反射物・悪天候・グレアに対するセンサー物理が製品差になることが分かる。

### 7. Aurora, Continental, and NVIDIA Partner to Deploy Driverless Trucks at Scale

- リンク: https://ir.aurora.tech/news-events/press-releases/detail/112/aurora-continental-and-nvidia-partner-to-deploy
- index.html: 収録済み (#20)
- Aurora Driverの量産展開で、NVIDIA DRIVE Thorをデュアル構成で採用し、Continentalが2027年量産ハードウェアを担う計画。
- AuroraはVerifiable AIとSafety Caseを前面に出し、AI導入と安全説明可能性をセットで製品化している。
- 自社開発スタックをTier 1量産ECU/SoCに載せる際の分業モデルとして読む価値が高い。

### 8. Gatik: Gatik and NVIDIA Collaborate on Autonomous Trucks

- リンク: https://gatik.ai/news/press-releases/gatik-collaboration-with-nvidia/
- index.html: 収録済み (#31)
- GatikがClass 6/7の中距離商用無人トラックにNVIDIA DRIVE AGXを採用する発表。
- 顧客はWalmart、Kroger、Tyson Foodsなどで、閉じたB2B物流ODDに絞ってL4を量産展開する戦略が見える。
- 長距離Class 8のAuroraと比較すると、商用化はODD制約、車両クラス、顧客運用の絞り込みで前倒しできることが分かる。

### 9. Nuro: Nuro Driver

- リンク: https://www.nuro.ai/nuro-driver
- index.html: 追加済み (#105)
- Nuro Driverの製品ページで、E2E AIモデル、ガードレール、AI-driven mapping、LiDAR/レーダー/カメラ、独自ECU、NVIDIA Thor採用がまとまっている。
- 第4世代ハードウェアはL4用途を前提に、ソフトウェアとセンサー統合をライセンス可能な汎用自動運転プラットフォームとして設計。
- 「ロボタクシー企業」ではなく、OEM/モビリティ事業者にDriverとToolkitをライセンスする方向性が重要。

### 10. Nuro / Lucid / Uber: Next-Generation Autonomous Robotaxi Program

- リンク: https://www.nuro.ai/blog/lucid-nuro-and-uber-partner-on-next-generation-autonomous-robotaxi-program
- index.html: 追加済み (#106)
- Uberが6年間で2万台以上のLucid車両にNuro Driverを載せる計画を示す提携発表。
- 車両はLucid、運行ネットワークはUber、自動運転スタックはNuroという分業型ロボタクシー構造。
- Waymoの垂直統合モデルと対照的に、AV Driverを部品化して大規模プラットフォームに供給するモデルとして重要。

### 11. NVIDIA: DRIVE AGX Hyperion 10 / Uber partnership

- リンク: https://nvidianews.nvidia.com/news/nvidia-uber-robotaxi
- index.html: 追加済み (#107)
- DRIVE AGX Hyperion 10をL4-readyなリファレンス計算・センサーアーキテクチャとして位置付け、Uberの10万台規模ロボタクシー構想に接続する発表。
- 2基のDRIVE AGX Thor、Blackwell、各1,000 TOPS INT8、VLA/生成AIワークロード最適化、CosmosベースのAI data factoryが要点。
- AV企業ごとの専用ハードから、互換性のある量産リファレンスHW + AVソフトの時代に移る兆候として読むべき。

### 12. Qualcomm / BMW: Snapdragon Ride Pilot

- リンク: https://www.qualcomm.com/news/releases/2025/09/qualcomm-and-bmw-group-unveil-groundbreaking-automated-driving-s
- index.html: 追加済み (#108)、関連記事あり (#44は外部解説)
- BMW iX3 Neue Klasseに搭載されるSnapdragon Ride Pilotの公式発表。
- 8MP/3MPカメラ、レーダー、HD map、GNSS、V2X 200、Snapdragon Ride SoC、BEV低レベル知覚、AI+ルールベース計画、データ/シミュレーションファクトリが具体的。
- L2+/都市NOAを量産乗用車へ広く展開するための、コストと性能を両立した中央コンピュートADASの代表例。

### 13. Mobileye: Mobileye's new ECU Series: Modularity from ADAS to AV

- リンク: https://www.mobileye.com/blog/modularity-from-adas-to-av/
- index.html: 追加済み (#109)
- EyeQ6Hを2基載せた共通プライマリボードとMCUを中核に、SuperVisionからChauffeurまで段階的に拡張するECUシリーズ。
- SuperVisionは11カメラ+任意レーダーのhands-off/eyes-on、Chauffeurは追加EyeQ6Hボードとレーダー/LiDAR層でhands-off/eyes-offへ拡張。
- OEMにとって検証済み基盤を使い回しながら自動化レベルを上げる「モジュラーECU戦略」が分かる。

### 14. Mobileye: Chauffeur

- リンク: https://www.mobileye.com/solutions/chauffeur/
- index.html: 追加済み (#110)
- Mobileye Chauffeurの公式製品ページで、REM、EyeQ6 High、True Redundancy、RSS、カメラ系とレーダー/LiDAR系の独立冗長構成を確認できる。
- サンプル構成は8MPカメラ群、2MP短距離サラウンドカメラ、フロントLiDAR、サラウンド/イメージングレーダー、最大4基のEyeQ6 Highへ拡張。
- 地理的スケールをHDマップではなくREMのクラウドソース地図で支える点が、Waymo/Wayve/Teslaと異なる。

### 15. Pony.ai: Gen-7 Robotaxi Lineup

- リンク: https://ir.pony.ai/news-releases/news-release-details/pony-ai-inc-unveils-seventh-generation-robotaxi-lineup-targets/
- index.html: 追加済み (#111)
- 第7世代RobotaxiをToyota、BAIC、GACと公開し、2025年中盤から量産を狙う発表。
- 100% automotive-grade ADK、前世代比でBOM 70%削減、計算ユニット80%削減、ソリッドステートLiDAR 68%削減と、量産コストの数字が具体的。
- L4の技術成熟だけでなく、ADKの車載グレード化とBOM削減がスケールの主戦場になっていることが分かる。

### 16. WeRide: HPC 3.0 Platform Powered by NVIDIA DRIVE AGX Thor

- リンク: https://ir.weride.ai/news-releases/news-release-details/weride-teams-lenovo-launch-100-automotive-grade-hpc-30-platform
- index.html: 追加済み (#112)、関連情報あり (#26の概要内で言及)
- WeRideとLenovoが、NVIDIA DRIVE AGX Thorを使った100% automotive-gradeのHPC 3.0を発表。
- Robotaxi GXRに搭載される量産L4向けプラットフォームで、デュアルThor、DriveOS、Lenovo AD1 L4 domain controller、最大2,000 TOPSが要点。
- 中国勢のロボタクシーが、独自SoCよりもNVIDIA Thor + Tier 1/ODMドメインコントローラで量産速度を取る動きとして重要。

### 17. Li Auto: MindVLA autonomous driving architecture

- リンク: https://cnevpost.com/2025/03/18/li-auto-unveils-mindvla-autonomous-driving-architecture/
- index.html: 収録済み (#34)
- MindVLAはVision-Language-Action大型モデルとして、空間・言語・行動知能を単一モデルに統合するLi Autoの次世代自動運転アーキテクチャ。
- E2EとVLMを単純に足すのではなく、3D空間理解、論理推論、行動生成を統合してL4へ進む設計思想。
- 中国OEMが量産車向けADASを「VLA/Physical AI」へ再定義している流れを追う上で必読。

### 18. XPENG: VLA 2.0 public-road testing and 2027 delivery plan

- リンク: https://www.xpeng.com/pressroom/news/019cae5e67b99c0960ee8a028129016a
- index.html: 追加済み (#113)、関連記事あり (#35)
- XPENG VLA 2.0は、従来のvision-language-action逐次パイプラインではなく、vision-to-actionのE2E構造を掲げる。
- Robotaxi、乗用車、ヒューマノイド、飛行体まで同一基盤を広げるPhysical AI戦略の一部として説明されている。
- 中国OEMのVLA競争では、言語推論を中間に置く設計から、直接行動生成する設計への揺り戻しが見える。

### 19. BYD: God's Eye / DiPilot ADAS suite

- リンク: https://paultan.org/2025/02/13/byd-unveils-gods-eye-dipilot-adas-suite-to-roll-out-in-all-byd-denza-yangwang-models-sold-in-china/
- index.html: 追加済み (#114)
- BYDがGod's Eye/DiPilotを中国販売モデルへ広く展開する動きで、最廉価帯まで高度ADASを下ろす価格破壊が主題。
- God’s Eye CはDiPilot 100、12カメラ、5ミリ波レーダー、12超音波レーダーで、上位グレードはLiDARを含む構成。
- 技術最先端というより、センサー/ECU構成を大衆車価格へ落とし込む量産戦略として重要。

### 20. Renesas: R-Car X5H 3nm multi-domain SoC

- リンク: https://www.renesas.com/en/about/newsroom/renesas-unveils-industry-s-first-automotive-multi-domain-soc-built-3-nm-process-technology
- index.html: 収録済み (#45)
- ADAS、IVI、ゲートウェイを単一SoCで統合する3nmマルチドメインSoCで、400 TOPS AI、32 Arm Cortex-A720AE、ASIL D対応R52、チップレット拡張が要点。
- 車両E/Eアーキテクチャは、分散ECUから中央/ゾーン/マルチドメイン統合へ移行しており、その受け皿となる半導体。
- AVソフト単体ではなく、電力、冷却、混在安全、OTA、将来拡張を含む車載コンピュート設計の参考になる。

## おすすめの読み順

1. L4ロボタクシー/トラックの現実解: Waymo、Aurora、Pony.ai、WeRide、Nuro
2. 量産乗用ADAS/Consumer AV: Qualcomm/BMW、Mobileye、BYD、Li Auto、XPENG
3. 基盤技術: NVIDIA Hyperion 10、Renesas R-Car X5H、Wayve GAIA-3

## ざっくり技術トレンド

- L4は「カメラのみ」より、カメラ + LiDAR + イメージングレーダー + 冗長計算の採用が主流。Waymo、Aurora、Nuro、Pony.ai、WeRideはこの方向。
- 量産L2+/L3は、コスト別にカメラ/レーダー中心からLiDAR追加まで段階化する構成が主流。Qualcomm/BMW、Mobileye、BYDが典型。
- MLモデルはE2E、VLA、ワールドモデルへ寄っているが、製品では安全ガードレール、冗長センサー、Safety Case、OTA、データ/シミュレーションファクトリとセットで採用される。
- 車載HWはNVIDIA Thor、Mobileye EyeQ6H、Qualcomm Snapdragon Ride、Renesas R-Car X5Hのような中央/マルチドメインSoCへ集約が進んでいる。
- 中国勢はVLAと量産コスト低減が速い。米欧勢はSafety Case、冗長性、運用設計、量産パートナーシップを重視している。
