# Claude Code prompt — DSA study site

Copy everything below the `---` line into Claude Code, opened with this folder (`Data Structure & Algorithm/`) as the working directory.

---

# DSA Study Site — Astro migration

I have a single-file HTML study tool for data structures and algorithms (`DSA_Reference_Catalog.html`, ~200KB). It has 92 catalog entries, 459 LeetCode problems mapped in, a progress dashboard, and three curated-list flags (Grind 75, Blind 75, NeetCode 150). I want to migrate it to a sustainable, content-first Astro site that I run locally and (later) host on a free static host.

## Constraints

- Static site only — no backend, no database. Data lives in JSON files committed to git.
- Progress lives in browser `localStorage`. I'll sync the project folder itself via iCloud Drive; per-device progress doesn't have to merge automatically, but JSON export/import must work and so must auto-save to a folder I pick (File System Access API where available — gracefully degrade where not).
- Must run locally with `npm run dev`. Must also build to a `dist/` folder I can open in a browser without a server.
- Easy to extend with a parallel **system design** content collection later — same architecture, different content.

## Tech stack

- **Astro 4+** with TypeScript strict
- **Content Collections** for catalog entries (one entry = one MDX file, frontmatter has metadata, body is study notes)
- **Tailwind CSS** for styling (replace inline CSS from the current HTML)
- **React** islands for the interactive bits only (filters, dashboard, progress checkboxes)
- **Vitest** for unit tests
- **Pagefind** for static full-text search (built at the end of `npm run build`)
- **prettier** + **eslint** with the recommended Astro/TS configs

## Source data (already in this folder under `data/`)

- `data/dsa_enriched.json` — the 92 catalog entries, each with `name`, `kind`, `category`, `definition`, `time`, `space`, `techniques`, `wikipedia`, `resources`, `sean_prashad`, `grind75` (topic-level flag), `notes`, and a `leetcode` array of 3-7 problems with `{id, title, slug, difficulty, ac_rate, premium, url, grind75, blind75, neetcode150}`.
- `data/dsa_data.py` — the original Python source-of-truth before LeetCode mapping. Use this if you need to regenerate `dsa_enriched.json` from scratch.
- `data/leetcode_tags2.json` — raw LeetCode tag → problems data scraped from LeetCode GraphQL on 2026-05-27.
- `data/grind75_slugs.json` — 75 LeetCode title-slugs.
- `data/blind75_slugs.json` — 75 slugs.
- `data/neetcode150_slugs.json` — 148 slugs.
- `data/map_leetcode.py` and `data/add_badges.py` — Python scripts that produced `dsa_enriched.json`. Re-implement in TypeScript so I can run the whole pipeline with Node, no Python required.

The current HTML is `DSA_Reference_Catalog.html` and the spreadsheet is `DSA_Reference_Catalog.xlsx` — keep both for reference but neither needs to be touched.

## Project structure (target)

```
.
├── README.md
├── astro.config.mjs
├── package.json
├── tsconfig.json
├── tailwind.config.mjs
├── data/                          # source data (committed)
│   ├── dsa_enriched.json
│   ├── grind75_slugs.json
│   ├── blind75_slugs.json
│   └── neetcode150_slugs.json
├── scripts/
│   ├── refresh-leetcode.ts        # re-fetch LC problem metadata
│   ├── refresh-curated-lists.ts   # re-fetch G75/B75/NC150
│   └── build-content.ts           # turn dsa_enriched.json into src/content/dsa/*.mdx
├── src/
│   ├── content/
│   │   ├── config.ts              # content collection schema (zod)
│   │   ├── dsa/                   # one .mdx per catalog entry, generated + hand-editable
│   │   │   ├── array.mdx
│   │   │   ├── binary-search.mdx
│   │   │   └── ...
│   │   └── system-design/         # placeholder for later
│   ├── layouts/
│   │   └── Base.astro
│   ├── pages/
│   │   ├── index.astro            # landing
│   │   ├── catalog.astro          # filterable list (uses CatalogIsland)
│   │   ├── dashboard.astro        # progress aggregates (uses DashboardIsland)
│   │   ├── about.astro            # sources + how-to-use
│   │   └── dsa/[slug].astro       # per-entry detail page with LC problems + checkboxes
│   ├── components/
│   │   ├── EntryCard.astro
│   │   ├── ProblemRow.tsx         # React island with progress checkbox
│   │   ├── CatalogIsland.tsx      # React island with filters
│   │   └── DashboardIsland.tsx
│   ├── lib/
│   │   ├── progress.ts            # localStorage + File System Access wrapper
│   │   ├── data.ts                # helpers to load and query catalog data
│   │   └── types.ts               # shared types
│   └── styles/global.css
└── tests/
    ├── data.test.ts
    └── progress.test.ts
```

