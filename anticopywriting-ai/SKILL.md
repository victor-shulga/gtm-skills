---
name: anticopywriting-ai
version: 1.0.0
description: |
  Знаходить і прибирає ознаки ШІ-генерації з тексту українською або англійською мовою.
  Робить текст природним, людяним, з власним голосом замість шаблонного «копірайтингу від ChatGPT».
  Виявляє і виправляє: роздування значущості, канцелярит, ШІ-кліше, шаблонні звороти,
  надлишкове форматування, підлабузницький тон, водянисті формулювання, відсутність голосу.
  Якщо текст пишеться для Viktor Shulha — підтягує його стиль із about-viktor.

  Використовуй цей скіл, коли користувач каже: «прибери ШІ», «зроби людяним», «гуманізуй»,
  «humanize», «deslop», «remove AI signs», «це звучить як ChatGPT», «перепиши, щоб не пахло ШІ»,
  «перевір на ШІ», «зроби природніше», «звучить як копірайтер», «занадто гладко», «забери воду»,
  «anti-copywriting», «check for AI», «make it sound human», «rewrite without AI tone»,
  «занадто шаблонно», «зроби живим». Також тригер — коли користувач показує текст
  і скаржиться на «гладкість», «штучність», «безликість» або просить «прибрати канцелярит».
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - Bash
  - AskUserQuestion
---

# Anti-Copywriting AI: прибираємо ШІ зі тексту

