---
name: case-study-writer
description: >
  Turns a finished client project into a publishable case study in the canonical
  12-section Case Study Kit structure: SME interview questionnaire → data collection →
  result-first narrative (snapshot → 3-type Challenge → 1:1 Solution → before→after
  Results → testimonial → CTA → SEO), plus a designer visual brief and a pre-launch
  checklist. Also outputs 3 derivative formats (website page, one-pager PDF outline,
  LinkedIn handoff). Built for B2B service companies (agencies, outsourcing, consulting).
  Use when the user says: "напиши кейс", "зроби case study", "оформи проєкт у кейс",
  "case study from this project", "перепиши кейс", "у нас є результат — треба кейс",
  or pastes project notes / a call transcript / an old case and asks to turn it into
  a proper case study. NOT for collecting testimonials or reviews (that is a separate
  outreach ask) and NOT for writing LinkedIn posts from scratch (use linkedin-post-writing;
  this skill only hands off a post-ready summary).
---

# Case Study Writer

Produces a case study in the **Case Study Kit** structure — the canonical 12-section format
(result-first, scannable in 60 seconds). The case study is a salesperson: it convinces the
NEXT prospect with numbers and a sequence of decisions, not adjectives.

## What this skill produces

1. **Website case page** — full 12-section copy with inline visual markers, ready for CMS.
2. **One-pager outline** — condensed sections for the PDF sales attaches to proposals.
3. **LinkedIn handoff** — a post-ready summary passed to the post-writing process.
4. On demand: the **SME interview questionnaire** (if nothing is written yet), the
   **designer visual brief**, and the **pre-launch checklist**.

Working language: match the user. Case language: the client's market (ask if unclear —
usually English). Ask up front which output formats are needed (default = website page).

## Hard rules

- **No fabrication.** Every number comes from the user or their materials. Missing number →
  insert a visible placeholder `[[уточнити: X]]` and list all placeholders at the end.
  Never invent metrics, quotes, or timelines.
- **No result — no case.** No measurable outcome yet → say so and offer Weak-numbers mode
  (below) instead of faking impact.
- **≤150 words per section.** Must scan in 60 seconds. "2000 words" is NOT the goal —
  clarity is. If a section does not move the sale, cut it.
- **Outcome ≠ output.** Results = business consequences (before → after). Features = what
  was shipped. Never mix them.
- **Client confidentiality / NDA.** Ask whether the client's name/logo may be used. If not,
  anonymize: "a 120-person MEP engineering firm (US)" — industry + size + geo, no name.
  Blur/anonymize any NDA data in screenshots. Ask what may NOT be published (numbers, names).
- **Quotes only verbatim** from provided materials. Light grammar cleanup allowed, meaning
  untouched. Minimum **2 pull-quotes** (one at the Challenge, one at the Result) + 1 full
  testimonial.
- **CTA mandatory**, ends with a question. A case without a CTA loses the lead.
- **No AI clichés, no negative parallelism** («не X, а Y» — banned; "cutting-edge",
  "seamless", "game-changing" — banned). Active voice, past tense, concrete. Run the final
  through `anticopywriting-ai`.
- **Fact-check** every number and name against the SME answers before shipping.

## Step 1 — Intake (SME questionnaire → 12 sections)

If the user has notes / a call transcript → extract answers from there first, ask only the
gaps. If they have nothing written → output this questionnaire (they run it with the delivery
team or the client in one 45–60 min interview, then continue). Ask open questions, always ask
for **numbers**; "don't know the exact figure" → ask for a range/estimate.

- **A · Client context** (→ sections 2, 3) — what the company does, market/geo, headcount;
  how they stand out; who the stakeholder was (role, not name yet); engagement model,
  duration, our team composition. *(Can be self-researched.)*
- **B · Challenge** (→ section 4) — the **business** result they needed and why now (deadline,
  investor, competitor); the hardest **technical** part (legacy, integrations, load, data);
  the **delivery** challenges (timeline, team, unstable requirements, time zones); the cost of
  NOT solving it; prior attempts / other vendor and why it failed.
- **C · Why us + approach** (→ section 5) — why us over a competitor / in-house; how it
  started (discovery / workshop / audit); key milestones and dates (Week 0 → launch); what
  changed along the way (scope, priorities).
- **D · Solution** (→ section 6) — how EACH of the 3 challenges (business / tech / delivery)
  was solved; the key architectural/product decisions and why; deliberate trade-offs
  (scope cut, MVP focus); which screen/flow best illustrates the solution (→ designer).
- **E · Results — NUMBERS REQUIRED** (→ section 7) — the main result metric + figure
  (mandatory); before → after on 3–4 metrics (time, money, conversion, users, % growth);
  business consequences (revenue, funding, savings, speed, retention); what the client can now
  do that they couldn't before; any post-launch data (3 / 6 months).
- **F · Output** (→ section 8) — the 4–6 key features/modules shipped; what the client values
  most.
- **G · Tech** (→ section 9) — full stack (frontend, backend, infra, integrations, AI/data);
  why these technologies.
- **H · Quote** (→ sections 4, 7, 10) — will the client give an official quote + name/role/logo;
  one sentence on why they'd recommend us; may the company be named publicly or anonymized (NDA).
- **I · Legal / media** — what may NOT be published (numbers, names, screens under NDA);
  brand assets available (logo, team photo, product screens).

## Step 2 — Find the spine

Before writing, state in one sentence: **for whom this case sells what**. Pick the ONE result
that matters to the target reader (the next prospect, not the past client). Everything else
supports it. If the project had many outcomes, lead with the one closest to money or risk.

## Step 3 — Write (website format · 12 sections, strict order)

Each solution maps 1:1 to its challenge. One narrative — the reader flows pain → why us →
what we did → what came out; each section sets up the next. Mark visual placeholders inline
(they go to the designer).

