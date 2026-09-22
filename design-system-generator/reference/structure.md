# Design-system HTML — anatomy & scaffold

## The 16-section anatomy (sticky TOC links to each)
1. **Hero** — dark brand-bg with a motif (blueprint grid for engineering, dot-grid + `</>`
   for dev, etc.), mono kicker, big display H1 with one accent word, 1-line value prop,
   mono meta row, accent bottom-border.
2. **Logo & wordmark** — the mark concept + wordmark on light AND dark box; clear-space note.
3. **Color** — grouped swatch rows (ink / accent / neutrals+functional) each with name, hex,
   usage note; close with the 60/30/10 rule line.
4. **Typography** — 3 family cards (display / body / character) + a specimen ladder
   (display 52 → heading 34 → subhead 22 → body 16 → mono label).
5. **Spacing & grid** — 8pt bar scale + radius/container/gutter note.
6. **Buttons** — primary / dark / ghost + size row. One primary per view.
7. **Tags & badges** — stack pills + trust pills + status dots.
8. **Stats / trust bar** — 4 real numbers from the site (proof that closes).
9. **Cards** — 2 service cards + 2 case-study cards (gradient cover + result metrics).
10. **Signature component(s)** — the client's OWN methodology rendered reusable (e.g. an
    N-step delivery framework; or a process pipeline + a pricing/estimate card). This is the
    spine of future proposals — make it strong.
11. **Pricing / scope table** — dark header, mono prices, zebra rows, `£X,XXX` placeholders.
12. **Callout / quote** — one real positioning line or testimonial, accent left-bar.
13. **Voice & tone** — voice chips + Do / Don't columns using the client's real copy.
14. **Next-phase bridge** — dark section: 2 proposal templates (A call-deck / B send-proposal)
    + the ICP-swappable-blocks note (swap 3 blocks: pain / case / scope-price). This is
    Viktor's standard proposal architecture — keep it consistent across clients.
15. **LinkedIn artifacts** — the brand applied to the 3 LinkedIn surfaces the client ships:
    **profile banner** (1584×396), **post footer** (1080×156), **carousel cover** (1080×1350).
    Brand-token-driven mockups so they restyle per client. See the LinkedIn-artifacts recipe below.
16. **Graphic elements & icons** — the post/carousel visual kit: ~10 Pierre-style chart atoms
    (Donut · Dot grid · Funnel · Curve · Bars · Concentric · Quadrant · Hub & spokes · Score
    ring · Timeline) + a 6-8 line-icon set, all in brand tokens. Same vocabulary as the
    `infographic` / `linkedin-carousel` skills, recolored per client. See the recipe below.

## LinkedIn artifacts (section 15) — recipe

Goal: show the client their brand living on LinkedIn, with 3 ready templates. These are
**showcase mockups** rendered at proportional (not pixel-exact) size — caption each with its
TRUE export size and note that the pixel-perfect asset is built in Figma via the `infographic`
/ `linkedin-carousel` skills. Use ONLY brand tokens (`--acc-*`, `--ink-*`, `--paper`,
`--font-display/-body/-mono`) so the whole block restyles when the palette changes.

