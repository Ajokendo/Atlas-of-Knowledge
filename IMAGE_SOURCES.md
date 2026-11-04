# Physics — IMAGE_SOURCES

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

Initial file-level comparisons have confirmed this relationship for:
- Energy: `original-engine/energy/pages.js` ↔ upstream `energy/pages.js`
- Magnetism: `original-engine/magnetism/pages.js` ↔ upstream `magnetism/pages.js`
- Induction: `original-engine/induction/pages.js` ↔ upstream `induction/pages.js`

The Russian `pages.js` files translate chart/SVG labels, axis units, captions, and accessible names; the affected visual outputs are therefore Category B (adapted). The corresponding `world.js` and `model.js` files differ from upstream and require line-level review before final classification. This is a source-lineage note, not a count of distinct visuals.

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

| Chapter | Required visual | Search / review status | Reason unresolved | Next action |
|---|---|---|---|---|
| 04 — Work and Energy | Force direction and displacement; energy comparison; height-dependent potential energy | Resolved with original SVG, code-generated plot and interactive 3D scene; no external image required | No specific learning objective requires a third-party photograph or illustration; original visuals communicate the relevant vectors and equations directly | Keep responsive/accessibility verification in CI; reopen only if classroom feedback identifies a visual gap |

## Integrated assets

## Independently created visuals

### Chapter 04 — Force and displacement diagram
- Chapter: 04 — Work and Energy
- Learning objective: Show the angle between a constant force and displacement, and identify the force component that contributes to mechanical work
- File: chapters/work-energy.html (inline SVG in the section “1. Механическая работа”)
- Original source: Original SVG authored directly in the chapter; no external source
- Author / creator: **PENDING** — compare against the English source; do not infer authorship from the in-repository SVG implementation
- Source-work attribution: Nathan Liow (inherited source attribution; exact figure-level lineage pending)
- Licence / permission: **Unknown / PENDING** for the inherited source and Russian derivative use
- Licence evidence: **PENDING** — repository-level MIT licence is not sufficient evidence for inherited source material
- Checked date: 2026-11-05
- RU caption: Работа совершается составляющей силы вдоль перемещения: F cos α
- EN caption: The component of force along the displacement is F cos α
- Alt RU: Ящик перемещается горизонтально вправо; сила направлена вверх под углом α, её горизонтальная составляющая F cos α показана отдельно
- Alt EN: A box moves horizontally to the right; the applied force points upward at angle α, with its horizontal component F cos α shown separately
- Modified: Original SVG; no external asset modified
- Scientific review: Formula and vector geometry correspond to A = Fs cos α; included as a schematic, not to scale
- Rights review: **PENDING** — the repository MIT licence alone does not establish the right to reproduce or adapt inherited source visuals
- Integration: chapters/work-energy.html, immediately below the work formula
- Mobile check: Verified in GitHub Actions browser smoke on 2026-11-04 at 390×844; the force-and-displacement SVG is present in the responsive chapter, with zero serious/critical axe violations and no horizontal page overflow.


### Chapter 04 — Energy comparison plot
- Chapter: 04 — Work and Energy
- Learning objective: Compare kinetic, gravitational potential and total mechanical energy as mass, speed and height change
- File: `chapters/work-energy.html`
- Original source: Original in-repository JavaScript canvas drawing (`draw()`); no external image source
- Author / creator: **PENDING** — compare the scene and code lineage with the English source before attributing authorship
- Source-work attribution: Nathan Liow (inherited source attribution; exact figure/scene lineage pending)
- Licence / permission: **Unknown / PENDING** for inherited source and derivative use
- Licence evidence: **PENDING** — repository-level MIT licence does not establish rights in inherited educational content
- Checked date: 2026-11-05
- RU caption: Сравнение кинетической, потенциальной и суммарной энергии
- EN caption: Comparison of kinetic, potential and total energy
- Alt RU: Столбчатая диаграмма трёх значений энергии, пересчитываемых при изменении массы, скорости и высоты
- Alt EN: Bar chart of three energy values recalculated when mass, speed and height change
- Modified: No external asset; generated dynamically from the chapter's equations
- Scientific review: Formula-based; browser smoke confirmed live recalculation, chart rendering and slider interaction on desktop and mobile.
- Rights review: **PENDING** — source lineage and any inherited/third-party components must be checked before claiming rights clearance
- Integration: Interactive model in `chapters/work-energy.html`
- Mobile check: Verified in GitHub Actions on 2026-11-04 at 390×844; the canvas chart / WebGL scene rendered without horizontal page overflow.

### Chapter 04 — Three-dimensional energy scene
- Chapter: 04 — Work and Energy
- Learning objective: Show an object moving along an inclined plane and relate its height to gravitational potential energy per unit mass
- File: `physics-lab.js`
- Original source: Original in-repository Three.js scene code; no external image source
- Author / creator: Atlas of Knowledge repository code; individual author not specified in file
- License: MIT License (repository LICENSE; copyright notice retained)
- License URL: https://opensource.org/license/mit/
- Access date: 2026-11-04
- RU caption: Трёхмерная модель движения тела по наклонной поверхности
- EN caption: Three-dimensional model of an object moving along an inclined surface
- Alt RU: Шар на наклонной плоскости; модель предназначена для иллюстрации движения и изменения высоты
- Alt EN: A sphere on an inclined plane; the model illustrates motion and changing height
- Modified: No external asset; rendered programmatically with Three.js
- Scientific review: Conceptual model; the phase slider moves the sphere down the incline and updates Eп/m = gh. It illustrates the height dependence of potential energy, not a complete quantitative energy-conservation simulation
- Rights review: No third-party image rights involved; repository MIT licence applies and attribution notice must be retained
- Integration: Shared 3D laboratory component in `chapters/work-energy.html`
- Mobile check: Verified in GitHub Actions on 2026-11-04 at 390×844; the canvas chart / WebGL scene rendered without horizontal page overflow.

No third-party external image is currently claimed as integrated for Chapter 04. However, this does not establish that the listed SVG, canvas plot, or Three.js scene are independently authored in the Russian derivative. Their source lineage and rights basis remain pending comparison with the English atlas. Do not count them as Category C or rights-cleared until that comparison is complete.
