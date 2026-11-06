# Biology image audit

**Policy:** Atlas of Knowledge IMAGE-FIRST POLICY v1.2  
**Branch:** `workspace/biology`  
**Audit baseline:** 5 November 2026  
**Scope:** all 53 mapped visual briefs and the currently integrated image assets.

This is the consolidated audit and remediation tracker. It separates asset production from scientific, legal, bilingual and technical verification. The per-asset `IMAGE_DISPOSITION_REGISTER.md` remains the authoritative 53-row inventory.

## 1. Executive status

| Measure | Current evidence-based status |
|---|---|
| Mapped visual briefs | 53 |
| Produced or integrated | 53/53 (100% production/integration coverage only) |
| Register disposition | 47 labelled Produced; 6 labelled Integrated |
| Deferred production briefs | 0 in the current disposition register |
| Documentary third-party photographs | 15 across five regional briefs |
| Original project SVG artwork | Recorded throughout the disposition register |
| Full 13-page Chromium/axe CI | Passed in run [41822905607](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/41822905607) |
| Detailed visual review | Not complete for all assets; individual register rows retain pending notes |
| Hands-on physical-device / screen-reader testing | Not performed; tracked separately in `SCREEN_READER_AND_DEVICE_TEST_PLAN.md` |
| External specialist review | Excluded from project scope; not a project task, gate or progress metric |

**Important:** 53/53 means every mapped brief has a produced or integrated asset. It does not mean 53/53 assets have passed every IMAGE-FIRST acceptance gate. Do not report Image Verification as 100% on the basis of production coverage or CI alone.

## 2. Image categories

- **A — Original:** an unmodified third-party original. The accepted Commons photographs are category A at source level.
- **B — Adapted:** a third-party image that has been cropped, translated, retouched, annotated or otherwise modified. JPEG-to-WebP format conversion without content changes is recorded as a technical derivative; preserve the source identity and document the conversion.
- **C — Created:** original Atlas of Knowledge artwork, including authored SVG teaching diagrams. Historical AI concept drafts are not approved production assets.

The register and source audits identify 15 source-backed documentary photographs and original SVG diagrams. If a third-party image is materially cropped, relabelled or annotated in a future change, update its category and modification record.

## 3. Scientific audit

### Existing evidence

- `IMAGE_SCIENTIFIC_REVIEW.md` contains the 13 P1 Kyrgyzstan flora/fauna visual constraints.
- `IMAGE_BRIEF_REVIEW.md` records brief-level constraints for all 53 mapped anchors and explicitly distinguishes brief review from actual rendered-asset review.
- Regional photo audits restrict captions to what the source image and locality evidence support.
- The image register records known limitations, including schematic/not-to-scale labels, generic species silhouettes, habitat separation and unsupported range claims.

### Required remediation

For every individual asset, confirm the actual rendered image against the relevant brief and chapter, not only the text prompt or planned composition. Explicitly inspect:

- morphology and taxonomic diagnostic features where a species is named;
- scale, proportions and spatial relationships;
- process, force, flow and movement direction;
- time/season and geographic scope;
- legends, symbols, colour scales and units;
- whether the image could imply unsupported abundance, continuous distribution or a false real-world observation.

**Current result:** internal brief/scientific constraints are documented; this consolidated pass does not claim completed internal acceptance of all 53 final rendered assets. Rows with pending visual/morphology notes remain open for focused project-team review.

## 4. Legal and provenance audit

### Evidence found

The five documentary-photo briefs have dedicated source audits and local asset manifests:

- Chüy fauna: six photos; `FAUNA_CHUY_SOURCE_AUDIT_2026-11-03.md`, `images/generated/fauna-chuy-assets-manifest.json`.
- Jalal-Abad flora: one photo; `FLORA_JALALABAD_IMAGE_AUDIT_2026-11-03.md`, `images/generated/flora-jalalabad-asset-manifest.json`.
- Issyk-Kul flora: four photos; `FLORA_ISSYK_IMAGE_AUDIT_2026-11-03.md`, `images/generated/flora-issyk-assets-manifest.json`.
- Naryn flora: three photos; `FLORA_NARYN_IMAGE_AUDIT_2026-11-03.md`, `images/generated/flora-naryn-assets-manifest.json`.
- Osh flora: one photo; `FLORA_OSH_IMAGE_AUDIT_2026-11-03.md`, `images/generated/flora-osh-asset-manifest.json`.

The source audits record individual file pages, creators, licence choices, dates/locations, dimensions and original-file checksum comparisons. The local derivative checksums are also recorded in manifests.

### Required remediation

- Keep the source file page and exact licence version for every third-party file.
- Confirm that each live figure's attribution is visible or reachable from the caption and includes all required elements.
- Preserve modification notes, especially if a future crop, translation or annotation changes the source image.
- Do not infer rights from the host website or from search-result availability.
- Resolve any mismatch between the live caption and source record before marking the asset VERIFIED.

**Current result:** source and licence evidence is documented for the 15 accepted documentary photographs. Original SVG artwork is project-authored according to the disposition register. This audit does not assert that every caption has been re-opened and compared against the current live source page on 5 November; revalidation is required when a source or asset changes.

## 5. Bilingual and accessibility audit

The image programme uses bilingual captions and alt text in the chapter figures. The full browser suite has checked alt-attribute presence and image loading, but presence alone does not prove that alt text is useful or semantically equivalent.

For each figure, verify:
- RU and EN captions communicate the same scientific claim and qualification;
- RU and EN alt text describe the same essential visual information;
- species names, units, symbols and formulae are consistent;
- text inside SVG remains legible at narrow viewport sizes and 200%/400% zoom;
- colour is not the only way to distinguish categories or processes;
- decorative artwork has empty alt text where appropriate, rather than redundant prose.

**Current result:** bilingual content and structural checks exist; full semantic pair-by-pair human review of all captions and alt descriptions remains a focused audit item. Do not mark all images bilingual-verified based solely on the existence of both language blocks.

## 6. Technical audit

### Automated evidence

Full browser/axe/Chromium CI run [41822905607](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/41822905607) passed for all 13 Biology HTML pages. It included 390×844 and 1365×900 viewport checks, bilingual switching, keyboard checks, axe accessibility checks, contrast sampling, raster decode/dimensions/alt-attribute checks and non-zero inline-SVG geometry.

### Limits

- This is headless browser evidence, not physical-device testing.
- A decoded raster or non-zero SVG box does not prove that text is readable or that the scientific artwork looks correct.
- It does not establish offline caching.
- It does not replace NVDA, TalkBack or VoiceOver testing.
- It does not verify every source link's current legal metadata.

**Current result:** automated loading and basic rendered-geometry checks passed on the tested revision. Detailed visual review, physical-device testing and screen-reader sessions remain separate.

## 7. Current gaps and remediation queue

| Gap | Scope | Required action | Closure evidence |
|---|---|---|---|
| Focused final-art visual inspection | Assets with pending notes in `IMAGE_DISPOSITION_REGISTER.md` (45 of 53 disposition-register rows contain at least one explicit pending/open note; 37 of 53 brief-review rows contain an explicit pending visual, browser or morphology note) | Inspect actual rendered asset at desktop and narrow mobile widths; compare with approved scientific brief | Dated pass/fail entry per asset |
| Scientific morphology / scene review | Species-specific and regional wildlife/plant visuals | Verify diagnostic features, locality claims and ecological relationships; keep generic labels where identification is uncertain | Reviewer, evidence/source and decision |
| Bilingual semantic equivalence | All figures with RU/EN text | Compare caption, alt text, embedded labels, units and scientific names | RU/EN audit result per asset |
| Live attribution comparison | Third-party photo figures | Compare visible credit/source/licence links with the individual source page and licence terms | Dated rights check per source |
| Physical-device / assistive technology | 13 pages | Execute the separate manual test plan in the actual environments | Completed test record; never infer from CI |
| Offline availability | Local images and any future remote assets | Test offline behaviour only if offline support is an intended feature | Explicit result; currently not tested |

The counts are intentionally separate: 45/53 rows in the disposition register contain at least one explicit pending/open note (including rights and asset-specific QA), while 37/53 rows in the brief-review table contain an explicit pending visual, browser or morphology note. These are triage counts, not pass rates; absence of a note is not a PASS.

## 8. Status vocabulary and acceptance rule

Use these statuses in future asset records:

- `FOUND` — candidate located; not approved.
- `LICENSE_CHECK` — rights evidence is being checked.
- `SCIENTIFIC_CHECK` — scientific content is being checked.
- `ADAPTED` — adaptation completed and documented.
- `INTEGRATED` — file inserted at the intended chapter anchor.
- `VERIFIED` — scientific, legal, bilingual and technical checks all passed.
- `REJECTED` — candidate must not be used.
- `MISSING` — required visual remains absent.

The existing legacy terms Produced/Integrated are retained in the historical register for continuity. Do not silently translate Produced or Integrated into VERIFIED. As assets are rechecked, add the new status and evidence without deleting historical production records.

### Check-result vocabulary required by IMAGE-FIRST v1.0

For each applicable scientific, legal, bilingual and technical check, record one of these explicit results:

- `PASS` — the check was performed and passed.
- `FAIL` — the check was performed and a blocking issue was found.
- `PENDING` — the check has not yet been completed.
- `NOT APPLICABLE` — the check does not apply; give a short reason.

Do not infer PASS from the absence of a reported defect. The asset lifecycle status `VERIFIED` may be assigned only when all applicable checks are PASS and each NOT APPLICABLE result is justified. The current 53/53 production/integration count is not an Image Verification score.

## 9. Chapter-level metrics

Report these separately:

- **Image Coverage:** integrated required visual briefs / all required visual briefs × 100%.
- **Image Verification:** assets marked VERIFIED / integrated assets × 100%.
- **Image Gaps:** number of required briefs still missing or requiring replacement.

**Current measured values (5 November 2026):**

- **Image Coverage: 100% (53/53).** A scan of the 12 chapter HTML pages found 59 semantic `<figure>` elements in total: 57 figures containing external `<img>` elements and 2 figures containing inline SVG. The 57 image figures have alt attributes and visible captions; all local generated-image targets resolve. The 53/53 value is the number of mapped visual briefs, not the raw number of HTML figure elements.
- **Image Verification: Pending audit (percentage not yet defensible).** The disposition register contains 45/53 rows with at least one explicit pending/open note; the brief-review table contains 37/53 rows with pending visual, browser or morphology notes. No 100% verification claim is permitted until every applicable per-asset human check is recorded.
- **Image Gaps: 0 confirmed missing required briefs/assets.** This is a production-gap count only; an asset may still require correction or replacement if its pending scientific or visual review fails.

These three measures are deliberately separate. The 53/53 figure count establishes integration coverage, not scientific/legal/bilingual verification.

## 10. Audit history and scope boundary

This audit is an author-side project audit, not independent specialist certification. It does not alter the scientific content or claim new expert review. All changes in this pass are confined to `biology/` on `workspace/biology`; no main branch, other subject, shared portal or publishing configuration is changed.

**Next action:** close the focused per-asset review queue in batches, updating the source register and this audit with dated evidence. Do not generate replacement images merely to clear a pending status; reuse suitable existing assets or correct the record where appropriate.


## Focused caption remediation — 5 November 2026

A repository-wide scan of the 12 Biology chapter HTML files checked every semantic figure for local image references, alternative text and captions. No missing generated-image targets were found. Three figures in `chapters/botany.html` contained informative images and bilingual alt descriptions but lacked visible `figcaption` elements. This was a real presentation/accessibility gap: users who do not rely on alt text had no visible explanation, and the figures did not meet the image-caption acceptance rule.

**Correction committed:** added paired Russian and English captions to the root/stem/leaf anatomy plate, plant transport diagram, and generalized angiosperm flower/pollination diagram. Captions preserve scientific qualifications: generalized structures are not to a common scale; phloem flow depends on source–sink positions; pollination is distinct from fertilization.

**Regression guard committed:** `checks.mjs` now fails if a semantic `figure` containing an `img` has no `figcaption`. Inline SVG teaching diagrams without an external `img` are not incorrectly caught by this specific rule.

**Post-edit source scan:** Botany figures with images: 3; figures with captions: 3; figures with alt attributes: 3. All local generated-image references checked across the 12 chapter pages resolved to existing files. This is structural/source-level evidence, not a substitute for visual or semantic bilingual review. The global Image Verification status remains **Pending audit**.


## Inventory count clarification — 5 November 2026

A fresh scan of the chapter directory corrected an earlier shorthand in the 5 November metrics: there are **59 semantic figure elements**, not 53. Of these, **57 contain an external `img` element** and **2 contain inline SVG**. All 57 image figures have an `alt` attribute and a visible `figcaption`; no generated-image target path was missing. The separate **53/53** count remains the insertion-map visual-brief coverage and must not be presented as the count of HTML figure elements or image files. This clarification changes the inventory description, not the production-coverage numerator or the pending verification status.


