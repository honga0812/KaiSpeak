# -*- coding: utf-8 -*-
import json
import re

from builder_part1 import PART_1_DATA
from builder_part2 import PART_2_DATA
from builder_part3 import PART_3_DATA
from builder_part4 import PART_4_DATA
from builder_part5 import PART_5_DATA

ALL_DATA = {}
for part in [PART_1_DATA, PART_2_DATA, PART_3_DATA, PART_4_DATA, PART_5_DATA]:
    for k, v in part.items():
        if k in ALL_DATA:
            print(f"DUPLICATE KEY: {k}")
        ALL_DATA[k] = v

print(f"Total curated words merged: {len(ALL_DATA)}")

with open('vocab.json', 'r', encoding='utf-8') as f:
    vocab = json.load(f)

vocab_words = [x['word'] for x in vocab]
print(f"Total words in vocab.json: {len(vocab_words)}")

missing = set(vocab_words) - set(ALL_DATA.keys())
extra = set(ALL_DATA.keys()) - set(vocab_words)
if missing:
    print(f"MISSING WORDS ({len(missing)}): {missing}")
if extra:
    print(f"EXTRA WORDS ({len(extra)}): {extra}")

banned = [
    'fragrant', 'ceramic', 'delightfully', 'translucent', 'sturdy', 'subtle', 'intricate',
    'harmonious', 'sculpture', 'silhouette', 'precise', 'elegantly', 'luminous', 'serene',
    'brilliant', 'exquisite', 'captivating', 'breathtaking', 'magnificent', 'fascinating',
    'invigorating', 'effervescent', 'splendid', 'impeccable', 'majestic', 'astounding'
]

errors = []
for idx, w in enumerate(vocab_words):
    item = ALL_DATA.get(w)
    if not item:
        errors.append(f"#{idx+1} {w} not found in ALL_DATA!")
        continue
    s1, s2, s3 = item['s1'], item['s2'], item['s3']
    w1, w2, w3 = len(s1.split()), len(s2.split()), len(s3.split())
    if not (3 <= w1 <= 4):
        errors.append(f"#{idx+1} {w} L1 length {w1} not in [3, 4]: {s1}")
    if not (4 <= w2 <= 6):
        errors.append(f"#{idx+1} {w} L2 length {w2} not in [4, 6]: {s2}")
    if not (6 <= w3 <= 8):
        errors.append(f"#{idx+1} {w} L3 length {w3} not in [6, 8]: {s3}")
    
    # Check banned words
    for s_idx, sent in enumerate([s1, s2, s3]):
        words_in_sent = [x.lower().strip(".,!?\"'") for x in sent.split()]
        for b in banned:
            if b in words_in_sent:
                errors.append(f"#{idx+1} {w} L{s_idx+1} contains banned word '{b}': {sent}")

if errors:
    print(f"FOUND {len(errors)} ERRORS:")
    for e in errors[:10]:
        print("  -", e)
    raise SystemExit(1)
else:
    print("ALL 500 WORDS & 1,500 SENTENCES PASSED 100% STRICT VALIDATION!")
