# Signals Catalog

> **Where this file lives.** A copy travels with `signal-research` so the skill is self-contained;
> the same catalogue ships with `hypo-generator`. When you add or retire a signal, keep the ids
> stable and update both — otherwise a signal id means different things in different skills.

Canonical reference for the `/hypo-generator` skill. Every "Buying signal" value in a generated hypothesis must come from this catalog.

**Architecture (v2, 2026-07-16):**
- **Universal signals (U01–U34)** — cross-vertical. Fire for any client (SaaS/dev, GIS, AEC, iGaming). This is the kept generic layer.
- **Vertical packs (V-series)** — industry-specific signals that make a niche ICP non-trivial. First pack shipped: **AEC / construction (V01–V16)** for structural/architecture/BIM outsourcing clients. Add more packs over time (one `## Vertical pack — <name>` section each).
- **Data points** — static facts, split the same way: Universal (D01–D10) + AEC (DV01–DV15).

**Total: 50 signals (34 U + 16 V) · 25 data points (10 D + 15 DV).**

Sources combined: growth.band signals-framework · Maja Voje outreach triggers · Buying-Triggers template (Individual/Account/Persona) · Trigify companies/news/jobs/tech datasets · field experience in AEC outsourcing.

---

## Core dichotomy: Signals vs Data Points

- **Signal** = time-bound event. Fires for ~3–5% of TAM at any moment. Tells you **WHEN** to reach out. Strongest trigger scores.
- **Data point** = static fact about current state. Applies to ~100% of TAM. Tells you **WHAT to say**. Weak for timing, rich for message adaptation.
- **Individual-level signal** = event tied to a specific person, not the company. Usually strongest for LinkedIn.

A strong hypothesis = **one signal as the trigger** + **one or two data points** to adapt the message.

**Every run scores signals & data points for FIT against the target ICP** — see `SKILL.md` → Phase 2 (Fit analysis). The catalog is the library; the fit pass picks what actually fits the vertical. For a niche vertical (e.g. structural engineering), generic Universal signals like funding/IPO will score 1–2 and drop out; the AEC pack carries the run.

---

# UNIVERSAL SIGNALS (U01–U34)

Cross-vertical. Kept generic on purpose — reused across all of Viktor's clients.

## Corporate / account events

### U01. Recent funding round
**Signals:** fresh budget, board pressure to grow, vendor openness. First 3–6 mo post-raise = peak receptivity.
**Best use:** congrats + capacity/pipeline angle matched to the new ambition.
**Detection:** Crunchbase, Clay, PredictLeads, Intellizence · **Window:** 0–90 days · **Trigger weight:** 4/5
**Fit note:** high for VC-backed SaaS; **low (1–2) for AEC/services** — those firms rarely raise.

### U02. M&A (acquired or merged)
**Signals:** new workflows, tool consolidation, org churn (12–18 mo).
**Best use:** "post-merger teams rebuild ops — want to compare notes?"
**Detection:** Crunchbase, PredictLeads, press · **Window:** 30–90 days · **Trigger weight:** 4/5

### U03. IPO / public listing
**Signals:** enterprise-readiness moment, compliance, structured GTM, bigger budgets.
**Detection:** SEC filings, Crunchbase · **Window:** 60–180 days · **Trigger weight:** 4/5
**Fit note:** low for private services firms.

### U04. New office / geographic expansion
**Signals:** growth + need for local capacity/pipeline.
**Detection:** LinkedIn location filter, Crunchbase, press · **Window:** 30–90 days · **Trigger weight:** 4/5

### U05. Rapid headcount growth
**Signals:** processes built for N break at 2N; systems/external help needed.
**Detection:** LinkedIn employee counts, Clay · **Window:** rolling · **Trigger weight:** 3/5

### U06. Layoffs / headcount decrease
**Signals:** financial pressure OR restructuring. Churn risk OR cost-saving opening.
**Best use:** cost-saving angle ("get the output without the headcount").
**Detection:** Layoffs.fyi, LinkedIn, Trigify · **Window:** 0–60 days · **Trigger weight:** 3/5 (angle-sensitive)

### U07. New product / service launch
**Signals:** new market to sell into; need capacity/pipeline fast for something unproven.
**Detection:** press, Serper, company blog, LinkedIn · **Window:** 14–60 days · **Trigger weight:** 4/5

