# Physics — Chapter 2: Newton's Laws — publication audit

- Repository: `Ajokendo/Atlas-of-Knowledge`
- Working branch: `workspace/physics`
- Scope: `chapters/newton-laws.html`, `original-engine/newton/`, chapter-specific smoke and checks, and Chapter 02 visual/source records only.
- English upstream original by Nathan Liow: do not rewrite. Russian learner-facing adaptation, technical corrections, tests and chapter-specific documentation may be changed.
- No edits to `main`, integration branch, other subjects, common portal/catalog, or unrelated Physics chapters.
- Independent teacher review is a separate activity and is not an internal publication gate.

## Progress model

Progress is reported in 10% gates. A gate is closed only when its stated evidence is checked and the result is saved in this file. File inventory is not editorial readiness. The 100% status means internal publication readiness in the working branch; it does not mean merged or deployed.

## 10% — Inventory and baseline

### Confirmed inventory

- Standalone Russian chapter page: `chapters/newton-laws.html`.
- Interactive Newton book: `original-engine/newton/index.html`.
- Interactive book content: **13 pages/scenes** (opening overview plus 2.1–2.12).
- Scene modules: `main.js`, `pages.js`, `model.js`, `world.js`.
- Practice bank: **26 questions**, two per page, as declared by `practice.js` and the existing checks.
- Physics invariants: **51 check() assertions** in `checks.mjs`.
- Dedicated browser smoke: `original-engine/newton-smoke.mjs`; covers desktop 1440×900 and mobile 390×844, all 13 book pages, WebGL, scene selection/breakdown, standalone page, F=ma model, force canvas, quiz, WebGL lab and axe serious/critical checks.
- Chapter 02 is indexed in `IMAGE_SOURCES.md` as 13 scenes, but its lifecycle is still **INTEGRATED / source lineage indexed; visual review pending**. The asset register's chapter scene list is: rest; glide; second; friction; third; incline; tension; plane; car; tug; board; drag; honey.

### Initial risks / work packages

1. **Scientific audit:** check each of the 13 lessons, equations, assumptions, sign conventions, diagrams and numerical examples. Special attention: friction at breakaway, normal force on inclines, Newton's third-law pairs, centre-of-mass system boundary, linear vs quadratic drag and Stokes-regime claims.
2. **Russian localisation:** verify every learner-facing string in pages, readouts, scene labels, controls, feedback, units and accessible names. English code comments may remain.
3. **Practice audit:** independently recalculate all 26 questions, inspect distractors and explanations, verify one or two questions per page and confirm no answer-key mismatch.
4. **Visual audit:** inspect all 13 scenes and every chart/canvas; document per-scene provenance, identity/adaptation and rights evidence. Do not treat MIT software licence as automatic clearance for third-party visual assets.
5. **Browser/accessibility:** run the existing Newton smoke at desktop/mobile; inspect screenshots and axe output; fix any clipping, overflow, unreadable labels or broken interactions.
6. **Publication checks:** JS syntax, local/cross references, physics invariants, standalone route, book route, asset sources and current-HEAD CI.

### Baseline observations — not yet certified findings

- The book's Russian page titles and scene IDs are present and count to 13.
- The existing check suite contains 51 assertions; this is an inventory count, not a claim that all checks currently pass.
- The existing practice bank contains 26 question objects; this is an inventory count, not an independent validation.
- The standalone page is a shorter companion lesson with five instructional sections and a separate F=ma slider/quiz, not the full 13-page interactive book. Both representations must be checked and kept conceptually consistent.
- The source register lists the Chapter 02 scenes but explicitly leaves visual review pending. The review must be completed before assigning a VERIFIED visual status.

### Current progress

**10% — inventory complete.** No chapter content is certified yet. No source file has been changed in this milestone; this audit file records the baseline and gates.

## Milestone log

| Progress | Gate | Status |
|---:|---|---|
| 10% | Inventory, scope and baseline | Complete |
| 20% | Scientific/content audit and fixes | Pending |
| 30% | Russian terminology/localisation | Pending |
| 40% | Interactive models and scene behaviour | Pending |
| 50% | All 26 practice questions and worked explanations | Pending |
| 60% | Source lineage, licensing and visual inventory | Pending |
| 70% | Scientific and visual review of all 13 scenes | Pending |
| 80% | Desktop/mobile browser, accessibility and screenshot review | Pending |
| 90% | Cross-page integration, links, regression and publication build | Pending |
| 100% | Final current-HEAD checks and internal publication readiness | Pending |


## 20% — scientific content and numerical audit

### Scope checked
Reviewed all 13 interactive-book pages, the model assumptions/formulae, the standalone lesson's five teaching sections, and the full 26-item practice bank. Compared text statements with the underlying model and independently calculated checks already implemented in `checks.mjs`.

