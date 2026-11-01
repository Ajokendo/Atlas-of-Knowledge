# Bilingual source-parity audit — Atlas of Biology

**Audit date:** 1 November 2026  
**Branch:** `workspace/biology`  
**Scope:** the Biology index and all 12 chapter HTML pages.

## Results

| Page | Russian blocks | English blocks | Numeric multiset differences |
|---|---:|---:|---:|
| `index.html` | 6 | 6 | 0 |
| `botany.html` | 57 | 57 | 0 |
| `zoology.html` | 40 | 40 | 0 |
| `cell-biology.html` | 39 | 39 | 0 |
| `anatomy.html` | 37 | 37 | 0 |
| `genetics.html` | 44 | 44 | 0 |
| `microbiology.html` | 49 | 49 | 0 |
| `ecology.html` | 51 | 51 | 0 |
| `evolution.html` | 43 | 43 | 0 |
| `biochemistry.html` | 55 | 55 | 0 |
| `systematics.html` | 40 | 40 | 0 |
| `flora-kyrgyzstan.html` | 253 | 253 | 0 |
| `fauna-kyrgyzstan.html` | 433 | 433 | 0 |
| **Total** | **1,147** | **1,147** | **0** |

- All 13 pages have matching Russian/English content-block counts.
- Numeric-token multisets match in all 1,136 paired blocks. One fauna block places the same dates in a different sentence order; the values themselves match.
- The scientific-name sets inside the Russian and English content blocks match on all 13 pages. The Kyrgyzstan flora chapter contains 34 unique Latin-name strings in each language; the fauna chapter contains 69 in each.
- The fauna parity pass found and corrected a genuine scope omission: the Russian Himalayan Snowcock note now includes the same OSME Region List v10.1 (August 2024) and ITIS taxonomic-validity caveats as the English note. The same pass aligned the OSME 2019 reference, the count of 14 wildlife-related violations and the 112,363.5 ha reserve-area figure.
- These parity assertions are now part of `checks.mjs`: paired block counts, numeric-token multisets and scientific-name sets are checked automatically for every page.

## Limits

This is an author-side, source-level parity audit. It does not assess whether every sentence is idiomatic, elegant, age-appropriate or pedagogically equivalent, and it is not an independent professional translation/editing certificate. It forms part of the completed internal G5 audit; optional external copy-editing is not a required gate.


## Follow-up: Biochemistry control labels — 1 November 2026

A source-level review found that the interactive controls for enzyme/substrate matching, enzyme-activity factors, ATP reactions and cellular-respiration stages retained Russian-only labels after switching the page to English. The explanatory output changed language, but the controls themselves did not.

All 11 controls now contain paired RU/EN labels (the pH label is intentionally identical in both languages). The Biochemistry row and total above include these 11 new bilingual pairs. Automated static checks now require paired labels in all four control groups, and the Chromium smoke test checks that English labels are visible and Russian labels hidden after the language switch. These tests have been added to the workflow; they have not yet been executed in this session.


## Agreed G5 status — 2 November 2026

The internal G5 editorial/bilingual audit is complete (4/4 planned blocks, 100%). The measured structural parity results above remain bounded to block counts, numeric-token multisets and scientific-name sets; they do not claim sentence-by-sentence professional equivalence.
