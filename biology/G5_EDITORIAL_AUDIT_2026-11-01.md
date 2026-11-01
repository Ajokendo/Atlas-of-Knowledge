# G5 — Editorial and bilingual audit

**Date:** 1 November 2026  
**Canonical branch:** `workspace/biology`  
**Scope:** Russian–English editorial consistency, translation completeness, terminology, headings/navigation, learning objectives, glossaries, interactive text and reader-facing labels.

## Progress

**G5 progress: 50% — 2 of 4 review blocks completed.**

The audit is divided into four equal blocks:
1. Main Biology index + Cell Biology + Genetics + Microbiology.
2. Biochemistry + Botany + Ecology.
3. Anatomy + Zoology + Systematics + Evolution.
4. Cross-chapter terminology, navigation, glossaries, interactive language switching and final consistency pass.

This percentage measures completion of the planned author-side G5 work. It is not an independent professional translation certificate.

## Block 1 — index, cell biology, genetics and microbiology (complete)

### Files reviewed
- `biology/index.html`
- `biology/chapters/cell-biology.html`
- `biology/chapters/genetics.html`
- `biology/chapters/microbiology.html`

### Structural bilingual checks

- Main index: 14 Russian and 14 English inline language spans after correction; regional flora/fauna cards now use paired language labels and descriptions.
- Cell Biology: 62 Russian and 62 English spans.
- Genetics: 85 Russian and 85 English spans.
- Microbiology: 71 Russian and 71 English spans.
- No duplicate HTML IDs found in these four files.
- The paired span counts are a structural check, not proof that every translation is semantically equivalent. The audit also inspected the main topic panels, learning objectives, glossaries, key interactive text and selected explanatory sections.

### Corrections committed

1. **Main index — regional biodiversity cards.** The Kyrgyzstan regional heading, explanatory subtitle, flora/fauna card titles and calls to action previously displayed Russian and English together rather than following the selected interface language. Converted these to paired `ru/en` spans. Restored concise bilingual card descriptions to preserve the original card structure.
2. **Main index — accessible diagram name.** The cell diagram's `aria-label` was Russian-only even after switching the page to English. It now updates between “Схема эукариотической клетки” and “Diagram of a eukaryotic cell” with the language control.
3. **Cell Biology — glossary precision.** The cytoplasm definition was phrased as contents between the plasma membrane and “nucleus”, which could blur the distinction between the nucleus and its envelope. Both languages now define it as the region between the plasma membrane and nuclear envelope, containing cytosol, organelles and other cellular structures.

### Editorial and terminology findings

- **Cell Biology:** checked the distinction between cell division, mitosis and cytokinesis; the language-specific descriptions of the cell-cycle stages; membrane transport vocabulary; learning objectives and the core glossary. The cytoplasm wording above was the clear precision correction.
- **Genetics:** checked the bilingual topic list and objectives against the DNA replication, transcription/translation, mutation, inheritance and biotechnology sections. Terminology such as semiconservative replication, leading/lagging strands, substitution/insertion/deletion, codon, allele and gene expression is used consistently in the inspected passages. Russian and English objectives remain aligned.
- **Microbiology:** checked the distinction between cellular microorganisms and viruses, Bacteria versus Archaea, viral replication, lytic/lysogenic cycles, antimicrobial resistance, horizontal gene transfer, microbial eukaryotes and microbiome terminology. The English text uses British forms such as “organisation”, “recognise”, “favourable”, “specialised” and “colonisation”; this is the style baseline to verify across the remaining chapters.
- **Index:** the ten field descriptions and regional links are present in both languages. The regional links now follow the language toggle rather than showing mixed-language card text.

### Terminology references consulted

- Russian National Library, *Biology: reference and bibliographic resources*, including the Glazko two-volume terminology dictionary, which provides English equivalents for Russian biology terms: https://nlr.ru/res/inv/guideseria/biolog/record_full.php?IDs=39921%2C21156%2C25081%2C27074%2C20717%2C45965%2C&record_ID=39921&rid=17809
- National Coordinating Center for the Regional Genetics Networks, *Glossary of Genetics Terms in Russian* (2023): https://nccrcg.org/resource/glossary-of-genetics-terms-in-russian/
- UNESCO Thesaurus, multilingual subject vocabulary for Biology and related disciplines: https://vocabularies.unesco.org/

These are reference aids for terminology, not substitutes for specialist review or a single mandatory style guide.

### Commits

- `325b3357d91c4738855e02a23df61880907db06e` — regional navigation and diagram accessible name.
- `58d139225d9c1f3cf1d7d0393e64f76cf956f158` — restore bilingual regional card descriptions.
- `9e60e7274057f6667e1cc03a3f7504da04217362` — cytoplasm glossary precision.

### Remaining work

- Blocks 2 and 3: full chapter-by-chapter editorial and bilingual review.
- Block 4: unify terminology and British-English spelling, compare all learning objectives/glossaries/navigation, audit interactive language switching and final cross-chapter consistency.
- External independent editorial/bilingual review remains recommended before publication.


## Block 2 — biochemistry, botany and ecology (complete)

### Files reviewed
- `biology/chapters/biochemistry.html`
- `biology/chapters/botany.html`
- `biology/chapters/ecology.html`

### Structural bilingual checks

- Biochemistry: 55 Russian and 55 English inline language spans.
- Botany: 76 Russian and 76 English spans.
- Ecology: 102 Russian and 102 English spans.
- No duplicate HTML IDs found in these three files.
- After corrections, the automated length-ratio screen found no unusually short/long paired language fragments in these three chapters. This is a screening heuristic, not a substitute for semantic proofreading.

### Corrections committed

