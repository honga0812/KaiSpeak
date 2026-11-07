import json
import os
import subprocess
import shutil
from concurrent.futures import ThreadPoolExecutor

os.makedirs("audio", exist_ok=True)

with open("vocab.json", "r", encoding="utf-8") as f:
    vocab = json.load(f)

tasks = []

# 1. 50 words
for w in vocab:
    w_id = w["id"]
    w_text = w["word"]
    out_m4a = f"audio/word_{w_id}.m4a"
    if not os.path.exists(out_m4a) or os.path.getsize(out_m4a) < 500:
        tasks.append((f"word_{w_id}", w_text, 150, out_m4a))

# 2. 450 sentences (3 scenarios x 3 sentences each)
for w in vocab:
    w_id = w["id"]
    for s_idx, sc in enumerate(w.get("scenarios", [])):
        for sent_idx, sent_text in enumerate(sc.get("sentences", [])):
            out_m4a = f"audio/sentence_{w_id}_{s_idx}_{sent_idx}.m4a"
            if not os.path.exists(out_m4a) or os.path.getsize(out_m4a) < 500:
                tasks.append((f"sentence_{w_id}_{s_idx}_{sent_idx}", sent_text, 160, out_m4a))

print(f"Total audio generation tasks to process: {len(tasks)}")

def process_task(task):
    task_id, text, rate, out_m4a = task
    try:
        # say directly outputs .m4a
        subprocess.run(
            ["say", "-v", "Samantha", "-r", str(rate), "-o", out_m4a, text],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return True
    except Exception as e:
        print(f"Error on {task_id}: {e}")
        return False

with ThreadPoolExecutor(max_workers=6) as executor:
    results = list(executor.map(process_task, tasks))

success_count = sum(1 for r in results if r)
print(f"Successfully generated {success_count}/{len(tasks)} audio files!")

# Backward compatibility copy
for w in vocab:
    w_id = w["id"]
    for s_idx in range(3):
        src = f"audio/sentence_{w_id}_{s_idx}_0.m4a"
        dst = f"audio/sentence_{w_id}_{s_idx}.m4a"
        if os.path.exists(src) and not os.path.exists(dst):
            shutil.copyfile(src, dst)

print("Audio library setup complete!")
