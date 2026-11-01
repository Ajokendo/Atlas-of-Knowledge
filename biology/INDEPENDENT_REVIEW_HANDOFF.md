# Independent reviewer handoff and acceptance protocol — Atlas of Biology

**Date:** 1 November 2026  
**Repository:** `Ajokendo/Atlas-of-Knowledge`  
**Canonical branch:** `workspace/biology`  
**Scope:** Biology subject area only; 13 bilingual HTML pages (index + 12 chapters).  
**Purpose:** operational handoff for independent scientific review (G4) and professional Russian–English editorial review (G5).

> This document prepares the review. It is not a review report, certificate, endorsement or publication approval. G4 and G5 remain open until independent reviewers complete the work and sign the records.

## 1. Reviewer package — files to provide

Provide reviewers with a read-only snapshot of the exact commit under review, not an evolving working copy. Include:

| Material | Repository path | Purpose |
|---|---|---|
| Main review brief and priority claims | `biology/EXTERNAL_REVIEW_PACKET.md` | Scientific questions, editorial scope and sign-off forms |
| Scientific and editorial standard | `biology/EDITORIAL-AND-SCIENTIFIC-STANDARDS.md` | Evidence, taxonomy, uncertainty, bilingual and attribution rules |
| Scientific author-side audit | `biology/G4_SCIENTIFIC_AUDIT_2026-11-01.md` | Prior checks, evidence trail and author-side decisions; not independent approval |
| Editorial author-side audit | `biology/G5_EDITORIAL_AUDIT_2026-11-01.md` | Corrections and coverage already completed internally |
| Bilingual structural parity | `biology/BILINGUAL_PARITY_AUDIT.md` | Paired block, numeric and scientific-name checks; not semantic proofreading |
| Kyrgyzstan species evidence | `biology/KYRGYZSTAN_SPECIES_AUDIT.md` | Regional records, taxonomy and evidence limitations |
| Biodiversity data standard | `biology/KYRGYZSTAN_BIODIVERSITY_DATA_STANDARD.md` | Rules for locality, status, dates, abundance and evidence |
| Image scientific briefs | `biology/IMAGE_SCIENTIFIC_REVIEW.md` and `biology/IMAGE_BRIEF_REVIEW.md` | Scientific constraints for future images; not approval of rendered assets |
| Image inventory and anchors | `biology/IMAGE_INSERTION_MAP.md`, `biology/IMAGE_DISPOSITION_REGISTER.md` | Exact 52 planned image IDs, target paths and current deferred status |
| Current checkpoint | `biology/PROGRESS_CHECKPOINT.md` | Gate status and limitations |

The reviewer snapshot must include all 13 page files:
- `biology/index.html`
- `biology/chapters/anatomy.html`
- `biology/chapters/biochemistry.html`
- `biology/chapters/botany.html`
- `biology/chapters/cell-biology.html`
- `biology/chapters/ecology.html`
- `biology/chapters/evolution.html`
- `biology/chapters/fauna-kyrgyzstan.html`
- `biology/chapters/flora-kyrgyzstan.html`
- `biology/chapters/genetics.html`
- `biology/chapters/microbiology.html`
- `biology/chapters/systematics.html`
- `biology/chapters/zoology.html`

The reviewer should receive the rendered site or a reproducible local copy as well as the source files, because wording, captions, language switching, navigation and interactive labels must be reviewed in context.

## 1A. Page-by-page assignment matrix

Use [`INDEPENDENT_REVIEW_PAGE_MATRIX.md`](INDEPENDENT_REVIEW_PAGE_MATRIX.md) as the operational assignment sheet for all 13 pages. It specifies page-level scientific scope, recommended specialist competence, Russian/English editorial focus, cross-page consistency checks and the 13 required signed page records. It also tracks the six P1 and four P2 entries in the priority claim register.

## 2. G4 — independent scientific reviewer

### Required competence

Assign a reviewer with demonstrable expertise in biology and the relevant subject areas. For the Kyrgyzstan biodiversity block, the reviewer should have relevant regional taxonomic, zoological, botanical, ichthyological, ornithological or conservation-science experience. A single generalist should not be represented as having independently verified specialist taxa outside their competence; use a second specialist or explicitly mark those claims deferred.

The reviewer must disclose institutional or personal conflicts of interest and confirm that they did not author the material being reviewed.

### Review sequence

