# -*- coding: utf-8 -*-
"""Master pipeline to build 200-word vocabulary, generate missing Samantha audio,
update Excel/CSV prompt spreadsheets, update vocab.json, and update index.html."""

import os
import sys
import json
import shutil
import subprocess
from concurrent.futures import ThreadPoolExecutor

from vocab_data_part1 import PART_1
from vocab_data_part2 import PART_2
from vocab_data_part3 import PART_3
from vocab_data_part4 import PART_4
from vocab_data_part5 import PART_5

# Map category names to uniform lower snake_case
CAT_MAP = {
    "home": "home",
    "food": "food",
    "animal": "animal",
    "nature": "nature",
    "toy_school": "toy_school",
    "daily_body": "daily_body",
    "Travel": "travel",
    "travel": "travel",
    "Clothes": "clothes",
    "clothes": "clothes",
    "Colors & Shapes": "colors_shapes",
    "colors_shapes": "colors_shapes",
    "Actions & Sports": "actions",
    "actions": "actions"
}

CHAPTER_MAP = {
    "home": (1, "🌅 第一幕 · 晨光甦醒與溫馨家居"),
    "food": (2, "🥞 第二幕 · 活力美味廚房與餐點"),
    "animal": (3, "🐾 第三幕 · 動物森林奇遇與陪伴"),
    "nature": (4, "🌲 第四幕 · 大自然奇妙天地探索"),
    "toy_school": (5, "🎒 第五幕 · 校園學習與同樂玩耍"),
    "daily_body": (6, "💖 第六幕 · 健康身心與自理習慣"),
    "travel": (7, "🚗 第七幕 · 城市探索與便捷交通"),
    "clothes": (8, "👗 第八幕 · 日常服飾與自信穿搭"),
    "colors_shapes": (9, "🎨 第九幕 · 繽紛色彩與奇妙形狀"),
    "actions": (10, "🏃 第十幕 · 活力律動與動感探索")
}

