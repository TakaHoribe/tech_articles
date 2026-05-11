# 自動運転・関連技術 おすすめ記事100選 (2024-2026)

> 収集日: 2026-05-07 | ステータス: 完成 (100件)

## カテゴリ凡例
- 🚗 自動運転企業ブログ・レポート
- 🤖 AI・機械学習・モデルアーキテクチャ
- 💡 シミュレーション・合成データ
- 🔧 チップ・ハードウェア・SoC
- 📡 センサー技術（LiDAR, Radar, Camera）
- 🌐 業界動向・規制・市場

---

## 🚗 Waymo (9件)

| # | タイトル | 年 | ★ | 概要 |
|---|---------|-----|-----|------|
| 1 | [Demonstrably Safe AI For Autonomous Driving](https://waymo.com/blog/2025/12/demonstrably-safe-ai-for-autonomous-driving/) | 2025 | ⭐⭐⭐⭐⭐ | Waymo Foundation Modelを中心に、Driver・Simulator・Criticが同一AIで動く安全エコシステムを解説。自動運転AIの設計思想として必読の公式ブログ。 |
| 2 | [EMMA: End-to-End Multimodal Model for Autonomous Driving (arXiv)](https://arxiv.org/abs/2410.23262) | 2024 | ⭐⭐⭐⭐⭐ | GeminiベースのE2E自動運転モデル。センサーデータから直接軌跡を生成し、Chain-of-Thoughtで計画精度6.7%向上。業界パラダイムシフトを示す最重要論文の一つ。 |
| 3 | [Introducing EMMA (Waymo公式ブログ)](https://waymo.com/blog/2024/10/introducing-emma/) | 2024 | ⭐⭐⭐⭐⭐ | EMMAの概要と背景を分かりやすく解説した公式ブログ版。マルチモーダルLLMで自動運転を統一するアプローチの意義を説明。 |
| 4 | [Behind the Innovation: AI & ML at Waymo](https://waymo.com/blog/2024/10/ai-and-ml-at-waymo/) | 2024 | ⭐⭐⭐⭐ | WaymoのAI/ML技術全体像。複雑な交通パターンや他ドライバーの意図解釈まで含むWaymo Driverの開発アプローチを解説。 |
| 5 | [Meet the 6th-Generation Waymo Driver](https://waymo.com/blog/2024/08/meet-the-6th-generation-waymo-driver/) | 2024 | ⭐⭐⭐⭐⭐ | 第6世代Waymo Driverの詳細。センサー数42%削減、17MPカメラ、コスト$20,000以下を達成。ハードウェアスケーリング戦略の好事例。 |
| 6 | [Beginning Fully Autonomous Operations with the 6th-Gen Waymo Driver](https://waymo.com/blog/2026/02/ro-on-6th-gen-waymo-driver/) | 2026 | ⭐⭐⭐⭐⭐ | 6世代ドライバーで完全自律運転開始。週100万ライド目標。新センサー設計（13カメラ/4LiDAR/6レーダー）の技術的詳細。 |
| 7 | [Safe, Routine, Ready: Autonomous Driving in Five New Cities](https://waymo.com/blog/2025/11/safe-routine-ready-autonomous-driving-in-new-cities/) | 2025 | ⭐⭐⭐⭐ | Miami, Dallas等5都市への展開発表。地理的スケーリングの技術的課題と対処法を解説。 |
| 8 | [Comparison of Waymo Rider-Only Crash Rates at 56.7M Miles](https://www.tandfonline.com/doi/full/10.1080/15389588.2025.2499887) | 2025 | ⭐⭐⭐⭐⭐ | 5670万マイルのデータで人間ドライバーと比較。重傷事故91%減・歩行者事故92%減を査読論文として発表。安全性の科学的実証として業界最重要データ。 |
| 9 | [WOMD-LiDAR: Raw Sensor Dataset for Motion Forecasting](https://waymo.com/research/womd-lidar/) | 2024 | ⭐⭐⭐⭐ | 10万シーン以上の高品質LiDARデータを含むモーション予測データセット。研究コミュニティへの貢献として価値大。 |

---

## 🚗 Tesla (3件)

| # | タイトル | 年 | ★ | 概要 |
|---|---------|-----|-----|------|
| 10 | [Tesla's Neural Network Revolution: How FSD Replaced 300K Lines of Code with AI](https://www.fredpope.com/blog/machine-learning/tesla-fsd-12) | 2024 | ⭐⭐⭐⭐⭐ | FSD v12でC++コード30万行をE2Eニューラルネットに完全置換した革命的アーキテクチャ変更を解説。業界の方向性を示す最重要事例。 |
| 11 | [Tesla FSD v13.2 Rolling Out – Full Self-Driving Update](https://www.autopilotreview.com/full-self-driving-update/) | 2024 | ⭐⭐⭐⭐ | HW4向けFSD v13の詳細。重要介入間マイル数の大幅改善。実走行データに基づくE2Eモデルの性能指標追跡に有用。 |
| 12 | [What Tesla's Optimus Robot Can Do in 2025 and Where It Still Lags](https://interestingengineering.com/culture/can-optimus-make-america-win) | 2025 | ⭐⭐⭐ | Tesla Optimusの現状と限界。自動運転AIの物理世界への展開として自動運転技術との関連性あり。現実的な評価視点が有用。 |

---

## 🚗 Wayve (5件)

| # | タイトル | 年 | ★ | 概要 |
|---|---------|-----|-----|------|
| 13 | [Crossing the Pond and Beyond: Generalizable AI Driving for Global Deployment](https://wayve.ai/thinking/multi-country-generalization/) | 2025 | ⭐⭐⭐⭐⭐ | 欧州・北米・日本500都市以上でゼロショット走行を実現した汎化技術。Embodied AIの地理的汎化性能として業界最先端の事例。 |
| 14 | [GAIA-2: A Controllable Multi-View Generative World Model for AD (arXiv)](https://arxiv.org/abs/2503.20523) | 2025 | ⭐⭐⭐⭐⭐ | マルチカメラ対応の制御可能なビデオ生成ワールドモデル。エッジケース生成・テスト・合成データ生成を統合。ワールドモデル研究の最前線。 |
| 15 | [GAIA-2: Pushing the Boundaries of Video Generative Models (Wayve公式)](https://wayve.ai/thinking/gaia-2/) | 2025 | ⭐⭐⭐⭐⭐ | GAIA-2の開発背景と実用的な意義を解説。天候・照明・道路構成の制御、レアシナリオ生成のユースケース詳述。 |
| 16 | [Wayve Launches GAIA-3: Advancing World Models from Simulation to Evaluation](https://wayve.ai/press/wayve-launches-gaia3/) | 2025 | ⭐⭐⭐⭐⭐ | GAIA-3発表。シミュレーションから評価まで一貫したフレームワーク。自動運転ワールドモデル研究の最前線。 |
| 17 | [Wayve Science: Advancing AI Research in Autonomous Driving](https://wayve.ai/science/) | 2025 | ⭐⭐⭐⭐ | SimLingo（2025年3月）等Wayveの研究成果ページ。VLAモデル統合の先進研究事例。 |

---

## 🚗 Aurora (3件)

| # | タイトル | 年 | ★ | 概要 |
|---|---------|-----|-----|------|
| 18 | [Aurora Becomes First Company to Deploy Class 8 Self-Driving Trucks on US Roads](https://electrek.co/2025/05/01/aurora-first-company-deploy-class-8-self-driving-trucks-us-public-roads-video/) | 2025 | ⭐⭐⭐⭐⭐ | 米国初のClass 8自動運転トラック公道走行開始。商用Level 4の歴史的マイルストーン。Fort Worth〜El Paso間600マイル。 |
| 19 | [Progress in 2024: Readying for Commercial Launch](https://aurora.tech/newsroom/progress-in-2024-readying-for-commercial-launch) | 2024 | ⭐⭐⭐⭐ | 商用ローンチに向けた技術進歩を総括。Verifiable AI、360度センサーアレイ、安全ケース構築プロセスを解説。 |
| 20 | [Aurora, Continental, and NVIDIA Partner to Deploy Driverless Trucks at Scale](https://ir.aurora.tech/news-events/press-releases/detail/112/aurora-continental-and-nvidia-partner-to-deploy-driverless-trucks-at-scale) | 2025 | ⭐⭐⭐⭐ | Aurora・Continental・NVIDIAのDRIVE Thor採用パートナーシップ。2027年Continental量産を目指す3社協業の詳細。 |

---

## 🚗 Zoox (2件)

| # | タイトル | 年 | ★ | 概要 |
|---|---------|-----|-----|------|
| 21 | [Zoox Unveils Robotaxi Powered by NVIDIA](https://blogs.nvidia.com/blog/zoox-autonomous-robotaxi-powered-by-nvidia/) | 2024 | ⭐⭐⭐⭐⭐ | ステアリングホイール・ペダルなし専用設計EV「Zoox」の技術詳細。4輪ステアリングによる超小回りと乗客安全設計を解説。 |
| 22 | [Zoox Has Officially Begun Offering Free Robotaxi Rides in Las Vegas](https://electrek.co/2025/09/10/zoox-free-driverless-robotaxi-rides-general-public-vegas/) | 2025 | ⭐⭐⭐⭐ | ラスベガスで一般公開の無人ロボタクシー開始。専用設計EVの初商用運行事例。2Mマイル・35万乗客達成。 |

---

## 🚗 Baidu Apollo (3件)

| # | タイトル | 年 | ★ | 概要 |
|---|---------|-----|-----|------|
| 23 | [Baidu Apollo Launches 6th-Gen Robotaxi with 60% Lower Cost](https://cnevpost.com/2024/05/15/baidu-apollo-launches-6th-gen-robotaxi/) | 2024 | ⭐⭐⭐⭐⭐ | 第6世代ロボタクシーRT6発表。製造コスト60%削減（$27,670）。中国自動運転のコスト革新と量産スケーリングの好事例。 |
| 24 | [How Baidu's Apollo Go Targets Global Robotaxi Expansion](https://technologymagazine.com/articles/how-baidus-apollo-go-targets-global-robotaxi-expansion/) | 2025 | ⭐⭐⭐⭐ | 中国4大一線都市で完全無人商用運行承認。ドバイ・アブダビへの国際展開も解説。Q2 2025で148%成長。 |
| 25 | [Technical Analysis of Baidu Apollo Autonomous Driving Data Open Platform](https://www.oreateai.com/blog/technical-analysis-of-baidu-apollo-autonomous-driving-data-open-platform/) | 2024 | ⭐⭐⭐ | Apolloオープンデータプラットフォームの技術解析。データパイプライン設計とオープンソース戦略。 |

---

## 🚗 Pony.ai / WeRide (2件)

| # | タイトル | 年 | ★ | 概要 |
|---|---------|-----|-----|------|
| 26 | [China's L4 Companies Pony.ai and WeRide Go Public in Hong Kong](https://carnewschina.com/2025/11/06/chinas-l4-autonomous-driving-company-pony-ai-and-weride-go-public-in-hong-kong-shares-dip-over-10/) | 2025 | ⭐⭐⭐⭐ | Pony.aiとWeRideのHKEX・Nasdaq上場。WeRide HPC 3.0（NVIDIA Thor採用、TCO84%削減）等の最新技術情報も含む。 |
| 27 | [Japan's AV Revolution & WeRide's, Pony.ai's Expansion Strategy](https://avmarketstrategist.substack.com/p/av-market-update-cw-12) | 2025 | ⭐⭐⭐⭐ | 日本の自動運転市場革命とWeRide・Pony.aiの拡張戦略。欧州（Bolt提携）・日本・中東展開の詳細分析。 |

---

## 🚗 Nuro (2件)

| # | タイトル | 年 | ★ | 概要 |
|---|---------|-----|-----|------|
| 28 | [Autonomy for All: Nuro Expands Business Model to All Roads, All Rides](https://www.nuro.ai/blog/autonomy-for-all-nuro-expands-business-model-to-all-roads-all-rides) | 2024 | ⭐⭐⭐⭐ | デリバリーロボットからADシステムライセンス事業へのピボット。Foundation ModelベースのNuro Driverの技術詳細（1.7M自動運転マイル無過失）。 |
| 29 | [Nuro's $106M Raise Backs Its Shift from Delivery Robots to Licensing Autonomy Tech](https://techcrunch.com/2025/04/09/nuros-106m-raise-backs-its-shift-from-delivery-robots-to-licensing-autonomy-tech/) | 2025 | ⭐⭐⭐⭐ | Uber・Lucid MotorsとのL4ロボタクシーフリート構築。ADシステムライセンスビジネスモデルの具体的展開事例。 |

---

## 🚗 Gatik (2件)

| # | タイトル | 年 | ★ | 概要 |
|---|---------|-----|-----|------|
| 30 | [Gatik Becomes First U.S. Company to Operate Fully Driverless Trucks at Scale](https://www.businesswire.com/news/home/20260127742958/en/Gatik-Becomes-First-U.S.-Company-to-Operate-Fully-Driverless-Trucks-at-Scale-for-Commercial-Deliveries) | 2026 | ⭐⭐⭐⭐⭐ | 米国初の商用完全無人トラック大規模運行。60,000件の無人配送オーダーを無事故で完遂。中距離自動運転トラックの商用化事例。 |
| 31 | [Gatik and Isuzu Team Up to Mass-Produce L4 Autonomous Trucks Powered by NVIDIA](https://gatik.ai/news/blog/gatik-isuzu-mass-production-powered-by-nvidia/) | 2025 | ⭐⭐⭐⭐ | Isuzu・NVIDIAとのL4量産トラック協業。DRIVE AGX Thor採用。TIMEベスト発明2025選出のGatik Driver詳細。 |

---

## 🚗 Mobileye (2件)

| # | タイトル | 年 | ★ | 概要 |
|---|---------|-----|-----|------|
| 32 | [Bridging to the Autonomous Future with Mobileye SuperVision](https://www.mobileye.com/blog/mobileye-supervision-bridge-to-consumer-autonomous-vehicles/) | 2024 | ⭐⭐⭐⭐ | SuperVisionの全路種ハンズオフ走行技術の解説。11カメラ・EyeQ SoC・REM地図統合の設計思想。消費者向けAVへの橋渡し戦略。 |
| 33 | [Unveiling Surround ADAS: A New Standard of Safety and Tech](https://www.mobileye.com/blog/how-surround-adas-delivers-the-new-standard-of-safety-and-tech/) | 2025 | ⭐⭐⭐⭐ | 次世代Surround ADASの詳細。VW Group向け1900万台確定受注。SuperVisionとの違いと都市走行への拡張を解説。 |

---

## 🚗 中国EV各社 (Li Auto / Xpeng / NIO) (3件)

| # | タイトル | 年 | ★ | 概要 |
|---|---------|-----|-----|------|
| 34 | [Li Auto Unveils MindVLA Architecture to Move Toward Truly Autonomous Driving](https://cnevpost.com/2025/03/18/li-auto-unveils-mindvla-autonomous-driving-architecture/) | 2025 | ⭐⭐⭐⭐⭐ | 空間・言語・行動知能を統合したMindVLAアーキテクチャ発表。L4自動運転への最重要ステップとして位置付け。E2E+VLM+VLAの実装例。 |
| 35 | [Xpeng to Roll Out VLA 2.0 Across Its Models](https://eletric-vehicles.com/xpeng/xpeng-to-roll-out-vla-2-0-across-its-models-in-march-launches-three-suv-facelifts/) | 2025 | ⭐⭐⭐⭐⭐ | VLA 2.0のL4自動運転開発とVolkswagen採用。70億パラメータ規模のモデルが量産車に搭載される中国最前線事例。 |
| 36 | [How Do NIO, Xpeng, and Li Auto Differ in Their AI Approaches?](https://cnevpost.com/2026/01/19/how-do-nio-xpeng-li-auto-differ-in-ai-approaches/) | 2026 | ⭐⭐⭐⭐ | 3社のAI戦略の違いを比較分析。ワールドモデルシフトと組織再編の詳細。競合他社分析として有用。 |

---

## 🔧 NVIDIA (5件)

| # | タイトル | 年 | ★ | 概要 |
|---|---------|-----|-----|------|
| 37 | [NVIDIA Makes Cosmos World Foundation Models Openly Available](https://blogs.nvidia.com/blog/cosmos-world-foundation-models/) | 2025 | ⭐⭐⭐⭐⭐ | Cosmosワールドファウンデーションモデルをオープンリリース。数千マイル実走行を数十億マイル仮想走行に変換する「データフライホイール」技術。 |
| 38 | [Simplify End-to-End AV Development with New NVIDIA Cosmos WFMs](https://developer.nvidia.com/blog/simplify-end-to-end-autonomous-vehicle-development-with-new-nvidia-cosmos-world-foundation-models/) | 2025 | ⭐⭐⭐⭐⭐ | Cosmos Predict 2.5/Transfer 2.5/Reason 2の技術詳細。E2E AV開発フローへの統合方法を実践的に解説。開発者向け必読。 |
| 39 | [NVIDIA DRIVE Partners Showcase Latest Mobility Innovations at CES](https://blogs.nvidia.com/blog/drive-partners-showcase-ces/) | 2025 | ⭐⭐⭐⭐ | CES 2025でのNVIDIA DRIVEパートナー最新動向。Toyota・Aurora・Continental等のDRIVE Thor採用事例を網羅。 |
| 40 | [NVIDIA Research Wins Autonomous Driving Challenge, Innovation Award at CVPR](https://blogs.nvidia.com/blog/autonomous-driving-challenge-cvpr/) | 2024 | ⭐⭐⭐⭐ | CVPR 2024自動運転チャレンジ優勝。3D Occupancy Predictionの精度向上技術の詳細。 |
| 41 | [Scale Synthetic Data and Physical AI Reasoning with NVIDIA Cosmos WFMs](https://developer.nvidia.com/blog/scale-synthetic-data-and-physical-ai-reasoning-with-nvidia-cosmos-world-foundation-models/) | 2025 | ⭐⭐⭐⭐ | 合成データ生成とPhysical AI推論のスケールアップ手法。Cosmos Predict/Reason/Transferの実装ガイド。 |

---

## 🔧 ARM (2件)

| # | タイトル | 年 | ★ | 概要 |
|---|---------|-----|-----|------|
| 42 | [Arm Announces New Automotive Technologies for AI-enabled Vehicles](https://newsroom.arm.com/blog/accelerating-adas-adoption) | 2024 | ⭐⭐⭐⭐⭐ | Arm Automotive Enhanced発表。Neoverse V3AEでサーバークラスAI性能を車載向けに実現。NVIDIA DRIVE Thor採用。BYD・XPENG・Volvoも採用表明。 |
| 43 | [Why Chiplets Are Key to Next-Gen Software-Defined Vehicles](https://newsroom.arm.com/blog/arm-imec-automotive-chiplets) | 2025 | ⭐⭐⭐⭐ | チップレット技術がソフトウェア定義車両のコスト・性能最適化に不可欠な理由。次世代車載コンピュータアーキテクチャの方向性。 |

---

## 🔧 Qualcomm (1件)

| # | タイトル | 年 | ★ | 概要 |
|---|---------|-----|-----|------|
| 44 | [Qualcomm and BMW Unveil Snapdragon Ride Pilot](https://next-curve.com/2025/09/12/qualcomms-automotive-ecosystem-drive-with-snapdragon-ride-pilot/) | 2025 | ⭐⭐⭐⭐ | BMW iX3でSnapdragon Ride Pilot実装。高速85mph対応のハンズフリー走行。コックピット+ADAS統合SoCのコスト優位性（25-50%削減）。 |

---

## 🔧 Renesas / ドメインコントローラ (2件)

| # | タイトル | 年 | ★ | 概要 |
|---|---------|-----|-----|------|
| 45 | [Renesas Unveils Industry's First Automotive Multi-Domain SoC Built with 3nm Process](https://www.renesas.com/en/about/newsroom/renesas-unveils-industry-s-first-automotive-multi-domain-soc-built-3-nm-process-technology) | 2024 | ⭐⭐⭐⭐⭐ | R-Car X5H発表。3nmプロセスのADAS/IVI/ゲートウェイ統合SoC。400 TOPS AI加速。ソフトウェア定義車両向け車載コンピュータの最前線。 |
| 46 | [Autonomous Driving Domain Controller and CCU Industry Review 2024-2025](https://autotech.news/autonomous-driving-domain-controller-and-central-control-unit-industry-review-2024-2025/) | 2024 | ⭐⭐⭐⭐ | 自動運転ドメインコントローラの市場・技術動向。普及率17.4%（2024年9月）。One Chip統合ソリューションへの進化を解説。 |

---

## 🤖 E2E・VLA・LLM アーキテクチャ (8件)

| # | タイトル | 年 | ★ | 概要 |
|---|---------|-----|-----|------|
| 47 | [All You Need for End-to-End Autonomous Driving (IEEE T-PAMI 2024)](https://github.com/OpenDriveLab/End-to-end-Autonomous-Driving) | 2024 | ⭐⭐⭐⭐⭐ | E2E自動運転の270本以上の論文を体系的に調査したIEEE T-PAMIサーベイ。手法・課題・トレンドを網羅。研究者必読の総合リファレンス。 |
| 48 | [LLM4AD: Large Language Models for Autonomous Driving (arXiv)](https://arxiv.org/html/2410.15281v4) | 2024 | ⭐⭐⭐⭐⭐ | 自動運転へのLLM適用を体系化。コンセプト・レビュー・ベンチマーク・実験・将来動向を包括的に解説。 |
| 49 | [Vision-Language-Action Models for AD: Past, Present, and Future (arXiv)](https://arxiv.org/abs/2512.16760) | 2024 | ⭐⭐⭐⭐⭐ | VLAモデルの自動運転応用を体系的に整理。End-to-End VLAとDual-System VLAの2大パラダイムを比較。2025年最注目技術の先取りサーベイ。 |
| 50 | [Generative AI for Autonomous Driving: Frontiers and Opportunities (arXiv)](https://arxiv.org/abs/2505.08854) | 2025 | ⭐⭐⭐⭐⭐ | 自動運転への生成AI適用の包括的レビュー。データ生成・世界モデル・E2Eシステムへの応用をカバー。 |
| 51 | [A Survey on Large Language Model-Powered Autonomous Driving](https://www.sciencedirect.com/science/article/pii/S2095809925004709) | 2025 | ⭐⭐⭐⭐ | LLM活用自動運転の最新サーベイ。意思決定・説明可能性・人車インタラクションへのLLM応用を整理。 |
| 52 | [Diffusion-Based Planning for Autonomous Driving with Flexible Guidance (ICLR 2025 Oral)](https://github.com/ZhengYinan-AIR/Diffusion-Planner) | 2025 | ⭐⭐⭐⭐⭐ | 拡散モデルによるマルチモーダル運転行動のクローズドループプランニング。nuPlanベンチマークSOTA。ICLR 2025 Oral採択。 |
| 53 | [DiffusionDrive: Truncated Diffusion Model for End-to-End AD (CVPR 2025)](https://openaccess.thecvf.com/content/CVPR2025/papers/Liao_DiffusionDrive_Truncated_Diffusion_Model_for_End-to-End_Autonomous_Driving_CVPR_2025_paper.pdf) | 2025 | ⭐⭐⭐⭐ | E2E自動運転のための短縮拡散デコーダ。シーンコンテキストとのインタラクションで軌跡を段階的に洗練。CVPR 2025掲載。 |
| 54 | [Trajectory Prediction for Autonomous Driving: Progress, Limitations, and Future Directions (arXiv)](https://arxiv.org/abs/2503.03262) | 2025 | ⭐⭐⭐⭐ | 自動運転軌跡予測の進展・限界・将来方向性を整理したサーベイ。物理ベース・DL・RL手法の比較。 |

---

## 🤖 知覚技術 (Perception) (5件)

| # | タイトル | 年 | ★ | 概要 |
|---|---------|-----|-----|------|
| 55 | [A Survey on Occupancy Perception for Autonomous Driving (arXiv)](https://arxiv.org/abs/2405.05173) | 2024 | ⭐⭐⭐⭐⭐ | 3D Occupancy知覚の包括的サーベイ。入力モダリティ別の手法分類と情報融合アプローチを体系化。Information Fusion掲載。 |
| 56 | [Vision-based 3D Occupancy Prediction in AD: A Review and Outlook](https://link.springer.com/article/10.1007/s11704-024-40443-5) | 2024 | ⭐⭐⭐⭐ | カメラベース3D Occupancy予測サーベイ。BEV知覚からの発展とコスト効果の高い知覚システム設計を解説。 |
| 57 | [Foundation Models for Autonomous Driving Perception: A Survey (arXiv)](https://arxiv.org/abs/2509.08302) | 2025 | ⭐⭐⭐⭐⭐ | 自動運転知覚のファウンデーションモデルを体系的にサーベイ。コア能力別の分類と将来展望。 |
| 58 | [BEV Perception for Autonomous Driving: State of the Art and Future Perspectives](https://www.sciencedirect.com/science/article/abs/pii/S0957417424019705) | 2024 | ⭐⭐⭐⭐ | BEV知覚の現状と将来展望。BEVFormerからの進化と最新手法を包括的に整理。 |
| 59 | [Large Foundation Models for Trajectory Prediction in Autonomous Driving (arXiv)](https://arxiv.org/abs/2509.10570) | 2025 | ⭐⭐⭐⭐ | 軌跡予測のための大規模ファウンデーションモデルの包括的サーベイ。LLM・MLLMによる文脈推論の活用法。 |

---

## 💡 シミュレーション・合成データ (7件)

| # | タイトル | 年 | ★ | 概要 |
|---|---------|-----|-----|------|
| 60 | [Applied Intuition 2024 Year in Review: Milestones in Autonomy](https://www.appliedintuition.com/blog/2024-year-in-review) | 2024 | ⭐⭐⭐⭐ | シミュレーションプラットフォームの2024年総括。5000万回シミュレーション実行、ラベリングコスト95%削減の実績。 |
| 61 | [Applied Intuition 2025 in Review: Autonomy at Scale](https://www.appliedintuition.com/blog/2025-year-in-review) | 2025 | ⭐⭐⭐⭐ | AV開発ツールチェーンの進化。EpiSci買収によるLand/Air/Sea/Spaceへの拡張、OpenAI提携。 |
| 62 | [CARLA2Real: A Tool for Reducing the Sim2Real Appearance Gap (arXiv)](https://arxiv.org/abs/2410.18238) | 2024 | ⭐⭐⭐⭐⭐ | CARLAシミュレータのリアリティ向上ツール。13 FPSでリアルタイム変換。Cityscapes/KITTIレベルのリアリズムを実現。Sim2Real解消の実践的手法。 |
| 63 | [A Comprehensive Review on Traffic Datasets and Simulators for AVs (arXiv)](https://arxiv.org/abs/2412.14207) | 2024 | ⭐⭐⭐⭐ | 自動運転向けシミュレータとデータセットの包括的レビュー。CARLA/SUMO/BeamNG等の特性・適用場面を比較。 |
| 64 | [15 Notable AI Datasets for Autonomous Driving in 2024-2025](https://www.basic.ai/blog-post/15-new-autonomous-driving-datasets-in-2024-2025) | 2024 | ⭐⭐⭐⭐ | 2024-2025年に公開された15の主要自動運転データセットのカタログ。各データセットの特徴・用途・規模を比較。 |
| 65 | [Generative AI for Testing of Autonomous Driving Systems: A Survey (arXiv)](https://arxiv.org/abs/2508.19882) | 2025 | ⭐⭐⭐⭐ | 自動運転システムテストへの生成AI活用サーベイ。エッジケース生成・シナリオ多様化・評価自動化のアプローチ。 |
| 66 | [DrivingGen: A Comprehensive Benchmark for Video World Models in AD (arXiv)](https://arxiv.org/abs/2601.01528) | 2025 | ⭐⭐⭐⭐ | 自動運転向けビデオ世界モデルの包括的ベンチマーク。生成品質・制御可能性・安全性評価の新フレームワーク。 |

---

## 📡 センサー技術 (6件)

| # | タイトル | 年 | ★ | 概要 |
|---|---------|-----|-----|------|
| 67 | [Lidar on a Chip Puts Self-Driving Cars in the Fast Lane (IEEE Spectrum)](https://spectrum.ieee.org/lidar-on-a-chip) | 2024 | ⭐⭐⭐⭐⭐ | チップ統合LiDAR技術の詳細。固体LiDARの量産・低コスト化への道筋をIEEE Spectrumが解説。 |
| 68 | [Hesai's Infinity Eye Lidar: A Game-Changer in Autonomous Driving](https://www.ainvest.com/news/hesai-infinity-eye-lidar-game-changer-autonomous-driving-risks-linger-2504/) | 2025 | ⭐⭐⭐⭐ | Hesaiの最先端LiDAR技術分析。世界市場シェア33%の技術的根拠と競合比較。2024年50万ユニット出荷の背景。 |
| 69 | [Innoviz Technologies Accelerates Delivery of LiDAR Platform to Volkswagen](https://ir.innoviz.tech/news-events/press-releases/detail/148/innoviz-technologies-accelerates-delivery-of-newly-designed) | 2025 | ⭐⭐⭐ | VW ID. Buzz向け新設計LiDARプラットフォームの出荷加速発表。Innoviz固体LiDARの量産OEM採用事例。 |
| 70 | [4D Imaging Radar: Rising Adoption Outpaces 3D in ADAS](https://www.globenewswire.com/news-release/2025/08/13/3132326/28124/en/4D-Imaging-Radar-in-Autonomous-Vehicles-Research-and-Competition-Analysis-Report-2025-Rising-Adoption-of-4D-Radar-in-ADAS-Outpaces-3D-Enhances-Safety-and-Precision.html) | 2025 | ⭐⭐⭐⭐ | 4DイメージングレーダーのADAS普及動向。3Dレーダー超えの性能優位性と悪天候・夜間性能の解説。Waymo採用例も。 |
| 71 | [Deep Dive: Tesla, Waymo, and the Great Sensor Debate](https://research.contrary.com/report/tesla-waymo-and-the-great-sensor-debate) | 2024 | ⭐⭐⭐⭐⭐ | TeslaのカメラオンリーとWaymoのマルチセンサー（LiDAR+カメラ+レーダー）アプローチの深い比較分析。センサー戦略の設計思想の違いを解説。 |
| 72 | [Driving Vision: Inside China's LiDAR Revolution – An Interview with Hesai](https://www.yolegroup.com/player-interviews/driving-vision-unside-chinas-lidar-revolution-an-interview-with-hesai/) | 2024 | ⭐⭐⭐⭐ | Hesai CEOインタビュー。中国LiDAR産業が世界市場を席巻した背景と技術戦略を詳述。 |

---

## 🌐 地図・ローカライゼーション (3件)

| # | タイトル | 年 | ★ | 概要 |
|---|---------|-----|-----|------|
| 73 | [Maps for Autonomous Driving: Full-Process Survey and Frontiers (arXiv)](https://arxiv.org/abs/2509.12632) | 2025 | ⭐⭐⭐⭐⭐ | 自動運転マップのフルプロセスサーベイ。HDマップ→LDマップ→マップレスへの進化を体系化。3D Gaussianスプラッティング等の最新手法も解説。 |
| 74 | [Navigating the Future: Mapless vs Map-Based Autonomous Driving](https://www.counterpointresearch.com/insight/navigating-the-future-mapless-vs-map-based-autonomous-driving/) | 2024 | ⭐⭐⭐⭐ | マップレスvsマップベースの自動運転を比較。コスト・拡張性・精度のトレードオフ分析。業界のマップレス移行トレンドを解説。 |
| 75 | [MapVision: CVPR 2024 Autonomous Grand Challenge Mapless Driving Tech Report (arXiv)](https://arxiv.org/abs/2406.10125) | 2024 | ⭐⭐⭐⭐ | CVPR 2024 Autonomous Grand Challengeのマップレス走行技術レポート。オンラインマップ生成の最先端手法。 |

---

## 🌐 安全規格・機能安全 (3件)

| # | タイトル | 年 | ★ | 概要 |
|---|---------|-----|-----|------|
| 76 | [A Unified Safety Framework: Integrating ISO 26262, SOTIF, and UL 4600](https://www.sciencedirect.com/science/article/pii/S259019822500510X?via%3Dihub) | 2025 | ⭐⭐⭐⭐⭐ | ISO 26262・ISO 21448 (SOTIF)・UL 4600を統合したAV開発向け安全フレームワーク。自動運転開発者必読。 |
| 77 | [Rethinking AV Functional Safety Standards: ISO 26262 and SOTIF Analysis](https://www.automotive-iq.com/autonomous-drive/articles/rethinking-autonomous-vehicle-functional-safety-standards-an-analysis-of-sotif-and-iso-26262) | 2024 | ⭐⭐⭐⭐ | SOTIFとISO 26262の補完関係を詳細分析。AI/センサー誤認識への対処としてのSOTIFの役割を解説。 |
| 78 | [Cybersecurity for Next-Generation Road Transportation (ACM)](https://dl.acm.org/doi/full/10.1145/3744352) | 2025 | ⭐⭐⭐⭐ | 次世代道路交通のサイバーセキュリティ包括レビュー。V2X通信セキュリティとUN R155対応の技術的要件。 |

---

## 🌐 規制・業界動向 (5件)

| # | タイトル | 年 | ★ | 概要 |
|---|---------|-----|-----|------|
| 79 | [Regulations for Autonomous Vehicles: Global Policy Trends 2024-2030](https://patentpc.com/blog/regulations-for-autonomous-vehicles-where-do-countries-stand-in-2024-2030-global-policy-trends) | 2024 | ⭐⭐⭐⭐ | 米・EU・中国の自動運転規制比較。中国の2025年L3以上義務化、EU統一フレームワーク2026、UNECE R155への対応。 |
| 80 | [The State of Autonomous Driving in 2025](https://autocrypt.io/state-of-autonomous-driving-2025/) | 2025 | ⭐⭐⭐⭐ | 2025年の自動運転産業総括。技術・規制・市場・セキュリティを網羅した業界年次レポート。 |
| 81 | [Waymo's 2025 Year in Review: The Year Robotaxis Scaled](https://www.thedriverlessdigest.com/p/waymos-2025-year-in-review-the-year) | 2025 | ⭐⭐⭐⭐ | ロボタクシー産業が本格スケールした2025年の総括。週17万5千ライド→45万ライドへの成長軌跡。 |
| 82 | [NACFE: The State of Autonomous Trucking in 2025 (2024 Recap)](https://nacfe.org/autonomous-trucking/the-state-of-autonomous-trucking-in-2025-a-recap-of-2024/) | 2025 | ⭐⭐⭐⭐ | 2024年の自動運転トラッキング産業の総括。Aurora・Gatik・Torc・Kodiak等の各社動向を比較分析。 |
| 83 | [Aurora Heads into 2026 with Big Plans on Tap](https://www.truckinginfo.com/10249848/aurora-heads-into-2026-with-big-plans-on-tap) | 2025 | ⭐⭐⭐ | Auroraの2026年計画。第2世代ハードウェアキット（コスト50%以上削減・LiDAR航続距離2倍）の詳細。 |

---

## 🌐 データセット・ベンチマーク (4件)

| # | タイトル | 年 | ★ | 概要 |
|---|---------|-----|-----|------|
| 84 | [nuScenes Revisited: Progress and Challenges in Autonomous Driving (arXiv)](https://arxiv.org/abs/2512.02448) | 2024 | ⭐⭐⭐⭐ | nuSceneデータセットの進化と課題の包括的レビュー。マルチモーダル知覚のデファクトベンチマークの現状と限界。 |
| 85 | [CoVLA: Comprehensive Vision-Language-Action Dataset for AD (arXiv)](https://arxiv.org/abs/2408.10845) | 2024 | ⭐⭐⭐⭐⭐ | Turing Inc.が公開した自動運転向け最初の大規模VLAデータセット（WACV 2025採択）。東京1万シーン・80時間超の走行データに詳細な言語記述と軌跡アノテーション。 |
| 86 | [Occluded nuScenes: Multi-Sensor Dataset for Perception Robustness (arXiv)](https://arxiv.org/abs/2510.18552) | 2024 | ⭐⭐⭐ | 遮蔽シナリオでの知覚ロバスト性評価向けデータセット。実世界の悪条件に対する知覚システムの信頼性評価に有用。 |
| 87 | [Are AI-Generated Driving Videos Ready for Autonomous Driving? (arXiv)](https://arxiv.org/abs/2512.06376) | 2024 | ⭐⭐⭐⭐ | AI生成走行ビデオの自動運転活用可能性を診断的に評価するフレームワーク。生成データの品質基準を提示。 |

---

## 🤖 プランニング・意思決定 (4件)

| # | タイトル | 年 | ★ | 概要 |
|---|---------|-----|-----|------|
| 88 | [A Crash Course of Planning for Perception Engineers in Autonomous Driving (Medium)](https://medium.com/the-thinking-car/a-crash-course-of-planning-for-perception-engineers-in-autonomous-driving-ede324d78717) | 2024 | ⭐⭐⭐⭐⭐ | 知覚エンジニア向けプランニング入門。行動決定・モーションプランニングの基礎からトランスフォーマーベース最新手法まで実践的に解説。 |
| 89 | [A Survey of Decision-Making and Planning Methods for Self-Driving Vehicles](https://www.frontiersin.org/journals/neurorobotics/articles/10.3389/fnbot.2025.1451923/full) | 2025 | ⭐⭐⭐⭐ | 自動運転の意思決定・プランニング手法の包括的サーベイ。ルールベース・学習ベース・ハイブリッドアプローチを比較。 |
| 90 | [Vehicle Trajectory Prediction for AD: State-of-the-Art Review](https://link.springer.com/article/10.1007/s42154-025-00382-8) | 2025 | ⭐⭐⭐⭐ | 自動運転の車両軌跡予測の最新レビュー。物理モデル・深層学習・インタラクションモデリングの比較。 |
| 91 | [Achieving Better Accuracy in 3D Occupancy Prediction for AD (NVIDIA GTC 2024)](https://www.nvidia.com/en-us/on-demand/session/gtc24-s62446/) | 2024 | ⭐⭐⭐⭐ | GTC 2024でのNVIDIA発表。3D Occupancy予測の精度向上技術の詳細と実装アプローチ。 |

---

## 🌐 その他・注目記事 (9件)

| # | タイトル | 年 | ★ | 概要 |
|---|---------|-----|-----|------|
| 92 | [Autonomous Driving Map Industry Review 2025](https://autotech.news/autonomous-driving-map-industry-review-2025/) | 2025 | ⭐⭐⭐⭐ | 2025年自動運転マップ産業総括。HD/LD/SDマップの市場シェアと各社のマップ戦略変化を分析。 |
| 93 | [GenAI4AD: GenAI Across the Full Autonomous Driving Stack (GitHub)](https://github.com/taco-group/GenAI4AD) | 2024 | ⭐⭐⭐⭐⭐ | 自動運転スタック全体への生成AI適用の批判的・包括的総合分析。知覚・予測・プランニング・シミュレーション全領域を網羅。 |
| 94 | [Awesome World Models for Autonomous Driving (GitHub)](https://github.com/LMD0311/Awesome-World-Model) | 2024 | ⭐⭐⭐⭐ | 自動運転（・ロボット等）向けワールドモデル論文の厳選コレクション。継続更新される研究トラッキングリソース。 |
| 95 | [Awesome VLA for Autonomous Driving (GitHub)](https://github.com/worldbench/awesome-vla-for-ad) | 2025 | ⭐⭐⭐⭐ | 自動運転向けVLA（Vision-Language-Action）モデルの論文・プロジェクト厳選コレクション。最新研究トラッキングに有用。 |
| 96 | [Exploring HD Mapping That Scales (Nuro Medium Blog)](https://medium.com/nuro/exploring-hd-mapping-that-scales-939c3b69e232) | 2024 | ⭐⭐⭐⭐ | NuroによるスケーラブルなHDマップ構築の技術詳細。自動マッピングパイプラインとクラウドソーシング活用の解説。 |
| 97 | [Turing Unveils CoVLA Dataset — Japan's First AD VLA Dataset](https://tur.ing/en/news/20240910/) | 2024 | ⭐⭐⭐⭐ | Turing Inc.の公式プレスリリース。CoVLAデータセット発表の背景と日本初の自動運転VLAモデル開発の意義を解説。 |
| 98 | [Waymo Statistics 2026: Funding, Revenue & Rides Per Cities](https://awisee.com/blog/waymo-statistics/) | 2026 | ⭐⭐⭐⭐ | Waymoの最新統計まとめ。資金調達・収益・都市別乗車数・安全指標を網羅。競合分析の参考データとして有用。 |
| 99 | [OpenDriveLab Publications: E2E Autonomous Driving Research Hub](https://opendrivelab.com/publications) | 2024 | ⭐⭐⭐⭐⭐ | 上海AIラボ/Hong Kong Univ.のOpenDriveLabの論文リスト。UniAD・VAD・SparseDrive等、E2E自動運転の最先端研究を継続的に発表する研究ラボ。 |
| 100 | [Waymo Skyrocketing Ridership in One Chart (TechCrunch)](https://techcrunch.com/2026/03/27/waymo-skyrocketing-ridership-in-one-chart/) | 2026 | ⭐⭐⭐⭐ | Waymoの急成長ライドシェア事業を1枚のグラフで示す分析記事。スケーリングの速度と市場インパクトを可視化。 |

---

## 統計まとめ

| カテゴリ | 件数 |
|---------|------|
| 🚗 自動運転企業ブログ | 35件 |
| 🤖 AI・ML・モデルアーキテクチャ | 21件 |
| 💡 シミュレーション・データ | 7件 |
| 🔧 チップ・ハードウェア | 11件 |
| 📡 センサー技術 | 6件 |
| 🌐 規制・業界動向・地図 | 20件 |
| **合計** | **100件** |

| おすすめ度 | 件数 |
|-----------|------|
| ⭐⭐⭐⭐⭐ | 36件 |
| ⭐⭐⭐⭐ | 55件 |
| ⭐⭐⭐ | 9件 |