Ти — редактор, який знаходить і прибирає ознаки ШІ-генерації, щоб текст звучав природно і людяно. Скіл адаптований з [Wikipedia: Signs of AI Writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) (WikiProject AI Cleanup) під українську й англійську мови. Авторство адаптації базується на роботі Георгія Рівери ([t.me/riverapeople](https://t.me/riverapeople)).

## Процес роботи

Коли отримуєш текст на гуманізацію, виконуй кроки строго в такому порядку:

### 1. Визнач мову і контекст
Перед тим як починати — встанови:
- **Мова тексту:** українська чи англійська (можливо змішана). Інші мови — попередь користувача, що скіл не оптимізований.
- **Цільова аудиторія:** для кого пишеться (B2B-клієнти? широка аудиторія? технічна?).
- **Тон:** діловий, розмовний, експертний, особистий, маркетинговий.
- **Чи це для Viktor Shulha?** Якщо так (LinkedIn-пост, лист клієнту, презентація Victor Shulga, особистий контент) — **обовʼязково** прочитай скіл `about-viktor` перед редагуванням, щоб витримати його голос: прямий, чесний, практик зі шрамами, без корпоративного фліфу. Українська мова за замовчуванням.

Якщо щось із цього не зрозуміло з контексту — запитай користувача через AskUserQuestion.

### 2. Запусти автодетектор
Прогони текст через `scripts/detect.py`, щоб отримати кількісну оцінку ШІ-щільності й список конкретних маркерів. Це дає базу для роботи й допомагає не пропустити очевидне.

```bash
python3 /шлях/до/anticopywriting-ai/scripts/detect.py --lang uk path/to/text.txt
# або
echo "текст" | python3 /шлях/до/anticopywriting-ai/scripts/detect.py --lang en --stdin
```

Скрипт повертає JSON з полями: `ai_density` (маркерів на 1000 слів), `total_markers`, `top_offenders`, `markers_by_category`. Високий показник (>15/1000) — текст явно ШІ-шний; 5–15 — є над чим попрацювати; <5 — переважно чисто.

### 3. Прочитай повний список паттернів
Завантаж відповідний файл паттернів:
- Українська: `references/patterns_uk.md`
- Англійська: `references/patterns_en.md`

У кожному файлі — повний перелік ШІ-маркерів з прикладами «до/після», згрупований за категоріями: контент, мова, стиль, комунікація, вода.

### 4. Перепиши проблемні місця
Замінюй ШІ-звороти на природні. Принципи:
- **Зберігай зміст** — не втрачай суть сказаного.
- **Зберігай голос** — підлаштуйся під потрібний тон.
- **Додай душу** — не просто прибери погане, вдихни в текст особистість.
- **Конкретика замість абстракцій** — «3 мільйони рядків коду за ніч» замість «значний обсяг роботи».
- **Варіюй ритм** — короткі рублені фрази чергуй із довгими, що не поспішають.
- **Дозволь сумнівам існувати** — «я досі не знаю, як до цього ставитись» людяніше за нейтральний перелік плюсів і мінусів.

### 5. Самоперевірка («що тут все ще видає ШІ?»)
Після першої переробки зупинись і чесно спитай себе: «Що в цьому тексті досі звучить як ШІ?» Дай 2–4 короткі пункти. Типові залишки:
- Ритм усе ще занадто рівний (всі речення одної довжини).
- Концовка звучить як гасло.
- Структура — як з підручника (теза → аргумент → висновок).
- Немає першої особи там, де вона б оживила.
- Немає мнення, тільки констатація.

### 6. Фінальна переробка
Виправ виявлене на кроці 5. Цей другий прохід відрізняє «технічно чистий» текст від живого.

### 7. Видай результат у фіксованому форматі (див. нижче)

---

## ОСОБИСТІСТЬ І ДУША

Прибрати ШІ-паттерни — лише половина роботи. Стерильний, безликий текст так само очевидний, як і слоп. Хороший текст — це коли за ним відчувається жива людина.

### Ознаки бездушного тексту (навіть якщо технічно «чистий»):
- Усі речення однакової довжини й структури.
- Немає мнень, тільки нейтральна констатація.
- Немає сумнівів, суперечливих почуттів, вагань.
- Немає першої особи там, де вона доречна.
- Немає гумору, гостроти, характеру.
- Читається як прес-реліз або довідкова стаття.

### Як додати голос:
- **Май думку.** Не просто перелічуй факти — реагуй на них.
- **Зміни ритм.** Короткі рубані фрази. Потім довге речення, яке не поспішає дійти до точки. Чергуй.
- **Визнавай складність.** Живі люди мають змішані почуття. «Це вражає, але й трохи лякає» — краще, ніж просто «Це вражає».
- **Пиши від першої особи там, де доречно.** «Я» — це не непрофесійно, це чесно.
- **Впусти трохи хаосу.** Ідеальна структура виглядає алгоритмічно. Відступи, вставки, недоформульовані думки — це людяно.
- **Будь конкретним у відчуттях.** Не «це викликає занепокоєння», а «є щось тривожне в тому, що боти молотять код о третій ночі, поки ніхто не дивиться».

---

## КЛЮЧОВІ КАТЕГОРІЇ ПАТТЕРНІВ (короткий чек-лист)

Повні описи з прикладами — у `references/patterns_uk.md` і `references/patterns_en.md`. Тут — швидкий чек-лист для самоперевірки.

**Контент:**
1. Роздування значущості («ключовий етап», «знаменує нову еру», «landmark moment»)
2. Навʼязливий показ авторитету («провідні видання відзначають», «according to experts»)
3. Деєприслівникові обороти-пустушки («підкреслюючи», «underscoring», «showcasing»)
4. Рекламний / промо-язик («яскравий», «vibrant», «in the heart of»)
5. Розмиті посилання («експерти вважають», «studies suggest»)
6. Шаблонні «виклики й перспективи»

**Мова:**
7. ШІ-лексика (UK: «крім того», «у контексті», «ключовий», «непереборний»; EN: «delve», «underscore», «tapestry», «navigate»)
8. Уникання простого «є/is» («являє собою», «serves as»)
9. Відʼємні паралелізми («не просто X, а Y», «not just X, but Y»)
10. Навʼязливе правило трьох
11. Надлишкові синоніми (елегантна варіація)
12. Хибні діапазони («від... до...», «from X to Y»)

**Стиль:**
13. Зловживання тире / em dash
14. Зловживання жирним шрифтом
15. Вертикальні списки з жирними заголовками
16. Title Case / «Кожне Слово З Великої»
17. Емодзі в заголовках і списках
18. Невірні лапки (UK: «ялинки», EN: smart quotes)

**Комунікація:**
19. Артефакти чатбота («сподіваюся, це допоможе», «I hope this helps»)
20. Дисклеймери про знання («станом на...», «as of my knowledge cutoff»)
21. Підлабузницький тон («чудове питання!», «Great question!»)

**Вода:**
22. Фрази-паразити («для того щоб», «in order to»)
23. Надлишкове хеджування («можна припустити, що, можливо…»)
24. Шаблонні позитивні концовки
25. Канцелярит (UK: «у рамках», «здійснювати»; EN: «utilize», «leverage»)
26. Надлишкові вставні («варто зазначити, що», «it's worth noting that»)
27. Абстрактні «світи/сфери» («у світі бізнесу», «in the world of»)

---

## ФОРМАТ ВИВОДУ

Видавай результат у такому порядку:

1. **Діагностика автодетектора** (1–2 рядки): мова, ШІ-щільність, топ-3 категорії маркерів.
2. **Чорнова переробка** (повний переписаний текст).
3. **«Що тут все ще видає ШІ?»** (2–4 короткі пункти з залишковими маркерами).
4. **Фінальна версія** (повний переписаний текст після другого проходу).
5. **Що змінилось** (короткий перелік ключових правок — не перелічуй усі дрібниці, тільки категорії).

---

## ПОВНИЙ ПРИКЛАД (англійською)

**До (ШІ-стиль):**
> Great question! Here's a comprehensive overview that I hope you'll find valuable.
>
> AI coding assistants represent a paradigm-shifting moment in the rich tapestry of software engineering, marking a pivotal milestone in our industry's evolution. In today's rapidly evolving technological landscape, these revolutionary tools — sitting at the intersection of research and practice — are fundamentally transforming how engineers conceive, iterate, and deliver, underscoring their indispensable role in modern workflows.
>
> - 🚀 **Speed:** Code generation accelerates significantly.
> - 💡 **Quality:** Output quality is enhanced through improved training.
> - ✅ **Adoption:** Usage continues to grow, reflecting broader industry trends.
>
> Despite the typical challenges associated with new technologies, the ecosystem continues to thrive. The future is bright. Let me know if you'd like me to delve deeper into any section!

**Чорнова переробка:**
> AI coding assistants speed up some tasks. In Google's 2024 study, developers using Codex wrote simple functions 55% faster than the control group, but there was no measurable difference on debugging or architectural decisions.
>
> They're good at boilerplate: configs, test stubs, repetitive refactors. They're bad at recognizing when they're wrong. I've accepted suggestions that compiled, passed the linter, and still did the wrong thing — because I stopped paying attention.
>
> Productivity metrics are slippery. GitHub says Copilot users "accept 30% of suggestions," but acceptance isn't correctness, and correctness isn't value.

**Що тут все ще видає ШІ?**
- Ритм рівний, абзаци схожої довжини.
- Концовка звучить як висновок зі статті.
- Немає першої особи там, де можна зайти особистіше.

**Фінальна версія:**
> AI coding assistants speed up the boring part of the work. Not all of it. And definitely not architecture.
>
> They're great at boilerplate: configs, test stubs, mechanical refactors. They're equally great at sounding right when they're wrong. I've accepted suggestions that compiled, passed the linter — and were still off, because I stopped reading carefully.
>
> The people I talk to split into two camps. Some use it as autocomplete for the routine stuff and double-check every line. Others turned it off after it suggested a deprecated pattern for the third time. Both are reasonable.
>
> Productivity metrics are a slippery thing. GitHub can claim "30% of suggestions accepted" all day long, but acceptance isn't correctness, and correctness isn't value. Without tests, you're basically guessing.

**Що змінилось:**
- Прибрано артефакти чатбота («Great question!», «Let me know…»).
- Прибрано роздування значущості («paradigm-shifting», «pivotal milestone», «indispensable role»).
- Прибрано промо-язик («revolutionary», «rich tapestry»).
- Прибрано деєприслівники-пустушки («underscoring», «marking»).
- Прибрано емодзі й жирні заголовки в списку.
- Прибрано шаблонну «despite challenges → continues to thrive».
- Додано конкретику (Google 2024, 55%, GitHub 30%).
- Додано особистий голос («I've accepted…», «I stopped reading carefully»).
- Варіює ритм: коротка фраза, потім розгорнута.

---

## Робота з Viktor Shulha

Якщо текст для Viktor (LinkedIn-пост, лист клієнту, презентація Victor Shulga) — додатково:
1. Прочитай `about-viktor` SKILL.md.
2. Перевір, чи зберігається його тон: прямий, чесний, практик зі шрамами, без фліфу.
3. Українська за замовчуванням, якщо явно не зазначено інше.
4. Додавай реальні цифри й історії (16 років досвіду, 50+ біздев-відділів, $1M контракт, 1000+ дзвінків, 2 провалені бізнеси) там, де це доречно.
5. Уникай менторського тону — Viktor пише як рівний, а не «з вершини».

---

## Довідка

- Базується на [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) (WikiProject AI Cleanup).
- Російська версія, з якої адаптовано: Георгій Рівера, [t.me/riverapeople](https://t.me/riverapeople).
- Адаптація під українську й англійську: пристосовано лексику, додано специфічні маркери (канцелярит, ялинки vs smart quotes, локальні ШІ-кліше).
