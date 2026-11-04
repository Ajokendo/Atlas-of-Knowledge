# Physics — IMAGE_AUDIT

- Subject: Physics
- Working branch: `workspace/physics`
- Audit date: 2026-11-05
- Target policy: `IMAGE-FIRST POLICY v1.1` (AOK-IMG-001)
- Canonical policy observed at: `atlas-of-knowledge-integration:IMAGE_FIRST_POLICY.md`
- Policy availability note: at audit time the canonical file is present in `atlas-of-knowledge-integration`, but was not present in the fetched `main` tree. The Physics branch still contains the older local `IMAGE_POLICY.md`. Do not create another copy of the universal policy; replace the local duplicate with a link after the canonical root document is integrated into the subject branch through the central project process.
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
- The upstream repository declares the **MIT License**, with copyright notice **Copyright (c) 2026 Nathan Liow**. The licence grants rights to use, copy, modify, merge, publish, distribute, sublicense, and sell the software, subject to retaining the copyright and permission notice.
- The Physics branch's `original-engine/README.md` explicitly identifies the upstream project and states that original interactive laboratories are integrated, while learning text, interface, labels, and explanations are adapted into Russian.

This establishes a documented MIT licence basis for the upstream repository code and permitted modifications, subject to retaining the required notice. It does **not** automatically clear any separately embedded third-party content if such content is present; those components still require their own rights checks. The root-level Russian chapter pages are separate implementations and must be mapped to their source material before their assets are assigned A/B/C.

### 1.3 Initial source comparison — confirmed samples

A direct source comparison was made for the Energy, Magnetism, and Induction interactive-book modules:

- `original-engine/energy/pages.js` vs upstream `energy/pages.js`;
- `original-engine/magnetism/pages.js` vs upstream `magnetism/pages.js`;
- `original-engine/induction/pages.js` vs upstream `induction/pages.js`.

The local modules preserve the source module structure and visual/chart-generation logic while translating learner-facing text, chart labels, axis units, figure names, and SVG accessible names into Russian. These changes are **Category B — Adapted** for the affected SVG/chart visual outputs, not merely a translation of surrounding page prose, because the labels and accessible names are part of the visual component. The code's upstream lineage and MIT licence must be recorded; retain Nathan Liow's copyright/licence notice.

The corresponding `world.js` and `model.js` files in the three sampled chapters are not byte-identical to upstream. Their differences have not yet been classified line by line, so do not call those 3D scenes unchanged A or independently created C. Keep them **B/PENDING comparison** until the differences are reviewed to determine whether they are translation/localisation, bug fixes, or substantive changes to the visual/physical model.

The sample confirms the upstream lineage for these modules; it does not yet constitute a complete asset-by-asset inventory of all 15 chapters.

A second comparison of the Magnetism and Induction scene/model files found:

- In `magnetism/world.js`, object names, scene titles, vector descriptions, field/current labels, and voltage labels are translated into Russian. The 3D geometry and scene construction are retained in the sampled sections. Because in-scene labels are part of the visual output, these scene visuals are **B — Adapted** (localised visual labels), not A.
- In `induction/world.js`, the same pattern is present: the 3D scene structure is retained while names, magnetic-field/current labels, loop/coil labels, and explanatory text are translated. The affected scene visuals are **B — Adapted**.
- In `induction/model.js`, the four magnet-pole movement case names are translated; the sampled change is learner-facing scenario text, not a new independent visual.
- In `magnetism/model.js`, additional `sinDeg`/`cosDeg` helpers remove floating-point residue at exact parallel/perpendicular angles. This is a computational correction, not evidence of a newly authored visual. It should remain documented as a branch-specific physics/model fix and be covered by the chapter's numerical checks.
- In `energy/pages.js`, Russian chart labels, axis units, figure names and accessible names are present. A chart range also differs from upstream (`bondU` y-range), so this is not a translation-only difference; the altered domain requires scientific/pedagogical verification before the corresponding chart is marked VERIFIED.

These comparisons support Category B for the affected Russian-labelled scene/chart outputs. They do not establish that every scene in the modules has been reviewed, nor do they determine final per-visual counts.

### 1.4 Localisation review required

The Russian edition must be checked for accurate terminology, labels, symbols, legends, units, formulas, vector directions, numerical values, layout after text expansion, readable mobile presentation, captions, alt text, long descriptions, and equivalent data/text for complex visuals. The English source is not to be edited as part of this work.

