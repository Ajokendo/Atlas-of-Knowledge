# Physics — IMAGE_SOURCES

- Applicable universal standard: [`IMAGE-FIRST POLICY v1.1`](https://github.com/Ajokendo/Atlas-of-Knowledge/blob/main/IMAGE_FIRST_POLICY.md) (`AOK-IMG-001`).
- Working branch: `workspace/physics`.
- Physics-owned asset directory on this subject branch: `assets/visuals/` (not a shared cross-subject asset folder).
- Upstream comparison snapshot: [Nathan Liow / Atlas of Physics, commit `bcd67d9b75425f4a78f5c7c1d17a2d0614727309`](https://github.com/nathanliow/atlas-of-physics/commit/bcd67d9b75425f4a78f5c7c1d17a2d0614727309) (2026-10-30).

This register documents every visual asset integrated into the Physics atlas. Add one complete record per asset. Do not list search results or unverified candidates as integrated.

## Reporting metrics — provisional during source-lineage audit

The Physics branch is a derivative Russian-language edition of Nathan Liow's pre-existing English atlas. The current three Chapter 04 records describe implementation forms found in this branch; they do **not yet prove** that those visuals were independently authored here.

| Metric | Count | Counting rule |
|---|---:|---|
| Image Coverage | PROVISIONAL / NOT CALCULATED | Full deduplicated denominator of required visuals is not established |
| Image Verification | NOT CALCULATED | Count only assets whose required checks are all PASS and lifecycle is VERIFIED |
| Image Gaps | 0 known explicit placeholders; full gap count PENDING | Do not treat zero known placeholders as zero total gaps; finish chapter/scene inventory |
| Inherited visuals mapped to English source | PENDING | Requires source-to-derivative comparison |
| Inherited visuals reused unchanged (A) | PENDING | Count only after visual identity and unchanged status are verified |
| Inherited visuals adapted (B) | PENDING | Count only after the visual-content changes and adaptation rights are checked |
| Genuinely new project-created visuals (C) | 4 integrated | Four new AI-assisted, hand-authored SVG teaching diagrams with four stacked mobile variants (eight SVG files), published under CC BY-NC 4.0; independent external expert review is a separate post-publication activity, not a publication gate |
| Rights / reproduction permission verified | PENDING | Requires evidence for the exact source work and applicable components |
| Russian-edition localisation verified | PENDING | Requires per-visual Russian labels, captions, alt text, descriptions and rendering checks |
| Known visual placeholders | 0 | The four previously specified gaps now have SVG assets integrated; other unrecorded gaps may still emerge during the full inventory |

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


## New project-created vector assets — 2026-11-05

The four known placeholders have been replaced with four original, hand-authored SVG schematics, each with a dedicated mobile layout (eight SVG files total). The SVG markup was produced with AI assistance from the chapter-specific physics briefs; no OpenStax figure or raster artwork was copied. During the 2026-11-05 internal bilingual review, the Chapter 14 desktop/mobile footnotes were clarified to state that the displayed μ₀ formulae assume an air core; linear magnetic-core materials require μ = μ₀μᵣ. The ideal-toroid external-field approximation is explicitly qualified. Internal RU/EN terminology and caption/alt review is PASS. Independent learner-comprehension testing and external subject-matter sign-off are separate follow-up activities, not publication gates. OpenStax pages were searched and consulted as scientific references only. OpenStax textbook content is generally CC BY-NC-SA 4.0; that licence is not applied to these independently created diagrams because no OpenStax artwork or expressive text was adapted. **Project licence decision (approved 2026-11-05): all eight SVG files belonging to PHY-14-001 and PHY-15-001–003 are published under Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0): https://creativecommons.org/licenses/by-nc/4.0/.** This asset-specific licence applies to the extent the project has rights to license the material; it does not claim exclusive copyright in AI-generated elements or override third-party rights if any are later identified. The repository's root MIT licence continues to govern code as stated in its licence; it does not replace this asset-specific licence. Independent external scientific review is a separate post-publication activity and is not required for publication; VERIFIED depends on completion of the internal publication checks.

### PHY-14-001 — Four magnetic-field configurations

- Visual ID: PHY-14-001
- Subject / chapter: Physics, Chapter 14 — Magnetism
- Title: Four magnetic-field configurations
- Integration status: INTEGRATED (not VERIFIED)
- Lifecycle: FOUND → LICENSE_CHECK (**PASS — project publication licence declared, CC BY-NC 4.0**) → SCIENTIFIC_CHECK (**internal review PASS**) → ADAPTED (**N/A — Category C, original independent asset**) → INTEGRATED → VERIFIED (**pending completion of internal publication QA**). External expert review is tracked separately and is not a publication gate.
- Publication verification gate: file/path and integration, internal scientific review, rights/licence evidence, final bilingual/accessibility review, and current desktop/mobile browser/CI evidence must each be PASS before VERIFIED. External expert sign-off is optional follow-up and does not block publication.
- Source relationship: New independent project-created diagram
- Category: C
- Learning objective: Compare field geometry and idealised field-strength relations for a long straight wire, a circular current loop, a long solenoid, and an ideal toroid.
- File: assets/visuals/phy-14-magnetism-four-configurations.svg
- Mobile variant file: assets/visuals/phy-14-magnetism-four-configurations-mobile.svg
- Search record: 2026-11-05; search terms: “magnetic field straight wire circular loop solenoid toroid diagram”, “right-hand rule current field”; searched OpenStax College Physics 2e §22.9 and University Physics Volume 2 §§12.5–12.6 for straight-wire, loop, solenoid, and toroid field geometry, right-hand-rule directions, and equations. Candidate OpenStax diagrams were considered but not reused: the section presents the configurations as separate figures rather than one integrated bilingual teaching plate with all four idealisations and a common right-hand-rule comparison. The new SVG was drawn independently to meet that combined learning need.
- Source page / scientific references: https://openstax.org/books/college-physics-2e/pages/22-9-magnetic-fields-produced-by-currents-amperes-law ; https://openstax.org/books/university-physics-volume-2/pages/12-6-solenoids-and-toroids
- Direct asset URL: Not applicable — original local SVG.
- Creator / rightsholder: AI-assisted SVG authoring with ChatGPT; published by the Atlas of Knowledge project. Project publication licence: CC BY-NC 4.0 (approved 2026-11-05). No claim of exclusive copyright in AI-generated elements.
- Method: Hand-authored vector SVG markup with labels, formulas, and arrow geometry.
- Licence / permission: CC BY-NC 4.0 — https://creativecommons.org/licenses/by-nc/4.0/ (project publication licence approved 2026-11-05; applies to the extent the project has licensable rights).
- Licence evidence: Not applicable to external artwork; no third-party image is embedded.
- Checked/accessed date: 2026-11-05.
- Changes: Original diagram; no source image adapted.
- Attribution: Original AI-assisted vector diagram created for Atlas of Knowledge, 2026. Scientific relations cross-checked against OpenStax references listed in this record; no OpenStax figure reused.
- RU caption: Четыре конфигурации магнитного поля: прямой проводник, круговой виток, соленоид и тороид.
- EN caption: Four magnetic-field configurations: straight wire, circular loop, solenoid, and toroid.
- Alt RU: Четыре схемы магнитного поля с направлениями тока и магнитной индукции, формулами и условиями идеализации.
- Alt EN: Four magnetic-field schematics showing current and magnetic-field directions, equations, and idealisation limits.
- Limitations: Long straight wire; field at the centre of a single circular loop; long-solenoid approximation; ideal toroid approximation. Not to scale.
- Scientific review: Internal second-pass physics review: PASS (2026-11-05) — equations, directions, assumptions and graph relationships checked; identified notation/direction defects corrected in the SVGs. Independent external subject-matter expert review: separate follow-up activity; not a publication gate.
- Rights review: PASS — project publication licence declared as CC BY-NC 4.0; no third-party artwork is embedded. This does not assert exclusive copyright in AI-generated elements.
- Language/accessibility review: PENDING — bilingual labels, captions and alt text present; final visual comprehension review outstanding.
- Integration: chapters/magnetism.html, section “Визуальные материалы главы”.
- Technical review: PASS — desktop 1440×900 and mobile 390×844 browser checks confirm SVG loading, correct responsive source selection, bilingual captions, meaningful alt text, zero horizontal overflow, and axe serious/critical 0 after correcting metric-label contrast (run 42006633285).
- Desktop/mobile check: PASS — 1440×900 and 390×844; responsive SVG source selection, loading, bilingual captions, meaningful alt text, zero horizontal overflow, and axe serious/critical 0 (run 42006633285).

### PHY-15-001 — Lenz's law: approaching and receding magnet

- Visual ID: PHY-15-001
- Subject / chapter: Physics, Chapter 15 — Electromagnetic Induction
- Title: Lenz's law — approaching and receding magnet
- Integration status: INTEGRATED (not VERIFIED)
- Lifecycle: FOUND → LICENSE_CHECK (**PASS — project publication licence declared, CC BY-NC 4.0**) → SCIENTIFIC_CHECK (**internal review PASS**) → ADAPTED (**N/A — Category C, original independent asset**) → INTEGRATED → VERIFIED (**pending completion of internal publication QA**). External expert review is tracked separately and is not a publication gate.
- Publication verification gate: file/path and integration, internal scientific review, rights/licence evidence, final bilingual/accessibility review, and current desktop/mobile browser/CI evidence must each be PASS before VERIFIED. External expert sign-off is optional follow-up and does not block publication.
- Source relationship: New independent project-created diagram
- Category: C
- Learning objective: Distinguish the induced field that opposes increasing flux from the induced field that sustains decreasing flux.
- File: assets/visuals/phy-15-01-lenz-law.svg
- Mobile variant file: assets/visuals/phy-15-01-lenz-law-mobile.svg
- Search record: 2026-11-05; search terms: “Lenz law magnet approaching coil receding magnet induced current”; searched OpenStax University Physics Volume 2 §13.2 and College Physics §23.2 for the approaching/receding north-pole case and induced-current direction. The OpenStax figure was considered but not reused: the selected figure focuses on the approaching magnet, while this requirement needs an explicit paired approach/recession comparison with bilingual direction labels. The two-panel vector schematic was drawn independently.
- Source page / scientific references: https://openstax.org/books/university-physics-volume-2/pages/13-2-lenzs-law ; https://openstax.org/books/college-physics/pages/23-2-faradays-law-of-induction-lenzs-law
- Direct asset URL: Not applicable — original local SVG.
- Creator / rightsholder: AI-assisted SVG authoring with ChatGPT; published by the Atlas of Knowledge project. Project publication licence: CC BY-NC 4.0 (approved 2026-11-05). No claim of exclusive copyright in AI-generated elements.
- Method: Hand-authored vector SVG; paired approach/withdrawal states.
- Licence / permission: CC BY-NC 4.0 — https://creativecommons.org/licenses/by-nc/4.0/ (project publication licence approved 2026-11-05; applies to the extent the project has licensable rights).
- Licence evidence: No third-party artwork embedded.
- Checked/accessed date: 2026-11-05.
- Changes: Original diagram; no source image adapted.
- Attribution: Original AI-assisted vector diagram created for Atlas of Knowledge, 2026; scientific cross-check references are listed in the Physics image register.
- RU caption: Закон Ленца: магнит приближается к катушке и удаляется от неё.
- EN caption: Lenz's law: a magnet approaches and recedes from a coil.
- Alt RU: Два состояния катушки с северным полюсом магнита: при приближении поле катушки направлено против роста потока, при удалении — в сторону исходного поля.
- Alt EN: Two coil states with a north pole facing the coil: the induced field opposes increasing flux during approach and supports the original field during recession.
- Limitations: Assumes the north pole faces the coil and the coil axis is aligned with the magnet; current direction is viewed from the magnet side.
- Scientific review: Internal second-pass physics review: PASS (2026-11-05) — equations, directions, assumptions and graph relationships checked; identified notation/direction defects corrected in the SVGs. Independent external subject-matter expert review: separate follow-up activity; not a publication gate. Lenz-law polarity and flux-change directions were rechecked.
- Rights review: PASS — project publication licence declared as CC BY-NC 4.0; no third-party artwork is embedded. This does not assert exclusive copyright in AI-generated elements.
- Language/accessibility review: PENDING — bilingual captions and alt text present; final visual comprehension review outstanding.
- Integration: chapters/induction.html, visual item 15.1.
- Desktop/mobile check: PASS — 1440×900 and 390×844; responsive SVG source selection, loading, bilingual captions, meaningful alt text, zero horizontal overflow, and axe serious/critical 0 (run 42006633285).

### PHY-15-002 — Motional EMF in a moving rod

- Visual ID: PHY-15-002
- Subject / chapter: Physics, Chapter 15 — Electromagnetic Induction
- Title: Motional EMF in a moving rod
- Integration status: INTEGRATED (not VERIFIED)
- Lifecycle: FOUND → LICENSE_CHECK (**PASS — project publication licence declared, CC BY-NC 4.0**) → SCIENTIFIC_CHECK (**internal review PASS**) → ADAPTED (**N/A — Category C, original independent asset**) → INTEGRATED → VERIFIED (**pending completion of internal publication QA**). External expert review is tracked separately and is not a publication gate.
- Publication verification gate: file/path and integration, internal scientific review, rights/licence evidence, final bilingual/accessibility review, and current desktop/mobile browser/CI evidence must each be PASS before VERIFIED. External expert sign-off is optional follow-up and does not block publication.
- Source relationship: New independent project-created diagram
- Category: C
- Learning objective: Relate mutually perpendicular velocity, magnetic field, rod orientation, charge separation, motional EMF, and the distinction between closed and open circuits.
- File: assets/visuals/phy-15-02-motional-emf-rod.svg
- Mobile variant file: assets/visuals/phy-15-02-motional-emf-rod-mobile.svg
- Search record: 2026-11-05; search terms: “motional EMF rod rails magnetic field open circuit closed circuit”; searched OpenStax College Physics §23.3 and University Physics Volume 2 §13.3 for the moving-rod-on-rails arrangement, polarity, induced current, and magnetic braking force. The OpenStax figure was considered but not reused: it illustrates the moving-rod closed-circuit case, while this requirement also needs a clear open-circuit charge-separation state and explicit q(v × B) geometry. The two circuit states were drawn independently.
- Source page / scientific references: https://openstax.org/books/college-physics/pages/23-3-motional-emf ; https://openstax.org/books/university-physics-volume-2/pages/13-3-motional-emf
- Direct asset URL: Not applicable — original local SVG.
- Creator / rightsholder: AI-assisted SVG authoring with ChatGPT; published by the Atlas of Knowledge project. Project publication licence: CC BY-NC 4.0 (approved 2026-11-05). No claim of exclusive copyright in AI-generated elements.
- Method: Hand-authored vector SVG with explicit right-hand-rule geometry.
- Licence / permission: CC BY-NC 4.0 — https://creativecommons.org/licenses/by-nc/4.0/ (project publication licence approved 2026-11-05; applies to the extent the project has licensable rights).
- Licence evidence: No third-party artwork embedded.
- Checked/accessed date: 2026-11-05.
- Changes: Original diagram; no source image adapted.
- Attribution: Original AI-assisted vector diagram created for Atlas of Knowledge, 2026; scientific cross-check references are listed in the Physics image register.
- RU caption: ЭДС движения: замкнутая и разомкнутая цепи со стержнем на рельсах.
- EN caption: Motional EMF: closed and open circuits with a sliding rod on rails.
- Alt RU: Стержень движется вправо в поле, направленном в плоскость рисунка; положительные заряды смещаются вверх. Показаны ток в замкнутой цепи, тормозящая сила и отсутствие тока в разомкнутой цепи.
- Alt EN: A rod moves right in a field directed into the page; positive charges move upward. The closed circuit shows current and magnetic braking, while the open circuit shows charge separation without current.
- Limitations: Assumes uniform B into the page and mutually perpendicular B, v, and rod; the ideal magnitude is |ε| = BLv.
- Scientific review: Internal second-pass physics review: PASS (2026-11-05) — B/v/rod geometry, q(v×B), charge separation, closed-loop current and magnetic drag checked. Independent external subject-matter expert review: separate follow-up activity; not a publication gate.
- Rights review: PASS — project publication licence declared as CC BY-NC 4.0; no third-party artwork is embedded. This does not assert exclusive copyright in AI-generated elements.
- Language/accessibility review: PENDING — bilingual captions and alt text present; final visual comprehension review outstanding.
- Integration: chapters/induction.html, visual item 15.2.
- Desktop/mobile check: PASS — 1440×900 and 390×844; responsive SVG source selection, loading, bilingual captions, meaningful alt text, zero horizontal overflow, and axe serious/critical 0 (run 42006633285).

### PHY-15-003 — Self-induction, RL transient, and LC oscillations

- Visual ID: PHY-15-003
- Subject / chapter: Physics, Chapter 15 — Electromagnetic Induction
- Title: Self-induction, RL transient, and LC oscillations
- Integration status: INTEGRATED (not VERIFIED)
- Lifecycle: FOUND → LICENSE_CHECK (**PASS — project publication licence declared, CC BY-NC 4.0**) → SCIENTIFIC_CHECK (**internal review PASS**) → ADAPTED (**N/A — Category C, original independent asset**) → INTEGRATED → VERIFIED (**pending completion of internal publication QA**). External expert review is tracked separately and is not a publication gate.
- Publication verification gate: file/path and integration, internal scientific review, rights/licence evidence, final bilingual/accessibility review, and current desktop/mobile browser/CI evidence must each be PASS before VERIFIED. External expert sign-off is optional follow-up and does not block publication.
- Source relationship: New independent project-created diagram
- Category: C
- Learning objective: Separate the self-induction law, exponential current rise/decay in an RL circuit, and ideal energy exchange in an LC circuit.
- File: assets/visuals/phy-15-03-self-induction-rl-lc.svg
- Mobile variant file: assets/visuals/phy-15-03-self-induction-rl-lc-mobile.svg
- Search record: 2026-11-05; search terms: “RL circuit transient current rise decay”, “LC circuit charge current energy exchange”; searched OpenStax University Physics Volume 2 §§14.4–14.5 for RL time constant/current response and LC charge/current/energy relations. The OpenStax RL and LC figures were considered but not reused: they are separate topic figures, while this requirement needs a single bilingual comparison that keeps RL transients distinct from ideal LC oscillations and energy exchange. The composite was drawn independently from the equations.
- Source page / scientific references: https://openstax.org/books/university-physics-volume-2/pages/14-4-rl-circuits ; https://openstax.org/books/university-physics-volume-2/pages/14-5-oscillations-in-an-lc-circuit
- Direct asset URL: Not applicable — original local SVG.
- Creator / rightsholder: AI-assisted SVG authoring with ChatGPT; published by the Atlas of Knowledge project. Project publication licence: CC BY-NC 4.0 (approved 2026-11-05). No claim of exclusive copyright in AI-generated elements.
- Method: Hand-authored vector SVG with original schematic curves and formula labels.
- Licence / permission: CC BY-NC 4.0 — https://creativecommons.org/licenses/by-nc/4.0/ (project publication licence approved 2026-11-05; applies to the extent the project has licensable rights).
- Licence evidence: No third-party artwork embedded.
- Checked/accessed date: 2026-11-05.
- Changes: Original diagram; no source image adapted.
- Attribution: Original AI-assisted vector diagram created for Atlas of Knowledge, 2026; scientific cross-check references are listed in the Physics image register.
- RU caption: Самоиндукция, переходный процесс в RL-цепи и колебания в LC-контуре.
- EN caption: Self-induction, an RL transient, and oscillations in an LC circuit.
- Alt RU: Показаны ЭДС самоиндукции, экспоненциальный рост и спад тока с постоянной времени L/R, а также сдвинутые по фазе заряд и ток и обмен энергией в идеальном LC-контуре.
- Alt EN: The diagram shows self-induced EMF, exponential RL current rise and decay with time constant L/R, and phase-shifted charge/current with energy exchange in an ideal LC circuit.
- Limitations: RL plots are schematic; LC assumes ideal components, zero resistance, constant L and C, and initial conditions q(0)=Q₀ and I(0)=0.
- Scientific review: Internal second-pass physics review: PASS (2026-11-05) — εL, τ=L/R, LC phase/initial conditions and complementary energy curves checked; U_B notation clarified. Independent external subject-matter expert review: separate follow-up activity; not a publication gate.
- Rights review: PASS — project publication licence declared as CC BY-NC 4.0; no third-party artwork is embedded. This does not assert exclusive copyright in AI-generated elements.
- Language/accessibility review: PENDING — bilingual captions and alt text present; final visual comprehension review outstanding.
- Integration: chapters/induction.html, visual item 15.3.
- Desktop/mobile check: PASS — 1440×900 and 390×844; responsive SVG source selection, loading, bilingual captions, meaningful alt text, zero horizontal overflow, and axe serious/critical 0 (run 42006633285).

## Visual requirement review

Record a requirement here before starting a search. Move it to the integrated-asset section only after all checks are complete.

| Chapter / Visual ID | Required visual | Search / review status | Reason unresolved | Next action |
|---|---|---|---|---|
| 04 — Work and Energy | Force direction and displacement; energy comparison; height-dependent potential energy | Three local implementations are present (inline SVG, canvas plot, Three.js scene); source lineage and item-level rights are still pending | The visuals may be suitable as local explanatory models, but the current evidence does not prove independent authorship or clear all inherited content rights | Map each implementation to upstream source; complete A/B/C classification and rights review before marking VERIFIED |
| 14 / PHY-14-001 | Four-topic infographic: straight wire, circular loop, solenoid, and toroid | **INTEGRATED** — original bilingual SVG and RU/EN captions/alt text are in `chapters/magnetism.html` | Responsive desktop/mobile browser QA and contrast PASS; CC BY-NC 4.0 publication licence declared; independent external expert review is a separate post-publication activity, not a publication gate | Rerun responsive browser QA after the Chapter 14 footnote clarification; external expert sign-off is a separate post-publication activity and does not block publication |
| 15.1 / PHY-15-001 | Magnet and coil: increasing/decreasing magnetic flux, induced current, field direction, and Lenz's law | **INTEGRATED** — original bilingual SVG and RU/EN captions/alt text are in `chapters/induction.html` | Responsive desktop/mobile browser QA and contrast PASS; CC BY-NC 4.0 publication licence declared; independent external expert review is a separate post-publication activity, not a publication gate | Rerun responsive browser QA after the Chapter 14 footnote clarification; external expert sign-off is a separate post-publication activity and does not block publication |
| 15.2 / PHY-15-002 | Moving conducting rod on rails in a uniform magnetic field; mutually perpendicular geometry, charge separation, motional EMF, and closed/open circuit cases | **INTEGRATED** — original bilingual SVG and RU/EN captions/alt text are in `chapters/induction.html` | Responsive desktop/mobile browser QA and contrast PASS; CC BY-NC 4.0 publication licence declared; independent external expert review is a separate post-publication activity, not a publication gate | Rerun responsive browser QA after the Chapter 14 footnote clarification; external expert sign-off is a separate post-publication activity and does not block publication |
| 15.3 / PHY-15-003 | Self-induction law; separate RL rise/decay curves with τ = L/R; LC charge/current oscillations with ω = 1/√(LC); energy exchange, labelled axes, units, and initial conditions | **INTEGRATED** — original bilingual SVG and RU/EN captions/alt text are in `chapters/induction.html` | Responsive desktop/mobile browser QA and contrast PASS; CC BY-NC 4.0 publication licence declared; independent external expert review is a separate post-publication activity, not a publication gate | Rerun responsive browser QA after the Chapter 14 footnote clarification; external expert sign-off is a separate post-publication activity and does not block publication |


## Interactive-book assembly inventory — Chapters 01, 02, 04, 06–10

On 2026-11-05, the local PLATES breakdown keys were compared with the corresponding world.js assembly keys. The following 98 named assembly groups are now indexed as inherited interactive-scene candidates. This is an implementation inventory, **not** a count of unique approved visual assets: some groups are components of one composite scene, while some page-level breakdowns do not correspond one-to-one with a top-level assembly. The English source remains unchanged.

| Original chapter | Module | Assembly keys identified in world.js | Count | Status |
|---|---|---|---:|---|
| 01 — Kinematics | kinematics | staff; ball; vArrow; aArrow; boardX; boardV; boardA; proj; projV; shadow; rainRoad; rainCar; rainSum; river; boatA; boatB; pull; pullA; cubeLine; bead | 20 | INTEGRATED / source lineage indexed; scene-to-page mapping and visual review pending |
| 02 — Newton's Laws | newton | rest; glide; second; friction; third; incline; tension; plane; car; tug; board; drag; honey | 13 | INTEGRATED / source lineage indexed; visual review pending |
| 04 — Work and Energy | energy | pull; toss; whirl; car; drop; spring; push; bead; bond; pendulum; slide; lift | 12 | INTEGRATED / source lineage indexed; visual review pending |
| 06 — Oscillations | oscillations | spring; hooke; trace; energy; hang; pendulum; springs4; pend4; amp; bobs; starts; string; rod; hoop; disc; car; swing | 17 | INTEGRATED / source lineage indexed; visual review pending |
| 07 — Rotation | rotation | wheel; disc; doors; plank; ladder; inertia; race; well; skater; integ; parallel; wrench; slip; impulse; particle | 15 | INTEGRATED / source lineage indexed; visual review pending |
| 08 — Fluids | fluids | blocks; feet; diver; pascal; cube; float; pipe; bernoulli; tank | 9 | INTEGRATED / source lineage indexed; keyboard focus fix verified separately; visual review pending |
| 09 — Electrostatics | electrostatics | atoms; induce; balloon; coulomb; line; point; dipole; rod; ring; plates | 10 | INTEGRATED / source lineage indexed; visual review pending |
| 10 — Gauss's Law | gauss | flux; gauss; box; line; sheet; plate; cage | 7 | INTEGRATED / source lineage indexed; keyboard focus fix verified separately; visual review pending |
| **Total** | **8 modules** | **98 assembly keys** | **98** | **Inventory only; do not report as 98 VERIFIED visuals** |

Special mapping notes:
- Kinematics has 20 top-level scene assemblies and 20 corresponding PLATES breakdown entries. The 15 dedicated assembly groups are created with literal `asm(...)` calls; `boardX`, `boardV`, and `boardA` are created by the `BOARDS.map(...)` factory, while `boatA` and `boatB` are created by the `boats.map(...)` factory. These five dynamically named groups are real rendered 3D assemblies, not unresolved extra diagrams. The three board groups are the interactive coordinate/velocity/acceleration graph panels; count each assembly once and do not double-count their internal lines, tangents, cursors or area fills as separate top-level scenes.
- Gauss's Law has additional PLATES variants csphere, isphere, nsphere, crod, and irod that are not top-level assembly keys. They represent different charge-distribution/model breakdowns and must be mapped to the corresponding underlying scene before counting distinct visuals.
- The module page descriptors and PLATES breakdowns use different identifiers in several chapters. Resolve each relationship explicitly before converting these candidate groups into final asset IDs.

## Chapter 01 — item-level visual register (2026-11-05)

This register assigns stable IDs to the four programmatically rendered visuals in the Russian standalone chapter and the 20 top-level interactive 3D scene assemblies. These are **24 scene/visual units**, not 24 separate image files and not an Image Coverage percentage. The 20 3D units are distinct registered assemblies in the interactive book; their component meshes, vector arrows, graph lines, graph cursors and other subparts are not double-counted as separate assets.

### A. Standalone Russian chapter — project-created programmatic visuals

The corresponding upstream path chapters/kinematics.html was checked at the pinned upstream snapshot and does not exist (GitHub API returned 404). These four visuals are implemented locally in chapters/kinematics.html; they are generated by HTML canvas or inline SVG code and do not embed external raster artwork.

| Visual ID | Rendered visual / local source | RU caption and meaningful alternative text | EN equivalent | Source relationship / category | Rights and review status |
|---|---|---|---|---|---|
| PHY-01-001 | Uniform-motion position–time graph; canvas #plot | «График координаты от времени». Прямая \(x(t)\) для равномерного движения; наклон соответствует постоянной скорости, точка показывает выбранное время. | N/A — no corresponding English standalone-page visual in this branch. | New project-created programmatic visual; Category C. | Source code is part of the repository's MIT-licensed software; no separate output-level image licence or exclusive copyright claim is asserted. No external artwork identified. Axis/relationship and alternative-text review PASS; desktop/mobile browser rendering PASS. |
| PHY-01-002 | Projectile trajectory diagram; canvas #klScene | «Траектория тела, брошенного под углом». Показано движение тела по параболической траектории при постоянном ускорении свободного падения; сопротивление воздуха не учитывается. | N/A — no corresponding English standalone-page visual in this branch. | New project-created programmatic visual; Category C. | Source code is part of the repository's MIT-licensed software; no separate output-level image licence or exclusive copyright claim is asserted. No external artwork identified. Model assumptions, trajectory, visual and alternative-text review PASS; desktop/mobile browser rendering PASS. |
| PHY-01-003 | Live height and vertical-velocity graph; canvas #klGraph | «Высота и вертикальная скорость от времени». Верхняя панель — \(y(t)\) в метрах; нижняя — \(v_y(t)\) в м/с; у панелей отдельные вертикальные шкалы и общая ось времени. | N/A — no corresponding English standalone-page visual in this branch. | New project-created programmatic visual; Category C. | Source code is part of the repository's MIT-licensed software; no separate output-level image licence or exclusive copyright claim is asserted. No external artwork identified. Separate scales, units and accessible description review PASS; desktop/mobile browser rendering PASS. |
| PHY-01-004 | Three-panel vertical-throw graph; inline SVG in section 1.4 | «Три графика вертикального броска». Отдельные графики координаты \(y(t)\) в метрах, скорости \(v_y(t)\) в м/с и ускорения \(a_y(t)\) в м/с²; общая ось времени, отдельные вертикальные шкалы. | N/A — no corresponding English standalone-page visual in this branch. | New project-created programmatic visual; Category C. | Source code is part of the repository's MIT-licensed software; no separate output-level image licence or exclusive copyright claim is asserted. No external artwork identified. Internal science/axis/units, SVG title/description and responsive desktop/mobile review PASS. |

**Creator/provenance note for Category C items:** these are locally authored, code-generated visual components of the Russian standalone chapter. No individual visual author is named in the repository record. The project does not claim exclusive copyright in AI-assisted code or in the underlying scientific concepts. The MIT notice is retained for the repository software; it is not represented as a separate licence for an independently exported image file.

### B. Interactive 3D book — inherited scene assemblies with Russian-localised labels

- Original creator/rightsholder: Nathan Liow.
- Pinned upstream source: [kinematics/world.js](https://github.com/nathanliow/atlas-of-physics/blob/bcd67d9b75425f4a78f5c7c1d17a2d0614727309/kinematics/world.js) and [kinematics/pages.js](https://github.com/nathanliow/atlas-of-physics/blob/bcd67d9b75425f4a78f5c7c1d17a2d0614727309/kinematics/pages.js).
- Local implementation: original-engine/kinematics/world.js, original-engine/kinematics/pages.js.
- Source relationship: inherited interactive geometry and scene construction, with Russian titles, descriptions, labels and page text; Category B where the rendered visual text is localised. Kinematics also preallocates/updates its graph-area vertex buffer; the generated vertex coordinates and draw range are retained.
- Rights basis: upstream MIT License; retain Copyright (c) 2026 Nathan Liow and the full MIT notice. Three.js is a separate MIT-licensed dependency, documented in THIRD_PARTY_NOTICES.md. No external image or texture artwork was identified in the inspected Kinematics scene module.
- Access date: 2026-11-05.
- External subject-matter review is a separate post-publication activity, not a publication gate. Internal visual and scientific review remains required.

| Visual ID | Assembly key | EN source caption / description | RU local caption / description | Local / upstream source | Category / status |
|---|---|---|---|---|---|
| PHY-01-005 | staff | Position axis — where the ball is, measured from the launch point | Ось координат — положение тела относительно точки запуска | original-engine/kinematics/world.js / kinematics/world.js | B — lineage/MIT rights, geometry, labels and vector directions reviewed PASS; desktop/mobile browser rendering PASS |
| PHY-01-006 | ball | The ball — thrown straight up at v0 | Шар — брошен вертикально вверх со скоростью v0 | same | B — lineage/MIT rights, geometry, labels and vector directions reviewed PASS; desktop/mobile browser rendering PASS |
| PHY-01-007 | vArrow | Velocity — how fast, and which way | Скорость — модуль и направление движения | same | B — lineage/MIT rights, geometry, labels and vector directions reviewed PASS; desktop/mobile browser rendering PASS |
| PHY-01-008 | aArrow | Acceleration — how the velocity changes | Ускорение — как изменяется скорость | same | B — lineage/MIT rights, geometry, labels and vector directions reviewed PASS; desktop/mobile browser rendering PASS |
| PHY-01-009 | boardX | Position–time graph — its slope is the velocity | Координата — график зависимости от времени; наклон равен скорости | same | B — lineage/MIT rights, graph axes, units, slope/area meaning reviewed PASS; desktop/mobile browser rendering PASS |
| PHY-01-010 | boardV | Velocity–time graph — its slope is acceleration; its area is displacement | Скорость — график зависимости от времени; наклон равен ускорению, алгебраическая площадь — перемещению | same | B — lineage/MIT rights, graph axes, units, slope/area meaning reviewed PASS; desktop/mobile browser rendering PASS |
| PHY-01-011 | boardA | Acceleration–time graph — its area is the change in velocity | Ускорение — график зависимости от времени; алгебраическая площадь равна изменению скорости | same | B — lineage/MIT rights, graph axes, units, slope/area meaning reviewed PASS; desktop/mobile browser rendering PASS |
| PHY-01-012 | proj | The thrown-across ball — launched at v0 and angle θ | Шар, брошенный под углом — начальная скорость и угол к горизонту | same | B — lineage/MIT rights, vector components and trajectory reviewed PASS; desktop/mobile browser rendering PASS |
| PHY-01-013 | projV | Its velocity — one arrow, two independent parts | Скорость шара — один вектор, две независимые составляющие | same | B — lineage/MIT rights and component-vector meaning reviewed PASS; desktop/mobile browser rendering PASS |
| PHY-01-014 | shadow | Its floor shadow — the horizontal motion alone | Проекция на горизонтальную плоскость — только горизонтальная составляющая движения | same | B — lineage/MIT rights and horizontal projection reviewed PASS; desktop/mobile browser rendering PASS |
| PHY-01-015 | rainRoad | Seen from the road — the rain falls straight down; the car drives through it | Наблюдение с дороги — дождь падает вертикально, автомобиль движется сквозь него | same | B — lineage/MIT rights and relative-motion vector directions reviewed PASS; desktop/mobile browser rendering PASS |
| PHY-01-016 | rainCar | Seen from the car — the car is at rest; road and rain stream past | Наблюдение из автомобиля — автомобиль покоится, дорога и дождь движутся относительно него | same | B — lineage/MIT rights and relative-motion vector directions reviewed PASS; desktop/mobile browser rendering PASS |
| PHY-01-017 | rainSum | Adding the velocities — vRC = vRG + vGC, tip to tail | Сложение скоростей — vRC = vRG + vGC, сложение векторов по правилу треугольника | same | B — lineage/MIT rights and tip-to-tail vector addition reviewed PASS; desktop/mobile browser rendering PASS |
| PHY-01-018 | river | The river — the water moves; everything on it is carried along | Река — вода течёт и увлекает находящиеся на ней тела | same | B — lineage/MIT rights and river/current scene content reviewed PASS; desktop/mobile browser rendering PASS |
| PHY-01-019 | boatA | Aimed straight across — fastest crossing, but carried downstream | Направлена прямо поперёк реки — самый быстрый переход, но течение сносит лодку вниз по реке | same | B — lineage/MIT rights and crossing-time/drift trajectory reviewed PASS; desktop/mobile browser rendering PASS |
| PHY-01-020 | boatB | Aimed upstream — slower, but lands straight across | Направлена вверх против течения — более медленный переход, лодка достигает берега напротив точки старта | same | B — lineage/MIT rights and crossing-time/drift trajectory reviewed PASS; desktop/mobile browser rendering PASS |
| PHY-01-021 | pull | A car pulling away — its acceleration fades: a = a0 − kt | Разгоняющийся автомобиль — ускорение уменьшается со временем: a = a0 − kt | same | B — lineage/MIT rights and piecewise acceleration model reviewed PASS; desktop/mobile browser rendering PASS |
| PHY-01-022 | pullA | Its acceleration — shrinking by k each second | Ускорение автомобиля — уменьшается на k каждую секунду | same | B — lineage/MIT rights, acceleration vector and variable-acceleration model reviewed PASS; desktop/mobile browser rendering PASS |
| PHY-01-023 | cubeLine | The number line — position, displacement and distance | Координатная прямая — координата x, перемещение и пройденный путь | same | B — lineage/MIT rights, turning point, displacement and distance reviewed PASS; desktop/mobile browser rendering PASS |
| PHY-01-024 | bead | The particle — x(t) = t³ − 3t | Материальная точка — x(t) = t³ − 3t | same | B — lineage/MIT rights, calculus model and turning point reviewed PASS; desktop/mobile browser rendering PASS |

**Inventory integrity:** the 20 PLATES entries match the 20 top-level assembly groups in world.js: 15 dedicated literal groups, 3 graph-board groups created by BOARDS.map(...), and 2 boat groups created by boats.map(...). Do not treat the latter five as unresolved extras, and do not double-count their internal meshes/lines as separate assets.

**70% internal visual/accessibility checkpoint — PASS (2026-11-05):** all 24 registered visual units have completed the internal content and visual pass. The 20 inherited 3D assemblies were inspected in the desktop screenshot set; the four standalone canvas/SVG visuals were checked for scientific relationships, axes, units, meaningful text alternatives and mobile/desktop rendering. The interactive-book browser test selected all 20 scenes on desktop and mobile, checked their text breakdowns and keyboard focus, and confirmed the first scene is correctly framed even when rendering is throttled. Chapter 1 browser accessibility checks reported 0 critical and 0 serious violation groups. Public attribution to Nathan Liow and the MIT License is visible in the standalone chapter footer. These results are internal publication QA, not independent expert certification. External expert review remains a separate post-publication activity and is not a publication gate.

**Current verification boundary:** the source, rights, internal visual/scientific review, alternative text and desktop/mobile rendering evidence for all 24 units is documented. VERIFIED still requires the remaining final integrated publication checks on one current HEAD, including the final quiz/attribution-footer refinements and CI.

---

## Interactive-book page-scene index — Chapters 03, 05, 11–15

This is a **page-level index**, not yet the final asset-level visual register. Each row records a `scene` descriptor in `pages.js`; a page descriptor does not always map one-to-one to an underlying `asm()` group in `world.js` (some pages combine multiple assemblies or use a different assembly key). The source comparison indicates inherited scene code with Russian-localised in-scene names/labels; affected rendered labels are Category B. Before treating an entry as a distinct visual asset, map it to the actual assembly group(s), then complete individual captions/alt text, rights, and manual review.

| Page index ID | Chapter / page | `pages.js` scene descriptor | Local source | Upstream source | Status |
|---|---|---|---|---|---|
| PHY-03-3D-01 | 03 — 3 — Движение по окружности | `whirl` | `original-engine/circular/world.js` | `circular/world.js` | PAGE INDEXED / asset-level mapping pending |
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

### Confirmed page-descriptor to assembly mappings

These examples demonstrate why a page-level `scene` value must not automatically be counted as one visual asset:

| Chapter / page | `pages.js` descriptor | Actual `asm()` group(s) in `world.js` |
|---|---|---|
| 12.1 — capacitor gap | `gap` | `pillbox` |
| 12.5 — series/parallel | `circuits` | `series`, `parallel` |
| 12.7 — battery state | `compare` | `battery`, `isolated` |
| 13.5 — series/parallel circuits | `sp` | `series`, `parallel` |
| 14.7 — parallel wires | `wires` | `same`, `opposite` |
| 14.8 — solenoid and toroid | `solenoid` | `solenoid`, `toroid` |
| 15.1 — Lenz's law | `lenz` | `core` |
| 15.9 — LC oscillations | `lc` | `lcCap`, `lcCoil` |

Other page descriptors still require the same explicit mapping. Do not infer the underlying assembly count from the number of page descriptors or from the number of `STATIONS` keys.

**Review still required for all 71 page-index entries:** map each descriptor to the actual `asm()` group(s) in `world.js`; split any page that contains multiple distinct assemblies; then assign final asset IDs, confirm geometry at desktop/mobile sizes, inspect label contrast and accessible names, add complete RU/EN descriptions, and retain item-level rights evidence. This page index does not count as final Image Coverage and does not include the four missing static infographic requirements listed above.

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

## Superseded discovery search — Chapter 14 infographic (2026-11-05)

The Wikimedia Commons candidates listed in the historical discovery note below were not selected or integrated. They were superseded by the four original project-created SVG panels recorded as `PHY-14-001` in the current asset register. Do not treat the old candidate search as the current implementation or as a publication blocker. The four-panel visual has passed internal scientific review, rights/licence documentation, bilingual/accessibility review and current desktop/mobile browser checks. External subject-matter review remains a separate post-publication activity.

<!-- Historical discovery notes retained below for provenance; candidates were not integrated. -->

## Documented discovery search — Chapter 14 infographic (2026-11-05)

Search scope: Wikimedia Commons, using queries for magnetic-field diagrams of a straight current-carrying wire, a current loop, a solenoid, and a toroid. These are **discovery candidates only**. None is integrated or approved by this entry; scientific suitability, exact file rendering, and the final four-panel consistency check remain pending.

| Required panel | Candidate and source | Creator / licence shown on source page | Preliminary suitability / unresolved checks |
|---|---|---|---|
| Straight wire | [Magnetic field produced by current.svg](https://commons.wikimedia.org/wiki/File:Magnetic_field_produced_by_current.svg) | Laurens R. Krol; CC0 1.0 | Relevant field/current diagram. Inspect arrow directions, orientation and scale before selection. |
| Circular loop | [Magnetic field of wire loop.svg](https://commons.wikimedia.org/wiki/File:Magnetic_field_of_wire_loop.svg) | Chetvorno; CC0 1.0 | Relevant field-line pattern through the loop. Check current direction and field direction against the chapter convention. |
| Solenoid | [VFPt cylindrical tightly-wound coil.svg](https://commons.wikimedia.org/wiki/File:VFPt_cylindrical_tightly-wound_coil.svg) | MikeRun (derived from Geek3); CC BY-SA 3.0 and GFDL | Physically computed ideal-coil field lines; visually suitable candidate, but adaptation/share-alike compatibility and full attribution must be assessed. |
| Solenoid (alternative) | [Solenoid field lines rough vector.svg](https://commons.wikimedia.org/wiki/File:Solenoid_field_lines_rough_vector.svg) | Wikimedia Commons file page; CC0 1.0 indicated | Possible simpler alternative; do not select until author/source metadata and scientific quality are inspected. |
| Toroid | [Magnetic Vector Potential Circular Toroid.svg](https://commons.wikimedia.org/wiki/File:Magnetic_Vector_Potential_Circular_Toroid.svg) | F=q(E+v^B); public domain dedication shown on file page | Shows toroidal geometry and magnetic-flux/current information; inspect whether its field representation adequately teaches the required toroid field direction and radial dependence. |

Search also surfaced OpenStax *University Physics, Volume 2*, section 12.6, which explains the solenoid and toroid field models and identifies the finite-field limitations of the ideal toroid. Its book content and images are CC BY-NC-SA 4.0; do not incorporate or adapt them without checking the project-level licence compatibility and the required attribution/share-alike terms. The section explicitly notes that a real helical toroid can have a small external field, so a diagram must not imply perfect confinement without qualification.

Sources reviewed:
- https://openstax.org/books/university-physics-volume-2/pages/12-6-solenoids-and-toroids
- https://commons.wikimedia.org/wiki/File:Magnetic_field_produced_by_current.svg
- https://commons.wikimedia.org/wiki/File:Magnetic_field_of_wire_loop.svg
- https://commons.wikimedia.org/wiki/File:VFPt_cylindrical_tightly-wound_coil.svg
- https://commons.wikimedia.org/wiki/File:Solenoid_field_lines_rough_vector.svg
- https://commons.wikimedia.org/wiki/File:Magnetic_Vector_Potential_Circular_Toroid.svg

**Historical status at the time of discovery only:** these candidates were not selected. The search was superseded by the four integrated original panels recorded as PHY-14-001. The former Chapter 14 placeholder is no longer present. Current internal scientific, rights, bilingual/accessibility and responsive browser checks are recorded in IMAGE_AUDIT.md; external expert review is a separate post-publication activity.