def normalize_vocab():
    raw_all = PART_1 + PART_2 + PART_3 + PART_4 + PART_5
    assert len(raw_all) == 200, f"Expected 200 words, got {len(raw_all)}"

    normalized = []
    excel_rows = []

    for idx, item in enumerate(raw_all, 1):
        cat = CAT_MAP.get(item["category"], item["category"].lower())
        chap_num, chap_title = CHAPTER_MAP.get(cat, (1, "日常情境"))

        # Extract 3 sentences & translations
        if "scenarios" in item:
            scs = item["scenarios"]
            s0 = scs[0]["sentences"][0]
            t0 = scs[0]["translations"][0]
            s1 = scs[1]["sentences"][0]
            t1 = scs[1]["translations"][0]
            s2 = scs[2]["sentences"][0]
            t2 = scs[2]["translations"][0]
        else:
            s0 = item["sentences"][0]
            t0 = item["translations"][0]
            s1 = item["sentences"][1]
            t1 = item["translations"][1]
            s2 = item["sentences"][2]
            t2 = item["translations"][2]

        # Extract prompt details
        if "prompt_data" in item:
            pd = item["prompt_data"]
            scene_details = pd.get("action_details", "")
            prompt_en = pd.get("english_prompt", "")
            neg_prompt = pd.get("negative_prompt", "cartoon, anime, illustration, 3d render, plastic, CGI, ugly, distorted, deformed, blurry, flickering, watermark, signature, grainy, low resolution, duplicate limbs.")
            tech_specs = pd.get("tech_specs", "解析度 1024x1024 (1:1 正方形) | 幀率 20 fps | 時長 3秒無縫循環 | 輸出 GIF / WebP")
        else:
            scene_details = item.get("sceneDetails", "")
            prompt_en = item.get("prompt", "")
            neg_prompt = "cartoon, anime, illustration, 3d render, plastic, CGI, ugly, distorted, deformed, blurry, flickering, watermark, signature, grainy, low resolution, duplicate limbs."
            tech_specs = "解析度 1024x1024 (1:1 正方形) | 幀率 20 fps | 時長 3秒無縫循環 | 輸出 GIF / WebP"

        card = {
            "id": item["id"],
            "word": item["word"],
            "phonetic": item["phonetic"],
            "meaning": item["meaning"],
            "emoji": item["emoji"],
            "category": cat,
            "level": "L1",
            "role": item.get("role", "review"),
            "variants": item.get("variants", [item["word"]]),
            "audioWord": f"audio/word_{item['id']}.m4a",
            "gradedSentences": [
                {
                    "level": 1,
                    "levelLabel": "簡單 · 初階短句",
                    "tag": "簡單",
                    "text": s0,
                    "translation": t0,
                    "audioSrc": f"audio/sentence_{item['id']}_0_0.m4a"
                },
                {
                    "level": 2,
                    "levelLabel": "中等 · 生活日常",
                    "tag": "中等",
                    "text": s1,
                    "translation": t1,
                    "audioSrc": f"audio/sentence_{item['id']}_1_0.m4a"
                },
                {
                    "level": 3,
                    "levelLabel": "進階 · 拓展挑戰",
                    "tag": "進階",
                    "text": s2,
                    "translation": t2,
                    "audioSrc": f"audio/sentence_{item['id']}_2_0.m4a"
                }
            ],
            "scenarios": [
                {
                    "tag": "難度 1 · 簡單初階",
                    "desc": "基礎入門短句（適合低年級/初學啟蒙）",
                    "sentences": [s0],
                    "translations": [t0]
                },
                {
                    "tag": "難度 2 · 中等日常",
                    "desc": "生活日常短句（適合中年級/日常口語）",
                    "sentences": [s1],
                    "translations": [t1]
                },
                {
                    "tag": "難度 3 · 進階挑戰",
                    "desc": "拓展進階長句（適合高年級/拓展能力）",
                    "sentences": [s2],
                    "translations": [t2]
                }
            ],
            "storyChapter": chap_num,
            "storyChapterTitle": chap_title,
            "storyOrder": idx,
            "storyScene": item.get("storyScene", scene_details)
        }
        normalized.append(card)

        excel_rows.append({
            "num": idx,
            "word": item["word"],
            "phonetic": item["phonetic"],
            "meaning": item["meaning"],
            "category": cat,
            "filename": f"card_{item['id']}.gif",
            "action_details": scene_details,
            "english_prompt": prompt_en,
            "negative_prompt": neg_prompt,
            "tech_specs": tech_specs
        })

    return normalized, excel_rows


def generate_audio_task(task):
    out_path, text, rate = task
    if os.path.exists(out_path) and os.path.getsize(out_path) > 1000:
        return f"[SKIP] {out_path}"
    
    tmp_aiff = out_path + ".aiff"
    try:
        # Use say command with Samantha
        cmd = ["say", "-v", "Samantha", "-r", str(rate), "-o", tmp_aiff, text]
        subprocess.run(cmd, check=True)
        # Convert to m4a (AAC)
        conv_cmd = ["afconvert", "-f", "m4af", "-d", "aac", tmp_aiff, out_path]
        subprocess.run(conv_cmd, check=True)
        if os.path.exists(tmp_aiff):
            os.remove(tmp_aiff)
        return f"[GEN] {out_path}"
    except Exception as e:
        if os.path.exists(tmp_aiff):
            os.remove(tmp_aiff)
        return f"[ERR] {out_path}: {e}"


