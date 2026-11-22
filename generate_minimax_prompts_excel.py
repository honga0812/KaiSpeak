#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_minimax_prompts_excel.py
---------------------------------
為 KaiSpeak 生成 14 部 15 秒地端 MiniMax Video-01 (海螺視頻模型)
首幀圖生視頻 (I2V) 專屬提示詞與檔案規範對照 Excel 總表。

修正版：
1. 修正 4 筆摩天大樓圖片配對錯位，精準對齊 images/ui/SKY-01~05 及 index.html：
   - SKY-01: 台北 101 (Taipei 101)
   - SKY-02: 哈里發塔 (Burj Khalifa)
   - SKY-03: 上海中心大廈 (Shanghai Tower)
   - SKY-04: 帝國大廈 (Empire State Building)
   - SKY-05: 默迪卡 118 (Merdeka 118)
2. 修正第三島 (ISL-03.jpeg)：精準契合「恐龍遠古叢林島」視覺元素（萌萌小暴龍、長頸龍、史前蕨類樹屋、粉紅煙霧火山）與神獸共鳴。
3. 修正第四島 (ISL-04.jpeg)：精準契合「糖果夢幻點心島」視覺元素（棒棒糖森林、薑餅城堡、巧克力河、棉花糖山丘、糖果金幣雨）。
4. 修正第五島 (ISL-05.jpeg)：精準契合「亞特蘭提斯水下珊瑚島 / 海底城市王國」視覺元素（水晶氣泡穹頂、七彩珊瑚礁城堡、潛水艇與海豚海龜、海底丁達爾聖光）。
"""

import os
import openpyxl
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.utils import get_column_letter

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "MiniMax 15s 動畫總表"

# Ensure grid lines are visible
ws.views.sheetView[0].showGridLines = True

# Data definition (14 items)
data = [
    # -------------------------------------------------------------
    # Category A: 4 Mythical Beasts Stage 5 Evolution Animations
    # -------------------------------------------------------------
    (
        "A. 巨獸養成聖域 (4大神獸)",
        "BST-ANIM-01",
        "綠角翡翠天龍 · 巴迪\n(Buddy - Emerald Sky Dragon)",
        "15 秒",
        "BST_ANIM_01_Buddy.mp4",
        "videos/beasts/BST_ANIM_01_Buddy.mp4",
        "images/ui/Buddy-5.jpeg",
        "原始雨林神樹頂端、青翠翡翠羽翼、發光藤蔓、懸浮綠晶石、漫天綠色發光微粒花粉。",
        "【0~5s】：鏡頭以第一幀為起點特寫成龍威嚴自信的笑容，巨大的翡翠羽翼重力拍打，震起漫天綠色微光花粉，巨龍凌空拔地而起。\n【5~10s】：空拍無人機鏡頭跟隨巨龍在熱帶浮島巨樹間高速俯衝穿梭，身姿靈動優雅，龍尾劃出碧綠色的發光流線軌跡。\n【10~15s】：巨龍昂首仰衝穿透金色雲層，迎著旭日向蒼穹發出雄壯咆哮，天際爆發出燦爛的翡翠極光波紋，鏡頭環繞拉遠定格。",
        "Cinematic 3D animation, Pixar and Disney masterpiece style, beginning from the first frame image. A majestic adult emerald sky dragon with magnificent jade-green wings and glowing emerald horns initiates flight from its lush rainforest cliff. At 0-5s, camera slow zoom on the dragon's confident, heroic face before it beats its wings powerfully, sending green luminous pollen floating across the air, launching gracefully into the clear sky. At 5-10s, dynamic aerial following shot swooping low through giant floating islands, lush waterfalls, and ancient mossy canopies, the dragon leaving a dazzling trail of emerald stardust in its wake. At 10-15s, the dragon climbs vertically through golden clouds toward the morning sun, letting out an epic, majestic roar of triumph as brilliant aurora light ripples across the dawn horizon. Volumetric lighting, 8k resolution, fluid organic motion, ultra-detailed textures, Pixar cinematic lighting.",
        "【第一幀無縫銜接】：以 Buddy-5.jpeg 成龍翡翠巨龍為起點。\n【視覺核心】：巨大翡翠翼展、熱帶巨樹浮島俯衝、金色晨曦極光波紋。\n【音畫同步】：振翅破空聲、清脆鳥鳴與樹海呼嘯、高亢榮耀龍吟。"
    ),
    (
        "A. 巨獸養成聖域 (4大神獸)",
        "BST-ANIM-02",
        "奔雷神鷹獅鷲 · 雷恩\n(Ray - Golden Thunder Gryphon)",
        "15 秒",
        "BST_ANIM_02_Ray.mp4",
        "videos/beasts/BST_ANIM_02_Ray.mp4",
        "images/ui/Ray-5.jpeg",
        "高聳紫晶懸崖頂端、滾滾金色雷雲、耀眼金藍電弧、音爆氣流圈、落日晚霞平靜雲海。",
        "【0~5s】：第一幀起步，金色獅鷲展露如刀鋒般的金羽，雙翼凝聚耀眼金藍電弧，伴隨破空音爆聲，以極限速度衝出紫晶崖頂。\n【5~10s】：鏡頭平行側飛跟拍，獅鷲在滾滾雷雲中進行高速滾轉特技，雙翼撕裂暴風雨雲層，無害的金黃色天雷沿著羽梢不斷躍動。\n【10~15s】：獅鷲突破音障衝出暴風雨，暮色晚霞破雲而出，獅鷲在金色落日與平靜雲海之上展開遮天羽翼優雅滑翔，鏡頭側逆光展示金光輪廓。",
        "Cinematic 3D animation, Pixar Disney animation quality, initiating exactly from the first frame image. A magnificent adult golden thunder gryphon with razor-sharp lightning-infused feathers and glowing blue crystal eyes perches atop a stormy violet cliff. At 0-5s, brilliant harmless gold lightning crackles along its feather tips, creating a sonic pop as the gryphon leaps aggressively into supersonic flight. At 5-10s, high-speed tracking action camera racing alongside the gryphon as it executes thrilling barrel rolls through towering purple thunderclouds, slicing through stormy gusts with majestic golden wingtips. At 10-15s, the gryphon breaches the cloud layer into a breathtaking golden sunset above the sea of clouds, spreading its immense wings in a peaceful, victorious glide while golden evening rim light silhouettes its heroic form. Masterpiece grade CGI, octane render look, intense dynamic energy, crisp particle physics.",
        "【第一幀無縫銜接】：以 Ray-5.jpeg 雷恩成年金羽獅鷲為起點。\n【視覺核心】：極限音爆、金色電弧粒子跳躍、穿透暴風雨破曉黃金雲海。\n【音畫同步】：雷電劈啪劈啪聲、音爆呼嘯震撼、雄鷹長嘯展翅。"
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
    # Category B: 5 Skyscraper Completed Animations (CORRECTED MATCHING)
    # -------------------------------------------------------------
    (
        "B. 摩天大樓島 (5大世界名樓)",
        "SKY-ANIM-01",
        "台北 101 經典名樓竣工\n(Taipei 101 Skyline Spire)",
        "15 秒",
        "SKY_ANIM_01_Taipei101.mp4",
        "videos/skyscrapers/SKY_ANIM_01_Taipei101.mp4",
        "images/ui/SKY-01.jpeg",
        "8 節竹節層疊如意造型、綠色翡翠琉璃玻璃帷幕、避雷針頂部、信義區璀璨夜景、金色與紫色跨年百萬煙火瀑布。",
        "【0~5s】：由 SKY-01.jpeg 第一幀銜接，金黃色起重吊車將頂部最後一節竹節與避雷天線精準安嵌，整座綠色竹節寶塔逐層點亮璀璨翡翠琉璃光輝。\n【5~10s】：鏡頭以 360 度急速空拍圍繞台北 101 由下向上螺旋盤旋上升，俯瞰整座璀璨繁華的台北市盆地夜景與信義區五彩車流。\n【10~15s】：鏡頭升至塔頂尖端，101 塔身四面同時爆發出盛大壯麗的金色與粉紫色跨年煙火光瀑，塔頂射出直通星空的金色雷射光柱，全城歡呼，定格為奇蹟之樓。",
        "Cinematic 3D architectural animation, Pixar Disney celebration style, starting from the first frame image of Taipei 101 (SKY-01.jpeg). At 0-5s, a golden construction crane perfectly drops the final luminous spire piece onto the apex of Taipei 101, triggering a magnificent wave of emerald green and golden lights illuminating each stacked bamboo-pagoda section from bottom to top. At 5-10s, thrilling 360-degree spiral drone shot ascending rapidly along the skyscraper facade, revealing the breathtaking panoramic night cityscape of vibrant neon Taipei below. At 10-15s, camera crests the glowing spire as monumental colorful celebratory fireworks erupt from all sides of the tower into the starry night sky, brilliant golden spotlights illuminating the clouds, ultra-detailed glass reflections, 4K resolution, 60fps, festive triumphant wonder.",
        "【第一幀銜接】：以 SKY-01.jpeg 台北 101 特寫為起始。\n【建築象徵】：節節高升的竹節如意結構、逐層通電點亮琉璃光、盛大跨年煙火慶典。\n【視覺亮點】：台北夜景全景空拍、塔頂雷射貫穿星空。"
    ),
    (
        "B. 摩天大樓島 (5大世界名樓)",
        "SKY-ANIM-02",
        "哈里發塔 雲端神針竣工\n(Burj Khalifa Sky-Piercing Needle)",
        "15 秒",
        "SKY_ANIM_02_BurjKhalifa.mp4",
        "videos/skyscrapers/SKY_ANIM_02_BurjKhalifa.mp4",
        "images/ui/SKY-02.jpeg",
        "三瓣沙漠之花 Y 形遞減層次、世界第一高銀亮金屬科技感、杜拜音樂噴泉湖泊、阿拉伯灣日落金光、雲海倒灌平流層。",
        "【0~5s】：以 SKY-02.jpeg 哈里發塔為起點，銀白色梯級建築在阿拉伯灣落日餘暉下反射耀眼金芒，最頂端數十米鋼製尖塔完成精密對接，光環逐級向下綻放。\n【5~10s】：鏡頭以超廣角垂直俯衝加速，沿著銀色金屬反光帷幕從八百米雲端如閃電般直墜，掠過底層如夢似幻的杜拜音樂噴泉巨型水幕秀。\n【10~15s】：鏡頭瞬間反向拉升躍出雲海，破雲而出屹立於平流層星空之下，哈里發塔通體射出萬道璀璨的銀河雷射矩陣，照亮整座沙漠綠洲都市，冠絕全球！",
        "Cinematic 3D architectural animation, hyper-scale cinematic masterpiece, starting from the first frame image of Burj Khalifa (SKY-02.jpeg). At 0-5s, golden hour sunlight washes over the iconic Y-shaped stepped silver glass tower as the ultra-slender pinnacle needle spire snaps firmly into place, pulsing a wave of brilliant white-gold LED light cascading down 828 meters. At 5-10s, a thrilling, vertigo-inducing first-person drone dive rushes vertically down the mirrored metallic curtain walls, revealing the dancing fountains spraying water jets across turquoise lakes below. At 10-15s, the camera swoops back up into deep twilight, breaking through the sea of clouds where Burj Khalifa's pinnacle touches the stars, releasing an epic 360-degree laser and firework festival across the entire desert oasis metropolis, 4K, 60fps, absolute pinnacle wonder.",
        "【第一幀銜接】：以 SKY-02.jpeg 哈里發塔為起始（原配對錯位已修正）。\n【建築象徵】：三瓣沙漠之花幾何層次、828米平流層高度、銀白金屬反光質感。\n【視覺亮點】：垂直萬米俯衝與穿雲破曉、水舞噴泉全景、平流層雷射光網。"
    ),
    (
        "B. 摩天大樓島 (5大世界名樓)",
        "SKY-ANIM-03",
        "上海中心大廈 螺旋巨龍竣工\n(Shanghai Tower Spiral Dragon Spire)",
        "15 秒",
        "SKY_ANIM_03_ShanghaiTower.mp4",
        "videos/skyscrapers/SKY_ANIM_03_ShanghaiTower.mp4",
        "images/ui/SKY-03.jpeg",
        "120度旋轉雙層玻璃幕牆、流線型圓角與空中綠色花園、黃浦江 S 型江水倒影、外灘萬國建築群與陸家嘴賽博夜景、金色祥龍光帶。",
        "【0~5s】：以 SKY-03.jpeg 第一幀為起點，雙層玻璃帷幕猶如一條蜿蜒巨龍旋轉盤旋而上，最後一圈圓弧頂部帷幕閉合，巨龍歸位。\n【5~10s】：鏡頭跟隨一條金色光龍沿著 120 度旋轉上升的螺旋軌道直衝六百米高空，黃浦江兩岸的萬家燈火與外灘鐘樓在身後如波浪展現。\n【10~15s】：鏡頭躍出雲霧頂層的冠頂觀景台，陸家嘴三件套在雲霧夜景中熠熠生輝，上海中心大廈旋轉發射出金色與深紅的祥龍光暈，祥瑞君臨大地。",
        "Cinematic 3D animation, breathtaking futuristic urban animation style, beginning smoothly from the Shanghai Tower first frame (SKY-03.jpeg). At 0-5s, the elegant 120-degree twisting spiral glass double-curtain facade completes its majestic ascent, glowing with soft champagne gold and jade reflections like a slumbering coiled sky dragon. At 5-10s, a thrilling ascending roller-coaster camera tracks a golden light beam spiraling smoothly around the curved twisting grooves, showcasing the winding Huangpu River and historical Bund lights sparkling far below. At 10-15s, the camera crests the crown spire through ethereal mist into the futuristic Pudong night sky, the twisting tower pulsing with a grand harmonic light festival of golden and crimson ribbons, cinematic volumetric city fog, 4K, 60fps, majestic and legendary.",
        "【第一幀銜接】：以 SKY-03.jpeg 上海中心大廈為起點（原配對錯位已修正）。\n【建築象徵】：120度旋轉上升的雙層旋轉巨龍、陸家嘴核心天際線、黃浦江水之印。\n【視覺亮點】：沿著螺旋凹槽急速盤旋爬升鏡頭、外灘夜景全貌、頂層祥龍慶典光芒。"
    ),
    (
        "B. 摩天大樓島 (5大世界名樓)",
        "SKY-ANIM-04",
        "帝國大廈 經典名樓竣工\n(Empire State Building Art-Deco)",
        "15 秒",
        "SKY_ANIM_04_EmpireState.mp4",
        "videos/skyscrapers/SKY_ANIM_04_EmpireState.mp4",
        "images/ui/SKY-04.jpeg",
        "曼哈頓黃金落日天際線、經典裝飾藝術 (Art Deco) 幾何階梯退縮、飛船繫留塔尖、穿梭的黃色計程車車流、四柱交錯復古白色探照燈。",
        "【0~5s】：以 SKY-04.jpeg 為起點，裝飾藝術風格的石灰石塔樓在落日餘暉下散發古典金銅光輝，最後一座復古鋼架完成鉚接，整座大樓巍然屹立。\n【5~10s】：鏡頭從曼哈頓街道由低向高垂直急速仰衝爬升，掠過無數對稱的經典窗格與鋁合金浮雕飾帶，落日金光在窗玻璃上折射出絢爛光芒。\n【10~15s】：鏡頭躍出塔頂避雷天線，迎向深邃溫暖的黃金時段夕陽天際線，四盞巨型白色復古探照燈在天空交錯掃動，金色五彩碎紙如雨飄落，經典永恆。",
        "Cinematic 3D animation, vintage Art Deco cinematic masterpiece, initiating from the first frame of the Empire State Building (SKY-04.jpeg). At 0-5s, the grand limestone skyscraper gleams in radiant late-afternoon golden hour sunlight as the final vintage steel framework locks seamlessly into place atop the mooring mast. At 5-10s, a dramatic vertical soaring drone camera rockets straight up the facade, skimming past thousands of sun-reflecting windows and geometric art-deco eagle sculptures. At 10-15s, the camera crests the illuminated spire, revealing the epic Manhattan skyline and Hudson River bathed in warm sunset orange and purple hues, with iconic white celebration beam searchlights sweeping across the sky as golden confetti sparkles in the wind, timeless majestic atmosphere, 4K, 60fps.",
        "【第一幀銜接】：以 SKY-04.jpeg 帝國大廈建築立面為起始（原配對錯位已修正）。\n【建築象徵】：百老匯與曼哈頓黃金時代經典、裝飾藝術幾何雕花、探照燈交錯。\n【視覺亮點】：極速垂直爬升視角、金色夕陽映照整座曼哈頓島。"
    ),
    (
        "B. 摩天大樓島 (5大世界名樓)",
        "SKY-ANIM-05",
        "默迪卡 118 鑽石天際塔竣工\n(Merdeka 118 Diamond Facet Tower)",
        "15 秒",
        "SKY_ANIM_05_Merdeka118.mp4",
        "videos/skyscrapers/SKY_ANIM_05_Merdeka118.mp4",
        "images/ui/SKY-05.jpeg",
        "鑽石幾何多面切割晶體外殼、超長優雅垂直天線尖頂、空中綠洲露台、吉隆坡熱帶黃昏雲海、青藍色 LED 晶面脈衝。",
        "【0~5s】：由 SKY-05.jpeg 第一幀銜接，鑽石多面切割立面在熱帶晚霞下折射出如稜鏡般的五彩虹光，超長天線尖塔完成最終校準，通體晶瑩剔透。\n【5~10s】：鏡頭以動態側飛視角掠過多面幾何三角玻璃晶面，觀察光影在吉隆坡熱帶綠意與現代城市天際線之間的快速流動。\n【10~15s】：鏡頭由低角度仰拍躍升至頂峰尖針，整座 678.9 米鑽石神塔啟動通體青藍色與純金色相間的慶典燈光秀，塔頂光束劃破蒼穹，宣告現代建築奇蹟落成！",
        "Cinematic 3D architectural animation, luxury modern style, initiating smoothly from the Merdeka 118 first frame (SKY-05.jpeg). At 0-5s, the triangular multi-faceted crystalline glass facade gleams like a finely-cut raw diamond under a warm tropical dusk, as the soaring pinnacle spire gently docks and locks into position. At 5-10s, dynamic low-altitude drone orbit capturing the iridescent rainbow reflections dancing across thousands of angular diamond mirrors, overlooking the sprawling green hills and cityscape of Kuala Lumpur. At 10-15s, the camera swoops up to the apex observation deck as the entire Merdeka tower pulses with a rhythmic cascading wave of gold and cyan LED illumination from bottom to top, culminating in an awe-inspiring pillar of cyan light firing from the very tip into the twilight clouds, sharp crystalline aesthetics, 4K resolution, 60fps, ultra-modern triumph.",
        "【第一幀銜接】：以 SKY-05.jpeg 默迪卡 118 未來天際塔為起點（原配對錯位已修正）。\n【建築象徵】：如鑽石切割的多面體水晶立面、超高天線尖針、現代幾何奇蹟。\n【視覺亮點】：三角稜鏡對稱折射、青藍色 LED 矩陣波浪、平流層信標光柱。"
    ),

    # -------------------------------------------------------------
    # Category C: 5 Adventure Island Galaxy Boss Clear Animations (CORRECTED CONFLICTS)
    # -------------------------------------------------------------
    (
        "C. 探險島星系 (5大島嶼終極通關)",
        "ISL-ANIM-01",
        "第一島 · 隕石擊墜終極大捷\n(Meteor Crystal Island Boss Defeat)",
        "15 秒",
        "ISL_ANIM_01_MeteorDefense.mp4",
        "videos/islands/ISL_ANIM_01_MeteorDefense.mp4",
        "images/ui/ISL-01.jpeg",
        "懸浮紫色水晶簇、神秘發光洞窟入口、小型隕石坑、Kai 騎乘的烈焰噴火龍、彩虹音波雷射重砲、太空白熱星塵煙火。",
        "【0~5s】：第一幀由 ISL-01.jpeg 水晶洞窟島銜接，天際最後一顆遮天蔽日的暗黑骷髏巨型隕石呼嘯墜落，Kai 騎乘烈焰龍由洞窟神廟騰空而起。\n【5~10s】：Kai 堅定大聲喊出單字口號，烈焰龍口中轟然噴射出直徑數十米的彩虹音波雷射光束，筆直貫穿魔王隕石核心，裂紋瞬間蔓延。\n【10~15s】：巨型隕石在水晶島天空中轟然瓦解，炸裂成萬千顆五彩斑斕的星塵煙火如流星雨般灑向大地，紫色水晶簇全數發光共鳴，Kai 與火龍在半空擊掌大獲全勝！",
        "Cinematic 3D space-action animation, Pixar superhero style, starting smoothly from the first frame image of Meteor Crystal Island (ISL-01.jpeg). At 0-5s, a colossal glowing purple skull-faced boss meteor plummets from the burning sky toward the floating island, while brave kid hero Kai mounted on his friendly red dragon launches from the crystal cave temple with fierce determination. At 5-10s, Kai shouts a heroic English command, and the fire dragon unleashes a monumental beam of iridescent rainbow soundwave laser directly into the molten core of the meteor, spiderweb cracks spreading rapidly. At 10-15s, the gigantic meteor completely shatters into millions of harmless glittering stardust fireworks and sparkling confetti raining over the glowing purple crystal peaks, Kai and his dragon high-fiving mid-air in triumphant celebration, 4K resolution, 60fps, joyful and epic.",
        "【第一幀銜接】：以 ISL-01.jpeg 水晶洞窟島全景為起點。\n【核心劇情】：Kai 騎龍發射終極彩虹音波雷射砲，正面轟碎魔王隕石。\n【視覺亮點】：隕石在太空中化作萬千星塵煙火、英雄少男與火龍空中擊掌慶祝。"
    ),
    (
        "C. 探險島星系 (5大島嶼終極通關)",
        "ISL-ANIM-02",
        "第二島 · 摩天大樓建造島天際大成\n(Skyscraper Builder Island Metropolis Glory)",
        "15 秒",
        "ISL_ANIM_02_SkyscraperMetropolis.mp4",
        "videos/islands/ISL_ANIM_02_SkyscraperMetropolis.mp4",
        "images/ui/ISL-02.jpeg",
        "雲海之上的浮島、世界 5 大經典摩天大樓群、可愛黃金塔吊起重機、金色腳手架拆卸、天頂智慧之冠幾何能量光網、彩色慶祝熱氣球。",
        "【0~5s】：以 ISL-02.jpeg 第二島整體建造浮島為起點，海島上的五座摩天大樓全部建造完工，金色巨型塔吊起重機緩緩退場，夕陽將整座浮島染成燦爛純金。\n【5~10s】：五座大樓尖頂同時射出金色能量光束，在浮島天空中交織成一座巨大的「智慧之冠」光之幾何網絡，照亮整片雲海與蔚藍海洋。\n【10~15s】：鏡頭以超低空高速掠過雲浪，隨後猛烈仰衝穿過五座摩天大樓之間的立體空中天橋，全城鐘聲齊鳴，無數彩色慶祝熱氣球升空，建築工程大圓滿！",
        "Cinematic 3D animation, Pixar utopian builder style, initiating directly from Skyscraper Builder Island (ISL-02.jpeg). At 0-5s, golden hour sunlight washes over the floating builder island where all five iconic skyscrapers stand tall and complete, animated yellow cranes cheerfully waving and folding away. At 5-10s, every skyscraper pinnacle simultaneously shoots a pillar of radiant golden light into the blue sky, interweaving into a majestic geometric dome of architectural achievement above the clouds. At 10-15s, the camera takes an exhilarating swooping fly-through between skybridges connecting the towers, as hundreds of colorful hot-air balloons drift gracefully into the sunset sky and golden streamers cascade across the city, monumental celebration, 4K, 60fps, inspiring and majestic.",
        "【第一幀銜接】：以 ISL-02.jpeg 第二島群樓建造地圖為起點。\n【核心劇情】：五大世界名樓共同竣工，天頂交織成金色智慧之冠能量網。\n【視覺亮點】：海浪低空掠過至摩天峽谷垂直仰衝、熱氣球與金色彩帶全島狂歡。"
    ),
    (
        "C. 探險島星系 (5大島嶼終極通關)",
        "ISL-ANIM-03",
        "第三島 · 恐龍叢林與神獸共鳴大捷\n(Dino Prehistoric Island & Beast Resonance Triumph)",
        "15 秒",
        "ISL_ANIM_03_DinoBeastSanctuary.mp4",
        "videos/islands/ISL_ANIM_03_DinoBeastSanctuary.mp4",
        "images/ui/ISL-03.jpeg",
        "巨型史前蕨類樹屋、溫和噴發彩色泡泡的小火山、萌萌小暴龍與長頸龍、神獸完全體翱翔、陽光灑落遠古熱帶雨林、金色恐龍神獸皇冠獎盃。",
        "【0~5s】：以 ISL-03.jpeg 恐龍遠古叢林島為起點，畫面中的小暴龍與長頸龍在史前樹屋旁驚喜仰望，可愛的小火山噗噗噴出粉紅煙霧與彩色泡泡。\n【5~10s】：四大完全體神獸（翡翠天龍、雷鷹獅鷲、極光聖龍、熔岩泰坦）自雲端呼嘯而至，在恐龍叢林上方低空列隊翱翔，龍吟與恐龍歡鳴引起整座島嶼的金色聲波共振！\n【10~15s】：鏡頭推至島嶼中央高台，可愛的小恐龍們與神獸並肩圍繞在 Kai 身旁快樂躍動，天空綻放出一頂巨大的「遠古叢林口語大師」黃金恐龍皇冠，漫天熱帶繁花盛開！",
        "Cinematic 3D animation, Disney Pixar prehistoric fantasy style, starting directly from the Dino Prehistoric Island first frame (ISL-03.jpeg). At 0-5s, camera focuses on the cute chubby baby T-rex and friendly long-necked brachiosaurus cheering beside giant fern treehouses, as the gentle cartoon volcano puffs soft pink clouds and floating rainbow bubbles into the sunny jungle sky. At 5-10s, the four legendary guardian beasts (Emerald Dragon, Thunder Gryphon, Glacial Wyrm, Magma Titan) swoop down gracefully through giant tree canopies and rope bridges, their harmonic voices creating ripples of golden phonics soundwaves that heal and awaken the lush ancient island. At 10-15s, Kai, the friendly dinosaurs, and the mythical dragons gather atop a sunlit cliff to celebrate together, as a glorious golden prehistoric dinosaur-and-dragon master trophy illuminates the sky, vibrant tropical petals drifting in the breeze, 4K resolution, 60fps, warmhearted and joyful.",
        "【第一幀銜接】：以 ISL-03.jpeg 恐龍遠古叢林島為起點（已修正衝突：融合恐龍樂園與神獸共鳴）。\n【核心劇情】：可愛史前恐龍與四大成龍神獸同慶，音波共振驅散迷霧。\n【視覺亮點】：粉紅火山噴泡泡、萌萌小暴龍長頸龍同樂、熱帶繁花與黃金恐龍神獸皇冠。"
    ),
    (
        "C. 探險島星系 (5大島嶼終極通關)",
        "ISL-ANIM-04",
        "第四島 · 糖果夢幻點心島寶藏大盛宴\n(Sweet Candy Wonderland Maze & Treasure Bloom)",
        "15 秒",
        "ISL_ANIM_04_CandyMazeTreasure.mp4",
        "videos/islands/ISL_ANIM_04_CandyMazeTreasure.mp4",
        "images/ui/ISL-04.jpeg",
        "飄浮薑餅城堡、巨型七彩棒棒糖森林、流淌的溫熱牛奶巧克力河、粉紅棉花糖山丘、小熊軟糖守衛、英文字母糖果金幣雨、黃金棒棒糖智慧獎盃。",
        "【0~5s】：以 ISL-04.jpeg 糖果夢幻點心島為起點，Kai 手持發光的黃金音叉鑰匙來到薑餅城堡門前，七彩螺旋棒棒糖森林在粉紅棉花糖雲朵下旋轉。\n【5~10s】：Kai 轉動音波鑰匙，薑餅城堡巨門歡快彈開，伴隨歡欣的音樂盒音效，融化的牛奶巧克力河歡暢奔流，噴發出無數閃耀著英文字母的彩色小熊軟糖與金箔巧克力幣！\n【10~15s】：鏡頭在糖果迷宮上空暢快飛掠，可愛的小熊軟糖們在薄荷跳跳糖石階上快樂跳舞，天空中緩緩升起一座閃耀無比的「黃金巨型棒棒糖聽力之星獎盃」，全島陷入甜蜜狂歡！",
        "Cinematic 3D animation, whimsical Pixar candy wonderland style, starting smoothly from the first frame image of Sweet Candy Wonderland Island (ISL-04.jpeg). At 0-5s, hero kid Kai approaches the magnificent floating gingerbread castle nestled amidst towering rainbow swirl lollipop trees and cotton candy pink hills, holding a glowing golden tuning-fork microphone key. At 5-10s, unlocking the candy castle gates triggers a cheerful musical chime as the doors swing open, releasing a lavish, joyful eruption of glowing alphabet jelly beans, gold-wrapped chocolate coins, and sparkling sugar crystals flying like confetti across chocolate rivers. At 10-15s, dynamic camera swoops over the sweet candy maze where adorable bouncy gummy bears celebrate and dance on peppermint stepping stones, as a grand rotating Golden Lollipop Trophy crowns the gingerbread spire under a shower of pastel sparkle dust, 4K, 60fps, deliciously magical.",
        "【第一幀銜接】：以 ISL-04.jpeg 糖果點心島為起點（已修正衝突：由原海底金庫改為糖果夢幻迷宮寶藏）。\n【核心劇情】：盲聽尋寶金鑰開啟薑餅城堡，噴發字母軟糖與金箔巧克力幣大盛宴。\n【視覺亮點】：巧克力河奔流、七彩棒棒糖旋轉、小熊軟糖跳舞、黃金棒棒糖皇冠獎盃。"
    ),
    (
        "C. 探險島星系 (5大島嶼終極通關)",
        "ISL-ANIM-05",
        "第五島 · 亞特蘭提斯海底城之光\n(Atlantis Coral Kingdom Arena Triumph)",
        "15 秒",
        "ISL_ANIM_05_AtlantisCoralArena.mp4",
        "videos/islands/ISL_ANIM_05_AtlantisCoralArena.mp4",
        "images/ui/ISL-05.jpeg",
        "發光透明水晶氣泡穹頂 (Crystal Biodome)、七彩分支珊瑚礁宮殿、黃色卡通潛水艇、發光海豚與溫柔海龜衛隊、穿透清澈海水的金色丁達爾聖光、終極海皇金三叉戟/皇冠獎盃。",
        "【0~5s】：以 ISL-05.jpeg 亞特蘭提斯海底珊瑚島為起點，深海中的巨型發光水晶氣泡穹頂內，競技場中央的遠古珍珠圖騰正匯聚強大的能量脈衝。\n【5~10s】：Kai 攜手海洋生物衛隊一同大聲吟誦終極單字，珍珠圖騰爆發出直貫海面的純金聖光，溫暖金光驅散深海陰霾，整片珊瑚礁宮殿被七彩霓虹與清澈碧藍海水照亮！\n【10~15s】：鏡頭在水下珊瑚城堡間高速穿梭，迷你黃色潛水艇噴出慶祝愛心氣泡，發光海豚與海龜在空中翻滾共舞，天頂浮現出「KAI-SPEAK 亞特蘭提斯海皇終極榮耀」金色三叉戟星環，星系迎來大圓滿！",
        "Cinematic 3D animation, Pixar underwater fantasy masterpiece style, starting directly from the Deep-Sea Coral Atlantis Island (ISL-05.jpeg). At 0-5s, the camera enters through the glowing crystal bubble biodome kingdom resting on the vibrant coral reef seabed, where Kai stands confidently in the ancient pearl arena surrounded by friendly sea turtles and playful dolphins. At 5-10s, Kai channels all the master language power into the central pearl pillar, sending a blinding pulse of golden sunlight filtering deep down through the turquoise waters, illuminating towering coral reef palaces in dazzling bioluminescent colors. At 10-15s, sweeping cinematic camera tracks joyful yellow cartoon submarines puffing heart-shaped air bubbles as sea creatures dance, and a monumental holographic golden 'KAI-SPEAK OCEAN MASTER' trident-crown illuminates the ocean sky, 4K resolution, 60fps, awe-inspiring underwater paradise triumph.",
        "【第一幀銜接】：以 ISL-05.jpeg 亞特蘭提斯水下珊瑚島為起點（已修正衝突：由原漆黑魔王島改為海底珊瑚城市王者大捷）。\n【核心劇情】：亞特蘭提斯水晶穹頂競技場大捷，終極珍珠圖騰激發金色丁達爾聖光。\n【視覺亮點】：清澈碧藍水下宮殿、發光海豚海龜翻滾、黃色潛水艇愛心泡泡、金色海皇三叉戟星環。"
    )
]

# Set Title
ws.merge_cells("A1:K1")
title_cell = ws["A1"]
title_cell.value = "KaiSpeak 奇妙星 15 秒高清終極通關動畫提示詞總表 (MiniMax Video-01 專用 · 修正版)"
title_cell.font = Font(name="Arial", size=16, bold=True, color="FFFFFF")
title_cell.fill = PatternFill(start_color="1E1B4B", end_color="1E1B4B", fill_type="solid")
title_cell.alignment = Alignment(horizontal="center", vertical="center")
ws.row_dimensions[1].height = 42

# Subtitle
ws.merge_cells("A2:K2")
sub_cell = ws["A2"]
sub_cell.value = "說明：本清單已精確校正「4 筆摩天大樓圖片錯位」及「恐龍島/糖果島/海底城市」圖片主題一致性。專供地端 MiniMax Video-01 首幀 I2V 15 秒動畫製作。"
sub_cell.font = Font(name="Arial", size=10, italic=True, color="4338CA")
sub_cell.fill = PatternFill(start_color="EEF2FF", end_color="EEF2FF", fill_type="solid")
sub_cell.alignment = Alignment(horizontal="center", vertical="center")
ws.row_dimensions[2].height = 26

# Headers
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
    "提示詞中文意境解析與特效要點 (修正說明)"
]

header_fill = PatternFill(start_color="312E81", end_color="312E81", fill_type="solid")
header_font = Font(name="Arial", size=11, bold=True, color="FFFFFF")
thin_border = Border(
    left=Side(style="thin", color="CBD5E1"),
    right=Side(style="thin", color="CBD5E1"),
    top=Side(style="thin", color="CBD5E1"),
    bottom=Side(style="thin", color="CBD5E1"),
)

for col_num, h_text in enumerate(headers, 1):
    cell = ws.cell(row=3, column=col_num)
    cell.value = h_text
    cell.fill = header_fill
    cell.font = header_font
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    cell.border = thin_border
ws.row_dimensions[3].height = 32

# Fill Data Rows
cat_colors = {
    "A": ("F0FDF4", "166534"),  # Mint Green for Beasts
    "B": ("FEF3C7", "92400E"),  # Warm Amber for Skyscrapers
    "C": ("EFF6FF", "1E40AF"),  # Soft Blue for Islands
}

for row_idx, item in enumerate(data, 4):
    cat_key = item[0][0]
    bg_color, fg_color = cat_colors.get(cat_key, ("FFFFFF", "000000"))
    row_fill = PatternFill(start_color=bg_color, end_color=bg_color, fill_type="solid")

    for col_idx, val in enumerate(item, 1):
        cell = ws.cell(row=row_idx, column=col_idx)
        cell.value = val
        cell.fill = row_fill
        cell.border = thin_border
        
        # Alignments & Fonts
        if col_idx in [1, 2, 4]:
            cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
            cell.font = Font(name="Arial", size=10, bold=(col_idx == 2))
        elif col_idx in [5, 6, 7]:
            cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
            cell.font = Font(name="Courier New", size=9, bold=(col_idx == 5))
        elif col_idx == 3:
            cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
            cell.font = Font(name="Arial", size=10, bold=True)
        else:
            cell.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
            cell.font = Font(name="Arial", size=9)

    ws.row_dimensions[row_idx].height = 125

# Column Widths
col_widths = {
    "A": 22,  # 分類
    "B": 14,  # 編號
    "C": 28,  # 項目名稱
    "D": 10,  # 目標時長
    "E": 34,  # 建議檔案名稱
    "F": 38,  # 目標存放路徑
    "G": 24,  # 首幀參考圖
    "H": 36,  # 場景特色元素
    "I": 52,  # 15秒動態節奏
    "J": 78,  # MiniMax 提示詞 (英文)
    "K": 48   # 中文意境解析
}

for col_letter, width in col_widths.items():
    ws.column_dimensions[col_letter].width = width

output_file = "KaiSpeak_15s_Cinematic_Animation_Prompts_MiniMax.xlsx"
wb.save(output_file)
print(f"Successfully generated corrected Excel: {output_file}")