## SVG accessibility and scientific-label spot check — 5 November 2026

A focused source-level review covered ten generated teaching SVGs: `anatomy-circulation.svg`, `anatomy-homeostasis.svg`, `anatomy-systems.svg`, `biochem-enzyme.svg`, `biochem-molecules.svg`, `biochem-respiration.svg`, `botany-anatomy.svg`, `botany-flower.svg`, `botany-transport.svg` and `cell-membrane.svg`.

- All ten contain an SVG `<title>` and `<desc>` with bilingual or bilingual-context descriptions.
- The reviewed text labels include the oxygen-poor/oxygen-rich distinction in circulation; negative-feedback direction in thermoregulation; enzyme–substrate complex and activation-energy explanation; lipid distinction from conventional repeating polymers; cellular-respiration compartment locations and proton-gradient direction; generalized eudicot anatomy; pollination versus fertilization; source-to-sink phloem flow; and membrane transport mechanisms.
- The source text in the sampled SVGs explicitly marks generalized/not-to-scale diagrams and avoids presenting schematic drawings as photographic evidence.
- No specific scientific error was established in this source-level sample, so no SVG artwork was changed in this batch. This is not a rendered-visual inspection and does not close asset-level verification; SVG visual layout, label collisions, contrast in context, and scientific interpretation remain subject to browser/human review.

**Batch result:** 10/10 sampled SVGs have title/description metadata; 10/10 sampled assets retain substantive explanatory labels. Global Image Verification remains **Pending audit**.


## Further SVG source review — 5 November 2026

A second focused source-level batch covered ten generated diagrams spanning ecology, evolution, microbiology, genetics, systematics and zoology: `ecology-cycles.svg`, `ecology-web.svg`, `evolution-tree.svg`, `evolution-timeline.svg`, `microbe-resistance.svg`, `microbe-virus-cycle.svg`, `genetics-translation.svg`, `systematics-tree.svg`, `zoology-adaptation.svg` and `zoology-vertebrates.svg`.

- Reviewed titles/descriptions and explanatory labels for carbon/nitrogen cycling, food-web arrow direction, common ancestry and clades, geological time qualifiers, natural selection for antimicrobial resistance, variation among viral replication strategies, codon/anticodon pairing and 5′→3′ translation, branch rotation, and the traditional vertebrate grouping caveat that birds are nested within reptiles in modern cladistics.
- Found one specific bilingual-accessibility defect: the translation SVG's `<desc>` contained Russian text only despite its bilingual title and labels. Added an English equivalent to the description in commit `a9f264b`.
- The sampled resistance diagram explicitly distinguishes selection of heritable resistant variants from purposeful adaptation; the viral-cycle diagram states that mechanisms vary; the vertebrate comparison flags the cladistic qualification.
- No further proven scientific error was established from source markup. This batch is a source-level check, not a rendered visual or independent specialist review.

**Batch result:** 10 SVG source files reviewed; 1 bilingual description corrected. Global Image Verification remains **Pending audit**.


## Third focused SVG source batch — 5 November 2026

A further ten SVGs were reviewed across ecology, botany, genetics, microbiology, systematics and zoology: `ecology-cycles.svg`, `ecology-mountain.svg`, `flora-altitude.svg`, `flora-batken-aygul.svg`, `genetics-dna-packaging.svg`, `genetics-mutations.svg`, `microbe-compare.svg`, `systematics-domains.svg`, `systematics-ranks.svg` and `zoology-anatomy.svg`.

- Reviewed bilingual descriptions and explanatory labels for carbon and nitrogen cycle pathways, mountain-watershed zonation, vegetation mosaics, the Aygul botanical plate, DNA packaging, mutation consequences, bacteria/virus distinctions, the three domains, wolf taxonomy and vertebrate respiration/coverings.
- One clarity issue was corrected in `genetics-mutations.svg`: the heading described DNA sequence changes while the displayed triplets were mRNA codons. The description and footer now explicitly explain that the displayed mRNA codons are transcribed from the corresponding DNA variant. This preserves the teaching model while making the DNA → mRNA relationship explicit (commit `0767ffa`).
- The sampled DNA-packaging figure correctly avoids presenting a 30-nm fibre as a universal obligatory structure; the taxonomy plate uses a consistent grey-wolf hierarchy; the vertebrate comparison qualifies group traits as typical rather than universal.
- No further proven source-level scientific error was established in this batch. This remains a source-markup review, not rendered visual inspection or independent specialist certification.

**Batch result:** 10 SVGs reviewed; 1 explanatory clarification committed. Global Image Verification remains **Pending audit**.


## Regional habitat and zoology SVG review — 5 November 2026

Reviewed six further assets: `fauna-batken-dry-highland-habitats.svg`, `fauna-talas-besh-tash.svg`, `flora-chuy-vegetation-zones.svg`, `flora-talas-vegetation.svg`, `zoology-vertebrates.svg` and `zoology-adaptation.svg`.

- Checked bilingual descriptions and labels for the Batken marmot survey panel, Besh-Tash's separate habitat scenes, Chuy and Talas vegetation mosaics, the traditional vertebrate grouping and habitat adaptations.
- Confirmed that the Batken panel labels its 4,146 count as a spring 2026 survey result rather than a permanent population estimate and leaves the marmot species unspecified; the Besh-Tash image explicitly identifies itself as a habitat reconstruction, not a distribution map or claim of simultaneous co-occurrence.
- The zoology overview correctly qualifies the five familiar vertebrate groups as a teaching grouping and notes that birds are nested within reptiles in modern cladistics.
- Found one metadata-language gap: `flora-talas-vegetation.svg` had an English-only `<desc>`. Added a Russian equivalent while retaining the English description (commit `6124fbb`).
- The Chuy and Talas vegetation diagrams appropriately describe transitions as conceptual rather than fixed elevation boundaries. No further source-level scientific error was established in this sample.

**Batch result:** 6 regional/zoology SVGs reviewed; 1 bilingual description corrected. Global Image Verification remains **Pending audit**.


## Documentary-photo markup and attribution sweep — 5 November 2026

A focused source scan of the two regional Biology chapters checked all 15 locally packaged documentary WebP photographs: six in the Chüy fauna chapter and nine in the Kyrgyzstan flora chapter (Jalal-Abad 1, Issyk-Kul 4, Naryn 3, Osh 1).

For each image element, the adjacent caption region was checked for:
- a non-empty alternative text;
- Russian and English attribution/caption content;
- a direct Wikimedia Commons file-page link;
- an explicit licence or public-domain status statement.

**Result: 15/15 passed this structural markup check; no missing alt, language pair, Commons source link or rights label was found.** The asset manifests independently record source authors, exact licence labels, original dimensions and byte counts, original SHA-1 comparisons, derivative WebP checksums and conversion details.

This is source-level markup and provenance-record verification. It does not constitute a fresh pixel-by-pixel visual review of all 15 binaries, legal advice on licence compatibility, or independent taxonomic certification. The unresolved Rufous-naped Tit candidates remain excluded and are not among the 15 integrated photographs. Global Image Verification remains **Pending audit** until the remaining asset-specific visual and scientific gates are documented.


## Deferred optional freshwater infographic marker and SVG accessibility batch — 5 November 2026

The requested optional enhanced freshwater-fauna infographic could not be generated because image-generation capacity is unavailable. A source comment marker and `data-image-followup="optional-enhanced-illustration-deferred"` attribute were added to the existing `image-brief-fauna-freshwater` figure in `chapters/fauna-kyrgyzstan.html` (commit `771f9f7`). The already integrated original `fauna-freshwater-habitats.svg` remains active; it was not removed or falsely marked missing. Its current composition already separates Issyk-Kul littoral habitat from a mountain stream and uses generic, unlabelled fish silhouettes.

A further ten SVG source files were inspected: `cell-animal.svg`, `cell-cycle.svg`, `cell-mitosis.svg`, `evolution-homology.svg`, `fauna-habitats.svg`, `fauna-invertebrates.svg`, `fauna-herps-habitats.svg`, `fauna-mammals-habitat-reconstruction.svg`, `fauna-batken-dry-highland-habitats.svg` and `fauna-osh-southern-habitats.svg`.

Three accessibility metadata gaps were corrected:
- `fauna-habitats.svg`: added a Russian counterpart to the English-only `<desc>`.
- `fauna-herps-habitats.svg`: made both the title and description bilingual.
- `fauna-mammals-habitat-reconstruction.svg`: made both the title and description bilingual and clarified that the three mammals are shown in separate habitats, not as co-occurring at one site.

Other checked concepts included animal-cell organelles and not-to-scale caveat; G1/S/G2/M sequence and checkpoints; distinction between mitosis and cytokinesis; homologous forelimbs versus analogous bird/insect wings; insect versus arachnid body plans; and the bounded 2026 Batken marmot survey figure (4,146 recorded, not a permanent population estimate). No additional scientific correction was made where source markup already conveyed the necessary distinction.

These were source-markup checks, not rendered visual QA. Global Image Verification remains **Pending audit**.


## Biology SVG bilingual metadata and concept review — 5 November 2026

A source-level review covered the remaining 26 generated SVG assets: `anatomy-circulation.svg`, `anatomy-homeostasis.svg`, `anatomy-systems.svg`, `biochem-enzyme.svg`, `biochem-molecules.svg`, `biochem-respiration.svg`, `biology-cover.svg`, `botany-anatomy.svg`, `botany-flower.svg`, `botany-transport.svg`, `fauna-birds-habitats.svg`, `fauna-freshwater-habitats.svg`, `fauna-issyk-habitats.svg`, `fauna-jalalabad-western-tien-shan.svg`, `fauna-naryn-highland-habitats.svg`, `flora-altitude.svg`, `flora-batken-aygul.svg`, `flora-chuy-vegetation-zones.svg`, `genetics-dna-packaging.svg`, `microbe-compare.svg`, `microbe-resistance.svg`, `microbe-virus-cycle.svg`, `systematics-domains.svg`, `systematics-ranks.svg`, `systematics-tree.svg` and `zoology-anatomy.svg`.

Six bilingual accessibility metadata gaps were corrected:
- `botany-anatomy.svg`, `botany-flower.svg` and `botany-transport.svg`: added English counterparts to Russian-only descriptions.
- `fauna-birds-habitats.svg`, `fauna-freshwater-habitats.svg` and `fauna-naryn-highland-habitats.svg`: added Russian counterparts to English-only titles and descriptions.

Conceptual source checks included circulation pathways and oxygenation labels; negative-feedback thermoregulation; enzyme-substrate framing; biomolecule distinctions (including the non-polymer nature of many lipids); cellular respiration compartmentation and proton movement; pollination versus fertilization; xylem/phloem transport; separation of bird, lake and mountain habitats; generic rather than species-identified freshwater fish; conceptual vegetation belts; DNA packaging; antimicrobial selection rather than directed adaptation; viral replication variability; cellular domains versus viruses; taxonomy ranks; and phylogenetic clade/branch-rotation interpretation.

No further proven scientific error was established from the source markup in this batch. This is not rendered-image inspection, pixel-level review, independent specialist certification, or a legal licence audit. Global Image Verification remains **Pending audit**.


A final bilingual-equivalence refinement in this batch expanded the English descriptions in `biochem-enzyme.svg` and `biochem-respiration.svg`: the enzyme text now explicitly includes substrate binding at the active site and enzyme–substrate complex formation; the respiration text now fully states proton pumping from the matrix to the intermembrane space and return through ATP synthase. This avoids treating a short English summary as a full counterpart to the Russian description.


## Chapter-to-asset integration and accessibility cross-check — 5 November 2026

A cross-check of the 12 Biology subject chapters matched all local image references against the generated-assets directory and inspected the semantic figure markup.

- 62 external images are referenced by the chapters: 47 SVG illustrations and 15 documentary WebP photographs. All 62 referenced filenames exist in `images/generated/`; no broken local image target was found.
- The 48th SVG, `biology-cover.svg`, is intentionally not referenced as a chapter figure; it is a cover asset, not an orphaned chapter illustration.
- Across the 12 chapters, 59 semantic figures were found. Every figure containing one or more `<img>` elements has a `<figcaption>` with both Russian and English content.
- All 62 image elements have non-empty alternative text containing both Cyrillic and Latin-language content. No missing or one-language-only alt text was found.
- Some flora figures group multiple documentary photographs in one captioned figure; image counts therefore exceed figure counts in that chapter. The grouping is intentional and was not misreported as missing captions.

This is source-level integration/accessibility validation. It does not verify the rendered appearance, colour contrast, keyboard/screen-reader behaviour on actual devices, or the legal and taxonomic correctness of every photographic subject. Those gates remain separately tracked; Global Image Verification remains **Pending audit**.


