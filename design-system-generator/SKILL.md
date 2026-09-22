---
name: design-system-generator
description: >
  Generates a complete, client-ready brand/design system as a single-file HTML page
  from a website URL — Viktor's repeatable client flow. Scrapes the live site for REAL brand colors & fonts (filtering WordPress/
  Gutenberg default-palette noise), grounds tone/ICP/copy, builds an elevated-but-
  recognizable single-file HTML design system (hero, logo, color, type, spacing, buttons,
  tags, stats, cards, 1-2 signature components, pricing table, callout, voice, proposal
  bridge, plus LinkedIn artifacts — banner, post footer, carousel cover — in the client's brand),
  previews it, and deploys to Netlify under a clean subdomain. Trigger when
  Viktor says: "зроби дизайн систему для [client/URL]", "design system for [URL]",
  "брендкіт по сайту", "build a brand system", "дизайн-систему для клієнта", or pastes a
  client URL and asks for a design/brand system. NOT for LinkedIn creatives (use
  infographic/linkedin-carousel) and NOT for the public free-tool version (that is the
  separate brand-style-guide-tool, deterministic, no LLM).
---

# Design System Generator

Viktor's house flow for turning a client's website into a polished, single-file HTML
design system he can show the client and grow proposals from. Two archetypes anchor the
range: an **engineering/construction brand** (charcoal + a corporate-blue accent, blueprint
character) and a **software/dev brand** (green + dev-mono, friendly-SaaS character). Prior
builds are saved locally as `<workspace>/<client>-design-system/index.html` — read
the most recent ones as gold-standard references before building.

## Output contract

A **single self-contained `index.html`** (no build step, Google Fonts via CDN), saved to
`<workspace>/<client>-design-system/index.html`, previewed locally, then deployed
to `https://<client>-design-system.netlify.app`. Plus a memory file.

---

## Step 0 — Confirm 2 forks (AskUserQuestion)

Before building, lock:
1. **Format** — default is single-file HTML page (this skill). Only branch to Figma if asked.
2. **Visual direction** — `faithful` (codify the site as-is) · `elevate` (keep base + hero
   colors recognizable, lift typography/grid/character to Tier-1 — **the usual pick**) ·
   `restyle` (new accent). Both reference builds chose **elevate**.

Skip if Viktor already stated them.

---

## Step 1 — Ground the brand (REAL data, not guesses)

Run BOTH in parallel:

**A) Narrative** — `WebFetch` the URL for: what they do, services, value prop, ICP/target,
tone of voice, key headlines + real copy quotes, proof/stats, differentiators.

**B) Real colors & fonts** — pull the live CSS and rank by frequency:
```bash
cd /tmp && curl -sL "<URL>" -o site.html
grep -oiE '#[0-9a-f]{6}|#[0-9a-f]{3}\b' site.html | tr 'A-Z' 'a-z' | sort | uniq -c | sort -rn | head -25
grep -oiE 'rgba?\([0-9, .]+\)' site.html | sort | uniq -c | sort -rn | head -12
grep -oiE 'family=[A-Za-z+]+' site.html | sort -u            # Google Fonts = most reliable
grep -oiE '<link[^>]+stylesheet[^>]*>' site.html | grep -oiE 'href="[^"]+"' | head
```
If colors are sparse inline (common on builder/WordPress sites), the brand colors live in
external CSS — `curl` the top linked stylesheet(s) and grep those too.

**Critical: filter WordPress/Gutenberg default-palette noise.** These hexes are theme
defaults, NOT brand: `#0693e3 #00d084 #ff6900 #fcb900 #ff6900 #cf2e2e #9b51e0 #ab1dfe
#7bdcb5 #8ed1fc #f78da7 #fcb900 #abb8c3 #eee #ddd #313131 #32373c`. See
`reference/brand-extraction.md` for the full noise list + classification heuristic
(accent vs ink vs neutral). Keep only the high-frequency custom hexes.

State your read back to Viktor: "base = X, hero accent = Y, rest = WP noise."

---

## Step 2 — Design the token system

