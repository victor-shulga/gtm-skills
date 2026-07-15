# Signals Catalog

Canonical reference for the `/hypo-generator` skill. All "Buying signal" values in generated hypotheses must come from this catalog.

Sources combined:
- **growth.band/signals-framework** — 15 signals (Dynamic + Static)
- **Maja Voje Outreach Triggers** — website, hiring, tech stack, events
- **Buying Triggers Template** — Individual / Account / Persona level (30 total)

---

## Core dichotomy: Signals vs Data Points

- **Dynamic signals** = time-bound events. Fire for ~3-5% of TAM at any moment. Tell you **when** to reach out. Strongest "trivial trigger" scores. Examples: hired a new SDR, raised a Series A.
- **Static data points** = facts about current state. Apply to ~100% of TAM. Tell you **what to say**. Weaker for timing but rich for messaging adaptation. Examples: 0 SDRs + 5 AEs, selling to CTOs.
- **Individual-level signals** = events tied to a specific person, not the company. Often the strongest for LinkedIn outreach. Examples: just changed role, posted on a relevant topic.

A strong hypothesis uses **one dynamic OR individual signal as the trigger**, plus one static data point to adapt the message.

---

## A. Dynamic signals (account-level, timing)

### A1. Hiring for specific roles
**What it signals:** Investment in a function. Hiring SDRs = building outbound. Hiring devs = scaling product. Hiring CSMs = focus on retention.
**Best use:** Match the role they're hiring to your offer ("hiring SDRs but no outbound infrastructure yet").
**Detection:** Clay, Bitscale, Trigify, LinkedIn job posts
**Trivial-trigger weight:** 4/5

### A2. Recent funding round
**What it signals:** Fresh budget, board pressure to grow, openness to new vendors. First 3-6 months post-raise = highest receptivity.
**Best use:** Lead with congrats + pipeline angle ("most companies post-raise prioritize pipeline but don't have the engine to match the ambition").
**Detection:** Crunchbase, Clay, Bitscale, Trigify
**Trivial-trigger weight:** 4/5 (high TAM relevance for some ICPs, low for others)

### A3. New decision-maker joined (90-day window)
**What it signals:** New leaders make changes in their first 90 days. They audit vendors, rethink processes. Most open window in the relationship.
**Best use:** Address the role directly ("you stepped into VP Sales 6 weeks ago — pipeline is the first thing").
**Detection:** Trigify, Clay, LinkedIn, Bitscale
**Trivial-trigger weight:** 5/5

### A4. Tech stack change
**What it signals:** Adopted new CRM/sales tool. First 6 months = rethinking everything around that tool.
**Best use:** Position your service as complementary to the new stack ("you started HubSpot recently — most teams rethink their entire lead gen process in the first 6 months").
**Detection:** BuiltWith, Clay, Bitscale
**Trivial-trigger weight:** 4/5

### A5. Rapid headcount growth
**What it signals:** Growing from 20 to 40 people in 6 months. Processes built for 20 break at 40. Need systems and external help.
**Best use:** "You doubled in 6 months. Teams that grow that fast usually find what worked at 20 ppl breaks at 40 — especially pipeline."
**Detection:** LinkedIn employee counts, Clay, Bitscale
**Trivial-trigger weight:** 3/5

### A6. SDR/AE job posting removed (failed-hire signal)
**What it signals:** Tried to hire for outbound, couldn't find someone or pulled the budget. Need still exists. Hiring approach failed.
**Best use:** "You were hiring for an SDR last month — listing's gone. What if you could get the pipeline without the headcount?"
**Detection:** Trigify, Clay (job posting history)
**Trivial-trigger weight:** 5/5

### A7. Event / conference attendance
**What it signals:** Attending or sponsoring events = investing in visibility, market-building mode. Open to pipeline conversations.
**Best use:** "Saw you're sponsoring [Event]. Companies investing in events usually need outbound to maximize lead follow-up."
**Detection:** LinkedIn posts, Clay, LLM analysis
**Trivial-trigger weight:** 3/5

### A8. New product / feature launch
**What it signals:** New market to sell into. Need pipeline for something they haven't sold before. Existing inbound won't cover it.
**Best use:** "Just saw you launched [product]. New products need pipeline fast — your existing inbound probably won't cover a new segment."
**Detection:** Bitscale, LLM analysis, LinkedIn announcements, press releases
**Trivial-trigger weight:** 4/5

