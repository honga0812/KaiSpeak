#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate KaiSpeak 15s Cinematic Animation Prompts for MiniMax Video-01
Includes:
- Category A: 4 Mythical Beasts Stage 5 Graduation Soaring Animations
- Category B: 5 Skyscraper Completed Spire & Metropolis Flyby Animations
- Category C: 5 Adventure Island Galaxy Boss Clear & Planetary Triumph Animations
"""

import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "MiniMax 15s 動畫總表"

# Ensure grid lines are visible
ws.views.sheetView[0].showGridLines = True

headers = [
    "分類",
    "編號",
    "項目名稱 (英中文)",
    "目標時長",
    "建議檔案名稱",
    "目標存放路徑",
    "首幀圖生視頻 (I2V) 參考圖",
    "專屬場景特色元素",
    "15秒鏡頭動態節奏 (0~5s, 5~10s, 10~15s)",
    "MiniMax 影片生成提示詞 (英文 Prompt)",
    "提示詞中文意境解析與特效要點"
]

data = [
    # -------------------------------------------------------------
    # Category A: 4 Mythical Beasts Final Graduation Animations
    # -------------------------------------------------------------
    (
        "A. 巨獸養成聖域 (4大神獸)",
        "BST-ANIM-01",
        "綠角翡翠天龍 · 巴迪\n(Buddy - Emerald Sky Dragon)",
        "15 秒",
        "BST_ANIM_01_Buddy.mp4",
        "videos/beasts/BST_ANIM_01_Buddy.mp4",
        "images/ui/Buddy-5.jpeg",
        "熱帶遠古浮空島嶼、參天巨木樹冠、青苔神廟廢墟、飄散的翡翠花粉微粒、溫暖晨曦金光。",
        "【0~5s】：鏡頭以第一幀為起點特寫成龍威嚴自信的笑容，巨大的翡翠羽翼重力拍打，震起漫天綠色微光花粉，巨龍凌空拔地而起。\n【5~10s】：空拍無人機鏡頭跟隨巨龍在熱帶浮島巨樹間高速俯衝穿梭，身姿靈動優雅，龍尾劃出碧綠色的發光流線軌跡。\n【10~15s】：巨龍昂首仰衝穿透金色雲層，迎著旭日向蒼穹發出雄壯咆哮，天際爆發出燦爛的翡翠極光波紋，鏡頭環繞拉遠定格。",
        "Cinematic 3D animation, Pixar and Disney masterpiece style, beginning from the first frame image. A majestic adult emerald-green feathered dragon soars majestically off a mossy floating island temple. At 0-5s, close-up on the dragon's joyful smiling expression and glowing jade antlers as its colossal feathered wings beat powerfully, kicking up shimmering emerald pollen and golden morning light. At 5-10s, dynamic aerial drone tracking shot following the dragon swooping gracefully through ancient canopy trees and waterfalls, looping smoothly with radiant green particle trails behind its tail. At 10-15s, the emerald sovereign dragon surges vertically through sun-drenched golden clouds, unleashing a joyful heroic roar towards the rising sun as an emerald auroral shockwave ripples across the azure sky. Smooth camera motion, ultra-detailed feathers and scales, volumetric sunlight, 4K resolution, 60fps, joyful and triumphant mood.",
        "【第一幀無縫銜接】：以 Buddy-5.jpeg 成龍立繪為起始視角。\n【視覺核心】：凸顯綠色羽翼的大氣展翼感與穿梭浮空熱帶島嶼的自由暢快。\n【音畫同步】：前段起飛呼嘯、中段風馳電掣穿雲、尾段天雷與晨光共鳴咆哮。"
    ),
    (
        "A. 巨獸養成聖域 (4大神獸)",
        "BST-ANIM-02",
        "奔雷神鷹獅鷲 · 雷恩\n(Ray - Golden Thunder Gryphon)",
        "15 秒",
        "BST_ANIM_02_Ray.mp4",
        "videos/beasts/BST_ANIM_02_Ray.mp4",
        "images/ui/Ray-5.jpeg",
        "暮色雷暴雲海、高聳紫晶懸崖、浮空機械航道、金色閃電電弧、音爆雲環 (Sonic Boom Rings)。",
        "【0~5s】：第一幀起步，金色獅鷲展露如刀鋒般的金羽，雙翼凝聚耀眼金藍電弧，伴隨破空音爆聲，以極限速度衝出紫晶崖頂。\n【5~10s】：鏡頭平行側飛跟拍，獅鷲在滾滾雷雲中進行高速滾轉特技，雙翼撕裂暴風雨雲層，無害的金黃色天雷沿著羽梢不斷躍動。\n【10~15s】：獅鷲突破音障衝出暴風雨，暮色晚霞破雲而出，獅鷲在金色落日與平靜雲海之上展開遮天羽翼優雅滑翔，鏡頭側逆光展示金光輪廓。",
        "Cinematic 3D animation, Pixar Disney animation quality, initiating exactly from the first frame image. A magnificent adult golden-feathered thunder gryphon launches off a jagged purple-crystal cliff into twilight storm clouds. At 0-5s, camera focuses on its sharp golden beak and electrifying azure eyes as crackling golden lightning arcs envelop its massive wings, triggering a sonic shockwave ring as it rockets forward. At 5-10s, dynamic side-tracking high-speed camera flying parallel to the gryphon as it executes thrilling aerial barrel rolls through towering thunderclouds, golden electricity ribboning across its metallic feather tips. At 10-15s, the thunder sovereign pierces through the storm into serene golden sunset skies, spreading its colossal wingspan to glide effortlessly over a golden sea of clouds, triumphant noble expression, volumetric god rays, hyper-detailed feather physics, 4K, 60fps, exhilarating epic energy.",
        "【第一幀無縫銜接】：以 Ray-5.jpeg 金翼獅鷲天尊為起點。\n【視覺核心】：極限速度感、破音障衝擊波、金色電弧在雷雲與黃金落日交錯。\n【音畫同步】：電弧嘶鳴聲、音爆重低音、穿雲後的澄澈悠揚配樂。"
    ),
    (
        "A. 巨獸養成聖域 (4大神獸)",
        "BST-ANIM-03",
        "萬年極光聖龍 · 弗羅斯特\n(Frost - Glacial Crystal Wyrm)",
        "15 秒",
        "BST_ANIM_03_Frost.mp4",
        "videos/beasts/BST_ANIM_03_Frost.mp4",
        "images/ui/Frost-5.jpeg",
        "終年積雪的冰川雪峰、浮空藍晶冰山、極光帷幕 (Aurora Borealis)、漫天飄落的菱形雪晶光塵。",
        "【0~5s】：第一幀淡藍冰龍甦醒，晶瑩剔透的冰晶鹿角散發青綠色微光，長長的身軀如絲綢般優雅盤旋升空，冰塵環繞。\n【5~10s】：鏡頭以流暢長鏡頭跟隨冰龍在浮空冰川大裂谷間優雅穿梭，半透明光翼輕輕扇動，在空中撒下如鑽石粉末般的冰晶流蘇。\n【10~15s】：冰龍游向夜空正中央，天空翻滾起璀璨絢麗的綠紫雙色極光，冰龍昂首吐息凝聚出一顆旋轉的巨大極光冰魄之星，鏡頭全景環繞，宛如天界神蹟。",
        "Cinematic 3D animation, Disney Pixar fantasy style, beginning smoothly from the first frame image. An ethereal adult glacial ice wyrm dragon takes flight from a towering iceberg summit. At 0-5s, gentle elegant camera movement admiring its translucent cyan crystal wings and branching glacier antlers as diamond frost dust spirals from its long serpentine body. At 5-10s, seamless tracking shot gliding alongside the majestic wyrm as it weaves effortlessly through floating ice canyons and frosted pine valleys, leaving a shimmering sparkling mist trail behind. At 10-15s, the dragon ascends into a twilight arctic night sky illuminated by magnificent waving green and violet aurora borealis, performing a graceful celestial loop, turning back towards the camera with a gentle noble gaze, cinematic crystal reflections, volumetric icy moonlight, 4K resolution, 60fps, serene and breathtaking.",
        "【第一幀無縫銜接】：以 Frost-5.jpeg 冰晶聖龍為起點。\n【視覺核心】：優雅空靈的冰晶流動感、極光光影折射、鑽石光粉漫天飄散。\n【音畫同步】：空靈的冰晶風鈴音、柔美管弦樂、極光流動的低鳴呼嘯。"
    ),
    (
        "A. 巨獸養成聖域 (4大神獸)",
        "BST-ANIM-04",
        "炎岩泰坦天尊 · 戈爾隆\n(Gorlon - Magma Titan Sovereign)",
        "15 秒",
        "BST_ANIM_04_Gorlon.mp4",
        "videos/beasts/BST_ANIM_04_Gorlon.mp4",
        "images/ui/Gorlon-5.jpeg",
        "遠古活火山口、流淌的黃金熔岩瀑布、黑曜石巨石柱、飄散的溫暖火星灰燼、壯闊血色落日。",
        "【0~5s】：以第一幀黑曜石重裝泰坦為起點，胸前岩漿符文如同心臟跳動般爆發熾熱光芒，巨大的熔岩重翼猛烈拍動，大地微微震顫，泰坦拔地升空。\n【5~10s】：鏡頭在火山口上方環繞巡遊，泰坦低空掠過沸騰的岩漿湖，雙爪划過岩壁激起耀眼的金色火花雨，身姿雄偉不可撼動。\n【10~15s】：泰坦直衝火山煙柱頂端，迎著壯麗的赤紅落日張開雙臂引頸長嘯，胸中噴薄出溫暖璀璨的金色地核光柱直貫雲霄，火雨如金色煙火般飄落，大獲全勝。",
        "Cinematic 3D animation, Pixar heroic style, starting directly from the first frame image. A colossal yet noble adult magma titan dragon awakens and takes flight from the rim of an ancient volcanic caldera. At 0-5s, camera focuses on its indestructible obsidian rock armor as radiant golden lava veins pulse brilliantly with immense energy, unfolding gigantic magma-infused armored wings that kick up warm glowing embers as it launches skyward. At 5-10s, orbiting wide-angle drone shot circling the titan as it sweeps low over glowing volcanic lava rivers, its stony tail creating cascades of fire sparks against obsidian cliff sides. At 10-15s, the titan sovereign ascends through golden smoke into a dramatic crimson and amber sunset, spreading its monumental armored wings in triumphant guardian pose, a friendly heroic smile, cinematic heat shimmer, volumetric golden hour haze, 4K, 60fps, epic and heartwarming power.",
        "【第一幀無縫銜接】：以 Gorlon-5.jpeg 熔岩泰坦為起點。\n【視覺核心】：厚重岩石與流動黃金岩漿的質感對比、溫暖金橘色夕陽、地核光柱。\n【音畫同步】：厚重低沉的心跳轟鳴、大地熔岩湧動聲、終段輝煌的勝利號角。"
    ),

    # -------------------------------------------------------------
    # Category B: 5 Skyscraper Completed Animations
    # -------------------------------------------------------------
    (
        "B. 摩天大樓島 (5大世界名樓)",
        "SKY-ANIM-01",
        "台北 101 經典名樓竣工\n(Taipei 101 Skyline Spire)",
        "15 秒",
        "SKY_ANIM_01_Taipei101.mp4",
        "videos/skyscrapers/SKY_ANIM_01_Taipei101.mp4",
        "images/ui/SKY-01.jpeg",
        "竹節層疊綠色玻璃帷幕、塔頂雷射探照燈、象山俯瞰夜景視角、跨年百萬金色煙火瀑布、信義區璀璨車軌。",
        "【0~5s】：由 SKY-01.jpeg 第一幀銜接，巨大金色吊車將頂層最後一塊金磚與避雷針精準安嵌，整座綠色竹節寶塔逐層點亮翡翠琉璃光芒。\n【5~10s】：鏡頭以 360 度急速空拍圍繞台北 101 由下向上螺旋盤旋上升，俯瞰整座璀璨繁華的台北市盆地夜景與五彩車流。\n【10~15s】：鏡頭升至塔頂尖端，101 塔身四面同時爆發出盛大壯麗的金色與粉紫色跨年煙火光瀑，塔頂射出直通星空的金色雷射光柱，全城歡呼，定格為奇蹟之樓。",
        "Cinematic 3D architectural animation, Pixar Disney celebration style, starting from the first frame image of Taipei 101. At 0-5s, a golden construction crane perfectly drops the final luminous spire piece onto the apex of Taipei 101, triggering a magnificent wave of emerald green and golden lights illuminating each stacked bamboo-pagoda section from bottom to top. At 5-10s, thrilling 360-degree spiral drone shot ascending rapidly along the skyscraper facade, revealing the breathtaking panoramic night cityscape of vibrant neon Taipei below. At 10-15s, camera crests the glowing spire as monumental colorful celebratory fireworks erupt from all sides of the tower into the starry night sky, brilliant golden spotlights illuminating the clouds, ultra-detailed glass reflections, 4K resolution, 60fps, festive triumphant wonder.",
        "【第一幀銜接】：以 SKY-01.jpeg 台北 101 特寫為起始。\n【建築象徵】：節節高升的竹節結構、逐層通電點亮琉璃光、盛大跨年煙火慶典。\n【視覺亮點】：台北夜景全景空拍、塔頂雷射貫穿星空。"
    ),
    (
        "B. 摩天大樓島 (5大世界名樓)",
        "SKY-ANIM-02",
        "帝國大廈 經典名樓竣工\n(Empire State Building Art-Deco)",
        "15 秒",
        "SKY_ANIM_02_EmpireState.mp4",
        "videos/skyscrapers/SKY_ANIM_02_EmpireState.mp4",
        "images/ui/SKY-02.jpeg",
        "曼哈頓黃金落日天際線、經典裝飾藝術 (Art Deco) 尖頂、飛馳的復古黃色計程車、哈德遜河金光水面、金色探照燈柱。",
        "【0~5s】：以 SKY-02.jpeg 為起點，裝飾藝術風格的石灰石塔樓在落日餘暉下散發古典金銅光輝，最後一座復古鋼架完成鉚接，整座大樓巍然屹立。\n【5~10s】：鏡頭從曼哈頓街道由低向高垂直急速仰衝爬升，掠過無數對稱的經典窗格與鋁合金浮雕飾帶，落日金光在窗玻璃上折射出絢爛光芒。\n【10~15s】：鏡頭躍出塔頂避雷天線，迎向深邃溫暖的黃金時段夕陽天際線，四盞巨型白色復古探照燈在天空交錯掃動，金色五彩碎紙如雨飄落，經典永恆。",
        "Cinematic 3D animation, vintage Art Deco cinematic masterpiece, initiating from the first frame of the Empire State Building. At 0-5s, the grand limestone skyscraper gleams in radiant late-afternoon golden hour sunlight as the final vintage steel framework locks seamlessly into place atop the mooring mast. At 5-10s, a dramatic vertical soaring drone camera rockets straight up the facade, skimming past thousands of sun-reflecting windows and geometric art-deco eagle sculptures. At 10-15s, the camera crests the illuminated spire, revealing the epic Manhattan skyline and Hudson River bathed in warm sunset orange and purple hues, with iconic white celebration beam searchlights sweeping across the sky as golden confetti sparkles in the wind, timeless majestic atmosphere, 4K, 60fps.",
        "【第一幀銜接】：以 SKY-02.jpeg 帝國大廈建築立面為起始。\n【建築象徵】：百老匯與曼哈頓黃金時代經典、裝飾藝術幾何雕花、探照燈交錯。\n【視覺亮點】：極速垂直垂直爬升視角、金色夕陽映照整座曼哈頓島。"
    ),
    (
        "B. 摩天大樓島 (5大世界名樓)",
        "SKY-ANIM-03",
        "哈利法塔 雲端神針竣工\n(Burj Khalifa Sky-Piercing Needle)",
        "15 秒",
        "SKY_ANIM_03_BurjKhalifa.mp4",
        "videos/skyscrapers/SKY_ANIM_03_BurjKhalifa.mp4",
        "images/ui/SKY-03.jpeg",
        "杜拜天際線、浩瀚雲海 (Sea of Clouds)、銀白不鏽鋼反光立面、世界最高人工瀑布水舞、璀璨雷射水銀天芒。",
        "【0~5s】：以 SKY-03.jpeg 為起點，銀白色的花瓣型塔樓底部向上傳遞一道耀眼的銀白光環，直入八百米九霄雲海，天際線萬籟俱寂。\n【5~10s】：空拍鏡頭從浩瀚壯觀的白色雲海上方俯衝直下，緊貼著哈利法塔極具未來感的三叉翼立面盤旋下落，如同一柄穿透雲層的星際神針。\n【10~15s】：鏡頭拉遠為全景，塔底全世界最大的音樂噴泉騰空萬道水柱，塔身八百米 LED 螢幕綻放出彩虹色的「KAI-SPEAK CHAMPION」光效，震撼寰宇。",
        "Cinematic 3D architectural masterpiece, ultra-futuristic Pixar wonder style, starting from the Burj Khalifa first frame. At 0-5s, a brilliant pulse of silver starlight travels from the flower-shaped base all the way up the 828-meter skyscraper, piercing through thick fluffy clouds into sapphire blue outer skies. At 5-10s, an exhilarating supersonic aerial dive from above the cloud sea, spiraling down alongside the reflective steel and glass Y-shaped wings, capturing shimmering sunlight dancing on the curved tiers. At 10-15s, wide panoramic reveal showing the entire monumental needle piercing the clouds, with world-famous dancing water fountain jets shooting hundreds of feet in synchronization below and cascading golden celebration light beams enveloping the skyscraper, 4K, 60fps, awe-inspiring scale.",
        "【第一幀銜接】：以 SKY-03.jpeg 哈利法塔為起點。\n【建築象徵】：世界第一高樓、穿透雲海的星際神針、三叉幾何花瓣結構。\n【視覺亮點】：穿透雲海的超高速俯衝跳水鏡頭、底部世界級音樂噴泉共舞。"
    ),
    (
        "B. 摩天大樓島 (5大世界名樓)",
        "SKY-ANIM-04",
        "默迪卡 118 鑽石天際塔竣工\n(Merdeka 118 Diamond Facet Tower)",
        "15 秒",
        "SKY_ANIM_04_Merdeka118.mp4",
        "videos/skyscrapers/SKY_ANIM_04_Merdeka118.mp4",
        "images/ui/SKY-04.jpeg",
        "多面體三角形玻璃鑽石切面、超長擎天尖頂天線、熱帶雨林城市微縮全景、藍紫水晶 LED 動態燈光矩陣。",
        "【0~5s】：以 SKY-04.jpeg 第一幀銜接，鑽石多面體幾何玻璃在藍紫日光下如同巨大水晶寶石，塔頂超長尖頂天線綻放出第一道啟動星芒。\n【5~10s】：鏡頭以極度動感視角圍繞鑽石菱形切面做大角度傾斜飛行，每塊三角形玻璃如同一面面鏡子，折射出熱帶吉隆坡雙子塔與綠意森林。\n【10~15s】：塔身數萬顆菱形 LED 水晶燈陣如同多米諾骨牌般整齊點亮，天線頂端射出一道直通平流層的青藍色極光信標，如同大地之鑽閃耀宇宙。",
        "Cinematic 3D animation, sleek modern architectural spectacle, beginning with the first frame of Merdeka 118. At 0-5s, the diamond-faceted triangular glass panels shimmer with crystalline cyan and violet reflections as the soaring needle spire reaches the sky, initiating its pinnacle beacon. At 5-10s, dynamic tilt-shift aerobatic drone camera swooping around the faceted prism corners, capturing sharp geometric reflections of tropical green landscapes and distant twin towers mirrored on the futuristic glass surfaces. At 10-15s, the entire crystalline facade cascades with dynamic waves of turquoise LED illumination from bottom to top, culminating in an awe-inspiring pillar of cyan light firing from the very tip into the twilight clouds, sharp crystalline aesthetics, 4K resolution, 60fps, ultra-modern triumph.",
        "【第一幀銜接】：以 SKY-04.jpeg 默迪卡 118 未來天際塔為起點。\n【建築象徵】：如鑽石切割的多面體水晶立面、超高天線尖針、現代幾何奇蹟。\n【視覺亮點】：三角稜鏡對稱折射、青藍色 LED 矩陣波浪、平流層信標光柱。"
    ),
    (
        "B. 摩天大樓島 (5大世界名樓)",
        "SKY-ANIM-05",
        "上海中心大廈 螺旋巨龍竣工\n(Shanghai Tower Spiral Dragon Spire)",
        "15 秒",
        "SKY_ANIM_05_ShanghaiTower.mp4",
        "videos/skyscrapers/SKY_ANIM_05_ShanghaiTower.mp4",
        "images/ui/SKY-05.jpeg",
        "雙層玻璃幕牆旋轉 120 度螺旋升騰、黃浦江 S 型江水倒影、外灘萬國建築群與陸家嘴賽博夜景、金色龍形光帶。",
        "【0~5s】：以 SKY-05.jpeg 第一幀為起點，雙層玻璃帷幕猶如一條蜿蜒巨龍旋轉盤旋而上，最後一圈圓弧幕牆合攏，巨龍歸位。\n【5~10s】：鏡頭跟隨一條金色光龍沿著 120 度旋轉上升的螺旋軌道直衝六百米高空，黃浦江兩岸的萬家燈火與外灘鐘樓在身後如波浪展現。\n【10~15s】：鏡頭躍出雲霧頂層的冠頂觀景台，陸家嘴三件套在雲霧夜景中熠熠生輝，上海中心大廈旋轉發射出金色與深紅的祥龍光暈，祥瑞君臨大地。",
        "Cinematic 3D animation, breathtaking futuristic urban animation style, beginning smoothly from the Shanghai Tower first frame. At 0-5s, the elegant 120-degree twisting spiral glass double-curtain facade completes its majestic ascent, glowing with soft champagne gold and jade reflections like a slumbering coiled sky dragon. At 5-10s, a thrilling ascending roller-coaster camera tracks a golden light beam spiraling smoothly around the curved twisting grooves, showcasing the winding Huangpu River and historical Bund lights sparkling far below. At 10-15s, the camera crests the crown spire through ethereal mist into the futuristic Pudong night sky, the twisting tower pulsing with a grand harmonic light festival of golden and crimson ribbons, cinematic volumetric city fog, 4K, 60fps, majestic and legendary.",
        "【第一幀銜接】：以 SKY-05.jpeg 上海中心大廈為起點。\n【建築象徵】：120度旋轉上升的雙層旋轉巨龍、陸家嘴核心天際線、黃浦江水之印。\n【視覺亮點】：沿著螺旋凹槽急速盤旋爬升鏡頭、外灘夜景全貌、頂層祥龍慶典光芒。"
    ),

    # -------------------------------------------------------------
    # Category C: 5 Adventure Island Galaxy Boss Clear Animations
    # -------------------------------------------------------------
    (
        "C. 探險島星系 (5大島嶼終極通關)",
        "ISL-ANIM-01",
        "第一島 · 隕石擊墜終極大捷\n(Meteor Island Boss Annihilation)",
        "15 秒",
        "ISL_ANIM_01_MeteorDefense.mp4",
        "videos/islands/ISL_ANIM_01_MeteorDefense.mp4",
        "images/ui/ISL-01.jpeg",
        "燃燒的紫黑巨型魔王隕石、Kai 騎乘的烈焰噴火龍、彩虹音波雷射重砲 (Rainbow Sonic Cannon)、太空星雲星塵煙火。",
        "【0~5s】：第一幀銜接，最後一顆遮天蔽日的暗黑骷髏巨型隕石呼嘯墜落，Kai 騎乘在火龍背上堅定握拳，火龍胸口匯聚出彩虹色強大音波能量。\n【5~10s】：Kai 振臂大聲喊出終極口號，火龍口中轟然噴射出直徑數十米的彩虹音波雷射光束，筆直貫穿魔王隕石核心，裂紋瞬間蔓延。\n【10~15s】：巨型隕石在宇宙星空中轟然瓦解，炸裂成萬千顆五彩斑斕的星塵煙火如流星雨般灑向星系，Kai 與火龍擊掌歡呼，第一島防衛成功！",
        "Cinematic 3D space-action animation, Pixar superhero style, starting from the first frame of Meteor Island. At 0-5s, a colossal glowing purple boss meteor with glowing magma cracks plummets menacingly towards the island planet, as cute hero kid Kai riding his fierce friendly red fire dragon charges bravely upwards, dragon's chest glowing with supercharged rainbow sonic energy. At 5-10s, Kai shouts a heroic command and the fire dragon unleashes a monumental beam of iridescent rainbow laser soundwaves directly through the heart of the dark meteor, shattering its crust into millions of cracks. At 10-15s, the giant boss meteor explodes harmlessly into magnificent colorful starfireworks, sparkling diamond confetti washing across space, Kai and his dragon do a mid-air high five, celebratory cosmic victory, 4K, 60fps.",
        "【第一幀銜接】：以 ISL-01.jpeg 第一島全景為起點。\n【核心劇情】：Kai 騎龍發射終極彩虹音波雷射砲，正面轟碎魔王隕石。\n【視覺亮點】：隕石在太空中化作萬千星塵煙火、英雄少男與火龍空中擊掌慶祝。"
    ),
    (
        "C. 探險島星系 (5大島嶼終極通關)",
        "ISL-ANIM-02",
        "第二島 · 摩天大樓群島金頂榮耀\n(Skyscraper Island Metropolis Glory)",
        "15 秒",
        "ISL_ANIM_02_SkyscraperMetropolis.mp4",
        "videos/islands/ISL_ANIM_02_SkyscraperMetropolis.mp4",
        "images/ui/ISL-02.jpeg",
        "海島上並立的五大世界摩天大樓、金色天秤巨型起重機、金色天際線能量網絡、島嶼狂歡彩帶。",
        "【0~5s】：以第二島整體地圖為起點，海島上的五座摩天大樓全部建造完工，金色巨型起重機緩緩退場，夕陽將整座島嶼染成燦爛純金。\n【5~10s】：五座大樓尖頂同時射出金色能量光束，在海島天空中交織成一座巨大的「智慧之冠」光之幾何網絡，照亮整片蔚藍海洋。\n【10~15s】：鏡頭以超低空高速掠過海浪，隨後猛烈仰衝穿過五座摩天大樓之間的立體天橋，全城鐘聲齊鳴，無數熱氣球升空，建築工程大圓滿！",
        "Cinematic 3D animation, Pixar utopian paradise style, initiating smoothly from the Skyscraper Island map. At 0-5s, camera sweeps over the sun-drenched island showcasing all 5 iconic world skyscrapers standing completed in magnificent harmony, giant golden construction cranes gently bowing in celebration. At 5-10s, all 5 skyscraper pinnacles simultaneously fire beams of luminous golden light into the sky, weaving together into a radiant celestial geometric Crown of Wisdom hovering above the island. At 10-15s, thrilling dynamic drone camera swoops low across sapphire ocean waves and climbs up between the gleaming towers, colorful celebration hot air balloons and festive ribbons floating everywhere, majestic orchestral brass fanfare vibe, 4K, 60fps, joyful and inspiring.",
        "【第一幀銜接】：以 ISL-02.jpeg 第二島群樓地圖為起點。\n【核心劇情】：五大世界名樓共同竣工，天頂交織成金色智慧之冠能量網。\n【視覺亮點】：海浪低空掠過至摩天峽谷垂直仰衝、熱氣球與金色彩帶全島狂歡。"
    ),
    (
        "C. 探險島星系 (5大島嶼終極通關)",
        "ISL-ANIM-03",
        "第三島 · 四大神獸完全體天際翱翔\n(Four Sovereigns Sky Flight Reunion)",
        "15 秒",
        "ISL_ANIM_03_BeastSanctuaryAwakening.mp4",
        "videos/islands/ISL_ANIM_03_BeastSanctuaryAwakening.mp4",
        "images/ui/ISL-03.jpeg",
        "四大成龍完全體（巴迪、雷恩、弗羅斯特、戈爾隆）、遠古聖域中央神聖祭壇、四色元素光柱 (綠/金/藍/紅)、浮空仙島群。",
        "【0~5s】：以第三島遠古叢林地圖為起點，中央祭壇上的古老暗黑水晶屏障徹底爆碎，綠、金、藍、紅四道巨型天雷光柱直衝雲霄。\n【5~10s】：四大完全體傳奇成龍（翡翠天龍、金翼獅鷲、極光聖龍、炎岩泰坦）同時展翼騰空，在島嶼上空列隊翺翔，神威赫赫，神采飛揚。\n【10~15s】：四隻成龍在鏡頭前並肩做環形大迴旋特技，向天際共同引頸長鳴，天地間灑落無盡的生機繁花與元素彩虹，第三島聖域完全覺醒！",
        "Cinematic 3D fantasy animation, Pixar Disney triumphant celebration style, initiating from the Beast Island sanctuary map. At 0-5s, the ancient dark mist crystal barrier at the sanctuary center shatters into glittering dust as four monumental columns of green, golden, cyan, and crimson elemental light erupt towards the heavens. At 5-10s, all four adult legendary sovereigns—Buddy the emerald dragon, Ray the thunder gryphon, Frost the crystal wyrm, and Gorlon the magma titan—take flight in glorious unison, swooping over lush floating jungle valleys with magnificent confidence. At 10-15s, the four majestic dragons perform an aerial loop formation directly towards the camera, letting out a harmonious joyful roar that causes vibrant magical flowers and rainbow light rings to bloom across the entire island, 4K, 60fps, legendary triumphant joy.",
        "【第一幀銜接】：以 ISL-03.jpeg 巨獸聖域地圖為起點。\n【核心劇情】：四隻完全體成龍同台集結，解除遠古封印，列隊翺翔護島。\n【視覺亮點】：四色元素光柱衝天、四龍編隊空中大迴轉、彩虹與花雨灑滿大地。"
    ),
    (
        "C. 探險島星系 (5大島嶼終極通關)",
        "ISL-ANIM-04",
        "第四島 · 聽音尋寶深海金庫開啟\n(Sunken Sonic Vault Treasure Bloom)",
        "15 秒",
        "ISL_ANIM_04_SoundTreasureLabyrinth.mp4",
        "videos/islands/ISL_ANIM_04_SoundTreasureLabyrinth.mp4",
        "images/ui/ISL-04.jpeg",
        "海底亞特蘭提斯神廟金庫、音符共鳴黃金音叉鑰匙、噴湧的七彩寶石與黃金寶箱、發光水母與海豚衛隊。",
        "【0~5s】：以第四島尋寶迷宮為起點，Kai 插入最後一把發光的古代音波黃金鑰匙，整座沉沒海底的巨型珊瑚黃金大門緩緩開啟。\n【5~10s】：大門向兩側轟鳴打開，金色光芒照亮整個深邃海溝，無數散發著溫暖神聖光芒的遠古英文字母寶石與黃金寶藏如噴泉般湧出。\n【10~15s】：鏡頭在金光燦爛的水下神殿中高速穿梭，一群發光海豚在寶藏噴泉中歡快躍水跳躍，Kai 高高舉起象徵智慧的古代金羊毛獎盃，寶藏大豐收！",
        "Cinematic 3D fantasy animation, Pixar underwater magical wonderland style, starting from Sound Treasure Island. At 0-5s, an ancient golden sonic tuner key slots into the colossal sunken coral temple door, sending waves of glowing musical notes cascading across underwater ruins. At 5-10s, the monumental golden vault doors slide open, releasing a dazzling eruption of glowing English alphabet gemstones, diamond crowns, and treasure crystals into the crystal-clear ocean waters. At 10-15s, sweeping cinematic underwater camera gliding through the shimmering golden hall as friendly glowing dolphins leap through cascades of golden coins, Kai proudly raises the legendary golden trophy of wisdom, joyful radiant lighting, 4K, 60fps, magical and lavish celebration.",
        "【第一幀銜接】：以 ISL-04.jpeg 尋寶島地圖為起點。\n【核心劇情】：音波金鑰開啟海底遠古金庫，萬千英文寶石與黃金如噴泉爆發。\n【視覺亮點】：水下光影丁達爾效應、發光海豚群躍、高舉金羊毛智慧獎盃。"
    ),
    (
        "C. 探險島星系 (5大島嶼終極通關)",
        "ISL-ANIM-05",
        "第五島 · 終極魔王島破曉破滅\n(Galaxy Boss Defeat Dawn Awakening)",
        "15 秒",
        "ISL_ANIM_05_CosmicBossDefeat.mp4",
        "videos/islands/ISL_ANIM_05_CosmicBossDefeat.mp4",
        "images/ui/ISL-05.jpeg",
        "暗黑虛空魔王核心、全星系夥伴集結、全螢幕金色極光破曉、探險島全星系金色和平光環、終極語言之神獎盃。",
        "【0~5s】：以第五島魔王島為起點，漆黑虛空魔王城堡正在釋放暗黑風暴，Kai 與全島神獸夥伴並肩站在山巔，無畏直面暴風。\n【5~10s】：Kai 攜手夥伴們釋放出融合了全島 2000 個單字能量的終極黃金星光長矛，一舉擊穿虛空魔王核心，黑暗如潮水般退散溶解。\n【10~15s】：一輪無比溫暖璀璨的黃金破曉之日從星系邊緣升起，溫暖陽光重新籠罩所有五座島嶼，天空中浮現出「KAI-SPEAK MASTER」傳奇金色星環，星系迎來和平！",
        "Cinematic 3D animation, grand cosmic finale Pixar masterpiece style, beginning with the dark Final Boss Island. At 0-5s, the menacing dark void shadow fortress releases purple storm clouds, but hero kid Kai stands resolute atop a mountain surrounded by glowing mythical dragon guardians, holding the luminous Golden Voice Scepter. At 5-10s, Kai and his companions unleash a colossal beam of pure warm golden cosmic light, shattering the dark void core into dissolving purple butterflies and sparkling dust. At 10-15s, a magnificent golden dawn breaks over the entire galaxy of five adventure islands, bathing the oceans and sky in warm radiant sunlight, a giant holographic golden crown inscribed with 'KAI-SPEAK MASTER' shines proudly across the horizon, ultra-epic orchestral climax, 4K, 60fps, ultimate triumph.",
        "【第一幀銜接】：以 ISL-05.jpeg 第五島魔王全景為起點。\n【核心劇情】：集結全星系能量一擊擊潰虛空魔王，迎來全星系黃金破曉。\n【視覺亮點】：黑暗消解化為紫色蝴蝶微粒、溫暖晨曦普照五大島嶼、宇宙級傳奇獎盃星環。"
    )
]

# Set Title
ws.merge_cells("A1:K1")
title_cell = ws["A1"]
title_cell.value = "KaiSpeak 奇妙星 15 秒高清終極通關動畫提示詞總表 (MiniMax Video-01 專用)"
title_cell.font = Font(name="Arial", size=16, bold=True, color="FFFFFF")
title_cell.fill = PatternFill(start_color="312E81", end_color="312E81", fill_type="solid")
title_cell.alignment = Alignment(horizontal="center", vertical="center")
ws.row_dimensions[1].height = 40

# Set Subtitle / Instructions
ws.merge_cells("A2:K2")
sub_cell = ws["A2"]
sub_cell.value = "說明：本清單專供地端 MiniMax Video-01 (海螺視頻模型) 首幀圖生視頻 (I2V) 製作。時長設定 15 秒，生成後請依建議路徑存入專案目錄。"
sub_cell.font = Font(name="Arial", size=10, italic=True, color="4338CA")
sub_cell.fill = PatternFill(start_color="EEF2FF", end_color="EEF2FF", fill_type="solid")
sub_cell.alignment = Alignment(horizontal="center", vertical="center")
ws.row_dimensions[2].height = 25

# Header formatting
ws.row_dimensions[3].height = 32
header_font = Font(name="Arial", size=11, bold=True, color="FFFFFF")
header_fill = PatternFill(start_color="4F46E5", end_color="4F46E5", fill_type="solid")
thin_border = Border(
    left=Side(style="thin", color="CBD5E1"),
    right=Side(style="thin", color="CBD5E1"),
    top=Side(style="thin", color="CBD5E1"),
    bottom=Side(style="thin", color="CBD5E1")
)

for col_idx, header in enumerate(headers, 1):
    cell = ws.cell(row=3, column=col_idx, value=header)
    cell.font = header_font
    cell.fill = header_fill
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    cell.border = thin_border

# Fill data rows
row_start = 4
for row_idx, item in enumerate(data, row_start):
    ws.row_dimensions[row_idx].height = 110  # generous height for multiline text
    cat_prefix = item[0][:1]
    
    # Alternate row colors based on category
    if cat_prefix == "A":
        bg_color = "F0FDF4"  # light emerald
    elif cat_prefix == "B":
        bg_color = "FFFBEB"  # light amber
    else:
        bg_color = "F5F3FF"  # light indigo

    row_fill = PatternFill(start_color=bg_color, end_color=bg_color, fill_type="solid")

    for col_idx, val in enumerate(item, 1):
        cell = ws.cell(row=row_idx, column=col_idx, value=val)
        cell.fill = row_fill
        cell.border = thin_border
        
        # Alignment specific
        if col_idx in [1, 2, 4]:
            cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
            cell.font = Font(name="Arial", size=10, bold=(col_idx==2))
        elif col_idx in [5, 6, 7]:
            cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
            cell.font = Font(name="Courier New", size=9, bold=(col_idx==5))
        elif col_idx == 10:  # English prompt
            cell.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
            cell.font = Font(name="Arial", size=9, color="1E1B4B")
        else:
            cell.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
            cell.font = Font(name="Arial", size=9)

# Adjust column widths
col_widths = {
    1: 18,   # 分類
    2: 15,   # 編號
    3: 24,   # 項目名稱
    4: 10,   # 目標時長
    5: 28,   # 建議檔案名稱
    6: 34,   # 目標存放路徑
    7: 24,   # 首幀圖生視頻 (I2V) 參考圖
    8: 30,   # 專屬場景特色元素
    9: 45,   # 15秒鏡頭動態節奏
    10: 65,  # MiniMax 影片生成提示詞 (英文 Prompt)
    11: 40   # 提示詞中文意境解析與特效要點
}

for col_idx, width in col_widths.items():
    col_letter = get_column_letter(col_idx)
    ws.column_dimensions[col_letter].width = width

output_path = "KaiSpeak_15s_Cinematic_Animation_Prompts_MiniMax.xlsx"
wb.save(output_path)
print(f"Successfully generated: {output_path}")
