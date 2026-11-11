# -*- coding: utf-8 -*-
"""Master Execution Pipeline:
1. Merge 500 words with simplified sentences (L1: 3-4w, L2: 4-6w, L3: 6-8w).
2. Assign systematic codes (EN_W0001 ~ EN_W0500, EN_W0001_S1 ~ S3).
3. Synthesize Samantha audio for all modified sentences in parallel.
4. Populate canonical and legacy audio paths.
5. Save audio_manifest.json and vocab.json.
"""

import os
import json
import shutil
import hashlib
import subprocess
from concurrent.futures import ThreadPoolExecutor

from builder_part1 import PART_1_DATA
from builder_part2 import PART_2_DATA
from builder_part3 import PART_3_DATA
from builder_part4 import PART_4_DATA
from builder_part5 import PART_5_DATA

os.makedirs("audio", exist_ok=True)
os.makedirs("audio/words", exist_ok=True)
os.makedirs("audio/sentences", exist_ok=True)

# Merge all curated sentence data
ALL_CURATED = {}
for p in [PART_1_DATA, PART_2_DATA, PART_3_DATA, PART_4_DATA, PART_5_DATA]:
    ALL_CURATED.update(p)

print(f"Loaded {len(ALL_CURATED)} curated sentence sets.")

with open("vocab.json", "r", encoding="utf-8") as f:
    vocab = json.load(f)

def md5_str(s):
    return hashlib.md5(s.strip().lower().encode('utf-8')).hexdigest()

manifest = {}
if os.path.exists("audio_manifest.json"):
    try:
        with open("audio_manifest.json", "r", encoding="utf-8") as f:
            manifest = json.load(f)
    except Exception:
        manifest = {}

LEVEL_LABELS = {
    1: ("難度 1 · 簡單初階", "基礎入門短句（適合低年級/初學啟蒙）", "簡單 · 初階短句", "簡單"),
    2: ("難度 2 · 中等日常", "生活日常情境（適合鞏固日常口語表達）", "中等 · 生活日常", "中等"),
    3: ("難度 3 · 熟練挑戰", "拓展思維進階（建議連續登錄多日後挑戰）", "進階 · 熟練挑戰", "進階")
}

audio_tasks = []

for idx, item in enumerate(vocab):
    w_id = item["id"]
    w_word = item["word"]
    num = idx + 1
    w_code = f"EN_W{num:04d}"
    item["wordCode"] = w_code
    item["lang"] = "en-US"

    curated = ALL_CURATED[w_word]

    # Word Audio Paths
    w_canonical = f"audio/words/{w_code.lower()}_{w_id}.m4a"
    w_legacy = f"audio/word_{w_id}.m4a"
    item["audioWord"] = w_legacy
    item["audioWordCanonical"] = w_canonical

    # Check word audio
    w_hash = md5_str(w_word)
    w_manifest_entry = manifest.get(w_code)
    if not os.path.exists(w_legacy) or os.path.getsize(w_legacy) < 1000 or not w_manifest_entry or w_manifest_entry.get("hash") != w_hash:
        audio_tasks.append((w_code, w_word, 145, w_legacy, [w_canonical], "word"))
    else:
        if not os.path.exists(w_canonical) or os.path.getsize(w_canonical) != os.path.getsize(w_legacy):
            shutil.copyfile(w_legacy, w_canonical)

    # Scenarios and GradedSentences
    new_scenarios = []
    new_graded = []

    for s_idx in range(3):
        lvl = s_idx + 1
        s_code = f"{w_code}_S{lvl}"
        s_text = curated[f"s{lvl}"]
        s_trans = curated[f"t{lvl}"]
        s_hash = md5_str(s_text)

        tag, desc, lvl_label, short_tag = LEVEL_LABELS[lvl]

        s_canonical = f"audio/sentences/{w_code.lower()}_s{lvl}_{w_id}.m4a"
        s_legacy_0 = f"audio/sentence_{w_id}_{s_idx}_0.m4a"
        s_legacy = f"audio/sentence_{w_id}_{s_idx}.m4a"

        new_scenarios.append({
            "tag": tag,
            "desc": desc,
            "sentences": [s_text],
            "translations": [s_trans]
        })

        new_graded.append({
            "level": lvl,
            "levelLabel": lvl_label,
            "tag": short_tag,
            "text": s_text,
            "translation": s_trans,
            "sentenceCode": s_code,
            "audioSrc": s_legacy_0,
            "audioSrcCanonical": s_canonical,
            "textHash": s_hash
        })

        s_manifest_entry = manifest.get(s_code)
        needs_audio = (
            (not os.path.exists(s_legacy_0)) or
            (os.path.getsize(s_legacy_0) < 1000) or
            (not s_manifest_entry) or
            (s_manifest_entry.get("hash") != s_hash) or
            (idx < 200) # Force regenerate words 0-199 to replace legacy bad audio!
        )

        if needs_audio:
            audio_tasks.append((s_code, s_text, 155, s_legacy_0, [s_canonical, s_legacy], "sentence"))
        else:
            if not os.path.exists(s_canonical) or os.path.getsize(s_canonical) != os.path.getsize(s_legacy_0):
                shutil.copyfile(s_legacy_0, s_canonical)
            if not os.path.exists(s_legacy) or os.path.getsize(s_legacy) != os.path.getsize(s_legacy_0):
                shutil.copyfile(s_legacy_0, s_legacy)

    item["scenarios"] = new_scenarios
    item["gradedSentences"] = new_graded