### A9. Company expansion to new office/geography
**What it signals:** Physical expansion = growth + need for local pipeline.
**Best use:** "You're expanding to [city]. Teams entering new markets usually need 2-3 months to spin up local pipeline."
**Detection:** LinkedIn (location filter), Crunchbase, Bitscale
**Trivial-trigger weight:** 4/5

### A10. M&A activity (acquired or merged)
**What it signals:** New workflows, tools consolidation, organizational change. Often 12-18 months of churn.
**Best use:** "Post-merger teams usually consolidate tools and rebuild ops. Want to chat about how others have navigated this?"
**Detection:** Crunchbase, press releases, LinkedIn
**Trivial-trigger weight:** 4/5

### A11. New client / case study announcement
**What it signals:** Product is selling well, GTM works — but can be scaled. Confidence-building moment.
**Best use:** "Saw you landed [Client X]. Amazing — want to amplify it with similar accounts?"
**Detection:** LinkedIn posts, press releases
**Trivial-trigger weight:** 3/5

### A12. Layoffs / headcount decrease
**What it signals:** Financial pressure or restructuring. Either churn risk OR cost-saving play.
**Best use (cost-saving angle):** "Sorry to see the changes. If you're looking to reduce SDR overhead, we run pipeline as a service."
**Detection:** Layoffs.fyi, LinkedIn, Trigify
**Trivial-trigger weight:** 3/5 (sensitive — angle matters)

### A13. Award / recognition
**What it signals:** They're in the spotlight, often looking to ride momentum.
**Best use:** "Saw your award. Great time to build on that visibility with outbound to similar accounts."
**Detection:** LinkedIn, press, Bitscale
**Trivial-trigger weight:** 2/5

### A14. Strategic partnership / integration announcement
**What it signals:** Market expansion via partner ecosystem. Complementary product opportunity.
**Best use:** "Saw your integration with [X]. Let's help you scale activation across that user base."
**Detection:** LinkedIn, press releases
**Trivial-trigger weight:** 3/5

### A15. IPO / public listing
**What it signals:** Enterprise-readiness moment. Heavy compliance, structured GTM, larger budgets.
**Best use:** "Congrats on the IPO. Want to chat about scaling pipeline to public-market expectations?"
**Detection:** Public filings, Crunchbase
**Trivial-trigger weight:** 4/5

### A16. Website messaging change / repositioning
**What it signals:** Major homepage rewrite, new positioning. Often product or GTM strategy shift.
**Best use:** "Saw your new positioning around [X]. Curious if outbound has caught up with the new story?"
**Detection:** Wayback Machine, Bitscale, manual review
**Trivial-trigger weight:** 2/5

### A17. New regulation in their industry
**What it signals:** New rules → new way of doing things. Risk-mitigation appetite.
**Best use:** "[New regulation] hits [date]. Teams in your space usually spend 60 days rebuilding around it — we help with [angle]."
**Detection:** LLM analysis of industry news
**Trivial-trigger weight:** 3/5

### A18. New license issued / pre-opening (vertical: regulated retail) (added 2026-07-10, needs validation)
**What it signals:** A brand-new operator just got (or applied for) an operating license and will open in <6 months. They must buy their entire operational stack from zero before day one. Highest-intent moment in the lifecycle — no incumbent to displace.
**Best use:** "Congrats on the license. Before you lock in a POS — the #1 thing that trips up new operators in month one is compliance sync. Here's a launch checklist."
**Detection:** State/regulator public license databases, Cannabiz Media, license-list aggregators, LLM aggregation
**Trivial-trigger weight:** 5/5 (a new license deterministically needs the operational stack)

### A19. New market / jurisdiction goes live (regulation flip) (added 2026-07-10, needs validation)
**What it signals:** A whole jurisdiction flips status on a fixed date (e.g., med→adult-use, or a new legal market opening). Every licensed operator in it must re-tool for new volume + new compliance rules against a hard deadline. Time-boxed land-grab.
**Best use:** "[State] goes adult-use [date]. Med-only stores usually need to re-tool checkout + compliance for the volume jump — here's what changes."
**Detection:** Regulatory calendars, industry news, state regulator sites, LLM analysis
**Trivial-trigger weight:** 5/5 (hard deadline, whole-market cohort) — but episodic, not continuous

---

## B. Static data points (account-level, situation)

