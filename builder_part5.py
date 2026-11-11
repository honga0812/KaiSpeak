# -*- coding: utf-8 -*-
"""Builder Part 5: Colors/Shapes (50 words) and Actions (50 words).
All sentences strictly adhere to:
L1: 3-4 words (Early stage, sight words)
L2: 4-6 words (Everyday routine)
L3: 6-8 words (Progressive challenge, simple child-friendly vocabulary)
"""

PART_5_DATA = {
    # ================= COLORS & SHAPES (50 words) =================
    "red": {
        "s1": "I see red roses.", "t1": "我看見紅色的玫瑰花。",
        "s2": "The ripe apple is red.", "t2": "熟透的水果蘋果是紅澄澄的。",
        "s3": "The shiny red apple is very sweet.", "t3": "這顆紅彤彤誘人的蘋果吃起來好甜。"
    },
    "blue": {
        "s1": "The ocean is blue.", "t1": "大海是湛藍湛藍的。",
        "s2": "Blue sky has no clouds.", "t2": "碧藍如洗的晴空萬里無雲。",
        "s3": "The vast sky is deep ocean blue.", "t3": "高遠的天空呈現出深邃純淨的蔚藍色。"
    },
    "green": {
        "s1": "The grass is green.", "t1": "小草是翠綠翠綠的。",
        "s2": "Fresh green leaves sprout everywhere.", "t2": "到處都冒出了鮮綠嫩綠的新樹葉。",
        "s3": "Fresh green grass grows in the park.", "t3": "公園裡長滿了綠油油又茂盛的小草。"
    },
    "yellow": {
        "s1": "The banana is yellow.", "t1": "香蕉是明亮的黃色。",
        "s2": "Yellow sunflowers face the sun.", "t2": "金黃色的向日葵朝向溫暖的太陽。",
        "s3": "Bright yellow lemons grow on the tree.", "t3": "明亮金黃的檸檬掛在結滿果實的樹上。"
    },
    "pink": {
        "s1": "I like pink flowers.", "t1": "我喜歡粉紅色的花朵。",
        "s2": "Pink cherry blossoms bloom early.", "t2": "粉嫩的櫻花在春天早早綻放枝頭。",
        "s3": "She wears a pretty soft pink dress.", "t3": "她今天穿了一件漂亮溫柔的粉紅色洋裝。"
    },
    "purple": {
        "s1": "Eat sweet purple grapes.", "t1": "吃甜甜的紫葡萄。",
        "s2": "Sweet purple grapes grow high.", "t2": "香甜的紫葡萄掛在長長的綠藤架上。",
        "s3": "Sweet purple grapes grow in the vineyard.", "t3": "紫色的葡萄在陽光充沛的果園裡成熟。"
    },
    "brown": {
        "s1": "See the brown bear.", "t1": "看那隻棕色的大熊。",
        "s2": "Brown acorns fall from oak.", "t2": "深褐色的橡子從高高的橡樹枝頭掉落。",
        "s3": "A fluffy brown bear catches a fish.", "t3": "一隻毛茸茸的棕熊在清澈小溪裡抓魚吃。"
    },
    "white": {
        "s1": "Snow is pure white.", "t1": "白雪純潔潔白無瑕。",
        "s2": "White fluffy clouds float gently.", "t2": "潔白鬆軟的朵朵白雲在藍天中隨風漫步。",
        "s3": "Pure white snow falls from the sky.", "t3": "潔白純淨的雪花紛紛揚揚從天空飄落。"
    },
    "black": {
        "s1": "Night sky is black.", "t1": "夜晚的天空漆黑深邃。",
        "s2": "A cute black cat purrs.", "t2": "一隻靈巧的小黑貓蹲在門口輕聲呼嚕。",
        "s3": "A little black cat plays with yarn.", "t3": "一隻可愛的小黑貓在地毯上玩著毛線球。"
    },
    "gold": {
        "s1": "Wear a gold coin.", "t1": "戴著一枚金色的幣飾。",
        "s2": "Win the shiny gold medal.", "t2": "在跑步比賽中贏得閃亮的冠軍金牌。",
        "s3": "The gold medal shines on his chest.", "t3": "閃閃發光的金色獎牌榮譽地掛在他胸前。"
    },
    "circle": {
        "s1": "Draw a round circle.", "t1": "畫一個圓圓的圓形。",
        "s2": "The yellow sun is circle.", "t2": "頭頂紅彤彤的大太陽是一個大圓形。",
        "s3": "We sit in a circle on carpet.", "t3": "我們大家圍成一個大圓圈坐在地毯上。"
    },
    "square": {
        "s1": "Draw a neat square.", "t1": "畫一個端正的正方形。",
        "s2": "Chessboard has sixty-four small squares.", "t2": "國際象棋盤由整齊的六十四個小方格組成。",
        "s3": "The toy box has four square sides.", "t3": "這個漂亮的積木收納盒四面都是正方形。"
    },
    "triangle": {
        "s1": "Draw a green triangle.", "t1": "畫一個綠色的三角形。",
        "s2": "A pizza slice is triangle.", "t2": "切下來的一片披薩呈現出三角形狀。",
        "s3": "The roof of the house forms triangle.", "t3": "小木屋的屋頂輪廓呈現出一個穩固的三角形。"
    },
    "round": {
        "s1": "The ball is round.", "t1": "皮球是圓滾滾的。",
        "s2": "Round moon lights the night.", "t2": "滿月圓圓的銀色光芒照亮安靜的夜晚。",
        "s3": "The round orange ball bounces very high.", "t3": "圓滾滾的橘色籃球在地板上彈得好高。"
    },
    "line": {
        "s1": "Draw a straight line.", "t1": "畫一條筆直筆直的線。",
        "s2": "Students stand in straight line.", "t2": "同學們在操場上整齊地排成一列縱隊。",
        "s3": "Students stand in a neat straight line.", "t3": "小朋友們在走廊上排成一條筆直整齊的隊伍。"
    },
    "light": {
        "s1": "The lamp gives light.", "t1": "檯燈散發柔和的光芒。",
        "s2": "Morning light fills my room.", "t2": "清晨的第一道陽光灑滿了我的小臥室。",
        "s3": "Warm sunlight fills our cozy study room.", "t3": "溫暖柔和的陽光照亮了我們溫馨的小書房。"
    },
    "dark": {
        "s1": "Night sky is dark.", "t1": "夜晚的天空好黑。",
        "s2": "Stars twinkle in dark night.", "t2": "明亮的星光在漆黑深邃的夜空中閃爍。",
        "s3": "Stars shine brightly in the dark sky.", "t3": "閃爍的群星在漆黑的夜空中格外明亮動人。"
    },
    "bright": {
        "s1": "The sun is bright.", "t1": "太陽格外明亮耀眼。",
        "s2": "Bright smiles cheer everyone up.", "t2": "燦爛陽光的微笑讓身邊每個人都開心。",
        "s3": "The bright morning sun warms our garden.", "t3": "明朗燦爛的晨光把花園照耀得生機盎然。"
    },
    "diamond": {
        "s1": "See the diamond shape.", "t1": "看那個菱形狀鑽石狀。",
        "s2": "Flying kite has diamond shape.", "t2": "天空中高高飛揚的風箏呈現菱形外觀。",
        "s3": "A colorful kite has a diamond shape.", "t3": "在空中飛翔的漂亮風箏呈現出一個大菱形。"
    },
    "silver": {
        "s1": "The spoon is silver.", "t1": "小湯匙是銀色的。",
        "s2": "Silver moon shines on lake.", "t2": "銀色的月光靜靜倒映在平靜的湖面上。",
        "s3": "A shiny silver spoon stirs warm soup.", "t3": "銀光閃閃的金屬小湯匙輕輕攪動著熱湯。"
    },
    "gray": {
        "s1": "The cloud is gray.", "t1": "雲朵變成了灰濛濛的。",
        "s2": "Gray elephant walks with baby.", "t2": "灰色的大象媽媽帶著小象漫步在草原上。",
        "s3": "Rain falls softly from the gray clouds.", "t3": "細雨綿綿從天空中厚厚的灰色雨雲落下。"
    },
    "violet": {
        "s1": "See the violet flower.", "t1": "看那一朵紫羅蘭花。",
        "s2": "Sweet violet blooms in shade.", "t2": "淡雅的小紫羅蘭花在樹蔭下悄悄綻放。",
        "s3": "Sweet violet flowers bloom in the forest.", "t3": "淡雅幽香的小紫羅蘭花在綠色森林中綻放。"
    },
    "cyan": {
        "s1": "Water glows bright cyan.", "t1": "海水泛著清新的青碧色。",
        "s2": "Cyan ocean water is clear.", "t2": "熱帶小島的青色潟湖海水清澈透明見底。",
        "s3": "Tropical sea water glows a clear cyan.", "t3": "海島邊緣熱帶海灣呈現出透明夢幻的青碧色。"
    },
    "beige": {
        "s1": "The sofa is beige.", "t1": "沙發是米褐色的。",
        "s2": "Beige cotton coat is cozy.", "t2": "米白色的棉布風衣穿起來格外優雅溫馨。",
        "s3": "We sit on the cozy beige sofa.", "t3": "我們一家人圍坐在米白色的柔軟大沙發上。"
    },
    "golden": {
        "s1": "See the golden sun.", "t1": "看那一輪金燦燦的太陽。",
        "s2": "Golden wheat sways in wind.", "t2": "金黃色的麥浪在秋風吹拂下層層翻滾。",
        "s3": "Golden morning sunlight warms the green grass.", "t3": "金黃燦爛的晨光把草地照耀得溫暖柔和。"
    },
    "bronze": {
        "s1": "Touch the bronze bell.", "t1": "摸摸厚重的青銅鐘。",
        "s2": "The antique bronze statue glimmers.", "t2": "古老的青銅雕像在自然光下泛著古樸光澤。",
        "s3": "The ancient bronze bell rings with sound.", "t3": "古老沉穩的青銅古鐘發出悠揚深遠的鐘鳴。"
    },
    "rectangle": {
        "s1": "The door is rectangle.", "t1": "房門是長方形的。",
        "s2": "Picture book has rectangle shape.", "t2": "精裝繪本的封面呈現工整長方形結構。",
        "s3": "The wooden study desk is a rectangle.", "t3": "我們讀書寫字的小書桌呈現端正的長方形。"
    },
    "oval": {
        "s1": "An egg is oval.", "t1": "雞蛋是橢圓形的。",
        "s2": "Watermelon has big oval shape.", "t2": "熟透的大西瓜呈現圓滾滾的橢圓形形狀。",
        "s3": "The white duck egg is an oval.", "t3": "窩裡剛下的一顆新鮮水煮蛋呈現出橢圓形。"
    },
    "crescent": {
        "s1": "See the crescent moon.", "t1": "看那輪彎彎的月牙。",
        "s2": "Crescent moon smiles in sky.", "t2": "細細彎彎的蛾眉月像微笑掛在夜空。",
        "s3": "A golden crescent moon shines in sky.", "t3": "一輪金黃色的彎彎新月在星空宛如溫柔笑臉。"
    },
    "dot": {
        "s1": "Draw a red dot.", "t1": "畫一個紅色的圓點點。",
        "s2": "Ladybug has black round dots.", "t2": "可愛的小瓢蟲背上點綴著七個黑斑點。",
        "s3": "The red ladybug has black round dots.", "t3": "小瓢蟲紅豔豔的背翅上長著小黑斑圓點。"
    },
    "stripe": {
        "s1": "Zebras have bold stripes.", "t1": "斑馬身上長著條紋。",
        "s2": "Tigers have orange black stripes.", "t2": "威風的老虎身上長著橘黑相間的斑紋。",
        "s3": "Zebras have black and white body stripes.", "t3": "大斑馬奔跑時身上黑白相間的斑紋格外醒目。"
    },
    "spiral": {
        "s1": "Snail has spiral shell.", "t1": "蝸牛背著螺旋形的外殼。",
        "s2": "Lollipop swirls in sweet spiral.", "t2": "棒棒糖旋轉出令人垂涎的七彩螺旋圖紋。",
        "s3": "The snail shell has a pretty spiral.", "t3": "小蝸牛背上背著一個旋轉漂亮的螺紋小外殼。"
    },
    "cube": {
        "s1": "Roll the wooden cube.", "t1": "擲擲木頭正方體積木。",
        "s2": "Rubik cube has six colors.", "t2": "魔術方塊六個面上分別有六種不同顏色。",
        "s3": "We build a castle with block cubes.", "t3": "我們用一個個立方體小積木搭建起高高城堡。"
    },
    "cone": {
        "s1": "Eat sweet ice cone.", "t1": "吃甜筒冰淇淋。",
        "s2": "Orange traffic cone warns cars.", "t2": "施工路段擺放著醒目的橘色三角錐。",
        "s3": "Ice cream sits in a waffle cone.", "t3": "香甜的香草冰淇淋球裝在香脆的甜筒甜錐裡。"
    },
    "cylinder": {
        "s1": "The can is cylinder.", "t1": "鐵罐是圓柱形的。",
        "s2": "A soup can is cylinder.", "t2": "廚房裡的濃湯金屬罐呈現標準圓柱外形。",
        "s3": "A tall drinking cup is a cylinder.", "t3": "我們每天喝水的高腳水杯呈現出圓柱形狀。"
    },
    "sphere": {
        "s1": "The ball is sphere.", "t1": "球體是完美球狀。",
        "s2": "Earth is a giant sphere.", "t2": "我們居住的美麗地球是一顆巨大的球體。",
        "s3": "Our planet Earth is a blue sphere.", "t3": "我們居住的這顆美麗行星是一顆湛藍球體。"
    },
    "curve": {
        "s1": "The road has curve.", "t1": "前方的道路有彎道。",
        "s2": "Draw a smooth curved line.", "t2": "用柔軟畫筆在紙上勾畫出一條優雅弧線。",
        "s3": "The train travels around a gentle curve.", "t3": "疾馳的火車沿著山腰一道平緩的弧形軌道前行。"
    },
    "angle": {
        "s1": "Measure the sharp angle.", "t1": "測量尖尖的角角落度數。",
        "s2": "Triangle has three sharp angles.", "t2": "任意三角形都擁有三個鮮明的幾何角度。",
        "s3": "A square has four sharp right angles.", "t3": "每個正方形都工整地擁有四個方正的直角。"
    },
    "edge": {
        "s1": "Touch table smooth edge.", "t1": "摸摸桌子平滑的邊緣。",
        "s2": "Walk along the sidewalk edge.", "t2": "小心翼翼地沿著人行道安全外緣漫步。",
        "s3": "Do not leave glass near table edge.", "t3": "裝滿水的水杯不要擺在靠近桌邊易碰倒處。"
    },
    "point": {
        "s1": "Point at the star.", "t1": "伸手指向天上的星星。",
        "s2": "Pencil has sharp writing point.", "t2": "削好的鉛筆前端有著尖銳順手的筆尖。",
        "s3": "Use a pencil with a sharp point.", "t3": "寫字畫畫時要用削好筆尖順手的鉛筆。"
    },
    "thick": {
        "s1": "Read a thick book.", "t1": "讀一本厚厚的故事書。",
        "s2": "Wear a thick winter coat.", "t2": "在雪天穿上一件厚實保暖的羊毛大衣。",
        "s3": "I read a thick picture story book.", "t3": "我在圖書館借了一本厚厚的精美童話故事書。"
    },
    "thin": {
        "s1": "Cut a thin slice.", "t1": "切下一片薄薄的切片。",
        "s2": "Thin ice covers the puddle.", "t2": "清晨寒冷的小水窪上結著一層薄薄的冰皮。",
        "s3": "Draw pictures on thin white tracing paper.", "t3": "我們在透光的薄白描紙上臨摹漂亮的卡通。"
    },
    "wide": {
        "s1": "Cross the wide road.", "t1": "穿過寬闊平整的大馬路。",
        "s2": "Open your arms very wide.", "t2": "把雙臂大大地向兩側張開擁抱自然。",
        "s3": "Cars travel on the wide modern highway.", "t3": "寬闊的大馬路能讓許多汽車並排行駛無阻。"
    },
    "narrow": {
        "s1": "Walk the narrow path.", "t1": "走在窄窄的林間小路上。",
        "s2": "The narrow path winds up.", "t2": "陡峭曲折的小路蜿蜒通往山頂小木屋。",
        "s3": "We walk along a narrow forest path.", "t3": "我們沿著森林裡一條幽靜窄小的小石徑散步。"
    },
    "big": {
        "s1": "The elephant is big.", "t1": "大象的身軀好巨大。",
        "s2": "A big bear eats honey.", "t2": "森林裡的大棕熊大口品嚐香甜的野蜂蜜。",
        "s3": "The blue whale is very big animal.", "t3": "深海裡遨遊的藍鯨是地球上最大的動物。"
    },
    "small": {
        "s1": "The mouse is small.", "t1": "小老鼠個頭小巧玲瓏。",
        "s2": "Tiny ant is very small.", "t2": "在泥土上搬東西的小黑螞蟻非常小巧。",
        "s3": "A small cute baby mouse eats cheese.", "t3": "一隻小巧可愛的小老鼠正抱著起司大快朵頤。"
    },
    "tall": {
        "s1": "The tree is tall.", "t1": "這棵大樹長得好高。",
        "s2": "Giraffe is a tall animal.", "t2": "脖子長長的長頸鹿是世界上最高的身軀。",
        "s3": "Tall green trees grow in the mountains.", "t3": "高聳入雲霄的常青松柏在大山間傲然生長。"
    },
    "short": {
        "s1": "The grass is short.", "t1": "修剪好的草皮短短的。",
        "s2": "Take a short healthy break.", "t2": "讀書累了做個短短的眼部放鬆休息。",
        "s3": "Green short grass grows along the pathway.", "t3": "綠油油短短的修剪草坪平整覆蓋在小路兩側。"
    },
    "deep": {
        "s1": "The ocean is deep.", "t1": "海水無邊無際深不可測。",
        "s2": "Whales dive into deep ocean.", "t2": "巨大的藍鯨一頭扎入深邃清澈的深藍海洋。",
        "s3": "Whales swim inside the deep cold ocean.", "t3": "巨大的鯨魚群在深不可測的大洋深處自在游弋。"
    },
    "clear": {
        "s1": "The sky is clear.", "t1": "天空晴朗清澈無比。",
        "s2": "Clear stream flows over rocks.", "t2": "清澈甘甜的山泉水潺潺流過圓潤的岩石。",
        "s3": "Clear clean water flows in mountain lake.", "t3": "高山上的天池湖水像鏡子一樣清澈透亮無暇。"
    },

    # ================= ACTIONS (50 words) =================
    "play": {
        "s1": "Play with your toys.", "t1": "開心地玩你的玩具。",
        "s2": "Children play in the park.", "t2": "孩子們在草地上開心地追逐做遊戲。",
        "s3": "We play fun puzzle games after school.", "t3": "放學後我們聚在客廳一起玩好玩的桌遊遊戲。"
    },
    "swim": {
        "s1": "Swim in cool water.", "t1": "在清涼的水中暢游。",
        "s2": "Fish swim across the pond.", "t2": "金魚甩動著尾巴敏捷游過清澈的小池塘。",
        "s3": "We swim in the cool pool summer.", "t3": "炎炎夏日我們在清涼乾淨的泳池裡快活戲水。"
    },
    "sing": {
        "s1": "Sing a happy song.", "t1": "唱一首快樂動聽的歌。",
        "s2": "Birds sing in the morning.", "t2": "枝頭小鳥在清晨時分齊聲鳴叫唱晨曲。",
        "s3": "We sing a cheerful song together happily.", "t3": "我們在音樂課上開開心心地齊聲合唱童謠。"
    },
    "dance": {
        "s1": "Dance to the music.", "t1": "跟著音樂節奏跳舞。",
        "s2": "Twirl and dance with joy.", "t2": "開心地轉著圈兒跳起歡快的踢踏舞步。",
        "s3": "Children dance happily to the upbeat music.", "t3": "小朋友們隨著歡快的音樂節拍歡快地跳舞。"
    },
    "read": {
        "s1": "Read a good book.", "t1": "讀一本開卷有益的好書。",
        "s2": "Read bedtime stories every night.", "t2": "每晚睡覺前靠在床頭安靜讀一本小繪本。",
        "s3": "I read funny stories at my desk.", "t3": "我坐在明亮整潔的小書桌前看有趣的故事書。"
    },
    "write": {
        "s1": "Write with a pencil.", "t1": "用削好的鉛筆寫字。",
        "s2": "Write your name very neatly.", "t2": "在作文本上工整平正地寫下你的名字。",
        "s3": "I write my name with black ink.", "t3": "我用黑色的墨水筆在作業本上工整簽名。"
    },
    "draw": {
        "s1": "Draw a red heart.", "t1": "在畫紙上畫顆小愛心。",
        "s2": "Draw a picture with crayons.", "t2": "用繽紛的彩色蠟筆畫一幅漂亮風景畫。",
        "s3": "I draw a sunny picture with crayons.", "t3": "我用五彩繽紛的蠟筆在畫紙上畫美麗風景。"
    },
    "cook": {
        "s1": "Cook a warm dinner.", "t1": "烹飪一頓熱騰騰的晚餐。",
        "s2": "Mom cooks delicious noodle soup.", "t2": "媽媽在廚房煮了一大鍋香濃可口的牛肉麵。",
        "s3": "Dad cooks delicious pancakes for our breakfast.", "t3": "爸爸為我們的週末早餐煎了香噴噴的鬆餅。"
    },
    "eat": {
        "s1": "Eat a red apple.", "t1": "吃一顆甜甜的紅蘋果。",
        "s2": "Eat fresh vegetables every day.", "t2": "每天都要多吃綠色新鮮蔬菜保持營養。",
        "s3": "We eat dinner together at the table.", "t3": "我們全家人圍坐在溫暖的餐桌旁一起吃飯。"
    },
    "drink": {
        "s1": "Drink a cup water.", "t1": "大口喝一杯溫開水。",
        "s2": "Drink warm milk before bed.", "t2": "睡前喝一杯香濃溫熱的牛奶幫助睡眠。",
        "s3": "I drink a glass of milk daily.", "t3": "我每天早晨都會喝滿滿一杯新鮮的牛奶。"
    },
    "help": {
        "s1": "Help clean the table.", "t1": "幫忙擦拭收拾餐桌。",
        "s2": "Help your friends with kindness.", "t2": "充滿愛心與善意地主動幫助身邊的同學。",
        "s3": "We help each other learn new words.", "t3": "我們在學習新單字時互相幫助彼此進步。"
    },
    "wash": {
        "s1": "Wash hands with soap.", "t1": "用肥皂洗乾淨雙手。",
        "s2": "Wash face after waking up.", "t2": "早晨起床後用溫水把小臉洗得精神爽朗。",
        "s3": "Wash your hands before eating any meals.", "t3": "在每次吃東西之前一定要把雙手洗乾淨。"
    },
    "open": {
        "s1": "Open the front door.", "t1": "推開大門迎接陽光。",
        "s2": "Open your textbook to page.", "t2": "把英語課本翻到今天上課的進度頁面。",
        "s3": "Please open the window for fresh air.", "t3": "請把窗戶打開讓新鮮空氣流進房間裡。"
    },
    "close": {
        "s1": "Close the bedroom door.", "t1": "輕輕關上臥室房門。",
        "s2": "Close your eyes and rest.", "t2": "閉上雙眼深呼吸讓大腦安靜休息片刻。",
        "s3": "Please close the door after you leave.", "t3": "離開房間時請輕輕帶上門保持室內安靜。"
    },
    "catch": {
        "s1": "Catch the flying ball.", "t1": "穩穩接住飛來的皮球。",
        "s2": "Cats catch mice at night.", "t2": "敏捷的小花貓在夜幕中靈巧抓捕小老鼠。",
        "s3": "I catch the yellow ball with hands.", "t3": "我伸出雙手穩穩接住了爸爸拋來的黃皮球。"
    },
    "throw": {
        "s1": "Throw the ball high.", "t1": "把球高高拋向天空。",
        "s2": "Throw the trash in bin.", "t2": "把吃完的果皮紙屑主動扔進分類垃圾桶。",
        "s3": "Throw the basketball into the high hoop.", "t3": "雙手發力把籃球精準投進高高的籃框中。"
    },
    "listen": {
        "s1": "Listen to the music.", "t1": "聽優美動聽的音樂。",
        "s2": "Listen to the teacher speak.", "t2": "專注認真地聽課堂老師講話講課。",
        "s3": "Listen carefully to the English story audio.", "t3": "專注傾聽耳機裡地道純真的英語繪本音檔。"
    },
    "speak": {
        "s1": "Speak in polite voice.", "t1": "用禮貌清晰的語氣說話。",
        "s2": "Practice to speak English daily.", "t2": "每天堅持張開嘴巴開口大聲練習英文口語。",
        "s3": "We speak English with confidence in class.", "t3": "我們在課堂上充滿自信地用英語大聲交談。"
    },
    "learn": {
        "s1": "Learn ten new words.", "t1": "學習十個全新的生字。",
        "s2": "We learn English every day.", "t2": "我們每一天都充滿好奇地探索學習新知識。",
        "s3": "We learn new English words every day.", "t3": "我們每天開心地跟著Kai學習有用的新單字。"
    },
    "climb": {
        "s1": "Climb up the tree.", "t1": "敏捷攀爬上大樹叉。",
        "s2": "Climb the stairs one step.", "t2": "握好安全扶手一級一級拾級登上樓梯。",
        "s3": "Monkeys climb tall trees in green forest.", "t3": "靈活的小猴子在熱帶森林的高樹間攀爬。"
    },
    "look": {
        "s1": "Look at blue sky.", "t1": "看晴朗遼闊的藍天。",
        "s2": "Look at the stars tonight.", "t2": "在夜深人靜時抬頭望望繁星滿天的星空。",
        "s3": "Look at the colorful rainbow in sky.", "t3": "抬頭仰望大雨過後掛在天邊的七彩美麗彩虹。"
    },
    "see": {
        "s1": "I see a bird.", "t1": "我看見一隻小鳥在飛。",
        "s2": "I see green tall trees.", "t2": "我看見窗外綠油油高大挺拔的常青樹木。",
        "s3": "I see a little bird in tree.", "t3": "我看見一隻五彩斑斕的小鳥在樹枝間蹦跳。"
    },
    "share": {
        "s1": "Share your favorite toys.", "t1": "分享你最心愛的玩具。",
        "s2": "Share delicious snacks with friends.", "t2": "把帶來的小零食和好朋友們一起開心分享。",
        "s3": "We share books and read together happily.", "t3": "我們分享彼此喜歡的繪本坐在地毯上一同閱讀。"
    },
    "pull": {
        "s1": "Pull the wagon along.", "t1": "拉著心愛的小玩具車。",
        "s2": "Pull open the study drawer.", "t2": "輕輕向外拉開書桌第一層裝文具的抽屜。",
        "s3": "Pull the red wagon across the grass.", "t3": "拉著裝滿玩具的小紅拖車穿過綠色草坪。"
    },
    "push": {
        "s1": "Push the swing high.", "t1": "把鞦韆輕輕往前推高。",
        "s2": "Push the door open gently.", "t2": "手掌搭在門板上輕輕將兒童房的門推開。",
        "s3": "Push the study chair under the desk.", "t3": "讀書寫字完畢把學習椅端正推回書桌下方。"
    },
    "kick": {
        "s1": "Kick the soccer ball.", "t1": "一腳踢飛足球射門。",
        "s2": "Kick the ball past goalie.", "t2": "奮力起腳一腳把皮球踢過守門員十指關。",
        "s3": "Kick the soccer ball into the goal.", "t3": "在綠茵操場上一腳將足球精準踢入大球門。"
    },
    "hit": {
        "s1": "Hit the baseball hard.", "t1": "用力擊打棒球出擊。",
        "s2": "Hit the tennis ball back.", "t2": "揮動球拍把飛過網頂的網球大力抽擊回去。",
        "s3": "He hits the baseball with wooden bat.", "t3": "他手握木質球棒準確把投來的棒球擊打出遠處。"
    },
    "pass": {
        "s1": "Pass the ball friend.", "t1": "把球傳給好朋友。",
        "s2": "Pass the salt shaker please.", "t2": "餐桌上請幫忙把調味鹽罐輕輕傳遞過來。",
        "s3": "Pass the basketball to your open teammate.", "t3": "在球場上靈巧把籃球分球傳給有空檔的隊友。"
    },
    "roll": {
        "s1": "Roll the round ball.", "t1": "讓小圓球在地上滾動。",
        "s2": "Roll the ball on grass.", "t2": "讓皮球在柔軟平整的青草地上骨碌碌滾動。",
        "s3": "Roll the ball across the flat floor.", "t3": "輕輕把圓皮球在地板上骨碌碌推向好朋友。"
    },
    "turn": {
        "s1": "Turn the door knob.", "t1": "轉動臥房的門把手。",
        "s2": "Turn the page very gently.", "t2": "小心翼翼地把精裝繪本翻到精彩下一頁。",
        "s3": "Turn left at the busy street corner.", "t3": "走到熱鬧的街角轉彎處記得依指示向左轉。"
    },
    "spin": {
        "s1": "Spin the bright top.", "t1": "轉動發光的小陀螺。",
        "s2": "Spin the top on floor.", "t2": "在地板平整處把彩色陀螺飛速旋轉起來。",
        "s3": "Spin the colorful top on smooth floor.", "t3": "在平整的光滑木地板上轉動起七彩小陀螺。"
    },
    "slide": {
        "s1": "Slide down the slide.", "t1": "從溜滑梯上滑下來。",
        "s2": "Children slide down the playground.", "t2": "小朋友們從高高的旋轉滑梯上歡快滑落。",
        "s3": "We slide down the fun playground slide.", "t3": "我們在公園裡排著隊開心地玩旋轉大滑梯。"
    },
    "swing": {
        "s1": "Swing up very high.", "t1": "盪鞦韆盪得好高好高。",
        "s2": "Swing on the park swing.", "t2": "坐在公園的鞦韆木板上迎著風高高飛起。",
        "s3": "We swing high on the playground swings.", "t3": "我們在遊樂場的鞦韆上迎著微風歡樂盪高。"
    },
    "bounce": {
        "s1": "Bounce the rubber ball.", "t1": "拍打彈力橡膠皮球。",
        "s2": "Bounce on the trampoline safely.", "t2": "在安全跳跳床上腳踩彈簧墊開心地彈跳。",
        "s3": "Bounce the rubber ball on the sidewalk.", "t3": "在平坦的人行道上一下一下拍打著彈力球。"
    },
    "hop": {
        "s1": "Hop like a rabbit.", "t1": "像小兔子一樣跳跳跳。",
        "s2": "Hop on one foot forward.", "t2": "收起一隻腳用單腿蹦蹦跳跳向前邁進步。",
        "s3": "Little green frogs hop across green grass.", "t3": "綠色的小青蛙一蹦一跳穿過綠油油的草地。"
    },
    "bend": {
        "s1": "Bend over touch toes.", "t1": "彎下腰觸摸你的小腳趾。",
        "s2": "Bend knees to jump high.", "t2": "彎曲雙膝做深蹲準備蓄力向上高高躍起。",
        "s3": "Bend your knees before you jump high.", "t3": "起跳前微屈膝蓋蓄滿力量再一躍而起向上跳。"
    },
    "stretch": {
        "s1": "Stretch your arms up.", "t1": "雙手高舉拉伸雙臂。",
        "s2": "Stretch body after waking up.", "t2": "清晨剛醒來在床上做個全身舒展大伸展。",
        "s3": "Stretch your arms high up toward sky.", "t3": "做早操時把雙臂向著藍天高高向上舒展開來。"
    },
    "shake": {
        "s1": "Shake hands say hello.", "t1": "握握雙手親切道好。",
        "s2": "Shake the juice bottle well.", "t2": "喝新鮮果汁之前先把瓶子均勻搖一搖。",
        "s3": "Shake hands warmly and say good morning.", "t3": "親切地和新朋友握握手道一聲早安好久不見。"
    },
    "count": {
        "s1": "Count one two three.", "t1": "數數一二三開始跑。",
        "s2": "Count numbers up to ten.", "t2": "從一認真工整地一路數到數字十。",
        "s3": "Count numbers from one up to ten.", "t3": "大聲地從數字一一口氣數到數字十數得準。"
    },
    "build": {
        "s1": "Build a block tower.", "t1": "用積木搭建高高的小塔。",
        "s2": "Build tall castles with sand.", "t2": "在海灘上用細軟的沙子堆出一座雄偉城堡。",
        "s3": "We build a tall tower with blocks.", "t3": "我們在客廳地毯上用彩色積木搭建高塔。"
    },
    "cut": {
        "s1": "Cut the craft paper.", "t1": "剪開彩色手工紙張。",
        "s2": "Cut paper with safety scissors.", "t2": "用兒童安全圓頭小剪刀剪出可愛圖案。",
        "s3": "Cut paper shapes along the dotted line.", "t3": "沿著紙上的虛線痕跡把可愛圖案剪下來。"
    },
    "fold": {
        "s1": "Fold a paper plane.", "t1": "折一架帥氣的紙飛機。",
        "s2": "Fold clothes into tidy stacks.", "t2": "把洗乾淨曬乾的衣物整整齊齊摺疊碼好。",
        "s3": "Fold a neat paper plane with paper.", "t3": "用乾淨的彩色白紙折出一架飛得遠的紙飛機。"
    },
    "paint": {
        "s1": "Paint a blue sky.", "t1": "畫一片晴朗的藍天。",
        "s2": "Paint rainbow colors on paper.", "t2": "用水彩在潔白畫紙上畫出一道絢麗彩虹。",
        "s3": "I paint a colorful rainbow on paper.", "t3": "我用明亮的水彩在紙上畫出七色彩虹與藍天。"
    },
    "plant": {
        "s1": "Plant a tiny seed.", "t1": "播種下一顆小種子。",
        "s2": "Plant flowers in sunny garden.", "t2": "在陽光充沛的花園苗圃裡種下五彩鮮花。",
        "s3": "We plant flowers in our sunny garden.", "t3": "我們在溫暖的春天在花園裡種下漂亮花草。"
    },
    "dig": {
        "s1": "Dig with toy shovel.", "t1": "用玩具塑膠小鏟子挖沙。",
        "s2": "Dig hole to plant tree.", "t2": "在鬆軟的泥土地上挖個小坑準備種樹。",
        "s3": "Dogs love to dig holes in dirt.", "t3": "活潑的小狗最喜歡在草地泥土裡挖小坑藏骨頭。"
    },
    "feed": {
        "s1": "Feed the pet cat.", "t1": "給心愛的小貓咪餵飯。",
        "s2": "Feed seeds to garden birds.", "t2": "在院子鳥食台上放些穀物種子餵小鳥吃。",
        "s3": "I feed the little goldfish every morning.", "t3": "我每天清晨醒來都給魚缸裡的金魚餵魚飼料。"
    },
    "hold": {
        "s1": "Hold my hand safe.", "t1": "牽好我的手安全走。",
        "s2": "Hold the cup with care.", "t2": "雙手拿穩裝滿熱牛奶的水杯別灑出來。",
        "s3": "Hold hands while crossing the busy street.", "t3": "穿越熱鬧繁忙的馬路時一定要牽緊大人的手。"
    },
    "carry": {
        "s1": "Carry the school bag.", "t1": "背起心愛的小書包。",
        "s2": "Carry grocery bags with care.", "t2": "雙手幫忙拎著從超市買回來的水果蔬菜袋。",
        "s3": "I carry my heavy bag to school.", "t3": "我每天背著裝滿課本講義的書包走去上學。"
    },
    "drop": {
        "s1": "Do not drop cup.", "t1": "拿穩水杯小心別摔破了。",
        "s2": "Leaves drop in autumn breeze.", "t2": "金黃的落葉在瑟瑟秋風中輕輕飄落滿地。",
        "s3": "Do not drop the glass water cup.", "t3": "拿玻璃杯時雙手要拿牢可千萬別失手掉落了。"
    },
    "find": {
        "s1": "Find the hidden star.", "t1": "找出藏在圖畫裡的小星星。",
        "s2": "Find lost keys under couch.", "t2": "在客廳沙發底下找出了不小心掉落的鑰匙。",
        "s3": "We find pretty seashells on the beach.", "t3": "我們在金黃色的沙灘上找到了許多精緻的貝殼。"
    }
}
