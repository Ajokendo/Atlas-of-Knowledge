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
| 30% — learner-facing text and formula audit | IN PROGRESS | Initial static review confirms the core work, work–energy theorem, kinetic/potential energy, conservation, power and efficiency explanations. A stray English sentence remains in the Russian standalone diagram caption and will be corrected; full paragraph-by-paragraph review remains |
| 40% — practice and answer-key audit | PENDING | Verify all 24 questions, units, distractors, explanations and the free-response solution independently |
| 50% — model assumptions and edge cases | PENDING | Review all 12 physical scenarios, phase boundaries, idealisations and limiting cases |
| 60% — visual source lineage and rights | PENDING | Complete upstream comparison and per-scene provenance/attribution checks for the 12 inherited scenes and standalone visuals |
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
