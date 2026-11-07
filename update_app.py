# update_app.py
import json

with open("vocab.json", "r", encoding="utf-8") as f:
    vocab_data = json.load(f)

vocab_json_str = json.dumps(vocab_data, ensure_ascii=False)

html_template = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
  <meta http-equiv="Pragma" content="no-cache">
  <meta http-equiv="Expires" content="0">
  <title>KaiSpeak - 50核心词库 · 450情境例句 · 智能少儿英语系统 (v1.1)</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@400;600;700&family=Noto+Sans+SC:wght@400;500;700&display=swap" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/qrcode@1.5.3/build/qrcode.min.js"></script>
  <style>
    body {
      font-family: 'Fredoka', 'Noto Sans SC', sans-serif;
      background: linear-gradient(135deg, #EEF2FF 0%, #F5F3FF 50%, #EDE9FE 100%);
    }
    .pulse-ring {
      animation: pulse 1.2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
    }
    @keyframes pulse {
      0%, 100% { transform: scale(1); opacity: 0.8; }
      50% { transform: scale(1.22); opacity: 0.2; }
    }
    .hide-scrollbar::-webkit-scrollbar { display: none; }
    .hide-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }
  </style>
</head>
<body class="min-h-screen text-slate-800 p-3 md:p-6 flex flex-col items-center">

  <!-- Top Global Bar -->
  <header class="w-full max-w-5xl bg-white/95 backdrop-blur rounded-3xl p-4 shadow-sm border border-indigo-100 mb-4 flex flex-wrap items-center justify-between gap-3">
    <div class="flex items-center gap-3">
      <div class="w-12 h-12 bg-gradient-to-tr from-indigo-600 to-violet-600 rounded-2xl flex items-center justify-center text-white text-2xl shadow-md shadow-indigo-200">
        🎙️
      </div>
      <div>
        <h1 class="text-xl font-black text-indigo-950 tracking-wide flex items-center gap-2">
          KaiSpeak
          <span class="text-xs bg-indigo-100 text-indigo-700 px-2.5 py-0.5 rounded-full font-bold">50 词库 · 450 情境例句</span>
        </h1>
        <p class="text-xs text-slate-500">每词 3 大情境 × 3 条精选例句 (共9句) · 智能任务 · 错词本</p>
      </div>
    </div>

    <!-- Mode Selector Tabs -->
    <nav class="flex bg-slate-100 p-1.5 rounded-2xl text-xs font-bold gap-1 shadow-inner">
      <button id="navQuestBtn" onclick="switchAppMode('quest')" class="px-3.5 py-2 rounded-xl bg-indigo-600 text-white shadow-sm transition flex items-center gap-1.5">
        🎯 每日任务 (10新+8复+2固)
      </button>
      <button id="navFreeBtn" onclick="switchAppMode('free')" class="px-3.5 py-2 rounded-xl text-slate-600 hover:text-slate-900 transition flex items-center gap-1.5">
        📚 50词自由库与错词本
      </button>
      <button id="navAdventureBtn" onclick="switchAppMode('adventure')" class="px-3.5 py-2 rounded-xl text-slate-600 hover:text-slate-900 transition flex items-center gap-1.5">
        🗺️ 50关探险岛
      </button>
    </nav>

    <!-- Right Quick Actions -->
    <div class="flex items-center gap-2">
      <button onclick="toggleMobileModal()" class="p-2 rounded-xl border border-slate-200 hover:bg-slate-50 text-slate-600 text-xs font-semibold flex items-center gap-1 transition">
        📱 <span class="hidden sm:inline">手机连线</span>
      </button>
      <button onclick="toggleLogModal()" class="p-2 rounded-xl border border-slate-200 hover:bg-slate-50 text-slate-600 text-xs font-semibold flex items-center gap-1 transition">
        📋 <span class="hidden sm:inline">日志</span> (<span id="logBadge">0</span>)
      </button>
    </div>
  </header>

  <!-- ========================================== -->
  <!-- VIEW 1: DAILY QUEST MODE                   -->
  <!-- ========================================== -->
  <section id="viewQuest" class="w-full max-w-5xl flex flex-col gap-4">
    <div class="bg-gradient-to-r from-indigo-600 via-indigo-700 to-purple-700 text-white p-5 rounded-3xl shadow-lg shadow-indigo-100 flex flex-col md:flex-row items-center justify-between gap-4">
      <div class="flex items-center gap-4">
        <div class="w-14 h-14 bg-white/10 backdrop-blur rounded-2xl flex items-center justify-center text-3xl shadow-inner">
          🎯
        </div>
        <div>
          <div class="flex items-center gap-2">
            <h2 class="text-lg font-bold">今日智能挑战任务 (20 词清单)</h2>
            <span class="text-[10px] bg-amber-400 text-amber-950 font-extrabold px-2 py-0.5 rounded-full">
              🔥 连续打卡 <span id="questStreakDays">3</span> 天
            </span>
          </div>
          <p class="text-xs text-indigo-100 mt-1">
            动态精选：包含 <strong>10 个新学词汇</strong> + <strong>8 个薄弱复习词</strong> + <strong>2 个常态巩固词</strong>
          </p>
        </div>
      </div>

      <div class="flex items-center gap-3 bg-white/10 backdrop-blur px-4 py-2.5 rounded-2xl border border-white/10 w-full md:w-auto justify-between">
        <div class="text-right">
          <div class="text-[11px] text-indigo-200">今日完成进度</div>
          <div class="text-base font-extrabold font-mono"><span id="questProgressNum">0</span> / 20 词</div>
        </div>
        <div class="w-24 bg-white/20 h-2.5 rounded-full overflow-hidden">
          <div id="questProgressBar" class="bg-amber-400 h-full rounded-full transition-all duration-500" style="width: 0%"></div>
        </div>
      </div>
    </div>

    <!-- Quest Task Stepper (Horizontal step tracker) -->
    <div class="bg-white/80 backdrop-blur rounded-2xl p-3 border border-slate-100 shadow-sm flex items-center gap-2 overflow-x-auto hide-scrollbar" id="questStepperContainer">
      <!-- 20 step dots populated by JS -->
    </div>
  </section>

  <!-- ========================================== -->
  <!-- VIEW 2: FREE PRACTICE & 50-WORD DATABASE   -->
  <!-- ========================================== -->
  <section id="viewFree" class="w-full max-w-5xl hidden flex-col gap-4">
    <div class="bg-white rounded-3xl p-5 shadow-sm border border-slate-100 flex flex-col md:flex-row items-center justify-between gap-4">
      <div>
        <h2 class="text-lg font-bold text-slate-800 flex items-center gap-2">
          📚 50 个少儿全景词汇库
        </h2>
        <p class="text-xs text-slate-500 mt-1">覆盖 6 大生活主题与 Phonics 阶梯，支持错词本集中攻坚</p>
      </div>

      <!-- Category Filter Pills -->
      <div class="flex items-center gap-1.5 overflow-x-auto hide-scrollbar text-xs">
        <button onclick="setFreeCategory('all')" class="free-cat-btn active px-3 py-1.5 rounded-xl font-bold bg-indigo-600 text-white shadow-sm whitespace-nowrap" data-cat="all">全部 (50)</button>
        <button onclick="setFreeCategory('weak')" class="free-cat-btn px-3 py-1.5 rounded-xl font-bold bg-rose-50 text-rose-700 border border-rose-200 hover:bg-rose-100 whitespace-nowrap" data-cat="weak">⚠️ 错词本 (<span id="weakCountBadge">0</span>)</button>
        <button onclick="setFreeCategory('home')" class="free-cat-btn px-3 py-1.5 rounded-xl font-semibold bg-slate-100 text-slate-600 hover:bg-slate-200 whitespace-nowrap" data-cat="home">🏠 家居 (8)</button>
        <button onclick="setFreeCategory('food')" class="free-cat-btn px-3 py-1.5 rounded-xl font-semibold bg-slate-100 text-slate-600 hover:bg-slate-200 whitespace-nowrap" data-cat="food">🍎 饮食 (8)</button>
        <button onclick="setFreeCategory('animals')" class="free-cat-btn px-3 py-1.5 rounded-xl font-semibold bg-slate-100 text-slate-600 hover:bg-slate-200 whitespace-nowrap" data-cat="animals">🐱 动物 (9)</button>
        <button onclick="setFreeCategory('nature')" class="free-cat-btn px-3 py-1.5 rounded-xl font-semibold bg-slate-100 text-slate-600 hover:bg-slate-200 whitespace-nowrap" data-cat="nature">🌳 自然 (8)</button>
        <button onclick="setFreeCategory('play')" class="free-cat-btn px-3 py-1.5 rounded-xl font-semibold bg-slate-100 text-slate-600 hover:bg-slate-200 whitespace-nowrap" data-cat="play">⚽ 玩乐 (9)</button>
      </div>
    </div>

    <!-- 50 Word Cards Grid -->
    <div id="freeGridContainer" class="grid grid-cols-4 sm:grid-cols-5 md:grid-cols-10 gap-2">
      <!-- 50 Word buttons populated by JS -->
    </div>
  </section>

  <!-- ========================================== -->
  <!-- VIEW 3: 50-LEVEL ADVENTURE MAP            -->
  <!-- ========================================== -->
  <section id="viewAdventure" class="w-full max-w-5xl hidden flex-col gap-4">
    <div class="bg-gradient-to-br from-emerald-500 via-teal-600 to-indigo-700 text-white p-6 rounded-3xl shadow-xl relative overflow-hidden">
      <div class="relative z-10 flex flex-col md:flex-row items-center justify-between gap-4">
        <div>
          <span class="text-xs font-bold uppercase tracking-wider bg-white/20 px-3 py-1 rounded-full">50-Stage Adventure</span>
          <h2 class="text-2xl font-black mt-2">英语发音大探险：50关语音群岛</h2>
          <p class="text-xs text-emerald-100 mt-1">横跨 5 大语音岛屿（小屋岛、美食镇、萌宠园、森林谷、乐园岛），80分即可过关点亮三星！</p>
        </div>
        <div class="bg-white/10 backdrop-blur px-5 py-3 rounded-2xl border border-white/20 text-center">
          <div class="text-xs text-emerald-200">当前总星数</div>
          <div class="text-2xl font-black text-amber-300">⭐ <span id="adventureTotalStars">24</span> / 150</div>
        </div>
      </div>

      <!-- 50 Level Nodes Grid -->
      <div class="relative z-10 mt-6 grid grid-cols-4 sm:grid-cols-5 md:grid-cols-10 gap-2.5 max-h-[380px] overflow-y-auto pr-1" id="adventureNodesContainer">
        <!-- 50 Level Nodes populated by JS -->
      </div>
    </div>
  </section>

  <!-- ======================================================== -->
  <!-- MAIN WORKSPACE: WORD CARD + 3 CONTEXTS x 3 SENTENCES     -->
  <!-- ======================================================== -->
  <main class="w-full max-w-5xl grid grid-cols-1 md:grid-cols-12 gap-6 mt-4">
    
    <!-- Left Column: Word & 9 Scenario Sentences (7 Cols) -->
    <div class="md:col-span-7 flex flex-col gap-5">
      
      <!-- Card Container -->
      <div class="bg-white rounded-3xl p-6 shadow-xl shadow-indigo-100/60 border border-indigo-50 relative overflow-hidden">
        
        <!-- Header: Category & Role in Daily Quest -->
        <div class="flex items-center justify-between mb-4">
          <div class="flex items-center gap-2">
            <span id="cardQuestRoleTag" class="px-3 py-1 rounded-full text-xs font-extrabold bg-indigo-100 text-indigo-800">
              🌟 今日新词 (New)
            </span>
            <span id="cardCategoryTag" class="px-2.5 py-0.5 rounded-full text-[10px] font-bold bg-slate-100 text-slate-600">
              🏠 日常起居
            </span>
          </div>
          <div class="flex items-center gap-2">
            <button onclick="prevCard()" class="w-8 h-8 rounded-full border border-slate-200 flex items-center justify-center text-slate-600 hover:bg-slate-100 transition">←</button>
            <span id="cardIndex" class="text-xs font-bold text-slate-500 font-mono">1 / 50</span>
            <button onclick="nextCard()" class="w-8 h-8 rounded-full border border-slate-200 flex items-center justify-center text-slate-600 hover:bg-slate-100 transition">→</button>
          </div>
        </div>

        <!-- Illustration & Word Header -->
        <div class="flex flex-col sm:flex-row items-center gap-6 mb-5">
          <div id="wordIllustration" class="w-28 h-28 bg-gradient-to-tr from-amber-50 to-orange-100 rounded-2xl flex items-center justify-center text-6xl shadow-inner border border-amber-200/60 select-none">
            🪑
          </div>
          <div class="text-center sm:text-left flex-1">
            <div class="flex items-center justify-center sm:justify-start gap-3">
              <h2 id="wordText" class="text-4xl font-extrabold text-slate-800 tracking-wide">desk</h2>
              <button onclick="playAudio('word')" title="播放真人母语纯正发音" class="px-3 py-1.5 rounded-full bg-indigo-50 hover:bg-indigo-100 text-indigo-700 flex items-center gap-1.5 text-xs font-bold transition shadow-sm border border-indigo-200/60">
                🔊 听真人单字
              </button>
            </div>
            <p id="wordPhonetic" class="text-sm font-medium text-indigo-500 mt-1 font-mono tracking-wider">/dɛsk/</p>
            <p id="wordMeaning" class="text-sm text-slate-500 mt-1">名词：书桌，办公桌</p>
            <div class="mt-2 text-[11px] text-slate-400">
              历史表现：已练 <strong id="wordPracticeCount" class="text-indigo-600">0</strong> 次 · 最高 <strong id="wordBestScore" class="text-emerald-600">--</strong> 分 · 状态：<strong id="wordStatusTag" class="text-slate-600">待练习</strong>
            </div>
          </div>
        </div>

        <!-- LEVEL 1 SELECTOR: 3 Context Scenarios + Word Mode -->
        <div class="space-y-2 mb-3">
          <div class="text-xs font-bold text-slate-600 flex justify-between items-center px-1">
            <span>第一步：选择情境主题 (3 种生活场景)</span>
            <span class="text-indigo-600 text-[11px] font-semibold">每个情境配备 3 个例句</span>
          </div>

          <div class="grid grid-cols-4 gap-1.5 bg-slate-100 p-1.5 rounded-2xl text-xs font-semibold">
            <button id="scTabWord" onclick="selectPracticeMode('word')" class="py-2 rounded-xl text-slate-600 hover:text-slate-900 transition text-center truncate px-1">
              单字精读
            </button>
            <button id="scTab0" onclick="selectScenarioTab(0)" class="py-2 rounded-xl bg-white text-indigo-700 shadow-sm transition text-center truncate px-1 font-bold">
              情境一 · 描述
            </button>
            <button id="scTab1" onclick="selectScenarioTab(1)" class="py-2 rounded-xl text-slate-600 hover:text-slate-900 transition text-center truncate px-1">
              情境二 · 动作
            </button>
            <button id="scTab2" onclick="selectScenarioTab(2)" class="py-2 rounded-xl text-slate-600 hover:text-slate-900 transition text-center truncate px-1">
              情境三 · 对话
            </button>
          </div>
        </div>

        <!-- LEVEL 2 SELECTOR: 3 Sentences within current scenario -->
        <div id="sentenceSubSelector" class="space-y-1.5 mb-4">
          <div class="text-[11px] font-bold text-slate-500 flex justify-between items-center px-1">
            <span>第二步：选择要跟读的例句 (该情境下共有 3 个句子)：</span>
          </div>
          <div class="grid grid-cols-3 gap-1.5 bg-indigo-50/60 p-1 rounded-xl text-xs font-medium">
            <button id="sentSub0" onclick="selectSentenceIndex(0)" class="py-1.5 rounded-lg bg-indigo-600 text-white font-bold transition text-center truncate px-1">
              例句 1 (基础)
            </button>
            <button id="sentSub1" onclick="selectSentenceIndex(1)" class="py-1.5 rounded-lg text-indigo-900 hover:bg-indigo-100 transition text-center truncate px-1">
              例句 2 (进阶)
            </button>
            <button id="sentSub2" onclick="selectSentenceIndex(2)" class="py-1.5 rounded-lg text-indigo-900 hover:bg-indigo-100 transition text-center truncate px-1">
              例句 3 (拓展)
            </button>
          </div>
        </div>

        <!-- Current Target Box -->
        <div class="p-4 rounded-2xl bg-indigo-50/70 border border-indigo-100 mb-4">
          <div class="flex items-center justify-between mb-1.5">
            <span id="targetTag" class="text-[10px] font-bold uppercase tracking-wider text-indigo-700 bg-indigo-100 px-2 py-0.5 rounded">
              场景一 · 认知特征描述 (例句 1/3)
            </span>
            <span class="text-[11px] text-slate-400">大声朗读下方内容</span>
          </div>
          <div class="flex items-start justify-between gap-3">
            <div class="flex-1">
              <p id="targetSentence" class="text-xl md:text-2xl font-bold text-indigo-950 leading-snug">This is a clean wooden desk.</p>
              <div class="mt-2 flex items-baseline gap-2">
                <span class="text-[10px] font-extrabold uppercase px-1.5 py-0.5 rounded bg-indigo-200/60 text-indigo-800 tracking-wider">译文对照</span>
                <p id="targetTranslationText" class="text-sm md:text-base font-medium text-slate-600">这是一张干净的木质书桌。</p>
              </div>
            </div>
            <button onclick="playAudio('target')" class="px-3.5 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-700 text-white text-xs font-bold flex items-center gap-1.5 transition shadow-sm whitespace-nowrap mt-0.5">
              <span>🔊 听真人范读</span>
            </button>
          </div>
        </div>

        <!-- Live Waveform Canvas -->
        <div class="w-full h-11 bg-slate-50 rounded-xl overflow-hidden border border-slate-200/80 mb-4 flex items-center justify-center relative">
          <canvas id="waveformCanvas" class="w-full h-full"></canvas>
          <span id="waveformPlaceholder" class="absolute text-[11px] text-slate-400 font-medium">麦克风声波捕获区（录音时随声音实时跳动）</span>
        </div>

        <!-- Recording & Control Section -->
        <div class="flex flex-col items-center justify-center py-2">
          <div class="relative flex items-center justify-center">
            <div id="pulseRing" class="absolute w-24 h-24 rounded-full bg-rose-400 opacity-0 transition duration-300"></div>
            <button id="recordBtn" onclick="handleRecordClick()" class="relative z-10 w-20 h-20 rounded-full bg-gradient-to-tr from-rose-500 to-red-500 hover:from-rose-600 hover:to-red-600 text-white shadow-lg shadow-rose-300/50 flex flex-col items-center justify-center transition transform active:scale-95 focus:outline-none">
              <span id="recordIcon" class="text-2xl">🎙️</span>
              <span id="recordStatus" class="text-[10px] font-bold mt-0.5 tracking-tight">点击录音</span>
            </button>
          </div>
          <p id="recordTip" class="text-xs text-slate-500 mt-2.5 font-medium">
            点击红色麦克风开始录音，念完再次点击停止（支持无限次重录）
          </p>
        </div>

        <!-- Fast Simulation Testing Bar -->
        <div class="mt-4 pt-3 border-t border-slate-100 bg-slate-50/70 -mx-6 -mb-6 p-4 rounded-b-3xl">
          <div class="text-[11px] font-bold text-slate-500 mb-2 flex items-center justify-between">
            <span>⚡ 评测算法快捷验证（一键模拟不同水平）：</span>
          </div>
          <div class="grid grid-cols-3 gap-1.5 text-xs">
            <button onclick="simulateEval('bad')" class="py-1.5 px-2 bg-rose-50 text-rose-700 hover:bg-rose-100 rounded-lg border border-rose-200 font-semibold transition text-center">
              🚫 乱念/含糊杂音<br><span class="text-[10px] opacity-75 font-normal">低分 (0~20分)</span>
            </button>
            <button onclick="simulateEval('wrong_word')" class="py-1.5 px-2 bg-amber-50 text-amber-700 hover:bg-amber-100 rounded-lg border border-amber-200 font-semibold transition text-center">
              ⚠️ 读错关键单词<br><span class="text-[10px] opacity-75 font-normal">精准定位错词标红</span>
            </button>
            <button onclick="simulateEval('good')" class="py-1.5 px-2 bg-emerald-50 text-emerald-700 hover:bg-emerald-100 rounded-lg border border-emerald-200 font-semibold transition text-center">
              ✅ 正确标准朗读<br><span class="text-[10px] opacity-75 font-normal">高分 (92~98分)</span>
            </button>
          </div>
        </div>

      </div>

      <!-- Real Live Speech Recognition Result -->
      <div class="bg-white/90 rounded-2xl p-4 border border-slate-200/80 shadow-sm">
        <div class="flex items-center justify-between text-xs text-slate-500 mb-2">
          <span class="font-bold flex items-center gap-1.5">
            <span id="liveDot" class="w-2 h-2 rounded-full bg-slate-300"></span>
            麦克风实际接收到的内容 (完整聚合)
          </span>
          <span id="statusTimer" class="font-mono text-slate-400">00:00</span>
        </div>
        <div id="liveTranscript" class="text-sm text-slate-700 italic min-h-[36px] p-2.5 bg-slate-50 rounded-xl border border-slate-100 flex items-center">
          等待录音中...
        </div>
        <div id="liveConfidence" class="text-[11px] text-slate-400 mt-1.5 flex justify-between">
          <span>识别置信度：<strong id="confidenceVal" class="text-slate-600">--</strong></span>
          <span>声学响度：<strong id="energyVal" class="text-slate-600">--</strong></span>
        </div>
      </div>

    </div>

    <!-- Right Column: Evaluation & SRS Review Engine (5 Cols) -->
    <div class="md:col-span-5 flex flex-col gap-5">
      
      <!-- Pronunciation Score Card -->
      <div id="resultCard" class="bg-white rounded-3xl p-6 shadow-xl shadow-indigo-100/60 border border-indigo-50 relative">
        <h3 class="text-base font-bold text-slate-800 flex items-center justify-between mb-4">
          <span>发音评估结果</span>
          <span id="scoreBadge" class="text-xs px-2.5 py-1 rounded-full bg-slate-100 text-slate-600 font-bold">待评测</span>
        </h3>

        <!-- Overall Score Ring -->
        <div class="flex items-center justify-center gap-6 py-2">
          <div class="relative w-28 h-28 flex items-center justify-center">
            <svg class="w-full h-full transform -rotate-90" viewBox="0 0 100 100">
              <circle cx="50" cy="50" r="40" stroke="#f1f5f9" stroke-width="8" fill="transparent" />
              <circle id="scoreProgressCircle" cx="50" cy="50" r="40" stroke="#6366f1" stroke-width="8" stroke-dasharray="251.2" stroke-dashoffset="251.2" stroke-linecap="round" fill="transparent" class="transition-all duration-700 ease-out" />
            </svg>
            <div class="absolute flex flex-col items-center">
              <span id="overallScoreNum" class="text-3xl font-extrabold text-slate-800">--</span>
              <span class="text-[10px] text-slate-400 font-bold uppercase">综合得分</span>
            </div>
          </div>

          <!-- Star Rating for Kids -->
          <div class="flex flex-col items-center gap-1">
            <div id="starContainer" class="flex text-2xl text-slate-200">
              <span>★</span><span>★</span><span>★</span>
            </div>
            <span id="praiseText" class="text-xs font-bold text-slate-500 text-center">念完即可实时评测</span>
          </div>
        </div>

        <!-- Metric Bars -->
        <div class="space-y-2.5 my-4 pt-2 border-t border-slate-100">
          <div>
            <div class="flex justify-between text-xs font-semibold text-slate-600 mb-1">
              <span>咬字准确度 (Accuracy)</span>
              <span id="accScore">--</span>
            </div>
            <div class="w-full bg-slate-100 h-2 rounded-full overflow-hidden">
              <div id="accBar" class="bg-indigo-500 h-full rounded-full transition-all duration-500" style="width: 0%"></div>
            </div>
          </div>
          <div>
            <div class="flex justify-between text-xs font-semibold text-slate-600 mb-1">
              <span>发音完整度 (Completeness)</span>
              <span id="fluScore">--</span>
            </div>
            <div class="w-full bg-slate-100 h-2 rounded-full overflow-hidden">
              <div id="fluBar" class="bg-emerald-500 h-full rounded-full transition-all duration-500" style="width: 0%"></div>
            </div>
          </div>
          <div>
            <div class="flex justify-between text-xs font-semibold text-slate-600 mb-1">
              <span>声学响度与节奏 (Acoustic)</span>
              <span id="proScore">--</span>
            </div>
            <div class="w-full bg-slate-100 h-2 rounded-full overflow-hidden">
              <div id="proBar" class="bg-amber-500 h-full rounded-full transition-all duration-500" style="width: 0%"></div>
            </div>
          </div>
        </div>

        <!-- Word / Phoneme Granular Diagnostics -->
        <div class="mt-4 pt-3 border-t border-slate-100">
          <div class="text-xs font-bold text-slate-600 mb-2">逐词诊断明细（点击词块查看分析）：</div>
          <div id="wordsFeedback" class="flex flex-wrap gap-1.5 min-h-[42px] items-center">
            <span class="text-xs text-slate-400 italic">完成朗读后，此处真实标出正确或错误的词</span>
          </div>
        </div>

        <!-- Next Quest Word Button -->
        <div class="mt-4 pt-3 border-t border-slate-100 flex justify-between items-center">
          <button onclick="resetEvaluationState()" class="text-xs text-slate-500 hover:text-indigo-600 font-semibold flex items-center gap-1 transition">
            🔄 重置本题
          </button>
          <button id="nextQuestActionBtn" onclick="nextCard()" class="px-4 py-2 bg-indigo-600 hover:bg-indigo-700 text-white rounded-xl text-xs font-bold transition flex items-center gap-1 shadow-md shadow-indigo-200">
            <span>下一个任务词</span> →
          </button>
        </div>

      </div>

      <!-- Spaced Repetition (SRS) Engine Status -->
      <div class="bg-white rounded-3xl p-5 shadow-xl shadow-indigo-100/60 border border-indigo-50">
        <div class="flex items-center justify-between mb-3">
          <h4 class="text-xs font-bold text-slate-700 flex items-center gap-1.5">
            <span>🧠 智能复习算法联动 (SRS)</span>
          </h4>
          <span class="text-[10px] bg-indigo-50 text-indigo-700 px-2 py-0.5 rounded font-mono font-bold">SM-2 / FSRS</span>
        </div>

        <div class="bg-slate-50 rounded-2xl p-3 border border-slate-100 text-xs space-y-2">
          <div class="flex justify-between items-center">
            <span class="text-slate-500">当前熟练度等级：</span>
            <span id="srsMastery" class="font-bold text-slate-700">未测定</span>
          </div>
          <div class="flex justify-between items-center">
            <span class="text-slate-500">下次推荐复习时间：</span>
            <span id="srsNextReview" class="font-bold text-indigo-600">--</span>
          </div>
          <div class="flex justify-between items-center">
            <span class="text-slate-500">调度规则：</span>
            <span id="srsLogicNote" class="text-[11px] text-slate-500 text-right">念得糟将立即排入10分钟复习队列</span>
          </div>
        </div>
      </div>

    </div>

  </main>

  <!-- Mobile LAN QR Code Modal -->
  <div id="mobileModal" class="fixed inset-0 bg-slate-900/40 backdrop-blur-sm z-50 hidden flex items-center justify-center p-4">
    <div class="bg-white rounded-3xl max-w-md w-full p-6 shadow-2xl border border-slate-100 text-center">
      <div class="flex items-center justify-between pb-3 border-b border-slate-100">
        <h3 class="text-lg font-bold text-slate-800">手机 / 平板 局域网真机测试</h3>
        <button onclick="toggleMobileModal()" class="text-slate-400 hover:text-slate-600 font-bold text-lg">✕</button>
      </div>

      <div class="my-5 flex flex-col items-center">
        <div class="p-3 bg-white border-2 border-indigo-100 rounded-2xl shadow-sm mb-3">
          <canvas id="qrCanvas" class="w-48 h-48"></canvas>
        </div>
        <p class="text-xs text-slate-600 font-bold">用 iPhone / iPad 相机或微信扫一扫直接打开</p>
        
        <div class="mt-3 p-3 bg-indigo-50 rounded-xl text-left text-xs space-y-1.5 w-full border border-indigo-100">
          <div class="text-indigo-900 font-bold">局域网 HTTPS 直连地址：</div>
          <code id="lanUrlText" class="block bg-white p-2 rounded border border-indigo-200 text-indigo-700 font-mono text-[11px] select-all break-all">https://192.168.100.114:8443</code>
          <p class="text-[10px] text-slate-500 leading-relaxed pt-1">
            <strong>⚠️ 苹果 Safari 麦克风权限提示：</strong><br>
            手机浏览器对麦克风要求高安全性。首次打开会提示“证书不受信任”，请点击「显示详细信息」并选择「访问此网站（继续）」，即可正常授权麦克风收音！
          </p>
        </div>
      </div>

      <div class="flex justify-end">
        <button onclick="toggleMobileModal()" class="px-4 py-2 bg-indigo-600 text-white rounded-xl text-xs font-bold hover:bg-indigo-700 transition">知道了</button>
      </div>
    </div>
  </div>

  <!-- Practice Log & History Modal -->
  <div id="logModal" class="fixed inset-0 bg-slate-900/40 backdrop-blur-sm z-50 hidden flex items-center justify-center p-4">
    <div class="bg-white rounded-3xl max-w-2xl w-full p-6 shadow-2xl border border-slate-100 max-h-[90vh] flex flex-col">
      <div class="flex items-center justify-between pb-3 border-b border-slate-100">
        <div>
          <h3 class="text-lg font-bold text-slate-800">学习与朗读记录日志 (Practice Logs)</h3>
          <p class="text-xs text-slate-500">详细记录每一次发音朗读时间点、得分与复习统计</p>
        </div>
        <button onclick="toggleLogModal()" class="text-slate-400 hover:text-slate-600 font-bold text-lg">✕</button>
      </div>

      <div class="flex items-center justify-between my-3 text-xs">
        <span class="text-slate-600">总练习记录：<strong id="totalLogsNum" class="text-indigo-600">0</strong> 条</span>
        <button onclick="exportLogsCSV()" class="px-3 py-1 bg-indigo-50 text-indigo-700 hover:bg-indigo-100 rounded-lg font-bold transition flex items-center gap-1">
          📥 导出练习日志 (CSV)
        </button>
      </div>

      <div id="logsTableContainer" class="flex-1 overflow-y-auto border border-slate-100 rounded-2xl">
        <table class="w-full text-left border-collapse text-xs">
          <thead class="bg-slate-50 sticky top-0 text-slate-500 font-bold border-b">
            <tr>
              <th class="p-2.5">时间戳</th>
              <th class="p-2.5">词汇 / 情境例句</th>
              <th class="p-2.5">类型</th>
              <th class="p-2.5">得分</th>
              <th class="p-2.5">复习状态</th>
            </tr>
          </thead>
          <tbody id="logsTableBody" class="divide-y divide-slate-100 text-slate-700">
            <tr>
              <td colspan="5" class="p-6 text-center text-slate-400 italic">暂无练习记录，开始朗读后将自动记录</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="mt-4 pt-3 border-t border-slate-100 flex justify-between items-center">
        <button onclick="clearLogs()" class="text-xs text-rose-500 hover:underline">清空所有记录</button>
        <button onclick="toggleLogModal()" class="px-4 py-2 bg-slate-800 text-white rounded-xl text-xs font-bold hover:bg-slate-900 transition">关闭</button>
      </div>
    </div>
  </div>

  <script>
    // --- 50 Complete Children's Vocabulary Master Database with 3 Scenarios x 3 Sentences = 9 Sentences Each ---
    const MASTER_VOCAB = """ + vocab_json_str + """;

    // Application State
    let appMode = 'quest'; // 'quest' | 'free' | 'adventure'
    let currentCardIndex = 0; // 0 to 49
    let practiceMode = 'scenario'; // 'scenario' | 'word'
    let currentScenarioIdx = 0; // 0, 1, 2
    let currentSentenceIdx = 0; // 0, 1, 2 (within scenario)
    let isRecording = false;
    let isProcessing = false;

    // Daily Quest Dynamic Queue (20 items: 10 new, 8 review, 2 consolidate)
    let questQueue = [];
    let questCompletedSet = new Set();

    // Streak & Storage
    let streakDays = parseInt(localStorage.getItem('kai_streak_days') || '3');
    let practiceLogs = JSON.parse(localStorage.getItem('kai_practice_logs') || '[]');
    let adventureStars = JSON.parse(localStorage.getItem('kai_adventure_stars') || '{}');

    // Audio & Web Audio
    let recognition = null;
    let audioContext = null;
    let analyser = null;
    let microphoneStream = null;
    let animFrameId = null;
    let currentAudioPlayer = null;

    // Evaluation buffer
    let capturedTranscript = "";
    let capturedConfidence = 0;
    let maxRmsVolume = 0;
    let recordStartTime = 0;
    let timerInterval = null;

    const currentCard = () => {
      if (appMode === 'quest') {
        return questQueue[currentCardIndex] || MASTER_VOCAB[0];
      }
      return MASTER_VOCAB[currentCardIndex] || MASTER_VOCAB[0];
    };

    // --- App Mode Switcher ---
    function switchAppMode(mode) {
      appMode = mode;
      
      const vQuest = document.getElementById('viewQuest');
      const vFree = document.getElementById('viewFree');
      const vAdv = document.getElementById('viewAdventure');

      const bQuest = document.getElementById('navQuestBtn');
      const bFree = document.getElementById('navFreeBtn');
      const bAdv = document.getElementById('navAdventureBtn');

      [bQuest, bFree, bAdv].forEach(b => b.className = "px-3.5 py-2 rounded-xl text-slate-600 hover:text-slate-900 transition flex items-center gap-1.5");

      if (mode === 'quest') {
        vQuest.classList.remove('hidden');
        vFree.classList.add('hidden');
        vAdv.classList.add('hidden');
        bQuest.className = "px-3.5 py-2 rounded-xl bg-indigo-600 text-white shadow-sm transition flex items-center gap-1.5";
        renderQuestStepper();
      } else if (mode === 'free') {
        vQuest.classList.add('hidden');
        vFree.classList.remove('hidden');
        vAdv.classList.add('hidden');
        bFree.className = "px-3.5 py-2 rounded-xl bg-indigo-600 text-white shadow-sm transition flex items-center gap-1.5";
        renderFreeGrid('all');
      } else if (mode === 'adventure') {
        vQuest.classList.add('hidden');
        vFree.classList.add('hidden');
        vAdv.classList.remove('hidden');
        bAdv.className = "px-3.5 py-2 rounded-xl bg-indigo-600 text-white shadow-sm transition flex items-center gap-1.5";
        renderAdventureMap();
      }

      currentCardIndex = 0;
      currentScenarioIdx = 0;
      currentSentenceIdx = 0;
      renderCard();
    }

    // --- Quest Mode (10 New + 8 Review + 2 Consolidate) ---
    function initQuestQueue() {
      const news = MASTER_VOCAB.filter(v => v.role === 'new');
      const reviews = MASTER_VOCAB.filter(v => v.role === 'review');
      const consolidates = MASTER_VOCAB.filter(v => v.role === 'consolidate');

      questQueue = [];
      let nIdx = 0, rIdx = 0, cIdx = 0;
      for (let i = 0; i < 20; i++) {
        if (i % 6 === 0 && cIdx < consolidates.length) {
          questQueue.push(consolidates[cIdx++]);
        } else if (i % 2 === 0 && nIdx < news.length) {
          questQueue.push(news[nIdx++]);
        } else if (rIdx < reviews.length) {
          questQueue.push(reviews[rIdx++]);
        } else if (nIdx < news.length) {
          questQueue.push(news[nIdx++]);
        }
      }

      renderQuestStepper();
    }

    function renderQuestStepper() {
      const container = document.getElementById('questStepperContainer');
      container.innerHTML = '';

      questQueue.forEach((item, idx) => {
        const isCurrent = idx === currentCardIndex;
        const isDone = questCompletedSet.has(item.id);

        let bgClass = "bg-slate-100 text-slate-500 border-slate-200";
        let roleBadge = "新";
        if (item.role === 'review') roleBadge = "复";
        if (item.role === 'consolidate') roleBadge = "固";

        if (isCurrent) {
          bgClass = "bg-indigo-600 text-white border-indigo-600 ring-2 ring-indigo-300 font-bold scale-105";
        } else if (isDone) {
          bgClass = "bg-emerald-100 text-emerald-800 border-emerald-300 font-bold";
        }

        const pill = document.createElement('button');
        pill.className = `px-3 py-1.5 rounded-xl border text-xs flex items-center gap-1.5 shrink-0 transition ${bgClass}`;
        pill.innerHTML = `
          <span>${item.emoji}</span>
          <span class="font-bold">${idx + 1}. ${item.word}</span>
          <span class="text-[9px] px-1 py-0.2 rounded ${isCurrent ? 'bg-white/20' : 'bg-slate-200/80'}">${roleBadge}</span>
          ${isDone ? '<span>✓</span>' : ''}
        `;
        pill.onclick = () => {
          currentCardIndex = idx;
          currentScenarioIdx = 0;
          currentSentenceIdx = 0;
          renderCard();
          renderQuestStepper();
        };
        container.appendChild(pill);
      });

      document.getElementById('questProgressNum').innerText = questCompletedSet.size;
      const pct = Math.round((questCompletedSet.size / 20) * 100);
      document.getElementById('questProgressBar').style.width = `${pct}%`;
      document.getElementById('questStreakDays').innerText = streakDays;
    }

    // --- Free Practice & Weak Spot Bank (50 Words) ---
    function renderFreeGrid(cat = 'all') {
      const container = document.getElementById('freeGridContainer');
      container.innerHTML = '';

      const weakWordIds = getWeakWordIds();
      document.getElementById('weakCountBadge').innerText = weakWordIds.size;

      MASTER_VOCAB.forEach((c, idx) => {
        if (cat === 'weak' && !weakWordIds.has(c.word)) return;
        if (cat !== 'all' && cat !== 'weak' && c.category !== cat) return;

        const isSelected = idx === currentCardIndex;
        const isWeak = weakWordIds.has(c.word);

        const btn = document.createElement('button');
        btn.className = `p-2 rounded-2xl flex flex-col items-center justify-center transition border relative ${
          isSelected 
            ? 'bg-indigo-600 text-white border-indigo-600 shadow-md scale-105 font-bold' 
            : (isWeak 
                ? 'bg-rose-50 text-rose-900 border-rose-200 hover:bg-rose-100' 
                : 'bg-slate-50 text-slate-700 border-slate-200/80 hover:bg-indigo-50 hover:border-indigo-200')
        }`;

        btn.innerHTML = `
          ${isWeak ? '<span class="absolute top-1 right-1 w-2 h-2 rounded-full bg-rose-500 animate-ping"></span>' : ''}
          <span class="text-xl mb-0.5">${c.emoji}</span>
          <span class="text-[11px] font-bold truncate w-full text-center">${c.word}</span>
          <span class="text-[9px] opacity-75">${isWeak ? '待加强' : c.level}</span>
        `;
        btn.onclick = () => {
          currentCardIndex = idx;
          currentScenarioIdx = 0;
          currentSentenceIdx = 0;
          renderCard();
          renderFreeGrid(cat);
        };
        container.appendChild(btn);
      });
    }

    function getWeakWordIds() {
      const weak = new Set();
      if (practiceLogs.length === 0) {
        weak.add("desk"); weak.add("dog"); weak.add("shoe");
        return weak;
      }
      practiceLogs.forEach(l => {
        if (l.score < 75) weak.add(l.word);
      });
      return weak;
    }

    function setFreeCategory(cat) {
      document.querySelectorAll('.free-cat-btn').forEach(btn => {
        if (btn.getAttribute('data-cat') === cat) {
          btn.className = "free-cat-btn px-3 py-1.5 rounded-xl font-bold bg-indigo-600 text-white shadow-sm whitespace-nowrap";
        } else {
          btn.className = "free-cat-btn px-3 py-1.5 rounded-xl font-semibold bg-slate-100 text-slate-600 hover:bg-slate-200 whitespace-nowrap";
        }
      });
      renderFreeGrid(cat);
    }

    // --- 50 Stage Adventure Map ---
    function renderAdventureMap() {
      const container = document.getElementById('adventureNodesContainer');
      container.innerHTML = '';
      let totalStars = 0;

      MASTER_VOCAB.forEach((c, idx) => {
        const stars = adventureStars[c.id] || (idx < 5 ? 3 : (idx < 8 ? 2 : 0));
        totalStars += stars;
        const isUnlocked = idx === 0 || (adventureStars[MASTER_VOCAB[idx-1].id] || 0) > 0 || idx < 8;

        const node = document.createElement('button');
        node.className = `p-2 rounded-2xl flex flex-col items-center justify-center border transition relative ${
          idx === currentCardIndex 
            ? 'bg-amber-400 text-amber-950 border-amber-300 shadow-lg scale-105 font-bold ring-2 ring-white' 
            : (isUnlocked 
                ? 'bg-white/95 text-slate-800 border-white/50 hover:bg-white shadow' 
                : 'bg-black/20 text-white/50 border-white/10 cursor-not-allowed')
        }`;

        let starsStr = '';
        for (let s = 1; s <= 3; s++) starsStr += s <= stars ? '★' : '☆';

        node.innerHTML = `
          <div class="text-[9px] font-mono font-bold opacity-75">关卡 ${idx + 1}</div>
          <div class="text-xl my-0.5">${c.emoji}</div>
          <div class="text-[11px] font-black truncate w-full text-center">${c.word}</div>
          <div class="text-[10px] text-amber-500 font-bold tracking-tight">${isUnlocked ? starsStr : '🔒'}</div>
        `;

        if (isUnlocked) {
          node.onclick = () => {
            currentCardIndex = idx;
            currentScenarioIdx = 0;
            currentSentenceIdx = 0;
            renderCard();
            renderAdventureMap();
          };
        }
        container.appendChild(node);
      });

      document.getElementById('adventureTotalStars').innerText = totalStars;
    }

    // --- Card Rendering with 3 Contexts x 3 Sentences = 9 Sentences ---
    function renderCard() {
      const card = currentCard();
      const maxLen = appMode === 'quest' ? 20 : 50;
      document.getElementById('cardIndex').innerText = `${currentCardIndex + 1} / ${maxLen}`;
      document.getElementById('wordIllustration').innerText = card.emoji;
      document.getElementById('wordText').innerText = card.word;
      document.getElementById('wordPhonetic').innerText = card.phonetic;
      document.getElementById('wordMeaning').innerText = card.meaning;
      
      const catMap = { home: "🏠 日常起居", food: "🍎 美味饮食", animals: "🐱 动物伙伴", nature: "🌳 大自然", play: "⚽ 趣味玩乐" };
      document.getElementById('cardCategoryTag').innerText = catMap[card.category] || "生活情境";
      
      const roleEl = document.getElementById('cardQuestRoleTag');
      if (card.role === 'new') {
        roleEl.innerText = "🌟 今日新学词汇";
        roleEl.className = "px-3 py-1 rounded-full text-xs font-extrabold bg-indigo-100 text-indigo-800";
      } else if (card.role === 'review') {
        roleEl.innerText = "⚠️ 重点温习词汇";
        roleEl.className = "px-3 py-1 rounded-full text-xs font-extrabold bg-amber-100 text-amber-900";
      } else {
        roleEl.innerText = "🛡️ 常态巩固词汇";
        roleEl.className = "px-3 py-1 rounded-full text-xs font-extrabold bg-emerald-100 text-emerald-800";
      }

      const wordLogs = practiceLogs.filter(l => l.word === card.word);
      document.getElementById('wordPracticeCount').innerText = wordLogs.length;
      if (wordLogs.length > 0) {
        const best = Math.max(...wordLogs.map(l => l.score));
        document.getElementById('wordBestScore').innerText = `${best}`;
        document.getElementById('wordStatusTag').innerText = best >= 85 ? "已熟练" : "需加强";
        document.getElementById('wordStatusTag').className = best >= 85 ? "text-emerald-600 font-bold" : "text-amber-600 font-bold";
      } else {
        document.getElementById('wordBestScore').innerText = '--';
        document.getElementById('wordStatusTag').innerText = "未练习";
        document.getElementById('wordStatusTag').className = "text-slate-500 font-normal";
      }

      updateTargetBox();
      resetEvaluationState();
    }

    function selectPracticeMode(mode) {
      if (isRecording) stopRecording();
      practiceMode = mode;
      updateTargetBox();
      resetEvaluationState();
    }

    function selectScenarioTab(scIdx) {
      if (isRecording) stopRecording();
      practiceMode = 'scenario';
      currentScenarioIdx = scIdx;
      currentSentenceIdx = 0; // reset to sentence 1
      updateTargetBox();
      resetEvaluationState();
    }

    function selectSentenceIndex(sentIdx) {
      if (isRecording) stopRecording();
      practiceMode = 'scenario';
      currentSentenceIdx = sentIdx;
      updateTargetBox();
      resetEvaluationState();
    }

    function updateTargetBox() {
      const card = currentCard();
      const sentenceEl = document.getElementById('targetSentence');
      const tagEl = document.getElementById('targetTag');
      const subSelector = document.getElementById('sentenceSubSelector');

      // Update Scenario Tabs styling
      ['scTabWord', 'scTab0', 'scTab1', 'scTab2'].forEach(id => {
        const el = document.getElementById(id);
        if (el) el.className = "py-2 rounded-xl text-slate-600 hover:text-slate-900 transition text-center truncate px-1";
      });

      const transEl = document.getElementById('targetTranslationText');

      if (practiceMode === 'word') {
        subSelector.classList.add('hidden');
        sentenceEl.innerText = card.word;
        if (transEl) transEl.innerText = card.meaning || "";
        tagEl.innerText = "单字精读 · 辅音与爆破音咬字练习";
        document.getElementById('scTabWord').className = "py-2 rounded-xl bg-white text-indigo-700 shadow-sm transition text-center truncate px-1 font-bold";
      } else {
        subSelector.classList.remove('hidden');
        document.getElementById(`scTab${currentScenarioIdx}`).className = "py-2 rounded-xl bg-white text-indigo-700 shadow-sm transition text-center truncate px-1 font-bold";

        // Update Sub Sentence Selector buttons
        ['sentSub0', 'sentSub1', 'sentSub2'].forEach((id, idx) => {
          const btn = document.getElementById(id);
          if (idx === currentSentenceIdx) {
            btn.className = "py-1.5 rounded-lg bg-indigo-600 text-white font-bold transition text-center truncate px-1 shadow-sm";
          } else {
            btn.className = "py-1.5 rounded-lg text-indigo-900 hover:bg-indigo-100 transition text-center truncate px-1";
          }
        });

        const sc = card.scenarios[currentScenarioIdx];
        const targetSentenceText = sc.sentences[currentSentenceIdx];
        const targetTransText = (sc.translations && sc.translations[currentSentenceIdx]) ? sc.translations[currentSentenceIdx] : "";
        sentenceEl.innerText = targetSentenceText;
        if (transEl) transEl.innerText = targetTransText;
        tagEl.innerText = `${sc.tag} (例句 ${currentSentenceIdx + 1}/3)`;
      }
    }

    function nextCard() {
      if (isRecording) stopRecording();
      const maxLen = appMode === 'quest' ? 20 : 50;
      currentCardIndex = (currentCardIndex + 1) % maxLen;
      currentScenarioIdx = 0;
      currentSentenceIdx = 0;
      renderCard();
      if (appMode === 'quest') renderQuestStepper();
      if (appMode === 'free') renderFreeGrid();
      if (appMode === 'adventure') renderAdventureMap();
    }

    function prevCard() {
      if (isRecording) stopRecording();
      const maxLen = appMode === 'quest' ? 20 : 50;
      currentCardIndex = (currentCardIndex - 1 + maxLen) % maxLen;
      currentScenarioIdx = 0;
      currentSentenceIdx = 0;
      renderCard();
      if (appMode === 'quest') renderQuestStepper();
      if (appMode === 'free') renderFreeGrid();
      if (appMode === 'adventure') renderAdventureMap();
    }

    // --- Audio Playback of 100% Real Studio Audio or High-Def Fallback ---
    function playAudio(target) {
      if (currentAudioPlayer) {
        currentAudioPlayer.pause();
        currentAudioPlayer.currentTime = 0;
      }

      const card = currentCard();
      const audioCandidates = [];
      let targetText = "";

      if (target === 'word' || practiceMode === 'word') {
        if (card.audioWord) audioCandidates.push(card.audioWord);
        audioCandidates.push(`audio/word_${card.id}.m4a`);
        targetText = card.word;
      } else {
        // Specific sentence under current scenario
        audioCandidates.push(`audio/sentence_${card.id}_${currentScenarioIdx}_${currentSentenceIdx}.m4a`);
        audioCandidates.push(`audio/sentence_${card.id}_${currentScenarioIdx}.m4a`);
        if (card.scenarios && card.scenarios[currentScenarioIdx] && card.scenarios[currentScenarioIdx].sentences) {
          targetText = card.scenarios[currentScenarioIdx].sentences[currentSentenceIdx] || "";
        }
      }

      function tryPlay(index) {
        if (index >= audioCandidates.length) {
          fallbackNaturalTTS(targetText);
          return;
        }
        const player = new Audio(audioCandidates[index]);
        currentAudioPlayer = player;
        player.play().catch(() => {
          tryPlay(index + 1);
        });
      }

      tryPlay(0);
    }

    let loadedVoices = [];
    function refreshVoices() {
      if ('speechSynthesis' in window) {
        loadedVoices = window.speechSynthesis.getVoices();
      }
    }
    if ('speechSynthesis' in window) {
      window.speechSynthesis.onvoiceschanged = refreshVoices;
      refreshVoices();
    }

    function fallbackNaturalTTS(text) {
      if (!('speechSynthesis' in window) || !text) return;
      window.speechSynthesis.cancel();
      const u = new SpeechSynthesisUtterance(text);
      u.lang = 'en-US';
      u.rate = 0.86; // Gentle, child-friendly cadence
      u.pitch = 1.05; // Warm and inviting tone

      refreshVoices();
      const preferred = loadedVoices.filter(v => 
        (v.lang === 'en-US' || v.lang === 'en_US' || v.lang.startsWith('en')) && 
        (v.name.includes('Samantha') || v.name.includes('Ava') || v.name.includes('Karen') || 
         v.name.includes('Natural') || v.name.includes('Neural') || v.name.includes('Google') || 
         v.name.includes('Siri') || v.name.includes('Moira') || v.name.includes('Tessa') ||
         v.name.includes('Flo') || v.name.includes('Junior') || v.name.includes('Sandy'))
      );
      if (preferred.length > 0) u.voice = preferred[0];

      window.speechSynthesis.speak(u);
    }

    // --- Audio Waveform Visualizer ---
    async function startWaveformVisualizer(stream) {
      const canvas = document.getElementById('waveformCanvas');
      const ctx = canvas.getContext('2d');
      document.getElementById('waveformPlaceholder').classList.add('hidden');

      try {
        audioContext = new (window.AudioContext || window.webkitAudioContext)();
        if (audioContext.state === 'suspended') await audioContext.resume();

        analyser = audioContext.createAnalyser();
        analyser.fftSize = 256;
        const source = audioContext.createMediaStreamSource(stream);
        source.connect(analyser);

        const bufferLength = analyser.frequencyBinCount;
        const dataArray = new Uint8Array(bufferLength);

        function draw() {
          if (!isRecording) return;
          animFrameId = requestAnimationFrame(draw);

          analyser.getByteFrequencyData(dataArray);

          let sum = 0;
          for (let i = 0; i < bufferLength; i++) sum += dataArray[i];
          const avg = sum / bufferLength;
          if (avg > maxRmsVolume) maxRmsVolume = avg;

          canvas.width = canvas.parentElement.clientWidth;
          canvas.height = canvas.parentElement.clientHeight;
          ctx.clearRect(0, 0, canvas.width, canvas.height);

          const barWidth = (canvas.width / bufferLength) * 2.5;
          let barHeight;
          let x = 0;

          for (let i = 0; i < bufferLength; i++) {
            barHeight = (dataArray[i] / 255) * canvas.height * 0.9;
            ctx.fillStyle = `rgba(99, 102, 241, ${Math.min(1, dataArray[i] / 160 + 0.2)})`;
            ctx.fillRect(x, (canvas.height - barHeight) / 2, barWidth - 1, barHeight);
            x += barWidth + 1;
          }
        }
        draw();
      } catch (e) {
        console.warn("Waveform error:", e);
      }
    }

    function stopWaveformVisualizer() {
      if (animFrameId) cancelAnimationFrame(animFrameId);
      if (audioContext && audioContext.state !== 'closed') {
        try { audioContext.close(); } catch(e){}
      }
      document.getElementById('waveformPlaceholder').classList.remove('hidden');
      const canvas = document.getElementById('waveformCanvas');
      const ctx = canvas.getContext('2d');
      ctx.clearRect(0, 0, canvas.width, canvas.height);
    }

    // --- Recording Lifecycle & Full Aggregation ---
    async function handleRecordClick() {
      if (isProcessing) return;
      if (isRecording) {
        stopRecording();
      } else {
        await startRecording();
      }
    }

    async function startRecording() {
      capturedTranscript = "";
      capturedConfidence = 0;
      maxRmsVolume = 0;
      isRecording = true;
      isProcessing = false;

      const btn = document.getElementById('recordBtn');
      btn.className = "relative z-10 w-20 h-20 rounded-full bg-rose-600 text-white shadow-lg shadow-rose-400/50 flex flex-col items-center justify-center transition transform active:scale-95 focus:outline-none";
      document.getElementById('recordIcon').innerText = '⏹️';
      document.getElementById('recordStatus').innerText = '点击停止';
      document.getElementById('pulseRing').classList.remove('opacity-0');
      document.getElementById('pulseRing').classList.add('pulse-ring');
      document.getElementById('recordTip').innerText = '正在录音中... 请大声清晰朗读！';
      document.getElementById('liveTranscript').innerHTML = '<span class="text-indigo-600 animate-pulse font-medium">正在倾听收音...</span>';
      document.getElementById('liveDot').className = 'w-2 h-2 rounded-full bg-rose-500 animate-ping';

      recordStartTime = Date.now();
      timerInterval = setInterval(() => {
        const sec = Math.floor((Date.now() - recordStartTime) / 1000);
        document.getElementById('statusTimer').innerText = `00:${sec < 10 ? '0' + sec : sec}`;
      }, 500);

      try {
        if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
          throw new Error("浏览器安全限制：非 HTTPS 无法开启麦克风，请使用 HTTPS 链接访问或使用下方快捷评测按钮");
        }
        microphoneStream = await navigator.mediaDevices.getUserMedia({ audio: true });
        await startWaveformVisualizer(microphoneStream);
      } catch (err) {
        alert("麦克风启动提示：\\n" + err.message);
        setButtonIdle();
        return;
      }

      const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
      if (SpeechRecognition) {
        if (recognition) {
          try { recognition.abort(); } catch(e){}
        }

        recognition = new SpeechRecognition();
        recognition.continuous = true;
        recognition.interimResults = true;
        recognition.lang = 'en-US';
        recognition.maxAlternatives = 3;

        // FIXED: Aggregate ALL results so far across the entire utterance
        recognition.onresult = (event) => {
          let aggregated = '';
          for (let i = 0; i < event.results.length; ++i) {
            aggregated += event.results[i][0].transcript + ' ';
            if (event.results[i][0].confidence > 0) {
              capturedConfidence = event.results[i][0].confidence;
            }
          }
          capturedTranscript = aggregated.trim();
          document.getElementById('liveTranscript').innerText = `"${capturedTranscript}"`;
          document.getElementById('confidenceVal').innerText = capturedConfidence > 0 ? `${Math.round(capturedConfidence * 100)}%` : '正常';
        };

        recognition.onerror = (event) => {
          console.warn("Speech recognition notice/error:", event.error);
        };

        try {
          recognition.start();
        } catch (e) {
          console.warn("Recognition start warning:", e);
        }
      }
    }

    function stopRecording() {
      if (!isRecording) return;
      isRecording = false;
      isProcessing = true;

      clearInterval(timerInterval);
      document.getElementById('statusTimer').innerText = '00:00';

      const btn = document.getElementById('recordBtn');
      btn.disabled = true;
      btn.className = "relative z-10 w-20 h-20 rounded-full bg-slate-400 text-white shadow flex flex-col items-center justify-center cursor-not-allowed";
      document.getElementById('recordIcon').innerText = '⏳';
      document.getElementById('recordStatus').innerText = '评分中...';
      document.getElementById('pulseRing').classList.add('opacity-0');
      document.getElementById('pulseRing').classList.remove('pulse-ring');
      document.getElementById('recordTip').innerText = '正在智能诊断发音...';
      document.getElementById('liveDot').className = 'w-2 h-2 rounded-full bg-slate-400';

      setTimeout(() => {
        if (recognition) {
          try { recognition.stop(); } catch(e){}
        }

        stopWaveformVisualizer();
        if (microphoneStream) {
          microphoneStream.getTracks().forEach(track => track.stop());
          microphoneStream = null;
        }

        document.getElementById('energyVal').innerText = maxRmsVolume > 5 ? '清晰 (Normal)' : '偏轻 (Low)';

        executeSmartPhoneticEvaluation(capturedTranscript, capturedConfidence, maxRmsVolume);
        setButtonIdle();
      }, 400);
    }

    function setButtonIdle() {
      isRecording = false;
      isProcessing = false;
      const btn = document.getElementById('recordBtn');
      btn.disabled = false;
      btn.className = "relative z-10 w-20 h-20 rounded-full bg-gradient-to-tr from-rose-500 to-red-500 hover:from-rose-600 hover:to-red-600 text-white shadow-lg shadow-rose-300/50 flex flex-col items-center justify-center transition transform active:scale-95 focus:outline-none";
      document.getElementById('recordIcon').innerText = '🎙️';
      document.getElementById('recordStatus').innerText = '点击录音';
      document.getElementById('pulseRing').classList.add('opacity-0');
      document.getElementById('pulseRing').classList.remove('pulse-ring');
      document.getElementById('recordTip').innerText = '点击红色麦克风开始录音，可无限次重新录音评测';
    }

    function resetEvaluationState() {
      document.getElementById('liveTranscript').innerHTML = '<span class="text-slate-400">等待录音中...</span>';
      document.getElementById('liveDot').className = 'w-2 h-2 rounded-full bg-slate-300';
      document.getElementById('confidenceVal').innerText = '--';
      document.getElementById('energyVal').innerText = '--';
      
      document.getElementById('overallScoreNum').innerText = '--';
      document.getElementById('accScore').innerText = '--';
      document.getElementById('fluScore').innerText = '--';
      document.getElementById('proScore').innerText = '--';
      document.getElementById('accBar').style.width = '0%';
      document.getElementById('fluBar').style.width = '0%';
      document.getElementById('proBar').style.width = '0%';
      document.getElementById('scoreProgressCircle').style.strokeDashoffset = '251.2';
      document.getElementById('scoreBadge').innerText = '待评测';
      document.getElementById('scoreBadge').className = 'text-xs px-2.5 py-1 rounded-full bg-slate-100 text-slate-600 font-bold';
      document.getElementById('starContainer').innerHTML = '<span>★</span><span>★</span><span>★</span>';
      document.getElementById('praiseText').innerText = '念完即可实时评测';
      document.getElementById('wordsFeedback').innerHTML = '<span class="text-xs text-slate-400 italic">完成朗读后，此处真实标出正确或错误的词</span>';
      document.getElementById('srsMastery').innerText = '未测定';
      document.getElementById('srsNextReview').innerText = '--';
      document.getElementById('srsLogicNote').innerText = '念得糟将立即排入10分钟复习队列';

      setButtonIdle();
    }

    // --- Fast Simulation Helper ---
    function simulateEval(type) {
      if (isRecording) stopRecording();
      const card = currentCard();
      const targetStr = practiceMode === 'word' 
        ? card.word 
        : card.scenarios[currentScenarioIdx].sentences[currentSentenceIdx];

      if (type === 'bad') {
        document.getElementById('liveTranscript').innerText = '"[含糊杂音 / 乱念]"';
        document.getElementById('confidenceVal').innerText = '10%';
        document.getElementById('energyVal').innerText = '偏弱';
        executeSmartPhoneticEvaluation("", 0, 10);
      } else if (type === 'wrong_word') {
        const wrongText = "This is a wrong shoe";
        document.getElementById('liveTranscript').innerText = `"${wrongText}"`;
        document.getElementById('confidenceVal').innerText = '85%';
        document.getElementById('energyVal').innerText = '清晰';
        executeSmartPhoneticEvaluation(wrongText, 0.85, 40);
      } else if (type === 'good') {
        document.getElementById('liveTranscript').innerText = `"${targetStr}"`;
        document.getElementById('confidenceVal').innerText = '96%';
        document.getElementById('energyVal').innerText = '清晰';
        executeSmartPhoneticEvaluation(targetStr, 0.96, 60);
      }
    }

    // --- Strict & Fair Phonetic Evaluation ---
    function executeSmartPhoneticEvaluation(spokenText, confidence, maxVolume) {
      const card = currentCard();
      const targetStr = practiceMode === 'word' 
        ? card.word 
        : card.scenarios[currentScenarioIdx].sentences[currentSentenceIdx];
      
      const cleanTarget = targetStr.toLowerCase().replace(/[^a-z0-9\s]/g, '').trim();
      const cleanSpoken = (spokenText || '').toLowerCase().replace(/[^a-z0-9\s]/g, '').trim();

      const targetWords = cleanTarget.split(/\s+/).filter(Boolean);
      const spokenWords = cleanSpoken.split(/\s+/).filter(Boolean);

      // 1. Silent
      if (spokenWords.length === 0 && maxVolume < 2) {
        recordPracticeLog(card.word, targetStr, 0, "未出声 0分");
        renderStrictResult({
          overall: 0, accuracy: 0, completeness: 0, acoustic: 0,
          praise: '没有检测到声音！请靠近麦克风大声朗读。',
          praiseClass: 'text-xs font-bold text-rose-500',
          badgeText: '未出声 0分',
          badgeClass: 'text-xs px-2.5 py-1 rounded-full bg-rose-100 text-rose-700 font-bold',
          stars: 0,
          words: targetWords.map(w => ({ word: w, score: 0, note: "未检测到收音" })),
          srsLevel: '重点攻坚 (Level 0)', srsNext: '10 分钟后立即重练', srsNote: '完全未收音，系统安排高频复习！'
        });
        return;
      }

      // 2. Unintelligible
      if (spokenWords.length === 0) {
        recordPracticeLog(card.word, targetStr, 15, "含糊不清 15分");
        renderStrictResult({
          overall: 15, accuracy: 10, completeness: 15, acoustic: 20,
          praise: '听不清楚发音！请放慢语速，大声清晰朗读。',
          praiseClass: 'text-xs font-bold text-rose-500',
          badgeText: '含糊不清 15分',
          badgeClass: 'text-xs px-2.5 py-1 rounded-full bg-rose-100 text-rose-700 font-bold',
          stars: 0,
          words: targetWords.map(w => ({ word: w, score: 10, note: "发音含糊或非英语" })),
          srsLevel: '重点攻坚 (Level 0)', srsNext: '10 分钟后立即重练', srsNote: '咬字偏差过大，已自动排入今日重点复习！'
        });
        return;
      }

      // 3. Matching
      let wordDetails = [];
      let totalWordScore = 0;

      if (practiceMode === 'word') {
        const targetWord = targetWords[0];
        let bestScore = 0;
        let note = "未匹配到目标单词";

        for (const sw of spokenWords) {
          const score = getWordPhoneticScore(targetWord, sw, card.variants);
          if (score > bestScore) {
            bestScore = score;
            note = score >= 88 ? "发音清晰标准" : (score >= 70 ? `读音相近 ("${sw}")` : `严重偏差 ("${sw}")`);
          }
        }

        totalWordScore = bestScore;
        wordDetails.push({ word: targetWord, score: bestScore, note });
      } else {
        targetWords.forEach((tw) => {
          let bestScore = 0;
          let note = "漏读 (Omission)";

          for (const sw of spokenWords) {
            const score = getWordPhoneticScore(tw, sw, (tw === card.word ? card.variants : [tw]));
            if (score > bestScore) {
              bestScore = score;
              note = score >= 88 ? "发音清晰标准" : (score >= 70 ? `读音相近 ("${sw}")` : `读音有偏差 ("${sw}")`);
            }
          }

          if (bestScore < 35) {
            bestScore = 0;
            note = "漏读或不匹配";
          }

          totalWordScore += bestScore;
          wordDetails.push({ word: tw, score: bestScore, note });
        });
      }

      const wordAccuracy = Math.round(totalWordScore / targetWords.length);
      const passedWords = wordDetails.filter(w => w.score >= 65).length;
      const completeness = Math.round((passedWords / targetWords.length) * 100);
      const acoustic = maxVolume > 5 ? 90 : 75;

      let overall = Math.round((wordAccuracy * 0.80) + (completeness * 0.15) + (acoustic * 0.05));
      overall = Math.min(100, Math.max(0, overall));

      let stars = 0;
      let praise = "";
      let praiseClass = "";
      let badgeText = "";
      let badgeClass = "";
      let srsLevel = "";
      let srsNext = "";
      let srsNote = "";

      if (overall >= 85) {
        stars = 3;
        praise = "太棒了！发音非常纯正地道 🎉";
        praiseClass = "text-xs font-bold text-emerald-600";
        badgeText = `优秀 ${overall}分`;
        badgeClass = "text-xs px-2.5 py-1 rounded-full bg-emerald-100 text-emerald-700 font-bold";
        srsLevel = "熟练掌握 (Level 4)";
        srsNext = "3 天后复习 (延期调度)";
        srsNote = "发音标准，系统降低复习频率，建立长期记忆！";
      } else if (overall >= 68) {
        stars = 2;
        praise = "读得很棒！大部分单词准确，再清晰一点更完美 💪";
        praiseClass = "text-xs font-bold text-indigo-600";
        badgeText = `良好 ${overall}分`;
        badgeClass = "text-xs px-2.5 py-1 rounded-full bg-indigo-100 text-indigo-700 font-bold";
        srsLevel = "基本良好 (Level 2)";
        srsNext = "1 天后温习 (正常调度)";
        srsNote = "整体良好，明天自动安排温习巩固。";
      } else if (overall >= 40) {
        stars = 1;
        praise = "部分音标发音有偏差，听听真人范读再试一次 💡";
        praiseClass = "text-xs font-bold text-amber-600";
        badgeText = `需巩固 ${overall}分`;
        badgeClass = "text-xs px-2.5 py-1 rounded-full bg-amber-100 text-amber-800 font-bold";
        srsLevel = "待提高 (Level 1)";
        srsNext = "10 分钟后再次弹出";
        srsNote = "检测到发音偏差，已自动调高今日复习几率！";
      } else {
        stars = 0;
        praise = "发音与目标偏差较大，请点击听范读重新跟读 ❌";
        praiseClass = "text-xs font-bold text-rose-500";
        badgeText = `不达标 ${overall}分`;
        badgeClass = "text-xs px-2.5 py-1 rounded-full bg-rose-100 text-rose-700 font-bold";
        srsLevel = "重点攻坚 (Level 0)";
        srsNext = "10 分钟后立即重练";
        srsNote = "已被锁定为高频重点攻坚词汇！";
      }

      // Record Quest Completion if passed
      if (overall >= 65) {
        questCompletedSet.add(card.id);
        adventureStars[card.id] = Math.max(adventureStars[card.id] || 0, stars);
        localStorage.setItem('kai_adventure_stars', JSON.stringify(adventureStars));
        if (appMode === 'quest') renderQuestStepper();
      }

      recordPracticeLog(card.word, targetStr, overall, badgeText);

      renderStrictResult({
        overall, accuracy: wordAccuracy, completeness, acoustic,
        praise, praiseClass, badgeText, badgeClass, stars,
        words: wordDetails, srsLevel, srsNext, srsNote
      });
    }

    function getWordPhoneticScore(target, spoken, variants) {
      if (!target || !spoken) return 0;
      if (target === spoken) return 96;
      if (variants && variants.includes(spoken)) return 92;

      const dist = levenshtein(target, spoken);
      const maxLen = Math.max(target.length, spoken.length);
      const ratio = 1 - (dist / maxLen);

      if (ratio >= 0.75) return 88;
      if (ratio >= 0.50) return 65;
      if (spoken.includes(target) || target.includes(spoken)) return 85;

      return Math.round(ratio * 50);
    }

    function levenshtein(a, b) {
      const matrix = [];
      for (let i = 0; i <= b.length; i++) matrix[i] = [i];
      for (let j = 0; j <= a.length; j++) matrix[0][j] = j;
      for (let i = 1; i <= b.length; i++) {
        for (let j = 1; j <= a.length; j++) {
          if (b.charAt(i - 1) === a.charAt(j - 1)) {
            matrix[i][j] = matrix[i - 1][j - 1];
          } else {
            matrix[i][j] = Math.min(matrix[i - 1][j - 1] + 1, Math.min(matrix[i][j - 1] + 1, matrix[i - 1][j] + 1));
          }
        }
      }
      return matrix[b.length][a.length];
    }

    function renderStrictResult(data) {
      document.getElementById('overallScoreNum').innerText = data.overall;
      const circumference = 251.2;
      const offset = circumference - (data.overall / 100) * circumference;
      document.getElementById('scoreProgressCircle').style.strokeDashoffset = offset;

      document.getElementById('accScore').innerText = `${data.accuracy} 分`;
      document.getElementById('fluScore').innerText = `${data.completeness} 分`;
      document.getElementById('proScore').innerText = `${data.acoustic} 分`;

      document.getElementById('accBar').style.width = `${data.accuracy}%`;
      document.getElementById('fluBar').style.width = `${data.completeness}%`;
      document.getElementById('proBar').style.width = `${data.acoustic}%`;

      document.getElementById('scoreBadge').innerText = data.badgeText;
      document.getElementById('scoreBadge').className = data.badgeClass;

      const starContainer = document.getElementById('starContainer');
      let starHtml = '';
      for (let s = 1; s <= 3; s++) {
        starHtml += (s <= data.stars) ? '<span class="text-amber-400">★</span>' : '<span class="text-slate-200">★</span>';
      }
      starContainer.innerHTML = starHtml;

      const praiseEl = document.getElementById('praiseText');
      praiseEl.innerText = data.praise;
      praiseEl.className = data.praiseClass;

      const wordsBox = document.getElementById('wordsFeedback');
      wordsBox.innerHTML = '';
      data.words.forEach(w => {
        const chip = document.createElement('div');
        let colorClass = "bg-emerald-50 text-emerald-800 border-emerald-200";
        if (w.score < 50) {
          colorClass = "bg-rose-50 text-rose-800 border-rose-300 animate-pulse font-bold";
        } else if (w.score < 80) {
          colorClass = "bg-amber-50 text-amber-800 border-amber-300 font-semibold";
        }

        chip.className = `px-2.5 py-1 rounded-xl text-xs border flex items-center gap-1.5 cursor-pointer shadow-sm transition hover:scale-105 ${colorClass}`;
        chip.title = `点击查看诊断建议`;
        chip.innerHTML = `<span>${w.word}</span><span class="text-[10px] opacity-75 font-mono">${w.score}分</span>`;
        chip.onclick = () => alert(`【单词诊断: ${w.word}】\n得分: ${w.score} 分\n分析: ${w.note}`);
        wordsBox.appendChild(chip);
      });

      document.getElementById('srsMastery').innerText = data.srsLevel;
      document.getElementById('srsNextReview').innerText = data.srsNext;
      document.getElementById('srsLogicNote').innerText = data.srsNote;
    }

    // --- Practice Logs ---
    function recordPracticeLog(word, target, score, status) {
      const now = new Date();
      const timeStr = `${now.getFullYear()}-${pad(now.getMonth()+1)}-${pad(now.getDate())} ${pad(now.getHours())}:${pad(now.getMinutes())}:${pad(now.getSeconds())}`;
      
      const card = currentCard();
      const sc = card.scenarios ? card.scenarios[currentScenarioIdx] : null;
      const trans = practiceMode === 'word' ? (card.meaning || '') : (sc && sc.translations ? (sc.translations[currentSentenceIdx] || '') : '');

      const entry = {
        time: timeStr,
        word: word,
        target: target,
        trans: trans,
        type: practiceMode === 'word' ? '单字' : `情境${currentScenarioIdx+1}-句${currentSentenceIdx+1}`,
        score: score,
        status: status
      };

      practiceLogs.unshift(entry);
      if (practiceLogs.length > 500) practiceLogs.pop();
      localStorage.setItem('kai_practice_logs', JSON.stringify(practiceLogs));
      updateLogUI();
      renderCardHeaderStats();
    }

    function renderCardHeaderStats() {
      const card = currentCard();
      const wordLogs = practiceLogs.filter(l => l.word === card.word);
      document.getElementById('wordPracticeCount').innerText = wordLogs.length;
      if (wordLogs.length > 0) {
        const best = Math.max(...wordLogs.map(l => l.score));
        document.getElementById('wordBestScore').innerText = `${best}`;
      }
    }

    function updateLogUI() {
      document.getElementById('logBadge').innerText = practiceLogs.length;
      document.getElementById('totalLogsNum').innerText = practiceLogs.length;
      const tbody = document.getElementById('logsTableBody');
      if (practiceLogs.length === 0) {
        tbody.innerHTML = '<tr><td colspan="5" class="p-6 text-center text-slate-400 italic">暂无练习记录</td></tr>';
        return;
      }

      tbody.innerHTML = practiceLogs.map(l => `
        <tr class="hover:bg-slate-50 transition">
          <td class="p-2.5 font-mono text-slate-500 text-[11px]">${l.time}</td>
          <td class="p-2.5">
            <div class="font-bold text-slate-800">${l.target}</div>
            ${l.trans ? `<div class="text-[11px] text-slate-400 font-medium">${l.trans}</div>` : ''}
          </td>
          <td class="p-2.5"><span class="px-2 py-0.5 rounded text-[10px] bg-slate-100 font-bold">${l.type}</span></td>
          <td class="p-2.5 font-bold ${l.score >= 80 ? 'text-emerald-600' : (l.score >= 60 ? 'text-indigo-600' : 'text-rose-600')}">${l.score} 分</td>
          <td class="p-2.5 text-slate-600">${l.status}</td>
        </tr>
      `).join('');
    }

    function exportLogsCSV() {
      if (practiceLogs.length === 0) {
        alert("暂无记录可导出");
        return;
      }
      let csv = "时间戳,单词,跟读内容,类型,得分,评测结果\\n";
      practiceLogs.forEach(l => {
        csv += `"${l.time}","${l.word}","${l.target}","${l.type}","${l.score}","${l.status}"\\n`;
      });
      const blob = new Blob(["\\uFEFF" + csv], { type: 'text/csv;charset=utf-8;' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `KaiSpeak_练习日志_${new Date().toISOString().slice(0,10)}.csv`;
      a.click();
    }

    function clearLogs() {
      if (confirm("确定要清空所有练习记录吗？")) {
        practiceLogs = [];
        localStorage.removeItem('kai_practice_logs');
        updateLogUI();
        renderCard();
      }
    }

    // --- Mobile Modal & QR Code ---
    function initQRCode() {
      const lanUrl = "https://192.168.100.114:8443";
      document.getElementById('lanUrlText').innerText = lanUrl;
      const canvas = document.getElementById('qrCanvas');
      if (window.QRCode && canvas) {
        QRCode.toCanvas(canvas, lanUrl, { width: 190, margin: 1, color: { dark: '#312E81', light: '#FFFFFF' } }, function (error) {
          if (error) console.error(error);
        });
      }
    }

    function toggleMobileModal() {
      const m = document.getElementById('mobileModal');
      m.classList.toggle('hidden');
      if (!m.classList.contains('hidden')) initQRCode();
    }

    function toggleLogModal() {
      const m = document.getElementById('logModal');
      m.classList.toggle('hidden');
      if (!m.classList.contains('hidden')) updateLogUI();
    }

    function pad(n) { return n < 10 ? '0' + n : n; }

    window.addEventListener('DOMContentLoaded', () => {
      initQuestQueue();
      renderCard();
      updateLogUI();
    });
  </script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print("Updated index.html with 50 words and 450 scenario sentences successfully!")