Lay the three in a responsive grid; banner spans the full row (it's wide), footer + cover
share the second row. Each artifact sits in a bordered `.li-card` with a `<figcaption>`.

```css
.li-grid{display:grid;grid-template-columns:1fr;gap:28px}
.li-card figcaption{font-family:var(--font-mono);font-size:12px;color:var(--ink-500);margin-top:10px}
.li-art{border:1px solid var(--n-300);border-radius:10px;overflow:hidden;background:var(--white)}
.li-row2{display:grid;grid-template-columns:1.1fr 1fr;gap:28px}   /* footer + cover */
@media(max-width:760px){.li-row2{grid-template-columns:1fr}}
```

**a) Profile banner — 1584×396 (4:1).** `aspect-ratio:1584/396`. Brand-bg (dark ink with the
hero motif, OR paper for a light brand) + wordmark top-left + a one-line value prop (display)
+ accent keyline + domain/CTA bottom-right. **Keep the bottom-left ~16% clear** (avatar safe
zone on personal profiles; company-page logo sits top-left). Use `clamp()` for type so it
scales with the card.
```html
<div class="li-art" style="aspect-ratio:1584/396;position:relative;background:var(--ink-800)">
  <div style="position:absolute;inset:0;padding:clamp(18px,3.4vw,52px);display:flex;flex-direction:column;justify-content:space-between">
    <div style="font-family:var(--font-display);font-weight:800;color:var(--white);font-size:clamp(16px,2.4vw,30px)">[Client]<span style="color:var(--acc-500)">.</span></div>
    <div style="font-family:var(--font-display);font-weight:700;color:var(--white);font-size:clamp(15px,2.6vw,34px);max-width:70%;line-height:1.15">[Value prop in one line]</div>
    <div style="align-self:flex-end;font-family:var(--font-mono);color:var(--acc-500);font-size:clamp(11px,1.4vw,18px)">[client].com</div>
  </div>
</div>
```

**b) Post footer — 1080×156.** `aspect-ratio:1080/156`. The strip that ends every post:
avatar circle (accent ring) OR logo mark left + name (display) + accent role/handle **pill**
(white text — brand rule) + domain right + small brand mark. Mirror the Victor Shulga footer
(`infographic` skill `makeAuthor`/`makeWordmark`): photo lives left, mark+domain right.
```html
<div class="li-art" style="aspect-ratio:1080/156;background:var(--white);display:flex;align-items:center;justify-content:space-between;padding:0 clamp(16px,2.6vw,30px);border-top:3px solid var(--acc-500)">
  <div style="display:flex;align-items:center;gap:14px">
    <div style="width:clamp(40px,5.4vw,58px);aspect-ratio:1;border-radius:50%;border:3px solid var(--acc-500);background:var(--ink-800)"></div>
    <div>
      <div style="font-family:var(--font-display);font-weight:800;color:var(--ink-800);font-size:clamp(15px,1.9vw,22px)">[Name / Brand]</div>
      <span style="display:inline-block;margin-top:5px;background:var(--acc-500);color:var(--white);font-family:var(--font-mono);font-size:clamp(9px,1vw,12px);letter-spacing:.08em;padding:4px 10px;border-radius:7px">[ROLE / HANDLE]</span>
    </div>
  </div>
  <div style="display:flex;align-items:center;gap:10px">
    <div style="width:clamp(32px,4vw,44px);aspect-ratio:1;border-radius:11px;background:var(--acc-500)"></div>
    <span style="font-family:var(--font-mono);color:var(--acc-500);font-size:clamp(11px,1.3vw,16px)">[client].com</span>
  </div>
</div>
```
(The mark square is a placeholder — drop the client's symbol; for Viktor's own brand it's the bowtie.)

**c) Carousel cover — 1080×1350 (4:5).** `aspect-ratio:1080/1350`. Accent top bar (12px on the
real export), mono eyebrow, big display title CAPS with ONE accent word, 1-line subtitle,
`swipe →` accent, footer lockup (mark + name + handle + `1 / N`). Slides 2-N reuse body
components (cards/lists) — note that under the cover.
```html
<div class="li-art" style="aspect-ratio:1080/1350;background:var(--white);position:relative;padding:clamp(20px,4vw,46px);display:flex;flex-direction:column">
  <div style="position:absolute;top:0;left:0;right:0;height:6px;background:var(--acc-500)"></div>
  <div style="font-family:var(--font-mono);color:var(--acc-500);font-size:clamp(10px,1.5vw,15px);letter-spacing:.14em;text-transform:uppercase;margin-top:8px">[Eyebrow]</div>
  <div style="font-family:var(--font-display);font-weight:800;color:var(--ink-800);font-size:clamp(22px,5vw,54px);line-height:1.05;margin-top:auto">[BIG TITLE WITH <span style="color:var(--acc-500)">ONE ACCENT</span> WORD]</div>
  <div style="font-family:var(--font-body);color:var(--ink-500);font-size:clamp(12px,2vw,22px);margin:14px 0 auto">[One-line subtitle]</div>
  <div style="display:flex;align-items:center;justify-content:space-between">
    <div style="display:flex;align-items:center;gap:10px"><div style="width:clamp(26px,3.4vw,38px);aspect-ratio:1;border-radius:9px;background:var(--acc-500)"></div><span style="font-family:var(--font-display);font-weight:800;color:var(--ink-800);font-size:clamp(12px,1.6vw,18px)">[Name]</span></div>
    <span style="font-family:var(--font-mono);color:var(--acc-500);font-size:clamp(11px,1.4vw,16px)">swipe →</span>
  </div>
</div>
```