## 2. Repository inventory findings

| Check | Observed result | Interpretation |
|---|---:|---|
| Standalone Physics chapter pages | 15 | All chapters 01–15 in the current chapter set were included |
| HTML `<img>` elements in those pages | 0 | No ordinary raster/photo assets are embedded in the 15 standalone chapter pages |
| Inline SVG in standalone chapter pages | 2 | Present in Kinematics and Work & Energy; require complete source/creator/rights/accessibility records |
| Canvas elements in standalone chapter pages | 43 after this audit's cleanup | Initially 45; the generic non-informative canvas in Magnetism and the equivalent canvas in Induction were removed and replaced with accurate explanatory text. Remaining canvases are rendering surfaces, not automatically distinct assets. |
| Explicit visual placeholder groups | 4 | Chapter 14: one four-topic infographic; Chapter 15: three separate visual briefs |
| Existing records in `IMAGE_SOURCES.md` | 3 | All three currently documented records concern Chapter 04 |
| External visual assets documented as integrated | 0 | No external image is claimed as integrated in the current register |
| Interactive-book modules | 15 | Each contains a substantial set of programmatic figures/scenes; figure-label metadata was found across all modules, but each scene still needs individual asset IDs and checks |

The absence of `<img>` elements is not a finding that the atlas lacks visual learning material. The Physics branch relies heavily on inline SVG, canvas, charts, and WebGL/Three.js scenes. Rendering technology alone does not establish authorship or category: each visual must first be traced to the English source or to a documented branch-specific addition. Unchanged inherited scenes are normally A; actual visual modifications are B; only genuinely new independent assets are C.

## 3. Chapter-by-chapter preliminary visual audit

Status meanings: **PENDING** = the visual requirement or asset still needs a complete evidence-based review; **INVENTORY** = code/markup presence observed, not approval. No chapter is declared visually VERIFIED by this preliminary audit.

