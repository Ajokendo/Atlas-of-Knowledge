# IMAGE-FIRST POLICY
## Universal visual-content standard for Atlas of Knowledge

**Document ID:** AOK-IMG-001  
**Version:** 1.2  
**Status:** Mandatory  
**Applies to:** Every current and future subject atlas, chapter, language edition, interactive lesson, and visual learning component in the Atlas of Knowledge project  
**Owner:** Atlas of Knowledge central project governance  
**Canonical location:** Repository root — `IMAGE_FIRST_POLICY.md`  
**Language:** English master text; subject-level implementation records and learner-facing visual content must use the language requirements below.

---

## 1. Purpose and governing principles

This policy establishes one consistent, auditable process for finding, evaluating, creating, integrating, and maintaining visual learning materials across all Atlas of Knowledge disciplines.

Visuals include, but are not limited to: photographs, scientific illustrations, diagrams, maps, charts, graphs, timelines, infographics, models, animations, interactive visualizations, icons, and explanatory UI graphics.

The following principles are mandatory:

1. **Image-first, not image-only.** Search for a suitable existing, reusable visual before commissioning or generating a new one. Do not create a new image merely because generation is convenient.
2. **Scientific and factual accuracy before decoration.** A visually attractive but misleading image must not be published.
3. **Rights before publication.** Every externally sourced or adapted asset needs file-specific rights evidence and the required attribution.
4. **Accessibility and language parity.** Every learner-facing visual must be understandable in every supported language and must not rely on colour alone.
5. **Traceability.** Each visual must be identifiable in its subject's source register and audit.
6. **Honest status reporting.** Unknown, unchecked, missing, or unverified information must remain explicitly marked as such. Never invent a creator, source, licence, date, or verification result.
7. **Discipline independence.** Apply the same workflow to every subject. Scientific review criteria must be appropriate to the discipline and visual type; this policy does not prescribe one discipline's scientific conventions to another.
8. **Future compatibility.** New disciplines inherit this policy automatically. A new subject must not create a competing local copy of this standard.

## 2. Mandatory workflow

Every new visual and every existing visual selected for re-audit must pass through the following sequence.

### Step 1 — Define the learning need

Before searching or creating, record:
- subject, chapter, and learning objective;
- what the learner should understand from the visual;
- intended visual type and essential information;
- required languages and expected display contexts (desktop, tablet, phone, print, or interactive use);
- whether a visual is essential, helpful, or decorative.

Do not add a visual without a clear learning purpose. Avoid redundant illustrations that repeat nearby text without improving understanding.

### Step 2 — Search for suitable existing material first

Search for a relevant existing visual before generating or drawing a replacement.

Potential discovery sources include reputable scientific, educational, governmental, university, museum, and public-domain collections; examples include Wikimedia Commons, NASA, USGS, NOAA, OpenStax, national mapping agencies, universities, and museums. These are discovery starting points, **not blanket evidence that every item they host is reusable**.

For each meaningful search, record:
- search date;
- terms or source collections searched;
- candidate visual(s) considered;
- why the selected item is suitable, or why candidates were rejected;
- whether no suitable reusable visual was found.

Search effort should be proportionate to the importance and specificity of the visual. Do not claim that a search occurred unless it is documented or otherwise evidenced.

### Step 3 — Validate scientific, factual, and pedagogical accuracy

A competent reviewer must check that the visual:
- represents the relevant process, object, data, geography, or concept correctly;
- uses correct labels, units, scales, proportions, symbols, directions, legends, and relationships;
- distinguishes observation, measured data, conceptual model, reconstruction, simulation, and artistic interpretation;
- states meaningful simplifications, uncertainty, limitations, or scale distortions;
- does not imply unsupported causation, certainty, chronology, or geographic precision;
- is appropriate for the intended learner level and consistent with the chapter text.

The exact review checklist must be adapted to the discipline and visual type. For example, maps require geographic projection, scale, orientation, and data-date checks; charts require data provenance, units, axes, and statistical integrity; scientific diagrams require correct structures, processes, symbols, and model limitations.