Caption each: `Profile banner · 1584×396`, `Post footer · 1080×156`, `Carousel cover · 1080×1350
(slides 2-N reuse body components)`. Add a one-line note under the block: "Pixel-perfect
exports built in Figma via the `infographic` / `linkedin-carousel` skills."

## Graphic elements & icons (section 16) — recipe

Goal: hand the client a **reusable visual vocabulary** so every post/carousel card gets a
real graphic, not text. These are the `infographic`-skill chart atoms (Pierre Herubel's
vocabulary, approved 2026-06-19) **recolored to the client's tokens**. Render each as plain
inline SVG inside a bordered tile in a grid; the client copies one into a 1080×1350 post and
resizes.

**Accent rule (state this in the section copy):** `--acc-500` = the punch, the positive/win
state = a functional green, the negative/leak state = a functional red — **one accent per
card**. If the brand has no functional colors, add `--good`/`--bad` to the scaffold (a green
+ red that don't clash with the accent); otherwise reuse a second accent for "win".

Two sub-grids: **Chart atoms** (`repeat(5,1fr)`, 10 tiles) + **Line icons**
(`repeat(8,1fr)`). Pick the icon set from the client's vertical (e.g. for iGaming: voice call,
SMS, deposit, tracking, player, operator, reactivation, player-base; for dev: repo, deploy,
bug, API, sprint, etc.). Mapping of atom → intent (carry verbatim into the section copy):
proportion → Donut · share of a base → Dot grid · narrowing stages → Funnel · change over time
→ Growth curve · magnitude/rank → Bar chart · narrow-to-niche → Concentric · positioning →
Quadrant · hub→attributes (ICP/committee) → Hub & spokes · single metric → Score ring · two
opposed states → Timeline.

```css
.gfx-grid{display:grid;grid-template-columns:repeat(5,1fr);gap:16px}
.gfx{border:1px solid var(--n-300);border-radius:14px;padding:16px 12px 14px;text-align:center;background:var(--white)}
.gfx svg{display:block;margin:0 auto 10px}
.gfx .nm{font-size:12px;font-weight:700;color:var(--ink-800)}
.gfx .use{font-size:10.5px;color:var(--ink-500);margin-top:3px}
.ico-grid{display:grid;grid-template-columns:repeat(8,1fr);gap:14px}
.ico{border:1px solid var(--n-300);border-radius:12px;padding:15px 8px 11px;text-align:center;color:var(--ink-800)}
@media(max-width:760px){.gfx-grid{grid-template-columns:repeat(2,1fr)}.ico-grid{grid-template-columns:repeat(4,1fr)}}
```

Atom SVGs (all viewBox `0 0 90 90`, swap hexes for `var(--acc-500)` / `var(--good)` /
`var(--bad)` / `var(--n-300)` / `var(--ink-500)`):

