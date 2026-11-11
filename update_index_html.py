# -*- coding: utf-8 -*-
"""Update index.html with new MASTER_VOCAB, streak gating, and difficulty badges."""

import re
import json

print("Reading vocab.json...")
with open("vocab.json", "r", encoding="utf-8") as f:
    vocab = json.load(f)

print(f"Loaded {len(vocab)} words.")

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Replace MASTER_VOCAB
pos_start = content.find("const MASTER_VOCAB = [")
if pos_start == -1:
    raise ValueError("const MASTER_VOCAB not found in index.html")

pos_semicolon = content.find(";\n", pos_start)
if pos_semicolon == -1:
    pos_semicolon = content.find(";", pos_start)

vocab_json_str = json.dumps(vocab, ensure_ascii=False)
new_master_vocab_str = f"const MASTER_VOCAB = {vocab_json_str};"

content = content[:pos_start] + new_master_vocab_str + content[pos_semicolon + 1:]
print("Updated const MASTER_VOCAB in index.html.")

# 2. Update getAdaptiveAnalysis
target_adaptive_start = "function getAdaptiveAnalysis(profile) {"
pos_adapt = content.find(target_adaptive_start)
if pos_adapt != -1:
    # Find matching closing brace or function boundary
    pos_adapt_end = content.find("function updateAdaptiveBadgeUI() {", pos_adapt)
    if pos_adapt_end != -1:
        new_adaptive_fn = """function getAdaptiveAnalysis(profile) {
      const p = profile || getActiveProfile();
      const history = p.scoreHistory || [];
      const streak = p.streakDays || 1;

      if (history.length === 0) {
        return {
          level: 1,
          title: "🟢 基礎入門（極簡短句）",
          desc: "初期啟蒙階段：專注 3~4 詞極簡例句，保護發音開口自信心！（連續登錄練習滿 5 天解鎖日常句，滿 14 天解鎖熟練挑戰句）",
          badgeClass: "bg-emerald-100 text-emerald-800 border-emerald-300",
          avgScore: 80,
          accuracyPct: 100
        };
      }

      const recent = history.slice(-10);
      const avg = Math.round(recent.reduce((a, b) => a + b, 0) / recent.length);
      const goodCount = recent.filter(s => s >= 75).length;
      const accuracyPct = Math.round((goodCount / recent.length) * 100);

      // Low score or low accuracy -> strictly downgrade to Level 1
      if (avg < 73 || accuracyPct < 60) {
        return {
          level: 1,
          title: "🟢 基礎入門（極簡短句）",
          desc: `近期平均 ${avg} 分 · 正確率 ${accuracyPct}%。智能降階為 3~4 詞初階短句，減輕負擔、鞏固基礎！`,
          badgeClass: "bg-emerald-100 text-emerald-800 border-emerald-300",
          avgScore: avg,
          accuracyPct
        };
      }

      // 熟練挑戰句（Level 3）：必須同時滿足「連續登錄 14 天以上」且「近期平均 85 分以上、正確率 80% 以上」才晉升解鎖！
      if (streak >= 14 && avg >= 85 && accuracyPct >= 80) {
        return {
          level: 3,
          title: "🟣 熟練挑戰（進階適配）",
          desc: `連續登錄 ${streak} 天 · 近期平均 ${avg} 分！已達成高度熟練，解鎖進階挑戰句型！`,
          badgeClass: "bg-purple-100 text-purple-800 border-purple-300",
          avgScore: avg,
          accuracyPct
        };
      }

      // 生活日常句（Level 2）：連續登錄 5 天以上且平均 75 分以上
      if (streak >= 5 && avg >= 75) {
        return {
          level: 2,
          title: "🟡 生活日常（中階情境）",
          desc: `連續登錄 ${streak} 天 · 近期平均 ${avg} 分。日常情境句型，穩定提升聽讀流暢度！（滿 14 天解鎖進階挑戰）`,
          badgeClass: "bg-amber-100 text-amber-800 border-amber-300",
          avgScore: avg,
          accuracyPct
        };
      }

      // 初期入門（嚴格適配 3~4 詞短句，保護開口自信心）
      return {
        level: 1,
        title: "🟢 基礎入門（極簡短句）",
        desc: `連續登錄 ${streak} 天 · 近期平均 ${avg} 分。專注 3~4 詞極簡例句，保護發音自信心！（連續登錄滿 5 天解鎖日常句）`,
        badgeClass: "bg-emerald-100 text-emerald-800 border-emerald-300",
        avgScore: avg,
        accuracyPct
      };
    }

    """
        content = content[:pos_adapt] + new_adaptive_fn + content[pos_adapt_end:]
        print("Updated getAdaptiveAnalysis with streak-gated progression.")

# 3. Update initQuestQueue streak-gated sentence selection
target_init_queue = "// Assign 2 age-appropriate sentences according to the child's adaptive level!"
pos_iq = content.find(target_init_queue)
if pos_iq != -1:
    pos_iq_end = content.find("return {", pos_iq)
    if pos_iq_end != -1:
        new_iq_selection = """// Assign 2 age-appropriate sentences according to the child's adaptive level and streak!
      const userStreak = activeP.streakDays || 1;
      questQueue = selected.map(wordObj => {
        const g = wordObj.gradedSentences;
        let picked = [];
        if (userLevel === 1 || userStreak < 5) {
          // 初期入門 (連續天數 < 5 或初階)：嚴格鎖定 Level 1 + Level 2，絕不出現 Level 3 拓展句！
          picked = [
            { text: g[0].text, translation: g[0].translation, level: 1, levelLabel: "簡單 · 初階短句", audioSrc: g[0].audioSrc },
            { text: g[1].text, translation: g[1].translation, level: 2, levelLabel: "中等 · 生活日常", audioSrc: g[1].audioSrc }
          ];
        } else if (userLevel === 2 || userStreak < 14) {
          // 中期生活日常 (5 <= streak < 14)：Level 1 + Level 2 鞏固日常
          picked = [
            { text: g[0].text, translation: g[0].translation, level: 1, levelLabel: "簡單 · 初階短句", audioSrc: g[0].audioSrc },
            { text: g[1].text, translation: g[1].translation, level: 2, levelLabel: "中等 · 生活日常", audioSrc: g[1].audioSrc }
          ];
        } else {
          // 連續登錄 14+ 天且表現優異者：解鎖 Level 2 + Level 3 熟練挑戰！
          picked = [
            { text: g[1].text, translation: g[1].translation, level: 2, levelLabel: "中等 · 生活日常", audioSrc: g[1].audioSrc },
            { text: g[2].text, translation: g[2].translation, level: 3, levelLabel: "進階 · 熟練挑戰", audioSrc: g[2].audioSrc }
          ];
        }

        """
        content = content[:pos_iq] + new_iq_selection + content[pos_iq_end:]
        print("Updated initQuestQueue with streak-gated sentence assignment.")

# 4. Update Free Practice scenario tabs with descriptive badges
content = content.replace(
    '🟢 難度 1 · 簡單',
    '🟢 難度 1 · 簡單啟蒙 (推薦初期)'
)
content = content.replace(
    '🟡 難度 2 · 中等',
    '🟡 難度 2 · 生活日常 (進階)'
)
content = content.replace(
    '🟣 難度 3 · 進階',
    '🟣 難度 3 · 熟練挑戰 (連續登錄解鎖)'
)

# 5. Bump cache buster
content = re.sub(r'v=27', 'v=28', content)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("index.html successfully updated and saved!")