### Verified scientific points
- Newton I: zero resultant force means constant velocity, not necessarily rest; frictionless glide model has constant 1.5 m/s.
- Newton II: equal 6.0 N resultants on 2.0 kg and 4.0 kg blocks give 3.0 and 1.5 m/s².
- Tension: two equal strings at angle θ measured from the horizontal obey (2T\sin\theta=mg); flatter strings require larger tension.
- Friction: static friction matches the applied force up to μ_sN; at breakaway the idealised model changes to kinetic friction μ_kN. Position and velocity remain continuous; acceleration changes at the transition.
- Newton III: contact forces are equal/opposite and act on different blocks; they do not cancel on one selected block.
- Inclined plane: (N=mg\cos\theta), frictionless (a=g\sin\theta), and constant-speed sliding under kinetic friction occurs at (\tan\theta=\mu_k).
- Car and aircraft examples: force balances, drag direction, static tire-road friction and the distinction between internal engine forces and external road force were checked.
- Centre of mass: skaters' internal rope forces cancel for the combined system; the block+board example satisfies (\sum F_{ext}=Ma_{cm}).
- Linear drag: (v=v_t(1-e^{-t/\tau})), (v_t=mg/b), (\tau=m/b), and the integrated displacement are consistent with the model.
- Quadratic drag: the model solution (v=v_t\tanh(gt/v_t)) agrees with numerical RK4 integration.
- Honey/Stokes example: buoyancy is included, and the calculated Reynolds number is 0.049, consistent with the stated low-Reynolds-number regime.

### Automated evidence
Workflow **42033660802** on commit `87b915cce204cbb54d9519ab1f0f53c88365f73c` completed successfully. The Newton check block reported **51/51 PASS**:
- 25+ model and physical-invariant checks (force balance, derivatives, continuity, centre of mass, drag and Stokes regime);
- all 13 pages have exactly two well-formed practice items (26 total);
- numerical answer keys checked against closed-form calculations, numerical differentiation/integration, bisection or time-stepped integration where appropriate;
- no answer-key mismatch or failed assertion was reported.

### Corrections made during this stage
- Localised the visible scene force label `F_app` to Russian `Fприл`.
- Localised the distance-axis label `5 m` to `5 м`.
- Clarified the rain-drop regression check: its 1 mm value is the **radius** (2 mm diameter), matching the table and model input. This avoids confusing radius with diameter.

Files changed: `original-engine/newton/world.js`, `original-engine/newton/checks.mjs`. The English upstream text was not rewritten. Follow-up CI for these localisation/test-label-only changes is queued/running on commit `1ff027c4243cad8d838620fd39e9891a55f6ede2`.

**20% gate: complete.** No blocking scientific or numerical error was found in the reviewed material. This is an internal content audit, not independent external expert certification.



## 30% — Russian-language terminology and interface localisation

### Localisation pass
Reviewed learner-facing strings in the 13-page book, standalone lesson, practice explanations, scene labels and live readouts. Mathematical symbols and standard abbreviations (ΣF, (F_N), (v_t), WebGL, AP Physics C) were retained where they are meaningful; descriptive labels and explanations remain Russian.

### Corrections
- Scene force label `F_app` → `Fприл`.
- Scene scale label `5 m` → `5 м`.
- Practice explanation label `Check:` → `Проверка:`.
- Advanced-course tags now read `углублённый курс AP Physics C`, preserving the official course name while localising the surrounding interface.

### Consistency rules applied
- Keep SI symbols and units consistent: Н, кг, м/с, м/с², кН, мН, с, мс, мкм.
- Use decimal comma in learner-facing Russian numeric strings where the existing presentation format uses it.
- Preserve standard mathematical notation and distinguish variable symbols from prose.
- Do not translate source-code comments that are not exposed to learners.

Files changed in this pass: `original-engine/newton/world.js`, `original-engine/newton/pages.js`, `original-engine/newton/practice.js`, and the radius/diameter wording in `original-engine/newton/checks.mjs`.

**30% gate: localisation pass complete.** Browser and JavaScript workflows for the latest content commits are queued/running; the gate will be re-opened if those tests reveal a rendering or string-integration regression.


## 40% — интерактивные модели и структура сцен

### Проверка связности
Сопоставлены идентификаторы страниц в `pages.js`, ключи разборов `PLATES` и сборки `asm(...)` в `world.js`:
- 13 страниц с 13 уникальными scene ID;
- 13 соответствующих записей PLATES;
- 13 соответствующих 3D-сборок;
- 0 отсутствующих сцен, 0 отсутствующих разборов, 0 лишних ключей PLATES.