| Chapter | Visual learning needs to verify | Observed implementation | Required action |
|---|---|---|---|
| 01 — Kinematics | Position/displacement vectors; velocity and acceleration; motion graphs; projectile path; relative motion/reference frames | Inline SVG and 3 canvas elements in standalone page; interactive-book figures include position, velocity, acceleration, stroboscopic sequence, graphs, projectile and river-crossing examples | Assign stable IDs to each distinct visual; verify vector directions, graph axes/units, projectile assumptions and bilingual descriptions; add a text/data alternative for graphs |
| 02 — Newton's Laws | Free-body diagrams; action–reaction pairs on different bodies; friction/tension/normal-force cases; acceleration comparisons | 3 canvas elements; interactive figures cover all three laws, tension, friction, system selection and centre-of-mass acceleration | Audit each force diagram for body isolation, equal/opposite pair placement, vector direction and labels; ensure meaning is not colour-only |
| 03 — Circular Motion | Tangential velocity and centripetal acceleration; force direction; turning, conical pendulum, vertical circle, banked turn and orbits | 1 canvas element; interactive-book figures cover these cases | Add separate records for distinct diagrams/scenes; verify instantaneous vector directions, radial direction, orbit scale/assumptions and non-uniform cases |
| 04 — Work and Energy | Force/displacement angle; positive/negative/zero work; energy transformations; potential-energy profile | Inline SVG, 3 canvas elements; 3 assets already documented in register (force diagram, energy plot, 3D incline scene) | Retain existing records but migrate them to v1.0 fields; explicitly identify creator/rightsholder evidence, method, limitations, reviewer/date, bilingual captions/alt and technical evidence; confirm whether the three records cover every required visual |
| 05 — Momentum | Before/after collision states; momentum vectors; impulse over time; elastic/inelastic distinctions; centre of mass | 3 canvas elements; interactive figures cover impulse, collisions, explosion, ballistic pendulum and centre of mass | Record visual IDs; check vector conservation, system boundaries, mass/velocity labels and energy distinction; add accessible textual summary |
| 06 — Oscillations | Spring and pendulum geometry; x/v/a phase; energy exchange; damping and driven resonance | 3 canvas elements; interactive figures cover spring, pendulum, phase variables and energy | Add records; check phase relationships, equilibrium positions, small-angle assumptions and damping/drive distinctions; provide accessible graph summaries |
| 07 — Rotation | Angular variables; torque arms; equilibrium; moment of inertia; parallel-axis theorem; rolling; angular momentum | 3 canvas elements; interactive figures cover torque, equilibrium, ladder, inertia, Steiner theorem, work/power and rolling | Add records; verify lever arms, torque signs, axes, mass distributions, rolling conditions and vector direction; include bilingual descriptions and mobile checks |
| 08 — Fluids | Density/volume comparison; pressure and depth; Pascal press; buoyancy/free-body balance; continuity; Bernoulli; Torricelli | 3 canvas elements; interactive figures cover pressure, depth, hydraulic force, buoyancy, flow area/speed and outflow | Add records; check units, pressure reference, flow assumptions, streamline/area relationships, buoyant-force direction and model limitations |
| 09 — Electrostatics | Charge signs; Coulomb-force vectors; superposition; field lines; dipoles; extended charge distributions; uniform fields | 3 canvas elements; interactive figures include charge configurations, field, dipole, rod, ring and parallel plates | Add records; check field-line direction and density conventions, vector superposition, signs, geometry and whether diagrams are conceptual or quantitative |
| 10 — Gauss's Law | Electric flux and surface orientation; Gaussian surfaces; symmetry cases (line, sheet, sphere); conductor vs insulator | 3 canvas elements; interactive figures include rotating surface, Gaussian surfaces, line, sheet, sphere and conductor cases | Add records; verify normals, enclosed charge, flux sign, symmetry and conductor boundary conditions; mark idealisations |
| 11 — Electric Potential | Potential energy vs potential; equipotentials; potential landscapes; dipole and extended-charge examples | 3 canvas elements; interactive figures include potential landscape, dipole, rod/ring/disk and spheres | Add records; distinguish scalar potential from vector field, label units and zero reference, explain potential-landscape analogy and add text alternative |
| 12 — Capacitors | Plate geometry and field; charge/voltage relation; dielectric insertion; connected/disconnected battery cases; series/parallel combinations; energy | 3 canvas elements; interactive figures include parallel plates, dielectric, battery state and combinations | Add records; verify what is held constant in each scenario, field direction, polarity, dimensions and formula assumptions |
| 13 — Electric Circuits | Circuit symbols; current direction vs electron drift; potential rise/drop; series/parallel networks; Kirchhoff loops; RC transients | 3 canvas elements; interactive figures include resistor networks, battery, power, Kirchhoff and RC examples | Add records; verify conventional-current arrows, polarity, node/loop labels, component values and graph axes/time constants; ensure circuit diagrams are readable on mobile |
| 14 — Magnetism | Magnetic-field lines; Lorentz force and trajectories; velocity selector; current-loop moment; Ampère/Biot–Savart; parallel wires; solenoid and toroid | 2 canvas elements remain in standalone page; generic placeholder canvas removed and replaced by a text explanation of the fixed-angle Lorentz-force calculation; interactive-book scenes and Russian labels are inherited/adapted; one four-topic infographic placeholder remains | Keep the bilingual four-topic infographic PENDING; register inherited/adapted scenes; check right-hand rules, current/field directions, toroid leakage and ideal-model qualifications; verify contextual canvas names and text alternatives |
| 15 — Electromagnetic Induction | Flux change; Lenz's law; mutual induction; motional EMF; moving rod; self-induction; RL and LC behaviour | 2 canvas elements remain in standalone page; generic placeholder canvas removed and replaced by a text explanation of the calculator's ΔB/ΔΦ assumptions; interactive-book scenes and Russian labels are inherited/adapted; three visual placeholders remain | Keep three bilingual visual briefs PENDING; register inherited/adapted scenes; verify sign conventions, flux orientation, mutually perpendicular geometry, energy/current curves and RL/LC assumptions; verify contextual canvas names and text alternatives |

Numbering note: chapter numbers follow Nathan Liow's original 15-chapter sequence and the chapter metadata in the Russian HTML files. The filenames in `chapters/` are thematic and must not be interpreted as sequential chapter numbers. The standalone placeholders are Chapter 14 (Magnetism: one planned four-topic infographic) and Chapter 15 (Electromagnetic Induction: three planned visual briefs).
## 4. Physics derivative-edition corrections required by IMAGE-FIRST v1.1

### 4.1 Required governance and record files
- Maintain this `IMAGE_AUDIT.md` as the Physics derivative-edition audit, explicitly preserving source lineage.
- Expand `IMAGE_SOURCES.md` to identify inherited visuals and branch-specific additions, but do not assume every canvas or figure label is a distinct asset. Use stable IDs only after the underlying visual and its source relationship are identified.
- The universal standard was updated centrally to v1.1 on `atlas-of-knowledge-integration`. The subject branch should link to that canonical document when it is brought into this branch through the central integration process; do not create a competing local copy or claim the branch already contains the canonical file.
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

