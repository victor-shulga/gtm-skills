---
name: weekly-outreach-report
description: >
  Builds a canonical WEEKLY outreach report for a client as a standalone narrative
  page — the exact 7(+2)-section format instead of a dashboard dump. Pulls live data
  from the client's outreach platform (LinkedIn automation and/or email sending tools),
  applies the known platform gotchas, classifies every reply with root cause, and ends
  with gold leads + ready-to-send drafts. Trigger with: "weekly report", "outreach
  report", "analyse this week's results", "build the report from our template". NOT for
  batch reply forensics alone (use reply-audit) and NOT for benchmarking a single metric
  (use outbound-analyst).
---

# Weekly Outreach Report

The report is a **standalone readable narrative page**, not a row-dump into a matrix DB.
The data store and the report are two separate artifacts.

## Hard rules

- NEVER dump rows into a matrix DB and point at a kanban. Matrix DB = data store;
  the report = its own readable artifact.
- Report language: match the client's working language. Lead drafts: the prospect's
  language (usually English).
- Every draft message ends with a question (soft CTA).
- Data-quality warnings come BEFORE the numbers, not in a footnote.
- Numbers must be genuine per-(flow × sender × week). If a platform can't give a weekly
  cut, say so explicitly and show the method used.

## Step 1 — Route to the client's platform (apply the gotchas)

Every outreach platform lies in its own way. Know the trap before you trust the number:

| Platform type | Gotcha you MUST apply |
|---|---|
| LinkedIn automation (lifetime-stats tools) | Stats are often LIFETIME-only → the weekly delta = this week's snapshot minus last week's snapshot. Store/ask for the previous snapshot; never present lifetime totals as "this week". |
| LinkedIn automation (per-flow CRM) | A platform "Replied" CRM stage can read 0 even when replies exist. Count real replies from the reply/trigger events per flow, NOT the CRM stage. |
| Email sending tools | Reply/open data may be dark or partial. Report the dark channel as a data-quality item rather than implying zero. |
| Workspace/day-level tools | Stats may only be available workspace-level per day, not per campaign per week. Note the granularity limit. |

If the platform data source is not connected, say which one is missing and build the
report from whatever export the client provides (CSV / Sheet / paste) instead of stopping.

## Step 2 — Assemble the page in this exact order

1. **Header** — client, week (Mon–Sun dates), platforms, senders.
2. **Main takeaway** — one paragraph: the single most important thing about the week.
3. **⚠️ Data quality** — FIRST, before any table: what's missing, fake-zero fields,
   lifetime-only metrics, dark channels, snapshot method used.
4. **Overall funnel** — table: sent → connected → replied → positive → calls booked,
   with week-over-week delta where possible.
5. **By flow / campaign** — table per flow: volume, connect %, reply %, positive replies;
   one line of interpretation per flow (not just numbers).
6. **By sender** — same cut per sender; flag connect-heavy/message-starved funnels
   (lots of accepts, few messages sent — a common failure pattern).
7. **Actions** — numbered actions, each with owner + date.
8. **Reply analysis (forensics)** — classify EVERY reply of the week: positive /
   objection / referral / not-now / negative / auto-reply. For each non-positive class,
   root cause: **targeting/data problem vs message problem vs pitch problem**. Watch known
   false positives: event smalltalk inflating reply counts; warm replies sitting unstaged
   in the CRM.
9. **Gold leads** — for each warm/positive lead: full thread quoted, context, and a
   ready-to-send draft in the prospect's language (route objection drafts through the
   reply-objection-handler taxonomy).

## Step 3 — Ship

- Create the page in the client's reporting area (ask once if unknown, then remember).
  New week = new page — never regenerate an existing report page (it kills saved chart
  views).
- If your tool renders tables from pipe-delimited text, don't put a literal `|` inside a
  cell — use `·`.
- Post a 5-line TL;DR back in chat: headline metric, biggest problem, top action.