- **Donut** — 4 `<circle cx=45 cy=45 r=33 fill=none stroke-width=14>` with `stroke-dasharray="LEN 1000"` + `transform="rotate(DEG 45 45)"`; circumference ≈ 207, biggest slice = accent, rest neutral tints. Start the first at `rotate(-90 …)`.
- **Funnel** — 4 narrowing `<polygon>` tiers, accent with opacity ramp `1 → .7 → .5`, **last tier = `--good`** (the convert stage).
- **Dot grid** — 5×4 `<circle r≈4.4>` on a 15px pitch; first N = accent, rest `--n-300`.
- **Growth curve** — grey L-axis (`<path d="M14 78 V8 M14 78 H82">`), accent `<path>` curve (`stroke-width 2.6`), area fill = accent `opacity .12`, end dot accent.
- **Bar chart** — grey L-axis + 4 `<rect rx=2>` rising, accent opacity ramp `.45/.62/.8/1`.
- **Concentric** — 4 nested `<circle>` r `34/25/16/8`, accent opacity `.15/.4/.7/1`.
- **Quadrant** — accent-tint `<rect>` + grey cross axes + 4 dots (3 accent, 1 second-accent/neutral).
- **Hub & spokes** — centre accent disc (r10) + 6 grey spoke `<line>` to white `<circle r6 stroke=accent>` nodes on a r30 ring (angles `-90 + k·60°`).
- **Score ring** — `--n-200` track ring + accent arc (`stroke-dasharray` for pct, `stroke-linecap=round`, `rotate(-90 …)`) + centre `<text>` number (display 900).
- **Timeline** — grey `<line>` + `--bad` node left + `--good` node right + small grey mid ticks + two mono end labels.

Line icons: 24×24, `fill=none stroke=currentColor stroke-width≈1.9 stroke-linecap=round`
(inherit `--ink-800` from `.ico`; accent a few if useful). Mirror the client's signature flow
(for the campaign/process pipeline use the SAME glyphs as the flow component).

Close with a one-line note: "Each atom is plain inline SVG on the brand tokens — copy into a
post/carousel and resize. Same vocabulary as the `infographic` / `linkedin-carousel` skills."
Reference build (iGaming, recolored to blue): that client's design system, section 11.

## CSS-variable scaffold (adapt hexes per brand)
```css
:root{
  /* INK — dark brand base, 4-5 steps */
  --ink-900:#…; --ink-800:#…(core); --ink-700:#…; --ink-600:#…; --ink-500:#…(muted text);
  /* ACCENT — the one hero color, 5-6 steps */
  --acc-700:#…(deep/hover); --acc-600:#…; --acc-500:#…(primary); --acc-300:#…; --acc-100:#…(tint); --acc-50:#…;
  /* NEUTRALS + FUNCTIONAL (tint functional toward brand hue) */
  --paper:#…; --n-200:#…; --n-300:#…; --n-400:#…; --white:#fff;
  --ok:#…; --warn:#…; --err:#…;
  /* TYPE */
  --font-display:'…'; --font-body:'Inter'; --font-mono:'…';
  --maxw:1080px;
}
```
Shared conventions: `section{padding:84px 0;border-bottom:1px solid var(--n-200)}`,
`.wrap{max-width:1080px;margin:0 auto;padding:0 32px}`, sticky blurred TOC, mono section
labels, hover lift on cards. Mobile: hide TOC, shrink hero H1, collapse grids to 1-2 col.

## Font pairing guidance (pick a CHARACTER font that fits the vertical)
- Display = geometric/grotesque (Space Grotesk, Plus Jakarta Sans, Archivo, Clash) for warmth/structure.
- Body = **Inter** (default workhorse) or the site's real body font if clean.
- Character = the differentiator:
  - Engineering / construction / data → **IBM Plex Mono** (specs, ISO codes).
  - Software / dev / "code" brands → **JetBrains Mono** / Geist Mono.
  - Finance / legal → a serif accent (e.g. Fraunces) instead of mono.
  Use the character font for mono labels, stat captions, tags, prices.

## Distinctiveness rule
Every client must look different: vary the hero motif, corner radius (corporate = 6-10px
sharper; friendly = 12-18px rounder), accent discipline, and the signature component(s).
Never ship two clients with the same layout — use the engineering vs dev archetypes as two poles.

## Port & deploy bookkeeping
Take the next free 460X/461X port (check existing `.claude/launch.json` entries).
Deploy: `npx netlify-cli deploy --dir . --prod` then rename via `api updateSite` with the
UUID from `.netlify/state.json`. Final URL: `https://<client>-design-system.netlify.app`.
