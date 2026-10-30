---
name: offer-factory
description: Use when Viktor wants to invent offers FAST for an IT-agency client and test them with outbound. From a client website URL, generates 5–10 testable offer-bets (ICP × pain × mechanism), scores them, and expands the winners into outbound-ready cards with built-in test design. Trigger when the user says "придумай офери для клієнта", "що продавати цій агенції", "офери під аутбаунд", "build offers from this URL", "offer factory", "розроби офер для [клієнт]", or pastes an agency URL and asks what to sell/test. NOT for choosing WHO+WHICH-SIGNAL to target (use hypothesis-builder / hypo-generator for that) — this skill is about the OFFER itself.
---

# Offer Factory

Turn an IT-agency client into 5–10 outbound-testable offer-bets, fast. Each bet is a distinct wager (not one offer reworded), scored, ranked, and expanded into a card you can ship to outbound this week.

**Language:** reasoning + commentary in Ukrainian; the offers, promises, and cold hooks in English (outbound usually targets the West). Override if the user says otherwise.

## What you need
- **Client website URL** (required) — the source of services, verticals, ICP signals, and case studies.
- Optional: fixed ICPs to build under, constraints ("US only", "no enterprise", "fixed-price only"), or a best-client example.

If the user already gave fixed ICPs, build under those instead of enumerating your own (Phase 2 narrows to them).

## Process (7 phases)

### Phase 1 — Scrape & extract
Fetch the site (Google Drive `read_file_content` for Docs; `WebFetch` / Apify `rag-web-browser` for live web — note WebFetch only sees Google-Docs chrome, so use the Drive connector for Docs). Pull the raw material:
- service lines, tech stack, capabilities
- industries / verticals served
- ICP signals (who they already serve — size, type, geo, stage)
- **case studies with concrete numbers** (this is the proof bank)
- positioning, stated differentiators

### Phase 2 — Axis candidates
From the material, list 3–4 candidates on each of three axes:
- **ICP / vertical** — who buys
- **Pain / dream outcome** — what result they want
- **Mechanism / service** — how it's delivered

These three axes are what make bets *different bets*. (Packaging/pricing is a 4th optional axis — use only if the user asks.)

### Phase 3 — Cheap matrix
Generate ~12–15 one-line combos: `We help [ICP] achieve [outcome] via [mechanism]`. One line each, no detail yet. Cheap to produce, cheap to discard.

### Phase 4 — Score & select
Score every combo, keep the top 5–10:
```
Value  = geomean(Dream, Likelihood, Time, Effort)      # each 1–10; Time/Effort: 10 = fast / low friction
Testability = geomean(MarketSize, TargetingEase, HookClarity)  # each 1–10
BLEND  = 0.6 * Value + 0.4 * Testability
```
- **Value** = Hormozi value equation (dream × likelihood, divided by delay & effort — encoded as a geometric mean so it stays 1–10).
- **Testability** = how fast cold outreach can prove or kill the offer (is the market findable, targetable, and is the hook punchy). Not to be confused with buying signals (signal catalog, hypo-generator): this score needs no signal catalog.
- Curate the kept set for **axis diversity** — don't ship 5 variants of the same ICP×pain. Cover different ICPs, pains, and mechanisms.

### Phase 5 — Expand winners into Standard cards
For each kept offer (UA reasoning, EN promise + hook):
```
#  Offer name
   Promise (EN):  see Promise Formulas below — NEVER default to "We help X..."
   Bet:           what makes this a distinct wager (UA)
   ICP:           who + where to find them
   Pain/trigger:  the pain and the moment it's acute
   Mechanism:     what's delivered
   Proof:         REAL case from the site; where missing → [TODO: need case ___]
   Risk-reversal: guarantee / success criteria (esp. high-ticket)
   Cold hook (EN): 1–2 lines + small CTA (+ 1 alt hook for A/B)
   Score:         value for the client X/10 · how fast cold outreach tests it Y/10 · total Z/10
                  (D L T E and the formula stay in your working notes, never in the client document)
```

