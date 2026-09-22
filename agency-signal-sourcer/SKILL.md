---
name: agency-signal-sourcer
description: >-
  Operational buying-signal engine for B2B service agencies (BIM/MEP, custom dev, GIS, AI/SaaS
  engineering outsourcing). Answers the OPERATIONAL half of signal-based outbound: how to DETECT a
  signal (which tool, Clay credit cost), WHEN it expires (freshness and decay windows), how to SCORE
  and prioritise accounts (recency multipliers, multi-signal stacking, heat tiers with SLAs) and WHAT
  to do once it fires (signal-to-action plays). Use for: detecting buying signals, which tool finds
  which signal, Clay cost per signal, signal freshness / decay / timing, signal scoring, heat-tier
  SLAs, signal-to-action plays, visitor-tracking and intent tooling (RB2B, Trigify, Common Room,
  Bombora, Koala, Warmly, 6sense, with EU/GDPR and agency-budget caveats), or "how do we
  operationalise signal X". Pairs with the STRATEGY layer (which signal x ICP x offer to test). Do NOT
  use it to invent the signal list (hypo-generator's signals-catalog) or to write outreach copy
  (sequence-writer).
---

# Agency Signal Sourcer (operational layer)

Adapted from adapted from public playbook's signal-sourcer, **re-pointed at B2B service agencies** instead of US SaaS vendors.
This skill is the *operational* half of signal-based outbound. The *strategic* half (what to test)
already lives in Viktor's `hypo-generator` and `hypothesis-builder` — they compose (see Integration).

## Setup (run once per session)

Resolve the install dir dynamically — never hardcode:
1. Glob for `**/agency-signal-sourcer/SKILL.md`
2. Its directory is `SKILL_BASE`; resources are at `{SKILL_BASE}/resources/...`

## Agency adaptation rules (apply to EVERYTHING below)

These override the source material, which was written for product/SaaS sellers:

1. **Signals ≠ Data Points** (Viktor's core frame, shared with `hypo-generator/signals-catalog.md`):
   - **Dynamic signal** = time-bound event, fires for ~3–5% of TAM → tells you *WHEN* to reach out.
   - **Static data point** = a fact true for ~100% of TAM → tells you *WHAT to say*.
   - A strong play = **one dynamic/individual signal as the trigger + one static data point to adapt the message.**
2. **Service-agency motion, not product motion.** DROP or down-rank product-led signals that don't apply:
   product-usage spikes, free-trial signups, G2 head-to-head, Bombora topic surge, PLG cross-sell.
   KEEP the signals that fit agency selling: **funding, hiring / hiring-surge, failed-hire, champion job change,
   new decision-maker (90-day window), tech-stack change, headcount growth, expansion/new-geo, product launch,
   event attendance, LinkedIn post engagement.**
3. **EU/GDPR + geography reality.** Many clients are EU/UA selling into US/UK/DACH. Person-level website ID
   (RB2B, Warmly de-anon) is **US-only**; in the EU only **company-level** IP ID is compliant. Flag this
   whenever recommending visitor tracking — never hand a client a US-only tool for an EU target list.
4. **Agency budget, not enterprise.** Demote enterprise-intent tools (**Bombora ~$30–100k/yr, 6sense ~$35–130k/yr,
   ZoomInfo ~$15–60k/yr**) to "enterprise only — usually out of scope." The realistic agency stack is
   **Clay + Serper/Claygent (0-credit detection first) + Trigify + RB2B-free + LinkedIn/Sales Nav.**
5. **Benchmarks are directional, not promises.** The source's 18–22% / 35–40% reply figures are adapted from public playbook self-cited
   and optimistic. Treat as ceiling; reality is closer to the team's house benchmark (top reply ~10%+). Never quote
   35–40% to a client as expected.

## Routing Table

| Request | Load |
|---|---|
| Which tool detects signal X · Clay credit cost · 0-credit-first cost optimisation · 1st/2nd/3rd-party sources | `{SKILL_BASE}/resources/detection-tools.md` ⭐ |
| Signal freshness / decay / optimal outreach window / reliability tiers | `{SKILL_BASE}/resources/detection-tools.md` (same file) |
| Score & prioritise accounts: weights, recency multipliers, multi-signal stacking, heat tiers + SLAs | `{SKILL_BASE}/resources/scoring.md` (apply adaptation rule 2 — strip PLG rows) |
| Signal-to-action playbooks (day-by-day sequences, owner, escalation) | `{SKILL_BASE}/resources/gtm-plays.md` (use agency-relevant plays only) |
| Full trigger taxonomy + INBOUND/POSTBOUND/BRIDGEBOUND/OUTBOUND framing | `{SKILL_BASE}/resources/taxonomy.md` |
| Set up a signal tool (RB2B, Trigify, Common Room, Bombora…) | `{SKILL_BASE}/resources/tool-setup-guides.md` (apply GDPR + budget caveats) |
| Track champion/contact job changes in Clay (step-by-step) | `{SKILL_BASE}/resources/job-change-tracking.md` |

## ⭐ Integration with hypothesis generation (the answer to "can we use these together")

These skills form a pipeline. Keep the division of labour clean:

```
STRATEGY (what to test)                          OPERATIONS (how to source + act)
─────────────────────────                         ───────────────────────────────
hypo-generator                                    agency-signal-sourcer (this skill)
  · reads signals-catalog.md (the signal LIST)      · detection-tools.md → HOW to detect each catalog signal,
  · builds 10-hyp matrix: ICP × signal × offer        which tool, Clay credit cost, freshness window
  · scores w/ 5-factor trivial-trigger weight       · scoring.md → once detected, SCORE & rank the accounts
hypothesis-builder                               · gtm-plays.md → the signal-to-action sequence to run
  · persona × signal × angle backlog                · tool-setup-guides.md → stand up the detection tool
```

**How to run them together:**
1. **Strategy first** — run `hypo-generator` (from client URL) or `hypothesis-builder` (from a known ICP+signal set)
   to pick which **signal × ICP × offer** hypotheses to test. The signal names come from
   `hypo-generator/signals-catalog.md`, NOT from this skill.
2. **Then operationalise here** — for each chosen signal, use this skill to answer:
   *which tool detects it, what it costs in Clay credits, how fresh it stays, how to score accounts that have it,
   and which GTM play to fire.*
3. **Feedback loop** — this skill's `taxonomy.md` / `detection-tools.md` can also **surface NEW signals worth
   adding** to `signals-catalog.md`. When you spot a catalog gap (a detectable trigger not yet listed with a
   trivial-trigger weight), flag it for Viktor to add — don't silently invent it inside a hypothesis.

> Rule of thumb: if the question is **"which signal should we bet on?"** → `hypo-generator` / `hypothesis-builder`.
> If it's **"how do we actually find / score / act on this signal?"** → this skill.
> If it's **"we already have a base of accounts — go find who has a live signal right now"** → `signal-research`,
> which executes this skill's method over a real list and returns an evidenced, dated, scored file + coverage report.

## Hand-off — use the EXISTING skills for these (don't reinvent)

| Ask | Use |
|---|---|
| Pick which signal × ICP × offer to test (from a URL) | `hypo-generator` |
| Build a persona × signal × angle hypothesis matrix | `hypothesis-builder` |
| The canonical signal LIST with trivial-trigger weights | `hypo-generator/signals-catalog.md` |
| Map a single buyer signal to messaging | `buyer-signal-mapper` |
| Run Clay/LinkedIn signal detection on a company list | `signal-research` |
| Score leads (general lead scoring) | `13-lead-scoring` |
| Score meeting/booking intent | `28-meeting-intent-scorer` |
| Write the actual outreach copy off the signal | `copy-generation`, `sequence-writer` |

## Response format

1. State whether the request is **strategy** (→ hand off to hypo-generator/06) or **operations** (→ handle here).
2. Apply the agency adaptation rules — strip PLG/enterprise noise, flag US-only/GDPR tools, demote enterprise pricing.
3. For any signal: give **detect (tool + Clay credits) → freshness window → score → GTM play**, in that order.
4. Quote benchmarks as directional only; never promise 35–40%.
