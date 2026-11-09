import http.server
import ssl
import os
import threading

HTTP_PORT = 8088
HTTPS_PORT = 8443
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

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
