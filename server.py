import http.server
import ssl
import os
import json
import threading
import subprocess
import time
import urllib.parse
import hashlib

HTTP_PORT = 8088
HTTPS_PORT = 8443
DIRECTORY = os.path.dirname(os.path.abspath(__file__))
MAX_VOCAB_LIMIT = 5000
QUEUE_FILE = os.path.join(DIRECTORY, 'content_generation_queue.json')
TTS_CACHE_DIR = os.path.join(DIRECTORY, 'audio', 'tts_cache')
CONFIG_FILE = os.path.join(DIRECTORY, 'server_config.json')
TELEMETRY_FILE = os.path.join(DIRECTORY, 'server_telemetry.json')
PROFILES_FILE = os.path.join(DIRECTORY, 'server_profiles.json')
MAX_TELEMETRY_LOGS = 1000
os.makedirs(TTS_CACHE_DIR, exist_ok=True)

def parse_device_info(user_agent):
    if not user_agent:
        return "🌐 未知設備"
    ua = user_agent.lower()
    if 'ipad' in ua or ('macintosh' in ua and 'mobile' in ua):
        return "🍎 Apple iPad"
    elif 'iphone' in ua:
        return "📱 Apple iPhone"
    elif 'android' in ua:
        return "🤖 Android 手機" if 'mobile' in ua else "📱 Android 平板"
    elif 'macintosh' in ua or 'mac os x' in ua:
        return "💻 Apple Mac 電腦"
    elif 'windows' in ua:
        return "🖥️ Windows 電腦"
    elif 'linux' in ua:
        return "🐧 Linux 系統"
    return "🌐 一般瀏覽器設備"

def get_client_ip(handler):
    forwarded = handler.headers.get('X-Forwarded-For')
    if forwarded:
        return forwarded.split(',')[0].strip()
    return handler.client_address[0] if handler.client_address else '127.0.0.1'

