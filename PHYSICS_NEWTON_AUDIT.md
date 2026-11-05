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