### B1. Sales team composition
**What it signals:** 0 SDRs + 5 AEs = AEs do everything. 1 SDR + 10 AEs = SDR can't keep up. Reveals whether outbound is systematic or ad-hoc.
**Best use:** "Your 5 AEs handle prospecting to close. That's 40% of their time on pipeline gen instead of selling."
**Detection:** LinkedIn (filter by title), Clay, Bitscale
**Best paired with:** A1, A5, A6 as the trigger.

### B2. In-house capability (or lack of)
**What it signals:** Having 2 in-house recruiters vs. zero = entirely different messaging. Presence/absence of a function changes the angle.
**Best use (has function):** "Your 2 recruiters handle everything. We'd give them pre-screened candidates so they focus on quality." (lack of):** "No recruitment team? We send 3-5 candidates free to prove fit."
**Detection:** LinkedIn, Clay, LLM analysis

### B3. Current tool stack
**What it signals:** Salesforce = enterprise. HubSpot = mid-market growing. No CRM = early stage. Tools reveal sophistication, budget, gaps.
**Best use:** "You're running HubSpot + Instantly. Good stack — but who's managing the deliverability layer underneath?"
**Detection:** BuiltWith, Clay, Bitscale

### B4. Who they sell to
**What it signals:** Selling to CTOs = skeptical, research-heavy audience. Selling to CMOs = inbox-flooded. Changes entire outbound approach.
**Best use:** "Your audience [CTO/CMO/etc.] researches before talking to sales. Only way in is perfect timing."
**Detection:** LLM analysis of their case studies + ICP, Bitscale, Clay

### B5. Geographic / team distribution
**What it signals:** Distributed team = timezone / cost optimization. Nearshore presence = already cost-aware. Reveals operational maturity.
**Best use:** "Your team is split between [City A] and [City B]. You've optimized engineering cost — have you done the same for pipeline?"
**Detection:** LinkedIn, Clay, LLM analysis

### B6. Revenue model / ACV indicators
**What it signals:** Enterprise pricing = high ACV, long cycles. Self-serve = low ACV, volume. ACV determines whether outbound math works.
**Best use:** "At your price point, one closed deal covers the entire outbound campaign. The math: [N] meetings × your close rate = ROI."
**Detection:** LLM analysis, Bitscale, Clay

### B7. Content / LinkedIn activity level
**What it signals:** Active poster = marketing-aware. No content = referral/outbound reliant.
**Best use (active):** "Your LinkedIn is generating engagement. But content is slow — what if outbound ran in parallel?"
**Detection:** LinkedIn, Exa, Bitscale

### B8. Has structured company description / strong metadata
**What it signals:** Public-facing maturity, positioning clarity.
**Best use:** "Saw your team focuses on [XYZ] — we help similar companies [outcome]."
**Detection:** Clay, Maja Voje pattern from website data

### B9. Ticker available (public company)
**What it signals:** Listed company → larger budgets, structured GTM, longer cycles.
**Best use:** Lead with public-company specifics (compliance, scale).
**Detection:** Clay, Crunchbase

### B10. Tech stack: competitor tool detected
**What it signals:** Solving a similar problem with a competitor. Displacement opportunity.
**Best use:** "Many teams switching from [Competitor] tell us it was too complex/pricey for what they needed."
**Detection:** BuiltWith, Clay, Bitscale

### B11. Tech stack: complementary / integration partner detected
**What it signals:** Easy positioning angle — your tool plugs in.
**Best use:** "Since you're using HubSpot already, our tool plugs right in — no migration."
**Detection:** BuiltWith, Clay

### B12. Customer base trajectory (increasing or decreasing)
**What it signals:** Increasing = double-down opportunity. Decreasing = churn/cashflow angle.
**Best use:** Mirror the trajectory in the offer framing.
**Detection:** Press releases, LinkedIn announcements, LLM review

---

## C. Individual-level signals (person-specific, best for LinkedIn)

### C1. Self-authored content — LinkedIn post
**What it signals:** They wrote and shared something publicly. Strongest possible relevancy hook.
**Best use:** "Your post on [topic] last week — the take on [specific point] matched something we're seeing across [their ICP]."
**Detection:** LinkedIn, Trigify, Exa
**Difficulty:** Easy
**Trivial-trigger weight:** 5/5

### C2. Self-authored content — webinar / podcast
**What it signals:** Hosted or guested on a webinar/podcast in your space.
**Best use:** Reference a specific point they made.
**Detection:** Search engines, LinkedIn, podcast platforms
**Difficulty:** Easy

