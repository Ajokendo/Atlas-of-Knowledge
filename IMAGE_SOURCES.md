# Physics — IMAGE_SOURCES

This register documents every visual asset integrated into the Physics atlas. Add one complete record per asset. Do not list search results or unverified candidates as integrated.

## Reporting metrics

Update these counts for each progress report. Count only assets that are both integrated into a chapter/page and documented below.

| Metric | Count | Counting rule |
|---|---:|---|
| Found and integrated | 0 | External assets with verified scientific accuracy, licence and attribution |
| Independently created — authored SVG/HTML/CSS | 1 | Original force-and-displacement diagram in Chapter 04 |
| Independently created — code-generated plots | 1 | Plots generated from verified equations/data; Chapter 04 energy comparison canvas |
| Independently created — interactive JS/WebGL models | 1 | Programmatic Three.js model registered for Chapter 04 |
| Independently created — AI-generated images | 0 | Generated images that passed scientific review |
| Outstanding | 0 required visuals identified | Chapter 04 visual objectives are covered by the original force diagram, energy plot and interactive 3D model; final responsive/browser verification remains tracked in CI |

**Counting note:** the counts above cover only assets registered in this file. They do not claim that the entire repository contains no other visual assets. Do not count an asset until its provenance and integration have been checked.

## Asset record template

Copy this block for each integrated asset:

```markdown
## Image: [descriptive asset title]

- Chapter: [chapter number and title]
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
- Author / creator: Atlas of Knowledge project contribution
- License: MIT License (repository LICENSE; copyright notice retained)
- License URL: https://opensource.org/license/mit/
- Access date: 2026-11-04
- RU caption: Работа совершается составляющей силы вдоль перемещения: F cos α
- EN caption: The component of force along the displacement is F cos α
- Alt RU: Ящик перемещается горизонтально вправо; сила направлена вверх под углом α, её горизонтальная составляющая F cos α показана отдельно
- Alt EN: A box moves horizontally to the right; the applied force points upward at angle α, with its horizontal component F cos α shown separately
- Modified: Original SVG; no external asset modified
- Scientific review: Formula and vector geometry correspond to A = Fs cos α; included as a schematic, not to scale
- Rights review: Verified against repository MIT licence; retain copyright and licence notice when redistributing
- Integration: chapters/work-energy.html, immediately below the work formula
- Mobile check: Verified in GitHub Actions browser smoke on 2026-11-04 at 390×844; the force-and-displacement SVG is present in the responsive chapter, with zero serious/critical axe violations and no horizontal page overflow.


### Chapter 04 — Energy comparison plot
- Chapter: 04 — Work and Energy
- Learning objective: Compare kinetic, gravitational potential and total mechanical energy as mass, speed and height change
- File: `chapters/work-energy.html`
- Original source: Original in-repository JavaScript canvas drawing (`draw()`); no external image source
- Author / creator: Atlas of Knowledge repository code; individual author not specified in file
- License: MIT License (repository LICENSE; copyright notice retained)
- License URL: https://opensource.org/license/mit/
- Access date: 2026-11-04
- RU caption: Сравнение кинетической, потенциальной и суммарной энергии
- EN caption: Comparison of kinetic, potential and total energy
- Alt RU: Столбчатая диаграмма трёх значений энергии, пересчитываемых при изменении массы, скорости и высоты
- Alt EN: Bar chart of three energy values recalculated when mass, speed and height change
- Modified: No external asset; generated dynamically from the chapter's equations
- Scientific review: Formula-based; browser smoke confirmed live recalculation, chart rendering and slider interaction on desktop and mobile.
- Rights review: No third-party image rights involved; repository MIT licence applies and attribution notice must be retained
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

No third-party external image is currently claimed as integrated for Chapter 04. External imagery was not added because the original vector diagram, equation-driven plot and interactive scene directly address the chapter's visual learning objectives. These are counted separately as authored/code-generated visuals, not as found internet images.