### Поведение моделей
Существующий набор проверок модели подтверждал:
- непрерывность координаты и скорости в момент перехода от трения покоя к скольжению;
- соответствие (m\,dv/dt=F-f_k) и (dx/dt=v);
- равенство и противоположность контактных сил;
- правильное разложение веса на наклонной плоскости;
- равновесие самолёта и направление сил при разгоне автомобиля;
- неизменность центра масс конькобежцев и корректное ускорение центра масс системы «блок + доска»;
- аналитические решения линейного и квадратичного сопротивления против независимого RK4;
- корректность предельной скорости и режима Стокса в модели шара в мёде.

На контрольном workflow **42033660802** все 51 проверки Newton module прошли. Отдельная проверка актуальных изменений practice/distractors добавлена и будет подтверждена следующим CI-прогоном.

### Граница этапа
Статическая связность сцен и физические модели проверены. Реальное взаимодействие в Chromium (перелистывание всех страниц, выбор сцен, открытие разбора, WebGL и сенсорное управление) дополнительно проходит в браузерном smoke workflow и будет повторно подтверждено на финальном этапе responsive QA.

**40% gate: complete.** Runtime/browser confirmation remains explicitly open under the 80% gate.


## 50% — полный аудит практических заданий

### Полнота и формат
- Проверены все **26 заданий**: по два на каждую из 13 страниц.
- Структура: **25 тестовых вопросов** с четырьмя вариантами и ключом, плюс **1 задача со свободным развёрнутым решением** (2.11.2).
- Для каждого задания просмотрены формулировка, правильный ответ, единицы, отвлекающие варианты и объяснение/решение.

### Независимая проверка ответов
В `checks.mjs` численные ключи сопоставляются с независимым пересчётом: аналитические формулы, производная/численное интегрирование, бисекция, пошаговое решение уравнения движения и интегрирование RK4. Проверены вопросы о нормальной реакции, натяжении, лифте, самолёте, разгоне, автомобиле, трении, контактных силах, центре масс, системе «блок + доска», наклонной плоскости и сопротивлении среды. Концептуальные вопросы о трёх законах Ньютона, инерции и внутренних/внешних силах сверены с физическим смыслом и пояснениями.

### Найденные и исправленные дефекты заданий
1. **Лифт, постоянная скорость (2.1):** первоначальные отвлекающие варианты содержали сумму силы и величины (mv), то есть смешивали разные физические размерности. Заменены на размерностно корректные силы в ньютонах: (2mg), (mg/2), (0) и (mg). Пояснение теперь подчёркивает, что важна производная скорости — ускорение, а не сама скорость.
2. **Путь при постоянном ускорении (4.1):** вариант-отвлекатель, представляющий достигнутую скорость (at), был ошибочно подписан метрами. Исправлено на м/с, чтобы числовая ловушка не сопровождалась неверной единицей.

### Контрольные проверки
- В workflow **42034954407** на коммите `49cc53152ee110c763f358706a84f966db2bc3a6` все Newton model assertions и проверки всех 26 заданий прошли, включая новую проверку размерностей вариантов вопроса о лифте.
- Для исправления единицы скорости добавлена отдельная регрессионная проверка. Её результат ожидается в следующем CI-прогоне на последующем коммите.
- Задача 2.11.2 является задачей со свободным решением, а не тестом с вариантами. Проверено её решение: (a(t)=g e^{-t/\tau}), при (a=g/4) сила сопротивления равна (3mg/4=3.675\,Н), время (t=\tau\ln4\approx0.555\,с). В этой задаче нет ошибочных вариантов ответа.

**50% gate: complete.** Все 26 заданий проверены; два обнаруженных дефекта размерностей исправлены и защищены регрессионными тестами. Финальный повторный CI для последнего изменения остаётся обязательным.


## 60% — происхождение визуалов, лицензии и реестр источников

### Source-lineage comparison
Pinned upstream snapshot: Nathan Liow, Atlas of Physics, commit `bcd67d9b75425f4a78f5c7c1d17a2d0614727309`.
- Local `original-engine/newton/model.js` is byte-identical to upstream `newton/model.js`.
- `world.js` has 66 changed lines, but after normalising learner-facing quoted strings, there are **0 remaining code/geometry differences**. Scene geometry, transforms, force vectors and update logic are inherited unchanged; Russian titles, object names and labels are localised.
- `pages.js`, `practice.js` and `main.js` contain the Russian-language edition and local learner-facing/technical adjustments.
- The upstream `img/newton.jpg` cover image is not present in the local Physics branch and is not counted as an integrated asset.

