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
