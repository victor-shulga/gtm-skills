---
name: hypo-generator
description: Use when Viktor wants to generate outreach hypotheses for an IT agency client from a website URL or text brief. Performs Phase 1 (extract services / ICP / use cases / case studies from the client's site) + Phase 2 (build a 10-hypothesis matrix of 2-3 ICP × 2-3 signals × 2-3 offers, each scored with Viktor's 5-factor weighted framework). Trigger when the user says: "генеруй гіпотези для клієнта", "побудуй матрицю гіпотез", "оціни цей агентський сайт", "що тестувати для [клієнт]", "hypothesis generation for agency", "матриця гіпотез по URL", or provides a client URL and asks what campaigns to run. NOT for one-off campaign idea generation when ICP/signals are already known — use hypothesis-builder for that.
---

# Hypo Generator

Generates a full 10-hypothesis outreach matrix for an IT agency client, starting from a website URL (preferred) or a text brief. Built on Viktor Shulha's two-phase methodology + signals-catalog.md.

**Audience for the output:** Viktor's client (an IT agency founder or their biz dev team). Hypotheses are framed for *their* outbound, not for Viktor outreaching to them.

---

## Required input

One of:
- **A client URL** (preferred) — agency's main marketing site
- **A text brief** — what the agency does, who they sell to, where, recent cases

Optional (always welcome):
- Geographic priorities or no-go regions
- Industries to focus on or avoid
- 1-3 case studies with numeric outcomes (preferred for proof)
- Current state of outbound (none / ad-hoc / has SDR / has agency)

---

## Workflow

### Phase 1 — Discovery (do this first, before any hypotheses)

If a URL was provided:

1. WebFetch the homepage. Extract:
   - **Services / capabilities** (what they sell — design, custom dev, mobile, AI, etc.)
   - **Vertical / industry focus** (who they sell to today)
   - **Geographic indicators** (HQ, team distribution, sales markets)
   - **Case studies** with quantified outcomes — note the client logos and any numbers
   - **Existing positioning** ("we help X achieve Y by Z")
   - **Team size / company size proxies** (about page, careers page)
   - **Tech stack signals** (technologies mentioned in case studies)
2. If the homepage references `/case-studies`, `/services`, `/industries` — WebFetch one or two of these for deeper context.
3. Note explicit gaps: anything critical you still don't know.

If a text brief was provided: extract the same fields from it; flag missing fields.

### Phase 1.5 — Ask clarifying questions (only if needed)

Use `AskUserQuestion` to fill **only critical gaps**. Don't over-ask. Likely candidates:

- **Geo priority** — if site doesn't make it clear, ask: US / UK / EU / DACH / LATAM / no preference?
- **No-go segments** — anything they explicitly won't sell to (e.g., crypto, gambling)?
- **Best case study to use as proof** — which 1-2 cases have actual numeric outcomes (revenue lifted, time saved, conversion improved)?
- **Current outbound state** — none / has SDR / has agency / has tried & burned

Skip questions you can answer from the site. Maximum 4 questions in one batch.

### Phase 2 — Build the hypothesis matrix

1. **Read `signals-catalog.md`** (in this skill folder) — this is your signals library. Don't invent signals; pick from the catalog.
   > **Operational pairing:** this skill is the STRATEGY layer (which signal × ICP × offer to bet on). For the OPERATIONS layer — *how* to detect a chosen signal (which tool, Clay credit cost, freshness/decay window), how to score accounts that have it, and which signal-to-action GTM play to fire — use the **`agency-signal-sourcer`** skill (`resources/detection-tools.md` ⭐, `scoring.md`, `gtm-plays.md`). Its `detection-tools.md` directly informs the **"Easy to scrape"** factor in Phase 3, and its `taxonomy.md` can surface NEW signals worth adding to `signals-catalog.md`.