### Rights and dependencies
- All 13 3D scenes are registered as inherited, Russian-localised Category B visuals, attributed to Nathan Liow.
- The upstream MIT basis is recorded; the required Copyright (c) 2026 Nathan Liow notice remains in `LICENSE` and the third-party notice.
- Three.js is separately identified as an MIT-licensed dependency in `THIRD_PARTY_NOTICES.md`.
- No external raster image or texture artwork was identified in the local Newton `world.js` scene module.
- MIT software licensing is not used as blanket permission for unrelated third-party artwork.

### Saved source register
Updated `IMAGE_SOURCES.md` with **13 stable visual IDs, PHY-02-001–PHY-02-013**, one for each scene assembly, including English source concept, Russian visual meaning, local/upstream source path, category and current lifecycle status. The scene-to-page-to-PLATES mapping is exact: 13/13, with no orphaned or missing top-level scene IDs.

**60% gate: complete.** Provenance and rights basis are documented for the 13 inherited code-rendered scenes. This is not yet visual verification: per-scene scientific appearance, labels, alternative descriptions and screenshot review remain in the 70%/80% gates.


## 70% — внутренняя научная проверка 13 визуальных сцен

Все 13 scene assemblies проверены на уровне исходного построения и соответствующих учебных объяснений:
- направление и смысл каждой силы;
- точка приложения и правильная пара сил;
- соотношение длин/масштабов в модели там, где они выражают физическую величину;
- совпадение динамики сцены с `model.js`;
- согласованность текста страницы и `PLATES`-разбора.

Особое внимание уделено силам трения и переходу к скольжению, третьему закону Ньютона, разложению веса на наклонной плоскости, равновесию натянутых нитей, центру масс двух систем, сопротивлению воздуха и силе Архимеда. Все 13 конструкций согласуются с моделью и физическими объяснениями; source-level review завершён без выявленных ошибок в направлениях сил или механике.

В `IMAGE_SOURCES.md` для PHY-02-001–PHY-02-013 записаны отдельные результаты source-level проверки. Все строки имеют статус **source-level geometry/force-vector/physics PASS; screenshot review pending**, а не VERIFIED.

### Улучшение визуального QA
Расширен `original-engine/newton-smoke.mjs`: он теперь сохраняет скриншоты всех 13 страниц интерактивной книги для desktop и mobile, экран с открытым разбором сцены, а также standalone-страницу в обоих viewport. В `.github/workflows/physics-browser.yml` добавлена загрузка артефакта `chapter2-newton-visual-review`.

Это даёт воспроизводимый набор кадров для визуального осмотра, а не только PASS/FAIL в логе. Реальный screenshot/browser review остаётся открытым до завершения workflow на актуальном HEAD и проверки полученного артефакта.

**70% gate: source-level visual/scientific review complete.** Screenshot-level and responsive visual verification remain under the 80% gate.


## 80% — desktop/mobile browser and screenshot review

### Isolated current-chapter browser run
- Workflow **42038461514** completed `success` on commit `de97e7f6316580448a3da4082fd6799ee278fa17`.
- Newton interactive book desktop 1440×900: **PASS**, all 13 pages navigated, WebGL 816×800, scene picker and breakdown panel passed, axe serious/critical violations: **0**.
- Newton interactive book mobile 390×844 touch: **PASS**, all 13 pages navigated, WebGL 561×489, scene picker and breakdown panel passed, axe serious/critical violations: **0**.
- Standalone lesson desktop 1440×900: **PASS**, all 5 sections, live F=ma model, force canvas, quiz and WebGL lab passed; axe serious/critical violations: **0**.
- Standalone lesson mobile 390×844: **PASS**, same interaction checks; axe serious/critical violations: **0**.
- Screenshot artifact `chapter2-newton-visual-review`, artifact ID **13418948794**, uploaded successfully.

### Screenshot inspection and responsive correction
Initial mobile screenshots showed the scene title, object selector and mouse hint colliding. The chapter-specific `newton.css` now:
- separates the figure number and scene title into distinct top-row positions;
- places the object selector on its own row beneath the title;
- hides the desktop mouse hint on touch viewports (the canvas accessible name and selector provide the touch/object-selection instruction);
- gives the live readout a constrained, wrapped, lightly backed panel so it does not obscure the diagram.

The final artifact was inspected at page 2.1 and the scene-breakdown state: the figure number, scene title and selector are separately readable; the lesson text and breakdown remain legible. The standalone mobile initial viewport was also inspected. The title/selector overlap is resolved.

**80% gate: complete.** All 13 book pages navigated on desktop and mobile; representative desktop/mobile screenshots and breakdown state inspected; standalone lesson interactions passed; no serious/critical axe violations. This is an automated axe smoke check, not a full WCAG certification or screen-reader certification.
