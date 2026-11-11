# -*- coding: utf-8 -*-
"""Builder Part 4: Travel (50 words) and Clothes (50 words).
All sentences strictly adhere to:
L1: 3-4 words (Early stage, sight words)
L2: 4-6 words (Everyday routine)
L3: 6-8 words (Progressive challenge, simple child-friendly vocabulary)
"""

PART_4_DATA = {
    # ================= TRAVEL & CITY (50 words) =================
    "car": {
        "s1": "The car drives fast.", "t1": "汽車開得好快。",
        "s2": "Buckle up in the car.", "t2": "上車後繫好安全帶。",
        "s3": "Dad drives our blue family car.", "t3": "爸爸開著我們家藍色的家庭轎車出遊。"
    },
    "bike": {
        "s1": "Ride the red bike.", "t1": "騎那輛紅色的自行車。",
        "s2": "Pedal your bike down street.", "t2": "踩著自行車穿過社區街道。",
        "s3": "I ride my red bike with helmet.", "t3": "我戴好安全帽開心地騎著紅色腳踏車。"
    },
    "train": {
        "s1": "Hear the train chug.", "t1": "聽火車轟隆轟隆前進。",
        "s2": "The bullet train is fast.", "t2": "高鐵列車飛馳速度極快。",
        "s3": "The long train speeds down the tracks.", "t3": "長長的火車在鐵軌上飛快向前奔馳。"
    },
    "plane": {
        "s1": "The plane flies high.", "t1": "飛機在高空中飛翔。",
        "s2": "Jet plane soars above clouds.", "t2": "噴射客機翱翔在白雲之上。",
        "s3": "A white plane flies across the sky.", "t3": "一架白色的大飛機飛越了晴朗的天空。"
    },
    "ship": {
        "s1": "The ship sails far.", "t1": "大輪船航行向遠方。",
        "s2": "Huge cruise ship crosses ocean.", "t2": "巨大的郵輪航行在浩瀚的大洋上。",
        "s3": "A giant cruise ship crosses deep ocean.", "t3": "巨大的白色豪華郵輪航行在藍藍大海上。"
    },
    "boat": {
        "s1": "Row the wooden boat.", "t1": "划這艘小木船。",
        "s2": "Rowboat glides on calm lake.", "t2": "小木舟輕快地滑過平靜的湖面。",
        "s3": "We row a small boat on lake.", "t3": "我們在平靜的小湖上一邊划著小木舟。"
    },
    "road": {
        "s1": "Cross the open road.", "t1": "過馬路前看兩側。",
        "s2": "Cars travel on the road.", "t2": "車輛在平整的道路上來來往往。",
        "s3": "Cars drive along the long mountain road.", "t3": "許多小汽車沿著長長的山間公路行駛。"
    },
    "street": {
        "s1": "Walk down the street.", "t1": "走在熱鬧的街道上。",
        "s2": "Shops line the busy street.", "t2": "繁華的街邊開滿了各式店鋪。",
        "s3": "Children walk along the quiet town street.", "t3": "小朋友們沿著安靜祥和的市鎮街道漫步。"
    },
    "park": {
        "s1": "Play in the park.", "t1": "在公園裡玩耍。",
        "s2": "We play in the park.", "t2": "我們在公園裡玩遊戲。",
        "s3": "We ride our bikes in the park.", "t3": "我們在綠意盎然的大公園裡騎腳踏車。"
    },
    "shop": {
        "s1": "Visit the toy shop.", "t1": "逛逛好玩的玩具店。",
        "s2": "Buy sweet bread at shop.", "t2": "在街角麵包店買剛出爐的甜麵包。",
        "s3": "We buy fresh fruit at the shop.", "t3": "我們在街角的水果小商店買新鮮水果。"
    },
    "city": {
        "s1": "The city is big.", "t1": "這座城市非常大。",
        "s2": "Tall skyscrapers in the city.", "t2": "大都市裡聳立著摩天大樓群。",
        "s3": "Bright lights shine across the night city.", "t3": "璀璨閃爍的燈光照亮了城市的迷人夜景。"
    },
    "bridge": {
        "s1": "Walk over the bridge.", "t1": "走過這座跨河大橋。",
        "s2": "Red bridge spans wide river.", "t2": "紅色的大橋跨越寬闊的大河面。",
        "s3": "Trains cross the long bridge over river.", "t3": "長長的火車穿過橫跨大河的高架鋼橋。"
    },
    "station": {
        "s1": "Wait at the station.", "t1": "在車站月台等車。",
        "s2": "Train arrives at the station.", "t2": "列車緩緩進站停靠在月台邊。",
        "s3": "We wait for train at the station.", "t3": "我們在明亮的車站月台等候列車抵達。"
    },
    "truck": {
        "s1": "The big truck rumbles.", "t1": "大貨車轟隆隆駛過。",
        "s2": "Heavy truck hauls building supplies.", "t2": "大型卡車運載沉重的建築材料。",
        "s3": "A yellow dump truck carries heavy sand.", "t3": "黃色翻斗卡車在工地上運送沉重砂石。"
    },
    "taxi": {
        "s1": "Hail a yellow taxi.", "t1": "招手叫一輛黃色計程車。",
        "s2": "Taxi takes us to airport.", "t2": "計程車載著我們一路前往機場。",
        "s3": "We take a yellow taxi to hotel.", "t3": "我們搭乘一輛黃色計程車直達度假飯店。"
    },
    "zoo": {
        "s1": "Visit the big zoo.", "t1": "去逛逛大動物園。",
        "s2": "We visit the zoo today.", "t2": "我們今天去逛動物園。",
        "s3": "We see funny monkeys at the zoo.", "t3": "我們在動物園裡看頑皮的小猴子跳水。"
    },
    "museum": {
        "s1": "Visit the history museum.", "t1": "參觀歷史文化博物館。",
        "s2": "Dinosaur bones inside the museum.", "t2": "博物館展廳裡陳列著巨大的恐龍化石。",
        "s3": "We see dinosaur bones at the museum.", "t3": "我們在自然博物館看巨大真實的恐龍骨架。"
    },
    "traffic": {
        "s1": "Watch the busy traffic.", "t1": "注意街上繁忙的交通。",
        "s2": "Traffic light turns bright green.", "t2": "路口交通號誌燈變成了綠燈。",
        "s3": "Stop and look before crossing city traffic.", "t3": "在過馬路穿行前停看聽確認交通狀況。"
    },
    "wheel": {
        "s1": "The round wheel turns.", "t1": "圓圓的輪子骨碌轉。",
        "s2": "Four wheels on the wagon.", "t2": "小拖車底下安裝著四個小輪子。",
        "s3": "The wheels on the bus go round.", "t3": "公車上的大車輪咕嚕嚕轉動載我們前行。"
    },
    "airport": {
        "s1": "Arrive at the airport.", "t1": "抵達國際機場航廈。",
        "s2": "Planes take off at airport.", "t2": "飛機在機場跑道上轟鳴起飛升空。",
        "s3": "Planes take off at the international airport.", "t3": "各國的巨大客機在現代化機場跑道起降。"
    },
    "subway": {
        "s1": "Take the clean subway.", "t1": "搭乘乾淨便捷的捷運。",
        "s2": "Subway train travels underground fast.", "t2": "捷運地鐵在地下隧道裡飛速行駛。",
        "s3": "We take the fast subway to school.", "t3": "我們搭乘快捷乾淨的捷運去學校上學。"
    },
    "scooter": {
        "s1": "Ride the kick scooter.", "t1": "滑滑步滑板車。",
        "s2": "Kick your scooter on sidewalk.", "t2": "在人行道上輕快滑動你的小滑板車。",
        "s3": "I ride my kick scooter with helmet.", "t3": "我戴上頭盔在公園人行道滑著小滑板車。"
    },
    "helicopter": {
        "s1": "The helicopter chops loud.", "t1": "直升機旋翼發出轟鳴。",
        "s2": "Helicopter blades spin round fast.", "t2": "直升機的巨大螺旋槳飛速旋轉。",
        "s3": "The rescue helicopter lands on the roof.", "t3": "救援直升機平穩降落在醫院的停機坪上。"
    },
    "rocket": {
        "s1": "The rocket launches high.", "t1": "火箭發射直衝雲霄。",
        "s2": "Space rocket flies to stars.", "t2": "太空火箭點火噴射飛向浩瀚星辰。",
        "s3": "The space rocket flies into deep space.", "t3": "巨大的太空火箭點火騰空飛向浩瀚宇宙。"
    },
    "submarine": {
        "s1": "Submarine dives deep down.", "t1": "潛水艇深深下潛入海。",
        "s2": "Yellow submarine explores the ocean.", "t2": "黃色潛水艇在神祕的海底探險。",
        "s3": "A yellow submarine explores the deep ocean.", "t3": "黃色深海潛水艇在神祕海底悠遊探險。"
    },
    "ticket": {
        "s1": "Show your train ticket.", "t1": "出示你的火車票。",
        "s2": "Scan entry ticket at gate.", "t2": "在驗票閘門前感應掃描車票二維碼。",
        "s3": "Show your train ticket at entry gate.", "t3": "在月台剪票口前出示你手上的火車票。"
    },
    "passport": {
        "s1": "Stamp the travel passport.", "t1": "在出國護照上蓋章。",
        "s2": "Keep your passport very safe.", "t2": "出國旅行時隨身保管好你的護照。",
        "s3": "Keep your blue passport in safe pocket.", "t3": "把出國護照妥善保存在隨身貼身小包裡。"
    },
    "suitcase": {
        "s1": "Pack the rolling suitcase.", "t1": "打包拉桿行李箱。",
        "s2": "Roll your suitcase through airport.", "t2": "在機場大廳推著輪式旅行箱前進。",
        "s3": "We pack clothes into the rolling suitcase.", "t3": "我們把換洗衣物整齊疊放進行李箱中。"
    },
    "hotel": {
        "s1": "Check into the hotel.", "t1": "入住溫馨的渡假飯店。",
        "s2": "Resort hotel has swimming pool.", "t2": "度假飯店院子裡有一個超大泳池。",
        "s3": "We stay at a cozy family hotel.", "t3": "我們在海邊一家溫馨舒適的飯店住下來。"
    },
    "camp": {
        "s1": "Set up summer camp.", "t1": "搭建夏日露營營地。",
        "s2": "Sing around the camp fire.", "t2": "大家圍坐在營火旁歡快地彈唱嬉笑。",
        "s3": "We sing happy songs around camp fire.", "t3": "大家圍坐在溫暖的營火邊開心地齊聲歌唱。"
    },
    "tent": {
        "s1": "Pitch the blue tent.", "t1": "搭起藍色露營帳篷。",
        "s2": "Sleep inside the camping tent.", "t2": "在野外露營帳篷裡鑽進睡袋安歇。",
        "s3": "We sleep inside a warm camping tent.", "t3": "我們躺在野外溫暖防風的露營帳篷裡。"
    },
    "market": {
        "s1": "Visit the morning market.", "t1": "逛逛熱鬧的早市。",
        "s2": "Fresh vegetables at outdoor market.", "t2": "露天農夫市集裡擺滿了新鮮蔬菜瓜果。",
        "s3": "We buy fresh vegetables at morning market.", "t3": "我們在熱鬧的晨間市集採買最新鮮的蔬果。"
    },
    "supermarket": {
        "s1": "Push supermarket shopping cart.", "t1": "推著超市手推車購物。",
        "s2": "Buy groceries at local supermarket.", "t2": "在鄰近的生活大超市採買日用乾貨。",
        "s3": "Mom pushes the cart at local supermarket.", "t3": "媽媽在明亮的大超市裡推著推車選購商品。"
    },
    "bakery": {
        "s1": "Smell warm sweet bakery.", "t1": "聞聞麵包烘焙坊的香氣。",
        "s2": "Buy fresh bread at bakery.", "t2": "在麵包店買出爐香氣撲鼻的法式麵包。",
        "s3": "The bakery smells of warm fresh bread.", "t3": "轉角的麵包坊飄來陣陣剛出爐麵包的甜香。"
    },
    "cinema": {
        "s1": "Watch cartoon at cinema.", "t1": "在電影院看卡通片。",
        "s2": "Cinema screen is huge bright.", "t2": "電影院的大銀幕非常巨大而震撼。",
        "s3": "We watch a fun movie at cinema.", "t3": "我們在電影院裡一邊吃爆米花一邊看電影。"
    },
    "hospital": {
        "s1": "Visit kind hospital doctor.", "t1": "看望親切的醫院醫生。",
        "s2": "Doctors care patients at hospital.", "t2": "白衣天使與醫生在醫院裡細心照顧病人。",
        "s3": "Kind doctors help us at the hospital.", "t3": "親切有愛心的醫生在醫院裡為我們檢查身體。"
    },
    "bank": {
        "s1": "Save money in bank.", "t1": "把零用錢存在銀行。",
        "s2": "Deposit coins into piggy bank.", "t2": "把一枚枚零錢存入自己的小豬儲蓄罐。",
        "s3": "We save our shiny coins in bank.", "t3": "我們把平時攢下的零用錢整齊存入銀行。"
    },
    "farm": {
        "s1": "Visit the sunny farm.", "t1": "參觀陽光明媚的農場。",
        "s2": "Cows graze peacefully on farm.", "t2": "黑白花牛在農場綠油油的牧草地上吃草。",
        "s3": "Horses and cows live on the farm.", "t3": "大馬、乳牛和小綿羊在農場裡快樂生活。"
    },
    "harbor": {
        "s1": "Boats rest in harbor.", "t1": "船隻停泊在港灣裡。",
        "s2": "Fishing boats anchor inside harbor.", "t2": "歸航的捕魚船整齊拋錨在避風港灣裡。",
        "s3": "Sail boats rest quietly in the harbor.", "t3": "色彩繽紛的帆船整齊安靜地停泊在海港。"
    },
    "tunnel": {
        "s1": "Drive through the tunnel.", "t1": "開車穿越隧道。",
        "s2": "Train enters the dark tunnel.", "t2": "長長的列車鳴笛駛入山洞隧道中。",
        "s3": "The train travels through the long tunnel.", "t3": "疾馳的火車呼嘯穿過穿山而過的長隧道。"
    },
    "highway": {
        "s1": "Drive on the highway.", "t1": "行駛在高速公路上。",
        "s2": "Cars cruise along scenic highway.", "t2": "車輛在平坦筆直的公路幹線上勻速巡航。",
        "s3": "Cars travel fast on the wide highway.", "t3": "很多小汽車在寬廣平坦的高速公路上飛馳。"
    },
    "sidewalk": {
        "s1": "Walk on the sidewalk.", "t1": "走在人行道上安全。",
        "s2": "Children walk safely on sidewalk.", "t2": "孩子們在寬敞安全的人行道上邁步。",
        "s3": "Always walk safely on the concrete sidewalk.", "t3": "走在路上時請一定要走在安全的人行道上。"
    },
    "crosswalk": {
        "s1": "Use the marked crosswalk.", "t1": "走斑馬線過馬路。",
        "s2": "Cross street at zebra crosswalk.", "t2": "在黑白斑馬線處遵守號誌過馬路。",
        "s3": "Hold hands and cross at the crosswalk.", "t3": "過馬路時牽好大人的手走在斑馬線上。"
    },
    "corner": {
        "s1": "Turn at the corner.", "t1": "在街角轉彎處轉彎。",
        "s2": "Flower stand at street corner.", "t2": "街角轉彎處有一間芳香四溢的花攤。",
        "s3": "The friendly bakery stands on street corner.", "t3": "那家熱門美味的麵包店就座落在街角轉彎處。"
    },
    "tower": {
        "s1": "Look up at tower.", "t1": "抬頭仰望高塔。",
        "s2": "Climb up the clock tower.", "t2": "拾級而上登上高聳古老的鐘樓頂端。",
        "s3": "The tall clock tower stands in town.", "t3": "高聳的歷史鐘樓巍然矗立在小鎮中心廣場。"
    },
    "castle": {
        "s1": "Explore the stone castle.", "t1": "探索石頭古堡。",
        "s2": "Fairy tale king in castle.", "t2": "童話故事裡的國王和公主住在城堡裡。",
        "s3": "The stone castle sits high on hill.", "t3": "古老的石頭大城堡雄偉地坐落在山丘頂上。"
    },
    "village": {
        "s1": "Visit the quiet village.", "t1": "走訪寧靜的小村莊。",
        "s2": "Cottages dot the peaceful village.", "t2": "溫馨的小木屋星羅棋布點綴在小村落裡。",
        "s3": "Green hills surround the peaceful mountain village.", "t3": "層巒疊翠的青山環抱著寧靜祥和的世外山村。"
    },
    "country": {
        "s1": "Travel to new country.", "t1": "前往新的國家旅行。",
        "s2": "Learn flags of every country.", "t2": "認識世界各個不同國家的美麗國旗。",
        "s3": "We travel to a new country yearly.", "t3": "我們一家人每年都會去一個新的國家旅行。"
    },
    "trip": {
        "s1": "Pack for our trip.", "t1": "為我們的旅行收拾行囊。",
        "s2": "Enjoy the family road trip.", "t2": "盡情享受全家自駕旅行的歡樂時光。",
        "s3": "We go on a fun family trip.", "t3": "我們全家人一起出發展開歡樂的家庭旅行。"
    },
    "drive": {
        "s1": "Dad can drive car.", "t1": "爸爸會開車行駛。",
        "s2": "Drive safely in bad weather.", "t2": "遇到下雨大霧天氣一定要減速安全慢行。",
        "s3": "Dad drives carefully down the mountain road.", "t3": "爸爸手握方向盤小心平穩地在山路行駛。"
    },

    # ================= CLOTHES & ACCESSORIES (50 words) =================
    "hat": {
        "s1": "Wear a sun hat.", "t1": "戴上一頂遮陽草帽。",
        "s2": "Straw hat shades from sun.", "t2": "寬邊草帽為臉龐遮擋炎炎夏日烈陽。",
        "s3": "Wear a sun hat on hot days.", "t3": "大晴天出門在頭上戴上一頂漂亮遮陽帽。"
    },
    "coat": {
        "s1": "Button up your coat.", "t1": "把外套鈕扣扣好。",
        "s2": "Warm wool coat in winter.", "t2": "冬天穿上溫暖防風的羊毛厚大衣。",
        "s3": "Wear a warm coat on cold days.", "t3": "天氣寒冷時出門一定要穿上厚暖的外套。"
    },
    "shoe": {
        "s1": "Tie your shoe lace.", "t1": "繫好運動鞋的鞋帶。",
        "s2": "Put shoes on before outside.", "t2": "在推門出門前穿好自己的外出鞋。",
        "s3": "Put on clean shoes before going out.", "t3": "出門去上學前把乾淨舒適的球鞋穿好。"
    },
    "socks": {
        "s1": "Pull on warm socks.", "t1": "穿上暖和的襪子。",
        "s2": "Striped cotton socks keep warm.", "t2": "條紋純棉襪子讓腳丫保暖舒適不著涼。",
        "s3": "Wear soft cotton socks on your feet.", "t3": "在腳上穿上柔軟吸汗的純棉小襪子。"
    },
    "shirt": {
        "s1": "Button the clean shirt.", "t1": "扣上乾淨的襯衫扣子。",
        "s2": "Iron the white collared shirt.", "t2": "把白色的翻領襯衫燙得平平整整。",
        "s3": "I wear a clean shirt to school.", "t3": "我穿上一件整潔乾淨的白襯衫去上學。"
    },
    "dress": {
        "s1": "Wear the pretty dress.", "t1": "穿上美麗的小洋裝裙。",
        "s2": "Twirl in the floral dress.", "t2": "穿著小碎花洋裝歡快地轉圈起舞。",
        "s3": "She wears a pretty pink dress today.", "t3": "她今天穿了一件漂亮得體的粉紅連衣裙。"
    },
    "jacket": {
        "s1": "Zip up your jacket.", "t1": "拉起夾克外套拉鍊。",
        "s2": "Windbreaker jacket keeps you dry.", "t2": "防風防水的外套保護你在雨霧中乾爽。",
        "s3": "Zip your warm jacket before you leave.", "t3": "出門到戶外前把保暖夾克的拉鍊拉上。"
    },
    "pants": {
        "s1": "Put on long pants.", "t1": "穿上長長的外褲。",
        "s2": "Denim pants fit very well.", "t2": "這條牛仔長褲剪裁合身又耐磨耐穿。",
        "s3": "I wear long pants in cold winter.", "t3": "在寒冷的冬天我會穿上厚實保暖的長褲。"
    },
    "cap": {
        "s1": "Wear a baseball cap.", "t1": "戴上一頂棒球帽。",
        "s2": "Adjust the sporty baseball cap.", "t2": "調節好後扣戴正帥氣的棒球帽。",
        "s3": "Wear a red cap to the park.", "t3": "去公園打球時頭上戴著一頂紅色棒球帽。"
    },
    "boots": {
        "s1": "Wear your rain boots.", "t1": "穿上防水的小雨靴。",
        "s2": "Splash puddle with rubber boots.", "t2": "穿著高筒橡膠雨靴開心地踩踩水坑。",
        "s3": "Wear rubber boots on rainy wet days.", "t3": "下雨天走在泥濘路上記得穿上防水雨靴。"
    },
    "gloves": {
        "s1": "Put on wool gloves.", "t1": "戴上溫暖的羊毛手套。",
        "s2": "Gloves keep your fingers warm.", "t2": "手套保護手指在冰天雪地中不受凍。",
        "s3": "Wear warm gloves in the cold snow.", "t3": "在雪地堆雪人時雙手要戴好厚厚的手套。"
    },
    "scarf": {
        "s1": "Wrap the soft scarf.", "t1": "圍上柔軟舒適的圍巾。",
        "s2": "Knitted scarf keeps neck warm.", "t2": "針織毛線圍巾呵護脖頸免受寒風吹。",
        "s3": "Wrap a red scarf around your neck.", "t3": "在脖子上鬆鬆圍上一條溫暖的紅羊毛圍巾。"
    },
    "belt": {
        "s1": "Buckle your leather belt.", "t1": "扣緊皮帶的腰帶扣。",
        "s2": "Tighten the smart leather belt.", "t2": "將這條精緻的皮帶繫好固定褲腰。",
        "s3": "Buckle the brown belt around your waist.", "t3": "在腰間繫好這條深棕色的牛皮腰帶。"
    },
    "skirt": {
        "s1": "Wear a pleated skirt.", "t1": "穿上一條百褶裙。",
        "s2": "The skirt swishes with dance.", "t2": "裙擺隨著歡快的芭蕾舞步輕輕擺動。",
        "s3": "She wears a blue pleated skirt today.", "t3": "她今天穿著一條漂亮的藍色百褶短裙。"
    },
    "pocket": {
        "s1": "Put keys in pocket.", "t1": "把小鑰匙放進口袋裡。",
        "s2": "Keep treasures in jacket pocket.", "t2": "把撿到的小寶貝小心放進外套口袋中。",
        "s3": "Put the small coin into your pocket.", "t3": "把找零的小硬幣妥善放進衣服口袋裡。"
    },
    "watch": {
        "s1": "Look at your watch.", "t1": "看手腕上的手錶。",
        "s2": "Wrist watch tells exact time.", "t2": "石英腕錶準確走時告訴我們時間。",
        "s3": "Look at your watch to check time.", "t3": "抬起手腕看手錶確認目前幾點幾分。"
    },
    "glasses": {
        "s1": "Wear your reading glasses.", "t1": "戴上清晰的看書眼鏡。",
        "s2": "Glasses help you see clearly.", "t2": "合適度數的眼鏡幫助你看清黑板文字。",
        "s3": "Wear clean glasses to read story books.", "t3": "看書做作業時戴上擦得明亮乾淨的眼鏡。"
    },
    "ring": {
        "s1": "Wear a gold ring.", "t1": "手指上佩戴著金戒指。",
        "s2": "Shiny ring glitters on finger.", "t2": "閃亮戒圈在無名指上散發璀璨光芒。",
        "s3": "A shiny silver ring fits her finger.", "t3": "一枚銀白色閃亮的戒指戴在她纖細手指上。"
    },
    "uniform": {
        "s1": "Wear your neat uniform.", "t1": "穿上整潔乾淨的校服。",
        "s2": "School uniform is blue white.", "t2": "我們的學生校服是清新的藍白配色。",
        "s3": "I wear our school uniform with pride.", "t3": "每天清晨我都自豪地穿上整潔筆挺的校服。"
    },
    "backpack": {
        "s1": "Zip your school backpack.", "t1": "拉上雙肩書包拉鍊。",
        "s2": "Backpack carries books to school.", "t2": "書包裡裝滿了課本講義與鉛筆盒。",
        "s3": "Carry your green backpack on both shoulders.", "t3": "出門時用雙肩平穩背好沉甸甸的綠書包。"
    },
    "sweater": {
        "s1": "Wear a wool sweater.", "t1": "穿上一件羊毛毛衣。",
        "s2": "Knit sweater is soft warm.", "t2": "針織小毛衣貼身穿著柔軟又暖和。",
        "s3": "Wear a warm sweater in autumn wind.", "t3": "秋風起時在身上套一件溫暖軟和的毛衣。"
    },
    "hoodie": {
        "s1": "Pull up hoodie hood.", "t1": "拉起連帽衫的帽子。",
        "s2": "Cozy hoodie has front pouch.", "t2": "舒適的連帽衛衣前面帶有袋鼠暖手袋。",
        "s3": "I wear a blue hoodie to playground.", "t3": "去遊樂場活動時我穿著一件寬鬆的連帽衫。"
    },
    "vest": {
        "s1": "Zip your warm vest.", "t1": "拉上保暖小背心拉鍊。",
        "s2": "Fleece vest keeps chest warm.", "t2": "抓絨背心既保暖軀幹又方便手臂活動。",
        "s3": "Wear a yellow vest for bike safety.", "t3": "騎自行車時套上鮮豔醒目的反光背心安全。"
    },
    "pajamas": {
        "s1": "Put on soft pajamas.", "t1": "換上柔軟的睡衣。",
        "s2": "Put on your soft pajamas.", "t2": "穿上你柔軟舒服的睡衣。",
        "s3": "I change into soft pajamas before bed.", "t3": "睡覺洗澡後換上一身柔軟乾淨的純棉睡衣。"
    },
    "raincoat": {
        "s1": "Wear the yellow raincoat.", "t1": "穿上明亮的黃色雨衣。",
        "s2": "Waterproof raincoat repels rain drops.", "t2": "防水雨衣讓雨水順著光滑表面滑落。",
        "s3": "Wear a yellow raincoat in heavy rain.", "t3": "外面傾盆大雨時出門一定要穿上黃色雨衣。"
    },
    "swimsuit": {
        "s1": "Put on your swimsuit.", "t1": "換上合身舒適的泳裝。",
        "s2": "Wear swimsuit for swimming lesson.", "t2": "穿戴好泳衣泳鏡準備上游泳課。",
        "s3": "Put on your swimsuit for beach fun.", "t3": "換上好看的泳衣泳褲準備在海灘衝浪玩水。"
    },
    "slippers": {
        "s1": "Slip on soft slippers.", "t1": "換上軟綿綿的室內拖鞋。",
        "s2": "Fuzzy slippers warm your feet.", "t2": "毛茸茸的棉拖鞋在冬天溫暖雙腳。",
        "s3": "I wear cozy slippers inside our house.", "t3": "一進家門就脫下皮鞋換上舒服的室內拖鞋。"
    },
    "sandals": {
        "s1": "Wear open toe sandals.", "t1": "穿上透氣的涼鞋。",
        "s2": "Beach sandals are light cool.", "t2": "夏日沙灘涼鞋透氣輕便又好穿。",
        "s3": "We wear open sandals on sunny beach.", "t3": "在向陽的金黃沙灘漫步時我們穿著涼鞋。"
    },
    "sneakers": {
        "s1": "Lace up running sneakers.", "t1": "繫緊跑步運動鞋的鞋帶。",
        "s2": "Cushioned sneakers help you run.", "t2": "避震氣墊慢跑鞋讓跑步更加輕鬆自如。",
        "s3": "Lace up your sneakers for gym class.", "t3": "在上體育課前繫緊彈力跑鞋的雙色鞋帶。"
    },
    "necklace": {
        "s1": "Wear a pearl necklace.", "t1": "戴著一串珍珠項鍊。",
        "s2": "Shiny pendant on gold necklace.", "t2": "金色細項鍊上懸掛著精巧的小墜飾。",
        "s3": "A pretty silver necklace rests on collar.", "t3": "一條精緻的純銀小項鍊垂掛在衣領前。"
    },
    "bracelet": {
        "s1": "Slip on the bracelet.", "t1": "戴上手腕上的手鍊手鐲。",
        "s2": "Beaded friendship bracelet looks colorful.", "t2": "五彩串珠編織的友誼手鍊美麗別緻。",
        "s3": "She wears a beaded bracelet on wrist.", "t3": "她手腕上戴著一串朋友親手編的彩色手鍊。"
    },
    "earrings": {
        "s1": "Wear small silver earrings.", "t1": "戴上一副小巧的銀耳環。",
        "s2": "Sparkling earrings glitter in light.", "t2": "閃爍的耳釘在燈光下映襯耳垂亮晶晶。",
        "s3": "Small flower earrings sparkle in the light.", "t3": "小花形狀的銀耳釘在陽光下閃閃動人。"
    },
    "button": {
        "s1": "Button up your shirt.", "t1": "扣上襯衫的小鈕扣。",
        "s2": "Sew loose button on shirt.", "t2": "媽媽用針線重新縫牢鬆脫的塑膠鈕扣。",
        "s3": "Button up your coat against the wind.", "t3": "起大風時趕快把大衣上的每顆鈕扣扣好。"
    },
    "zipper": {
        "s1": "Zip up metal zipper.", "t1": "拉上金屬拉鍊。",
        "s2": "The smooth zipper closes pouch.", "t2": "順滑的拉鍊輕輕一拉就把收納小包關好。",
        "s3": "Zip the metal zipper of your coat.", "t3": "把外套厚實的防風金屬拉鍊向上拉嚴實。"
    },
    "ribbon": {
        "s1": "Tie a pink ribbon.", "t1": "綁一根粉紅色的絲帶。",
        "s2": "Satin ribbon wraps gift box.", "t2": "光滑的緞帶在禮物盒上打出漂亮蝴蝶結。",
        "s3": "Tie a red ribbon on the gift.", "t3": "在送給朋友的生日禮物盒上繫上紅絲帶。"
    },
    "bow": {
        "s1": "Tie a neat bow.", "t1": "繫一個端正的蝴蝶結。",
        "s2": "Tie a bow on gift.", "t2": "在包裝精美的禮物盒上打個精巧領結。",
        "s3": "Tie a pretty bow on your hair.", "t3": "在扎好的馬尾髮梢上綁一個好看的蝴蝶結。"
    },
    "collar": {
        "s1": "Straighten your shirt collar.", "t1": "翻好並撫平你的襯衫衣領。",
        "s2": "Fold down the polo collar.", "t2": "把Polo衫的翻領整齊摺疊服帖。",
        "s3": "Fold the shirt collar down very neatly.", "t3": "出門穿好西裝前把襯衫衣領翻整齊服貼。"
    },
    "sleeve": {
        "s1": "Roll up long sleeves.", "t1": "挽起長長的衣服袖子。",
        "s2": "Roll sleeves up before wash.", "t2": "洗手洗碗之前先把兩隻袖子高高挽起。",
        "s3": "Roll up your sleeves before you wash.", "t3": "洗臉洗手前挽起袖子防止衣袖濺濕沾水。"
    },
    "apron": {
        "s1": "Tie the cook apron.", "t1": "繫好廚房防油圍裙。",
        "s2": "Wear apron while baking cookies.", "t2": "在廚房烘焙小餅乾時套上防水小圍裙。",
        "s3": "Wear a clean apron while cooking meals.", "t3": "進廚房幫媽媽做飯做點心時戴上小圍裙。"
    },
    "cape": {
        "s1": "Wear a superhero cape.", "t1": "披上帥氣的超級英雄披風。",
        "s2": "Red cape billows in wind.", "t2": "紅色的英雄披風在風中獵獵飄揚展翅。",
        "s3": "A red cape floats in the wind.", "t3": "打扮成小超人時紅紅的披風在背後飄揚。"
    },
    "helmet": {
        "s1": "Strap on safety helmet.", "t1": "扣緊騎車安全頭盔。",
        "s2": "Bicycle helmet protects your head.", "t2": "騎自行車時合格的安全頭盔保護頭部。",
        "s3": "Always wear a helmet while riding bikes.", "t3": "每次騎自行車前一定要把安全頭盔戴好扣緊。"
    },
    "mask": {
        "s1": "Wear clean face mask.", "t1": "戴上乾淨透氣的口罩。",
        "s2": "Cover nose mouth with mask.", "t2": "出入公共場所用口罩將口鼻保護好。",
        "s3": "Wear a mask to protect from dust.", "t3": "在灰塵較大的環境中戴好防塵防護口罩。"
    },
    "umbrella": {
        "s1": "Open your blue umbrella.", "t1": "撐開你遮雨的藍色小傘。",
        "s2": "Raindrops tap on the umbrella.", "t2": "細密的雨滴滴滴答答敲打在傘面上。",
        "s3": "Open your colorful umbrella in the rain.", "t3": "天空下起小雨時撐開你手裡漂亮的小傘。"
    },
    "wallet": {
        "s1": "Keep money in wallet.", "t1": "把紙鈔硬幣整齊放在錢包裡。",
        "s2": "Leather wallet holds money cards.", "t2": "小巧的真皮卡夾安全存放零用錢與卡片。",
        "s3": "Keep your pocket money in the wallet.", "t3": "把自己的零用錢整整齊齊放在小錢包中。"
    },
    "purse": {
        "s1": "Carry cute little purse.", "t1": "拎著小巧可愛的手提包包。",
        "s2": "Small coin purse holds change.", "t2": "可愛的零錢包裡裝著幾枚閃亮的小硬幣。",
        "s3": "Mom carries a small purse to dinner.", "t3": "媽媽出門去參加聚會時拎著一個精美小手包。"
    },
    "tie": {
        "s1": "Wear red silk tie.", "t1": "打上一條紅色的真絲領帶。",
        "s2": "Dad straightens his silk tie.", "t2": "爸爸出門上班前在鏡前整理打正領帶。",
        "s3": "Dad wears a handsome tie to work.", "t3": "爸爸去公司上班時繫著一條帥氣的領帶。"
    },
    "shorts": {
        "s1": "Wear cool denim shorts.", "t1": "穿上清涼透氣的牛仔短褲。",
        "s2": "Wear shorts on sunny days.", "t2": "在晴朗的日子裡穿短褲活動。",
        "s3": "Wear cool shorts on hot summer days.", "t3": "在炎熱的夏天穿著寬鬆透氣的運動短褲。"
    },
    "jeans": {
        "s1": "Pull on blue jeans.", "t1": "穿上經典的藍色牛仔褲。",
        "s2": "Blue denim jeans wear well.", "t2": "這條牛仔長褲耐穿又舒適好看。",
        "s3": "I wear blue jeans on casual weekends.", "t3": "在週末戶外活動時我喜歡穿舒適的牛仔褲。"
    },
    "wool": {
        "s1": "Wool is warm soft.", "t1": "天然羊毛又溫暖又柔軟。",
        "s2": "Sweater made of pure wool.", "t2": "這件毛衣由優質純羊毛細膩紡織而成。",
        "s3": "Pure wool keeps us warm in winter.", "t3": "天然柔軟的羊毛讓我們在嚴冬感到無比溫暖。"
    },
    "cotton": {
        "s1": "Cotton is soft white.", "t1": "棉花潔白又蓬鬆柔軟。",
        "s2": "Pure cotton t-shirt breathes well.", "t2": "純棉T恤吸汗透氣穿在身上格外親膚舒適。",
        "s3": "Soft cotton shirts feel gentle on skin.", "t3": "柔軟透氣的純棉襯衫穿在身上非常舒服。"
    }
}