## Pages

1. **Home (`/`)** — short intro, "What's in here," 3 stat cards (topics, problems, currently completed), and three CTAs: Catalog, Dashboard, About.
2. **Catalog (`/catalog`)** — filterable list (search box; Kind; Category; Sean Prashad Yes/No; Grind 75 Yes/No; Progress not-started/in-progress/done; Curated list G75/B75/NC150/any). Each row links to `/dsa/<slug>` and shows a tiny progress bar. This is a React island so filters work without a page reload.
3. **Per-entry (`/dsa/<slug>`)** — full detail: definition, complexity, techniques, links to Wikipedia + resources, list of LeetCode problems with checkboxes (per-problem progress), and a "Personal notes" section sourced from the MDX body. Page is mostly static; only the problem checkboxes are an island.
4. **Dashboard (`/dashboard`)** — overall progress bar, by-difficulty (Easy/Medium/Hard), by-category, by-curated-list (G75/B75/NC150). Recently completed feed. Day streak. Import/Export/Reset buttons. Everything is a single React island.
5. **About (`/about`)** — sources used (Sean Prashad, Grind 75, NeetCode, TIH cheatsheet), data refresh date, license, how progress storage works.

## Content collection schema

```ts
// src/content/config.ts
import { defineCollection, z } from 'astro:content';

const dsa = defineCollection({
  type: 'content',  // MDX
  schema: z.object({
    name: z.string(),
    slug: z.string(),
    kind: z.enum(['Data Structure', 'Algorithm', 'Technique', 'Paradigm']),
    category: z.string(),
    definition: z.string(),
    time: z.string(),
    space: z.string(),
    techniques: z.string(),
    wikipedia: z.string().url(),
    resources: z.array(z.string().url()),
    sean_prashad: z.boolean(),
    grind75_topic: z.boolean(),
    notes: z.string().optional(),
    leetcode: z.array(z.object({
      id: z.string(),
      title: z.string(),
      slug: z.string(),
      difficulty: z.enum(['Easy', 'Medium', 'Hard']),
      ac_rate: z.number(),
      premium: z.boolean(),
      url: z.string().url(),
      grind75: z.boolean(),
      blind75: z.boolean(),
      neetcode150: z.boolean(),
    })),
  }),
});

export const collections = { dsa };
```

## Data pipeline

`scripts/build-content.ts` reads `data/dsa_enriched.json` and emits one MDX file per entry into `src/content/dsa/<slug>.mdx`. The body of each MDX is empty by default (just a `## My notes` heading) so I can fill it in as I study. If an MDX file already exists with body content, **preserve the body** and only update the frontmatter — never overwrite my notes.

`scripts/refresh-leetcode.ts` is a TypeScript port of `data/map_leetcode.py` + the GraphQL scrape logic. It hits `https://leetcode.com/graphql/` with the same query I used in the chrome session (see `data/leetcode_tags2.json` for an example of the output shape) and rebuilds `data/dsa_enriched.json`. Add a `package.json` script: `npm run refresh:leetcode`. Document in README that this requires no auth — LeetCode's problemsetQuestionList endpoint is public.

