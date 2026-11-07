# build_vocab.py - Generate 50 comprehensive vocabulary words with 3 scenarios x 3 sentences = 9 sentences each
import json

DATA = [
  # --- Category 1: Home & Daily Life (8 words) ---
  {
    "id": "desk", "word": "desk", "phonetic": "/dɛsk/", "meaning": "名词：书桌，办公桌", "emoji": "🪑",
    "category": "home", "level": "L1", "role": "review",
    "variants": ["desk", "desks", "deck", "disk", "disc", "das"],
    "scenarios": [
      {
        "tag": "情境一 · 认知特征描述",
        "desc": "观察桌子的外观与状态",
        "sentences": [
          "This is a clean wooden desk.",
          "The desk is next to the window.",
          "I have a small blue study desk."
        ]
      },
      {
        "tag": "情境二 · 动作指令与整理",
        "desc": "在书桌前的动作与自理能力",
        "sentences": [
          "Put your story book on the desk.",
          "Please wipe the dust off your desk.",
          "Sit down at your desk and draw a picture."
        ]
      },
      {
        "tag": "情境三 · 课堂与生活应用",
        "desc": "在学校与家里的对话场景",
        "sentences": [
          "I sit at my desk in school every day.",
          "Is this desk yours or your sister's?",
          "We can share this big desk together."
        ]
      }
    ]
  },
  {
    "id": "bed", "word": "bed", "phonetic": "/bɛd/", "meaning": "名词：床，小床", "emoji": "🛏️",
    "category": "home", "level": "L1", "role": "review",
    "variants": ["bed", "beds", "bad", "bet"],
    "scenarios": [
      {
        "tag": "情境一 · 认知特征描述",
        "desc": "床的外观与触感",
        "sentences": [
          "My bed is very soft and warm.",
          "There is a blue blanket on the bed.",
          "The big bed is in the master bedroom."
        ]
      },
      {
        "tag": "情境二 · 动作指令与自理",
        "desc": "起卧与整理动作",
        "sentences": [
          "Time to make your bed in the morning.",
          "Do not jump up and down on the bed.",
          "Go to bed early and sleep well tonight."
        ]
      },
      {
        "tag": "情境三 · 睡前对话",
        "desc": "睡前亲子温馨交流",
        "sentences": [
          "Mom tells me a story beside my bed.",
          "I like to hug my teddy bear in bed.",
          "Are you ready to get out of bed now?"
        ]
      }
    ]
  },
  {
    "id": "cup", "word": "cup", "phonetic": "/kʌp/", "meaning": "名词：水杯，茶杯", "emoji": "🥛",
    "category": "home", "level": "L1", "role": "new",
    "variants": ["cup", "cups", "cap", "cop"],
    "scenarios": [
      {
        "tag": "情境一 · 认知特征描述",
        "desc": "杯子的颜色与造型",
        "sentences": [
          "This is a cute yellow plastic cup.",
          "The glass cup is full of fresh milk.",
          "My favorite cup has a cartoon animal."
        ]
      },
      {
        "tag": "情境二 · 动作指令与安全",
        "desc": "拿放与使用水杯",
        "sentences": [
          "Hold the cup with both hands carefully.",
          "Please pass me that clean water cup.",
          "Wash your cup after you drink your milk."
        ]
      },
      {
        "tag": "情境三 · 日常对话应用",
        "desc": "点餐与日常饮水交流",
        "sentences": [
          "Would you like a warm cup of hot water?",
          "Can I have another cup of apple juice?",
          "Mom drinks a cup of fragrant tea every day."
        ]
      }
    ]
  },
  {
    "id": "door", "word": "door", "phonetic": "/dɔːr/", "meaning": "名词：房门，大门", "emoji": "🚪",
    "category": "home", "level": "L1", "role": "review",
    "variants": ["door", "doors"],
    "scenarios": [
      {
        "tag": "情境一 · 认知特征描述",
        "desc": "门的方位与材质",
        "sentences": [
          "The front door of our house is red.",
          "There is a small bell beside the door.",
          "The bedroom door is made of solid wood."
        ]
      },
      {
        "tag": "情境二 · 动作指令与礼貌",
        "desc": "开门关门的日常动作",
        "sentences": [
          "Please knock on the door before entering.",
          "Remember to close the door gently behind you.",
          "Open the front door to welcome our guests."
        ]
      },
      {
        "tag": "情境三 · 日常生活对话",
        "desc": "迎客与外出提醒",
        "sentences": [
          "Who is knocking loudly at the door?",
          "Dad is standing right outside the door.",
          "Lock the door when we leave the house."
        ]
      }
    ]
  },
  {
    "id": "clock", "word": "clock", "phonetic": "/klɑːk/", "meaning": "名词：时钟，闹钟", "emoji": "⏰",
    "category": "home", "level": "L1", "role": "new",
    "variants": ["clock", "clocks", "cock", "lock"],
    "scenarios": [
      {
        "tag": "情境一 · 认知特征描述",
        "desc": "钟表的形状与指针",
        "sentences": [
          "The round wall clock has twelve numbers.",
          "The alarm clock makes a loud ringing sound.",
          "A small digital clock sits on the desk."
        ]
      },
      {
        "tag": "情境二 · 动作指令与看时间",
        "desc": "看时间和设置闹钟",
        "sentences": [
          "Look at the clock to see the time.",
          "Set the alarm clock for seven in the morning.",
          "Listen to the clock go tick tick tick."
        ]
      },
      {
        "tag": "情境三 · 作息对话应用",
        "desc": "时间观念与作息交流",
        "sentences": [
          "What time does the kitchen clock say?",
          "The clock tells us it is time for bed.",
          "We must hurry because the clock is ticking."
        ]
      }
    ]
  },
  {
    "id": "box", "word": "box", "phonetic": "/bɑːks/", "meaning": "名词：盒子，箱子", "emoji": "📦",
    "category": "home", "level": "L1", "role": "review",
    "variants": ["box", "boxes", "fox", "backs"],
    "scenarios": [
      {
        "tag": "情境一 · 认知特征描述",
        "desc": "盒子的材质与颜色",
        "sentences": [
          "This cardboard box is light and brown.",
          "Here is a colorful mystery gift box.",
          "The plastic box keeps all my toys safe."
        ]
      },
      {
        "tag": "情境二 · 动作整理与打开",
        "desc": "收纳整理与开箱",
        "sentences": [
          "Open the big box to see the surprise.",
          "Put all your wooden blocks into the box.",
          "Help me carry this small paper box."
        ]
      },
      {
        "tag": "情境三 · 日常游戏与应用",
        "desc": "找玩具与装收纳交流",
        "sentences": [
          "What is hidden inside this little box?",
          "My puppy likes to sleep inside the shoe box.",
          "We packed the old books in a heavy box."
        ]
      }
    ]
  },
  {
    "id": "lamp", "word": "lamp", "phonetic": "/læmp/", "meaning": "名词：台灯，电灯", "emoji": "💡",
    "category": "home", "level": "L1", "role": "new",
    "variants": ["lamp", "lamps", "lamb", "lump"],
    "scenarios": [
      {
        "tag": "情境一 · 认知特征描述",
        "desc": "灯光的亮度与颜色",
        "sentences": [
          "The table lamp gives off a warm yellow light.",
          "A cute desk lamp sits right by my computer.",
          "The floor lamp makes the living room bright."
        ]
      },
      {
        "tag": "情境二 · 开关操作指令",
        "desc": "节约用电与开关动作",
        "sentences": [
          "Turn on the desk lamp when you read.",
          "Please switch off the lamp before going out.",
          "Adjust the lamp so it shines on your book."
        ]
      },
      {
        "tag": "情境三 · 睡前与生活对话",
        "desc": "夜读与伴睡交流",
        "sentences": [
          "Can you leave the small night lamp on?",
          "The bright lamp helps me see things clearly.",
          "I turn off my bedside lamp to fall asleep."
        ]
      }
    ]
  },
  {
    "id": "chair", "word": "chair", "phonetic": "/tʃɛr/", "meaning": "名词：椅子", "emoji": "🪑",
    "category": "home", "level": "L1", "role": "consolidate",
    "variants": ["chair", "chairs", "cheer"],
    "scenarios": [
      {
        "tag": "情境一 · 认知特征描述",
        "desc": "椅子的款式与舒适度",
        "sentences": [
          "This is a comfortable wooden rocking chair.",
          "There are four sturdy chairs around the dining table.",
          "The baby high chair is very safe and clean."
        ]
      },
      {
        "tag": "情境二 · 动作指令与礼貌",
        "desc": "拉椅子与入座礼仪",
        "sentences": [
          "Pull out the chair and sit down quietly.",
          "Push your chair in when you stand up.",
          "Please offer that soft chair to grandma."
        ]
      },
      {
        "tag": "情境三 · 生活聚餐对话",
        "desc": "家庭用餐与聚会交流",
        "sentences": [
          "Is anyone sitting in this empty chair?",
          "I sit in my own small chair at dinner.",
          "We need one more chair for our guest."
        ]
      }
    ]
  },

  # --- Category 2: Food & Drinks (8 words) ---
  {
    "id": "apple", "word": "apple", "phonetic": "/ˈæp.əl/", "meaning": "名词：苹果", "emoji": "🍎",
    "category": "food", "level": "L2", "role": "new",
    "variants": ["apple", "apples", "app", "able", "apo"],
    "scenarios": [
      {
        "tag": "情境一 · 美味口感与外观",
        "desc": "苹果的颜色与香甜口感",
        "sentences": [
          "I eat a sweet and crunchy red apple.",
          "This green apple tastes a little bit sour.",
          "Fresh apples are round and shiny on the tree."
        ]
      },
      {
        "tag": "情境二 · 分享与准备动作",
        "desc": "洗切分享苹果的动作",
        "sentences": [
          "Wash the ripe red apple before taking a bite.",
          "Mom cuts the juicy apple into four slices.",
          "Would you like to share this apple with me?"
        ]
      },
      {
        "tag": "情境三 · 营养与生活对话",
        "desc": "日常对话与健康谚语",
        "sentences": [
          "An apple a day keeps the doctor away.",
          "Apples are definitely my favorite healthy fruit.",
          "Do you prefer sweet red apples or green apples?"
        ]
      }
    ]
  },
  {
    "id": "water", "word": "water", "phonetic": "/ˈwɔː.tər/", "meaning": "名词：水，白开水", "emoji": "💧",
    "category": "food", "level": "L2", "role": "consolidate",
    "variants": ["water", "wat", "warter", "walter"],
    "scenarios": [
      {
        "tag": "情境一 · 认知特征描述",
        "desc": "水的清澈与自然状态",
        "sentences": [
          "Pure water is clear and has no color.",
          "Cool water feels refreshing on a hot day.",
          "Fish swim happily in the clean blue water."
        ]
      },
      {
        "tag": "情境二 · 动作指令与卫生",
        "desc": "喝水与清洗动作",
        "sentences": [
          "Wash your dirty hands with soap and water.",
          "Pour some warm water into my little cup.",
          "Drink plenty of water after running and playing."
        ]
      },
      {
        "tag": "情境三 · 日常生活对话",
        "desc": "口渴需求与关怀对话",
        "sentences": [
          "Can I please have a glass of cold water?",
          "Are you thirsty and in need of some water?",
          "Remember to bring your water bottle to school."
        ]
      }
    ]
  },
  {
    "id": "banana", "word": "banana", "phonetic": "/bəˈnæn.ə/", "meaning": "名词：香蕉", "emoji": "🍌",
    "category": "food", "level": "L2", "role": "new",
    "variants": ["banana", "bananas"],
    "scenarios": [
      {
        "tag": "情境一 · 颜色成熟与形状",
        "desc": "香蕉的弯弯形状与色泽",
        "sentences": [
          "The yellow banana is sweet and crescent-shaped.",
          "Green bananas need a few days to ripen.",
          "A bunch of fresh bananas sits in the fruit basket."
        ]
      },
      {
        "tag": "情境二 · 动作剥皮与吃法",
        "desc": "剥皮与垃圾分类动作",
        "sentences": [
          "Peel the yellow banana before you take a bite.",
          "Throw the banana peel into the trash can.",
          "Slice the soft banana over your morning cereal."
        ]
      },
      {
        "tag": "情境三 · 趣味常识与对话",
        "desc": "动物食性与加餐交流",
        "sentences": [
          "Playful monkeys in the zoo love to eat bananas.",
          "Can I have a sweet banana for my afternoon snack?",
          "We can blend ripe bananas into a yummy smoothie."
        ]
      }
    ]
  },
  {
    "id": "milk", "word": "milk", "phonetic": "/mɪlk/", "meaning": "名词：牛奶", "emoji": "🥛",
    "category": "food", "level": "L1", "role": "review",
    "variants": ["milk", "milks", "make"],
    "scenarios": [
      {
        "tag": "情境一 · 认知特征描述",
        "desc": "牛奶的白色与营养",
        "sentences": [
          "Fresh cow milk is creamy, white, and healthy.",
          "Warm milk has a comforting and pleasant smell.",
          "A carton of organic milk is in the refrigerator."
        ]
      },
      {
        "tag": "情境二 · 动作指令与饮用",
        "desc": "倒牛奶与早餐自理",
        "sentences": [
          "Drink a tall glass of warm milk every morning.",
          "Pour the milk carefully without spilling a drop.",
          "Stir a spoonful of honey into your warm milk."
        ]
      },
      {
        "tag": "情境三 · 早餐与常识对话",
        "desc": "早餐搭配与骨骼健康交流",
        "sentences": [
          "I usually eat crispy bread and milk for breakfast.",
          "Friendly cows on the farm give us delicious milk.",
          "Drinking milk helps build strong and healthy bones."
        ]
      }
    ]
  },
  {
    "id": "bread", "word": "bread", "phonetic": "/brɛd/", "meaning": "名词：面包", "emoji": "🍞",
    "category": "food", "level": "L1", "role": "new",
    "variants": ["bread", "breads", "bed", "red"],
    "scenarios": [
      {
        "tag": "情境一 · 香气与口感描述",
        "desc": "面包的松软与金黄外观",
        "sentences": [
          "The freshly baked bread smells wonderful.",
          "This slice of white bread is very soft.",
          "Golden toast bread is warm and crispy."
        ]
      },
      {
        "tag": "情境二 · 动作制作与涂抹",
        "desc": "涂果酱与做三明治",
        "sentences": [
          "Spread sweet strawberry jam on your bread.",
          "Cut the loaf of bread with a butter knife.",
          "Put cheese between two slices of brown bread."
        ]
      },
      {
        "tag": "情境三 · 烘焙生活对话",
        "desc": "面包店选购与分享",
        "sentences": [
          "Do you want toasted bread or plain bread?",
          "The baker bakes fresh bread every single morning.",
          "Can you buy a loaf of whole wheat bread?"
        ]
      }
    ]
  },
  {
    "id": "egg", "word": "egg", "phonetic": "/ɛɡ/", "meaning": "名词：鸡蛋，蛋", "emoji": "🥚",
    "category": "food", "level": "L1", "role": "new",
    "variants": ["egg", "eggs", "leg"],
    "scenarios": [
      {
        "tag": "情境一 · 外观形状描述",
        "desc": "椭圆造型与蛋壳特征",
        "sentences": [
          "The hen laid a smooth oval egg in the nest.",
          "The yellow egg yolk is in the middle of the egg.",
          "There are six brown eggs inside the carton."
        ]
      },
      {
        "tag": "情境二 · 烹饪与动作指令",
        "desc": "剥蛋壳与煎蛋动作",
        "sentences": [
          "Peel the boiled egg carefully after it cools down.",
          "Crack the fresh egg into the frying pan.",
          "Handle the raw egg gently so it does not break."
        ]
      },
      {
        "tag": "情境三 · 营养餐桌对话",
        "desc": "煎蛋水煮蛋口味选择",
        "sentences": [
          "Do you like your morning egg fried or boiled?",
          "Eating an egg provides great energy for growing kids.",
          "Mom is making scrambled eggs with sweet tomatoes."
        ]
      }
    ]
  },
  {
    "id": "juice", "word": "juice", "phonetic": "/dʒuːs/", "meaning": "名词：果汁", "emoji": "🧃",
    "category": "food", "level": "L1", "role": "review",
    "variants": ["juice", "juices", "choose"],
    "scenarios": [
      {
        "tag": "情境一 · 色泽与风味描述",
        "desc": "果汁的清新果香与颜色",
        "sentences": [
          "Fresh orange juice is bright orange and sweet.",
          "Cold watermelon juice is wonderful in the hot summer.",
          "This bottle of grape juice has no added sugar."
        ]
      },
      {
        "tag": "情境二 · 压榨与饮用动作",
        "desc": "鲜榨果汁与倒果汁动作",
        "sentences": [
          "Squeeze the fresh lemon to make sour juice.",
          "Pour the cold apple juice into my tall glass.",
          "Sip your fruit juice with a colorful straw."
        ]
      },
      {
        "tag": "情境三 · 野餐聚会对话",
        "desc": "日常点单与聚会分享",
        "sentences": [
          "What kind of juice would you like to drink?",
          "We brought sweet apple juice for our family picnic.",
          "Can I have another cup of freshly squeezed juice?"
        ]
      }
    ]
  },
  {
    "id": "cake", "word": "cake", "phonetic": "/keɪk/", "meaning": "名词：蛋糕", "emoji": "🎂",
    "category": "food", "level": "L1", "role": "new",
    "variants": ["cake", "cakes", "take", "make"],
    "scenarios": [
      {
        "tag": "情境一 · 奶油与造型描述",
        "desc": "蛋糕的香甜层层与装饰",
        "sentences": [
          "The birthday cake is covered in pink sweet cream.",
          "A chocolate cake smells wonderfully rich and sweet.",
          "There are colorful fresh berries on top of the cake."
        ]
      },
      {
        "tag": "情境二 · 吹蜡烛与分切动作",
        "desc": "许愿与切蛋糕动作",
        "sentences": [
          "Make a wish and blow out the candles on the cake.",
          "Cut the birthday cake into equal slices for everyone.",
          "Help me put pretty candles onto the birthday cake."
        ]
      },
      {
        "tag": "情境三 · 生日派对对话",
        "desc": "庆祝与分享祝福交流",
        "sentences": [
          "Happy birthday to you! Enjoy this delicious cake!",
          "Who would like the first slice of chocolate cake?",
          "Mom baked this lovely sponge cake just for my party."
        ]
      }
    ]
  },

  # --- Category 3: Animals & Pets (9 words) ---
  {
    "id": "cat", "word": "cat", "phonetic": "/kæt/", "meaning": "名词：猫咪", "emoji": "🐱",
    "category": "animals", "level": "L1", "role": "review",
    "variants": ["cat", "cats", "cut", "cap", "cad"],
    "scenarios": [
      {
        "tag": "情境一 · 动物萌态与外貌",
        "desc": "毛色、胡须与温顺特征",
        "sentences": [
          "The cute kitten has soft fur and long whiskers.",
          "A sleeping white cat is curled up on the rug.",
          "The playful black cat has big green eyes."
        ]
      },
      {
        "tag": "情境二 · 抚摸动作与互动",
        "desc": "抱猫、梳毛与喂食动作",
        "sentences": [
          "Pet the friendly cat gently on its furry head.",
          "Give the hungry cat a small bowl of fresh milk.",
          "Do not pull the cat's tail because it hurts."
        ]
      },
      {
        "tag": "情境三 · 趣味习性与对话",
        "desc": "叫声、捉迷藏与陪伴交流",
        "sentences": [
          "The happy cat purrs and says meow meow.",
          "Look! The nimble cat caught a toy mouse.",
          "My pet cat always sleeps at the foot of my bed."
        ]
      }
    ]
  },
  {
    "id": "dog", "word": "dog", "phonetic": "/dɔːɡ/", "meaning": "名词：小狗，猎犬", "emoji": "🐶",
    "category": "animals", "level": "L1", "role": "review",
    "variants": ["dog", "dogs", "dock", "doc"],
    "scenarios": [
      {
        "tag": "情境一 · 外貌特征与毛色",
        "desc": "耳朵、尾巴与活泼特征",
        "sentences": [
          "The cheerful golden dog has floppy long ears.",
          "A brave big shepherd dog guards our quiet yard.",
          "The tiny puppy is fluffy, playful, and very energetic."
        ]
      },
      {
        "tag": "情境二 · 动作指令与投掷游戏",
        "desc": "扔飞盘、握手与遛狗指令",
        "sentences": [
          "Throw the red rubber ball for the excited dog.",
          "Walk the dog in the park every sunny afternoon.",
          "Teach the smart dog to sit down and shake hands."
        ]
      },
      {
        "tag": "情境三 · 情感陪伴与生活对话",
        "desc": "忠实玩伴与家庭成员对话",
        "sentences": [
          "The loyal dog wags its tail to welcome me home.",
          "My puppy barks happily when we play in the garden.",
          "Dogs are known as human beings' very best friends."
        ]
      }
    ]
  },
  {
    "id": "fish", "word": "fish", "phonetic": "/fɪʃ/", "meaning": "名词：小鱼，鱼类", "emoji": "🐟",
    "category": "animals", "level": "L1", "role": "new",
    "variants": ["fish", "fished"],
    "scenarios": [
      {
        "tag": "情境一 · 水中外观与游动",
        "desc": "鱼鳞、鱼鳍与水族箱特征",
        "sentences": [
          "The tiny goldfish has shiny scales and a long tail.",
          "Colorful little tropical fish swim in the blue aquarium.",
          "A big silver fish leaps out of the river water."
        ]
      },
      {
        "tag": "情境二 · 喂食动作与观察",
        "desc": "撒饲料与水族馆观察指令",
        "sentences": [
          "Feed the hungry fish with a pinch of fish flakes.",
          "Watch how smoothly the fish moves through the water.",
          "Keep the fish tank clean so the fish stay healthy."
        ]
      },
      {
        "tag": "情境三 · 生态习性与对话",
        "desc": "海洋自然与常识探索",
        "sentences": [
          "Can fish close their eyes when they are asleep?",
          "Fish use their fins and gills to swim and breathe.",
          "Look at that funny clownfish hiding among sea anemones."
        ]
      }
    ]
  },
  {
    "id": "bird", "word": "bird", "phonetic": "/bɜːrd/", "meaning": "名词：小鸟，飞鸟", "emoji": "🐦",
    "category": "animals", "level": "L1", "role": "review",
    "variants": ["bird", "birds"],
    "scenarios": [
      {
        "tag": "情境一 · 羽毛与外貌观察",
        "desc": "翅膀、喙与彩色羽毛",
        "sentences": [
          "The cheerful little bird has bright blue feathers.",
          "A mother bird is sitting quietly in her round nest.",
          "The tiny hummingbird has a long, slender beak."
        ]
      },
      {
        "tag": "情境二 · 展翅动作与投喂",
        "desc": "飞翔动作与撒面包屑指令",
        "sentences": [
          "Birds flap their strong wings to soar in the sky.",
          "Scatter some breadcrumbs in the yard for wild birds.",
          "Listen carefully to the sweet melody the bird sings."
        ]
      },
      {
        "tag": "情境三 · 清晨大自然对话",
        "desc": "清晨鸟鸣与筑巢习性",
        "sentences": [
          "The early bird catches the juicy little worm.",
          "Birds sing sweet songs to wake us up in the morning.",
          "Where do the swallows fly when cold winter comes?"
        ]
      }
    ]
  },
  {
    "id": "duck", "word": "duck", "phonetic": "/dʌk/", "meaning": "名词：鸭子", "emoji": "🦆",
    "category": "animals", "level": "L1", "role": "new",
    "variants": ["duck", "ducks", "dark"],
    "scenarios": [
      {
        "tag": "情境一 · 外观特征与蹼足",
        "desc": "黄色鸭嘴、扁平蹼足与羽毛",
        "sentences": [
          "The mother duck has waterproof feathers and orange feet.",
          "Cute yellow ducklings waddle behind their loving mother.",
          "A wild mallard duck has a shiny green head."
        ]
      },
      {
        "tag": "情境二 · 划水动作与叫声指令",
        "desc": "池塘游水与学鸭子叫",
        "sentences": [
          "Ducks paddle their webbed feet quickly to swim.",
          "Can you imitate the duck saying quack quack quack?",
          "Throw small pieces of bread to the ducks in the pond."
        ]
      },
      {
        "tag": "情境三 · 农场池塘对话",
        "desc": "乡村农场与童谣对话",
        "sentences": [
          "Five little ducks went out to play one sunny day.",
          "Ducks stay warm and dry even inside the cold pond.",
          "Look at the funny ducks diving underwater for food."
        ]
      }
    ]
  },
  {
    "id": "pig", "word": "pig", "phonetic": "/pɪɡ/", "meaning": "名词：小猪，家猪", "emoji": "🐷",
    "category": "animals", "level": "L1", "role": "new",
    "variants": ["pig", "pigs", "big", "pick"],
    "scenarios": [
      {
        "tag": "情境一 · 粉嫩外观特征",
        "desc": "卷尾巴、大鼻子与粉色皮肤",
        "sentences": [
          "The cute pink piggy has a curly little tail.",
          "The mother pig has large floppy ears and a flat snout.",
          "Fat little piglets love rolling happily in wet mud."
        ]
      },
      {
        "tag": "情境二 · 动作互动与喂养",
        "desc": "吃食与学小猪哼哼声",
        "sentences": [
          "The hungry pig oinks loudly when dinner time arrives.",
          "Give the farm pigs fresh vegetables and clean water.",
          "Watch the chubby pig take a relaxing mud bath."
        ]
      },
      {
        "tag": "情境三 · 经典童话生活对话",
        "desc": "三只小猪与农场生活",
        "sentences": [
          "Have you ever heard the fairy tale of the three little pigs?",
          "Pigs are actually very clean and intelligent animals.",
          "The baby pig nudges its mother with its round pink nose."
        ]
      }
    ]
  },
  {
    "id": "bear", "word": "bear", "phonetic": "/bɛr/", "meaning": "名词：熊，狗熊", "emoji": "🐻",
    "category": "animals", "level": "L1", "role": "new",
    "variants": ["bear", "bears", "bare", "pear"],
    "scenarios": [
      {
        "tag": "情境一 · 雄壮外观描述",
        "desc": "厚重皮毛、利爪与体型",
        "sentences": [
          "The big brown bear has thick fur and strong paws.",
          "A polar bear is furry and pure white like fresh snow.",
          "The giant panda bear loves munching on green bamboo."
        ]
      },
      {
        "tag": "情境二 · 捕鱼与动作指令",
        "desc": "捕鱼抓蜜与爬树动作",
        "sentences": [
          "Bears stand on two legs to reach high tree branches.",
          "Watch the brown bear catch jumping salmon in the river.",
          "Do not approach a wild bear in the deep forest."
        ]
      },
      {
        "tag": "情境三 · 冬眠与童话对话",
        "desc": "泰迪熊玩偶与森林童话",
        "sentences": [
          "Bears sleep in cozy mountain caves all through the winter.",
          "I love to cuddle with my soft brown teddy bear in bed.",
          "Winnie the Pooh is a famous bear who loves sweet honey."
        ]
      }
    ]
  },
  {
    "id": "rabbit", "word": "rabbit", "phonetic": "/ˈræb.ɪt/", "meaning": "名词：兔子，小白兔", "emoji": "🐰",
    "category": "animals", "level": "L2", "role": "new",
    "variants": ["rabbit", "rabbits", "habit"],
    "scenarios": [
      {
        "tag": "情境一 · 软萌外貌描述",
        "desc": "长耳朵、红眼睛与毛绒尾巴",
        "sentences": [
          "The white bunny has long upright ears and a cotton-ball tail.",
          "A pet rabbit has very soft gray fur and twitching whiskers.",
          "Baby rabbits are tiny, shy, and incredibly adorable."
        ]
      },
      {
        "tag": "情境二 · 蹦跳动作与喂养",
        "desc": "蹦蹦跳跳与喂胡萝卜指令",
        "sentences": [
          "Feed the fluffy rabbit with fresh green carrot tops.",
          "Rabbits hop around quickly on their strong hind legs.",
          "Stroke the friendly rabbit gently from head to tail."
        ]
      },
      {
        "tag": "情境三 · 寓言童话对话",
        "desc": "龟兔赛跑与爱丽丝梦游仙境",
        "sentences": [
          "The speedy rabbit lost the race to the steady turtle.",
          "Rabbits dig deep underground burrows to keep safe and warm.",
          "Look at the bunny munching quietly on fresh sweet clover."
        ]
      }
    ]
  },
  {
    "id": "monkey", "word": "monkey", "phonetic": "/ˈmʌŋ.ki/", "meaning": "名词：猴子", "emoji": "🐵",
    "category": "animals", "level": "L2", "role": "new",
    "variants": ["monkey", "monkeys", "money"],
    "scenarios": [
      {
        "tag": "情境一 · 机灵外貌与长尾",
        "desc": "棕色毛发、长尾巴与灵巧手足",
        "sentences": [
          "The clever little monkey has a long and flexible tail.",
          "A baby monkey clings tightly to its mother's belly.",
          "The cheeky brown monkey has bright, curious brown eyes."
        ]
      },
      {
        "tag": "情境二 · 攀爬动作与玩耍",
        "desc": "荡秋千、摘果子与抓痒指令",
        "sentences": [
          "Monkeys swing skillfully from vine to vine in trees.",
          "Hand a ripe yellow banana to the hungry zoo monkey.",
          "Watch the playful monkey jump across the wooden bars."
        ]
      },
      {
        "tag": "情境三 · 趣味习性与对话",
        "desc": "动物园游览与儿歌对话",
        "sentences": [
          "Five little monkeys were jumping on the big soft bed.",
          "Monkeys use both their agile hands and feet to climb trees.",
          "The funny monkey is making goofy faces at the tourists."
        ]
      }
    ]
  },

  # --- Category 4: Nature & Weather (8 words) ---
  {
    "id": "sun", "word": "sun", "phonetic": "/sʌn/", "meaning": "名词：太阳，阳光", "emoji": "☀️",
    "category": "nature", "level": "L1", "role": "new",
    "variants": ["sun", "son", "some"],
    "scenarios": [
      {
        "tag": "情境一 · 天空光芒与色彩",
        "desc": "朝阳、晚霞与金色光辉",
        "sentences": [
          "The brilliant golden sun shines in the clear blue sky.",
          "The morning sun warms the cool mountain grass.",
          "A spectacular orange sunset marks the end of the day."
        ]
      },
      {
        "tag": "情境二 · 户外防晒动作指令",
        "desc": "戴太阳镜、涂防晒与日光浴",
        "sentences": [
          "Put on your sun hat and sunglasses when going outside.",
          "Feel the pleasant warm sun directly upon your face.",
          "Do not look straight into the bright sun with bare eyes."
        ]
      },
      {
        "tag": "情境三 · 作息规律与自然对话",
        "desc": "日出日落与植物光合作用",
        "sentences": [
          "The bright sun rises in the east and sets in the west.",
          "Green plants need warm sunlight and pure water to grow.",
          "What a gorgeous, bright, and sunny weekend morning!"
        ]
      }
    ]
  },
  {
    "id": "moon", "word": "moon", "phonetic": "/muːn/", "meaning": "名词：月亮，月光", "emoji": "🌙",
    "category": "nature", "level": "L1", "role": "new",
    "variants": ["moon", "moons"],
    "scenarios": [
      {
        "tag": "情境一 · 夜空月色与轮廓",
        "desc": "弯月、满月与银白清辉",
        "sentences": [
          "The silver crescent moon glows gently in the night sky.",
          "Tonight the big round full moon looks like a silver plate.",
          "Soft moonlight streams in through my bedroom window."
        ]
      },
      {
        "tag": "情境二 · 仰望观察动作指令",
        "desc": "用望远镜看月亮环形山",
        "sentences": [
          "Look up at the glowing moon through our telescope.",
          "Point your finger toward the bright moon among clouds.",
          "Watch the white clouds glide slowly across the moon."
        ]
      },
      {
        "tag": "情境三 · 中秋节与睡前对话",
        "desc": "中秋赏月与睡前晚安对话",
        "sentences": [
          "We eat sweet mooncakes while admiring the harvest moon.",
          "Good night moon, good night stars, see you in the morning.",
          "Did you know brave astronauts have walked on the moon?"
        ]
      }
    ]
  },
  {
    "id": "star", "word": "star", "phonetic": "/stɑːr/", "meaning": "名词：星星，恒星", "emoji": "⭐",
    "category": "nature", "level": "L1", "role": "review",
    "variants": ["star", "stars", "start"],
    "scenarios": [
      {
        "tag": "情境一 · 闪烁光芒与夜空",
        "desc": "繁星点点、星座与银河",
        "sentences": [
          "Countless twinkling stars decorate the dark velvet sky.",
          "The North Star shines steadily to guide travelers at night.",
          "A brilliant shooting star darts across the midnight sky."
        ]
      },
      {
        "tag": "情境二 · 数星星与许愿动作",
        "desc": "手指点数与闭眼许愿指令",
        "sentences": [
          "Close your eyes and make a wish upon that bright star.",
          "Count the visible stars you can spot above our house.",
          "Connect the bright stars with your finger to form shapes."
        ]
      },
      {
        "tag": "情境三 · 经典儿歌童年对话",
        "desc": "小星星儿歌与天文奥秘",
        "sentences": [
          "Twinkle, twinkle, little star, how I wonder what you are!",
          "Stars look tiny to us because they are trillions of miles away.",
          "My teacher gave me a shiny golden star sticker for good work."
        ]
      }
    ]
  },
  {
    "id": "tree", "word": "tree", "phonetic": "/triː/", "meaning": "名词：大树，树木", "emoji": "🌳",
    "category": "nature", "level": "L1", "role": "new",
    "variants": ["tree", "trees", "three"],
    "scenarios": [
      {
        "tag": "情境一 · 挺拔树木与枝叶",
        "desc": "粗壮树干、茂盛树冠与落叶",
        "sentences": [
          "The tall oak tree has thick brown bark and green leaves.",
          "In autumn, colorful orange and red leaves fall from the tree.",
          "A blossoming apple tree is full of fragrant white flowers."
        ]
      },
      {
        "tag": "情境二 · 动作植树与攀爬",
        "desc": "给树浇水、种树苗与避暑指令",
        "sentences": [
          "Plant a young tree sapling in the school yard.",
          "Rest under the cool shade of the leafy tree on hot days.",
          "Do not break branches when you play around the old tree."
        ]
      },
      {
        "tag": "情境三 · 鸟类家园与生态对话",
        "desc": "鸟巢家园与环境保护交流",
        "sentences": [
          "Birds build cozy straw nests high up in the tree branches.",
          "Squirrels store sweet acorns inside hollow tree trunks.",
          "Trees clean our air and give us fresh oxygen to breathe."
        ]
      }
    ]
  },
  {
    "id": "rain", "word": "rain", "phonetic": "/reɪn/", "meaning": "名词：雨水，下雨", "emoji": "🌧️",
    "category": "nature", "level": "L1", "role": "new",
    "variants": ["rain", "rains", "train"],
    "scenarios": [
      {
        "tag": "情境一 · 雨丝淅沥与声音",
        "desc": "毛毛雨、暴雨与泥土清香",
        "sentences": [
          "Gentle raindrops fall rhythmically upon the glass window.",
          "The heavy summer rain creates clear puddles on the sidewalk.",
          "The refreshing smell of clean rain fills the evening air."
        ]
      },
      {
        "tag": "情境二 · 撑伞踩水动作指令",
        "desc": "撑雨伞、穿雨靴与跳水坑",
        "sentences": [
          "Open your umbrella before stepping out into the cold rain.",
          "Put on your yellow waterproof boots to splash in rain puddles.",
          "Stay safe inside the house until the thunderstorm stops."
        ]
      },
      {
        "tag": "情境三 · 雨后彩虹生活对话",
        "desc": "植物喝水与雨过天晴彩虹",
        "sentences": [
          "Rain, rain, go away, come again another sunny day!",
          "Thirsty garden flowers drink the pure rainwater to blossom.",
          "Look! A magnificent rainbow appeared right after the rain!"
        ]
      }
    ]
  },
  {
    "id": "flower", "word": "flower", "phonetic": "/ˈflaʊ.ər/", "meaning": "名词：花朵，鲜花", "emoji": "🌸",
    "category": "nature", "level": "L2", "role": "new",
    "variants": ["flower", "flowers", "flour"],
    "scenarios": [
      {
        "tag": "情境一 · 花容花色与芳香",
        "desc": "花瓣色彩、芬芳气味与花蕊",
        "sentences": [
          "This lovely pink rose flower smells delightful and sweet.",
          "Yellow sunflower blossoms turn their heads toward the sun.",
          "Tiny purple wildflower petals blanket the green hill."
        ]
      },
      {
        "tag": "情境二 · 浇花采摘动作指令",
        "desc": "拿水壶浇花与爱护花木",
        "sentences": [
          "Water the blooming garden flowers with the watering can.",
          "Smell the delicate sweet scent of this fresh spring flower.",
          "Do not pluck the pretty flowers in public city parks."
        ]
      },
      {
        "tag": "情境三 · 蜜蜂传粉与节日对话",
        "desc": "蜜蜂采蜜与送妈妈鲜花交流",
        "sentences": [
          "Busy honeybees collect sweet nectar from colorful flowers.",
          "I picked a bouquet of lovely flowers for my dear mother.",
          "Spring has arrived because all the garden flowers are blooming!"
        ]
      }
    ]
  },
  {
    "id": "grass", "word": "grass", "phonetic": "/ɡræs/", "meaning": "名词：青草，草地", "emoji": "🌱",
    "category": "nature", "level": "L1", "role": "new",
    "variants": ["grass", "glass"],
    "scenarios": [
      {
        "tag": "情境一 · 绿茵茵草坪描述",
        "desc": "草地色泽、露珠与地毯感",
        "sentences": [
          "The fresh green grass feels soft like a natural carpet.",
          "Morning dew drops sparkle brightly on blades of grass.",
          "The expansive soccer field is covered in lush thick grass."
        ]
      },
      {
        "tag": "情境二 · 赤脚奔跑动作指令",
        "desc": "草地打滚、修剪草坪与散步",
        "sentences": [
          "Take off your shoes and walk barefoot on the cool grass.",
          "Sit down with your friends on the sunny park grass for lunch.",
          "Help your dad push the lawnmower to trim the tall grass."
        ]
      },
      {
        "tag": "情境三 · 野餐聚会对话交流",
        "desc": "草地放风筝与亲近大自然",
        "sentences": [
          "Let's spread our picnic blanket over the dry green grass.",
          "Cute sheep and white horses graze peacefully on mountain grass.",
          "Keep off the freshly planted grass so it can grow strong."
        ]
      }
    ]
  },
  {
    "id": "wind", "word": "wind", "phonetic": "/wɪnd/", "meaning": "名词：风，微风", "emoji": "🍃",
    "category": "nature", "level": "L1", "role": "new",
    "variants": ["wind", "winds", "win"],
    "scenarios": [
      {
        "tag": "情境一 · 风声风势与触感",
        "desc": "微风拂面与大风呼啸",
        "sentences": [
          "A gentle cool breeze whispers softly through the trees.",
          "The strong autumn wind blows dry leaves across the street.",
          "The chilly winter wind makes our cheeks turn rosy pink."
        ]
      },
      {
        "tag": "情境二 · 借风放风筝动作指令",
        "desc": "利用风向放飞风筝与关窗",
        "sentences": [
          "Hold the kite string tightly as the wind lifts it up.",
          "Close the bedroom window tightly before the stormy wind hits.",
          "Feel the invigorating sea wind blowing through your hair."
        ]
      },
      {
        "tag": "情境三 · 风车动力生活对话",
        "desc": "风车发电与帆船乘风破浪",
        "sentences": [
          "The giant white windmills spin around to create clean energy.",
          "Which direction is the prevailing wind blowing from today?",
          "The small sailboat glides swiftly across the bay with the wind."
        ]
      }
    ]
  },

  # --- Category 5: Play & School (9 words) ---
  {
    "id": "ball", "word": "ball", "phonetic": "/bɔːl/", "meaning": "名词：球，皮球", "emoji": "⚽",
    "category": "play", "level": "L1", "role": "review",
    "variants": ["ball", "balls", "bowl"],
    "scenarios": [
      {
        "tag": "情境一 · 球体外形与弹性",
        "desc": "皮球弹跳、颜色与材质",
        "sentences": [
          "The round soccer ball is made of black and white leather.",
          "This bouncy rubber basketball rebounds very high off the gym floor.",
          "A small yellow tennis ball rolls swiftly under the couch."
        ]
      },
      {
        "tag": "情境二 · 踢球接球动作指令",
        "desc": "传球、射门与投篮动作",
        "sentences": [
          "Kick the soccer ball right into the goal net!",
          "Can you catch the bouncy red ball with both hands?",
          "Throw the ball gently to your little brother."
        ]
      },
      {
        "tag": "情境三 · 团队运动对话交流",
        "desc": "课间体育游戏与友谊交流",
        "sentences": [
          "Who wants to join our team to play ball together?",
          "Pass the ball quickly to the open teammate on the left.",
          "Playing ball in the fresh air keeps our bodies strong."
        ]
      }
    ]
  },
  {
    "id": "book", "word": "book", "phonetic": "/bʊk/", "meaning": "名词：书本，画册", "emoji": "📖",
    "category": "play", "level": "L1", "role": "consolidate",
    "variants": ["book", "books", "look", "took"],
    "scenarios": [
      {
        "tag": "情境一 · 书籍外观与插图",
        "desc": "精美绘本、彩色封面与页码",
        "sentences": [
          "This fairy tale picture book has colorful illustrations.",
          "A thick English dictionary is placed on the wooden shelf.",
          "The bedtime story book has exciting tales of brave knights."
        ]
      },
      {
        "tag": "情境二 · 翻书阅读动作指令",
        "desc": "打开翻页与放回书包指令",
        "sentences": [
          "Open your English book to page twenty-five.",
          "Turn the paper pages gently without tearing them.",
          "Pack your textbooks neatly inside your school backpack."
        ]
      },
      {
        "tag": "情境三 · 亲子共读对话交流",
        "desc": "图书馆借书与睡前读书时光",
        "sentences": [
          "What fascinating story are you reading in your new book?",
          "Mom and Dad read me a wonderful story book before sleep.",
          "We can borrow exciting books from our school library."
        ]
      }
    ]
  },
  {
    "id": "pen", "word": "pen", "phonetic": "/pɛn/", "meaning": "名词：笔，钢笔，圆珠笔", "emoji": "🖊️",
    "category": "play", "level": "L1", "role": "new",
    "variants": ["pen", "pens", "pan", "pin"],
    "scenarios": [
      {
        "tag": "情境一 · 笔的外形与墨水",
        "desc": "笔杆颜色、墨水与书写顺畅",
        "sentences": [
          "My favorite gel pen writes in smooth dark blue ink.",
          "The silver fountain pen has a shiny golden metal nib.",
          "A pack of colorful marker pens sits on the craft table."
        ]
      },
      {
        "tag": "情境二 · 握笔书写动作指令",
        "desc": "端正握笔、盖上笔帽与签名",
        "sentences": [
          "Hold the pen properly between your thumb and index finger.",
          "Cap your pen tightly after writing so the ink stays fresh.",
          "Write your full name clearly on the exam paper with a pen."
        ]
      },
      {
        "tag": "情境三 · 课堂文具借还对话",
        "desc": "同学间借笔与练习书法交流",
        "sentences": [
          "May I please borrow your black pen for just a minute?",
          "I ran out of ink; does anyone have an extra spare pen?",
          "Dad signed the important permission slip with his fancy pen."
        ]
      }
    ]
  },
  {
    "id": "bag", "word": "bag", "phonetic": "/bæɡ/", "meaning": "名词：书包，提袋", "emoji": "🎒",
    "category": "play", "level": "L1", "role": "new",
    "variants": ["bag", "bags", "back", "beg"],
    "scenarios": [
      {
        "tag": "情境一 · 书包材质与容量",
        "desc": "拉链、口袋与人体工学双肩包",
        "sentences": [
          "My school backpack has two shoulder straps and many pockets.",
          "A reusable canvas shopping bag hangs behind the kitchen door.",
          "The red travel bag is packed with warm clothes for the trip."
        ]
      },
      {
        "tag": "情境二 · 整理背起动作指令",
        "desc": "拉拉链、背上与存放书包指令",
        "sentences": [
          "Zip up your backpack securely before boarding the bus.",
          "Put your pencil box and lunchbox carefully into the bag.",
          "Hang your heavy school bag on the wooden wall hook."
        ]
      },
      {
        "tag": "情境三 · 出行上学对话交流",
        "desc": "检查上学物品与收拾行囊",
        "sentences": [
          "Did you double check if all your homework is in your bag?",
          "This backpack feels quite heavy with all our new library books.",
          "Can you help mom carry this paper grocery bag into the kitchen?"
        ]
      }
    ]
  },
  {
    "id": "toy", "word": "toy", "phonetic": "/tɔɪ/", "meaning": "名词：玩具", "emoji": "🧸",
    "category": "play", "level": "L1", "role": "new",
    "variants": ["toy", "toys", "boy"],
    "scenarios": [
      {
        "tag": "情境一 · 玩具种类与造型",
        "desc": "毛绒熊、积木与遥控车",
        "sentences": [
          "The soft plush teddy bear is my favorite bedtime toy.",
          "A shiny red toy sports car can race across the living room carpet.",
          "Colorful building block toys let kids create tall towers."
        ]
      },
      {
        "tag": "情境二 · 整理玩具动作指令",
        "desc": "收纳箱整理与分享玩具动作",
        "sentences": [
          "Pack away all your plastic toys into the wooden toy box.",
          "Learn to share your favorite toys happily with playmates.",
          "Do not leave small toy pieces scattered on the bedroom floor."
        ]
      },
      {
        "tag": "情境三 · 商店选购与分享对话",
        "desc": "玩具店挑选与生日礼物交流",
        "sentences": [
          "Which exciting toy would you like to choose for your birthday?",
          "We can build an entire futuristic city with these construction toys.",
          "Santa brought so many delightful surprise toys on Christmas morning."
        ]
      }
    ]
  },
  {
    "id": "car", "word": "car", "phonetic": "/kɑːr/", "meaning": "名词：小汽车，轿车", "emoji": "🚗",
    "category": "play", "level": "L1", "role": "new",
    "variants": ["car", "cars", "card"],
    "scenarios": [
      {
        "tag": "情境一 · 车型外观与颜色",
        "desc": "车轮、车灯与流线型车身",
        "sentences": [
          "Our family sedan is an electric car painted shiny blue.",
          "A speedy red racing car zoomed past on the highway.",
          "The modern car has four rubber wheels and bright headlights."
        ]
      },
      {
        "tag": "情境二 · 安全乘车动作指令",
        "desc": "系安全带与安全上下车",
        "sentences": [
          "Fasten your seatbelt snugly as soon as you enter the car.",
          "Please lock the car doors before we begin driving.",
          "Look both ways carefully before stepping out of the car."
        ]
      },
      {
        "tag": "情境三 · 自驾出行生活对话",
        "desc": "全家自驾游与日常接送",
        "sentences": [
          "Dad is driving our car to the sunny beach this weekend.",
          "Mom drove the car to pick us up right after school ended.",
          "Where did dad park the car in the underground parking lot?"
        ]
      }
    ]
  },
  {
    "id": "bus", "word": "bus", "phonetic": "/bʌs/", "meaning": "名词：公交车，校车", "emoji": "🚌",
    "category": "play", "level": "L1", "role": "new",
    "variants": ["bus", "buses", "buzz", "bath"],
    "scenarios": [
      {
        "tag": "情境一 · 外观造型与车身",
        "desc": "黄色校车、双层巴士与长车身",
        "sentences": [
          "The bright yellow school bus has flashing safety lights.",
          "A double-decker city bus carries passengers across the town.",
          "The electric municipal bus is very quiet and eco-friendly."
        ]
      },
      {
        "tag": "情境二 · 排队上下车动作指令",
        "desc": "文明乘车与扶稳坐好",
        "sentences": [
          "Wait patiently in line at the bus stop for your turn.",
          "Hold onto the handrail tightly when the bus is in motion.",
          "Wave goodbye to the friendly driver when you step off the bus."
        ]
      },
      {
        "tag": "情境三 · 乘车路线对话交流",
        "desc": "看站牌与日常通勤交流",
        "sentences": [
          "Which bus number goes straight to the central science museum?",
          "The wheels on the bus go round and round all through the town.",
          "My school bus arrives promptly at seven-thirty every morning."
        ]
      }
    ]
  },
  {
    "id": "bike", "word": "bike", "phonetic": "/baɪk/", "meaning": "名词：自行车，单车", "emoji": "🚲",
    "category": "play", "level": "L1", "role": "new",
    "variants": ["bike", "bikes", "back"],
    "scenarios": [
      {
        "tag": "情境一 · 车铃车把与车轮",
        "desc": "踏板、车把手与辅助轮",
        "sentences": [
          "My brand-new red bicycle has a loud, clear silver bell.",
          "The mountain bike has sturdy off-road tires for bumpy trails.",
          "A toddler bike is equipped with two safe training wheels."
        ]
      },
      {
        "tag": "情境二 · 骑行安全动作指令",
        "desc": "戴头盔、踩脚踏与刹车指令",
        "sentences": [
          "Always put on your safety helmet before riding your bike.",
          "Pedal steadily and keep your balance on the smooth bike path.",
          "Squeeze the handbrakes gently when you want to stop the bike."
        ]
      },
      {
        "tag": "情境三 · 公园骑行生活对话",
        "desc": "周末骑行与户外健康活动",
        "sentences": [
          "Dad taught me how to ride a two-wheel bike in the park.",
          "Let's go for an enjoyable bike ride along the riverfront trail.",
          "Ring your bike bell to politely alert pedestrians ahead."
        ]
      }
    ]
  },
  {
    "id": "kite", "word": "kite", "phonetic": "/kaɪt/", "meaning": "名词：风筝", "emoji": "🪁",
    "category": "play", "level": "L1", "role": "new",
    "variants": ["kite", "kites", "night"],
    "scenarios": [
      {
        "tag": "情境一 · 图案与长尾巴特征",
        "desc": "蝴蝶风筝、龙风筝与彩带",
        "sentences": [
          "The colorful diamond kite has a long fluttering ribbon tail.",
          "A giant dragon kite looks magnificent soaring among white clouds.",
          "This lightweight nylon kite is shaped like an eagle with open wings."
        ]
      },
      {
        "tag": "情境二 · 迎风奔跑放飞指令",
        "desc": "逆风跑、放线与收线动作",
        "sentences": [
          "Run into the wind quickly and let go of the kite.",
          "Unwind the spool of string gradually so the kite climbs higher.",
          "Pull the string firmly to maneuver your kite against the breeze."
        ]
      },
      {
        "tag": "情境三 · 春游草坪生活对话",
        "desc": "春天踏青与全家放风筝",
        "sentences": [
          "Springtime is the most wonderful season to fly kites on grass.",
          "Look how high our paper kite is flying in the endless blue sky!",
          "Can you help me reel in the kite string as the wind dies down?"
        ]
      }
    ]
  },

  # --- Category 6: Body, Clothes & People (8 words) ---
  {
    "id": "baby", "word": "baby", "phonetic": "/ˈbeɪ.bi/", "meaning": "名词：小婴儿，宝宝", "emoji": "👶",
    "category": "home", "level": "L2", "role": "new",
    "variants": ["baby", "babies"],
    "scenarios": [
      {
        "tag": "情境一 · 可爱面容特征",
        "desc": "胖乎乎小手、明亮眼睛与襁褓",
        "sentences": [
          "The precious baby has chubby pink cheeks and tiny hands.",
          "The newborn infant is wrapped snugly in a warm yellow blanket.",
          "The sweet baby sleeps peacefully inside the wooden cradle."
        ]
      },
      {
        "tag": "情境二 · 抚育照顾动作指令",
        "desc": "轻摇摇篮、喂奶粉与哄睡指令",
        "sentences": [
          "Rock the baby carriage very gently to soothe the crying infant.",
          "Wash your hands thoroughly before holding the delicate newborn baby.",
          "Sing a sweet lullaby softly to help the baby fall asleep."
        ]
      },
      {
        "tag": "情境三 · 亲情互动生活对话",
        "desc": "抓周、学步与亲子温情",
        "sentences": [
          "The cheerful baby giggles and smiles whenever mommy tickles him.",
          "Look! The little baby is taking her very first hesitant steps!",
          "We must speak very quietly because the baby is sleeping soundly."
        ]
      }
    ]
  },
  {
    "id": "shoe", "word": "shoe", "phonetic": "/ʃuː/", "meaning": "名词：鞋子，跑鞋", "emoji": "👟",
    "category": "home", "level": "L1", "role": "review",
    "variants": ["shoe", "shoes", "shoot"],
    "scenarios": [
      {
        "tag": "情境一 · 鞋款材质与鞋底",
        "desc": "运动跑鞋、皮鞋与橡胶鞋底",
        "sentences": [
          "My athletic running shoes are blue with white bouncy soles.",
          "Shiny black dress shoes are polished nicely for the concert.",
          "Warm fleece-lined winter shoes keep little feet cozy in snow."
        ]
      },
      {
        "tag": "情境二 · 穿鞋系鞋带自理动作",
        "desc": "区分左右脚与独立系鞋带",
        "sentences": [
          "Put on your sneakers and tie the shoelaces securely.",
          "Make sure you put the right shoe on your right foot.",
          "Place your muddy shoes neatly upon the entrance shoe rack."
        ]
      },
      {
        "tag": "情境三 · 出门换鞋生活对话",
        "desc": "鞋码大小与户外出行交流",
        "sentences": [
          "Do your new school shoes fit comfortably without pinching toes?",
          "I have grown so fast that my old shoes are already too tight.",
          "Take off your outdoor shoes before walking onto the living room rug."
        ]
      }
    ]
  },
  {
    "id": "hat", "word": "hat", "phonetic": "/hæt/", "meaning": "名词：帽子", "emoji": "🧢",
    "category": "home", "level": "L1", "role": "new",
    "variants": ["hat", "hats", "hot", "cat"],
    "scenarios": [
      {
        "tag": "情境一 · 帽檐造型与保暖",
        "desc": "鸭舌帽、遮阳帽与毛线帽",
        "sentences": [
          "My favorite baseball cap has an adjustable visor.",
          "The knitted wool hat has a fluffy pom-pom on top.",
          "A wide-brimmed straw hat keeps strong sunlight off the face."
        ]
      },
      {
        "tag": "情境二 · 佩戴整理动作指令",
        "desc": "戴好帽子与进屋脱帽礼节",
        "sentences": [
          "Put on your warm woolen hat before going out into snow.",
          "Take off your hat politely when you enter the classroom.",
          "Adjust your cap visor so the bright sun does not blind you."
        ]
      },
      {
        "tag": "情境三 · 出游保暖生活对话",
        "desc": "防风御寒与沙滩出游交流",
        "sentences": [
          "Does this stylish blue hat match my winter jacket nicely?",
          "Hold onto your hat tightly so the sudden gust of wind does not blow it away.",
          "Grandpa always wears a classic brown fedora hat when he travels."
        ]
      }
    ]
  },
  {
    "id": "hand", "word": "hand", "phonetic": "/hænd/", "meaning": "名词：手，小手", "emoji": "✋",
    "category": "home", "level": "L1", "role": "new",
    "variants": ["hand", "hands", "and"],
    "scenarios": [
      {
        "tag": "情境一 · 五指外形与功能",
        "desc": "手掌、十指与灵巧指甲",
        "sentences": [
          "Each human hand has five agile fingers and a palm.",
          "Clean hands have neatly trimmed fingernails and no dirt.",
          "A baby's tiny hand can curl around an adult's finger."
        ]
      },
      {
        "tag": "情境二 · 拍手洗手动作指令",
        "desc": "勤洗手、拍拍手与举手发言",
        "sentences": [
          "Wash your hands thoroughly with antibacterial soap for twenty seconds.",
          "Raise your right hand politely if you wish to ask a question.",
          "Clap your hands cheerfully if you know the lyrics to the song."
        ]
      },
      {
        "tag": "情境三 · 牵手礼貌生活对话",
        "desc": "过马路牵手与手工劳作",
        "sentences": [
          "Hold mom's hand tightly whenever we cross the busy road.",
          "We crafted this colorful Mother's Day card with our own hands.",
          "Give me a helping hand to carry these heavy grocery bags."
        ]
      }
    ]
  },
  {
    "id": "eye", "word": "eye", "phonetic": "/aɪ/", "meaning": "名词：眼睛", "emoji": "👁️",
    "category": "home", "level": "L1", "role": "new",
    "variants": ["eye", "eyes", "I"],
    "scenarios": [
      {
        "tag": "情境一 · 瞳孔虹膜与明亮目光",
        "desc": "清澈双眼、长睫毛与眼色",
        "sentences": [
          "The little girl has sparkling big brown eyes and dark eyelashes.",
          "Cats have unique slit pupils that dilate wide in the dark.",
          "Healthy human eyes can see a spectrum of vibrant colors."
        ]
      },
      {
        "tag": "情境二 · 保护视力动作指令",
        "desc": "眼保健操、闭目养神与眨眼",
        "sentences": [
          "Close your tired eyes and take a brief five-minute rest.",
          "Blink your eyes naturally to keep them moist and comfortable.",
          "Do not rub your delicate eyes with unwashed dirty fingers."
        ]
      },
      {
        "tag": "情境三 · 视力检查生活对话",
        "desc": "看远看近与阅读护眼交流",
        "sentences": [
          "The optometrist doctor examined my vision during the checkup.",
          "Keep proper distance from the screen to protect your precious eyes.",
          "Look far into the distant green trees to relax your eye muscles."
        ]
      }
    ]
  },
  {
    "id": "smile", "word": "smile", "phonetic": "/smaɪl/", "meaning": "名词/动词：微笑，笑容", "emoji": "😊",
    "category": "home", "level": "L1", "role": "new",
    "variants": ["smile", "smiles"],
    "scenarios": [
      {
        "tag": "情境一 · 灿烂笑容特征",
        "desc": "嘴角上扬、酒窝与温暖亲和力",
        "sentences": [
          "A radiant warm smile brightens up her whole face.",
          "The child has cute deep dimples whenever he breaks into a smile.",
          "A friendly welcoming smile makes strangers feel right at home."
        ]
      },
      {
        "tag": "情境二 · 拍照与问候动作指令",
        "desc": "看镜头笑一个与对人微笑",
        "sentences": [
          "Look directly at the camera lens and say cheese with a big smile!",
          "Smile warmly when you greet your teachers and classmates in the morning.",
          "Never forget to smile even when facing challenging tasks."
        ]
      },
      {
        "tag": "情境三 · 治愈情感生活对话",
        "desc": "快乐感染力与关怀对话",
        "sentences": [
          "Your delightful smile always brings joy to everyone around you.",
          "A simple sincere smile can turn someone's gloomy day completely around.",
          "Mom smiled with deep pride when she saw my neat report card."
        ]
      }
    ]
  },
  {
    "id": "heart", "word": "heart", "phonetic": "/hɑːrt/", "meaning": "名词：心，爱心，心脏", "emoji": "❤️",
    "category": "home", "level": "L1", "role": "new",
    "variants": ["heart", "hearts", "hard"],
    "scenarios": [
      {
        "tag": "情境一 · 爱心图形与跳动",
        "desc": "红色爱心形状与强健心跳",
        "sentences": [
          "The shiny red heart-shaped greeting card is drawn with crayons.",
          "A healthy human heart beats steadily day and night.",
          "There is a gold heart locket dangling from her necklace."
        ]
      },
      {
        "tag": "情境二 · 感受心跳动作指令",
        "desc": "摸胸口听心跳与手比爱心",
        "sentences": [
          "Place your palm flat on your left chest to feel your beating heart.",
          "Make a cute heart gesture with your two hands for the photograph.",
          "Listen to your heart rate speed up after running around the track."
        ]
      },
      {
        "tag": "情境三 · 关爱感恩情感对话",
        "desc": "用真心表达爱与感谢",
        "sentences": [
          "I love you with all my whole heart, mom and dad!",
          "Thank you from the bottom of my heart for your generous help.",
          "Regular physical exercise keeps your heart youthful and strong."
        ]
      }
    ]
  },
  {
    "id": "friend", "word": "friend", "phonetic": "/frɛnd/", "meaning": "名词：朋友，伙伴", "emoji": "🤝",
    "category": "home", "level": "L1", "role": "new",
    "variants": ["friend", "friends"],
    "scenarios": [
      {
        "tag": "情境一 · 友善伙伴品质描述",
        "desc": "善良忠诚、形影不离的知己",
        "sentences": [
          "A true friend is always kind, honest, and supportive.",
          "My best friend and I share our hobbies and secrets together.",
          "New classmates can quickly become great lifelong friends."
        ]
      },
      {
        "tag": "情境二 · 握手互助动作指令",
        "desc": "交朋友握手、分享玩具指令",
        "sentences": [
          "Shake hands and introduce your name politely to make a new friend.",
          "Share your favorite colored crayons generously with your friend.",
          "Help your friend stand back up if they trip on the playground."
        ]
      },
      {
        "tag": "情境三 · 友谊长青生活对话",
        "desc": "周末结伴出游与互致问候",
        "sentences": [
          "Would you like to come over to my house this Saturday, my friend?",
          "A friend in need is indeed a trustworthy friend forever.",
          "We sang a cheerful friendship song together at summer camp."
        ]
      }
    ]
  }
]

with open("vocab.json", "w", encoding="utf-8") as f:
    json.dump(DATA, f, ensure_ascii=False, indent=2)

print(f"Generated {len(DATA)} words in vocab.json successfully!")
total_sents = sum(sum(len(sc["sentences"]) for sc in w["scenarios"]) for w in DATA)
print(f"Total sentences across all scenarios: {total_sents}")
