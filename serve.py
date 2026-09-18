import sys
import os
import socket
import http.server
import socketserver

port = 8080
for p in [8080, 8000, 5000, 8085, 3000]:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind(('127.0.0.1', p))
        s.close()
        port = p
        break
    except Exception:
        pass

os.chdir(r'C:\Users\HP TTS\.gemini\antigravity\scratch\sauver-ton-couple-landing')
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(('127.0.0.1', port), Handler) as httpd:
    print(f"Serving HTTP on 127.0.0.1 port {port} (http://127.0.0.1:{port}/) ...")
    httpd.serve_forever()
