---
name: prospect-profiler
description: >-
  Turns a SCORED account list into one tactical pre-touch dossier per account: a compact "60-second
  card" an SDR reads right before writing the first touch. Batch by design: reads the output of lead-
  scoring / agency-signal-sourcer (or any list with company + signal + role data) and emits one action
  card per account (summary, talking points, comm style, grounded pain, recommended approach, data-
  quality flag). Adapted for B2B service agencies (BIM/MEP, GIS, custom dev, AI/SaaS engineering
  outsourcing), NOT US-SaaS. Use when asked: "зроби картки по лідах", "профайли проспектів", "pre-
  touch brief", "дос'є на акаунти", "prep cards before outreach", "build prospect profiles", or when
  handed a scored list before copy is written. Sits between the list stage and the copy stage. NOT for
  deep one-company intelligence (account-dossier), NOT for persona archetypes (persona-builder), NOT
  for writing the sequence (sequence-writer).
---

# Prospect Profiler — the 60-second pre-touch card

You turn a scored account list into **tactical dossiers a rep acts on**. One card per account. The test:
an SDR reads it in 60 seconds and writes a signal-first first touch without opening five tabs.

**Core principle (Viktor's frame).** A profile is not a research essay. It separates:
- **The dynamic signal** = the time-bound trigger → tells the rep *WHEN* and *why now*.
- **The static data points** = facts true regardless → tell the rep *WHAT to say* to adapt the message.
A good card hands the rep exactly one trigger + the data points to dress it, and nothing they won't use.

**Anti-hallucination rule (the thing janskuba's version gets wrong).** Never invent pain. Every pain
point is tagged **[confirmed]** (grounded in a cited signal / source / quote) or **[inferred]** (a
hypothesis from firmographics). Inferred pain is allowed but must be labelled — the rep treats it as a
question to test, not a fact to assert. If you can't ground or honestly infer it, leave it out.

---

## When to use / inputs

Runs over a **scored list** — ideally the output of `13-lead-scoring` or `agency-signal-sourcer`
(account + signal + role + score). Minimum viable input: company name + at least one signal OR role.

Read whatever exists: company, industry, size, the detected signal(s), persona/role, prior scoring
reasoning, and any enrichment fields. If a signal source URL or quote is present, keep it for grounding.

Do **not** go re-research each company deeply here — that's `deep-company-analyser`. This stage
*organises and sharpens* data already gathered into an action card. If a field is missing, flag it
(see `data_quality`) rather than inventing it.

---

## The card schema (one per account)

| Field | Rule |
| :-- | :-- |
| `account` | Company name |
| `tier` | Carry over from scoring (T1/T2/T3) — drives effort, see below |
| `summary` | **≤ 80 words.** Who they are · what changed (the signal) · why now is a window. Every word earns its place. No filler, no "leading provider of" marketing voice. |
| `the_signal` | The single dynamic trigger to open on + its freshness (e.g. "Hiring 3 BIM coordinators, posted 11 days ago"). If multiple, pick the **freshest + most actionable**, list others in notes. |
| `talking_points` | 2-4. Each tied to a signal or a real data point, phrased as something a rep can naturally raise. Specific to THIS account, never generic industry takes. |
| `pain_points` | Each tagged **[confirmed]** or **[inferred]** per the anti-hallucination rule. Max 3. Tie each to the buyer's likely cost-of-inaction, not a feature gap. |
| `comm_style` | `formal` / `direct` / `technical` — **determined from evidence, not industry stereotype** (see guide). |
| `recommended_approach` | Triplet: `channel \| angle \| timing`. channel = email / linkedin / multi. angle = direct / proof-led / question-led / value-first. timing = now / this week / event-window. |
| `data_quality` | `HIGH` / `MEDIUM` / `LOW` — honesty flag (see guide). Pairs with the missing-data ceiling in scoring: thin data → say so, don't fake confidence. |
| `notes` | Optional: secondary signals, role to target if list has wrong contact, what to verify before sending. |

**Language.** Write the card in Viktor's working language (UA). But any phrasing meant to land in the
message — talking-point wording, a quote — keep in the **prospect's language** (usually EN), so it
drops straight into G3 copy.

---

## Determination guides

### comm_style — from evidence, not cliché
Do NOT default "enterprise = formal". Read actual signals of how they communicate:
- `technical` → engineering-led firm, technical buyer title, spec/tool language in their posts/JD
- `direct` → founder/owner-led, lean team, plain-spoken public voice, SMB
- `formal` → regulated/procurement-driven buying, committee, public-sector or large-contractor tone
If there's no evidence → default `direct` and flag `data_quality` accordingly. A guess dressed as a fact is worse than `direct`.

### data_quality — the honesty flag
- `HIGH` — signal is fresh + sourced, role confirmed as decision-influencer, firmographics known
- `MEDIUM` — signal present but older/unsourced, OR role/size partly unknown
- `LOW` — no live signal, or scoring flagged capped dimensions (missing-data ceiling fired). On LOW: the rep should enrich before sending, or treat the touch as a probe.

---

## Tier-aware effort (budget tokens where they pay)
- **T1 / T2** → full card, sharpest talking points, grounded pain, 2-4 points.
- **T3** → short card: summary + the_signal + comm_style + data_quality. Skip deep pain; one talking point. Don't over-invest in accounts the scoring already deprioritised.

---

## Agency adaptation (overrides US-SaaS instincts)
- Drop product-led framing (usage spikes, trial signups, seat expansion). Agency buyers buy **capacity,
  expertise, de-risking**.
- Pain is usually: hiring can't keep up, a project is at risk, an in-house gap, a deadline, a failed
  vendor. Ground talking points in delivery reality, not software ROI.
- "Who can buy" matters: if the listed contact isn't a decision-influencer, say so in `notes` and name
  the role to target — a perfect account profiled against the wrong junior is wasted.

---

## Output format

Lead with a **batch table** (one row per account, sorted T1→T3) for scanning, then the **full cards**
for T1/T2 below it. Write the table to `output/prospect-profiles.csv` if the run is file-based; otherwise
render inline.

```
Prospect profiles — [list / hypothesis name] · [date] · [n accounts]

[batch table: account | tier | the_signal | comm_style | approach | data_quality]

— T1/T2 full cards —
[card per account]
```

---

## Integration (where this sits)

```
G1 strategy → G2 list (lead-scoring / agency-signal-sourcer)
                         │
                         ▼
              prospect-profiler  ← THIS skill: scored list → pre-touch cards
                         │
                         ▼
              G3 copy (sequence-writer / 03-copy-generation / linkedin-sequence)
```

- **Upstream:** `13-lead-scoring`, `agency-signal-sourcer` (signal + freshness + score).
- **Deeper research, if a T1 needs it:** hand the account to `deep-company-analyser` (verbatim pain,
  why-buy) — this skill points there, it does not duplicate it.
- **Downstream:** each card feeds G3. `the_signal` becomes the first-touch opener; `comm_style` sets
  tone; `recommended_approach.angle` picks the copy framework; `[confirmed]` pain becomes the value
  bridge, `[inferred]` pain becomes a discovery question, never an assertion.

## Hard rules
1. Never assert `[inferred]` pain as fact. Tag everything.
2. ≤ 80-word summary. No marketing voice.
3. comm_style from evidence or default `direct` — never industry stereotype.
4. `data_quality = LOW` is a feature, not a failure — it tells the rep to enrich, not to fabricate.
5. One trigger per card. Extra signals go to notes.
