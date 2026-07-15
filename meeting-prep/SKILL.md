---
name: meeting-prep
description: >
  Generates a pre-call brief for a BOOKED meeting (discovery or demo) — the handoff dossier that lets
  whoever takes the call walk in fully prepared. Entire brief ≤ 500 words. Built from the G6 handoff
  context (thread + signal + hypothesis), the prospect-profiler card, and any scoring/profile data.
  Produces: exec summary, company snapshot, prospect profile, conversation starters, no-BANT discovery
  questions, grounded objection-handles, time-blocked agenda (30/60 min), success metrics. Adapted for
  B2B service agencies (Viktor Shulha's clients — BIM/MEP, GIS, custom dev, AI/SaaS
  engineering outsourcing), NOT US-SaaS. Use when Viktor says: "підготуй до зустрічі", "pre-call brief",
  "бриф на дзвінок", "meeting prep", "prep me for [meeting]", "дос'є на зустріч", "handoff brief",
  or hands a booked discovery/demo and wants prep. This is the G6 HANDOFF artifact in the Outreach QA
  Framework (Viktor's studio preps it, client sales runs the call). NOT a cold-call script (use cold-call-script for
  outbound dials), NOT meeting-intent scoring (use 28-meeting-intent-scorer to decide if the meeting is
  worth prepping), NOT deep customer research (use deep-company-analyser for a T1 that needs more).
---

# Meeting Prep — the pre-call brief (≤ 500 words)

You build the dossier someone reads right before a booked call so they don't walk in cold. The whole
brief is **under 500 words** — a rep skims it in 2 minutes and knows the goal, the questions, and the
landmines.

**Where this sits.** This is the **G6 handoff artifact** in the Outreach QA Framework. Viktor's studio
prepared the lead; the brief travels with the lead to the client's sales team so they don't start from
zero on a warm lead (the most expensive place to lose one). Run `28-meeting-intent-scorer` FIRST — only
prep meetings that clear the qualification threshold.

**Grounding rule (don't fabricate the call).** Every objection, pain, and starter ties to a real
signal / thread / profile fact, or is tagged **[inferred]**. Do not invent objections to look thorough —
a fabricated objection wastes the rep's prep and misframes the call. If you can't ground it or honestly
infer it, leave it out.

---

## Inputs

Pull from whatever exists, in priority order:
1. **G6 handoff context** — the reply thread, the signal that triggered outreach, the hypothesis.
2. **prospect-profiler card** — summary, the_signal, comm_style, grounded pain, approach.
3. **Scoring / profile data** — tier, role, firmographics.

If a `prospect-profiler` card exists, build ON it — don't re-derive. If the account is a T1 needing
deeper research, hand it to `deep-company-analyser` first, then prep.

---

## Brief structure (≤ 500 words total across all fields)

| Field | Rule |
| :-- | :-- |
| `exec_summary` | 2-3 sentences: who you're meeting · why they took the meeting (the signal/thread) · the ONE outcome to aim for. |
| `company_snapshot` | 2-3 sentences: what they do, size, the change in play (signal), delivery context. No marketing voice. |
| `prospect_profile` | 2-3 sentences: their role, likely priorities, comm_style (carry from profiler). Are they a decision-influencer or a gate? |
| `conversation_starters` | 3, tied to real signals / their activity — substantive, not small talk. In the **prospect's language** (spoken on the call). |
| `discovery_questions` | 5, **NO BANT** (see below). Use the consequence / priority / ownership construction from `cold-call-script`. Prospect's language. |
| `objection_handles` | Up to 3. Format `Objection: X — Handle: Y`. Each grounded or tagged **[inferred]**. Pull plays from `reply-objection-handler`. |
| `recommended_agenda` | Time-blocked, matched to meeting_type (30 or 60 min). See templates. |
| `success_metrics` | 2-3 bullets defining a successful call (e.g. "named top-2 pains", "agreed a concrete next step", "surfaced internal champion"). |

**Language.** Brief framing in Viktor's working language (UA); everything spoken on the call —
starters, discovery questions — in the **prospect's language** (usually EN).

---

## NO BANT (hard rule)
Never include: "What's your budget?", "Who's the decision maker?", "What's your timeline?", "Are you
evaluating other vendors?", or any variant. Instead, questions that:
- explore their specific situation and the pain behind the signal
- uncover the **impact / cost of inaction** (the strongest lever)
- reveal what "good" looks like to them
- reframe the problem
Reuse the discovery-question construction in `cold-call-script` (consequence > priority > ownership).

## Call-type ratio (drives the agenda balance)
- **discovery** → 80% questions / 20% positioning
- **demo** → 30% discovery / 70% tailored demo

## Agenda templates
**Discovery (30 min):** 0-3 rapport+context · 3-15 discovery · 15-22 initial positioning from answers ·
22-27 next steps · 27-30 recap+actions.
**Demo (60 min):** 0-5 rapport+agenda · 5-15 confirm understanding · 15-45 tailored demo · 45-55 Q&A +
objection handling · 55-60 next steps+actions.

---

## Integration

```
G6 Reply QA: positive reply → 28-meeting-intent-scorer (worth it?) → meeting booked
                                          │
                                          ▼
                              meeting-prep  ← THIS skill: handoff dossier
                                          │
                                          ▼
                        client sales runs the call (brief travels with the lead)
```

- **Score first:** `28-meeting-intent-scorer` — don't prep meetings below threshold.
- **Build on:** `prospect-profiler` card (don't re-derive); `deep-company-analyser` for a T1 that needs depth.
- **Objection plays:** `reply-objection-handler`. **Discovery construction:** `cold-call-script`.

## Hard rules
1. ≤ 500 words total. A rep skims it in 2 minutes.
2. NO BANT questions — consequence/impact instead.
3. No fabricated objections — ground each or tag `[inferred]`.
4. Score with `28-meeting-intent-scorer` before prepping.
5. One outcome goal per brief — state it in `exec_summary`.
6. Spoken fields in the prospect's language; framing in UA.