`scripts/refresh-curated-lists.ts` fetches:
- Grind 75 from `https://www.techinterviewhandbook.org/grind75/` (parse the rendered HTML — it lists LeetCode URLs in `<a href>` attributes)
- Blind 75 and NeetCode 150 from `https://raw.githubusercontent.com/neetcode-gh/leetcode/main/.problemSiteData.json` (read `blind75` / `neetcode150` boolean fields)

Then it rewrites `data/grind75_slugs.json`, `data/blind75_slugs.json`, `data/neetcode150_slugs.json`.

## Progress storage (`src/lib/progress.ts`)

API:
```ts
type Progress = Record<string, { done: true; at: number }>;
function load(): Progress
function save(p: Progress): void
function toggle(problemId: string): void
function exportJson(): string                  // returns the JSON string for download
function importJson(json: string): void        // merges into current
function reset(): void
async function chooseSyncFile(): Promise<void> // File System Access API — picks a JSON file in iCloud
async function syncToFile(): Promise<void>     // writes current localStorage state to the chosen file
async function loadFromFile(): Promise<void>   // reads the file and merges
```

The File System Access API works in Chromium browsers. In Safari/Firefox, the "choose sync file" button is hidden and only import/export is exposed. Use `'showOpenFilePicker' in window` to feature-detect.

When the user has chosen a sync file:
- Auto-save to it after every progress change (debounced 1s)
- On page load, read it and merge (file wins on conflict)
- Show a small "Synced to ~/path/to/file.json" status

## Styling

Convert the existing CSS (look at `DSA_Reference_Catalog.html` for the color palette and component styles) to Tailwind utility classes. Keep the same visual language: rounded cards, blue (#2f5597) header accents, green/yellow/red difficulty pills, green/blue/purple curated-list badges.

Light mode only for now. Use `color-scheme: light` so the OS doesn't force dark.

## Testing

- `tests/data.test.ts` — load `data/dsa_enriched.json`, verify shape matches the schema, no duplicate slugs, every LeetCode URL is well-formed.
- `tests/progress.test.ts` — round-trip export/import, toggle behavior, JSON shape stable.
- Add `npm test` script.

## Local run

- `npm install`
- `npm run build:content` (one-time, generates the MDX files)
- `npm run dev` — Astro dev server at http://localhost:4321
- `npm run build` — produces `dist/`; can be opened directly OR served by any static host
- `npm test`
- `npm run refresh:leetcode` to refresh problem data
- `npm run refresh:curated-lists` to refresh G75/B75/NC150

## Hosting (document in README, don't deploy)

The `dist/` folder is fully static. Three documented options in README:
1. **Open `dist/index.html` directly** — works for read-only review, but `localStorage` and File System Access don't always behave when opened via `file://` URLs. Recommend `npx serve dist` instead.
2. **Local dev server** — `npm run preview` after a build, or `npm run dev` during work.
3. **Free static hosting later** — `dist/` can drop into Cloudflare Pages, GitHub Pages, Netlify, or Vercel. README has a 5-line section per option.

## Acceptance checklist

- [ ] `npm install && npm run build:content && npm run dev` starts a working site in under a minute on a fresh clone.
- [ ] All 92 entries render at `/dsa/<slug>`.
- [ ] Catalog filters work without page reloads.
- [ ] Checking a problem on a per-entry page updates the dashboard when I navigate to it.
- [ ] Progress survives a page reload.
- [ ] Export, then Reset, then Import → same state.
- [ ] `npm test` passes.
- [ ] `npm run build` produces a `dist/` under 5 MB total (no source maps, no Wikipedia data bundled).
- [ ] README has setup, dev commands, data-refresh commands, and hosting options.
- [ ] No system-design content yet, but the `src/content/system-design/` folder exists with a `README.md` placeholder so the structure is obvious for a later pass.

## Out of scope

- Authentication, accounts, cloud sync. localStorage + optional sync-file is enough.
- A backend.
- Deployment automation (CI/CD). Just document the build command.
- System-design content itself — only the folder.

Once you finish, briefly summarize: file count, total `dist/` size, and how to run.
