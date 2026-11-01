# G5 — Editorial and bilingual audit

**Date:** 1 November 2026  
**Canonical branch:** `workspace/biology`  
**Scope:** Russian–English editorial consistency, translation completeness, terminology, headings/navigation, learning objectives, glossaries, interactive text and reader-facing labels.

## Progress

**G5 progress: 25% — 1 of 4 review blocks completed.**

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