**Internal verification:** the scientific/factual review must be performed by a competent reviewer distinct from the creator. This reviewer may be part of the project team; an external specialist is not mandatory for internal verification. The reviewer must record findings, role/competence, date, and outcome. The creator must never be the sole approver of their own visual.

**External expert review:** an independent specialist review is an additional assurance level, recommended where appropriate, but it is not a universal publication prerequisite. Record it separately and claim it only when completed. Its absence does not invalidate a visual that has passed all internal checks.

If a visual cannot be validated internally, mark it **PENDING** or reject it. Do not publish it as verified or imply that its accuracy has been established.

### Step 4 — Validate rights and licence for the exact asset

A hosting platform, institution, search result, or website is not itself a licence.

For every external or adapted asset, record and verify:
- the exact source page and, where available, direct asset URL;
- creator, author, photographer, institution, or rightsholder;
- the licence or permission applying to that exact item;
- a link to the licence terms or permission evidence;
- access/check date;
- required attribution wording;
- whether modification, translation, cropping, redistribution, and commercial/non-commercial use are allowed under the project's intended use.

Check relevant conditions:
- **Public domain / CC0:** verify the public-domain or CC0 claim for the exact item and jurisdiction where relevant.
- **CC BY:** provide the required attribution and identify changes.
- **CC BY-SA:** comply with attribution and applicable share-alike requirements for adaptations.
- **CC BY-NC:** assess whether the project's actual distribution and use satisfy the non-commercial condition; do not assume.
- **CC BY-ND:** do not distribute adaptations where the licence prohibits them. Translation, cropping, annotation, and other modifications require particular care.
- **Permission / custom terms:** preserve written permission and follow its scope and conditions.
- **Unknown / unclear rights:** do not publish until resolved or replace the asset with a rights-cleared alternative.

Do not remove watermarks or copyright notices. Do not use a visually accessible image merely because it appears in search results.

### Step 5 — Decide whether to reuse, adapt, create, or reject

Use the following categories consistently:

- **A — Original reuse:** an existing external visual is used without content alteration. Resizing for responsive display and non-substantive file optimisation may be recorded as technical processing, not a content adaptation.
- **B — Adapted:** an existing external visual is translated, cropped, recoloured, annotated, relabelled, combined, simplified, or otherwise substantively modified. Record the original source and every material change.
- **C — Created:** a new project-specific visual is authored. Record the method precisely: AI-generated, hand-drawn, SVG, HTML/CSS/JavaScript, code-generated chart/map, photography, 3D render, or other specified method.

A category is not a rights status. Project-created content still requires an identified creator/rightsholder and an explicit project licence or other documented rights basis. AI-generated content must not be described as a real photograph, measurement, specimen, historical document, or direct observation.

For AI-generated or illustrative reconstructions, label the visual appropriately (for example, “illustration”, “conceptual model”, “simulation”, or “reconstruction”) wherever a learner could otherwise mistake it for documentary evidence.

Reject an asset if it is scientifically misleading, inaccessible without a reasonable alternative, low quality, unlawfully sourced, or unsuitable for the learning objective.

### Step 6 — Integrate and attribute

Each integrated visual must:
- be stored in the relevant subject's own asset directory, following that atlas's established structure;
- have a stable, descriptive filename;
- be referenced using a valid local path or approved external delivery method;
- include a learner-facing caption in every supported language;
- include meaningful alternative text in every supported language, unless a documented accessibility decision establishes that the visual is purely decorative;
- include source attribution in the visual, caption, credits, or an accessible source record as required by the licence;
- identify material adaptations and any model/data limitations;
- remain legible and useful at supported screen sizes.

Do not place all subjects' image assets in a shared subject-specific folder. Each discipline owns its own assets and records.

### Step 7 — Complete language and accessibility review

For each supported language:
- translate captions, labels, legends, annotations, units where localised, and alternative text;
- check scientific terminology and consistency with the chapter;
- preserve the meaning, precision, and qualifications of the source;
- ensure no essential information exists only in one language.

