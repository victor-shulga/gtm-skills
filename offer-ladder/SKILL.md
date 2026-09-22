---
name: offer-ladder
description: Use when Viktor wants to build a vertical OFFER LADDER (value/ascension ladder) for an IT-agency client from their website — free → low → mid → high tiers around ONE core transformation, grounded in the agency's real services and case studies. Trigger when the user says "сходи оферів", "побудуй драбину оферів", "offer ladder", "value ladder for [client]", "ascension ladder", "розклади офери по тірах", or pastes an agency URL and asks how to structure their portfolio / monetization. NOT for generating parallel offer-bets to A/B test in cold outbound — that is the offer-factory skill. Ladder = vertical portfolio architecture; offer-factory = horizontal test batch. They compose: ladder gives structure, offer-factory tests the entry rungs.
---

# Offer Ladder

Build a vertical ascension ladder for an IT-agency client: a small set of tiers around **one core transformation**, where the SAME buyer ascends as their readiness (money + trust) grows. Grounded in the agency's real services and case studies.

**Core principle (do not violate):** a ladder is NOT different products for different people. It is *different levels of readiness of the same person to invest, to get the same result*. If the tiers don't share one outcome, you've built a shelf, not a ladder.

**Language:** reasoning in Ukrainian; tier names, promises, CTAs in English.

## What you need
- **Client website URL** (required) — services + case studies.
- Optional: known core promise, price points, constraints, what content/assets they already have.

## Process (9 phases)

### Phase 1 — Scrape everything
Pull **all** service lines (not just headline ones), capabilities, verticals, positioning, and **case studies with concrete numbers** (the proof bank). Use the Google Drive connector for Docs; WebFetch / Apify for live web.

### Phase 2 — Rank services
Score each service: `proof strength (has a case with numbers) × differentiation × outcome clarity`. This surfaces which services can anchor real rungs vs which are filler.

### Phase 3 — Find the ONE core transformation
Identify the single result the whole ladder delivers (e.g. Viktor's own "2X new revenue", an AI agency's "idea → production AI product"). Every tier delivers THIS — only the depth of involvement and who does the work changes. If you can't name one core outcome, stop and ask the user; without it there is no ladder.

### Phase 4 — Build adaptive tiers
Build only the tiers the client can actually support (proof or capability exists). Don't force four. Missing-but-valuable tiers → mark `[TODO: create — no asset yet]`, never invent. For each tier capture:
- **Tier** (Free / Low / Mid-frontend / High) + offer name
- **How the result is delivered** at this depth
- **Agency's role** (content integrator → framework author → coach/reviewer → executor)
- **Price band**
- **Proof** (real case) or `[TODO]`

Reference shape (Viktor's portfolio model):

| Tier | How the result is delivered | Agency role | Price |
|---|---|---|---|
| Free | buyer SEES the right vs their wrong; problem becomes named | content integration | $0 |
| Low | buyer gets frameworks/SOPs and applies them solo | framework author | $ |
| Mid (frontend) | buyer applies under supervision — groupwork, accountability | coach + reviewer | $$ |
| High | you do it WITH and FOR the buyer: strategy, hiring, launch | executor | $$$$ |

**Mid-tier (frontend) format heuristic:** default to a **cohort / group program**, not 1:1 — unless the client's resources & strengths clearly say otherwise. 1:1 mentoring (a) **cannibalizes high-ticket** (a founder who'll pay for personal work usually just buys the high-ticket), (b) **doesn't scale** on limited hours, (c) **underuses** the real strength (frameworks + group case-review). Offer 1:1 only as an inactive, pay-as-you-go fallback for buyers a cohort doesn't fit by timing.

### Phase 5 — ICP map across tiers
The ICP **widens going down** the ladder: high-ticket = narrow (ready + budget), lower tiers = broader (not yet ready / no budget / authority-building). For each tier, name the ICP (industry × size × readiness). Rules:
- **Don't actively sell lower tiers to a high-ticket-ready ICP** — it dilutes the message and the deal.
- **No reverse movement** — a high-ticket client does not later buy the guide; design the funnel upward only.
- Lower tiers exist to **nurture the not-yet-ready** toward the top, or (free) to **build authority/visibility** — not as the main revenue.

### Phase 6 — Ascent logic (trigger + CTA per transition)
A ladder works only if each step up is triggered. For every transition (Free→Low, Low→Mid, Mid→High, and any direct Free→High jump) define:
- the **trigger thought** in the buyer's head ("this resonates but I have no step-by-step for my situation")
- the **CTA** that moves them up.
No trigger = it's a price list, not a ladder.