1. Record the exact commit SHA, review date, files and sections examined.
2. Read the scientific standard before assessing individual claims.
3. Review all priority claims in Section 1 of `EXTERNAL_REVIEW_PACKET.md`, including the source conflicts listed there.
4. Check the underlying primary paper, dataset, official record or taxonomic authority—not only the Atlas summary or an author-side audit.
5. Check whether the stated locality, date, method, sample size, taxonomic identification and evidence type are supported.
6. Review the remaining scientific content in the assigned scope for unsupported generalisations, outdated taxonomy, false precision, missing caveats and incorrect mechanisms.
7. Record each finding with an exact file, heading or claim, a decision, supporting source and proposed replacement wording where needed.
8. Sign the disposition. Unresolved claims must remain qualified or be deferred; silence is not acceptance.

### Priority questions already identified

The reviewer must explicitly address the following items in the existing priority claim register:
- Son-Kul fish survey: fieldwork chronology and conflicting `Triplophysa` / `Diptychus` taxonomic combinations.
- Suusamyr fish survey: abstract's four-plus-one versus body/conclusion's four-total discrepancy and fish identifications.
- Kempir-Abad expedition: unpublished or pending identifications; no inference of a complete basin checklist.
- Argali genomic study: sample provenance and limits on geographic generalisation.
- Maral counts: incompatible 2024 totals from different sources and survey scopes.
- Tibetan Snowcock: range-edge suggestion versus confirmed Kyrgyz locality evidence.
- Common Crane at Issyk-Kul: nest/chick record, attribution and publication status.
- Black-necked Crane near Soek Pass: candidate observation lacking independently assessed primary evidence.
- Reptile and amphibian checklists: count/status inconsistencies and accepted-name questions.

These are review prompts, not pre-decided errors. The reviewer may accept, correct, qualify or defer each item, with reasons.

### G4 decision labels

- **Accepted:** evidence and wording are adequate for the stated scope.
- **Accepted with qualification:** claim is usable only with a specified limitation.
- **Correction required:** provide exact replacement wording and supporting evidence.
- **Deferred:** evidence is insufficient; specify what is missing and safe interim wording.
- **Out of expertise:** refer to a named specialist discipline; do not treat as accepted.

G4 acceptance requires all P1 items to have a documented disposition, all P2 items to have a documented disposition or justified deferral, no unresolved critical error in the reviewed pages, and a signed report identifying the reviewer’s expertise and sources consulted.

## 3. G5 — independent Russian–English editorial review

### Required competence

Use a professional bilingual editor or two qualified language editors working to one agreed glossary and style sheet. The review must be independent of the authoring and machine-translation pass. Russian and English must both be reviewed by a person competent to edit that language; fluency alone is not a substitute for professional editing experience.

### Review coverage

Review all 13 pages in both languages, including:
- body text, headings, learning objectives and summaries;
- tables, captions, glossary entries and scientific-name explanations;
- quizzes, feedback, button labels, form controls and interactive outputs;
- navigation, language-switch behaviour and accessible names;
- terminology, transliteration, units, dates, citations and attribution.

Use the parity audit as a navigation aid only. Matching block counts and numbers do not establish semantic, idiomatic or pedagogical equivalence.

### Required editorial checks

1. Scientific meaning and certainty are equivalent in Russian and English.
2. No translation adds or removes a condition, causal relationship, locality, date, estimate or degree of certainty.
3. Russian grammar, punctuation, terminology and educational register are natural and consistent.
4. English prose is idiomatic and consistent with the project’s British-English spelling baseline, except where official source titles or institutional names must remain verbatim.
5. Scientific names, common names, transliteration, units and proper nouns are consistent.
6. Terms such as occurrence, range, population, abundance estimate, sample count, native, introduced, historical record and confirmed local record are not conflated.
7. Sentences are understandable to the intended school-level audience without sacrificing scientific accuracy.
8. Citations support the exact claim and are not merely links to general homepages.
9. Corrections are supplied as exact replacement text, with file and location.

### G5 acceptance

G5 is accepted only when every page has been reviewed in both languages, all critical and major comments are resolved or explicitly accepted as documented exceptions, the editor supplies a final terminology/style list, and the editor signs the exact reviewed commit. Automated parity, spelling checks or author-side proofreading cannot close G5.

## 4. Comment severity and issue record

Use one issue per finding. Do not combine unrelated corrections into a general comment.