Alternative text should communicate the visual's educational purpose and essential information, not merely say “image” or repeat the filename. Complex charts, maps, and diagrams need a nearby text explanation or data/table equivalent when alt text alone cannot communicate their content.

Use sufficient contrast, readable labels, keyboard-operable controls for interactive visuals, visible focus, and screen-reader names/descriptions. Never encode meaning through colour alone; add labels, patterns, symbols, line styles, or text.

### Step 8 — Technical quality assurance

Check, as applicable:
- file existence, correct path, successful loading, and absence of broken links;
- suitable resolution, dimensions, aspect ratio, and file size;
- responsive behaviour at phone, tablet, and desktop widths;
- legibility under browser zoom and reflow;
- SVG validity and accessible title/description where appropriate;
- image loading and fallback behaviour;
- keyboard interaction and focus management for interactive visuals;
- screen-reader output for meaningful visual controls;
- no horizontal overflow, clipped labels, overlapping elements, or unreadable legends;
- a text alternative or equivalent information where the visual cannot be accessed.

Automated tests should cover objective, repeatable checks. Manual checks remain mandatory where automation cannot establish actual scientific validity, rights, translation quality, visual comprehension, or assistive-technology behaviour.

## 3. Required per-discipline records

Each subject atlas must maintain its own records in its own subject directory.

### 3.1 `IMAGE_SOURCES.md` — source register

The register must include one record per visual asset or coherent language pair, with at least:

| Field | Required information |
|---|---|
| Visual ID | Stable unique identifier within the subject |
| Subject / chapter | Discipline and chapter or page |
| Learning purpose | What the visual teaches |
| Title | Clear visual title |
| Filename(s) | Exact file path(s), including language variants |
| Category | A, B, or C |
| Method | Required for C; describe the actual authoring method |
| Search record | Search date, terms/collections, candidates and decision |
| Source page | Exact source page, if external |
| Direct asset URL | Exact asset URL, if available |
| Creator / rightsholder | Name or explicitly Unknown |
| Licence / permission | Exact item-specific licence or explicitly Unknown |
| Licence evidence | Link to licence terms or permission evidence |
| Checked/accessed date | Date the source and licence were checked |
| Changes | Every material adaptation; “none” for unmodified A assets |
| Attribution | Exact required attribution wording |
| Caption | Each supported learner-facing language |
| Alt text | Each supported learner-facing language |
| Limitations | Scale, uncertainty, reconstruction, simplification, or “none identified” |
| Integration status | Current status from section 4 |
| Review evidence | Reviewer/date or explicitly pending |

Unknown values must be marked **Unknown**. If a field does not apply, mark **Not applicable** and explain why.

### 3.2 `IMAGE_AUDIT.md` — visual audit

Each subject must maintain an audit with:
- scope, branch, audit date, and policy version;
- chapter-by-chapter visual needs and known gaps;
- a record for every visual ID;
- scientific/factual review;
- rights/licence review;
- bilingual review;
- accessibility review;
- technical review;
- result, findings, required correction, reviewer, and date;
- separate coverage and verification metrics.

The audit must distinguish a visual being present from a visual being approved.

## 4. Standard status vocabulary and result values

Use these status values consistently:

- **MISSING** — a required visual has not been located or created.
- **FOUND** — a candidate has been located but not fully checked.
- **LICENSE_CHECK** — rights evidence is being examined or is incomplete.
- **SCIENTIFIC_CHECK** — scientific/factual validation is incomplete.
- **ADAPTED** — a source has been modified and the adaptation record must be completed.
- **INTEGRATED** — the visual is present in the atlas but not yet fully verified.
- **VERIFIED** — all applicable internal scientific, rights, language, accessibility, and technical checks have passed and evidence is recorded, including review by a competent person distinct from the creator. In narrative reporting this means **INTERNALLY VERIFIED**. External expert review is a separate, optional additional designation: use **EXTERNALLY VERIFIED** only when a documented independent external specialist review has also passed.
- **REJECTED** — the visual must not be used.

