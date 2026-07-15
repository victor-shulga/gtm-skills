# anticopywriting-ai

Скіл для Claude, який знаходить і прибирає ознаки ШІ-генерації з тексту українською або англійською мовою.

## Що робить

1. Прогоняє текст через автодетектор (`scripts/detect.py`), який рахує ШІ-маркери й видає JSON зі щільністю та топ-порушниками.
2. Завантажує повний список паттернів для відповідної мови (`references/patterns_uk.md` або `references/patterns_en.md`).
3. Переписує проблемні місця, зберігаючи зміст і голос.
4. Робить самоперевірку («що тут все ще видає ШІ?») і другий прохід.
5. Якщо текст для Viktor Shulha — підтягує `about-viktor` для збереження голосу.

## Тригери

«прибери ШІ», «гуманізуй», «humanize», «deslop», «remove AI signs», «це звучить як ChatGPT», «перевір на ШІ», «занадто шаблонно», «забери воду», «make it sound human», «anti-copywriting» тощо.

## Структура

```
anticopywriting-ai/
├── SKILL.md                 # головний файл
├── README.md                # цей файл
├── references/
│   ├── patterns_uk.md       # повний список ШІ-маркерів для української
│   └── patterns_en.md       # повний список ШІ-маркерів для англійської
└── scripts/
    └── detect.py            # автодетектор, повертає JSON із метриками
```

## Окремий запуск автодетектора

```bash
python3 scripts/detect.py path/to/text.txt --lang uk --pretty
python3 scripts/detect.py path/to/text.txt --lang en --pretty
echo "any text" | python3 scripts/detect.py --stdin --lang auto
```

Виводить JSON із полями:
- `language` — мова тексту
- `total_words` — кількість слів
- `total_markers` — загальна кількість ШІ-маркерів
- `ai_density_per_1000_words` — щільність ШІ-маркерів на 1000 слів
- `severity` — `low` (<5), `medium` (5–15), `high` (>15)
- `markers_by_category` — розбивка за категоріями
- `style_metrics` — окремі метрики стилю (тире, жирний, емодзі, лапки, Title Case)
- `top_offenders` — топ-15 знайдених маркерів з номерами рядків і прикладами

## Авторство

- Базується на [Wikipedia: Signs of AI Writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) (WikiProject AI Cleanup).
- Російська версія Георгія Рівери, [t.me/riverapeople](https://t.me/riverapeople).
- Адаптація під українську й англійську + автодетектор — для Viktor Shulha.

## Версія

1.0.0
