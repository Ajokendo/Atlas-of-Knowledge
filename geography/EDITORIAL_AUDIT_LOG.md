# Geography Editorial Audit Log

**Audit date:** 2026-11-01  
**Working branch:** `workspace/geography`  
**Scope:** Initial targeted audit of Chapters 01, 02, 17, 24 and 26. This is an editorial tracking note, not a declaration that the atlas has passed final scientific review.

## Verified items

### Chapter 24 — Seven Regions of Kyrgyzstan

- The population values in the comparison table for 1 January 2026 match the National Statistical Committee's open-data table:
  - Batken: 605.3 thousand
  - Jalal-Abad: 1,379.9 thousand
  - Issyk-Kul: 554.3 thousand
  - Naryn: 316.2 thousand
  - Osh Region: 1,438.5 thousand
  - Talas: 282.9 thousand
  - Chuy: 983.7 thousand
- The same official table lists Bishkek separately at 1,358.6 thousand and Osh city separately at 484.9 thousand. The chapter correctly explains that these two republican-level cities are not included in the corresponding oblast totals.
- The chapter correctly uses **Manas** as the current name of the city formerly called Jalal-Abad. Law No. 200 was signed on 17 September 2025; the official presidential website confirms the renaming.
- The chapter's reference to the 2024 administrative-territorial changes is supported by Law No. 128 of 18 July 2024.

**Editorial issue to address:** The NSC population series shows a marked change between 2023 and 2024 for Osh Region, Chuy Region, Bishkek and Osh city. The table's 2026 cross-section is confirmed, but historical comparisons must not interpret these changes as demographic migration without checking the statistical boundary/classification metadata. Add a clear comparability note when the chapter discusses population trends.

## Issues found in the sampled chapters

### Chapter 01 — Geography as a Science

- The file is a useful introductory draft with objectives, concepts, methods, map literacy, worked examples, activities and review questions.
- The English headings and selected English worked examples are present, but most explanatory prose is Russian-only. This does not yet meet the bilingual-parity standard.
- The bibliography is a starting list; links, editions and publication details still need checking.
- Illustration briefs are present and should be retained for the later illustration stage; do not create images during the current text-first phase.

### Chapter 02 — Earth's Geographic Envelope

- A substantial Russian-language text draft exists, with structured sections, tables and illustration briefs.
- The file itself states that scientific source verification, illustrations and final editing remain outstanding.
- English section headings do not constitute a complete English edition. Language parity remains to be checked.

### Chapter 17 — Geographic Location and Geological Evolution of Kyrgyzstan

- The chapter includes a bilingual introduction and substantial material on location, area, relief and geological evolution.
- The text appropriately flags the need to verify official area and extreme-point coordinates against a consistent national geodetic source.
- Exact coordinates and a dated authoritative source remain required before publication.

### Chapter 26 — Environmental Challenges and the Future of Kyrgyzstan

- The chapter distinguishes observations, policy commitments and scenarios, and warns against combining statistics from different periods or methodologies.
- The reported climate trend and NDC 3.0 targets require line-by-line source verification and exact citation to the relevant dated source documents.
- Forecasts must remain explicitly labelled as scenarios, not certainties.

## Sources checked

1. National Statistical Committee of the Kyrgyz Republic, open data: Resident population as of the beginning of the year (2022–2026): https://stat.gov.kg/ru/opendata/category/39/
2. National Statistical Committee of the Kyrgyz Republic, Population statistics: https://www.stat.gov.kg/ru/statistics/naselenie/
3. President of the Kyrgyz Republic, announcement on signing the law renaming Jalal-Abad to Manas, 17 September 2025: https://president.kg/kg/news/21/39594
4. Centralised Legal Information Bank of the Kyrgyz Republic, Law No. 128 of 18 July 2024 on administrative-territorial units at the level of aiyl aimaks and cities: https://cbd.minjust.gov.kg/4-5363/edition/12923/ru
5. Centralised Legal Information Bank of the Kyrgyz Republic, Law No. 200 of 17 September 2025 on renaming Jalal-Abad to Manas: https://cbd.minjust.gov.kg/4-5636/edition/36959/ru

## Next editorial sequence

1. Establish a reliable inventory and status matrix for all 26 chapters without rewriting or duplicating existing material.
2. Complete bilingual parity, beginning with Chapter 01, then proceed systematically.
3. Verify all dated statistical claims and administrative references in the Kyrgyzstan section.
4. Verify scientific claims and bibliographies in the general geography chapters.
5. Only after text and source audits, complete illustration production and web-navigation/accessibility checks.

**Status:** Initial targeted audit recorded. No chapter text was rewritten in this audit. No other discipline, portal, catalogue, publication setting or main branch was changed.


## Follow-up work — Chapter 23 (1 November 2026)

- Added a bilingual subsection **23.8.2, Recent Migration Patterns: Official Statistics and Mobility Estimates** to `chapters/23-population-and-settlement-of-kyrgyzstan.md`.
- Included the NSC migration balance series for 2021–2025 and the 2025 breakdown for seven oblasts plus Bishkek and Osh city; verified that the regional/city values sum to the national balance of 15,426.
- Added the NSC 2025 immigrant and emigrant counts (17,965 and 2,539) and explained that net balance, annual flows and the stock of citizens abroad are different measures.
- Added IOM DTM Baseline Mobility Assessment Round 7 (April 2026) estimates: 30,073 international migrant workers hosted in assessed communities, 70,340 internal migrants, 110,354 Kyrgyz nationals still abroad, and 85,197 return migrants. The text states the 1,151-community / 1,939-key-informant methodology and warns against summing these categories or treating them as census/register totals.
- The new material is bilingual and inserted into the existing migration section; no duplicate chapter was created.
- Sources: NSC open data https://stat.gov.kg/ru/opendata/category/6209/ and https://stat.gov.kg/ru/opendata/category/316/; IOM DTM https://dtm.iom.int/reports/kyrgyzstan-baseline-mobility-assessment-round-7-april-2026.
- The revised Chapter 23 was fetched again from `workspace/geography`; the new subsection, both language versions, tables and bibliography entry were checked.

**Chapter 23 update commit:** `a078b650d3eec23b0dc98c89ae98e29c33767eab`.
