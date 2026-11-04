# Physics — IMAGE_SOURCES

- Applicable universal standard: [`IMAGE-FIRST POLICY v1.1`](https://github.com/Ajokendo/Atlas-of-Knowledge/blob/main/IMAGE_FIRST_POLICY.md) (`AOK-IMG-001`).
- Working branch: `workspace/physics`.
- Upstream comparison snapshot: [Nathan Liow / Atlas of Physics, commit `bcd67d9b75425f4a78f5c7c1d17a2d0614727309`](https://github.com/nathanliow/atlas-of-physics/commit/bcd67d9b75425f4a78f5c7c1d17a2d0614727309) (2026-10-30).

This register documents every visual asset integrated into the Physics atlas. Add one complete record per asset. Do not list search results or unverified candidates as integrated.

## Reporting metrics — provisional during source-lineage audit

The Physics branch is a derivative Russian-language edition of Nathan Liow's pre-existing English atlas. The current three Chapter 04 records describe implementation forms found in this branch; they do **not yet prove** that those visuals were independently authored here.

| Metric | Count | Counting rule |
|---|---:|---|
| Inherited visuals mapped to English source | PENDING | Requires source-to-derivative comparison |
| Inherited visuals reused unchanged (A) | PENDING | Count only after visual identity and unchanged status are verified |
| Inherited visuals adapted (B) | PENDING | Count only after the visual-content changes and adaptation rights are checked |
| Genuinely new project-created visuals (C) | PENDING | Do not infer from SVG/canvas/Three.js implementation alone |
| Rights / reproduction permission verified | PENDING | Requires evidence for the exact source work and applicable components |
| Russian-edition localisation verified | PENDING | Requires per-visual Russian labels, captions, alt text, descriptions and rendering checks |
| Known visual placeholders | 4 | One planned infographic in Chapter 14 and three visual briefs in Chapter 15 |

**Important:** the three existing Chapter 04 entries are retained as discovery records, not certified Category C assets. Their relationship to the English source, actual creator/rightsholder, and rights basis must be checked before assigning a final A/B/C category or reporting readiness. A repository licence must not be treated as proof that third-party inherited material may be reproduced or adapted.

## Provenance rule for this derivative edition

For every inherited visual, record the English source location/identifier where it can be established, the source-work attribution, the actual relationship of the Russian implementation to that source, and the evidence for reproduction/adaptation rights. Keep unknown facts as **Unknown / PENDING**. Translation of surrounding page text, captions, controls, or alt text is recorded as localisation and does not by itself make the visual Category B. Editing text or content inside the visual, cropping, recolouring, annotation, redrawing, or changing data/meaning is Category B and requires adaptation rights. Genuinely independent new assets are Category C.

The implementation technology (SVG, canvas, JavaScript, WebGL, Three.js) describes how a visual is rendered; it does not establish who authored the underlying educational visual or whether it is inherited.


## Verified upstream source for inherited interactive visuals

- Original work: Nathan Liow, *Atlas of Physics*
- Repository: https://github.com/nathanliow/atlas-of-physics
- Upstream description and architecture: https://github.com/nathanliow/atlas-of-physics/blob/main/README.md
- Licence: MIT License — https://github.com/nathanliow/atlas-of-physics/blob/main/LICENSE
- Copyright notice required by the upstream licence: Copyright (c) 2026 Nathan Liow
- Local integration record: `original-engine/README.md`

The upstream README describes the interactive 3D textbook architecture and the original chapter modules. The local integration README explicitly identifies Nathan Liow's repository as the source and states that the original interactive laboratories are integrated while learner-facing text, interface, labels, and explanations are adapted into Russian.

Initial file-level comparisons have confirmed this relationship for all 15 interactive-book page modules (original chapter order):

- Chapter 01: `kinematics/pages.js`
- Chapter 02: `newton/pages.js`
- Chapter 03: `circular/pages.js`
- Chapter 04: `energy/pages.js`
- Chapter 05: `momentum/pages.js`
- Chapter 06: `oscillations/pages.js`
- Chapter 07: `rotation/pages.js`
- Chapter 08: `fluids/pages.js`
- Chapter 09: `electrostatics/pages.js`
- Chapter 10: `gauss/pages.js`
- Chapter 11: `potential/pages.js`
- Chapter 12: `capacitors/pages.js`
- Chapter 13: `circuits/pages.js`
- Chapter 14: `magnetism/pages.js`
- Chapter 15: `induction/pages.js`

Each local module differs from its upstream counterpart and contains Russian localisation. Embedded SVG/chart labels and accessible visual labels are Category B where those visual outputs are changed. This is a page-module lineage comparison, not a count or complete visual audit of every distinct scene. The Energy chart-domain correction and Magnetism numerical helper correction are documented separately in `IMAGE_AUDIT.md`.

The comparison was extended to the matching `world.js` and `model.js` modules for all 15 chapters:

- All 15 `world.js` scene modules have been compared. Fourteen retain upstream executable logic after string/comment normalisation; the Russian scene names, labels, and accessible descriptions are localisation of the visual output (Category B where embedded in the scene). Kinematics additionally preallocates and updates its graph-area vertex buffer rather than rebuilding the attribute each frame; the generated vertex coordinates and draw range are retained.
- Eleven `model.js` modules are code-equivalent to upstream after string/comment normalisation.
- Four `model.js` modules contain specific local changes: `electrostatics` adds the sampled electron-trajectory helper used by its chart; `potential` corrects the charged-disc potential symmetry with `|z|); `capacitors` corrects the disc-field direction and symmetry with `Math.sign(z)` and `Math.abs(z)` and adds a numerical line-integral helper; `magnetism` adds exact-angle sine/cosine helpers to remove floating-point residue.
- These model changes are calculation or rendering-data changes, not independent authorship of the inherited 3D scenes. Their regression checks are present in the branch; execution remains to be confirmed by CI or a local test run.

The module comparison is source-lineage evidence, not a substitute for individual visual IDs, item-level rights evidence, manual visual review, or final verification.

The Russian `pages.js` files translate chart/SVG labels, axis units, captions, and accessible names; the affected visual outputs are therefore Category B (adapted). All 15 `world.js` and all 15 `model.js` files have now been compared with upstream at the code level; the specific rendering and calculation differences are documented in this register and `IMAGE_AUDIT.md`. This is source-lineage evidence, not a count of distinct visuals.

Retain the upstream copyright and MIT licence notice in distributed copies/substantial portions. The MIT grant covers the upstream software as licensed; any separately embedded third-party assets, if identified, require their own rights review.


## Asset record template

Copy this block for each integrated asset:

```markdown
## Image: [descriptive asset title]

- Visual ID: [stable subject-level ID]
- Chapter: [chapter number and title]
- Source relationship: [Inherited unchanged / Inherited adapted / New independent / Unknown — evidence]
- Category: [A / B / C / PENDING]
- Learning objective: [what the learner should understand]
- File: [repository-relative path]
- Original source: [canonical item/page URL]
- Author / creator: [name, or "not stated"]
- License: [exact licence and version]
- License URL: [URL]
- Access date: [YYYY-MM-DD]
- RU caption: [Russian caption]
- EN caption: [English caption]
- Alt RU: [concise meaningful Russian alternative text]
- Alt EN: [concise meaningful English alternative text]
- Modified: [No / Yes — describe crop, translation, labels or other changes]
- Scientific review: [Reviewed / Pending — reviewer and concise notes]
- Rights review: [Verified / Pending — evidence or unresolved condition]
- Integration: [page/component where displayed]
- Mobile check: [Passed / Pending]
```

## Visual requirement review

Record a requirement here before starting a search. Move it to the integrated-asset section only after all checks are complete.

| Chapter / Visual ID | Required visual | Search / review status | Reason unresolved | Next action |
|---|---|---|---|---|
| 04 — Work and Energy | Force direction and displacement; energy comparison; height-dependent potential energy | Three local implementations are present (inline SVG, canvas plot, Three.js scene); source lineage and item-level rights are still pending | The visuals may be suitable as local explanatory models, but the current evidence does not prove independent authorship or clear all inherited content rights | Map each implementation to upstream source; complete A/B/C classification and rights review before marking VERIFIED |
| 14 / PHY-14-001 | Four-topic infographic: straight wire (concentric field, B = μ₀I/2πr), circular loop (axis field and centre value), solenoid (nearly uniform interior field), and toroid (field mainly inside the core); current and B directions, right-hand rule, units, and idealisation limits | **MISSING** — a descriptive placeholder is present in `chapters/magnetism.html`; no image is integrated | Image generation is currently unavailable; the placeholder is not visual coverage and no item-specific source/licence has been approved | Search for a suitable rights-cleared scientific visual first; otherwise prepare a bilingual independent diagram when authoring capacity is available |
| 15.1 / PHY-15-001 | Magnet and coil: increasing/decreasing magnetic flux, induced current, field direction, and Lenz's law | **MISSING** — placeholder present in `chapters/induction.html`; no image integrated | Need a clear paired comparison of approach/withdrawal without implying that induced current directly opposes magnet motion | Search for a reusable scientific diagram; verify flux and current directions, then localise captions/alt text |
| 15.2 / PHY-15-002 | Moving conducting rod on rails in a uniform magnetic field; mutually perpendicular geometry, charge separation, motional EMF, and closed/open circuit cases | **MISSING** — placeholder present in `chapters/induction.html`; no image integrated | The geometry and cross-product direction must be unambiguous; placeholder does not count as an integrated visual | Search for a reusable diagram or prepare a precise bilingual schematic; verify `B`, `v`, rod orientation, force and current directions |
| 15.3 / PHY-15-003 | Self-induction law; separate RL rise/decay curves with τ = L/R; LC charge/current oscillations with ω = 1/√(LC); energy exchange, labelled axes, units, and initial conditions | **MISSING** — placeholder present in `chapters/induction.html`; no image integrated | Several related concepts must be represented without conflating the RL transient with LC oscillations | Search for suitable separate diagrams/plots or prepare a bilingual composite; validate curves and initial conditions |

## Interactive 3D scene inventory — Chapters 03, 05, 11–15

This is a scene-level source-lineage index for the interactive-book scenes. It is not a claim that the scenes have passed manual visual review, item-level rights review, or final accessibility verification. Each scene is inherited from the upstream module and has Russian-localised in-scene names/labels; classify the affected rendered scene output as **B — Adapted**. The 3D geometry and executable scene construction were retained in the compared sections.

| Visual ID | Chapter / page | Scene key | Local source | Upstream source | Status |
|---|---|---|---|---|---|
| PHY-03-3D-01 | 03 — 3 — Движение по окружности | `whirl` | `original-engine/circular/world.js` | `circular/world.js` | INTEGRATED / visual review pending |
| PHY-03-3D-02 | 3.1 — Центростремительная сила | `double` | `original-engine/circular/world.js` | `circular/world.js` | INTEGRATED / visual review pending |
| PHY-03-3D-03 | 3.2 — Автомобиль на повороте | `flatcar` | `original-engine/circular/world.js` | `circular/world.js` | INTEGRATED / visual review pending |
| PHY-03-3D-04 | 3.3 — Конический маятник | `cone` | `original-engine/circular/world.js` | `circular/world.js` | INTEGRATED / visual review pending |
| PHY-03-3D-05 | 3.4 — Движение по вертикальной окружности | `loop` | `original-engine/circular/world.js` | `circular/world.js` | INTEGRATED / visual review pending |
| PHY-03-3D-06 | 3.5 — Виражи | `bank` | `original-engine/circular/world.js` | `circular/world.js` | INTEGRATED / visual review pending |
| PHY-03-3D-07 | 3.6 — Угловая скорость | `disc` | `original-engine/circular/world.js` | `circular/world.js` | INTEGRATED / visual review pending |
| PHY-03-3D-08 | 3.7 — Закон всемирного тяготения | `gravity` | `original-engine/circular/world.js` | `circular/world.js` | INTEGRATED / visual review pending |
| PHY-03-3D-09 | 3.8 — Орбиты | `orbit` | `original-engine/circular/world.js` | `circular/world.js` | INTEGRATED / visual review pending |
| PHY-03-3D-10 | 3.9 — Эллиптические орбиты | `kepler` | `original-engine/circular/world.js` | `circular/world.js` | INTEGRATED / visual review pending |
| PHY-03-3D-11 | 3.10 — Энергия на орбите | `orbitE` | `original-engine/circular/world.js` | `circular/world.js` | INTEGRATED / visual review pending |
| PHY-03-3D-12 | 3.11 · AP Physics C — Потенциальная энергия | `well` | `original-engine/circular/world.js` | `circular/world.js` | INTEGRATED / visual review pending |
| PHY-03-3D-13 | 3.12 · AP Physics C — Вторая космическая скорость | `escape` | `original-engine/circular/world.js` | `circular/world.js` | INTEGRATED / visual review pending |
| PHY-05-3D-01 | 05 — 5 — Импульс тела | `mom` | `original-engine/momentum/world.js` | `momentum/world.js` | INTEGRATED / visual review pending |
| PHY-05-3D-02 | 5.1 — Импульс силы | `wall` | `original-engine/momentum/world.js` | `momentum/world.js` | INTEGRATED / visual review pending |
| PHY-05-3D-03 | 5.2 — Меньшая сила | `eggs` | `original-engine/momentum/world.js` | `momentum/world.js` | INTEGRATED / visual review pending |
| PHY-05-3D-04 | 5.3 — Закон сохранения импульса | `stick` | `original-engine/momentum/world.js` | `momentum/world.js` | INTEGRATED / visual review pending |
| PHY-05-3D-05 | 5.4 — Упругие столкновения | `bounce` | `original-engine/momentum/world.js` | `momentum/world.js` | INTEGRATED / visual review pending |
| PHY-05-3D-06 | 5.5 — Взрыв | `burst` | `original-engine/momentum/world.js` | `momentum/world.js` | INTEGRATED / visual review pending |
| PHY-05-3D-07 | 5.6 — Баллистический маятник | `pend` | `original-engine/momentum/world.js` | `momentum/world.js` | INTEGRATED / visual review pending |
| PHY-05-3D-08 | 5.7 — Движение в двух измерениях | `crash` | `original-engine/momentum/world.js` | `momentum/world.js` | INTEGRATED / visual review pending |
| PHY-05-3D-09 | 5.8 — Центр масс | `shell` | `original-engine/momentum/world.js` | `momentum/world.js` | INTEGRATED / visual review pending |
| PHY-05-3D-10 | 5.9 · AP Physics C — Сплошные тела | `rods` | `original-engine/momentum/world.js` | `momentum/world.js` | INTEGRATED / visual review pending |
| PHY-05-3D-11 | 5.10 · AP Physics C — Пластины | `plates` | `original-engine/momentum/world.js` | `momentum/world.js` | INTEGRATED / visual review pending |
| PHY-05-3D-12 | 5.11 · AP Physics C — Составные тела и отверстия | `parts` | `original-engine/momentum/world.js` | `momentum/world.js` | INTEGRATED / visual review pending |
| PHY-11-3D-01 | 11 — 11 — Потенциальная энергия электрического взаимодействия | `pair` | `original-engine/potential/world.js` | `potential/world.js` | INTEGRATED / visual review pending |
| PHY-11-3D-02 | 11.1 — Сборка системы зарядов | `square` | `original-engine/potential/world.js` | `potential/world.js` | INTEGRATED / visual review pending |
| PHY-11-3D-03 | 11.2 — Электрический потенциал | `uniform` | `original-engine/potential/world.js` | `potential/world.js` | INTEGRATED / visual review pending |
| PHY-11-3D-04 | 11.3 — Потенциальный рельеф | `hill` | `original-engine/potential/world.js` | `potential/world.js` | INTEGRATED / visual review pending |
| PHY-11-3D-05 | 11.4 — Электрический диполь | `dipole` | `original-engine/potential/world.js` | `potential/world.js` | INTEGRATED / visual review pending |
| PHY-11-3D-06 | 11.5 — Заряженный стержень | `rod` | `original-engine/potential/world.js` | `potential/world.js` | INTEGRATED / visual review pending |
| PHY-11-3D-07 | 11.6 — Кольцо, дуга и диск | `ring` | `original-engine/potential/world.js` | `potential/world.js` | INTEGRATED / visual review pending |
| PHY-11-3D-08 | 11.7 — Заряженные сферы | `spheres` | `original-engine/potential/world.js` | `potential/world.js` | INTEGRATED / visual review pending |
| PHY-11-3D-09 | 11.8 — Электрон-вольт | `accel` | `original-engine/potential/world.js` | `potential/world.js` | INTEGRATED / visual review pending |
| PHY-12-3D-01 | 12 — 12 — Конденсаторы | `plates` | `original-engine/capacitors/world.js` | `capacitors/world.js` | INTEGRATED / visual review pending |
| PHY-12-3D-02 | 12.1 — Плоский конденсатор | `gap` | `original-engine/capacitors/world.js` | `capacitors/world.js` | INTEGRATED / visual review pending |
| PHY-12-3D-03 | 12.2 — Две сферы | `sphere` | `original-engine/capacitors/world.js` | `capacitors/world.js` | INTEGRATED / visual review pending |
| PHY-12-3D-04 | 12.3 — Два цилиндра | `coax` | `original-engine/capacitors/world.js` | `capacitors/world.js` | INTEGRATED / visual review pending |
| PHY-12-3D-05 | 12.4 — Запасённая энергия | `energy` | `original-engine/capacitors/world.js` | `capacitors/world.js` | INTEGRATED / visual review pending |
| PHY-12-3D-06 | 12.5 — Последовательное и параллельное соединения | `circuits` | `original-engine/capacitors/world.js` | `capacitors/world.js` | INTEGRATED / visual review pending |
| PHY-12-3D-07 | 12.6 — Диэлектрики | `slab` | `original-engine/capacitors/world.js` | `capacitors/world.js` | INTEGRATED / visual review pending |
| PHY-12-3D-08 | 12.7 — Подключён или отключён | `compare` | `original-engine/capacitors/world.js` | `capacitors/world.js` | INTEGRATED / visual review pending |
| PHY-12-3D-09 | 12.8 — Проводники | `conductor` | `original-engine/capacitors/world.js` | `capacitors/world.js` | INTEGRATED / visual review pending |
| PHY-13-3D-01 | 13 — 13 — Электрический ток | `wire` | `original-engine/circuits/world.js` | `circuits/world.js` | INTEGRATED / visual review pending |
| PHY-13-3D-02 | 13.1 — Сопротивление | `wires` | `original-engine/circuits/world.js` | `circuits/world.js` | INTEGRATED / visual review pending |
| PHY-13-3D-03 | 13.2 — Закон Ома | `ohm` | `original-engine/circuits/world.js` | `circuits/world.js` | INTEGRATED / visual review pending |
| PHY-13-3D-04 | 13.3 — Мощность | `bulb` | `original-engine/circuits/world.js` | `circuits/world.js` | INTEGRATED / visual review pending |
| PHY-13-3D-05 | 13.4 — ЭДС | `cell` | `original-engine/circuits/world.js` | `circuits/world.js` | INTEGRATED / visual review pending |
| PHY-13-3D-06 | 13.5 — Последовательное и параллельное соединения | `sp` | `original-engine/circuits/world.js` | `circuits/world.js` | INTEGRATED / visual review pending |
| PHY-13-3D-07 | 13.6 — Смешанные соединения | `combo` | `original-engine/circuits/world.js` | `circuits/world.js` | INTEGRATED / visual review pending |
| PHY-13-3D-08 | 13.7 — Правила Кирхгофа | `kirch` | `original-engine/circuits/world.js` | `circuits/world.js` | INTEGRATED / visual review pending |
| PHY-13-3D-09 | 13.8 — RC-цепи | `rc` | `original-engine/circuits/world.js` | `circuits/world.js` | INTEGRATED / visual review pending |
| PHY-14-3D-01 | 14 — Magnetism | `magnet` | `original-engine/magnetism/world.js` | `magnetism/world.js` | INTEGRATED / visual review pending |
| PHY-14-3D-02 | 14.1 — Magnetic force | `rhr` | `original-engine/magnetism/world.js` | `magnetism/world.js` | INTEGRATED / visual review pending |
| PHY-14-3D-03 | 14.2 — Circular motion in a field | `cyclo` | `original-engine/magnetism/world.js` | `magnetism/world.js` | INTEGRATED / visual review pending |
| PHY-14-3D-04 | 14.3 — Crossed electric and magnetic fields | `selector` | `original-engine/magnetism/world.js` | `magnetism/world.js` | INTEGRATED / visual review pending |
| PHY-14-3D-05 | 14.4 — Force on a current and torque on a loop | `loop` | `original-engine/magnetism/world.js` | `magnetism/world.js` | INTEGRATED / visual review pending |
| PHY-14-3D-06 | 14.5 — Ampère's law | `ampere` | `original-engine/magnetism/world.js` | `magnetism/world.js` | INTEGRATED / visual review pending |
| PHY-14-3D-07 | 14.6 — Biot–Savart law | `ring` | `original-engine/magnetism/world.js` | `magnetism/world.js` | INTEGRATED / visual review pending |
| PHY-14-3D-08 | 14.7 — Parallel wires | `wires` | `original-engine/magnetism/world.js` | `magnetism/world.js` | INTEGRATED / visual review pending |
| PHY-14-3D-09 | 14.8 — Solenoids and toroids | `solenoid` | `original-engine/magnetism/world.js` | `magnetism/world.js` | INTEGRATED / visual review pending |
| PHY-15-3D-01 | 15 — Electromagnetic induction | `flux` | `original-engine/induction/world.js` | `induction/world.js` | INTEGRATED / visual review pending |
| PHY-15-3D-02 | 15.1 — Lenz's law | `lenz` | `original-engine/induction/world.js` | `induction/world.js` | INTEGRATED / visual review pending |
| PHY-15-3D-03 | 15.2 — Mutual induction | `mutual` | `original-engine/induction/world.js` | `induction/world.js` | INTEGRATED / visual review pending |
| PHY-15-3D-04 | 15.3 — Loop near a current-carrying wire | `wire` | `original-engine/induction/world.js` | `induction/world.js` | INTEGRATED / visual review pending |
| PHY-15-3D-05 | 15.4 — Motional EMF | `bar` | `original-engine/induction/world.js` | `induction/world.js` | INTEGRATED / visual review pending |
| PHY-15-3D-06 | 15.5 — Loop crossing a magnetic-field boundary | `crossing` | `original-engine/induction/world.js` | `induction/world.js` | INTEGRATED / visual review pending |
| PHY-15-3D-07 | 15.6 — Rod on rails | `rails` | `original-engine/induction/world.js` | `induction/world.js` | INTEGRATED / visual review pending |
| PHY-15-3D-08 | 15.7 — Inductance | `solenoid` | `original-engine/induction/world.js` | `induction/world.js` | INTEGRATED / visual review pending |
| PHY-15-3D-09 | 15.8 — RL circuits | `rl` | `original-engine/induction/world.js` | `induction/world.js` | INTEGRATED / visual review pending |
| PHY-15-3D-10 | 15.9 — LC oscillations | `lc` | `original-engine/induction/world.js` | `induction/world.js` | INTEGRATED / visual review pending |

**Review still required for all 71 indexed entries:** confirm rendered geometry at desktop/mobile sizes, inspect scene labels and their contrast, verify the canvas/scene accessible name and keyboard picker announcement, add complete RU/EN descriptions where needed, and retain asset-level rights evidence for any embedded non-code components. The scene index does not include the four missing static infographic requirements listed above.

## Integrated assets

## Chapter 04 visual records — source lineage pending

### Chapter 04 — Force and displacement diagram
- Chapter: 04 — Work and Energy
- Learning objective: Show the angle between a constant force and displacement, and identify the force component that contributes to mechanical work
- File: chapters/work-energy.html (inline SVG in the section “1. Механическая работа”)
- Local implementation: Inline SVG in `chapters/work-energy.html`; source relationship to the upstream work has not yet been established. Do not treat it as independently authored.
- Author / creator: **PENDING** — compare against the English source; do not infer authorship from the in-repository SVG implementation
- Source-work attribution: Nathan Liow (inherited source attribution; exact figure-level lineage pending)
- Licence / permission: **Unknown / PENDING** for the inherited source and Russian derivative use
- Licence evidence: **PENDING** — repository-level MIT licence is not sufficient evidence for inherited source material
- Checked date: 2026-11-05
- RU caption: Работа совершается составляющей силы вдоль перемещения: F cos α
- EN caption: The component of force along the displacement is F cos α
- Alt RU: Ящик перемещается горизонтально вправо; сила направлена вверх под углом α, её горизонтальная составляющая F cos α показана отдельно
- Alt EN: A box moves horizontally to the right; the applied force points upward at angle α, with its horizontal component F cos α shown separately
- Modified: **Unknown / PENDING** — compare visual content with the upstream/source material before classifying A, B, or C.
- Scientific review: Formula and vector geometry correspond to A = Fs cos α; included as a schematic, not to scale
- Rights review: **PENDING** — the repository MIT licence alone does not establish the right to reproduce or adapt inherited source visuals
- Integration: chapters/work-energy.html, immediately below the work formula
- Mobile check: Verified in GitHub Actions browser smoke on 2026-11-04 at 390×844; the force-and-displacement SVG is present in the responsive chapter, with zero serious/critical axe violations and no horizontal page overflow.


### Chapter 04 — Energy comparison plot
- Chapter: 04 — Work and Energy
- Learning objective: Compare kinetic, gravitational potential and total mechanical energy as mass, speed and height change
- File: `chapters/work-energy.html`
- Local implementation: JavaScript canvas drawing (`draw()`) in `chapters/work-energy.html`; source relationship to the upstream/source material has not yet been established.
- Author / creator: **PENDING** — compare the scene and code lineage with the English source before attributing authorship
- Source-work attribution: Nathan Liow (inherited source attribution; exact figure/scene lineage pending)
- Licence / permission: **Unknown / PENDING** for inherited source and derivative use
- Licence evidence: **PENDING** — repository-level MIT licence does not establish rights in inherited educational content
- Checked date: 2026-11-05
- RU caption: Сравнение кинетической, потенциальной и суммарной энергии
- EN caption: Comparison of kinetic, potential and total energy
- Alt RU: Столбчатая диаграмма трёх значений энергии, пересчитываемых при изменении массы, скорости и высоты
- Alt EN: Bar chart of three energy values recalculated when mass, speed and height change
- Modified: **PENDING source mapping** — chart is generated from equations, but the implementation and educational visual lineage still need comparison.
- Scientific review: Formula-based; browser smoke confirmed live recalculation, chart rendering and slider interaction on desktop and mobile.
- Rights review: **PENDING** — source lineage and any inherited/third-party components must be checked before claiming rights clearance
- Integration: Interactive model in `chapters/work-energy.html`
- Mobile check: Verified in GitHub Actions on 2026-11-04 at 390×844; the canvas chart / WebGL scene rendered without horizontal page overflow.

### Chapter 04 — Three-dimensional energy scene
- Chapter: 04 — Work and Energy
- Learning objective: Show an object moving along an inclined plane and relate its height to gravitational potential energy per unit mass
- File: `physics-lab.js`
- Local implementation: Three.js scene in `physics-lab.js`; source relationship to the upstream/source material has not yet been established.
- Author / creator: **Unknown / PENDING** — the code is in the derivative repository, but its relationship to Nathan Liow's upstream scene has not yet been compared line by line; do not infer independent authorship.
- License: Repository-level MIT License is present, with Nathan Liow's copyright notice; applicability to this exact inherited visual and any embedded third-party components remains **PENDING**.
- License URL: https://opensource.org/license/mit/
- Access date: 2026-11-04
- RU caption: Трёхмерная модель движения тела по наклонной поверхности
- EN caption: Three-dimensional model of an object moving along an inclined surface
- Alt RU: Шар на наклонной плоскости; модель предназначена для иллюстрации движения и изменения высоты
- Alt EN: A sphere on an inclined plane; the model illustrates motion and changing height
- Modified: Rendered programmatically with Three.js; this describes the rendering method, not authorship or source lineage.
- Scientific review: Conceptual model; the phase slider moves the sphere down the incline and updates Eп/m = gh. It illustrates the height dependence of potential energy, not a complete quantitative energy-conservation simulation
- Rights review: **PENDING** — confirm source lineage and whether any separately licensed or third-party components are embedded; repository-level MIT notice alone is not a visual-by-visual rights determination.
- Integration: Shared 3D laboratory component in `chapters/work-energy.html`
- Mobile check: Verified in GitHub Actions on 2026-11-04 at 390×844; the canvas chart / WebGL scene rendered without horizontal page overflow.

No third-party external image is currently claimed as integrated for Chapter 04. However, this does not establish that the listed SVG, canvas plot, or Three.js scene are independently authored in the Russian derivative. Their source lineage and rights basis remain pending comparison with the English atlas. Do not count them as Category C or rights-cleared until that comparison is complete.