### Phase 6 — Test design (built into every card)
```
Test:  N = 40–60 targeted leads
       metric: positive reply rate (sprint/trial → also booked calls)
       keep ≥ 10% / kill < 5%  (5–10% = keep angle, swap signal or persona)
       window: 2 weeks / cohort
```

### Phase 7 — Output
Ranked table + full cards. **Ask before writing to Google Sheets** (the user's "Service – use case – offer" 12-column template). Optionally hand off the winners to `hypothesis-builder` (signals/personas) then `sequence-writer` (outbound-engine-skills, sequences).

## Promise Formulas (replace "We help X achieve Y via Z")
"We help…" is fine for the internal card line, but never as the outbound promise. Use:
1. **Without** (Hormozi): `[Dream outcome] — without [main sacrifice]`
2. **Transformation**: `From [bad state] to [desired state] in [time]`
3. **Imperative**: `[Verb] [outcome] — [differentiator]`
4. **Pain-removal**: `Stop [pain]. Start [outcome].`
5. **Identity/role**: `Your [role/team] — [what you do instead of the client]`
6. **Risk-reversal**: `Try [thing] for [small commitment]. Keep it only if [proof].`

## Built-in rules

### High-ticket → entry rung (land-and-expand)
For high-ticket offers with a complex/long sales cycle, **never test the full contract cold.** Split into two cards:
- `Entry rung` — paid pilot / diagnostic / scoped sprint, priced in **discretionary budget ($5–20K)** so it skips CFO approval. THIS is the cold-outbound offer.
- `Core contract` — the big engagement, sold on **expand** after the rung delivers.
For high-ticket test KPI = **booked discovery / pilot accepted**, NOT closed deal (cycle is 60–180 days). Add a `risk-reversal` (refund-if-criteria-not-met, milestone/phased) and a `multi-thread map` (who else is in the deal: CFO→ROI, IT→security/architecture, procurement→SLA, ops→timeline).
The Testability score naturally penalizes big commitments — that's the math telling you to lead with the rung.

### Low-testability rescue
When an offer has high **Value** but low **Testability** (a good offer drowning in a commoditized channel, e.g. generic outstaff), don't fix the offer — fix the **wedge on the channel**:
1. narrow the ICP / talent niche (e.g. "LLM engineers" not "developers"),
2. add risk-reversal (paid trial week),
3. make the CTA concretely small.
Re-score after sharpening; a good wedge typically lifts BLEND by ~1 point.

### Proof handling
Use only real case studies from the site. Where a card needs proof you don't have, insert an explicit `[TODO: need case ___]` placeholder — never fabricate metrics. General proof (e.g. "170+ MVPs, 30+ clients") can back any card.

## Worked example
Run on an AI-MVP dev agency site with 3 fixed ICPs → 9 variants scored → top 3 cold-test winners:
- ICP non-tech founder → **Paid Discovery & Architecture Sprint** (entry rung, BLEND 7.97)
- ICP AI-startup CTO → **Senior LLM Engineer 1-week trial** (low-signal rescue of outstaff, 7.95)
- ICP marketing agency → **White-Label AI Feature Sprint** (7.70)
Pattern observed: all three winners were low-friction entry rungs; the big ongoing commitments (embedded team, pod) ranked lowest — confirming the high-ticket rule above.

## Notes
- 5–10 offers is the target. Fewer = under-exploring the space; more = no focus.
- This is a backlog of bets, not a campaign. Only expand what the client can resource to test.
- Keep the cheap matrix (Phase 3) cheap — don't write full cards before scoring.
- **Pairs with `offer-ladder`:** offer-factory = horizontal batch of bets to test cold; `offer-ladder` = vertical free→low→mid→high portfolio around one core transformation. If the user wants portfolio/monetization structure (not a test batch), route to `offer-ladder`. The ladder's cold-facing entry rung loops back here for the test card.

## Terms and plain-language output

<!-- glossary:start terms=offer-bet,axes,value-score,signal-score,blend,test-card,kill-keep,positive-reply-rate,risk-reversal,multi-thread,low-signal-rescue,entry-rung,expand,hook,cta,promise-formula,proof -->
Rules for every document a client or their team will read (review, roast, canvas, offer cards, instruction):

1. **Open with «Словник цього документа»**: only the terms that actually appear in it, at most 10, each as «термін — що це простими словами». Like the definitions section of a contract.
2. **No internal codes or letter scales in the text** (A/B/C, D L T E, BLEND numbers without words, Own/Shared/Generic, Z1.4, GATE 2.5, T1–T6). Write the meaning instead: «є цифра з клієнтом», not «A».
3. **Use the plain form from the table below.** English stays only for tool names and for copy that ships in English (promises, hooks, subject lines). If the document is in another language, translate the plain form, never the internal term.
4. **Do not score what cannot exist yet.** A block that depends on work not done (signal catalog, case studies, a previous step) gets «пропущено: спершу потрібно <що саме>», not a score.
5. **Every section of a review opens with one concrete action** («до наступного дзвінка: …»), then at most five lines of why. No paragraph that only restates the framework.

| Internal term (this skill) | Write for the client | What it means |
|---|---|---|
| offer-bet, bet | варіант оферу на тест | окрема ставка: інша комбінація «кому · який результат · як робимо», а не той самий офер іншими словами |
| axes (ICP / pain / mechanism) | три виміри оферу: кому, який результат, як робимо | щоб варіанти справді відрізнялися, між ними міняється хоча б один вимір |
| Value score, D L T E (Dream, Likelihood, Time, Effort) | оцінка цінності для клієнта | наскільки бажаний результат, наскільки клієнт вірить, що він буде, як швидко і скільки зусиль від нього; кожне від 1 до 10 |
| Testability score (MarketSize, TargetingEase, HookClarity), formerly Signal | оцінка, як швидко офер перевіримо в холодних листах | чи великий ринок, чи легко знайти цих людей і чи зрозуміло з першого рядка, про що офер; кожне від 1 до 10 |
| BLEND | підсумкова оцінка варіанту | 60% цінність плюс 40% швидкість перевірки; за нею сортуємо варіанти |
| test card, offer-factory card | картка тесту оферу | одна сторінка на один варіант: обіцянка, кому пишемо, доказ, перший лист, скільки контактів і за яким результатом лишаємо чи прибираємо офер |
| kill / keep threshold, N | поріг «лишаємо чи прибираємо» | на 40–60 контактів за 2 тижні: від 10% позитивних відповідей лишаємо, менше 5% прибираємо, між ними міняємо сигнал або посаду |
| positive reply rate | частка позитивних відповідей | скільки з тих, кому написали, відповіли з інтересом, а не «відпишіть мене» |
| risk reversal, guarantee | гарантія, що знімає ризик | що клієнт отримає, якщо результату не буде: повернення грошей, безкоштовне продовження, оплата за етапами |
| multi-thread map | карта людей в угоді | хто ще впливає на рішення і що кожному показати: фінансисту окупність, технічному безпеку, закупівлям умови |
| low-testability rescue, wedge | звуження під канал | коли офер добрий, але тоне серед схожих: звужуємо нішу, додаємо гарантію, робимо прохання меншим |
| entry rung, cold-facing rung | вхідний офер для холодних листів | офер, з яким ідемо до людей, що вас не знають: невеликий за ціною й ризиком (платний пілот, діагностика, короткий спринт) |
| expand, land-and-expand | допродаж після першої роботи | дорожчі сходинки не пропонуємо холодним людям, їх продаємо клієнту, який уже отримав результат на вхідному офері |
| hook, cold hook | гачок | перший рядок листа, через який людина читає далі |
| CTA | прохання в кінці листа | конкретний маленький наступний крок: відповісти, подивитися, погодитися на дзвінок |
| Promise Formulas | формула обіцянки | шаблон першого речення оферу: «результат без жертви», «з поганого стану в добрий за N днів» тощо |
| proof, [TODO: need case] | доказ | кейс, цифра або відгук, що підтверджують обіцянку; якщо його немає, пишемо «потрібен кейс», а не вигадуємо |
<!-- glossary:end -->