For each audit dimension use:
- **PASS** — evidence supports completion;
- **FAIL** — a check found a defect;
- **PENDING** — not yet checked or evidence is incomplete;
- **NOT APPLICABLE** — genuinely irrelevant, with a reason.

A visual is **VERIFIED / INTERNALLY VERIFIED** only when every applicable internal dimension is PASS and all evidence is recorded. External review is not required for this status. Use **EXTERNALLY VERIFIED** only when internal verification is complete and a documented independent external specialist review has also passed. A placeholder is not an integrated or verified visual. A source register entry alone does not establish verification.

## 5. Metrics and readiness reporting

Report visual readiness separately from editorial completeness and technical website readiness.

For each chapter and for the whole subject, report:

- **Required visual count** — number of visuals judged necessary by the chapter plan.
- **Image Coverage** = required visuals integrated ÷ all required visuals × 100%.
- **Image Verification** = integrated visuals marked VERIFIED ÷ all integrated visuals × 100%.
- **Image Gaps** — missing visuals, rejected visuals needing replacement, and unresolved required visual needs.
- **Rights status** — counts PASS, PENDING, FAIL.
- **Scientific/factual status** — counts PASS, PENDING, FAIL.
- **Language/accessibility status** — counts PASS, PENDING, FAIL.
- **Technical status** — counts PASS, PENDING, FAIL.
- **A/B/C category counts** — number of assets in each category.

Rules:
1. Do not claim 100% Image Coverage while a required visual is missing or represented only by a placeholder.
2. Do not claim 100% Image Verification while any integrated visual remains unverified.
3. Do not mark a visual VERIFIED while its rights are unknown or pending.
4. External expert review is not a prerequisite for internal verification or publication; disclose whether it has or has not taken place.
5. A visual with unresolved rights must not be publicly released, regardless of its scientific review status.
4. If the required visual plan has not been completed, label coverage **provisional** and explain the scope.
5. Never combine image readiness, editorial readiness, and technical readiness into one misleading percentage.

## 6. Automation and CI requirements

Each subject should implement automated checks appropriate to its asset types and build system. At minimum, automate what can be objectively verified:

- referenced local files exist;
- asset paths resolve;
- required source-register and audit records exist;
- category A/B/C is present;
- external assets have source and licence fields, or an explicit pending/unknown state that blocks VERIFIED;
- created assets have method and creator/rightsholder fields or explicit unresolved status;
- supported language variants, captions, and alt text are present;
- SVG files parse and have valid geometry/viewBox where applicable;
- image dimensions and formats meet project requirements;
- responsive layout tests detect overflow and clipping where feasible;
- interactive visuals have accessible names and keyboard checks where feasible;
- audit status and metrics use the approved vocabulary.

CI must not automatically mark scientific, legal, pedagogical, or translation checks as passed solely because a field is populated. Human review evidence is required for those dimensions.

A CI failure must be investigated and resolved or explicitly documented before a subject reports technical visual checks as passed.

## 7. Chapter acceptance criteria

A chapter's visual component may be accepted as complete only when:

1. Its visual needs have been identified and reviewed.
2. Every required visual is integrated; placeholders are not counted.
3. Every visual has a complete source-register entry.
4. Every applicable source and licence has been checked for the exact asset.
5. Scientific/factual and pedagogical checks pass.
6. Captions, labels, and alt text are complete in all supported languages.
7. Accessibility and technical checks pass.
8. The chapter's Image Coverage, Image Verification, and Image Gaps are updated.
9. The audit records evidence, reviewer, and date.

If any requirement remains open, report the chapter's visual status as incomplete and list the specific blockers.

## 8. Special cases and discipline-specific extensions

This policy is universal, but a discipline may add stricter requirements in its own documentation. Local extensions must not weaken the universal requirements or create conflicting status vocabularies.

