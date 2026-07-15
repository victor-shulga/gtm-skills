# Hypothesis Report — Northcrest Labs (FICTIONAL EXAMPLE)
Generated: 2026-05-12 · Source: https://northcrest.example/

> This is a fictional example used as a formatting reference for the `/hypo-generator` skill. Do not use the hypotheses below for actual outreach — Northcrest Labs does not exist.

## Executive summary
- **Strongest hypothesis:** H03 — "Funded fintech founders post-Series A, no in-house mobile team" — total 4.70 — Trivial trigger 5 + Clear problem 5 + exact case study match
- **Weakest hypothesis kept:** H09 — "UK SaaS founders selling to CTO, no outbound" — total 2.60 — below the 3.0 threshold but kept as a portfolio long-shot since the problem framing is strong
- **Recommended starting batch:** H01, H03, H05 — total addressable accounts ≈ 1,800
- **Key portfolio risk:** 6 of 10 hypotheses lean on Series A/B funding signals. If funding velocity drops in the next quarter, half the matrix degrades simultaneously. Worth seeding 2-3 hypotheses on non-funding triggers (A4, A6, B2) as insurance.

## Phase 1 — What I extracted from the site
- **Services:** Custom software development, mobile app dev (iOS/Android), MVP discovery sprints, post-launch product engineering, AI/ML feature integration
- **Existing use cases:** "MVP in 90 days for SaaS founders" / "Scale-up product engineering for Series A-B teams" / "Mobile app for fintech compliance workflows"
- **Vertical / industry signals:** Strong fintech track record (3 of 5 case studies). Healthtech mentioned but only 1 case. SaaS B2B mentioned generally but no specific cases.
- **Case studies with numbers:**
  - **Vellam (fintech, Series A):** Cut deploy time from 14 days to 2; MRR grew 3.2× in 9 months post-launch
  - **Loop Lending (fintech, seed):** Built compliance KYC flow in 11 weeks; passed FCA audit on first try
  - **Beacon Health (healthtech, undisclosed):** Reduced patient-onboarding clicks by 60% (no revenue number disclosed)
- **Geographic signals:** HQ Manchester UK, team distributed UK + Poland + Ukraine. Site copy targets US and UK markets explicitly ("we work with founders on both sides of the Atlantic").
- **Tech stack signals:** Mentions of TypeScript, React Native, FastAPI, Postgres, AWS. No platform-specific positioning (e.g., not a "Salesforce shop").
- **Gaps I had to ask Viktor about:**
  - Confirmed: US is the priority market (revenue-wise); UK is secondary
  - Confirmed: No-go on crypto and gambling
  - Confirmed: Beacon Health case can be used as proof despite no public revenue number — they have a quote from the client

---

## Hypotheses (sorted by total score, descending)

> Example note: the order shown below is illustrative of the structure. In a real agent run, hypotheses are strictly sorted by Total descending: H03 (4.70) → H01 (4.10) → H02 (4.10) → H05 (4.00) → H06 (3.70) → H04 (3.40) → H08 (3.10) → H07 (3.00) → H10 (2.90) → H09 (2.60).

### H03 — Funded fintech founders post-Series A, no in-house mobile team — Total: 4.70 ✅ Run first

| Field | Value |
|---|---|
| ICP | US fintech, Series A or A+, 30-150 people |
| Persona (primary) | Founder / CEO |
| Buying committee | • CTO (technical evaluator) <br> • Head of Product (scope owner) <br> • Investor on board (gates timeline) |
| Geo | US (NYC, SF, Boston, Austin) |
| Subindustry | Embedded fintech, lending, payments |
| Problem | Just raised $8-20M Series A. Board expects a mobile product or new vertical in 6-9 months. Hiring 4-6 mobile engineers takes 4 months and burns $400K/yr. Window is closing. |
| Buying signal | A2 (recent funding round) + A1 (hiring mobile devs) — both must be true |
| Offer | "Ship a production mobile app in 16 weeks with our embedded squad — your in-house team focuses on core product" |
| Case study / Proof | Vellam — fintech Series A, 14→2 day deploy time, 3.2× MRR in 9 months |
| TAM | ≈ 250-400 US fintech accounts post-Series A in last 6 months (Crunchbase + LinkedIn cross-filter) |
| Test batch | 200 accounts |

