# Physics — предметная адаптация стандарта обратной связи
# Physics — Subject Feedback Implementation Note

**Основа / Based on:** `biology/FEEDBACK_SYSTEM_STANDARD.md`, `biology/FEEDBACK_PORTING_GUIDE.md`, and the Atlas of Knowledge shared feedback principles.  
**Рабочая ветка / Branch:** `workspace/physics`.  
**Граница / Boundary:** только физический атлас; не менять Biology, Chemistry, Geography, портал, каталог или настройки публикации.

## 1. Файлы / Files

- `FEEDBACK_SYSTEM_STANDARD.md` — адаптация общего стандарта для физики.
- `PHYSICS_FEEDBACK_QUESTIONNAIRE.md` — двуязычная анкета.
- `FEEDBACK_MODERATION_GUIDE.md` — порядок проверки и решений.
- `FEEDBACK_WIDGET_TEMPLATE.html` — отключённый макет формы.

## 2. Предметные поля / Subject-specific prompts

Фиксировать точную главу/подраздел, формулу, физическую величину, размерность, единицу СИ, график, лабораторию, параметр модели и наблюдаемый результат. Эти поля помогают локализовать проблему, но не должны превращаться в обязательный сбор лишних персональных данных.

Capture the exact chapter/section, equation, physical quantity, dimension, SI unit, graph, laboratory, model parameter, and observed result. These fields help locate an issue and must not become a reason to collect unnecessary personal data.

## 3. Точки входа / Entry points

Будущие варианты: отзыв об атласе целиком; замечание к конкретной главе/элементу. При интеграции из страницы главы можно передать page path, язык и content anchor. **В текущем задании не добавлять эти точки входа на сайт** — для этого требуется отдельное согласование.

Future options: review the whole atlas; report an issue on a specific chapter/element. A future chapter integration may pass page path, language, and content anchor. **Do not add these entry points to the live site in this task**; separate approval is required.

## 4. Безопасное состояние / Safe state

- Не подключать внешний сервис или endpoint.
- Не добавлять сетевой код отправки.
- Не создавать хранилище ответов.
- Не включать форму в страницы атласа.
- В HTML-макете submit-кнопка постоянно disabled.
- Рядом явно сообщать, что данные не отправляются и не сохраняются.
- Любое включение — только после завершения портала, отдельного security review, end-to-end проверки и прямого разрешения владельца.

No external service or endpoint; no network submission code; no response storage; no embedding in atlas pages; submit button permanently disabled in the mock-up; explicit notice that data is not sent or stored. Activation requires portal completion, separate security review, end-to-end testing, and the owner's explicit approval.

## 5. Проверки / Checks

Перед передачей проверить: RU/EN parity; обязательные 9 критериев и 7 физических критериев; «Cannot assess»; необязательность контакта; раздельное согласие на публикацию; точную локализацию; постоянное отключение кнопки; отсутствие fetch/XHR/beacon/form action и внешних подключений.
