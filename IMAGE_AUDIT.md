# Physics — IMAGE_AUDIT

- Subject: Physics
- Working branch: `workspace/physics`
- Audit date: 2026-11-05
- Target policy: `IMAGE-FIRST POLICY v1.0` (AOK-IMG-001)
- Canonical policy observed at: `atlas-of-knowledge-integration:IMAGE_FIRST_POLICY.md`
- Policy availability note: at audit time the canonical file is present in `atlas-of-knowledge-integration`, but was not present in the fetched `main` tree. The Physics branch still contains the older local `IMAGE_POLICY.md`. Do not create another copy of the universal policy; replace the local duplicate with a link after the canonical root document is integrated into the subject branch through the central project process.
- Scope: all 15 standalone chapter pages under `chapters/`, the 15 corresponding interactive-book page modules under `original-engine/*/pages.js`, and the existing `IMAGE_SOURCES.md` register.
- Audit type: preliminary structural and inventory audit. This document does not claim that every visual has passed expert scientific, rights, bilingual, accessibility, or manual visual review.

## 1. Repository inventory findings

| Check | Observed result | Interpretation |
|---|---:|---|
| Standalone Physics chapter pages | 15 | All chapters 01–15 in the current chapter set were included |
| HTML `<img>` elements in those pages | 0 | No ordinary raster/photo assets are embedded in the 15 standalone chapter pages |
| Inline SVG in standalone chapter pages | 2 | Present in Kinematics and Work & Energy; require complete source/creator/rights/accessibility records |
| Canvas elements in standalone chapter pages | 45 (3 per page) | Rendering surfaces, not automatically 45 distinct assets; each canvas must be classified by its actual content and learning purpose |
| Explicit visual placeholder groups | 4 | Chapter 14: one four-topic infographic; Chapter 15: three separate visual briefs |
| Existing records in `IMAGE_SOURCES.md` | 3 | All three currently documented records concern Chapter 04 |
| External visual assets documented as integrated | 0 | No external image is claimed as integrated in the current register |
| Interactive-book modules | 15 | Each contains a substantial set of programmatic figures/scenes; figure-label metadata was found across all modules, but each scene still needs individual asset IDs and checks |

The absence of `<img>` elements is not a finding that the atlas lacks visual learning material. The Physics atlas relies heavily on code-authored SVG, canvas, charts, and WebGL/Three.js scenes. These are Category C assets under v1.0 and must be registered, reviewed, and counted separately by method.

## 2. Chapter-by-chapter preliminary visual audit

Status meanings: **PENDING** = the visual requirement or asset still needs a complete evidence-based review; **INVENTORY** = code/markup presence observed, not approval. No chapter is declared visually VERIFIED by this preliminary audit.

