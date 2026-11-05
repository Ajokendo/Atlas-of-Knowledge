# Editorial Standard Adoption — Geography

**Working branch:** `workspace/geography`  
**Discipline folder:** `geography/`  
**Adopted reference:** root-level `EDITORIAL_STANDARD.md` in `main`  
**Reference blob SHA:** `38294a18c47e8127fdd25669d5d15b10b1887256`  
**Project-registry blob SHA:** `03537236951f30b0a6f3b79d011bcfd04cd5b652`  
**Adoption record date:** 2 November 2026

## Authority and scope

The shared standard is mandatory for Geography. This file records its adoption within the discipline workspace; it does not copy or modify the project-wide standard or registry. The common files remain under the authority of the central integration process.

The current Geography branch remains the only working branch for this discipline. Work is limited to `geography/`; no other subject folder, root portal file, catalogue, shared publishing setting or branch is changed.

## Applied review criteria

Each chapter and its related assets are reviewed against these criteria:

1. **Scientific accuracy:** definitions, classifications, causal explanations, dates, quantities, units, spatial scope, uncertainty and source quality.
2. **Clear teaching language:** accessible explanations without removing scientific meaning; unfamiliar terms defined at first important use; short and logically sequenced explanations.
3. **Learning sequence:** concepts introduced before they are used; progression from core idea to mechanisms, examples, applications and limitations.
4. **Examples and models:** examples are reproducible and appropriately scoped; analogies and simplified models disclose their limits.
5. **Russian–English parity:** equivalent explanations, definitions, examples, caveats, questions and activities in both languages; consistent terminology.
6. **Visual and interactive quality:** every asset has a stable ID, bilingual brief/caption, grounded source and date, licence, correct geography, legibility and text alternative; no placeholder is reported as a finished asset.
7. **Accessibility and usability:** semantic headings, keyboard operation, visible focus, contrast, meaningful labels, responsive layout and understandable feedback.
8. **Evidence and traceability:** sources support the adjacent claims; dynamic statistics are dated; unresolved verification is explicitly recorded; corrections are committed.

## Progress accounting

The audit distinguishes:
- **Inventory:** file and asset existence.
- **Structural review:** chapter hierarchy, numbering, duplicated or missing sections.
- **Bilingual review:** content parity, not merely the presence of English headings.
- **Scientific/source review:** claim-by-claim checks against cited primary or authoritative sources.
- **Visual review:** brief, data provenance, production, embedding and approval are separate statuses.
- **Technical/accessibility review:** static checks, browser tests and real-device checks are reported separately.

A chapter is not marked publication-ready merely because it has a complete outline, references or a bilingual heading. A visual is not approved merely because an SVG exists or renders.

Overall readiness will be reported only against a documented work matrix and verified tasks. No completion percentage is inferred from file count, word count or commit count.

## First audit finding

During the initial bilingual review, Chapter 01 had a Russian/English glossary table, but its English-language section did not provide English definitions for the key terms. A matching English-language Key Terms table has now been added under section 1.12.

Commit: `8ce1a147f3dfc1b07689355cd84658046501ae61`.

## Current known limitations

- The chapter-level inventory rows currently sum to 283 visual positions, but the exact unique-ID total remains unresolved because two Chapter 05 labels are not yet identified. These positions are briefs/slots, not completed illustrations.
- A direct repository scan found 54 local SVG assets across Chapters 01–05 and 18–20. File presence and basic SVG accessibility structure do not establish authorship, licence, scientific approval or final accessibility; many individual creator/rightsholder and project-licence records remain Unknown / PENDING.
- The Markdown chapter files contain Russian and English material, but the landing-page language switch does not yet filter chapter content.
- A rendered chapter reader, full browser testing, mobile-device testing, keyboard/contrast audit and final deployment verification remain separate tasks.
- Source links and claims still require systematic verification; a bibliography heading is not proof that every citation supports its adjacent statement.


## IMAGE-FIRST POLICY v1.1 — mandatory adoption

**Adopted:** 5 November 2026  
**Policy:** [IMAGE-FIRST POLICY v1.1](https://github.com/Ajokendo/Atlas-of-Knowledge/blob/main/IMAGE_FIRST_POLICY.md)  
**Reference branch:** `main`  
**Canonical-main status:** The policy is already canonical at the repository root on `main` (commit `bd3deb97`). This Geography document links to that source; do not copy or edit the universal policy in this subject branch.

Geography adopts the complete mandatory workflow, status vocabulary, evidence requirements, metrics, CI principles and derivative/inherited-material protocol in sections 1–10, including section 8.1. This record supplements but does not redefine the universal policy.

### Geography-specific extension

1. **Physical/topographic maps:** record projection, scale, CRS, orientation, elevation-data source, vertical datum, data date, resolution and accuracy limits.
2. **Climate/statistical maps:** record observation/reference period, units, source, spatial coverage, classification method and class intervals; explain colour and symbol meaning.
3. **Kyrgyzstan maps:** verify administrative names/boundaries against dated authoritative sources; record imagery dates, basin boundaries, glacier-outline provenance and limitations. Do not generalise local measurements into national claims.
4. **GIS/remote sensing:** record satellite/sensor, product, acquisition date, resolution, processing level, bands/indices, classification, validation and interpretation limits.
5. **Demography/economy:** record period, territorial coverage, denominator, collection method, and whether values are observations, estimates, model outputs or projections.
6. **Conservation-sensitive geography:** generalise sensitive species, nest, breeding-site and habitat locations where disclosure could increase poaching or disturbance; document the decision.
7. **Cartographic comparability:** explain differences in projection, scale, classification, boundary vintage and data period when maps are compared.

### Derivative and inherited-material protocol

Classify each asset as A — Original reuse, B — Adapted or C — Created, separately from rights status. The atlas-wide source relationship is not yet established comprehensively; do not label the atlas wholly original, derivative or mixed without evidence. Record source lineage and creator/rightsholder per asset. Unknown provenance, permission or adaptation rights remain Unknown / PENDING. Repository ownership does not establish authorship or permission. Do not repeat discovery searches for identifiable unchanged inherited assets solely to satisfy image-first; verify lineage, rights, accuracy, localisation, accessibility and rendering. Search for replacements when assets are missing, unsuitable, inaccurate, inaccessible, rights-restricted or need replacement. Translation of surrounding captions/alt text alone does not change the visual category; translation of embedded labels or other substantive visual edits is an adaptation.

**Current limitation (5 November 2026):** detailed or provisional IMAGE_SOURCES records now cover Chapters 01–05, plus a MISSING gap record for Chapter 09-G. Chapter 05's 40 embeds (20 per language, 20 unique URLs each) have source-level parity confirmed, but many rights/scientific checks remain pending. Chapters 06–08 and 10–26 must not be treated as source-verified until their individual records are completed.

### Required reporting

Report required/integrated counts, provisional Image Coverage, Image Verification, Image Gaps, A/B/C counts and separate rights, scientific, language/accessibility and technical results for each chapter and the atlas. Placeholders do not count as integrated. INTEGRATED does not mean VERIFIED. No overall percentage is assigned until IDs and evidence are reconciled.