### U08. Strategic partnership / integration announced
**Signals:** ecosystem expansion; complementary opportunity.
**Detection:** LinkedIn, press · **Window:** 14–60 days · **Trigger weight:** 3/5

### U09. New client / case-study win announced
**Signals:** GTM works and can be scaled; confidence moment.
**Detection:** LinkedIn posts, press · **Window:** 0–45 days · **Trigger weight:** 3/5

### U10. Award / recognition (firm)
**Signals:** in the spotlight, riding momentum.
**Detection:** LinkedIn, press, Bitscale · **Window:** 0–60 days · **Trigger weight:** 2/5

### U11. Website repositioning / messaging change
**Signals:** major homepage rewrite → product or GTM strategy shift.
**Detection:** Wayback Machine, Claygent scrape · **Window:** 30–60 days · **Trigger weight:** 2/5

### U12. New regulation in their industry
**Signals:** new rules → new way of working; risk-mitigation appetite.
**Detection:** LLM analysis of industry news · **Window:** deadline-driven · **Trigger weight:** 3/5

### U13. New leadership / C-suite change (account-level)
**Signals:** new exec = new priorities, vendor audit, "vendor amnesty".
**Detection:** LinkedIn, Trigify, Clay · **Window:** days 14–90 · **Trigger weight:** 4/5

## Hiring

### U14. Hiring for a specific role (function investment)
**Signals:** building a function. The role hired = the gap. **Instantiate per vertical:** SDR → outbound; Revit modeler/structural drafter → drafting capacity; ML eng → data maturity.
**Best use:** match the hired role to your offer ("hiring drafters but PEs still doing CDs").
**Detection:** LinkedIn Jobs, PredictLeads, Clay, Trigify · **Window:** 14–60 days · **Trigger weight:** 4/5

### U15. Failed hire — role pulled after long open
**Signals:** tried to hire, couldn't fill or lost budget. Need still exists; the hire path failed.
**Best use:** "listing's gone — what if you got the output without the headcount?"
**Detection:** Trigify, Clay (job-posting history) · **Window:** 0–30 days after removal · **Trigger weight:** 5/5

### U16. Hiring surge (5+ open roles)
**Signals:** funding or high-growth; capacity crunch.
**Detection:** LinkedIn Jobs, PredictLeads · **Window:** 30–90 days · **Trigger weight:** 3/5

### U17. Job post mentions a specific tool / stack
**Signals:** confirmed stack → personalize by integration or displacement. **Instantiate per vertical:** HubSpot; Tekla/SDS2/RISA/ETABS/Revit for AEC.
**Detection:** LinkedIn JD text, TheirStack, Clay · **Window:** while live · **Trigger weight:** 4/5

### U18. Job post uses pain language
**Signals:** "overtime", "fast-paced", "deadline-driven", "wear many hats", "CD crunch" → capacity pain in their own words.
**Detection:** LinkedIn JD text, Claygent · **Window:** while live · **Trigger weight:** 4/5

### U19. Repeated repost of the same req
**Signals:** chronic unfilled need → outsource-ready.
**Detection:** Trigify, Clay job history · **Window:** rolling · **Trigger weight:** 4/5

## Tech

### U20. New tech adoption (first-seen)
**Signals:** evolving stack; first 6 mo = rethinking everything around the new tool.
**Detection:** BuiltWith, TheirStack, HG Insights · **Window:** 30–90 days · **Trigger weight:** 4/5

### U21. Tech stack removal / vendor switch
**Signals:** vendor churn → active replacement window.
**Detection:** BuiltWith, HG Insights · **Window:** 0–30 days · **Trigger weight:** 4/5

### U22. Competitor tool detected (displacement)
**Signals:** solving the same problem with a competitor.
**Detection:** BuiltWith, Clay · **Window:** near renewal · **Trigger weight:** 3/5

### U23. Complementary / integration partner detected
**Signals:** easy "plugs right in" angle.
**Detection:** BuiltWith, Clay · **Window:** rolling · **Trigger weight:** 3/5

## Individual-level (best for LinkedIn)

### U24. Self-authored content — LinkedIn post
**Signals:** wrote & shared publicly. Strongest relevancy hook.
**Detection:** LinkedIn, Trigify, Exa · **Difficulty:** Easy · **Trigger weight:** 5/5

