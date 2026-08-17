---
name: hypothesis-scoring
description: >-
  Scores and ranks outbound hypotheses BEFORE launch and turns them into a launch queue — the
  pre-launch evaluation method from Victor Shulga's guide on testing cold-outreach hypotheses:
  stop-filter gate, canonical hypothesis format with the number N, channel capacity check,
  6-factor weighted score on the 0/1/3/5 scale, priority queue where the top three go into work,
  and a journal skeleton for the facts. Trigger when the user says "оціни гіпотези", "оцінка
  гіпотез", "пріоритизуй гіпотези", "яку гіпотезу запускати першою", "черга запуску", "відбери
  3 гіпотези", "score these hypotheses", "prioritize hypotheses", "which hypothesis do we run
  first", or hands a list of campaign ideas / a hypothesis matrix and asks what goes into work.
  Also use to re-score a hypothesis matrix before launch, or to audit a hypothesis list a team
  wrote itself. NOT for generating hypotheses from scratch (use hypo-generator), NOT for reading
  results after a test has already run.
---

# Hypothesis Scoring — the pre-launch queue

Takes a pile of hypothesis ideas and returns a **launch queue**: which three go into work now, which wait, which are disqualified and why.

The point of this skill is to end the argument that usually follows a batch of outbound tests — "did it work or not" — with a number agreed on *before* the send.

**Output language:** the team's working language (Ukrainian by default for Ukrainian-speaking teams; English if the input is English). Plain words, no jargon.

---

## What you need

- **A list of hypothesis ideas** — a matrix from `hypo-generator`, a workshop output, the team's own list, or raw text.
- Per idea, ideally: ICP · trigger (or static data point) · offer · channel · proof (a case with a number) · where the list comes from.

Missing fields are not a blocker — they are a **finding**. An idea with no proof or no list source fails the gate at Step 1. Never invent either one.

Ask for, if not given: which channels are live and how many senders (LinkedIn accounts / mailboxes), and whether the team has its own campaign history (own numbers always beat market benchmarks).

---

## Workflow

### Step 1 — Stop-filter (the gate before any scoring)

Four yes/no gates. **One "no" means the hypothesis is not scored at all.** Scoring something you can't execute only pollutes the queue.

| # | Gate | PASS means |
|---|---|---|
| G1 | The list can be built | a named source + filter that yields ≥300 companies carrying this trigger. "Somewhere on LinkedIn" = FAIL |
| G2 | The trigger is verifiable | for one specific company you can confirm the event happened and name the date |
| G3 | Proof exists | a case, a number, or an adjacent project the decision maker will accept as relevant to THIS segment |
| G4 | The decision maker is reachable in the channel | they read LinkedIn, or have a work mailbox that passes the gateway |

**Technical stop-filter (email only — checked once per company, not per hypothesis):** SPF/DKIM/DMARC set on every domain · inbox-placement tested (not "well, the emails are going out") · mailboxes warmed ≥3 weeks · bounce rate under 3% in previous campaigns.

A failure here blocks *every* email hypothesis at once — report it as one blocker with an owner, not as N separate findings. These checks cost a day; skipped, they poison every conclusion that follows, because a hypothesis looks dead when the emails simply never arrived.

Output a gate table: `hypothesis | G1 | G2 | G3 | G4 | verdict`. For each FAIL, write the single action that fixes it and who owns it.

### Step 2 — Rewrite into the canonical format

A hypothesis that cannot be refuted by a number stays an opinion. Rewrite every survivor into one sentence:

> For **[ICP]** with trigger **[T]**, offer **[O]** in channel **[C]** will produce at least **[N]** replies per 300 contacts in 3 weeks.
> Below half of N: close it. Between half and N: change one variable and repeat. N or above: scale the volume to 1000.

**Calculating N** — use the team's own history when it exists; market baselines only when it doesn't:

| Channel | Math on 300 contacts | Default N |
|---|---|---|
| Email | 300 × 1.5% (2026 average reply rate) | 4–5 |
| LinkedIn | 300 × 30% accepted × 20% replied | 15–20 |

N is a floor, not a forecast. If someone wants N set below the market baseline, the hypothesis isn't worth a slot.

### Step 3 — Channel physics (how many tests actually fit)

Capacity decides how many hypotheses run in parallel. Ambition doesn't.

- **LinkedIn:** ~20 invites/day per account → 300 contacts = 15 working days = 3 weeks for ONE account on ONE hypothesis. Three parallel tests need three accounts. There is no third option.
- **Email:** 3 mailboxes × 30 emails/day = 90 sends/day. A 3-step sequence over 300 contacts ≈ 900 sends ≈ 10 working days.

Output: available capacity → how many hypotheses physically fit this cycle → a stop date for each test, in the calendar. If the queue is longer than the capacity, say so plainly — that, and not the score, is why the rest are waiting. A plan for five parallel hypotheses on one LinkedIn account is really a five-month plan.

### Step 4 — Score (6 factors, scale 0 / 1 / 3 / 5)

The zero is mandatory. Without it every option clusters around 3 and the score stops separating anything.

