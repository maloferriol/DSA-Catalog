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
- GET  /learn/         → renders markdown docs with client-side marked.js
- GET  /api/docs       → returns the docs index as JSON

Progress is stored in `progress.json` next to this script. Since it's just a file
in your Documents folder, iCloud Drive will sync it across devices automatically.

Stop with Ctrl-C.
"""
import http.server
import json
import os
import re
import socketserver
import threading
import webbrowser
from pathlib import Path
from urllib.parse import unquote

PORT = 8765
HERE = Path(__file__).parent.resolve()
DOCS_DIR = HERE / "docs-site" / "docs"
PROGRESS_FILE = HERE / "progress.json"
DEFAULT_PAGE = "DSA_Reference_Catalog.html"

LEARN_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — DSA Reference</title>
<link rel="icon" type="image/png" href="/favicon.png">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github.min.css">
<style>
* {{ box-sizing: border-box; }}
body {{ margin: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background: #f7f7f8; color: #24292f; }}
.top-nav {{ background: #2f5597; padding: 10px 24px; display: flex; gap: 16px; align-items: center; }}
.top-nav a {{ color: #fff; text-decoration: none; font-size: 14px; padding: 6px 14px; border-radius: 6px; }}
.top-nav a:hover {{ background: rgba(255,255,255,0.15); }}
.top-nav a.active {{ background: rgba(255,255,255,0.25); font-weight: 600; }}
.top-nav .title {{ font-weight: 700; font-size: 16px; color: #fff; margin-right: auto; }}
.layout {{ display: flex; max-width: 1400px; margin: 0 auto; min-height: calc(100vh - 48px); }}
.sidebar {{ width: 280px; padding: 20px 16px; background: #fff; border-right: 1px solid #e1e4e8; overflow-y: auto; position: sticky; top: 0; height: calc(100vh - 48px); font-size: 13px; }}
.sidebar a {{ display: block; padding: 5px 10px; color: #57606a; text-decoration: none; border-radius: 4px; margin: 1px 0; }}
.sidebar a:hover {{ background: #f0f4f8; color: #2f5597; }}
.sidebar a.active {{ background: #e8eef6; color: #2f5597; font-weight: 600; }}
.sidebar h3 {{ font-size: 11px; text-transform: uppercase; color: #8b949e; margin: 16px 0 6px 10px; letter-spacing: 0.5px; }}
.content {{ flex: 1; padding: 32px 48px; max-width: 900px; }}
.content h1 {{ font-size: 28px; border-bottom: 2px solid #2f5597; padding-bottom: 8px; }}
.content h2 {{ font-size: 20px; margin-top: 32px; color: #2f5597; }}
.content h3 {{ font-size: 16px; margin-top: 24px; }}
.content blockquote {{ border-left: 4px solid #2f5597; margin: 16px 0; padding: 8px 16px; background: #f0f4f8; color: #444; }}
.content pre {{ background: #f6f8fa; border: 1px solid #e1e4e8; border-radius: 6px; padding: 16px; overflow-x: auto; font-size: 13px; }}
.content code {{ font-family: "SF Mono", Consolas, monospace; font-size: 13px; }}
.content p code {{ background: #f0f3f6; padding: 2px 6px; border-radius: 4px; }}
.content table {{ border-collapse: collapse; width: 100%; margin: 16px 0; font-size: 13px; }}
.content th, .content td {{ border: 1px solid #d0d7de; padding: 8px 12px; text-align: left; }}
.content th {{ background: #f6f8fa; font-weight: 600; }}
.content a {{ color: #2f5597; }}
@media (max-width: 768px) {{
  .sidebar {{ display: none; }}
  .content {{ padding: 20px 16px; }}
}}
</style>
</head>
<body>
<nav class="top-nav">
  <span class="title">DSA Reference</span>
  <a href="/">Exercises</a>
  <a href="/learn/" class="active">Learn</a>
</nav>
<div class="layout">
  <aside class="sidebar" id="sidebar">{sidebar}</aside>
  <main class="content" id="content">{content}</main>
</div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/python.min.js"></script>
<script>hljs.highlightAll();</script>
</body>
</html>"""


def build_sidebar(current_path=""):
    if not DOCS_DIR.exists():
        return "<p>No docs found</p>"

    SECTION_ORDER = ["data-structures", "algorithms", "paradigms", "techniques"]
    SECTION_LABELS = {
        "data-structures": "Data Structures",
        "algorithms": "Algorithms",
        "paradigms": "Paradigms",
        "techniques": "Techniques",
    }
    html_parts = []
    for section in SECTION_ORDER:
        section_dir = DOCS_DIR / section
        if not section_dir.is_dir():
            continue
        html_parts.append(f'<h3>{SECTION_LABELS.get(section, section)}</h3>')
        for cat_dir in sorted(section_dir.iterdir()):
            if not cat_dir.is_dir():
                continue
            cat_label = cat_dir.name.replace("-", " ").title()
            for md_file in sorted(cat_dir.glob("*.md")):
                title = extract_title(md_file)
                url = f"/learn/{section}/{cat_dir.name}/{md_file.stem}"
                active = " active" if url == current_path else ""
                html_parts.append(f'<a href="{url}" class="{active}">{title}</a>')
    return "\n".join(html_parts)