Examples of discipline-specific additions may include:
- cartographic projection, coordinate reference system, scale, boundary/date provenance, and map-data licensing;
- scientific measurement uncertainty, significant figures, units, and experimental conditions;
- historical image date, archive provenance, and distinction between contemporary evidence and reconstruction;
- biological specimen identification, taxonomic authority, location/date, and conservation-sensitive disclosure;
- chemical structures, stereochemistry, reaction conditions, and representation conventions;
- engineering schematics, safety conventions, and standards references.

These are examples only. Apply the relevant expert review for the subject and asset.

Any special source restrictions or authorship obligations for a particular atlas must be recorded as a local extension. Such an extension supplements, but does not replace, this universal policy.


### 8.1 Derivative, translated, and inherited atlases

Some subject atlases may be based on a pre-existing atlas, textbook, course, dataset, or other source created by an external author or organisation. Such an atlas must follow this policy, but its audit must distinguish inherited material from new project work. The workflow must be proportionate to the actual changes; it must not falsely present a derivative translation as an independently authored atlas.

**A. Establish the source relationship before auditing**

Record:
- the original work's title, author/rightsholder, edition or version, source location, and date where known;
- the relationship between the source and the derivative atlas (for example, translation, localisation, adaptation, or partial reuse);
- which chapters, text, diagrams, figures, interactive models, code, and other components are inherited;
- what the project has and has not changed;
- the permission, licence, or other documented legal basis for reproducing and distributing the source material and any translations or adaptations.

Do not infer permission from public availability, repository access, possession of source files, or the fact that a translation has already been made. If authorship, licence, or permission cannot be established, mark it **Unknown / PENDING** and do not claim that rights have been cleared. Preserve the original creator's attribution and any source notices. Never relabel inherited material as project-created.

**B. Audit inherited visuals without treating them as newly created assets**

For an unchanged inherited visual:
- retain its original creator, source, attribution, and rights status;
- identify the corresponding source visual or source location where possible;
- verify that the project's actual use and distribution are permitted;
- check that the visual still renders correctly in the derivative atlas;
- review its educational meaning and scientific/factual accuracy where appropriate;
- complete the derivative edition's language and accessibility checks.

An unchanged inherited visual is normally recorded as **A — Original reuse**, with the original creator/rightsholder and source clearly identified. Its status as inherited must be explicit in the register. The fact that it is embedded in a project-owned page or repository does not make it project-created.

A complete re-audit does **not** require repeating discovery searches for every inherited visual when the source work and the visual are already identifiable and no replacement is being considered. Instead, record the source lineage and verify the rights, accuracy, localisation, accessibility, and technical condition relevant to the derivative edition. Conduct a new image-first search when a visual is missing, unsuitable, inaccurate, inaccessible, rights-restricted, or genuinely needs replacement.

**C. Distinguish language localisation from modification of the visual asset**

The audit must distinguish changes to the surrounding page/interface from changes to the visual itself.

- Translating surrounding page text, captions, controls, or alternative text while leaving the visual file and its visual content unchanged does not, by itself, turn that visual into category B. Keep the visual classified according to the underlying asset, and record the language-localisation checks separately.
- Translating labels or annotations inside the image, replacing embedded text, changing a legend, adding language-specific callouts, or otherwise editing the visual content is an adaptation: **B — Adapted**.
- Cropping, recolouring, redrawing, simplifying, combining, changing data, or changing the scientific/geographic meaning or presentation is also **B — Adapted**, even if the change appears minor.
- A newly authored visual that is not derived from an existing protected visual is **C — Created**. Record its actual authoring method and creator/rightsholder.
- If the original visual is replaced by a new independent visual, record the new asset separately; do not overwrite or erase the inherited asset's provenance.

Where it is unclear whether a change is merely technical or is a substantive adaptation, mark the classification **PENDING** and resolve it with evidence rather than guessing.

**D. Verify adaptation rights before modifying inherited material**

A right to reproduce an original work does not automatically establish a right to translate, crop, annotate, recolour, or otherwise adapt every component. Check the exact licence or written permission for the source work and the relevant visual. Pay particular attention to no-derivatives conditions and to separate rights that may apply to figures, photographs, diagrams, datasets, or embedded third-party assets.