### U25. Self-authored — webinar / podcast / article
**Signals:** hosted or guested in your space.
**Detection:** search, LinkedIn, podcast platforms · **Difficulty:** Easy

### U26. Engaged content — commented on a relevant post
**Signals:** active topical interest.
**Detection:** LinkedIn, Trigify · **Difficulty:** Easy

### U27. Engaged content — liked / shared
**Signals:** passive interest. Use carefully (easy to over-fire).
**Detection:** LinkedIn, Trigify · **Difficulty:** Easy

### U28. New to role (last 90 days)
**Signals:** building credibility, seeking quick wins. Most receptive window.
**Detection:** LinkedIn, Trigify, LoneScale, Champify · **Difficulty:** Easy · **Trigger weight:** 5/5

### U29. Change of role / internal promotion
**Signals:** expanded scope, often new budget authority.
**Detection:** LinkedIn, Trigify · **Difficulty:** Medium

### U30. Self-attributed traits (headline / about / experience)
**Signals:** what they want to be known for → direct hook.
**Detection:** LinkedIn, Clay · **Difficulty:** Medium

### U31. Dissatisfaction with current vendor (review left)
**Signals:** active displacement. Strong but rare/hard at scale.
**Detection:** G2, Capterra, TrustRadius scrape · **Difficulty:** Hard

### U32. Reverse IP / first-party intent
**Signals:** anonymously visited your site → active research.
**Detection:** RB2B, Clearbit Reveal, Snitcher · **Difficulty:** Medium (needs site pixel)

### U33. Award / recognition (individual)
**Signals:** visibility moment; warm opener.
**Detection:** LinkedIn, search · **Difficulty:** Easy

### U34. Events — attending / exhibiting (generic)
**Signals:** market-building mode; reason to reach out.
**Detection:** LinkedIn posts, event sites, Clay · **Window:** around event date · **Trigger weight:** 3/5

---

# VERTICAL PACK — AEC / CONSTRUCTION (V01–V16)

For structural / architecture / MEP / BIM outsourcing clients. The **buying trigger for outsourced BIM / drafting / detailing capacity = project pipeline exceeding internal drafting throughput.** Project-flow signals are therefore the core.

## Project-flow / demand (the core)

### V01. New project award / contract win (structural scope)
**Signals:** a firm just won structural scope → drafting/modeling demand incoming. The purest demand pull.
**Best use:** "congrats on [project] — new awards usually hit the drafting team before you can staff up."
**Detection:** Dodge, ConstructConnect, ENR project wire, firm press, LinkedIn · **Window:** 0–60 days · **Trigger weight:** 5/5

### V02. Building permit filed — 10+ story / 150k+ sq ft, firm = SER
**Signals:** firm named Structural Engineer of Record on a large filing → CD-phase drafting load coming.
**Best use:** "saw the [address] filing — CDs on a [N]-story usually mean weeks of modeling."
**Detection:** NYC DOB, Shovels.ai, BuildZoom, county permit portals · **Window:** 0–90 days · **Trigger weight:** 5/5

### V03. Named EOR on a won public bid / RFP
**Signals:** public contract award, structural scope, fixed schedule.
**Detection:** SAM.gov, state/city bid boards, BidNet · **Window:** 0–60 days · **Trigger weight:** 5/5

### V04. Groundbreaking / construction start on a named project
**Signals:** project moving into build → structural docs must be complete/near-complete; change-order & shop-drawing load.
**Detection:** construction press, LinkedIn, firm posts · **Window:** 0–45 days · **Trigger weight:** 4/5

### V05. Design competition win / RFQ shortlist
**Signals:** a big new project entering design → forward capacity need.
**Detection:** AIA/architecture press, RFQ boards, LinkedIn · **Window:** 0–90 days · **Trigger weight:** 4/5

### V06. Named on a major high-rise in construction press
**Signals:** firm publicly tied to a flagship tall/complex building → matches STR high-rise ICP.
**Detection:** NY YIMBY, The Real Deal, ENR, Skyscrapercenter, local dev news · **Window:** 0–90 days · **Trigger weight:** 4/5

### V07. Rezoning / entitlement approved for a large development they're tied to
**Signals:** upstream — a big project cleared entitlement; design/structural work follows.
**Detection:** city planning portals, local dev news · **Window:** 30–120 days · **Trigger weight:** 3/5