### C3. Engaged content — commented on a relevant post
**What it signals:** Active interest in the topic. Lower commitment than authoring, but signals attention.
**Best use:** "Saw your comment on [post about X] — your point about [Y] is exactly what we're solving for."
**Detection:** LinkedIn, Trigify
**Difficulty:** Easy

### C4. Engaged content — liked/shared a relevant post
**What it signals:** Passive interest signal. Use carefully — easy to over-fire.
**Detection:** LinkedIn, Trigify
**Difficulty:** Easy

### C5. New to role (last 90 days)
**What it signals:** Starting a new position, building credibility, looking for quick wins. Most receptive window.
**Best use:** "Congrats on the new role. Whenever someone steps into [title], pipeline is usually the first audit."
**Detection:** LinkedIn, Trigify
**Difficulty:** Easy
**Trivial-trigger weight:** 5/5

### C6. Change of role (internal promotion or lateral move)
**What it signals:** Expanded scope, often new budget authority.
**Best use:** Match the new responsibilities to your offer.
**Detection:** LinkedIn, Trigify
**Difficulty:** Medium

### C7. Award / recognition received
**What it signals:** Visibility moment. Lower commercial signal but warm starting point.
**Detection:** LinkedIn, search

### C8. Dissatisfaction with current vendor (review left)
**What it signals:** Active displacement window. Strong signal but rare and hard to find at scale.
**Best use:** Lead with the specific pain they mentioned in the review.
**Detection:** G2, Capterra, TrustRadius scraping
**Difficulty:** Hard

### C9. Self-attributed traits (LinkedIn headline / about / experience)
**What it signals:** What they want to be known for. Direct messaging hook.
**Best use:** "Saw your headline mentions [trait] — that's the exact profile we built [solution] for."
**Detection:** LinkedIn, Clay
**Difficulty:** Medium

### C10. Reverse IP / first-party intent
**What it signals:** Visited your site (anonymously detected). Active research.
**Detection:** RB2B, Clearbit Reveal, Snitcher
**Difficulty:** Medium (needs site instrumentation)

---

## D. How to pair signals for a strong hypothesis

A hypothesis = **one trigger** (Dynamic OR Individual) + **one or two static data points** to adapt the message.

**Strong pairings:**
- A1 (hiring SDRs) + B1 (current 0 SDRs / 5 AEs) → "You're hiring SDRs but your 5 AEs are already doing all prospecting"
- A2 (recent funding) + B6 (ACV indicator) → "Post-raise, you need pipeline matching the new ARR target — your current ACV says [math]"
- A6 (pulled SDR job) + B2 (no in-house outbound team) → "Tried hiring an SDR, withdrew the role. We run outbound without the headcount"
- A4 (started using HubSpot) + B3 (broader stack) → "6 months into HubSpot — most teams rethink lead gen entirely at this point"
- C5 (new in role) + B4 (who they sell to) → "New to VP Sales. Your buyers are CTOs — toughest audience to cold-email"

**Weak pairings to avoid:**
- A13 (award) + B7 (active LinkedIn) → both are "they're visible" — no problem hook
- A11 (new client) + B12 (growing customer base) → tautological, no contrast

---

## E. Tools by signal coverage

| Tool | Strongest for |
|---|---|
| **Clay** | Almost everything — primary enrichment + signal detection layer |
| **Bitscale** | LLM enrichment, custom signal research, static data points at scale |
| **Trigify** | LinkedIn-native real-time signals (new role, SDR removed, posts) |
| **BuiltWith** | B3, B10, B11 (tech stack) |
| **Crunchbase** | A2, A9, A10, A15 (funding, M&A, IPO) |
| **LinkedIn (Sales Nav)** | TAM definition, A1, A5, B1, B2, B5, C-series |
| **Apollo** | Initial list building, TAM sizing, basic enrichment |
| **Exa / search APIs** | C1, C2 (authored content) |

---

## F. Maintaining this catalog

If a new signal comes up that doesn't fit any of A/B/C above:
1. Add it with a new ID (A18, B13, C11 as appropriate)
2. Include: what it signals, best-use cold-email framing, detection tool, trivial-trigger weight
3. Tag with `(added YYYY-MM-DD, needs validation)` until at least one campaign has tested it

If a signal proves unreliable after 3+ campaigns (low scoring or no replies), tag it `(unreliable — avoid)` instead of deleting — that history is itself useful.
