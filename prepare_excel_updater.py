# -*- coding: utf-8 -*-
"""Updates KaiSpeak_500_Vocab_Realistic_GIF_Prompts.xlsx and .csv
with systematic codes, L1/L2/L3 simple child-friendly sentences, translations,
and audio paths."""

import csv
import json
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

from builder_part1 import PART_1_DATA
from builder_part2 import PART_2_DATA
from builder_part3 import PART_3_DATA
from builder_part4 import PART_4_DATA
from builder_part5 import PART_5_DATA

ALL_CURATED = {}
for p in [PART_1_DATA, PART_2_DATA, PART_3_DATA, PART_4_DATA, PART_5_DATA]:
    ALL_CURATED.update(p)

# Read original Excel to preserve prompts and scene details
wb_orig = openpyxl.load_workbook('KaiSpeak_500_Vocab_Realistic_GIF_Prompts.xlsx', data_only=True)
ws_orig = wb_orig.active

orig_rows = list(ws_orig.iter_rows(values_only=True))
headers_orig = orig_rows[0]
print(f"Original headers: {headers_orig}")

# Map word to prompt details
orig_details = {}
for r in orig_rows[1:]:
    if not r or not r[1]:
        continue
    w = str(r[1]).strip().lower()
    orig_details[w] = {
        "action": r[6] if len(r) > 6 else "",
        "prompt": r[7] if len(r) > 7 else "",
        "negative": r[8] if len(r) > 8 else "",
        "specs": r[9] if len(r) > 9 else ""
    }

print(f"Loaded original details for {len(orig_details)} words.")

with open('vocab.json', 'r', encoding='utf-8') as f:
    vocab = json.load(f)

new_headers = [
    '序號\nNo.',
    '系統編碼\nSystem Code',
    '英文單字\nWord',
    '美式音標\nPhonetic',
    '中文釋義\nMeaning',
    '分類主題\nCategory',
    '建議檔名\nFilename',
    '初階例句 (L1 短句)\nLevel 1 Sentence',
    '初階中文 (L1 翻譯)\nLevel 1 Translation',
    '日常例句 (L2 生活)\nLevel 2 Sentence',
    '日常中文 (L2 翻譯)\nLevel 2 Translation',
    '進階例句 (L3 挑戰)\nLevel 3 Sentence',
    '進階中文 (L3 翻譯)\nLevel 3 Translation',
    '語音編碼與檔案路徑\nAudio System Info',
    '真實動態場景設計 (生活攝影視角)\nAction & Scene Details',
    'AI 影片/GIF 提示詞 (Midjourney/Runway/Luma/Kling)\nDynamic GIF Prompt',
    '負面提示詞 (確保真實攝影質感)\nNegative Prompt',
    '技術規格建議\nTechnical Specs'
]

rows_data = []
for idx, v in enumerate(vocab):
    num = idx + 1
    w_code = f"EN_W{num:04d}"
    w = v["word"]
    cur = ALL_CURATED.get(w, {})
    det = orig_details.get(w, {})

    s1 = cur.get("s1", "")
    t1 = cur.get("t1", "")
    s2 = cur.get("s2", "")
    t2 = cur.get("t2", "")
    s3 = cur.get("s3", "")
    t3 = cur.get("t3", "")

    audio_info = f"Word: audio/words/{w_code.lower()}_{v['id']}.m4a\nS1: audio/sentences/{w_code.lower()}_s1_{v['id']}.m4a\nS2: audio/sentences/{w_code.lower()}_s2_{v['id']}.m4a\nS3: audio/sentences/{w_code.lower()}_s3_{v['id']}.m4a"

    action = det.get("action") or v.get("storyScene", "")
    prompt = det.get("prompt", "")
    neg = det.get("negative") or "cartoon, anime, illustration, 3d render, plastic, CGI, ugly, distorted, deformed, blurry, flickering, watermark, signature, grainy, low resolution, duplicate limbs."
    specs = det.get("specs") or "解析度 1024x1024 (1:1 正方形) | 幀率 20 fps | 時長 3秒無縫循環 | 輸出 GIF / WebP"

    row = [
        num,
        w_code,
        w,
        v.get("phonetic", ""),
        v.get("meaning", ""),
        v.get("category", ""),
        f"card_{v['id']}.gif",
        s1,
        t1,
        s2,
        t2,
        s3,
        t3,
        audio_info,
        action,
        prompt,
        neg,
        specs
    ]
    rows_data.append(row)

# 1. Write CSV
print("Writing KaiSpeak_500_Vocab_Realistic_GIF_Prompts.csv...")
with open('KaiSpeak_500_Vocab_Realistic_GIF_Prompts.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    writer.writerow([h.replace('\n', ' ') for h in new_headers])
    for r in rows_data:
        writer.writerow(r)
print("CSV saved successfully.")

# 2. Write Excel with nice styles
print("Writing KaiSpeak_500_Vocab_Realistic_GIF_Prompts.xlsx...")
wb_new = openpyxl.Workbook()
ws_new = wb_new.active
ws_new.title = "500單字系統編碼與例句庫"

header_fill = PatternFill(start_color="1E3A8A", end_color="1E3A8A", fill_type="solid")
header_font = Font(name="Microsoft JhengHei", size=10, bold=True, color="FFFFFF")
cell_font = Font(name="Microsoft JhengHei", size=9)
code_font = Font(name="Courier New", size=9, bold=True, color="1E3A8A")

thin_border = Border(
    left=Side(style='thin', color='E2E8F0'),
    right=Side(style='thin', color='E2E8F0'),
    top=Side(style='thin', color='E2E8F0'),
    bottom=Side(style='thin', color='E2E8F0')
)

ws_new.append(new_headers)

for row_idx, r in enumerate(rows_data, start=2):
    ws_new.append(r)
    for col_idx in range(1, len(r) + 1):
        cell = ws_new.cell(row=row_idx, column=col_idx)
        cell.border = thin_border
        if col_idx in [2, 14]:
            cell.font = code_font
        else:
            cell.font = cell_font
        if col_idx in [1, 2, 6, 7]:
            cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        else:
            cell.alignment = Alignment(vertical="center", wrap_text=True)

# Format headers
for col_idx in range(1, len(new_headers) + 1):
    cell = ws_new.cell(row=1, column=col_idx)
    cell.fill = header_fill
    cell.font = header_font
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

ws_new.freeze_panes = "C2"

col_widths = {
    1: 8,   # No
    2: 14,  # System Code
    3: 14,  # Word
    4: 12,  # Phonetic
    5: 22,  # Meaning
    6: 14,  # Category
    7: 18,  # Filename
    8: 24,  # L1
    9: 24,  # L1 trans
    10: 28, # L2
    11: 28, # L2 trans
    12: 36, # L3
    13: 36, # L3 trans
    14: 38, # Audio Info
    15: 45, # Action
    16: 55, # Prompt
    17: 25, # Negative
    18: 25  # Specs
}
for col_idx, width in col_widths.items():
    col_letter = openpyxl.utils.get_column_letter(col_idx)
    ws_new.column_dimensions[col_letter].width = width

wb_new.save('KaiSpeak_500_Vocab_Realistic_GIF_Prompts.xlsx')
print("Excel saved successfully with systematic codes and simplified sentences!")