**Scoring:**
- Easy to scrape: 5 (0.75) — Crunchbase Series A filter + LinkedIn "mobile engineer" job filter, both API-accessible
- Scaling: 3 (0.45) — TAM is mid-size; would saturate in 6-9 months without rotating to A or A+ rounds
- Clear & expensive problem: 5 (1.25) — Hiring delay = missed board commitment = direct revenue loss
- Offer relevance: 5 (1.00) — Vellam case is an exact match: fintech, Series A, mobile, real numbers
- Trivial trigger: 5 (1.25) — A2 + A1 combination is unambiguous; the "we raised → we need mobile → we can't hire fast enough" logic is straightforward
- **Total: 4.70 / 5.0**

---

### H01 — US fintech CTOs at HubSpot CRM transition (first 6 months) — Total: 4.15 ✅ Run first

| Field | Value |
|---|---|
| ICP | US fintech, Series A-B, 50-200 people |
| Persona (primary) | CTO |
| Buying committee | • VP Eng (deputy) <br> • Head of Sales (CRM stakeholder) <br> • RevOps Lead (integrations) |
| Geo | US |
| Subindustry | B2B fintech (lending, payments, treasury) |
| Problem | Just adopted HubSpot 3-5 months ago. Sales team wants custom workflows + product-data sync, but in-house eng is buried with core product. Workflows getting hacked together in Zapier, breaking weekly. |
| Buying signal | A4 (tech stack change — HubSpot adoption, last 6 months) + B3 (full stack including dev tools, no integration platform) |
| Offer | "HubSpot integration sprint: ship 5 custom workflows + product-data sync in 4 weeks, no in-house eng time required" |
| Case study / Proof | Loop Lending — built compliance KYC integration in 11 weeks, FCA-pass on first try (proof of integration competence; not HubSpot-specific) |
| TAM | ≈ 600-900 US fintech accounts with HubSpot in last 6 months (BuiltWith + Crunchbase) |
| Test batch | 300 accounts |

**Scoring:**
- Easy to scrape: 5 (0.75) — BuiltWith detects HubSpot install date precisely
- Scaling: 5 (0.75) — TAM is large; ~3-5% of TAM enters this state every quarter (rolling supply)
- Clear & expensive problem: 5 (1.25) — Sales <> product data gap = closed-won attribution broken = wrong investment decisions
- Offer relevance: 3 (0.60) — Agency has integration competence but no HubSpot-specific case study with numbers. Stretch but defensible
- Trivial trigger: 3 (0.75) — A4 fires reliably but "they need integration help" is not guaranteed; some teams handle it in-house
- **Total: 4.10 / 5.0**

---

### H05 — Failed SDR hire at UK SaaS, no outbound infra — Total: 3.85 ✅ Run first

| Field | Value |
|---|---|
| ICP | UK B2B SaaS, 20-80 people, founder-led sales |
| Persona (primary) | Founder / CEO |
| Buying committee | • Head of Growth (if exists) <br> • First AE (if exists) |
| Geo | UK |
| Subindustry | B2B SaaS, vertical SaaS, dev tools |
| Problem | Tried to hire an SDR — posted job for 2-4 months, withdrew it. Either couldn't find someone or burned out on cost. Pipeline gap remains. AE (if there is one) is doing prospecting + closing — burned out. |
| Buying signal | A6 (SDR/AE job posting removed) + B1 (sales team composition: 1-3 AEs, 0 SDRs) |
| Offer | "Outbound-as-a-service for UK SaaS founders: we build the pipeline, your AE closes. No SDR hire needed." |
| Case study / Proof | TBD — no matching SaaS-only case on site, recommend Loop Lending (UK, B2B-adjacent) as fallback with disclaimer |
| TAM | ≈ 400-600 UK B2B SaaS in this size range (LinkedIn + Trigify job-posting-history filter) |
| Test batch | 200 accounts |

**Scoring:**
- Easy to scrape: 3 (0.45) — Trigify catches the SDR-withdrawal signal but requires polling; less common than other tools support
- Scaling: 3 (0.45) — UK SaaS is mid-size TAM; signal fires for maybe 1-2% per quarter
- Clear & expensive problem: 5 (1.25) — Founder-led sales burnout is a top-3 churn driver in early-stage SaaS
- Offer relevance: 3 (0.60) — Agency doesn't have a clear SaaS-outbound case study; offer is real but proof is weak
- Trivial trigger: 5 (1.25) — A6 is one of the highest-conviction signals; the buyer essentially raised their hand
- **Total: 4.00 / 5.0**

---