2. **Define 2-3 ICPs** based on Phase 1 findings. Each ICP = (industry × company size × geo). Examples: "US fintech series A-B, 50-200 ppl"; "UK D2C ecom, 20-100 ppl"; "EU healthtech post-seed, 10-50 ppl".
3. **Pick 2-3 signals per ICP** from the catalog. Prefer **dynamic signals** (timing-based, 3-5% TAM) over static data points unless static gives a stronger problem hook.
4. **Pick 2-3 offers** based on Phase 1 services + use case mapping. Each offer = (service + outcome) → e.g., "Discovery + MVP in 90 days for fintech founders launching a new product line".
5. **Cross-combine into exactly 10 hypotheses.** Don't list all 27 possible combos — diversify across ICP × signal × offer so no two hypotheses are too similar.
6. **For each hypothesis, fill these 12 fields** (matching Viktor's Hypothesis Report Template):

   | Field | What goes here |
   |---|---|
   | `#` | H01–H10 |
   | `Hyp name` | Short label: "Fintech Series A — new product launch — Discovery+MVP" |
   | `ICP` | Industry + size, in one line |
   | `Persona (primary)` | Title of the person you'll target first |
   | `Buying committee` | 2-3 other roles that influence the deal, in a sub-bullet |
   | `Geo` | Region(s) |
   | `Subindustry` | More granular vertical if relevant |
   | `Problem` | The expensive, specific problem they have (1-2 sentences) |
   | `Buying signal` | The trigger from signals-catalog.md you're using |
   | `Offer` | The service/outcome framing |
   | `Case study / Proof` | Which of the agency's cases you'd use as proof (with the actual numeric outcome) |
   | `TAM` | Estimated account count + brief reasoning ("US fintech Series A-B, 50-200 ppl ≈ 800-1500 per LinkedIn") |
   | `Test batch` | Recommended initial outreach size: usually 200-500 accounts |

### Phase 3 — Score every hypothesis

Apply Viktor's **5-factor weighted model** exactly. Each factor scored 1, 3, or 5:

| Factor | Weight | Scoring rules |
|---|---|---|
| **Easy to scrape** | 0.15 | 5 = signal is trivially detectable in Clay / LinkedIn / BuiltWith / Crunchbase. 3 = requires LLM enrichment or moderate effort. 1 = manual review needed or signal lives only in private data. |
| **Scaling possibility** | 0.15 | 5 = TAM > 3,000 and signal fires for 5%+ of TAM continuously. 3 = TAM 300-3,000 OR signal is infrequent. 1 = TAM < 300 OR signal fires rarely. |
| **Clear & expensive problem** | 0.25 | 5 = problem causes obvious revenue/cost pain ("AEs spending 40% time prospecting"). 3 = problem is real but not urgent. 1 = problem is theoretical or "nice to have". |
| **Offer relevance** | 0.20 | 5 = the agency has the exact case study + capability for this ICP + signal combo. 3 = adjacent fit, would require slight repositioning. 1 = stretch — agency doesn't have proof or capability here. |
| **Trivial trigger** | 0.25 | 5 = signal is unambiguous and almost always means the buyer has the problem ("posted SDR role 4 weeks ago, then withdrew it"). 3 = signal is suggestive but not deterministic ("growing team"). 1 = signal is weak / generic / could mean many things. |

**Total score** = Σ(score × weight). Range: 1.0 — 5.0.

**Verdict thresholds:**
- **Total > 3.5** → "Run first" — high conviction, start with 500+ batch
- **Total 3.0 – 3.5** → "Worth testing" — start with 200-300 batch, iterate fast
- **Total < 3.0** → "Skip or rework" — at least one factor is fundamentally broken

Each individual score must include a **one-line justification** ("Trivial trigger = 3: 'recent funding round' is detectable but not all funded companies need outbound help right now").

### Phase 4 — Generate the report

Output a single Markdown document in this order:

```
# Hypothesis Report — [Client name]
Generated: YYYY-MM-DD · Source: [URL or "text brief"]

## Executive summary
- Strongest hypothesis: H0X — [name] — total score [X.X] — [one-line why]
- Weakest hypothesis kept: H0X — [name] — total score [X.X] — [why included anyway]
- Recommended starting batch: [H01, H03, H07] — total addressable accounts ≈ [X]
- Key risk in this client's portfolio: [one observation, e.g., "all 10 lean on Series A funding — concentration risk"]

## Phase 1 — What I extracted from the site
- **Services:** [list]
- **Existing use cases:** [list]
- **Vertical / industry signals:** [list]
- **Case studies with numbers:** [list with quantified outcomes]
- **Gaps I had to ask about:** [list]

## Summary table (all 10, sorted by score)

| # | Hypothesis | ICP | Persona | Signal | Offer | Final Score | Verdict |
|---|---|---|---|---|---|:---:|---|
| H01 | [short name] | [industry + size + geo] | [title] | [signal in plain words, e.g. "Hiring a BDR + sales is founder-led" — NOT the catalog ID] | [offer] | 4.70 | ✅ Run first |
| ... | ... | ... | ... | ... | ... | ... | ... |

Rules for this table:
- **Signals in plain words, never catalog IDs.** Write "New sales leader joined in last 90 days", not "A3/C5". The ID lives only in the detailed card below.
- **Final score only** — no per-factor breakdown in this table (that stays in the detailed cards).
- Verdict: ✅ Run first (>3.5) · ⚠️ Worth testing (3.0–3.5) · ❌ Skip/rework (<3.0).
- End with one line: **Старт: [H0X · H0X · H0X]** — the highest-conviction batch.

## Hypotheses (sorted by total score, descending)

### H01 — [Hyp name] — Total: 4.2 ✅ Run first

| Field | Value |
|---|---|
| ICP | ... |
| Persona (primary) | ... |
| Buying committee | • Title 1 (role) <br> • Title 2 (role) |
| Geo | ... |
| Subindustry | ... |
| Problem | ... |
| Buying signal | ... (from signals-catalog.md: section X) |
| Offer | ... |
| Case study / Proof | ... |
| TAM | ... |
| Test batch | ... |

**Scoring:**
- Easy to scrape: 5 (0.75) — [reason]
- Scaling: 5 (0.75) — [reason]
- Clear & expensive problem: 5 (1.25) — [reason]
- Offer relevance: 3 (0.60) — [reason]
- Trivial trigger: 5 (1.25) — [reason]
- **Total: 4.60 / 5.0**

---

[Repeat for H02 ... H10]

## Post-launch reference (Kill / Optimize / Scale)

After running a hypothesis with at least 200 accounts:
- **Kill:** reply rate < 1% OR interest rate (positive replies / all replies) < 17% → hypothesis disproven, find new signal or angle
- **Optimize:** interest rate 17–30% → potential. Test new copy angles, refine data filters, keep running
- **Scale:** interest rate > 30% → validated. Add LinkedIn channel, increase volume, promote to Tier 1

Speed of testing > polish. Get 3 hypotheses live in 7 days, not 1 hypothesis perfected in 30.

## Next steps
1. Validate TAM numbers in Apollo / Sales Navigator
2. Build account lists in Clay using the signals listed above
3. Draft copy variants for top 3 hypotheses
4. Set up tracking: reply rate + interest rate per hypothesis (not per campaign)
```

---

## Language

Default: **Ukrainian** (Viktor's clients are mostly Ukrainian-speaking IT agencies).
Switch to English only if the source URL/brief is in English AND Viktor explicitly asks for English output.

The signals catalog itself stays in English (it's a reference).

---

## Hard rules

- **Never invent signals.** Every "Buying signal" field must reference one from `signals-catalog.md`. If a real-world signal applies but isn't in the catalog, add it to the catalog first with a note "(new, added YYYY-MM-DD, needs validation)" before using it.
- **Never invent case studies.** If the site doesn't show a case with numeric outcome for an ICP, write `Proof: TBD — no matching case study on site, recommend adding one` in that hypothesis. Don't fabricate.
- **TAM must include reasoning.** "≈800-1500 accounts" alone is unacceptable; always add the source ("US fintech 50-200 ppl per LinkedIn Sales Nav filters").
- **No more, no fewer than 10 hypotheses.** Discipline forces prioritization.
- **Diversity check before finalizing:** if two hypotheses share both ICP and signal, replace one. Don't ship near-duplicates.
- **Each score needs a one-line reason.** Bare numbers are useless for Viktor's review.

---

## References in this skill folder

- `signals-catalog.md` — the canonical signals/data-points library to draw from
- `examples/example-report.md` — one full sample report to anchor formatting expectations
