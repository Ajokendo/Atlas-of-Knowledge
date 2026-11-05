# Geography — IMAGE-FIRST visual audit

**Working branch:** `workspace/geography`  
**Scope:** `geography/` only  
**Audit date:** 5 November 2026  
**Policy:** [IMAGE-FIRST POLICY v1.2](https://github.com/Ajokendo/Atlas-of-Knowledge/blob/main/IMAGE_FIRST_POLICY.md), canonical source is now in `main` (commit `bd3deb97`).  
**State:** Rolling audit; inventory and chapter-source presence counts reconciled on 5 November 2026. Per-asset review is in progress, not complete.

## 1. Purpose and interpretation

This file is the Geography audit required by policy v1.2. It records the IDs that could be enumerated from the chapter-level inventory available for this baseline; the total conflicts with the register's stated 231-ID count and separates presence from approval. It does not replace VISUAL_ASSET_REGISTER.md (production inventory) or IMAGE_SOURCES.md (provenance, creator, licence and attribution evidence). An ID or bilingual brief is not proof that an image exists. INTEGRATED means only that existing Geography records report integration; it is not verification. No item is marked VERIFIED in this baseline.

## 2. Derivative and inherited material protocol — policy §8.1

The atlas-wide source relationship and complete source-work inventory are not yet established. Determine provenance asset by asset. Record original work, creator/rightsholder, edition/version, source location, inheritance relationship, changes and the permission/licence for actual reproduction and adaptation. Classify A — Original reuse, B — Adapted or C — Created separately from rights status. Mark unknown values Unknown / PENDING. Do not infer authorship or permission from repository ownership, public availability or prior integration. Do not repeat discovery searches for an identifiable unchanged inherited visual solely to satisfy image-first; verify lineage, rights, scientific meaning, localisation, accessibility and rendering. Search for a replacement when an asset is missing, unsuitable, inaccurate, inaccessible, rights-restricted or needs replacement. Translating surrounding captions/alt text alone does not change the visual category; translating embedded labels or substantively editing the visual is adaptation.

Source-work coverage is provisional. Detailed IMAGE_SOURCES records now cover Chapters 01–06 (with unresolved creator/licence fields for project-local SVGs and several external images) and one MISSING gap record for Chapter 09-G. Chapter 05's 16 pre-existing integrated IDs plus 5.18-A are mapped in IMAGE_SOURCES.md; the separate register is retained as production history. Chapter 06 has records for 6-A, 6-B and 6-C but is not fully source-verified; Chapters 07–08 and 10–26 are not source-verified by the existence of IDs or briefs. Chapter 06 now has five integrated assets (6-A, 6-C, 6.1-A, 6.5-A and 6.7-A); 6-B has a candidate dataset with confirmed CC BY 4.0 terms but no finished map, and the remaining 10 visual IDs are still open.

## 3. Geography-specific checks

Apply the supplement in EDITORIAL_STANDARD_ADOPTION.md: maps require projection, scale, CRS, orientation, data/boundary vintage, source, licence and accuracy; elevation products require DEM/DSM/DTM type, resolution and vertical datum; climate/statistical visuals require period, units, denominator, coverage and classification; Kyrgyzstan maps require authoritative boundary/name checks and dated basin/glacier/imagery provenance; remote sensing requires sensor, product, acquisition date, resolution, processing, bands/indices and validation; sensitive conservation locations must be generalised where disclosure creates risk.

## 4. Audit dimensions

Each asset has five separate results: scientific/factual, rights/licence, Russian–English parity, accessibility, and technical integration. Each uses PASS / FAIL / PENDING / NOT APPLICABLE. VERIFIED requires every applicable dimension to be PASS with evidence recorded. Technical checks of the deployed reader, mobile widths, zoom/reflow, keyboard and screen-reader behaviour are separate from static file checks.

Lifecycle status uses the policy vocabulary: MISSING, FOUND, LICENSE_CHECK, SCIENTIFIC_CHECK, ADAPTED, INTEGRATED, VERIFIED, REJECTED. PENDING in the lifecycle column means the lifecycle classification itself has not yet been established; it is not a new lifecycle status and must be replaced after checking the actual asset.

## 5. Chapter baseline

The chapter inventory contains **281 named visual IDs** plus **two unresolved historical Chapter 05 inventory positions**. The older headline value 231 is superseded and must not be used. The two unnamed positions are not assigned invented IDs. The 281 named IDs are distinct chapter-prefixed labels; the two unresolved positions remain outside per-asset counts until recovered.

| Chapter | Planned IDs | Integrated in chapter source | Open / missing | Evidence / qualification |
|---:|---:|---:|---:|---|
| 01 | 5 | 5 | 0 | Five local bilingual SVGs embedded; RU/EN parity PASS; rights for four original project-local SVGs remain pending; 01-D CC BY 4.0 attribution documented; scientific, accessibility and rendered technical checks pending. |
| 02 | 19 | 19 | 0 | All 19 planned IDs have imagery in both language sections; one ID (2.10-B) uses two separate cycle images. Not all assets are fully verified. |
| 03 | 13 | 13 | 0 | Ten local SVGs plus three sourced images reported integrated; final scientific/editorial and rights review remains asset-specific. |
| 04 | 16 | 16 | 0 | Sixteen local bilingual SVGs embedded; source records identify remaining creator/licence and technical review work. |
| 05 | 18 named + 2 unresolved legacy slots | 17 | 1 named + 2 unresolved | Seventeen named assets are embedded; 18 named IDs are enumerated. Two old inventory positions remain unidentifiable and are not counted as assets until recovered. |
| 06 | 15 | 5 | 10 | 6-A, 6-C, 6.1-A, 6.5-A and 6.7-A integrated; 6-B has a licensed candidate dataset but no finished map. |
| 07 | 9 | 7 | 2 | 07-A, 07-B, 07-F, 07-G, 07-H and 07-I are original bilingual SVGs; 07-D remains an adapted CC BY 4.0 figure. Accessibility and rendered technical QA remain pending. 07-C and 07-E remain open pending usable map geometry. |
| 08 | 7 | 6 | 1 | 08-A, 08-C, 08-D, 08-E, 08-F and 08-G are original bilingual SVGs; 08-B remains open pending a validated global WRB map. Rights and rendered/accessibility QA remain pending. |
| 09 | 7 | 5 | 2 | 09-B, 09-C, 09-D, 09-F and 09-G are original bilingual conceptual SVGs. 09-A (WPP 2024 time series) and 09-E (gridded population-density map) remain open pending source-data extraction and documented chart/map metadata. |
| 10 | 7 | 6 | 1 | 10-B–10-G are original bilingual conceptual SVGs; 10-A remains open pending a current, source-backed world political map and documented boundary-status policy. Rights and rendered/accessibility QA remain pending. |
| 11 | 7 | 7 | 0 | Seven local SVG assets embedded in chapter source. |
| 12 | 10 | 8 | 2 | 12-A, 12-B, 12-D–12-I integrated; 12-C (transboundary systems) and 12-J (Antarctica with station coverage) remain open. |
| 13 | 11 | 11 | 0 | Eleven local SVG assets embedded. |
| 14 | 9 | 8 | 1 | 14-A, 14-B, 14-C, 14-D, 14-E, 14-F, 14-H and 14-I embedded; 14-G remains open. |
| 15 | 11 | 11 | 0 | Eleven local SVG assets embedded. |
| 16 | 9 | 9 | 0 | Nine local SVG assets embedded. |
| 17 | 9 | 8 | 1 | 17-A, 17-B, 17-C, 17-D, 17-E, 17-F, 17-G and 17-I integrated; 17-H (geology/mineral districts) remains open. 17-A is a provisional locator; OCHA source release date and legal-border validation remain pending. 17-D's valley anchors are not boundary polygons; spatial verification remains pending. |
| 18 | 10 | 5 | 5 | 18-B, 18-C (three-photo set), 18-D, 18-H and 18-J embedded. Supplementary Blue Green Atlas relief image does not close 18-A. |
| 19 | 10 | 7 | 3 | 19-C, 19-D, 19-E, 19-F, 19-H, 19-I and 19-J embedded; 19-I is a distinct qualitative seasonal snow/precipitation profile, not a duplicate of 19-C. |
| 20 | 11 | 8 | 3 | 20-C, 20-D, 20-E, 20-F, 20-H, 20-I, 20-J and 20-K embedded; the Frontiers glacial-lake figure is supporting source material, not counted as an additional planned ID. |
| 21–26 | 68 | 16 | 52 | 21-B, 21-C, 21-H, 21-I, 21-J; 22-F, 22-G, 22-H, 22-J; 23-E, 23-J; 25-D, 25-I; 26-H, 26-I and 26-K are now embedded as original bilingual SVGs. 52 planned IDs remain open. |
| **Total named inventory** | **281** | **197** | **84** | Plus two unresolved historical Chapter 05 positions; no invented IDs. |

**Separate metrics (5 November 2026):**
- **Image Coverage:** 197/281 named IDs have an image embedded in the relevant chapter source (70.1%). This measures presence only.
- **Image Verification:** 0/197 integrated IDs are fully VERIFIED in this audit. Individual PASS results do not imply full verification.
- **Image Gaps:** 84 named IDs remain without a confirmed integrated image, plus two unresolved historical Chapter 05 inventory positions.
- Browser/mobile/accessibility QA and any missing evidence remain PENDING; do not infer completion from integration.

## 6. Per-asset audit register

The per-asset table enumerates 281 named IDs. Two unresolved historical Chapter 05 positions remain unassigned. Each review dimension is set independently from the evidence available; integration alone is not approval. No item is promoted to VERIFIED unless every applicable dimension is PASS with evidence.

| Chapter | Visual ID | Lifecycle status | Scientific | Rights | RU/EN | Accessibility | Technical | Evidence / next action |
|---|---|---|---|---|---|---|---|---|
| 10 | 10-A | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 10 | 10-B | INTEGRATED | PASS | PENDING | PASS | PENDING | PENDING | Original bilingual conceptual SVG compares geometric, river, watershed and historical boundary types; no real disputed border is depicted. Rights, accessibility and rendered QA pending. |
| 10 | 10-C | INTEGRATED | PASS | PENDING | PASS | PENDING | PENDING | Original bilingual UNCLOS cross-section; correctly distinguishes baseline distances, contiguous-zone overlap with EEZ, water-column zones and continental-shelf seabed rights. Not to scale. Rights, accessibility and rendered QA pending. |
| 10 | 10-D | INTEGRATED | PASS | PENDING | PASS | PENDING | PENDING | Original bilingual conceptual comparison of unitary, federal and regionalised structures; actual powers remain constitution-specific. Rights, accessibility and rendered QA pending. |
| 10 | 10-E | INTEGRATED | PASS | PENDING | PASS | PENDING | PENDING | Original bilingual hypothetical district/representation diagram; all boundaries and values are fictional, not election results. Rights, accessibility and rendered QA pending. |
| 10 | 10-F | INTEGRATED | PASS | PENDING | PASS | PENDING | PENDING | Original bilingual cooperation-level diagram; no universal hierarchy or binding force is implied. Rights, accessibility and rendered QA pending. |
| 10 | 10-G | INTEGRATED | PASS | PENDING | PASS | PENDING | PENDING | Original bilingual political-map reading checklist; supports critical source/date/status/projection/scale/legend review. Rights, accessibility and rendered QA pending. |
| 11 | 11-A | INTEGRATED | PENDING | PENDING | PASS | PENDING | PASS — source-level SVG checks; live render pending | Original bilingual sector-structure SVG; project licence and scientific review remain open. |
| 11 | 11-B | INTEGRATED | PENDING | PENDING | PASS | PENDING | PASS — source-level SVG checks; live render pending | Original bilingual location-factors SVG; project licence and scientific review remain open. |
| 11 | 11-C | INTEGRATED | PENDING | PENDING | PASS | PENDING | PASS — source-level SVG checks; live render pending | Original multimodal supply-chain schematic; explicitly not a real transport-corridor map. Project licence pending. |
| 11 | 11-D | INTEGRATED | PASS | PENDING | PASS | PENDING | PASS — source-level SVG checks; live render pending | Original bilingual global-value-chain flow; UNCTAD/UNSD definitions support multi-country fragmentation and sequence of activities. It is conceptual, not a real product/country map. Rights and accessibility pending. |
| 11 | 11-E | INTEGRATED | PASS | PENDING | PASS | PENDING | PASS — source-level SVG checks; live render pending | Original bilingual conceptual agricultural-landscape profile; links climate, soil, relief, water, labour, markets and transport without claiming crop suitability or mapping a real territory. Rights/accessibility pending. |
| 11 | 11-F | INTEGRATED | PASS | PENDING | PASS | PENDING | PASS — source-level SVG checks; live render pending | Original bilingual energy-system diagram; separates primary resources, generation, transmission, distribution, consumption, storage and cross-border flows. 2025 Kyrgyzstan figures are rounded and explicitly not a complete energy balance. Rights/accessibility pending. |
| 11 | 11-G | INTEGRATED | PASS | PENDING | PASS | PENDING | PASS — source-level SVG checks; live render pending | Original bilingual tourism-destination system; natural/cultural resources, infrastructure, services, visitors, local communities, governance and environmental limits. UN Tourism destination-monitoring framework supports governance, local satisfaction and economic/environmental dimensions. Rights/accessibility pending. |
| 12 | 12-A | INTEGRATED | PENDING | PASS — Atlas Abierto CC BY 4.0 attribution recorded | PASS | PENDING | PENDING — remote Wikimedia dependency | Adapted relief base with bilingual approximate markers; not a georeferenced river/boundary layer. |
| 12 | 12-B | INTEGRATED | PENDING | PASS — Dou et al. 2018 CC BY 4.0 attribution recorded | PASS | PENDING | PENDING — remote MDPI dependency | Adapted Asia relief/regionalisation map; explicitly not an official UN M49 boundary map. |
| 12 | 12-C | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 12 | 12-D | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 12 | 12-E | INTEGRATED | PENDING | PASS — Blue Green Atlas page states CC BY 4.0; attribution and licence link added | PASS — bilingual alt text, feature key and caption | PENDING | PENDING — remote JPEG dependency; test deployed load/responsive rendering | External physical-relief map by Blue Green Atlas (SRTM3 / GEBCO 2019 / Natural Earth), Albers Equal Area Conic. Added bilingual key for major plains, ranges, peninsulas and seas; not an official macroregional-boundary map. Scientific review and live technical QA pending. |
| 12 | 12-F | INTEGRATED | PENDING | PASS — Blue Green Atlas page states CC BY 4.0; attribution and licence link added | PASS — bilingual alt text, drainage key and caption | PENDING | PENDING — remote JPEG dependency; test deployed load/responsive rendering | External physical-relief map, Lambert Azimuthal Equal Area; SRTM3 / GEBCO 2019 / Natural Earth. Bilingual key names five major drainage systems and approximate outlet directions. Scientific review and live QA pending. |
| 12 | 12-G | INTEGRATED | PENDING | PASS — CIA source image is public domain; source credit recorded | PASS — bilingual alt text, island/strait/canal key and caption | PENDING | PENDING — remote Wikimedia image dependency; test deployed load/responsive rendering | CIA World Factbook 2021 shaded relief, Lambert Conformal Conic, 7°/24° N standard parallels; no text or borders. Key identifies Antilles, Bahamas, major passages and Panama Canal. Scientific/live QA pending. |
| 12 | 12-H | INTEGRATED | PENDING | PASS — Blue Green Atlas page states CC BY 4.0; attribution and licence link added | PASS — bilingual alt text and physical-systems key | PENDING | PENDING — remote JPEG dependency; test deployed load/responsive rendering | External physical-relief map, Albers Equal Area Conic; SRTM3 / GEBCO 2019 / Natural Earth. Bilingual key identifies Andes, Amazon, Orinoco, highlands, plains and main drainage directions. Scientific/live QA pending. |
| 12 | 12-I | INTEGRATED | PENDING | PASS — Blue Green Atlas page states CC BY 4.0; attribution and licence link added | PASS — bilingual alt text, island-origin key and caption | PENDING | PENDING — remote JPEG dependency; test deployed load/responsive rendering | External physical-relief map, Lambert Conformal Conic; SRTM3 / GEBCO 2019 / Natural Earth. Bilingual key distinguishes continental, volcanic and coral-island examples with mixed-origin caveat. Scientific/live QA pending. |
| 12 | 12-J | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 13 | 13-A | INTEGRATED | PENDING | PENDING | PASS | PENDING | PASS — source-level SVG checks; live render pending | Original bilingual greenhouse-effect diagram; project licence and scientific review remain open. |
| 13 | 13-B | INTEGRATED | PASS | PENDING | PASS | PENDING | PASS — source-level SVG checks; live render pending | Original bilingual biodiversity-levels and direct-drivers diagram; IPBES Global Assessment framework supports the five direct drivers and separation from indirect social/economic causes. Rights/accessibility pending. |
| 13 | 13-C | INTEGRATED | PENDING | PENDING | PASS | PENDING | PASS — source-level SVG checks; live render pending | Original bilingual environmental-risk model; project licence and scientific review remain open. |
| 13 | 13-D | INTEGRATED | PENDING | PENDING | PASS | PENDING | PASS — source-level SVG checks; live render pending | Original bilingual EIA/SEA/monitoring comparison; jurisdiction caveat retained. Legal terminology and country-specific procedures require further review. Rights/accessibility pending. |
| 13 | 13-E | INTEGRATED | PASS | PENDING | PASS | PENDING | PASS — source-level SVG checks; live render pending | Original bilingual social-ecological system diagram adapts the six interlinked elements of the IPBES conceptual framework; explicitly not a linear causal chain. Rights/accessibility pending. |
| 13 | 13-F | INTEGRATED | PASS | PENDING | PASS | PENDING | PASS — source-level SVG checks; live render pending | Original bilingual qualitative matrix separates observed climate impacts from projected risks; aligned with IPCC AR6 WGII. No quantitative or Kyrgyzstan-specific forecast is claimed. Rights/accessibility pending. |
| 13 | 13-G | INTEGRATED | PASS | PENDING | PASS | PENDING | PASS — source-level SVG checks; live render pending | Original bilingual land-degradation/restoration sequence; erosion, salinisation, compaction and cover loss distinguished; avoid–reduce–reverse hierarchy checked against UNCCD LDN framework. Rights/accessibility pending. |
| 13 | 13-H | INTEGRATED | PASS | PENDING | PASS | PENDING | PASS — source-level SVG checks; live render pending | Original bilingual mitigation/adaptation comparison; conceptual distinction checked against IPCC/UNFCCC sources. No universal adaptation indicator set is asserted. Rights/accessibility pending. |
| 13 | 13-I | INTEGRATED | PASS | PENDING | PASS | PENDING | PASS — source-level SVG checks; live render pending | Original bilingual environmental-monitoring workflow; field, laboratory, remote-sensing and community inputs, QA/QC, analysis and publication checked against EPA/UNEP guidance. Rights/accessibility pending. |
| 13 | 13-J | INTEGRATED | PASS | PENDING | PASS | PENDING | PASS — source-level SVG checks; live render pending | Original bilingual circular-economy loops; prioritises sharing, maintenance, repair and reuse before recycling. Ellen MacArthur Foundation technical-cycle guidance reviewed; butterfly graphic not copied. Rights/accessibility pending. |
| 13 | 13-K | INTEGRATED | PASS | PENDING | PASS | PENDING | PASS — source-level SVG checks; live render pending | Original bilingual hypothetical-city environmental-justice schematic; distributional, recognition and procedural dimensions separated. US-specific indices are not transferred as Kyrgyzstan measurements. Rights/accessibility pending. |
| 14 | 14-A | INTEGRATED | PENDING | PENDING | PASS | PENDING | PASS — source-level SVG checks; live render pending | Original bilingual vector/raster model comparison; project licence pending. |
| 14 | 14-B | INTEGRATED | PENDING | PENDING | PASS | PENDING | PASS — source-level SVG checks; live render pending | Original bilingual CRS/vertical-reference diagram; project licence pending. |
| 14 | 14-C | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 14 | 14-D | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 14 | 14-E | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 14 | 14-F | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 14 | 14-G | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 14 | 14-H | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 14 | 14-I | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 15 | 15-A | INTEGRATED | PENDING | PENDING | PASS | PENDING | PASS — source-level SVG checks; live render pending | Original bilingual electromagnetic-spectrum diagram; project licence pending. |
| 15 | 15-B | INTEGRATED | PENDING | PENDING | PASS | PENDING | PASS — source-level SVG checks; live render pending | Original bilingual active/passive sensor diagram; project licence pending. |
| 15 | 15-C | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 15 | 15-D | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 15 | 15-E | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 15 | 15-F | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 15 | 15-G | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 15 | 15-H | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 15 | 15-I | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 15 | 15-J | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 15 | 15-K | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 16 | 16-A | INTEGRATED | PENDING | PENDING | PASS | PENDING | PASS — source-level SVG checks; live render pending | Original bilingual research-cycle diagram; project licence pending. |
| 16 | 16-B | INTEGRATED | PENDING | PENDING | PASS | PENDING | PASS — source-level SVG checks; live render pending | Original bilingual analytical-scale diagram; project licence pending. |
| 16 | 16-C | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 16 | 16-D | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 16 | 16-E | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 16 | 16-F | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 16 | 16-G | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 16 | 16-H | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 16 | 16-I | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 17 | 17-A | INTEGRATED | PENDING | PASS — Blue Green Atlas CC BY 4.0; OCHA COD-AB CC BY-IGO; Natural Earth public domain; all credited | PASS — bilingual alt text, neighbour/landmark key and explicit boundary caveat | PENDING | PENDING — external JPEG and SVG dependencies; deployed load/responsive QA pending | Two-map locator: Blue Green Atlas relief map for regional context plus OCHA COD-AB / Ministry of Emergency Situations administrative outline with Natural Earth neighbours. OCHA release/version date is not exposed; the national-border line is explicitly not certified as legally current. |
| 17 | 17-B | INTEGRATED | PENDING | PASS — Wikimedia Commons source page records public-domain dedication | PASS — bilingual alt text, physical-feature key and limitation note | PENDING | PENDING — external PNG dependency; browser/mobile responsive QA pending | SRTM-derived GMT topographic map (file uploaded 2007; exact raster date unknown), 0–4,000 m+ elevation scale. Bilingual key names principal Tien Shan/Pamir–Alay ranges and valleys without drawing invented boundaries. Scientific review of feature labels remains pending. |
| 17 | 17-C | INTEGRATED | PASS | PENDING | PASS | PENDING | PENDING | Original bilingual regionalisation comparison integrated; explicitly not a map or source of precise boundaries; creator/rightsholder and project licence pending. |
| 17 | 17-D | INTEGRATED | PENDING | PASS — Blue Green Atlas CC BY 4.0 for map; project rights assignment for original profile pending | PASS — bilingual alt text, valley-anchor key and scale/outline caveats | PENDING | PASS — SVG source structure checked; external map load/responsive QA pending | Relief map plus original bilingual transverse valley profile. Seven named valleys are linked to reference settlements only; no valley-boundary polygons or precise measured transects are asserted. Spatial anchor verification remains pending. |
| 17 | 17-E | INTEGRATED | PASS | PENDING | PASS | PENDING | PENDING | Original bilingual conceptual timeline integrated in RU/EN; global ICS boundaries are distinguished from local event dating; creator/rightsholder and project licence pending. |
| 17 | 17-F | INTEGRATED | PASS | PASS — Poggi et al. (2024) CC BY 4.0; author/DOI attribution and licence link added | PASS — bilingual alt text and captions for both panels | PENDING | PENDING — external figure dependencies; browser/mobile responsive QA pending | Two research maps: earthquake epicentres from harmonised source catalogues (catalogue selection M≥2, ~300 km buffer, historical/instrumental records through 2020) and selected AFEAD/GEM active faults (World Bank download updated 2023-02-21, classes A–D). Regional selection, not exhaustive or live. |
| 17 | 17-G | INTEGRATED | PASS | PENDING | PASS | PENDING | PENDING | Original bilingual not-to-scale relief-process schematic integrated in RU/EN; endogenic and exogenic processes distinguished; creator/rightsholder and project licence pending. |
| 17 | 17-H | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 17 | 17-I | INTEGRATED | PENDING | PASS — OCHA COD-AB / Ministry of Emergency Situations boundaries CC BY-IGO; attribution added; map renderer credited | PASS — bilingual alt text, region/city key and caption | PENDING | PENDING — external SVG dependency; live render and keyboard/screen-reader QA pending | Labelled SVG identifies seven regions and separate Bishkek/Osh cities; Lambert azimuthal equal-area. Underlying OCHA release date is not exposed on source page, so date/version validation remains pending. |
| 18 | 18-A | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 18 | 18-B | INTEGRATED | PENDING | PENDING | PASS | PENDING | PASS — source-level SVG checks; live render pending | Original schematic orographic regionalisation; not georeferenced. Project licence pending. |
| 18 | 18-C | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 18 | 18-D | INTEGRATED | PENDING | PENDING | PASS | PENDING | PASS — source-level SVG checks; live render pending | Original conceptual glacial-landform diagram. Project licence pending. |
| 18 | 18-E | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 18 | 18-F | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 18 | 18-G | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 18 | 18-H | INTEGRATED | PENDING | PENDING | PASS | PENDING | PASS — source-level SVG checks; live render pending | Original conceptual river-valley cross-section. Project licence pending. |
| 18 | 18-I | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 18 | 18-J | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Asset register lists a local SVG; final checks remain PENDING. |
| 19 | 19-A | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 19 | 19-B | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 19 | 19-C | INTEGRATED | PENDING | PENDING | PASS | PENDING | PASS — source-level SVG checks; live render pending | Original conceptual altitudinal climate profile; variable belt boundaries noted. Project licence pending. |
| 19 | 19-D | INTEGRATED | PENDING | PENDING | PASS | PENDING | PASS — source-level SVG checks; live render pending | Original climate-hazard infographic; no frequencies or regional rankings asserted. Project licence pending. |
| 19 | 19-E | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 19 | 19-F | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 19 | 19-G | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 19 | 19-H | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Asset register lists a local SVG; final checks remain PENDING. |
| 19 | 19-I | INTEGRATED | PASS | PENDING — original SVG; formal project creator/licence assignment pending | PASS — bilingual alt text, labels and explicit qualitative/no-threshold caveats | PENDING | PASS — source-level SVG checks; live render pending | Original bilingual conceptual profile distinguishes temperature decrease, aspect-dependent precipitation, increasing snow-cover duration and seasonal accumulation/melt. It complements 19-C rather than repeating its vegetation-belt sequence. No numeric values or universal altitude bands asserted. |
| 19 | 19-J | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 20 | 20-A | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 20 | 20-B | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 20 | 20-C | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 20 | 20-D | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 20 | 20-E | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 20 | 20-F | INTEGRATED | PENDING | PENDING | PASS | PENDING | PASS — source-level SVG checks; live render pending | Original conceptual GLOF pathway; not an operational risk map. Project licence pending. |
| 20 | 20-G | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 20 | 20-H | INTEGRATED | PENDING | PENDING | PASS | PENDING | PASS — source-level SVG checks; live render pending | Original catchment water-balance diagram; assumptions stated. Project licence pending. |
| 20 | 20-I | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Asset register lists a local SVG; final checks remain PENDING. |
| 20 | 20-J | INTEGRATED | PENDING | PENDING | PASS | PENDING | PASS — source-level SVG checks; live render pending | Original conceptual groundwater section; not site-specific. Project licence pending. |
| 20 | 20-K | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Asset register lists a local SVG; final checks remain PENDING. |
| 21 | 21-A | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 21 | 21-B | INTEGRATED | PASS | PENDING — original SVG; formal project creator/licence assignment pending | PASS | PENDING | PASS — source-level SVG checks; live render pending | Original bilingual qualitative vegetation-belt profile; no universal altitude thresholds; aspect/moisture variability stated. |
| 21 | 21-C | INTEGRATED | PASS | PENDING — original SVG; formal project creator/licence assignment pending | PASS | PENDING | PASS — source-level SVG checks; live render pending | Original bilingual forest-type comparison; FAO Kyrgyzstan forest-sector review and NFI#2 support spruce, juniper, walnut-fruit and poplar/willow groups. No distribution map or quantitative shares claimed. |
| 21 | 21-D | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 21 | 21-E | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 21 | 21-F | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 21 | 21-G | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 21 | 21-H | INTEGRATED | PASS | PENDING — original SVG; formal project creator/licence assignment pending | PASS | PENDING | PASS — source-level SVG checks; live render pending | Original bilingual simplified high-mountain food web; energy arrows and decomposer nutrient return are conceptual, not a complete species-specific web. |
| 21 | 21-I | INTEGRATED | PASS | PENDING — original SVG; formal project creator/licence assignment pending | PASS | PENDING | PASS — source-level SVG checks; live render pending | Original bilingual pressure–effect–response framework; examples are not a causal assessment of a particular site or proof of intervention effectiveness. |
| 21 | 21-J | INTEGRATED | PASS | PENDING — original SVG; formal project creator/licence assignment pending | PASS | PENDING | PASS — source-level SVG checks; live render pending | Original bilingual comparison of transects, plots, camera traps, GPS telemetry, eDNA and satellite analysis; limitations and sensitive-location caveat included. |
| 22 | 22-A | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 22 | 22-B | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 22 | 22-C | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 22 | 22-D | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 22 | 22-E | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 22 | 22-F | INTEGRATED | PASS | PENDING — original SVG; formal project creator/licence assignment pending | PASS | PENDING | PASS — source-level SVG checks; live render pending | Original bilingual UNESCO MAB core/buffer/transition model; explicitly schematic, not a real reserve boundary. |
| 22 | 22-G | INTEGRATED | PASS | PENDING — original SVG; formal project creator/licence assignment pending | PASS | PENDING | PASS — source-level SVG checks; live render pending | Original bilingual low-impact visitor-route schematic; no real trail or protected-area boundary implied; aligns with UNEP/IUCN visitor-management guidance. |
| 22 | 22-H | INTEGRATED | PASS | PENDING — original SVG; formal project creator/licence assignment pending | PASS | PENDING | PASS — source-level SVG checks; live render pending | Original bilingual protected-area stakeholder-management model; collaboration and feedback shown without asserting a universal legal hierarchy. |
| 22 | 22-I | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 22 | 22-J | INTEGRATED | PASS | PENDING — original SVG; formal project creator/licence assignment pending | PASS | PENDING | PASS — source-level SVG checks; live render pending | Original bilingual six-component management-effectiveness cycle (context, planning, inputs, processes, outputs, outcomes); no scores or real-park performance values. |
| 23 | 23-A | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 23 | 23-B | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 23 | 23-C | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 23 | 23-D | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 23 | 23-E | INTEGRATED | PASS | PENDING — original SVG; formal project creator/licence assignment pending | PASS | PENDING | PASS — source-level SVG checks; live render pending | Original bilingual urban/rural comparison using ideal types; no rigid threshold or settlement-level data asserted; continuum caveat included. |
| 23 | 23-F | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 23 | 23-G | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 23 | 23-H | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 23 | 23-I | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 23 | 23-J | INTEGRATED | PASS | PENDING — original SVG; formal project creator/licence assignment pending | PASS | PENDING | PASS — source-level SVG checks; live render pending | Original bilingual conceptual comparison of valley village, mountain settlement and seasonal jailoo; variation between households and regions explicitly noted. |
| 23 | 23-K | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 23 | 23-L | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 24 | 24-A | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 24 | 24-B | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 24 | 24-C | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 24 | 24-D | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 24 | 24-E | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 24 | 24-F | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 24 | 24-G | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 24 | 24-H | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 24 | 24-I | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 24 | 24-J | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 24 | 24-K | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 24 | 24-L | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 25 | 25-A | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 25 | 25-B | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 25 | 25-C | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 25 | 25-D | INTEGRATED | PASS | PENDING — original SVG; formal project creator/licence assignment pending | PASS | PENDING | PASS — source-level SVG checks; live render pending | Original bilingual natural-capital-to-uses-to-pressures-to-stewardship framework; no monetary valuation or depletion estimate. |
| 25 | 25-E | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 25 | 25-F | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 25 | 25-G | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 25 | 25-H | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 25 | 25-I | INTEGRATED | PASS | PENDING — original SVG; formal project creator/licence assignment pending | PASS | PENDING | PASS — source-level SVG checks; live render pending | Original bilingual agri-food chain from production through collection, storage, sorting, processing, logistics and market; FAO value-chain guidance reviewed; no region-specific route or volumes asserted. |
| 25 | 25-J | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 25 | 25-K | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 25 | 25-L | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 26 | 26-A | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 26 | 26-B | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 26 | 26-C | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 26 | 26-D | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 26 | 26-E | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 26 | 26-F | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 26 | 26-G | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 26 | 26-H | INTEGRATED | PASS | PENDING — original SVG; formal project creator/licence assignment pending | PASS | PENDING | PASS — source-level SVG checks; live render pending | Original bilingual waste hierarchy: prevention, preparing for reuse, recycling/composting, other recovery and residual disposal; priority order checked against EU/UNEP law platform. |
| 26 | 26-I | INTEGRATED | PASS | PENDING — original SVG; formal project creator/licence assignment pending | PASS | PENDING | PASS — source-level SVG checks; live render pending | Original bilingual hazard/exposure/vulnerability/capacity framework; follows UNDRR terminology; no literal multiplication or forecast implied. |
| 26 | 26-J | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 26 | 26-K | INTEGRATED | PASS | PENDING — original SVG; formal project creator/licence assignment pending | PASS | PENDING | PASS — source-level SVG checks; live render pending | Original bilingual green-urban-infrastructure concept; cooling, infiltration, habitat, air-quality and access co-benefits are conditional on design and maintenance. |
| 26 | 26-L | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 01 | 01-A | INTEGRATED | PENDING — preliminary AI-assisted screen only; competent internal reviewer distinct from creator not yet recorded | PENDING — project creator/rightsholder and redistribution licence not assigned | PASS | PENDING — text alternative and bilingual SVG metadata checked; assistive-technology output not tested | PENDING — SVG structure/viewBox checked; rendered browser/device QA not run | Conceptual systems model; no quantitative or geographic claims. Mobile-first vertical composition updated 5 Nov 2026. |
| 01 | 01-B | INTEGRATED | PENDING — preliminary AI-assisted screen only; competent internal reviewer distinct from creator not yet recorded | PENDING — project creator/rightsholder and redistribution licence not assigned | PASS | PENDING — text alternative and bilingual SVG metadata checked; assistive-technology output not tested | PENDING — SVG structure/viewBox checked; rendered browser/device QA not run | Coordinate grid and settlement network are schematic, not real geodata. Mobile-first vertical composition updated 5 Nov 2026. |
| 01 | 01-C | INTEGRATED | PENDING — preliminary AI-assisted screen only; competent internal reviewer distinct from creator not yet recorded | PENDING — project creator/rightsholder and redistribution licence not assigned | PASS | PENDING — text alternative and bilingual SVG metadata checked; assistive-technology output not tested | PENDING — SVG structure/viewBox checked; rendered browser/device QA not run | Independent six-stage project model; National Geographic Geo-Inquiry is a related teaching reference, not an equivalent six-stage source. Mobile-first vertical composition updated 5 Nov 2026. |
| 01 | 01-D | INTEGRATED | PENDING — preliminary AI-assisted screen only; competent internal reviewer distinct from creator not yet recorded | PASS — exact GeogSage source page and CC BY 4.0 terms checked; attribution and changes recorded | PASS | PENDING — text alternative and bilingual SVG metadata checked; assistive-technology output not tested | PENDING — SVG structure/viewBox checked; rendered browser/device QA not run | Adapted from GeogSage BranchesOfGeography.png; three fields overlap. Mobile-first composition updated 5 Nov 2026. |
| 01 | 01-E | INTEGRATED | PENDING — preliminary AI-assisted screen only; competent internal reviewer distinct from creator not yet recorded | PENDING — project creator/rightsholder and redistribution licence not assigned | PASS | PENDING — text alternative and bilingual SVG metadata checked; assistive-technology output not tested | PENDING — SVG structure/viewBox checked; rendered browser/device QA not run | Five analytical levels are schematic and distinct from cartographic map scale. Mobile-first vertical composition updated 5 Nov 2026. |
| 02 | 2-A | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Existing register reports bilingual integration; five audit dimensions remain PENDING. |
| 02 | 2.1-A | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Existing register reports bilingual integration; five audit dimensions remain PENDING. |
| 02 | 2.2-A | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Existing register reports bilingual integration; five audit dimensions remain PENDING. |
| 02 | 2-B | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Existing register reports bilingual integration; five audit dimensions remain PENDING. |
| 02 | 2.3-A | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Existing register reports bilingual integration; five audit dimensions remain PENDING. |
| 02 | 2-C | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Existing register reports bilingual integration; five audit dimensions remain PENDING. |
| 02 | 2.4-A | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Existing register reports bilingual integration; five audit dimensions remain PENDING. |
| 02 | 2.5-A | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Existing register reports bilingual integration; five audit dimensions remain PENDING. |
| 02 | 2.6-A | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Existing register reports bilingual integration; five audit dimensions remain PENDING. |
| 02 | 2.8-A | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Existing register reports bilingual integration; five audit dimensions remain PENDING. |
| 02 | 2.9-A | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Existing register reports bilingual integration; five audit dimensions remain PENDING. |
| 02 | 2-D | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Existing register reports bilingual integration; five audit dimensions remain PENDING. |
| 02 | 2.10-A | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Existing register reports bilingual integration; five audit dimensions remain PENDING. |
| 02 | 2.10-B | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Existing register reports bilingual integration; five audit dimensions remain PENDING. |
| 02 | 2.11-A | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Existing register reports bilingual integration; five audit dimensions remain PENDING. |
| 02 | 2.12-A | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Existing register reports bilingual integration; five audit dimensions remain PENDING. |
| 02 | 2.13-A | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Existing register reports bilingual integration; five audit dimensions remain PENDING. |
| 02 | 2.14-A | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Existing register reports bilingual integration; five audit dimensions remain PENDING. |
| 02 | 2.15-A | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Existing register reports bilingual integration; five audit dimensions remain PENDING. |
| 03 | 3.1-A | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Existing register reports bilingual integration; five audit dimensions remain PENDING. |
| 03 | 3.2-A | INTEGRATED | PENDING | PASS | PENDING | PENDING | PENDING | Exact USGS media page labels the complete Ore/Mineral Sample Images composite Public Domain; mixed component origins are disclosed. No standalone component reuse. |
| 03 | 3.3-A | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Existing register reports bilingual integration; five audit dimensions remain PENDING. |
| 03 | 3.4-A | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Existing register reports bilingual integration; five audit dimensions remain PENDING. |
| 03 | 3.5-A | INTEGRATED | PENDING | PASS | PENDING | PENDING | PENDING | Exact USGS media page for This Dynamic Planet I-2800 labels the image Public Domain; dated 2006 reference map. |
| 03 | 3.6-A | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Existing register reports bilingual integration; five audit dimensions remain PENDING. |
| 03 | 3.7-A | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Existing register reports bilingual integration; five audit dimensions remain PENDING. |
| 03 | 3.8-A | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Existing register reports bilingual integration; five audit dimensions remain PENDING. |
| 03 | 3.9-A | INTEGRATED | PENDING | PASS | PENDING | PENDING | PENDING | Exact ICS current chart v2026/06 page states CC BY 4.0. Chart labels remain English-only; a Russian key to the hierarchy and principal eons/eras was added, but a full translation of chart subdivisions remains open. |
| 03 | 3.10-A | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Existing register reports bilingual integration; five audit dimensions remain PENDING. |
| 03 | 3.11-A | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Existing register reports bilingual integration; five audit dimensions remain PENDING. |
| 03 | 3.12-A | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Existing register reports bilingual integration; five audit dimensions remain PENDING. |
| 03 | 3.12-B | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Existing register reports bilingual integration; five audit dimensions remain PENDING. |
| 04 | 4.2-A | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Existing register reports bilingual integration; five audit dimensions remain PENDING. |
| 04 | 4.3-A | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Existing register reports bilingual integration; five audit dimensions remain PENDING. |
| 04 | 4.4-A | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Existing register reports bilingual integration; five audit dimensions remain PENDING. |
| 04 | 4.5-A | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Existing register reports bilingual integration; five audit dimensions remain PENDING. |
| 04 | 4.6-A | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Existing register reports bilingual integration; five audit dimensions remain PENDING. |
| 04 | 4.7-A | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Existing register reports bilingual integration; five audit dimensions remain PENDING. |
| 04 | 4.8-A | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Existing register reports bilingual integration; five audit dimensions remain PENDING. |
| 04 | 4.9-A | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Existing register reports bilingual integration; five audit dimensions remain PENDING. |
| 04 | 4.10-A | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Existing register reports bilingual integration; five audit dimensions remain PENDING. |
| 04 | 4.11-A | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Existing register reports bilingual integration; five audit dimensions remain PENDING. |
| 04 | 4.12-A | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Existing register reports bilingual integration; five audit dimensions remain PENDING. |
| 04 | 4.13-A | INTEGRATED | PASS | PENDING | PENDING | PENDING | PENDING | Everest 8,848.86 ±0.06 m (IHRS, 2020); Challenger Deep 10,935 ±6 m (2021 pressure method) and 10,927 m preferred 2026 gridded estimate with 10,914–10,932 m model-sensitivity envelope verified against cited studies. Diagram correctly distinguishes methods and caveats. SVG rights/rendering remain open. |
| 04 | 4.14-A | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Existing register reports bilingual integration; five audit dimensions remain PENDING. |
| 04 | 4.14-B | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Existing register reports bilingual integration; five audit dimensions remain PENDING. |
| 04 | 4.15-A | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Existing register reports bilingual integration; five audit dimensions remain PENDING. |
| 04 | 4.15-B | INTEGRATED | PENDING | PENDING | PENDING | PENDING | PENDING | Existing register reports bilingual integration; five audit dimensions remain PENDING. |
| 05 | 5.1-A | INTEGRATED | PENDING | PENDING | PASS | PENDING | PENDING | Project-local bilingual SVG embedded in RU/EN; static SVG structure checked. Scientific content, creator/licence, accessibility and rendered QA remain open. |
| 05 | 5.2-A | INTEGRATED | PASS | PENDING | PASS | PENDING | PENDING | German CC0 candidate rejected (wrong language and W3C errors); replaced with original bilingual local SVG. NOAA layer ranges, boundary values, ionosphere placement within the thermosphere (about 60–300 km) and Kármán-line convention checked. Project licence, accessibility and rendered QA remain open. |
| 05 | 5.3-A | INTEGRATED | PASS | PASS | PASS | PENDING | PENDING | NASA / My NASA Data energy-budget diagram; NASA credit and educational-use guidance verified. Energy-balance arithmetic closes to rounding (TOA residual ≈0.6 W/m²; surface residual ≈0.6 W/m²). Caption identifies historic ten-year average and Loeb/Trenberth sources; exact averaging interval not specified. Russian key translates all English labels. Rendered accessibility remains open. |
| 05 | 5.4-A | INTEGRATED | PENDING | PASS | PASS | PENDING | PENDING | Commons file page confirms CC BY-SA 4.0; attribution, Copernicus/ERA5 data credit, licence link and unchanged reuse recorded. Russian key translates English title and temperature legend. Scientific map review and rendered QA remain open. |
| 05 | 5.5-A | INTEGRATED | PENDING | PASS | PASS | PENDING | PENDING | NWS image on official weather.gov training page; NOAA U.S. public-domain guidance applies absent a third-party credit; worldwide copyright status is not separately assessed. NOAA/NWS Louisville attribution recorded. Northern Hemisphere limitation remains in bilingual caption. |
| 05 | 5.6-A | INTEGRATED | PENDING | PASS | PASS | PENDING | PENDING | Exact NOAA JetStream image verified; U.S. public-domain guidance applies absent a third-party credit; worldwide copyright status is not separately assessed. Image uses only numbered cells; bilingual caption explains the simplified three-cell model. |
| 05 | 5.7-A | INTEGRATED | PENDING | PASS | PASS | PENDING | PENDING | Exact NOAA JetStream water-cycle image verified; public-domain guidance applies absent a third-party credit. Russian key now translates all six English process labels; groundwater limitation remains explicit. |
| 05 | 5.7-B | INTEGRATED | PENDING | PENDING | PASS | PENDING | PENDING | Local bilingual SVG adapted from AMS Project Atmosphere: Clouds (2025), Figure 2. Exact source CC BY-SA 4.0 verified; chapter attribution, licence link and change statement present. Derivative project licence decision and scientific review remain open. |
| 05 | 5.8-A | INTEGRATED | PENDING | PASS | PASS | PENDING | PENDING | Five NOAA JetStream components enumerated (four language-neutral front symbols plus cold-occlusion cross-section); public-domain guidance applies absent third-party credit. Russian key translates all English cross-section labels. |
| 05 | 5.9-A | INTEGRATED | PENDING | PENDING | PASS | PENDING | PENDING | Project-local bilingual weather-versus-climate SVG embedded in RU/EN; static SVG structure checked. Scientific content, creator/licence, accessibility and rendered QA remain open. |
| 05 | 5.10-A | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | Chapter 05 asset-to-ID mapping has been reconciled for this named visual; review dimensions remain pending. |
| 05 | 5.11-A | INTEGRATED | PENDING | PASS | PASS | PENDING | PENDING | Commons file page confirms CC0 1.0; creator Nothda and Beck et al. (2023) data source/DOI credited. Russian key translates the English title; standard Köppen–Geiger codes remain unchanged. Methodology and rendered QA remain open. |
| 05 | 5.12-A | INTEGRATED | PENDING | PENDING | PASS | PENDING | PENDING | Project-local bilingual climate-belts SVG embedded in RU/EN; static SVG structure checked. Scientific review, creator/licence, accessibility and rendered QA remain open. |
| 05 | 5.13-A | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | Provisional audit label only: no corresponding in-text visual marker, selected asset or chapter-register source record found. Do not count as a confirmed ID. |
| 05 | 5.14-A | INTEGRATED | PENDING | PENDING | PASS | PENDING | PENDING | Project-local bilingual atmospheric-hazards SVG embedded in RU/EN; static SVG structure checked. Safety/scientific review, creator/licence, accessibility and rendered QA remain open. |
| 05 | 5.15-A | INTEGRATED | PENDING | PENDING | PASS | PENDING | PENDING | Project-local bilingual climate-change SVG embedded in RU/EN; static SVG structure checked. Scientific review, creator/licence, accessibility and rendered QA remain open. |
| 05 | 5.16-A | INTEGRATED | PENDING | PENDING | PASS | PENDING | PENDING | Project-local bilingual observations-to-forecast SVG embedded in RU/EN; static SVG structure checked. Scientific review, creator/licence, accessibility and rendered QA remain open. |
| 05 | 5.17-A | INTEGRATED | PENDING | PENDING | PASS | PENDING | PENDING | Project-local bilingual climate-graph exercise embedded in RU/EN; static SVG structure checked. Synthetic data/arithmetic, creator/licence, accessibility and rendered QA remain open. |
| 05 | 5.18-A | INTEGRATED | PASS | PENDING | PASS | PENDING | PENDING | Synthetic values and map conventions checked against NOAA: cold front SW of low, warm front east/northeast, symbols point toward movement; isobars at 4 hPa intervals; station pressure codes decode correctly. RU/EN embed and text data table present. Project rights/licence, accessibility and rendered QA remain open. |
| 06 | 6-A | INTEGRATED | PASS | PASS | PASS | PENDING | PENDING | Exact USGS Water Cycle Diagram is Public Domain and reused unchanged with credit; diagram's pools/fluxes and human influences are described in bilingual keys; arrows are identified as qualitative, not measured flow rates. Screen-reader/rendered QA remains open. |
| 06 | 6-B | FOUND | PENDING | PASS | PENDING | PENDING | PENDING | Flanders Marine Institute Global Oceans and Seas v1 (2021) candidate data licence confirmed as CC BY 4.0; attribution required and source requests that raw downloads not be redistributed. Geometry, map design, separate bathymetry background and bilingual integration remain unchecked; Southern Ocean boundary requires an explicit convention note. |
| 06 | 6-C | INTEGRATED | PASS | PENDING | PASS | PENDING | PENDING | New bilingual schematic SVG committed and embedded in both language sections; scientific review is limited to conceptual feature relationships and explicit not-to-scale caveat. Creator/rightsholder and project licence unresolved; rendered and assistive-technology QA pending. |
| 06 | 6-D | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 06 | 6.1-A | INTEGRATED | PASS | PASS | PASS | PENDING | PENDING | Exact USGS chart is public domain and reused unchanged with credit; nested percentages and 1993 data basis are stated; bilingual alt text and translation key added. Screen-reader/rendered QA remains open. |
| 06 | 6.5-A | INTEGRATED | PASS | PENDING | PASS | PENDING | PENDING | New bilingual qualitative profile SVG committed and embedded in both language sections; separates temperature and salinity patterns and notes equatorial-rainfall exception. Creator/rightsholder and project licence unresolved; rendered and assistive-technology QA pending. |
| 06 | 6.7-A | INTEGRATED | PASS | PENDING | PASS | PENDING | PENDING | NOAA/AOML public-domain map of major surface currents plus a new bilingual ChatGPT-assisted schematic of deep-water formation and circulation are embedded in both languages. The schematic distinguishes a conceptual process model from a literal continuous conveyor; local SVG creator/licence unresolved; rendered and assistive-technology QA pending. |
| 06 | 6.9-A | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 06 | 6.11-A | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 06 | 6.12-A | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 06 | 6.13-A | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 06 | 6.14-A | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 06 | 6.15-A | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 06 | 6.17-A | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 06 | 6.18-A | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 07 | 07-A | INTEGRATED | PASS | PENDING | PASS | PENDING | PENDING | Original bilingual conceptual SVG created and embedded; project creator/licence evidence, accessibility review and live browser/mobile QA remain open. |
| 07 | 07-B | INTEGRATED | PASS | PENDING | PASS | PENDING | PENDING | Original bilingual food-web and energy-pyramid SVG created and embedded; arrow direction and example values cross-checked against Chapter 07.4; project creator/licence evidence, accessibility review and live browser/mobile QA remain open. |
| 07 | 07-C | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 07 | 07-D | INTEGRATED | PASS | PASS | PASS | PENDING | PENDING | Adapted bilingual SVG integrated; concept cross-checked against Chapter 07.3 and source figure; exact source file is CC BY 4.0 and attribution/changes recorded. Static SVG and live browser/mobile/accessibility QA remain pending. |
| 07 | 07-E | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 07 | 07-F | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 07 | 07-G | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 07 | 07-H | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 07 | 07-I | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 08 | 08-A | INTEGRATED | PASS | PENDING | PASS | PENDING | PENDING | Original bilingual soil-profile SVG embedded; horizon sequence is explicitly illustrative, not universal. Rights, accessibility and rendered QA remain pending. |
| 08 | 08-B | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 08 | 08-C | INTEGRATED | PASS | PENDING | PASS | PENDING | PENDING | Original bilingual soil-degradation SVG embedded; erosion, salinisation and compaction are conceptual. Rights, accessibility and rendered QA remain pending. |
| 08 | 08-D | INTEGRATED | PASS | PENDING | PASS | PENDING | PENDING | Original bilingual soil–Earth-spheres interface SVG embedded; flows are qualitative, not measured. Rights, accessibility and rendered QA remain pending. |
| 08 | 08-E | INTEGRATED | PASS | PENDING | PASS | PENDING | PENDING | Original bilingual soil-forming-factors SVG embedded; six interacting factors shown. Rights, accessibility and rendered QA remain pending. |
| 08 | 08-F | INTEGRATED | PASS | PENDING | PASS | PENDING | PENDING | Original bilingual landscape-morphology SVG embedded; relief and hierarchy are schematic and school-dependent. Rights, accessibility and rendered QA remain pending. |
| 08 | 08-G | INTEGRATED | PASS | PENDING | PASS | PENDING | PENDING | Original bilingual landscape-mosaic SVG embedded; patches, corridor, matrix and barrier are conceptual. Rights, accessibility and rendered QA remain pending. |
| 09 | 09-A | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 09 | 09-B | INTEGRATED | PASS | PENDING | PASS | PENDING | PENDING | Original bilingual age-sex-pyramid SVG with three hypothetical shapes on a shared age scale; no country/year data asserted. Rights, accessibility and rendered QA pending. |
| 09 | 09-C | INTEGRATED | PASS | PENDING | PASS | PENDING | PENDING | Original bilingual migration-types SVG; distinguishes internal/international, seasonal, return and forced movement, and flow versus stock. No real routes asserted. Rights, accessibility and rendered QA pending. |
| 09 | 09-D | INTEGRATED | PASS | PENDING | PASS | PENDING | PENDING | Original bilingual demographic-transition SVG; conceptual curves only, not a country-specific trajectory. Rights, accessibility and rendered QA pending. |
| 09 | 09-E | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Actual file, lineage/category and embedding not yet reconciled. |
| 09 | 09-F | INTEGRATED | PASS | PENDING | PASS | PENDING | PENDING | Original bilingual hypothetical urban-growth sequence; no real boundaries, dates or remote-sensing observations asserted. Rights, accessibility and rendered QA pending. |
| 09 | 09-G | INTEGRATED | PASS | PENDING | PASS | PENDING | PENDING | Original bilingual demographic-data-source SVG; distinguishes census, civil registration, surveys, administrative and geospatial sources. Rights, accessibility and rendered QA pending. |

## 7. Current metrics — 5 November 2026

- **Image Coverage:** 147/281 named IDs have an image embedded in the relevant chapter source; two historical Chapter 05 positions remain unresolved and are excluded from the denominator.
- **Image Verification:** 0/147 integrated IDs are fully VERIFIED in this audit. Individual PASS results do not imply full verification.
- **Image Gaps:** 134 of 281 named IDs have no confirmed integrated image; two historical Chapter 05 inventory positions remain unresolved. Chapters 07–10 and 21–26 contain substantial remaining gaps. Chapters 01–06 and 11–20 have integrated assets, but most still require rights, scientific, accessibility and rendered technical review.
- **A/B/C counts:** pending asset-by-asset provenance classification.
- **Rights, scientific, language/accessibility and technical results:** pending; no unverified item is counted as PASS.

Do not treat the above as an atlas-wide completion percentage.

## 8. Evidence inspected

- VISUAL_ASSET_REGISTER.md — 231-ID inventory and existing integration claims.
- IMAGE_SOURCES.md — detailed records for Chapters 01–05 plus the Chapter 09-G missing-asset record; remaining chapters still need per-asset provenance records.
- EDITORIAL_STANDARD_ADOPTION.md — previous editorial adoption record, now extended with v1.1 adoption and Geography checks.
- EDITORIAL_READINESS_MATRIX.md — chapter checkpoints and known technical-QA limitations.
- visuals/chapter-05-visual-register.md — detailed Chapter 05 integration/pending list.

This baseline is not a complete visual inspection of all chapter files and is not a live-site QA run. No creator, licence, source date, scientific PASS or rendering PASS is inferred without evidence.

## 9. Next audit sequence

1. Reconcile chapter in-text IDs, production briefs, actual files and embedded paths; Chapter 09's 09-G is now reconciled as MISSING, while Chapter 05's two unnamed slots remain first priority.
2. Verify Chapters 01–02 against exact source pages, licences, attribution, files and bilingual alt text.
3. Complete provenance/category/rights records for Chapters 03–26, prioritising existing integrated assets before any new search.
4. Review scientific accuracy and pedagogical limitations.
5. Check RU/EN labels, captions and alt text; distinguish page localisation from visual adaptation.
6. Run local-file/SVG/path/metadata checks, then deployed desktop/tablet/mobile, zoom/reflow, keyboard and screen-reader QA.
7. Update lifecycle statuses and calculate coverage, verification, gaps and A/B/C counts only from reconciled evidence.

**No visual is marked VERIFIED in this baseline.**

## 7. Direct repository reconciliation — 5 November 2026

This section supersedes earlier provisional statements in Sections 5–6 wherever they conflict with the direct file inspection below.

### 7.1 Chapter 09 correction

The actual file `chapters/09-population-and-demography.md` contains the bilingual teaching marker and production brief for **09-G** (demographic data sources). It is not a missing or speculative ID. The register's Chapter 09 row must therefore include 09-A–09-G (7 IDs), and the earlier statement that 09-G was absent from the chapter is withdrawn. The 09-G visual itself remains a placeholder: no finished image is embedded in the chapter.

### 7.2 Chapter-count reconciliation

The chapter-level inventory counts, with Chapter 09 corrected to seven IDs, sum to **283**. The register's headline claim of 231 is therefore not supported by its own chapter rows. Chapter 05 still needs exact ID-name reconciliation: its inventory says 20, while the source and subsection sequence has not yet been mapped into a verified, complete 20-ID list. Do not invent missing Chapter 05 labels. Until that mapping and the chapter-by-chapter marker/brief audit are complete, 283 is the sum of stated chapter counts, not a fully validated unique-ID total.

### 7.3 Direct Markdown embedding scan

The following counts are from the actual chapter Markdown files in `workspace/geography`, not from prior checkpoint summaries:

| Chapter | Markdown image embeds | Findings |
|---:|---:|---|
| 01 | 10 | Five distinct local SVGs, each embedded in both language sections (5 unique assets). |
| 02 | 40 | Twenty distinct source/local image assets across the bilingual chapter (19 visual IDs; one ID uses two separate cycle images). |
| 03 | 26 | Thirteen distinct visuals embedded in both language sections; local SVGs plus three external scientific source images. |
| 04 | 32 | Sixteen distinct local bilingual SVGs embedded in both language sections. |
| 05 | 42 | 21 distinct image URLs (10 local SVGs and 11 external source-image URLs); 17 named visual IDs now have integrated imagery. Exact ID-to-image mapping and two unnamed inventory slots still need reconciliation. |
| 06–17 | 12 | Chapter 06 has five integrated visual IDs (6-A, 6-C, 6.1-A, 6.5-A and 6.7-A); 6.7-A contains two separate visuals, giving six embeds in RU and six in EN. Chapters 07–17 have no Markdown image embeds in this scan. |
| 18 | 1 | Local SVG 18-J referenced. |
| 19 | 1 | Local SVG 19-H referenced. |
| 20 | 2 | Local SVGs 20-I and 20-K referenced. |
| 21–26 | 0 | No Markdown image embeds found in these chapter files in this scan. In-text visual markers/briefs are present; treat these as unintegrated placeholders unless another rendering mechanism is independently demonstrated. |

The current `geography/visuals/` directory contains eight SVG assets plus the Chapter 05 source/integration register. The current `geography/assets/` directory contains the chapter SVG assets and a `diagrams/` subdirectory. Presence in a directory does not by itself prove that an asset is embedded, scientifically approved, licensed, accessible or verified.

### 7.4 What this scan does and does not establish

- Markdown link presence and local file existence are confirmed for the items listed above.
- This scan does not establish successful loading from external hosts, visual correctness, current source permissions, bilingual equivalence of every caption/alt text, or deployed/mobile rendering.
- No asset is promoted to VERIFIED by this scan.
- The earlier Chapter 09 discrepancy is resolved at the chapter-file level; the overall inventory discrepancy and Chapter 05 mapping remain open.
- Progress percentage is intentionally withheld until the complete ID list and per-asset evidence are reconciled; counting Markdown embeds would overstate completed visual work.


### 7.5 Chapter 05 local SVG and alt-text spot check

The eight SVG files currently present in `geography/visuals/` were fetched from the working branch and checked for basic embedded accessibility metadata. All eight contain an SVG `viewBox`, `role="img"`, `aria-labelledby`, a `<title>` and a `<desc>`. This is a positive static structural check, not a full accessibility pass: title/description quality, reading order, contrast, small-screen legibility and screen-reader output still require content-level and rendered review.

The Chapter 05 Markdown now contains 42 image embeds; all 42 have non-empty Markdown alt text. Chapters 18, 19 and 20 contain respectively 1, 1 and 2 local SVG embeds, and all four have non-empty bilingual alt text. These checks establish that alt text is present, not that every alternative is sufficiently descriptive or equivalent in both languages.

**Chapter 05 current evidence state:** local SVG metadata = structural PASS; non-empty Markdown alt text = structural PASS; full scientific review, exact ID-to-asset mapping, rights/source verification for every embedded external image, bilingual semantic equivalence and deployed rendering/accessibility = PENDING.


## Chapter-source ID token scan — 5 November 2026

A source-level scan was run across all 26 Markdown chapter files in the current branch. It extracts chapter-prefixed visual-ID-shaped tokens from the full chapter text. This is a discovery scan, **not** a deduplicated count of visual assets: legacy aliases, production-brief references, repeated teaching markers and malformed/ambiguous tokens require semantic reconciliation.

| Chapter | ID-shaped tokens found | Interpretation / follow-up |
|---:|---:|---|
| 01 | 5 | Matches the register's five IDs. |
| 02 | 21 | Includes both zero-padded and unpadded forms (for example, 02-A/2-A and 02-D/2-D); confirm alias equivalence before counting. |
| 03 | 14 | Includes legacy 3-A in addition to the 13 numbered subsection IDs; resolve alias or duplicate status. |
| 04 | 17 | Includes legacy 4-A in addition to the 16 numbered subsection IDs; resolve alias or duplicate status. |
| 05 | 17 named IDs | Seventeen named visual IDs now have image assets embedded in both language sections, including 5.18-A. The chapter's legacy inventory still claims 20 positions; two labels remain unresolved, and provisional 5.10-A/5.13-A entries are not accepted as confirmed IDs. |
| 06 | 15 | Matches the current 15-ID inventory. |
| 07 | 9 | 7 integrated (07-A, 07-B, 07-D, 07-F, 07-G, 07-H, 07-I); two map needs remain open (07-C, 07-E). |
| 08 | 7 | Matches the current inventory. |
| 09 | 7 | Matches the current inventory: 09-B, 09-C, 09-D, 09-F and 09-G integrated; 09-A and 09-E remain open. |
| 10 | 7 | Matches the current inventory. |
| 11 | 7 | Matches the current inventory. |
| 12 | 10 | Matches the current inventory. |
| 13 | 11 | Matches the current inventory. |
| 14 | 9 | Matches the current inventory. |
| 15 | 11 | Matches the current inventory. |
| 16 | 9 | Matches the current inventory. |
| 17 | 9 | Matches the current inventory. |
| 18 | 10 | Matches the current inventory. |
| 19 | 10 | Matches the current inventory. |
| 20 | 11 | Matches the current inventory. |
| 21 | 10 | Matches the current inventory. |
| 22 | 10 | Matches the current inventory. |
| 23 | 12 | Matches the current inventory. |
| 24 | 12 | Matches the current inventory. |
| 25 | 12 | Matches the current inventory. |
| 26 | 12 | Matches the current inventory. |
| **Total** | **275** | Raw ID-shaped tokens across chapter sources; not a unique-asset denominator. The register's chapter-row sum is 283 and its legacy headline is 231. These three figures describe different counting scopes and are not reconciled. |

### Immediate conclusions

1. The Chapter 09 discrepancy is resolved: 09-G exists in the chapter and is a missing visual, not an invented ID.
2. Chapters 02–04 contain legacy aliases or mixed ID formats; these must be mapped to canonical IDs without deleting source history.
3. Chapter 05 needs a dedicated ID-to-figure reconciliation. Its chapter source does not expose the 20-ID inventory as 20 distinct, consistently marked needs. Existing embedded visuals and captions must be mapped individually before any coverage calculation.
4. Chapters 06–26 (except the Chapter 09 gap status) have token counts matching the register's row counts in this scan. This confirms count-level consistency only, not actual file existence, provenance, scientific validity, rights, bilingual parity or accessibility.

No Image Coverage or Image Verification percentage is calculated from this token scan.


### 7.6 Static SVG structure and Markdown alt-text checks — Chapters 01–06 and 18–20

A direct fetch-and-inspect pass covered the **56 pre-existing local SVG assets** in Chapters 01–05 and 18–20. Three additional local SVGs were added for Chapter 06 visuals 6-C, 6.5-A and 6.7-A; all three were separately spot-checked for the required structural metadata:
- 5 Chapter 01 SVGs in `assets/diagrams/`;
- 11 Chapter 02 SVGs in `assets/diagrams/`;
- 10 Chapter 03 SVGs in `assets/`;
- 16 Chapter 04 SVGs in `assets/`;
- 10 Chapter 05 SVGs in `visuals/`;
- 4 Chapter 18–20 SVGs in `assets/`.

All 56 pre-existing fetched SVG files and all three new Chapter 06 SVGs (6-C, 6.5-A and 6.7-A) contain the five structural elements checked: `viewBox`, `<title>`, `<desc>`, `role="img"` and `aria-labelledby`. This is a static structure check only; it does not certify that descriptions are sufficiently informative, labels are legible, colour contrast is adequate, or screen readers announce the content in a useful order.

Markdown alt-text checks:
- Chapters 01–02: the source register records 50 embeds with non-empty bilingual alt text (10 + 40).
- Chapter 03: 26 embeds representing 13 unique assets; zero empty alt attributes.
- Chapter 04: 32 embeds representing 16 unique assets; zero empty alt attributes.
- Chapter 05: 42 embeds (21 RU + 21 EN; 21 distinct URLs in each language, exact parity); zero empty alt attributes.
- Chapters 18–20: 4 embeds; zero empty alt attributes.
- Chapter 06: 6-A, 6-C, 6.1-A, 6.5-A and 6.7-A each appear once in RU and once in EN; all ten embeds have non-empty bilingual alt text.

**Result:** structural SVG metadata and non-empty Markdown alt text pass for the checked local assets and chapter embeds. Semantic alt-text quality, bilingual equivalence, scientific correctness, rights evidence and deployed accessibility remain separate and pending checks. No asset is promoted to VERIFIED.


## Chapters 03–04 — source-path, SVG metadata and bilingual-alt validation — 5 November 2026

### Chapter 03 — Lithosphere and geological processes

- Confirmed 10/10 expected local SVG assets exist under `geography/assets/` and are referenced from the chapter: 03-1-A, 03-3-A, 03-4-A, 03-6-A, 03-7-A, 03-8-A, 03-10-A, 03-11-A, 03-12-A and 03-12-B.
- Confirmed three distinct external image references are present: USGS mineral specimens (`OreSampleImages.png`), the USGS/Smithsonian *This Dynamic Planet* tectonic map (`DynamicPlanet.JPG`), and the International Commission on Stratigraphy chart (2026/06).
- The 13 distinct visual references are each embedded twice in the Markdown source (Russian and English sections): 26 image embeds. All 26 image elements have meaningful alt text containing both language descriptions.
- All 10 local SVG files have a `viewBox`, one bilingual `title`, one bilingual `desc`, and no detected `script`, `foreignObject` or embedded `image` element. This is source-pattern validation, not a full XML conformance or rendered-visual test.
- **Still pending:** exact-file rights evidence for the three external images; provenance, creator/rightsholder and authoring-method evidence for the 10 project-local SVGs; detailed geological accuracy review; caption/attribution audit; responsive/rendered and assistive-technology checks.

### Chapter 04 — Landforms and relief

- Confirmed all 16 expected local SVG assets exist under `geography/assets/` and are referenced from the chapter: 04-2-A through 04-15-B, including the two 04-14 and two 04-15 visual pairs.
- The 16 distinct visual references are each embedded twice (Russian and English sections): 32 image embeds. All 32 image elements have meaningful bilingual alt text.
- All 16 SVG files have a `viewBox`, one bilingual `title`, one bilingual `desc`, and no detected `script`, `foreignObject` or embedded `image` element.
- **Still pending:** creator/rightsholder and authoring-method evidence; scientific review of landform morphology, process direction, map conventions, vertical datum/scale where applicable, and the Everest/Challenger Deep comparison; captions/attribution; rendered and assistive-technology QA.

### Status interpretation

These checks establish that the expected local files exist, the chapter source references them, the bilingual alt text is populated, and the SVG source contains basic accessible metadata. They do **not** establish scientific accuracy, rights clearance, complete learner-facing captions, visual legibility after rendering, or VERIFIED status. All 26 local SVG assets remain lifecycle **INTEGRATED** at most; the five review dimensions remain **PENDING** pending evidence.


### Chapter 03 — exact-file rights verification update — 5 November 2026

- `3.2-A` USGS Ore/Mineral Sample Images: the exact USGS media page identifies this complete composite as Public Domain. The page also discloses source imagery from USGS, Smithsonian Institution, Minerals Education Coalition and Adobe Stock. Rights are recorded PASS for reuse of the complete published composite under the page's item-level Public Domain statement; do not extract or reuse component specimens as separate files.
- `3.5-A` *This Dynamic Planet* I-2800: the exact USGS media page identifies the image as Public Domain. It is a 2006 reference map and must not be represented as current hazard, earthquake or plate-motion data.
- `3.9-A` ICS International Chronostratigraphic Chart v2026/06: the current ICS chart page identifies © ICS 2026 and CC BY 4.0. The chapter reuses the chart unchanged and provides a bilingual source credit. Rights PASS. A Russian companion key to the paired stratigraphic/geochronologic ranks and principal eons/eras was added; full translation of all chart subdivisions remains PENDING.
- These are rights findings only; scientific, language/accessibility and technical review dimensions remain separately open as recorded in the per-asset table.


### 7.7 Chapter 05 stable-ID anchors added

To make the image-first audit traceable in the chapter itself, non-rendering HTML comments were added immediately before every Markdown image embed in both language sections. Verification after the commit found **42 anchors covering 17 distinct integrated visual IDs**:
`5.1-A`, `5.2-A` (legacy alias `5-A`), `5.3-A`, `5.4-A`, `5.5-A`, `5.6-A`, `5.7-A`, `5.7-B`, `5.8-A`, `5.9-A`, `5.11-A`, `5.12-A`, `5.14-A`, `5.15-A`, `5.16-A`, `5.17-A` and `5.18-A`. Repeated anchors for the same ID are intentional: Russian and English placements share one asset ID, and 5.8-A groups the official front symbols/cross-section into one teaching visual set.

The 5.18-A placeholder has been replaced by a bilingual SVG and the chapter now embeds it once in each language section. The chapter-level inventory still claims 20 IDs, while the visual source/integration register explicitly names 16 integrated IDs plus 5.18-A. **Two inventory ID positions remain unaccounted for by name** and must be recovered from the original chapter brief/history or removed only after documented reconciliation; do not invent labels. The legacy label 5-A is an alias for 5.2-A, not a separate visual asset. The comments do not alter visible page content.


### Chapter 04 — focused scientific review: 4.13-A — 5 November 2026

- Checked Everest's 8,848.86 m ± 0.06 m IHRS snow-surface height against Xie et al. (2022); checked Challenger Deep's 10,935 m ± 6 m (95% CI) pressure-derived value against Greenaway et al. (2021); and checked the 10,927 m preferred gridded estimate plus 10,914–10,932 m model-sensitivity envelope against Fujii et al. (2026).
- Confirmed that the sensitivity range is not labelled as a confidence interval, that the 2026 result is not presented as a definitive redetermination, and that the figure warns the vertical comparison is not one linear scale.
- Scientific/data-claim result for 4.13-A: **PASS**. The SVG's creator/rightsholder, project licence, technical rendering and full accessibility review remain PENDING; therefore lifecycle status remains INTEGRATED, not VERIFIED.


### 7.8 Marker repetition scan — Chapters 06–26

A source scan of all chapter files 06–26 found **210 distinct visual IDs** across those 21 chapters. Every enumerated ID appears at least twice in its chapter file. This is consistent with repeated teaching-location/production-brief references, but repetition alone does not prove that the Russian and English contexts are semantically equivalent. The chapter files in this range now contain **sixteen Markdown image embeds** representing nine integrated visual IDs: 6-A, 6-C, 6.1-A, 6.5-A and 6.7-A in both languages, plus the four local SVG placements in Chapters 18–20 (18-J, 19-H, 20-I and 20-K). The remaining 201 IDs are MISSING; 6-B is FOUND but not integrated. Repeated IDs are not evidence of finished visuals and still require source, rights, scientific, language, accessibility and technical review.


### Chapter 05 — bilingual image parity correction — 5 November 2026

- The chapter source contains 21 distinct image URLs and 42 Markdown image embeds. A previous scan incorrectly reported three project-local SVGs as Russian-only because it misclassified English headings; a fresh section-boundary-aware scan confirms every URL appears once in each language section.
- Added the same three assets to the corresponding English sections, with bilingual alt text, captions and the existing learning limitations preserved.
- Rechecked the chapter: **42 image embeds, 21 unique URLs, every URL appears exactly twice** (one RU and one EN occurrence). The three SVGs each have a bilingual title, bilingual source text/labels, a viewBox, and no detected script, foreignObject or embedded image element.
- RU/EN parity for 5.12-A, 5.14-A and 5.15-A is now **PASS** at the chapter-source level. Their creator/rightsholder, project licence, scientific review and rendered technical checks remain PENDING; none is VERIFIED.
- The chapter's 5.18-A synoptic-map exercise is now integrated in both language sections; scientific, rights, accessibility and rendered technical review remain pending.


### 7.9 Chapter 05 visual defect corrected — climate diagram month labels

The static content review of `chapter-05-climate-diagram-exercise.svg` found that all 24 month labels (12 months in each of two climate diagrams) were Russian-only despite the asset being presented as bilingual. Replaced them with stacked Russian/English abbreviations. A post-update fetch confirms 24/24 month-label groups now contain both scripts. The dataset remains explicitly labelled as synthetic teaching data, not observations from real weather stations. This fixes the language-parity defect for the month labels only; the full visual and scientific review remains pending.


### Current integration snapshot — Chapters 06–26 — 5 November 2026

A refreshed chapter-by-chapter source scan confirms 210 planned visual IDs in Chapters 06–26. Seventy-seven are embedded in their relevant chapter source; 133 remain open. This counts actual chapter embeds only and does not imply scientific, rights, language, accessibility or rendered technical approval.

| Chapter range | Required IDs | Integrated | Missing |
|---|---:|---:|---:|
| 06–17 | 111 | 58 | 53 |
| 18–20 | 31 | 19 | 12 |
| 21–26 | 68 | 0 | 68 |
| **Total** | **210** | **77** | **133** |

Chapter 07-D is a bilingual adapted SVG under CC BY 4.0 and is integrated. Chapter 07-A, 07-B, 07-C, 07-E, 07-F, 07-G, 07-H and 07-I remain open. Integrated assets remain INTEGRATED until all applicable review dimensions are supported by evidence.
### 7.10 Chapter 05 bilingual embed parity rechecked

A fresh section-boundary-aware scan (using the explicit `## English-language chapter text` heading, rather than guessing from bilingual subsection titles) confirms **42 Markdown image embeds: 21 in Russian and 21 in English**. The same 21 unique image URLs occur exactly once in each language section; no source URL is missing from either section and none of the 42 alt-text fields is empty. All 42 embeds have a preceding stable visual-ID anchor. This supersedes any earlier 37-embed counts in this audit, which came from an incomplete scan.


### Chapter 05 — static SVG structure check — 5 November 2026

Fetched and inspected all eight project-local Chapter 05 SVGs:
- `chapter-05-dry-air-composition.svg`
- `chapter-05-cloud-formation-processes.svg`
- `chapter-05-weather-vs-climate.svg`
- `chapter-05-global-climate-belts.svg`
- `chapter-05-atmospheric-hazards.svg`
- `chapter-05-climate-change-drivers-evidence-responses.svg`
- `chapter-05-weather-observations-to-forecast.svg`
- `chapter-05-climate-diagram-exercise.svg`

All eight contain a `viewBox`, SVG `title`, `desc` and `role="img"`; both Cyrillic and Latin text are present. No `script`, `foreignObject` or embedded `image` element was detected. This is a static source-structure check only. It does not validate SVG rendering, visual contrast at display size, reading order, text scaling, scientific correctness of every label, creator/rightsholder or licence, keyboard interaction, or screen-reader output. Accordingly, accessibility and technical integration remain PENDING in the per-asset audit.


## Chapters 03–04 — scientific and bilingual content review

### Chapter 03 — Visual 3.9-A: International Chronostratigraphic Chart

The source chart is the official ICS version 2026/06, reused unchanged under CC BY 4.0. Its embedded labels are English-only. The Russian chapter section now includes a compact key translating the hierarchy and principal eons/eras; the English section now includes the equivalent bilingual guide. Both sections distinguish geochronological time units (eon, era, period, epoch, age) from chronostratigraphic rock units (eonothem, erathem, system, series, stage), and explain that the chart layout is non-linear. The previous editorial instruction beginning “Vertical geological time scale…” has been removed from the learner-facing text.

**Result:** source rights PASS for unchanged reuse; bilingual explanatory parity PASS at the surrounding-text level; no claim of a complete translation of every label in the source chart. Scientific age-boundary verification, full alt-text quality and deployed rendering remain PENDING.


### Chapter 04 — Visual 4.14-B: DEM, DSM and DTM

The static content review found a misleading DTM depiction: the original graphic described it as a “terrain representation” and included a dashed subsurface line, while the adjacent chapter text correctly defines a DTM as a model intended to represent bare ground. Corrected the SVG description and labels to state that the DTM panel shows bare-earth terrain with buildings and vegetation removed, and removed the subsurface line so the figure no longer suggests that a DTM represents underground geology. The chapter text continues to warn that DEM/DTM terminology varies by provider and that dataset metadata must be checked.

**Result:** conceptual definition now aligns with the chapter explanation; scientific concept check PASS for the distinction represented. Rights/creator provenance for the project-local SVG, detailed alt-text review and rendered layout remain PENDING.

### Chapter 04 — Visual 4.15-B: topographic-map exercise

Cross-checked the diagram's elevations and distances against the chapter's bilingual answer key. A–C: 40 m rise over 500 m horizontal distance = 8% gradient (about 4.6°); C–B: 20 m over 750 m = about 2.7% (about 1.5°). Spot heights A=100 m, C=140 m and B=160 m are internally consistent. The exercise is explicitly schematic and not for navigation.

**Result:** arithmetic and diagram-label consistency PASS. Rights/creator provenance, full accessibility and rendered technical checks remain PENDING.


### Chapter 05 — 5.18-A integration checkpoint — 5 November 2026

- Created `geography/visuals/chapter-05-synoptic-map-climate-analysis.svg` as a new bilingual synthetic teaching schematic. It contains a schematic low-pressure centre (1000 hPa) and high-pressure centre (1032 hPa), closed isobars at 4 hPa intervals, cold and warm fronts, simplified station plots and two synthetic monthly climate graphs.
- Replaced the Russian and English placeholders with the same local SVG and bilingual alt text/captions. The chapter source now has 42 image embeds and 21 unique image URLs; the new asset appears once in each language section.
- Static source inspection confirms `viewBox`, `title`, `desc`, `role="img"`, Cyrillic and Latin text; no script, foreignObject or embedded image element was detected.
- The climate graph arrays were checked: A has a 32 °C annual temperature range and 401 mm annual precipitation; B has a 14 °C range and 886 mm annual precipitation. These are synthetic values, not observations.
- Image-first discovery consulted NOAA synoptic meteorology and surface-weather-plot teaching resources. No existing image was reused because the brief requires synthetic data and two climate graphs in one bilingual teaching visual.
- Lifecycle is INTEGRATED; RU/EN parity is PASS at source level. Scientific convention review, project rightsholder/licence, visual/accessibility review and rendered browser/device QA remain PENDING. No CI pass is claimed.


### Chapter 03 — Visual 3.9-A: external source verification

The official ICS chart page and its 2026/06 release note were checked against the source record. The current chart is explicitly labelled v2026/06 and CC BY 4.0; the release note confirms that the version includes revised numerical ages for the Anisian, Olenekian and Wuchiapingian boundaries. The official translations page lists Russian as v2017/02, not as a current 2026/06 Russian chart. The atlas therefore keeps the current English original unchanged and provides its own bilingual explanatory key. This avoids silently substituting an outdated Russian chart for the current official version.

Rights/licence and version provenance: PASS. Chapter-level RU/EN explanatory support: PASS. Scientific use limitation (ages may be revised; non-linear chart layout) is stated. The chart itself remains English-labelled; a full graphic translation is not claimed. Source evidence: [current chart](https://stratigraphy.org/chart/), [2026/06 update](https://stratigraphy.org/news/156), [official translations](https://stratigraphy.org/supplementary).


### Chapter 03 — Visual 3.11-A: mineral-resource lifecycle

The bilingual SVG had two localisation/sequence clarity defects: the “control and monitoring” line was English-only, and the diagram did not explain clearly that resource assessment precedes extraction while waste/water management spans the project lifecycle. Added the Russian equivalent and a concise bilingual sequence note; updated the SVG description to include resource assessment. This improves language parity and prevents readers from interpreting waste management as a single late-stage activity. The conceptual diagram is still simplified and does not replace a full mine-planning or closure framework.

**Result:** bilingual label completeness PASS for the corrected labels and note; scientific sequence statement PASS at introductory teaching level. Rights/creator provenance, detailed visual legibility and rendered accessibility remain PENDING.

### Chapter 04 — Visual 4.10-A: coastal and ocean-floor relief

Corrected a mixed-script typo in the Russian label for *tombolo* (“Тombolo” → “Томболо”). No change to the scientific content.


### Chapter 04 — Visual 4.11-A: slope processes

The diagram grouped *talus* with movement types, although talus is an accumulation/deposit of angular rock fragments rather than a movement mechanism. Corrected the label to “Осыпное отложение / Talus deposit”, revised the SVG description so it no longer classifies talus as a movement, and changed the footer to distinguish movements from their deposits. The adjacent chapter text already defines scree/talus as an accumulation at the foot of a slope.

**Result:** scientific classification and bilingual label corrected; conceptual consistency PASS for this distinction. Rights/creator provenance, detailed accessibility and rendered technical checks remain PENDING.


### Chapter 03 — Visual 3.12-B: relative dating and cross-cutting relationships

The original SVG and chapter caption implied that the relative order of the intrusion and fault could be inferred from their cross-cutting relationships. Inspection of the actual geometry showed that both features cut the strata but do **not** intersect each other. Their relative order therefore cannot be established from this diagram. Corrected the SVG title description and footer, and updated both language sections of the chapter to state the limitation explicitly. Removed a learner-facing editorial instruction (“provide learner questions and a separate answer key”) that had been left in the Russian section.

**Result:** scientific interpretation corrected; bilingual caveat now present in both language sections. The diagram supports dating each cross-cutting feature relative to the strata, but not dating the fault relative to the intrusion. Rights/creator provenance, detailed accessibility and rendered technical checks remain PENDING.


### Chapter 05 — 5.18-A scientific convention review — 5 November 2026

Scientific/data review for the synthetic exercise is **PASS** at the teaching-schematic level:
- NOAA's surface-map guidance confirms that cold-front triangles and warm-front semicircles point in the direction of movement; the schematic follows this convention.
- The low-pressure centre is shown with the cold front extending southwest and the warm front extending east/northeast, consistent with the standard Northern Hemisphere mid-latitude cyclone teaching pattern.
- Isobars are closed and labelled at 4 hPa intervals; pressure increases outward from the low and decreases outward from the high.
- The simplified station plots clearly distinguish temperature, dew point, three-digit sea-level pressure code and wind-from direction. The codes 142, 118 and 208 are decoded as 1014.2, 1011.8 and 1020.8 hPa, respectively.
- Climate-graph values are explicitly synthetic. The data table gives all 12 monthly values; arithmetic checks confirm A = 401 mm annual precipitation and 32 °C annual temperature range, B = 886 mm and 14 °C.
- The graphic is labelled as a Northern Hemisphere schematic with no geographic location/date; it is not an operational weather analysis or forecast.

Sources checked: NOAA, [How to read Surface Weather Maps](https://www.noaa.gov/jetstream/wxmaps) and [Surface Weather Plot Symbols](https://www.noaa.gov/jetstream/wxmaps-max/jetstream-max-surface-weather-plot-symbols); Penn State METEO 3, [decoding sea-level pressure on a station model](https://courses.ems.psu.edu/meteo3/book/export/html/1998).

This PASS is limited to the stated scientific conventions and synthetic data. It does not approve the unknown project licence/rightsholder, colour contrast at rendered sizes, full screen-reader usability, or deployed display.


### Chapter 05 — Visual 5.12-A: global climate belts

A comparison of the SVG with the adjacent chapter text found that the text listed seven broad belt types, including the subequatorial belt, while the diagram omitted the subequatorial zones in both hemispheres. Added the missing northern and southern subequatorial bands and updated the SVG description. A post-update source scan confirms 13 labelled zones: six paired belt types (polar, subpolar, temperate, subtropical, tropical and subequatorial) plus the equatorial belt shared at the centre.

**Result:** alignment with the chapter's seven belt types PASS at the conceptual classification level. Boundaries remain schematic and must not be presented as precise global boundaries; local/regional climate controls and seasonal shifts remain noted. Detailed scientific review of the exact geographic boundaries, rights/creator provenance, accessibility and rendered layout remain PENDING.


### Chapter 05 — bilingual SVG accessibility descriptions

A content-level pass found that several SVG `<desc>` elements were English-only, while one was Russian-only. Updated the descriptions for 5.7-B, 5.9-A, 5.12-A, 5.14-A, 5.15-A, 5.16-A and 5.17-A to provide Russian and English descriptions; 5.1-A already contained both languages. A post-update fetch confirms **8/8 local Chapter 05 SVG descriptions contain both Cyrillic and Latin text**. The descriptions summarise each graphic's subject and relevant limits (including synthetic data for 5.17-A and the seven climate-belt types for 5.12-A).

**Result:** presence of bilingual SVG descriptions PASS. Detailed semantic quality, screen-reader output, contrast and rendered layout remain PENDING.


### Chapter 05 — NOAA media rights and bilingual-label check — 5 November 2026

- 5.5-A: the NWS training page identifies the exact embedded image and provides the explanatory context. NOAA's public-domain guidance states that most NOAA material may be reused unless the individual credit/caption says otherwise; no third-party credit is shown. Attribution is recorded as NOAA/NWS Louisville.
- 5.6-A: the exact NOAA `circ.jpg` asset was opened and visually inspected. It contains numbered circulation cells but no English prose labels; the bilingual chapter caption supplies the explanation. NOAA attribution recorded; reuse basis is U.S. public domain, not a worldwide CC licence.
- 5.7-A: the exact NOAA water-cycle image was opened. It contains six English labels; a bilingual key was added in the chapter to translate each process. NOAA attribution recorded. The caption continues to state that groundwater exchange and some reservoirs are omitted.
- 5.8-A: all five exact NOAA components were enumerated and opened: cold, warm, stationary and occluded front symbols, plus the cold-occlusion cross-section. The four symbol files are language-neutral; a bilingual key now translates all English labels in the cross-section. NOAA attribution recorded.
- For these unchanged NOAA/NWS assets, rights and RU/EN explanatory support are now PASS. Scientific review of each source figure, rendered accessibility and browser/device QA remain separate and pending.

Source: NOAA [image reuse guidance](https://oceanservice.noaa.gov/about/faq.html) and [JetStream usage note](https://www.noaa.gov/jetstream).


### Chapter 05 — Visual 5.3-A rights correction and source replacement

The prior embed was a UCAR-hosted reproduction of IPCC AR6 WGI Figure 7.2. The IPCC copyright policy states that its figures may be reproduced only within its specified limited non-commercial terms and prohibits redistribution/alteration beyond those conditions; the chapter's public-site redistribution rights were not established. The IPCC figure was therefore removed rather than treating UCAR hosting as a licence.

Replaced it with the NASA / My NASA Data “Earth's Energy Budget” diagram, whose exact source page credits NASA and whose image contains data citations to Loeb et al. (2009) and Trenberth et al. (2009). NASA's current media guidance generally permits factual educational/informational reuse on websites when NASA is credited and no third-party copyright notice applies. The chapter caption now states that the flux values are a ten-year average, not current measurements. The image is reused unchanged.

**Result:** rights PASS for educational/informational reuse with NASA credit; RU/EN caption and alt-text parity PASS. Scientific review of the historic ten-year data context is recorded; full scientific verification of each numeric flux, detailed accessibility and deployed rendering remain PENDING.


The newly integrated Chapter 05 visual 5.18-A was also fetched and checked for the same five structural SVG elements; all are present. This brings the current local SVG inventory checked in this pass to 55.


### Chapter 05 — 5.2-A replacement checkpoint — 5 November 2026

The previous Commons CC0 file was inspected directly. Despite its filename, `Atmosphere layers edu.svg` is a German-language diagram, and its file page reports two W3C SVG validation errors. It was not suitable for the Russian/English atlas. A new original bilingual SVG now replaces it. The new diagram's layer ranges and temperature trends were checked against NOAA JetStream; the ionosphere is explicitly shown as an overlapping region, not a sixth thermal layer. The 100-km Kármán line is labelled as a convention, not a physical boundary.

The new local SVG passed static source checks (`viewBox`, bilingual title/description, `role="img"`, no script/foreignObject/embedded image). Its creator/rightsholder and project licence remain Unknown / PENDING; visual rendering and accessibility QA remain open.


The newly integrated Chapter 05 local atmosphere-layer SVG (5.2-A) was fetched and checked for the same five structural elements; all are present. The English section now uses the same local bilingual SVG as the Russian section, replacing the former German-language CC0 candidate. A fresh chapter scan confirms 21 image URLs in each language, exact URL parity, and 42 total embeds.


### Chapter 05 — consolidated local SVG source check — 5 November 2026

The Chapter 05 local-SVG inventory now contains 10 files: the original eight checked above, plus the new 5.18-A synoptic/climate SVG and the replacement 5.2-A atmosphere-layers SVG. Static source checks on both new files confirm a `viewBox`, bilingual `title` and `desc`, `role="img"`, Cyrillic and Latin text, and no `script`, `foreignObject` or embedded `image` element. Together with the earlier eight-file check, all 10 local SVGs have passed this limited structural check. This is not XML schema validation, visual rendering, contrast/accessibility QA, or browser/device testing; technical and accessibility statuses remain PENDING.

### Chapter 06 — Visual 6.1-A: distribution of Earth's water — 5 November 2026

Integrated the exact USGS Water Science School chart “The distribution of water on, in, and above the Earth” in both Russian and English sections. The USGS media page identifies the image as Public Domain and credits the underlying estimate to Igor Shiklomanov's 1993 chapter in *Water in Crisis*. The chapter now credits USGS and the data source, and explicitly labels the values as rounded historical estimates rather than current measurements.

The three bars are treated as nested categories: total global water; all freshwater; and only surface/other freshwater. The Russian and English sections include matching translations of every chart label. The figure's rounded percentages (96.5% ocean, 2.5% freshwater; 68.7% ice/glaciers, 30.1% groundwater and 1.2% surface/other freshwater) align with the chapter's stated estimates. The right-hand breakdown is not added to the first two bars.

**Result:** scientific/data interpretation PASS for faithful presentation of the cited 1993 estimate; exact-image rights PASS under the USGS Public Domain statement; RU/EN explanatory parity PASS. Alt text and a bilingual key are present, but screen-reader behaviour, contrast at rendered sizes, responsive display and deployed loading remain PENDING.

Source: USGS, [exact image record and detailed description](https://www.usgs.gov/media/images/distribution-water-and-above-earth), [original image file](https://d9-wret.s3.us-west-2.amazonaws.com/assets/palladium/production/s3fs-public/thumbnails/image/EarthsWater-BarChart.png).

### Chapter 06 — Visual 6-A: global water cycle — 5 November 2026

Integrated the exact USGS Water Cycle Diagram (WCD 1) in both Russian and English sections. The USGS media record identifies the exact image as Public Domain; the diagram was created by USGS VizLab with the Water Resources Mission Area Web Communications Branch. The 2022 diagram (image record dated 2023) shows water pools and fluxes across ocean, atmosphere, land, cryosphere and groundwater, as well as human water use and impacts.

The chapter now credits USGS, reuses the image unchanged and provides bilingual keys for the diagram's main pools, fluxes and human-use labels. The caption explicitly states that the schematic is not to scale and that arrows are qualitative directions, not measured annual fluxes. This avoids confusing reservoir stocks with flow rates and keeps the diagram's anthropogenic additions visible.

**Result:** scientific/conceptual fit PASS for the stated teaching purpose; exact-image rights PASS under the USGS Public Domain statement; RU/EN explanatory parity PASS. Screen-reader behaviour, contrast at rendered sizes, responsive display and deployed loading remain PENDING.

Sources: USGS, [exact image record](https://www.usgs.gov/media/images/wcd-1png), [GIP 221 publication and creators](https://pubs.usgs.gov/publication/gip221), [poster PDF and detailed diagram text](https://d9-wret.s3.us-west-2.amazonaws.com/assets/palladium/production/s3fs-public/media/files/USGS_WaterCycle_English_PRINT_20221013_508.pdf).

### Chapter 06 — Visual 6-C: ocean-floor relief — 5 November 2026

Created and integrated a bilingual schematic SVG (geography/assets/06-4-C-ocean-floor-cross-section-bilingual.svg) in both language sections. It labels the continent, continental shelf, continental slope, continental rise, abyssal plain, mid-ocean ridge and deep-sea trench. The graphic explicitly states that horizontal and vertical scales are not proportional and that the depicted features do not necessarily occur together in one real transect. It is a conceptual teaching profile, not measured bathymetry.

**Result:** conceptual scientific review PASS for the limited explanatory purpose; RU/EN parity PASS; source lineage is identified as a new ChatGPT-assisted local SVG, but creator/rightsholder and project licence remain PENDING. Rendered display, contrast, screen-reader behaviour and device QA remain PENDING. The file's structural metadata should be checked in the automated SVG scan before any technical PASS is assigned.

### Chapter 06 — Visual 6.5-A: seawater temperature and salinity profiles — 5 November 2026

Created and integrated a bilingual qualitative SVG (geography/assets/06-5-A-seawater-temperature-salinity-profiles-bilingual.svg) in both Russian and English sections. It compares generalized temperature and salinity profiles in subtropical, temperate and polar waters. The caption explicitly says that curves are illustrative rather than measured data and that actual profiles vary by basin, season, latitude and water masses. It also distinguishes the subtropical evaporation-driven surface salinity maximum from rainy equatorial waters, where surface salinity can be lower.

**Result:** conceptual scientific fit PASS for a qualitative teaching diagram; RU/EN parity PASS. The curves are intentionally unscaled and are not suitable for numerical inference. Creator/rightsholder and project licence remain PENDING; screen-reader behaviour, contrast, responsive rendering and device QA remain PENDING.

### Chapter 06 — Visual 6.7-A: global ocean circulation — 5 November 2026

Integrated two complementary visuals in both language sections. The surface-current map is NOAA/AOML's 2008 map by Rick Lumpkin, reused unchanged from Wikimedia Commons; the file page identifies it as Public Domain. It is labelled as a generalized teaching map, not real-time data. The second image is a new bilingual conceptual SVG created with ChatGPT assistance. It shows poleward surface transport, cooling and densification at high latitudes, sinking, deep spreading, mixing and upwelling. Its description explicitly rejects the idea of one continuous global pipe or an exact route for a single water mass.

**Result:** scientific/conceptual fit PASS for the stated explanatory scope; map rights PASS as a NOAA public-domain work; RU/EN parity PASS. The new local SVG's creator/rightsholder and project licence remain PENDING. Screen-reader behaviour, contrast, responsive rendering and device QA remain PENDING.


## Chapter 17 — detailed visual audit — 5 November 2026

**Scope:** all nine required Chapter 17 visual IDs; branch `workspace/geography`; IMAGE-FIRST POLICY v1.1.  
**Search record:** see `geography/IMAGE_SOURCES.md`, Chapter 17. Candidate searches included the Kyrgyz State Agency/Geoportal and Water Information System, CIA country maps, peer-reviewed Tien Shan tectonic figures, and the Ministry of Natural Resources' 2026 geological-atlas announcement.

| Visual ID | Presence | Scientific / factual | Rights / licence | RU–EN parity | Accessibility | Technical | Finding / next action |
|---|---|---|---|---|---|---|---|
| 17-A | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Current boundary geometry and political-map provenance not established; do not use 2005 CIA map as a current border map. |
| 17-B | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | AF NWRMP's 2017 terrain map is an image, not the underlying DEM; vertical datum/accuracy and image reuse terms remain unknown. |
| 17-C | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Academic tectonic figures are study-specific; choose a regional classification and document rights before reuse or redraw. |
| 17-D | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | AF NWRMP has river-basin maps uploaded in 2022, but these are hydrological catchments, not the intermontane-valley geomorphology requested; reuse terms remain unknown. |
| 17-E | INTEGRATED | PASS | PENDING | PASS | PENDING | PENDING | Original bilingual timeline integrated; creator/rightsholder, project licence and rendered/technical checks remain pending. |
| 17-F | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | AF NWRMP's 2017 seismic-hazard map is a historical hazard-zonation image, not an active-fault map/current catalogue; source image rights and current dataset remain unverified. |
| 17-G | INTEGRATED | PASS | PENDING | PASS | PENDING | PENDING | Original bilingual relief-process schematic integrated; creator/rightsholder, project licence and rendered/technical checks remain pending. |
| 17-H | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | AF NWRMP's 2017 geology map cites a 1988 source and is not a current mineral-district map; await the national atlas or verified open layers. |
| 17-I | MISSING | PENDING | PENDING | PENDING | PENDING | PENDING | Open Data classifier is 2019, licence unspecified and not geometry; Kyrgyzmap/nsdi.kg current access not confirmed on 5 Nov 2026; obtain a current official boundary dataset and reuse terms. |

**Results and controls**
- Required visuals: 9. Integrated: 3 (17-C, 17-E and 17-G). **Image Coverage: 3/9 = 33.3%.**
- Image Verification: 0/3 = 0%; none of the three integrated visuals is VERIFIED because creator/rightsholder, project licence and rendered/technical/accessibility evidence remain pending.
- Categories A/B/C: 0/0/3 integrated. All three integrated assets are Category C original bilingual SVGs authored with ChatGPT assistance; creator/rightsholder and explicit project licence remain Unknown / PENDING.
- Rights: no Chapter 17 asset has passed. Scientific/conceptual fit and RU/EN parity PASS for 17-C, 17-E and 17-G within their stated limits; rights, rendered accessibility and technical QA remain PENDING. The other six assets remain MISSING.
- Candidate CIA maps (2005) were rejected for current administrative/border use because of age; their public-domain status does not cure geographic obsolescence. Peer-reviewed tectonic figures remain literature candidates only; their exact figure rights and scope must be checked.
- The Ministry's 11 March 2026 geological-atlas announcement describes a project in preparation; it is not evidence that the atlas or its maps are already published or reusable. The 2019 open-data classifier and historical Kyrgyzmap/nsdi.kg announcement do not provide a current licensed administrative-boundary layer.
- The 2018 WIS boundary layer is an archival GIS record in WGS 84, not proof of a current legal boundary. The AF NWRMP catalogue adds 2017 terrain/admin/seismic/geology images and 2022 basin maps, but no individual reuse terms; these dated images are historical references, not current source data.
- No item is VERIFIED. This audit does not certify rendered site behaviour, mobile layout or screen-reader output.

**Audit status:** chapter visual component remains incomplete. The nine production briefs and IDs are aligned one-to-one. Three assets (17-C, 17-E and 17-G) are integrated; six map/data-dependent assets remain placeholders and are not counted as coverage.


## Chapters 11–16 — first integrated visual tranche — 5 November 2026

**Scope:** one first-priority visual per chapter (11-A, 12-A, 13-A, 14-A, 15-A, 16-A). This is a partial integration checkpoint, not a full chapter visual audit.

| Visual ID | Presence | Scientific / factual | Rights / licence | RU–EN parity | Accessibility | Technical | Finding / next action |
|---|---|---|---|---|---|---|---|
| 11-A | INTEGRATED | PENDING | PENDING | PASS — bilingual labels and caption | PENDING — semantic alt text and rendered screen-reader behaviour not manually checked | PASS — static SVG structure check; live render pending | Original sector-structure schematic has no fabricated percentages and distinguishes employment from GVA. Assign project creator/rightsholder and licence; inspect rendering and label legibility. |
| 12-A | INTEGRATED | PENDING | PASS for the base and recorded CC BY 4.0 adaptation attribution | PASS — bilingual labels and caption | PENDING — semantic alt text and rendered behaviour not manually checked | PENDING — SVG uses a remote Wikimedia image dependency; live loading and responsive behaviour untested | Atlas Abierto 2026 relief/bathymetry base uses ETOPO 2022 and Natural Earth. Approximate numbered markers are orientation aids, not georeferenced boundaries. Confirm marker placement and the map's use as a relief base; river names are supplied in the side key, not digitised river lines. |
| 13-A | INTEGRATED | PENDING — specialist review of radiative-transfer depiction remains necessary | PENDING — original visual's project licence not assigned | PASS — bilingual labels and caption | PENDING | PASS — static SVG structure check; live render pending | Original qualitative diagram shows shortwave input and longwave absorption/re-emission. It must not imply that heat is fully trapped or that greenhouse gases reflect incoming sunlight. Confirm the added emissions-source note remains legible. |
| 14-A | INTEGRATED | PENDING | PENDING | PASS — bilingual labels and caption | PENDING | PASS — static SVG structure check; live render pending | Original vector/raster comparison correctly distinguishes geometries from a cell grid; it does not claim that one model is inherently more accurate. |
| 15-A | INTEGRATED | PENDING — verify band boundaries and sensor-specific exceptions during specialist review | PENDING | PASS — bilingual labels and caption | PENDING | PASS — static SVG structure check; live render pending | Original spectrum schematic labels approximate bands and the 8–14 μm atmospheric window; ranges are not universal sensor specifications. |
| 16-A | INTEGRATED | PENDING | PENDING | PASS — bilingual labels and caption | PENDING | PASS — static SVG structure check; live render pending | Original iterative research-cycle model contains a feedback loop; it is not presented as a mandatory universal protocol. |

### Static checks performed

All six SVG files were re-fetched from the working branch and passed the following source-level presence checks: viewBox, title, description, role="img", aria-labelledby, closing SVG element, and both Cyrillic and Latin text. This is not a rendered-browser test and does not certify XML parsing in every browser, visual legibility, contrast, meaningful screen-reader output or responsive behaviour.

### Coverage and remaining gaps

- Chapters 11–16: 12 of 57 registered visual IDs now have an integrated asset in this tranche; the remaining IDs are still production gaps and must not be counted as complete.
- Chapter 12-A uses an external image dependency inside its SVG; offline availability and remote loading must be tested before release.
- No asset in this tranche is marked VERIFIED. The five original SVGs require an explicit project rights/licence decision; all six require scientific/editorial review, and browser/accessibility QA remains outstanding.


## Chapters 18–20 — second integrated visual tranche — 5 November 2026

| Visual ID / figure | Presence | Scientific / factual | Rights / licence | RU–EN parity | Accessibility | Technical | Finding / next action |
|---|---|---|---|---|---|---|---|
| 18-A | MISSING | PENDING | Public-domain candidate identified but not used | N/A | N/A | N/A | The 2007 Commons topography map has unknown creation date and lacks a current DEM specification, vertical datum and accuracy statement. Do not substitute it for the required validated physical map. |
| 18-D | INTEGRATED | PENDING — check landform terminology and spatial relationships | PENDING — original SVG project licence not assigned | PASS | PENDING | PASS — source-level SVG structure; live render pending | Conceptual glacial-landform diagram added. Check arête spelling and the placement of moraine and outwash features in specialist review. |
| 18-H | INTEGRATED | PENDING — check valley morphology and alluvial-fan depiction | PENDING | PASS | PENDING | PASS — source-level SVG structure; live render pending | Conceptual river-valley cross-section added; explicitly not a site-specific Kyrgyz valley. |
| 18-J | INTEGRATED | PENDING | PENDING | PASS — bilingual SVG title, labels and description | PENDING | PASS — existing SVG; live render pending | Mountain-slope processes diagram retained; description now includes Russian and English. |
| 19-C | INTEGRATED | PENDING — elevation belts and vegetation/climate sequence vary regionally | PENDING | PASS | PENDING | PASS — source-level SVG structure; live render pending | Conceptual altitudinal profile added; no fixed elevation boundaries are asserted. |
| 19-H | INTEGRATED | PENDING — check wind directions and inversion conditions | PENDING | PASS — bilingual SVG labels and description | PENDING | PASS — existing SVG; live render pending | Mountain-valley circulation diagram retained; description now includes Russian and English. |
| 20-F | INTEGRATED | PENDING — verify dam failure and downstream-flow sequence | PENDING | PASS | PENDING | PASS — source-level SVG structure; live render pending | Conceptual GLOF pathway separates hazard, flow path and downstream exposure. It is not an operational risk map. |
| 20-H | INTEGRATED | PENDING — verify sign convention and closed-basin assumptions | PENDING | PASS | PENDING | PASS — source-level SVG structure; live render pending | Water-balance schematic shows P = ET + Q + ΔS and states that abstractions/transfers require additional terms. |
| 20-I | INTEGRATED | PENDING — check glacier anatomy and ELA/firn-line wording | PENDING | PASS — bilingual SVG labels and description | PENDING | PASS — existing SVG; live render pending | Glacier-anatomy diagram retained; description now includes Russian and English. |
| 20-J | INTEGRATED | PENDING — conceptual hydrogeology only | PENDING | PASS | PENDING | PASS — source-level SVG structure; live render pending | Groundwater cross-section added; explicitly not a geological section of a real valley. |
| 20-K | INTEGRATED | PASS — numerical values checked against the 2025 NSC table | PENDING — NSC data CC BY-NC-SA 4.0; original SVG project licence not assigned | PASS — bilingual labels and description | PENDING | PASS — source-level SVG; live render pending | Chart retains distinct indicators, units, source, year and licence note. Check share-alike compatibility before release. |
| 20.6.7 supporting figure | INTEGRATED | PASS with scope note — 2019 glacial lakes in Kyrgyz and Teskey ranges only | PASS — Frontiers CC BY 4.0 with author/article attribution | PASS — bilingual alt text and caption; labels within source figure remain English | PENDING | PENDING — remote image loading and responsive rendering untested | Reproduced Figure 1 from Daiyrov et al. (2022) as a supporting research map. It is not counted as a completed 20-C or 20-F asset. |

### Static checks performed

The new 18-D, 18-H, 19-C, 20-F, 20-H and 20-J SVG files were re-fetched and passed source-level checks for viewBox, title, description, role="img", aria-labelledby, closing SVG element, and Cyrillic and Latin text. The existing 18-J, 19-H, 20-I and 20-K files now have bilingual descriptions. This is not a browser-render or assistive-technology test.

### Coverage limits

- Chapter 18: 3 of 10 planned visuals integrated (18-D, 18-H, 18-J); 18-A remains blocked by authoritative DEM and geospatial provenance.
- Chapter 19: 2 of 10 planned visuals integrated (19-C, 19-H); maps and data plots still require validated climate datasets and station metadata.
- Chapter 20: 5 of 11 planned visuals integrated (20-F, 20-H, 20-I, 20-J, 20-K); the supporting 2019 research figure is additional and does not count toward those 11.
- None of the original project SVGs is marked VERIFIED. Scientific review, project licence assignment, accessibility review and browser testing remain open.


## Third visual integration tranche — Chapters 11–16 and 18–19 — 5 November 2026

| Visual ID | Presence | Scientific / factual | Rights / licence | RU–EN parity | Accessibility | Technical | Finding / next action |
|---|---|---|---|---|---|---|---|
| 11-B | INTEGRATED | PENDING — review factor grouping and examples | PENDING — original SVG project licence not assigned | PASS | PENDING | PASS — source-level SVG structure; live render pending | Location factors shown as interacting inputs; no universal factor weights asserted. |
| 13-C | INTEGRATED | PENDING — risk framework terminology requires subject review | PENDING | PASS | PENDING | PASS — source-level SVG structure; live render pending | Hazard, exposure and vulnerability are distinct; caption says conceptual model, not a universal equation. |
| 14-B | INTEGRATED | PENDING — check h/H/N relationship and CRS terminology | PENDING | PASS | PENDING | PASS — source-level SVG structure; live render pending | Separates Earth model, geographic CRS, projection and vertical reference. Verify formula H = h − N against the chapter's chosen sign convention. |
| 15-B | INTEGRATED | PENDING — check sensor examples and all-weather caveat | PENDING | PASS | PENDING | PASS — source-level SVG structure; live render pending | Passive optical/thermal and active SAR/LiDAR principles shown. Radar caveat is qualified by wavelength and conditions. |
| 16-B | INTEGRATED | PENDING | PENDING | PASS | PENDING | PASS — source-level SVG structure; live render pending | Four spatial-analysis levels are shown; caption distinguishes them from map scale. |
| 18-B | INTEGRATED | PENDING — orographic regionalisation must be checked against the selected classification | PENDING | PASS | PENDING | PASS — source-level SVG structure; live render pending | Schematic regional classification only; not a georeferenced map or tectonic-terrane map. |
| 19-D | INTEGRATED | PENDING — climate attribution and hazard categories require expert review | PENDING | PASS | PENDING | PASS — source-level SVG structure; live render pending | Presents hazard families without inventing frequency, regional rankings or forecast values. |

### Updated scoped visual coverage — Chapters 11–20

| Chapter | Registered IDs | Integrated | Missing |
|---|---:|---:|---:|
| 11 | 7 | 3 | 4 |
| 12 | 10 | 2 | 8 |
| 13 | 11 | 2 | 9 |
| 14 | 9 | 2 | 7 |
| 15 | 11 | 2 | 9 |
| 16 | 9 | 2 | 7 |
| 17 | 9 | 3 | 6 |
| 18 | 10 | 4 | 6 |
| 19 | 10 | 3 | 7 |
| 20 | 11 | 5 | 6 |
| **Total** | **97** | **28** | **69** |

All seven new SVGs were re-fetched from the working branch and passed source-level checks for viewBox, title, description, role="img", aria-labelledby, closing SVG element, and Cyrillic and Latin text. This is not a browser-render or assistive-technology test. Their project licence, scientific review, accessibility and live rendering remain pending.


### Chapter 12-B — Asia macro-regions map

| Presence | Scientific / factual | Rights / licence | RU–EN parity | Accessibility | Technical | Finding / next action |
|---|---|---|---|---|---|---|
| INTEGRATED | PENDING — confirm that the map's regional groupings are not confused with UN M49; this distinction is stated in the chapter and caption | PASS for source attribution and CC BY 4.0 adaptation record | PASS — bilingual side key and caption; source map labels remain English | PENDING — screen-reader output and label legibility not tested | PENDING — SVG embeds a remote MDPI image; live loading and responsive rendering untested | Adapted from Dou et al. (2018), Figure 1. The source map's region boundaries follow the study's regionalisation and RESDC data, not an official UN M49 map. Do not remove the scope caveat. |


### Chapter 11-C — multimodal transport chain

| Presence | Scientific / factual | Rights / licence | RU–EN parity | Accessibility | Technical | Finding / next action |
|---|---|---|---|---|---|---|
| INTEGRATED | PENDING — review multimodal sequence and examples | PENDING — original SVG project licence not assigned | PASS | PENDING | PASS — source-level SVG structure; live render pending | Schematic chain includes producer, consolidation, rail, port, ship, warehouse and market, with road and air alternatives. It contains no invented route distances or travel times. |


### Chapter 11-C — technical source check

The SVG was re-fetched from the working branch and passed source-level checks for viewBox, title, description, role="img", aria-labelledby, closing SVG element, and Cyrillic and Latin text. Live browser rendering, legibility and assistive-technology output remain untested.


## Fourth visual integration tranche — Chapters 11–16 — 5 November 2026

| Visual ID | Presence | Scientific / factual | Rights / licence | RU–EN parity | Accessibility | Technical | Finding / next action |
|---|---|---|---|---|---|---|---|
| 11-E | INTEGRATED | PENDING — review regional agricultural examples if any are later added | PENDING — original SVG project licence not assigned | PASS | PENDING | PASS — source-level SVG structure; live render pending | Conceptual landscape profile links climate, soils, relief and water with agricultural land use; no local crop suitability or site-specific recommendation is implied. |
| 12-D | INTEGRATED | PASS for checklist logic; PENDING for any future statistical application | PENDING — original SVG project licence not assigned | PASS | PENDING | PASS — source-level SVG structure; live render pending | Six checks: boundary/territory, date/period, classification, units/denominator, source/method, comparability/uncertainty. |
| 13-D | INTEGRATED | PENDING — confirm national legal terminology when country-specific legislation is discussed | PENDING — original SVG project licence not assigned | PASS | PENDING | PASS — source-level SVG structure; live render pending | Distinguishes project-level EIA, strategic SEA and repeated environmental monitoring; notes that monitoring does not replace assessment and procedures vary by jurisdiction. |
| 14-C | INTEGRATED | PASS for set-logic definitions; PENDING for live software-specific output comparison | PENDING — original SVG project licence not assigned | PASS | PENDING | PASS — source-level SVG structure; live render pending | Illustrates intersection, union, difference and symmetric difference; QGIS bibliography now links to the official spatial-analysis guide. |
| 15-C | INTEGRATED | PASS for formulas and Landsat/Sentinel-2 band mappings; local thresholds and product-specific processing remain PENDING | PENDING — original SVG project licence not assigned | PASS | PENDING | PASS — source-level SVG structure; live render pending | Shows NDVI, NDMI, McFeeters NDWI, NDBI and NBR. Explicitly distinguishes McFeeters Green–NIR NDWI from Gao NIR–SWIR NDWI; states Landsat 8–9 and Sentinel-2 bands and warns against universal thresholds. |
| 16-C | INTEGRATED | PASS for conceptual sampling definitions; actual sample design and sample-size calculations remain PENDING | PENDING — original SVG project licence not assigned | PASS | PENDING | PASS — source-level SVG structure; live render pending | Compares simple random, systematic, stratified and cluster designs; includes random-start and within-cluster caveats. |

### Static checks — fourth tranche

All six new SVG files were re-fetched from the working branch and passed source-level checks for viewBox, title, description, role="img", aria-labelledby, closing SVG element, and Cyrillic and Latin text. The six chapter files were re-fetched and the relevant placeholders were replaced by local Markdown image embeds with bilingual alt text and captions. This is not browser-render, mobile, keyboard, screen-reader or specialist scientific approval.

### Superseding scoped visual coverage — Chapters 11–20 — 5 November 2026

| Chapter | Registered IDs | Integrated | Missing |
|---|---:|---:|---:|
| 11 | 7 | 4 | 3 |
| 12 | 10 | 3 | 7 |
| 13 | 11 | 3 | 8 |
| 14 | 9 | 3 | 6 |
| 15 | 11 | 3 | 8 |
| 16 | 9 | 3 | 6 |
| 17 | 9 | 3 | 6 |
| 18 | 10 | 4 | 6 |
| 19 | 10 | 3 | 7 |
| 20 | 11 | 5 | 6 |
| **Total, Chapters 11–20** | **97** | **34** | **63** |

The earlier 28/97 table is a historical snapshot and is superseded by this 34/97 table. The supplementary 2019 glacial-lake research figure in Chapter 20.6.7 remains additional and is not counted as a planned ID. Original SVG creator/rightsholder and project redistribution licence remain pending for this tranche; none is marked VERIFIED.

## Fifth visual integration tranche — Chapters 11 and 13–16 — 5 November 2026

| Visual ID | Presence | Scientific / factual | Rights / licence | RU–EN parity | Accessibility | Technical | Finding / next action |
|---|---|---|---|---|---|---|---|
| 11-D | INTEGRATED | PASS as a generic value-chain model; no specific product or country is asserted | PENDING — original SVG project licence not assigned | PASS | PENDING | PASS — source-level SVG structure; live render pending | Stages run from research/design through inputs, production, assembly, logistics and market, with service/reuse feedback and supporting conditions. UNCTAD and UNIDO sources added. |
| 13-B | INTEGRATED | PASS for the three biodiversity levels and five direct drivers in the IPBES framework | PENDING — original SVG project licence not assigned | PASS | PENDING | PASS — source-level SVG structure; live render pending | Distinguishes genetic, species and ecosystem diversity; five direct drivers are separated from indirect social/economic causes. |
| 14-E | INTEGRATED | PASS for five-component GIS concept and workflow; operational details vary by system | PENDING — original SVG project licence not assigned | PASS | PENDING | PASS — source-level SVG structure; live render pending | GIS includes people, data, software, hardware and methods; feedback loop shows iterative workflow. QGIS reference added. |
| 15-E | INTEGRATED | PASS as a passive optical sensing concept; thermal and active radar modes are explicitly distinguished | PENDING — original SVG project licence not assigned | PASS | PENDING | PASS — source-level SVG structure; live render pending | Shows solar path through atmosphere, surface interaction, reflected energy, satellite sensor and processing; caption warns that SAR is active. NASA ARSET reference added. |
| 16-D | INTEGRATED | PASS as a conceptual generalisation example; no real geodata is implied | PENDING — original SVG project licence not assigned | PASS | PENDING | PASS — source-level SVG structure; live render pending | Shows selection and simplification from large to small scales; OS generalisation guidance added. |

### Static checks — fifth tranche

All five new SVG files were re-fetched from the working branch and passed source-level checks for viewBox, title, description, role="img", aria-labelledby, closing SVG element, and Cyrillic and Latin text. Their chapter embeds and matching relative asset paths were checked. This is not live browser rendering, responsive/mobile, keyboard or screen-reader QA.

### Superseding scoped visual coverage — Chapters 11–20 — 5 November 2026

| Chapter | Registered IDs | Integrated | Missing |
|---|---:|---:|---:|
| 11 | 7 | 5 | 2 |
| 12 | 10 | 3 | 7 |
| 13 | 11 | 4 | 7 |
| 14 | 9 | 4 | 5 |
| 15 | 11 | 4 | 7 |
| 16 | 9 | 4 | 5 |
| 17 | 9 | 3 | 6 |
| 18 | 10 | 4 | 6 |
| 19 | 10 | 3 | 7 |
| 20 | 11 | 5 | 6 |
| **Total** | **97** | **39** | **58** |

This 39/97 table supersedes earlier 28/97 and 34/97 snapshots. The supplementary 2019 glacial-lake research figure in Chapter 20.6.7 remains additional and is not counted as a planned ID. Original SVG creator/rightsholder and project redistribution licence remain pending; none is marked VERIFIED.


### Corrective cleanup — 5 November 2026

- Chapter 14 visual 14-C was refined after source inspection: the intersection, A-minus-B and symmetric-difference panels now use clipping/masking rather than approximate overlap shapes. This improves the mathematical set-logic depiction. Static SVG source structure remains valid; visual rendering still requires browser inspection.
- Removed obsolete placeholder labels for already integrated visuals 18-J, 19-H, 20-I and 20-K. Their image embeds and captions remain in place. This prevents a completed embed from appearing simultaneously as an unresolved placeholder.


## Sixth visual integration tranche — Chapter 20 — 5 November 2026

| Visual ID | Presence | Scientific / factual | Rights / licence | RU–EN parity | Accessibility | Technical | Finding / next action |
|---|---|---|---|---|---|---|---|
| 20-C | INTEGRATED — partial scope stated | PASS for the displayed surface-area comparison; full morphometry remains PENDING | PENDING — original SVG project licence not assigned; data attribution recorded in Chapter 20 | PASS | PENDING | PASS — source-level SVG structure; live render pending | Compares Issyk-Kul (6,236 km²), Son-Kul (278 km²), Chatyr-Kul (175 km²) and Sary-Chelek (~4.9 km²). It is explicitly an area comparison, not a map. Depth and origin are omitted because sources and measurement dates require reconciliation. |
| 20-D | INTEGRATED | PASS for the five-plant sequence and reported 2,870 MW total in the cited AF NWRMP source; individual plant capacities are not inferred | PENDING — original SVG project licence not assigned | PASS | PENDING | PASS — source-level SVG structure; live render pending | Schematic Lower Naryn cascade sequence: Toktogul, Kurpsai, Tash-Kumyr, Shamaldy-Sai and Uch-Kurgan. Kambar-Ata projects are shown separately and excluded from the operating total. Not to scale. |

### Static checks — sixth tranche

Both new SVGs were re-fetched from the working branch and passed source-level checks for viewBox, title, description, role="img", aria-labelledby, closing SVG element and Cyrillic/Latin text. Both chapter embeds resolve to existing files. This is not browser-render, responsive/mobile or assistive-technology QA.

### Superseding scoped visual coverage — Chapters 11–20 — 5 November 2026

| Chapter | Registered IDs | Integrated | Missing |
|---|---:|---:|---:|
| 11 | 7 | 5 | 2 |
| 12 | 10 | 3 | 7 |
| 13 | 11 | 4 | 7 |
| 14 | 9 | 4 | 5 |
| 15 | 11 | 4 | 7 |
| 16 | 9 | 4 | 5 |
| 17 | 9 | 3 | 6 |
| 18 | 10 | 4 | 6 |
| 19 | 10 | 3 | 7 |
| 20 | 11 | 7 | 4 |
| **Total** | **97** | **41** | **56** |

This 41/97 table supersedes earlier 39/97, 34/97 and 28/97 snapshots. The supplementary 2019 glacial-lake research figure in Chapter 20.6.7 remains additional and is not counted as a planned ID. Project licensing, specialist approval and rendered accessibility checks remain outstanding for original SVGs.


### Chapter 20-E — transboundary water management

| Presence | Scientific / factual | Rights / licence | RU–EN parity | Accessibility | Technical | Finding / next action |
|---|---|---|---|---|---|---|
| INTEGRATED | PASS as a conceptual comparison; it is explicitly not a basin map or quantitative allocation diagram | PENDING — original SVG project licence not assigned | PASS | PENDING | PASS — source-level SVG structure; live render pending | Separates Chu–Talas cooperation (Kyrgyzstan–Kazakhstan and the interstate commission) from Naryn–Syr Darya reservoir, hydropower and downstream irrigation coordination. Uses existing UNECE, CAWater-Info and AF NWRMP chapter sources. |

Static SVG structure and chapter embed were checked. The schematic does not replace a georeferenced basin map, treaty/allocation table or seasonal flow dataset.

### Superseding Chapter 11–20 count — 5 November 2026

Chapter 20 now has 8/11 planned IDs integrated (20-C, 20-D, 20-E, 20-F, 20-H, 20-I, 20-J, 20-K); three remain open (20-A, 20-B and 20-G). Total scoped integration is 42/97; 55 remain missing. The 41/97 table above is superseded.


## Current scoped visual count — Chapters 11–20 — 5 November 2026

| Chapter | Registered IDs | Integrated | Missing |
|---|---:|---:|---:|
| 11 | 7 | 5 | 2 |
| 12 | 10 | 3 | 7 |
| 13 | 11 | 4 | 7 |
| 14 | 9 | 4 | 5 |
| 15 | 11 | 4 | 7 |
| 16 | 9 | 4 | 5 |
| 17 | 9 | 3 | 6 |
| 18 | 10 | 4 | 6 |
| 19 | 10 | 3 | 7 |
| 20 | 11 | 8 | 3 |
| **Total** | **97** | **42** | **55** |

This table supersedes all earlier scoped counts in this audit. Chapter 20's supplementary 2019 CC BY 4.0 glacial-lake map is additional and not counted in the 20-A–20-K inventory. The count records integration only, not full verification.


## Eighth visual integration tranche — Chapters 11 and 19 — 5 November 2026

| Visual ID | Presence | Scientific / factual | Rights / licence | RU–EN parity | Accessibility | Technical | Finding / next action |
|---|---|---|---|---|---|---|---|
| 11-F | INTEGRATED | PASS for 2025 figures against Ministry of Energy / CAWater-Info sources; values are rounded and not presented as a full balance | PENDING — original SVG project licence not assigned | PASS | PENDING | PASS — source-level SVG structure; live render pending | Separates primary resources, generation, transmission, distribution, consumption, storage and cross-border trade. 2025 Kyrgyzstan panel reports generation 15.4 bn kWh, consumption 19.3 bn kWh and imports about 3.8 bn kWh; generation components are listed separately. It does not imply a complete balance or mix planned capacity with operating output. |
| 19-J | INTEGRATED | PASS as a sectoral impact/adaptation overview grounded in the 2025 BTR1 and UNDP examples; not a forecast or local plan | PENDING — original SVG project licence not assigned | PASS | PENDING | PASS — source-level SVG structure; live render pending | Covers water, agriculture, energy, transport, health, ecosystems and cities; caption requires local risk assessment before applying measures. |

Both new SVGs were re-fetched and passed static structure and RU/EN checks; both chapter embeds resolve. Live browser, responsive, keyboard and screen-reader checks remain pending.

### Superseding scoped coverage — Chapters 11–20 — 5 November 2026

| Chapter | Registered IDs | Integrated | Missing |
|---|---:|---:|---:|
| 11 | 7 | 6 | 1 |
| 12 | 10 | 3 | 7 |
| 13 | 11 | 4 | 7 |
| 14 | 9 | 4 | 5 |
| 15 | 11 | 4 | 7 |
| 16 | 9 | 4 | 5 |
| 17 | 9 | 3 | 6 |
| 18 | 10 | 4 | 6 |
| 19 | 10 | 4 | 6 |
| 20 | 11 | 8 | 3 |
| **Total** | **97** | **44** | **53** |

This 44/97 table supersedes the previous 42/97 count. Original SVG licensing and final scientific/editorial approval remain outstanding.


### Chapter 11-G — tourism destination system

| Presence | Scientific / factual | Rights / licence | RU–EN parity | Accessibility | Technical | Finding / next action |
|---|---|---|---|---|---|---|
| INTEGRATED | PASS as a conceptual destination-system model; no site-specific carrying capacity or visitor statistics are asserted | PENDING — original SVG project licence not assigned | PASS | PENDING | PASS — source-level SVG structure; live render pending | Connects natural/cultural assets, infrastructure, service providers, visitors, host communities, management/monitoring and environmental/social limits. UNESCO and UN Tourism references added. |

The diagram is a conceptual system, not an assessment of a named tourism destination. The 11-G embed and SVG structure passed static checks.

### Superseding scoped coverage — Chapters 11–20 — 5 November 2026

| Chapter | Registered IDs | Integrated | Missing |
|---|---:|---:|---:|
| 11 | 7 | 7 | 0 |
| 12 | 10 | 3 | 7 |
| 13 | 11 | 4 | 7 |
| 14 | 9 | 4 | 5 |
| 15 | 11 | 4 | 7 |
| 16 | 9 | 4 | 5 |
| 17 | 9 | 3 | 6 |
| 18 | 10 | 4 | 6 |
| 19 | 10 | 4 | 6 |
| 20 | 11 | 8 | 3 |
| **Total** | **97** | **45** | **52** |

This 45/97 table supersedes the previous 44/97 count. Chapter 11's seven planned visuals are all now integrated, but scientific, rights, accessibility and browser verification remain outstanding.


### Chapter 19-F — seasonal atmospheric circulation

| Presence | Scientific / factual | Rights / licence | RU–EN parity | Accessibility | Technical | Finding / next action |
|---|---|---|---|---|---|---|
| INTEGRATED | PASS as a simplified regional model grounded in peer-reviewed Central Asian circulation studies; it does not claim a single uniform seasonal pattern for all Kyrgyzstan | PENDING — original SVG project licence not assigned | PASS | PENDING | PASS — source-level SVG structure; live render pending | Contrasts cold-season westerlies/mid-latitude disturbances with warm-season continental heating, anticyclonic conditions and northerly intrusions; caveat states that flow varies by month, elevation and locality. |

The asset and chapter embed passed static SVG checks. This is not a daily forecast or a georeferenced circulation map.

### Current scoped visual coverage — Chapters 11–20 — 5 November 2026

| Chapter | Registered IDs | Integrated | Missing |
|---|---:|---:|---:|
| 11 | 7 | 7 | 0 |
| 12 | 10 | 3 | 7 |
| 13 | 11 | 4 | 7 |
| 14 | 9 | 4 | 5 |
| 15 | 11 | 4 | 7 |
| 16 | 9 | 4 | 5 |
| 17 | 9 | 3 | 6 |
| 18 | 10 | 4 | 6 |
| 19 | 10 | 5 | 5 |
| 20 | 11 | 8 | 3 |
| **Total** | **97** | **46** | **51** |

This 46/97 table supersedes the previous 45/97 count.


## Eleventh visual integration tranche — Chapter 13 — 5 November 2026

| Visual ID | Presence | Scientific / factual | Rights / licence | RU–EN parity | Accessibility | Technical | Finding / next action |
|---|---|---|---|---|---|---|---|
| 13-E | INTEGRATED | PASS against the six elements in the official IPBES conceptual framework | PENDING — original SVG project licence not assigned | PASS | PENDING | PASS — source-level SVG structure; live render pending | Shows nature, nature's contributions to people, anthropogenic assets, institutions/indirect drivers, direct drivers and quality of life. It is a simplified analytical framework, not a linear causal chain. |
| 13-F | INTEGRATED | PASS as a qualitative IPCC-based teaching matrix; it does not claim local quantitative evidence or a forecast | PENDING — original SVG project licence not assigned | PASS | PENDING | PASS — source-level SVG structure; live render pending | Separates observed impacts from potential future risks across cryosphere, water, ecosystems, agriculture, cities/infrastructure and health. Regional confidence and local applicability require separate evidence. |
| 13-H | INTEGRATED | PASS for mitigation/adaptation distinction; adaptation metrics are explicitly context-dependent | PENDING — original SVG project licence not assigned | PASS | PENDING | PASS — source-level SVG structure; live render pending | Compares goals, examples, time horizons and indicative metrics. It does not imply one universal adaptation indicator set. |

All three SVGs were re-fetched and passed static source checks and their chapter embeds resolve. Live browser, accessibility and project-licence checks remain open.

### Current scoped visual coverage — Chapters 11–20 — 5 November 2026

| Chapter | Registered IDs | Integrated | Missing |
|---|---:|---:|---:|
| 11 | 7 | 7 | 0 |
| 12 | 10 | 3 | 7 |
| 13 | 11 | 7 | 4 |
| 14 | 9 | 4 | 5 |
| 15 | 11 | 4 | 7 |
| 16 | 9 | 4 | 5 |
| 17 | 9 | 3 | 6 |
| 18 | 10 | 4 | 6 |
| 19 | 10 | 5 | 5 |
| 20 | 11 | 8 | 3 |
| **Total** | **97** | **49** | **48** |

This 49/97 table supersedes the previous 46/97 count.


## Twelfth visual integration tranche — Chapter 14 — 5 November 2026

| Visual ID | Presence | Scientific / factual | Rights / licence | RU–EN parity | Accessibility | Technical | Finding / next action |
|---|---|---|---|---|---|---|---|
| 14-F | INTEGRATED | PASS for the distinction between Euclidean buffer and network service area | PENDING — original SVG project licence not assigned | PASS | PENDING | PASS — source-level SVG structure; live render pending | Shows straight-line radius versus reachable road-network segments and a barrier; QGIS 3.44 service-area documentation added. |
| 14-H | INTEGRATED | PASS for common gap, overlap, undershoot, overshoot and duplicate examples; context caveat included | PENDING — original SVG project licence not assigned | PASS | PENDING | PASS — source-level SVG structure; live render pending | Shows typical vector topology issues; rules must follow the data model. QGIS topology and GDAL geometry-validity sources added. |
| 14-I | INTEGRATED | PASS as a reproducible project workflow | PENDING — original SVG project licence not assigned | PASS | PENDING | PASS — source-level SVG structure; live render pending | Captures question, data provenance/licence, CRS/software versions, processing scripts/parameters, validation, metadata and publication. |

All three SVGs passed static source and chapter-embed checks. Live browser, keyboard/screen-reader, project licensing and software-specific execution QA remain open.

### Current scoped visual coverage — Chapters 11–20 — 5 November 2026

| Chapter | Registered IDs | Integrated | Missing |
|---|---:|---:|---:|
| 11 | 7 | 7 | 0 |
| 12 | 10 | 3 | 7 |
| 13 | 11 | 7 | 4 |
| 14 | 9 | 7 | 2 |
| 15 | 11 | 4 | 7 |
| 16 | 9 | 4 | 5 |
| 17 | 9 | 3 | 6 |
| 18 | 10 | 4 | 6 |
| 19 | 10 | 5 | 5 |
| 20 | 11 | 8 | 3 |
| **Total** | **97** | **52** | **45** |

This 52/97 table supersedes the previous 49/97 count.


## Thirteenth visual integration tranche — Chapter 15 — 5 November 2026

| Visual ID | Presence | Scientific / factual | Rights / licence | RU–EN parity | Accessibility | Technical | Finding / next action |
|---|---|---|---|---|---|---|---|
| 15-F | INTEGRATED | PASS as a qualitative teaching illustration; not measured reflectance data | PENDING — original SVG project licence not assigned | PASS | PENDING | PASS — source-level SVG structure; live render pending | Compares vegetation, clear water, dry soil and snow spectral signatures; explicitly notes dependence on moisture, composition, season and atmosphere. |
| 15-G | INTEGRATED | PASS for the four resolution concepts | PENDING — original SVG project licence not assigned | PASS | PENDING | PASS — source-level SVG structure; live render pending | Explains spatial, spectral, radiometric and temporal resolution and warns that they are distinct properties. |
| 15-H | INTEGRATED | PASS for the Landsat processing sequence and Level-2 caveat | PENDING — original SVG project licence not assigned | PASS | PENDING | PASS — source-level SVG structure; live render pending | Shows processing toward surface reflectance and QA masks; notes that Level-2 products already include algorithmic correction and product-specific scale/QA details. |

All three assets passed static SVG and chapter-embed checks. They are not live-browser, mobile or assistive-technology verified.

### Current scoped visual coverage — Chapters 11–20 — 5 November 2026

| Chapter | Registered IDs | Integrated | Missing |
|---|---:|---:|---:|
| 11 | 7 | 7 | 0 |
| 12 | 10 | 3 | 7 |
| 13 | 11 | 7 | 4 |
| 14 | 9 | 7 | 2 |
| 15 | 11 | 7 | 4 |
| 16 | 9 | 4 | 5 |
| 17 | 9 | 3 | 6 |
| 18 | 10 | 4 | 6 |
| 19 | 10 | 5 | 5 |
| 20 | 11 | 8 | 3 |
| **Total** | **97** | **55** | **42** |

This 55/97 table supersedes the previous 52/97 count.


## Chapter 16 — final five cartography visuals — 5 November 2026

| Visual ID | Presence | Scientific / factual | Rights / licence | RU–EN parity | Accessibility | Technical | Finding / next action |
|---|---|---|---|---|---|---|---|
| 16-E | INTEGRATED | PASS — map type/data matching aligned with UCGIS CV-04-011 | PENDING — original project licence not assigned | PASS — bilingual title, description and caption | PENDING — alt text present; manual comprehension/contrast review pending | PASS — static SVG structure and relative embed; live render pending | Five conceptual examples; fictional territory and data. |
| 16-F | INTEGRATED | PASS — visual variables aligned with Penn State GEOG 486 and Roth (2017) | PENDING | PASS | PENDING | PASS — static SVG and embed | Position, size, shape, orientation, hue, lightness and texture; colour is not the only channel. |
| 16-G | INTEGRATED | PASS with limitation — equal interval and quantile examples are explicit; natural-break ranges are illustrative, not computed Jenks results | PENDING | PASS | PENDING | PASS — static SVG and embed | Add/retain explicit warning that exact Jenks breaks must be calculated from source data. |
| 16-H | INTEGRATED | PASS — mock-up distinguishes applicable metadata from non-applicable scale/CRS | PENDING | PASS | PENDING | PASS — static SVG and embed | Fictional map-layout example; no geospatial precision is implied. |
| 16-I | INTEGRATED | PASS — includes source lineage, metadata, code, environment, processing, outputs, rights and access control | PENDING | PASS | PENDING | PASS — static SVG and embed | Conceptual workflow, not a prescribed software stack. |

The five new assets were fetched from the working branch and passed source-level checks for SVG opening/closing elements, viewBox, title, description, role="img", and Russian/English text. Their chapter embeds resolve to local files and their Markdown captions are bilingual. No browser rendering, responsive layout, keyboard navigation or screen-reader test is claimed. No visual is VERIFIED.

**Chapter 16 coverage:** 9/9 planned IDs are integrated (16-A–16-I). This is Image Coverage only; Image Verification remains 0/9 under the full policy because rights, accessibility and rendered technical QA are still pending.


## Chapter 19 — Visual 19-E — 5 November 2026

| Visual ID | Presence | Scientific / factual | Rights / licence | RU–EN parity | Accessibility | Technical | Finding / next action |
|---|---|---|---|---|---|---|---|
| 19-E | INTEGRATED | PASS WITH SOURCE CAVEAT — bar values reproduce Kyrgyzhydromet's published table (annual 0.28; winter 0.21; spring 0.59; summer/autumn 0.15 °C per decade). The source has a period inconsistency: table heading 1981–2020, narrative 1981–2021. The chart labels this explicitly. | PENDING — original SVG project licence not assigned; source data attribution included | PASS — bilingual chart title, labels, description and caption | PENDING — descriptive alt text present; manual contrast/comprehension review pending | PASS — static SVG structure and relative chapter embed; live browser/mobile rendering pending | Do not use as an annual anomaly time series. Resolve the source's period discrepancy before cross-study comparison. |

Static source checks confirm SVG boundary, viewBox, title, description, role=img, bilingual text and local chapter path. No browser or assistive-technology test is claimed. No visual is VERIFIED.


## Chapter 18 — Visual 18-C — 5 November 2026

| Visual ID | Presence | Scientific / factual | Rights / licence | RU–EN parity | Accessibility | Technical | Finding / next action |
|---|---|---|---|---|---|---|---|
| 18-C | INTEGRATED — three photographs | PASS WITH SCOPE NOTE — photographs identify the named mountains/landscape, but are not used to infer elevations | PASS — exact file pages confirm CC BY-SA 4.0 (Maryliflower), CC BY 2.0 (Chen Zhao) and CC0 1.0 (Benoît Vicart); attribution/links included | PASS — bilingual alt text and credit captions | PENDING — alt text present; visual contrast and assistive-tech review pending | PENDING — external Wikimedia thumbnail loading and responsive display not tested in deployed reader | Three separate images, not a stitched panorama. Height labels are supported by separate official sources. |

The images were visually inspected from their Commons file pages. The source files are unchanged. Browser/mobile and screen-reader checks remain open; therefore 18-C is INTEGRATED, not VERIFIED.


## Chapter 17 — Visual 17-F — source discovery checkpoint — 5 November 2026

| Visual ID | Presence | Scientific / factual | Rights / licence | RU–EN parity | Accessibility | Technical | Finding / next action |
|---|---|---|---|---|---|---|---|
| 17-F | MISSING — no map generated or embedded | PENDING — candidate catalogue and fault data found; national clipping boundary, period, magnitude threshold and completeness must be checked | PASS for candidate source terms — World Bank earthquake catalogue and active-fault dataset pages state CC BY 4.0; derived map attribution still to be authored | PENDING | PENDING | PENDING | Candidate sources: HECCA earthquake catalogue and Central Asia Seismic Fault Database, both covering five countries plus 300 km buffer. Do not present selected faults as a complete national inventory. Next: inspect data package metadata and verify the country boundary and chosen event filter before map production. |

The 2024 NHESS paper is open access under CC BY 4.0 and documents the harmonisation methods, data limitations and selected fault compilation. It does not remove the need to check the actual dataset fields, CRS, catalogue completeness and Kyrgyzstan clipping boundary. Visual 17-F remains MISSING until a map is generated and integrated.


### Chapter 17 — supplementary Figure 1 from Poggi et al. (2024)

| Figure | Presence | Scientific / factual | Rights / licence | RU–EN parity | Accessibility | Technical | Finding / next action |
|---|---|---|---|---|---|---|---|
| Regional seismicity context | INTEGRATED — remote research figure | PASS WITH SCOPE NOTE — five-country Central Asia region plus 300 km buffer; source-catalogue colours, not magnitude; input-source distribution, not final HECCA | PASS — article page states CC BY 4.0; author/article/DOI credit included | PASS — bilingual alt text and caption | PENDING — alt text present; manual assistive review pending | PENDING — external image loading and responsive behaviour untested | Supplementary context only; not a substitute for Kyrgyzstan-specific 17-F active-fault/seismicity map and not counted in planned visual coverage. |


## Chapter 20 — Visual 20-G — source discovery checkpoint — 5 November 2026

| Visual ID | Presence | Scientific / factual | Rights / licence | RU–EN parity | Accessibility | Technical | Finding / next action |
|---|---|---|---|---|---|---|---|
| 20-G | MISSING — no chart integrated | PARTIAL SOURCE METADATA — Naryn station 16055, 41.430° N / 76.000° E, drainage area 10,500 km², long-term mean 92.117 m³/s, published graph period 1931–2006 | PENDING — raw data reuse terms not established | PENDING | PENDING | PENDING | UNH page displays annual/monthly graph but raw reusable values and item-specific licence are not yet confirmed. Do not digitise the displayed raster graph as exact data. Obtain raw data and document QC, time step and gaps before creating the chart. |


## Chapters 14 and 15 — final conceptual visuals tranche — 5 November 2026

| Visual ID | Presence | Scientific / factual | Rights / licence | RU–EN parity | Accessibility | Technical | Finding / next action |
|---|---|---|---|---|---|---|---|
| 14-D | INTEGRATED | PASS — sequential/diverging/qualitative palettes matched to ordered, centred and categorical data | PENDING — original project licence not assigned | PASS | PENDING — labels present; contrast/colour-vision review pending | PASS — static SVG and local embed; browser/mobile render pending | Palette examples are illustrative; no universal colour standard is implied. |
| 15-D | INTEGRATED | PASS WITH LIMITATION — independent validation is separated from training; confusion matrix is conceptual, no accuracy values invented | PENDING | PASS | PENDING | PASS — static SVG and local embed; browser render pending | Add real accuracy statistics only when a documented reference sample and sampling design exist. |
| 15-I | INTEGRATED | PASS — side-looking geometry and incidence angle to local surface normal shown; not an optical camera | PENDING | PASS | PENDING | PASS — static SVG and local embed; browser render pending | Simplified geometry; actual incidence and distortions depend on orbit and terrain. |
| 15-J | INTEGRATED | PASS — multiple returns, ground/canopy distinction, DSM, DTM and CHM=DSM−DTM shown | PENDING | PASS | PENDING | PASS — static SVG and local embed; browser render pending | Explicitly notes that not every pulse reaches ground; not site-specific LiDAR data. |
| 15-K | INTEGRATED | PASS — co-registration, seasonal matching, analysis and independent validation shown | PENDING | PASS | PENDING | PASS — static SVG and local embed; browser render pending | Explicitly warns about clouds, shadows, seasonality and sensor differences. |

The five SVG files were fetched and passed source-level structure and bilingual-text checks. Their relative embed paths exist in the relevant chapter files. No browser, responsive, keyboard or assistive-technology test is claimed. None is marked VERIFIED.


## Cross-chapter Markdown asset-path audit — Chapters 11–20 — 5 November 2026

A fresh fetch of all ten chapter files found 80 Markdown image embeds:
- 73 local relative-path embeds; the earlier 64/64 local path audit passed, and the nine subsequently added local SVGs (13-G/I/J/K, 14-D, 15-D/I/J/K) were each fetched and passed source-level checks (73/73 local paths resolve).
- 7 external image embeds: NASA/JPL North America relief (Chapter 12), regional seismicity context (Chapter 17), Blue Green Atlas Kyrgyzstan relief (Chapter 18), three licensed Wikimedia peak photographs (Chapter 18), and the CC BY 4.0 glacial-lake research figure (Chapter 20).
- No Markdown image embed has an empty alt attribute (0/80).
- Six alt strings appear in one language only because the same local bilingual asset is embedded separately in the Russian and English sections of Chapter 17; each language version has a matching-language alt string. These are not six missing translations.
- The seven external images were located at their cited source pages; this does not substitute for deployed-site image-load, responsive-layout or accessibility testing.

This is a repository path/source check, not a browser test. Image Verification remains separate from Image Coverage.


## Chapter 14 — Visual 14-G — source discovery checkpoint — 5 November 2026

| Visual ID | Presence | Scientific / factual | Rights / licence | RU–EN parity | Accessibility | Technical | Finding / next action |
|---|---|---|---|---|---|---|---|
| 14-G | MISSING — no raster or derivative maps integrated | PENDING — NASA SRTM GL1 v003 (~30 m, 2000) and Copernicus GLO-30 (30 m DSM, 2011–2015) identified as candidates; no exact Kyrgyzstan tile or derived raster validated | Candidate terms identified; exact tile-level licence/attribution and public availability must be checked before use | PENDING | PENDING | PENDING | Do not use Copernicus DSM as bare-earth terrain; it includes vegetation/buildings. Obtain actual tile, verify CRS/vertical datum/NoData, then derive slope and aspect reproducibly. |


## Chapter 13 — final four visuals — 5 November 2026

| Visual ID | Presence | Scientific / factual | Rights / licence | RU–EN parity | Accessibility | Technical | Finding / next action |
|---|---|---|---|---|---|---|---|
| 13-G | INTEGRATED | PASS — erosion, salinisation, compaction and vegetation-cover loss are shown as distinct processes; response hierarchy follows UNCCD avoid–reduce–reverse | PENDING — original project licence not assigned | PASS | PENDING — alt text and labels present; contrast review pending | PASS — static SVG and local embed; browser render pending | Measures are context-specific; no universal restoration prescription. |
| 13-I | INTEGRATED | PASS — objective-setting, multiple data streams, QA/QC, analysis, publication and feedback shown | PENDING | PASS | PENDING | PASS — static SVG and local embed; browser render pending | Community observations are shown as a separate stream, not a substitute for standardised measurement. |
| 13-J | INTEGRATED | PASS — technical and biological cycles separated; inner value-retention loops prioritised; recycling shown as last resort | PENDING | PASS | PENDING | PASS — static SVG and local embed; browser render pending | Original diagram is distinct from the Ellen MacArthur Foundation butterfly graphic; no tracing/copying. |
| 13-K | INTEGRATED | PASS WITH SCOPE NOTE — fictional urban districts; pollution and green-space access are hypothetical; distributional, recognition and procedural dimensions distinguished | PENDING | PASS | PENDING | PASS — static SVG and local embed; browser render pending | Do not interpret as a real Kyrgyzstan map or as a single numerical environmental-justice index. |

All four files pass source-level SVG checks for root, viewBox, title, description, role=img and Russian/English text. The local chapter embed paths resolve. No browser, responsive or assistive-technology test is claimed. None is VERIFIED.


### Chapter 18 — supplementary Blue Green Atlas relief overview

| Figure | Presence | Scientific / factual | Rights / licence | RU–EN parity | Accessibility | Technical | Finding / next action |
|---|---|---|---|---|---|---|---|
| Kyrgyzstan relief overview | INTEGRATED — supplementary map | PASS WITH LIMITATION — projection and source datasets identified; map compilation date, vertical reference and accuracy are not stated | PASS — source page explicitly CC BY 4.0; attribution included | PASS — bilingual alt text/caption | PENDING — alt text present; manual accessibility review pending | PENDING — external image loading/responsive behaviour untested | Useful relief context only; does not close 18-A, which still requires a validated DEM with full metadata. |


### Chapter 12 — supplementary NASA/JPL North America relief image

| Figure | Presence | Scientific / factual | Rights / licence | RU–EN parity | Accessibility | Technical | Finding / next action |
|---|---|---|---|---|---|---|---|
| NASA/JPL PIA03377 | INTEGRATED — supplementary relief image | PASS WITH LIMITATION — SRTM acquisition, reduction, resampling, Mercator projection and date are documented; not a named hydrography layer | PASS subject to NASA media-use guidance; NASA/JPL credit retained, no third-party copyright notice shown | PASS — bilingual alt text and caption | PENDING — alt text present; manual accessibility review pending | PENDING — remote image load and responsive behaviour untested | Useful relief context only. Planned 12-F still requires a verified drainage-network map with named systems and flow directions. |


## Consolidated open visual blockers — Chapters 11–20 — 5 November 2026

This table lists only visual IDs that still lack a confirmed integrated asset. Integrated visuals with outstanding scientific, rights, date, accessibility or rendered QA are listed separately below. A placeholder is not counted as coverage.

| Visual ID | Required asset | Why it remains open | Evidence needed to close |
|---|---|---|---|
| 12-C | Central Asia/transboundary systems map | Requires a consistent regional layer set for basins, mountain systems, marine ecosystems and corridors; no single verified combined map found. | Documented basin/mountain/marine/corridor datasets, dates, CRS, licences and clear thematic scope; do not combine unrelated layers without metadata. |
| 12-J | Antarctica and Southern Ocean map | Needs a dated ice-sheet and research-station layer plus an explicit ocean-boundary convention; territorial claims must not be implied. | Current SCAR/BAS or equivalent layers, station data date, adopted Southern Ocean boundary and polar projection. |
| 14-G | DEM, slope and aspect | NASA SRTM (~30 m) and Copernicus GLO-30/90 candidates found, but no exact Kyrgyzstan tile downloaded and validated. Copernicus GLO-30 is a DSM, not bare-earth DTM. | Exact raster tile, licence, CRS, vertical datum/geoid, NoData/void treatment, pixel spacing; reproducible slope/aspect derivation and stated units. |
| 17-H | Geological structure and mineral districts | National geological atlas is announced but not confirmed as published/open; older map images are dated or have unclear rights. | Published geological map layers with source, date, scale, licence and resource-status categories; distinguish occurrence, prospect, deposit and producing mine. |
| 18-A | Validated national physical map / DEM | Blue Green Atlas relief overview is integrated as supplementary context (SRTM3 ~90 m, Mercator) but lacks compilation date, vertical reference and accuracy statement. | Validated DEM and derived hypsometry/range/basin layers with CRS, vertical datum, source date and accuracy. |
| 18-E | Multi-hazard map | No authoritative, consistently dated layers for seismicity, landslides, debris flows, rockfalls, avalanches and glacial lakes have been validated together. | Separate hazard layers, dates, scales and methods; keep hazard, exposure and vulnerability distinct; avoid implying a single comparable risk index. |
| 18-F | Tectonic map | Candidate academic tectonic figures have been screened, but figure-level reuse rights and a consistent scientific model for the whole Tien Shan are unresolved. | A peer-reviewed regional tectonic model with explicit terranes/sutures/faults, source date and reuse terms; review by a geologist. |
| 18-G | Orographic map | A schematic range hierarchy is described, but no validated spatial layer set has been assembled for the named Tien Shan/Pamir-Alay divisions. | Verified range geometry and authoritative toponymy; map scale, CRS and classification explanation. |
| 18-I | Mineral-resource districts | National geological map/atlas layers are not yet available with verified public reuse terms; avoid turning occurrences into producing mines or reserves. | Official published mineral-occurrence/deposit data, date, status classes, scale and licence. |
| 19-A | Climate-region map | Climate classification is described, but spatial boundaries need station data, elevation and a stated classification method. | Official station normals, climate classification thresholds, period, elevation data and validated boundary method. |
| 19-B | Annual precipitation and orographic rain-shadow map | Station summaries are documented; raw spatial data and a validated interpolation method are not yet available for a defensible national surface. | Station-level precipitation series, normal period, station metadata, quality flags, interpolation method/cross-validation and orographic interpretation. |
| 19-G | Mean annual temperature map | A national trend chart is integrated, but it is not a spatial temperature surface. | Station-level normals for a single climate period, station locations/elevations, interpolation method, cross-validation and uncertainty. |
| 20-A | Current glacier inventory | Research inventory for the Kyrgyz/Teskey ranges and global inventories are candidates, but no complete dated national outline set and clipping boundary are validated. | Dated glacier outlines, minimum-area threshold, inventory method, CRS, uncertainty and national boundary source. |
| 20-B | River basins and transboundary flow map | Historical AF NWRMP basin maps are located but are dated and item-level reuse rights/current geometry are unresolved. | Current basin/watershed boundaries, river network and direction, transboundary-flow evidence, CRS, source date and licence. |
| 20-G | Naryn seasonal/interannual hydrograph | UNH station 16055 metadata identified (1931–2006; mean 92.117 m³/s), but raw reusable observations and item-specific licence are unconfirmed. | Raw daily/monthly series, station identity, time step, quality flags, missing-data treatment, licence and gauge metadata. |

### Integrated assets with outstanding verification

| Visual ID | Integrated visual | Remaining verification |
|---|---|---|
| 12-E | Blue Green Atlas Europe physical-relief map, CC BY 4.0 | Scientific review of named plains/ranges/peninsulas and macroregional key; remote-image responsive/browser/accessibility QA. |
| 12-F | Blue Green Atlas North America relief map, CC BY 4.0 | Scientific review of river-direction key and map interpretation; remote-image QA. |
| 12-G | CIA Central America/Caribbean shaded-relief map, public domain | Scientific review of named island arcs/passages/canal key; remote-image QA. |
| 12-H | Blue Green Atlas South America relief map, CC BY 4.0 | Scientific review of regional/drainage key; remote-image QA. |
| 12-I | Blue Green Atlas Oceania relief map, CC BY 4.0 | Scientific review of island-origin examples and coverage; remote-image QA. |
| 17-A | Blue Green Atlas locator + OCHA COD-AB administrative outline | OCHA source release/version date and current legal-border validation; remote JPEG/SVG QA. |
| 17-B | SRTM/GMT topographic map of Kyrgyzstan, public domain | Exact source-raster date unknown; verify range/valley labels and caveat the red boundary line; remote-image QA. |
| 17-D | Blue Green Atlas relief context + original bilingual valley profile | Verify the seven reference anchors geospatially; assign formal project creator/licence to original SVG; remote-image QA. |
| 17-F | Poggi et al. (2024) earthquake-epicentre and active-fault maps, CC BY 4.0 | Remote figure rendering/responsive/accessibility QA; scientific scope caveat already recorded. |
| 17-I | OCHA COD-AB labelled administrative map, CC BY-IGO | OCHA source release/version date; confirm Manas city toponym update; remote SVG and accessibility QA. |
| 19-I | Original bilingual seasonal snow/precipitation profile SVG | Formal project creator/licence assignment and live render/accessibility QA; scientific concept reviewed as qualitative only. |

### Closure rule

Do not replace a missing map with a decorative or approximate schematic when the learning objective requires real spatial data. If a suitable dataset cannot be accessed or licensed, keep the item MISSING and record the exact blocker. Where a conceptual diagram is appropriate, author it separately and label it as conceptual rather than presenting it as measured geography.


### Chapter 07 — Visuals 07-G and 07-I integrated — 5 November 2026

- **07-G:** original bilingual SVG comparing lake and ocean cross-sections; photic/aphotic water, littoral/coastal, pelagic and benthic zones are labelled. No universal depth threshold is shown. Published lake/ocean zonation diagrams were reviewed; no third-party figure was copied. Scientific concept and RU/EN labels checked; project rights, accessibility and rendered browser/mobile QA remain PENDING.
- **07-I:** original bilingual SVG summarising carbon and nitrogen pathways. It separates reservoirs from processes and gives no numerical stocks or flux rates. Public-domain Commons cycle diagrams were reviewed as references; no source artwork was copied. Scientific pathway and RU/EN checks completed; project rights, accessibility and rendered browser/mobile QA remain PENDING.
- Chapter 07: **5/9 integrated** (07-A, 07-B, 07-D, 07-G, 07-I); four gaps remain. Atlas coverage: **153/281 (54.4%)**, with **128 named IDs** still lacking integrated images. Integrated does not mean VERIFIED.


### Chapter 07 — Visuals 07-F and 07-H integrated — 5 November 2026

- **07-F:** original bilingual 11-scene vector panorama, grouped to compare major terrestrial-biome structures and adaptations. Scenes are conceptual, not mapped locations or current land cover; the figure directs readers to the named RESOLVE 2017 classification for formal biome mapping. Scientific concept and RU/EN labels checked; project rights/licence decision, accessibility and rendered browser/mobile QA remain PENDING.
- **07-H:** original bilingual conceptual habitat-connectivity diagram showing core areas, buffer zones, a corridor, a road barrier, fragmented patches and landscape matrix. Dashed movement is explicitly hypothetical. The components were checked against NatureScot's habitat-network guidance; no real protected-area network is implied. Scientific concept and RU/EN labels checked; project rights/licence decision, accessibility and rendered browser/mobile QA remain PENDING.
- Chapter 07: **7/9 integrated**; 07-C (global biome map) and 07-E (biogeographical realms map) remain open because the source geometries have not yet been obtained and validated for a reproducible map. Atlas coverage: **153/281 (54.4%)**; **128 named IDs** remain without an integrated image. Integrated does not mean VERIFIED.
