# Atlas of Knowledge — стандарт педагогической обратной связи: физика
# Atlas of Knowledge — Teacher Feedback Standard: Physics

**Дисциплина / Subject:** Physics / Физика  
**Рабочая ветка / Working branch:** `workspace/physics`  
**Область / Scope:** только физический атлас. Документы не разрешают менять общие файлы портала или другие дисциплины.

## 1. Назначение / Purpose

Система предназначена для будущего педагогического пилота с приглашёнными учителями после завершения портала. Это сбор содержательной педагогической обратной связи, а не независимая научная экспертиза, сертификация или формальное рецензирование.

The system is intended for a future pedagogical pilot with invited teachers after the portal is complete. It gathers practical educational feedback; it is not independent scientific peer review, certification, or formal accreditation.

Оцениваются: соответствие школьной программе и возрасту, ясность объяснений, физическая точность, русско-английская паритетность, иллюстрации, интерактивные лаборатории, доступность и применимость на уроках.

## 2. Точки входа / Entry points

В будущем физический атлас может иметь две точки входа: «Оценить атлас целиком» и «Сообщить о проблеме в этой главе/элементе». При открытии из главы должны предварительно заполняться предмет, язык, путь страницы и якорь элемента; учитель может их изменить.

In a future release, Physics may provide “Review the whole atlas” and “Report an issue in this chapter/element”. When opened from a chapter, subject, language, page path, and element anchor should be prefilled and remain editable.

**На текущем этапе точки входа не добавляются в опубликованный интерфейс.** Этот пакет — подготовительная документация и отключённый шаблон.

## 3. Единые категории / Shared categories

1. Научная или фактическая ошибка / Scientific or factual correction
2. Источник, ссылка или данные / Source, citation, or data concern
3. Объяснение, структура или методика / Explanation, structure, or pedagogy
4. Перевод или терминология RU/EN / Russian-English translation or terminology
5. Иллюстрация, схема, график или таблица / Illustration, diagram, graph, or table
6. Интерактивная лаборатория или техническая проблема / Interactive laboratory or technical issue
7. Доступность или мобильное отображение / Accessibility or mobile display
8. Предложение / Suggestion

Не использовать публичные звёздные рейтинги как показатель научного качества. / Do not use public star ratings as a proxy for scientific quality.

## 4. Обязательные критерии анкеты / Required questionnaire criteria

Каждый критерий оценивается по шкале 1–5 или «Не могу оценить / Cannot assess»:
1. Соответствие школьной программе / Curriculum alignment
2. Соответствие возрасту и уровню учащихся / Age and learner-level appropriateness
3. Понятность объяснений / Clarity of explanations
4. Научная и фактическая точность / Scientific and factual accuracy
5. Качество русского и английского языков / Russian and English language quality
6. Иллюстрации и визуальные материалы / Illustrations and visual materials
7. Полезность интерактивных инструментов / Usefulness of interactive tools
8. Применимость на уроках / Classroom usefulness
9. Мобильное удобство и доступность / Mobile usability and accessibility

Физическая адаптация дополнительно спрашивает о формулах, обозначениях, размерностях и единицах СИ; точности законов и объяснений; соответствии 3D/интерактивных лабораторий описываемым явлениям; корректности графиков, параметров, допущений и результатов экспериментов.

Physics-specific prompts cover formulas, symbols, dimensions and SI units; accuracy of laws and explanations; fidelity of 3D/interactive laboratories to the described phenomena; and correctness of graphs, parameters, assumptions, and experiment results.

## 5. Приоритет замечаний / Issue priority

- Критическая ошибка / Critical error — может закрепить опасное или принципиально неверное понимание, приводит к неверным физическим выводам или расчётам.
- Существенная проблема / Major issue — заметно искажает объяснение, формулу, модель или учебную последовательность.
- Рекомендация / Improvement recommendation — улучшает ясность, доступность или преподавание, но не указывает на фактическую ошибку.
- Дополнительное предложение / Additional idea — новая тема, пример, лаборатория или функция.

Приоритет, выбранный учителем, является сигналом для проверки, а не готовым редакционным решением.

## 6. Минимизация данных и согласие / Data minimisation and consent

Имя, школа/организация и контакт для ответа необязательны. Регистрация и электронная почта не требуются для обычного отзыва. Не запрашивать сведения об учениках, здоровье или иные чувствительные данные. Анонимный отзыв не позволяет направить персональный ответ.

Публикация отзыва, цитаты, имени или организации требует отдельного явного добровольного согласия. Согласие на публикацию имени и согласие на публикацию текста должны быть раздельными. Отказ не влияет на рассмотрение замечания.

