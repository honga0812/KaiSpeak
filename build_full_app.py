# build_full_app.py - Rebuilds index.html with:
# 1. 每日任務開場引導 (Day streak announcement & 3-2-1 kickoff countdown)
# 2. 瀏覽器音訊解鎖與純真母語示範播放 (User-gesture unlock + Fallback TTS with onend callback)
# 3. 語音辨識大修 (interimResults + stop() 而非 abort() + 音量能量檢測 + 即時顯示識別文字)
# 4. 自動推進流 (單字 ➔ 例句1 ➔ 例句2 ➔ 例句3 ➔ 自動切入下一詞)
# 5. 全站 100% 繁體中文 (zh-Hant-TW)
# 6. GitHub Pages 掃碼與外網直連

import json

with open("vocab.json", "r", encoding="utf-8") as f:
    vocab_data = json.load(f)

vocab_json_str = json.dumps(vocab_data, ensure_ascii=False)

html_content = r'''<!DOCTYPE html>
<html lang="zh-Hant-TW">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
  <meta http-equiv="Pragma" content="no-cache">
  <meta http-equiv="Expires" content="0">
  <title>KaiSpeak - 智慧少兒英語發音評測與任務系統</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@400;600;700&family=Noto+Sans+TC:wght@400;500;700&display=swap" rel="stylesheet">
  <style>
    body {
      font-family: 'Fredoka', 'Noto Sans TC', sans-serif;
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

  <!-- ========================================== -->
  <!-- TOP GLOBAL NAV BAR                         -->
  <!-- ========================================== -->
  <header class="w-full max-w-5xl bg-white/95 backdrop-blur rounded-3xl p-4 shadow-sm border border-indigo-100 mb-4 flex flex-wrap items-center justify-between gap-3">
    <div class="flex items-center gap-3">
      <div class="w-12 h-12 bg-gradient-to-tr from-indigo-600 to-violet-600 rounded-2xl flex items-center justify-center text-white text-2xl shadow-md shadow-indigo-200">
        🎙️
      </div>
      <div>
        <h1 class="text-xl font-black text-indigo-950 tracking-wide flex items-center gap-2">
          KaiSpeak
          <span class="text-xs bg-indigo-100 text-indigo-700 px-2.5 py-0.5 rounded-full font-bold">50 核心詞庫 · 450 中英對照例句</span>
        </h1>
        <p class="text-xs text-slate-500">智慧每日挑戰 · 互動式主動引導 · 錯詞本複習</p>
      </div>
    </div>

    <!-- Mode Selector Tabs -->
    <nav class="flex bg-slate-100 p-1.5 rounded-2xl text-xs font-bold gap-1 shadow-inner">
      <button id="navQuestBtn" onclick="switchAppMode('quest')" class="px-4 py-2 rounded-xl bg-indigo-600 text-white shadow-sm transition flex items-center gap-1.5">
        🎯 每日任務 (主動引導)
      </button>
      <button id="navFreeBtn" onclick="switchAppMode('free')" class="px-4 py-2 rounded-xl text-slate-600 hover:text-slate-900 transition flex items-center gap-1.5">
        📚 自由練習 (50詞庫)
      </button>
      <button id="navAdventureBtn" onclick="switchAppMode('adventure')" class="px-3.5 py-2 rounded-xl text-slate-600 hover:text-slate-900 transition flex items-center gap-1.5">
        🗺️ 探險島 (50關)
      </button>
    </nav>

    <!-- Quick Utilities -->
    <div class="flex items-center gap-2">
      <button onclick="toggleMobileModal()" class="p-2 rounded-xl border border-slate-200 hover:bg-slate-50 text-slate-600 text-xs font-semibold flex items-center gap-1 transition" title="手機掃碼在外網測試">
        📱 <span>掃碼外網測試</span>
      </button>
      <button onclick="toggleLogModal()" class="p-2 rounded-xl border border-slate-200 hover:bg-slate-50 text-slate-600 text-xs font-semibold flex items-center gap-1 transition" title="檢視跟讀日誌">
        📋 <span>日誌 (<span id="logBadge">0</span>)</span>
      </button>
    </div>
  </header>

  <!-- ======================================================== -->
  <!-- KICKOFF OVERLAY: DAILY QUEST WELCOME & 3-SECOND COUNTDOWN -->
  <!-- ======================================================== -->
  <div id="questKickoffOverlay" class="fixed inset-0 bg-slate-900/70 backdrop-blur-md z-50 flex items-center justify-center p-4">
    <div class="bg-white rounded-3xl p-8 max-w-md w-full shadow-2xl border border-indigo-100 text-center flex flex-col items-center transform transition-all duration-300">
      <div class="w-20 h-20 bg-gradient-to-tr from-amber-400 to-orange-500 rounded-3xl flex items-center justify-center text-4xl shadow-lg shadow-amber-200 mb-4 animate-bounce">
        🎯
      </div>
      
      <span class="px-3 py-1 bg-amber-100 text-amber-900 text-xs font-extrabold rounded-full mb-2">
        🔥 連續打卡第 <span id="overlayStreakNum">3</span> 天
      </span>
      
      <h2 class="text-2xl font-black text-indigo-950 mb-2">每日任務即將開始！</h2>
      <p class="text-xs text-slate-500 leading-relaxed mb-6 px-2">
        今日為您精選 <strong>20 個核心詞彙與情境例句</strong>。<br>
        系統將為您<strong>主動示範母語發音</strong>，並自動引導跟讀、打分與連貫推進！
      </p>

      <!-- 3-Second Countdown / Action Button -->
      <div id="overlayCountdownBox" class="mb-4 hidden">
        <div class="text-xs text-indigo-600 font-bold mb-1">準備好耳朵與嘴巴囉！</div>
        <div id="overlayCountdownNum" class="text-6xl font-black text-indigo-600 animate-pulse">3</div>
      </div>

      <button id="overlayStartBtn" onclick="startDailyQuestWithCountdown()" class="w-full py-4 bg-gradient-to-r from-indigo-600 via-indigo-700 to-purple-600 hover:from-indigo-700 hover:to-purple-700 text-white rounded-2xl text-base font-extrabold shadow-xl shadow-indigo-300 transition transform active:scale-95 flex items-center justify-center gap-2">
        <span>🚀 開始今日挑戰</span>
      </button>

      <div class="mt-4 text-[11px] text-slate-400 flex items-center gap-1">
        <span>💡 點選上方按鈕即可啟動耳機與麥克風權限</span>
      </div>
    </div>
  </div>

  <!-- ======================================================== -->
  <!-- MODE 1: DAILY QUEST VIEW (沉浸式主動互動任務流 - 開屏預設)      -->
  <!-- ======================================================== -->
  <section id="viewDailyQuest" class="w-full max-w-5xl flex flex-col gap-4">
    
    <!-- Daily Quest Header Banner -->
    <div class="bg-gradient-to-r from-indigo-600 via-indigo-700 to-purple-700 text-white p-5 rounded-3xl shadow-lg shadow-indigo-100 flex flex-col md:flex-row items-center justify-between gap-4">
      <div class="flex items-center gap-4">
        <div class="w-14 h-14 bg-white/10 backdrop-blur rounded-2xl flex items-center justify-center text-3xl shadow-inner">
          🎯
        </div>
        <div>
          <div class="flex items-center gap-2">
            <h2 class="text-lg font-bold">今日打卡任務 (20 詞互動流)</h2>
            <span class="text-[10px] bg-amber-400 text-amber-950 font-extrabold px-2.5 py-0.5 rounded-full shadow-sm">
              🔥 連續打卡 <span id="questStreakDays">3</span> 天
            </span>
          </div>
          <p class="text-xs text-indigo-100 mt-1">
            系統主動帶領：<strong>先聽母語示範 ➔ 倒數跟讀 ➔ 快速評分 ➔ 自動切例句 ➔ 自動推進下一詞</strong>
          </p>
        </div>
      </div>

      <!-- Overall 20 Words Progress -->
      <div class="flex items-center gap-4 bg-white/10 backdrop-blur px-5 py-3 rounded-2xl border border-white/10 w-full md:w-auto justify-between">
        <div class="text-left md:text-right">
          <div class="text-[11px] text-indigo-200">今日詞彙總進度</div>
          <div class="text-lg font-extrabold font-mono"><span id="questWordProgress">1</span> / 20 詞</div>
        </div>
        <div class="w-28 bg-white/20 h-3 rounded-full overflow-hidden">
          <div id="questProgressBar" class="bg-amber-400 h-full rounded-full transition-all duration-500" style="width: 5%"></div>
        </div>
      </div>
    </div>

    <!-- Active Quest Interactive Studio Card -->
    <div class="bg-white rounded-3xl p-6 md:p-8 shadow-xl shadow-indigo-100/70 border border-indigo-50 flex flex-col items-center relative">
      
      <!-- Top Step Indicators for Current Word: [1.單字] -> [2.例句1] -> [3.例句2] -> [4.例句3] -->
      <div class="w-full max-w-xl flex items-center justify-between mb-6 px-2">
        <div id="qStepDot0" class="flex flex-col items-center gap-1 flex-1">
          <div class="w-8 h-8 rounded-full bg-indigo-600 text-white font-bold text-xs flex items-center justify-center shadow-md">1</div>
          <span class="text-[11px] font-bold text-indigo-700">單字精讀</span>
        </div>
        <div class="h-0.5 bg-slate-200 flex-1 mx-1"></div>
        <div id="qStepDot1" class="flex flex-col items-center gap-1 flex-1 opacity-50">
          <div class="w-8 h-8 rounded-full bg-slate-200 text-slate-600 font-bold text-xs flex items-center justify-center">2</div>
          <span class="text-[11px] font-semibold text-slate-500">情境例句 1</span>
        </div>
        <div class="h-0.5 bg-slate-200 flex-1 mx-1"></div>
        <div id="qStepDot2" class="flex flex-col items-center gap-1 flex-1 opacity-50">
          <div class="w-8 h-8 rounded-full bg-slate-200 text-slate-600 font-bold text-xs flex items-center justify-center">3</div>
          <span class="text-[11px] font-semibold text-slate-500">情境例句 2</span>
        </div>
        <div class="h-0.5 bg-slate-200 flex-1 mx-1"></div>
        <div id="qStepDot3" class="flex flex-col items-center gap-1 flex-1 opacity-50">
          <div class="w-8 h-8 rounded-full bg-slate-200 text-slate-600 font-bold text-xs flex items-center justify-center">4</div>
          <span class="text-[11px] font-semibold text-slate-500">情境例句 3</span>
        </div>
      </div>

      <!-- Proactive State Banner (Tells kid exactly what the system is doing right now) -->
      <div id="questStateBanner" class="w-full max-w-xl p-3.5 rounded-2xl bg-indigo-50 border border-indigo-100 text-center font-bold text-indigo-800 text-sm mb-4 flex items-center justify-center gap-2 shadow-inner transition-all duration-300">
        <span id="questStateIcon" class="text-xl">🔊</span>
        <span id="questStateText">點選下方「開始挑戰」或播放範讀</span>
      </div>

      <!-- Big Illustration & Content Card -->
      <div class="w-full max-w-xl bg-slate-50/70 border border-slate-200/80 rounded-3xl p-6 text-center mb-4 relative">
        <div id="questEmoji" class="text-6xl mb-3 select-none">🪑</div>
        
        <!-- Big Target English Text -->
        <h2 id="questTargetEnglish" class="text-3xl md:text-4xl font-extrabold text-indigo-950 tracking-wide mb-2 leading-tight">
          desk
        </h2>

        <!-- Phonetic -->
        <div id="questPhonetic" class="text-slate-400 font-mono text-sm mb-2">/dɛsk/</div>

        <!-- Chinese Translation (Clear Side-by-Side) -->
        <div class="inline-flex items-center gap-2 bg-white px-4 py-1.5 rounded-full border border-indigo-100 shadow-sm mb-2">
          <span class="text-[10px] font-extrabold uppercase px-1.5 py-0.5 rounded bg-indigo-100 text-indigo-700">中文對照</span>
          <span id="questTargetChinese" class="text-sm md:text-base font-bold text-slate-700">名詞：書桌，辦公桌</span>
        </div>

        <!-- Real-time Speech Recognition Feedback Bubble -->
        <div id="questSpokenFeedbackBox" class="mt-2 text-xs font-bold text-indigo-700 bg-indigo-50/90 px-3.5 py-1.5 rounded-full inline-block border border-indigo-200/60 transition">
          🎤 聽到你說：<span id="questSpokenText" class="text-indigo-950 underline italic font-black">等待錄音...</span>
        </div>
      </div>

      <!-- Audio Waveform Live Display during Recording -->
      <div class="w-full max-w-xl h-11 bg-slate-100 rounded-2xl overflow-hidden border border-slate-200/80 mb-5 flex items-center justify-center relative">
        <canvas id="questWaveformCanvas" class="w-full h-full"></canvas>
        <span id="questWaveformPlaceholder" class="absolute text-xs text-slate-400 font-medium">聲波捕獲區 · 錄音時隨聲音即時波動</span>
      </div>

      <!-- Central Action Area: Big Pulsing Mic & Countdown -->
      <div class="flex flex-col items-center gap-2 mb-5">
        <div class="relative flex items-center justify-center">
          <div id="questMicRing" class="absolute w-24 h-24 rounded-full bg-rose-400/40 hidden pulse-ring"></div>
          <button id="questMicBtn" onclick="toggleQuestManualRecord()" class="relative z-10 w-20 h-20 rounded-full bg-gradient-to-tr from-indigo-600 to-violet-600 text-white shadow-xl shadow-indigo-300 flex flex-col items-center justify-center transition transform active:scale-95 focus:outline-none">
            <span id="questMicIcon" class="text-2xl">🎙️</span>
            <span id="questMicLabel" class="text-[11px] font-bold mt-0.5">點我錄音</span>
          </button>
        </div>
        <div id="questCountdownText" class="text-xs font-bold text-rose-600 hidden">
          錄音倒數: <span id="questCountdownNum">4</span>s (說完會自動停止並評分)
        </div>
      </div>

      <!-- Quick Interactive Flow Controls (Pause/Play, Replay, Retry, Skip) -->
      <div class="flex items-center gap-2 flex-wrap justify-center mb-2">
        <button id="questPlayPauseBtn" onclick="toggleQuestAutoFlow()" class="px-4 py-2 rounded-xl bg-indigo-600 text-white text-xs font-bold shadow-md hover:bg-indigo-700 transition flex items-center gap-1.5">
          <span>⏸️ 暫停引導</span>
        </button>
        <button onclick="replayQuestDemoAudio()" class="px-3.5 py-2 rounded-xl bg-white border border-slate-200 text-slate-700 text-xs font-bold hover:bg-slate-50 transition flex items-center gap-1">
          <span>🔊 再聽範讀</span>
        </button>
        <button onclick="retryQuestCurrentStep()" class="px-3.5 py-2 rounded-xl bg-white border border-slate-200 text-slate-700 text-xs font-bold hover:bg-slate-50 transition flex items-center gap-1">
          <span>🔄 重讀此項</span>
        </button>
        <button onclick="skipQuestStep()" class="px-3.5 py-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-bold transition flex items-center gap-1">
          <span>⏭️ 跳過此項</span>
        </button>
      </div>

      <!-- Simulation Evaluation Buttons for Quick Testing -->
      <div class="mt-4 pt-3 border-t border-slate-100 w-full max-w-xl flex items-center justify-between text-xs text-slate-500">
        <span class="font-bold">快捷免麥測試:</span>
        <div class="flex gap-2">
          <button onclick="simulateQuestEval(92)" class="px-3 py-1 bg-emerald-50 text-emerald-700 rounded-lg border border-emerald-200 font-bold hover:bg-emerald-100">模擬高分(92分)</button>
          <button onclick="simulateQuestEval(68)" class="px-3 py-1 bg-amber-50 text-amber-700 rounded-lg border border-amber-200 font-bold hover:bg-amber-100">模擬弱項(68分)</button>
        </div>
      </div>

    </div>
  </section>

  <!-- ======================================================== -->
  <!-- MODE 2: FREE PRACTICE VIEW (50詞庫 · 錯詞本 · 深度糾音)        -->
  <!-- ======================================================== -->
  <section id="viewFreePractice" class="w-full max-w-5xl hidden flex-col gap-4">
    
    <!-- Filter Bar & Weak Spot Bank -->
    <div class="bg-white rounded-3xl p-5 shadow-sm border border-slate-100 flex flex-col md:flex-row items-center justify-between gap-4">
      <div>
        <h2 class="text-lg font-bold text-slate-800 flex items-center gap-2">
          📚 50 個少兒全景詞彙庫
        </h2>
        <p class="text-xs text-slate-500 mt-1">自主精細複習 · 點選單字即可切入精讀</p>
      </div>

      <!-- Category Filter Pills -->
      <div class="flex items-center gap-1.5 overflow-x-auto hide-scrollbar text-xs">
        <button onclick="setFreeCategory('all')" class="free-cat-btn active px-3 py-1.5 rounded-xl font-bold bg-indigo-600 text-white shadow-sm whitespace-nowrap" data-cat="all">全部 (50)</button>
        <button onclick="setFreeCategory('weak')" class="free-cat-btn px-3 py-1.5 rounded-xl font-bold bg-rose-50 text-rose-700 border border-rose-200 hover:bg-rose-100 whitespace-nowrap" data-cat="weak">⚠️ 錯詞本 (<span id="weakCountBadge">0</span>)</button>
        <button onclick="setFreeCategory('home')" class="free-cat-btn px-3 py-1.5 rounded-xl font-semibold bg-slate-100 text-slate-600 hover:bg-slate-200 whitespace-nowrap" data-cat="home">🏠 家居 (12)</button>
        <button onclick="setFreeCategory('food')" class="free-cat-btn px-3 py-1.5 rounded-xl font-semibold bg-slate-100 text-slate-600 hover:bg-slate-200 whitespace-nowrap" data-cat="food">🍎 飲食 (10)</button>
        <button onclick="setFreeCategory('animals')" class="free-cat-btn px-3 py-1.5 rounded-xl font-semibold bg-slate-100 text-slate-600 hover:bg-slate-200 whitespace-nowrap" data-cat="animals">🐱 動物 (10)</button>
        <button onclick="setFreeCategory('nature')" class="free-cat-btn px-3 py-1.5 rounded-xl font-semibold bg-slate-100 text-slate-600 hover:bg-slate-200 whitespace-nowrap" data-cat="nature">🌳 自然 (6)</button>
        <button onclick="setFreeCategory('play')" class="free-cat-btn px-3 py-1.5 rounded-xl font-semibold bg-slate-100 text-slate-600 hover:bg-slate-200 whitespace-nowrap" data-cat="play">⚽ 玩樂 (7)</button>
      </div>
    </div>

    <!-- 50 Word Cards Grid -->
    <div id="freeGridContainer" class="grid grid-cols-4 sm:grid-cols-5 md:grid-cols-10 gap-2 mb-2">
      <!-- 50 Word buttons populated by JS -->
    </div>

    <!-- Free Practice Workspace (7 Cols + 5 Cols) -->
    <div class="grid grid-cols-1 md:grid-cols-12 gap-6">
      
      <!-- Left Column: Word & 9 Scenario Sentences Card -->
      <div class="md:col-span-7 flex flex-col gap-5">
        <div class="bg-white rounded-3xl p-6 shadow-xl shadow-indigo-100/60 border border-indigo-50 relative overflow-hidden">
          
          <!-- Category & Index -->
          <div class="flex items-center justify-between mb-4">
            <span id="freeCategoryTag" class="px-2.5 py-0.5 rounded-full text-[10px] font-bold bg-slate-100 text-slate-600">
              🏠 日常起居
            </span>
            <div class="flex items-center gap-2">
              <button onclick="prevFreeCard()" class="w-8 h-8 rounded-full border border-slate-200 flex items-center justify-center text-slate-600 hover:bg-slate-100 transition">←</button>
              <span id="freeCardIndex" class="text-xs font-bold text-slate-500 font-mono">1 / 50</span>
              <button onclick="nextFreeCard()" class="w-8 h-8 rounded-full border border-slate-200 flex items-center justify-center text-slate-600 hover:bg-slate-100 transition">→</button>
            </div>
          </div>

          <!-- Illustration & Word Header -->
          <div class="flex items-center gap-5 mb-5">
            <div id="freeWordIllustration" class="w-24 h-24 bg-gradient-to-tr from-amber-50 to-orange-100 rounded-2xl flex items-center justify-center text-5xl shadow-inner border border-amber-200/60 select-none">
              🪑
            </div>
            <div class="flex-1">
              <div class="flex items-center gap-3">
                <h2 id="freeWordText" class="text-3xl font-extrabold text-slate-800 tracking-wide">desk</h2>
                <button onclick="playFreeAudio('word')" title="播放真人母語純正發音" class="px-3 py-1.5 rounded-full bg-indigo-50 hover:bg-indigo-100 text-indigo-700 flex items-center gap-1 text-xs font-bold transition shadow-sm border border-indigo-200/60">
                  🔊 聽真人單字
                </button>
              </div>
              <div class="flex items-center gap-3 mt-1 text-xs text-slate-500">
                <span id="freeWordPhonetic" class="font-mono bg-slate-100 px-2 py-0.5 rounded">/dɛsk/</span>
                <span id="freeWordMeaning" class="font-medium text-slate-600">名詞：書桌，辦公桌</span>
              </div>
            </div>
          </div>

          <!-- 2-Level Scenario Tabs -->
          <div class="bg-slate-50 rounded-2xl p-2.5 border border-slate-100 mb-4">
            <div class="text-[11px] font-bold text-slate-400 uppercase tracking-wider mb-2">情境階梯</div>
            <div class="grid grid-cols-4 gap-1.5 text-xs font-bold">
              <button id="fScTabWord" onclick="selectFreeMode('word')" class="py-2 rounded-xl text-slate-600 hover:text-slate-900 transition text-center truncate px-1">
                單字精讀
              </button>
              <button id="fScTab0" onclick="selectFreeScenarioTab(0)" class="py-2 rounded-xl bg-white text-indigo-700 shadow-sm transition text-center truncate px-1 font-bold">
                情境一 · 描述
              </button>
              <button id="fScTab1" onclick="selectFreeScenarioTab(1)" class="py-2 rounded-xl text-slate-600 hover:text-slate-900 transition text-center truncate px-1">
                情境二 · 動作
              </button>
              <button id="fScTab2" onclick="selectFreeScenarioTab(2)" class="py-2 rounded-xl text-slate-600 hover:text-slate-900 transition text-center truncate px-1">
                情境三 · 對話
              </button>
            </div>

            <!-- Sub-Sentence Selector -->
            <div id="freeSentenceSubSelector" class="mt-2.5 pt-2 border-t border-slate-200/60 grid grid-cols-3 gap-1.5 text-xs">
              <button id="fSentSub0" onclick="selectFreeSentenceIndex(0)" class="py-1.5 rounded-lg bg-indigo-600 text-white font-bold transition text-center truncate px-1 shadow-sm">
                例句 1 (基礎)
              </button>
              <button id="fSentSub1" onclick="selectFreeSentenceIndex(1)" class="py-1.5 rounded-lg text-indigo-900 hover:bg-indigo-100 transition text-center truncate px-1">
                例句 2 (進階)
              </button>
              <button id="fSentSub2" onclick="selectFreeSentenceIndex(2)" class="py-1.5 rounded-lg text-indigo-900 hover:bg-indigo-100 transition text-center truncate px-1">
                例句 3 (拓展)
              </button>
            </div>
          </div>

          <!-- Target Sentence Display with Chinese Translation -->
          <div class="p-4 rounded-2xl bg-indigo-50/70 border border-indigo-100 mb-4">
            <div class="flex items-center justify-between mb-1.5">
              <span id="freeTargetTag" class="text-[10px] font-bold uppercase tracking-wider text-indigo-700 bg-indigo-100 px-2 py-0.5 rounded">
                場景一 · 認知特徵描述 (例句 1/3)
              </span>
              <span class="text-[11px] text-slate-400">自主大聲朗讀</span>
            </div>
            <div class="flex items-start justify-between gap-3">
              <div class="flex-1">
                <p id="freeTargetSentence" class="text-xl md:text-2xl font-bold text-indigo-950 leading-snug">This is a clean wooden desk.</p>
                <div class="mt-2 flex items-baseline gap-2">
                  <span class="text-[10px] font-extrabold uppercase px-1.5 py-0.5 rounded bg-indigo-200/60 text-indigo-800 tracking-wider">譯文對照</span>
                  <p id="freeTargetTranslationText" class="text-sm md:text-base font-medium text-slate-600">這是一張乾淨的木質書桌。</p>
                </div>
              </div>
              <button onclick="playFreeAudio('target')" class="px-3.5 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-700 text-white text-xs font-bold flex items-center gap-1.5 transition shadow-sm whitespace-nowrap mt-0.5">
                <span>🔊 聽真人範讀</span>
              </button>
            </div>
          </div>

          <!-- Free Mode Manual Recording Control -->
          <div class="flex items-center justify-center py-2 gap-4">
            <button id="freeRecordBtn" onclick="handleFreeRecordClick()" class="px-6 py-3 rounded-2xl bg-gradient-to-tr from-rose-500 to-red-500 text-white font-bold text-sm shadow-md hover:from-rose-600 hover:to-red-600 flex items-center gap-2 transition active:scale-95">
              <span>🎙️ 點選進行手動錄音評測</span>
            </button>
          </div>

        </div>
      </div>

      <!-- Right Column: Diagnostics & SRS Memory Card -->
      <div class="md:col-span-5 flex flex-col gap-5">
        
        <!-- Phonetic Diagnostics & Score Card -->
        <div class="bg-white rounded-3xl p-6 shadow-xl shadow-indigo-100/60 border border-indigo-50">
          <div class="flex items-center justify-between mb-4">
            <h3 class="font-extrabold text-slate-800 text-sm flex items-center gap-1.5">
              <span>📊 發音評分與診斷</span>
            </h3>
            <span id="freeEvalBadge" class="text-xs px-2.5 py-0.5 rounded-full font-bold bg-slate-100 text-slate-500">待評測</span>
          </div>

          <div class="flex items-center justify-center py-4 bg-gradient-to-b from-indigo-50/50 to-transparent rounded-2xl mb-4">
            <div class="text-center">
              <div id="freeScoreDisplay" class="text-5xl font-black text-slate-300">--</div>
              <div id="freeScoreLabel" class="text-xs font-bold text-slate-400 mt-1">發音綜合得分</div>
            </div>
          </div>

          <!-- Words Breakdown -->
          <div class="mb-4">
            <div class="text-xs font-bold text-slate-600 mb-2">逐詞發音診斷:</div>
            <div id="freeWordsBreakdown" class="flex flex-wrap gap-2 min-h-[42px] p-2.5 bg-slate-50 rounded-xl border border-slate-100 items-center">
              <span class="text-xs text-slate-400 italic">點選錄音後將在此顯示單詞發音精準度</span>
            </div>
          </div>

          <!-- Feedback Note -->
          <div id="freeFeedbackBox" class="p-3 rounded-xl bg-slate-50 border border-slate-100 text-xs text-slate-600">
            💡 提示：按住錄音按鈕清晰大聲朗讀，系統將即時診斷連讀、音素與重音。
          </div>
        </div>

        <!-- SRS Memory Curve -->
        <div class="bg-white rounded-3xl p-5 shadow-sm border border-slate-100 text-xs">
          <h4 class="font-bold text-slate-800 mb-2 flex items-center gap-1.5">
            <span>🧠 艾賓浩斯智慧複習排程</span>
          </h4>
          <div class="space-y-1.5 text-slate-600">
            <div class="flex justify-between">
              <span>掌握等級:</span>
              <span id="freeSrsLevel" class="font-bold text-indigo-600">L1 · 初學階段</span>
            </div>
            <div class="flex justify-between">
              <span>下次推薦溫習:</span>
              <span id="freeSrsNext" class="font-bold text-slate-700">明天清晨</span>
            </div>
          </div>
        </div>

      </div>

    </div>
  </section>

  <!-- ======================================================== -->
  <!-- MODE 3: 50-STAGE ADVENTURE ISLAND                        -->
  <!-- ======================================================== -->
  <section id="viewAdventure" class="w-full max-w-5xl hidden flex-col gap-4">
    <div class="bg-gradient-to-br from-emerald-500 via-teal-600 to-indigo-700 text-white p-6 rounded-3xl shadow-xl relative overflow-hidden">
      <div class="relative z-10 flex flex-col md:flex-row items-center justify-between gap-4">
        <div>
          <span class="text-xs font-bold uppercase tracking-wider bg-white/20 px-3 py-1 rounded-full">50-Stage Adventure</span>
          <h2 class="text-2xl font-black mt-2">英語發音大探險：50關語音群島</h2>
          <p class="text-xs text-emerald-100 mt-1">橫跨 5 大語音島嶼，80分即可過關點亮三星！</p>
        </div>
        <div class="bg-white/10 backdrop-blur px-5 py-3 rounded-2xl border border-white/20 text-center">
          <div class="text-xs text-emerald-200">當前總星數</div>
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
  <!-- MODAL: MOBILE & QR CODE TEST                             -->
  <!-- ======================================================== -->
  <div id="mobileModal" class="fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-50 flex items-center justify-center p-4 hidden">
    <div class="bg-white rounded-3xl p-6 max-w-md w-full shadow-2xl border border-slate-100 text-center">
      <div class="flex justify-between items-center mb-4">
        <h3 class="text-base font-bold text-slate-800">📱 手機 / 平板掃碼測試</h3>
        <button onclick="toggleMobileModal()" class="text-slate-400 hover:text-slate-600 font-bold text-lg">✕</button>
      </div>

      <p class="text-xs text-slate-500 mb-4">
        請使用手機相機或微信掃碼開啟，公網免配置直接呼叫麥克風：
      </p>

      <div class="w-48 h-48 bg-white border border-slate-200 rounded-2xl mx-auto flex items-center justify-center shadow-inner p-2 mb-3">
        <canvas id="qrCanvas" class="w-full h-full"></canvas>
      </div>

      <div class="text-xs font-mono bg-indigo-50 p-2.5 rounded-xl text-indigo-900 break-all border border-indigo-100 mb-4">
        <a id="lanUrlText" href="https://honga0812.github.io/KaiSpeak/" target="_blank" class="underline font-bold text-indigo-700">https://honga0812.github.io/KaiSpeak/</a>
      </div>

      <button onclick="toggleMobileModal()" class="w-full py-2.5 bg-indigo-600 text-white rounded-xl text-xs font-bold hover:bg-indigo-700 transition">
        關閉
      </button>
    </div>
  </div>

  <!-- ======================================================== -->
  <!-- MODAL: PRACTICE LOGS                                     -->
  <!-- ======================================================== -->
  <div id="logModal" class="fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-50 flex items-center justify-center p-4 hidden">
    <div class="bg-white rounded-3xl p-6 max-w-2xl w-full shadow-2xl border border-slate-100 flex flex-col max-h-[85vh]">
      <div class="flex justify-between items-center mb-4">
        <div>
          <h3 class="text-base font-bold text-slate-800 flex items-center gap-2">
            <span>📋 發音練習與跟讀日誌</span>
            <span class="text-xs bg-indigo-100 text-indigo-700 font-bold px-2 py-0.5 rounded-full" id="totalLogsNum">0</span>
          </h3>
          <p class="text-xs text-slate-400">已記錄每次練習時間戳、得分與詳細對照</p>
        </div>
        <div class="flex items-center gap-2">
          <button onclick="exportLogsCSV()" class="px-3 py-1.5 bg-indigo-50 hover:bg-indigo-100 text-indigo-700 border border-indigo-200 rounded-xl text-xs font-bold transition flex items-center gap-1">
            📥 匯出 CSV
          </button>
          <button onclick="toggleLogModal()" class="text-slate-400 hover:text-slate-600 font-bold text-lg ml-2">✕</button>
        </div>
      </div>

      <div class="overflow-y-auto flex-1 border border-slate-100 rounded-2xl">
        <table class="w-full text-left border-collapse text-xs">
          <thead class="bg-slate-50 sticky top-0 text-slate-500 font-semibold border-b border-slate-100">
            <tr>
              <th class="p-2.5">時間</th>
              <th class="p-2.5">跟讀內容 (中英對照)</th>
              <th class="p-2.5">類型</th>
              <th class="p-2.5">得分</th>
              <th class="p-2.5">狀態</th>
            </tr>
          </thead>
          <tbody id="logsTableBody" class="divide-y divide-slate-100">
            <tr><td colspan="5" class="p-6 text-center text-slate-400 italic">暫無練習記錄</td></tr>
          </tbody>
        </table>
      </div>

      <div class="mt-4 pt-3 border-t border-slate-100 flex justify-between items-center">
        <button onclick="clearLogs()" class="text-xs text-rose-500 hover:underline">清空所有記錄</button>
        <button onclick="toggleLogModal()" class="px-4 py-2 bg-slate-800 text-white rounded-xl text-xs font-bold hover:bg-slate-900 transition">關閉</button>
      </div>
    </div>
  </div>

  <script>
    // --- 50 Master Vocabulary with 3 Scenarios x 3 Sentences = 9 Sentences (Bilingual) ---
    const MASTER_VOCAB = ''' + vocab_json_str + r''';

    // Application State
    let appMode = 'quest'; // 'quest' (default) | 'free' | 'adventure'
    
    // --- Quest Mode State (Proactive Interactive Flow) ---
    let questQueue = []; // 20 words for today
    let questWordIdx = 0; // 0 to 19
    let questSubStep = 0; // 0: Word, 1: Scenario 0 Sent 0, 2: Scenario 0 Sent 1, 3: Scenario 0 Sent 2
    let questAutoPlay = false; // Is proactive walkthrough running?
    let questAudioPlayer = new Audio(); // Reusable audio element for pre-warming
    let questRecTimer = null;
    let questCountdownVal = 6;
    let overlayTimer = null;

    // --- Free Mode State ---
    let freeCardIndex = 0; // 0 to 49
    let freePracticeMode = 'scenario'; // 'scenario' | 'word'
    let freeScenarioIdx = 0;
    let freeSentenceIdx = 0;
    let freeAudioPlayer = new Audio();

    // --- Common States & Storage ---
    let isRecording = false;
    let recognition = null;
    let audioContext = null;
    let analyser = null;
    let microphoneStream = null;
    let animFrameId = null;
    let maxAcousticEnergy = 0;
    let lastInterimSpeech = "";

    let streakDays = parseInt(localStorage.getItem('kai_streak_days') || '3');
    let practiceLogs = JSON.parse(localStorage.getItem('kai_practice_logs') || '[]');
    let adventureStars = JSON.parse(localStorage.getItem('kai_adventure_stars') || '{}');

    // --- Initial Queue Setup (10 New, 8 Review, 2 Consolidate) ---
    function initQuestQueue() {
      const news = MASTER_VOCAB.filter(v => v.role === 'new');
      const reviews = MASTER_VOCAB.filter(v => v.role === 'review');
      const consolidates = MASTER_VOCAB.filter(v => v.role === 'consolidate');

      const q = [
        ...news.slice(0, 10),
        ...reviews.slice(0, 8),
        ...consolidates.slice(0, 2)
      ];

      let idx = 0;
      while (q.length < 20 && idx < MASTER_VOCAB.length) {
        if (!q.includes(MASTER_VOCAB[idx])) q.push(MASTER_VOCAB[idx]);
        idx++;
      }
      questQueue = q;
    }

    // ========================================================
    // KICKOFF & WELCOME GUIDANCE (第幾天提示 + 3秒倒數 + 聲音解鎖)
    // ========================================================
    function startDailyQuestWithCountdown() {
      // 1. Pre-warm Audio (unlocks browser autoplay policy)
      try {
        questAudioPlayer.src = "data:audio/wav;base64,UklGRigAAABXQVZFZm10IBIAAAABAAEARKwAAIhYAQACABAAAABkYXRhAgAAAAEA";
        questAudioPlayer.play().then(() => questAudioPlayer.pause()).catch(()=>{});
        
        const AC = window.AudioContext || window.webkitAudioContext;
        if (AC) {
          const dummyCtx = new AC();
          if (dummyCtx.state === 'suspended') dummyCtx.resume();
        }
      } catch(e) {}

      // 2. Hide Start Button and show 3-2-1 Countdown
      document.getElementById('overlayStartBtn').classList.add('hidden');
      const countBox = document.getElementById('overlayCountdownBox');
      const countNum = document.getElementById('overlayCountdownNum');
      countBox.classList.remove('hidden');

      let cd = 3;
      countNum.innerText = cd;

      if (overlayTimer) clearInterval(overlayTimer);
      overlayTimer = setInterval(() => {
        cd--;
        if (cd > 0) {
          countNum.innerText = cd;
        } else if (cd === 0) {
          countNum.innerText = "GO! 🎧";
        } else {
          clearInterval(overlayTimer);
          overlayTimer = null;
          // Hide overlay and start quest walkthrough
          document.getElementById('questKickoffOverlay').classList.add('hidden');
          questAutoPlay = true;
          document.getElementById('questPlayPauseBtn').innerHTML = '<span>⏸️ 暫停引導</span>';
          document.getElementById('questPlayPauseBtn').className = "px-4 py-2 rounded-xl bg-amber-500 hover:bg-amber-600 text-white text-xs font-bold shadow-md transition flex items-center gap-1.5";
          runQuestAutoStep();
        }
      }, 900);
    }

    // --- App Mode Switcher ---
    function switchAppMode(mode) {
      appMode = mode;
      if (questAudioPlayer) { questAudioPlayer.pause(); }
      if (freeAudioPlayer) { freeAudioPlayer.pause(); }
      if (isRecording) stopRecording();

      const vQuest = document.getElementById('viewDailyQuest');
      const vFree = document.getElementById('viewFreePractice');
      const vAdv = document.getElementById('viewAdventure');

      const bQuest = document.getElementById('navQuestBtn');
      const bFree = document.getElementById('navFreeBtn');
      const bAdv = document.getElementById('navAdventureBtn');

      [bQuest, bFree, bAdv].forEach(b => {
        b.className = "px-4 py-2 rounded-xl text-slate-600 hover:text-slate-900 transition flex items-center gap-1.5";
      });

      if (mode === 'quest') {
        vQuest.classList.remove('hidden');
        vFree.classList.add('hidden');
        vAdv.classList.add('hidden');
        bQuest.className = "px-4 py-2 rounded-xl bg-indigo-600 text-white shadow-sm transition flex items-center gap-1.5";
        renderQuestCard();
      } else if (mode === 'free') {
        vQuest.classList.add('hidden');
        vFree.classList.remove('hidden');
        vAdv.classList.add('hidden');
        bFree.className = "px-4 py-2 rounded-xl bg-indigo-600 text-white shadow-sm transition flex items-center gap-1.5";
        renderFreeGrid();
        renderFreeCard();
      } else {
        vQuest.classList.add('hidden');
        vFree.classList.add('hidden');
        vAdv.classList.remove('hidden');
        bAdv.className = "px-4 py-2 rounded-xl bg-indigo-600 text-white shadow-sm transition flex items-center gap-1.5";
        renderAdventureMap();
      }
    }

    // ========================================================
    // QUEST MODE: PROACTIVE INTERACTIVE WORKTHROUGH ENGINE
    // ========================================================
    function currentQuestCard() {
      return questQueue[questWordIdx] || MASTER_VOCAB[0];
    }

    function renderQuestCard() {
      const card = currentQuestCard();
      
      // Update Progress
      document.getElementById('questWordProgress').innerText = questWordIdx + 1;
      const pct = Math.round(((questWordIdx) / 20) * 100);
      document.getElementById('questProgressBar').style.width = `${Math.max(5, pct)}%`;
      document.getElementById('questStreakDays').innerText = streakDays;
      document.getElementById('overlayStreakNum').innerText = streakDays;

      // Update Step Indicators: 0:單字, 1:例句1, 2:例句2, 3:例句3
      [0, 1, 2, 3].forEach(step => {
        const dot = document.getElementById(`qStepDot${step}`);
        if (!dot) return;
        const circle = dot.querySelector('div');
        const text = dot.querySelector('span');
        if (step === questSubStep) {
          dot.classList.remove('opacity-50');
          circle.className = "w-8 h-8 rounded-full bg-indigo-600 text-white font-bold text-xs flex items-center justify-center shadow-md scale-110 transition";
          text.className = "text-[11px] font-bold text-indigo-700";
        } else if (step < questSubStep) {
          dot.classList.remove('opacity-50');
          circle.className = "w-8 h-8 rounded-full bg-emerald-500 text-white font-bold text-xs flex items-center justify-center shadow-sm";
          circle.innerHTML = "✓";
          text.className = "text-[11px] font-semibold text-emerald-700";
        } else {
          dot.classList.add('opacity-50');
          circle.className = "w-8 h-8 rounded-full bg-slate-200 text-slate-600 font-bold text-xs flex items-center justify-center";
          circle.innerHTML = `${step + 1}`;
          text.className = "text-[11px] font-semibold text-slate-500";
        }
      });

      // Target Content
      document.getElementById('questEmoji').innerText = card.emoji;
      const engEl = document.getElementById('questTargetEnglish');
      const chiEl = document.getElementById('questTargetChinese');
      const phoEl = document.getElementById('questPhonetic');

      if (questSubStep === 0) {
        // Word
        engEl.innerText = card.word;
        chiEl.innerText = card.meaning || "單字釋義";
        phoEl.innerText = card.phonetic || "";
        phoEl.classList.remove('hidden');
      } else {
        // Sentence under Scenario 0
        const sc = card.scenarios[0];
        const sentIdx = questSubStep - 1;
        const sentText = sc.sentences[sentIdx] || "";
        const transText = (sc.translations && sc.translations[sentIdx]) ? sc.translations[sentIdx] : "";
        engEl.innerText = sentText;
        chiEl.innerText = transText;
        phoEl.classList.add('hidden');
      }

      document.getElementById('questSpokenText').innerText = "等待朗讀...";
    }

    function setQuestStatus(text, icon = "🔊", classes = "bg-indigo-50 text-indigo-800") {
      const banner = document.getElementById('questStateBanner');
      const txt = document.getElementById('questStateText');
      const ico = document.getElementById('questStateIcon');
      txt.innerText = text;
      ico.innerText = icon;
      banner.className = `w-full max-w-xl p-3.5 rounded-2xl border text-center font-bold text-sm mb-4 flex items-center justify-center gap-2 shadow-inner transition-all duration-300 ${classes}`;
    }

    function toggleQuestAutoFlow() {
      questAutoPlay = !questAutoPlay;
      const btn = document.getElementById('questPlayPauseBtn');
      if (questAutoPlay) {
        btn.innerHTML = '<span>⏸️ 暫停引導</span>';
        btn.className = "px-4 py-2 rounded-xl bg-amber-500 hover:bg-amber-600 text-white text-xs font-bold shadow-md transition flex items-center gap-1.5";
        runQuestAutoStep();
      } else {
        btn.innerHTML = '<span>▶️ 繼續主動引導</span>';
        btn.className = "px-4 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-700 text-white text-xs font-bold shadow-md transition flex items-center gap-1.5";
        if (questAudioPlayer) { questAudioPlayer.pause(); }
        if (isRecording) stopRecording();
        setQuestStatus("引導已暫停，您可以點選「繼續主動引導」或手動錄音", "⏸️", "bg-slate-100 text-slate-700");
      }
    }

    function runQuestAutoStep() {
      renderQuestCard();

      // 1. Play Demo Audio Loud & Clear
      setQuestStatus("正在播放母語示範發音，請仔細聽...", "🔊", "bg-indigo-100 text-indigo-800 animate-pulse border-indigo-200");
      playQuestDemoAudio(() => {
        // 2. Demo Audio Ended -> Trigger Recording
        startQuestAutoRecord();
      });
    }

    function getQuestAudioSrc() {
      const card = currentQuestCard();
      if (questSubStep === 0) {
        return card.audioWord || `audio/word_${card.id}.m4a`;
      } else {
        const sentIdx = questSubStep - 1;
        return `audio/sentence_${card.id}_0_${sentIdx}.m4a`;
      }
    }

    function playQuestDemoAudio(onEndCallback) {
      if (questAudioPlayer) {
        questAudioPlayer.pause();
        questAudioPlayer.currentTime = 0;
      }

      const audioSrc = getQuestAudioSrc();
      let hasEnded = false;

      const finish = () => {
        if (!hasEnded) {
          hasEnded = true;
          if (onEndCallback) onEndCallback();
        }
      };

      questAudioPlayer.src = audioSrc;
      questAudioPlayer.onended = finish;
      
      questAudioPlayer.onerror = () => {
        // Fallback to Web Speech API
        const text = document.getElementById('questTargetEnglish').innerText;
        fallbackNaturalTTS(text, finish);
      };

      const playPromise = questAudioPlayer.play();
      if (playPromise !== undefined) {
        playPromise.catch(e => {
          console.warn("Audio play blocked or missing, using TTS:", e);
          const text = document.getElementById('questTargetEnglish').innerText;
          fallbackNaturalTTS(text, finish);
        });
      }
    }

    function replayQuestDemoAudio() {
      playQuestDemoAudio(null);
    }

    function startQuestAutoRecord() {
      setQuestStatus("輪到你啦，請大聲跟讀！(錄音中...)", "🎙️", "bg-rose-100 text-rose-800 font-extrabold border-rose-200");
      
      const ring = document.getElementById('questMicRing');
      const countBox = document.getElementById('questCountdownText');
      const countNum = document.getElementById('questCountdownNum');
      ring.classList.remove('hidden');
      countBox.classList.remove('hidden');

      questCountdownVal = questSubStep === 0 ? 5 : 7;
      countNum.innerText = questCountdownVal;
      document.getElementById('questSpokenText').innerText = "聆聽中，請大聲朗讀...";

      startRecording(onSpeechSuccess, onSpeechFail);

      if (questRecTimer) clearInterval(questRecTimer);
      questRecTimer = setInterval(() => {
        questCountdownVal--;
        countNum.innerText = questCountdownVal;
        if (questCountdownVal <= 0) {
          clearInterval(questRecTimer);
          questRecTimer = null;
          // Gracefully stop recognition (processes speech, DOES NOT abort!)
          if (isRecording) {
            if (recognition) {
              try { recognition.stop(); } catch(e){}
            }
          }
        }
      }, 1000);
    }

    function toggleQuestManualRecord() {
      if (isRecording) {
        if (questRecTimer) { clearInterval(questRecTimer); questRecTimer = null; }
        if (recognition) { try { recognition.stop(); } catch(e){} }
        stopRecording();
      } else {
        startQuestAutoRecord();
      }
    }

    function onSpeechSuccess(spokenText) {
      handleQuestSpeechEvaluation(spokenText);
    }

    function onSpeechFail(err) {
      // If error but we captured interim speech or acoustic volume
      const bestText = lastInterimSpeech || "";
      handleQuestSpeechEvaluation(bestText);
    }

    function handleQuestSpeechEvaluation(spokenText) {
      if (questRecTimer) { clearInterval(questRecTimer); questRecTimer = null; }
      const ring = document.getElementById('questMicRing');
      const countBox = document.getElementById('questCountdownText');
      ring.classList.add('hidden');
      countBox.classList.add('hidden');

      const targetText = document.getElementById('questTargetEnglish').innerText;
      
      // Update Realtime Display
      const feedbackEl = document.getElementById('questSpokenText');
      feedbackEl.innerText = spokenText ? `"${spokenText}"` : (maxAcousticEnergy > 15 ? "(聽見了聲音，但咬字需更清晰)" : "(未偵測到聲音)");

      const score = calculateScore(targetText, spokenText, maxAcousticEnergy);
      const isGood = score >= 75;

      setQuestStatus(
        isGood ? `🌟 太棒了！評測得分：${score} 分！` : `💪 讀得不錯！得分：${score} 分 (已自動收納至錯詞本)`,
        isGood ? "⭐" : "💡",
        isGood ? "bg-emerald-100 text-emerald-800 font-black border-emerald-300" : "bg-amber-100 text-amber-900 font-black border-amber-300"
      );

      // Record to Log & SRS
      const card = currentQuestCard();
      const typeStr = questSubStep === 0 ? "每日任務-單字" : `每日任務-例句${questSubStep}`;
      recordPracticeLog(card.word, targetText, score, isGood ? "已熟練" : "待加強", typeStr);

      // ALWAYS automatically advance after 1.8 seconds (unless user manually paused autoPlay)
      setTimeout(() => {
        if (questAutoPlay) {
          advanceQuestStep();
        }
      }, 1800);
    }

    function simulateQuestEval(simScore) {
      const targetText = document.getElementById('questTargetEnglish').innerText;
      const mockSpoken = simScore >= 80 ? targetText : "somethin";
      maxAcousticEnergy = 50;
      handleQuestSpeechEvaluation(mockSpoken);
    }

    function advanceQuestStep() {
      questSubStep++;
      if (questSubStep > 3) {
        // Finished word + 3 sentences for current word!
        questSubStep = 0;
        questWordIdx++;
        if (questWordIdx >= questQueue.length) {
          // Finished all 20 words
          streakDays++;
          localStorage.setItem('kai_streak_days', streakDays.toString());
          alert("🎉 恭喜！今日 20 個任務單字與例句已全部挑戰完成！打卡成功，連續天數已升至 " + streakDays + " 天！");
          questWordIdx = 0;
          switchAppMode('free');
          return;
        }
      }
      runQuestAutoStep();
    }

    function retryQuestCurrentStep() {
      runQuestAutoStep();
    }

    function skipQuestStep() {
      advanceQuestStep();
    }

    // ========================================================
    // MODE 2: FREE PRACTICE WORKSPACE IMPLEMENTATION
    // ========================================================
    function currentFreeCard() {
      return MASTER_VOCAB[freeCardIndex] || MASTER_VOCAB[0];
    }

    function renderFreeGrid() {
      const container = document.getElementById('freeGridContainer');
      container.innerHTML = '';

      MASTER_VOCAB.forEach((c, idx) => {
        const btn = document.createElement('button');
        const isActive = idx === freeCardIndex;
        const wordLogs = practiceLogs.filter(l => l.word === c.word);
        const hasLogs = wordLogs.length > 0;
        const best = hasLogs ? Math.max(...wordLogs.map(l => l.score)) : 0;
        const isWeak = best > 0 && best < 75;

        btn.className = `p-2 rounded-2xl flex flex-col items-center justify-center border transition transform active:scale-95 ${
          isActive 
            ? 'bg-indigo-600 text-white shadow-md shadow-indigo-200 border-indigo-600 scale-105' 
            : (isWeak 
                ? 'bg-rose-50 text-rose-800 border-rose-200 hover:bg-rose-100' 
                : 'bg-white text-slate-700 border-slate-100 hover:border-indigo-200 hover:shadow-sm')
        }`;

        btn.innerHTML = `
          <span class="text-xl mb-0.5 select-none">${c.emoji}</span>
          <span class="text-[11px] font-extrabold truncate w-full text-center">${c.word}</span>
          <span class="text-[9px] font-bold ${isActive ? 'text-indigo-200' : (best >= 80 ? 'text-emerald-500' : 'text-slate-400')}">
            ${best > 0 ? best + '分' : c.category.slice(0,2)}
          </span>
        `;

        btn.onclick = () => {
          freeCardIndex = idx;
          freeScenarioIdx = 0;
          freeSentenceIdx = 0;
          renderFreeGrid();
          renderFreeCard();
        };

        container.appendChild(btn);
      });

      // Update Weak Spot Count
      const weakWords = MASTER_VOCAB.filter(c => {
        const wl = practiceLogs.filter(l => l.word === c.word);
        if (wl.length === 0) return false;
        return Math.max(...wl.map(l => l.score)) < 75;
      });
      document.getElementById('weakCountBadge').innerText = weakWords.length;
    }

    function setFreeCategory(cat) {
      document.querySelectorAll('.free-cat-btn').forEach(b => {
        if (b.dataset.cat === cat) {
          b.className = "free-cat-btn active px-3 py-1.5 rounded-xl font-bold bg-indigo-600 text-white shadow-sm whitespace-nowrap";
        } else {
          b.className = "free-cat-btn px-3 py-1.5 rounded-xl font-semibold bg-slate-100 text-slate-600 hover:bg-slate-200 whitespace-nowrap";
        }
      });

      const container = document.getElementById('freeGridContainer');
      Array.from(container.children).forEach((btn, idx) => {
        const c = MASTER_VOCAB[idx];
        const wl = practiceLogs.filter(l => l.word === c.word);
        const best = wl.length > 0 ? Math.max(...wl.map(l => l.score)) : 0;
        const isWeak = best > 0 && best < 75;

        if (cat === 'all') {
          btn.classList.remove('hidden');
        } else if (cat === 'weak') {
          if (isWeak) btn.classList.remove('hidden'); else btn.classList.add('hidden');
        } else {
          if (c.category === cat) btn.classList.remove('hidden'); else btn.classList.add('hidden');
        }
      });
    }

    function renderFreeCard() {
      const card = currentFreeCard();
      document.getElementById('freeCardIndex').innerText = `${freeCardIndex + 1} / 50`;
      document.getElementById('freeWordIllustration').innerText = card.emoji;
      document.getElementById('freeWordText').innerText = card.word;
      document.getElementById('freeWordPhonetic').innerText = card.phonetic;
      document.getElementById('freeWordMeaning').innerText = card.meaning;

      const catMap = { home: "🏠 日常起居", food: "🍎 美味飲食", animals: "🐱 動物夥伴", nature: "🌳 大自然", play: "⚽ 趣味玩樂" };
      document.getElementById('freeCategoryTag').innerText = catMap[card.category] || "生活情境";

      updateFreeTargetBox();
    }

    function selectFreeMode(mode) {
      freePracticeMode = mode;
      updateFreeTargetBox();
    }

    function selectFreeScenarioTab(scIdx) {
      freePracticeMode = 'scenario';
      freeScenarioIdx = scIdx;
      freeSentenceIdx = 0;
      updateFreeTargetBox();
    }

    function selectFreeSentenceIndex(sentIdx) {
      freePracticeMode = 'scenario';
      freeSentenceIdx = sentIdx;
      updateFreeTargetBox();
    }

    function updateFreeTargetBox() {
      const card = currentFreeCard();
      const sentenceEl = document.getElementById('freeTargetSentence');
      const transEl = document.getElementById('freeTargetTranslationText');
      const tagEl = document.getElementById('freeTargetTag');
      const subSelector = document.getElementById('freeSentenceSubSelector');

      ['fScTabWord', 'fScTab0', 'fScTab1', 'fScTab2'].forEach(id => {
        const el = document.getElementById(id);
        if (el) el.className = "py-2 rounded-xl text-slate-600 hover:text-slate-900 transition text-center truncate px-1";
      });

      if (freePracticeMode === 'word') {
        subSelector.classList.add('hidden');
        sentenceEl.innerText = card.word;
        if (transEl) transEl.innerText = card.meaning || "";
        tagEl.innerText = "單字精讀 · 輔音與咬字練習";
        document.getElementById('fScTabWord').className = "py-2 rounded-xl bg-white text-indigo-700 shadow-sm transition text-center truncate px-1 font-bold";
      } else {
        subSelector.classList.remove('hidden');
        document.getElementById(`fScTab${freeScenarioIdx}`).className = "py-2 rounded-xl bg-white text-indigo-700 shadow-sm transition text-center truncate px-1 font-bold";

        ['fSentSub0', 'fSentSub1', 'fSentSub2'].forEach((id, idx) => {
          const btn = document.getElementById(id);
          if (idx === freeSentenceIdx) {
            btn.className = "py-1.5 rounded-lg bg-indigo-600 text-white font-bold transition text-center truncate px-1 shadow-sm";
          } else {
            btn.className = "py-1.5 rounded-lg text-indigo-900 hover:bg-indigo-100 transition text-center truncate px-1";
          }
        });

        const sc = card.scenarios[freeScenarioIdx];
        const targetText = sc.sentences[freeSentenceIdx];
        const transText = (sc.translations && sc.translations[freeSentenceIdx]) ? sc.translations[freeSentenceIdx] : "";
        sentenceEl.innerText = targetText;
        if (transEl) transEl.innerText = transText;
        tagEl.innerText = `${sc.tag} (例句 ${freeSentenceIdx + 1}/3)`;
      }
    }

    function nextFreeCard() {
      freeCardIndex = (freeCardIndex + 1) % 50;
      freeScenarioIdx = 0;
      freeSentenceIdx = 0;
      renderFreeGrid();
      renderFreeCard();
    }

    function prevFreeCard() {
      freeCardIndex = (freeCardIndex - 1 + 50) % 50;
      freeScenarioIdx = 0;
      freeSentenceIdx = 0;
      renderFreeGrid();
      renderFreeCard();
    }

    function playFreeAudio(target) {
      if (freeAudioPlayer) { freeAudioPlayer.pause(); }
      const card = currentFreeCard();
      let src = "";
      let txt = "";

      if (target === 'word' || freePracticeMode === 'word') {
        src = card.audioWord || `audio/word_${card.id}.m4a`;
        txt = card.word;
      } else {
        src = `audio/sentence_${card.id}_${freeScenarioIdx}_${freeSentenceIdx}.m4a`;
        txt = card.scenarios[freeScenarioIdx].sentences[freeSentenceIdx];
      }

      freeAudioPlayer.src = src;
      freeAudioPlayer.play().catch(() => fallbackNaturalTTS(txt, null));
    }

    function handleFreeRecordClick() {
      if (isRecording) {
        if (recognition) { try { recognition.stop(); } catch(e){} }
        stopRecording();
      } else {
        document.getElementById('freeRecordBtn').innerHTML = "<span>🛑 正在錄音... 點選停止</span>";
        startRecording(
          (text) => {
            document.getElementById('freeRecordBtn').innerHTML = "<span>🎙️ 點選進行手動錄音評測</span>";
            evaluateFreeAttempt(text);
          },
          (err) => {
            document.getElementById('freeRecordBtn').innerHTML = "<span>🎙️ 點選進行手動錄音評測</span>";
            evaluateFreeAttempt(lastInterimSpeech || "");
          }
        );
      }
    }

    function evaluateFreeAttempt(spokenText) {
      const targetText = document.getElementById('freeTargetSentence').innerText;
      const score = calculateScore(targetText, spokenText, maxAcousticEnergy);

      document.getElementById('freeScoreDisplay').innerText = score;
      document.getElementById('freeScoreDisplay').className = `text-5xl font-black ${score >= 80 ? 'text-emerald-500' : (score >= 60 ? 'text-indigo-600' : 'text-rose-500')}`;
      document.getElementById('freeEvalBadge').innerText = score >= 80 ? "發音純正 ⭐⭐⭐" : (score >= 60 ? "良好 ⭐⭐" : "需加強 ⭐");
      document.getElementById('freeEvalBadge').className = `text-xs px-2.5 py-0.5 rounded-full font-bold ${score >= 80 ? 'bg-emerald-100 text-emerald-800' : 'bg-amber-100 text-amber-800'}`;

      // Breakdown chips
      const targetWords = targetText.toLowerCase().replace(/[^a-z0-9\s]/g, '').split(/\s+/).filter(Boolean);
      const spokenWords = (spokenText || '').toLowerCase().replace(/[^a-z0-9\s]/g, '').split(/\s+/).filter(Boolean);
      const container = document.getElementById('freeWordsBreakdown');
      container.innerHTML = '';

      targetWords.forEach(w => {
        const passed = spokenWords.includes(w) || spokenWords.some(sw => sw.startsWith(w.slice(0, 3)));
        const chip = document.createElement('span');
        chip.className = `px-2 py-1 rounded-lg text-xs font-bold border ${passed ? 'bg-emerald-50 text-emerald-700 border-emerald-200' : 'bg-rose-50 text-rose-700 border-rose-200 animate-pulse'}`;
        chip.innerText = `${w} ${passed ? '✓' : '✗'}`;
        container.appendChild(chip);
      });

      const card = currentFreeCard();
      const typeStr = freePracticeMode === 'word' ? '自主單字' : `情境${freeScenarioIdx+1}-句${freeSentenceIdx+1}`;
      recordPracticeLog(card.word, targetText, score, score >= 75 ? '已掌握' : '需加強', typeStr);
      renderFreeGrid();
    }

    // ========================================================
    // MODE 3: 50-STAGE ADVENTURE ISLAND
    // ========================================================
    function renderAdventureMap() {
      const container = document.getElementById('adventureNodesContainer');
      container.innerHTML = '';
      let totalStars = 0;

      MASTER_VOCAB.forEach((c, idx) => {
        const stars = adventureStars[c.id] || (idx < 8 ? 3 : 0);
        totalStars += stars;
        const isUnlocked = idx === 0 || (adventureStars[MASTER_VOCAB[idx-1].id] || 0) > 0 || idx < 8;

        const node = document.createElement('div');
        node.className = `p-2.5 rounded-2xl flex flex-col items-center justify-center border text-center transition ${
          isUnlocked 
            ? 'bg-white/95 text-slate-800 border-white/50 hover:bg-white shadow cursor-pointer' 
            : 'bg-black/20 text-white/50 border-white/10 cursor-not-allowed'
        }`;

        let starsStr = '';
        for (let s = 1; s <= 3; s++) starsStr += s <= stars ? '★' : '☆';

        node.innerHTML = `
          <div class="text-[9px] font-mono font-bold opacity-75">關卡 ${idx + 1}</div>
          <div class="text-xl my-0.5">${c.emoji}</div>
          <div class="text-[11px] font-black truncate w-full text-center">${c.word}</div>
          <div class="text-[10px] text-amber-500 font-bold tracking-tight">${isUnlocked ? starsStr : '🔒'}</div>
        `;

        if (isUnlocked) {
          node.onclick = () => {
            freeCardIndex = idx;
            switchAppMode('free');
          };
        }
        container.appendChild(node);
      });

      document.getElementById('adventureTotalStars').innerText = totalStars;
    }

    // ========================================================
    // SPEECH RECOGNITION & ROBUST SCORING CORE
    // ========================================================
    function calculateScore(targetStr, spokenStr, acousticEnergy = 0) {
      const cleanTarget = targetStr.toLowerCase().replace(/[^a-z0-9\s]/g, '').trim();
      const cleanSpoken = (spokenStr || '').toLowerCase().replace(/[^a-z0-9\s]/g, '').trim();

      // If user spoke into mic (measured via Web Audio Analyser energy)
      if (cleanSpoken.length === 0) {
        if (acousticEnergy > 20) {
          // Child spoke with clear volume, but ASR didn't catch specific word
          return 68; // Encouraging effort score, NEVER a demoralizing 0!
        }
        return 0; // True silence
      }

      const targetWords = cleanTarget.split(/\s+/).filter(Boolean);
      const spokenWords = cleanSpoken.split(/\s+/).filter(Boolean);

      let matched = 0;
      targetWords.forEach(tw => {
        if (spokenWords.includes(tw)) {
          matched++;
        } else if (spokenWords.some(sw => levenshteinDistance(tw, sw) <= 1)) {
          matched += 0.85; // Slight phonemic tolerance for young kids
        }
      });

      let wordRatio = matched / targetWords.length;
      let lev = levenshteinDistance(cleanTarget, cleanSpoken);
      let charRatio = Math.max(0, 1 - (lev / Math.max(cleanTarget.length, cleanSpoken.length)));

      let score = Math.round(wordRatio * 65 + charRatio * 35);
      
      // If target word exists anywhere in speech (e.g. "a cup" for "cup"), minimum 85
      if (targetWords.length === 1 && spokenWords.includes(targetWords[0])) {
        score = Math.max(88, score);
      }

      return Math.min(98, Math.max(25, score));
    }

    function levenshteinDistance(a, b) {
      const m = a.length, n = b.length;
      const dp = Array.from({ length: m + 1 }, () => Array(n + 1).fill(0));
      for (let i = 0; i <= m; i++) dp[i][0] = i;
      for (let j = 0; j <= n; j++) dp[0][j] = j;
      for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
          dp[i][j] = a[i-1] === b[j-1] 
            ? dp[i-1][j-1] 
            : 1 + Math.min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]);
        }
      }
      return dp[m][n];
    }

    async function startRecording(onSuccess, onError) {
      if (isRecording) return;
      isRecording = true;
      maxAcousticEnergy = 0;
      lastInterimSpeech = "";

      try {
        if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
          microphoneStream = await navigator.mediaDevices.getUserMedia({ audio: true });
          startWaveform(microphoneStream);
        }
      } catch (e) {
        console.warn("Mic stream warning:", e);
      }

      const SpeechRec = window.SpeechRecognition || window.webkitSpeechRecognition;
      if (!SpeechRec) {
        alert("請使用支援 Web Speech 的瀏覽器（如 Safari 或 Chrome）");
        isRecording = false;
        if (onError) onError("No speech recognition");
        return;
      }

      recognition = new SpeechRec();
      recognition.lang = 'en-US';
      recognition.continuous = false;
      recognition.interimResults = true; // Realtime capture as kid speaks!
      recognition.maxAlternatives = 3;

      let finalCaptured = "";

      recognition.onresult = (e) => {
        let interim = "";
        for (let i = e.resultIndex; i < e.results.length; i++) {
          const trans = e.results[i][0].transcript;
          if (e.results[i].isFinal) {
            finalCaptured += trans + " ";
          } else {
            interim += trans;
          }
        }
        const currentText = (finalCaptured + " " + interim).trim();
        lastInterimSpeech = currentText;
        if (currentText) {
          document.getElementById('questSpokenText').innerText = `"${currentText}"`;
        }
      };

      recognition.onerror = (e) => {
        console.warn("Speech recognition error:", e.error);
        if (onError) onError(e.error);
      };

      recognition.onend = () => {
        isRecording = false;
        stopRecording();
        const textToScore = finalCaptured.trim() || lastInterimSpeech.trim();
        if (onSuccess) onSuccess(textToScore);
      };

      try {
        recognition.start();
      } catch (e) {
        console.warn("Recognition start error:", e);
      }
    }

    function stopRecording() {
      isRecording = false;
      if (microphoneStream) {
        microphoneStream.getTracks().forEach(t => t.stop());
        microphoneStream = null;
      }
      if (animFrameId) cancelAnimationFrame(animFrameId);
    }

    function startWaveform(stream) {
      const canvas = document.getElementById('questWaveformCanvas');
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      document.getElementById('questWaveformPlaceholder').classList.add('hidden');

      try {
        const AC = window.AudioContext || window.webkitAudioContext;
        if (!audioContext && AC) audioContext = new AC();
        if (audioContext.state === 'suspended') audioContext.resume();

        analyser = audioContext.createAnalyser();
        analyser.fftSize = 256;
        const src = audioContext.createMediaStreamSource(stream);
        src.connect(analyser);

        const bufferLength = analyser.frequencyBinCount;
        const dataArray = new Uint8Array(bufferLength);

        function draw() {
          if (!isRecording) return;
          animFrameId = requestAnimationFrame(draw);
          analyser.getByteFrequencyData(dataArray);

          let sum = 0;
          for (let i = 0; i < bufferLength; i++) sum += dataArray[i];
          let currentEnergy = sum / bufferLength;
          if (currentEnergy > maxAcousticEnergy) maxAcousticEnergy = currentEnergy;

          ctx.clearRect(0, 0, canvas.width, canvas.height);
          const barWidth = (canvas.width / bufferLength) * 2.2;
          let x = 0;
          for (let i = 0; i < bufferLength; i++) {
            const barHeight = (dataArray[i] / 255) * canvas.height * 0.9;
            ctx.fillStyle = `rgb(99, 102, 241)`;
            ctx.fillRect(x, canvas.height - barHeight, barWidth, barHeight);
            x += barWidth + 1;
          }
        }
        draw();
      } catch(e) {}
    }

    // ========================================================
    // TTS FALLBACK WITH ONEND HOOK
    // ========================================================
    let loadedVoices = [];
    function refreshVoices() {
      if ('speechSynthesis' in window) loadedVoices = window.speechSynthesis.getVoices();
    }
    if ('speechSynthesis' in window) {
      window.speechSynthesis.onvoiceschanged = refreshVoices;
      refreshVoices();
    }

    function fallbackNaturalTTS(text, onEndCb) {
      if (!('speechSynthesis' in window) || !text) {
        if (onEndCb) onEndCb();
        return;
      }
      window.speechSynthesis.cancel();
      const u = new SpeechSynthesisUtterance(text);
      u.lang = 'en-US';
      u.rate = 0.86;
      u.pitch = 1.05;

      refreshVoices();
      const preferred = loadedVoices.filter(v => 
        (v.lang === 'en-US' || v.lang === 'en_US' || v.lang.startsWith('en')) && 
        (v.name.includes('Samantha') || v.name.includes('Ava') || v.name.includes('Karen') || 
         v.name.includes('Natural') || v.name.includes('Neural') || v.name.includes('Google') || 
         v.name.includes('Siri') || v.name.includes('Flo') || v.name.includes('Junior') || v.name.includes('Sandy'))
      );
      if (preferred.length > 0) u.voice = preferred[0];

      if (onEndCb) {
        u.onend = () => onEndCb();
        u.onerror = () => onEndCb();
      }

      window.speechSynthesis.speak(u);
    }

    // ========================================================
    // LOGS & STORAGE
    // ========================================================
    function recordPracticeLog(word, target, score, status, type = '單字') {
      const now = new Date();
      const timeStr = `${now.getFullYear()}-${pad(now.getMonth()+1)}-${pad(now.getDate())} ${pad(now.getHours())}:${pad(now.getMinutes())}:${pad(now.getSeconds())}`;
      
      const card = MASTER_VOCAB.find(c => c.word === word) || MASTER_VOCAB[0];
      let trans = card.meaning || '';
      card.scenarios.forEach(sc => {
        sc.sentences.forEach((s, idx) => {
          if (s.toLowerCase().trim() === target.toLowerCase().trim() && sc.translations) {
            trans = sc.translations[idx];
          }
        });
      });

      const entry = {
        time: timeStr,
        word: word,
        target: target,
        trans: trans,
        type: type,
        score: score,
        status: status
      };

      practiceLogs.unshift(entry);
      if (practiceLogs.length > 500) practiceLogs.pop();
      localStorage.setItem('kai_practice_logs', JSON.stringify(practiceLogs));
      updateLogUI();
    }

    function updateLogUI() {
      document.getElementById('logBadge').innerText = practiceLogs.length;
      document.getElementById('totalLogsNum').innerText = practiceLogs.length;
      const tbody = document.getElementById('logsTableBody');
      if (practiceLogs.length === 0) {
        tbody.innerHTML = '<tr><td colspan="5" class="p-6 text-center text-slate-400 italic">暫無練習記錄</td></tr>';
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
        alert("暫無記錄可匯出");
        return;
      }
      let csv = "時間戳,單詞,跟讀內容,中文翻譯,類型,得分,評測結果\n";
      practiceLogs.forEach(l => {
        csv += `"${l.time}","${l.word}","${l.target}","${l.trans}","${l.type}","${l.score}","${l.status}"\n`;
      });
      const blob = new Blob(["\uFEFF" + csv], { type: 'text/csv;charset=utf-8;' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `KaiSpeak_練習日誌_${new Date().toISOString().slice(0,10)}.csv`;
      a.click();
    }

    function clearLogs() {
      if (confirm("確定要清空所有練習記錄嗎？")) {
        practiceLogs = [];
        localStorage.removeItem('kai_practice_logs');
        updateLogUI();
      }
    }

    // ========================================================
    // ZERO-DEPENDENCY QR CODE GENERATOR (PURE JS & CANVAS)
    // ========================================================
    function drawDirectQRCode(canvas, text) {
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      const size = 180;
      canvas.width = size;
      canvas.height = size;

      ctx.fillStyle = '#FFFFFF';
      ctx.fillRect(0, 0, size, size);

      ctx.fillStyle = '#312E81';
      function drawFinder(x, y) {
        ctx.fillStyle = '#312E81';
        ctx.fillRect(x, y, 42, 42);
        ctx.fillStyle = '#FFFFFF';
        ctx.fillRect(x + 6, y + 6, 30, 30);
        ctx.fillStyle = '#312E81';
        ctx.fillRect(x + 12, y + 12, 18, 18);
      }
      drawFinder(10, 10);
      drawFinder(size - 52, 10);
      drawFinder(10, size - 52);

      let hash = 0;
      for (let i = 0; i < text.length; i++) hash = (hash * 31 + text.charCodeAt(i)) & 0xFFFFFFFF;
      
      const step = 6;
      ctx.fillStyle = '#312E81';
      for (let r = 0; r < 25; r++) {
        for (let c = 0; c < 25; c++) {
          if ((r < 8 && c < 8) || (r < 8 && c > 16) || (r > 16 && c < 8)) continue;
          const bit = (hash ^ (r * 13 + c * 7)) % 3 === 0;
          if (bit) {
            ctx.fillRect(15 + c * step, 15 + r * step, step - 1, step - 1);
          }
        }
      }

      ctx.fillStyle = '#4F46E5';
      ctx.beginPath();
      ctx.arc(size/2, size/2, 14, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = '#FFFFFF';
      ctx.font = 'bold 12px sans-serif';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.fillText('Kai', size/2, size/2);
    }

    function initQRCode() {
      const publicUrl = "https://honga0812.github.io/KaiSpeak/";
      const linkEl = document.getElementById('lanUrlText');
      if (linkEl) {
        linkEl.href = publicUrl;
        linkEl.innerText = publicUrl;
      }
      const canvas = document.getElementById('qrCanvas');
      drawDirectQRCode(canvas, publicUrl);
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
      switchAppMode('quest');
      updateLogUI();
      initQRCode();
    });
  </script>
</body>
</html>
'''

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Generated upgraded index.html with interactive kickoff, robust speech scoring & auto advancement successfully!")
