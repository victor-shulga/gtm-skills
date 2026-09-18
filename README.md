# GTM Skills — Victor Shulga

Five Claude Skills I use to run go-to-market for B2B service agencies — buying signals,
hypotheses, offers, and the writing pass that strips AI tone. Each skill is one
`/command` that carries a full working method, not a prompt snippet.

These are the **strategy and pre-outreach** skills. The execution skills that used to live here —
reply handling, reply audits, lead scoring, weekly reporting — moved into the
[outbound-engine](https://github.com/victor-shulga/outbound-engine-skills) bundle, and `meeting-prep`
moved into [sales-engine](https://github.com/victor-shulga/sales-engine-skills), so that no skill
exists in two repos at once. See the changelog below.

Built by [Victor Shulga](https://victorshulga.com) — Fractional CRO for IT agencies.

## Install

Install the whole library with the [Skills CLI](https://github.com/anthropics/skills):

```bash
npx skills add victor-shulga/gtm-skills
```

Or a single skill:

```bash
npx skills add victor-shulga/gtm-skills/hypo-generator
```

Then call it in Claude with `/<skill-name>`.

## Skills

| Skill | What it does |
|---|---|
| `hypo-generator` | From an agency site → a weighted ICP × signal × offer hypothesis matrix. |
| `hypothesis-scoring` | From a pile of hypotheses → a launch queue: stop-filter gate, the number N, capacity check, 6-factor score, top three go. |
| `offer-factory` | From a site → 5–10 testable offer-bets (ICP × pain × mechanism), scored. |
| `agency-signal-sourcer` | Buying-signal engine: detect, decay windows, scoring, heat tiers, signal-to-action plays. |
| `signal-research` | Runs an existing account base through a signal hunt → evidenced, dated, scored list + coverage report. |
| `anticopywriting-ai` | Strips the AI tone from UK/EN text — clichés, filler, over-formatting. |

## Changelog

**Sep 2026 — `proposal-generator` moved to [sales-engine](https://github.com/victor-shulga/sales-engine-skills).**
A proposal is the end of the sales block, not a pre-outreach step; it now sits next to `offer-ladder`,
`meeting-prep` and `pipeline-analysis`. Same rule as before: one home per skill.

**Aug 2026 — repo boundaries drawn.** Five skills left this repo to remove cross-repo duplicates:
`reply-objection-handler`, `reply-audit`, `lead-scoring` and `weekly-outreach-report` are now in
[outbound-engine](https://github.com/victor-shulga/outbound-engine-skills); `meeting-prep` is in
[sales-engine](https://github.com/victor-shulga/sales-engine-skills). Previously some of them were
installable from two places under the same name, with the copies drifting apart — installing both
bundles gave you two different skills answering to one name. This repo now holds strategy and
pre-outreach only.

## Master skills

These mono skills pair with two larger master flows:

- **GTM Strategy** — a 13-step cold-audit that turns a URL into a full GTM strategy → [`victor-shulga/gtm-strategy-skills`](https://github.com/victor-shulga/gtm-strategy-skills)
- **Content Engine** — an 8-step LinkedIn content system → [`victor-shulga/content-engine-skills`](https://github.com/victor-shulga/content-engine-skills)

## License

MIT © Victor Shulga