def generate_all_audio(vocab):
    os.makedirs("audio", exist_ok=True)
    tasks = []

    for item in vocab:
        w_id = item["id"]
        word = item["word"]
        # Word audio (rate 145)
        w_path = f"audio/word_{w_id}.m4a"
        tasks.append((w_path, word, 145))

        # 3 Sentences (rate 155)
        for sIdx in range(3):
            s_text = item["scenarios"][sIdx]["sentences"][0]
            s_path = f"audio/sentence_{w_id}_{sIdx}_0.m4a"
            tasks.append((s_path, s_text, 155))

    print(f"Total audio tasks to evaluate: {len(tasks)}")
    
    with ThreadPoolExecutor(max_workers=8) as ex:
        results = list(ex.map(generate_audio_task, tasks))
    
    gen_count = sum(1 for r in results if r.startswith("[GEN]"))
    skip_count = sum(1 for r in results if r.startswith("[SKIP]"))
    err_count = sum(1 for r in results if r.startswith("[ERR]"))
    print(f"Audio results -> Generated: {gen_count}, Skipped (already exist): {skip_count}, Errors: {err_count}")

    # Create alias sentence_{id}_{sIdx}.m4a matching sentence_{id}_{sIdx}_0.m4a
    alias_count = 0
    for item in vocab:
        w_id = item["id"]
        for sIdx in range(3):
            src = f"audio/sentence_{w_id}_{sIdx}_0.m4a"
            dst = f"audio/sentence_{w_id}_{sIdx}.m4a"
            if os.path.exists(src) and (not os.path.exists(dst) or os.path.getsize(dst) != os.path.getsize(src)):
                shutil.copyfile(src, dst)
                alias_count += 1
    print(f"Sentence alias copies updated: {alias_count}")