### V08. Developer / GC client announces a big new pipeline (downstream pull)
**Signals:** the firm's KEY CLIENT is scaling → the firm will be pulled into more work.
**Best use:** "[their client] just announced [pipeline] — your team's usually next in line."
**Detection:** client press, Dodge, ENR · **Window:** 30–120 days · **Trigger weight:** 3/5

### V09. Design-phase milestone (SD → DD → CD transition)
**Signals:** the CD phase is exactly when drafting/detailing demand peaks; the crunch moment.
**Detection:** firm posts, project trackers, LLM inference from award date · **Window:** phase-timed · **Trigger weight:** 4/5

### V10. Backlog / revenue-growth commentary
**Signals:** principal interview / ENR note about record backlog → capacity strain.
**Detection:** ENR, ACEC, principal interviews, LinkedIn · **Window:** rolling · **Trigger weight:** 3/5

### V11. New master-agreement / on-call contract with an owner
**Signals:** DOT / university / agency on-call → steady multi-project throughput.
**Detection:** public procurement records, press · **Window:** 0–90 days · **Trigger weight:** 4/5

### V12. Firm issues an RFP/RFQ to subcontract detailing / modeling
**Signals:** they are literally shopping for outsourced capacity. **Highest intent in the pack.**
**Detection:** bid boards, LinkedIn posts, industry Slack/forums · **Window:** while open · **Trigger weight:** 5/5

### V13. Adaptive-reuse / seismic-retrofit project win
**Signals:** direct match to STR service line (retrofit modeling).
**Detection:** permits, press, firm posts · **Window:** 0–90 days · **Trigger weight:** 4/5

## AEC tech / regulatory / events

### V14. Won a project under an owner / state BIM mandate
**Signals:** forced BIM workflow; if they lack Revit maturity, outsource is the fast path.
**Detection:** RFP text, owner BIM standards, GSA/DOT requirements · **Window:** project-timed · **Trigger weight:** 4/5

### V15. Seismic ordinance / new code-cycle deadline in their geo
**Signals:** hard deadline (soft-story retrofit SF/LA; IBC/ASCE 7 cycle) → re-tooling window.
**Detection:** municipal ordinance calendars, ICC/ASCE adoption trackers · **Window:** deadline-driven · **Trigger weight:** 3/5

### V16. AEC event — attending / exhibiting
**Signals:** NASCC Steel Conference, Autodesk University, ACEC, Greenbuild, BILT → reason to reach out, buying-adjacent.
**Detection:** event exhibitor lists, LinkedIn · **Window:** around event · **Trigger weight:** 3/5

---

# VERTICAL PACK — AI-AGENT INFRA / DEV-TOOL (VA01–VA10)

*(added 2026-07-23, needs validation)* For self-hosted / source-available AI-agent & LLM-infra products. The **buying trigger = a team is building AI agents/automations AND cannot use cloud SaaS agent tools** (regulated data, on-prem mandate, data-residency, security review). Cloud-only agent builders (n8n cloud, Zapier, CrewAI cloud, Lindy, Relay) can't clear that bar — that gap is the wedge.

## Build-intent / demand (the core)

### VA01. Hiring an AI/ML/LLM/AI-agent engineer role
**Signals:** the org is standing up an AI-automation function → will need a build surface. Instantiation of U14 for this vertical.
**Best use:** "you're hiring an LLM engineer — most teams hit the 'where do agents run' question in month one."
**Detection:** LinkedIn Jobs, Clay, Trigify, TheirStack (JD text) · **Window:** 14–60 days · **Trigger weight:** 4/5

### VA02. Job post / JD names an agent stack (LangChain, LangGraph, CrewAI, AutoGen, n8n, Zapier, MCP)
**Signals:** confirmed they're building agents and on which framework → personalize by integration or displacement. Instantiation of U17.
**Detection:** LinkedIn JD text, TheirStack, Clay · **Window:** while live · **Trigger weight:** 4/5

### VA03. JD / post states data-residency / on-prem / self-hosted / air-gapped AI requirement
**Signals:** the purest fit — they explicitly can't send data to a hosted LLM/agent SaaS. Highest-intent signal in the pack.
**Best use:** "saw the 'must run on our infra' line — that's exactly the wall cloud agent tools hit."
**Detection:** LinkedIn JD text, Claygent, careers-page scrape · **Window:** while live · **Trigger weight:** 5/5