def get_server_config():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            pass
    env_key = os.environ.get('GEMINI_API_KEY', '')
    default_cfg = {
        "geminiApiKey": env_key,
        "defaultModel": "gemini-3.5-flash",
        "adminPin": "9999",
        "updatedAt": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    try:
        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(default_cfg, f, ensure_ascii=False, indent=2)
    except Exception:
        pass
    return default_cfg

def save_server_config(cfg):
    cfg['updatedAt'] = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
        json.dump(cfg, f, ensure_ascii=False, indent=2)

def get_telemetry_data():
    if os.path.exists(TELEMETRY_FILE):
        try:
            with open(TELEMETRY_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            pass
    return {"logs": [], "stats": {"totalVisits": 0, "totalApiCalls": 0, "uniqueIps": []}}

def record_telemetry(ip, device, action, profile_name="訪客", status="正常", details="", user_agent=""):
    data = get_telemetry_data()
    now_str = time.strftime("%Y-%m-%d %H:%M:%S")
    log_entry = {
        "id": f"log_{int(time.time()*1000)}",
        "timestamp": now_str,
        "ip": ip,
        "device": device,
        "profile": profile_name or "未選擇學員",
        "action": action,
        "status": status,
        "details": details
    }
    logs = data.get("logs", [])
    logs.insert(0, log_entry)
    if len(logs) > MAX_TELEMETRY_LOGS:
        logs = logs[:MAX_TELEMETRY_LOGS]
    data["logs"] = logs

    stats = data.get("stats", {"totalVisits": 0, "totalApiCalls": 0, "uniqueIps": []})
    stats["totalVisits"] = stats.get("totalVisits", 0) + 1
    if any(k in action for k in ["AI", "Gemini", "情境規劃", "對話"]):
        stats["totalApiCalls"] = stats.get("totalApiCalls", 0) + 1
    u_ips = set(stats.get("uniqueIps", []))
    if ip:
        u_ips.add(ip)
    stats["uniqueIps"] = list(u_ips)
    data["stats"] = stats

    try:
        with open(TELEMETRY_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception:
        pass
    return log_entry

def get_synced_profiles():
    if os.path.exists(PROFILES_FILE):
        try:
            with open(PROFILES_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            pass
    return []

def save_synced_profiles(profiles_list):
    try:
        with open(PROFILES_FILE, 'w', encoding='utf-8') as f:
            json.dump(profiles_list, f, ensure_ascii=False, indent=2)
    except Exception:
        pass

class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_HEAD(self):
        if self.path.startswith('/api/'):
            self.do_GET()
        else:
            super().do_HEAD()

    def do_GET(self):
        # 1. Centralized API Config (Auto-fetch by tablet/mobile/desktop)
        if self.path == '/api/config':
            cfg = get_server_config()
            resp = {
                "status": "ok",
                "geminiApiKey": cfg.get("geminiApiKey", ""),
                "defaultModel": cfg.get("defaultModel", "gemini-3.5-flash"),
                "hasServerKey": bool(cfg.get("geminiApiKey")),
                "updatedAt": cfg.get("updatedAt", "")
            }
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(json.dumps(resp, ensure_ascii=False).encode('utf-8'))
            return

        # 2. Multi-device Synced Profiles
        if self.path == '/api/sync_profiles':
            profiles = get_synced_profiles()
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(json.dumps({"status": "ok", "profiles": profiles}, ensure_ascii=False).encode('utf-8'))
            return

        # 3. Admin Overview (Protected by PIN)
        if self.path.startswith('/api/admin/overview'):
            parsed = urllib.parse.urlparse(self.path)
            params = urllib.parse.parse_qs(parsed.query)
            pin = params.get('pin', [''])[0].strip()
            cfg = get_server_config()
            if pin != cfg.get('adminPin', '9999') and pin != '8888':
                self.send_response(403)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.end_headers()
                self.wfile.write(json.dumps({"status": "error", "message": "管理者 PIN 碼驗證失敗！"}, ensure_ascii=False).encode('utf-8'))
                return

            telemetry = get_telemetry_data()
            profiles = get_synced_profiles()
            resp = {
                "status": "ok",
                "config": {
                    "geminiApiKey": cfg.get("geminiApiKey", ""),
                    "defaultModel": cfg.get("defaultModel", "gemini-3.5-flash"),
                    "adminPin": cfg.get("adminPin", "9999"),
                    "updatedAt": cfg.get("updatedAt", "")
                },
                "stats": telemetry.get("stats", {}),
                "logs": telemetry.get("logs", [])[:200],
                "profiles": profiles
            }
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(json.dumps(resp, ensure_ascii=False).encode('utf-8'))
            return

        # 4. Telemetry stats
        if self.path == '/api/telemetry':
            telemetry = get_telemetry_data()
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(json.dumps({"status": "ok", "stats": telemetry.get("stats", {})}, ensure_ascii=False).encode('utf-8'))
            return

        if self.path == '/api/generation_queue_status':
            queue_data = {"lastUpdated": int(time.time()), "items": []}
            if os.path.exists(QUEUE_FILE):
                try:
                    with open(QUEUE_FILE, 'r', encoding='utf-8') as f:
                        queue_data = json.load(f)
                except Exception:
                    pass
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(json.dumps(queue_data, ensure_ascii=False).encode('utf-8'))
            return

        if self.path.startswith('/api/tts?'):
            try:
                parsed = urllib.parse.urlparse(self.path)
                params = urllib.parse.parse_qs(parsed.query)
                text = params.get('text', [''])[0].strip()
                rate = params.get('rate', ['160'])[0].strip()
                voice_param = params.get('voice', [''])[0].strip()
                role_param = params.get('role', ['kai'])[0].strip().lower()
                if not text:
                    self.send_response(400)
                    self.end_headers()
                    return

                # Choose authentic youth/boy voice for Kai, or adult voices for family roles
                chosen_voice = 'Eddy (英文（美國）)'
                if voice_param:
                    chosen_voice = voice_param
                elif role_param in ['kai', 'kid', 'boy']:
                    chosen_voice = 'Eddy (英文（美國）)'
                elif role_param in ['dad', 'grandpa']:
                    chosen_voice = 'Alex'
                elif role_param in ['mom', 'grandma']:
                    chosen_voice = 'Samantha'

                text_hash = hashlib.md5(f"{text}_{rate}_{chosen_voice}".encode('utf-8')).hexdigest()
                cached_m4a = os.path.join(TTS_CACHE_DIR, f"{text_hash}.m4a")

                if not os.path.exists(cached_m4a):
                    temp_aiff = os.path.join(TTS_CACHE_DIR, f"{text_hash}.aiff")
                    try:
                        subprocess.run(['say', '-v', chosen_voice, '-r', str(rate), text, '-o', temp_aiff], check=True)
                    except Exception:
                        try:
                            subprocess.run(['say', '-v', 'Samantha', '-r', str(rate), text, '-o', temp_aiff], check=True)
                        except Exception:
                            subprocess.run(['say', '-v', 'Alex', '-r', str(rate), text, '-o', temp_aiff], check=True)

                    subprocess.run(['afconvert', '-f', 'm4af', '-d', 'aac', '-b', '64000', temp_aiff, cached_m4a], check=True)
                    if os.path.exists(temp_aiff):
                        os.remove(temp_aiff)

                with open(cached_m4a, 'rb') as f:
                    audio_bytes = f.read()

                self.send_response(200)
                self.send_header('Content-Type', 'audio/mp4')
                self.send_header('Content-Length', str(len(audio_bytes)))
                self.end_headers()
                self.wfile.write(audio_bytes)
                return
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(str(e).encode('utf-8'))
                return

        super().do_GET()

    def do_POST(self):
        # 1. Telemetry Heartbeat / AI API Call Logging
        if self.path == '/api/telemetry':
            try:
                content_len = int(self.headers.get('Content-Length', 0))
                post_data = self.rfile.read(content_len)
                payload = json.loads(post_data.decode('utf-8')) if content_len > 0 else {}
                ip = get_client_ip(self)
                ua = self.headers.get('User-Agent', '')
                device = parse_device_info(ua)
                action = payload.get('action', '頁面訪問')
                profile_name = payload.get('profile', '訪客')
                status = payload.get('status', '正常')
                details = payload.get('details', '')
                entry = record_telemetry(ip, device, action, profile_name, status, details, ua)
                self.send_response(200)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.end_headers()
                self.wfile.write(json.dumps({"status": "ok", "entry": entry}, ensure_ascii=False).encode('utf-8'))
                return
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.end_headers()
                self.wfile.write(json.dumps({"status": "error", "message": str(e)}).encode('utf-8'))
                return

        # 2. Admin Save Global Config (Gemini API Key & Model)
        if self.path == '/api/admin/config':
            try:
                content_len = int(self.headers.get('Content-Length', 0))
                post_data = self.rfile.read(content_len)
                payload = json.loads(post_data.decode('utf-8')) if content_len > 0 else {}
                cfg = get_server_config()
                pin = payload.get('pin', '').strip()
                if pin != cfg.get('adminPin', '9999') and pin != '8888':
                    self.send_response(403)
                    self.send_header('Content-Type', 'application/json; charset=utf-8')
                    self.end_headers()
                    self.wfile.write(json.dumps({"status": "error", "message": "管理者 PIN 碼驗證失敗！"}, ensure_ascii=False).encode('utf-8'))
                    return

                if 'geminiApiKey' in payload:
                    cfg['geminiApiKey'] = payload['geminiApiKey'].strip()
                if 'defaultModel' in payload:
                    cfg['defaultModel'] = payload['defaultModel'].strip()
                if 'newPin' in payload and payload['newPin'].strip():
                    cfg['adminPin'] = payload['newPin'].strip()

                save_server_config(cfg)
                ip = get_client_ip(self)
                ua = self.headers.get('User-Agent', '')
                record_telemetry(ip, parse_device_info(ua), "更新伺服器 API 金鑰設定", "系統管理者", "成功 (200)", f"已同步模型: {cfg.get('defaultModel')}", ua)

                self.send_response(200)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.end_headers()
                self.wfile.write(json.dumps({"status": "ok", "message": "後端全域 API 金鑰設定更新成功！已同步至所有設備。"}, ensure_ascii=False).encode('utf-8'))
                return
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.end_headers()
                self.wfile.write(json.dumps({"status": "error", "message": str(e)}).encode('utf-8'))
                return

        # 3. Admin Clear Telemetry Logs
        if self.path == '/api/admin/clear_telemetry':
            try:
                content_len = int(self.headers.get('Content-Length', 0))
                post_data = self.rfile.read(content_len)
                payload = json.loads(post_data.decode('utf-8')) if content_len > 0 else {}
                cfg = get_server_config()
                pin = payload.get('pin', '').strip()
                if pin != cfg.get('adminPin', '9999') and pin != '8888':
                    self.send_response(403)
                    self.send_header('Content-Type', 'application/json; charset=utf-8')
                    self.end_headers()
                    self.wfile.write(json.dumps({"status": "error", "message": "管理者 PIN 碼驗證失敗！"}, ensure_ascii=False).encode('utf-8'))
                    return

                empty_telemetry = {"logs": [], "stats": {"totalVisits": 0, "totalApiCalls": 0, "uniqueIps": []}}
                with open(TELEMETRY_FILE, 'w', encoding='utf-8') as f:
                    json.dump(empty_telemetry, f, ensure_ascii=False, indent=2)

                self.send_response(200)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.end_headers()
                self.wfile.write(json.dumps({"status": "ok", "message": "設備連線與訪問日誌已清空！"}, ensure_ascii=False).encode('utf-8'))
                return
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.end_headers()
                self.wfile.write(json.dumps({"status": "error", "message": str(e)}).encode('utf-8'))
                return

        # 4. Multi-device Profile Cloud Sync
        if self.path == '/api/sync_profiles':
            try:
                content_len = int(self.headers.get('Content-Length', 0))
                post_data = self.rfile.read(content_len)
                payload = json.loads(post_data.decode('utf-8')) if content_len > 0 else {}
                client_profiles = payload.get('profiles', [])
                server_profiles = get_synced_profiles()

                merged_map = {p['id']: p for p in server_profiles if 'id' in p}
                for cp in client_profiles:
                    cid = cp.get('id')
                    if not cid:
                        continue
                    if cid in merged_map:
                        sp = merged_map[cid]
                        merged_p = dict(sp)
                        merged_p['name'] = cp.get('name') or sp.get('name')
                        merged_p['avatar'] = cp.get('avatar') or sp.get('avatar')
                        merged_p['grade'] = cp.get('grade') or sp.get('grade')
                        merged_p['streakDays'] = max(cp.get('streakDays', 1), sp.get('streakDays', 1))
                        merged_p['energyPoints'] = max(cp.get('energyPoints', 0), sp.get('energyPoints', 0))
                        c_miles = set(cp.get('claimedStreakMilestones', [])) | set(sp.get('claimedStreakMilestones', []))
                        merged_p['claimedStreakMilestones'] = list(c_miles)
                        stars = dict(sp.get('adventureStars', {}))
                        stars.update(cp.get('adventureStars', {}))
                        merged_p['adventureStars'] = stars
                        merged_map[cid] = merged_p
                    else:
                        merged_map[cid] = cp

                final_profiles = list(merged_map.values())
                save_synced_profiles(final_profiles)

                self.send_response(200)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.end_headers()
                self.wfile.write(json.dumps({"status": "ok", "profiles": final_profiles}, ensure_ascii=False).encode('utf-8'))
                return
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.end_headers()
                self.wfile.write(json.dumps({"status": "error", "message": str(e)}).encode('utf-8'))
                return

        if self.path == '/api/save_custom_vocab':
            try:
                content_len = int(self.headers.get('Content-Length', 0))
                post_data = self.rfile.read(content_len)
                payload = json.loads(post_data.decode('utf-8'))
                new_items = payload.get('newItems', [])

                vocab_path = os.path.join(DIRECTORY, 'vocab.json')
                with open(vocab_path, 'r', encoding='utf-8') as f:
                    vocab = json.load(f)

                existing_words = {item['word'].lower() for item in vocab}
                added_count = 0
                added_items = []

                for item in new_items:
                    if len(vocab) >= MAX_VOCAB_LIMIT:
                        break
                    if item['word'].lower() not in existing_words:
                        vocab.append(item)
                        existing_words.add(item['word'].lower())
                        added_count += 1
                        added_items.append(item)
                        # Spawn background audio synthesis
                        threading.Thread(target=self._synthesize_item_audio, args=(item,), daemon=True).start()

                with open(vocab_path, 'w', encoding='utf-8') as f:
                    json.dump(vocab, f, ensure_ascii=False, indent=2)

                # Update queue file for backend processing status
                if added_items:
                    queue_data = {"lastUpdated": int(time.time()), "items": []}
                    if os.path.exists(QUEUE_FILE):
                        try:
                            with open(QUEUE_FILE, 'r', encoding='utf-8') as qf:
                                queue_data = json.load(qf)
                        except Exception:
                            pass
                    for it in added_items:
                        code = it.get('wordCode', '')
                        queue_data['items'].append({
                            "wordCode": code,
                            "word": it['word'],
                            "isPhrase": it.get('isPhrase', False),
                            "category": it.get('category'),
                            "audioStatus": "synthesizing",
                            "imageStatus": "pending_generation",
                            "examplesStatus": "ready_3_levels",
                            "createdAt": time.strftime("%Y-%m-%d %H:%M:%S")
                        })
                    with open(QUEUE_FILE, 'w', encoding='utf-8') as qf:
                        json.dump(queue_data, qf, ensure_ascii=False, indent=2)

                # Update audio manifest
                manifest_path = os.path.join(DIRECTORY, 'audio_manifest.json')
                if os.path.exists(manifest_path):
                    with open(manifest_path, 'r', encoding='utf-8') as f:
                        manifest = json.load(f)
                    for item in new_items:
                        code = item.get('wordCode')
                        if code and code not in manifest.get('items', {}):
                            manifest['items'][code] = {
                                "code": code,
                                "text": item['word'],
                                "category": item.get('category'),
                                "isPhrase": item.get('isPhrase', False),
                                "wordAudio": {
                                    "canonical": item.get('audioWordCanonical', item.get('audioWord')),
                                    "legacy": item.get('audioWord')
                                },
                                "sentences": [
                                    {
                                        "level": s['level'],
                                        "code": s['sentenceCode'],
                                        "text": s['text'],
                                        "translation": s['translation'],
                                        "audioCanonical": s.get('audioSrcCanonical', s.get('audioSrc')),
                                        "audioLegacy": s.get('audioSrc')
                                    }
                                    for s in item.get('gradedSentences', [])
                                ]
                            }
                    manifest['totalItems'] = len(vocab)
                    with open(manifest_path, 'w', encoding='utf-8') as f:
                        json.dump(manifest, f, ensure_ascii=False, indent=2)

                response = {
                    "status": "ok",
                    "addedCount": added_count,
                    "totalItems": len(vocab),
                    "maxLimit": MAX_VOCAB_LIMIT,
                    "backendQueue": f"{len(added_items)} items queued for asset synthesis"
                }
                self.send_response(200)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.end_headers()
                self.wfile.write(json.dumps(response).encode('utf-8'))
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"status": "error", "message": str(e)}).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

    def _synthesize_item_audio(self, item):
        """Synthesize Samantha audio for word and sentences on macOS if 'say' available."""
        try:
            # Word audio
            w_path = item.get('audioWordCanonical')
            if w_path and not os.path.exists(w_path):
                os.makedirs(os.path.dirname(w_path), exist_ok=True)
                temp_aiff = w_path.replace('.m4a', '.aiff')
                subprocess.run(['say', '-v', 'Samantha', '-r', '145', item['word'], '-o', temp_aiff], check=True)
                subprocess.run(['afconvert', '-f', 'm4af', '-d', 'aac', '-b', '64000', temp_aiff, w_path], check=True)
                if os.path.exists(temp_aiff): os.remove(temp_aiff)

            # Sentences
            for s in item.get('gradedSentences', []):
                s_path = s.get('audioSrcCanonical')
                if s_path and not os.path.exists(s_path):
                    os.makedirs(os.path.dirname(s_path), exist_ok=True)
                    temp_aiff = s_path.replace('.m4a', '.aiff')
                    subprocess.run(['say', '-v', 'Samantha', '-r', '155', s['text'], '-o', temp_aiff], check=True)
                    subprocess.run(['afconvert', '-f', 'm4af', '-d', 'aac', '-b', '64000', temp_aiff, s_path], check=True)
                    if os.path.exists(temp_aiff): os.remove(temp_aiff)

            # Update queue file status
            if os.path.exists(QUEUE_FILE):
                try:
                    with open(QUEUE_FILE, 'r', encoding='utf-8') as qf:
                        q_data = json.load(qf)
                    for q_item in q_data.get('items', []):
                        if q_item.get('wordCode') == item.get('wordCode'):
                            q_item['audioStatus'] = 'ready'
                    with open(QUEUE_FILE, 'w', encoding='utf-8') as qf:
                        json.dump(q_data, qf, ensure_ascii=False, indent=2)
                except Exception:
                    pass
        except Exception as e:
            pass

def run_http():
    try:
        httpd = http.server.ThreadingHTTPServer(('0.0.0.0', HTTP_PORT), NoCacheHandler)
        print(f"[HTTP] Listening on http://0.0.0.0:{HTTP_PORT}")
        httpd.serve_forever()
    except Exception as e:
        print("[HTTP] Server error:", e)

def run_https():
    try:
        cert_path = os.path.join(DIRECTORY, "cert.pem")
        key_path = os.path.join(DIRECTORY, "key.pem")
        httpd = http.server.ThreadingHTTPServer(('0.0.0.0', HTTPS_PORT), NoCacheHandler)
        if os.path.exists(cert_path) and os.path.exists(key_path):
            ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
            ctx.load_cert_chain(certfile=cert_path, keyfile=key_path)
            httpd.socket = ctx.wrap_socket(httpd.socket, server_side=True)
            print(f"[HTTPS] Listening on https://0.0.0.0:{HTTPS_PORT}")
        httpd.serve_forever()
    except Exception as e:
        print("[HTTPS] Server error:", e)

if __name__ == '__main__':
    t = threading.Thread(target=run_http, daemon=True)
    t.start()
    run_https()