| Chapter | Visual learning needs to verify | Observed implementation | Required action |
|---|---|---|---|
| 01 — Kinematics | Position/displacement vectors; velocity and acceleration; motion graphs; projectile path; relative motion/reference frames | Inline SVG and 3 canvas elements in standalone page; interactive-book figures include position, velocity, acceleration, stroboscopic sequence, graphs, projectile and river-crossing examples | Assign stable IDs to each distinct visual; verify vector directions, graph axes/units, projectile assumptions and bilingual descriptions; add a text/data alternative for graphs |
| 02 — Newton's Laws | Free-body diagrams; action–reaction pairs on different bodies; friction/tension/normal-force cases; acceleration comparisons | 3 canvas elements; interactive figures cover all three laws, tension, friction, system selection and centre-of-mass acceleration | Audit each force diagram for body isolation, equal/opposite pair placement, vector direction and labels; ensure meaning is not colour-only |
| 03 — Momentum | Before/after collision states; momentum vectors; impulse over time; elastic/inelastic distinctions; centre of mass | 3 canvas elements; interactive figures cover impulse, collisions, explosion, ballistic pendulum and centre of mass | Record visual IDs; check vector conservation, system boundaries, mass/velocity labels and energy distinction; add accessible textual summary |
| 04 — Work and Energy | Force/displacement angle; positive/negative/zero work; energy transformations; potential-energy profile | Inline SVG, 3 canvas elements; 3 assets already documented in register (force diagram, energy plot, 3D incline scene) | Retain existing records but migrate them to v1.0 fields; explicitly identify creator/rightsholder evidence, method, limitations, reviewer/date, bilingual captions/alt and technical evidence; confirm whether the three records cover every required visual |
| 05 — Circular Motion | Tangential velocity and centripetal acceleration; force direction; turning, conical pendulum, vertical circle, banked turn and orbits | 1 canvas element; interactive-book figures cover these cases | Add separate records for distinct diagrams/scenes; verify instantaneous vector directions, radial direction, orbit scale/assumptions and non-uniform cases |
| 06 — Fluids | Density/volume comparison; pressure and depth; Pascal press; buoyancy/free-body balance; continuity; Bernoulli; Torricelli | 3 canvas elements; interactive figures cover pressure, depth, hydraulic force, buoyancy, flow area/speed and outflow | Add records; check units, pressure reference, flow assumptions, streamline/area relationships, buoyant-force direction and model limitations |
| 07 — Electrostatics | Charge signs; Coulomb-force vectors; superposition; field lines; dipoles; extended charge distributions; uniform fields | 3 canvas elements; interactive figures include charge configurations, field, dipole, rod, ring and parallel plates | Add records; check field-line direction and density conventions, vector superposition, signs, geometry and whether diagrams are conceptual or quantitative |
| 08 — Electric Potential | Potential energy vs potential; equipotentials; potential landscapes; dipole and extended-charge examples | 3 canvas elements; interactive figures include potential landscape, dipole, rod/ring/disk and spheres | Add records; distinguish scalar potential from vector field, label units and zero reference, explain potential-landscape analogy and add text alternative |
| 09 — Capacitors | Plate geometry and field; charge/voltage relation; dielectric insertion; connected/disconnected battery cases; series/parallel combinations; energy | 3 canvas elements; interactive figures include parallel plates, dielectric, battery state and combinations | Add records; verify what is held constant in each scenario, field direction, polarity, dimensions and formula assumptions |
| 10 — Electric Circuits | Circuit symbols; current direction vs electron drift; potential rise/drop; series/parallel networks; Kirchhoff loops; RC transients | 3 canvas elements; interactive figures include resistor networks, battery, power, Kirchhoff and RC examples | Add records; verify conventional-current arrows, polarity, node/loop labels, component values and graph axes/time constants; ensure circuit diagrams are readable on mobile |
| 11 — Gauss's Law | Electric flux and surface orientation; Gaussian surfaces; symmetry cases (line, sheet, sphere); conductor vs insulator | 3 canvas elements; interactive figures include rotating surface, Gaussian surfaces, line, sheet, sphere and conductor cases | Add records; verify normals, enclosed charge, flux sign, symmetry and conductor boundary conditions; mark idealisations |
| 12 — Magnetism | Magnetic-field lines; Lorentz force and trajectories; velocity selector; current-loop moment; Ampère/Biot–Savart; parallel wires; solenoid and toroid | 3 canvas elements; interactive-book figures across magnetic-field topics; one four-topic infographic placeholder in standalone chapter | Complete one planned bilingual infographic for straight wire, circular loop, solenoid and toroid; register all interactive figures separately; verify right-hand rules, current/field directions, toroid leakage and ideal-model qualifications |
| 13 — Electromagnetic Induction | Flux change; Lenz's law; mutual induction; motional EMF; moving rod; self-induction; RL and LC behaviour | 3 canvas elements; interactive-book figures cover magnet/coil, Lenz, mutual induction, moving rod, inductance, RL and LC; three placeholders in standalone chapter | Complete three bilingual visual briefs; verify sign conventions, flux orientation, mutually perpendicular geometry, energy/current curves and RL/LC assumptions |
| 14 — Oscillations | Spring and pendulum geometry; x/v/a phase; energy exchange; damping and driven resonance | 3 canvas elements; interactive figures cover spring, pendulum, phase variables and energy | Add records; check phase relationships, equilibrium positions, small-angle assumptions and damping/drive distinctions; provide accessible graph summaries |
| 15 — Rotation | Angular variables; torque arms; equilibrium; moment of inertia; parallel-axis theorem; rolling; angular momentum | 3 canvas elements; interactive figures cover torque, equilibrium, ladder, inertia, Steiner theorem, work/power and rolling | Add records; verify lever arms, torque signs, axes, mass distributions, rolling conditions and vector direction; include bilingual descriptions and mobile checks |

## 3. Cross-atlas corrections required by IMAGE-FIRST v1.0

### 3.1 Required governance and record files
- **Create/maintain this `IMAGE_AUDIT.md`** as the Physics audit record.
- Expand `IMAGE_SOURCES.md` from its Chapter 04-only register into a complete register for all distinct assets in standalone chapters and interactive-book modules.
- Replace the old subject-level policy copy with a link to the canonical root `IMAGE_FIRST_POLICY.md` once that file is present in the Physics branch through the central integration process. Until then, preserve the current local policy and record this governance dependency; do not silently claim v1.0 is already implemented.
- Add a Physics-specific checklist supplement only where needed (for example: vector directions, coordinate frames, sign conventions, idealisations, units, scale and measurement-vs-model distinctions). It must not redefine universal statuses or metrics.

