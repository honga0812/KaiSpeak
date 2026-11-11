# -*- coding: utf-8 -*-
"""Builder Part 3: Toy/School (50 words) and Daily/Body (50 words).
All sentences strictly adhere to:
L1: 3-4 words (Early stage, sight words)
L2: 4-6 words (Everyday routine)
L3: 6-8 words (Progressive challenge, simple child-friendly vocabulary)
"""

PART_3_DATA = {
    # ================= TOY & SCHOOL (50 words) =================
    "book": {
        "s1": "Read a good book.", "t1": "讀一本好書。",
        "s2": "Open the colorful picture book.", "t2": "翻開這本色彩豐富的繪本。",
        "s3": "I read a funny story book daily.", "t3": "我每天都讀一本有趣的故事書。"
    },
    "pen": {
        "s1": "Write with a pen.", "t1": "用筆寫字。",
        "s2": "Sign your name with pen.", "t2": "用原子筆簽下你的名字。",
        "s3": "I write my name with blue pen.", "t3": "我用藍色的原子筆寫上我的名字。"
    },
    "bag": {
        "s1": "Pack your school bag.", "t1": "收拾你的書包。",
        "s2": "Carry the light yellow bag.", "t2": "背著這只輕便的黃色背包。",
        "s3": "I carry my heavy bag to school.", "t3": "我每天背著書包去學校上學。"
    },
    "ball": {
        "s1": "Kick the red ball.", "t1": "踢那顆紅球。",
        "s2": "Bounce the ball on ground.", "t2": "在草地上拍打反彈皮球。",
        "s3": "We play with a ball after school.", "t3": "放學後我們在操場上一起踢球玩耍。"
    },
    "pencil": {
        "s1": "Sharpen your wooden pencil.", "t1": "削削你的木頭鉛筆。",
        "s2": "Draw a star with pencil.", "t2": "用鉛筆畫一顆漂亮的小星星。",
        "s3": "I draw pictures with my sharp pencil.", "t3": "我用削尖的鉛筆畫出漂亮的圖畫。"
    },
    "paper": {
        "s1": "Fold white craft paper.", "t1": "折白色的手工紙。",
        "s2": "Draw pictures on clean paper.", "t2": "在乾淨的圖畫紙上畫畫。",
        "s3": "We fold paper airplanes with white paper.", "t3": "我們用乾淨的白紙折出帥氣的紙飛機。"
    },
    "ruler": {
        "s1": "Measure with a ruler.", "t1": "用尺量量長度。",
        "s2": "Draw straight lines with ruler.", "t2": "用直尺畫出筆直的線條。",
        "s3": "Use a clear ruler to draw lines.", "t3": "用透明直尺畫出筆直工整的線條。"
    },
    "bus": {
        "s1": "I ride the bus.", "t1": "我搭乘公車。",
        "s2": "The school bus arrives early.", "t2": "黃色校車很早就到了。",
        "s3": "We ride the yellow bus to school.", "t3": "我們搭著黃色的校車一起去上學。"
    },
    "toy": {
        "s1": "Share your favorite toy.", "t1": "分享你最心愛的玩具。",
        "s2": "Put your toys away neatly.", "t2": "把散落的玩具整齊收進箱子。",
        "s3": "We share toys and play with friends.", "t3": "我們和朋友們一起分享好玩的玩具。"
    },
    "school": {
        "s1": "I go to school.", "t1": "我去上學。",
        "s2": "We learn English at school.", "t2": "我們在學校裡開心地學英文。",
        "s3": "I walk to school with my friends.", "t3": "我每天都和好朋友們結伴走去學校。"
    },
    "teacher": {
        "s1": "Listen to the teacher.", "t1": "認真聽老師講課。",
        "s2": "Our teacher smiles very warmly.", "t2": "我們的老師笑得非常溫柔親切。",
        "s3": "Our kind teacher teaches us many songs.", "t3": "我們親切的老師教我們唱許多好聽的歌。"
    },
    "friend": {
        "s1": "Play with a friend.", "t1": "和朋友一起玩耍。",
        "s2": "Friends help each other always.", "t2": "好朋友總是彼此相親相愛互相幫忙。",
        "s3": "I play funny games with my friend.", "t3": "我和好朋友一起玩有趣的益智遊戲。"
    },
    "student": {
        "s1": "I am a student.", "t1": "我是一名學生。",
        "s2": "Good students study hard daily.", "t2": "認真的好學生每天努力學習向上。",
        "s3": "Every good student listens in class carefully.", "t3": "每位好學生在課堂上都認真專心聽講。"
    },
    "eraser": {
        "s1": "Use the soft eraser.", "t1": "用軟軟的橡皮擦。",
        "s2": "Erase pencil marks very cleanly.", "t2": "把鉛筆痕跡擦得乾乾淨淨。",
        "s3": "The soft white eraser cleans pencil marks.", "t3": "白色橡皮擦能把鉛筆筆跡擦得乾乾淨淨。"
    },
    "crayon": {
        "s1": "Draw with a crayon.", "t1": "用蠟筆畫畫。",
        "s2": "Color the sun bright yellow.", "t2": "把大太陽塗上耀眼的金黃色。",
        "s3": "I color the picture with red crayon.", "t3": "我用紅色的蠟筆為圖畫塗上漂亮的顏色。"
    },
    "game": {
        "s1": "Play a fun game.", "t1": "玩個有趣的遊戲。",
        "s2": "We win the board game.", "t2": "我們在桌遊遊戲中贏得勝利。",
        "s3": "We play a fun game after class.", "t3": "下課後我們在教室裡玩好玩的遊戲。"
    },
    "playground": {
        "s1": "Run in the playground.", "t1": "在操場遊樂場奔跑。",
        "s2": "Children laugh on the swings.", "t2": "孩子們在鞦韆上盪得好高好開懷。",
        "s3": "Children play happily on the school playground.", "t3": "小朋友們在學校遊樂場上開心地玩耍。"
    },
    "robot": {
        "s1": "Build a toy robot.", "t1": "組裝一隻玩具機器人。",
        "s2": "The smart robot beeps happily.", "t2": "聰明的機器人發出歡快的嗶嗶聲。",
        "s3": "The toy robot walks across the floor.", "t3": "酷炫的玩具機器人在地板上走來走去。"
    },
    "bell": {
        "s1": "Hear the school bell.", "t1": "聽學校鐘聲響起。",
        "s2": "The recess bell rings now.", "t2": "下課休息的鐘聲現在敲響了。",
        "s3": "The school bell rings at eight morning.", "t3": "學校的鐘聲在清晨八點準時響起。"
    },
    "kite": {
        "s1": "Fly the high kite.", "t1": "放飛高高的風箏。",
        "s2": "Wind lifts the colorful kite.", "t2": "一陣強風將七彩的風箏吹向雲端。",
        "s3": "We fly a colorful kite in spring.", "t3": "我們在溫暖的春天在草地上放風箏。"
    },
    "notebook": {
        "s1": "Open your blue notebook.", "t1": "打開藍色的筆記本。",
        "s2": "Write notes in your notebook.", "t2": "在你的小筆記本上記下重點。",
        "s3": "I write new English words in notebook.", "t3": "我在筆記本裡工整寫下新的英文單字。"
    },
    "scissors": {
        "s1": "Cut with safe scissors.", "t1": "用安全剪刀剪紙。",
        "s2": "Use safety scissors with care.", "t2": "小心握持使用兒童安全剪刀。",
        "s3": "Use safety scissors to cut craft paper.", "t3": "使用圓頭安全剪刀小心地剪裁手工紙。"
    },
    "glue": {
        "s1": "Stick with paper glue.", "t1": "用膠水黏貼好。",
        "s2": "Squeeze sticky glue on paper.", "t2": "把黏黏的膠水擠在色紙邊緣。",
        "s3": "Use sticky glue to paste the pictures.", "t3": "用膠水把剪好的圖片整齊貼在紙上。"
    },
    "tape": {
        "s1": "Pull a clear tape.", "t1": "拉出一截透明膠帶。",
        "s2": "Stick the poster with tape.", "t2": "用透明膠帶把海報平整固定在牆上。",
        "s3": "I fix the ripped book with tape.", "t3": "我用透明膠帶修補破損的故事書。"
    },
    "marker": {
        "s1": "Draw with black marker.", "t1": "用黑色麥克筆畫線。",
        "s2": "Draw bold lines with marker.", "t2": "用彩色麥克筆勾勒出粗獷線條。",
        "s3": "I draw bold lines with colorful marker.", "t3": "我用彩色麥克筆畫出又黑又粗的輪廓線。"
    },
    "paintbrush": {
        "s1": "Dip your soft paintbrush.", "t1": "沾沾柔軟的毛筆水彩筆。",
        "s2": "Paint rainbow with a paintbrush.", "t2": "用水彩筆在圖畫紙上畫一道彩虹。",
        "s3": "Dip the paintbrush in bright blue paint.", "t3": "把水彩畫筆輕輕浸入明亮的藍色顏料中。"
    },
    "chalkboard": {
        "s1": "Look at the chalkboard.", "t1": "看著綠色的黑板。",
        "s2": "Teacher writes on the chalkboard.", "t2": "老師在黑板上工整板書。",
        "s3": "Teacher writes English words on the chalkboard.", "t3": "老師在黑板上工整地寫下英文單字。"
    },
    "classroom": {
        "s1": "Enter our bright classroom.", "t1": "走進我們明亮的教室。",
        "s2": "Keep our classroom very clean.", "t2": "保持我們的教室整潔乾淨又明亮。",
        "s3": "We learn English inside our bright classroom.", "t3": "我們在明亮寬敞的教室裡一起快樂學習。"
    },
    "library": {
        "s1": "Read in quiet library.", "t1": "在安靜的圖書館閱讀。",
        "s2": "Whisper softly inside the library.", "t2": "在圖書館內請輕聲細語別打擾他人。",
        "s3": "We borrow story books from school library.", "t3": "我們在學校圖書館借閱有趣的童話書。"
    },
    "gym": {
        "s1": "Play in the gym.", "t1": "在體育館裡玩耍。",
        "s2": "We run laps in gym.", "t2": "我們在體育館室內跑道上跑步熱身。",
        "s3": "We play fun basketball in school gym.", "t3": "我們在學校體育館裡打好玩的籃球。"
    },
    "locker": {
        "s1": "Open your metal locker.", "t1": "打開你的金屬置物櫃。",
        "s2": "Put your shoes in locker.", "t2": "把書包和外套放進自己的儲物櫃。",
        "s3": "Put your heavy bags in the locker.", "t3": "把沉重的大書包收進自己的置物櫃裡。"
    },
    "map": {
        "s1": "Look at the map.", "t1": "看著這張地圖。",
        "s2": "Find our city on map.", "t2": "在地圖上找出我們居住的城市位置。",
        "s3": "We find Taiwan on the world map.", "t3": "我們在世界地圖上找到了美麗的台灣。"
    },
    "globe": {
        "s1": "Spin the round globe.", "t1": "轉動圓圓的地球儀。",
        "s2": "Find continents on the globe.", "t2": "在地球儀上尋找七大洲與大洋。",
        "s3": "We spin the globe and find oceans.", "t3": "我們轉動地球儀尋找五大洋與各國。"
    },
    "puzzle": {
        "s1": "Fit this puzzle piece.", "t1": "拼上這塊拼圖碎片。",
        "s2": "Solve the jigsaw puzzle together.", "t2": "大家一起合力完成這幅拼圖。",
        "s3": "We put puzzle pieces together on table.", "t3": "我們圍坐在桌子旁一起完成大拼圖。"
    },
    "blocks": {
        "s1": "Build with toy blocks.", "t1": "用積木搭建城堡。",
        "s2": "Play with the toy blocks.", "t2": "開心地玩彩色積木。",
        "s3": "We build a tall tower with blocks.", "t3": "我們用積木搭建起一座高聳的大城堡。"
    },
    "doll": {
        "s1": "Dress the cute doll.", "t1": "給可愛的娃娃穿衣服。",
        "s2": "Brush the doll's curly hair.", "t2": "為心愛的洋娃娃輕輕梳理捲髮。",
        "s3": "The little girl hugs her cute doll.", "t3": "小女孩抱著心愛的洋娃娃安穩睡著了。"
    },
    "teddy": {
        "s1": "Hug the soft teddy.", "t1": "抱抱軟綿綿的泰迪熊。",
        "s2": "Sleep with your teddy bear.", "t2": "抱著泰迪熊玩偶進入甜美夢鄉。",
        "s3": "I sleep with my brown teddy bear.", "t3": "每天晚上我都抱著棕色泰迪熊入睡。"
    },
    "yo-yo": {
        "s1": "Spin the blue yo-yo.", "t1": "甩動這只藍色的溜溜球。",
        "s2": "Trick the yo-yo up down.", "t2": "上下靈巧擺動溜溜球施展花式技藝。",
        "s3": "Kai does fun tricks with his yo-yo.", "t3": "凱用溜溜球做出了好幾個帥氣特技。"
    },
    "drum": {
        "s1": "Beat the loud drum.", "t1": "敲響響亮的小軍鼓。",
        "s2": "Play drums to the beat.", "t2": "隨著音樂節拍咚咚敲響鼓點。",
        "s3": "The little boy plays a loud drum.", "t3": "小男孩敲著鼓發出歡樂熱鬧的節奏聲。"
    },
    "piano": {
        "s1": "Play the black piano.", "t1": "彈奏黑色的鋼琴。",
        "s2": "Practice piano keys every day.", "t2": "每天堅持端坐練習鋼琴黑白琴鍵。",
        "s3": "She plays sweet songs on the piano.", "t3": "她在鋼琴上彈奏出優美動聽的旋律。"
    },
    "guitar": {
        "s1": "Strum the wood guitar.", "t1": "撥動木吉他的琴弦。",
        "s2": "Acoustic guitar sounds so warm.", "t2": "木吉他琴弦流淌出溫暖動人的民謠樂音。",
        "s3": "Dad plays acoustic guitar and sings songs.", "t3": "爸爸彈著木吉他為我們唱好聽的歌。"
    },
    "flute": {
        "s1": "Blow the silver flute.", "t1": "吹奏銀色的長笛。",
        "s2": "The flute plays high notes.", "t2": "長笛吹奏出清脆高亢悠揚的音符。",
        "s3": "The silver flute makes very sweet music.", "t3": "銀色的長笛吹奏出如鳥鳴般甜美的樂音。"
    },
    "whistle": {
        "s1": "Blow the coach whistle.", "t1": "吹響教練哨子。",
        "s2": "The referee blew his whistle.", "t2": "裁判在球場上吹響了尖銳的哨聲。",
        "s3": "The coach blows the whistle for game.", "t3": "教練吹響哨子宣布精彩的比賽開始。"
    },
    "badge": {
        "s1": "Wear a gold badge.", "t1": "佩戴金色的榮譽徽章。",
        "s2": "Pin the star badge proudly.", "t2": "把星星榮譽獎章自豪別在胸前。",
        "s3": "I wear a shiny badge on shirt.", "t3": "我在胸前別上一枚閃亮耀眼的成就徽章。"
    },
    "sticker": {
        "s1": "Peel the star sticker.", "t1": "撕下一張星星貼紙。",
        "s2": "Put good job star sticker.", "t2": "在完成的作業本上貼上小紅花獎勵貼紙。",
        "s3": "Teacher gives me a gold star sticker.", "t3": "老師獎勵我一張亮晶晶的金星星貼紙。"
    },
    "homework": {
        "s1": "Do your daily homework.", "t1": "完成今天的功課作業。",
        "s2": "Finish math homework before dinner.", "t2": "在吃晚餐前把今天的功課全部完成。",
        "s3": "I finish my English homework before dinner.", "t3": "我在晚餐前就完成了今天的英文功課。"
    },
    "question": {
        "s1": "Ask a good question.", "t1": "提出一個好問題。",
        "s2": "Raise hand to ask question.", "t2": "舉起右手向老師禮貌提出疑問。",
        "s3": "Raise your hand to ask a question.", "t3": "有不懂的地方要舉手向老師發問。"
    },
    "answer": {
        "s1": "Know the right answer.", "t1": "知道正確的答案。",
        "s2": "Write answer on test paper.", "t2": "把答案工整填寫在作業答案紙上。",
        "s3": "Kai knows the correct answer in class.", "t3": "凱在課堂上自信地回答出正確答案。"
    },
    "story": {
        "s1": "Read a bedtime story.", "t1": "讀一本睡前故事。",
        "s2": "Grandpa tells a funny story.", "t2": "爺爺給我們講述有趣的民間傳說故事。",
        "s3": "Mom reads a bedtime story to me.", "t3": "媽媽每晚都會給我講一個溫馨睡前故事。"
    },
    "song": {
        "s1": "Sing a happy song.", "t1": "唱一首快樂的歌。",
        "s2": "Learn to sing English song.", "t2": "一起開心地學唱這首動聽的英文童謠。",
        "s3": "We sing a happy song in music class.", "t3": "我們在音樂課上開心地齊唱快樂歌謠。"
    },

    # ================= DAILY & BODY (50 words) =================
    "eye": {
        "s1": "Close your tired eyes.", "t1": "閉上疲憊的雙眼休息。",
        "s2": "My eyes are clear bright.", "t2": "我的眼睛清澈又明亮。",
        "s3": "I see the stars with my eyes.", "t3": "我用雙眼看著天上的星星。"
    },
    "hand": {
        "s1": "Wash your clean hands.", "t1": "把雙手洗乾淨。",
        "s2": "Clap your hands with joy.", "t2": "開心地拍起手來鼓掌。",
        "s3": "Raise your hand to ask a question.", "t3": "舉手提出一個好問題。"
    },
    "face": {
        "s1": "Wash your pretty face.", "t1": "把漂亮的小臉洗乾淨。",
        "s2": "A smile on your face.", "t2": "臉龐洋溢著甜美的微笑。",
        "s3": "The warm sun shines on my face.", "t3": "溫暖的陽光照在我的臉上。"
    },
    "smile": {
        "s1": "Give me a smile.", "t1": "給我一個大大的微笑。",
        "s2": "Smile warmly at your friends.", "t2": "親切地對著好朋友們綻放微笑。",
        "s3": "Kai has a big smile every day.", "t3": "凱每天臉上都帶著大大的微笑。"
    },
    "ear": {
        "s1": "Listen with both ears.", "t1": "用雙耳仔細聆聽。",
        "s2": "Rabbits have long pink ears.", "t2": "小白兔有長長的粉紅耳朵。",
        "s3": "I listen to stories with my ears.", "t3": "我用耳朵聆聽精彩的故事。"
    },
    "nose": {
        "s1": "Touch your cute nose.", "t1": "摸摸你可愛的小鼻子。",
        "s2": "Smell flowers with your nose.", "t2": "用小鼻子聞一聞花朵的香氣。",
        "s3": "I smell the flower with my nose.", "t3": "我用鼻子聞著美麗的花朵。"
    },
    "mouth": {
        "s1": "Open your mouth wide.", "t1": "把嘴巴大大張開。",
        "s2": "Speak English with mouth clearly.", "t2": "開口清晰標準地說出英語。",
        "s3": "Open your mouth to sing a song.", "t3": "張開嘴巴開心地唱一首歌。"
    },
    "foot": {
        "s1": "Stamp your right foot.", "t1": "跺一跺你的右腳。",
        "s2": "Wash your feet very clean.", "t2": "在睡前把雙腳洗得乾乾淨淨。",
        "s3": "I jump on one foot with joy.", "t3": "我開心地用單腳跳來跳去。"
    },
    "head": {
        "s1": "Nod your head yes.", "t1": "點點頭表示同意肯定。",
        "s2": "Wear a hat on head.", "t2": "在頭上戴上一頂遮陽帽。",
        "s3": "Wear a warm hat on your head.", "t3": "在你的頭上戴一頂溫暖的帽子。"
    },
    "arm": {
        "s1": "Raise your right arm.", "t1": "舉起你的右手臂。",
        "s2": "Stretch your arms very wide.", "t2": "向兩側大大伸展你的雙臂。",
        "s3": "Spread your arms and fly like birds.", "t3": "張開雙臂像小鳥一樣自由飛翔。"
    },
    "leg": {
        "s1": "Kick with left leg.", "t1": "用左腿踢踢腿伸展。",
        "s2": "Long legs run very fast.", "t2": "長長的雙腿奔跑得像風一樣快。",
        "s3": "Strong legs help us run and jump.", "t3": "強健有力的雙腿能幫助我們跑跳。"
    },
    "hair": {
        "s1": "Comb your dark hair.", "t1": "把烏黑的頭髮梳整齊。",
        "s2": "Dry your hair with towel.", "t2": "洗完澡後用乾毛巾把頭髮擦乾。",
        "s3": "Mom brushes my soft brown hair gently.", "t3": "媽媽溫柔地為我梳理柔軟的頭髮。"
    },
    "baby": {
        "s1": "The baby is asleep.", "t1": "小嬰兒正甜甜地睡著。",
        "s2": "Baby smiles in the crib.", "t2": "小寶寶在嬰兒床裡甜美微笑。",
        "s3": "The cute baby smiles in her sleep.", "t3": "可愛的小寶寶在睡夢中露出微笑。"
    },
    "heart": {
        "s1": "Feel your heart beat.", "t1": "摸摸胸口感受心跳。",
        "s2": "Heart pumps blood all day.", "t2": "心臟不知疲倦地為全身輸送活力。",
        "s3": "I feel my heart beat after running.", "t3": "跑步過後我能摸到心臟撲通撲通跳。"
    },
    "walk": {
        "s1": "Walk down the path.", "t1": "沿著石子小徑散散步。",
        "s2": "We walk to school together.", "t2": "我們早晨一起步行去學校上學。",
        "s3": "We walk to the green park daily.", "t3": "我們每天都步行到綠色的公園散步。"
    },
    "run": {
        "s1": "Run fast in field.", "t1": "在開闊草地上飛奔。",
        "s2": "Children run across the playground.", "t2": "小朋友們在操場跑道上歡快奔馳。",
        "s3": "We run and play on the field.", "t3": "我們在寬闊的草地上盡情奔跑玩耍。"
    },
    "jump": {
        "s1": "Jump up very high.", "t1": "高高跳起來跳高高。",
        "s2": "Frogs jump in the grass.", "t2": "小青蛙在草叢裡歡快地跳躍。",
        "s3": "We jump rope together on the playground.", "t3": "我們在學校操場上一塊快樂跳繩。"
    },
    "clean": {
        "s1": "Keep your hands clean.", "t1": "保持雙手乾淨整潔。",
        "s2": "Clean up your toy room.", "t2": "把你的玩具房間收拾得整整齊齊。",
        "s3": "Wash with soap to keep hands clean.", "t3": "勤用肥皂洗手讓雙手保持乾淨無菌。"
    },
    "strong": {
        "s1": "Grow big and strong.", "t1": "健康長大變得好強壯。",
        "s2": "Exercise makes your muscles strong.", "t2": "日常鍛鍊讓你的肌肉變得更強壯。",
        "s3": "Drink milk to make your bones strong.", "t3": "多喝牛奶能讓你的骨骼更加強壯堅固。"
    },
    "sleep": {
        "s1": "Time to sleep now.", "t1": "現在是該睡覺的時間囉。",
        "s2": "Sleep eight hours every night.", "t2": "每天夜裡保證八小時高質量睡眠。",
        "s3": "I sleep early to stay healthy always.", "t3": "我早睡早起讓身體隨時保持健康活力。"
    },
    "toe": {
        "s1": "Wiggle your little toes.", "t1": "動一動小腳趾頭。",
        "s2": "Touch your toes with hands.", "t2": "彎下腰用手指輕輕觸摸腳趾。",
        "s3": "Wiggle your ten toes in warm bath.", "t3": "在溫暖的洗澡水裡動動十隻腳趾頭。"
    },
    "finger": {
        "s1": "Count ten small fingers.", "t1": "數數十隻靈巧的小手指。",
        "s2": "I have ten little fingers.", "t2": "我有十隻靈巧的小小手指。",
        "s3": "I have ten fingers to play piano.", "t3": "我有十隻靈巧的手指可以彈鋼琴。"
    },
    "thumb": {
        "s1": "Give a thumbs up.", "t1": "比個大大的讚。",
        "s2": "Thumbs up for good work.", "t2": "為你出色的表現豎起大拇指點讚。",
        "s3": "Give a thumbs up for great effort.", "t3": "為你認真努力的表現豎起大拇指點讚。"
    },
    "nail": {
        "s1": "Clip your finger nail.", "t1": "修剪整齊你的指甲。",
        "s2": "Keep your finger nails clean.", "t2": "保持指甲整潔無污垢。",
        "s3": "Keep your finger nails short and clean.", "t3": "指甲要常常修剪保持短而乾淨。"
    },
    "knee": {
        "s1": "Bend your knees now.", "t1": "現在彎曲膝蓋做深蹲。",
        "s2": "Wear pads on your knees.", "t2": "溜冰時膝蓋上記得戴好護膝保護。",
        "s3": "Bend your knees before you jump high.", "t3": "跳高之前要先稍微彎曲一下膝蓋蓄力。"
    },
    "elbow": {
        "s1": "Bend your left elbow.", "t1": "彎曲你的左手肘關節。",
        "s2": "Rest your elbows on table.", "t2": "手肘輕輕放在平整的書桌面上。",
        "s3": "Rest your elbow on the wooden table.", "t3": "把手肘平穩靠在書桌上看故事書。"
    },
    "shoulder": {
        "s1": "Roll your shoulders back.", "t1": "向後轉轉肩膀放鬆。",
        "s2": "Carry backpack on both shoulders.", "t2": "雙肩背書包能保護脊椎發育平衡。",
        "s3": "Carry the school bag on both shoulders.", "t3": "用雙肩背好書包走路才端正挺拔。"
    },
    "neck": {
        "s1": "Turn your neck gently.", "t1": "輕輕轉動放鬆脖子。",
        "s2": "Giraffes have very long necks.", "t2": "高高的長頸鹿擁有長長的脖子。",
        "s3": "Wrap a warm scarf around your neck.", "t3": "在脖子上圍一條暖呼呼的羊毛圍巾。"
    },
    "back": {
        "s1": "Straighten your back up.", "t1": "坐端正把背挺直。",
        "s2": "Keep your back straight sitting.", "t2": "坐著讀書寫字時記得背部挺直。",
        "s3": "Keep your back straight while reading books.", "t3": "閱讀寫字時背部要挺直保護視力骨骼。"
    },
    "stomach": {
        "s1": "Rub your full stomach.", "t1": "揉揉飽飽的小肚子。",
        "s2": "Healthy food fills my stomach.", "t2": "美味健康的飯菜填飽了小肚子。",
        "s3": "Warm milk settles my hungry stomach well.", "t3": "睡前一杯溫牛奶安撫了咕嚕嚕的肚子。"
    },
    "chest": {
        "s1": "Take breath in chest.", "t1": "深深吸口氣挺起胸膛。",
        "s2": "Cross arms over your chest.", "t2": "把雙臂交叉在胸口做出帥氣動作。",
        "s3": "Take a deep breath into your chest.", "t3": "做做深呼吸讓新鮮空氣充滿胸腔。"
    },
    "cheek": {
        "s1": "Pinch the rosy cheek.", "t1": "輕輕捏捏紅潤的小臉頰。",
        "s2": "Rosy cheeks glow in winter.", "t2": "冬天紅撲撲的臉頰像小蘋果般紅潤。",
        "s3": "Her rosy cheeks glow like red apples.", "t3": "小女孩粉紅色的臉頰像小蘋果一樣可愛。"
    },
    "chin": {
        "s1": "Rest chin on hands.", "t1": "手托著下巴在思考。",
        "s2": "Hold your chin up high.", "t2": "昂起下巴充滿自信與勇敢。",
        "s3": "Hold your chin up high with confidence.", "t3": "自信地抬起下巴迎接嶄新的每一天。"
    },
    "tongue": {
        "s1": "Stick out your tongue.", "t1": "伸伸舌頭做個小鬼臉。",
        "s2": "Taste sweet honey with tongue.", "t2": "用舌尖品嚐香甜金黃的蜂蜜。",
        "s3": "We taste sweet ice cream with tongue.", "t3": "我們用舌頭品嚐冰涼好吃的冰淇淋。"
    },
    "teeth": {
        "s1": "Brush your white teeth.", "t1": "刷刷潔白的牙齒。",
        "s2": "Brush teeth twice a day.", "t2": "每天堅持早晚各刷一次牙。",
        "s3": "Brush teeth morning and night every day.", "t3": "每天早晚刷牙保持牙齒潔白堅固。"
    },
    "lip": {
        "s1": "Moisten your dry lips.", "t1": "潤一潤乾燥的雙唇。",
        "s2": "Put lip balm on lips.", "t2": "在乾裂的嘴唇上塗上保護護唇膏。",
        "s3": "Put soft balm on your dry lips.", "t3": "在乾燥的嘴唇上輕輕抹上天然護唇膏。"
    },
    "voice": {
        "s1": "Speak in clear voice.", "t1": "用清脆響亮的聲音說話。",
        "s2": "Sing in a sweet voice.", "t2": "用甜美清澈的嗓音歡快歌唱。",
        "s3": "Speak in a polite and clear voice.", "t3": "用禮貌清晰又大方的聲音向大家問好。"
    },
    "laugh": {
        "s1": "Laugh out loud together.", "t1": "大家一起開懷大笑。",
        "s2": "Funny jokes make us laugh.", "t2": "好笑的笑話逗得大家哈哈大笑。",
        "s3": "We laugh out loud at funny cartoons.", "t3": "看到有趣的搞笑卡通我們忍不住哈哈大笑。"
    },
    "cry": {
        "s1": "Do not cry now.", "t1": "擦乾眼淚別哭了喔。",
        "s2": "Wipe tears and do not cry.", "t2": "擦擦眼角的淚花勇敢站起來別哭。",
        "s3": "Do not cry and give Mom hugs.", "t3": "擦乾眼淚別哭泣給媽媽一個溫暖擁抱。"
    },
    "hug": {
        "s1": "Give a big hug.", "t1": "給一個大大的擁抱。",
        "s2": "Hug your parents with love.", "t2": "充滿愛意地緊緊擁抱爸爸媽媽。",
        "s3": "Give mom a warm and big hug.", "t3": "每天放學回家都給媽媽一個大大的擁抱。"
    },
    "kiss": {
        "s1": "Blow a sweet kiss.", "t1": "飛吻一個甜甜的吻。",
        "s2": "Mom gives a bedtime kiss.", "t2": "媽媽在睡前給了我一個溫柔的晚安吻。",
        "s3": "Mom gives a good night kiss daily.", "t3": "媽媽每晚睡前都會給我一個溫柔晚安吻。"
    },
    "clap": {
        "s1": "Clap hands to beat.", "t1": "拍拍雙手打出節奏。",
        "s2": "Clap hands for great performance.", "t2": "為台上精彩的表演熱烈鼓掌喝采。",
        "s3": "Clap hands and sing along with music.", "t3": "拍拍雙手跟著音樂節拍開心地大聲合唱。"
    },
    "nod": {
        "s1": "Nod your head yes.", "t1": "點點頭表示贊同明白。",
        "s2": "Nod to say hello politely.", "t2": "禮貌點頭向走過來的鄰居問好。",
        "s3": "Nod your head to say good morning.", "t3": "點點頭禮貌地向老師同學道聲早安。"
    },
    "breath": {
        "s1": "Take deep slow breath.", "t1": "緩緩深吸一口氣。",
        "s2": "Take a breath of air.", "t2": "深吸一口清晨樹林間的新鮮空氣。",
        "s3": "Take a deep breath of fresh air.", "t3": "在花園裡做個深呼吸感受新鮮空氣。"
    },
    "taste": {
        "s1": "Taste sweet red apple.", "t1": "品嚐甜甜的紅蘋果。",
        "s2": "Sweet strawberries taste so delicious.", "t2": "新鮮飽滿的紅草莓品嚐起來好甜。",
        "s3": "Taste the sweet soup with your spoon.", "t3": "用你的小湯匙嚐嚐這碗濃濃甜甜的南瓜湯。"
    },
    "touch": {
        "s1": "Touch the soft puppy.", "t1": "摸摸毛茸茸的小狗。",
        "s2": "Touch the smooth green leaf.", "t2": "伸出手指摸摸光滑翠綠的葉片。",
        "s3": "Touch the soft fur of the puppy.", "t3": "伸出雙手輕輕撫摸小狗柔軟溫順的皮毛。"
    },
    "smell": {
        "s1": "Smell sweet spring flowers.", "t1": "聞聞春天花兒的香氣。",
        "s2": "Fresh bread smells so good.", "t2": "出爐的溫熱麵包聞起來真的好香。",
        "s3": "Smell the sweet flowers in sunny garden.", "t3": "在陽光明媚的花園裡聞著玫瑰淡淡花香。"
    },
    "hear": {
        "s1": "Hear the sweet birds.", "t1": "聽聽小鳥清脆歌唱。",
        "s2": "Listen carefully to hear birds.", "t2": "靜下心來仔細傾聽枝頭鳥兒鳴唱。",
        "s3": "I hear birds singing in the morning.", "t3": "清晨醒來我能聽見小鳥在窗外樹上唱歌。"
    },
    "rest": {
        "s1": "Rest on the bench.", "t1": "坐在長凳上歇歇腳。",
        "s2": "Sit down and rest now.", "t2": "跑累了快坐下來喝口水休息一下。",
        "s3": "Sit under tree to rest a bit.", "t3": "在樹蔭下坐下來喝口水放鬆休息一下。"
    },
    "dream": {
        "s1": "Have a sweet dream.", "t1": "做個香甜的美夢。",
        "s2": "Dream of flying in clouds.", "t2": "在夢中夢見自己像鳥兒在雲端飛翔。",
        "s3": "I dream of flying in the sky.", "t3": "我在香甜的夢裡夢見自己在藍天自由飛翔。"
    }
}