If adaptation rights are not established, do not publish the modified visual. Use the unchanged source visual only if its reproduction is permitted, seek permission, or find/create a rights-cleared alternative. Record the decision and evidence.

**E. Apply a derivative-edition localisation review**

For every supported language edition, check:
- labels, symbols, legends, units, and embedded text for accurate translation;
- terminology consistency with the chapter and discipline;
- preservation of formulas, numerical values, directions, scale, relationships, and scientific meaning;
- readability and layout after translation, including text expansion and right-to-left layout where relevant;
- captions, alternative text, long descriptions, and equivalent tables or data in the target language;
- accessible names, instructions, and feedback for interactive visual controls.

Do not assume that a visually unchanged source asset is automatically understandable or accessible in the translated edition. Conversely, do not classify a visual as adapted solely because the surrounding page and its accessibility text have been translated.

**F. Report inherited and project-created work separately**

For derivative atlases, report at least these separate groups:
1. inherited visuals reused unchanged;
2. inherited visuals adapted for the derivative edition;
3. new project-created visuals;
4. visuals with unknown or unresolved source lineage;
5. missing or replacement visuals.

Report rights clearance separately from category counts. A category A label does not mean rights have been cleared; a category B label does not mean adaptation rights have been granted. Unknown provenance or rights must remain visible as unresolved blockers and must never be converted into a pass merely because the visual is already present.

The audit must also distinguish:
- **source-work coverage** — how much of the inherited visual material has been identified and mapped to the original work;
- **derivative-edition localisation coverage** — how much of that material has passed language, accessibility, and rendering checks in the target edition;
- **rights verification** — how much has documented permission for the actual reproduction and any adaptations;
- **new-visual readiness** — the normal Image Coverage and Image Verification for newly required or newly created visuals.

Do not combine these measures into one percentage. Where the original work's complete visual inventory is unavailable, state that the source-work coverage is provisional and define the audited scope.

**G. Record a subject-specific derivative protocol**

A derivative atlas must include a short protocol in its `IMAGE_AUDIT.md` identifying:
- the original work and its author/rightsholder, or explicitly Unknown;
- the source version and exact scope used;
- which components are inherited and which are new;
- the classification rules applied to unchanged and modified visuals;
- the evidence available for reproduction and adaptation rights;
- any areas where the source inventory is incomplete.

This protocol supplements the normal `IMAGE_SOURCES.md` and `IMAGE_AUDIT.md`; it does not waive either record or any requirement of this policy.

## 9. Maintenance, versioning, and governance

- This root-level document is the single canonical policy. Subject branches must link to it rather than maintain copied versions.
- Changes to the universal policy are made through the central integration process and recorded in the project registry.
- Subject branches may maintain their own source registers, audits, and stricter discipline-specific supplements.
- A subject-specific supplement must identify the policy version it extends and must not redefine universal terms.
- Future disciplines inherit the latest approved policy automatically and must create their own `IMAGE_SOURCES.md` and `IMAGE_AUDIT.md` before reporting visual readiness.
- Do not claim compliance with a newer policy version until the subject has reviewed and applied the changes.
- Preserve historical audit evidence. When policy changes affect previous decisions, re-audit affected assets and record the new result rather than silently overwriting history.

## 10. Mandatory implementation report

Every visual audit or implementation checkpoint must report:

1. Subject and working branch.
2. Policy version applied.
3. Chapters and visual types checked.
4. Required visual count and integrated count.
5. Image Coverage, Image Verification, and Image Gaps (with scope and any provisional qualification).
6. A/B/C category counts.
7. Rights, scientific/factual, language/accessibility, and technical check results.
8. Outstanding issues and unresolved evidence.
9. Files changed and commit identifier.
10. CI result and any manual checks still required.

---

**End of IMAGE-FIRST POLICY v1.1**

This policy is a project governance standard. It does not itself grant copyright permission, prove scientific accuracy, or certify any particular visual asset. Those decisions must be evidenced in the relevant subject's source register and audit.