### 3.2 Asset identity and classification
- Give every distinct figure, diagram, chart, SVG, canvas visual, 3D scene, animation and infographic a stable Visual ID.
- Classify each as A (unmodified external reuse), B (adapted external asset), or C (created). For C, state the exact method: hand-authored SVG, HTML/CSS, code-generated chart, canvas, Three.js/WebGL, AI-generated image, photograph, etc.
- Do not treat a canvas element as a unique asset until its rendered visual and learning purpose have been identified. Do not count a multi-state interactive scene multiple times unless the states are separate learning assets.
- The 15 interactive-book page modules have numerous figure labels and examples. These need an asset-level inventory, not one blanket record per chapter.

### 3.3 Rights, creator and provenance
- For existing project-created visuals, identify the actual creator/rightsholder from repository history or mark **Unknown**; do not infer an individual author.
- Record the project licence and its exact evidence URL. A repository-level MIT licence is not a substitute for identifying creator/rightsholder or checking third-party components.
- For every external candidate, document search date, search terms/collections, exact item page, creator, item-specific licence, licence evidence, permitted modifications and attribution. No external asset is approved merely because it appears on a reputable platform.
- AI-generated visuals must be marked as illustrations/reconstructions, not real experiments or measured evidence.

### 3.4 Bilingual, accessibility and technical review
- Add Russian and English captions and meaningful alt text for every non-decorative visual, including visuals embedded in the interactive-book system.
- Add a nearby explanation or data/table equivalent for complex diagrams and charts.
- Check that colour is not the only carrier of meaning; use arrows, labels, patterns, line styles and symbols.
- For interactive diagrams: test keyboard operation, focus, accessible names/descriptions and screen-reader output where applicable.
- For charts: check axis titles, units, ranges, assumptions, data/equation provenance and text alternatives.
- For SVG: validate title/description, viewBox, geometry, scaling and accessible naming.
- For canvas/WebGL: provide a meaningful accessible name and a text explanation of the essential state; test fallback when rendering is unavailable.
- Verify actual phone, tablet and desktop rendering, zoom/reflow, labels, clipping, loading and fallback. Existing browser smoke evidence is useful but does not replace manual scientific, legal, language and assistive-technology review.

## 4. Preliminary status and metrics

These are inventory findings, **not readiness scores**:

- Required visual count: **PENDING** — complete visual requirement mapping and deduplication across standalone chapters and interactive-book scenes.
- Integrated visual count: **PENDING** — existing code visuals must be individually identified and reconciled with source records before counting.
- Image Coverage: **PROVISIONAL / NOT CALCULATED** — the required-visual denominator is not yet complete.
- Image Verification: **NOT CALCULATED** — no complete asset-level evidence set exists.
- Image Gaps: **PENDING INVENTORY** — four explicit placeholders are known (one in Chapter 12 and three in Chapter 13); additional gaps may be found during scene-by-scene review.
- External assets found and integrated: **0 documented** in the current register.
- Category C: **at least 3 documented** for Chapter 04; additional authored/code-generated visuals exist but are not yet fully registered.
- Category A / B: **0 documented** in the current register; this is not proof that none exist elsewhere in the repository.
- Scientific/factual, rights, language/accessibility and technical statuses: **PENDING at asset level**, except where individual test evidence is explicitly recorded in the register or CI logs.

## 5. Prioritised action plan

1. Resolve canonical-policy availability in the subject branch through the central integration process; remove the duplicate policy copy only when the canonical link will resolve.
2. Build a deduplicated Visual ID inventory for all 15 interactive-book modules and all 15 standalone chapter pages.
3. Repair the Chapter 04 source records to the v1.0 schema and add the remaining existing visuals before counting coverage.
4. Complete the four already specified placeholders in Chapters 12–13 only after suitable-source search and rights/scientific review; if image generation is unavailable, retain explicit PENDING status.
5. Add bilingual captions/alt text, accessibility alternatives and responsive checks to every inventoried visual.
6. Add CI checks for local asset existence, register fields, statuses, language fields, SVG validity, dimensions and responsive/overflow checks. Keep expert science, licence and translation approvals as human-reviewed fields; CI must not mark them PASS merely because fields are populated.
7. Recalculate chapter and subject Image Coverage, Image Verification, Image Gaps and A/B/C counts only after the denominator and asset inventory are complete.

## 6. Boundary and exclusions

- All audit and implementation work is restricted to `workspace/physics`.
- Do not edit `main`, the central policy, the portal, publishing settings or other subject branches.
- Do not alter the English original by Nathan Liow. This audit concerns the Physics branch's own visual components and permitted Russian/subject implementation records.
- The four existing placeholders remain pending; no image is claimed created or integrated by this audit.
- Physical-device classroom testing and expert sign-off remain separate from automated browser/CI evidence.

---

**Audit conclusion:** Physics has substantial programmatically created visual content, but its visual governance and provenance records are far behind the actual implementation. The main corrective work is not to indiscriminately add decorative pictures: it is to inventory and register the existing SVG/canvas/WebGL teaching visuals, validate their scientific and accessibility quality, document rights/creator accurately, close the four known placeholder needs, and only then calculate visual readiness.
