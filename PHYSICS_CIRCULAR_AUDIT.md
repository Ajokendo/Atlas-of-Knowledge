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
| 20% — mathematical model and practice baseline | PASS | 65 physics/regression assertions (63 baseline + 2 new practice regressions); 26 practice items (24 multiple-choice and 2 free-response); current baseline Physics Engine workflow passed |
| 30% — scene mapping and browser baseline | PASS | 13 pages map to 13 scenes; existing browser workflow passed desktop 1440×900 and mobile 390×844, with WebGL and scene picker |
| 40% — upstream lineage and test coverage | PASS | Upstream source compared; dedicated browser workflow passed all 13 pages and standalone lesson at desktop/mobile; screenshots uploaded |
| 50% — content and answer-key audit | PASS | All 26 items inventoried (24 MCQ + 2 FRQ); 65 physics/practice assertions; conceptual answer-key regression added; Physics Engine passed on commit 4a78df44 |
| 60% — rights and visual provenance | PASS | 13 individual scene records added to IMAGE_SOURCES.md; upstream Nathan Liow source, MIT code licence, Russian localisation and procedural-geometry boundary recorded; no external image files found in world.js |
| 70% — visual/scientific scene review | IN PROGRESS | Scene/source mapping complete; manual visual inspection of every scene, vector direction, scale and caption remains |
| 80% — desktop/mobile visual QA | IN PROGRESS | Dedicated desktop/mobile browser smoke and screenshots passed on run 42078922929; axe serious/critical findings = 0; screenshot-by-screenshot manual review and final rerun remain |
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
- 26 practice items: 24 multiple-choice questions and 2 free-response questions (one or two per page).
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
- The dedicated Chapter 3 browser workflow passed on commit 9806e3e365df57fb39a7ed5e999dfb87921b8519 (run 42078922929): 13 interactive book pages at desktop/mobile, standalone lesson controls and quiz at desktop/mobile, and screenshot upload all succeeded. The practice-count assertion was subsequently corrected from 24 to 26; the Physics Engine check passed on commit 4a78df44b5908a5d4ef133d9dbc8d5a81fbcf987. Later commits in this audit updated documentation/visual provenance only. A final rerun on the final chapter commit is still required.

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

1. Finish all 26 practice-item checks and verify every distractor's units and answer explanation.
2. Review the wording and model assumptions for all 13 pages, including the distinction between idealised and real motion.
3. Complete item-level provenance/attribution and scientific visual checks for the 13 inherited 3D scenes.
4. Inspect standalone lesson and interactive-book screenshots on desktop and mobile.
5. Confirm the new dedicated browser workflow, then fix any issues it reports.
6. Save the final 100% audit only after all required checks pass.

## Publication boundary

“100%” in this audit will mean internally checked and ready for publication in the working branch. It will not mean independent external certification, specialist teacher approval, merge to `main`, or deployment. External teacher review is a separate later activity.


## 50% — practice and answer-key audit

- Counted the full practice set: 24 multiple-choice items and 2 free-response items, 26 total across 13 pages.
- Numeric answer checks independently recompute values for circular acceleration, string tension, friction-limited speed, conical-pendulum speed/tension, vertical-loop normal force and minimum speed, banked-curve speed, turntable speed, gravity and orbital values, ellipse speeds/energies, gravitational work and potential-energy change, and escape speed.
- Added regression assertions for the exact 26-item inventory and the Russian meaning of key conceptual answers: inward acceleration, tangent motion after string break, mass independence on a flat turn, motion up a bank above design speed, acceleration scaling with radius, inverse-square gravity, angular momentum conservation, and energy exchange on an ellipse.
- One first run failed because the new inventory assertion incorrectly expected 24 total items. Inspection showed 24 MCQs plus two free-response solutions. The assertion and audit inventory were corrected; the Physics Engine workflow then passed.

## 60% — rights and visual provenance

- Added per-scene records for all 13 inherited Chapter 03 3D scenes (PHY-03-3D-01 through PHY-03-3D-13) in IMAGE_SOURCES.md.
- Compared local and upstream model.js, world.js, pages.js, and practice.js; the model/world/practice executable structures match after excluding comments and string literals. The page module has localised content and adapted embedded chart/HTML text.
- world.js builds scenes from procedural Three.js geometry/materials. No external raster/texture image assets were found in this module.
- The upstream MIT software licence and Nathan Liow attribution are recorded. No claim is made that MIT covers unrelated third-party material.
- Browser smoke status is not substituted for the still-pending manual scientific visual review.

## Browser evidence

- Dedicated workflow run: https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/42078922929
- Screenshot artifact ID: 13439188475 (chapter3-circular-visual-review); desktop and mobile full-page screenshots were generated and uploaded.
- The dedicated run reported success for all 13 interactive pages and for the standalone lesson's control recalculation, wrong/correct quiz response, horizontal overflow, browser errors and serious/critical axe checks.