1. **Title + headline metric** — `[what we did] + [main number]`. Not "How we built X".
   Example: *"Released MVP in 8 weeks → first 100 paying customers & $30K accelerator funding"*.
   Number is mandatory.
2. **At-a-glance snapshot** `[SNAPSHOT]` — scannable panel right under the title:
   Industry · Location · Team size · Engagement model · Duration · Stack · Headline result.
3. **About the Client** — 2–3 sentences: business, industry, market position, headcount.
   No water. Who they are and why to take them seriously.
4. **The Challenge** — three sub-blocks:
   - **Business Challenge** — the business problem being solved.
   - **Technical Challenge** — the hardest thing technically.
   - **Delivery Challenge** — team / process / timeline challenges.
   Insert the first **pull-quote** about the pain here `[QUOTE]`. State the cost of inaction.
5. **Why us + Approach** — why they chose us + how we worked: discovery → sprints → key
   milestones. Short timeline strip (Week 0 / 2 / 6 / 8). Removes "why trust you".
6. **The Solution → mapped 1:1 to Challenge** — each solution explicitly names the challenge
   it closes:
   - **Solution → Business Challenge:** … `[SCREEN]`
   - **Solution → Technical Challenge:** … `[DIAGRAM]`
   - **Solution → Delivery Challenge:** …
   Features are woven in here by the way, not as a detached list. The technical steps live
   here too — there is no separate "Approach" section competing with this one. This is the
   largest section of the case (400–500 words).
7. **Results & Business Value** — **before → after** with numbers `[METRIC]`, not "built a
   dashboard". Table: Metric · Before · After. Then the second **pull-quote** about the
   result `[QUOTE]`. Timeframe explicit.
8. **Features Delivered** — short list of what shipped (4–6). Output ≠ outcome — do not
   confuse with Results.
9. **Tech Stack** `[STACK]` — frontend, backend, infra, integrations (logos/list).
10. **Full Testimonial** `[QUOTE]` — 2–4 sentence quote + name, role, photo/logo. Strongest
    one is about ROI or trust; placed after the result.
11. **CTA** — one action for a reader with the same problem, ends with a question.
    *"Facing a similar challenge? → Book a call."*
12. **SEO / meta** — target keyword (in H1 + first 100 words), meta title ≤60 chars, meta
    description ≤155, alt tags on all visuals, internal links to adjacent cases/services.

Voice: dry, specific, zero superlatives.

**Length is a gate, not a preference.** Body **1500–2000 words**. Under 1200 it is a project
card, not a case study — go back to the SME for facts instead of shipping it. Per-section
budget:

| Section | Words |
| --- | --- |
| Title + number | 25 |
| Snapshot | 60 |
| About the client | 120 |
| Challenge | 250 |
| Why us + approach | 250 |
| **Solution** | **400–500** |
| Results before → after | 200 |
| Features delivered | 120 |
| Tech stack | 80 |
| Testimonial | 80 |
| CTA | 40 |

Two inline pull-quotes add ~60 more. **Solution must be the largest section.** If it is
shorter than Challenge, the case describes the problem instead of the work. A 40-word
section reads as underbaked; fill each one with real decisions and context, cut only water.

## Weak-numbers mode

If the client cannot share hard numbers (NDA, no baseline measured):
- Lead with the **operational** change: "from 3 tools and manual copy-paste to one pipeline",
  "first 5 SQLs from a channel that produced zero".
- Use ranges or ratios agreed with the client ("~2× faster", "under 4 weeks").
- Never dress qualitative claims as metrics.

## Step 4 — Derivative formats

- **One-pager**: Headline · 3 stat tiles · Problem (2 lines) · Solution (3 bullets) · Result
  (2 lines) · Quote · Contact. Fits one page.
- **LinkedIn handoff**: 5–7 line summary (hook candidate + core numbers + one surprising
  detail). Explicitly mark it as INPUT for the post-writing process, not a finished post.

## Step 5 — Designer brief (visual markers)

Every marker left in the draft is a visual to produce:

| Marker | What to make |
| --- | --- |
| `[HERO]` | Hero visual on top: product in context + headline metric as a badge |
| `[SNAPSHOT]` | At-a-glance panel (icons: industry / team / duration / stack) |
| `[BEFORE/AFTER]` | Before/after comparison (metrics or UI) |
| `[DIAGRAM]` | Architecture / flow / process |
| `[SCREEN]` | Product screens in a device frame, clean, retina |
| `[METRIC]` | Big number tiles for the Results section |
| `[STACK]` | Technology logos in a row |
| `[QUOTE]` | Pull-quote card with client photo/logo |

Design requirements: agency brand colors/fonts, white background under screens; real project
screens (blur/anonymize under NDA), not stock mocks; mobile contrast & readability (most
traffic is phone); alt text on every visual; export WebP/optimized, lazy-load, ≤200KB where
possible.

## Step 6 — Pre-launch checklist

- [ ] Number is in the headline
- [ ] Snapshot panel filled
- [ ] Each Challenge has a mapped Solution (1:1)
- [ ] Results in before→after format with numbers
- [ ] Body ≥1500 words and Solution is the largest section
- [ ] 2+ pull-quotes + 1 full testimonial
- [ ] CTA present, clickable, ends with a question
- [ ] All `[markers]` replaced with final visuals
- [ ] Legal approval on numbers / name / screens (especially NDA)
- [ ] SEO: meta title/description, keyword, alt tags, internal links
- [ ] Run through `anticopywriting-ai` (no AI trace, no negative parallelism)
- [ ] Mobile check
- [ ] Every number sourced or marked `[[уточнити]]` — placeholder list printed at the end
- [ ] Remove any internal / references section from the public version