From the real colors, build a disciplined scale (see `reference/structure.md`):
- **Ink** (the dark/charcoal brand base, 4-5 steps)
- **Hero accent** (the one brand color, 5-6 steps incl. a tint + a deep hover)
- **Neutrals** (paper, lines) + **functional** (ok/warn/err, tinted toward brand hue)
- Rule: **60 / 30 / 10** — accent never dominates.

**Fonts** — pick a 3-family system with a *character* font that earns the brand's nature
(engineering brand → IBM Plex Mono for specs; dev/software brand → JetBrains Mono for the "code" feel).
Display (geometric/grotesque) + Body (Inter) + Character (mono or distinctive). Prefer the
site's real fonts when usable; otherwise pick a pairing that fits the vertical. See
`reference/structure.md` font-pairing notes.

---

## Step 3 — Build the single-file HTML

Assemble the 15-section anatomy in `reference/structure.md`. Always include: sticky TOC,
hero (with a brand-appropriate background motif — blueprint grid, dot grid, etc.),
logo/wordmark (2 backgrounds), color, type specimens, 8pt spacing, buttons, tags/badges
(stack + trust + status), stats/trust bar (real numbers from Step 1), service + case
cards, **1–2 signature components** (the client's own methodology/process — this is the
spine of future proposals), pricing/scope table, callout/quote (real positioning line),
voice & do/don't, a **next-phase proposal bridge** (2 templates A call-deck / B send +
ICP-swappable blocks — Viktor's standard proposal logic), **LinkedIn artifacts**
(profile banner 1584×396 + post footer 1080×156 + carousel cover 1080×1350, brand-token
mockups), and a **Graphic elements & icons** kit (~10 chart atoms + a line-icon set,
recolored from the `infographic` skill vocabulary) — see both recipes in
`reference/structure.md`.

Make each client visually distinct — vary motif, radius (corporate=sharper, friendly=rounder),
and signature components. Do NOT clone the previous client's layout 1:1.

Per [[feedback_white_background]]: the white-BG rule is LinkedIn-only — dark brand sections
are fine in a design-system page.

---

## Step 4 — Preview & verify

```bash
mkdir -p /tmp/<client>-ds && cp ".../<client>-design-system/index.html" /tmp/<client>-ds/index.html
# write /tmp/serve_<client>.py (SimpleHTTPRequestHandler, chdir to /tmp/<client>-ds, no-store, next free port 460X)
```
Add a `.claude/launch.json` config pointing at the `/tmp` serve script (the sandbox blocks
`--directory`; mirror existing entries). `preview_start` → `preview_resize` 1280×860 →
`preview_console_logs` (expect none) → `preview_screenshot` the hero. Use the next free
port (check existing `.claude/launch.json` entries — several are already taken).

---

## Step 5 — Deploy to Netlify

Per [[feedback_share_via_netlify]] always deploy to a normal origin, not /share:
```bash
cd ".../<client>-design-system" && export npm_config_cache="$HOME/.npm-claude"
npx --yes netlify-cli deploy --dir . --prod          # creates a random-name site
SID=$(python3 -c "import json;print(json.load(open('.netlify/state.json'))['siteId'])")
npx --yes netlify-cli api updateSite --data "{\"site_id\":\"$SID\",\"body\":{\"name\":\"<client>-design-system\"}}"
curl -s -o /dev/null -w '%{http_code}\n' "https://<client>-design-system.netlify.app/"   # expect 200
```
`updateSite` needs the real UUID `site_id` from `.netlify/state.json` — the subdomain alone
404s. (Per [[reference_npm_cache_root_owned]] set `npm_config_cache=~/.npm-claude` for npx.)

---

## Step 6 — Save memory

Write `project_<client>_design_system.md` + a one-line MEMORY.md pointer: client one-liner,
palette hexes, fonts, signature components, file path, port, Netlify URL + site_id, and the
"next: critique proposals → 2 templates" hook. Mirror the existing client entries.

---

## Reference files
- `reference/brand-extraction.md` — WP noise list, curl/grep recipe, accent/ink/neutral heuristic
- `reference/structure.md` — 14-section anatomy, CSS-variable scaffold, font-pairing guidance