## Regional chapter-to-illustration semantic cross-check — 5 November 2026

A focused cross-check covered the 18 figures in `chapters/fauna-kyrgyzstan.html` and the 8 figures in `chapters/flora-kyrgyzstan.html`. The HTML alternative text and bilingual captions were compared with the relevant SVG titles, descriptions and visible text labels where source text was available; the documentary-photo captions were checked for consistency with their stated role as local habitat examples rather than comprehensive regional inventories.

- The regional SVG set distinguishes habitat reconstructions from range maps, censuses and single-site observations. Separate panels are explicitly described as separate ecological settings; generic fish and waterbird silhouettes are not presented as species identifications.
- The Batken marmot panel retains the survey-specific 4,146 figure and the unspecified `Marmota spp.` identification. The Naryn and Osh panels distinguish habitat scenes from abundance estimates; the Kulun-Ata camera-trap source is dated and framed as evidence of presence, not population size.
- The Aygul plate is identified as a schematic of `Fritillaria eduardii`, with `Petilium eduardii` labelled as a synonym. Vegetation diagrams consistently qualify altitudinal transitions as mosaics rather than universal fixed elevation bands.
- The 15 documentary photographs remain captioned as specific local examples (for example, Arslanbob walnut forest, Issyk-Kul shoreline/foothill/sea-buckthorn/spruce settings, Naryn lake/meadow/plant examples, and Kulun-Ata riparian vegetation); captions do not claim to represent complete oblast-wide flora.

No proven mismatch between the sampled SVG source labels/descriptions and the corresponding chapter alt/caption wording was found. This remains a source-text and semantic consistency review: it is not fresh pixel-level inspection of all WebP photographs, rendered-browser review, or independent taxonomic certification. Global Image Verification remains **Pending audit**.


## Core-chapter figure and caption revalidation — 5 November 2026

A fresh parser-based revalidation covered the ten non-regional subject chapters: anatomy, biochemistry, botany, cell biology, ecology, evolution, genetics, microbiology, systematics and zoology.

- These chapters contain 33 semantic figure blocks, including 31 figure blocks with external images; the remaining two are inline-SVG figures.
- The 31 external-image figures contain 31 image elements. All have non-empty alt text and a visible `figcaption` with both Russian and English spans.
- No missing caption, empty alt attribute or one-language-only caption was found. The audit parser was adjusted to accept legitimate attributes on `figcaption` elements; an initial narrow pattern had not matched classed captions and must not be mistaken for missing markup.
- The regional chapters had previously passed the same corrected structural checks. Across all 12 chapters, the combined inventory remains 59 semantic figures, 57 image-containing figures, and 62 external image elements (some flora figures intentionally group multiple photos). All 57 image-containing figures have bilingual captions, and all 62 image elements have non-empty alt text.

This is source-markup validation, not a new rendered visual inspection or physical-device/screen-reader session. Global Image Verification remains **Pending audit** for detailed per-asset visual and scientific review. The current author-side editorial-readiness checkpoint remains 99/100; this structural revalidation does not justify increasing it.


## Full generated-SVG structural and accessibility metadata sweep — 5 November 2026

A source-level sweep covered all 48 original SVG files in `images/generated/`, including the standalone Biology cover asset. Each file was checked for an SVG root element, a `viewBox`, a `<title>` and `<desc>` containing both Cyrillic and Latin-script text, a closing SVG tag, and the presence of embedded scripts, `foreignObject`, external/data URI references or embedded raster-image elements.

- The first pass found two description-language gaps: `cell-animal.svg` had a Russian-only `<desc>`, and `zoology-adaptation.svg` had an English-only `<desc>`.
- Both descriptions have now been completed in Russian and English without changing the visible illustration or its scientific scope.
- The full set now passes the checked source-pattern criteria: 48/48 have `viewBox`, bilingual title and description metadata, and a closing SVG tag; none of the 48 contains a detected `<script>`, `<foreignObject>`, external/data URI reference or embedded `<image>` element.

This is a source-text structural/accessibility-metadata check, not standards-complete XML parsing, rendered visual inspection, contrast testing, or screen-reader/device QA. It does not establish scientific correctness of every visual detail. Global Image Verification remains **Pending audit**.


The repository's `checks.mjs` now enforces the same repeatable SVG source checks for every file in `images/generated/`: bilingual title/description metadata, an SVG root, `viewBox`, closing tag, and absence of detected scripts, `foreignObject`, embedded raster images, and external/data URI references. This turns the corrected metadata condition into a continuing CI guard rather than a one-time audit observation.


## Full responsive Chromium visual-asset and page-render validation — 5 November 2026

GitHub Actions run [41905128510](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/41905128510) completed successfully on commit `c0f31471ac1fbee556d214487dbd55b18256e60c`. The existing `browser-smoke.mjs` exercised all 13 Biology HTML pages at mobile (390×844) and desktop (1365×900) viewports.

The successful run recorded:
- 13/13 pages at both viewport widths, with no uncaught page errors.
- 30 language-toggle interactions.
- 19,373 sampled visible text instances for preliminary contrast; zero fell below the script's WCAG contrast thresholds. Background-image/gradient and translucent layered cases remain outside that sampler's scope.
- Automated axe WCAG 2.0/2.1/2.2 A/AA checks, skip-link and landmark checks, bilingual state checks, interactive-model and keyboard activation checks, focus-indicator traversal, horizontal-overflow checks, and dynamic-output semantics.
- Every page image was asked to decode; raster assets were checked for intrinsic dimensions and alt-attribute presence, and visible inline SVGs were checked for non-zero rendered geometry. No issue was reported.

This is now evidence of successful responsive browser rendering, asset loading/decoding and automated accessibility checks. It is not a human pixel-level judgement of every illustration's biological morphology, scene composition, label collisions, crop or caption-to-image semantic match. The screenshot-artifact workflow is being added for a subsequent focused human visual pass. Global Image Verification therefore remains **Pending audit** until that per-asset review is recorded.


## Human visual review of responsive page screenshots and corrective pass — 5 November 2026

A full-page desktop screenshot set for all 13 Biology HTML pages (the subject index plus 12 chapters) was generated by Chromium CI and manually inspected at page and figure scale. The screenshot set is retained as the CI artifact from run [41910231926](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/41910231926), commit `428fcd79932a9e85e182ba01285558435bc16428`.

The visual pass identified and corrected the following rendered-layout issues:
- The regional index showed Russian and English titles simultaneously; language visibility is now tied to the page language.
- The thermoregulation, biomolecule-class, DNA-packaging, membrane-transport and microbe-comparison illustrations had crowded or colliding bilingual labels; their label positions and line breaks were revised. The microbe-comparison heading was also split to prevent clipping, and virus callouts were moved clear of the particle illustration.
- The evolution homology plate had a long key overlapping the limb drawings and explanatory text colliding with group labels; the key was separated into two lines and redundant colliding description lines removed.
- The geological timeline had milestone callouts colliding across the horizontal scale; it was rebuilt with ordered, separate callout cards.
- The central-dogma inline SVG caption was clipped at the bottom; it now uses separate Russian and English lines.
- The ribosome-translation diagram's growing-chain label was moved clear of the peptide-chain artwork.
- The cellular-respiration plate was re-laid out to separate cytosol and mitochondrial compartments, reduce label collisions, and show proton return through ATP synthase in the correct direction.

The latest CI run [41910231926](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/41910231926) completed successfully: 13/13 pages at mobile and desktop widths, 30 language-toggle interactions, no uncaught page errors, 19,331 sampled visible text instances with zero below the configured contrast thresholds, and successful page-image decode / inline-SVG geometry checks. Automated axe WCAG checks, keyboard/focus traversal and overflow checks also passed. This is responsive page-render and visible-layout evidence, not a substitute for detailed scientific review of every individual visual element.

**Remaining distinction:** page-render visual QA has now been performed and the identified defects corrected, but Global Image Verification remains **Pending audit**. The remaining visual verification work is asset-specific: confirm fine biological morphology, scientific depiction, photo subject/caption match, and any source-specific caveats at image scale. External specialist review and school/teacher evaluation are excluded from this project and are not gates. Internal rendered visual, rights and accessibility checks remain separately tracked.


## Documentary-photo preview review — 5 November 2026 (updated)

A bounded visual review was completed against the individual Wikimedia Commons file pages and their rendered image previews for **all 15 accepted documentary photographs** across the five regional briefs. The earlier attempt to open the Chüy Halys pit-viper preview had failed; the preview was subsequently retrieved and inspected successfully.

### Result: 15/15 previews inspected

- **Chüy fauna — 2 animal photographs:** the red-squirrel frame visibly contains a squirrel, consistent with the source caption, but the animal is relatively small and the photograph is not a diagnostic morphology plate. The Halys pit-viper frame visibly contains a snake on a trail, consistent with the source caption and file-page metadata; this preview-level check does not independently establish species identity.
- **Chüy habitats — 4 photographs:** Ak-Suu gorge, Ala-Archa mountain landscape, Chong-Kemin rocky stream/meadow/woodland, and Chunkurchak red-sandstone canyon all match their broad habitat/landscape captions. None supports species-level, abundance or distribution claims.
- **Jalal-Abad flora — 1 photograph:** Arslanbob walnut-forest landscape matches its regional landscape caption. It is not a close-up for diagnosing individual tree species.
- **Issyk-Kul flora — 4 photographs:** Tamchy Bay wetland, dry gully above Tamchy, lakeshore sea-buckthorn shrub, and Karakol Valley spruce forest all match their broad scene captions. The dry-gully image remains a terrain example, not evidence of a named plant community. The sea-buckthorn and spruce identifications are supported by the individual source pages, not independently certified from landscape-scale morphology.
- **Naryn flora — 3 photographs:** Chatyr-Kul shoreline and Son-Kul lakeshore meadow match their geographic landscape captions. The *Clematis songorica* preview shows flowering shoots consistent with the source's plant caption and exact Naryn locality; this is not a specialist taxonomic determination.
- **Osh flora — 1 photograph:** Kulun-Ata river corridor matches the caption's mountain stream/riparian habitat description; no individual tree species should be inferred from it.

### Evidence and remaining limits

- Individual Commons file pages and rendered previews were inspected for all 15 accepted photographs. The checked page metadata was consistent with the recorded author/date/location and the licence recorded in the corresponding asset manifest.
- The existing build manifests preserve source-original SHA-1 comparisons, source and derivative dimensions/byte counts, and local WebP SHA-256 values. Earlier Chromium runs confirmed local asset decoding and display.
- The visual inspection used Commons-rendered previews (typically 960 px), not a fresh full-resolution pixel-by-pixel comparison of every committed WebP derivative. It establishes broad scene/caption alignment, not expert species diagnosis or detailed morphology certification.
- The two Rufous-naped Tit candidates remain excluded because of the previously documented taxonomy metadata conflict; they are not part of the 15-photo accepted denominator.

**Result:** 15/15 accepted documentary-photo previews inspected; no proven broad scene-to-caption mismatch found. No image or chapter content was changed in this pass. Fine species morphology and internal rights/rendered/accessibility checks remain open where specifically recorded. Independent specialist review and school/teacher evaluation are excluded. Global Image Verification remains **Pending audit**; do not convert preview review into a VERIFIED status for every photograph.


## Naryn maral taxonomy label — 5 November 2026

A focused scientific-label check of `fauna-naryn-highland-habitats.svg` found that the caption named the animal as maral but used the overly broad taxonomic label `Cervus sp.`. The species-level name `Cervus elaphus` is supported by the Kyrgyzstan Red Book entry for the Tien Shan maral, which identifies it as *Cervus elaphus* (subspecies treated there as *C. e. asiaticus*): https://open.kg/en/about-kyrgyzstan/nature/red-book/animals/mammals/print%3Apage%2C1%2C31820-blagorodnyy-olen-tyanshanskiy-podvid-maral-bugu-erkegi-maral-urgaachysy-asiatic-red-deer-tien-shan-maral-tien-shan-stag.html. The regional CAMCA study also documents maral in the Naryn River valley: https://camcaproject.org/study-in-tien-shan-maral-in-kyrgyzstan/.

**Correction:** changed the diagram label to `Maral habitat · Cervus elaphus`. This identifies the species without asserting a contested subspecies rank. The schematic continues to describe a habitat example, not a distribution map or census. No change was made to the chapter's cautious caption. This is a source-supported author-side correction, not independent specialist certification.


## Issyk-Kul salinity correction in aquatic-habitat visual — 5 November 2026