| Severity | Meaning | Required action before acceptance |
|---|---|---|
| Critical | Scientific misinformation, unsafe implication, materially false identification or major meaning reversal | Must be corrected or removed; no waiver for publication |
| Major | Material factual, taxonomic, geographic or bilingual error; missing qualification; misleading learning explanation | Must be corrected and rechecked |
| Minor | Local grammar, terminology, typography or clarity issue without material meaning change | Correct or record an explicit editorial decision |
| Suggestion | Optional improvement | Editor/author may accept or decline with brief rationale |

### Required issue fields

- Issue ID:
- Gate: G4 scientific / G5 Russian / G5 English / cross-language:
- Severity:
- Exact file and heading or unique text excerpt:
- Current wording / claim:
- Reviewer decision:
- Evidence or style authority (full citation, URL, DOI, dataset or collection record):
- Proposed replacement wording:
- Does the issue affect the other language? If yes, identify the paired passage:
- Status: Open / Corrected / Rechecked / Deferred / Rejected with rationale:
- Reviewer and date:

## 5. Version control and correction workflow

1. Freeze the review snapshot and record its full commit SHA in each reviewer report.
2. Reviewers return comments against that snapshot; they must not silently edit the live branch.
3. The project maintainer logs each finding in an issue register and applies accepted corrections on `workspace/biology` only.
4. Every correction affecting meaning is checked in both languages and, where relevant, in the interactive interface.
5. Run the appropriate automated and browser checks after corrections. Record the workflow run and commit; do not reuse an earlier green run as evidence for a later commit.
6. Send corrected passages or a new commit to the reviewer for recheck. Close an issue only when the reviewer accepts the correction or records a reasoned disposition.
7. Publish the signed G4 and G5 reports and update the checkpoint only after read-back verification from the canonical branch.

## 6. Separate release gates — do not confuse with G4/G5

The following work remains separate and cannot be closed by a scientific or language review:

- **52 illustrations:** all 52 are currently deferred. Each final image requires visual scientific review, correct target dimensions and format, provenance/licence, appropriate Russian and English alt text/caption, successful insertion at its exact anchor and read-back verification. A generated draft or concept image is not a completed asset.
- **Screen-reader testing:** test meaningful page structure, headings, landmarks, accessible names, image alternatives, language changes, focus order, dynamic announcements and keyboard-only operation with actual screen-reader/browser combinations.
- **Contrast:** measure text, controls, focus indicators, hover/selected states and charts against WCAG 2.2 AA criteria; record tool, page/state, measured ratio and result. Do not infer compliance from visual appearance.
- **Physical devices:** test representative real phones, tablets and desktop/laptop browsers at narrow and wide viewports, including touch, zoom, orientation, keyboard access and language switching. Record device, OS, browser, viewport, date and reproducible defects.
- **Final release:** rerun the complete test suite and browser checks against the final post-review, post-illustration commit. Independent G4/G5 sign-off does not certify these technical gates.

## 7. Reviewer sign-off form

### G4 — scientific reviewer

- Reviewer name and professional role:
- Relevant specialist expertise:
- Institution / affiliation:
- Conflict-of-interest statement:
- Commit SHA and date reviewed:
- Files / sections reviewed:
- Primary sources and taxonomic authorities consulted:
- P1 dispositions:
- P2 dispositions:
- Critical / major findings remaining:
- Deferred claims and safe interim wording:
- Final decision: Accept / Accept with qualifications / Re-review required
- Signature and date:

### G5 — bilingual editorial reviewer

- Reviewer name and professional role:
- Russian editorial qualification:
- English editorial qualification:
- Conflict-of-interest statement:
- Commit SHA and date reviewed:
- Pages reviewed in Russian:
- Pages reviewed in English:
- Style guide / terminology list used:
- Critical / major findings remaining:
- Corrections supplied and rechecked:
- Final decision: Accept / Accept with corrections / Re-review required
- Signature and date:

## 8. Current status and completion rule

At handoff preparation:
- Internal author-side G4 scientific audit: completed for its recorded scope; independent G4: **not received**.
- Internal author-side G5 bilingual/editorial audit: completed for its recorded scope; independent G5: **not received**.
- Planned illustrations: **52 deferred; 0 approved as integrated raster assets**.
- Screen-reader, contrast and physical-device certification: **not completed**.

Do not raise the controlled publication-readiness score or close G4/G5 solely because this handoff document has been prepared. Close each gate only after the required independent evidence, signed disposition and repository read-back are present.
