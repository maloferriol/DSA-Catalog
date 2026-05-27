#!/usr/bin/env python3
"""
Tiny local server for the DSA Reference Catalog.

Run:
    python3 serve.py

Then open http://localhost:8765/ in your browser (it auto-opens).

What it does:
- Serves DSA_Reference_Catalog.html (and any other files in this folder)
- GET  /progress.json  → returns the current progress (or {} if none)
- POST /progress.json  → overwrites progress.json with the JSON body

Progress is stored in `progress.json` next to this script. Since it's just a file
in your Documents folder, iCloud Drive will sync it across devices automatically.

Stop with Ctrl-C.
"""
import http.server
import json
import os
import socketserver
import threading
import webbrowser
from pathlib import Path

PORT = 8765
HERE = Path(__file__).parent.resolve()
PROGRESS_FILE = HERE / "progress.json"
DEFAULT_PAGE = "DSA_Reference_Catalog.html"


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(HERE), **kwargs)

    def log_message(self, fmt, *args):
        # Quieter default logging — only show requests that hit /progress.json
        # send_error also calls this with non-string args, so guard with str()
        first = str(args[0]) if args else ""
        if "/progress.json" in first:
            super().log_message(fmt, *args)

    def do_GET(self):
        if self.path.rstrip("/") in ("", "/"):
            self.path = "/" + DEFAULT_PAGE
        if self.path == "/progress.json":
            return self._serve_progress()
        return super().do_GET()

    def do_POST(self):
        if self.path == "/progress.json":
            return self._save_progress()
        self.send_error(404, "Not found")

    def _serve_progress(self):
        try:
            data = PROGRESS_FILE.read_text() if PROGRESS_FILE.exists() else "{}"
        except OSError as e:
            return self.send_error(500, f"Read failed: {e}")
        body = data.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _save_progress(self):
        length = int(self.headers.get("Content-Length") or 0)
        raw = self.rfile.read(length) if length else b"{}"
        try:
            parsed = json.loads(raw.decode("utf-8") or "{}")
            if not isinstance(parsed, dict):
                raise ValueError("expected a JSON object")
        except (ValueError, json.JSONDecodeError) as e:
            return self.send_error(400, f"Bad JSON: {e}")
        tmp = PROGRESS_FILE.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(parsed, indent=2, ensure_ascii=False))
        tmp.replace(PROGRESS_FILE)  # atomic on POSIX
        body = b'{"ok":true}'
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def main():
    if not (HERE / DEFAULT_PAGE).exists():
        print(f"⚠  {DEFAULT_PAGE} not found in {HERE}")
        print("   The server will still start, but the home page won't load.")
    if not PROGRESS_FILE.exists():
        PROGRESS_FILE.write_text("{}\n")
        print(f"Created {PROGRESS_FILE.name}")
    with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as srv:
        url = f"http://localhost:{PORT}/"
        print(f"\nDSA Reference Catalog → {url}")
        print(f"Progress file: {PROGRESS_FILE}")
        print("Press Ctrl-C to stop.\n")
        threading.Timer(0.6, lambda: webbrowser.open(url)).start()
        try:
            srv.serve_forever()
        except KeyboardInterrupt:
            print("\nBye.")


if __name__ == "__main__":
    main()
