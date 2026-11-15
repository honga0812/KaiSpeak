import http.server
import ssl
import os
import json
import threading
import subprocess
import time

HTTP_PORT = 8088
HTTPS_PORT = 8443
DIRECTORY = os.path.dirname(os.path.abspath(__file__))
MAX_VOCAB_LIMIT = 5000
QUEUE_FILE = os.path.join(DIRECTORY, 'content_generation_queue.json')

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

    def do_GET(self):
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

        super().do_GET()

    def do_POST(self):
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