| Factor | Weight | 5 = | 0 = |
|---|---|---|---|
| **Proof strength for this segment** | 0.25 | a case with a real number in exactly this niche | no proof at all |
| **Pain sharpness** | 0.25 | hurts right now, budget already allocated | a pain we invented; the market never named it |
| **Trigger non-obviousness** | 0.20 | competitors don't use this signal | everyone uses it — noise |
| **Segment volume** | 0.10 | over 1,000 companies | can't even be assembled up to 300 |
| **Data-collection cost** | 0.10 | the list is built in an hour | manual research per account |
| **Speed of verification** | 0.10 | first replies within a week | the cycle runs longer than a month |

Intermediate values: **1** = weak but present · **3** = normal, works but unremarkable.

**Total** = Σ(score × weight), range 0.0–5.0.

**Two hard rules:**

1. **A zero on Proof or on Pain removes the hypothesis from the queue** — regardless of the total. Report it as dropped, and name the missing piece. A high total built on no proof is the most expensive kind of false confidence.
2. **The three highest totals go into work**, however many crossed 3.2. The threshold is secondary; the queue is the mechanism. A fourth hypothesis splits attention and splits the list.

Every score carries a **one-line reason**. A bare number can't be argued with later, and in a quarter nobody remembers what it meant.

The scoring is subjective, and that's fine: it decides launch ORDER only. The facts will come from replies either way.

### Step 5 — The queue

| # | Hypothesis (one line) | Proof | Pain | Trigger | Volume | Data | Speed | Total | Status |
|---|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|---|

Statuses: **launch** (top 3) · **queue** (waits for the next cycle or free capacity) · **dropped** (zero on Proof or Pain) · **failed the gate** (Step 1 FAIL + what to fix).

### Step 6 — Launch plan + journal

For the three launched:

- ICP · trigger · offer · channel · N · first batch size (300) · start date · **stop date** · who decides to close it.
- **Order of variables.** Round 1 "where": offer and copy frozen, 2–3 segments run in parallel (a segment = ICP + trigger, they move together). Round 2 "what": winning segment, two offer variants. Round 3 "how": same segment and offer, the angle changes — first line, proof, call. One change per round; two changes at once turn the result into a guess.
- **Write to 2–3 people per company, not one.** With a single contact you can't tell "wrong persona" from "wrong company", and you'll close a live segment by accident.
- **Triggers expire.** A job posting stops being a signal after ~30 days, a funding round after ~90. A list assembled three months ago is not a trigger list, and the campaign on it will fail regardless of copy quality.

Then emit the **journal skeleton** with the fact columns empty: number · ICP · trigger · offer · channel · start date · stop date · contacts · companies · sends · delivered · opens · replies · positives · meetings · three verbatim objection quotes · verdict · next step.

The verdict has exactly three values: **scale · change one variable · close**. If you're tempted to write "not clear yet", the volume was too small — that is also a journal entry.

Keep three verbatim objection quotes from every test. After five campaigns you have a dictionary in which the market itself explains why it doesn't buy.

### Step 7 — Portfolio 80/20 (once two hypotheses have confirmed meetings)

80% of the channel's daily quota goes to the proven ones. 20% stays for ONE active test — not two, not five, but one, carried all the way to 300 contacts. When a test wins, it moves into the working 80% and the weakest working hypothesis is switched off; the queue from Step 5 supplies the next one.

---

## Reading a failure (when the test comes back)

Scoring happens before launch, but the queue only stays honest if failures are diagnosed instead of mourned. Four axes, checked in this order:

1. **Technical** — opens under 30%, bounces over 3%, mail in spam. The hypothesis had nothing to do with it: fix delivery and rerun the same test.
2. **Targeting** — replies exist and they say "we don't do that", "you want a different person", "we're not in that region". The segment or the persona is wrong.
3. **Offer** — "got it, but we don't need it", "we handle this in-house", "we already have a contractor". Right segment, weak proposition.
4. **Message** — delivery fine, segment confirmed, silence in return. The copy and the angle are the problem.

---

## Hard rules

- Never invent proof or a list source. Missing = a gate FAIL, not "a 3".
- A hypothesis without the number N is not scored — rewrite it into the canonical format first.
- 300 contacts is the minimum test. Positives are not readable at 300 at all: the difference between one and three is randomness. Talk about positives and cost-per-meeting from 1000 up.
- The base metric of a test is the reply rate; the hypothesis wins on meetings. 4% replies and zero meetings is not a working hypothesis, whatever the table says.
- Exactly three hypotheses launch. The fourth divides attention and the list.
- Own campaign numbers beat market benchmarks whenever they exist.
- Agree in advance who decides to close a test. Without that, a test runs until somebody gets bored.

---

## Helper script

`scripts/score.py` does the arithmetic and sorts the queue, so nobody adds weights in their head:

```bash
python3 scripts/score.py hypotheses.json
```

Input format, the hard-zero rule and gate handling are documented in the script header. It prints a ranked markdown table you can paste straight into the report.

---

## Pairs with

- `hypo-generator` — builds the hypothesis matrix from an agency URL; this skill scores its output before launch.
- `agency-signal-sourcer` — detection tooling, cost and decay window per trigger; feeds the "Data-collection cost" and "Trigger non-obviousness" factors.
- `anticopywriting-ai` — run the finished report through it before sending it to anyone.