### H02 — New CTO at US Series B, first 90 days — Total: 3.80 ✅ Run first

| Field | Value |
|---|---|
| ICP | US tech, Series B, 100-300 people |
| Persona (primary) | New CTO (within 90 days of role start) |
| Buying committee | • Founder/CEO (sponsor) <br> • VP Eng (peer, sometimes threat) <br> • Head of Product (collaborator) |
| Geo | US |
| Subindustry | Vertical SaaS, B2B platforms, ecom infrastructure |
| Problem | First-90-day CTOs audit everything: stack, vendor mix, team allocation. They look for credibility wins: ship something visible, fast. In-house team is mid-roadmap; can't pivot for a new initiative. |
| Buying signal | A3 (new decision-maker joined — CTO, within 90 days) |
| Offer | "First-90-day momentum sprint: ship one visible initiative (mobile, AI feature, redesign) in 8 weeks while your team stays on roadmap" |
| Case study / Proof | Vellam — Series A fintech, 3.2× MRR. Adjacent but proves we ship at startup speed |
| TAM | ≈ 800-1200 US Series B with CTO change in last 90 days (LinkedIn + Crunchbase cross-filter) |
| Test batch | 300 accounts |

**Scoring:**
- Easy to scrape: 5 (0.75) — LinkedIn date-of-role-change filter, Trigify alerting
- Scaling: 5 (0.75) — High TAM, ~5% of Series B+ has a CTO change every 6 months
- Clear & expensive problem: 3 (0.75) — Real problem but not always financial pressure; depends on the individual
- Offer relevance: 3 (0.60) — Agency can deliver but doesn't have a CTO-sponsored case study to point to
- Trivial trigger: 5 (1.25) — A3 is one of the strongest signals; first-90-day buyers are well-documented as receptive
- **Total: 4.10 / 5.0** (note: ties with H01; tiebreaker = offer relevance, H01 wins on that field)

---

### H04 — US fintech with growing customer base, no mobile yet — Total: 3.55 🟡 Worth testing

| Field | Value |
|---|---|
| ICP | US fintech, Series A-B, 50-200 people, web-only product |
| Persona (primary) | Head of Product |
| Buying committee | • CTO <br> • Founder <br> • Head of Customer Success |
| Geo | US |
| Subindustry | Fintech (consumer-facing or SMB-facing) |
| Problem | Customer base grew 2× in last 12 months. Mobile usage is 60%+ but they have web-only or PWA. Customer complaints about mobile UX are rising in support tickets. |
| Buying signal | B12 (customer base trajectory — growing) + static observation (no mobile app detected in App Store / Play Store) |
| Offer | "Mobile MVP in 16 weeks for fintechs hitting product-market fit on web" |
| Case study / Proof | Vellam (fintech mobile) — exact match |
| TAM | ≈ 500-700 US fintech web-only with growth signals (LinkedIn + App Store inverse-filter) |
| Test batch | 200 accounts |

**Scoring:**
- Easy to scrape: 3 (0.45) — Combining "no mobile app" + "growing" requires manual review or LLM enrichment
- Scaling: 3 (0.45) — Mid-size TAM, but the signal is largely static (growing customer base is hard to detect time-bound)
- Clear & expensive problem: 5 (1.25) — Mobile UX gap = retention loss in fintech specifically
- Offer relevance: 5 (1.00) — Vellam case is an exact fit
- Trivial trigger: 1 (0.25) — "Growing customer base + no mobile" is inferential, not a single observable event
- **Total: 3.40 / 5.0**

---

### H06 — UK fintech post-funding, hiring AI/ML — Total: 3.70 ✅ Run first

| Field | Value |
|---|---|
| ICP | UK fintech, Series A or seed extension, 25-100 people |
| Persona (primary) | CTO |
| Buying committee | • Founder <br> • Head of Data |
| Geo | UK |
| Subindustry | Fintech (lending, fraud, treasury) |
| Problem | Hiring AI/ML engineers but the team has no AI infrastructure yet. Will take 6 months to assemble. Meanwhile, competitors are shipping AI features now. |
| Buying signal | A2 (recent funding) + A1 (hiring AI/ML roles, last 60 days) |
| Offer | "AI feature sprint: ship a production ML feature in 12 weeks while you build the in-house team" |
| Case study / Proof | TBD — no AI/ML case study disclosed publicly. Recommend internal proof or fast PoC offer |
| TAM | ≈ 150-250 UK fintech post-funding with AI hiring (Crunchbase + LinkedIn jobs) |
| Test batch | 150 accounts |