Name, school/organisation, and reply contact are optional. No registration or email is required for ordinary feedback. Do not collect student information or sensitive personal data. Anonymous feedback cannot receive an individual reply.

Publishing a review, quotation, name, or organisation requires separate, explicit, voluntary consent. Consent to publish identity and consent to publish comment text must be separate. Declining publication does not affect review.

## 7. Закрытая модерация и научная добросовестность / Private moderation and scientific integrity

Все будущие отправки сначала поступают в закрытую очередь. Комментарий — проверяемое утверждение, а не доказательство ошибки. Научные исправления сверяются с надёжными учебниками, первичными публикациями и авторитетными образовательными источниками. Педагогические рекомендации рассматриваются отдельно от фактических ошибок.

Решения: исправить; принять как рекомендацию; запросить уточнение; отложить; отклонить с обоснованием; объединить с дубликатом. Для принятого изменения фиксировать старую и новую формулировку, источник/обоснование, дату и commit SHA. Не менять научный материал автоматически по одному отзыву.

All future submissions first enter a private moderation queue. A comment is a claim to investigate, not proof of error. Scientific changes must be checked against reliable textbooks, primary publications, and authoritative educational sources. Pedagogical recommendations are assessed separately from factual errors.

Possible decisions: correct; accept as recommendation; request clarification; defer; reject with rationale; mark duplicate. For accepted changes, record old and new wording, evidence/rationale, date, and commit SHA. Never change scientific content automatically from a single submission.

## 8. Техническая и доступная реализация / Technical and accessible implementation

Статическая HTML-форма сама по себе не обеспечивает безопасное хранение и модерацию. Для будущего запуска потребуется одобренный HTTPS endpoint, закрытое хранилище с разграничением доступа, серверная валидация, защита от спама и ограничение частоты запросов, политика хранения и удаления данных, а также проверка безопасности.

The current static HTML atlas cannot securely store or moderate submissions by itself. Future activation requires an approved HTTPS endpoint, private storage with access controls, server-side validation, spam protection and rate limiting, a data-retention/deletion policy, and security testing.

Требования интерфейса: русский и английский языки; клавиатурная навигация и видимый фокус; семантические подписи; сообщения об ошибках; экранные дикторы; мобильные экраны; отсутствие зависимости только от цвета. Не показывать подтверждение получения до ответа сервера.

UI requirements: Russian and English; keyboard navigation and visible focus; semantic labels; clear errors; screen-reader support; mobile layouts; no colour-only cues. Never display a receipt confirmation before the server confirms receipt.

## 9. Ограничение текущего этапа / Current-stage restriction

**ПРИЁМ ОТВЕТОВ НЕ ВКЛЮЧАТЬ.** Нет публичной формы отправки, активной кнопки, сетевого запроса, endpoint, базы/таблицы ответов или внешнего сервиса. Шаблон служит только макетом для будущей реализации и должен явно сообщать, что ответы не отправляются и не сохраняются. Включение возможно только после завершения портала, отдельной проверки безопасности и технического тестирования и прямого разрешения владельца проекта.

**DO NOT ENABLE SUBMISSION.** There is no public submission form, active submit button, network request, endpoint, response database/table, or external service. The template is a future implementation mock-up only and must clearly state that responses are neither sent nor stored. Activation requires portal completion, separate security and technical testing, and the project owner's explicit approval.

## 10. Связанные файлы / Related files

- `PHYSICS_FEEDBACK_QUESTIONNAIRE.md` — двуязычная анкета / bilingual questionnaire.
- `FEEDBACK_MODERATION_GUIDE.md` — порядок обработки / moderation workflow.
- `FEEDBACK_WIDGET_TEMPLATE.html` — отключённый интерфейсный макет / disabled UI mock-up.
- `FEEDBACK_PORTING_GUIDE.md` — локальные правила адаптации / subject implementation note.

## 11. Контрольный список / Checklist

- [x] Предметная специфика физики описана / Physics-specific requirements documented.
- [x] Общие категории, приоритеты и приватность сохранены / Shared categories, priorities, and privacy preserved.
- [x] Реальный сбор ответов запрещён на текущем этапе / Live intake prohibited at this stage.
- [ ] Визуальная и техническая интеграция в страницы атласа — только после отдельного разрешения / UI integration only after separate approval.
- [ ] Endpoint, хранилище, безопасность и end-to-end тесты — только перед будущим запуском / Endpoint, storage, security, and end-to-end tests only before future launch.