### VA04. Regulated-industry company publicly building internal AI agents
**Signals:** fintech/health/insurance/defense/gov/legal firm announces an AI-agent/automation initiative → security review guaranteed. Instantiation of U07.
**Detection:** press, company blog, LinkedIn posts, Serper · **Window:** 14–60 days · **Trigger weight:** 4/5

### VA05. Using a cloud-only agent SaaS while in a regulated / security-sensitive segment (displacement)
**Signals:** BuiltWith/JD shows n8n cloud / Zapier / CrewAI cloud in a HIPAA/SOC2/GDPR-bound company → compliance mismatch, replacement window.
**Detection:** BuiltWith, TheirStack, JD text + industry filter · **Window:** near renewal / audit · **Trigger weight:** 4/5

### VA06. GitHub engagement with the repo or a direct competitor's repo (star/fork/issue)
**Signals:** hands-on evaluator already in the self-host category. Warmest individual signal.
**Detection:** GitHub stargazers/forks API, repo issues, Clay · **Window:** 0–45 days · **Trigger weight:** 4/5

### VA07. New Head of AI / VP Engineering / CISO / Head of Platform (last 90 days)
**Signals:** new exec owning the AI-infra or security decision → vendor audit + fresh budget. Instantiation of U13/U28.
**Detection:** LinkedIn, Trigify, Champify · **Window:** days 14–90 · **Trigger weight:** 4/5

