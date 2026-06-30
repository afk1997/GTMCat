#!/usr/bin/env python3
"""Local preview server for the GTMCat site.

  /          -> GTMCat Landing (standalone).html   (your file, served untouched)
  /pricing   -> landing/pricing.html
  /privacy   -> landing/privacy.html   (and /support /terms /refunds)
  /assets/*  -> landing/assets/*

Usage:  python3 serve.py [port]      (default 8080)
"""
import http.server
import socketserver
import os
import sys
from urllib.parse import urlparse, unquote

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "landing")
STANDALONE = os.path.join(HERE, "GTMCat Landing (standalone).html")
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8080


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=ROOT, **k)

    def do_GET(self):
        path = unquote(urlparse(self.path).path)
        if path in ("/", "/index.html"):
            return self._send_file(STANDALONE, "text/html; charset=utf-8")
        return super().do_GET()

    def _send_file(self, fs_path, ctype):
        try:
            with open(fs_path, "rb") as f:
                data = f.read()
        except OSError:
            self.send_error(404, "Not found")
            return
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def translate_path(self, path):
        p = unquote(urlparse(path).path)
        fs = os.path.normpath(os.path.join(ROOT, p.lstrip("/")))
        if (not os.path.splitext(p)[1]
                and not os.path.isdir(fs)
                and os.path.isfile(fs + ".html")):
            p += ".html"
        return super().translate_path(p)


class Server(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True


with Server(("127.0.0.1", PORT), Handler) as httpd:
    print(f"GTMCat preview running at  http://localhost:{PORT}/")
    print(f"  /          -> {os.path.basename(STANDALONE)}")
    print(f"  /pricing /privacy /support /terms /refunds -> landing/*.html")
    print("Ctrl+C (or stop the task) to quit.")
    httpd.serve_forever()
