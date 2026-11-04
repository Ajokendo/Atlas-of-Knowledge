# Physics — IMAGE_SOURCES

This register documents every visual asset integrated into the Physics atlas. Add one complete record per asset. Do not list search results or unverified candidates as integrated.

## Reporting metrics

Update these counts for each progress report. Count only assets that are both integrated into a chapter/page and documented below.

| Metric | Count | Counting rule |
|---|---:|---|
| Found and integrated | 0 | External assets with verified scientific accuracy, licence and attribution |
| Independently created — authored SVG/HTML/CSS | 0 | Original diagrams authored directly for the atlas |
| Independently created — code-generated plots | 1 | Plots generated from verified equations/data; Chapter 04 energy comparison canvas |
| Independently created — interactive JS/WebGL models | 1 | Programmatic Three.js model registered for Chapter 04 |
| Independently created — AI-generated images | 0 | Generated images that passed scientific review |
| Outstanding | Not yet audited | Required visuals not yet resolved and integrated |

**Important:** the zeroes above are initial register values, not a claim that the entire repository contains no visual assets. Existing assets must be audited before the counts can be considered complete. Do not count an asset until its provenance and integration have been checked.

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

## Outstanding visual requirements

Record a requirement here before starting a search. Move it to the integrated-asset section only after all checks are complete.

| Chapter | Required visual | Search / review status | Reason unresolved | Next action |
|---|---|---|---|---|
| 04 — Work and Energy | Energy-conversion model and energy comparison plot | Partially audited; in-repository code visuals registered below | External image requirement not established; visual completeness and mobile/browser behaviour still need review | Continue the scene audit; only search external imagery if a specific learning objective needs it |

## Integrated assets

## Independently created visuals

### Chapter 04 — Energy comparison plot
- Chapter: 04 — Work and Energy
- Learning objective: Compare kinetic, gravitational potential and total mechanical energy as mass, speed and height change
- File: `chapters/work-energy.html`
- Original source: Original in-repository JavaScript canvas drawing (`draw()`); no external image source
- Author / creator: Atlas of Knowledge repository code; individual author not specified in file
- License: Repository licence applies; verify repository-level licence before reuse outside this project
- License URL: Not applicable to an internally authored code visual
- Access date: 2026-11-04
- RU caption: Сравнение кинетической, потенциальной и суммарной энергии
- EN caption: Comparison of kinetic, potential and total energy
- Alt RU: Столбчатая диаграмма трёх значений энергии, пересчитываемых при изменении массы, скорости и высоты
- Alt EN: Bar chart of three energy values recalculated when mass, speed and height change
- Modified: No external asset; generated dynamically from the chapter's equations
- Scientific review: Formula-based; automated browser/interaction verification pending
- Rights review: No third-party image rights involved; repository code provenance recorded
- Integration: Interactive model in `chapters/work-energy.html`
- Mobile check: Pending

### Chapter 04 — Three-dimensional energy scene
- Chapter: 04 — Work and Energy
- Learning objective: Provide a spatial representation of motion on a slope while introducing energy transformation
- File: `physics-lab.js`
- Original source: Original in-repository Three.js scene code; no external image source
- Author / creator: Atlas of Knowledge repository code; individual author not specified in file
- License: Repository licence applies; verify repository-level licence before reuse outside this project
- License URL: Not applicable to an internally authored code visual
- Access date: 2026-11-04
- RU caption: Трёхмерная модель движения тела по наклонной поверхности
- EN caption: Three-dimensional model of an object moving along an inclined surface
- Alt RU: Шар на наклонной плоскости; модель предназначена для иллюстрации движения и изменения высоты
- Alt EN: A sphere on an inclined plane; the model illustrates motion and changing height
- Modified: No external asset; rendered programmatically with Three.js
- Scientific review: Conceptual model; relationship between slider, object position and displayed energy quantity needs further validation
- Rights review: No third-party image rights involved; repository code provenance recorded
- Integration: Shared 3D laboratory component in `chapters/work-energy.html`
- Mobile check: Pending

No third-party external image is currently claimed as integrated for Chapter 04. The model and plot above are counted separately as code-generated visuals, not as found internet images.
