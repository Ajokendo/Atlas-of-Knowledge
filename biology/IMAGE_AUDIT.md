# Biology image audit

**Policy:** Atlas of Knowledge IMAGE-FIRST POLICY v1.0  
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
| Independent specialist review | Not commissioned; do not describe author-side review as independent certification |

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

**Current result:** author-side brief/scientific constraints are documented; this consolidated pass does not claim independent expert validation of all 53 final rendered assets. Rows with pending visual/morphology notes remain open for focused human review.

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
| Focused final-art visual inspection | Assets with pending notes in `IMAGE_DISPOSITION_REGISTER.md` (33 rows explicitly retain pending visual/morphology/browser notes at this baseline) | Inspect actual rendered asset at desktop and narrow mobile widths; compare with approved scientific brief | Dated pass/fail entry per asset |
| Scientific morphology / scene review | Species-specific and regional wildlife/plant visuals | Verify diagnostic features, locality claims and ecological relationships; keep generic labels where identification is uncertain | Reviewer, evidence/source and decision |
| Bilingual semantic equivalence | All figures with RU/EN text | Compare caption, alt text, embedded labels, units and scientific names | RU/EN audit result per asset |
| Live attribution comparison | Third-party photo figures | Compare visible credit/source/licence links with the individual source page and licence terms | Dated rights check per source |
| Physical-device / assistive technology | 13 pages | Execute the separate manual test plan in the actual environments | Completed test record; never infer from CI |
| Offline availability | Local images and any future remote assets | Test offline behaviour only if offline support is an intended feature | Explicit result; currently not tested |

The count of 33 is derived from rows that explicitly retain pending visual, morphology or browser-validation notes in the current register. It is a triage count, not a claim that the remaining 20 have passed every manual gate.

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
- **Image Verification: Pending audit (percentage not yet defensible).** The register still contains 33 rows with explicit pending final visual, morphology or browser-review notes. No 100% verification claim is permitted until every applicable per-asset human check is recorded.
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

**Remaining distinction:** page-render visual QA has now been performed and the identified defects corrected, but Global Image Verification remains **Pending audit**. The remaining visual verification work is asset-specific: confirm fine biological morphology, scientific depiction, photo subject/caption match, and any source-specific caveats at image scale. Independent specialist review and the planned school/device feedback phase are also separate gates; they are not being falsely marked complete here.


## Documentary-photo preview review — 5 November 2026

A bounded visual review was carried out against the individual Wikimedia Commons file pages and their rendered image previews for the 15 accepted documentary photographs listed in the five regional manifests. Fourteen previews rendered successfully and were inspected; the Commons preview request for the Halys pit viper file returned an HTTP 400 and could not be visually assessed in this pass.

### Images visually inspected (14/15)

- **Chüy fauna:** red squirrel (*Sciurus vulgaris*) — the visible subject is consistent with the source caption; the animal occupies a relatively small part of the frame, so the photo is useful as a documentary example but not as a close diagnostic morphology plate.
- **Chüy habitats:** Ak-Suu gorge, Ala-Archa mountain landscape, Chong-Kemin rocky stream/meadow/woodland, and Chunkurchak red-sandstone canyon — all four previews match their broad landscape/habitat captions. They do not support species-level claims or abundance/distribution inferences.
- **Jalal-Abad flora:** Arslanbob walnut-forest landscape — the preview is consistent with a wooded Arslanbob landscape; it is not a close-up for identifying individual tree species. Keep the caption at habitat/landscape level.
- **Issyk-Kul flora:** Tamchy Bay wetland, dry gully above Tamchy, lakeshore sea-buckthorn shrub, and Karakol Valley spruce forest — each preview matches the stated setting. The dry-gully frame must remain a terrain example, not evidence of a named plant community. The sea-buckthorn image visibly shows a shoreline shrub; the spruce identification remains source-supported rather than independently diagnosed from this landscape-scale view.
- **Naryn flora:** Chatyr-Kul shoreline, Son-Kul lakeshore meadow, and *Clematis songorica* — the two lake photographs match their geographic landscape captions. The clematis preview shows flowering shoots consistent with the source's plant caption, but this visual review is not a specialist taxonomic determination.
- **Osh flora:** Kulun-Ata river corridor — the preview matches the caption's mountain stream/riparian habitat description; no individual tree species should be inferred from it.

### Still open

- fauna-chuy-pit-viper.webp: its source page identifies *Gloydius halys*, but the Commons image preview could not be retrieved in this pass. Do not mark its visual/morphology check complete until the actual image can be opened.
- The 14 successful inspections used Commons-rendered previews, not a fresh local pixel-by-pixel comparison of every committed WebP derivative. Existing manifest checksums and prior Chromium decode/visibility tests establish provenance and technical loading, not taxonomic certification.
- The two Rufous-naped Tit candidates remain excluded on the previously documented metadata conflict; they are not part of the 15 accepted-photo denominator.

**Result:** 14/15 accepted documentary-photo previews inspected in this pass; 1/15 visual check blocked by preview retrieval. No proven caption-to-scene mismatch was found in the 14 inspected previews. No image, caption or chapter content was changed as a result. Global Image Verification remains **Pending audit**; this sample does not close the SVG morphology review or independent specialist review.
