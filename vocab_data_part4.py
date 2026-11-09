# -*- coding: utf-8 -*-
"""Part 4 of Vocabulary Database (Words 121-160): Travel & City (20) + Clothes (20)"""

PART_4 = [
    # --- Travel & City (121-140) ---
    {
        "id": "car", "word": "car", "phonetic": "/kɑːr/", "meaning": "汽車", "emoji": "🚗",
        "category": "Travel", "level": "L1", "role": "review", "variants": ["cars"],
        "storyChapter": 7, "storyChapterTitle": "城市探索", "storyOrder": 1, "storyScene": "紅色小汽車行駛在綠樹成蔭的林蔭大道上",
        "scenarios": [
            {"tag": "難度 1 · 簡單初階", "desc": "基礎入門短句（適合低年級/初學啟蒙）", "sentences": ["A red car."], "translations": ["一輛紅色的車。"]},
            {"tag": "難度 2 · 中等日常", "desc": "生活日常短句（適合中年級/日常口語）", "sentences": ["Dad drives the car home."], "translations": ["爸爸開著汽車回家。"]},
            {"tag": "難度 3 · 進階挑戰", "desc": "拓展進階長句（適合高年級/拓展能力）", "sentences": ["The bright red electric car moves smoothly down the street."], "translations": ["這輛鮮紅色的電動汽車平穩地行駛在街道上。"]}
        ],
        "prompt_data": {
            "num": 121, "word": "car", "phonetic": "/kɑːr/", "meaning": "汽車", "category": "Travel", "filename": "car.gif",
            "action_details": "一輛亮紅色的流線型家庭轎車在陽光下的林蔭道平穩行駛，車輪旋轉，微風吹動樹葉",
            "english_prompt": "A modern glossy red sedan cruising smoothly on a sunlit city avenue lined with green trees, spinning wheels, realistic cinematic lighting, vibrant road reflections, smooth camera tracking.",
            "negative_prompt": "cartoon, low resolution, blurry, car crash, distorted wheels, dull colors, plastic look",
            "tech_specs": "Photorealistic 4K 60fps, 3s loop, cinematic depth of field, warm golden morning light"
        }
    },
    {
        "id": "bike", "word": "bike", "phonetic": "/baɪk/", "meaning": "自行車", "emoji": "🚲",
        "category": "Travel", "level": "L1", "role": "review", "variants": ["bikes", "biking"],
        "storyChapter": 7, "storyChapterTitle": "城市探索", "storyOrder": 2, "storyScene": "微風中戴著安全帽在河濱自行車道騎車",
        "scenarios": [
            {"tag": "難度 1 · 簡單初階", "desc": "基礎入門短句（適合低年級/初學啟蒙）", "sentences": ["Ride my bike."], "translations": ["騎我的腳踏車。"]},
            {"tag": "難度 2 · 中等日常", "desc": "生活日常短句（適合中年級/日常口語）", "sentences": ["I ride my bike to school."], "translations": ["我騎自行車去上學。"]},
            {"tag": "難度 3 · 進階挑戰", "desc": "拓展進階長句（適合高年級/拓展能力）", "sentences": ["He enjoys riding his blue bicycle through the park every afternoon."], "translations": ["他每天下午都喜歡在公園裡騎著藍色自行車兜風。"]}
        ],
        "prompt_data": {
            "num": 122, "word": "bike", "phonetic": "/baɪk/", "meaning": "自行車", "category": "Travel", "filename": "bike.gif",
            "action_details": "一台精緻的藍色休閒單車在公園綠意盎然的小徑上前進，踏板踩動，金屬車鈴微閃金光",
            "english_prompt": "A stylish blue bicycle riding through a sun-dappled park path, spinning spokes, clean asphalt road, green foliage background, soft camera dolly motion, hyper-detailed textures.",
            "negative_prompt": "illustration, flat drawing, unstable wheels, wobbly frame, dark underexposed",
            "tech_specs": "4K realism, 60fps looped motion, macro wheel tracking, gentle afternoon sun flare"
        }
    },
    {
        "id": "train", "word": "train", "phonetic": "/treɪn/", "meaning": "火車", "emoji": "🚆",
        "category": "Travel", "level": "L1", "role": "review", "variants": ["trains"],
        "storyChapter": 7, "storyChapterTitle": "城市探索", "storyOrder": 3, "storyScene": "高速列車在蔚藍天空下沿著現代化鐵軌疾馳",
        "scenarios": [
            {"tag": "難度 1 · 簡單初階", "desc": "基礎入門短句（適合低年級/初學啟蒙）", "sentences": ["The train comes."], "translations": ["火車來了。"]},
            {"tag": "難度 2 · 中等日常", "desc": "生活日常短句（適合中年級/日常口語）", "sentences": ["We took a fast train."], "translations": ["我們搭乘了一班高速火車。"]},
            {"tag": "難度 3 · 進階挑戰", "desc": "拓展進階長句（適合高年級/拓展能力）", "sentences": ["The silver high-speed train glided silently into the brightly lit terminal."], "translations": ["銀色的高速列車悄無聲息地滑進了燈火通明的終點站。"]}
        ],
        "prompt_data": {
            "num": 123, "word": "train", "phonetic": "/treɪn/", "meaning": "火車", "category": "Travel", "filename": "train.gif",
            "action_details": "流線型銀白高鐵在陽光明媚的綠色山谷高架橋上平穩飛馳，窗外風景如光影流轉",
            "english_prompt": "A modern sleek silver bullet train speeding smoothly across a scenic viaduct bridge over green hills, morning sunlight, dynamic motion blur on tracks, crisp crisp details.",
            "negative_prompt": "toy train, cartoon, smoky old train, derailed, jittery framerate",
            "tech_specs": "4K cinematic drone shot, 60fps fluid loop, clean sharp reflections, bright daylight"
        }
    },
    {
        "id": "plane", "word": "plane", "phonetic": "/pleɪn/", "meaning": "飛機", "emoji": "✈️",
        "category": "Travel", "level": "L1", "role": "review", "variants": ["planes", "airplane"],
        "storyChapter": 7, "storyChapterTitle": "城市探索", "storyOrder": 4, "storyScene": "客機在金色朝霞與棉花般的雲層中優雅爬升",
        "scenarios": [
            {"tag": "難度 1 · 簡單初階", "desc": "基礎入門短句（適合低年級/初學啟蒙）", "sentences": ["A big plane."], "translations": ["一架大飛機。"]},
            {"tag": "難度 2 · 中等日常", "desc": "生活日常短句（適合中年級/日常口語）", "sentences": ["The plane flies very high."], "translations": ["飛機飛得非常高。"]},
            {"tag": "難度 3 · 進階挑戰", "desc": "拓展進階長句（適合高年級/拓展能力）", "sentences": ["The passenger airplane climbed gracefully through golden clouds into the blue sky."], "translations": ["這架客機優雅地穿越金色雲層，直上藍天。"]}
        ],
        "prompt_data": {
            "num": 124, "word": "plane", "phonetic": "/pleɪn/", "meaning": "飛機", "category": "Travel", "filename": "plane.gif",
            "action_details": "巨大的白藍相間商用客機在金光閃耀的雲海之上翱翔，機翼尾部劃出輕柔航跡",
            "english_prompt": "A grand commercial airliner soaring majestically above a sea of fluffy golden sunset clouds, glistening wingtips, crystal clear atmospheric perspective, slow aerial pan.",
            "negative_prompt": "crash, military jet, low poly, noisy render, plastic toy plane",
            "tech_specs": "8K aerial cinematic view, 60fps loop, volumetric clouds, golden hour lighting"
        }
    },
    {
        "id": "ship", "word": "ship", "phonetic": "/ʃɪp/", "meaning": "輪船", "emoji": "🚢",
        "category": "Travel", "level": "L1", "role": "review", "variants": ["ships"],
        "storyChapter": 7, "storyChapterTitle": "城市探索", "storyOrder": 5, "storyScene": "巨型白色遊輪在深藍色大海上平穩航行",
        "scenarios": [
            {"tag": "難度 1 · 簡單初階", "desc": "基礎入門短句（適合低年級/初學啟蒙）", "sentences": ["A large ship."], "translations": ["一艘大輪船。"]},
            {"tag": "難度 2 · 中等日常", "desc": "生活日常短句（適合中年級/日常口語）", "sentences": ["The ship sails on the sea."], "translations": ["輪船在海面上航行。"]},
            {"tag": "難度 3 · 進階挑戰", "desc": "拓展進階長句（適合高年級/拓展能力）", "sentences": ["The luxury cruise ship sailed smoothly across the calm turquoise ocean."], "translations": ["豪華遊輪在平靜的青綠色大海上平穩航行。"]}
        ],
        "prompt_data": {
            "num": 125, "word": "ship", "phonetic": "/ʃɪp/", "meaning": "輪船", "category": "Travel", "filename": "ship.gif",
            "action_details": "龐大優雅的白色郵輪劃開碧藍清澈的海面，浪花在船艏翻滾跳躍，海鷗伴飛",
            "english_prompt": "A majestic white luxury cruise ship navigating through sparkling deep blue ocean waves, splashing sea foam at the bow, seagulls gliding overhead, breathtaking maritime panorama.",
            "negative_prompt": "sinking, pirate ship, rough storm, dark murky water, oversaturated",
            "tech_specs": "4K cinematic drone footage, 60fps realistic water physics, sunny tropical day"
        }
    },
    {
        "id": "boat", "word": "boat", "phonetic": "/boʊt/", "meaning": "小船", "emoji": "⛵",
        "category": "Travel", "level": "L1", "role": "review", "variants": ["boats"],
        "storyChapter": 7, "storyChapterTitle": "城市探索", "storyOrder": 6, "storyScene": "一艘木質小帆船在靜謐的翡翠湖心輕輕搖曳",
        "scenarios": [
            {"tag": "難度 1 · 簡單初階", "desc": "基礎入門短句（適合低年級/初學啟蒙）", "sentences": ["A small boat."], "translations": ["一艘小船。"]},
            {"tag": "難度 2 · 中等日常", "desc": "生活日常短句（適合中年級/日常口語）", "sentences": ["We row the boat together."], "translations": ["我們一起划這艘小船。"]},
            {"tag": "難度 3 · 進階挑戰", "desc": "拓展進階長句（適合高年級/拓展能力）", "sentences": ["A wooden rowboat floats peacefully on the misty lake surrounded by green pine trees."], "translations": ["一艘木製划艇在被綠色松樹環繞的薄霧湖面上寧靜地漂浮著。"]}
        ],
        "prompt_data": {
            "num": 126, "word": "boat", "phonetic": "/boʊt/", "meaning": "小船", "category": "Travel", "filename": "boat.gif",
            "action_details": "典雅木質小舟停泊在清可見底的湖邊，湖面波光粼粼，木槳輕盪帶起漣漪",
            "english_prompt": "A classic polished wooden rowboat gently bobbing on the crystal-clear reflective water of an alpine lake, gentle ripples, morning mist, photorealistic nature scene.",
            "negative_prompt": "rough sea, plastic speedboat, dirty water, blurry textures, artificial lighting",
            "tech_specs": "4K ultra HD, 60fps gentle seamless loop, ray-traced water reflections"
        }
    },
    {
        "id": "road", "word": "road", "phonetic": "/roʊd/", "meaning": "公路", "emoji": "🛣️",
        "category": "Travel", "level": "L1", "role": "review", "variants": ["roads"],
        "storyChapter": 7, "storyChapterTitle": "城市探索", "storyOrder": 7, "storyScene": "寬闊平整的高速公路伸向遠方巍峨的雪山",
        "scenarios": [
            {"tag": "難度 1 · 簡單初階", "desc": "基礎入門短句（適合低年級/初學啟蒙）", "sentences": ["Look at the road."], "translations": ["看看這條馬路。"]},
            {"tag": "難度 2 · 中等日常", "desc": "生活日常短句（適合中年級/日常口語）", "sentences": ["The road is very wide."], "translations": ["這條公路非常寬闊。"]},
            {"tag": "難度 3 · 進階挑戰", "desc": "拓展進階長句（適合高年級/拓展能力）", "sentences": ["A long straight scenic highway stretches toward majestic mountains under the blue sky."], "translations": ["一條筆直風景優美的大道在蔚藍天空下延伸至雄偉的群山。"]}
        ],
        "prompt_data": {
            "num": 127, "word": "road", "phonetic": "/roʊd/", "meaning": "公路", "category": "Travel", "filename": "road.gif",
            "action_details": "平整乾淨的黑色柏油公路帶著鮮黃色標線，筆直延伸通往雪山地平線，鏡頭向前推進",
            "english_prompt": "Cinematic forward driving shot along a smooth asphalt open road stretching to scenic snowcapped mountains, yellow center lines, clear horizon, crisp realistic atmosphere.",
            "negative_prompt": "potholes, traffic jam, muddy road, dark foggy, low resolution",
            "tech_specs": "4K 60fps smooth dolly forward, natural morning daylight, expansive landscape"
        }
    },
    {
        "id": "street", "word": "street", "phonetic": "/striːt/", "meaning": "街道", "emoji": "🏘️",
        "category": "Travel", "level": "L1", "role": "review", "variants": ["streets"],
        "storyChapter": 7, "storyChapterTitle": "城市探索", "storyOrder": 8, "storyScene": "鋪著紅磚的歐風小鎮街道旁開滿了色彩繽紛的花朵",
        "scenarios": [
            {"tag": "難度 1 · 簡單初階", "desc": "基礎入門短句（適合低年級/初學啟蒙）", "sentences": ["Cross the street."], "translations": ["過馬路。"]},
            {"tag": "難度 2 · 中等日常", "desc": "生活日常短句（適合中年級/日常口語）", "sentences": ["Children play on the street."], "translations": ["孩子們在街道上玩耍。"]},
            {"tag": "難度 3 · 進階挑戰", "desc": "拓展進階長句（適合高年級/拓展能力）", "sentences": ["Cobblestone streets are lined with cozy bakeries and blooming flower boxes."], "translations": ["鵝卵石鋪成的街道兩旁排列著溫馨的烘焙店與盛開的花箱。"]}
        ],
        "prompt_data": {
            "num": 128, "word": "street", "phonetic": "/striːt/", "meaning": "街道", "category": "Travel", "filename": "street.gif",
            "action_details": "陽光灑在古樸鵝卵石街道上，兩旁是溫暖的小咖啡館與木質櫥窗，綠葉光斑輕輕搖動",
            "english_prompt": "A charming European cobblestone street bathed in warm afternoon sunshine, boutique storefronts, vibrant flower baskets, gentle breeze rustling leaves, cozy atmosphere.",
            "negative_prompt": "dirty litter, abandoned cars, rainy storm, depressing colors, CGI blur",
            "tech_specs": "Photorealistic 4K, 60fps ambient loop, warm lighting, depth of field"
        }
    },
    {
        "id": "park", "word": "park", "phonetic": "/pɑːrk/", "meaning": "公園", "emoji": "🌳",
        "category": "Travel", "level": "L1", "role": "review", "variants": ["parks"],
        "storyChapter": 7, "storyChapterTitle": "城市探索", "storyOrder": 9, "storyScene": "城市公園中綠草如茵，噴泉散發出微小彩虹光芒",
        "scenarios": [
            {"tag": "難度 1 · 簡單初階", "desc": "基礎入門短句（適合低年級/初學啟蒙）", "sentences": ["Run in the park."], "translations": ["在公園裡奔跑。"]},
            {"tag": "難度 2 · 中等日常", "desc": "生活日常短句（適合中年級/日常口語）", "sentences": ["We had a picnic in the park."], "translations": ["我們在公園裡舉行了野餐。"]},
            {"tag": "難度 3 · 進階挑戰", "desc": "拓展進階長句（適合高年級/拓展能力）", "sentences": ["The public park features sprawling green lawns, a sparkling fountain, and shaded walking trails."], "translations": ["這座公共公園擁有廣闊的綠草坪、一座波光粼粼的噴泉與綠蔭步道。"]}
        ],
        "prompt_data": {
            "num": 129, "word": "park", "phonetic": "/pɑːrk/", "meaning": "公園", "category": "Travel", "filename": "park.gif",
            "action_details": "開闊的城市綠洲公園，噴泉噴灑著清涼水霧，綠油油的草坪與茂密大樹隨微風輕晃",
            "english_prompt": "A lush, serene city park with manicured emerald lawns, a graceful tiered water fountain, willow trees swaying gently, dappled golden sunlight, family-friendly vibrant scenery.",
            "negative_prompt": "trash, dying grass, crowded messy, gloomy weather, fake 3D look",
            "tech_specs": "4K 60fps tranquil loop, realistic water misting, rich foliage detail"
        }
    },
    {
        "id": "shop", "word": "shop", "phonetic": "/ʃɑːp/", "meaning": "商店", "emoji": "🏪",
        "category": "Travel", "level": "L1", "role": "review", "variants": ["shops", "shopping"],
        "storyChapter": 7, "storyChapterTitle": "城市探索", "storyOrder": 10, "storyScene": "明亮溫暖的烘焙麵包小店，櫥窗裡擺滿剛出爐的金黃可頌",
        "scenarios": [
            {"tag": "難度 1 · 簡單初階", "desc": "基礎入門短句（適合低年級/初學啟蒙）", "sentences": ["Go to the shop."], "translations": ["去商店。"]},
            {"tag": "難度 2 · 中等日常", "desc": "生活日常短句（適合中年級/日常口語）", "sentences": ["Mom buys fruit at the shop."], "translations": ["媽媽在商店買水果。"]},
            {"tag": "難度 3 · 進階挑戰", "desc": "拓展進階長句（適合高年級/拓展能力）", "sentences": ["The sweet neighborhood bakery shop display is filled with warm golden pastries."], "translations": ["街角這家甜美烘焙店的櫥窗裡擺滿了溫熱的金黃糕點。"]}
        ],
        "prompt_data": {
            "num": 130, "word": "shop", "phonetic": "/ʃɑːp/", "meaning": "商店", "category": "Travel", "filename": "shop.gif",
            "action_details": "街道旁一家溫馨明亮的精品店櫥窗，掛著木質招牌，玻璃擦拭得乾淨透亮，店內透出溫暖燈光",
            "english_prompt": "A warm, inviting boutique artisan shop storefront at twilight, gleaming display windows showing handmade goods, glowing warm yellow pendant lamps, cozy sidewalk view.",
            "negative_prompt": "cluttered, closed shutter, broken glass, dark eerie, anime illustration",
            "tech_specs": "4K cinematic still-motion loop, warm 2700K lighting, shallow depth of field"
        }
    },
    {
        "id": "city", "word": "city", "phonetic": "/ˈsɪt.i/", "meaning": "城市", "emoji": "🏙️",
        "category": "Travel", "level": "L1", "role": "review", "variants": ["cities"],
        "storyChapter": 7, "storyChapterTitle": "城市探索", "storyOrder": 11, "storyScene": "天際線聳立的摩天大樓在蔚藍天空下反射璀璨光芒",
        "scenarios": [
            {"tag": "難度 1 · 簡單初階", "desc": "基礎入門短句（適合低年級/初學啟蒙）", "sentences": ["A big city."], "translations": ["一座大城市。"]},
            {"tag": "難度 2 · 中等日常", "desc": "生活日常短句（適合中年級/日常口語）", "sentences": ["I love this busy city."], "translations": ["我喜歡這座繁忙的城市。"]},
            {"tag": "難度 3 · 進階挑戰", "desc": "拓展進階長句（適合高年級/拓展能力）", "sentences": ["The modern city skyline glistens proudly under the bright morning sunshine."], "translations": ["現代化的大都市天際線在燦爛的晨光中閃耀。"]}
        ],
        "prompt_data": {
            "num": 131, "word": "city", "phonetic": "/ˈsɪt.i/", "meaning": "城市", "category": "Travel", "filename": "city.gif",
            "action_details": "壯觀的現代化都市全景，玻璃帷幕摩天大樓倒映藍天白雲，下方車流平穩如流動的線條",
            "english_prompt": "A breathtaking high-angle view of a modern thriving metropolis skyline, glittering glass skyscrapers, clean streets, blue sky with wispy clouds, realistic drone motion.",
            "negative_prompt": "foggy smog, ruins, apocalyptic, gloomy, cartoon render",
            "tech_specs": "4K UHD drone sweep, 60fps seamless loop, ultra-crisp architectural lines"
        }
    },
    {
        "id": "bridge", "word": "bridge", "phonetic": "/brɪdʒ/", "meaning": "橋梁", "emoji": "🌉",
        "category": "Travel", "level": "L1", "role": "review", "variants": ["bridges"],
        "storyChapter": 7, "storyChapterTitle": "城市探索", "storyOrder": 12, "storyScene": "宏偉的紅色懸索大橋橫跨波濤起伏的海灣",
        "scenarios": [
            {"tag": "難度 1 · 簡單初階", "desc": "基礎入門短句（適合低年級/初學啟蒙）", "sentences": ["Over the bridge."], "translations": ["過這座橋。"]},
            {"tag": "難度 2 · 中等日常", "desc": "生活日常短句（適合中年級/日常口語）", "sentences": ["The cars cross the long bridge."], "translations": ["汽車穿過長長的橋樑。"]},
            {"tag": "難度 3 · 進階挑戰", "desc": "拓展進階長句（適合高年級/拓展能力）", "sentences": ["The iconic suspension bridge spans majestically across the sparkling harbor water."], "translations": ["這座標誌性的懸索吊橋雄偉地橫跨在波光粼粼的海港之上。"]}
        ],
        "prompt_data": {
            "num": 132, "word": "bridge", "phonetic": "/brɪdʒ/", "meaning": "橋梁", "category": "Travel", "filename": "bridge.gif",
            "action_details": "壯麗的紅色大懸索橋橫越藍色海灣，鋼纜線條清晰，橋下波浪翻動，水光粼粼",
            "english_prompt": "A majestic suspension bridge spanning over shimmering blue ocean bay water, strong steel cables, sunny horizon, slow majestic cinematic pan, hyper-detailed structure.",
            "negative_prompt": "broken bridge, heavy fog, dark night, cartoon, low polygon",
            "tech_specs": "4K cinematic drone camera, 60fps loop, natural sunlight, sharp water reflections"
        }
    },
    {
        "id": "station", "word": "station", "phonetic": "/ˈsteɪ.ʃən/", "meaning": "車站", "emoji": "🚉",
        "category": "Travel", "level": "L1", "role": "review", "variants": ["stations"],
        "storyChapter": 7, "storyChapterTitle": "城市探索", "storyOrder": 13, "storyScene": "寬敞明亮的火車月台上，人們井然有序地等候列車進站",
        "scenarios": [
            {"tag": "難度 1 · 簡單初階", "desc": "基礎入門短句（適合低年級/初學啟蒙）", "sentences": ["Wait at the station."], "translations": ["在車站等候。"]},
            {"tag": "難度 2 · 中等日常", "desc": "生活日常短句（適合中年級/日常口語）", "sentences": ["We met grandma at the station."], "translations": ["我們在車站迎接祖母。"]},
            {"tag": "難度 3 · 進階挑戰", "desc": "拓展進階長句（適合高年級/拓展能力）", "sentences": ["Commuters wait patiently along the clean railway platform as the morning train arrives."], "translations": ["清晨列車抵達時，通勤乘客在乾淨的鐵路月台上耐心地等待著。"]}
        ],
        "prompt_data": {
            "num": 133, "word": "station", "phonetic": "/ˈsteɪ.ʃən/", "meaning": "車站", "category": "Travel", "filename": "station.gif",
            "action_details": "玻璃與鋼骨結構的現代化車站大廳，自然光從天窗傾瀉而下，電子時刻表整潔明亮",
            "english_prompt": "A grand, modern railway station platform with sleek glass roof arches, sunbeams streaming through glass panels, polished floors, calm commuters waiting orderly.",
            "negative_prompt": "dirty subway, graffiti, creepy empty station, blur, low quality",
            "tech_specs": "4K architectural video loop, 60fps, natural volumetric sun rays, symmetrical framing"
        }
    },
    {
        "id": "truck", "word": "truck", "phonetic": "/trʌk/", "meaning": "卡車", "emoji": "🚚",
        "category": "Travel", "level": "L1", "role": "review", "variants": ["trucks"],
        "storyChapter": 7, "storyChapterTitle": "城市探索", "storyOrder": 14, "storyScene": "藍色貨運大卡車在寬闊公路上有力地向前行駛",
        "scenarios": [
            {"tag": "難度 1 · 簡單初階", "desc": "基礎入門短句（適合低年級/初學啟蒙）", "sentences": ["A big truck."], "translations": ["一輛大卡車。"]},
            {"tag": "難度 2 · 中等日常", "desc": "生活日常短句（適合中年級/日常口語）", "sentences": ["The delivery truck brought packages."], "translations": ["送貨卡車送來了包裹。"]},
            {"tag": "難度 3 · 進階挑戰", "desc": "拓展進階長句（適合高年級/拓展能力）", "sentences": ["The heavy blue freight truck transports supplies safely across the mountain pass."], "translations": ["這輛重型藍色貨運卡車安全地將物資運過山隘。"]}
        ],
        "prompt_data": {
            "num": 134, "word": "truck", "phonetic": "/trʌk/", "meaning": "卡車", "category": "Travel", "filename": "truck.gif",
            "action_details": "一輛光潔的藍色大型物流卡車在寬暢的洲際公路上平穩開動，輪胎有力轉動，車身鍍鉻裝飾反光",
            "english_prompt": "A modern clean blue freight truck driving steadily down an open highway, chrome details reflecting morning sunshine, rotating wheels, clear skies, realistic road dynamics.",
            "negative_prompt": "rusty broken truck, exhaust smoke, accident, messy drawing, plastic model",
            "tech_specs": "Photorealistic 4K, 60fps tracking side view, sharp tire texture, sunny daylight"
        }
    },
    {
        "id": "taxi", "word": "taxi", "phonetic": "/ˈtæk.si/", "meaning": "計程車", "emoji": "🚕",
        "category": "Travel", "level": "L1", "role": "review", "variants": ["taxis"],
        "storyChapter": 7, "storyChapterTitle": "城市探索", "storyOrder": 15, "storyScene": "鮮黃色計程車在熱鬧的市中心緩緩停靠在路旁",
        "scenarios": [
            {"tag": "難度 1 · 簡單初階", "desc": "基礎入門短句（適合低年級/初學啟蒙）", "sentences": ["Take a taxi."], "translations": ["搭計程車。"]},
            {"tag": "難度 2 · 中等日常", "desc": "生活日常短句（適合中年級/日常口語）", "sentences": ["The yellow taxi stops here."], "translations": ["黃色計程車停在這裡。"]},
            {"tag": "難度 3 · 進階挑戰", "desc": "拓展進階長句（適合高年級/拓展能力）", "sentences": ["A cheerful yellow cab navigates through downtown traffic and pulls up to the hotel curb."], "translations": ["一輛亮黃色計程車穿過市中心車流，穩穩地停在飯店路邊。"]}
        ],
        "prompt_data": {
            "num": 135, "word": "taxi", "phonetic": "/ˈtæk.si/", "meaning": "計程車", "category": "Travel", "filename": "taxi.gif",
            "action_details": "經典亮黃色城市計程車頂燈閃亮，在整潔的城市大道旁平穩靠邊減速停下",
            "english_prompt": "A vibrant yellow city taxi with lit rooftop sign cruising smoothly along a lively city boulevard and softly stopping by the curb, realistic urban reflections on paintwork.",
            "negative_prompt": "dented taxi, dirty cab, dark night rain, cartoon drawing, distorted proportions",
            "tech_specs": "4K 60fps street tracking shot, realistic metallic finish, bright daytime lighting"
        }
    },
    {
        "id": "zoo", "word": "zoo", "phonetic": "/zuː/", "meaning": "動物園", "emoji": "🦁",
        "category": "Travel", "level": "L1", "role": "review", "variants": ["zoos"],
        "storyChapter": 7, "storyChapterTitle": "城市探索", "storyOrder": 16, "storyScene": "充滿綠意生態的動物園園區，長頸鹿在林間自在漫步",
        "scenarios": [
            {"tag": "難度 1 · 簡單初階", "desc": "基礎入門短句（適合低年級/初學啟蒙）", "sentences": ["Visit the zoo."], "translations": ["參觀動物園。"]},
            {"tag": "難度 2 · 中等日常", "desc": "生活日常短句（適合中年級/日常口語）", "sentences": ["We saw funny monkeys at the zoo."], "translations": ["我們在動物園看到有趣的小猴子。"]},
            {"tag": "難度 3 · 進階挑戰", "desc": "拓展進階長句（適合高年級/拓展能力）", "sentences": ["Families spend a wonderful sunny weekend exploring the lush safari park and zoo."], "translations": ["家庭在陽光普照的週末一起探索這座綠意盎然的野生動物園。"]}
        ],
        "prompt_data": {
            "num": 136, "word": "zoo", "phonetic": "/zuː/", "meaning": "動物園", "category": "Travel", "filename": "zoo.gif",
            "action_details": "風景如畫的生態動物園，綠樹成蔭的遊步道邊，長頸鹿在開闊圍欄裡悠閒啃食高處樹葉",
            "english_prompt": "A beautiful lush botanical zoo habitat with tall green acacia trees, a graceful giraffe gently browsing leaves in the distance, clean visitor walkway, warm sunny ambience.",
            "negative_prompt": "sad caged animal, bars, barren concrete, poor lighting, cartoonish",
            "tech_specs": "4K nature documentary style, 60fps gentle loop, soft sunlight through leaves"
        }
    },
    {
        "id": "museum", "word": "museum", "phonetic": "/mjuːˈziː.əm/", "meaning": "博物館", "emoji": "🏛️",
        "category": "Travel", "level": "L1", "role": "review", "variants": ["museums"],
        "storyChapter": 7, "storyChapterTitle": "城市探索", "storyOrder": 17, "storyScene": "氣勢恢宏的古典石柱博物館大門，陽光灑滿寬闊的石階",
        "scenarios": [
            {"tag": "難度 1 · 簡單初階", "desc": "基礎入門短句（適合低年級/初學啟蒙）", "sentences": ["In the museum."], "translations": ["在博物館裡。"]},
            {"tag": "難度 2 · 中等日常", "desc": "生活日常短句（適合中年級/日常口語）", "sentences": ["The science museum is exciting."], "translations": ["這座科學博物館令人興奮。"]},
            {"tag": "難度 3 · 進階挑戰", "desc": "拓展進階長句（適合高年級/拓展能力）", "sentences": ["Visitors admire historical treasures inside the grand neoclassical art museum."], "translations": ["遊客在宏偉的新古典主義藝術博物館內欣賞歷史瑰寶。"]}
        ],
        "prompt_data": {
            "num": 137, "word": "museum", "phonetic": "/mjuːˈziː.əm/", "meaning": "博物館", "category": "Travel", "filename": "museum.gif",
            "action_details": "莊嚴古典的白色大理石博物館外觀，石雕廊柱在陽光下投下優雅陰影，人們信步登上石階",
            "english_prompt": "A majestic classical museum building with tall grand marble columns, wide stone stairs, clear blue sky, visitors walking peacefully, warm morning architectural glow.",
            "negative_prompt": "creepy museum, dilapidated building, dark shadows, flat painting, low resolution",
            "tech_specs": "4K wide-angle architectural pan, 60fps smooth loop, crisp marble texture"
        }
    },
    {
        "id": "traffic", "word": "traffic", "phonetic": "/ˈtræf.ɪk/", "meaning": "交通", "emoji": "🚦",
        "category": "Travel", "level": "L1", "role": "review", "variants": [],
        "storyChapter": 7, "storyChapterTitle": "城市探索", "storyOrder": 18, "storyScene": "十字路口的交通號誌燈從紅燈亮麗轉為綠燈，車流井然前行",
        "scenarios": [
            {"tag": "難度 1 · 簡單初階", "desc": "基礎入門短句（適合低年級/初學啟蒙）", "sentences": ["Follow the traffic lights."], "translations": ["遵守交通號誌。"]},
            {"tag": "難度 2 · 中等日常", "desc": "生活日常短句（適合中年級/日常口語）", "sentences": ["The morning traffic moves steadily."], "translations": ["早晨的交通平穩流暢。"]},
            {"tag": "難度 3 · 進階挑戰", "desc": "拓展進階長句（適合高年級/拓展能力）", "sentences": ["Drivers and pedestrians obey the traffic signals carefully at the bustling city crossroad."], "translations": ["駕駛與行人在繁忙的城市十字路口仔細遵守交通號誌。"]}
        ],
        "prompt_data": {
            "num": 138, "word": "traffic", "phonetic": "/ˈtræf.ɪk/", "meaning": "交通", "category": "Travel", "filename": "traffic.gif",
            "action_details": "十字路口整潔的現代交通號誌燈清晰亮起綠燈，斑馬線前車輛有序起步前行",
            "english_prompt": "A modern city intersection showing a clear traffic light switching smoothly to bright emerald green, well-ordered cars beginning to roll smoothly on asphalt, clean urban scene.",
            "negative_prompt": "chaotic gridlock, accident, reckless driving, dark polluted sky, comic art",
            "tech_specs": "4K cinematic street photography, 60fps seamless loop, realistic LED glow"
        }
    },
    {
        "id": "wheel", "word": "wheel", "phonetic": "/wiːl/", "meaning": "輪子", "emoji": "🎡",
        "category": "Travel", "level": "L1", "role": "review", "variants": ["wheels"],
        "storyChapter": 7, "storyChapterTitle": "城市探索", "storyOrder": 19, "storyScene": "精緻的金屬輪框在地面上高速而優雅地平穩旋轉",
        "scenarios": [
            {"tag": "難度 1 · 簡單初階", "desc": "基礎入門短句（適合低年級/初學啟蒙）", "sentences": ["A round wheel."], "translations": ["一個圓輪子。"]},
            {"tag": "難度 2 · 中等日常", "desc": "生活日常短句（適合中年級/日常口語）", "sentences": ["The wheels turn very fast."], "translations": ["輪子轉動得非常快。"]},
            {"tag": "難度 3 · 進階挑戰", "desc": "拓展進階長句（適合高年級/拓展能力）", "sentences": ["Four shiny alloy wheels keep the vehicle balanced and moving smoothly forward."], "translations": ["四個亮麗的合金輪圈保持車輛平衡並平穩向前行駛。"]}
        ],
        "prompt_data": {
            "num": 139, "word": "wheel", "phonetic": "/wiːl/", "meaning": "輪子", "category": "Travel", "filename": "wheel.gif",
            "action_details": "特寫精緻亮麗的合金汽車輪框與橡膠輪胎在乾淨路面上順暢旋轉，胎紋清晰，金屬反光",
            "english_prompt": "Close-up macro slow-motion shot of a sleek polished alloy car wheel spinning smoothly over clean asphalt, crisp rubber tire treads, metallic reflections, motion blur on spokes.",
            "negative_prompt": "flat tire, dirty mud, rusty rim, cartoonish, wobble",
            "tech_specs": "4K high-speed camera slow-motion, 60fps loop, sharp focus tracking"
        }
    },
    {
        "id": "airport", "word": "airport", "phonetic": "/ˈer.pɔːrt/", "meaning": "機場", "emoji": "🛫",
        "category": "Travel", "level": "L1", "role": "review", "variants": ["airports"],
        "storyChapter": 7, "storyChapterTitle": "城市探索", "storyOrder": 20, "storyScene": "現代國際機場的巨大落地窗前，飛機在停機坪上準備啟程",
        "scenarios": [
            {"tag": "難度 1 · 簡單初階", "desc": "基礎入門短句（適合低年級/初學啟蒙）", "sentences": ["At the airport."], "translations": ["在機場。"]},
            {"tag": "難度 2 · 中等日常", "desc": "生活日常短句（適合中年級/日常口語）", "sentences": ["We arrived at the airport early."], "translations": ["我們很早抵達了機場。"]},
            {"tag": "難度 3 · 進階挑戰", "desc": "拓展進階長句（適合高年級/拓展能力）", "sentences": ["Through the airport's glass terminal, passengers watch international airliners preparing for departure."], "translations": ["透過機場航廈的玻璃幕牆，旅客注視著國際客機準備起飛。"]}
        ],
        "prompt_data": {
            "num": 140, "word": "airport", "phonetic": "/ˈer.pɔːrt/", "meaning": "機場", "category": "Travel", "filename": "airport.gif",
            "action_details": "寬闊明亮的國際機場航站落地玻璃窗，向外眺望停機坪上的白色客機與地勤行李車，視野遼闊",
            "english_prompt": "Sprawling modern airport terminal interior with towering panoramic glass windows overlooking parked commercial jets on tarmac, polished terrazzo reflection, golden morning light.",
            "negative_prompt": "abandoned airport, dark runway, crash, messy illustration, blurry",
            "tech_specs": "4K cinematic interior-to-exterior view, 60fps loop, architectural clarity"
        }
    },

    # --- Clothes (141-160) ---
    {
        "id": "hat", "word": "hat", "phonetic": "/hæt/", "meaning": "帽子", "emoji": "👒",
        "category": "Clothes", "level": "L1", "role": "review", "variants": ["hats"],
        "storyChapter": 8, "storyChapterTitle": "日常服飾", "storyOrder": 1, "storyScene": "一頂優雅的編織草帽在海風中繫著飄逸的米色絲帶",
        "scenarios": [
            {"tag": "難度 1 · 簡單初階", "desc": "基礎入門短句（適合低年級/初學啟蒙）", "sentences": ["A cute hat."], "translations": ["一頂可愛的帽子。"]},
            {"tag": "難度 2 · 中等日常", "desc": "生活日常短句（適合中年級/日常口語）", "sentences": ["Wear a hat in the sun."], "translations": ["在陽光下戴帽子。"]},
            {"tag": "難度 3 · 進階挑戰", "desc": "拓展進階長句（適合高年級/拓展能力）", "sentences": ["She wears a woven straw sun hat with a cream ribbon on sunny beach days."], "translations": ["在晴朗的海灘日子裡，她戴著一頂帶有米色緞帶的編織草帽。"]}
        ],
        "prompt_data": {
            "num": 141, "word": "hat", "phonetic": "/hæt/", "meaning": "帽子", "category": "Clothes", "filename": "hat.gif",
            "action_details": "精美細膩的米色手工編織草帽放在木桌上，微風輕輕吹拂帽簷上的白色絲帶，陽光溫柔灑落",
            "english_prompt": "A beautiful handmade woven straw sun hat resting on a rustic wooden table, delicate white ribbon fluttering gently in a warm sea breeze, soft golden sunlight, macro weave texture.",
            "negative_prompt": "crushed hat, dirty fabric, cartoon drawing, overly synthetic, flat shading",
            "tech_specs": "4K macro still life, 60fps gentle motion loop, natural shallow depth of field"
        }
    },
    {
        "id": "coat", "word": "coat", "phonetic": "/koʊt/", "meaning": "大衣", "emoji": "🧥",
        "category": "Clothes", "level": "L1", "role": "review", "variants": ["coats"],
        "storyChapter": 8, "storyChapterTitle": "日常服飾", "storyOrder": 2, "storyScene": "溫暖厚實的羊毛呢大衣掛在木質衣架上，散發溫暖氣息",
        "scenarios": [
            {"tag": "難度 1 · 簡單初階", "desc": "基礎入門短句（適合低年級/初學啟蒙）", "sentences": ["Put on the coat."], "translations": ["穿上大衣。"]},
            {"tag": "難度 2 · 中等日常", "desc": "生活日常短句（適合中年級/日常口語）", "sentences": ["This winter coat is warm."], "translations": ["這件冬季大衣很保暖。"]},
            {"tag": "難度 3 · 進階挑戰", "desc": "拓展進階長句（適合高年級/拓展能力）", "sentences": ["The cozy camel wool coat keeps you comfortably warm against the chilly autumn wind."], "translations": ["舒適的駝色羊毛大衣能為你抵禦寒冷的秋風並保持溫暖。"]}
        ],
        "prompt_data": {
            "num": 142, "word": "coat", "phonetic": "/koʊt/", "meaning": "大衣", "category": "Clothes", "filename": "coat.gif",
            "action_details": "一件優雅經典的駝色羊毛長大衣整齊掛在胡桃木衣架上，羊毛質地柔軟細膩，扣環金屬質感高級",
            "english_prompt": "A high-end camel wool trench coat hanging neatly on a wooden hanger against a clean minimalist studio wall, luxurious textile texture, soft ambient indoor lighting.",
            "negative_prompt": "wrinkled coat, stained fabric, cheap plastic look, cartoonish render",
            "tech_specs": "4K commercial textile macro, 60fps subtle breathing loop, hyper-realistic cloth weave"
        }
    },
    {
        "id": "shoe", "word": "shoe", "phonetic": "/ʃuː/", "meaning": "鞋子", "emoji": "👟",
        "category": "Clothes", "level": "L1", "role": "review", "variants": ["shoes"],
        "storyChapter": 8, "storyChapterTitle": "日常服飾", "storyOrder": 3, "storyScene": "乾淨清爽的白球鞋繫著整齊鞋帶，輕快踩在木地板上",
        "scenarios": [
            {"tag": "難度 1 · 簡單初階", "desc": "基礎入門短句（適合低年級/初學啟蒙）", "sentences": ["Tie your shoe."], "translations": ["綁好你的鞋帶。"]},
            {"tag": "難度 2 · 中等日常", "desc": "生活日常短句（適合中年級/日常口語）", "sentences": ["These running shoes fit well."], "translations": ["這雙慢跑鞋很合腳。"]},
            {"tag": "難度 3 · 進階挑戰", "desc": "拓展進階長句（適合高年級/拓展能力）", "sentences": ["He laced up his brand new white sneakers and stepped out ready for a morning jog."], "translations": ["他繫好嶄新的白球鞋鞋帶，邁步出門準備晨跑。"]}
        ],
        "prompt_data": {
            "num": 143, "word": "shoe", "phonetic": "/ʃuː/", "meaning": "鞋子", "category": "Clothes", "filename": "shoe.gif",
            "action_details": "一雙純淨白色時尚運動休閒鞋，鞋帶整齊繫好，鞋底橡膠防滑紋路清晰，乾淨典雅",
            "english_prompt": "Product showcase of a pristine white leather sneaker with clean white laces, resting on light oak flooring, studio lighting with soft shadows, 360 slow smooth rotation.",
            "negative_prompt": "muddy shoe, worn out dirty sneakers, deformed sole, cartoon, blur",
            "tech_specs": "4K 60fps seamless turntable rotation, realistic leather texture, crisp studio lights"
        }
    },
    {
        "id": "socks", "word": "socks", "phonetic": "/sɑːks/", "meaning": "襪子", "emoji": "🧦",
        "category": "Clothes", "level": "L1", "role": "review", "variants": ["sock"],
        "storyChapter": 8, "storyChapterTitle": "日常服飾", "storyOrder": 4, "storyScene": "一雙柔軟棉質的條紋襪子整齊捲放在收納抽屜裡",
        "scenarios": [
            {"tag": "難度 1 · 簡單初階", "desc": "基礎入門短句（適合低年級/初學啟蒙）", "sentences": ["Warm warm socks."], "translations": ["暖洋洋的襪子。"]},
            {"tag": "難度 2 · 中等日常", "desc": "生活日常短句（適合中年級/日常口語）", "sentences": ["I wear blue cotton socks."], "translations": ["我穿著藍色棉襪。"]},
            {"tag": "難度 3 · 進階挑戰", "desc": "拓展進階長句（適合高年級/拓展能力）", "sentences": ["These thick wool socks keep little feet toasty warm during cold snowy nights."], "translations": ["這些厚實的羊毛襪在寒冷下雪的夜晚能讓小腳丫保持暖洋洋的。"]}
        ],
        "prompt_data": {
            "num": 144, "word": "socks", "phonetic": "/sɑːks/", "meaning": "襪子", "category": "Clothes", "filename": "socks.gif",
            "action_details": "一雙柔軟的米白與天藍相間條紋棉襪，針織紋路清晰，柔軟蓬鬆地摺疊在溫暖木托盤上",
            "english_prompt": "A pair of cozy striped cotton knit socks, fluffy and warm, neatly folded on a light wooden surface, close-up macro of knitted yarn texture, gentle morning lighting.",
            "negative_prompt": "holey socks, smelly, dirty, flat 2D graphic, unnatural colors",
            "tech_specs": "Photorealistic 4K macro, 60fps still-motion loop, hyper-detailed cotton fibers"
        }
    },
    {
        "id": "shirt", "word": "shirt", "phonetic": "/ʃɜːrt/", "meaning": "襯衫", "emoji": "👔",
        "category": "Clothes", "level": "L1", "role": "review", "variants": ["shirts"],
        "storyChapter": 8, "storyChapterTitle": "日常服飾", "storyOrder": 5, "storyScene": "熨燙平整的淺藍色純棉襯衫整齊掛在衣櫥中",
        "scenarios": [
            {"tag": "難度 1 · 簡單初階", "desc": "基礎入門短句（適合低年級/初學啟蒙）", "sentences": ["A clean shirt."], "translations": ["一件乾淨的襯衫。"]},
            {"tag": "難度 2 · 中等日常", "desc": "生活日常短句（適合中年級/日常口語）", "sentences": ["He buttons his school shirt."], "translations": ["他扣好學校襯衫的鈕扣。"]},
            {"tag": "難度 3 · 進階挑戰", "desc": "拓展進階長句（適合高年級/拓展能力）", "sentences": ["A crisp light-blue cotton button-down shirt is neatly pressed without any wrinkles."], "translations": ["一件筆挺的淺藍色純棉鈕扣襯衫熨燙整齊，毫無皺褶。"]}
        ],
        "prompt_data": {
            "num": 145, "word": "shirt", "phonetic": "/ʃɜːrt/", "meaning": "襯衫", "category": "Clothes", "filename": "shirt.gif",
            "action_details": "一件燙得筆直平整的淡藍色牛津紡襯衫，精緻貝殼鈕扣閃爍光芒，掛在原木衣架上",
            "english_prompt": "A perfectly ironed light-blue Oxford cotton shirt on a polished wooden hanger, pristine collar and mother-of-pearl buttons, soft natural window light, elegant textile detail.",
            "negative_prompt": "crumpled, wrinkled, stained, cartoon drawing, cheap synthetic fabric",
            "tech_specs": "4K studio product shot, 60fps subtle ambient loop, razor-sharp cloth fiber focus"
        }
    },
    {
        "id": "dress", "word": "dress", "phonetic": "/dres/", "meaning": "洋裝", "emoji": "👗",
        "category": "Clothes", "level": "L1", "role": "review", "variants": ["dresses", "dressing"],
        "storyChapter": 8, "storyChapterTitle": "日常服飾", "storyOrder": 6, "storyScene": "淡粉色碎花雪紡洋裝在微風中輕輕擺動裙襬",
        "scenarios": [
            {"tag": "難度 1 · 簡單初階", "desc": "基礎入門短句（適合低年級/初學啟蒙）", "sentences": ["A pretty dress."], "translations": ["一件漂亮的洋裝。"]},
            {"tag": "難度 2 · 中等日常", "desc": "生活日常短句（適合中年級/日常口語）", "sentences": ["She wears a pink dress."], "translations": ["她穿著一件粉紅色洋裝。"]},
            {"tag": "難度 3 · 進階挑戰", "desc": "拓展進階長句（適合高年級/拓展能力）", "sentences": ["The floral summer dress swirls gently as she turns gracefully in the garden."], "translations": ["當她在花園中優雅轉身時，碎花夏日洋裝隨之輕輕旋轉。"]}
        ],
        "prompt_data": {
            "num": 146, "word": "dress", "phonetic": "/dres/", "meaning": "洋裝", "category": "Clothes", "filename": "dress.gif",
            "action_details": "一襲輕柔的粉色碎花雪紡連衣裙掛在優雅鐵藝衣架上，微風吹起輕薄裙襬如波浪起伏",
            "english_prompt": "A flowy pastel pink floral summer chiffon dress gently billowing in a soft summer breeze, sunlight filtering through delicate sheer fabric, dreamy garden terrace background.",
            "negative_prompt": "clunky, static rigid, ugly pattern, dark grim, comic style",
            "tech_specs": "4K cinematic fashion loop, 60fps slow gentle cloth physics, dreamy bokeh"
        }
    },
    {
        "id": "jacket", "word": "jacket", "phonetic": "/ˈdʒæk.ɪt/", "meaning": "夾克", "emoji": "🧥",
        "category": "Clothes", "level": "L1", "role": "review", "variants": ["jackets"],
        "storyChapter": 8, "storyChapterTitle": "日常服飾", "storyOrder": 7, "storyScene": "帥氣防風的深藍色夾克拉上銀色金屬拉鍊",
        "scenarios": [
            {"tag": "難度 1 · 簡單初階", "desc": "基礎入門短句（適合低年級/初學啟蒙）", "sentences": ["Zip your jacket."], "translations": ["拉上夾克拉鍊。"]},
            {"tag": "難度 2 · 中等日常", "desc": "生活日常短句（適合中年級/日常口語）", "sentences": ["Take your warm jacket today."], "translations": ["今天帶上你保暖的夾克。"]},
            {"tag": "難度 3 · 進階挑戰", "desc": "拓展進階長句（適合高年級/拓展能力）", "sentences": ["He zipped up his lightweight windproof jacket before heading out on the trail."], "translations": ["他在踏上步道前拉上了輕量防風夾克的拉鍊。"]}
        ],
        "prompt_data": {
            "num": 147, "word": "jacket", "phonetic": "/ˈdʒæk.ɪt/", "meaning": "夾克", "category": "Clothes", "filename": "jacket.gif",
            "action_details": "深藍色防風運動夾克，金屬拉鍊順暢拉動，防潑水面料表面荷葉效應露珠滾動",
            "english_prompt": "A modern navy blue windbreaker outdoor jacket, metallic zipper pulling smoothly up, water-resistant technical fabric with tiny water droplets beading, crisp studio details.",
            "negative_prompt": "torn fabric, dull plastic, cartoonish, low resolution",
            "tech_specs": "4K macro technical apparel, 60fps smooth loop, realistic textile sheen"
        }
    },
    {
        "id": "pants", "word": "pants", "phonetic": "/pænts/", "meaning": "長褲", "emoji": "👖",
        "category": "Clothes", "level": "L1", "role": "review", "variants": ["pant"],
        "storyChapter": 8, "storyChapterTitle": "日常服飾", "storyOrder": 8, "storyScene": "舒適百搭的休閒牛仔長褲摺疊整齊放在木櫃上",
        "scenarios": [
            {"tag": "難度 1 · 簡單初階", "desc": "基礎入門短句（適合低年級/初學啟蒙）", "sentences": ["Blue long pants."], "translations": ["藍色的長褲。"]},
            {"tag": "難度 2 · 中等日常", "desc": "生活日常短句（適合中年級/日常口語）", "sentences": ["These pants have two pockets."], "translations": ["這條長褲有兩個口袋。"]},
            {"tag": "難度 3 · 進階挑戰", "desc": "拓展進階長句（適合高年級/拓展能力）", "sentences": ["Comfortable denim jeans are folded neatly on the wooden wardrobe shelf."], "translations": ["舒適的牛仔長褲整齊地摺疊在木質衣櫥的層架上。"]}
        ],
        "prompt_data": {
            "num": 148, "word": "pants", "phonetic": "/pænts/", "meaning": "長褲", "category": "Clothes", "filename": "pants.gif",
            "action_details": "經典深藍色純棉牛仔長褲，金黃色縫線針腳密實，銅質鉚釘閃亮，整齊平展展示",
            "english_prompt": "A classic pair of dark indigo denim jeans neatly presented on a wooden surface, showing authentic copper rivets, golden stitching, and rich twill weave texture.",
            "negative_prompt": "shredded, dirty, blurry, cartoon, plastic look",
            "tech_specs": "4K product photography, 60fps macro pan, rich denim weave detail"
        }
    },
    {
        "id": "cap", "word": "cap", "phonetic": "/kæp/", "meaning": "棒球帽", "emoji": "🧢",
        "category": "Clothes", "level": "L1", "role": "review", "variants": ["caps"],
        "storyChapter": 8, "storyChapterTitle": "日常服飾", "storyOrder": 9, "storyScene": "亮眼深藍色的休閒棒球帽帽簷微微向前彎曲遮陽",
        "scenarios": [
            {"tag": "難度 1 · 簡單初階", "desc": "基礎入門短句（適合低年級/初學啟蒙）", "sentences": ["A baseball cap."], "translations": ["一頂棒球帽。"]},
            {"tag": "難度 2 · 中等日常", "desc": "生活日常短句（適合中年級/日常口語）", "sentences": ["He wears a cool cap."], "translations": ["他戴著一頂酷酷的便帽。"]},
            {"tag": "難度 3 · 進階挑戰", "desc": "拓展進階長句（適合高年級/拓展能力）", "sentences": ["The boy adjusted his blue baseball cap to shield his eyes from the afternoon sun."], "translations": ["男孩調整了他的藍色棒球帽，以遮擋午後刺眼的陽光。"]}
        ],
        "prompt_data": {
            "num": 149, "word": "cap", "phonetic": "/kæp/", "meaning": "棒球帽", "category": "Clothes", "filename": "cap.gif",
            "action_details": "深藍色休閒棒球帽放在桌上，正面精緻立體刺繡，弧形帽簷弧度優美，微風輕撫",
            "english_prompt": "A modern sporty navy blue baseball cap with curved brim, subtle embroidered emblem, resting on a clean wooden bench outdoors, sunbeam highlighting the cotton twill texture.",
            "negative_prompt": "crushed cap, dirty sweat stains, cartoon, 3D low poly",
            "tech_specs": "4K studio lighting, 60fps subtle loop, sharp embroidery details"
        }
    },
    {
        "id": "boots", "word": "boots", "phonetic": "/buːts/", "meaning": "靴子", "emoji": "🥾",
        "category": "Clothes", "level": "L1", "role": "review", "variants": ["boot"],
        "storyChapter": 8, "storyChapterTitle": "日常服飾", "storyOrder": 10, "storyScene": "堅固耐磨的棕色皮革登山靴踩在森林落葉步道上",
        "scenarios": [
            {"tag": "難度 1 · 簡單初階", "desc": "基礎入門短句（適合低年級/初學啟蒙）", "sentences": ["Warm winter boots."], "translations": ["溫暖的冬靴。"]},
            {"tag": "難度 2 · 中等日常", "desc": "生活日常短句（適合中年級/日常口語）", "sentences": ["We wear rain boots today."], "translations": ["我們今天穿雨靴。"]},
            {"tag": "難度 3 · 進階挑戰", "desc": "拓展進階長句（適合高年級/拓展能力）", "sentences": ["Sturdy brown leather hiking boots protect feet along the rocky mountain trail."], "translations": ["堅固的棕色皮革登山靴能在崎嶇的山路上保護雙腳。"]}
        ],
        "prompt_data": {
            "num": 150, "word": "boots", "phonetic": "/buːts/", "meaning": "靴子", "category": "Clothes", "filename": "boots.gif",
            "action_details": "一雙經典復古棕色真皮登山靴，金屬鞋眼扣與牢固黃黑鞋帶，皮革散發油潤光澤",
            "english_prompt": "A pair of rugged brown leather heritage boots, sturdy rubber lug soles, polished metal eyelets, sitting proudly on a stone step, outdoor natural golden lighting.",
            "negative_prompt": "cracked leather, worn holes, cartoon illustration, cheap rubber",
            "tech_specs": "Photorealistic 4K, 60fps subtle camera orbit, rich leather grain"
        }
    },
    {
        "id": "gloves", "word": "gloves", "phonetic": "/ɡlʌvz/", "meaning": "手套", "emoji": "🧤",
        "category": "Clothes", "level": "L1", "role": "review", "variants": ["glove"],
        "storyChapter": 8, "storyChapterTitle": "日常服飾", "storyOrder": 11, "storyScene": "毛茸茸的溫暖針織羊毛手套保護雙手遠離冬日嚴寒",
        "scenarios": [
            {"tag": "難度 1 · 簡單初階", "desc": "基礎入門短句（適合低年級/初學啟蒙）", "sentences": ["Wear warm gloves."], "translations": ["戴上溫暖的手套。"]},
            {"tag": "難度 2 · 中等日常", "desc": "生活日常短句（適合中年級/日常口語）", "sentences": ["Gloves keep my fingers warm."], "translations": ["手套讓我的手指保持暖和。"]},
            {"tag": "難度 3 · 進階挑戰", "desc": "拓展進階長句（適合高年級/拓展能力）", "sentences": ["Soft knitted wool gloves keep small hands warm while making snowmen outside."], "translations": ["柔軟的針織羊毛手套在戶外堆雪人時能保持小手溫暖。"]}
        ],
        "prompt_data": {
            "num": 151, "word": "gloves", "phonetic": "/ɡlʌvz/", "meaning": "手套", "category": "Clothes", "filename": "gloves.gif",
            "action_details": "一對溫暖柔軟的燕麥色粗針羊毛手套整齊放置，毛線纖維蓬鬆，在冬日窗櫺前顯得暖意融融",
            "english_prompt": "A cozy pair of oatmeal knit wool gloves resting by a frosty window pane, soft morning light illuminating the fluffy fibers, warm hot cocoa steam in background.",
            "negative_prompt": "plastic medical gloves, holes, muddy, flat render, cartoon",
            "tech_specs": "4K macro close-up, 60fps cozy winter loop, high-resolution yarn detail"
        }
    },
    {
        "id": "scarf", "word": "scarf", "phonetic": "/skɑːrf/", "meaning": "圍巾", "emoji": "🧣",
        "category": "Clothes", "level": "L1", "role": "review", "variants": ["scarves"],
        "storyChapter": 8, "storyChapterTitle": "日常服飾", "storyOrder": 12, "storyScene": "柔軟深紅色的格紋喀什米爾圍巾在頸間打出溫暖的結",
        "scenarios": [
            {"tag": "難度 1 · 簡單初階", "desc": "基礎入門短句（適合低年級/初學啟蒙）", "sentences": ["A cozy scarf."], "translations": ["一條溫暖的圍巾。"]},
            {"tag": "難度 2 · 中等日常", "desc": "生活日常短句（適合中年級/日常口語）", "sentences": ["Wrap the scarf around neck."], "translations": ["把圍巾圍在脖子上。"]},
            {"tag": "難度 3 · 進階挑戰", "desc": "拓展進階長句（適合高年級/拓展能力）", "sentences": ["The red plaid wool scarf wraps snugly around the neck to block chilly winds."], "translations": ["紅色格紋羊毛圍巾舒適地圍在脖子上，阻擋陣陣寒風。"]}
        ],
        "prompt_data": {
            "num": 152, "word": "scarf", "phonetic": "/skɑːrf/", "meaning": "圍巾", "category": "Clothes", "filename": "scarf.gif",
            "action_details": "一條奢華柔軟的深紅色格紋羊絨圍巾，流蘇輕擺，隨微風輕盈飄動，質地蓬鬆細膩",
            "english_prompt": "A luxurious red tartan plaid cashmere scarf draped gently, delicate fringes swaying in a gentle breeze, soft woolen texture, warm holiday atmosphere.",
            "negative_prompt": "stiff plastic scarf, fraying threads, muddy color, cartoon drawing",
            "tech_specs": "4K cinematic textile close-up, 60fps soft flowing loop, rich fabric depth"
        }
    },
    {
        "id": "belt", "word": "belt", "phonetic": "/belt/", "meaning": "皮帶", "emoji": "➰",
        "category": "Clothes", "level": "L1", "role": "review", "variants": ["belts"],
        "storyChapter": 8, "storyChapterTitle": "日常服飾", "storyOrder": 13, "storyScene": "典雅深棕色真皮皮帶配上亮銀色金屬釦環",
        "scenarios": [
            {"tag": "難度 1 · 簡單初階", "desc": "基礎入門短句（適合低年級/初學啟蒙）", "sentences": ["Fasten the belt."], "translations": ["繫好皮帶。"]},
            {"tag": "難度 2 · 中等日常", "desc": "生活日常短句（適合中年級/日常口語）", "sentences": ["Dad wears a brown belt."], "translations": ["爸爸繫著一條棕色皮帶。"]},
            {"tag": "難度 3 · 進階挑戰", "desc": "拓展進階長句（適合高年級/拓展能力）", "sentences": ["The polished brown leather belt has a sleek silver buckle that matches his shoes."], "translations": ["這條光澤飽滿的棕色皮帶配有精緻銀扣，與他的鞋子非常相襯。"]}
        ],
        "prompt_data": {
            "num": 153, "word": "belt", "phonetic": "/belt/", "meaning": "皮帶", "category": "Clothes", "filename": "belt.gif",
            "action_details": "一條捲成優美圓弧的頂級棕色真皮腰帶，銀色拉絲金屬皮帶頭閃爍光芒，車線細膩",
            "english_prompt": "A premium rolled brown full-grain leather belt with a brushed silver buckle resting on dark slate, immaculate stitching detail, luxury fashion product lighting.",
            "negative_prompt": "peeling faux leather, cracked, bent buckle, cartoon, low resolution",
            "tech_specs": "4K commercial macro, 60fps subtle reflection rotation, razor-sharp edge focus"
        }
    },
    {
        "id": "skirt", "word": "skirt", "phonetic": "/skɜːrt/", "meaning": "裙子", "emoji": "👗",
        "category": "Clothes", "level": "L1", "role": "review", "variants": ["skirts"],
        "storyChapter": 8, "storyChapterTitle": "日常服飾", "storyOrder": 14, "storyScene": "清爽學院風的深藍色百褶裙整齊隨風輕擺",
        "scenarios": [
            {"tag": "難度 1 · 簡單初階", "desc": "基礎入門短句（適合低年級/初學啟蒙）", "sentences": ["A pleated skirt."], "translations": ["一條百褶裙。"]},
            {"tag": "難度 2 · 中等日常", "desc": "生活日常短句（適合中年級/日常口語）", "sentences": ["She wears a school skirt."], "translations": ["她穿著學校制服裙。"]},
            {"tag": "難度 3 · 進階挑戰", "desc": "拓展進階長句（適合高年級/拓展能力）", "sentences": ["The classic navy pleated skirt flutters gently as she steps along the garden path."], "translations": ["當她沿著花園步道漫步時，經典的海軍藍百褶裙隨風輕擺。"]}
        ],
        "prompt_data": {
            "num": 154, "word": "skirt", "phonetic": "/skɜːrt/", "meaning": "裙子", "category": "Clothes", "filename": "skirt.gif",
            "action_details": "一條俐落有型的深藍色百褶短裙，壓褶線條筆直清晰，在輕柔微風中優雅輕輕擺動",
            "english_prompt": "A sharp navy blue pleated school skirt swaying gently in a soft afternoon breeze, crisp fabric folds, bright sunlit classroom terrace background.",
            "negative_prompt": "wrinkled pleats, dirty, cartoonish illustration, flat texture, unnatural motion",
            "tech_specs": "4K 60fps soft cloth animation, photorealistic fabric motion, natural outdoor light"
        }
    },
    {
        "id": "pocket", "word": "pocket", "phonetic": "/ˈpɑː.kɪt/", "meaning": "口袋", "emoji": "👝",
        "category": "Clothes", "level": "L1", "role": "review", "variants": ["pockets"],
        "storyChapter": 8, "storyChapterTitle": "日常服飾", "storyOrder": 15, "storyScene": "外套胸前的小巧口袋裡露出一隻可愛的木質小鉛筆",
        "scenarios": [
            {"tag": "難度 1 · 簡單初階", "desc": "基礎入門短句（適合低年級/初學啟蒙）", "sentences": ["In my pocket."], "translations": ["在我的口袋裡。"]},
            {"tag": "難度 2 · 中等日常", "desc": "生活日常短句（適合中年級/日常口語）", "sentences": ["Put the key into pocket."], "translations": ["把鑰匙放入口袋。"]},
            {"tag": "難度 3 · 進階挑戰", "desc": "拓展進階長句（適合高年級/拓展能力）", "sentences": ["He tucked his favorite lucky coin safely inside his jacket pocket."], "translations": ["他把他最喜愛的幸運硬幣安全地塞在外套口袋裡。"]}
        ],
        "prompt_data": {
            "num": 155, "word": "pocket", "phonetic": "/ˈpɑː.kɪt/", "meaning": "口袋", "category": "Clothes", "filename": "pocket.gif",
            "action_details": "特寫一件牛仔外套的胸前縫線口袋，一隻手輕柔將一枚金色硬幣滑入口袋中，縫線精緻",
            "english_prompt": "Close-up macro of a hand sliding a shiny brass coin smoothly into a denim jacket chest pocket, pristine stitch details, golden hour sidelight, tactile realism.",
            "negative_prompt": "torn pocket, blurry hand, cartoon, flat rendering, noisy image",
            "tech_specs": "4K macro 60fps smooth loop, realistic cloth tension, cinematic depth of field"
        }
    },
    {
        "id": "watch", "word": "watch", "phonetic": "/wɑːtʃ/", "meaning": "手錶", "emoji": "⌚",
        "category": "Clothes", "level": "L1", "role": "review", "variants": ["watches", "watching"],
        "storyChapter": 8, "storyChapterTitle": "日常服飾", "storyOrder": 16, "storyScene": "精緻的金屬指針手錶在錶盤上規律安靜地跳動秒針",
        "scenarios": [
            {"tag": "難度 1 · 簡單初階", "desc": "基礎入門短句（適合低年級/初學啟蒙）", "sentences": ["A wrist watch."], "translations": ["一隻手錶。"]},
            {"tag": "難度 2 · 中等日常", "desc": "生活日常短句（適合中年級/日常口語）", "sentences": ["What time is your watch?"], "translations": ["你的手錶現在幾點？"]},
            {"tag": "難度 3 · 進階挑戰", "desc": "拓展進階長句（適合高年級/拓展能力）", "sentences": ["The classic analog wristwatch has a sleek leather strap and glowing silver hands."], "translations": ["這只經典指針手錶配有時尚皮錶帶與閃亮的銀色指針。"]}
        ],
        "prompt_data": {
            "num": 156, "word": "watch", "phonetic": "/wɑːtʃ/", "meaning": "手錶", "category": "Clothes", "filename": "watch.gif",
            "action_details": "特寫一隻高級手錶錶盤，銀色秒針規律順滑掃動，藍寶石水晶鏡面反射微光，棕色真皮錶帶",
            "english_prompt": "Macro shot of a luxury minimalist wristwatch dial, smooth sweeping second hand, sapphire crystal glass catching soft light reflections, fine leather strap, horology elegance.",
            "negative_prompt": "broken glass, cheap plastic toy watch, digital clock, blurry dial, cartoon",
            "tech_specs": "4K ultra-macro, 60fps smooth sweeping second hand loop, studio lighting"
        }
    },
    {
        "id": "glasses", "word": "glasses", "phonetic": "/ˈɡlæs.ɪz/", "meaning": "眼鏡", "emoji": "👓",
        "category": "Clothes", "level": "L1", "role": "review", "variants": ["glass"],
        "storyChapter": 8, "storyChapterTitle": "日常服飾", "storyOrder": 17, "storyScene": "晶瑩剔透的圓形金絲邊眼鏡靜置在翻開的精裝書上",
        "scenarios": [
            {"tag": "難度 1 · 簡單初階", "desc": "基礎入門短句（適合低年級/初學啟蒙）", "sentences": ["Wear reading glasses."], "translations": ["戴上閱讀眼鏡。"]},
            {"tag": "難度 2 · 中等日常", "desc": "生活日常短句（適合中年級/日常口語）", "sentences": ["Grandpa looks for his glasses."], "translations": ["爺爺在找他的眼鏡。"]},
            {"tag": "難度 3 · 進階挑戰", "desc": "拓展進階長句（適合高年級/拓展能力）", "sentences": ["She cleaned her round wire-rimmed glasses before sitting down to read the storybook."], "translations": ["她在坐下來閱讀故事書前，先擦乾淨了她的圓形金絲邊眼鏡。"]}
        ],
        "prompt_data": {
            "num": 157, "word": "glasses", "phonetic": "/ˈɡlæs.ɪz/", "meaning": "眼鏡", "category": "Clothes", "filename": "glasses.gif",
            "action_details": "一副優雅的金屬細框圓形眼鏡平放在打開的厚精裝書上，鏡片清澈透亮，微光透過鏡片在書頁上折射光影",
            "english_prompt": "A pair of elegant gold round spectacles resting gently on an open hardcover book, crystalline clean lenses with subtle anti-reflective blue glare, warm library lighting.",
            "negative_prompt": "smudged lenses, scratched glass, broken frame, dark, comic drawing",
            "tech_specs": "4K macro still life, 60fps gentle breathing loop, pristine glass caustics"
        }
    },
    {
        "id": "ring", "word": "ring", "phonetic": "/rɪŋ/", "meaning": "戒指", "emoji": "💍",
        "category": "Clothes", "level": "L1", "role": "review", "variants": ["rings", "ringing"],
        "storyChapter": 8, "storyChapterTitle": "日常服飾", "storyOrder": 18, "storyScene": "一枚精巧閃耀的銀色戒指靜靜置於天鵝絨首飾盒中",
        "scenarios": [
            {"tag": "難度 1 · 簡單初階", "desc": "基礎入門短句（適合低年級/初學啟蒙）", "sentences": ["A shiny ring."], "translations": ["一枚閃亮的戒指。"]},
            {"tag": "難度 2 · 中等日常", "desc": "生活日常短句（適合中年級/日常口語）", "sentences": ["Mom wears a gold ring."], "translations": ["媽媽戴著一枚金戒指。"]},
            {"tag": "難度 3 · 進階挑戰", "desc": "拓展進階長句（適合高年級/拓展能力）", "sentences": ["The delicate silver ring sparkles brilliantly on the deep blue velvet cushion."], "translations": ["精緻的銀戒指在深藍色天鵝絨墊上閃耀著璀璨光芒。"]}
        ],
        "prompt_data": {
            "num": 158, "word": "ring", "phonetic": "/rɪŋ/", "meaning": "戒指", "category": "Clothes", "filename": "ring.gif",
            "action_details": "特寫一枚優雅簡約的鉑金光面戒指，靜置於皇家藍色天鵝絨首飾盒內，寶石光澤隨微光閃爍",
            "english_prompt": "Macro cinematic reveal of an exquisite polished silver band ring sitting on plush royal blue velvet, radiant sparkle glistening from metallic reflections, luxury jewelry lighting.",
            "negative_prompt": "cheap plastic ring, tarnished metal, blur, comic illustration",
            "tech_specs": "4K jewelry commercial macro, 60fps subtle light shimmer, ray-traced reflections"
        }
    },
    {
        "id": "uniform", "word": "uniform", "phonetic": "/ˈjuː.nə.fɔːrm/", "meaning": "制服", "emoji": "🥋",
        "category": "Clothes", "level": "L1", "role": "review", "variants": ["uniforms"],
        "storyChapter": 8, "storyChapterTitle": "日常服飾", "storyOrder": 19, "storyScene": "整齊帥氣的英倫學院風格校服掛在明亮穿衣鏡旁",
        "scenarios": [
            {"tag": "難度 1 · 簡單初階", "desc": "基礎入門短句（適合低年級/初學啟蒙）", "sentences": ["My school uniform."], "translations": ["我的學校制服。"]},
            {"tag": "難度 2 · 中等日常", "desc": "生活日常短句（適合中年級/日常口語）", "sentences": ["Students wear clean uniforms."], "translations": ["學生們穿著整潔的制服。"]},
            {"tag": "難度 3 · 進階挑戰", "desc": "拓展進階長句（適合高年級/拓展能力）", "sentences": ["Every Monday morning, pupils wear their smart navy uniforms with pride."], "translations": ["每逢週一早晨，學生們都自豪地穿著他們帥氣的海軍藍制服。"]}
        ],
        "prompt_data": {
            "num": 159, "word": "uniform", "phonetic": "/ˈjuː.nə.fɔːrm/", "meaning": "制服", "category": "Clothes", "filename": "uniform.gif",
            "action_details": "一套筆挺整齊的英倫風深藍色學生西裝制服配有胸針與領帶，端正掛在衣架上，英姿颯爽",
            "english_prompt": "A crisp, impeccably tailored navy school blazer uniform with polished brass buttons and school crest badge, hung on a cedar coat hanger, warm morning sunlight streaming in.",
            "negative_prompt": "creased, disheveled, messy, cartoonish, low resolution",
            "tech_specs": "4K studio apparel shot, 60fps subtle loop, sharp textile and badge detail"
        }
    },
    {
        "id": "backpack", "word": "backpack", "phonetic": "/ˈbæk.pæk/", "meaning": "背包", "emoji": "🎒",
        "category": "Clothes", "level": "L1", "role": "review", "variants": ["backpacks"],
        "storyChapter": 8, "storyChapterTitle": "日常服飾", "storyOrder": 20, "storyScene": "裝好課本與水壺的雙肩背包安穩立在書桌旁",
        "scenarios": [
            {"tag": "難度 1 · 簡單初階", "desc": "基礎入門短句（適合低年級/初學啟蒙）", "sentences": ["Pack my backpack."], "translations": ["收拾我的背包。"]},
            {"tag": "難度 2 · 中等日常", "desc": "生活日常短句（適合中年級/日常口語）", "sentences": ["He carries a heavy backpack."], "translations": ["他背著一個沉甸甸的背包。"]},
            {"tag": "難度 3 · 進階挑戰", "desc": "拓展進階長句（適合高年級/拓展能力）", "sentences": ["The colorful ergonomic backpack is packed with notebooks, crayons, and a water bottle."], "translations": ["色彩繽紛的人體工學雙肩背包裡裝滿了筆記本、蠟筆和一個水壺。"]}
        ],
        "prompt_data": {
            "num": 160, "word": "backpack", "phonetic": "/ˈbæk.pæk/", "meaning": "背包", "category": "Clothes", "filename": "backpack.gif",
            "action_details": "一個色彩活潑且設計現代的兒童人體工學書包，側袋插著不鏽鋼水壺，拉鍊吊飾輕輕搖擺",
            "english_prompt": "A modern colorful student ergonomic backpack standing upright by a wooden desk, side mesh pocket holding a water bottle, smooth zipper pull swaying softly, bright cheerful study room.",
            "negative_prompt": "torn bag, dirty stains, cartoon, flat render, muddy colors",
            "tech_specs": "Photorealistic 4K, 60fps gentle loop, crisp nylon fabric weave, clean lighting"
        }
    }
]
