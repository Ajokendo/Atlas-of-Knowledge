# Physics — IMAGE_AUDIT

- Subject: Physics
- Working branch: `workspace/physics`
- Audit date: 2026-11-05
- Target policy: `IMAGE-FIRST POLICY v1.1` (AOK-IMG-001)
- Canonical policy: [`main:IMAGE_FIRST_POLICY.md`](https://github.com/Ajokendo/Atlas-of-Knowledge/blob/main/IMAGE_FIRST_POLICY.md)
- Historical note: when this audit was first drafted on 2026-11-05, v1.1 was available only in `atlas-of-knowledge-integration`; it has since been installed and verified in `main` (commit `bd3deb97`). The old Physics-local `IMAGE_POLICY.md` is now a pointer to the canonical document, not a competing copy.
- Scope: all 15 standalone chapter pages under `chapters/`, the 15 corresponding interactive-book page modules under `original-engine/*/pages.js`, and the existing `IMAGE_SOURCES.md` register.
- Audit type: preliminary structural and inventory audit. This document does not claim that every visual has passed expert scientific, rights, bilingual, accessibility, or manual visual review.

## 1. Derivative-atlas protocol and provenance boundary

The Physics atlas in this branch is a derivative/localised edition based on the pre-existing English *Atlas of Physics* by Nathan Liow. It is not being treated as an independently authored replacement atlas. The English source must remain unchanged.

This audit therefore separates four things:
1. **Inherited source visuals** — figures, diagrams, animations, interactive scenes, and other visuals carried over from the English source.
2. **Russian-edition localisation** — translated page text, captions, labels, controls, alt text, descriptions, layout and rendering checks.
3. **Actual visual adaptations** — edits to the visual content itself, such as translated text embedded in an image, changed labels/legends, crops, recolouring, annotations, redrawing or altered data.
4. **New project-specific visuals** — assets independently created for this derivative edition and not simply inherited unchanged.

The original creator/rightsholder for inherited material is Nathan Liow where that attribution is supported by the source-work context. The precise licence/permission applying to each visual and the derivative Russian edition has **not been established by this structural audit** and must remain **Unknown / PENDING** until item-specific evidence is checked. Do not infer permission from repository access or the existence of the translation.

### 1.1 Classification rules for this branch

- An inherited visual used without changing its visual content is **A — Original reuse**. Record its source lineage and original attribution; do not describe it as created by this project.
- Translating surrounding chapter prose, captions, page controls, or alt text while leaving the visual itself unchanged is a localisation check; it does **not by itself** make the visual Category B.
- Translating or replacing text inside the visual, changing labels/legends, adding callouts, cropping, recolouring, combining, simplifying, redrawing, or changing the visual's data or meaning is **B — Adapted**. Verify that the source licence/permission allows that adaptation before publication.
- A genuinely new independent visual is **C — Created**. Record the actual method and creator/rightsholder; do not assign C merely because a visual is rendered by SVG, canvas, JavaScript, or WebGL.
- If lineage or the nature of a change is unclear, mark **PENDING**. Do not guess.

No blanket re-search is required for every unchanged inherited visual if its source identity is traceable and it remains suitable. Search for a replacement only where an inherited visual is missing, unsuitable, inaccurate, inaccessible, rights-restricted, or genuinely needs replacement.

### 1.2 Verified source-work identity and licence evidence

The upstream source repository has now been identified and inspected:

- Original work: Nathan Liow, **Atlas of Physics** — https://github.com/nathanliow/atlas-of-physics
- Upstream README: https://github.com/nathanliow/atlas-of-physics/blob/main/README.md
- Upstream licence: https://github.com/nathanliow/atlas-of-physics/blob/main/LICENSE
- Reference snapshot used for the 15-module source comparisons: [upstream commit `bcd67d9b75425f4a78f5c7c1d17a2d0614727309`](https://github.com/nathanliow/atlas-of-physics/commit/bcd67d9b75425f4a78f5c7c1d17a2d0614727309), dated 2026-10-30. This pins the comparison reference; it does not by itself prove the exact commit from which every local file was originally imported.
- The upstream repository declares the **MIT License**, with copyright notice **Copyright (c) 2026 Nathan Liow**. The licence grants rights to use, copy, modify, merge, publish, distribute, sublicense, and sell the software, subject to retaining the copyright and permission notice.
- The Physics branch's `original-engine/README.md` explicitly identifies the upstream project and states that original interactive laboratories are integrated, while learning text, interface, labels, and explanations are adapted into Russian.

This establishes a documented MIT licence basis for the upstream repository code and permitted modifications, subject to retaining the required notice. It does **not** automatically clear any separately embedded third-party content if such content is present; those components still require their own rights checks. The root-level Russian chapter pages are separate implementations and must be mapped to their source material before their assets are assigned A/B/C.

### 1.3 Interactive-book page-module source comparison — all 15 chapters

On 2026-11-05, the local `pages.js` module for every interactive-book chapter was fetched and compared with the corresponding upstream file in Nathan Liow's repository. All 15 pairs were found; none was byte-identical because the local modules contain Russian-language localisation.

| Original chapter | Module | Comparison result |
|---:|---|---|
| 01 — Kinematics | `kinematics/pages.js` | Russian learner-facing text and visual labels |
| 02 — Newton's Laws | `newton/pages.js` | Russian learner-facing text and visual labels |
| 03 — Circular Motion | `circular/pages.js` | Russian learner-facing text and visual labels |
| 04 — Work and Energy | `energy/pages.js` | Russian text/labels; `bondU` chart domain also changed |
| 05 — Momentum | `momentum/pages.js` | Russian learner-facing text and visual labels |
| 06 — Oscillations | `oscillations/pages.js` | Russian learner-facing text and visual labels |
| 07 — Rotation | `rotation/pages.js` | Russian learner-facing text and visual labels |
| 08 — Fluids | `fluids/pages.js` | Russian learner-facing text and visual labels |
| 09 — Electrostatics | `electrostatics/pages.js` | Russian learner-facing text and visual labels |
| 10 — Gauss's Law | `gauss/pages.js` | Russian learner-facing text and visual labels |
| 11 — Electric Potential | `potential/pages.js` | Russian learner-facing text and visual labels |
| 12 — Capacitors | `capacitors/pages.js` | Russian learner-facing text and visual labels |
| 13 — Electric Circuits | `circuits/pages.js` | Russian learner-facing text and visual labels |
| 14 — Magnetism | `magnetism/pages.js` | Russian learner-facing text and visual labels |
| 15 — Electromagnetic Induction | `induction/pages.js` | Russian learner-facing text and visual labels |

The modules retain the upstream page structure and chart/SVG generation patterns in the compared sections. Where Russian text is embedded in an SVG, chart, figure, or accessible visual label, that affected output is **B — Adapted**; translation of surrounding prose alone is localisation and is not enough to reclassify an unchanged visual. This comparison establishes source lineage for the 15 page modules, not a complete inventory or approval of every individual scene, chart, or visual state.

The following non-translation differences were identified and require separate treatment:

- In `energy/pages.js`, the `bondU` chart domain changes from upstream `x0: 0.13, y1: 0.4` to `x0: 0.125, y1: 3.2`. Evaluating the unchanged Lennard–Jones potential in `energy/model.js`, (U(r)=\varepsilon[(r_0/r)^{12}-2(r_0/r)^6]), at (r=0.125\,\mathrm{nm}) gives approximately (2.94\,\mathrm{eV}). The previous 0.4 eV upper limit would clip the repulsive branch; the 3.2 eV limit includes it. This is a justified display-range correction, not a change to the physical model. Keep the graph's interpretation and axis labels in the scientific review.
- In `magnetism/pages.js` / `magnetism/model.js`, `sinDeg` and `cosDeg` helpers remove floating-point residue at exact parallel/perpendicular orientations. This is a computational correction, not a new visual. The local `magnetism/checks.mjs` adds endpoint and Lorentz-force checks; retain this as a documented branch-specific fix.
- A separate comparison of all 15 `world.js` scene modules is now complete at the source-code level. Fourteen are code-equivalent to upstream after normalising string literals and comments; their changed learner-facing object names, scene titles, and accessible labels are Russian localisation. The Kinematics scene has one additional rendering optimisation documented in section 1.4. This comparison does not replace visual inspection of each scene state.

These findings support Category B for the affected Russian-labelled SVG/chart outputs. They do not establish final per-visual counts, item-level rights clearance, or full chapter visual verification.

### 1.4 Scene and model source comparison — all 15 chapters

The source comparison was extended to all 15 `world.js` scene modules and all 15 `model.js` modules.

**Scene modules (`world.js`):**
- All 15 local modules were compared with the corresponding upstream module.
- For 14 modules, the executable code is identical after normalising quoted strings and comments; differences are Russian object names, scene titles, labels, and accessible descriptions. Those translated in-scene labels make the affected scene outputs **B — Adapted** under the policy.
- `kinematics/world.js` also changes how the graph-area mesh is updated: the local version preallocates a dynamic `Float32BufferAttribute` and updates its existing position array, while upstream rebuilds the position array and attribute each frame. Both paths write the same 18 vertex coordinates for each of 60 segments and the same draw range. This is a rendering/performance implementation change, not a new scientific visual or a change to the represented graph. It should still receive browser rendering QA.

**Model modules (`model.js`):**
- Eleven local modules are code-equivalent to upstream after normalising strings and comments.
- Four modules contain identifiable code changes:
  - `electrostatics/model.js`: adds `electronTrajectory()`, used by the Russian chart and regression check. It samples the same electron-motion model used by the upstream inline curve; this is a refactoring of chart data generation, not a new physical model.
  - `potential/model.js`: changes the charged-disc axial potential to use `Math.abs(z)`, making the potential symmetric on both sides of the disc. The local checks compare the closed form with a ring-sum calculation on both sides and check symmetry.
  - `capacitors/model.js`: corrects the charged-disc axial field to include `Math.sign(z)` and `Math.abs(z)`, returning the symmetric principal-value average zero at the plane; it also adds a numerical `lineIntegral()` helper used by the checks and practice calculations. Checks cover both sides of the disc, the wide-disc sheet limit, and voltage integrals.
  - `magnetism/model.js`: adds `sinDeg()`/`cosDeg()` helpers to suppress floating-point residue at exact parallel/perpendicular orientations. Local checks cover exact endpoints, Lorentz-force magnitude and direction, and the force's perpendicularity to velocity and field.
- These are branch-specific calculation/refactoring changes, not evidence of independently authored 3D visuals. The local `checks.mjs` files contain targeted regression assertions, but this audit does not claim they have been executed in this session.

These comparisons substantially improve source lineage coverage for the interactive engine. They do not establish final visual counts, rights clearance, complete scene-state QA, or scientific approval of every rendered visual.

### 1.5 Localisation review required

The Russian edition must be checked for accurate terminology, labels, symbols, legends, units, formulas, vector directions, numerical values, layout after text expansion, readable mobile presentation, captions, alt text, long descriptions, and equivalent data/text for complex visuals. The English source is not to be edited as part of this work.

## 2. Repository inventory findings

| Check | Observed result | Interpretation |
|---|---:|---|
| Standalone Physics chapter pages | 15 | All chapters 01–15 in the current chapter set were included |
| HTML `<img>` elements in those pages | 0 | No ordinary raster/photo assets are embedded in the 15 standalone chapter pages |
| Inline SVG in standalone chapter pages | 2 | Present in Kinematics and Work & Energy; require complete source/creator/rights/accessibility records |
| Canvas elements in standalone chapter pages | 43 after this audit's cleanup | Initially 45; the generic non-informative canvas in Magnetism and the equivalent canvas in Induction were removed and replaced with accurate explanatory text. Remaining canvases are rendering surfaces, not automatically distinct assets. |
| Explicit visual placeholder groups | 0 remaining | The four previously specified gaps are now filled by four original bilingual SVG visual assets with eight responsive desktop/mobile SVG files (one visual in Chapter 14, three in Chapter 15) |
| Detailed asset records in `IMAGE_SOURCES.md` | 7 | Three legacy Chapter 04 discovery records plus four new Category C records for Chapters 14–15; 71 page-level scene-index entries and 98 assembly candidates are indexed separately, but are not complete verified records for all inherited visuals |
| External visual assets documented as integrated | 0 | No external image is claimed as integrated in the current register |
| Interactive-book modules | 15 | All 15 page/world/model modules have source-lineage comparisons; 71 page-level scene descriptors are indexed across Chapters 03, 05, and 11–15; they still need mapping to actual assembly-level visuals. Page-level scene descriptors in Chapters 01, 02, 04, and 06–10 also remain to be indexed. |

The absence of `<img>` elements is not a finding that the atlas lacks visual learning material. The Physics branch relies heavily on inline SVG, canvas, charts, and WebGL/Three.js scenes. Rendering technology alone does not establish authorship or category: each visual must first be traced to the English source or to a documented branch-specific addition. Unchanged inherited scenes are normally A; actual visual modifications are B; only genuinely new independent assets are C.

An additional source-code inventory on 2026-11-05 identified 98 named `PLATES`/`world.js` assembly candidates across Chapters 01, 02, 04, and 06–10 (15 Kinematics, 13 Newton, 12 Energy, 17 Oscillations, 15 Rotation, 9 Fluids, 10 Electrostatics, and 7 Gauss assembly keys). These are candidate groups, not 98 verified or necessarily distinct visual assets. Kinematics has five additional PLATES breakdown keys without a top-level assembly match; Gauss has five model variants that require mapping to their underlying scene groups. Details are in `IMAGE_SOURCES.md`.

## 3. Chapter-by-chapter preliminary visual audit

Status meanings: **PENDING** = the visual requirement or asset still needs a complete evidence-based review; **INVENTORY** = code/markup presence observed, not approval. No chapter is declared visually VERIFIED by this preliminary audit.

| Chapter | Visual learning needs to verify | Observed implementation | Required action |
|---|---|---|---|
| 01 — Kinematics | Position/displacement vectors; velocity and acceleration; motion graphs; projectile path; relative motion/reference frames | Inline SVG and 3 canvas elements in standalone page; interactive-book figures include position, velocity, acceleration, stroboscopic sequence, graphs, projectile and river-crossing examples | Assign stable IDs to each distinct visual; verify vector directions, graph axes/units, projectile assumptions and bilingual descriptions; add a text/data alternative for graphs |
| 02 — Newton's Laws | Free-body diagrams; action–reaction pairs on different bodies; friction/tension/normal-force cases; acceleration comparisons | 3 canvas elements; interactive figures cover all three laws, tension, friction, system selection and centre-of-mass acceleration | Audit each force diagram for body isolation, equal/opposite pair placement, vector direction and labels; ensure meaning is not colour-only |
| 03 — Circular Motion | Tangential velocity and centripetal acceleration; force direction; turning, conical pendulum, vertical circle, banked turn and orbits | 1 canvas element; interactive-book figures cover these cases | Add separate records for distinct diagrams/scenes; verify instantaneous vector directions, radial direction, orbit scale/assumptions and non-uniform cases |
| 04 — Work and Energy | Force/displacement angle; positive/negative/zero work; energy transformations; potential-energy profile | Inline SVG, 3 canvas elements; 3 assets already documented in register (force diagram, energy plot, 3D incline scene) | Retain existing records but migrate them to v1.1 fields; explicitly identify creator/rightsholder evidence, method, limitations, reviewer/date, bilingual captions/alt and technical evidence; confirm whether the three records cover every required visual |
| 05 — Momentum | Before/after collision states; momentum vectors; impulse over time; elastic/inelastic distinctions; centre of mass | 3 canvas elements; interactive figures cover impulse, collisions, explosion, ballistic pendulum and centre of mass | Record visual IDs; check vector conservation, system boundaries, mass/velocity labels and energy distinction; add accessible textual summary |
| 06 — Oscillations | Spring and pendulum geometry; x/v/a phase; energy exchange; damping and driven resonance | 3 canvas elements; interactive figures cover spring, pendulum, phase variables and energy | 98 assembly candidates now indexed in IMAGE_SOURCES.md; map page descriptors to groups, then check phase relationships, equilibrium positions, small-angle assumptions and damping/drive distinctions; provide accessible graph summaries |
| 07 — Rotation | Angular variables; torque arms; equilibrium; moment of inertia; parallel-axis theorem; rolling; angular momentum | 3 canvas elements; interactive figures cover torque, equilibrium, ladder, inertia, Steiner theorem, work/power and rolling | Add records; verify lever arms, torque signs, axes, mass distributions, rolling conditions and vector direction; include bilingual descriptions and mobile checks |
| 08 — Fluids | Density/volume comparison; pressure and depth; Pascal press; buoyancy/free-body balance; continuity; Bernoulli; Torricelli | 3 canvas elements; interactive figures cover pressure, depth, hydraulic force, buoyancy, flow area/speed and outflow. Shared scene-picker focus handoff fixed; isolated desktop/mobile lesson and book tests pass 4/4, axe serious/critical 0 (run 41983167799). | Continue asset-level mapping and scientific/source review; keyboard focus defect is resolved by CI evidence |
| 09 — Electrostatics | Charge signs; Coulomb-force vectors; superposition; field lines; dipoles; extended charge distributions; uniform fields | 3 canvas elements; interactive figures include charge configurations, field, dipole, rod, ring and parallel plates | Add records; check field-line direction and density conventions, vector superposition, signs, geometry and whether diagrams are conceptual or quantitative |
| 10 — Gauss's Law | Electric flux and surface orientation; Gaussian surfaces; symmetry cases (line, sheet, sphere); conductor vs insulator | 3 canvas elements; interactive figures include rotating surface, Gaussian surfaces, line, sheet, sphere and conductor cases. Shared scene-picker focus handoff fixed; isolated desktop/mobile lesson and book tests pass 4/4, axe serious/critical 0 (run 41983167799). | Continue asset-level mapping and scientific/source review; keyboard focus defect is resolved by CI evidence |
| 11 — Electric Potential | Potential energy vs potential; equipotentials; potential landscapes; dipole and extended-charge examples | 3 canvas elements; interactive figures include potential landscape, dipole, rod/ring/disk and spheres | Add records; distinguish scalar potential from vector field, label units and zero reference, explain potential-landscape analogy and add text alternative |
| 12 — Capacitors | Plate geometry and field; charge/voltage relation; dielectric insertion; connected/disconnected battery cases; series/parallel combinations; energy | 3 canvas elements; interactive figures include parallel plates, dielectric, battery state and combinations | Add records; verify what is held constant in each scenario, field direction, polarity, dimensions and formula assumptions |
| 13 — Electric Circuits | Circuit symbols; current direction vs electron drift; potential rise/drop; series/parallel networks; Kirchhoff loops; RC transients | 3 canvas elements; interactive figures include resistor networks, battery, power, Kirchhoff and RC examples. On 2026-11-05 the standalone Ohm's-law canvas was changed from a generic circle/line graphic to a labelled closed-circuit schematic with source polarity, resistor value and conventional-current arrow; the battery source now visibly interrupts the left-hand wire so its plates are not drawn over a continuous conductor. Canvas alt text was made specific. A dedicated Playwright desktop/mobile smoke test checks that the schematic is painted, the Ohm-law/power outputs recalculate, quiz feedback works, WebGL and keyboard rotation load, mobile layout has no horizontal overflow, and serious/critical axe findings are absent. Its first accessibility run identified a 4.35:1 contrast ratio on the three 9px metric labels (`.stats small`); the Russian page now uses a darker `#55534f` label color against `#e9e9e4`. The corrected standalone rerun passed on desktop (1440×900) and mobile (390×844): schematic painted, Ohm recalculation and power outputs, quiz feedback, WebGL, keyboard interaction, zero horizontal overflow, and zero serious/critical axe findings. The test is included in `physics-browser.yml`. The follow-up isolated interactive-book test also passed on desktop and mobile: all 9/9 pages, WebGL (816×800 desktop; 561×489 mobile), scene picker, zero horizontal overflow, and zero serious/critical axe findings. The combined isolated job completed successfully in [GitHub Actions run 41968791691](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/41968791691), job `circuits-isolated`, on commit `ca668d5172140e7bc8d55227f2ef66d4c6796a8a`. | Continue asset-level mapping and scientific/source review; the standalone schematic and full 9-page interactive-book browser checks now pass on desktop and mobile. |
| 14 — Magnetism | Magnetic-field lines; Lorentz force and trajectories; velocity selector; current-loop moment; Ampère/Biot–Savart; parallel wires; solenoid and toroid | 2 canvas elements remain in standalone page; generic placeholder canvas removed and replaced by explanatory text; one original bilingual four-topic visual is integrated at PHY-14-001 with desktop and stacked mobile SVG variants; 9 page-level scene descriptors are indexed and still need assembly-level mapping | Responsive SVG browser QA on prior revision PASS; rerun after latest footnote clarification is part of publication QA. Internal second-pass physics review PASS; CC BY-NC 4.0 publication licence declared. External subject-matter sign-off is a separate post-publication activity and is not a publication gate; map inherited/adapted scenes and verify toroid leakage and ideal-model qualifications |
| 15 — Electromagnetic Induction | Flux change; Lenz's law; mutual induction; motional EMF; moving rod; self-induction; RL and LC behaviour | 2 canvas elements remain in standalone page; generic placeholder canvas removed and replaced by explanatory text; three original bilingual visuals are integrated at PHY-15-001–003 with desktop and stacked mobile SVG variants; 10 page-level scene descriptors are indexed and still need assembly-level mapping | Responsive SVG browser QA on prior revision PASS; rerun after latest Chapter 14 footnote clarification is part of publication QA. Internal second-pass physics review PASS; CC BY-NC 4.0 publication licence declared. External subject-matter sign-off is a separate post-publication activity and is not a publication gate; verify sign conventions, flux orientation, mutually perpendicular geometry, energy/current curves and RL/LC assumptions |

Numbering note: chapter numbers follow Nathan Liow's original 15-chapter sequence and the chapter metadata in the Russian HTML files. The filenames in `chapters/` are thematic and must not be interpreted as sequential chapter numbers. The four former standalone placeholders were Chapter 14 (Magnetism: one four-topic infographic) and Chapter 15 (Electromagnetic Induction: three visual briefs); all four are now integrated as SVG assets, with review status recorded below.
## 4. Physics derivative-edition corrections required by IMAGE-FIRST v1.1

### 4.1 Required governance and record files
- Maintain this `IMAGE_AUDIT.md` as the Physics derivative-edition audit, explicitly preserving source lineage.
- Expand `IMAGE_SOURCES.md` to identify inherited visuals and branch-specific additions, but do not assume every canvas or figure label is a distinct asset. Use stable IDs only after the underlying visual and its source relationship are identified.
- The universal standard v1.1 is canonical in `main`. This branch links to it; do not maintain a competing local copy.
- Keep Physics-specific review criteria (vector directions, coordinate frames, sign conventions, idealisations, units, scale and measurement-vs-model distinctions) as a supplement, without redefining universal statuses or metrics.

### 4.2 Asset identity and classification
- Identify each distinct learning visual and map it to the corresponding English-source figure/scene where possible.
- Record whether the Russian branch uses it unchanged, localises only surrounding text/accessibility content, or modifies the visual itself.
- Classify unchanged inherited visuals as A; actual visual adaptations as B; genuinely new independent visuals as C. For C, record the actual authoring method and creator/rightsholder. Do not infer authorship from SVG/canvas/WebGL implementation alone.
- Do not treat a canvas element as a unique asset until its rendered visual and learning purpose have been identified. Do not count a multi-state interactive scene multiple times unless the states are separate learning assets.
- The 15 interactive-book page modules contain numerous figure labels and examples. Treat those labels as discovery clues, not as a verified count of unique visuals.

### 4.3 Rights, creator and provenance
- For inherited visuals, preserve the source-work attribution to Nathan Liow where supported; verify the exact licence/permission for reproduction in this derivative edition and do not assume it is cleared.
- Identify separate third-party components embedded in the source work where present; their rights may differ from the atlas-level rights.
- For actual branch-specific additions, identify the creator/rightsholder from evidence or mark **Unknown**. A repository-level licence is not a substitute for asset-level provenance or third-party rights checks.
- For any replacement candidate, document search date, terms/collections, exact item page, creator, item-specific licence, licence evidence, permitted modifications and attribution.
- If AI-generated additions are ever made, label them as illustrations/reconstructions, not real experiments or measured evidence.

### 4.4 Russian-edition localisation, accessibility and technical review
- Check Russian captions and meaningful Russian alt text for every non-decorative visual; preserve the English source text and English assets unchanged. If the Russian edition has a separate interface/caption layer, localise that layer without changing the inherited visual file unless adaptation rights are established.
- Add a nearby explanation or data/table equivalent for complex diagrams and charts.
- Check that colour is not the only carrier of meaning; use arrows, labels, patterns, line styles and symbols.
- For interactive diagrams: test keyboard operation, focus, accessible names/descriptions and screen-reader output where applicable.
- For charts: check axis titles, units, ranges, assumptions, data/equation provenance and text alternatives.
- For SVG: validate title/description, viewBox, geometry, scaling and accessible naming; distinguish inherited SVG content from actual Russian-edition edits to embedded labels.
- For canvas/WebGL: provide a meaningful accessible name and a text explanation of the essential state; test fallback when rendering is unavailable.
- Verify actual phone, tablet and desktop rendering, zoom/reflow, labels, clipping, loading and fallback. Existing browser smoke evidence is useful but does not replace manual scientific, legal, language and assistive-technology review.



### Browser regression evidence — 2026-11-05

- Workflow run: https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/41983167799
- Tested commit: b5382a63ea83879bc6d74f9c2aa19a3cfd8deb94
- Result: **SUCCESS** — all six workflow jobs completed successfully.
- The Chromium job passed the existing desktop/mobile interactive-book and chapter smoke tests across all 15 chapters. Chapters 08 and 10 passed the strict isolated keyboard-focus checks (4/4 desktop/mobile lesson/book runs each); the shared native scene-picker focus handoff is therefore resolved for those tested flows.
- Chapter 13 passed its standalone schematic test on desktop and mobile, including Ohm's-law recalculation, power, quiz, WebGL, keyboard operation, no horizontal overflow, and zero serious/critical axe findings.
- Chapters 14 and 15 calculator/interactive lesson tests also passed in that run, but that commit predates the newly integrated SVG visuals. Those earlier results do **not** verify the new images; the updated visual-specific checks are being run separately.
- Latest full regression: [GitHub Actions run 42006633285](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/42006633285), commit `6a70ef79263bc9249ba29749a3b1472025df291e` — **SUCCESS**, all six jobs passed. The Chromium job completed all 28 steps, including the Chapter 14–15 visual/contrast smoke, 15/15 contextual canvas labels, desktop/mobile tests across all 15 chapters, Gauss/Fluids keyboard scene selection, and rotation-book navigation. The five isolated jobs (Gauss, Fluids, Circuits, Magnetism, Induction) also passed.

### Asset-level audit — newly integrated visual IDs

| Visual ID | Integration | Scientific / factual | Rights / licence | Language / accessibility | Technical / responsive | Overall |
|---|---|---|---|---|---|---|
| PHY-14-001 | PASS — desktop and mobile variants integrated | PASS — internal second-pass review: right-hand-rule direction corrected; air-core assumptions for solenoid/toroid formulae made explicit; ideal-toroid external-field limit qualified. External subject-matter review: separate post-publication activity; not a publication gate | PASS — CC BY-NC 4.0 publication licence declared for project-created SVGs; no third-party artwork embedded (does not assert exclusive copyright in AI-generated elements) | PASS — internal RU/EN terminology and caption/alt review; independent learner-comprehension review PENDING | PASS on prior SVG revision — desktop/mobile loading, no overflow, axe serious/critical 0 (run 42006633285); rerun after air-core footnote update PENDING | INTEGRATED, not VERIFIED |
| PHY-15-001 | PASS — desktop and mobile variants integrated | PASS — internal second-pass review: north-pole approach/recession, flux change, induced field, near-face polarity and current directions checked. External subject-matter review: separate post-publication activity; not a publication gate | PASS — CC BY-NC 4.0 publication licence declared for project-created SVGs; no third-party artwork embedded (does not assert exclusive copyright in AI-generated elements) | PASS — internal RU/EN terminology and caption/alt review; independent learner-comprehension review PENDING | PASS on prior SVG revision — desktop/mobile loading, no overflow, axe serious/critical 0 (run 42006633285); rerun after air-core footnote update PENDING | INTEGRATED, not VERIFIED |
| PHY-15-002 | PASS — desktop and mobile variants integrated | PASS — internal second-pass review: B/v/rod geometry, q(v×B), charge separation, closed-loop current and magnetic drag checked. External subject-matter review: separate post-publication activity; not a publication gate | PASS — CC BY-NC 4.0 publication licence declared for project-created SVGs; no third-party artwork embedded (does not assert exclusive copyright in AI-generated elements) | PASS — internal RU/EN terminology and caption/alt review; independent learner-comprehension review PENDING | PASS on prior SVG revision — desktop/mobile loading, no overflow, axe serious/critical 0 (run 42006633285); rerun after air-core footnote update PENDING | INTEGRATED, not VERIFIED |
| PHY-15-003 | PASS — desktop and mobile variants integrated | PASS — internal second-pass review: εL, τ=L/R, LC phase/initial conditions and complementary energy curves checked; U_B notation clarified. External subject-matter review: separate post-publication activity; not a publication gate | PASS — CC BY-NC 4.0 publication licence declared for project-created SVGs; no third-party artwork embedded (does not assert exclusive copyright in AI-generated elements) | PASS — internal RU/EN terminology and caption/alt review; independent learner-comprehension review PENDING | PASS on prior SVG revision — desktop/mobile loading, no overflow, axe serious/critical 0 (run 42006633285); rerun after air-core footnote update PENDING | INTEGRATED, not VERIFIED |

The four assets are Category C. There are eight responsive SVG files (four desktop, four mobile). The four former placeholders are no longer present. A 0% verification rate for these four new assets is provisional until their pending checks pass; it is not the atlas-wide Image Verification metric.

## 5. Preliminary status and metrics

The Russian standalone pages for Chapters 14–15 have also been improved: generic canvas drawings that only displayed a circle and line with the caption “Модель физических величин” were removed because they did not represent the stated physics. They were replaced with explanatory text describing the assumptions and equations of each calculator. Contextual Russian accessible names were added to the remaining 3D and plot canvases.

- Standalone chapter HTML: all 15 chapter pages were scanned on 2026-11-05; no explicit IMAGE PLACEHOLDER / visual TODO markers remain. The four former gaps in Chapters 14–15 are integrated as four Category C visuals with eight responsive SVG files.
- Canvas and lab accessibility names: a static audit of all 15 pages found no remaining generic canvas/lab/phase/formula labels. Generic labels were replaced with chapter-specific descriptions; the automated contextual-name regression test passed 15/15 chapter pages (run 42006633285).

These are inventory findings, **not readiness scores**. They describe the audited branch structure only; they do not establish the complete visual inventory of Nathan Liow's English source atlas:

- Required visual count: **PENDING** — complete visual requirement mapping and deduplication across standalone chapters and interactive-book scenes.
- Integrated visual count: **PENDING** — existing code visuals must be individually identified and reconciled with source records before counting.
- Image Coverage: **PROVISIONAL / NOT CALCULATED** — the required-visual denominator is not yet complete.
- Image Verification: **NOT CALCULATED** — no complete asset-level evidence set exists.
- Image Gaps: **0 known explicit placeholders remaining** — the four previously documented gaps (one in Chapter 14 and three in Chapter 15) now have original SVG assets integrated. The full visual denominator is still incomplete, so additional gaps may be found during scene-by-scene review.
- External assets found and integrated: **0 documented** in the current register.
- Category A / B / C: **not yet reliably counted** across the full derivative atlas. Four new project-created visual assets (eight responsive SVG files) are now recorded as Category C and published under the project-selected CC BY-NC 4.0 licence; independent scientific review remains PENDING. The upstream source and repository-level MIT licence are verified. All 15 `pages.js` modules and all 15 `world.js` modules have been compared with upstream; Russian labels embedded in SVGs, charts, and scenes are Category B for the affected outputs. Fourteen scene modules retain upstream executable logic after string/comment normalisation; Kinematics has a documented buffer-update optimisation. Eleven `model.js` modules are code-equivalent after normalisation; four contain documented calculation/refactoring changes. Individual inherited visual IDs, the three Chapter 04 root-page records, and item-level rights evidence remain pending; do not count unverified records as VERIFIED.
- Scientific/factual, rights, language/accessibility and technical statuses: **PENDING at asset level**, except where individual test evidence is explicitly recorded in the register or CI logs.

## 6. Prioritised action plan

1. Extend the source comparison to all 15 interactive-book modules; map SVG/chart outputs, 3D scenes, models, and embedded labels to their exact upstream files and classify changes.
2. Establish source lineage for the three existing Chapter 04 root-page register entries; do not assign C or creator attribution without evidence.
3. Build a deduplicated inherited-visual map for the 15 standalone chapters and 15 interactive-book modules, linking each identifiable visual to the English source where possible.
4. Audit the Russian edition's terminology, labels, formulas, symbols, units, directions, captions, alt text, long descriptions, layout, mobile rendering and interactive controls. Do not change the English original.
5. Verify source-work reproduction rights and any separate adaptation rights for visual content changed in the Russian edition. Keep unknown rights PENDING.
6. The four specified visual gaps are now filled by original bilingual SVGs: one in Chapter 14 and three in Chapter 15. Complete internal scientific, rights, bilingual/accessibility and current browser/CI checks before marking VERIFIED. Independent external expert review is separate and does not block publication; the project publication licence is declared as CC BY-NC 4.0.
7. Add or correct register records for inherited unchanged visuals, adapted visuals, and genuinely new additions, keeping those groups separate.
8. Add CI checks for file/path existence, register structure, statuses, language fields, SVG validity, dimensions and responsive/overflow checks. Keep scientific, legal and translation approvals human-reviewed.
9. Report source-work coverage, Russian-edition localisation coverage, rights verification and new-visual readiness separately; calculate only with a defined denominator.

## 7. Boundary and exclusions

- All audit and implementation work is restricted to `workspace/physics`.
- Do not edit `main`, the central policy, the portal, publishing settings or other subject branches.
- Do not alter the English original by Nathan Liow. This audit concerns the Physics branch's own visual components and permitted Russian/subject implementation records.
- The four previously identified placeholders now have SVG assets integrated. They are INTEGRATED, not VERIFIED; scientific, rights, and browser evidence must still be completed.
- Physical-device classroom testing and external expert sign-off are separate follow-up activities; neither substitutes for internal publication QA nor blocks publication.

---

**Audit conclusion:** Physics is a derivative Russian-language edition of Nathan Liow's pre-existing English atlas, not a newly authored visual atlas. The correct work is to trace inherited visuals to the source, verify reproduction and adaptation rights, and audit the Russian edition's localisation, accessibility and rendering. Only genuinely modified visuals should be classified B, and only genuinely new independent visuals should be classified C. The four known placeholders have been replaced by original bilingual SVG schematics and are recorded as Category C. Their eight responsive SVG files are published under CC BY-NC 4.0 (project decision approved 2026-11-05); independent external expert review is a separate post-publication activity, not a publication gate; assets remain INTEGRATED until internal publication checks are complete. No blanket re-creation or indiscriminate re-search of unchanged inherited visuals is required.
