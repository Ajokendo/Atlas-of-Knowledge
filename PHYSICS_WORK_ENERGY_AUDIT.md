# Physics — Chapter 04 audit

- Chapter: **Работа, энергия и мощность / Work, Energy and Power**
- Working branch: `workspace/physics`
- Audit started: 2026-11-06
- Baseline commit: `94317525bb6ca4af9add070d94320fa8a9893af8`
- Scope: internal publication-readiness review of the Russian edition; Nathan Liow's English source is not to be edited.
- Merge/deployment: not performed.

## Progress

| Milestone | Status | Evidence |
|---|---|---|
| 10% — inventory and branch guard | PASS | Standalone Russian lesson, 12-page interactive book, 12 scene keys, 12 practice-page groups, model, world, main and regression files located in the assigned Physics workspace |
| 20% — model and numerical regression baseline | PASS | Current-HEAD JavaScript validation (run 42154158118) and Physics Engine checks (run 42154158123) passed on commit 9bc9bb1; energy/checks.mjs contains 67 explicit checks, including independent numerical answer recomputation |
| 30% — learner-facing text and formula audit | PASS | Reviewed all 12 interactive-book page explanations and all 9 standalone lesson sections. Removed an untranslated English sentence from the standalone SVG caption. Clarified that kinetic-energy change depends on net work, and distinguished average from instantaneous power with the general directional factor cos α |
| 40% — practice and answer-key audit | IN PROGRESS | Confirmed 24 questions across 12 pages: 22 multiple-choice and 2 free-response. Existing regression checks independently recompute numeric answers and validate distractor separation; new text/constant regression checks are awaiting the current CI run |
| 50% — model assumptions and edge cases | IN PROGRESS | Reviewed the 12 scenario families and the documented assumptions: frictionless pull/spring, gravity-only toss/drop/pendulum, centripetal tension, net work, variable force, potential curves, Lennard–Jones bond, kinetic friction and steady-speed lift. Unified the 3D lab gravity constant from 9.81 to 9.80 m/s²; the new regression and browser reruns are pending |
| 60% — visual source lineage and rights | IN PROGRESS | Compared all 5 local energy modules with Nathan Liow’s pinned upstream snapshot. Mapped all 12 page descriptors to their inherited scene assemblies and documented MIT attribution plus the bond-potential graph-range adaptation in IMAGE_SOURCES.md. Three standalone-page visuals still need final creator/rights classification and per-visual evidence |
| 70% — scientific visual review | PENDING | Review every scene, vector direction, graph, scale, label and PLATES explanation against model.js and checks.mjs |
| 80% — desktop/mobile visual QA | PENDING | Run browser tests and inspect all chapter screenshots at desktop and mobile sizes |
| 90% — integration and regression | PENDING | Verify navigation, resources, touch/keyboard operation, reduced-motion behavior, canvas/WebGL, accessibility and absence of overflow |
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
