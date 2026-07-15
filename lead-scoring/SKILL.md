---
name: lead-scoring
description: Score a lead/account base against your ICP using a deterministic 100-pt rubric before SDR outreach. Use when someone pastes a lead list / CSV / Sheet and asks to score, qualify, rank, or prioritise it against the ICP — "score these leads", "qualify the list", "ICP score", "prioritise leads". Deterministic, no fabrication, data-gap flags. Pairs with a signal-detection layer (detect) and a prospect-profiler (pre-touch cards) in the outreach QA G2→G3 stage. NOT for inventing the ICP (build that first) or writing copy (use a sequence writer).
---

# Lead Scoring

Score a lead base against a defined **ICP** with a 100-pt rubric. The rubric must be
adapted to your ICP and approved before you run it on a real base — swap the example
bands below for your own firmographics, geos, industries, signals, and buyer titles.

## Hard rule
**The methodology (weights + thresholds) must be approved BEFORE scoring a real base.**
If it isn't confirmed, say so and score only as a labelled DRAFT preview. Never silently
run on unapproved weights — that produces wrong scores.

## Procedure
1. **Anti-ICP gates first.** If any fires → `Disqualify`, skip points. Define your own
   hard disqualifiers (e.g. wrong geography, strong in-house capability, deal size below
   floor with no recurring revenue, service you don't actually deliver, culture/policy
   block). Any gate hit = out, regardless of other points.
2. **Score the categories (100 pts max).** Pull each ONLY from provided/verifiable data.
   Missing → `0` + `data-gap` flag. Never guess firmographics, signals, or titles.

Example weighting (tune per ICP — weights should sum to 100):

| Category | Max | Bands (example) |
|---|---|---|
| Deal potential | 20 | T1 20 / T2 10 / T3 5 |
| Geo | 15 | focus region 15 / follow-up region 10 / else 0 |
| Industry | 10 | core-fit industry 10 / adjacent 5 / none 0 |
| Headcount | 5 | sweet-spot size 5 / near 3 / too small 1 |
| Services match | 10 | do-best 10 / understand-no-proof 5 / none 0 |
| Service-need signal | 15 | active buying signal 15 / capability gap 10 / legacy tooling 5 / leadership change 5 — take HIGHEST, don't sum |
| Digital maturity | 5 | mature 5 / mid 3 / immature 0 |
| DM title | 10 | true decision-maker 10 / influencer 5 / specialist 0 |
| Engagement & Intent | 10 | high-intent page 10 / newsletter 10 / visit 2 |

3. **Tier** from firmographics (industry + size + service fit), not assumption.
4. **Bands → action:** High 75–100 call · Medium 60–74 conditional (core dimensions must
   match) · Low 40–59 nurture · <40 or gate = Disqualify.
5. Each signal carries source + date. Freshness matters: recent hiring signals are hottest,
   tender/RFP wins stay warm ~2 weeks, most signals decay by ~30 days.

## Output
One row per account: `Company · Tier · per-category points · Total · Band · Action ·
Data-confidence(H/M/L) · Missing fields`. Plus a `data-gap` list of accounts needing
enrichment before a reliable score.

## Don't
- Don't round up on doubt — take the lower band.
- Don't invent missing firmographics, signals, or titles.
- Don't score a real base on unapproved weights.
