# Atlas of Knowledge

Бесплатный интерактивный атлас для школьников Кыргызстана. Предметы разбиты по темам, а не по классам. Весь текст на русском и английском.

## Предметы

- **Физика** — `physics/`. Своя физика на явлениях Кыргызстана. Блок I: измерения, строение вещества, движение и силы, давление, работа и энергия, простые механизмы. Готова глава 1.
- **Химия** — `chemistry/`.
- **Биология** — `biology/`.
- **География** — `geography/` (исходники глав в `geography/chapters/*.md`, страницы для чтения в `geography/read/`).

Главная страница — `index.html` (портал). `catalog.html` — каталог глав, `progress.html` — личный прогресс ученика.

## Запуск локально

```bash
python3 -m http.server 8137
```

Затем откройте http://localhost:8137.

## Проверки

```bash
node .github/scripts/check-local-links.mjs
node .github/scripts/check-inline-js.mjs
node chemistry/checks.mjs
node biology/checks.mjs
```

## История

Раньше на сайте была русская адаптация открытого учебника Atlas of Physics (Nathan Liow, лицензия MIT: https://github.com/nathanliow/atlas-of-physics). 9 ноября 2026 года её убрали с сайта и заменили своей физикой; код остаётся в истории git. Лицензия и уведомления — в `LICENSE` и `THIRD_PARTY_NOTICES.md`.