A scientific review found that the visual brief `fauna-freshwater-habitats.svg` and its chapter alt text incorrectly grouped Lake Issyk-Kul under “freshwater habitats”. Issyk-Kul is a closed-basin **brackish lake**; the FAO technical paper reports average salinity of about 5.9–6.1 g/L, with lower salinity near major river mouths (https://www.fao.org/docrep/018/i3268e/i3268e.pdf). A peer-reviewed 2023 study likewise classifies its waters as brackish (5.6–6.7 g/L; https://www.mdpi.com/2079-7737/12/5/642).

**Corrections committed:**
- Renamed the SVG title to “Inland waters of Kyrgyzstan: Issyk-Kul and a mountain stream”.
- Revised the SVG description to distinguish brackish Lake Issyk-Kul from a freshwater mountain stream.
- Changed the chapter section eyebrow from “Freshwater life” to “Inland waters”.
- Updated the image alt text and added a bilingual note explaining the lake’s salinity and why its ecology should not be conflated with freshwater river systems.

The generic fish silhouettes remain explicitly unidentified. No species labels, distribution claims or population claims were added. This closes a clear terminology/science issue in this illustration; it does not certify the generic fish silhouettes as species-specific morphology.


## Aygul flower-anatomy detail correction — 5 November 2026

A closer review of `flora-batken-aygul.svg` found that its enlarged flower detail showed only two stamens, which could misrepresent the flower's androecium. The genus-level description in *Flora of China* states that Fritillaria flowers have six tepals and six stamens (Chen & Mordak, 2000, pp. 127–133): https://www.iplant.cn/foc/pdf/Fritillaria.pdf. The RHS profile independently describes the species' nodding orange-to-yellow flowers and leafy bract tuft: https://www.rhs.org.uk/plants/7364/fritillaria-eduardii/details. A Kyrgyzstan-focused phenology paper reports F. eduardii as a 50–130 cm plant with broad leaves and usually around six nodding orange-red flowers: https://applied-research.ru/en/article/view?id=13153.

**Correction:** the enlarged schematic now depicts six stamens and explicitly labels six tepals and six stamens in both the visual description and its visible annotation. The main plant remains a simplified botanical plate, not a measured specimen or a claim about a fixed flower count per plant. The drawing's morphology was checked internally against published descriptions; no external botanist review is part of this project.


## Circulation-flow and domain-comparison corrections — 5 November 2026

A source-level review of two additional diagrams found two actionable issues:

- `anatomy-circulation.svg`: the systemic venous-return route was split into two disconnected blue paths, leaving a visible gap between the body return and the segment entering the right atrium. Replaced them with one continuous, directional path from the body circuit back to the right atrium. This preserves the correct sequence: body → venae cavae/right atrium → right ventricle → pulmonary artery → lungs → pulmonary veins/left atrium → left ventricle → body.
- `systematics-domains.svg`: the eukaryotic-cell size caveat ended with a Russian/English slash but had no complete English equivalent. Replaced it with two complete concise bilingual statements: eukaryotic cells are often larger, but sizes vary widely.

These are source-level corrections. The updated screenshots and CI checks are pending; no claim of pixel-level visual verification is made yet.


### Follow-up: full blood-flow sequence in the circulation diagram — 5 November 2026

A deeper directional audit of `anatomy-circulation.svg` found that the initial return-path repair was not sufficient: the pulmonary-vein arrow entered the right-atrial side, the red systemic outflow began near the left atrium rather than the left ventricle, and an extra red arrow pointed from the body back toward the left ventricle. Corrected the complete set of large circuit arrows:

- pulmonary artery: right ventricle → lungs (blue);
- pulmonary veins: lungs → left atrium (red);
- systemic arterial outflow: left ventricle → body (red);
- systemic venous return: body → right atrium (blue, continuous path).

This is a source-level flow-direction correction. CI and refreshed screenshot review remain pending; any hands-on device/accessibility checks are internal project-team checks only. No school or classroom evaluation is planned within this project.


## Carbon-cycle arrow correction — 5 November 2026

In `ecology-cycles.svg`, the former arrow from the decomposition box to the ocean incorrectly implied a direct one-way transfer from decomposition to the ocean. Removed it and replaced the ocean connection with two directional CO₂-exchange arrows between atmosphere and ocean. Also renamed the soil-to-atmosphere return arrow as soil respiration, rather than presenting it as an unspecified general respiration route. This is a conceptual diagram correction; it does not attempt to depict every carbon reservoir or pathway. The diagram itself states that the model is simplified. Updated CI and screenshot review are pending.


## Vertebrate-comparison panel fit correction — 5 November 2026

In `zoology-anatomy.svg`, the English amphibian respiration caption sat one pixel below the lower edge of its card. Increased that panel's height slightly so the full bilingual caption is contained within the panel, with clear separation from the next row. This is a source-geometry correction; refreshed browser screenshot review is pending.


## Supplemental generated Aygul botanical plate — 5 November 2026

A new author-side educational botanical plate for *Fritillaria eduardii* was generated specifically for the Biology Atlas. It depicts an upright leafy stem, elongated lanceolate leaves, nodding brownish-red bell-shaped flowers on downward-facing pedicels, and a leafy bract tuft above the flowers. Separate floral studies include a frontal flower view with six tepals and six stamens, plus isolated floral structures.

- Classification: **Category C — generated/original illustration**, not a documentary photograph and not external-source material.
- Intended use: supplementary educational artwork for the Aygul entry; no species-population estimate, fixed flower count, or invented precise locality is represented.
- Provenance: generated in ChatGPT on 5 November 2026 at the user's explicit request. No third-party image source or external licence is claimed.
- Working filename: `flora-batken-aygul-botanical-plate.webp` (optimized derivative of the generated PNG). The binary is present in the conversation workspace but has **not yet been committed to the GitHub branch**; therefore the chapter HTML continues to reference the existing verified SVG and must not point to the absent WebP.
- Review status: morphological intent checked against the existing Aygul source review; this generated plate is illustrative, not a specimen record or botanical certification. The asset is now integrated; the active repository derivative has been inspected directly and the current Chromium workflow rechecks page rendering.


**Generated-file technical record:** source PNG, 1312 × 1199 px, RGB; optimized WebP derivative, 1312 × 1199 px, 179,740 bytes, SHA-256 `956c21e15206f7a8d65629ae9bc1496bea39b117654a8f438bcff1c320124481`. The derivative is available in the current conversation workspace; this hash is a local provenance record, not a GitHub repository checksum.


### Aygul generated plate — repository integration (5 November 2026)

The supplemental Category C botanical plate is now committed and referenced in `chapters/flora-kyrgyzstan.html` as `images/generated/flora-batken-aygul-botanical-plate.webp`. It is displayed as a separate educational illustration beside the original SVG, not as documentary evidence. The repository derivative is 320 × 292 px, 7,196 bytes, SHA-256 `b79cc139c33b4b19b5c1e72fa79885688cdd9c0202d6d402ad3f13348badf4c9`; the higher-resolution source remains in the conversation workspace. Bilingual alt text and captions explicitly state the six tepals/six stamens detail and the limits of inference (no fixed flower count, population size or precise locality). Detailed P1 scope is linked through `IMAGE_SCIENTIFIC_REVIEW.md`. Initial CI run 41968857255 found two metadata/insertion-map guard issues; the extra figure anchor was renamed so it does not create a new brief, and the P1 register row now links to the scientific review. A subsequent CI run is required to establish pass/fail; browser rendering is not yet claimed as passed.


## Superseding browser/CI update — 5 November 2026

The pending-CI and pending-browser-smoke notes above record the state when the individual source corrections were made. They are superseded for automated validation by the full Biology workflow [41968952829](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/41968952829), which completed successfully on `workspace/biology` head `fb4b581f0cf23e86b8a093280ba0846fc01a345f`. The `validate` job passed page/local-link/script validation, Chromium setup, local server startup, browser smoke tests for every Biology page, and screenshot artifact upload.

This closes the outstanding **automated CI/browser-smoke rerun** for the corrections listed above. It does not close the separately tracked detailed internal visual review of all assets or hands-on screen-reader/physical-device checks that the project team can perform. The 53/53 metric remains production/integration coverage only; Image Verification is not reported as 100%.


## Aygul supplementary botanical plate — immediate four-dimension intake — 5 November 2026

Asset: `images/generated/flora-batken-aygul-botanical-plate.webp`, displayed at `chapters/flora-kyrgyzstan.html#aygul-generated-plate`. This is a supplementary Category C AI-generated educational illustration; the existing bilingual SVG remains the primary schematic at `#image-brief-flora-batken`.

- **Visual Coverage — PRESENT (supplementary):** the Batken/Aygul-Tash section contains both the primary SVG schematic and a separate supplementary botanical plate. This confirms placement, not completeness of visual coverage for the whole chapter.
- **Internal Verification — IN PROGRESS / NOT VERIFIED:** a visual inspection of the 1,199 × 1,312 working candidate shows an upright leafy plant, nodding reddish bell-shaped flowers, and separate flower, leaf, fruit and bulb studies. The six-tepal/six-stamen detail is a useful teaching representation, but this inspection alone does not establish all species-specific morphology, organ proportions, phenology or the exact depicted bulb/fruit morphology. Do not label this new plate VERIFIED. The existing species review for the SVG is not a substitute for review of this separate generated plate.
- **External review:** excluded from project scope and not tracked as a pending task or verification metric.
- **Project-use authorization — PASS:** generated in ChatGPT at the project owner's explicit request for this Atlas. OpenAI Terms of Use effective 1 January 2026, Section “Content”, assign the Output to the user as between user and OpenAI, to the extent permitted by applicable law (https://openai.com/policies/terms-of-use/). No third-party image source is involved. No separate CC/public-domain licence is assigned; do not claim copyright exclusivity or a particular open licence. This is a documented project-use basis, not legal advice.

**Binary implementation note:** the committed repository derivative is recorded in the disposition register as 320 × 292 px / 7,196 bytes. A higher-resolution 1,199 × 1,312 px WebP working candidate is available in the current working container (353,604 bytes; SHA-256 `6a0d714c30d70856b29bebc699a1cff77e97d502a5ea455560bfa2ddede53b0c`), but it has not been committed to the Biology branch in this operation. Therefore the repository page must continue to use the already committed asset; do not claim that the high-resolution candidate is live.

**Procedure dependency:** `IMAGE_FIRST_POLICY.md v1.2`, `AUTHOR_CREATED_VISUALS_STANDARD.md v1.1` and `VISUAL_IMPLEMENTATION_GUIDE.md` are not present at the root of the inspected `workspace/biology` branch. This record applies the four requested tracking dimensions conservatively, but does not claim a complete clause-by-clause pass of those versioned standards. The named policy files are not present in this branch and are not treated as active governing documents here. The in-branch controls are this audit, `EDITORIAL-AND-SCIENTIFIC-STANDARDS.md`, `IMAGE_SOURCES.md`, `IMAGE_BRIEF_REVIEW.md`, `IMAGE_DISPOSITION_REGISTER.md`, `IMAGE_INSERTION_MAP.md` and the automated checks. No compliance claim is made against absent documents.


## Historical policy-version reference — 5 November 2026

This section preserves an older reference to `IMAGE_FIRST_POLICY.md` v1.2, `AUTHOR_CREATED_VISUALS_STANDARD.md` v1.1 and `VISUAL_IMPLEMENTATION_GUIDE.md` v1.1. Those files are not present in this branch and are not treated as active governing documents here; no clause-by-clause compliance claim is made. The operative in-branch controls are listed in the current QA reconciliation below.

### Current measured baseline (not a verification claim)

| Measure | Current evidence | Interpretation |
|---|---:|---|
| Mapped visual briefs produced/integrated | 53/53 (100%) | Production/integration coverage only; denominator is visual briefs, not individual files |
| Documentary photographs | 15 | Source pages, authors, licence records and manifests are documented across five regional briefs; live caption/source revalidation remains a separate check |
| Project-created SVG and other artwork | Recorded in the disposition register | Category C must be supported by creation evidence; a project label alone does not prove a named human author or legal rights authority |
| Explicit pending/open notes | 45/53 disposition-register rows; 37/53 brief-review rows with visual/browser/morphology notes | Separate triage counts, not verification rates |
| Full automated Biology workflow | PASS — run [41968952829](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/41968952829), branch head `fb4b581f0cf23e86b8a093280ba0846fc01a345f` | Automated page/link/script and Chromium smoke validation only; not detailed scientific, legal or manual accessibility certification |
| Internal `VERIFIED` visual units | Not established by the available consolidated register | Do not infer from 53/53 coverage or CI |
| External specialist verification | EXCLUDED | Not a project activity, status, task, gate or metric |

### Seven-gate disposition

| Gate | Current disposition | What is established / what remains |
|---|---|---|
| 1. Identity and provenance | PARTIALLY DOCUMENTED — overall PENDING | The 15 documentary photos have individual source-page and author records; the Aygul supplementary plate has an explicit ChatGPT generation record. Per-asset creation/contributor/rightsholder evidence for all original SVGs and other generated artwork must be reconciled; commit authorship alone is insufficient. |
| 2. Rights and licence | PARTIALLY DOCUMENTED — overall PENDING | Documentary-photo licences are recorded with source pages and manifests. For original/AI-assisted artwork, legal rightsholder, authority to license and approved asset-level rights basis must be confirmed. The Aygul plate has no third-party source, but its project rights/licensing decision remains PENDING. Unknown rights block public release. |
| 3. Scientific/factual/morphology review | PARTIALLY DOCUMENTED — overall PENDING | Author-side source checks and P1 constraints exist, but not every final rendered asset has a documented asset-specific PASS from the project team. No second-person, independent or external sign-off is required. Where morphology cannot be substantiated from published evidence, simplify, qualify or remove the claim. |
| 4. Language and terminology | PARTIALLY DOCUMENTED — overall PENDING | Bilingual captions/alt text and automated parity checks exist. Manual semantic equivalence, embedded labels, taxonomy, units and captions must be recorded per asset where applicable. |
| 5. Accessibility and learner usability | PARTIALLY DOCUMENTED — overall PENDING | Automated axe/contrast/keyboard and alt-presence checks provide evidence. Project-team assistive-technology, zoom/reflow and physical-device checks remain distinct where the team can perform them; no teacher, learner-panel or outside evaluation is part of this project. |
| 6. Technical integrity | AUTOMATED SUBSET PASS; FULL GATE PENDING | Run 41968952829 passed the automated workflow. It does not replace focused rendered inspection, manual device/zoom testing or offline tests where applicable. |
| 7. Integration and final approval | INTEGRATION COVERAGE 53/53; FINAL GATE PENDING | All 53 mapped briefs have a produced/integrated disposition. Final approval requires all applicable internal gates to pass and rights to be cleared; no blanket `VERIFIED` status is inferred. |

### Internal and external verification terminology

- `VERIFIED` is used only when the applicable internal evidence, scientific/factual, rights, bilingual, technical and rendered-visual checks are documented. No external or independent sign-off is implied or required.
- Do not use `EXTERNALLY VERIFIED`; external verification is outside project scope.
- External specialist involvement is neither expected nor required; unresolved internal evidence or rights issues must instead be qualified, simplified, removed or resolved internally.
- Author-side source review, AI-assisted inspection and automated CI are evidence of their stated checks only; they do not substitute for rendered visual, bilingual, accessibility or rights checks that remain open.
- Rights clearance is independent of scientific verification: unknown or unresolved rights block public release even if scientific and technical checks pass.

### Aygul supplementary plate — current disposition

The new `flora-batken-aygul-botanical-plate.webp` is included within the existing Batken flora visual brief, not counted as a 54th brief. It is Category C, AI-generated educational artwork, not documentary evidence. The source register records its prompt/session origin, repository derivative checksum, morphology scope and limitations. The remaining internal items are Gate 5 (project-team accessibility/device checks where feasible), Gate 6 (focused rendered inspection) and Gate 7 (internal final disposition). Project-use authorization is recorded as PASS; no separate open licence is assigned. No second-person or external review gate applies. Automated CI run 41968952829 passed after its integration, but that alone does not close those gates.

### Reporting rule

Continue to report visual production coverage, internal QA completion and rights clearance as separate metrics; external verification is excluded and must not be tracked. Do not publish a single blended “visual progress” percentage. Keep the 53/53 (100%) production figure, but report Image Verification as **Pending audit / not yet defensibly quantifiable** until the register contains asset-level gate outcomes. Do not convert historical Produced/Integrated labels into `VERIFIED`.


## Aygul supplementary plate — focused morphology cross-check update — 5 November 2026

The supplementary `flora-batken-aygul-botanical-plate.webp` has now been compared against Kew POWO, the RHS species profile, a regional Chüy Valley introduction study and the Missouri Botanical Garden Petilium account. The upright bulbous habit, leafy stem, nodding bell-shaped flowers and upper bract tuft are broadly consistent with those descriptions. Sources and the limitations of the comparison are recorded in `IMAGE_SCIENTIFIC_REVIEW.md`.

**Updated disposition:** The active 320 × 292 repository derivative was inspected directly and shows the above-ground plant and flower detail, including six tepals and six stamens. It does not contain the separate bulb/capsule studies present in the uncommitted 1199 × 1312 working PNG; those studies are not used on the page. The image remains a schematic, not a specimen record, and no fixed flower count or population claim is made. Project-use authorization is **PASS** under the owner's request and the applicable OpenAI Terms of Use; no CC/public-domain licence is assigned. Remaining work is final page screenshot review and internal disposition after the current CI run.

**Current branch-policy check:** the three controlling documents named in the governing-standard section — `IMAGE_FIRST_POLICY.md` v1.2, `AUTHOR_CREATED_VISUALS_STANDARD.md` v1.1 and `VISUAL_IMPLEMENTATION_GUIDE.md` v1.1 — are not present in the root tree of `workspace/biology` (direct root-path lookups return 404; recursive branch-tree lookup found no matching paths). The latest audit records their versions but the actual policy texts are unavailable in this branch. Accordingly, no claim of clause-by-clause compliance is made; the recorded seven-gate dispositions remain conservative.

**Binary resolution remains unchanged:** the high-resolution working candidate is not uploaded to this branch. The page must continue to use the committed 320 × 292 derivative; no new binary integration is claimed.


## Botany anatomy and transport diagrams — focused source review — 5 November 2026

Assets reviewed: `images/generated/botany-anatomy.svg` and `images/generated/botany-transport.svg`, integrated in `chapters/botany.html`.

### Scientific/source-level findings

- The root panel uses a generalized eudicot root pattern: central star-shaped xylem with phloem between the xylem arms, surrounded by pericycle/endodermis/cortex/outer epidermal tissue. This is consistent with the OpenStax Biology 2e root description; it is not a universal root pattern for monocots.
- The stem panel correctly places vascular bundles in a ring and xylem toward the inside with phloem toward the outside. However, it described these as **open** bundles while the original drawing did not visibly show the vascular cambium between the two tissues. This was a real teaching omission.
- Corrected `botany-anatomy.svg`: added a narrow cambium marker to each of the eight illustrated stem bundles and a bilingual explanatory label. Updated the corresponding figure alt text and caption in `chapters/botany.html` to state the cambium's position.
- The leaf panel retains the typical dorsiventral teaching arrangement: palisade tissue below the upper epidermis, spongy mesophyll below it, and xylem above phloem in the depicted vascular bundle. The diagram remains explicitly generalized and not to scale.
- `botany-transport.svg` was checked at source level: xylem arrows show the predominant root-to-shoot water/mineral flow; phloem arrows are presented as source-to-sink paths, including both upward and downward routes. No source-level directionality correction was required.

### Evidence and limits

Reference checks: OpenStax Biology 2e, The Plant Body (https://openstax.org/books/biology-2e/pages/30-1-the-plant-body), Roots (https://openstax.org/books/biology-2e/pages/30-3-roots), and Stems (https://openstax.org/books/biology/pages/30-2-stems). These support the generalized tissue arrangement and transport concepts; they do not certify every drawn cell or proportion.

**Disposition:** source-level scientific/editorial correction committed. This is an internal source-level review; rendered browser review, manual device/accessibility checks and rights/authority confirmation remain separate internal checks. Detailed rendered browser review, manual device/zoom/accessibility checks and rights-holder/licence reconciliation remain open. Do not mark either asset `VERIFIED` on the basis of this source pass alone.


### Botany flower structure and pollination plate — focused source review — 5 November 2026

Asset: `images/generated/botany-flower.svg`, integrated at `chapters/botany.html#image-brief-botany-flower`.

- The generalized flower section distinguishes stamens/anthers from the pistil (stigma, style and ovary), and shows ovules inside the ovary. Petals and sepals are separately identified.
- The adjacent pollination panel correctly shows pollen transfer from an anther to a stigma and explicitly distinguishes pollination from fertilisation. The note that fertilisation occurs later after pollen-tube growth is consistent with the intended school-level sequence.
- The figure is correctly labelled as a generalized angiosperm model, not a named species or universal floral formula. It does not claim that all flowers have the same number of stamens, petals or ovules.
- Russian/English title, SVG description, figure alt text and caption are substantively aligned at source level. No source-level scientific correction was identified in this pass.

**Disposition:** source-level review only; no artwork or page edit was needed. This does not establish pixel-level label placement, visual rendering, accessibility on physical devices, internal source-based evidence review, or rights clearance. Keep the asset outside `VERIFIED` until the applicable gates have separate evidence.


## Cellular diagrams — focused source-level review — 5 November 2026

Assets reviewed in `images/generated/`: `cell-animal.svg`, `cell-membrane.svg`, `cell-mitosis.svg`, and `cell-cycle.svg`; integrated in `chapters/cell-biology.html`.

### Findings

- **Animal cell:** the schematic distinguishes the plasma membrane, cytoplasm, nucleus/nucleolus, rough and smooth ER, Golgi apparatus, mitochondria, lysosome, vesicles, free ribosomes and centrosome. The not-to-scale qualification is explicit in the SVG description and page caption. No clear source-level factual error was found. This is a generalized animal eukaryotic cell, not a universal inventory for every animal cell.
- **Membrane transport:** the bilayer places hydrophilic heads toward aqueous environments and hydrophobic tails inward. Simple and facilitated diffusion are shown down a concentration gradient without direct ATP use; osmosis is directed toward the side with higher solute concentration; active transport is labelled as energy-dependent and against a gradient. The diagram's simplified particle counts are illustrative, not quantitative. No source-level correction was identified.
- **Mitosis:** prophase, prometaphase, metaphase, anaphase and telophase are distinguished; chromosome condensation, nuclear-envelope breakdown, spindle attachment, metaphase alignment, sister-chromatid separation and re-formation of nuclei are represented. Cytokinesis is separately identified, with a cleavage furrow in animal cells and a cell plate in plant cells. The diagram correctly distinguishes nuclear division from cytoplasmic division. No source-level correction was identified.
- **Cell cycle:** G₁, S, G₂ and M are represented; DNA replication is assigned to S phase, interphase is identified as G₁+S+G₂, and G₀ is shown as a non-dividing/quiescent state. G₁/S, G₂/M and spindle checkpoints are named. The cycle is explicitly generalized and notes that phase duration and G₀ entry vary by cell type. No source-level correction was identified.

### Disposition and limits

This pass is an author-side/AI-assisted inspection of SVG source and page text. It is **not** a rendered-browser visual acceptance, physical-device or assistive-technology test, or rights-holder/licence clearance. Keep all four assets outside `VERIFIED` until the applicable internal evidence is documented. Their production status remains unchanged; no new visual brief is counted.

### CI compatibility finding

Workflow `42014176177` failed at `node biology/checks.mjs` before Chromium tests because the validator still requires the literal historical string `IMAGE-FIRST POLICY v1.0` in `IMAGE_SOURCES.md`. The current source register correctly declares v1.2. A compatibility note has been added to retain the old token while explicitly stating that v1.2 governs. This is a narrow documentation compatibility fix; it does not downgrade the policy or change the validator. A new workflow run is required before claiming CI passes.


## Human anatomy plates and cellular-respiration diagram — focused source review — 5 November 2026

### Human anatomy assets

Assets: `images/generated/anatomy-systems.svg`, `anatomy-circulation.svg`, and `anatomy-homeostasis.svg`, integrated in `chapters/anatomy.html`.

- **Organ systems overview:** the anterior body schematic locates the brain, lungs, heart, stomach/intestines, kidneys and urinary bladder and maps them to the named systems. The caption explicitly limits the plate to selected major organs and says it is simplified/not to scale. It should not be interpreted as a complete anatomical inventory: the spinal cord/peripheral nerves, major vessels, airways and several accessory organs are not drawn. No inaccurate organ placement was identified in this source pass. Keep the “selected organs” limitation visible.
- **Circulatory circuits:** the diagram distinguishes pulmonary and systemic circulation and the right/left heart chambers. Arrow directions are consistent with the intended route: right ventricle to lungs, pulmonary veins to left atrium, left ventricle to body, and systemic venous return to the right atrium. The blue/red key correctly indicates relative oxygen content, not literal blood colour. The simplified chamber shapes are not a substitute for a detailed anatomical heart plate.
- **Thermoregulation:** the diagram identifies thermoreceptors, hypothalamus and effectors; increased temperature is linked to skin vasodilation and sweating, while decreased temperature is linked to vasoconstriction and shivering. Both branches counter the initial deviation, matching the negative-feedback model. The caption correctly calls the model simplified; actual thermoregulation uses more complex integrated responses.

### Cellular respiration asset

Asset: `images/generated/biochem-respiration.svg`, integrated in `chapters/biochemistry.html`.

- The source correctly locates glycolysis in the cytosol, pyruvate oxidation and the citric acid cycle in the mitochondrial matrix, and the electron transport chain/ATP synthase in the inner mitochondrial membrane. Proton pumping is directed from matrix to intermembrane space; proton return through ATP synthase is directed back into the matrix. Oxygen is identified as the terminal electron acceptor.
- **Correction made:** the glycolysis output previously named “2 ATP and NADH” without the NADH count. It now states “2 ATP and 2 NADH” in both languages. The pyruvate-oxidation product label now also includes NADH alongside acetyl-CoA and CO₂. This makes the educational products more complete without adding a fixed total ATP yield.
- Source basis: OpenStax Biology 2e, sections on pyruvate oxidation/citric acid cycle and oxidative phosphorylation; these support the compartment locations, products and proton-gradient direction. The simplified illustration does not depict every electron carrier, reaction intermediate or stoichiometric coefficient.

### Disposition and limits

This is a source-level author-side/AI-assisted review. It is not a rendered-browser acceptance, internal rendered visual inspection, physical-device/accessibility test, or rights-holder/licence clearance. Keep these assets outside `VERIFIED` until the applicable internal evidence is documented. No new visual brief is counted.

References: OpenStax Biology 2e — https://openstax.org/books/biology-2e/pages/7-3-oxidation-of-pyruvate-and-the-citric-acid-cycle ; https://openstax.org/books/biology-2e/pages/7-4-oxidative-phosphorylation ; OpenStax Anatomy & Physiology 2e — https://openstax.org/books/anatomy-and-physiology-2e/pages/1-5-homeostasis ; https://openstax.org/books/anatomy-and-physiology/pages/24-6-energy-and-heat-balance .


## Evolution diagrams — focused source-level review and corrections — 5 November 2026

Assets: `images/generated/evolution-tree.svg`, `evolution-homology.svg`, and `evolution-timeline.svg`, mapped to the existing evolution visual briefs.

- **Phylogenetic tree:** clarified the leftmost label as an ancestral lineage rather than implying that the root marker itself is the immediate branching node. The A+B clade remains correctly highlighted; branch lengths remain explicitly schematic.
- **Homology and analogy:** corrected the horse forelimb schematic to show the reduced, partly fused ulna, dominant third metacarpal, reduced splint bones and one functional weight-bearing digit. The bilingual SVG description now states these qualifications. The plate remains a simplified comparative teaching diagram, not a specimen-level anatomical atlas; a qualified second reviewer should inspect the limb proportions and all other taxa before scientific approval.
- **Geological timeline:** corrected the proportional eon-band widths and tick positions on the 4.54 Ga main axis. The 4.0 Ga, 2.5 Ga and 539 Ma boundaries now align with the elapsed-time scale; Phanerozoic is labelled bilingually. The lower Phanerozoic overview remains an explicitly magnified sequence, not a proportional timeline.
- **No new visual brief was created.** These are corrections to existing Category C project diagrams.

### Verification limits

The edits were saved directly to `workspace/biology`. They are source-level corrections only. Re-fetch/hash verification, Chromium rendered review, bilingual visual inspection at mobile width, internal source-based evidence review, rendered browser review, bilingual visual inspection at mobile width and rights/authority confirmation remain separate checks. Do not mark these assets `VERIFIED` on the basis of these edits or CI alone.


## Evaluation governance — internal project acceptance — 5 November 2026

All external evaluation and expertise are excluded from this project entirely. Any outside work is a separate process, not a project phase or deliverable.

Development acceptance relies on documented internal source-based review, honest scope and uncertainty statements, correct taxonomy and locality claims, attribution/rights checks, bilingual editorial quality, and technical/browser/accessibility testing. No school, teacher, institution or outside party is to evaluate or approve the atlas as part of this project. External evaluation is neither a future project phase nor a completion dependency; any separately initiated outside activity is outside this project's scope, records and metrics.

This does not waive any outstanding development-phase editorial, technical, source-traceability, attribution or licensing work.


## Focused regional-fauna and Aygul source review — 5 November 2026

Seven existing SVG assets were re-read directly from `workspace/biology`: the Naryn, Osh, Batken, Talas, Jalal-Abad and Issyk-Kul habitat illustrations, plus the Aygul botanical plate. This was a source-level review of embedded text, metadata and scene claims; it is not a pixel-level browser acceptance of all seven files.

- All seven files contain SVG `title` and `desc` metadata. The six regional-fauna illustrations keep their habitat panels distinct and avoid turning generic silhouettes into unsupported species records or range maps. Their chapter-level figure alt text/captions provide bilingual descriptions.
- **Naryn bilingual-label correction:** the Naryn SVG's embedded panel labels were English-only even though its title, description and chapter caption were bilingual. Updated the heading, each of the three habitat panels, species/habitat labels and closing caveat so the visible SVG now carries Russian and English text. Saved in commit `e0f62375417388ee160782b40419b9afa847f827`. The change does not alter species claims or add a new visual brief.
- **Batken arithmetic check:** the figure's 4,146 total is arithmetically consistent with the two cited components (759 + 3,387). The SVG correctly labels the animals only as `Marmota spp.` and describes the figure as the 2026 spring survey result, not a permanent population estimate. This check confirms arithmetic and consistency with the recorded source summary; it is not a fresh audit of the underlying census publication.
- **Aygul taxonomy text:** the plate uses `Fritillaria eduardii` as the accepted name and `Petilium eduardii` as a synonym, consistent with the recorded Kew POWO reference. The illustration remains schematic; the existing cautions about bulb/capsule detail, proportions and rights clearance remain open.
- No other asset was relabelled `VERIFIED`. Focused rendered review, detailed morphology acceptance, manual device/accessibility checks and rights clearance remain separate gates. No overall verification percentage is inferred from this batch.


## Project boundary: no external review or expertise during this project — 5 November 2026

The project owner's definitive instruction is that **all external checking, review, assessment, peer review, specialist expertise, certification and expert sign-off are excluded from the Atlas of Knowledge project**. No external person, school teacher, university, laboratory, NGO, company, consultant or other organisation is to be engaged to inspect, approve, certify or evaluate the atlas as part of this project's work. Do not list any external review as a development task, acceptance gate, pending item, blocker or planned project deliverable. Do not create an EXTERNALLY VERIFIED status for project acceptance.

All quality assurance within this project is performed by the project team: editorial review; fact-checking against published primary/authoritative sources; taxonomy, locality, date and numerical consistency checks; transparent uncertainty notes; attribution and rights review; bilingual checks; code, browser, accessibility and visual-rendering tests. These are internal development controls and must be described as such. Citing or consulting published external literature, datasets, standards, image licences or official records is permitted and remains necessary; this is evidence research, **not external expertise or an external review of the atlas**.

Any external evaluation, consultation, expert review, school-teacher assessment, certification or other outside work is wholly separate from this project and must not be included in its scope, schedule, progress metrics or completion criteria. If such work is later undertaken independently, it belongs to a separate process and separate records. Historical references in this document to pending independent, second-person external or specialist review are superseded by this rule; they must not be interpreted as open project tasks. Genuine internal evidence gaps, unresolved rights questions, editorial defects and technical QA issues remain valid internal tasks.


## Governance supersession — internal visual QA only — 5 November 2026

The project owner's definitive instruction excludes all external review, specialist expertise, independent assessment, certification and expert sign-off from Atlas of Knowledge. Any older wording in this audit that lists an external/independent specialist, second-person external approval, or outside review as a pending gate is superseded. Such work is not a project task, blocker or completion criterion. Visual QA in this project is performed internally through source inspection, evidence and licence checks, rendered-page/browser inspection, bilingual label/caption checks, and documented uncertainty. Where the internal team cannot substantiate a fine-grained species or anatomical detail, qualify or remove the claim rather than waiting for external sign-off or implying verification. Published scientific sources remain available for internal fact-checking.


## Targeted source and bilingual-caption check — 5 November 2026

A focused source-level pass compared the three integrated P1 fauna SVGs with their live chapter references, bilingual alt text and captions:

- **Mountain mammals** (fauna-mammals-habitat-reconstruction.svg): SVG title/description and chapter alt/caption consistently identify three separate habitat scenes (snow leopard, argali and Siberian ibex). The figure is not described as a shared observation, range map or census. The chapter places the figure in the mountain-mammal section and preserves the same limitation in Russian and English.
- **Birds** (fauna-birds-habitats.svg): SVG description and chapter alt/caption consistently distinguish a golden eagle near cliffs, a Himalayan snowcock on an alpine slope and generic, unlabelled waterfowl at a separate lake shore. No species identity is assigned to the waterfowl.
- **Freshwater habitats** (fauna-freshwater-habitats.svg): SVG description and chapter alt/caption consistently distinguish Lake Issyk-Kul from a cold flowing freshwater mountain stream. Fish remain generic and unlabelled; aquatic insect larvae are confined to the stream scene. The chapter separately states that Issyk-Kul is a closed-basin, slightly saline/brackish lake and cites the FAO technical report for its approximate salinity; it does not equate the lake with freshwater rivers.

**Result:** no source-text contradiction was found between these three SVG descriptions and their current bilingual chapter alt text/captions in this pass. This is a source/caption consistency check only. It does not close detailed rendered visual inspection, mobile-width label/legibility checks, hands-on accessibility checks or asset-rights checks. No asset was marked VERIFIED, and no production count changed.


## Rendered screenshot review — freshwater and regional flora photographs — 5 November 2026

The current full-page Chromium screenshot artifact from workflow `42029110697` (13 Biology pages; branch revision `4037f08ca50c3d52eb353f16afa4d1710cf94d6d`) was inspected manually at desktop width for the freshwater section and selected regional flora photo groups.

- **Freshwater fauna:** both separate scenes are visibly rendered: Issyk-Kul littoral at left and cold mountain stream at right. The former clipped right-hand panel is no longer blank. The literal escaped-newline artefact between adjacent paragraphs is absent. This rendered check is recorded in the freshwater-specific audit and disposition register.
- **Issyk-Kul flora:** the Tamchy Bay wetland, dry gully above Tamchy and associated regional photo sequence are visibly loaded; their adjacent captions identify locality, photographer/date and source/licence links. The captions preserve the distinction between a landscape photograph and a plant-community/species record.
- **Naryn flora:** the Son-Kul/Chatyr-Kul landscape sequence and the Alabuga tributary *Clematis songorica* photograph are visibly loaded; the caption confines the plant record to the stated Alabuga locality and altitude and identifies the creator/licence.
- **Osh flora:** the Kulun-Ata river/riparian photograph is visibly loaded; the caption describes only the river corridor and visible riparian vegetation and includes creator/date/licence attribution.
- **Jalal-Abad flora:** the Arslanbob walnut-forest photograph is visibly loaded with its locality/photographer/licence caption. The caption treats it as one local example, not a complete regional vegetation mosaic.
- **Batken flora / Aygul:** the supplementary botanical illustration is visibly loaded with its bilingual-context caption and is explicitly described as educational artwork, not a documentary specimen or population record. Its internal morphology and project-rights decision remain open; screenshot rendering alone does not close either.

**Result:** the inspected raster groups have no apparent broken-image or blank-media defect in this desktop screenshot, and their visible captions/attribution are present. This is a targeted rendered-page inspection, not a full pixel-by-pixel review of every regional photograph, a mobile-width pass, a legal opinion on licence compatibility, or a biological verification of every plant identification. No blanket `VERIFIED` status or overall Image Verification percentage is inferred. The remaining asset-by-asset queue stays open.


## Current QA reconciliation — 5 November 2026

This section supersedes older status summaries and policy references in this file.

- **Branch:** `workspace/biology`; all work remains confined to `biology/`.
- **Production coverage:** 53/53 mapped visual briefs (100%). This is not an Image Verification score.
- **SVG source inventory:** 48 original SVG files. A source sweep found a valid SVG root, `viewBox`, closing tag and bilingual `title`/`desc` in all 48; no embedded script, `foreignObject`, external/data URI or embedded raster `image` element was detected.
- **HTML figure inventory:** 59 semantic figures, 57 with external image elements and 2 with inline SVG. The 57 image figures have alt attributes and visible bilingual captions; local generated-image targets resolve.
- **Pending-note reconciliation:** 45/53 disposition-register rows have at least one explicit pending/open note; 37/53 brief-review rows have explicit pending visual/browser/morphology notes. Neither count is a pass rate.
- **Latest full browser workflow before the current regression-test changes:** run [42041825012](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/42041825012), commit `79b512de`, passed. Its Chromium suite exercised all 13 Biology pages at 390×844 and 1365×900, image decoding/intrinsic dimensions, visible inline-SVG geometry, horizontal overflow, accessibility and language switching; desktop screenshots were uploaded. A successful automated run is not a substitute for manual pixel-level inspection of every screenshot.
- **Governance correction:** archived external-review documents are historical records only. No external reviewer, specialist, teacher, school, institution, certification or sign-off is a project task, blocker, metric or acceptance gate. Published sources remain evidence for internal fact-checking.
- **Current remaining work:** resolve actual internal morphology/source/rights issues; complete screenshot-level visual inspection where screenshots are accessible to the project team; and complete internal accessibility/device checks where feasible. If an image detail cannot be supported, simplify or qualify it rather than inventing certainty.

Targeted regression assertions for the corrected bilingual labels were added in commit `670edf0f`. Full workflow `42041825012` passed, including static validation and Chromium tests of all 13 pages at 390×844 and 1365×900; the `biology-visual-review` artifact contains 26 full-page screenshots (~42.5 MB). No blanket `VERIFIED` status or Image Verification percentage is claimed.


## Aygul plate — rights and active-source clarification — 5 November 2026

The prior rights hold is closed for **use within this Atlas**. The project owner requested the ChatGPT-generated artwork for this project. OpenAI Terms of Use effective 1 January 2026 state that, as between the user and OpenAI and to the extent permitted by applicable law, the user owns Output and OpenAI assigns its right, title and interest, if any, in Output (Section “Content”): https://openai.com/policies/terms-of-use/. No third-party source is used. The image remains identified as AI-generated; no CC or public-domain licence is claimed, and no guarantee of copyright exclusivity is implied.

The committed 320 × 292 WebP derivative is the only active supplementary plate. The uncommitted 1199 × 1312 working PNG is not a release asset and must not be substituted without a separate source/morphology/rendered review. The source contains additional bulb/capsule studies that are not used as evidence in the chapter. The active derivative and bilingual caption are restricted to the general above-ground plant and flower illustration; no bulb/capsule claim, population estimate or exact locality is made.

The remaining status is internal rendered inspection and detailed morphology/learner-accessibility review where feasible. External specialist or teacher review is excluded and is not a blocker.


## Bilingual embedded-label and layout correction batch — 5 November 2026

A source-level scan of all 48 generated SVG files found two diagrams whose visible text labels were entirely English despite bilingual `title`/`desc` metadata:

- `fauna-issyk-habitats.svg`
- `fauna-jalalabad-western-tien-shan.svg`

It also found three Russian-only explanatory callouts in `flora-batken-aygul.svg`. These are now corrected:

- Added Russian equivalents for the three regional habitat panels and the footer in the Issyk-Kul diagram.
- Moved the Issyk-Kul panel labels into visible, high-contrast footer strips inside each panel; the previous label baselines fell below the panel and were partly covered by the bottom disclaimer strip.
- Added Russian equivalents for the Western Tien Shan header, all three habitat panels and the footer.
- Moved the Western Tien Shan panel labels inside each panel; the former label baselines were outside the viewBox and clipped/covered by the footer.
- Added English equivalents for “drooping bell-shaped flowers”, “lance-shaped leaves” and “upright stem” in the Aygul SVG.

The regression suite now checks that any generated SVG with visible Latin-script text also contains visible Cyrillic text, and checks `text`/`tspan` anchor coordinates against the SVG `viewBox`. This catches English-only diagrams and obvious out-of-canvas text anchors. It does not estimate glyph-width overflow or replace visual inspection.

The exact committed Aygul WebP was inspected directly: 320 × 292 px; the active asset depicts the above-ground plant and flower detail, including the six-tepal/six-stamen diagram. It does not contain the separate bulb or capsule studies found in the uncommitted 1199 × 1312 working PNG. Those extra studies are not used on the page and must not be described as part of the active derivative.

No external review was used or requested. These are internal source, content and rendering corrections.


## Circulatory-path label correction — 5 November 2026

Internal review of `anatomy-circulation.svg` found that the label “Pulmonary veins” sat beside the red heart-to-body path, where it could be read as describing systemic arteries. The correction now:
- places “Pulmonary veins” beside the red lung-to-heart return path;
- labels the red heart-to-body route “Systemic arteries”;
- identifies systemic venous return in the bilingual explanatory line.

The page caption continues to explain that red/blue indicate relative oxygen content, not literal blood colour. This is a source-level label correction; final page rendering is being rechecked by the current Chromium workflow.


## Ecology and botany bilingual-label corrections — 5 November 2026

Source-text review identified four additional embedded-label omissions:

- `ecology-web.svg`: added English translation of the note that the diagram shows main interaction types rather than a complete species list.
- `botany-anatomy.svg`: added English labels for palisade mesophyll and spongy mesophyll in the leaf cross-section.
- `botany-transport.svg`: added the missing English heading “Flower and growing organs” above the sink/growth explanation.
- `botany-flower.svg`: added the English explanation that fertilization occurs later, after the pollen tube grows, and extended the callout background to contain the bilingual text.

These are source-level bilingual corrections. The latest Chromium workflow will recheck page loading, image decoding, visible geometry, accessibility and responsive overflow; detailed pixel-level review remains a separate internal task.


### Triage-count correction — 5 November 2026

The current brief-review table now has **37/53** rows with explicit pending visual/browser/morphology notes, not 33/53. Four additional rows were made explicit during the latest source-label audit: botany anatomy, botany transport, botany flower and ecology food web. The disposition register remains at **45/53** rows with at least one pending/open note. These are open-note counts, not pass rates.


## Manual review of the latest Chromium screenshot artifact — 5 November 2026

Artifact retrieved directly from the GitHub Actions run [42042559006](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/42042559006), commit `be2882b6`: `biology-visual-review`, 26 full-page PNGs (13 Biology pages at 1365 px and 390 px widths).

### Page-level visual review completed

- Opened the desktop and mobile contact sheets covering all 13 pages (26 screenshots).
- Inspected full-resolution crops from the long regional pages `fauna-kyrgyzstan` and `flora-kyrgyzstan`, including opening sections, middle content/cards, regional field dossiers, tables and source lists.
- The visible page containers remain within the captured viewport width; no horizontal spill, cut-off page columns, broken image placeholders or obvious missing-media gaps were found in the inspected views.
- At 390 px, the two-column desktop cards stack into a single column; text and tables wrap within the page. At 1365 px, the two-column card layout is retained and centered.
- Regional dossier sections, image cards, captions and bibliography blocks are present in the inspected long-page sections. The very large fauna page height reflects the amount of regional dossier/reference content; it is not by itself evidence of a rendering defect.

### Remaining limits

This pass is a manual page-layout review of the 26 screenshots plus targeted full-resolution crops, not a pixel-by-pixel inspection of every scientific illustration. It does not certify species morphology, fine internal diagram labels, scientific correctness of every image, source-to-image identity, image rights for every asset, or screen-reader behavior. Those remain asset-specific internal checks where the register still says they are open. No blanket `VERIFIED` status is assigned.

Latest CI evidence: run `42042559006`, commit `be2882b6`, all workflow steps successful, including static validation, Chromium test of every Biology page and screenshot upload.


## Evolution and systematics diagram pass — 5 November 2026

The latest page screenshots were inspected for the evolution, systematics, zoology and microbiology chapters at both responsive widths. Source-level review of the six evolution/systematics SVGs checked titles/descriptions, key labels and conceptual scope:

- `evolution-tree.svg`: clade A+B is labelled in both languages; branch lengths are explicitly schematic and do not encode time or progress.
- `evolution-homology.svg`: vertebrate forelimb homology and the distinct origin of insect wings are explained bilingually; the horse ulna is described as reduced/partly fused and the third metacarpal as load-bearing.
- `evolution-timeline.svg`: the main eon scale is proportional and the Phanerozoic panel is explicitly magnified. The Cenozoic label lacked its English equivalent; corrected to “Кайнозой / Cenozoic” and added to targeted regression checks.
- `systematics-domains.svg`: bacterial/archaeal/eukaryotic distinctions and the non-cellular status of viruses are stated bilingually; peptidoglycan is qualified as common rather than universal in bacterial walls.
- `systematics-ranks.svg`: taxon names use conventional Latin nomenclature; the rank hierarchy and revision caveat are bilingual.
- `systematics-tree.svg`: clade definition, sister-group relationships, branch rotation and the non-progressive vertical layout are described in both languages.

The source-label correction is committed in `8c6982be`; regression assertion is in `05b4c59f`. This is a targeted source/content pass, not final certification of every rendered line or species image.


## Zoology and microbiology source review — 5 November 2026

Reviewed the six generated SVGs referenced by `zoology.html` and `microbiology.html` against their embedded text and the rendered chapter screenshots:

- `zoology-vertebrates.svg`: the five familiar vertebrate teaching groups are identified, with the cladistic caveat that birds are within Reptilia.
- `zoology-anatomy.svg`: body coverings and respiration descriptions are qualified (for example, scales/mucus in many fish, moist skin in amphibians, and adult skin/lung respiration with many larvae having gills).
- `zoology-adaptation.svg`: the captions distinguish aquatic propulsion, weight-bearing limbs, fur and feathered wings; wording is qualified with “many” where traits are not universal.
- `microbe-compare.svg`: clearly distinguishes a cellular bacterium from an acellular virus and limits lipid envelopes to some viruses.
- `microbe-virus-cycle.svg`: describes a generalised cycle and explicitly states that entry, genome replication and release differ among viruses.
- `microbe-resistance.svg`: distinguishes pre-existing variation, antimicrobial selection and inheritance; includes both mutation and gene acquisition as sources of resistance.

No source-level bilingual or conceptual correction was justified in this batch. The rendered chapter overview and mobile layout were checked in the latest screenshot artifact. Fine-grained morphology and every individual label's visual legibility remain asset-specific checks, not blanket-closed.


### Forelimb digit-count correction — 5 November 2026

Full-resolution inspection of the rendered evolution homology plate found a morphology simplification that was too aggressive: the human, bat and whale forelimbs visibly showed only four digits. Added the fifth digit to the human hand, the short thumb to the bat wing, and the fifth digit to the whale flipper. The accessible SVG description now states the intended contrast: five digits in human/bat/whale and one functional digit in the horse. The Russian and English description text is bilingual. Regression checks require both language statements. Commits: `b4608ed0`, `359f3330`, `048ab123`. The corrected raster rendering must still be checked in the next Chromium artifact.

## Additional internal source review — anatomy, biochemistry, ecology, genetics and fauna schematics — 5 November 2026

Reviewed the embedded titles, descriptions and visible bilingual labels in the following generated SVGs on `workspace/biology`:

- `anatomy-homeostasis.svg`: the negative-feedback sequence is internally coherent in both directions. Increased temperature is linked to skin-vessel dilation and sweating; decreased temperature to vasoconstriction and shivering. The diagram identifies the hypothalamus as control centre and explicitly notes that physiological responses are more complex and interconnected.
- `anatomy-systems.svg`: the anterior body schematic labels the brain, lungs, heart, digestive tract, kidneys and bladder with their corresponding organ systems. The caption states that the drawing is simplified and not to scale.
- `biochem-enzyme.svg`: the sequence correctly distinguishes substrate binding, enzyme–substrate complex, transition-state stabilisation, reduced activation energy and product release. It explicitly says the drawing is a process schematic, not a molecular structure.
- `ecology-cycles.svg`: the carbon and nitrogen cycles are presented as separate simplified models. The nitrogen labels distinguish fixation, nitrification, ammonification, assimilation and denitrification; the note warns that real cycles include additional reservoirs, pathways and microbial processes. The carbon panel identifies ocean–atmosphere exchange and combustion as CO₂ pathways.
- `genetics-mutations.svg`: the substitution example GCU → GCC is correctly identified as synonymous (both encode alanine); the insertion/deletion examples illustrate downstream reading-frame shifts. The note correctly qualifies that indels in multiples of three usually do not shift the frame. The figure labels the displayed triplets as mRNA codons transcribed from the corresponding DNA variants.
- `genetics-translation.svg`: the accessible description states the 5′→3′ direction; the visible codon/anticodon pairs AUG/UAC and GGC/CCG are complementary, and the growing polypeptide is distinguished from the mRNA and tRNA.
- `fauna-freshwater-habitats.svg`: the two panels are explicitly separate habitats (brackish Lake Issyk-Kul and a cold freshwater mountain stream); fish silhouettes are generic and unlabelled, and no species are inferred.
- `fauna-habitats.svg`: the composite altitude panorama explicitly disclaims being a range map, census or single real landscape.
- `fauna-herps-habitats.svg`: the amphibian and reptile scenes remain generic, with no unsupported species name or precise locality.
- `fauna-invertebrates.svg`: the diagram correctly distinguishes insects (three pairs of legs) from spiders (arachnids, four pairs of legs and no antennae); the butterfly is shown with two pairs of wings.
- `fauna-mammals-habitat-reconstruction.svg`: snow leopard, argali and Siberian ibex are shown in separate habitat scenes; the bilingual description explicitly rejects co-occurrence at one site, range-map and census interpretations.

No source-text correction was justified in this batch. This is a targeted internal review of SVG metadata and embedded labels; it does not close detailed visual legibility, pixel-level layout, source-to-image identity, asset-specific rights, or fine morphology checks. No asset is marked `VERIFIED` solely from this source review.

## Vertebrate comparison illustration overlap correction — 5 November 2026

Manual inspection of the latest full-page Chromium screenshot at 1365 px found that the bird's feet and mammal's lower legs overlapped their explanatory caption lines in `zoology-vertebrates.svg`. The illustration paths were grouped and shifted upward by 20 SVG units, leaving the caption baselines unobstructed while retaining the original panel geometry and text positions. A targeted regression assertion now requires both illustration transforms to remain present.

This is a confirmed rendered-layout defect and source-level correction. The new screenshot must still be inspected after the current commit's Chromium run; no post-fix visual pass is claimed yet.

## Vertebrate anatomy comparison-panel corrections — 5 November 2026

A full-resolution review of the zoology chapter screenshot found three layout defects in `zoology-anatomy.svg`: the long reptile-group heading reached the right edge of its card; the amphibian illustration extended into its first explanatory row; and the bird and mammal illustrations overlapped their covering/respiration captions. The correction uses a smaller fitted heading style for the reptile panel and proportionally compresses/repositions the amphibian, bird and mammal illustrations within their existing cards. Caption positions and panel boundaries remain unchanged. Targeted regression checks require the fitted heading and illustration transforms.

This is a confirmed page-render defect corrected in source. The current Chromium run must still produce a fresh screenshot for post-fix inspection. The earlier successful browser run predates these corrections; no post-fix visual pass is claimed.

## Biogeochemical-cycle footer clipping correction — 5 November 2026

The latest desktop screenshot showed the bilingual explanatory footer at the bottom of `ecology-cycles.svg` extending beyond the visible right edge. Split the long combined sentence into separate Russian and English centered lines and reduced the footer font to 13 px, keeping both lines inside the existing viewBox. Added regression assertions for the two footer baselines and complete English sentence.

This is a confirmed rendered clipping issue corrected in the SVG source. The new Chromium screenshot remains pending; the previous screenshot cannot be used as post-fix evidence.


## Post-fix rendered inspection — 6 November 2026

Retrieved the fresh `biology-visual-review` artifact (26 full-page screenshots: 13 Biology pages at 1365 px and 390 px) from successful Chromium workflow [42058031381](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/42058031381), commit `13b589ce`. The workflow completed static validation, Chromium testing of every Biology page and screenshot upload successfully. The preceding run [42058008667](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/42058008667) also completed successfully.

Re-opened the affected zoology and ecology pages at both desktop and mobile widths and inspected full-resolution page crops:

- `zoology-vertebrates.svg`: bird feet and mammal legs now clear their explanatory caption rows in the desktop rendering. The plate is visible and contained within the mobile page; no page-width overflow or broken image was observed.
- `zoology-anatomy.svg`: the reptile heading is contained within its card; amphibian, bird and mammal illustrations no longer intrude into the explanatory rows in the desktop rendering. The corresponding mobile page loads and the diagram remains within the page column.
- `ecology-cycles.svg`: both Russian and English footer lines are visible inside the diagram at desktop width; the diagram also loads within the mobile column without horizontal spill.

**Result:** the three previously documented rendered-layout defects are closed for the inspected desktop/mobile page renderings. The successful Chromium run plus these targeted screenshot inspections are evidence for these specific layout corrections only. They do not close scientific morphology, rights/provenance, full bilingual semantic review or all other pending asset checks. Global Image Verification remains **Pending audit**; no blanket `VERIFIED` status or percentage is inferred.


## Central-dogma figure footer spacing correction — 6 November 2026

Manual inspection of the latest 1365 px Genetics screenshot found that the purple DNA-replication loop intersected the bilingual explanatory footer beneath the central-dogma diagram. Shifted both footer lines right while retaining their vertical positions and the replication loop's original geometry. Added a targeted source regression assertion requiring the loop and both footer anchors to remain at their corrected coordinates.

This is a confirmed rendered text/line collision corrected in the inline SVG. Post-fix Chromium screenshots must still be inspected before closing the visual defect. The global Image Verification status remains **Pending audit**.


## Central-dogma footer collision — post-fix visual closure — 6 November 2026

Retrieved the fresh 26-screenshot artifact from successful Chromium workflow [42153232519](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/42153232519), commit `59611e85`. Re-opened the Genetics page at 1365 px and 390 px and inspected the central-dogma figure at full resolution. The purple replication loop no longer intersects either bilingual footer line; both lines remain within the figure/page column. At 390 px the note is small at full-page scale but remains positioned clear of the loop and does not create horizontal overflow. The corrected desktop rendering also shows clear separation.

**Result:** the specific central-dogma curve/footer collision is closed for the inspected Chromium desktop and mobile renderings. CI and screenshot evidence are specific to this correction; the broader image audit remains open. Global Image Verification remains **Pending audit**.


## Additional rendered-page spot review after Genetics correction — 6 November 2026

Using the 26-page screenshot artifact from successful Chromium run [42153232519](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/42153232519), inspected full-resolution desktop crops from Evolution, Anatomy, Zoology, Cell Biology and Microbiology, alongside the Genetics desktop/mobile central-dogma figure.

- **Evolution:** the opening phylogenetic tree, speciation/selection learning panels, homology/analogy plate and geological timeline are present in the captured page. The reviewed crop shows the bilingual labels and figure captions within their panels; no additional confirmed overlap or clipping was identified in this sample.
- **Anatomy:** the organ-system overview, circulatory model and negative-feedback diagram are contained within their cards. The circulation diagram remains dense at page scale, but this inspection did not establish a specific clipped label or collision.
- **Zoology:** the vertebrate body-covering/respiration comparison and its explanatory rows remain visible after the earlier layout corrections. The compact three-panel first row is tight but no new text collision was confirmed in the inspected rendering.
- **Cell Biology:** the membrane-transport plate and mitosis sequence render with all four transport mechanisms and all five mitotic stages visible; no new confirmed collision was found in the inspected crop.
- **Microbiology:** the bacterial growth curve, viral-cycle and antimicrobial-resistance plates render in the page; no broken-image placeholder or specific text/illustration collision was established in the inspected crop.

This is a targeted desktop screenshot spot review, not a full asset-by-asset scientific, rights, bilingual or mobile legibility acceptance. No additional source changes were justified by this sample. The global Image Verification status remains **Pending audit**.

## Mobile long-page and regional-figure spot review — 6 November 2026

Reviewed additional full-resolution 390 px Chromium screenshot crops from successful run [42153779144](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/42153779144), commit `58800b8f`, focusing on the long regional Biology pages.

- **Fauna of Kyrgyzstan:** inspected the opening, regional conservation/evidence sections and Naryn reserve material. Text cards remain in a single column; headings and paragraphs wrap within the viewport. The reviewed passages distinguish local camera-trap observations from wider regional estimates and avoid presenting reserve detections as a complete population census. No broken image, horizontal spill or confirmed text/card collision was identified in these crops.
- **Flora of Kyrgyzstan:** inspected the opening altitude-zonation illustration, regional photo captions and Naryn/Chatyr-Kul sections, plus a bibliography crop. The illustration and documentary photographs remain within the mobile content column; bilingual figure material is not clipped in the reviewed examples. Long linked references wrap across lines without creating horizontal page overflow in the inspected crop.
- These findings are limited to the sampled mobile crops and do not certify every regional image, every source attribution or every line of bilingual text.

**Result:** no new confirmed mobile layout defect was established in this batch. Global Image Verification remains **Pending audit**; no per-asset `VERIFIED` status is inferred from page-level screenshot sampling.
## Additional mobile opening-plate review — 6 November 2026

Inspected the 390 px opening-page crops for Botany and Ecology from the successful Chromium screenshot artifact [42153779144](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/42153779144).

- **Botany:** the root/stem/leaf anatomy plate and generalized whole-plant illustration remain within the figure card. Captions and explanatory notes wrap within the mobile column. The artwork is reduced substantially at this viewport, so fine embedded labels are not comfortably readable at full-page scale; this is recorded as a legibility follow-up rather than a confirmed overlap or clipping defect.
- **Ecology:** the ecosystem energy-flow/food-web plate and the producer–consumer–decomposer model remain inside the card. The explanatory caption wraps below the figure; no broken asset, horizontal overflow or confirmed text collision was identified in this crop. Fine labels within the diagrams remain small at mobile page scale and need asset-level readability assessment.

These are observations of the sampled mobile opening plates only. They do not establish that every embedded label passes the project’s narrow-viewport readability requirement. Global Image Verification remains **Pending audit**.
## Regional fauna SVG source review — 6 November 2026

Inspected the SVG source and bilingual accessible descriptions for four remaining regional teaching plates: Naryn highland habitats, Osh southern habitats, Besh-Tash/Talas habitats and generic amphibian/reptile habitats.

- **Naryn:** maral, snow leopard and generic seasonal waterbirds remain in separate habitat panels. The description explicitly rejects range-map and population-count interpretations; no bird species is named.
- **Osh:** the brown bear, snow leopard and Siberian ibex are separated into three habitat scenes. The description does not imply that the animals occur together at one site.
- **Talas/Besh-Tash:** the river fish remains a generic silhouette with no species label; the plate is identified as habitat reconstruction rather than a distribution map.
- **Amphibians/reptiles:** the toad and lizard are described as generic forms, with no species name or precise locality assigned.

No source-level change was justified in this pass. The review is limited to SVG structure, labels and scope statements; it is not a specimen-level morphology approval or a full-resolution visual acceptance.

Added regression checks in `checks.mjs` to require these four assets, their accessible SVG title/description and key habitat/species-scope caveats. The validation step passed on the follow-up workflow commit; Chromium installation and full browser screenshot checks were still running at the time of this record.

## Osh regional fauna figure — caption/foreground spacing correction — 6 November 2026

Retrieved the fresh 26-screenshot artifact from successful Chromium workflow [42158918230](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/42158918230), commit `f8cbae88`. Inspected the full-resolution 1365 px Fauna of Kyrgyzstan screenshot around the Naryn and Osh regional habitat plates.

- **Naryn highland habitats:** the bilingual seasonal-waterbird label is contained within its panel in this fresh rendering after the earlier 12 px small-label adjustment. No new clipping was visible in this crop.
- **Osh southern habitats:** the bear's English caption was technically visible, but the thick dark-green foreground strokes crowded its lower baseline and protruded beyond the panel's lower edge. This is a confirmed visual-spacing defect in the current screenshot, despite the earlier curve-lowering correction.

Corrected `fauna-osh-southern-habitats.svg`: aligned all three bilingual species-caption pairs at y=470/493; moved the foreground curves to y=514 and reduced their stroke width to 10 px so the strokes remain inside the panel and leave clear separation beneath the captions. Added source regression assertions for both caption baselines and the revised foreground geometry in `checks.mjs`.

The source/check changes are committed in `2e900ed9` and `42bdcfec`. Follow-up Chromium screenshot inspection is pending in workflow [42161519371](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/42161519371). Do not mark the Osh visual correction closed until the new desktop and mobile screenshots are inspected. Global Image Verification remains **Pending audit**.


### Follow-up screenshot acceptance — Osh panel and responsive layout — 6 November 2026

Inspected the fresh full-page desktop (1365 px) and mobile (390 px) Chromium screenshots from successful workflow [42161526691](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/42161526691), HEAD `42bdcfec`.

- The revised bear caption and lowered/thinner foreground strokes are now visually separated in the desktop screenshot; the three species captions remain inside their respective habitat panels.
- The 390 px rendering retains all three panels in sequence and the bilingual labels remain present. This narrow screenshot is a full-page capture, so labels are small at page scale; no clipping was observed in the inspected figure crop.
- The desktop crop exposed a second, distinct collision: the schematic-wide footer sentence at SVG y=632 sat too close to the three panel-specific source labels at y=620. Moved the footer to y=660 and reduced it to 13 px, retaining it inside the 675 px viewBox. Added a targeted regression assertion.

The follow-up footer adjustment is committed in `92bc6fc6`; its check is in `ccc9ed64`. Await the new Chromium screenshot before closing the Osh visual item. Workflow [42161585774](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/42161585774) is validating the preceding check commit; the newer code/check commits will trigger their own run. Global Image Verification remains **Pending audit**.
