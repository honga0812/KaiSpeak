import json
import opencc

cc = opencc.OpenCC('s2twp')

# 1. Convert vocab.json
with open('vocab.json', 'r', encoding='utf-8') as f:
    vocab = json.load(f)

def convert_obj(obj):
    if isinstance(obj, str):
        return cc.convert(obj)
    elif isinstance(obj, list):
        return [convert_obj(x) for x in obj]
    elif isinstance(obj, dict):
        return {k: convert_obj(v) for k, v in obj.items()}
    return obj

converted_vocab = convert_obj(vocab)

with open('vocab.json', 'w', encoding='utf-8') as f:
    json.dump(converted_vocab, f, ensure_ascii=False, indent=2)

print("Converted vocab.json to Traditional Chinese successfully!")

# 2. Convert build_full_app.py
with open('build_full_app.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Convert content
# Note: opencc will convert Chinese characters while keeping English and code symbols intact
converted_content = cc.convert(content)

# Specifically ensure lang="zh-Hant-TW"
converted_content = converted_content.replace('lang="zh-CN"', 'lang="zh-Hant-TW"')

with open('build_full_app.py', 'w', encoding='utf-8') as f:
    f.write(converted_content)

print("Converted build_full_app.py to Traditional Chinese successfully!")
