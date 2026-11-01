# External review packet — Atlas of Biology

**Status:** prepared for external review; no independent sign-off has yet been received.  
**Working branch:** `workspace/biology`  
**Review scope:** 13 HTML pages (the Biology index and 12 chapters), with particular attention to the Kyrgyzstan flora and fauna chapters.

This packet defines the evidence and editorial work needed to close G4 and G5. It is not itself a review and must not be treated as approval.

## 1. Scientific review (G4)

### Review principles

For each claim, verify the taxon, accepted name and synonymy, locality, date, method, sample size, evidence type and source. Distinguish:

- a country-level checklist from a confirmed record in a named oblast or locality;
- a range map from a dated observation or specimen;
- a sample count from an abundance estimate;
- an author's identification from a taxonomically verified specimen;
- a national Red Data Book category from an IUCN Red List category;
- a historical record from current occurrence.

Do not silently normalize disputed names or resolve source discrepancies without documenting the authority and rationale.

### Priority claim register

| Priority | Claim requiring review | Questions for the reviewer |
|---|---|---|
| P1 | **Son-Kul fish survey (Sarieva, Konurbaev & Osmonov, 2023).** The abstract describes field visits in 2021–2023, while Methods lists 2020, 2021 and 2023. The paper reports processed samples of six fish taxa and uses the spelling `Triplophysa stoliczkae`. | Confirm the sampling chronology and lake/outflow locality assignments. Assess the `Triplophysa stoliczkae` / IUCN `T. stolickai` / Catalog of Fishes `T. elegans` conflict. The current Catalog of Fishes and ITIS treat `Gymnodiptychus dybowskii` as valid and `Diptychus dybowskii` as its synonym; assess the paper's `D. dybowskii micromakulatus` designation and whether voucher evidence supports it. Where possible, request voucher or genetic evidence. |
| P1 | **Suusamyr Valley fish survey (fieldwork 2024; published 2025).** The abstract says four recreational-fishing species plus one weed fish, while the body and conclusion report four species total. The paper names `Triplophysa stoliczkai` and `Diptychus gymnogaster`. | Resolve the 4+1 versus four-total discrepancy with the authors or original table. Confirm the `Triplophysa` identification. Verify that `Diptychus gymnogaster` is treated as a synonym of `D. maculatus` in the current catalogue and whether the local specimen determination is consistent. |
| P1 | **Kempir-Abad basin expedition (30 July–4 August 2026).** Osh State University reports 14 fish identifications, but its notice does not publish the complete taxon list; molecular-genetic analysis of samples from two taxa was pending. | Obtain the eventual list and laboratory results. Confirm which taxa were found in which of the five surveyed lower-river reaches. Do not infer that all 14 taxa occur in every river or that the press notice is a completed basin checklist. |
| P1 | **Argali genomic study and Dryad metadata.** The paper reports 88 samples collected in Kyrgyzstan and 72 retained after quality control; the linked dataset description indicates a Kyrgyzstan-and-Tajikistan provenance. The study reports 135,242 SNP markers and no Pamir Plateau samples. | Reconcile the article and dataset provenance using the supplementary table or authors. Confirm the sampled geographic scope before extending the genetic-unit conclusion to all Kyrgyz argali populations. |
| P1 | **Maral counts.** CAMCA's 2025 concept note gives 689 maral for Kyrgyzstan in 2024; the National Statistics Committee table gives 47 for 2024 and 61 for 2023. A 400–600 Naryn Valley range is a separate extrapolation. | Identify differences in method, spatial coverage and reporting. Do not average or combine the figures unless a defensible reconciliation is published. |
| P1 | **Tibetan Snowcock occurrence.** OSME describes a possible range edge into southern Kyrgyzstan, but the audit has not found a primary Kyrgyz locality record. | Seek a dated observation, specimen or authoritative national record. Until then, retain the taxon as an unresolved range-edge claim, not a confirmed national or oblast occurrence. |
| P2 | **Reptile checklist snapshot (19 October 2026).** The source header displays 44 species while its summary reports 43, with four unconfirmed. | Confirm the correct count and status of introduced, absent and unconfirmed taxa with the source maintainer. Do not silently reconcile the discrepancy. |
| P2 | **Amphibian checklist and Bufotes.** The dated country snapshot distinguishes resident and unconfirmed taxa; a 2021 study reports 209 adult male green toads from 14 localities and triploid hybrids. | Check current accepted names, the status flags in the GBIF-registered regional checklist, and the exact Kyrgyz localities supported by the study. Do not convert regional checklist inclusion into an oblast-level occurrence. |

### Required scientific review record

For every P1/P2 claim, the reviewer should return one of:

- **Accepted as written** — with the authority/source and reason.
- **Corrected** — with exact replacement wording, accepted name and supporting citation.
- **Qualified** — with the limitation that must remain visible.
- **Deferred / unresolved** — with the evidence still required and a safe interim wording.

A review is complete only when the reviewer identifies the materials examined, explains the taxonomic and geographic scope, and supplies citations or specimen/collection references sufficient for another specialist to reproduce the decision.

## 2. Bilingual editorial and release review (G5)

Review all 13 pages in both Russian and English. The review must be performed independently of the authoring pass. The author-side automated parity results are recorded in [`BILINGUAL_PARITY_AUDIT.md`](BILINGUAL_PARITY_AUDIT.md); that audit checks block counts, numeric-token parity and scientific-name sets, but is not an independent editorial sign-off.

### Editorial checklist

- Scientific meaning is equivalent in both languages; neither version adds certainty, scope or causal claims absent from the other.
- Russian grammar, punctuation, terminology and academic register are consistent and natural.
- English grammar, terminology and educational register are consistent and natural; avoid literal calques from Russian.
- Scientific names, author attributions, dates, units, geographic names and transliteration are consistent.
- Terms are used consistently: *species occurrence*, *range*, *population*, *abundance estimate*, *sample count*, *introduced*, *native*, *historical record*, *confirmed local record* and *national checklist* are not interchangeable.
- Every number has a date, source and evidence scope; no historical estimate is presented as current without support.
- Citations point to the specific claim they support; links open correctly and do not substitute a general homepage for a primary source.
- Headings, learning objectives, examples, quizzes, captions, control labels and explanatory notes are clear to the intended learner.
- The published pages are checked at mobile and desktop widths; keyboard focus, visible controls, accessible names and language switching are verified.

### Editorial review record

| Field | Reviewer response |
|---|---|
| Reviewer / editor | |
| Institution or professional role | |
| Russian-language qualification | |
| English-language qualification | |
| Date and version / commit reviewed | |
| Pages reviewed | |
| Terminology list or style guide used | |
| Corrections supplied (file, heading, exact wording) | |
| Unresolved items and recommended interim wording | |
| Final disposition | Accept / Accept with corrections / Re-review required |

## 3. Sign-off record

### G4 — Scientific review

- Reviewer name and relevant expertise:
- Institution / affiliation:
- Date:
- Files and claims reviewed:
- Taxonomic authorities and primary sources checked:
- Corrections or qualifications required:
- Unresolved / deferred claims:
- Reviewer disposition and sign-off:

### G5 — Bilingual editorial and release review

- Reviewer / editor:
- Russian and English qualifications:
- Date and commit reviewed:
- Pages reviewed:
- Corrections supplied:
- Mobile / desktop release review completed:
- Remaining issues:
- Reviewer disposition and sign-off:

## 4. Completion rule

G4 and G5 remain **open** until qualified independent reviewers complete and sign the relevant records. Preparing this packet, performing an author-side source audit, or passing automated checks does not substitute for independent expert or editorial approval.