### VA08. Eng/security leader self-authored content on self-hosting, data privacy, or agent security
**Signals:** publicly voiced the exact pain (won't send data to OpenAI, wants on-prem LLMs, agent governance). Strongest LinkedIn hook. Instantiation of U24.
**Detection:** LinkedIn, Trigify, Exa · **Window:** 0–30 days · **Trigger weight:** 5/5

### VA09. New AI/data-security regulation or mandate hits their industry
**Signals:** EU AI Act, sector data-handling rule, gov on-prem mandate → forces auditable/self-hosted tooling. Instantiation of U12.
**Detection:** LLM analysis of industry news, regulatory calendars · **Window:** deadline-driven · **Trigger weight:** 3/5

### VA10. Recent funding round at an AI-native or AI-adopting company
**Signals:** fresh budget + mandate to ship AI features fast → infra decisions being made now. Instantiation of U01, AI-filtered.
**Detection:** Crunchbase, PredictLeads, Intellizence · **Window:** 0–90 days · **Trigger weight:** 3/5

---

# DATA POINTS (static — shape the message)

## Universal (D01–D10)

- **D01. Team composition / function headcount** — 0 SDRs + 5 AEs, or 1 drafter + 6 PEs. Reveals whether the function is systematic or ad-hoc. *Pair with:* U14/U15/U16.
- **D02. In-house capability present/absent** — presence vs absence of a function flips the angle entirely.
- **D03. Current tool stack** — reveals sophistication, budget, gaps.
- **D04. Who they sell to (buyer type)** — CTO (skeptical) vs CMO (inbox-flooded) → different outbound.
- **D05. Geographic / team distribution** — distributed = cost/timezone-aware already.
- **D06. Revenue model / ACV indicators** — determines whether the outbound math works.
- **D07. Content / LinkedIn activity level** — active poster = marketing-aware; silent = referral-reliant.
- **D08. Company maturity / metadata strength** — public-facing polish, positioning clarity.
- **D09. Public / private (ticker)** — listed → bigger budgets, longer cycles.
- **D10. Customer-base trajectory** — growing (double-down) vs shrinking (churn/cashflow angle).

## AEC (DV01–DV15)

- **DV01. In-house drafting/detailing team size** — 0–2 vs 3+. Primary capacity proxy. *Core pairing for every AEC hypothesis.*
- **DV02. PE-to-drafter ratio** — high ratio = licensed engineers doing low-value CAD = expensive pain.
- **DV03. Has a VDC/BIM department?** — yes/no flips the whole message.
- **DV04. BIM/Revit maturity** — published capability vs none.
- **DV05. Detailing software in stack** — Tekla/SDS2 = steel detailing; Revit = modeling. Sets which service to pitch.
- **DV06. Analysis software** — RISA / ETABS / SAP2000 / RAM → sophistication + sector.
- **DV07. % high-rise / mixed-use in portfolio** — core ICP-fit gate for STR.
- **DV08. Sector mix** — residential / commercial / healthcare / data center / industrial.
- **DV09. Seismic / wind zone** — drives retrofit vs new-build angle and code exposure.
- **DV10. ENR rank / size band** — firm scale.
- **DV11. Already uses offshore/nearshore?** — outsource-aware → skip the education, pitch quality/switch.
- **DV12. # concurrent active projects** — throughput proxy.
- **DV13. SE-licensed states** — geographic license spread → project geography.
- **DV14. Client type** — developer / GC / owner / public agency → deadline & volume profile.
- **DV15. Labor-cost exposure** — union / prevailing-wage / HCOL metro → in-house drafting is dearer, outsource ROI stronger.

## AI-Agent Infra (DA01–DA08) *(added 2026-07-23)*

- **DA01. Regulated industry (fintech / health / insurance / defense / gov / legal)** — the core self-host qualifier. Presence = cloud agent SaaS is disqualified for them. *Core pairing for every VA hypothesis.*
- **DA02. Compliance posture (SOC2 / HIPAA / GDPR / FedRAMP / ISO 27001)** — badges on site or in JD → data can't leave their perimeter.
- **DA03. Has an in-house platform / DevOps / infra team** — yes = they CAN self-host, the "runs on your infra" pitch lands; no = lead with managed simplicity.
- **DA04. Current agent/automation stack** — n8n / Zapier / Make / CrewAI / LangChain / none → displacement vs greenfield.
- **DA05. Company type — AI-native vs traditional-enterprise-adopting-AI** — sets sophistication and message altitude.
- **DA06. Team size / eng headcount band** — proxy for build capacity and deal size.
- **DA07. Open-source affinity** — active GitHub org, OSS in stack → receptive to source-available/self-host story.
- **DA08. Buyer type (CISO vs Head of AI vs VP Eng)** — security-owner (risk framing) vs builder (velocity framing) → different angle.

---

## How to pair for a strong hypothesis

Hypothesis = **one signal** (prefer Signal over Data point as the trigger) + **one or two data points** to adapt the message.

**AEC strong pairings:**
- V01 (project award) + DV01 (0–2 drafters) → "won [project] but a 2-person drafting team — CDs will bury them"
- V02 (permit filed, SER) + DV02 (high PE-to-drafter) → "your PEs will be modeling instead of stamping"
- V12 (RFP for detailing) + DV05 (Tekla in stack) → "saw you're sourcing detailing — we run Tekla steel detailing"
- U15 (pulled drafter req) + DV11 (no offshore yet) → "hiring a drafter didn't work out — capacity without a new seat"
- V08 (client pipeline announced) + DV07 (high-rise portfolio) → "[client]'s pipeline lands on your desk next"

**Universal strong pairings:**
- U14 (hiring SDRs) + D01 (0 SDRs / 5 AEs) · U13 (new leader) + D04 (who they sell to) · U15 (pulled req) + D02 (no in-house function)

**Weak pairings to avoid:** two "they're visible" facts (U10 award + D07 active LinkedIn); tautologies (U09 new client + D10 growing base).

---

## Tools by signal coverage

| Tool | Strongest for |
|---|---|
| **Clay** | primary enrichment + detection layer for almost everything |
| **Trigify** | LinkedIn-native real-time (U24–U30, U15/U19 job history) |
| **PredictLeads / Intellizence** | U01, U02, U07, U13, U16 |
| **BuiltWith / TheirStack** | U17, U20, U21, U22, U23 |
| **Crunchbase** | U01, U02, U03, U04 |
| **Dodge / ConstructConnect / ENR** | V01, V04, V08, V10 |
| **Shovels.ai / BuildZoom / DOB portals** | V02, V07, V13 |
| **SAM.gov / bid boards** | V03, V11, V12 |
| **LinkedIn (Sales Nav)** | TAM, U14/U16, D01/D02, DV01–DV03, C-series |
| **Apollo** | list building, TAM sizing |

---

## Maintaining this catalog

- New universal signal → next `U##`. New AEC signal → next `V##`. New vertical → a fresh `## Vertical pack — <name>` section with its own `X##` prefix.
- Each card: what it signals · best-use framing · detection tool · timing window · trigger weight.
- New/untested signal → tag `(added YYYY-MM-DD, needs validation)` until a campaign tests it.
- Signal that fails 3+ campaigns → tag `(unreliable — avoid)`, don't delete (the history is useful).
