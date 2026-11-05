# Physics — Chapter 03 audit

- Chapter: **Движение по окружности / Circular motion**
- Working branch: `workspace/physics`
- Audit started: 2026-11-05
- Baseline commit: `76f1da42ecdccff5f4e2a6ecb32af32841a971e8`
- Scope: internal publication-readiness review of the Russian edition; the upstream English original by Nathan Liow is not to be edited.
- Merge/deployment: not performed.

## Progress

| Milestone | Status | Evidence |
|---|---|---|
| 10% — inventory and branch guard | PASS | 13 book pages, 13 3D scenes, 13 scene/plate keys, standalone HTML lesson and visual-source entries located on the correct branch |
| 20% — mathematical model and practice baseline | PASS | 63 existing physics/regression assertions; 24 practice items; current baseline Physics Engine workflow passed |
| 30% — scene mapping and browser baseline | PASS | 13 pages map to 13 scenes; existing browser workflow passed desktop 1440×900 and mobile 390×844, with WebGL and scene picker |
| 40% — upstream lineage and test coverage | IN PROGRESS | Upstream source compared; standalone lesson browser test added; new browser workflow run pending |
| 50% — content and answer-key audit | PENDING | Check every explanation, numerical answer, distractor, units and model assumptions |
| 60% — rights and visual provenance | PENDING | Complete per-scene records without treating MIT software licence as blanket rights to unrelated assets |
| 70% — visual/scientific scene review | PENDING | Inspect all 13 scenes, vector directions, labels, scales and accessible descriptions |
| 80% — desktop/mobile visual QA | PENDING | Dedicated screenshots, responsive review, axe smoke and correction of defects |
| 90% — integration and regression | PENDING | Local links, navigation, iframe, keyboard/touch controls and all chapter-specific checks |
| 100% — final internal readiness | PENDING | Final CI green on the final source commit; all audit evidence saved |

## Inventory

### Standalone lesson

- File: `chapters/circular-motion.html`
- Russian document language and title are present.
- 11 main lesson sections; 3 main numbered subject sections plus additional explanatory subsections.
- Topics include linear/angular speed, radians, period/frequency, centripetal acceleration, non-uniform circular motion, centripetal resultant force, flat and banked turns, vertical loops, and circular orbits.
- Includes an interactive three-control model (speed, radius, mass), calculated acceleration/force/period, a canvas vector diagram, and a three-option check question.
- The quiz key is `b`; the stated result is (a_c=8^2/4=16\,\mathrm{m/s^2}).

### Interactive book

- Files: `original-engine/circular/{index.html,main.js,pages.js,world.js,model.js,practice.js,checks.mjs}`
- 13 pages, 13 scene keys, 13 corresponding PLATES entries.
- 24 practice questions (one or two per page).
- 63 explicit regression assertions in `checks.mjs`.
- The chapter covers circular motion, force roles, flat and banked curves, conical pendulum, vertical loop, angular velocity, Newtonian gravitation, circular and elliptical orbits, orbital energy, gravitational potential, and escape speed.

## Source lineage snapshot

Compared the local files with Nathan Liow's upstream `circular/` module in `nathanliow/atlas-of-physics` on 2026-11-05:

- `model.js`: 193 lines in both files; the four differing executable lines are Russian names for the circular, elliptical, parabolic and hyperbolic launch cases. The mathematical implementation is otherwise line-identical.
- `world.js`: 480 lines in both files. Differences include Russian scene/object/vector labels and Russian unit notation. Scene geometry and numerical construction require the remaining visual-level review before final sign-off.
- `pages.js`: 285 lines in both files. Differences include Russian translation of page copy, chart labels, captions, and embedded SVG/HTML labels. Treat translated visual text as localisation/adaptation, not as independent authorship of the inherited scene.
- `practice.js`: 142 lines in both files. Differences include Russian translation and localisation of units and question/explanation text.
- Upstream source: https://github.com/nathanliow/atlas-of-physics/tree/main/circular
- Upstream licence: MIT; retain Nathan Liow's copyright and licence notice. The code licence is not blanket evidence for any separately embedded third-party asset.

## Work added during this audit

- Added `original-engine/circular/standalone-smoke.mjs` to test the separate HTML lesson at desktop and mobile sizes.
- The test checks initial outputs (5.00 m/s², 10.00 N, 12.57 s), recalculation after changing speed/radius/mass (10.00 m/s², 40.00 N, 12.57 s), wrong and correct quiz responses, horizontal overflow, browser errors, and serious/critical axe findings.
- The test captures desktop and mobile full-page screenshots under `/tmp/physics-visual-review/circular/`.
- Added the standalone test and screenshot artifact upload to `.github/workflows/physics-browser.yml`.
- Code and workflow commits: `32fb32229a97aecc0ea39c1e45ec0359f4fbec1b`, `8fe579525444ee97dc0c7f639e1c0d5068013934`.
- The browser workflow triggered by the latest change is pending at the time of this record. Do not treat it as passed until the run and its chapter-specific step conclude successfully.

## Initial scientific review notes

- Uniform circular motion: model uses (a_c=v^2/r), (T=2\pi r/v), tangent velocity and inward acceleration.
- Flat turn: static friction supplies the required inward resultant; (v_{max}=\sqrt{\mu_sgr}).
- Conical pendulum: angle is measured from vertical; (T\cos\theta=mg), (T\sin\theta=mv^2/r).
- Vertical loop: top contact threshold (v_{top}^2/r\geq g) is correctly distinguished from a universal constant-speed loop; the model includes gravitational energy exchange and varying speed.
- Frictionless banked turn: (\tan\theta=v^2/(rg)), with angle measured from the horizontal road.
- Circular orbit: radius is measured from Earth's centre; gravity supplies the centripetal resultant.
- Elliptical orbit: the model uses RK4 integration and checks energy/angular-momentum conservation, vis-viva, Kepler's laws and equal areas.
- Gravitational potential uses zero at infinity, (U=-GMm/r); escape condition uses total mechanical energy.
- These are initial formula/model checks, not yet the completed learner-facing explanation and diagram review.

## Outstanding items

1. Finish all 24 practice-question checks and verify every distractor's units and answer explanation.
2. Review the wording and model assumptions for all 13 pages, including the distinction between idealised and real motion.
3. Complete item-level provenance/attribution and scientific visual checks for the 13 inherited 3D scenes.
4. Inspect standalone lesson and interactive-book screenshots on desktop and mobile.
5. Confirm the new dedicated browser workflow, then fix any issues it reports.
6. Save the final 100% audit only after all required checks pass.

## Publication boundary

“100%” in this audit will mean internally checked and ready for publication in the working branch. It will not mean independent external certification, specialist teacher approval, merge to `main`, or deployment. External teacher review is a separate later activity.