**Scoring:**
- Easy to scrape: 3 (0.45) — Crunchbase + LinkedIn jobs API both work but require chaining
- Scaling: 1 (0.15) — UK fintech with both signals is small (<300 accounts)
- Clear & expensive problem: 5 (1.25) — "Competitor shipping AI" is among the strongest urgency frames in fintech
- Offer relevance: 3 (0.60) — Agency has eng capability but no AI/ML case on the site
- Trivial trigger: 5 (1.25) — Two strong signals combined; high conviction
- **Total: 3.70 / 5.0**

---

### H07 — US healthtech, recent funding, no engineering scale — Total: 3.30 🟡 Worth testing

| Field | Value |
|---|---|
| ICP | US healthtech, Series A, 20-80 people |
| Persona (primary) | CTO or Head of Product |
| Buying committee | • Founder/CEO <br> • Chief Medical Officer (compliance gate) |
| Geo | US |
| Subindustry | Digital health, patient engagement, clinical workflow |
| Problem | Just raised Series A but engineering team is 3-6 people. Roadmap is 12 months, runway pressure is now. Can't hire fast enough; in-house culture won't accept outsourcing core product. |
| Buying signal | A2 (recent funding) — healthtech filter |
| Offer | "Embedded engineering squad — we work as your team, your culture, your standup. 8-12 weeks per initiative." |
| Case study / Proof | Beacon Health — 60% reduction in onboarding clicks (no revenue number but quote available) |
| TAM | ≈ 200-300 US healthtech Series A in last 6 months |
| Test batch | 150 accounts |

**Scoring:**
- Easy to scrape: 5 (0.75) — Crunchbase healthtech filter is well-defined
- Scaling: 1 (0.15) — Small TAM, slow rotation
- Clear & expensive problem: 3 (0.75) — Real but not all funded healthtechs have the eng capacity problem
- Offer relevance: 3 (0.60) — Beacon Health is the only healthtech proof; one case is thin
- Trivial trigger: 3 (0.75) — A2 alone is moderate; would be stronger paired with A1 or B1
- **Total: 3.00 / 5.0**

---

### H08 — US Series B with HubSpot, new VP Sales in first 90 days — Total: 3.20 🟡 Worth testing

| Field | Value |
|---|---|
| ICP | US B2B SaaS or fintech, Series B, 80-250 people |
| Persona (primary) | New VP Sales (within 90 days) |
| Buying committee | • CRO (if exists) <br> • RevOps Lead <br> • Founder (gate for big spends) |
| Geo | US |
| Subindustry | Mixed |
| Problem | New VP Sales inheriting a HubSpot setup they didn't build. First 90 days = audit. Want custom workflows + reporting they can present to the board next quarter. |
| Buying signal | A3 (new decision-maker — VP Sales) + B3 (HubSpot in stack) |
| Offer | "HubSpot revamp sprint for new VP Sales: rebuild reporting + workflows in 4 weeks, ready for your first board update" |
| Case study / Proof | TBD — no HubSpot-specific case |
| TAM | ≈ 400-600 US Series B with VP Sales change + HubSpot |
| Test batch | 200 accounts |

**Scoring:**
- Easy to scrape: 3 (0.45) — Two filters needed (LinkedIn role-change + BuiltWith HubSpot)
- Scaling: 3 (0.45) — Mid-size TAM
- Clear & expensive problem: 3 (0.75) — Real but lower urgency than founder-level pains
- Offer relevance: 1 (0.20) — No HubSpot case study; offer is generic-sounding
- Trivial trigger: 5 (1.25) — A3 is strong; B3 confirms tooling
- **Total: 3.10 / 5.0**

---

### H09 — UK SaaS founders selling to CTO, no outbound — Total: 2.60 ❌ Skip or rework (kept as portfolio long-shot)

| Field | Value |
|---|---|
| ICP | UK B2B SaaS, 10-60 people, technical buyer |
| Persona (primary) | Founder / CEO |
| Buying committee | • First AE <br> • Technical co-founder |
| Geo | UK |
| Subindustry | Dev tools, infra SaaS, technical B2B |
| Problem | Selling to CTOs is uniquely hard: skeptical audience, generic outbound gets ignored, founders give up after 1-2 campaigns. They run on referrals + content but pipeline is unreliable. |
| Buying signal | B4 (who they sell to — CTO/technical buyer) + B1 (no SDR, founder-led sales) |
| Offer | "Outbound for technical-buyer SaaS: signal-based campaigns that get replies from CTOs. We've cracked this." |
| Case study / Proof | TBD — agency doesn't have a dev-tools case |
| TAM | ≈ 300-500 UK dev-tools SaaS in this range |
| Test batch | 150 accounts |

