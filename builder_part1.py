# -*- coding: utf-8 -*-
"""Builder Part 1: Home (50 words) and Food (50 words).
All sentences strictly adhere to:
L1: 3-4 words (Early stage, sight words)
L2: 4-6 words (Everyday routine)
L3: 6-8 words (Progressive challenge, simple child-friendly vocabulary)
"""

PART_1_DATA = {
    # ================= HOME (50 words) =================
    "desk": {
        "s1": "This is my desk.", "t1": "這是我的一張書桌。",
        "s2": "Put the book on the desk.", "t2": "把書本放在書桌上。",
        "s3": "I sit at my desk and study happily.", "t3": "我坐在書桌前開心地學習。"
    },
    "bed": {
        "s1": "My bed is soft.", "t1": "我的小床很柔軟。",
        "s2": "I make my bed every morning.", "t2": "我每天早晨都會整理床鋪。",
        "s3": "I sleep well in my warm bed.", "t3": "我在溫暖的床上睡得很香甜。"
    },
    "cup": {
        "s1": "This is my cup.", "t1": "這是我的一個水杯。",
        "s2": "Hold the cup with both hands.", "t2": "用雙手拿穩水杯。",
        "s3": "I drink warm water from my cup.", "t3": "我用我的水杯喝溫水。"
    },
    "door": {
        "s1": "Please open the door.", "t1": "請把門打開。",
        "s2": "Close the bedroom door softly.", "t2": "請輕輕地關上臥房門。",
        "s3": "Please close the door after you enter.", "t3": "走進來之後請記得把門關上。"
    },
    "clock": {
        "s1": "Look at the clock.", "t1": "看那個時鐘。",
        "s2": "The clock rings at seven.", "t2": "鬧鐘在七點鐘響起。",
        "s3": "The little clock ticks on the wall.", "t3": "小掛鐘在牆上滴答滴答地走著。"
    },
    "box": {
        "s1": "Open the toy box.", "t1": "打開玩具箱。",
        "s2": "Put the toys in the box.", "t2": "把玩具放進盒子裡。",
        "s3": "I keep my favorite toys in this box.", "t3": "我把心愛的玩具收在這個盒子裡。"
    },
    "lamp": {
        "s1": "Turn on the lamp.", "t1": "打開這盞檯燈。",
        "s2": "The desk lamp is bright.", "t2": "這盞書桌檯燈很明亮。",
        "s3": "The yellow lamp makes my room cozy.", "t3": "黃色的小檯燈讓我的房間很溫馨。"
    },
    "chair": {
        "s1": "Sit on the chair.", "t1": "坐在椅子上。",
        "s2": "Push in your study chair.", "t2": "把你的學習椅推進去。",
        "s3": "I sit on the chair to read.", "t3": "我坐在椅子上看故事書。"
    },
    "table": {
        "s1": "Set the dinner table.", "t1": "擺好餐桌。",
        "s2": "Clean the table with a cloth.", "t2": "用抹布把桌子擦乾淨。",
        "s3": "We eat dinner around the big table.", "t3": "我們圍坐在大餐桌旁吃晚餐。"
    },
    "window": {
        "s1": "Look out the window.", "t1": "看向窗外。",
        "s2": "Open the window for fresh air.", "t2": "打開窗戶呼吸新鮮空氣。",
        "s3": "I see birds through the big window.", "t3": "我透過大窗戶看見小鳥在飛。"
    },
    "sofa": {
        "s1": "Sit on the sofa.", "t1": "坐在沙發上。",
        "s2": "The cat sleeps on the sofa.", "t2": "小貓在沙發上睡覺。",
        "s3": "We sit on the sofa watching cartoons.", "t3": "我們坐在沙發上看卡通。"
    },
    "blanket": {
        "s1": "This blanket is warm.", "t1": "這條毛毯很溫暖。",
        "s2": "Fold the blue blanket neatly.", "t2": "把藍色毛毯折整齊。",
        "s3": "I stay warm under my soft blanket.", "t3": "我在柔軟的毛毯下覺得很溫暖。"
    },
    "pillow": {
        "s1": "My pillow is soft.", "t1": "我的枕頭很柔軟。",
        "s2": "Rest your head on the pillow.", "t2": "把頭靠在枕頭上休息。",
        "s3": "I sleep well on this soft pillow.", "t3": "躺在這個軟軟的枕頭上我睡得很好。"
    },
    "mirror": {
        "s1": "Look in the mirror.", "t1": "照照鏡子。",
        "s2": "Smile at yourself in the mirror.", "t2": "對著鏡子裡的自己微笑。",
        "s3": "I comb my hair before the mirror.", "t3": "我在鏡子前面整理梳梳頭髮。"
    },
    "brush": {
        "s1": "Brush your teeth daily.", "t1": "每天都要刷牙。",
        "s2": "I use my green tooth brush.", "t2": "我用我綠色的牙刷。",
        "s3": "Always brush your teeth before you sleep.", "t3": "睡覺之前一定要記得刷刷牙。"
    },
    "key": {
        "s1": "Here is the key.", "t1": "鑰匙在這裡。",
        "s2": "Turn the key in the lock.", "t2": "在鎖孔裡轉動鑰匙。",
        "s3": "The shiny key opens the front door.", "t3": "這把亮晶晶的鑰匙打開了大門。"
    },
    "spoon": {
        "s1": "Hold the soup spoon.", "t1": "拿好湯匙。",
        "s2": "Eat soup with your spoon.", "t2": "用你的湯匙喝湯。",
        "s3": "Use a small spoon to eat yogurt.", "t3": "用小湯匙吃好吃的優格。"
    },
    "fork": {
        "s1": "Pass me the fork.", "t1": "把叉子遞給我。",
        "s2": "Use a fork for the noodles.", "t2": "吃麵時使用叉子。",
        "s3": "I pick up strawberries with my fork.", "t3": "我用叉子叉起甜甜的草莓。"
    },
    "bowl": {
        "s1": "Fill the cereal bowl.", "t1": "裝滿麥片碗。",
        "s2": "Hold the bowl with two hands.", "t2": "用雙手端好碗。",
        "s3": "The blue bowl is full of berries.", "t3": "這個藍色的碗裡裝滿了甜甜的莓果。"
    },
    "towel": {
        "s1": "Dry with a towel.", "t1": "用毛巾擦乾。",
        "s2": "Hang the damp towel up.", "t2": "把微濕的毛巾掛好。",
        "s3": "I wipe my hands with a towel.", "t3": "我用乾淨的毛巾把雙手擦乾。"
    },
    "plate": {
        "s1": "This is a plate.", "t1": "這是一個盤子。",
        "s2": "Put the bread on the plate.", "t2": "把麵包放在盤子上。",
        "s3": "Put two warm pancakes on the plate.", "t3": "在盤子裡放兩片熱騰騰的鬆餅。"
    },
    "knife": {
        "s1": "Use a butter knife.", "t1": "使用一把奶油刀。",
        "s2": "Use the butter knife carefully.", "t2": "小心地使用奶油刀。",
        "s3": "Cut the sweet apple with a knife.", "t3": "用小刀切開甜甜的蘋果。"
    },
    "glass": {
        "s1": "This is a glass.", "t1": "這是一個玻璃杯。",
        "s2": "Hold the glass with care.", "t2": "小心拿好玻璃杯。",
        "s3": "Pour cold juice into the tall glass.", "t3": "把冰涼的果汁倒進高高的玻璃杯裡。"
    },
    "bottle": {
        "s1": "Bring your water bottle.", "t1": "帶上你的水壺。",
        "s2": "The bottle is full of water.", "t2": "水瓶裡裝滿了水。",
        "s3": "I bring my water bottle to school.", "t3": "我每天帶著水壺去學校上學。"
    },
    "pot": {
        "s1": "The pot is hot.", "t1": "這個鍋子很燙。",
        "s2": "Stir the warm vegetable pot.", "t2": "攪拌這鍋溫熱的蔬菜湯。",
        "s3": "Mom cooks soup in the big pot.", "t3": "媽媽在大鍋子裡煮好喝的湯。"
    },
    "pan": {
        "s1": "The pan is hot.", "t1": "平底鍋很熱。",
        "s2": "Cook the egg in the pan.", "t2": "在平底鍋裡煎雞蛋。",
        "s3": "Dad cooks eggs in the frying pan.", "t3": "爸爸在平底鍋裡煎美味的雞蛋。"
    },
    "stove": {
        "s1": "The stove is hot.", "t1": "爐子很燙。",
        "s2": "The stove heats the food.", "t2": "爐子把食物加熱。",
        "s3": "The stove warms our soup for dinner.", "t3": "瓦斯爐為我們的晚餐加熱美味的湯。"
    },
    "fridge": {
        "s1": "Open the fridge door.", "t1": "打開冰箱門。",
        "s2": "Cold milk is in the fridge.", "t2": "冰牛奶在冰箱裡。",
        "s3": "I take fresh milk from the fridge.", "t3": "我從冰箱裡拿出一瓶新鮮牛奶。"
    },
    "sink": {
        "s1": "Wash at the sink.", "t1": "在水槽洗手。",
        "s2": "The sink is shiny and clean.", "t2": "水槽亮晶晶又乾淨。",
        "s3": "Clean water flows into the big sink.", "t3": "乾淨的自來水流進了大水槽裡。"
    },
    "soap": {
        "s1": "Wash with clean soap.", "t1": "用乾淨的肥皂洗手。",
        "s2": "This soap smells like flowers.", "t2": "這塊肥皂聞起來像花香。",
        "s3": "Wash your hands with soap and water.", "t3": "用肥皂和清水把雙手洗得乾乾淨淨。"
    },
    "comb": {
        "s1": "Comb your hair neatly.", "t1": "把頭髮梳整齊。",
        "s2": "The wooden comb is smooth.", "t2": "這把木梳子很光滑。",
        "s3": "I comb my hair neatly every day.", "t3": "我每天都把自己的頭髮梳得很整齊。"
    },
    "toothbrush": {
        "s1": "Pick up your toothbrush.", "t1": "拿起你的牙刷。",
        "s2": "Brush teeth with a toothbrush.", "t2": "用牙刷刷牙。",
        "s3": "I brush my teeth with my toothbrush.", "t3": "我用自己的小牙刷把牙齒刷乾淨。"
    },
    "shampoo": {
        "s1": "Wash hair with shampoo.", "t1": "用洗髮精洗頭髮。",
        "s2": "The shampoo smells very sweet.", "t2": "這罐洗髮精聞起來很香甜。",
        "s3": "The baby shampoo makes lots of bubbles.", "t3": "這款兒童洗髮精搓出好多泡泡。"
    },
    "bathtub": {
        "s1": "The bathtub is full.", "t1": "浴缸裝滿水了。",
        "s2": "A duck is in the bathtub.", "t2": "一隻小鴨在浴缸裡。",
        "s3": "I play with water in the bathtub.", "t3": "我在浴缸裡開心地玩水洗澡。"
    },
    "shower": {
        "s1": "Take a warm shower.", "t1": "洗個溫水澡。",
        "s2": "Water sprays from the shower.", "t2": "蓮蓬頭噴灑出水花。",
        "s3": "A warm shower makes me feel good.", "t3": "洗個溫水澡讓我感覺舒服又清爽。"
    },
    "closet": {
        "s1": "Open the wooden closet.", "t1": "打開木質衣櫃。",
        "s2": "My clothes are in the closet.", "t2": "我的衣服都在衣櫃裡。",
        "s3": "Hang your coats inside the wooden closet.", "t3": "把外套整齊掛進木質衣櫃裡。"
    },
    "drawer": {
        "s1": "Pull open the drawer.", "t1": "拉開抽屜。",
        "s2": "Pencils are inside the drawer.", "t2": "鉛筆在抽屜裡面。",
        "s3": "Keep your pencils inside the desk drawer.", "t3": "把鉛筆整齊收在書桌抽屜裡面。"
    },
    "carpet": {
        "s1": "Sit on the carpet.", "t1": "坐在地毯上。",
        "s2": "The carpet is warm and thick.", "t2": "地毯溫暖又厚實。",
        "s3": "We play fun games on the carpet.", "t3": "我們在地毯上一邊玩有趣的遊戲。"
    },
    "curtain": {
        "s1": "Open the white curtain.", "t1": "拉開白色的窗簾。",
        "s2": "The curtain moves in the wind.", "t2": "窗簾在微風中輕輕擺動。",
        "s3": "The white curtain blows in the wind.", "t3": "白色的窗簾在微風中輕輕飄動。"
    },
    "fan": {
        "s1": "Turn on the fan.", "t1": "打開風扇。",
        "s2": "The fan blows cool air.", "t2": "風扇吹出涼爽的微風。",
        "s3": "The fan keeps our room cool today.", "t3": "電風扇今天讓我們的房間很涼爽。"
    },
    "heater": {
        "s1": "The heater is warm.", "t1": "電暖器很溫暖。",
        "s2": "Sit close to the heater.", "t2": "靠近電暖器坐著。",
        "s3": "We read books near the warm heater.", "t3": "我們在溫暖的電暖器旁看故事書。"
    },
    "floor": {
        "s1": "The floor is clean.", "t1": "地板很乾淨。",
        "s2": "Walk bare on the floor.", "t2": "赤腳走在乾淨的地板上。",
        "s3": "Sunlight shines on the clean wooden floor.", "t3": "陽光灑在乾淨明亮的木地板上。"
    },
    "wall": {
        "s1": "Look at the wall.", "t1": "看著牆壁。",
        "s2": "Touch the smooth wall.", "t2": "摸摸光滑的牆壁。",
        "s3": "We hang pictures on the bedroom wall.", "t3": "我們把漂亮的圖畫掛在臥房牆上。"
    },
    "roof": {
        "s1": "Look at the roof.", "t1": "看著屋頂。",
        "s2": "The red roof keeps us dry.", "t2": "紅色的屋頂保護我們不淋雨。",
        "s3": "Our cozy home has a red roof.", "t3": "我們溫馨的小家有一座紅色的屋頂。"
    },
    "stairs": {
        "s1": "Walk down the stairs.", "t1": "走下樓梯。",
        "s2": "Hold the rail on the stairs.", "t2": "走樓梯時要扶好扶手。",
        "s3": "Walk up the stairs one by one.", "t3": "一步一步踩穩慢慢走上樓梯。"
    },
    "doorbell": {
        "s1": "The doorbell rings clearly.", "t1": "門鈴清脆地響起。",
        "s2": "Press the smart doorbell.", "t2": "按一下門鈴。",
        "s3": "The doorbell rings when our friends come.", "t3": "當朋友來拜訪時門鈴就響起來了。"
    },
    "vase": {
        "s1": "Look at the vase.", "t1": "看著花瓶。",
        "s2": "The glass vase is pretty.", "t2": "這個玻璃花瓶很漂亮。",
        "s3": "Put pretty flowers in the glass vase.", "t3": "把美麗的花朵插在玻璃花瓶裡。"
    },
    "candle": {
        "s1": "Light a birthday candle.", "t1": "點亮生日蠟燭。",
        "s2": "The candle flame glows warm.", "t2": "燭光散發著溫暖的光芒。",
        "s3": "Blow out the candle on your cake.", "t3": "吹熄你生日蛋糕上的小蠟燭吧。"
    },
    "picture": {
        "s1": "This is a picture.", "t1": "這是一張照片。",
        "s2": "Look at the colorful picture.", "t2": "看這幅色彩豐富的圖畫。",
        "s3": "This happy picture shows our loving family.", "t3": "這張溫馨的照片記錄著我們相親相愛的一家人。"
    },
    "broom": {
        "s1": "Use the broom today.", "t1": "今天用掃把打掃。",
        "s2": "The broom cleans the floor.", "t2": "掃把把地板掃得乾乾淨淨。",
        "s3": "Sweep the floor with a wooden broom.", "t3": "拿著輕便的掃把把地板掃乾淨。"
    },

    # ================= FOOD (50 words) =================
    "apple": {
        "s1": "I like red apples.", "t1": "我喜歡紅蘋果。",
        "s2": "An apple a day is good.", "t2": "每天一顆蘋果對身體好。",
        "s3": "Mom slices a sweet red apple.", "t3": "媽媽切開一顆甜甜的紅蘋果。"
    },
    "milk": {
        "s1": "Drink your warm milk.", "t1": "喝掉你的溫牛奶。",
        "s2": "Milk makes your bones strong.", "t2": "牛奶能讓骨骼更強壯。",
        "s3": "I drink fresh milk every morning.", "t3": "我每天早晨喝新鮮牛奶。"
    },
    "water": {
        "s1": "Drink plenty of water.", "t1": "多喝開水。",
        "s2": "Water is clear and cool.", "t2": "水清澈又涼爽。",
        "s3": "Drink clean water every single day.", "t3": "每天都要多喝乾淨的開水。"
    },
    "banana": {
        "s1": "Monkeys love yellow bananas.", "t1": "猴子最愛黃香蕉。",
        "s2": "Peel the sweet banana carefully.", "t2": "小心地剝開甜甜的香蕉。",
        "s3": "A yellow banana gives me good energy.", "t3": "一根黃香蕉能帶給我滿滿活力。"
    },
    "bread": {
        "s1": "I like toasted bread.", "t1": "我喜歡烤吐司麵包。",
        "s2": "Spread butter on the bread.", "t2": "在麵包上抹上奶油。",
        "s3": "Fresh warm bread smells good for breakfast.", "t3": "早餐剛出爐的溫熱麵包聞起來很香。"
    },
    "egg": {
        "s1": "Eat a boiled egg.", "t1": "吃一顆水煮蛋。",
        "s2": "Fry an egg for breakfast.", "t2": "早餐煎一顆荷包蛋。",
        "s3": "A fried egg has a yellow yolk.", "t3": "煎荷包蛋有一個黃澄澄的蛋黃。"
    },
    "juice": {
        "s1": "I want orange juice.", "t1": "我想要喝柳橙汁。",
        "s2": "Juice is sweet and fresh.", "t2": "果汁香甜又新鮮。",
        "s3": "Fresh orange juice tastes sweet and cool.", "t3": "新鮮的柳橙汁喝起來又甜又冰涼。"
    },
    "cake": {
        "s1": "This is birthday cake.", "t1": "這是生日蛋糕。",
        "s2": "Cut a slice of cake.", "t2": "切一塊蛋糕。",
        "s3": "We eat sweet cake on my birthday.", "t3": "我們在我生日那天吃甜甜的蛋糕。"
    },
    "cheese": {
        "s1": "Mice like yellow cheese.", "t1": "老鼠喜歡黃起司。",
        "s2": "Melt cheese on your toast.", "t2": "在吐司上融化起司。",
        "s3": "Melted cheese stretches on the hot pizza.", "t3": "融化的起司在熱熱的披薩上拉長長。"
    },
    "cookie": {
        "s1": "Have a chocolate cookie.", "t1": "吃一片巧克力餅乾。",
        "s2": "Bake sweet cookies with Mom.", "t2": "跟媽媽一起烤甜甜的餅乾。",
        "s3": "These chocolate cookies taste good with milk.", "t3": "這些巧克力餅乾配牛奶非常好吃。"
    },
    "fruit": {
        "s1": "Eat colorful fresh fruit.", "t1": "多吃多彩的新鮮水果。",
        "s2": "Fruit makes your body healthy.", "t2": "水果讓身體更健康。",
        "s3": "We eat fresh fruit after every meal.", "t3": "我們每餐飯後都會吃新鮮的水果。"
    },
    "rice": {
        "s1": "I eat warm rice.", "t1": "我吃溫熱的米飯。",
        "s2": "Cook a bowl of rice.", "t2": "煮一碗熱騰騰的白飯。",
        "s3": "Warm white rice fills my hungry belly.", "t3": "熱騰騰的白米飯填飽了我咕嚕咕嚕的肚子。"
    },
    "meat": {
        "s1": "Eat healthy lean meat.", "t1": "吃健康的瘦肉。",
        "s2": "Cook the meat thoroughly.", "t2": "把肉徹底煮熟。",
        "s3": "Grilled chicken meat tastes tender and good.", "t3": "烤雞肉吃起來鮮嫩又美味。"
    },
    "orange": {
        "s1": "This orange is juicy.", "t1": "這顆柳橙好多汁。",
        "s2": "Peel an orange for me.", "t2": "幫我剝一顆柳橙。",
        "s3": "Sweet juicy oranges are my favorite fruit.", "t3": "香甜多汁的柳丁是我最喜歡的水果。"
    },
    "pizza": {
        "s1": "I love cheese pizza.", "t1": "我最愛起司披薩。",
        "s2": "Share a slice of pizza.", "t2": "分享一塊披薩。",
        "s3": "We eat warm pizza for our dinner.", "t3": "我們晚餐吃熱騰騰美味的披薩。"
    },
    "soup": {
        "s1": "Drink warm vegetable soup.", "t1": "喝溫熱的蔬菜湯。",
        "s2": "The soup smells so good.", "t2": "湯聞起來好香啊。",
        "s3": "Mom cooks hot soup on cold days.", "t3": "媽媽在寒冷的天氣裡煮熱湯。"
    },
    "tea": {
        "s1": "Drink the warm tea.", "t1": "喝這杯溫茶。",
        "s2": "Green tea tastes very fresh.", "t2": "綠茶嚐起來很清新。",
        "s3": "Grandpa drinks a cup of warm tea.", "t3": "爺爺喝著一杯香香溫溫的熱茶。"
    },
    "tomato": {
        "s1": "The tomato is red.", "t1": "番茄是紅色的。",
        "s2": "Slice the red round tomato.", "t2": "把又紅又圓的番茄切片。",
        "s3": "Red tomatoes grow in our sunny garden.", "t3": "紅紅的番茄在向陽的花園裡長大。"
    },
    "sandwich": {
        "s1": "Make a ham sandwich.", "t1": "做個火腿三明治。",
        "s2": "Pack sandwiches for our picnic.", "t2": "為野餐準備三明治。",
        "s3": "I eat a sandwich for my lunch.", "t3": "我午餐吃了一個營養的三明治。"
    },
    "candy": {
        "s1": "I like sweet candy.", "t1": "我喜歡甜甜的糖果。",
        "s2": "Sweet rainbow candy is chewy.", "t2": "彩虹糖又甜又有嚼勁。",
        "s3": "Brush teeth after eating any sweet candy.", "t3": "吃完甜甜的糖果一定要記得刷牙。"
    },
    "potato": {
        "s1": "Bake a sweet potato.", "t1": "烤一顆甜地瓜。",
        "s2": "Mashed potato is creamy soft.", "t2": "馬鈴薯泥濃郁綿密。",
        "s3": "Dad bakes sweet potatoes in the oven.", "t3": "爸爸在烤箱裡烤甜甜的馬鈴薯。"
    },
    "carrot": {
        "s1": "Rabbits eat orange carrots.", "t1": "兔子愛吃胡蘿蔔。",
        "s2": "Crunchy carrots are very healthy.", "t2": "脆脆的胡蘿蔔很健康。",
        "s3": "The white rabbit crunches an orange carrot.", "t3": "小白兔正咬著一根橘色脆胡蘿蔔。"
    },
    "corn": {
        "s1": "Boil sweet yellow corn.", "t1": "煮甜甜的黃玉米。",
        "s2": "Corn on the cob is sweet.", "t2": "整根玉米好香甜。",
        "s3": "We eat sweet corn at the farm.", "t3": "我們在農場裡吃甜甜的煮玉米。"
    },
    "onion": {
        "s1": "Chop the purple onion.", "t1": "切碎紫洋蔥。",
        "s2": "Sweet cooked onions smell nice.", "t2": "炒熟的洋蔥聞起來很香。",
        "s3": "Onions make food taste sweet and delicious.", "t3": "洋蔥讓菜餚吃起來更加鮮甜美味。"
    },
    "cucumber": {
        "s1": "Eat crisp cool cucumber.", "t1": "吃清脆涼爽的小黃瓜。",
        "s2": "Fresh cucumber slices in salad.", "t2": "沙拉裡的脆黃瓜片。",
        "s3": "Green cucumbers are crisp and very cool.", "t3": "綠色的小黃瓜吃起來清脆又涼爽。"
    },
    "mushroom": {
        "s1": "Mushroom grows in woods.", "t1": "蘑菇生長在樹林裡。",
        "s2": "Saute mushrooms with garlic butter.", "t2": "用蒜香奶油炒蘑菇。",
        "s3": "Little brown mushrooms grow under the trees.", "t3": "咖啡色的小蘑菇長在大樹底下。"
    },
    "strawberry": {
        "s1": "Pick a red strawberry.", "t1": "摘一顆紅草莓。",
        "s2": "Sweet strawberry melts in mouth.", "t2": "甜甜的草莓入口即化。",
        "s3": "We pick fresh strawberries on the farm.", "t3": "我們在農場採摘新鮮紅潤的草莓。"
    },
    "grape": {
        "s1": "Eat sweet purple grapes.", "t1": "吃甜甜的紫葡萄。",
        "s2": "Wash purple grapes in water.", "t2": "用水清洗紫葡萄。",
        "s3": "Sweet purple grapes grow on the vines.", "t3": "甜甜的紫葡萄掛在長長的藤架上。"
    },
    "peach": {
        "s1": "The peach is sweet.", "t1": "水蜜桃很香甜。",
        "s2": "Juicy peach skin is soft.", "t2": "多汁的蜜桃表皮柔軟。",
        "s3": "The pink peach is juicy and sweet.", "t3": "粉紅色的水蜜桃多汁又香甜。"
    },
    "lemon": {
        "s1": "Lemon is sour yellow.", "t1": "檸檬是酸酸的黃色。",
        "s2": "Squeeze lemon juice in tea.", "t2": "在茶裡擠入檸檬汁。",
        "s3": "Yellow lemons make cold tea taste fresh.", "t3": "黃色檸檬讓冰茶喝起來格外清爽。"
    },
    "watermelon": {
        "s1": "Watermelon is sweet red.", "t1": "西瓜是甜甜的紅色。",
        "s2": "Eat watermelon on hot days.", "t2": "在大熱天吃西瓜。",
        "s3": "We eat cool watermelon in the summer.", "t3": "我們在炎熱的夏天吃冰涼的大西瓜。"
    },
    "pear": {
        "s1": "The pear is sweet.", "t1": "這顆梨子好甜。",
        "s2": "Bite a crunchy juicy pear.", "t2": "咬一口清脆多汁的梨子。",
        "s3": "The green pear is sweet and crunchy.", "t3": "這顆綠梨子吃起來又脆又多汁。"
    },
    "cherry": {
        "s1": "Eat bright red cherry.", "t1": "吃鮮紅色的櫻桃。",
        "s2": "Pair of cherries on cake.", "t2": "蛋糕上的一對小櫻桃。",
        "s3": "Red cherries make our cake look pretty.", "t3": "紅紅的小櫻桃讓我們的蛋糕變得好漂亮。"
    },
    "mango": {
        "s1": "The mango is sweet.", "t1": "芒果好甜啊。",
        "s2": "Golden mango cubes on shaved ice.", "t2": "刨冰上的黃金芒果丁。",
        "s3": "Sweet golden mango is my favorite treat.", "t3": "香甜的黃金芒果是我最愛的美食。"
    },
    "noodles": {
        "s1": "Slurp long warm noodles.", "t1": "吸溜長長暖暖的麵條。",
        "s2": "Ramen noodles in rich broth.", "t2": "濃郁湯頭裡的拉麵麵條。",
        "s3": "I eat hot noodle soup for dinner.", "t3": "我晚餐吃了一碗熱騰騰的湯麵。"
    },
    "pasta": {
        "s1": "Eat the warm pasta.", "t1": "吃熱騰騰的義大利麵。",
        "s2": "Twirl pasta with your fork.", "t2": "用叉子捲起義大利麵。",
        "s3": "We enjoy tomato pasta with our family.", "t3": "我們全家人一起享用番茄義大利麵。"
    },
    "pancake": {
        "s1": "The pancake is warm.", "t1": "鬆餅很溫暖。",
        "s2": "Drizzle maple syrup on pancakes.", "t2": "在鬆餅上淋上楓糖漿。",
        "s3": "Mom flips warm pancakes for Sunday breakfast.", "t3": "媽媽在週日早餐煎熱騰騰的鬆餅。"
    },
    "toast": {
        "s1": "Toast bread in toaster.", "t1": "在烤麵包機裡烤吐司。",
        "s2": "Golden toast is crispy warm.", "t2": "金黃吐司酥脆溫熱。",
        "s3": "I eat crispy toast with sweet butter.", "t3": "我吃著抹了香甜奶油的酥脆吐司。"
    },
    "butter": {
        "s1": "Spread the yellow butter.", "t1": "抹上黃色的奶油。",
        "s2": "Butter melts on hot bread.", "t2": "奶油在熱麵包上融化。",
        "s3": "Yellow butter melts fast on hot toast.", "t3": "黃色奶油在熱吐司上很快融化了。"
    },
    "honey": {
        "s1": "Honey is sweet gold.", "t1": "蜂蜜是香甜的金色。",
        "s2": "Bees make sweet golden honey.", "t2": "蜜蜂釀造香甜的金黃蜂蜜。",
        "s3": "Drizzle sweet honey over your warm oatmeal.", "t3": "在溫熱的燕麥粥上淋上甜甜的蜂蜜。"
    },
    "jam": {
        "s1": "Spread sweet red jam.", "t1": "抹上甜甜的紅果醬。",
        "s2": "Strawberry jam on warm biscuits.", "t2": "熱比司吉上的草莓果醬。",
        "s3": "I spread strawberry jam on my bread.", "t3": "我在麵包上抹上甜甜的草莓果醬。"
    },
    "peanut": {
        "s1": "Crack the dry peanut.", "t1": "剝開乾花生殼。",
        "s2": "Peanut butter sandwich tastes nutty.", "t2": "花生醬三明治充滿堅果香。",
        "s3": "The squirrel hides peanuts under the tree.", "t3": "小松鼠把花生藏在大樹下面。"
    },
    "salad": {
        "s1": "Toss the green salad.", "t1": "拌拌綠色沙拉。",
        "s2": "Fresh vegetable salad is crisp.", "t2": "新鮮生菜沙拉清脆可口。",
        "s3": "We eat a green salad with dinner.", "t3": "我們晚餐吃了一大碗綠色生菜沙拉。"
    },
    "chicken": {
        "s1": "Eat the roast chicken.", "t1": "吃烤雞肉。",
        "s2": "Golden chicken nuggets taste crispy.", "t2": "金黃雞塊吃起來好酥脆。",
        "s3": "We share delicious roast chicken together happily.", "t3": "我們大家開心地一起分享美味烤雞。"
    },
    "beef": {
        "s1": "Cook the tender beef.", "t1": "煮軟嫩的牛肉。",
        "s2": "Tender beef in the stew.", "t2": "燉鍋裡軟嫩的牛肉塊。",
        "s3": "Dad grills beef patties for our burgers.", "t3": "爸爸為我們的漢堡煎美味的牛肉餅。"
    },
    "pork": {
        "s1": "Cook the lean pork.", "t1": "煮瘦豬肉。",
        "s2": "Grilled pork chops smell delicious.", "t2": "烤豬排聞起來真美味。",
        "s3": "Mom cooks sweet and sour pork tonight.", "t3": "媽媽今晚煮了酸甜好吃的糖醋里肌豬肉。"
    },
    "sausage": {
        "s1": "The sausage is brown.", "t1": "香腸煎成了褐色。",
        "s2": "Sizzling breakfast sausage smells savory.", "t2": "滋滋作響的早餐香腸好香。",
        "s3": "We grill sausages on our camping trip.", "t3": "我們在露營時烤了香噴噴的香腸。"
    },
    "burger": {
        "s1": "Eat a beef burger.", "t1": "吃一個牛肉漢堡。",
        "s2": "This burger tastes very good.", "t2": "這個漢堡吃起來非常好吃。",
        "s3": "I eat a warm cheese burger happily.", "t3": "我開心地吃著熱騰騰的起司漢堡。"
    },
    "popcorn": {
        "s1": "Popcorn pops up high.", "t1": "爆米花高高爆開。",
        "s2": "Movie theater popcorn is buttery.", "t2": "電影院的爆米花充滿奶油香。",
        "s3": "We share sweet popcorn watching our movie.", "t3": "我們一邊看電影一邊吃香甜的爆米花。"
    },
    "chocolate": {
        "s1": "I like dark chocolate.", "t1": "我喜歡黑巧克力。",
        "s2": "A bar of sweet chocolate.", "t2": "一塊甜甜的巧克力磚。",
        "s3": "Hot chocolate warms my hands in winter.", "t3": "熱巧克力在冬天溫暖了我的雙手。"
    }
}
