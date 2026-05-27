# DSA Reference Catalog

A local study site for data structures, algorithms, and the LeetCode problems that exercise them.

- **92 catalog entries** (data structures, algorithms, techniques, paradigms)
- **486 LeetCode problems** mapped to entries, with Grind 75 / Blind 75 / NeetCode 150 badges
- **Progress dashboard** with by-difficulty, by-category, and by-curated-list breakdowns
- Progress imported from your Sean Prashad account (last updated 2026-05-27)

## How to run

**Easiest:** double-click `DSA Catalog.app` in this folder. (If macOS refuses, see `DEBUG_APP_PROMPT.md` for diagnostics — or just use the Terminal version below.)

**Terminal:**

```
cd "/Users/user/Documents/Claude/Projects/Data Structure & Algorithm"
python3 serve.py
```

The browser opens at http://localhost:8765/. Stop with Ctrl-C (or quit from the Dock).

## Where progress lives

When the server is running, every checkbox click writes to `progress.json` in this folder. Since this folder is under Documents (which iCloud syncs by default), `progress.json` syncs across your Macs.

If you open `DSA_Reference_Catalog.html` directly (without the server), progress falls back to the browser's localStorage. The Sync & backup buttons on the Dashboard tab handle export/import as JSON either way.

## Folder layout

```
.
├── DSA Catalog.app/              double-click to launch (Mac app bundle)
├── DSA_Reference_Catalog.html    the site itself
├── DSA_Reference_Catalog.xlsx    same data in a spreadsheet
├── README.md                     this file
├── CLAUDE_CODE_PROMPT.md         future: Astro migration prompt
├── DEBUG_APP_PROMPT.md           prompt to debug the .app if it stops working
├── progress.json                 your progress (auto-created)
├── serve.py                      local web server (~120 lines, stdlib only)
├── start.command                 Terminal-style alternate launcher
│
├── data/                         JSON inputs to the build pipeline
│   ├── dsa_enriched.json         master dataset: 92 entries + 486 problems with all flags
│   ├── leetcode_tags2.json       raw LeetCode tag → problems data from GraphQL (2026-05-27)
│   ├── grind75_slugs.json        Grind 75 problem slugs
│   ├── blind75_slugs.json        Blind 75 problem slugs
│   ├── neetcode150_slugs.json    NeetCode 150 problem slugs
│   └── sean_prashad_done.json    your 56 completed problems from seanprashad.com
│
└── scripts/                      Python scripts that built everything
    ├── dsa_data.py               source-of-truth Python definition of the 92 catalog entries
    ├── map_leetcode.py           assigns 5 canonical LeetCode problems per entry
    ├── add_badges.py             adds Grind 75 / Blind 75 / NeetCode 150 flags
    ├── augment_with_progress.py  imports Sean Prashad progress and adds missing problems
    ├── build_xlsx_v2.py          builds DSA_Reference_Catalog.xlsx
    ├── build_html_v2.py          builds DSA_Reference_Catalog.html
    └── build_app.py              builds DSA Catalog.app
```

## Refreshing or rebuilding things

Each script in `scripts/` is independently runnable with `python3`. Note that several read `data/` via paths relative to their own location, so cd into `scripts/` first or run with full paths.

- **Rebuild the HTML or Excel** after editing the dataset:
  ```
  python3 scripts/build_html_v2.py "DSA_Reference_Catalog.html"
  python3 scripts/build_xlsx_v2.py "DSA_Reference_Catalog.xlsx"
  ```
- **Rebuild the .app icon / bundle:**
  ```
  python3 scripts/build_app.py
  ```
  (Requires Pillow: `pip3 install pillow`.)
- **Refresh LeetCode data** is a bigger job — the `leetcode_tags2.json` fetch used the LeetCode GraphQL endpoint via Chrome. The Astro migration described in `CLAUDE_CODE_PROMPT.md` includes a TypeScript port that does it directly from Node without needing a browser.

## First time the .app refuses to open

macOS protects unsigned local apps. Most common fix:

```bash
xattr -dr com.apple.quarantine "DSA Catalog.app"
chmod +x "DSA Catalog.app/Contents/MacOS/launcher"
```

If it still misbehaves, the launcher logs every step to `~/Library/Logs/DSA-Catalog.log`. See `DEBUG_APP_PROMPT.md` for a structured debugging walkthrough you can paste into Claude Code.

## Sources used to build the catalog

- Sean Prashad's [LeetCode Patterns](https://seanprashad.com/leetcode-patterns/) — technique cheatsheet + the 178-problem list
- [Grind 75](https://www.techinterviewhandbook.org/grind75/) — the 15-category default list
- NeetCode's [problemSiteData](https://github.com/neetcode-gh/leetcode/blob/main/.problemSiteData.json) — authoritative source for Blind 75 and NeetCode 150 membership
- [Tech Interview Handbook study cheatsheets](https://www.techinterviewhandbook.org/algorithms/study-cheatsheet/) — category definitions
- LeetCode GraphQL API — problem metadata (title, ID, difficulty, acceptance rate, premium flag) fetched 2026-05-27