### Phase 7 — Anti-cannibalization checks (validate the ladder)
Run these; flag any violation:
1. **≥5× price gap** between adjacent tiers (smaller gap → buyer hesitates, picks cheaper).
2. **Frontend ≤ 20%** of the high-ticket's first-year price (else it cannibalizes high-ticket).
3. **Each tier delivers distinct value**, not "the same thing cheaper" — name the difference explicitly (framework vs transformation-under-supervision vs done-for-you).
4. **Free gives ~20% of value** (problem + framing), never the ready-to-use artifact that the low tier sells.
5. **No down-sell:** never route a high-ticket-ready buyer into lower tiers; keep a direct "book a call" on every free touchpoint.
6. **Transitions via CTA + proof, not discounts** (discounts kill the premium signal).

### Phase 8 — Launch sequence (don't launch all tiers at once)
A ladder is also a build/launch ORDER, not just a structure. Sequence by: (a) what the client already has, (b) where it's cheapest to validate demand, (c) highest ROI on the founder's time. Principles:
- **One tier at a time.** Launching 4 tiers in a quarter = 4 weak offers.
- **Validate before climbing:** don't build the cohort/high rung until the low/entry rung has proven demand (e.g. low-tier: Playbook → Audit → DIY-course, in that order — not in parallel).
- **Every offer launches only with a warm audience / distribution** (LinkedIn, list, prior product) — never "into the void".
- Output a concrete month-by-month order for the tiers that exist + the `[TODO]` ones.

### Phase 9 — Connect to the test layer & hand off
- **Cold-facing rungs** (the entry rung you'd put in outbound) get the offer-factory card + test design (promise, hook, N, kill/keep). Upper rungs = **expand**, sold after delivery, NOT cold-tested.
- Hand off: `offer-factory` to generate/test the entry-rung bets; `hypo-generator` for who+signal on those rungs.

## Output format
1. **Ladder table** (Tier | how result delivered | agency role | price band | proof/[TODO]).
2. **ICP map across tiers** (which ICP each tier serves; note the narrow-at-top / wide-at-bottom shape).
3. **Per-tier detail**: offer name · EN promise (use offer-factory's Promise Formulas, never "We help…") · what's delivered · proof or [TODO].
4. **Ascent map**: trigger + CTA for each transition.
5. **Validity check**: pass/fail on the 6 anti-cannibalization rules, with fixes for any fail.
6. **Launch sequence**: month-by-month order to build/launch the rungs.
7. **Entry rung → outbound**: which rung to test cold + pointer to offer-factory.

## Hard rules
- **One core transformation across all tiers** — verify before building.
- **Adaptive tiers** — only what the client can support; gaps = `[TODO: create]`, never fabricated.
- **Proof only real** — case studies from the site; missing → `[TODO]`.
- **Run the 6 anti-cannibalization checks every time** and report results.
- A ladder is portfolio architecture, not a test batch. For cold A/B bets, route to `offer-factory`.

## Anti-patterns (flag these whenever you see them in the ladder)
1. **Message dilution.** "I help IT agencies with X" decays into "I sell courses + guides + some consulting." If you can't say what the agency does in one sentence, the ladder is too wide — cut tiers.
2. **Lower tiers eat high-ticket time.** A cohort quietly demands 20 hrs/wk and high-ticket sales starve. Antidote: time-box (fixed days for delivery vs high-ticket sales); priority never shifts.
3. **Low-ticket sold without a ladder.** Buyer grabs the guide and vanishes — no nurture to the next rung. Antidote: a post-purchase email/DM sequence with cases + invites to the next tier.
4. **Frontend priced "as convenient" → cannibalizes high-ticket.** Antidote: hard positioning — frontend = education/transformation, high-ticket = done-for-you execution. Different promises.
5. **Free becomes the main product.** Audience trained to consume free, never pay. Antidote: free = 20% value (problem + framing), never the ready-to-use artifact.
6. **Building into the void.** Made the asset, no distribution, no sales. Antidote: launch a rung only with a warm audience.
7. **"I'll do it myself."** Founder hand-builds landing pages / sequences / payments. Antidote: outsource the low-value ops; founder time is 5-figure, freelancer time is 2-figure.

## Worked reference
Viktor's own ladder: Free (self-audit/SOPs) → Low (Agency GTM Playbook) → Mid (Biz Dev OS cohort) → High (Fractional CBDO), all delivering one promise "2X new revenue YoY", with 5× gaps and frontend ≤20% of the CBDO retainer.
