# GTM Skills — Victor Shulga

Ten Claude Skills I use to run go-to-market for B2B service agencies — outbound,
lead scoring, offers, proposals, reply handling, and more. Each skill is one
`/command` that carries a full working method, not a prompt snippet.

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
| `reply-audit` | Forensic audit of outbound replies → root cause (targeting vs pitch) → 9-section report. |
| `lead-scoring` | Deterministic 100-pt ICP rubric with anti-ICP gates, before SDR outreach. |
| `offer-factory` | From a site → 5–10 testable offer-bets (ICP × pain × mechanism), scored. |
| `agency-signal-sourcer` | Buying-signal engine: detect, decay windows, scoring, heat tiers, signal-to-action plays. |
| `weekly-outreach-report` | Narrative weekly outreach report (7+2 sections) with data-quality warnings first. |
| `reply-objection-handler` | One reply → classify → one ready-to-send message + a library of proven templates. |
| `meeting-prep` | Pre-call brief ≤500 words for a booked discovery/demo call. |
| `proposal-generator` | Two proposals (call-deck + send version) on the client's brand, with a critique checklist. |
| `anticopywriting-ai` | Strips the AI tone from UK/EN text — clichés, filler, over-formatting. |

## Master skills

These mono skills pair with two larger master flows:

- **GTM Strategy** — a 13-step cold-audit that turns a URL into a full GTM strategy → [`victor-shulga/gtm-strategy-skills`](https://github.com/victor-shulga/gtm-strategy-skills)
- **Content Engine** — an 8-step LinkedIn content system → [`victor-shulga/content-engine-skills`](https://github.com/victor-shulga/content-engine-skills)

## License

MIT © Victor Shulga