**Scoring:**
- Easy to scrape: 3 (0.45) — LLM analysis of their site + LinkedIn for team comp
- Scaling: 3 (0.45) — Niche TAM but stable
- Clear & expensive problem: 5 (1.25) — Selling to CTOs is documented top-3 hardest GTM motion
- Offer relevance: 1 (0.20) — Agency itself sells dev work, not outbound. This offer would be a stretch unless Northcrest partners with a GTM consultancy
- Trivial trigger: 1 (0.25) — Pure static-data hypothesis; no timing
- **Total: 2.60 / 5.0** — borderline kill; included for portfolio coverage of UK SaaS but lowest priority

---

### H10 — UK healthtech, repositioning recently — Total: 2.90 ❌ Skip or rework (kept as wild-card)

| Field | Value |
|---|---|
| ICP | UK healthtech, 30-120 people |
| Persona (primary) | Founder or Head of Product |
| Buying committee | • CTO <br> • Chief Medical Officer |
| Geo | UK |
| Subindustry | Digital health |
| Problem | Major website repositioning in last 6 months suggests product or GTM strategy pivot. Engineering roadmap usually lags strategy by 3-6 months. Need execution muscle. |
| Buying signal | A16 (website messaging change — major repositioning) |
| Offer | "Reposition-to-launch sprint: turn your new strategy into shipped product in 16 weeks" |
| Case study / Proof | Beacon Health (UK adjacent — UK healthtech proof) |
| TAM | ≈ 150-250 UK healthtech with site changes in last 6 months |
| Test batch | 100 accounts |

**Scoring:**
- Easy to scrape: 1 (0.15) — Detecting "major repositioning" needs LLM analysis + Wayback comparison; expensive at scale
- Scaling: 1 (0.15) — Small TAM, slow signal cadence
- Clear & expensive problem: 5 (1.25) — Reposition-without-execution gap is acute and well-known
- Offer relevance: 3 (0.60) — Beacon case proves healthtech competence
- Trivial trigger: 3 (0.75) — A16 is a real signal but inferential
- **Total: 2.90 / 5.0** — kept as wild-card long-shot

---

## Post-launch reference (Kill / Optimize / Scale)

After running each hypothesis with at least 200 accounts:
- **Kill:** reply rate < 1% OR interest rate (positive replies / all replies) < 17% → hypothesis disproven, find new signal or angle
- **Optimize:** interest rate 17–30% → potential. Test new copy angles, refine data filters, keep running
- **Scale:** interest rate > 30% → validated. Add LinkedIn channel, increase volume, promote to Tier 1

Speed of testing > polish. Get H01 + H03 + H05 live in 7 days, not 1 hypothesis perfected in 30.

## Next steps for Viktor's client (Northcrest Labs)

1. Validate TAM numbers in Apollo / Sales Navigator for H01, H03, H05 (top 3)
2. Build account lists in Clay using:
   - H01: BuiltWith HubSpot + Crunchbase Series A-B + LinkedIn US fintech filter
   - H03: Crunchbase Series A last 6 months + LinkedIn mobile engineer job posts active
   - H05: Trigify SDR job-removed alert (UK filter) + LinkedIn AE-only team comp
3. Draft 2 copy variants per hypothesis (timing-led + problem-led angles)
4. Set up tracking dashboard: reply rate + interest rate per hypothesis, not per campaign
5. Schedule 7-day review checkpoint with Viktor: which hypotheses to kill, which to optimize, which to scale

## Recommended portfolio rebalancing (Viktor's note)

The matrix leans heavily on funding signals (A2 appears in H03, H06, H07, indirectly H08). If US fintech funding velocity drops next quarter, four hypotheses degrade together. Worth adding 2-3 hypotheses on non-funding triggers in the next iteration:
- A4 (HubSpot adoption) ✅ already in H01
- A6 (failed SDR hire) ✅ already in H05
- C5 (new in role — beyond CTO) — currently only A3 used in H02, H08
- B2 (in-house capability gap) — not used at all in this matrix

Consider rerunning this skill in 30 days with the rebalancing in mind.