def update_excel_and_csv(excel_rows):
    import openpyxl
    from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
    from openpyxl.utils import get_column_letter
    import csv

    # 1. Update KaiSpeak_200_Vocab_Realistic_GIF_Prompts.xlsx
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "200單字真實動態圖提示詞庫"

    headers = [
        "序號\nNo.",
        "英文單字\nWord",
        "美式音標\nPhonetic",
        "中文釋義\nMeaning",
        "分類主題\nCategory",
        "建議檔名\nFilename",
        "真實動態場景設計 (生活攝影視角)\nAction & Scene Details",
        "AI 動態 GIF 生成提示詞 (英文)\nRealistic Dynamic GIF Prompt (Midjourney / Sora / Kling / Runway)",
        "負面提示詞\nNegative Prompt",
        "長寬比與生成參數規格\nTechnical Specs"
    ]
    ws.append(headers)

    header_font = Font(name="微軟正黑體", size=11, bold=True, color="FFFFFF")
    header_fill = PatternFill(start_color="3B4CCA", end_color="3B4CCA", fill_type="solid")
    header_align = Alignment(horizontal="center", vertical="center", wrap_text=True)

    thin_border = Border(
        left=Side(style='thin', color='D0D7DE'),
        right=Side(style='thin', color='D0D7DE'),
        top=Side(style='thin', color='D0D7DE'),
        bottom=Side(style='thin', color='D0D7DE')
    )

    for col_idx in range(1, len(headers) + 1):
        cell = ws.cell(row=1, column=col_idx)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = header_align
        cell.border = thin_border
    ws.row_dimensions[1].height = 42

    regular_font = Font(name="微軟正黑體", size=10)
    alt_fill = PatternFill(start_color="F8FAFC", end_color="F8FAFC", fill_type="solid")
    white_fill = PatternFill(start_color="FFFFFF", end_color="FFFFFF", fill_type="solid")

    for r_idx, r in enumerate(excel_rows, 2):
        row_vals = [
            r["num"],
            r["word"],
            r["phonetic"],
            r["meaning"],
            r["category"],
            r["filename"],
            r["action_details"],
            r["english_prompt"],
            r["negative_prompt"],
            r["tech_specs"]
        ]
        ws.append(row_vals)
        fill = alt_fill if r_idx % 2 == 0 else white_fill
        for c_idx in range(1, len(row_vals) + 1):
            cell = ws.cell(row=r_idx, column=c_idx)
            cell.font = regular_font
            cell.fill = fill
            cell.border = thin_border
            if c_idx in [1, 5, 6]:
                cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
            elif c_idx in [2, 3]:
                cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=False)
            else:
                cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
        ws.row_dimensions[r_idx].height = 48

    col_widths = {
        1: 8,   # No.
        2: 12,  # Word
        3: 14,  # Phonetic
        4: 22,  # Meaning
        5: 14,  # Category
        6: 18,  # Filename
        7: 42,  # Action & Scene
        8: 52,  # Dynamic GIF Prompt
        9: 36,  # Negative Prompt
        10: 24  # Technical Specs
    }
    for col_idx, width in col_widths.items():
        ws.column_dimensions[get_column_letter(col_idx)].width = width

    xlsx_200 = "KaiSpeak_200_Vocab_Realistic_GIF_Prompts.xlsx"
    wb.save(xlsx_200)
    print(f"Saved {xlsx_200} with {len(excel_rows)} rows!")

    # Also keep 50 spreadsheet for compatibility or update it
    xlsx_50 = "KaiSpeak_50_Vocab_Realistic_GIF_Prompts.xlsx"
    # Create 200 CSV with UTF-8 BOM
    csv_200 = "KaiSpeak_200_Vocab_Realistic_GIF_Prompts.csv"
    with open(csv_200, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([h.replace("\n", " ") for h in headers])
        for r in excel_rows:
            writer.writerow([
                r["num"], r["word"], r["phonetic"], r["meaning"], r["category"],
                r["filename"], r["action_details"], r["english_prompt"],
                r["negative_prompt"], r["tech_specs"]
            ])
    print(f"Saved {csv_200}!")


def update_vocab_json(vocab):
    with open("vocab.json", "w", encoding="utf-8") as f:
        json.dump(vocab, f, ensure_ascii=False, indent=2)
    print(f"Updated vocab.json with {len(vocab)} items!")


def update_index_html(vocab):
    with open("index.html", "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update const MASTER_VOCAB = [...];
    start_tag = "const MASTER_VOCAB = ["
    start_idx = content.find(start_tag)
    assert start_idx != -1, "Could not find 'const MASTER_VOCAB = [' in index.html"

    # Find matching closing bracket
    end_tag = "];\n\n    // Application State"
    end_idx = content.find(end_tag, start_idx)

    assert end_idx != -1, "Could not find end of MASTER_VOCAB in index.html"

    json_str = json.dumps(vocab, ensure_ascii=False, indent=2)
    new_master_vocab_str = f"const MASTER_VOCAB = {json_str};\n\n    // Application State"

    # Replace MASTER_VOCAB block
    content = content[:start_idx] + new_master_vocab_str + content[end_idx + len(end_tag):]

    # 2. Update category buttons in HTML
    old_cat_buttons_start = '<div class="flex items-center gap-1.5 overflow-x-auto hide-scrollbar text-xs w-full py-1">'
    old_cat_buttons_end = '<!-- Kai Story Living Scene Navigator Banner'

    c_start = content.find(old_cat_buttons_start)
    c_end = content.find(old_cat_buttons_end, c_start)
    assert c_start != -1 and c_end != -1, "Could not find category button block in index.html"

    new_cat_buttons = """<div class="flex items-center gap-1.5 overflow-x-auto hide-scrollbar text-xs w-full py-1">
      <button onclick="setFreeCategory('all')" class="free-cat-btn active px-3.5 py-1.5 rounded-xl font-bold bg-indigo-600 text-white shadow-sm whitespace-nowrap" data-cat="all">全部詞庫 (200)</button>
      <button onclick="setFreeCategory('story')" class="free-cat-btn px-3.5 py-1.5 rounded-xl font-black bg-gradient-to-r from-amber-100 via-purple-100 to-indigo-100 text-purple-950 border border-purple-300 hover:from-amber-200 hover:to-purple-200 whitespace-nowrap shadow-sm flex items-center gap-1.5 active:scale-95 transition" data-cat="story">
        <span class="text-sm">📖</span>
        <span>生活故事 · Kai's Day</span>
        <span class="text-[9px] bg-purple-600 text-white px-2 py-0.5 rounded-full font-extrabold tracking-wider">10 幕故事</span>
      </button>
      <button onclick="setFreeCategory('weak')" class="free-cat-btn px-3.5 py-1.5 rounded-xl font-bold bg-rose-50 text-rose-700 border border-rose-200 hover:bg-rose-100 whitespace-nowrap" data-cat="weak">⚠️ 錯詞本 (<span id="weakCountBadge">0</span>)</button>
      <button onclick="setFreeCategory('home')" class="free-cat-btn px-3.5 py-1.5 rounded-xl font-semibold bg-slate-100 text-slate-600 hover:bg-slate-200 whitespace-nowrap" data-cat="home">🏠 家居 (20)</button>
      <button onclick="setFreeCategory('food')" class="free-cat-btn px-3.5 py-1.5 rounded-xl font-semibold bg-slate-100 text-slate-600 hover:bg-slate-200 whitespace-nowrap" data-cat="food">🍎 飲食 (20)</button>
      <button onclick="setFreeCategory('animal')" class="free-cat-btn px-3.5 py-1.5 rounded-xl font-semibold bg-slate-100 text-slate-600 hover:bg-slate-200 whitespace-nowrap" data-cat="animal">🐶 動物 (20)</button>
      <button onclick="setFreeCategory('nature')" class="free-cat-btn px-3.5 py-1.5 rounded-xl font-semibold bg-slate-100 text-slate-600 hover:bg-slate-200 whitespace-nowrap" data-cat="nature">🌿 自然 (20)</button>
      <button onclick="setFreeCategory('toy_school')" class="free-cat-btn px-3.5 py-1.5 rounded-xl font-semibold bg-slate-100 text-slate-600 hover:bg-slate-200 whitespace-nowrap" data-cat="toy_school">🎒 校園 (20)</button>
      <button onclick="setFreeCategory('daily_body')" class="free-cat-btn px-3.5 py-1.5 rounded-xl font-semibold bg-slate-100 text-slate-600 hover:bg-slate-200 whitespace-nowrap" data-cat="daily_body">❤️ 身心 (20)</button>
      <button onclick="setFreeCategory('travel')" class="free-cat-btn px-3.5 py-1.5 rounded-xl font-semibold bg-slate-100 text-slate-600 hover:bg-slate-200 whitespace-nowrap" data-cat="travel">🚗 交通 (20)</button>
      <button onclick="setFreeCategory('clothes')" class="free-cat-btn px-3.5 py-1.5 rounded-xl font-semibold bg-slate-100 text-slate-600 hover:bg-slate-200 whitespace-nowrap" data-cat="clothes">👗 服飾 (20)</button>
      <button onclick="setFreeCategory('colors_shapes')" class="free-cat-btn px-3.5 py-1.5 rounded-xl font-semibold bg-slate-100 text-slate-600 hover:bg-slate-200 whitespace-nowrap" data-cat="colors_shapes">🎨 色彩 (20)</button>
      <button onclick="setFreeCategory('actions')" class="free-cat-btn px-3.5 py-1.5 rounded-xl font-semibold bg-slate-100 text-slate-600 hover:bg-slate-200 whitespace-nowrap" data-cat="actions">🏃 律動 (20)</button>
    </div>

    """

    content = content[:c_start] + new_cat_buttons + content[c_end:]

    # 3. Update story chapter tabs
    old_story_tabs_start = '<div class="flex items-center gap-1.5 overflow-x-auto hide-scrollbar text-xs font-bold pt-1">'
    st_start = content.find(old_story_tabs_start, content.find('id="freeStoryIntroBanner"'))
    old_story_tabs_end = '<!-- Flashcard Pagination Header'
    st_end = content.find(old_story_tabs_end, st_start)
    assert st_start != -1 and st_end != -1, "Could not find story chapter pills in index.html"

    new_story_tabs = """<div class="flex items-center gap-1.5 overflow-x-auto hide-scrollbar text-xs font-bold pt-1">
        <button onclick="filterStoryChapter('all')" id="storyChapTab_all" class="story-chap-tab px-3 py-1.5 rounded-xl bg-purple-700 text-white shadow-xs whitespace-nowrap">全部 10 幕 (200詞)</button>
        <button onclick="filterStoryChapter(1)" id="storyChapTab_1" class="story-chap-tab px-3 py-1.5 rounded-xl bg-white text-purple-900 border border-purple-200 hover:bg-purple-100 whitespace-nowrap">🌅 1.居家晨起 (20)</button>
        <button onclick="filterStoryChapter(2)" id="storyChapTab_2" class="story-chap-tab px-3 py-1.5 rounded-xl bg-white text-purple-900 border border-purple-200 hover:bg-purple-100 whitespace-nowrap">🥞 2.元氣廚房 (20)</button>
        <button onclick="filterStoryChapter(3)" id="storyChapTab_3" class="story-chap-tab px-3 py-1.5 rounded-xl bg-white text-purple-900 border border-purple-200 hover:bg-purple-100 whitespace-nowrap">🐾 3.森林萌寵 (20)</button>
        <button onclick="filterStoryChapter(4)" id="storyChapTab_4" class="story-chap-tab px-3 py-1.5 rounded-xl bg-white text-purple-900 border border-purple-200 hover:bg-purple-100 whitespace-nowrap">🌲 4.奇妙自然 (20)</button>
        <button onclick="filterStoryChapter(5)" id="storyChapTab_5" class="story-chap-tab px-3 py-1.5 rounded-xl bg-white text-purple-900 border border-purple-200 hover:bg-purple-100 whitespace-nowrap">🎒 5.校園玩樂 (20)</button>
        <button onclick="filterStoryChapter(6)" id="storyChapTab_6" class="story-chap-tab px-3 py-1.5 rounded-xl bg-white text-purple-900 border border-purple-200 hover:bg-purple-100 whitespace-nowrap">💖 6.身心健康 (20)</button>
        <button onclick="filterStoryChapter(7)" id="storyChapTab_7" class="story-chap-tab px-3 py-1.5 rounded-xl bg-white text-purple-900 border border-purple-200 hover:bg-purple-100 whitespace-nowrap">🚗 7.城市探索 (20)</button>
        <button onclick="filterStoryChapter(8)" id="storyChapTab_8" class="story-chap-tab px-3 py-1.5 rounded-xl bg-white text-purple-900 border border-purple-200 hover:bg-purple-100 whitespace-nowrap">👗 8.日常服飾 (20)</button>
        <button onclick="filterStoryChapter(9)" id="storyChapTab_9" class="story-chap-tab px-3 py-1.5 rounded-xl bg-white text-purple-900 border border-purple-200 hover:bg-purple-100 whitespace-nowrap">🎨 9.色彩幾何 (20)</button>
        <button onclick="filterStoryChapter(10)" id="storyChapTab_10" class="story-chap-tab px-3 py-1.5 rounded-xl bg-white text-purple-900 border border-purple-200 hover:bg-purple-100 whitespace-nowrap">🏃 10.活力律動 (20)</button>
      </div>
    </div>

    """

    content = content[:st_start] + new_story_tabs + content[st_end:]

    # 4. Bump cache buster
    content = content.replace("?v=20", "?v=21")
    content = content.replace("?v=19", "?v=21")
    content = content.replace("const LATEST_CACHE_BUSTER = 'v20';", "const LATEST_CACHE_BUSTER = 'v21';")

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated index.html with 200 words and v21 cache-buster!")


def main():
    print("--- 1. Normalizing 200 Vocab Data ---")
    vocab, excel_rows = normalize_vocab()
    print(f"Normalized {len(vocab)} words successfully.")

    print("--- 2. Updating Excel & CSV Spreadsheets ---")
    update_excel_and_csv(excel_rows)

    print("--- 3. Updating vocab.json ---")
    update_vocab_json(vocab)

    print("--- 4. Generating Missing Audio via say -v Samantha ---")
    generate_all_audio(vocab)

    print("--- 5. Updating index.html ---")
    update_index_html(vocab)

    print("--- ALL PIPELINE STEPS COMPLETE! ---")

if __name__ == "__main__":
    main()
