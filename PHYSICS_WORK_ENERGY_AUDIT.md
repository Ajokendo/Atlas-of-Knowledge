# Physics — Chapter 04 audit

- Chapter: **Работа, энергия и мощность / Work, Energy and Power**
- Working branch: `workspace/physics`
- Audit started: 2026-11-06
- Baseline commit: `9bc9bb153fe0adf413ee4d76a56f35baf6d052bd`
- Scope: internal publication-readiness review of the Russian edition; Nathan Liow's English source is not to be edited.
- Merge/deployment: not performed.

## Progress

| Milestone | Status | Evidence |
|---|---|---|
| 10% — inventory and branch guard | PASS | Standalone Russian lesson, 12-page interactive book, 12 scene keys, 12 practice-page groups, model, world, main and regression files located in the assigned Physics workspace |
| 20% — model and numerical regression baseline | PASS | Current-HEAD JavaScript validation (run 42154158118) and Physics Engine checks (run 42154158123) passed on commit 9bc9bb1; energy/checks.mjs contains 67 explicit checks, including independent numerical answer recomputation |
| 30% — learner-facing text and formula audit | PASS | Reviewed all 12 interactive-book page explanations and all 9 standalone lesson sections. Removed an untranslated English sentence from the standalone SVG caption. Clarified that kinetic-energy change depends on net work, and distinguished average from instantaneous power with the general directional factor cos α |
| 40% — practice and answer-key audit | PASS | Confirmed 24 questions across 12 pages: 22 multiple-choice and 2 free-response. Numeric answers are independently recomputed; conceptual keys/explanations for zero work, net work, speed scaling and spring compression have explicit regressions. Physics Engine passed all 72 assertions on commit 7953581 |
| 50% — model assumptions and edge cases | PASS | Reviewed all 12 scenario families and documented assumptions: frictionless pull/spring, gravity-only toss/drop/pendulum, centripetal tension, net work, variable force, potential curves, Lennard–Jones bond, kinetic friction and steady-speed lift. The 3D lab uses g = 9.80 m/s² and its height/energy readout decreases from 10 m to 1 m as the object moves downhill. All 72 Physics Engine assertions passed on commit 7953581; the final visual-scale regression is being rerun |
| 60% — visual source lineage and rights | IN PROGRESS | Compared all 5 local energy modules with Nathan Liow’s pinned upstream snapshot. Mapped all 12 page descriptors to their inherited scene assemblies and documented MIT attribution plus the bond-potential graph-range adaptation in IMAGE_SOURCES.md. Three standalone-page visuals still need final creator/rights classification and per-visual evidence |
| 70% — scientific visual review | IN PROGRESS | Reviewed all 12 scene/PLATES mappings against the model and practice checks. Screenshot review found and corrected the clipped repulsive branch of the Lennard–Jones graph; final screenshots at the 0.4 m/eV scene scale are pending |
| 80% — desktop/mobile visual QA | IN PROGRESS | Dedicated browser run 42160523319 passed all 12 pages and the standalone lesson on desktop/mobile. All 24 book screenshots plus standalone screenshots were inspected. Mobile selector/title and desktop hint/readout overlaps were fixed in energy.css with geometry regressions; final run after the bond-scene scale correction is pending |
| 90% — integration and regression | IN PROGRESS | Dedicated browser workflow passed book navigation, scene picker, standalone controls, chart, quiz and WebGL lab; serious/critical axe findings and horizontal overflow checks passed. Final browser rerun on current branch head is pending |
| 100% — final internal readiness | PENDING | All chapter-specific checks green on final source commit; evidence saved in this audit |

## Inventory

### Standalone lesson
- File: `chapters/work-energy.html`
- Nine lesson sections: introduction; mechanical work; work–energy theorem; kinetic and potential energy; conservation of mechanical energy; power; interactive energy model; efficiency; knowledge check.
- Includes a force/displacement SVG diagram, an interactive three-control energy calculator (mass, speed, height), a canvas energy comparison chart, and a knowledge-check question.
- The calculator uses (g=9.80\,\mathrm{m/s^2}), consistent with the Chapter 4 engine model.

### Interactive book
- Files: `original-engine/energy/{index.html,main.js,pages.js,world.js,model.js,practice.js,checks.mjs}`.
- 12 pages and 12 scene keys: pull, toss, whirl, car, drop, spring, push, bead, bond, pendulum, slide and lift.
- Practice is organized across all 12 page indices; the source inventory contains 24 question definitions.
- The current regression file contains 67 explicit `check()` assertions, including model invariants, energy conservation, phase transitions, force/potential derivatives and recomputation of numerical practice answers.

