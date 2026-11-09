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
| 70% — visual/scientific scene review | PASS | Source-level review completed for all 13 scenes: geometry, vectors, force directions, scale factors, orbit paths, labels and PLATES explanations checked against model.js and regression invariants |
| 80% — desktop/mobile visual QA | PASS | Responsive correction verified; all 13 mobile book-page screenshots and the standalone mobile model/quiz screenshot inspected. Header, title, selector, diagrams and labels remain readable; vertical-loop force labels no longer overlap. Dedicated desktop/mobile browser run passed |
| 90% — integration and regression | PASS | Dedicated Chromium workflow passed all 13 interactive pages on desktop/mobile and the standalone lesson, controls and quiz on desktop/mobile; no workflow test failures; screenshot artifact uploaded |
| 100% — final internal readiness | PASS | Chapter-specific browser workflow 42085258562 passed; JavaScript validation and Physics Engine checks passed on branch HEAD c6c075f. Chapter 3 source files are unchanged between the dedicated passing run's source baseline and HEAD; intervening commits changed workflow configuration and visual-provenance documentation only. Audit evidence saved on workspace/physics |

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
- The dedicated Chapter 3 browser workflow's latest successful run is 42085258562 at commit 592c5a58682db57c7eddf131fb18b9ddd9bac675. All 13 interactive book pages, standalone lesson controls and quiz passed on desktop/mobile, and the screenshot artifact upload succeeded. Comparison to current branch HEAD c6c075f4f6b6ffedf52933ac341cc33701b13b6c shows only workflow configuration and IMAGE_SOURCES.md changes after that source baseline; Chapter 3 implementation files are unchanged.

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

## Final closure

- The 26-item practice inventory and numeric/conceptual answer-key regression checks are complete.
- All 13 scene/page mappings and their PLATES explanations have been reviewed; the 13 inherited 3D scenes have individual provenance records in IMAGE_SOURCES.md.
- Responsive visual defects found during screenshot inspection were corrected, then rechecked in the dedicated Chapter 3 browser run.
- The dedicated browser run passed both interactive-book and standalone lesson checks on desktop and mobile and uploaded its screenshot artifact.
- JavaScript validation and Physics Engine checks passed on the current branch HEAD.
- The broader multi-chapter Physics browser workflow is a separate suite and was still running at the time of this audit update. Its Chapter 14 magnetism job failed on a dynamic-readout timing assertion; that unrelated failure is not evidence of a Chapter 3 defect. Chapter 3's dedicated workflow is green.
- No merge to main or deployment was performed.

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


## 70% — scene-by-scene scientific visual review

Source-level review covered all 13 scenes and their matching PLATES explanations:

1. Ball on a string: tangent velocity and inward acceleration; the Δv construction points inward.
2. Double-speed comparison: tension is proportional to v²; normal force and weight balance vertically.
3. Flat curve: static friction and resultant point inward; the no-friction tangent path is distinguished.
4. Conical pendulum: tension follows the string; vertical component balances weight and horizontal component supplies centripetal force.
5. Vertical loop: inward normal direction at top/bottom, weight direction, varying speed and normal-force readouts agree with the loop model.
6. Banked turn: normal force tilts upward/inward; its horizontal component is the centripetal resultant.
7. Rotating disc: both points share angular speed; tangent velocity scales with radius.
8. Gravitation: action-reaction forces are equal/opposite; acceleration magnitudes differ by mass.
9. Circular orbits: velocity tangent, acceleration inward; angular and linear speeds decrease with orbital radius.
10. Elliptical orbit: perigee/apogee labels, radius and velocity vectors, equal-time swept sectors and Kepler model agree.
11. Orbital energy: gravity is resolved parallel/perpendicular to velocity; K, U and total E are consistent with the model.
12. Potential-energy curve: U = −GMm/r, inward force direction and near-surface tangent approximation are consistent.
13. Escape trajectories: circular, bound elliptical, parabolic and hyperbolic cases are paired with the correct sign of total energy.

No scene geometry or force logic was changed. This is an internal source-level review supported by the model checks; it is not an external specialist certification.

## 80% — responsive defect found and correction

- Manual inspection of the desktop and mobile full-page screenshots revealed that the mobile book's mouse/keyboard hint overlapped the scene selector and title.
- Added original-engine/circular/circular.css: hide the desktop mouse hint on touch-sized screens, place the scene title and figure number separately, move the selector below the title, and constrain/wrap the live readout.
- Updated the canvas accessible name with touch guidance.
- The standalone lesson's mobile diagram had overly long vector labels that could run beyond the small canvas; shortened the visible arrow labels to v and aц, while retaining the direction explanation in the canvas accessible name.
- Extended the browser smoke to assert the mobile title/selector geometry and hidden mouse hint, and to capture separate book-chrome screenshots.
- Final responsive verification: the dedicated Chapter 3 run 42085258562 passed on desktop and mobile. The uploaded mobile screenshots for all 13 book pages and the standalone model/quiz were manually inspected; the overlap was no longer visible. This closes the 80% milestone.


## 100% — final internal readiness (2026-11-06)

- Chapter-specific browser run: [42085258562](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/42085258562) — SUCCESS. Interactive book (13 pages, desktop/mobile), standalone lesson/model/quiz (desktop/mobile), and screenshot artifact upload all passed.
- Current branch HEAD: `c6c075f4f6b6ffedf52933ac341cc33701b13b6c`.
- Current-HEAD checks: Validate JavaScript run `42153737685` — SUCCESS; Physics Engine run `42153737783` — SUCCESS.
- The full multi-chapter browser workflow `42153737716` was still in progress during closure. Its separate magnetism job failed only the Chapter 14 right-hand-rule dynamic desktop readout timing assertion; its Chapter 14 mobile readout and other Chapter 14 checks passed. This does not invalidate the dedicated Chapter 3 green run.
- Chapter 3 implementation files did not change after the successful dedicated run; intervening commits touched `.github/workflows/physics-browser.yml` and `IMAGE_SOURCES.md` only.
- Internal publication-readiness review is complete on `workspace/physics`. No external certification, merge, or deployment is implied.