def extract_title(md_path):
    text = md_path.read_text(errors="replace")
    m = re.search(r'^title:\s*"(.+?)"', text, re.MULTILINE)
    if m:
        return m.group(1)
    m = re.search(r'^#\s+(.+)', text, re.MULTILINE)
    if m:
        return m.group(1)
    return md_path.stem.replace("-", " ").title()


def render_markdown_to_html(md_text):
    lines = md_text.strip().split("\n")
    if lines and lines[0].strip() == "---":
        end = -1
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                end = i
                break
        if end > 0:
            lines = lines[end + 1:]
    body = "\n".join(lines)
    return f'<div id="md-content" style="display:none">{escape_html(body)}</div>\n' + """
<script src="https://cdnjs.cloudflare.com/ajax/libs/marked/12.0.2/marked.min.js"></script>
<script>
const raw = document.getElementById('md-content').textContent;
document.getElementById('content').innerHTML = marked.parse(raw);
hljs.highlightAll();
</script>"""


def escape_html(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(HERE), **kwargs)

    def log_message(self, fmt, *args):
        first = str(args[0]) if args else ""
        if "/progress.json" in first:
            super().log_message(fmt, *args)

    def do_GET(self):
        if self.path.rstrip("/") in ("", "/"):
            self.path = "/" + DEFAULT_PAGE
        if self.path == "/progress.json":
            return self._serve_progress()
        if self.path.startswith("/learn"):
            return self._serve_learn()
        if self.path == "/api/docs":
            return self._serve_docs_index()
        return super().do_GET()

    def _serve_learn(self):
        path = unquote(self.path)
        rel = path[len("/learn"):].strip("/")
        if not rel:
            first_doc = self._first_doc_url()
            if first_doc:
                self.send_response(302)
                self.send_header("Location", first_doc)
                self.end_headers()
                return
            rel = ""
        md_path = DOCS_DIR / (rel + ".md")
        if not md_path.exists():
            md_path = DOCS_DIR / rel / "index.md"
        if not md_path.exists():
            for d in DOCS_DIR.rglob("*.md"):
                if d.stem == rel.split("/")[-1] if "/" in rel else rel:
                    md_path = d
                    break
        if md_path.exists() and md_path.is_file():
            md_text = md_path.read_text(errors="replace")
            title = extract_title(md_path)
            sidebar = build_sidebar(path)
            content = render_markdown_to_html(md_text)
            html = LEARN_TEMPLATE.format(title=title, sidebar=sidebar, content=content)
            body = html.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        else:
            sidebar = build_sidebar(path)
            content = "<h1>Learn DSA</h1><p>Select a topic from the sidebar.</p>"
            html = LEARN_TEMPLATE.format(title="Learn", sidebar=sidebar, content=content)
            body = html.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

    def _first_doc_url(self):
        for section in ["data-structures", "algorithms", "paradigms", "techniques"]:
            section_dir = DOCS_DIR / section
            if not section_dir.is_dir():
                continue
            for cat_dir in sorted(section_dir.iterdir()):
                if not cat_dir.is_dir():
                    continue
                for md in sorted(cat_dir.glob("*.md")):
                    return f"/learn/{section}/{cat_dir.name}/{md.stem}"
        return None

    def _serve_docs_index(self):
        index = []
        for md in sorted(DOCS_DIR.rglob("*.md")):
            rel = md.relative_to(DOCS_DIR)
            title = extract_title(md)
            index.append({"path": str(rel), "title": title, "url": f"/learn/{rel.with_suffix('')}"})
        body = json.dumps(index, indent=2).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

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
        tmp.replace(PROGRESS_FILE)
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
    docs_count = len(list(DOCS_DIR.rglob("*.md"))) if DOCS_DIR.exists() else 0
    with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as srv:
        url = f"http://localhost:{PORT}/"
        print(f"\nDSA Reference Catalog → {url}")
        print(f"Learn pages: {docs_count} topics at {url}learn/")
        print(f"Progress file: {PROGRESS_FILE}")
        print("Press Ctrl-C to stop.\n")
        threading.Timer(0.6, lambda: webbrowser.open(url)).start()
        try:
            srv.serve_forever()
        except KeyboardInterrupt:
            print("\nBye.")


if __name__ == "__main__":
    main()
