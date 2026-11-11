# -*- coding: utf-8 -*-
"""Builder Part 2: Animal (50 words) and Nature (50 words).
All sentences strictly adhere to:
L1: 3-4 words (Early stage, sight words)
L2: 4-6 words (Everyday routine)
L3: 6-8 words (Progressive challenge, simple child-friendly vocabulary)
"""

PART_2_DATA = {
    # ================= ANIMAL (50 words) =================
    "cat": {
        "s1": "The cat drinks milk.", "t1": "小貓在喝牛奶。",
        "s2": "My cat purrs softly beside me.", "t2": "我的貓咪在身旁溫柔呼嚕。",
        "s3": "The orange cat sleeps in the sun.", "t3": "橘色小貓在溫暖的陽光下睡覺。"
    },
    "dog": {
        "s1": "The dog can run.", "t1": "小狗會奔跑。",
        "s2": "Walk the dog in the park.", "t2": "在公園裡遛小狗。",
        "s3": "My little dog barks happily at me.", "t3": "我的小狗開心地對著我汪汪叫。"
    },
    "bird": {
        "s1": "I see a bird.", "t1": "我看見一隻小鳥。",
        "s2": "Birds fly high in sky.", "t2": "鳥兒在天空中高高飛翔。",
        "s3": "The little bird sings in the tree.", "t3": "小鳥在樹上唱著好聽的歌。"
    },
    "duck": {
        "s1": "Ducks swim in pond.", "t1": "鴨子在池塘裡游泳。",
        "s2": "The yellow duck says quack.", "t2": "黃色小鴨呱呱叫。",
        "s3": "A yellow duck swims across the pond.", "t3": "一隻黃色小鴨游過了小池塘。"
    },
    "rabbit": {
        "s1": "The rabbit can hop.", "t1": "兔子會跳跳。",
        "s2": "Rabbits like crunchy orange carrots.", "t2": "兔子喜歡吃脆脆的胡蘿蔔。",
        "s3": "The white bunny hops in the garden.", "t3": "小白兔在花園裡開心地跳來跳去。"
    },
    "fish": {
        "s1": "Fish swim in water.", "t1": "魚兒在水裡游動。",
        "s2": "Goldfish has a red tail.", "t2": "金魚有一條紅色的尾巴。",
        "s3": "A gold fish swims in clean water.", "t3": "一條金魚在乾淨的水裡游來游去。"
    },
    "bear": {
        "s1": "The big bear sleeps.", "t1": "大熊在睡覺。",
        "s2": "Bears love sweet golden honey.", "t2": "熊最喜歡香甜的蜂蜜。",
        "s3": "A brown bear catches fish for dinner.", "t3": "棕熊在小溪裡抓魚當作晚餐。"
    },
    "lion": {
        "s1": "The lion roars loud.", "t1": "獅子大聲地吼叫。",
        "s2": "Lion is king of beasts.", "t2": "獅子是萬獸之王。",
        "s3": "The strong lion stands on a rock.", "t3": "強壯的獅子威風地站在岩石上。"
    },
    "tiger": {
        "s1": "The tiger runs fast.", "t1": "老虎跑得非常快。",
        "s2": "Tigers have orange stripes.", "t2": "老虎有橘黑相間的條紋。",
        "s3": "The big tiger walks in the forest.", "t3": "大老虎在茂密的森林裡安靜走動。"
    },
    "monkey": {
        "s1": "The monkey swings high.", "t1": "猴子盪得很高。",
        "s2": "Monkeys are clever and quick.", "t2": "猴子既聰明又敏捷。",
        "s3": "The playful monkey climbs on tall trees.", "t3": "調皮的猴子在高高的樹上爬來爬去。"
    },
    "panda": {
        "s1": "The panda eats bamboo.", "t1": "熊貓正在吃竹子。",
        "s2": "Pandas are black and white.", "t2": "大熊貓是黑白相間的。",
        "s3": "A cute panda eats green bamboo leaves.", "t3": "可愛的大貓熊吃著綠色的竹葉。"
    },
    "elephant": {
        "s1": "The elephant is huge.", "t1": "大象的身形好巨大。",
        "s2": "Elephants have long trunks.", "t2": "大象有長長的象鼻。",
        "s3": "The big elephant drinks water with trunk.", "t3": "大象用牠長長的鼻子吸水喝。"
    },
    "horse": {
        "s1": "The horse runs free.", "t1": "馬兒自由地奔馳。",
        "s2": "Ride a gentle white horse.", "t2": "騎乘溫和的白馬。",
        "s3": "A brown horse runs across the grass.", "t3": "一匹棕色的馬在草地上奔跑。"
    },
    "sheep": {
        "s1": "The sheep has wool.", "t1": "綿羊身上長滿羊毛。",
        "s2": "Count the fluffy white sheep.", "t2": "數數毛茸茸的白羊。",
        "s3": "Fluffy white sheep eat grass on hills.", "t3": "毛茸茸的白羊在小山丘上吃草。"
    },
    "cow": {
        "s1": "The cow gives milk.", "t1": "乳牛為我們產牛奶。",
        "s2": "A dairy cow says moo.", "t2": "乳牛哞哞叫。",
        "s3": "The black and white cow gives milk.", "t3": "黑白相間的乳牛為我們提供牛奶。"
    },
    "pig": {
        "s1": "The pink pig oinks.", "t1": "粉紅小豬發出呼嚕聲。",
        "s2": "Little pigs play in mud.", "t2": "小豬在泥巴裡開心地玩耍。",
        "s3": "The cute pink pig plays with mud.", "t3": "可愛的小粉紅豬在泥巴裡玩耍。"
    },
    "frog": {
        "s1": "Green frog hops high.", "t1": "綠色青蛙跳得很高。",
        "s2": "Frogs catch bugs with tongue.", "t2": "青蛙用長舌頭抓蟲子吃。",
        "s3": "A little green frog jumps into water.", "t3": "一隻綠色小青蛙撲通跳進水裡。"
    },
    "mouse": {
        "s1": "Tiny mouse eats cheese.", "t1": "小老鼠正在吃起司。",
        "s2": "The quiet mouse runs fast.", "t2": "安靜的小老鼠跑得飛快。",
        "s3": "A tiny gray mouse hides behind books.", "t3": "一隻灰色的小老鼠躲在書本後面。"
    },
    "bee": {
        "s1": "The bee buzzes softly.", "t1": "蜜蜂嗡嗡地輕輕叫。",
        "s2": "Busy bees make sweet honey.", "t2": "忙碌的蜜蜂釀造香甜的蜂蜜。",
        "s3": "A yellow bee flies to sweet flowers.", "t3": "黃色的蜜蜂飛向香甜盛開的花朵。"
    },
    "butterfly": {
        "s1": "The butterfly has wings.", "t1": "蝴蝶有美麗的翅膀。",
        "s2": "Colorful butterfly flaps its wings.", "t2": "彩色的蝴蝶輕輕拍打翅膀。",
        "s3": "A colorful butterfly dances in the garden.", "t3": "一隻彩色的蝴蝶在花園裡翩翩起舞。"
    },
    "puppy": {
        "s1": "The puppy can run.", "t1": "小狗會奔跑。",
        "s2": "Playful puppy wags its tail.", "t2": "愛玩的小狗搖著小尾巴。",
        "s3": "The little brown puppy wags its tail.", "t3": "棕色的小狗開心地搖著尾巴迎向我。"
    },
    "kitten": {
        "s1": "Little kitten purrs soft.", "t1": "小貓咪輕輕打呼嚕。",
        "s2": "Fluffy kitten plays with yarn.", "t2": "毛茸茸的小貓玩毛線球。",
        "s3": "The little kitten drinks a bowl milk.", "t3": "小貓咪喝著一小碗溫溫的牛奶。"
    },
    "turtle": {
        "s1": "The turtle walks slow.", "t1": "烏龜慢慢地走。",
        "s2": "The turtle has green shell.", "t2": "烏龜有堅硬的綠色外殼。",
        "s3": "A green turtle walks on warm sand.", "t3": "綠色的小烏龜在溫暖的沙灘上爬行。"
    },
    "dolphin": {
        "s1": "Dolphin jumps very high.", "t1": "海豚跳得非常高。",
        "s2": "Friendly dolphins jump in ocean.", "t2": "親切的海豚在海洋中跳躍。",
        "s3": "Two playful dolphins leap over the waves.", "t3": "兩隻愛玩的海豚躍過了藍藍海浪。"
    },
    "whale": {
        "s1": "The whale swims deep.", "t1": "鯨魚在深海游泳。",
        "s2": "A giant whale breathes water.", "t2": "巨大的鯨魚向空中噴出水花。",
        "s3": "The big blue whale swims in ocean.", "t3": "巨大的藍鯨在廣闊的海洋裡游泳。"
    },
    "shark": {
        "s1": "Shark swims fast ocean.", "t1": "鯊魚在大海游得快。",
        "s2": "Sharks have sharp white teeth.", "t2": "鯊魚有鋒利潔白的牙齒。",
        "s3": "The gray shark swims in deep water.", "t3": "灰色的鯊魚在深深的海水裡游動。"
    },
    "penguin": {
        "s1": "Penguin waddles on ice.", "t1": "企鵝在冰上搖擺走。",
        "s2": "Cute penguins slide on snow.", "t2": "可愛的企鵝在雪地上滑行。",
        "s3": "A funny penguin waddles across the ice.", "t3": "滑稽的小企鵝在冰面上搖搖擺擺走路。"
    },
    "seal": {
        "s1": "The seal claps flippers.", "t1": "海豹拍打著鰭足。",
        "s2": "Spotted seal swims in sea.", "t2": "斑點海豹在冰冷海水中游泳。",
        "s3": "A brown seal rests on the rock.", "t3": "一隻棕色的海豹在岩石上曬太陽休息。"
    },
    "crab": {
        "s1": "Crab walks side ways.", "t1": "螃蟹橫著走路。",
        "s2": "Crabs have two strong pinchers.", "t2": "螃蟹有兩隻強壯的大鉗子。",
        "s3": "A little red crab hides under stones.", "t3": "小紅螃蟹躲進了沙灘上的石頭縫裡。"
    },
    "octopus": {
        "s1": "Octopus has eight arms.", "t1": "章魚有八隻長腕足。",
        "s2": "Clever octopus hides in coral.", "t2": "聰明的章魚隱藏在珊瑚礁間。",
        "s3": "The octopus swims with eight long arms.", "t3": "章魚揮舞著八隻長手臂在海裡游動。"
    },
    "snail": {
        "s1": "The snail moves slow.", "t1": "蝸牛爬得很慢。",
        "s2": "The snail carries spiral shell.", "t2": "蝸牛背著牠螺旋形的小家。",
        "s3": "A little snail crawls on green leaves.", "t3": "小蝸牛在濕潤的綠葉上慢慢爬行。"
    },
    "ant": {
        "s1": "Ant carries bread crumb.", "t1": "小螞蟻搬運麵包屑。",
        "s2": "Busy ants work all together.", "t2": "勤勞的螞蟻們團結合作。",
        "s3": "Tiny black ants work hard every day.", "t3": "小小黑螞蟻每天都非常勤勞地工作。"
    },
    "spider": {
        "s1": "Spider spins a web.", "t1": "蜘蛛正在織網。",
        "s2": "Spiders have eight hairy legs.", "t2": "蜘蛛有八條長長的細腿。",
        "s3": "A small spider spins a silver web.", "t3": "一隻小蜘蛛在樹枝間織出銀色的網。"
    },
    "ladybug": {
        "s1": "Ladybug has black dots.", "t1": "瓢蟲有黑色圓點。",
        "s2": "Red ladybug crawls on leaf.", "t2": "紅色瓢蟲在綠葉上爬行。",
        "s3": "A red ladybug crawls on green grass.", "t3": "紅底黑點的小瓢蟲在綠草地上爬著。"
    },
    "dragonfly": {
        "s1": "Dragonfly has clear wings.", "t1": "蜻蜓有透明的翅膀。",
        "s2": "Blue dragonfly hovers over water.", "t2": "藍色蜻蜓在水面盤旋。",
        "s3": "A shiny dragonfly hovers over the pond.", "t3": "閃亮的蜻蜓在小池塘水面上輕輕盤旋。"
    },
    "deer": {
        "s1": "The deer walks soft.", "t1": "小鹿輕柔地走動。",
        "s2": "Spotted deer eats fresh grass.", "t2": "斑點梅花鹿吃著新鮮嫩草。",
        "s3": "A gentle deer stands in the forest.", "t3": "溫柔的小鹿安靜地站在綠色森林裡。"
    },
    "fox": {
        "s1": "The fox is smart.", "t1": "狐狸很聰明敏捷。",
        "s2": "Red fox has bushy tail.", "t2": "紅狐狸有一條蓬鬆的大尾巴。",
        "s3": "A clever red fox runs through woods.", "t3": "聰明的紅狐狸穿過了安靜的樹林。"
    },
    "wolf": {
        "s1": "The wolf is strong.", "t1": "狼非常強壯英勇。",
        "s2": "The wolf howls at moon.", "t2": "灰狼對著明月長嚎。",
        "s3": "A gray wolf runs across snowy hills.", "t3": "灰色的狼奔跑過覆蓋白雪的山丘。"
    },
    "zebra": {
        "s1": "Zebra has black stripes.", "t1": "斑馬有黑白條紋。",
        "s2": "Zebras run across open plains.", "t2": "斑馬在大草原上奔馳。",
        "s3": "The zebra runs across the green plains.", "t3": "身上有條紋的斑馬奔馳在綠草原上。"
    },
    "giraffe": {
        "s1": "Giraffe has long neck.", "t1": "長頸鹿有長長的脖子。",
        "s2": "Tall giraffes reach tree leaves.", "t2": "高高的長頸鹿夠得到樹葉。",
        "s3": "A tall giraffe eats green tree leaves.", "t3": "高高的長頸鹿吃著樹頂上的綠葉。"
    },
    "kangaroo": {
        "s1": "Kangaroo hops on grass.", "t1": "袋鼠在草地上跳。",
        "s2": "Mother kangaroo carries her joey.", "t2": "袋鼠媽媽育兒袋裡裝著小袋鼠。",
        "s3": "The brown kangaroo hops across the grass.", "t3": "棕色的大袋鼠一蹦一跳躍過草地。"
    },
    "koala": {
        "s1": "The koala sleeps high.", "t1": "無尾熊睡在高處。",
        "s2": "Koalas hug the eucalyptus tree.", "t2": "無尾熊緊緊抱著尤加利樹。",
        "s3": "A gray koala hugs the tree trunk.", "t3": "毛茸茸的無尾熊抱著尤加利樹幹。"
    },
    "camel": {
        "s1": "Camel walks on sand.", "t1": "駱駝在沙地上行走。",
        "s2": "Camels carry humps on back.", "t2": "駱駝背上長著駝峰。",
        "s3": "A camel walks through hot desert sand.", "t3": "高大的駱駝走過炎熱金黃的沙漠。"
    },
    "owl": {
        "s1": "The owl hoots night.", "t1": "貓頭鷹在夜晚啼叫。",
        "s2": "Wise owl sees in dark.", "t2": "聰明的貓頭鷹在黑夜中視力極好。",
        "s3": "The wise owl sits on a branch.", "t3": "聰明的貓頭鷹靜靜坐在大樹枝上。"
    },
    "parrot": {
        "s1": "Parrot can speak words.", "t1": "鸚鵡能開口說話。",
        "s2": "Colorful parrot mimics human words.", "t2": "五彩繽紛的鸚鵡模仿人說話。",
        "s3": "A green parrot repeats our friendly words.", "t3": "綠色的小鸚鵡學著我們說話打招呼。"
    },
    "eagle": {
        "s1": "Eagle flies high sky.", "t1": "老鷹在高空飛翔。",
        "s2": "Eagles soar above the clouds.", "t2": "老鷹在白雲之上翱翔。",
        "s3": "The big eagle flies above tall mountains.", "t3": "威武的大老鷹翱翔在高聳的山峰上。"
    },
    "swan": {
        "s1": "Swan swims on lake.", "t1": "天鵝在湖面上游泳。",
        "s2": "Graceful white swans swim together.", "t2": "優雅的白天鵝結伴悠游。",
        "s3": "A white swan glides across calm water.", "t3": "美麗的白天鵝划過平靜清澈的湖面。"
    },
    "goose": {
        "s1": "The goose honks loud.", "t1": "大白鵝大聲鳴叫。",
        "s2": "Flock of geese fly south.", "t2": "大雁鵝群整齊地向南方飛去。",
        "s3": "A white goose walks along green grass.", "t3": "一隻大白鵝沿著綠綠的草地散步。"
    },
    "rooster": {
        "s1": "Rooster crows at dawn.", "t1": "公雞在清晨啼鳴。",
        "s2": "The rooster wakes farm animals.", "t2": "公雞啼叫喚醒了農場的動物。",
        "s3": "The rooster crows loudly in early morning.", "t3": "大公雞在清晨的大太陽下宏亮啼鳴。"
    },
    "hen": {
        "s1": "Hen sits on eggs.", "t1": "母雞蹲在雞蛋上孵蛋。",
        "s2": "Mother hen protects baby chicks.", "t2": "母雞媽媽保護她的小雞群。",
        "s3": "The brown hen lays eggs in nest.", "t3": "棕色的母雞在稻草窩裡下了新鮮的蛋。"
    },

    # ================= NATURE (50 words) =================
    "sun": {
        "s1": "The sun is bright.", "t1": "太陽非常明亮。",
        "s2": "Morning sun warms the earth.", "t2": "晨光溫暖了整片大地。",
        "s3": "The warm sun rises in the morning.", "t3": "溫暖的太陽在清晨緩緩升起。"
    },
    "moon": {
        "s1": "The moon is round.", "t1": "月亮又大又圓。",
        "s2": "The moon shines at night.", "t2": "月光在黑夜中灑下光輝。",
        "s3": "A silver moon shines in night sky.", "t3": "銀色的月亮在漆黑的夜空中照亮大地。"
    },
    "star": {
        "s1": "Look at the star.", "t1": "看看那顆星星。",
        "s2": "Little stars twinkle at night.", "t2": "小星星在夜晚一閃一閃眨著眼。",
        "s3": "Bright stars twinkle in dark night sky.", "t3": "明亮的星星在夜空中眨著發光的小眼睛。"
    },
    "tree": {
        "s1": "The tree is tall.", "t1": "大樹長得好高。",
        "s2": "Birds build nests in tree.", "t2": "鳥兒在大樹上築起了舒適的小巢。",
        "s3": "A green tree grows in the park.", "t3": "一棵翠綠茂盛的大樹生長在公園裡。"
    },
    "rain": {
        "s1": "I like the rain.", "t1": "我喜歡下雨天。",
        "s2": "Rain falls on green leaves.", "t2": "雨點輕輕打在綠葉上。",
        "s3": "Gentle rain falls from the gray clouds.", "t3": "綿綿細雨從灰灰的雲層中落下來。"
    },
    "flower": {
        "s1": "Smell the sweet flower.", "t1": "聞聞甜甜的花香。",
        "s2": "The pink flower blooms today.", "t2": "粉紅色的花兒今天盛開了。",
        "s3": "A pink flower blooms in warm spring.", "t3": "粉紅色的花朵在溫暖的春天盛開。"
    },
    "grass": {
        "s1": "The grass is green.", "t1": "小草是綠色的。",
        "s2": "Walk barefoot on soft grass.", "t2": "赤腳漫步在柔軟的草皮上。",
        "s3": "Green grass grows after the spring rain.", "t3": "綠色的小草在春雨過後紛紛冒了出來。"
    },
    "wind": {
        "s1": "The wind blows cool.", "t1": "微風吹拂好涼爽。",
        "s2": "Cool wind shakes the trees.", "t2": "涼風吹動了滿樹的枝葉。",
        "s3": "A cool wind blows through the trees.", "t3": "涼爽的微風輕輕吹過了樹梢林間。"
    },
    "cloud": {
        "s1": "See the white cloud.", "t1": "看那朵白雲。",
        "s2": "White clouds float in sky.", "t2": "朵朵白雲在藍天中隨風飄蕩。",
        "s3": "Fluffy white clouds float in blue sky.", "t3": "蓬鬆柔軟的白雲飄浮在藍天之中。"
    },
    "snow": {
        "s1": "The snow is cold.", "t1": "雪白茫茫好冰冷。",
        "s2": "We make snowmen in snow.", "t2": "我們在雪地裡一起堆可愛雪人。",
        "s3": "White snow falls softly from the sky.", "t3": "潔白的雪花從天空中輕輕飄落。"
    },
    "river": {
        "s1": "The river flows down.", "t1": "河水向下流動。",
        "s2": "Clear river water flows fast.", "t2": "清澈的河水奔流向遠方。",
        "s3": "The clear river flows past the green hills.", "t3": "清澈的小河流經綠油油的山腳下。"
    },
    "sea": {
        "s1": "The sea is blue.", "t1": "大海是湛藍的。",
        "s2": "Ships sail across wide sea.", "t2": "輪船航行在寬闊的大海上。",
        "s3": "Blue sea waves splash on the beach.", "t3": "藍藍的海浪嘩啦嘩啦拍打在沙灘上。"
    },
    "sky": {
        "s1": "The sky is blue.", "t1": "天空是藍色的。",
        "s2": "Look up at blue sky.", "t2": "抬頭仰望蔚藍的天空。",
        "s3": "White birds fly across the blue sky.", "t3": "白色的小鳥自由飛翔在晴朗的藍天。"
    },
    "hill": {
        "s1": "Climb up the hill.", "t1": "爬上小山丘。",
        "s2": "Green grass covers the hill.", "t2": "綠草覆蓋著起伏的小山坡。",
        "s3": "We run up the sunny green hill.", "t3": "我們一口氣跑上了陽光明媚的綠山丘。"
    },
    "stone": {
        "s1": "Skip the flat stone.", "t1": "打水漂扔小扁石。",
        "s2": "The smooth stone is round.", "t2": "這顆光滑的石頭圓圓的。",
        "s3": "I find a shiny stone by river.", "t3": "我在河邊撿到了一顆閃亮光滑的鵝卵石。"
    },
    "leaf": {
        "s1": "The leaf is green.", "t1": "樹葉是翠綠色的。",
        "s2": "Autumn leaves turn bright gold.", "t2": "秋天的樹葉變成了明亮的金黃色。",
        "s3": "A yellow leaf falls from the tree.", "t3": "一片金黃色的樹葉從樹枝上飄落下來。"
    },
    "garden": {
        "s1": "Water the flower garden.", "t1": "給花園澆澆水。",
        "s2": "Sweet roses bloom in garden.", "t2": "芬芳的玫瑰花在花園裡綻放。",
        "s3": "Colorful flowers bloom in our sunny garden.", "t3": "繽紛五彩的花朵在我們向陽的花園裡綻放。"
    },
    "rainbow": {
        "s1": "See the colorful rainbow.", "t1": "看那道七彩斑斕的彩虹。",
        "s2": "A rainbow follows summer rain.", "t2": "夏日陣雨過後天空出現了彩虹。",
        "s3": "A colorful rainbow appears after the rain.", "t3": "大雨過後一道七彩的彩虹掛在天空。"
    },
    "forest": {
        "s1": "Walk in the forest.", "t1": "漫步在森林裡。",
        "s2": "Tall green trees make forest.", "t2": "高聳綠樹組成了茂密的森林。",
        "s3": "Animals live happily in the green forest.", "t3": "各種小動物在綠意盎然的大森林裡快樂生活。"
    },
    "beach": {
        "s1": "Play on the beach.", "t1": "在沙灘上玩耍。",
        "s2": "We build sandcastles on beach.", "t2": "我們在海灘上堆起了大沙堡。",
        "s3": "We collect pretty seashells on the beach.", "t3": "我們在金黃色的沙灘上拾撿漂亮的貝殼。"
    },
    "ocean": {
        "s1": "The ocean is deep.", "t1": "海洋深邃又蔚藍。",
        "s2": "Whales swim across deep ocean.", "t2": "鯨魚在深邃浩瀚的大洋中游動。",
        "s3": "Whales and dolphins live in deep ocean.", "t3": "巨大的鯨魚與可愛海豚生活在深海裡。"
    },
    "lake": {
        "s1": "The lake is calm.", "t1": "湖水非常平靜。",
        "s2": "Boats row on calm lake.", "t2": "小船在平靜的湖面上輕輕划行。",
        "s3": "White ducks swim across the calm lake.", "t3": "白色的小水鴨悠閒游過平靜清澈的湖面。"
    },
    "pond": {
        "s1": "Fish swim in pond.", "t1": "魚兒在池塘裡游泳。",
        "s2": "Frogs leap across lily pond.", "t2": "小青蛙跳過開滿睡蓮的小池塘。",
        "s3": "Little green frogs jump into the pond.", "t3": "綠色的小青蛙開心地跳進了小池塘裡。"
    },
    "stream": {
        "s1": "The stream is clear.", "t1": "小溪清澈見底。",
        "s2": "Cold stream splashes over pebbles.", "t2": "清涼的溪水潑灑過圓潤的鵝卵石。",
        "s3": "Cool water flows down the little stream.", "t3": "清涼甘甜的水從小溪裡緩緩流淌下來。"
    },
    "mountain": {
        "s1": "The mountain is high.", "t1": "大山聳立好高。",
        "s2": "Snow covers the high mountain.", "t2": "白雪覆蓋著高聳的山頭頂峰。",
        "s3": "Snow covers the peak of the mountain.", "t3": "潔白的雪花覆蓋著高山雄偉的山頂。"
    },
    "valley": {
        "s1": "Walk down the valley.", "t1": "走下山谷。",
        "s2": "Wildflowers grow across the valley.", "t2": "野花開滿了整片深谷草原。",
        "s3": "A green valley rests between two mountains.", "t3": "兩座大山之間夾著一片翠綠美麗的山谷。"
    },
    "cave": {
        "s1": "Explore the stone cave.", "t1": "探索石頭山洞。",
        "s2": "Bears sleep inside dark cave.", "t2": "大熊在幽暗溫暖的岩洞裡冬眠。",
        "s3": "Bats sleep upside down in the cave.", "t3": "黑黑的蝙蝠倒掛在岩洞裡面安靜睡覺。"
    },
    "island": {
        "s1": "Visit the green island.", "t1": "拜訪綠色的小島。",
        "s2": "Palm trees on tropical island.", "t2": "熱帶島嶼上搖曳的棕櫚樹。",
        "s3": "We sail a boat to the island.", "t3": "我們駕著小船航向那座美麗的綠色島嶼。"
    },
    "rock": {
        "s1": "Sit on the rock.", "t1": "坐在岩石上休息。",
        "s2": "Climb over the big rock.", "t2": "攀爬過巨大堅硬的岩石。",
        "s3": "We sit on a rock and rest.", "t3": "我們坐在一塊平坦的大岩石上休息片刻。"
    },
    "sand": {
        "s1": "Walk on warm sand.", "t1": "走在溫暖的沙灘上。",
        "s2": "Soft golden sand on feet.", "t2": "腳丫踏在柔軟的金黃細沙上。",
        "s3": "We build a tall castle with sand.", "t3": "我們用金黃色的沙子堆了一座大城堡。"
    },
    "soil": {
        "s1": "Plant seed in soil.", "t1": "把種子種在泥土裡。",
        "s2": "Earthworms wiggle in rich soil.", "t2": "蚯蚓在肥沃濕潤的泥土裡鑽洞。",
        "s3": "We put fresh soil in plant pots.", "t3": "我們把營養的新鮮土壤倒進小花盆裡。"
    },
    "mud": {
        "s1": "Puddle of wet mud.", "t1": "一窪濕漉漉的泥水坑。",
        "s2": "Rain turns dirt into mud.", "t2": "雨水把泥土變成了軟軟的泥巴。",
        "s3": "Pigs love to roll in cool mud.", "t3": "可愛的小豬最喜歡在涼爽的泥巴裡打滾。"
    },
    "seed": {
        "s1": "Plant a tiny seed.", "t1": "種下一顆小種子。",
        "s2": "Seeds sprout into green plants.", "t2": "種子萌芽成長為翠綠小植物。",
        "s3": "Water the little seed every single day.", "t3": "每天都要給這顆小種子澆澆水。"
    },
    "root": {
        "s1": "Tree root grows deep.", "t1": "樹根深深紮根地底。",
        "s2": "Roots drink water from ground.", "t2": "植物的根系從地底吸收養分。",
        "s3": "The tree roots grow deep in ground.", "t3": "大樹的根深深地扎進溫暖的泥土裡。"
    },
    "branch": {
        "s1": "Birds sit on branch.", "t1": "鳥兒停歇在樹枝上。",
        "s2": "Green leaves on the branch.", "t2": "長長的樹枝上長滿了嫩綠樹葉。",
        "s3": "Two little birds sing on the branch.", "t3": "兩隻可愛的小鳥站在樹枝上開心地唱歌。"
    },
    "bark": {
        "s1": "Touch the tree bark.", "t1": "摸摸粗糙的樹皮。",
        "s2": "Tree bark protects the wood.", "t2": "樹皮保護著裡面的木質生長。",
        "s3": "The brown tree bark feels very rough.", "t3": "深棕色的樹皮摸起來粗糙又堅韌。"
    },
    "wood": {
        "s1": "Craft toy from wood.", "t1": "用木頭製作小玩具。",
        "s2": "Fireplace burns dry pine wood.", "t2": "壁爐裡燃燒著乾燥芬芳的松木。",
        "s3": "We make a small boat from wood.", "t3": "我們用乾淨的木頭做了一隻精緻小木船。"
    },
    "pine": {
        "s1": "Pine tree is green.", "t1": "松樹常年翠綠挺拔。",
        "s2": "Pine trees smell fresh outdoors.", "t2": "松樹在戶外散發清新森林香氣。",
        "s3": "Green pine trees stand in cold winter.", "t3": "綠綠的松樹在寒冷的冬天依然挺拔。"
    },
    "bamboo": {
        "s1": "Bamboo grows so tall.", "t1": "竹子長得好高好挺。",
        "s2": "Pandas chew fresh bamboo shoots.", "t2": "大熊貓嚼著鮮嫩多汁的竹筍。",
        "s3": "Green bamboo grows tall in the forest.", "t3": "翠綠挺拔的竹子在森林裡長得非常高。"
    },
    "rose": {
        "s1": "The rose smells sweet.", "t1": "玫瑰花散發芳香。",
        "s2": "Red rose blooms with thorns.", "t2": "帶刺的紅玫瑰綻放嬌豔花瓣。",
        "s3": "A pretty red rose blooms in garden.", "t3": "一朵美麗的紅玫瑰在花園裡嬌豔盛開。"
    },
    "lily": {
        "s1": "White lily is pure.", "t1": "白百合純潔雅致。",
        "s2": "Lilies float on pond water.", "t2": "純白睡蓮優雅地漂浮在池塘水面。",
        "s3": "A sweet white lily blooms by water.", "t3": "一朵純潔的白百合花在水邊靜靜綻放。"
    },
    "sunflower": {
        "s1": "Sunflower follows the sun.", "t1": "向日葵迎向太陽升起。",
        "s2": "Giant sunflowers have golden petals.", "t2": "高大的向日葵長著金燦燦的花瓣。",
        "s3": "Bright yellow sunflowers smile at the sun.", "t3": "金黃燦爛的向日葵對著溫暖的太陽微笑。"
    },
    "wave": {
        "s1": "The ocean wave splashes.", "t1": "海浪嘩啦拍打岸邊。",
        "s2": "Ocean waves crash on shore.", "t2": "大海的浪花嘩嘩衝擊著海岸沙灘。",
        "s3": "Blue ocean waves roll into the shore.", "t3": "藍藍的海浪一層一層捲上了海灘。"
    },
    "breeze": {
        "s1": "Gentle breeze blows cool.", "t1": "微風輕拂好涼快。",
        "s2": "Morning breeze sways green leaves.", "t2": "清晨的涼風吹動了滿園綠葉。",
        "s3": "A cool breeze blows on warm days.", "t3": "涼爽的微風在溫暖的日子裡輕輕拂面。"
    },
    "storm": {
        "s1": "The storm is loud.", "t1": "暴風雨聲音好大。",
        "s2": "Dark clouds bring heavy storm.", "t2": "烏雲帶來了陣陣強烈暴風雨。",
        "s3": "We stay inside during the heavy storm.", "t3": "在猛烈的暴風雨天我們都乖乖待在室內。"
    },
    "thunder": {
        "s1": "Hear the thunder boom.", "t1": "聽打雷轟隆巨響。",
        "s2": "Loud thunder rumbles in sky.", "t2": "沉悶的響雷在烏雲天際隆隆滾動。",
        "s3": "Loud thunder rumbles across dark stormy sky.", "t3": "隆隆的大雷聲在烏雲密布的天空滾動。"
    },
    "lightning": {
        "s1": "Lightning flashes so bright.", "t1": "閃電瞬間劃過天際好亮。",
        "s2": "Bright lightning strikes dark clouds.", "t2": "明亮的閃電撕裂了陰沉的暴風雨雲。",
        "s3": "Bright lightning flashes across dark storm clouds.", "t3": "耀眼的閃電在漆黑的暴風雲層中劃過。"
    },
    "ice": {
        "s1": "The ice is cold.", "t1": "冰塊非常冰涼。",
        "s2": "Ice cubes float in drink.", "t2": "晶瑩冰塊漂浮在冰涼飲料中。",
        "s3": "Cold ice cubes melt in warm water.", "t3": "冰涼的冰塊在溫水裡漸漸融化消失了。"
    },
    "frost": {
        "s1": "Frost coats the window.", "t1": "窗上結了一層薄白霜。",
        "s2": "Morning frost glitters on grass.", "t2": "清晨的白霜在草地上閃爍著銀光。",
        "s3": "White frost covers windows on winter mornings.", "t3": "白白的冬霜在寒冷冬天的早晨覆蓋窗戶。"
    },
    "fog": {
        "s1": "The fog is thick.", "t1": "晨霧好濃厚迷濛。",
        "s2": "Morning fog hides the hills.", "t2": "晨霧籠罩隱藏了遠處起伏的山丘。",
        "s3": "White morning fog covers the quiet forest.", "t3": "白茫茫的晨霧籠罩在安靜美麗的森林間。"
    }
}
