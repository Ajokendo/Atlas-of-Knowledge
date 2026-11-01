# Editorial Standard Adoption — Geography

**Working branch:** `workspace/geography`  
**Discipline folder:** `geography/`  
**Adopted reference:** root-level `EDITORIAL_STANDARD.md` in `atlas-of-knowledge-integration`  
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

- The 217 visual IDs are briefs/slots, not 217 completed illustrations.
- Four SVG assets are created and embedded; all four still require final scientific/editorial sign-off.
- The Markdown chapter files contain Russian and English material, but the landing-page language switch does not yet filter chapter content.
- A rendered chapter reader, full browser testing, mobile-device testing, keyboard/contrast audit and final deployment verification remain separate tasks.
- Source links and claims still require systematic verification; a bibliography heading is not proof that every citation supports its adjacent statement.