## Known pre-audit history
- The standalone chapter was previously expanded to clarify the angle in the work formula, joule, elastic potential energy, the arbitrary zero of gravitational potential energy, non-conservative work, and average versus instantaneous power.
- The work–energy theorem was added as a separate section and explicitly tied to the net work of all forces.
- The interactive book now explicitly distinguishes the work of one force from the net work, and average power from instantaneous power with the angle between force and velocity.
- The HTML calculator's gravitational acceleration was unified at 9.80 m/s² with the engine model.
- The spring model gained explicit continuity checks at first contact and release.
- The nonlinear pendulum gained opposite-turning-point, full-period return, angular-acceleration and radial-force-balance checks.
- The Lennard–Jones numerical tolerances were corrected to avoid comparing floating-point residuals to exact zero with an unrealistically strict absolute tolerance.
- These prior changes are historical evidence, not a substitute for this audit's final browser and visual review.

## Publication boundary
“100%” will mean internally checked and ready for publication in the working branch. It does not mean external certification, specialist teacher approval, merge to `main`, or deployment. The English upstream is not to be edited.

## 30% — learner-facing text corrections

- Read all 12 interactive-book page bodies and the complete standalone lesson. Core equations and examples for work, kinetic energy, gravitational/elastic potential energy, conservation, power and efficiency are consistent with the model.
- Removed an untranslated English sentence duplicated below the Russian force/displacement SVG caption in `chapters/work-energy.html`; added a browser regression guard against its return.
- Page 4.1 previously implied that positive work by any one force necessarily increases kinetic energy. It now states that the sign describes that force's contribution and that the change in kinetic energy is determined by the sum of the work of all forces.
- Page 4.11 previously gave (P=Fv) without its directional condition. It now distinguishes average power (P_{ср}=W/Δt) from instantaneous power (P=Fv\cos α), and states that (P=Fv) when force is parallel to velocity.
- English upstream content was not changed.

## Model and cross-component consistency findings

- The standalone HTML calculator and engine model use (g=9.80\,\mathrm{m/s^2}). The shared Chapter 04 3D lab had retained (g=9.81\,\mathrm{m/s^2}); this was corrected in the Chapter 04 branch of `physics-lab.js`, and the standalone browser assertion now expects 9.80.
- Added text/constant regressions to `original-engine/energy/checks.mjs` for the net-work distinction, the two power forms, and the shared 3D-lab gravity constant. The checks file now contains 70 explicit assertions; CI on the latest commit is pending.
- Added optional page-by-page screenshot capture to the shared physics book smoke runner (enabled only when `SCREENSHOT_DIR` is set) and desktop/mobile full-page screenshots to the Chapter 04 standalone smoke test.
- Added a dedicated workflow `.github/workflows/work-energy-browser.yml` to test all 12 interactive pages and the standalone lesson at desktop/mobile independently of unrelated chapter failures.

## Browser and visual evidence — 2026-11-06

- Dedicated Chapter 04 browser workflow [42160523319](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/42160523319) passed on commit `79535816681079d362a0ef6008b8f6bac071b1aa`: all 12 interactive pages on desktop/mobile; standalone lesson, calculator, canvas chart, quiz and 3D lab on desktop/mobile; screenshot upload succeeded.
- Screenshot artifact: `chapter4-work-energy-visual-review`, artifact ID `13476263737`. Manually inspected 24 interactive-book screenshots (12 desktop + 12 mobile) and the standalone desktop/mobile full-page captures.
- The first screenshot review identified: mobile scene-picker/title overlap, desktop hint/readout overlap, and an over-tall Lennard–Jones potential graph. Added chapter-specific `energy.css` plus desktop/mobile layout assertions in `book-smoke.mjs`. Reduced only the 3D scene's vertical graph scale; the potential function and numeric model are unchanged.
- Final graph display scale is `SC.bond.U = 0.4` m per eV, with the full potential range retained to 3.2 eV and the vertical axis extended to that same limit. The final browser rerun is pending on current source commit `5dc0152eea9bde93ccfc22c6cce64ef79bdd80a4`.
- JavaScript validation and all 72 Physics Engine checks passed on commit `79535816681079d362a0ef6008b8f6bac071b1aa`; the current 5dc source commit is being rechecked.
- The three standalone local visuals remain provisional Category C pending a project-owner creator/rightsholder and reuse-licence declaration. The 12 inherited interactive scenes are source-mapped to Nathan Liow and MIT attribution is recorded in `IMAGE_SOURCES.md`.