print(f"Total audio synthesis tasks queued: {len(audio_tasks)}")

def execute_audio_task(t):
    code, text, rate, primary_path, alias_paths, kind = t
    try:
        res = subprocess.run(
            ["say", "-v", "Samantha", "-r", str(rate), "-o", primary_path, text],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        if res.returncode != 0:
            return (code, False, f"Returncode {res.returncode}")
        
        for a in alias_paths:
            shutil.copyfile(primary_path, a)
            
        return (code, True, None)
    except Exception as e:
        return (code, False, str(e))

if audio_tasks:
    print(f"Running parallel synthesis with 14 workers on {len(audio_tasks)} tasks...")
    with ThreadPoolExecutor(max_workers=14) as ex:
        results = list(ex.map(execute_audio_task, audio_tasks))
    
    succ = sum(1 for r in results if r[1])
    fail = sum(1 for r in results if not r[1])
    print(f"Synthesis finished! Success: {succ}, Failed: {fail}")
    if fail > 0:
        for r in results:
            if not r[1]:
                print(f"  Error on {r[0]}: {r[2]}")

# Build audio_manifest.json
print("Writing audio_manifest.json...")
new_manifest = {}
for idx, item in enumerate(vocab):
    w_code = item["wordCode"]
    w_id = item["id"]
    new_manifest[w_code] = {
        "code": w_code,
        "lang": "en-US",
        "word": item["word"],
        "text": item["word"],
        "hash": md5_str(item["word"]),
        "voice": "Samantha",
        "rate": 145,
        "file": f"audio/words/{w_code.lower()}_{w_id}.m4a",
        "legacyFile": f"audio/word_{w_id}.m4a"
    }

    for s_idx in range(3):
        lvl = s_idx + 1
        s_code = f"{w_code}_S{lvl}"
        s_text = item["scenarios"][s_idx]["sentences"][0]
        new_manifest[s_code] = {
            "code": s_code,
            "lang": "en-US",
            "word": item["word"],
            "level": lvl,
            "text": s_text,
            "hash": md5_str(s_text),
            "voice": "Samantha",
            "rate": 155,
            "file": f"audio/sentences/{w_code.lower()}_s{lvl}_{w_id}.m4a",
            "legacyFile": f"audio/sentence_{w_id}_{s_idx}_0.m4a"
        }

with open("audio_manifest.json", "w", encoding="utf-8") as f:
    json.dump(new_manifest, f, ensure_ascii=False, indent=2)

print(f"Saved audio_manifest.json with {len(new_manifest)} entries.")

# Save vocab.json
with open("vocab.json", "w", encoding="utf-8") as f:
    json.dump(vocab, f, ensure_ascii=False, indent=2)

print("Saved updated vocab.json successfully!")