1. **Biochemistry — terminology and glossary.** Standardised the prose spelling `oxidised` (British English) in the citric-acid-cycle explanation. Rephrased the Russian enzyme glossary definition so it reads naturally and accurately: the enzyme speeds a reaction without being consumed in the overall reaction. Corrected the English previous-chapter navigation label from “Evolution” to “Evolutionary Biology”, matching the Russian chapter title.
2. **Botany — scientific wording and translation completeness.** Corrected the angiosperm glossary: ovules are enclosed within the ovary and develop into seeds after fertilisation; the seed does not arise directly from the ovary. The English interactive descriptions of stem and leaf were expanded to preserve details present in Russian (xylem and phloem transport, source of sugars, CO₂ uptake, oxygen/water-vapour release and stomatal regulation). Standardised `fertilisation` in the prose. Improved the flower-structure heading and the light/water/CO₂ availability labels.
3. **Ecology — exact terminology.** Replaced the generic Russian button label “Дыхание” with “Клеточное дыхание” to match “Cellular respiration”. Standardised `oxidise` and `specialised` in the English prose to the British-English baseline. Corrected the next-chapter navigation label to “Evolutionary Biology”.
4. **Image-brief consistency.** The revised Botany flower-brief title was synchronised with both central image-production registers (`IMAGE_GENERATION_PLAN.md` and `IMAGE_INSERTION_MAP.md`) and its accessible label. An intermediate CI run failed because the updated in-page title and central plan were temporarily inconsistent; after synchronising the registers, the latest validation/browser run passed.

### Verification

- Latest full run: GitHub Actions `41313625525`, commit `d919115edce3e3174373fa79e206752f831490d5`.
- Static validation of all Biology pages, local links, bilingual numeric parity, scientific-name parity, image anchors and inline JavaScript: passed.
- Chromium installation, local server and browser smoke tests for every Biology page: passed.
- These are automated/browser smoke tests, not a full independent editorial assessment, screen-reader certification or exhaustive device/contrast review.

### Relevant commits

- `be019cd3c48c6fcbbc1ad3d9522fc304ce1a9432` — ecology wording and British English.
- `84f46a900d22ae553e9f084f3d1e235b373de5d0` — biochemistry glossary and spelling.
- `37610b7cd4282376fb20371ab5c55e1c0bcfeb9b` — angiosperm glossary precision.
- `0f5ab2bb1fb1a59b54a77512b2642730a36307a5` — fuller English stem/leaf interactive descriptions.
- `e1242b734f77b1b674467cf8e136563c26c92546`, `c0a5e8aa5a59e97ac9b75088eeb93a776325d187`, `f89790b89d0eccff4fbbeb91df471849dd056950` — navigation and interactive-label alignment.
- `5f4eee063e2114da3a8b568d3a00db5fa9ba153e`, `a5fae9b48818d9f5bfeae855f1c87d1e0a3765ef`, `d919115edce3e3174373fa79e206752f831490d5` — central image register and bilingual brief synchronisation.


## Block 3 — anatomy, zoology, systematics and evolution (complete)

### Files reviewed
- `biology/chapters/anatomy.html`
- `biology/chapters/zoology.html`
- `biology/chapters/systematics.html`
- `biology/chapters/evolution.html`

### Structural bilingual checks

- Anatomy and Physiology: 81 Russian and 81 English inline language spans.
- Zoology: 58 Russian and 58 English spans.
- Systematics: 41 Russian and 41 English spans.
- Evolutionary Biology: 58 Russian and 58 English spans.
- No duplicate HTML IDs found in these four files.
- No unusually short/long paired language fragments were detected by the length-ratio screen. This heuristic does not prove semantic equivalence.

### Editorial findings and corrections

1. **Anatomy and Physiology.** Checked the levels-of-organisation introduction, cardiovascular and respiratory vocabulary, kidney/nephron and homeostasis explanations, nervous-system terminology, and the newly expanded musculoskeletal/endocrine section against the learning objectives and glossary. Corrected the remaining American spelling in the English reference description from “organization” to “organisation”. The official OpenStax source title “Structural Organization of the Human Body” is intentionally retained verbatim.
2. **Zoology.** Checked the distinction between vertebrates and invertebrates, the umbrella/non-clade status of “invertebrates”, the vertebrate-group caveat that fish are paraphyletic and birds are nested within reptiles, and the new animal-behaviour section. Innate/learned behaviour, migration/communication and proximate/evolutionary explanations are paired correctly in Russian and English. The source title “Behavioral Biology” retains the publisher's official spelling; the chapter's own prose uses British “behaviour”.
3. **Systematics.** Checked the three-domain model alongside the qualified two-domain phylogenomic hypothesis, taxonomic rank hierarchy, binomial nomenclature, clade/common-ancestor vocabulary and phylogenetic-tree explanations. The quiz and explanatory text preserve the caveat that some phylogenomic models place the eukaryotic lineage within Archaea. “National Center for Biotechnology Information” is retained as the institution's official name.
4. **Evolution.** Checked the definitions of natural selection, genetic drift, heritable variation, homology, clades, common ancestry and speciation against the chapter's interactive models, quiz and learning objectives. British English spelling (including “colour” and “behaviour”) is used in chapter prose.

### Verification

GitHub Actions run `41313876648` on commit `614caf54dbf689d6a95df47bee7b55c99a4c6f58` completed successfully:
- static Biology page, local-link, bilingual numeric-parity and scientific-name checks passed;
- Chromium installed and local site started;
- browser smoke tests for every Biology page passed.

### Commit

- `614caf54dbf689d6a95df47bee7b55c99a4c6f58` — standardise British English in the Anatomy reference description.