## 5. Preliminary status and metrics

The Russian standalone pages for Chapters 14–15 have also been improved: generic canvas drawings that only displayed a circle and line with the caption “Модель физических величин” were removed because they did not represent the stated physics. They were replaced with explanatory text describing the assumptions and equations of each calculator. Contextual Russian accessible names were added to the remaining 3D and plot canvases.

These are inventory findings, **not readiness scores**. They describe the audited branch structure only; they do not establish the complete visual inventory of Nathan Liow's English source atlas:

- Required visual count: **PENDING** — complete visual requirement mapping and deduplication across standalone chapters and interactive-book scenes.
- Integrated visual count: **PENDING** — existing code visuals must be individually identified and reconciled with source records before counting.
- Image Coverage: **PROVISIONAL / NOT CALCULATED** — the required-visual denominator is not yet complete.
- Image Verification: **NOT CALCULATED** — no complete asset-level evidence set exists.
- Image Gaps: **PENDING INVENTORY** — four explicit placeholders are known (one in Chapter 12 and three in Chapter 13); additional gaps may be found during scene-by-scene review.
- External assets found and integrated: **0 documented** in the current register.
- Category A / B / C: **not yet reliably counted** across the derivative atlas. The upstream source and MIT licence are now verified. The three sampled `pages.js` modules contain Russian-localised SVG/chart outputs and are Category B for the affected visuals; corresponding `world.js`/`model.js` scene differences remain B/PENDING pending line-level review. The three Chapter 04 root-page records remain PENDING source mapping and must not be counted as C yet.
- Scientific/factual, rights, language/accessibility and technical statuses: **PENDING at asset level**, except where individual test evidence is explicitly recorded in the register or CI logs.

## 6. Prioritised action plan

1. Extend the source comparison to all 15 interactive-book modules; map SVG/chart outputs, 3D scenes, models, and embedded labels to their exact upstream files and classify changes.
2. Establish source lineage for the three existing Chapter 04 root-page register entries; do not assign C or creator attribution without evidence.
3. Build a deduplicated inherited-visual map for the 15 standalone chapters and 15 interactive-book modules, linking each identifiable visual to the English source where possible.
3. Audit the Russian edition's terminology, labels, formulas, symbols, units, directions, captions, alt text, long descriptions, layout, mobile rendering and interactive controls. Do not change the English original.
4. Verify source-work reproduction rights and any separate adaptation rights for visual content changed in the Russian edition. Keep unknown rights PENDING.
5. Preserve the four already specified visual placeholders (Chapter 12: one four-topic infographic; Chapter 13: three visual briefs). These are genuine outstanding visual needs; only search/create replacements if appropriate and rights-cleared. If image generation is unavailable, retain explicit PENDING status.
6. Add or correct register records for inherited unchanged visuals, adapted visuals, and genuinely new additions, keeping those groups separate.
7. Add CI checks for file/path existence, register structure, statuses, language fields, SVG validity, dimensions and responsive/overflow checks. Keep scientific, legal and translation approvals human-reviewed.
8. Report source-work coverage, Russian-edition localisation coverage, rights verification and new-visual readiness separately; calculate only with a defined denominator.

## 7. Boundary and exclusions

- All audit and implementation work is restricted to `workspace/physics`.
- Do not edit `main`, the central policy, the portal, publishing settings or other subject branches.
- Do not alter the English original by Nathan Liow. This audit concerns the Physics branch's own visual components and permitted Russian/subject implementation records.
- The four existing placeholders remain pending; no image is claimed created or integrated by this audit.
- Physical-device classroom testing and expert sign-off remain separate from automated browser/CI evidence.

---

**Audit conclusion:** Physics is a derivative Russian-language edition of Nathan Liow's pre-existing English atlas, not a newly authored visual atlas. The correct work is to trace inherited visuals to the source, verify reproduction and adaptation rights, and audit the Russian edition's localisation, accessibility and rendering. Only genuinely modified visuals should be classified B, and only genuinely new independent visuals should be classified C. The four known placeholders remain separate outstanding visual needs. No blanket re-creation or indiscriminate re-search of unchanged inherited visuals is required.
