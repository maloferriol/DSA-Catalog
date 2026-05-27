"""Build the v2 HTML with LeetCode problems + progress dashboard."""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

DATA = json.load(open(os.path.join(os.path.dirname(__file__), 'dsa_enriched.json')))
OUT = sys.argv[1] if len(sys.argv) > 1 else "DSA_Reference_Catalog.html"

json_blob = json.dumps(DATA, ensure_ascii=False)

HTML = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>DSA Reference Catalog</title>
<style>
:root { color-scheme: light; }
* { box-sizing: border-box; }
body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  background: #f7f7f8; color: #1f2328; line-height: 1.5;
}
.container { max-width: 1400px; margin: 0 auto; padding: 24px 20px 80px; }
header h1 { margin: 0 0 4px 0; font-size: 26px; font-weight: 700; }
header p.sub { margin: 0 0 18px 0; color: #5a6471; font-size: 14px; }

/* Tabs */
.tabs { display: flex; gap: 4px; border-bottom: 2px solid #e1e4e8; margin-bottom: 20px; }
.tab { padding: 10px 18px; background: transparent; border: none; border-bottom: 2px solid transparent; margin-bottom: -2px; cursor: pointer; font-size: 14px; font-weight: 500; color: #57606a; }
.tab.active { color: #2f5597; border-bottom-color: #2f5597; }
.tab:hover:not(.active) { color: #2f5597; background: #f0f4f8; }
.view { display: none; }
.view.active { display: block; }

/* Stats cards */
.stats { display: flex; flex-wrap: wrap; gap: 12px; margin: 0 0 18px 0; }
.stat { background: #ffffff; border: 1px solid #e1e4e8; border-radius: 8px; padding: 12px 16px; font-size: 13px; min-width: 130px; }
.stat strong { display:block; font-size: 22px; color: #2f5597; line-height: 1.2; margin-bottom: 2px; }
.stat .label { color: #57606a; }

/* Toolbar */
.toolbar { display: flex; flex-wrap: wrap; gap: 10px; align-items: flex-end; background: #ffffff; border: 1px solid #e1e4e8; border-radius: 10px; padding: 12px 14px; margin-bottom: 14px; }
.toolbar label { font-size: 12px; color: #57606a; display: flex; flex-direction: column; gap: 4px; }
.toolbar select, .toolbar input[type=text] { font-size: 13px; padding: 6px 8px; border: 1px solid #d0d7de; border-radius: 6px; background: #fff; color: #1f2328; min-width: 140px; }
.toolbar input[type=text] { min-width: 220px; }
.toolbar button { font-size: 13px; padding: 7px 12px; border: 1px solid #d0d7de; border-radius: 6px; background: #f6f8fa; cursor: pointer; }
.toolbar button:hover { background: #eaeef2; }
.toolbar button.primary { background: #2f5597; color: white; border-color: #234478; }
.toolbar button.primary:hover { background: #234478; }

/* Catalog list */
.entry { background: #fff; border: 1px solid #e1e4e8; border-radius: 8px; margin-bottom: 10px; overflow: hidden; }
.entry-header { padding: 12px 16px; cursor: pointer; display: flex; align-items: center; gap: 12px; flex-wrap: wrap; }
.entry-header:hover { background: #fafbfc; }
.entry-header h3 { margin: 0; font-size: 15px; font-weight: 600; flex: 1 1 auto; min-width: 180px; }
.entry-progress { font-size: 12px; color: #57606a; }
.entry-progress .bar { display: inline-block; width: 80px; height: 6px; background: #e1e4e8; border-radius: 3px; overflow: hidden; vertical-align: middle; margin: 0 6px; }
.entry-progress .fill { height: 100%; background: #28a745; transition: width 0.2s; }

.entry-body { padding: 0 16px 16px 16px; border-top: 1px solid #f0f3f6; display: none; background: #fafbfc; }
.entry.expanded .entry-body { display: block; }
.entry-body .definition { font-size: 14px; margin: 12px 0; }
.entry-meta { display: flex; flex-wrap: wrap; gap: 14px; margin: 8px 0; font-size: 12px; }
.entry-meta > div { background: #fff; padding: 6px 10px; border-radius: 4px; border: 1px solid #e1e4e8; }
.entry-meta .label { color: #6a737d; font-size: 10px; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 2px; }

.lc-list { margin-top: 10px; }
.lc-list h4 { margin: 8px 0; font-size: 13px; color: #57606a; text-transform: uppercase; letter-spacing: 0.5px; }
.lc-row { display: flex; align-items: center; gap: 10px; padding: 8px 10px; background: #fff; border-radius: 6px; margin-bottom: 4px; border: 1px solid #e1e4e8; font-size: 13px; }
.lc-row.done { background: #f0fdf4; border-color: #bbf7d0; }
.lc-row input[type=checkbox] { width: 18px; height: 18px; cursor: pointer; accent-color: #28a745; }
.lc-row .pid { font-family: ui-monospace, "SF Mono", Menlo, monospace; color: #57606a; font-size: 12px; min-width: 50px; }
.lc-row .title { flex: 1 1 auto; }
.lc-row.done .title { text-decoration: line-through; color: #6a737d; }
.lc-row .diff { padding: 1px 8px; border-radius: 10px; font-size: 11px; font-weight: 600; }
.diff-Easy { background: #d4edda; color: #155724; }
.diff-Medium { background: #fff3cd; color: #856404; }
.diff-Hard { background: #f8d7da; color: #721c24; }
.lc-row .ac { font-size: 11px; color: #6a737d; min-width: 36px; text-align: right; }
.lc-row .premium { font-size: 11px; color: #b45309; background: #fef3c7; padding: 1px 6px; border-radius: 8px; }
.lc-badge { font-size: 10px; font-weight: 700; padding: 1px 6px; border-radius: 8px; letter-spacing: 0.3px; }
.badge-g75 { background: #c6f6d5; color: #22543d; }
.badge-b75 { background: #bee3f8; color: #2c5282; }
.badge-nc150 { background: #e9d8fd; color: #553c9a; }
.lc-row a { color: #0969da; text-decoration: none; }
.lc-row a:hover { text-decoration: underline; }

.pill { display: inline-block; padding: 2px 8px; border-radius: 10px; font-size: 11px; font-weight: 600; }
.pill-yes { background: #d4edda; color: #155724; }
.pill-no { background: #fff3cd; color: #856404; }
.kind-pill { display: inline-block; padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: 600; }
.kind-ds { background: #d9e1f2; color: #1f3864; }
.kind-algo { background: #fce4d6; color: #843c0c; }
.kind-tech { background: #e2efda; color: #375623; }
.kind-para { background: #fff2cc; color: #7f5f00; }

/* Dashboard */
.dash-section { background: #fff; border: 1px solid #e1e4e8; border-radius: 10px; padding: 18px; margin-bottom: 16px; }
.dash-section h3 { margin: 0 0 14px 0; font-size: 15px; }
.bar-row { display: grid; grid-template-columns: 180px 1fr 100px; gap: 12px; align-items: center; padding: 6px 0; font-size: 13px; }
.bar-row .label { color: #1f2328; }
.bar-track { background: #e1e4e8; border-radius: 4px; height: 18px; overflow: hidden; position: relative; }
.bar-fill { height: 100%; background: linear-gradient(90deg, #28a745, #5cb85c); transition: width 0.3s; }
.bar-fill.easy { background: linear-gradient(90deg, #28a745, #5cb85c); }
.bar-fill.medium { background: linear-gradient(90deg, #e0a800, #ffc107); }
.bar-fill.hard { background: linear-gradient(90deg, #c82333, #dc3545); }
.bar-text { position: absolute; top: 0; left: 8px; line-height: 18px; font-size: 11px; color: #1f2328; font-weight: 500; }
.bar-row .pct { font-family: ui-monospace, "SF Mono", Menlo, monospace; font-size: 12px; color: #57606a; text-align: right; }

.recent { font-size: 13px; }
.recent .row { display: flex; gap: 10px; align-items: center; padding: 6px 0; border-bottom: 1px solid #f0f3f6; }
.recent .row:last-child { border-bottom: none; }
.recent .when { color: #6a737d; font-size: 12px; min-width: 130px; }

.legend { display: flex; flex-wrap: wrap; gap: 14px; margin: 4px 0 14px 0; font-size: 12px; color: #57606a; }
.legend .swatch { display:inline-block; width:14px; height:14px; border-radius: 3px; vertical-align: middle; margin-right: 4px;}

footer { margin-top: 30px; font-size: 12px; color: #6a737d; line-height: 1.6; }
footer a { color: #0969da; text-decoration: none; }
footer a:hover { text-decoration: underline; }
.muted { color: #6a737d; }
.flex { display: flex; gap: 10px; align-items: center; flex-wrap: wrap; }
.spacer { flex: 1 1 auto; }
.danger { color: #c53030; }
</style>
</head>
<body>
<div class="container">
<header>
  <h1>Data Structures &amp; Algorithms — Reference Catalog</h1>
  <p class="sub">Search, filter, learn, track. 92 topics · 459 LeetCode problems · Progress saved in your browser.</p>
</header>

<div class="tabs">
  <button class="tab active" data-view="catalog">Catalog</button>
  <button class="tab" data-view="dashboard">Dashboard</button>
</div>

<!-- ========== CATALOG VIEW ========== -->
<div class="view active" id="view-catalog">
  <div class="stats" id="stats"></div>
  <div class="legend">
    <span><span class="swatch" style="background:#d9e1f2"></span>Data Structure</span>
    <span><span class="swatch" style="background:#fce4d6"></span>Algorithm</span>
    <span><span class="swatch" style="background:#e2efda"></span>Technique</span>
    <span><span class="swatch" style="background:#fff2cc"></span>Paradigm</span>
    <span><span class="swatch diff-Easy" style="background:#d4edda"></span>Easy</span>
    <span><span class="swatch diff-Medium" style="background:#fff3cd"></span>Medium</span>
    <span><span class="swatch diff-Hard" style="background:#f8d7da"></span>Hard</span>
    <span><span class="lc-badge badge-g75">G75</span> Grind 75</span>
    <span><span class="lc-badge badge-b75">B75</span> Blind 75</span>
    <span><span class="lc-badge badge-nc150">NC150</span> NeetCode 150</span>
  </div>

  <div class="toolbar">
    <label>Search<input type="text" id="search" placeholder="e.g. tree, dijkstra, sliding window" /></label>
    <label>Kind<select id="kind"><option value="">All</option></select></label>
    <label>Category<select id="category"><option value="">All</option></select></label>
    <label>Sean Prashad<select id="sp"><option value="">All</option><option value="Yes">Covered</option><option value="No">Not covered</option></select></label>
    <label>Grind 75<select id="gr"><option value="">All</option><option value="Yes">Covered</option><option value="No">Not covered</option></select></label>
    <label>Progress<select id="prog"><option value="">All</option><option value="not-started">Not started</option><option value="in-progress">In progress</option><option value="done">Complete</option></select></label>
    <label>Curated list<select id="curated"><option value="">All</option><option value="grind75">Grind 75</option><option value="blind75">Blind 75</option><option value="neetcode150">NeetCode 150</option><option value="any">In any list</option></select></label>
    <div class="spacer"></div>
    <button id="reset">Reset</button>
    <button id="expand-all">Expand all</button>
    <button id="collapse-all">Collapse all</button>
  </div>

  <div id="entry-list"></div>
</div>

<!-- ========== DASHBOARD VIEW ========== -->
<div class="view" id="view-dashboard">
  <div class="stats" id="dash-stats"></div>

  <div class="dash-section">
    <h3>Overall progress</h3>
    <div class="bar-row">
      <span class="label">All problems</span>
      <div class="bar-track"><div class="bar-fill" id="overall-bar" style="width:0%"></div><div class="bar-text" id="overall-text">0 / 0</div></div>
      <span class="pct" id="overall-pct">0%</span>
    </div>
  </div>

  <div class="dash-section">
    <h3>By difficulty</h3>
    <div id="difficulty-bars"></div>
  </div>

  <div class="dash-section">
    <h3>By curated list</h3>
    <p class="muted" style="margin-top:0;font-size:12px;">Of the problems mapped into the catalog, this is how many are also in each well-known list — and how many you've completed. Doing the curated list completes most of the catalog at the same time.</p>
    <div id="curated-bars"></div>
  </div>

  <div class="dash-section">
    <h3>By category</h3>
    <div id="category-bars"></div>
  </div>

  <div class="dash-section">
    <h3>Recently completed</h3>
    <div class="recent" id="recent"></div>
  </div>

  <div class="dash-section">
    <h3>Sync &amp; backup</h3>
    <p class="muted" style="margin-top:0;">When you run <code>python3 serve.py</code>, progress saves to <code>progress.json</code> in this folder (iCloud handles cross-device sync). When opened directly as a file, progress lives in this browser's localStorage. Use export/import to back up either way.</p>
    <div class="flex">
      <button class="primary" id="export-progress">Export progress (JSON)</button>
      <button id="import-progress">Import progress…</button>
      <input type="file" id="import-file" accept="application/json" style="display:none" />
      <button class="danger" id="reset-progress" style="margin-left:auto;color:#c53030;">Reset all progress…</button>
    </div>
  </div>
</div>

<footer>
  <p><strong>Sources:</strong>
    <a href="https://seanprashad.com/leetcode-patterns/" target="_blank" rel="noopener">Sean Prashad — LeetCode Patterns</a> ·
    <a href="https://www.techinterviewhandbook.org/grind75/" target="_blank" rel="noopener">Grind 75</a> ·
    <a href="https://www.techinterviewhandbook.org/algorithms/study-cheatsheet/" target="_blank" rel="noopener">TIH Study Cheatsheet</a> ·
    LeetCode data fetched via GraphQL on 2026-05-27.
  </p>
</footer>
</div>

<script>
const DATA = __DATA_JSON__;
const STORAGE_KEY = "dsa_progress_v1";

// ---- Progress store ----
// Server-aware: when this page is served from the local Python server, progress
// is read from and written to progress.json on disk (so iCloud can sync it).
// When opened directly as a file://, falls back to localStorage.
let SERVER_MODE = false;
let saveTimer = null;

function loadFromLocalStorage() {
  try { return JSON.parse(localStorage.getItem(STORAGE_KEY)) || {}; }
  catch(e) { return {}; }
}
function saveToLocalStorage(p) {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(p));
}
function saveProgress(p) {
  saveToLocalStorage(p);  // always keep a local copy
  if (SERVER_MODE) {
    // Debounce the network write so rapid clicks don't spam the server
    clearTimeout(saveTimer);
    saveTimer = setTimeout(() => {
      fetch('/progress.json', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(p),
      }).catch(err => console.warn('progress sync failed:', err));
    }, 300);
  }
}

let progress = loadFromLocalStorage();

async function bootstrapProgress() {
  // Detect whether we're running under the Python server. If so, fetch the
  // server's copy of progress.json and prefer it on first load.
  if (location.protocol === 'file:') return;  // opened directly, no server
  try {
    const r = await fetch('/progress.json', { cache: 'no-store' });
    if (!r.ok) return;
    const serverProgress = await r.json();
    if (typeof serverProgress !== 'object' || serverProgress === null) return;
    SERVER_MODE = true;
    // Merge: server wins on conflict, but keep any localStorage-only entries
    // (in case the user used the file:// version before)
    progress = Object.assign({}, progress, serverProgress);
    saveToLocalStorage(progress);
    showServerBadge();
    renderStats();
    renderList();
    if (document.getElementById('view-dashboard').classList.contains('active')) renderDashboard();
  } catch(e) {
    // Server not available — stay in localStorage mode
  }
}

function showServerBadge() {
  const el = document.createElement('div');
  el.style.cssText = 'position:fixed;bottom:10px;right:10px;background:#2f5597;color:#fff;padding:6px 10px;border-radius:6px;font-size:11px;font-weight:600;opacity:0.85;z-index:1000;';
  el.textContent = '● Synced to progress.json';
  el.title = 'Progress is being saved to progress.json in this folder';
  document.body.appendChild(el);
}

function toggleProblem(pid) {
  if (progress[pid]) delete progress[pid];
  else progress[pid] = { done: true, at: Date.now() };
  saveProgress(progress);
}

// ---- Populate dropdowns ----
const $kind = document.getElementById('kind');
const $cat = document.getElementById('category');
[...new Set(DATA.map(d => d.kind))].sort().forEach(k => { const o=document.createElement('option'); o.value=k;o.textContent=k;$kind.appendChild(o); });
[...new Set(DATA.map(d => d.category))].sort().forEach(k => { const o=document.createElement('option'); o.value=k;o.textContent=k;$cat.appendChild(o); });

// ---- Helpers ----
function kindPillClass(k) {
  return k==='Data Structure'?'kind-ds':k==='Algorithm'?'kind-algo':k==='Technique'?'kind-tech':'kind-para';
}
function entryProgress(e) {
  const total = e.leetcode.length;
  const done = e.leetcode.filter(p => progress[p.id]).length;
  return { total, done, pct: total ? done/total : 0 };
}

// ---- Stats ----
function renderStats() {
  const total = DATA.length;
  const sp = DATA.filter(d => d.sean_prashad).length;
  const gr = DATA.filter(d => d.grind75).length;
  const totalProblems = DATA.reduce((s,e) => s + e.leetcode.length, 0);
  const doneProblems = DATA.reduce((s,e) => s + e.leetcode.filter(p=>progress[p.id]).length, 0);
  document.getElementById('stats').innerHTML = `
    <div class="stat"><strong>${total}</strong><span class="label">topics</span></div>
    <div class="stat"><strong>${totalProblems}</strong><span class="label">LeetCode problems</span></div>
    <div class="stat"><strong>${doneProblems}</strong><span class="label">completed (${totalProblems?Math.round(100*doneProblems/totalProblems):0}%)</span></div>
    <div class="stat"><strong>${sp}</strong><span class="label">Sean Prashad covered</span></div>
    <div class="stat"><strong>${gr}</strong><span class="label">Grind 75 covered</span></div>
  `;
}

// ---- Filtering ----
function filtered() {
  const q = document.getElementById('search').value.toLowerCase().trim();
  const k = document.getElementById('kind').value;
  const c = document.getElementById('category').value;
  const sp = document.getElementById('sp').value;
  const gr = document.getElementById('gr').value;
  const pf = document.getElementById('prog').value;
  const cu = document.getElementById('curated').value;
  return DATA.filter(d => {
    if (k && d.kind !== k) return false;
    if (c && d.category !== c) return false;
    if (sp === 'Yes' && !d.sean_prashad) return false;
    if (sp === 'No' && d.sean_prashad) return false;
    if (gr === 'Yes' && !d.grind75) return false;
    if (gr === 'No' && d.grind75) return false;
    if (q) {
      const hay = (d.name+' '+d.category+' '+d.definition+' '+d.techniques+' '+d.notes+' '+d.leetcode.map(p=>p.title).join(' ')).toLowerCase();
      if (!hay.includes(q)) return false;
    }
    if (pf) {
      const pr = entryProgress(d);
      if (pf === 'not-started' && pr.done > 0) return false;
      if (pf === 'in-progress' && (pr.done === 0 || pr.done === pr.total)) return false;
      if (pf === 'done' && pr.done < pr.total) return false;
    }
    if (cu) {
      const hasMatch = d.leetcode.some(p =>
        cu === 'grind75' ? p.grind75 :
        cu === 'blind75' ? p.blind75 :
        cu === 'neetcode150' ? p.neetcode150 :
        cu === 'any' ? (p.grind75 || p.blind75 || p.neetcode150) : true
      );
      if (!hasMatch) return false;
    }
    return true;
  });
}

// ---- Render catalog list ----
function renderList() {
  const list = filtered();
  const html = list.map((e, idx) => {
    const pr = entryProgress(e);
    const pctW = Math.round(pr.pct * 100);
    return `<div class="entry" data-name="${escapeAttr(e.name)}">
      <div class="entry-header" onclick="toggleEntry(this)">
        <span class="kind-pill ${kindPillClass(e.kind)}">${e.kind}</span>
        <h3>${escapeHtml(e.name)}</h3>
        <span class="muted">${escapeHtml(e.category)}</span>
        <span class="entry-progress">${pr.done}/${pr.total}<span class="bar"><span class="fill" style="width:${pctW}%"></span></span>${pctW}%</span>
      </div>
      <div class="entry-body">
        <div class="definition">${escapeHtml(e.definition)}</div>
        <div class="entry-meta">
          <div><div class="label">Time</div>${escapeHtml(e.time)}</div>
          <div><div class="label">Space</div>${escapeHtml(e.space)}</div>
          <div><div class="label">Techniques</div>${escapeHtml(e.techniques)}</div>
          <div><div class="label">Sean Prashad</div><span class="pill ${e.sean_prashad?'pill-yes':'pill-no'}">${e.sean_prashad?'Yes':'No'}</span></div>
          <div><div class="label">Grind 75</div><span class="pill ${e.grind75?'pill-yes':'pill-no'}">${e.grind75?'Yes':'No'}</span></div>
        </div>
        <div class="muted" style="font-size:12px; margin-top:8px;"><strong>Notes:</strong> ${escapeHtml(e.notes)}</div>
        <div class="muted" style="font-size:12px; margin-top:4px;">
          <a href="${escapeAttr(e.wikipedia)}" target="_blank" rel="noopener">Wikipedia →</a>
          ${e.resources.split('|').map(s => s.trim()).filter(Boolean).map(u => `<a href="${escapeAttr(u)}" target="_blank" rel="noopener" style="margin-left:10px;">${shortUrl(u)} →</a>`).join('')}
        </div>
        <div class="lc-list">
          <h4>LeetCode practice (${e.leetcode.length})</h4>
          ${e.leetcode.map(p => {
            const done = !!progress[p.id];
            return `<div class="lc-row ${done?'done':''}" data-pid="${p.id}">
              <input type="checkbox" ${done?'checked':''} onclick="onCheck(event, '${p.id}', '${escapeAttr(e.name)}')" />
              <span class="pid">#${p.id}</span>
              <span class="title"><a href="${p.url}" target="_blank" rel="noopener">${escapeHtml(p.title)}</a></span>
              <span class="diff diff-${p.difficulty}">${p.difficulty}</span>
              <span class="ac">${p.ac_rate}%</span>
              ${p.grind75?'<span class="lc-badge badge-g75" title="In Grind 75">G75</span>':''}
              ${p.blind75?'<span class="lc-badge badge-b75" title="In Blind 75">B75</span>':''}
              ${p.neetcode150?'<span class="lc-badge badge-nc150" title="In NeetCode 150">NC150</span>':''}
              ${p.premium?'<span class="premium">PRO</span>':''}
            </div>`;
          }).join('')}
        </div>
      </div>
    </div>`;
  }).join('');
  document.getElementById('entry-list').innerHTML = html || '<div class="muted" style="padding:30px;text-align:center;">No entries match these filters.</div>';
}

function escapeHtml(s) { return String(s).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c])); }
function escapeAttr(s) { return escapeHtml(s); }
function shortUrl(u) { try { return new URL(u).hostname.replace(/^www\./,''); } catch(e) { return u; } }

window.toggleEntry = function(headerEl) {
  headerEl.parentElement.classList.toggle('expanded');
};
window.onCheck = function(ev, pid, entryName) {
  ev.stopPropagation();
  toggleProblem(pid);
  // Update only this row + the header progress for this entry — avoid full re-render
  const row = ev.target.closest('.lc-row');
  if (row) row.classList.toggle('done', !!progress[pid]);
  // Update entry header progress
  const entryDiv = ev.target.closest('.entry');
  if (entryDiv) {
    const entryData = DATA.find(e => e.name === entryName);
    if (entryData) {
      const pr = entryProgress(entryData);
      const headerProg = entryDiv.querySelector('.entry-progress');
      if (headerProg) {
        const pct = Math.round(pr.pct * 100);
        headerProg.innerHTML = `${pr.done}/${pr.total}<span class="bar"><span class="fill" style="width:${pct}%"></span></span>${pct}%`;
      }
    }
  }
  renderStats();
  if (document.getElementById('view-dashboard').classList.contains('active')) renderDashboard();
};

// ---- Dashboard ----
function renderDashboard() {
  // Stats
  const total = DATA.reduce((s,e) => s + e.leetcode.length, 0);
  const done = DATA.reduce((s,e) => s + e.leetcode.filter(p=>progress[p.id]).length, 0);
  const pct = total ? done/total : 0;
  document.getElementById('overall-bar').style.width = (pct*100) + '%';
  document.getElementById('overall-text').textContent = `${done} / ${total}`;
  document.getElementById('overall-pct').textContent = Math.round(pct*100) + '%';

  // Stats cards
  const byDiff = { Easy: {t:0,d:0}, Medium: {t:0,d:0}, Hard: {t:0,d:0} };
  DATA.forEach(e => e.leetcode.forEach(p => {
    byDiff[p.difficulty].t++;
    if (progress[p.id]) byDiff[p.difficulty].d++;
  }));
  // Streak
  const days = new Set();
  Object.values(progress).forEach(v => {
    if (v && v.at) {
      const d = new Date(v.at);
      days.add(d.toISOString().slice(0,10));
    }
  });
  const streak = computeStreak(days);
  const lastWeek = Array.from(days).filter(d => {
    const diff = (Date.now() - new Date(d).getTime()) / 86400000;
    return diff <= 7;
  }).length;

  document.getElementById('dash-stats').innerHTML = `
    <div class="stat"><strong>${done}</strong><span class="label">problems done</span></div>
    <div class="stat"><strong>${Math.round(pct*100)}%</strong><span class="label">of catalog</span></div>
    <div class="stat"><strong>${streak}</strong><span class="label">day streak</span></div>
    <div class="stat"><strong>${lastWeek}</strong><span class="label">active days (7d)</span></div>
    <div class="stat"><strong>${byDiff.Easy.d}/${byDiff.Easy.t}</strong><span class="label">Easy</span></div>
    <div class="stat"><strong>${byDiff.Medium.d}/${byDiff.Medium.t}</strong><span class="label">Medium</span></div>
    <div class="stat"><strong>${byDiff.Hard.d}/${byDiff.Hard.t}</strong><span class="label">Hard</span></div>
  `;

  // Difficulty bars
  document.getElementById('difficulty-bars').innerHTML = ['Easy','Medium','Hard'].map(d => {
    const { t, d: c } = byDiff[d];
    const p = t ? c/t : 0;
    const cls = d.toLowerCase();
    return `<div class="bar-row"><span class="label">${d}</span><div class="bar-track"><div class="bar-fill ${cls}" style="width:${Math.round(p*100)}%"></div><div class="bar-text">${c} / ${t}</div></div><span class="pct">${Math.round(p*100)}%</span></div>`;
  }).join('');

  // Curated list bars
  const byCurated = {
    'Grind 75': { t: 0, d: 0, cls: 'badge-g75' },
    'Blind 75': { t: 0, d: 0, cls: 'badge-b75' },
    'NeetCode 150': { t: 0, d: 0, cls: 'badge-nc150' },
  };
  DATA.forEach(e => e.leetcode.forEach(p => {
    if (p.grind75) { byCurated['Grind 75'].t++; if (progress[p.id]) byCurated['Grind 75'].d++; }
    if (p.blind75) { byCurated['Blind 75'].t++; if (progress[p.id]) byCurated['Blind 75'].d++; }
    if (p.neetcode150) { byCurated['NeetCode 150'].t++; if (progress[p.id]) byCurated['NeetCode 150'].d++; }
  }));
  document.getElementById('curated-bars').innerHTML = Object.entries(byCurated).map(([name, v]) => {
    const p = v.t ? v.d/v.t : 0;
    return `<div class="bar-row"><span class="label"><span class="lc-badge ${v.cls}">${name === 'Grind 75' ? 'G75' : name === 'Blind 75' ? 'B75' : 'NC150'}</span> ${name}</span><div class="bar-track"><div class="bar-fill" style="width:${Math.round(p*100)}%"></div><div class="bar-text">${v.d} / ${v.t}</div></div><span class="pct">${Math.round(p*100)}%</span></div>`;
  }).join('');

  // Category bars
  const byCat = {};
  DATA.forEach(e => e.leetcode.forEach(p => {
    if (!byCat[e.category]) byCat[e.category] = {t:0,d:0};
    byCat[e.category].t++;
    if (progress[p.id]) byCat[e.category].d++;
  }));
  const cats = Object.keys(byCat).sort();
  document.getElementById('category-bars').innerHTML = cats.map(c => {
    const { t, d } = byCat[c];
    const p = t ? d/t : 0;
    return `<div class="bar-row"><span class="label">${escapeHtml(c)}</span><div class="bar-track"><div class="bar-fill" style="width:${Math.round(p*100)}%"></div><div class="bar-text">${d} / ${t}</div></div><span class="pct">${Math.round(p*100)}%</span></div>`;
  }).join('');

  // Recent
  const recentItems = [];
  DATA.forEach(e => e.leetcode.forEach(p => {
    if (progress[p.id] && progress[p.id].at) {
      recentItems.push({ ...p, at: progress[p.id].at, entry: e.name });
    }
  }));
  recentItems.sort((a,b) => b.at - a.at);
  document.getElementById('recent').innerHTML = recentItems.slice(0, 12).map(r => {
    const when = relativeTime(r.at);
    return `<div class="row"><span class="when">${when}</span><span><a href="${r.url}" target="_blank" rel="noopener">#${r.id} ${escapeHtml(r.title)}</a> <span class="diff diff-${r.difficulty}">${r.difficulty}</span> <span class="muted">— ${escapeHtml(r.entry)}</span></span></div>`;
  }).join('') || '<div class="muted">No completed problems yet.</div>';
}

function computeStreak(days) {
  if (days.size === 0) return 0;
  let streak = 0;
  const today = new Date(); today.setHours(0,0,0,0);
  for (let i = 0; i < 365; i++) {
    const d = new Date(today); d.setDate(d.getDate() - i);
    const key = d.toISOString().slice(0,10);
    if (days.has(key)) streak++;
    else if (i > 0) break;  // gap — stop, but allow today to be empty
  }
  return streak;
}
function relativeTime(ts) {
  const diff = (Date.now() - ts) / 1000;
  if (diff < 60) return 'just now';
  if (diff < 3600) return Math.round(diff/60) + 'm ago';
  if (diff < 86400) return Math.round(diff/3600) + 'h ago';
  if (diff < 86400*7) return Math.round(diff/86400) + 'd ago';
  return new Date(ts).toLocaleDateString();
}

// ---- Tab switching ----
document.querySelectorAll('.tab').forEach(t => {
  t.addEventListener('click', () => {
    document.querySelectorAll('.tab').forEach(x => x.classList.remove('active'));
    document.querySelectorAll('.view').forEach(x => x.classList.remove('active'));
    t.classList.add('active');
    document.getElementById('view-' + t.dataset.view).classList.add('active');
    if (t.dataset.view === 'dashboard') renderDashboard();
    if (t.dataset.view === 'catalog') { renderList(); renderStats(); }
  });
});

// ---- Filter wiring ----
['search','kind','category','sp','gr','prog','curated'].forEach(id => {
  document.getElementById(id).addEventListener('input', renderList);
});
document.getElementById('reset').addEventListener('click', () => {
  ['search','kind','category','sp','gr','prog','curated'].forEach(id => document.getElementById(id).value = '');
  renderList();
});
document.getElementById('expand-all').addEventListener('click', () => {
  document.querySelectorAll('.entry').forEach(e => e.classList.add('expanded'));
});
document.getElementById('collapse-all').addEventListener('click', () => {
  document.querySelectorAll('.entry').forEach(e => e.classList.remove('expanded'));
});

// ---- Import/Export/Reset ----
document.getElementById('export-progress').addEventListener('click', () => {
  const blob = new Blob([JSON.stringify({ format: 'dsa-progress-v1', exported_at: new Date().toISOString(), progress }, null, 2)], {type: 'application/json'});
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url; a.download = 'dsa_progress_' + new Date().toISOString().slice(0,10) + '.json';
  document.body.appendChild(a); a.click(); a.remove();
  URL.revokeObjectURL(url);
});
document.getElementById('import-progress').addEventListener('click', () => document.getElementById('import-file').click());
document.getElementById('import-file').addEventListener('change', async (e) => {
  const f = e.target.files[0]; if (!f) return;
  try {
    const txt = await f.text();
    const obj = JSON.parse(txt);
    const incoming = obj.progress || obj;
    if (typeof incoming !== 'object') throw new Error('Bad format');
    if (confirm('Merge ' + Object.keys(incoming).length + ' entries into current progress? (Existing entries will be kept; imports add to them.)')) {
      progress = Object.assign({}, progress, incoming);
      saveProgress(progress);
      renderList(); renderStats(); renderDashboard();
      alert('Imported.');
    }
  } catch(err) { alert('Failed to import: ' + err.message); }
  e.target.value = '';
});
document.getElementById('reset-progress').addEventListener('click', () => {
  if (confirm('Reset ALL progress? This cannot be undone (unless you exported first).')) {
    progress = {};
    saveProgress(progress);
    renderList(); renderStats(); renderDashboard();
  }
});

// ---- Initial render ----
renderStats();
renderList();
bootstrapProgress();
</script>
</body>
</html>
"""

html_out = HTML.replace("__DATA_JSON__", json_blob)
with open(OUT, "w", encoding="utf-8") as f:
    f.write(html_out)
print(f"Wrote {OUT} ({len(html_out)} chars, {len(DATA)} entries, {sum(len(e['leetcode']) for e in DATA)} problems)")
