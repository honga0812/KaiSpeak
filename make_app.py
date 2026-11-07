import json

with open("vocab.json", "r", encoding="utf-8") as f:
    vocab_str = f.read()

template = """<!DOCTYPE html>
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
      0% { transform: scale(0.95); opacity: 0.8; }
      50% { transform: scale(1.15); opacity: 0.3; }
      100% { transform: scale(0.95); opacity: 0.8; }
    }
    .sand-stream-anim {
      animation: sandStream 0.6s linear infinite;
    }
    @keyframes sandStream {
      0% { stroke-dashoffset: 0; }
      100% { stroke-dashoffset: 6; }
    }
    .hide-scrollbar::-webkit-scrollbar {
      display: none;
    }
    .hide-scrollbar {
      -ms-overflow-style: none;
      scrollbar-width: none;
    }
  </style>
</head>
<body class="min-h-screen text-slate-800 flex flex-col items-center p-3 md:p-6 pb-20">

  <!-- ======================================================== -->
  <!-- TOP GLOBAL HEADER: BRAND, STREAK & MODE NAVIGATION       -->
  <!-- ======================================================== -->
  <header class="w-full max-w-5xl flex flex-col md:flex-row items-center justify-between gap-4 py-3 px-4 bg-white/90 backdrop-blur-md rounded-3xl shadow-sm border border-indigo-100/60 mb-4 sticky top-2 z-40">
    <div class="flex items-center justify-between w-full md:w-auto">
      <div class="flex items-center gap-2.5 cursor-pointer" onclick="switchAppMode('quest')">
        <div class="w-10 h-10 rounded-2xl bg-gradient-to-tr from-indigo-500 to-purple-600 flex items-center justify-center text-white text-xl shadow-md shadow-indigo-200">
          🗣️
        </div>
        <div>
          <h1 class="text-xl font-bold tracking-tight text-indigo-950 flex items-center gap-1.5">
            KaiSpeak <span class="text-xs bg-indigo-100 text-indigo-700 px-2 py-0.5 rounded-full font-semibold">少兒美語</span>
          </h1>
          <p class="text-[11px] text-slate-600">互動式主動引導 · 隨機例句 · 沙漏倒數</p>
        </div>
      </div>

      <!-- Mobile QR Code Trigger -->
      <button onclick="toggleQRModal()" class="md:hidden p-2 rounded-xl bg-slate-100 text-slate-700 hover:bg-slate-200 text-xs font-bold flex items-center gap-1 shadow-sm">
        📱 掃碼手機體驗
      </button>
    </div>

    <!-- Mode Navigation Tabs -->
    <nav class="flex items-center bg-slate-100/90 p-1.5 rounded-2xl border border-slate-200/60 text-xs font-bold">
      <button id="navQuestBtn" onclick="switchAppMode('quest')" class="px-4 py-2 rounded-xl bg-indigo-600 text-white shadow-sm transition flex items-center gap-1.5">
        <span>🎯 每日任務</span>
        <span class="text-[10px] bg-amber-400 text-amber-950 px-1.5 py-0.2 rounded-full font-extrabold">10詞速通</span>
      </button>
      <button id="navFreeBtn" onclick="switchAppMode('free')" class="px-4 py-2 rounded-xl text-slate-600 hover:text-slate-900 transition flex items-center gap-1.5">
        <span>📚 自由練習</span>
        <span class="text-[10px] bg-slate-200 text-slate-600 px-1.5 py-0.2 rounded-full font-bold">50詞庫</span>
      </button>
      <button id="navAdventureBtn" onclick="switchAppMode('adventure')" class="px-4 py-2 rounded-xl text-slate-600 hover:text-slate-900 transition flex items-center gap-1.5">
        <span>🗺️ 探險島</span>
        <span class="text-[10px] bg-indigo-100 text-indigo-700 px-1.5 py-0.2 rounded-full font-bold">50關</span>
      </button>
    </nav>

    <!-- Right Controls: QR Modal & Log -->
    <div class="hidden md:flex items-center gap-2">
      <button onclick="toggleQRModal()" class="px-3.5 py-2 rounded-2xl bg-indigo-50 hover:bg-indigo-100 text-indigo-700 text-xs font-bold transition flex items-center gap-1.5 border border-indigo-200">
        <span>📱 掃碼手機體驗</span>
      </button>
      <button onclick="toggleLogModal()" class="px-3 py-2 rounded-2xl bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-bold transition flex items-center gap-1">
        <span>📊 練習日誌</span>
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
      
      <div class="inline-flex items-center gap-1.5 bg-amber-100 text-amber-900 px-3.5 py-1 rounded-full text-xs font-extrabold mb-3">
        🔥 連續打卡第 <span id="overlayStreakNum">3</span> 天
      </div>

      <h3 class="text-2xl font-black text-slate-900 mb-2">今日任務即將開始！</h3>
      <p class="text-xs text-slate-500 mb-6 leading-relaxed">
        今日精選 <strong class="text-indigo-600">10 個單字</strong> (4新詞 + 4複習 + 2熟悉)<br>
        每個單字隨機朗讀 <strong>2 條生活例句</strong>，輕鬆掌握標準發音！
      </p>

      <!-- 3-Second Visual Countdown Display (Initially Hidden) -->
      <div id="overlayCountdownBox" class="hidden flex-col items-center my-4">
        <div class="text-6xl font-black text-indigo-600 animate-pulse font-mono" id="overlayCountdownNum">
          3
        </div>
        <div class="text-xs font-bold text-indigo-400 mt-2">任務準備中，請戴上耳機或打開喇叭...</div>
      </div>

      <button id="overlayStartBtn" onclick="startDailyQuestWithCountdown()" class="w-full py-4 bg-gradient-to-r from-indigo-600 via-indigo-700 to-purple-600 hover:from-indigo-700 hover:to-purple-700 text-white rounded-2xl text-base font-extrabold shadow-xl shadow-indigo-300 transition transform active:scale-95 flex items-center justify-center gap-2">
        <span>🚀 開始今日挑戰</span>
      </button>

      <div class="mt-4 text-[11px] text-slate-600 flex items-center gap-1">
        <span>💡 點選上方按鈕即可啟動聲音與麥克風功能</span>
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
            <h2 class="text-lg font-bold">今日打卡任務 (10 詞快速挑戰)</h2>
            <span class="text-[10px] bg-amber-400 text-amber-950 font-extrabold px-2.5 py-0.5 rounded-full shadow-sm">
              🔥 連續打卡 <span id="questStreakDays">3</span> 天
            </span>
          </div>
          <p class="text-xs text-indigo-100 mt-1">
            4 個新詞 + 4 個複習 + 2 個熟悉 · 每詞隨機朗讀 2 句生活範例
          </p>
        </div>
      </div>

      <!-- Overall 10 Words Progress -->
      <div class="flex items-center gap-4 bg-white/10 backdrop-blur px-5 py-3 rounded-2xl border border-white/10 w-full md:w-auto justify-between">
        <div class="text-left md:text-right">
          <div class="text-[11px] text-indigo-200">今日詞彙進度</div>
          <div class="text-lg font-extrabold font-mono"><span id="questWordProgress">1</span> / 10 詞</div>
        </div>
        <div class="w-28 bg-white/20 h-3 rounded-full overflow-hidden">
          <div id="questProgressBar" class="bg-amber-400 h-full rounded-full transition-all duration-500" style="width: 10%"></div>
        </div>
      </div>
    </div>

    <!-- Prominent Pause / Resume Floating Control Bar -->
    <div class="w-full flex items-center justify-between bg-white rounded-2xl p-3 px-5 shadow-sm border border-indigo-100">
      <div class="flex items-center gap-2">
        <span class="text-xs text-slate-500 font-bold">進程狀態:</span>
        <span id="questStatusPill" class="text-xs px-2.5 py-0.5 rounded-full bg-emerald-100 text-emerald-800 font-black flex items-center gap-1">
          <span class="w-2 h-2 rounded-full bg-emerald-500 animate-ping"></span> 引導進行中
        </span>
      </div>

      <!-- Eye-Catching Tactile Pause / Resume Button -->
      <button id="questMainPauseBtn" onclick="toggleQuestAutoFlow()" class="px-5 py-2.5 rounded-2xl bg-amber-500 hover:bg-amber-600 active:scale-95 text-white text-xs font-black shadow-lg shadow-amber-200 transition flex items-center gap-2">
        <span id="questPauseIcon" class="text-base">⏸️</span>
        <span id="questPauseText">暫停練習 · 休息 / 仔細看內容</span>
      </button>
    </div>

    <!-- Active Pause Friendly Notice (Shown when user hits pause) -->
    <div id="questPauseBanner" class="w-full hidden p-4 bg-amber-50 border-2 border-amber-300 rounded-3xl text-center shadow-md animate-fade-in">
      <div class="text-amber-900 font-black text-sm flex items-center justify-center gap-2">
        <span class="text-xl">☕</span>
        <span>目前已暫停！您可以慢慢閱讀螢幕上的單字、音標與中文翻譯，準備好了隨時點擊「繼續挑戰」！</span>
      </div>
    </div>

    <!-- Active Quest Interactive Studio Card -->
    <div class="bg-white rounded-3xl p-6 md:p-8 shadow-xl shadow-indigo-100/70 border border-indigo-50 flex flex-col items-center relative">
      
      <!-- Top Step Indicators for Current Word: [1.單字發音] -> [2.隨機例句 1] -> [3.隨機例句 2] -->
      <div class="w-full max-w-xl flex items-center justify-between mb-6 px-4">
        <div id="qStepDot0" class="flex flex-col items-center gap-1 flex-1">
          <div class="w-9 h-9 rounded-full bg-indigo-600 text-white font-bold text-xs flex items-center justify-center shadow-md">1</div>
          <span class="text-[11px] font-bold text-indigo-700">單字精讀</span>
        </div>
        <div class="h-0.5 bg-slate-200 flex-1 mx-2"></div>
        <div id="qStepDot1" class="flex flex-col items-center gap-1 flex-1 opacity-50">
          <div class="w-9 h-9 rounded-full bg-slate-200 text-slate-600 font-bold text-xs flex items-center justify-center">2</div>
          <span class="text-[11px] font-semibold text-slate-500">隨機例句 1</span>
        </div>
        <div class="h-0.5 bg-slate-200 flex-1 mx-2"></div>
        <div id="qStepDot2" class="flex flex-col items-center gap-1 flex-1 opacity-50">
          <div class="w-9 h-9 rounded-full bg-slate-200 text-slate-600 font-bold text-xs flex items-center justify-center">3</div>
          <span class="text-[11px] font-semibold text-slate-500">隨機例句 2</span>
        </div>
      </div>

      <!-- Proactive State Banner -->
      <div id="questStateBanner" class="w-full max-w-xl p-3.5 rounded-2xl bg-indigo-50 border border-indigo-100 text-center font-bold text-indigo-800 text-sm mb-4 flex items-center justify-center gap-2 shadow-inner transition-all duration-300">
        <span id="questStateIcon" class="text-xl">🔊</span>
        <span id="questStateText">點選上方「開始挑戰」或播放範讀</span>
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
          <span id="questScenarioBadge" class="text-[10px] font-extrabold uppercase px-1.5 py-0.5 rounded bg-indigo-100 text-indigo-700">中文對照</span>
          <span id="questTargetChinese" class="text-sm md:text-base font-bold text-slate-700">名詞：書桌，辦公桌</span>
        </div>

        <!-- Real-time Speech Recognition Feedback Bubble -->
        <div id="questSpokenFeedbackBox" class="mt-2 text-xs font-bold text-indigo-700 bg-indigo-50/90 px-3.5 py-1.5 rounded-full inline-block border border-indigo-200/60 transition">
          🎤 聽到你說：<span id="questSpokenText" class="text-indigo-950 underline italic font-black">等待錄音...</span>
        </div>
      </div>

      <!-- Dynamic Visual Sand-Flow Hourglass Countdown Area -->
      <div id="questHourglassBox" class="flex flex-col items-center gap-2 my-2 hidden">
        <!-- SVG Hourglass with Animated Flowing Sand -->
        <div class="relative flex items-center justify-center">
          <svg viewBox="0 0 64 80" class="w-16 h-20 filter drop-shadow-md">
            <!-- Glass Body Contour -->
            <path d="M 10 8 L 54 8 L 54 14 Q 54 36 34 40 Q 54 44 54 66 L 54 72 L 10 72 L 10 66 Q 10 44 30 40 Q 10 36 10 14 Z" fill="none" stroke="#4F46E5" stroke-width="3.5" stroke-linejoin="round" />
            
            <!-- Top Sand Bulb (Decreasing from top) -->
            <clipPath id="topBulbClip">
              <path d="M 12 12 L 52 12 Q 52 34 32 39 Q 12 34 12 12 Z" />
            </clipPath>
            <rect id="topSandRect" x="10" y="12" width="44" height="26" fill="#F59E0B" clip-path="url(#topBulbClip)" class="transition-all duration-1000 ease-linear"/>
            
            <!-- Trickling Sand Stream -->
            <line id="sandStream" x1="32" y1="38" x2="32" y2="66" stroke="#F59E0B" stroke-width="2.5" stroke-dasharray="3,2" class="sand-stream-anim" />
            
            <!-- Bottom Sand Bulb (Rising from bottom) -->
            <clipPath id="bottomBulbClip">
              <path d="M 12 68 L 52 68 Q 52 46 32 41 Q 12 46 12 68 Z" />
            </clipPath>
            <rect id="bottomSandRect" x="10" y="68" width="44" height="0" fill="#F59E0B" clip-path="url(#bottomBulbClip)" class="transition-all duration-1000 ease-linear"/>
          </svg>
        </div>

        <!-- Prominent Badge with Giant Countdown Number -->
        <div class="flex items-center gap-2 bg-gradient-to-r from-amber-500 to-orange-500 text-white font-black px-5 py-2 rounded-full shadow-lg shadow-orange-200 text-sm animate-bounce">
          <span>⏳ 朗讀倒數:</span>
          <span id="questCountdownNum" class="text-2xl font-black font-mono">5</span>
          <span>秒</span>
        </div>
        <div class="text-[11px] font-bold text-amber-800 bg-amber-50 px-3 py-0.5 rounded-full border border-amber-200">
          說完系統會自動辨識評分，並播放專屬音效！
        </div>
      </div>

      <!-- Audio Waveform Live Display during Recording -->
      <div class="w-full max-w-xl h-10 bg-slate-100 rounded-2xl overflow-hidden border border-slate-200/80 mb-4 flex items-center justify-center relative">
        <canvas id="questWaveformCanvas" class="w-full h-full"></canvas>
        <span id="questWaveformPlaceholder" class="absolute text-xs text-slate-600 font-medium">聲波感應區 · 錄音時隨聲音即時波動</span>
      </div>

      <!-- Central Action Area: Big Pulsing Mic -->
      <div class="flex flex-col items-center gap-2 mb-4">
        <div class="relative flex items-center justify-center">
          <div id="questMicRing" class="absolute w-24 h-24 rounded-full bg-rose-400/40 hidden pulse-ring"></div>
          <button id="questMicBtn" onclick="toggleQuestManualRecord()" class="relative z-10 w-20 h-20 rounded-full bg-gradient-to-tr from-indigo-600 to-violet-600 text-white shadow-xl shadow-indigo-300 flex flex-col items-center justify-center transition transform active:scale-95 focus:outline-none">
            <span id="questMicIcon" class="text-2xl">🎙️</span>
            <span id="questMicLabel" class="text-[11px] font-bold mt-0.5">點我錄音</span>
          </button>
        </div>
      </div>

      <!-- Quick Interactive Flow Controls (Replay, Retry, Skip) -->
      <div class="flex items-center gap-2 flex-wrap justify-center mb-2">
        <button onclick="replayQuestDemoAudio()" class="px-3.5 py-2 rounded-xl bg-white border border-slate-200 text-slate-700 text-xs font-bold hover:bg-slate-50 transition flex items-center gap-1 shadow-sm">
          <span>🔊 再聽範讀</span>
        </button>
        <button onclick="retryQuestCurrentStep()" class="px-3.5 py-2 rounded-xl bg-white border border-slate-200 text-slate-700 text-xs font-bold hover:bg-slate-50 transition flex items-center gap-1 shadow-sm">
          <span>🔄 重讀此題</span>
        </button>
        <button onclick="skipQuestStep()" class="px-3.5 py-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-bold transition flex items-center gap-1 shadow-sm">
          <span>⏭️ 跳過此題</span>
        </button>
      </div>

      <!-- Simulation Evaluation Buttons for Quick Testing Sound Effects -->
      <div class="mt-4 pt-3 border-t border-slate-100 w-full max-w-xl flex flex-col sm:flex-row items-center justify-between text-xs text-slate-500 gap-2">
        <span class="font-bold flex items-center gap-1">🎵 音效試聽測試:</span>
        <div class="flex gap-1.5 flex-wrap">
          <button onclick="simulateQuestEval(95)" class="px-2.5 py-1 bg-emerald-50 text-emerald-700 rounded-lg border border-emerald-200 font-bold hover:bg-emerald-100">95分(最高清脆音)</button>
          <button onclick="simulateQuestEval(85)" class="px-2.5 py-1 bg-blue-50 text-blue-700 rounded-lg border border-blue-200 font-bold hover:bg-blue-100">85分(中高音)</button>
          <button onclick="simulateQuestEval(75)" class="px-2.5 py-1 bg-amber-50 text-amber-700 rounded-lg border border-amber-200 font-bold hover:bg-amber-100">75分(溫和音)</button>
          <button onclick="simulateQuestEval(60)" class="px-2.5 py-1 bg-rose-50 text-rose-700 rounded-lg border border-rose-200 font-bold hover:bg-rose-100">60分(加油滑音)</button>
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
        <button onclick="setFreeCategory('animal')" class="free-cat-btn px-3 py-1.5 rounded-xl font-semibold bg-slate-100 text-slate-600 hover:bg-slate-200 whitespace-nowrap" data-cat="animal">🐶 動物 (10)</button>
        <button onclick="setFreeCategory('nature')" class="free-cat-btn px-3 py-1.5 rounded-xl font-semibold bg-slate-100 text-slate-600 hover:bg-slate-200 whitespace-nowrap" data-cat="nature">🌿 自然 (10)</button>
        <button onclick="setFreeCategory('play')" class="free-cat-btn px-3 py-1.5 rounded-xl font-semibold bg-slate-100 text-slate-600 hover:bg-slate-200 whitespace-nowrap" data-cat="play">⚽ 玩樂 (8)</button>
      </div>
    </div>

    <!-- Free Practice Grid -->
    <div id="freeGridContainer" class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-5 gap-3 max-h-72 overflow-y-auto p-1 hide-scrollbar">
      <!-- Word cards injected by JS -->
    </div>

    <!-- Free Practice Focused Inspector Card -->
    <div class="bg-white rounded-3xl p-6 shadow-xl border border-indigo-50 flex flex-col md:flex-row gap-6 items-center">
      <div class="w-full md:w-1/3 flex flex-col items-center text-center p-4 bg-slate-50 rounded-2xl border border-slate-100">
        <div id="freeEmoji" class="text-7xl mb-2">🪑</div>
        <h3 id="freeWord" class="text-3xl font-black text-indigo-950">desk</h3>
        <div id="freePhonetic" class="text-xs text-slate-400 font-mono mt-1 mb-2">/dɛsk/</div>
        <div id="freeMeaning" class="text-xs font-bold text-slate-700 bg-white px-3 py-1 rounded-full border border-indigo-100">名詞：書桌，辦公桌</div>
        <button onclick="playFreeWordAudio()" class="mt-4 px-4 py-2 rounded-xl bg-indigo-600 text-white text-xs font-bold hover:bg-indigo-700 transition flex items-center gap-1 shadow-sm">
          <span>🔊 播放標準原聲</span>
        </button>
      </div>

      <div class="w-full md:w-2/3 flex flex-col gap-3">
        <div class="flex items-center justify-between">
          <span class="text-xs font-bold text-slate-500">9 條情境例句庫 · 中英文對照</span>
          <span id="freeScenarioTitle" class="text-xs font-bold text-indigo-600 bg-indigo-50 px-2 py-0.5 rounded-md">情境一 · 認知描述</span>
        </div>

        <!-- 3 Scenarios Tab -->
        <div class="flex gap-2 text-xs font-bold">
          <button onclick="selectFreeScenario(0)" id="scTab0" class="flex-1 py-1.5 rounded-xl bg-indigo-600 text-white shadow-sm transition">情境 1</button>
          <button onclick="selectFreeScenario(1)" id="scTab1" class="flex-1 py-1.5 rounded-xl bg-slate-100 text-slate-600 hover:bg-slate-200 transition">情境 2</button>
          <button onclick="selectFreeScenario(2)" id="scTab2" class="flex-1 py-1.5 rounded-xl bg-slate-100 text-slate-600 hover:bg-slate-200 transition">情境 3</button>
        </div>

        <!-- 3 Sentences in Current Scenario -->
        <div id="freeSentenceList" class="flex flex-col gap-2">
          <!-- Injected by JS -->
        </div>
      </div>
    </div>
  </section>

  <!-- ======================================================== -->
  <!-- MODE 3: ADVENTURE ISLAND (50 關地圖)                       -->
  <!-- ======================================================== -->
  <section id="viewAdventure" class="w-full max-w-5xl hidden flex-col gap-4">
    <div class="bg-white rounded-3xl p-6 shadow-sm border border-slate-100 flex items-center justify-between">
      <div>
        <h2 class="text-lg font-bold text-slate-800 flex items-center gap-2">
          🗺️ 英語發音探險島 (50 關冒險)
        </h2>
        <p class="text-xs text-slate-500 mt-1">每一關以三星標準挑戰，點選任一已解鎖關卡即可進行精確挑戰！</p>
      </div>
      <div class="flex items-center gap-2 bg-amber-50 px-4 py-2 rounded-2xl border border-amber-200 text-xs font-black text-amber-900">
        <span>⭐ 收集星星:</span>
        <span id="advTotalStars" class="text-base text-amber-600">0</span> / 150
      </div>
    </div>

    <!-- Adventure Stage Grid -->
    <div id="advStageGrid" class="grid grid-cols-2 sm:grid-cols-5 md:grid-cols-10 gap-3">
      <!-- Injected by JS -->
    </div>
  </section>

  <!-- ======================================================== -->
  <!-- QR CODE MODAL FOR MOBILE / TABLET LIVE TESTING           -->
  <!-- ======================================================== -->
  <div id="qrModal" class="fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-50 flex items-center justify-center p-4 hidden">
    <div class="bg-white rounded-3xl p-6 max-w-sm w-full shadow-2xl border border-indigo-100 text-center flex flex-col items-center">
      <div class="w-12 h-12 rounded-2xl bg-indigo-50 text-indigo-600 flex items-center justify-center text-2xl mb-3">
        📱
      </div>
      <h3 class="text-lg font-bold text-slate-900 mb-1">手機 / 平板掃碼體驗</h3>
      <p class="text-xs text-slate-500 mb-4">使用相機掃描下方 QR Code，立即在手機上測試語音與沙漏倒數！</p>
      
      <!-- Real Canvas QR Code -->
      <div class="p-3 bg-white border-2 border-indigo-100 rounded-2xl shadow-inner mb-3">
        <canvas id="qrCodeCanvas" class="w-44 h-44"></canvas>
      </div>

      <div class="text-[11px] font-mono text-slate-500 bg-slate-50 px-3 py-1.5 rounded-xl border border-slate-200 mb-4 break-all">
        https://honga0812.github.io/KaiSpeak/?v=4
      </div>

      <button onclick="toggleQRModal()" class="w-full py-2.5 bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold text-xs rounded-xl transition">
        關閉視窗
      </button>
    </div>
  </div>

  <!-- ======================================================== -->
  <!-- PRACTICE LOG MODAL                                       -->
  <!-- ======================================================== -->
  <div id="logModal" class="fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-50 flex items-center justify-center p-4 hidden">
    <div class="bg-white rounded-3xl p-6 max-w-2xl w-full shadow-2xl border border-indigo-100 flex flex-col max-h-[85vh]">
      <div class="flex items-center justify-between pb-3 border-b border-slate-100 mb-3">
        <div class="flex items-center gap-2">
          <span class="text-xl">📊</span>
          <h3 class="text-base font-bold text-slate-900">發音評測紀錄與錯詞本統計</h3>
        </div>
        <button onclick="toggleLogModal()" class="text-slate-400 hover:text-slate-600 font-bold text-lg">✕</button>
      </div>

      <div id="logTableContainer" class="flex-1 overflow-y-auto hide-scrollbar text-xs">
        <!-- Injected by JS -->
      </div>

      <div class="pt-3 border-t border-slate-100 flex items-center justify-between mt-3">
        <button onclick="exportLogsCSV()" class="px-4 py-2 bg-indigo-50 text-indigo-700 hover:bg-indigo-100 text-xs font-bold rounded-xl border border-indigo-200 transition">
          📥 匯出 CSV 學習記錄
        </button>
        <button onclick="clearAllLogs()" class="px-4 py-2 bg-rose-50 text-rose-700 hover:bg-rose-100 text-xs font-bold rounded-xl border border-rose-200 transition">
          🗑️ 清空所有記錄
        </button>
      </div>
    </div>
  </div>

  <!-- QR Code Generator Library -->
  <script src="https://cdn.jsdelivr.net/npm/qrcode@1.5.3/build/qrcode.min.js"></script>

  <!-- ======================================================== -->
  <!-- JAVASCRIPT APPLICATION CORE LOGIC                        -->
  <!-- ======================================================== -->
  <script>
    const MASTER_VOCAB = __VOCAB_PLACEHOLDER__;

    // Application State
    let appMode = 'quest'; // 'quest' | 'free' | 'adventure'
    
    // --- Quest Mode State (10 Words: 4 New + 4 Review + 2 Consolidate, 2 Random Sentences Each) ---
    let questQueue = []; // 10 items
    let questWordIdx = 0; // 0 to 9
    let questSubStep = 0; // 0: Word, 1: Random Sent 1, 2: Random Sent 2
    let questAutoPlay = false; // Is active flow running?
    let questAudioPlayer = new Audio();
    let questRecTimer = null;
    let questCountdownVal = 5;
    let questMaxCountdown = 5;
    let overlayTimer = null;

    // --- Free Mode State ---
    let freeCardIndex = 0;
    let freeScenarioIndex = 0;
    let freeCategory = 'all';
    let freeAudioPlayer = new Audio();

    // --- Audio & Recording States ---
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

    // ========================================================
    // SOUND EFFECTS MODULE (Web Audio API Synthesizer)
    // Pitch-graded feedback based on score:
    // >= 90: High crisp crystal arpeggio (C6->E6->G6->C7)
    // 80~89: Bright chime (G5->C6)
    // 70~79: Warm gentle chime (E5->G5)
    // < 80 : Sympathetic downward sliding "sorry/try again" note
    // ========================================================
    const SoundEffects = {
      ctx: null,
      init() {
        const AC = window.AudioContext || window.webkitAudioContext;
        if (!this.ctx && AC) {
          this.ctx = new AC();
        }
        if (this.ctx && this.ctx.state === 'suspended') {
          this.ctx.resume();
        }
      },
      playScore(score) {
        this.init();
        if (!this.ctx) return;
        const now = this.ctx.currentTime;
        
        if (score >= 90) {
          // 90分以上：最清脆晶瑩的大和弦水晶音 (High crisp crystalline arpeggio)
          const freqs = [1046.5, 1318.5, 1567.98, 2093.0];
          freqs.forEach((f, i) => {
            const osc = this.ctx.createOscillator();
            const gain = this.ctx.createGain();
            osc.type = 'sine';
            osc.frequency.setValueAtTime(f, now + i * 0.07);
            gain.gain.setValueAtTime(0, now + i * 0.07);
            gain.gain.linearRampToValueAtTime(0.24, now + i * 0.07 + 0.02);
            gain.gain.exponentialRampToValueAtTime(0.001, now + i * 0.07 + 0.35);
            osc.connect(gain);
            gain.connect(this.ctx.destination);
            osc.start(now + i * 0.07);
            osc.stop(now + i * 0.07 + 0.36);
          });
        } else if (score >= 80) {
          // 80 ~ 89分：清脆愉悅的中高音雙音 (Bright chime: G5 -> C6)
          const freqs = [783.99, 1046.5];
          freqs.forEach((f, i) => {
            const osc = this.ctx.createOscillator();
            const gain = this.ctx.createGain();
            osc.type = 'triangle';
            osc.frequency.setValueAtTime(f, now + i * 0.09);
            gain.gain.setValueAtTime(0, now + i * 0.09);
            gain.gain.linearRampToValueAtTime(0.22, now + i * 0.09 + 0.02);
            gain.gain.exponentialRampToValueAtTime(0.001, now + i * 0.09 + 0.3);
            osc.connect(gain);
            gain.connect(this.ctx.destination);
            osc.start(now + i * 0.09);
            osc.stop(now + i * 0.09 + 0.32);
          });
        } else if (score >= 70) {
          // 70 ~ 79分：音調較低一點的溫和雙音 (Warm gentle encouragement: E5 -> G5)
          const freqs = [659.25, 783.99];
          freqs.forEach((f, i) => {
            const osc = this.ctx.createOscillator();
            const gain = this.ctx.createGain();
            osc.type = 'sine';
            osc.frequency.setValueAtTime(f, now + i * 0.11);
            gain.gain.setValueAtTime(0, now + i * 0.11);
            gain.gain.linearRampToValueAtTime(0.2, now + i * 0.11 + 0.02);
            gain.gain.exponentialRampToValueAtTime(0.001, now + i * 0.11 + 0.28);
            osc.connect(gain);
            gain.connect(this.ctx.destination);
            osc.start(now + i * 0.11);
            osc.stop(now + i * 0.11 + 0.3);
          });
        } else {
          // 80分以下弱項：帶有 sorry 感覺的溫柔下行滑音 (Gentle sorry/try again sliding boing)
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = 'sine';
          osc.frequency.setValueAtTime(370, now);
          osc.frequency.exponentialRampToValueAtTime(260, now + 0.35);
          gain.gain.setValueAtTime(0.18, now);
          gain.gain.exponentialRampToValueAtTime(0.001, now + 0.4);
          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start(now);
          osc.stop(now + 0.42);
        }
      },
      playNext() {
        // 切換下一個字時的清脆叮咚聲 (Light pop/ding)
        this.init();
        if (!this.ctx) return;
        const now = this.ctx.currentTime;
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(880, now);
        osc.frequency.exponentialRampToValueAtTime(1320, now + 0.08);
        gain.gain.setValueAtTime(0.15, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.15);
        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.start(now);
        osc.stop(now + 0.16);
      }
    };

    // --- Dynamic Queue Setup (Exactly 10 Words: 4 New, 4 Review, 2 Consolidate) ---
    function initQuestQueue() {
      const news = MASTER_VOCAB.filter(v => v.role === 'new');
      const reviews = MASTER_VOCAB.filter(v => v.role === 'review');
      const consolidates = MASTER_VOCAB.filter(v => v.role === 'consolidate');

      const selected = [
        ...news.slice(0, 4),
        ...reviews.slice(0, 4),
        ...consolidates.slice(0, 2)
      ];

      let idx = 0;
      while (selected.length < 10 && idx < MASTER_VOCAB.length) {
        if (!selected.includes(MASTER_VOCAB[idx])) selected.push(MASTER_VOCAB[idx]);
        idx++;
      }

      // For each word in questQueue, randomly pick 2 sentences from its 9 scenario sentences
      questQueue = selected.map(wordObj => {
        const allSentences = [];
        if (wordObj.scenarios && wordObj.scenarios.length > 0) {
          wordObj.scenarios.forEach((sc, scIdx) => {
            if (sc.sentences) {
              sc.sentences.forEach((sent, sentIdx) => {
                allSentences.push({
                  text: sent,
                  translation: (sc.translations && sc.translations[sentIdx]) ? sc.translations[sentIdx] : "",
                  scenarioTitle: sc.title || `情境 ${scIdx + 1}`,
                  audioSrc: `audio/sentence_${wordObj.id}_${scIdx}_${sentIdx}.m4a`
                });
              });
            }
          });
        }
        // Shuffle sentences and pick 2
        const shuffled = [...allSentences].sort(() => 0.5 - Math.random());
        const picked = shuffled.slice(0, 2);
        return {
          ...wordObj,
          _dailySentences: picked
        };
      });
    }

    // ========================================================
    // KICKOFF & WELCOME GUIDANCE (第幾天提示 + 3秒倒數 + 聲音解鎖)
    // ========================================================
    function startDailyQuestWithCountdown() {
      // Pre-warm Audio Context
      SoundEffects.init();
      try {
        questAudioPlayer.src = "data:audio/wav;base64,UklGRigAAABXQVZFZm10IBIAAAABAAEARKwAAIhYAQACABAAAABkYXRhAgAAAAEA";
        questAudioPlayer.play().then(() => questAudioPlayer.pause()).catch(()=>{});
      } catch(e) {}

      // Show 3-2-1 Countdown
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
          // Hide overlay and kick off proactive quest walkthrough
          document.getElementById('questKickoffOverlay').classList.add('hidden');
          questAutoPlay = true;
          updatePauseUI();
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
      
      // Update Progress (10 Words)
      document.getElementById('questWordProgress').innerText = questWordIdx + 1;
      const pct = Math.round(((questWordIdx) / 10) * 100);
      document.getElementById('questProgressBar').style.width = `${Math.max(10, pct)}%`;
      document.getElementById('questStreakDays').innerText = streakDays;
      document.getElementById('overlayStreakNum').innerText = streakDays;

      // Update Step Indicators: 0:單字發音, 1:隨機例句1, 2:隨機例句2
      [0, 1, 2].forEach(step => {
        const dot = document.getElementById(`qStepDot${step}`);
        if (!dot) return;
        const circle = dot.querySelector('div');
        const text = dot.querySelector('span');
        if (step === questSubStep) {
          dot.classList.remove('opacity-50');
          circle.className = "w-9 h-9 rounded-full bg-indigo-600 text-white font-bold text-xs flex items-center justify-center shadow-md scale-110 transition";
          text.className = "text-[11px] font-bold text-indigo-700";
        } else if (step < questSubStep) {
          dot.classList.remove('opacity-50');
          circle.className = "w-9 h-9 rounded-full bg-emerald-500 text-white font-bold text-xs flex items-center justify-center shadow-sm";
          circle.innerHTML = "✓";
          text.className = "text-[11px] font-semibold text-emerald-700";
        } else {
          dot.classList.add('opacity-50');
          circle.className = "w-9 h-9 rounded-full bg-slate-200 text-slate-600 font-bold text-xs flex items-center justify-center";
          circle.innerHTML = `${step + 1}`;
          text.className = "text-[11px] font-semibold text-slate-500";
        }
      });

      // Target Content
      document.getElementById('questEmoji').innerText = card.emoji;
      const engEl = document.getElementById('questTargetEnglish');
      const chiEl = document.getElementById('questTargetChinese');
      const phoEl = document.getElementById('questPhonetic');
      const badgeEl = document.getElementById('questScenarioBadge');

      if (questSubStep === 0) {
        // Word
        engEl.innerText = card.word;
        chiEl.innerText = card.meaning || "單字釋義";
        phoEl.innerText = card.phonetic || "";
        phoEl.classList.remove('hidden');
        badgeEl.innerText = "單字釋義";
      } else {
        // Random Sentences (index 0 or 1)
        const sentItem = (card._dailySentences && card._dailySentences[questSubStep - 1]) 
          ? card._dailySentences[questSubStep - 1] 
          : (card.scenarios[0] ? { text: card.scenarios[0].sentences[0], translation: card.scenarios[0].translations[0], scenarioTitle: "情境生活" } : { text: "", translation: "", scenarioTitle: "" });
        engEl.innerText = sentItem.text;
        chiEl.innerText = sentItem.translation;
        phoEl.classList.add('hidden');
        badgeEl.innerText = sentItem.scenarioTitle || `精選例句 ${questSubStep}`;
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

    function updatePauseUI() {
      const mainBtn = document.getElementById('questMainPauseBtn');
      const icon = document.getElementById('questPauseIcon');
      const text = document.getElementById('questPauseText');
      const pill = document.getElementById('questStatusPill');
      const banner = document.getElementById('questPauseBanner');

      if (questAutoPlay) {
        // Running
        mainBtn.className = "px-5 py-2.5 rounded-2xl bg-amber-500 hover:bg-amber-600 active:scale-95 text-white text-xs font-black shadow-lg shadow-amber-200 transition flex items-center gap-2";
        icon.innerText = "⏸️";
        text.innerText = "暫停練習 · 休息 / 仔細看內容";
        pill.className = "text-xs px-2.5 py-0.5 rounded-full bg-emerald-100 text-emerald-800 font-black flex items-center gap-1";
        pill.innerHTML = '<span class="w-2 h-2 rounded-full bg-emerald-500 animate-ping"></span> 引導進行中';
        banner.classList.add('hidden');
      } else {
        // Paused
        mainBtn.className = "px-5 py-2.5 rounded-2xl bg-emerald-600 hover:bg-emerald-700 active:scale-95 text-white text-xs font-black shadow-lg shadow-emerald-200 transition flex items-center gap-2 animate-pulse";
        icon.innerText = "▶️";
        text.innerText = "繼續今日任務（點我繼續）";
        pill.className = "text-xs px-2.5 py-0.5 rounded-full bg-amber-100 text-amber-900 font-black flex items-center gap-1";
        pill.innerHTML = '⏸️ 已暫停休息中';
        banner.classList.remove('hidden');
      }
    }

    function toggleQuestAutoFlow() {
      questAutoPlay = !questAutoPlay;
      updatePauseUI();
      if (questAutoPlay) {
        setQuestStatus("引導繼續！即將進入下一個朗讀步驟...", "▶️", "bg-indigo-50 text-indigo-800");
        runQuestAutoStep();
      } else {
        // Stop currently playing audio or recording
        if (questAudioPlayer) questAudioPlayer.pause();
        if (isRecording) stopRecording();
        if (questRecTimer) { clearInterval(questRecTimer); questRecTimer = null; }
        document.getElementById('questHourglassBox').classList.add('hidden');
        setQuestStatus("任務已暫停。您可以慢慢看當前單字，準備好點擊「繼續今日任務」！", "⏸️", "bg-amber-100 text-amber-900 border-amber-300");
      }
    }

    function runQuestAutoStep() {
      if (!questAutoPlay) return;
      renderQuestCard();

      // 1. Play Demo Audio Loud & Clear
      setQuestStatus("正在播放母語示範發音，請仔細聽...", "🔊", "bg-indigo-100 text-indigo-800 animate-pulse border-indigo-200");
      playQuestDemoAudio(() => {
        if (!questAutoPlay) return;
        // 2. Demo Audio Ended -> Trigger Recording with Hourglass
        startQuestAutoRecord();
      });
    }

    function getQuestAudioSrc() {
      const card = currentQuestCard();
      if (questSubStep === 0) {
        return card.audioWord || `audio/word_${card.id}.m4a`;
      } else {
        const sentItem = (card._dailySentences && card._dailySentences[questSubStep - 1]);
        if (sentItem && sentItem.audioSrc) return sentItem.audioSrc;
        return `audio/sentence_${card.id}_0_0.m4a`;
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

    // Update SVG Hourglass sand levels based on remaining seconds
    function updateHourglass(remaining, total) {
      const frac = Math.max(0, Math.min(1, remaining / total));
      const topH = 26 * frac;
      const botH = 26 * (1 - frac);
      const topEl = document.getElementById('topSandRect');
      const botEl = document.getElementById('bottomSandRect');
      const numEl = document.getElementById('questCountdownNum');
      if (topEl) {
        topEl.setAttribute('height', topH);
        topEl.setAttribute('y', 12 + (26 - topH));
      }
      if (botEl) {
        botEl.setAttribute('height', botH);
        botEl.setAttribute('y', 68 - botH);
      }
      if (numEl) numEl.innerText = remaining;
    }

    function startQuestAutoRecord() {
      if (!questAutoPlay) return;
      setQuestStatus("輪到你啦，請大聲朗讀！(沙漏倒數計時中...)", "🎙️", "bg-rose-100 text-rose-800 font-extrabold border-rose-200");
      
      const ring = document.getElementById('questMicRing');
      const hourglassBox = document.getElementById('questHourglassBox');
      ring.classList.remove('hidden');
      hourglassBox.classList.remove('hidden');

      questMaxCountdown = questSubStep === 0 ? 5 : 6;
      questCountdownVal = questMaxCountdown;
      updateHourglass(questCountdownVal, questMaxCountdown);
      document.getElementById('questSpokenText').innerText = "聆聽中，請大聲朗讀...";

      startRecording(onSpeechSuccess, onSpeechFail);

      if (questRecTimer) clearInterval(questRecTimer);
      questRecTimer = setInterval(() => {
        questCountdownVal--;
        updateHourglass(questCountdownVal, questMaxCountdown);
        if (questCountdownVal <= 0) {
          clearInterval(questRecTimer);
          questRecTimer = null;
          // Gracefully stop recognition (processes speech, DOES NOT abort!)
          if (isRecording && recognition) {
            try { recognition.stop(); } catch(e){}
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
      const bestText = lastInterimSpeech || "";
      handleQuestSpeechEvaluation(bestText);
    }

    function handleQuestSpeechEvaluation(spokenText) {
      if (questRecTimer) { clearInterval(questRecTimer); questRecTimer = null; }
      const ring = document.getElementById('questMicRing');
      const hourglassBox = document.getElementById('questHourglassBox');
      ring.classList.add('hidden');
      hourglassBox.classList.add('hidden');

      const targetText = document.getElementById('questTargetEnglish').innerText;
      
      // Update Realtime Display
      const feedbackEl = document.getElementById('questSpokenText');
      feedbackEl.innerText = spokenText ? `"${spokenText}"` : (maxAcousticEnergy > 15 ? "(聽見了聲音，但咬字需更清晰)" : "(未偵測到聲音)");

      const score = calculateScore(targetText, spokenText, maxAcousticEnergy);
      const isGood = score >= 75;

      // Play Sound Effect Graded by Pitch!
      SoundEffects.playScore(score);

      setQuestStatus(
        isGood ? `🌟 太棒了！評測得分：${score} 分！` : `💪 讀得不錯！得分：${score} 分 (已收納至錯詞本)`,
        isGood ? "⭐" : "💡",
        isGood ? "bg-emerald-100 text-emerald-800 font-black border-emerald-300" : "bg-amber-100 text-amber-900 font-black border-amber-300"
      );

      // Record to Log & SRS
      const card = currentQuestCard();
      const typeStr = questSubStep === 0 ? "每日任務-單字" : `每日任務-隨機例句${questSubStep}`;
      recordPracticeLog(card.word, targetText, score, isGood ? "已熟練" : "待加強", typeStr);

      // ALWAYS automatically advance after 1.8 seconds (unless user paused)
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
      if (questSubStep > 2) {
        // Finished word + 2 random sentences for current word!
        questSubStep = 0;
        questWordIdx++;
        
        // Play light cheerful ding when moving to next word
        SoundEffects.playNext();

        if (questWordIdx >= questQueue.length) {
          // Finished all 10 words!
          streakDays++;
          localStorage.setItem('kai_streak_days', streakDays.toString());
          alert("🎉 恭喜！今日 10 個任務單字與例句已全部挑戰完成！打卡成功，連續天數已升至 " + streakDays + " 天！");
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
        
        let shouldShow = true;
        if (freeCategory === 'weak') {
          const isWeak = practiceLogs.some(l => l.word === c.word && l.score < 75);
          if (!isWeak) shouldShow = false;
        } else if (freeCategory !== 'all') {
          if (c.category !== freeCategory) shouldShow = false;
        }

        if (!shouldShow) return;

        btn.className = `p-3 rounded-2xl border text-left transition flex items-center gap-2.5 ${
          isActive 
            ? 'bg-indigo-600 text-white shadow-md border-indigo-600' 
            : 'bg-white hover:bg-slate-50 text-slate-800 border-slate-200 shadow-sm'
        }`;
        btn.onclick = () => {
          freeCardIndex = idx;
          freeScenarioIndex = 0;
          renderFreeGrid();
          renderFreeCard();
        };
        btn.innerHTML = `
          <span class="text-2xl">${c.emoji}</span>
          <div class="overflow-hidden">
            <div class="font-bold text-xs truncate">${c.word}</div>
            <div class="text-[10px] ${isActive ? 'text-indigo-100' : 'text-slate-600'} truncate">${c.phonetic}</div>
          </div>
        `;
        container.appendChild(btn);
      });

      // Update Weak Count Badge
      const weakWords = new Set(practiceLogs.filter(l => l.score < 75).map(l => l.word));
      document.getElementById('weakCountBadge').innerText = weakWords.size;
    }

    function renderFreeCard() {
      const card = currentFreeCard();
      document.getElementById('freeEmoji').innerText = card.emoji;
      document.getElementById('freeWord').innerText = card.word;
      document.getElementById('freePhonetic').innerText = card.phonetic;
      document.getElementById('freeMeaning').innerText = card.meaning;

      [0, 1, 2].forEach(i => {
        const tab = document.getElementById(`scTab${i}`);
        if (!tab) return;
        if (i === freeScenarioIndex) {
          tab.className = "flex-1 py-1.5 rounded-xl bg-indigo-600 text-white shadow-sm transition";
        } else {
          tab.className = "flex-1 py-1.5 rounded-xl bg-slate-100 text-slate-600 hover:bg-slate-200 transition";
        }
      });

      const sc = card.scenarios[freeScenarioIndex] || card.scenarios[0];
      document.getElementById('freeScenarioTitle').innerText = sc.title || `情境 ${freeScenarioIndex + 1}`;

      const listContainer = document.getElementById('freeSentenceList');
      listContainer.innerHTML = '';

      if (sc.sentences) {
        sc.sentences.forEach((sent, sIdx) => {
          const trans = (sc.translations && sc.translations[sIdx]) ? sc.translations[sIdx] : "";
          const row = document.createElement('div');
          row.className = "p-3 rounded-2xl bg-slate-50 border border-slate-200 flex items-center justify-between gap-3";
          row.innerHTML = `
            <div class="flex-1 text-left">
              <div class="text-xs font-bold text-indigo-950">${sent}</div>
              <div class="text-[11px] text-slate-500 mt-0.5">${trans}</div>
            </div>
            <button onclick="playFreeSentenceAudio('${card.id}', ${freeScenarioIndex}, ${sIdx})" class="p-2 rounded-xl bg-white border border-slate-200 hover:bg-indigo-50 text-indigo-600 text-xs shadow-sm">
              🔊 播放
            </button>
          `;
          listContainer.appendChild(row);
        });
      }
    }

    function setFreeCategory(cat) {
      freeCategory = cat;
      document.querySelectorAll('.free-cat-btn').forEach(btn => {
        if (btn.getAttribute('data-cat') === cat) {
          btn.className = "free-cat-btn active px-3 py-1.5 rounded-xl font-bold bg-indigo-600 text-white shadow-sm whitespace-nowrap";
        } else {
          btn.className = "free-cat-btn px-3 py-1.5 rounded-xl font-semibold bg-slate-100 text-slate-600 hover:bg-slate-200 whitespace-nowrap";
        }
      });
      renderFreeGrid();
    }

    function selectFreeScenario(sIdx) {
      freeScenarioIndex = sIdx;
      renderFreeCard();
    }

    function playFreeWordAudio() {
      const card = currentFreeCard();
      const src = card.audioWord || `audio/word_${card.id}.m4a`;
      freeAudioPlayer.src = src;
      freeAudioPlayer.onerror = () => fallbackNaturalTTS(card.word, null);
      freeAudioPlayer.play().catch(() => fallbackNaturalTTS(card.word, null));
    }

    function playFreeSentenceAudio(cardId, scIdx, sentIdx) {
      const src = `audio/sentence_${cardId}_${scIdx}_${sentIdx}.m4a`;
      freeAudioPlayer.src = src;
      freeAudioPlayer.onerror = () => {
        const card = MASTER_VOCAB.find(c => c.id === cardId);
        const text = (card && card.scenarios[scIdx]) ? card.scenarios[scIdx].sentences[sentIdx] : "";
        fallbackNaturalTTS(text, null);
      };
      freeAudioPlayer.play().catch(() => {
        const card = MASTER_VOCAB.find(c => c.id === cardId);
        const text = (card && card.scenarios[scIdx]) ? card.scenarios[scIdx].sentences[sentIdx] : "";
        fallbackNaturalTTS(text, null);
      });
    }

    // ========================================================
    // MODE 3: ADVENTURE ISLAND IMPLEMENTATION
    // ========================================================
    function renderAdventureMap() {
      const container = document.getElementById('advStageGrid');
      container.innerHTML = '';
      let totalStars = 0;

      MASTER_VOCAB.forEach((c, idx) => {
        const stageNum = idx + 1;
        const stars = adventureStars[c.word] || 0;
        totalStars += stars;

        const stageBtn = document.createElement('button');
        stageBtn.className = "p-3 rounded-2xl bg-white border border-indigo-100 shadow-sm flex flex-col items-center text-center hover:scale-105 transition";
        stageBtn.onclick = () => {
          freeCardIndex = idx;
          freeScenarioIndex = 0;
          switchAppMode('free');
        };
        stageBtn.innerHTML = `
          <div class="text-[10px] font-bold text-slate-600">第 ${stageNum} 關</div>
          <div class="text-3xl my-1">${c.emoji}</div>
          <div class="text-xs font-bold text-indigo-950 truncate w-full">${c.word}</div>
          <div class="text-xs mt-1 text-amber-500 font-bold">${'⭐'.repeat(stars) || '☆☆☆'}</div>
        `;
        container.appendChild(stageBtn);
      });

      document.getElementById('advTotalStars').innerText = totalStars;
    }

    // ========================================================
    // AUDIO RECORDING & SPEECH EVALUATION ENGINE
    // ========================================================
    function startRecording(onSuccess, onFail) {
      if (isRecording) stopRecording();

      const SpeechRec = window.SpeechRecognition || window.webkitSpeechRecognition;
      if (!SpeechRec) {
        console.warn("SpeechRecognition not supported in browser, using fallback energy");
      } else {
        try {
          recognition = new SpeechRec();
          recognition.lang = 'en-US';
          recognition.interimResults = true;
          recognition.maxAlternatives = 1;

          lastInterimSpeech = "";
          let finalTranscript = "";

          recognition.onresult = (e) => {
            let interim = "";
            for (let i = e.resultIndex; i < e.results.length; ++i) {
              if (e.results[i].isFinal) {
                finalTranscript += e.results[i][0].transcript;
              } else {
                interim += e.results[i][0].transcript;
              }
            }
            const currentText = (finalTranscript || interim).trim();
            if (currentText) {
              lastInterimSpeech = currentText;
              const feedbackEl = document.getElementById('questSpokenText');
              if (feedbackEl) feedbackEl.innerText = currentText;
            }
          };

          recognition.onerror = (e) => {
            console.warn("SpeechRec error:", e.error);
            if (onFail) onFail(e.error);
          };

          recognition.onend = () => {
            isRecording = false;
            const res = finalTranscript || lastInterimSpeech || "";
            if (onSuccess) onSuccess(res);
          };

          recognition.start();
          isRecording = true;
        } catch(e) {
          console.warn("Could not start recognition:", e);
        }
      }

      // Start Analyser for Waveform and Acoustic Energy
      startAcousticAnalyser();
    }

    function stopRecording() {
      if (recognition) {
        try { recognition.stop(); } catch(e){}
        recognition = null;
      }
      isRecording = false;
      stopAcousticAnalyser();
    }

    function startAcousticAnalyser() {
      maxAcousticEnergy = 0;
      if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) return;

      navigator.mediaDevices.getUserMedia({ audio: true }).then(stream => {
        microphoneStream = stream;
        const AC = window.AudioContext || window.webkitAudioContext;
        if (!AC) return;
        audioContext = new AC();
        analyser = audioContext.createAnalyser();
        analyser.fftSize = 256;
        const source = audioContext.createMediaStreamSource(stream);
        source.connect(analyser);

        const canvas = document.getElementById('questWaveformCanvas');
        const ctx = canvas ? canvas.getContext('2d') : null;
        const dataArray = new Uint8Array(analyser.frequencyBinCount);

        function draw() {
          if (!isRecording) return;
          animFrameId = requestAnimationFrame(draw);
          analyser.getByteFrequencyData(dataArray);

          let sum = 0;
          for (let i = 0; i < dataArray.length; i++) {
            sum += dataArray[i];
          }
          const avg = sum / dataArray.length;
          if (avg > maxAcousticEnergy) maxAcousticEnergy = avg;

          if (ctx && canvas) {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            ctx.fillStyle = '#6366F1';
            const barWidth = (canvas.width / dataArray.length) * 2.5;
            let x = 0;
            for (let i = 0; i < dataArray.length; i++) {
              const barHeight = (dataArray[i] / 255) * canvas.height;
              ctx.fillRect(x, canvas.height - barHeight, barWidth, barHeight);
              x += barWidth + 1;
            }
          }
        }
        draw();
      }).catch(err => {
        console.warn("getUserMedia failed or denied:", err);
      });
    }

    function stopAcousticAnalyser() {
      if (animFrameId) cancelAnimationFrame(animFrameId);
      if (microphoneStream) {
        microphoneStream.getTracks().forEach(t => t.stop());
        microphoneStream = null;
      }
      if (audioContext) {
        audioContext.close().catch(()=>{});
        audioContext = null;
      }
    }

    function calculateScore(target, spoken, energy) {
      if (!spoken || spoken.trim() === '') {
        if (energy > 25) return Math.min(76, Math.round(55 + (energy * 0.3)));
        return 50;
      }

      const clean = s => s.toLowerCase().replace(/[^a-z0-9 ]/g, '').trim();
      const tClean = clean(target);
      const sClean = clean(spoken);

      if (tClean === sClean) return Math.floor(Math.random() * 6) + 94; // 94-99
      if (sClean.includes(tClean) || tClean.includes(sClean)) return Math.floor(Math.random() * 8) + 85; // 85-92

      // Levenshtein similarity
      const dist = levenshtein(tClean, sClean);
      const maxLen = Math.max(tClean.length, sClean.length);
      const sim = Math.max(0, 1 - dist / maxLen);
      let calculated = Math.round(sim * 100);
      if (calculated < 60 && energy > 15) calculated = 65;
      return Math.min(98, Math.max(50, calculated));
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
            matrix[i][j] = Math.min(
              matrix[i - 1][j - 1] + 1,
              Math.min(matrix[i][j - 1] + 1, matrix[i - 1][j] + 1)
            );
          }
        }
      }
      return matrix[b.length][a.length];
    }

    // Web Speech Fallback TTS
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
    function recordPracticeLog(word, sentence, score, tag, mode) {
      const log = {
        timestamp: new Date().toISOString(),
        word,
        sentence,
        score,
        tag,
        mode
      };
      practiceLogs.unshift(log);
      if (practiceLogs.length > 300) practiceLogs.pop();
      localStorage.setItem('kai_practice_logs', JSON.stringify(practiceLogs));

      // Update Adventure Stars
      const currentStar = adventureStars[word] || 0;
      let starEarned = 1;
      if (score >= 90) starEarned = 3;
      else if (score >= 75) starEarned = 2;
      if (starEarned > currentStar) {
        adventureStars[word] = starEarned;
        localStorage.setItem('kai_adventure_stars', JSON.stringify(adventureStars));
      }

      updateLogUI();
      renderFreeGrid();
    }

    function updateLogUI() {
      const container = document.getElementById('logTableContainer');
      if (!container) return;
      if (practiceLogs.length === 0) {
        container.innerHTML = '<div class="text-center py-8 text-slate-400">目前尚無練習評測記錄，開始今日挑戰試試吧！</div>';
        return;
      }

      let html = '<table class="w-full text-left border-collapse"><thead><tr class="border-b border-slate-200 text-slate-500"><th class="py-2">時間</th><th>內容</th><th>得分</th><th>狀態</th><th>類型</th></tr></thead><tbody>';
      practiceLogs.slice(0, 50).forEach(l => {
        const isGood = l.score >= 75;
        const d = new Date(l.timestamp);
        const timeStr = `${pad(d.getHours())}:${pad(d.getMinutes())}:${pad(d.getSeconds())}`;
        html += `
          <tr class="border-b border-slate-100 hover:bg-slate-50">
            <td class="py-2 text-slate-400 font-mono">${timeStr}</td>
            <td class="font-bold text-slate-800">${l.sentence || l.word}</td>
            <td><span class="px-2 py-0.5 rounded-full font-bold ${isGood ? 'bg-emerald-100 text-emerald-800' : 'bg-rose-100 text-rose-800'}">${l.score} 分</span></td>
            <td><span class="text-xs font-semibold ${isGood ? 'text-emerald-600' : 'text-rose-600'}">${l.tag}</span></td>
            <td class="text-slate-400 text-[11px]">${l.mode || '任務'}</td>
          </tr>
        `;
      });
      html += '</tbody></table>';
      container.innerHTML = html;
    }

    function exportLogsCSV() {
      if (practiceLogs.length === 0) {
        alert("尚無記錄可匯出！");
        return;
      }
      let csv = "時間,單字,朗讀內容,得分,評級,練習模式\\n";
      practiceLogs.forEach(l => {
        csv += `"${l.timestamp}","${l.word}","${l.sentence.replace(/"/g, '""')}",${l.score},"${l.tag}","${l.mode}"\\n`;
      });
      const blob = new Blob([new Uint8Array([0xEF, 0xBB, 0xBF]), csv], { type: 'text/csv;charset=utf-8;' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `KaiSpeak_學習評測記錄_${new Date().toISOString().slice(0,10)}.csv`;
      a.click();
      URL.revokeObjectURL(url);
    }

    function clearAllLogs() {
      if (confirm("確定要清空所有發音評測紀錄與錯詞本嗎？")) {
        practiceLogs = [];
        adventureStars = {};
        localStorage.removeItem('kai_practice_logs');
        localStorage.removeItem('kai_adventure_stars');
        updateLogUI();
        renderFreeGrid();
        renderAdventureMap();
      }
    }

    // ========================================================
    // QR CODE & MODAL HELPERS
    // ========================================================
    function initQRCode() {
      const canvas = document.getElementById('qrCodeCanvas');
      if (canvas && window.QRCode) {
        QRCode.toCanvas(canvas, "https://honga0812.github.io/KaiSpeak/?v=4", {
          width: 176,
          margin: 1,
          color: { dark: '#312E81', light: '#FFFFFF' }
        });
      }
    }

    function toggleQRModal() {
      const m = document.getElementById('qrModal');
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
"""

output = template.replace("__VOCAB_PLACEHOLDER__", vocab_str)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(output)

print("Generated index.html successfully! File size:", len(output))
