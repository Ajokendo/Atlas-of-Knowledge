# Atlas of Geography — Editorial Readiness Matrix
**Snapshot:** 4 November 2026  
**Canonical branch:** `workspace/geography`  
**Purpose:** auditable status of the 26 chapters and the remaining work. This matrix deliberately does not invent one overall completion percentage.



## Quantitative chapter progress — 4 November 2026

**Working production score: 76% average across all 26 chapters (equal chapter weighting).** This is a progress estimate for the editorial/content-production scope, not a publication-readiness or deployment score. Chapters 01–04 are recorded at 100% in that scope; Chapters 05–26 have been rescored using a weighted rubric: content/structure 30 points; Russian/English development 20; pedagogical apparatus 15; sources/evidence 20; visual integration 15. The 22 rescored chapters average 71.3%. The bilingual component is 16/20 where substantial RU/EN material exists but line-by-line parity is not verified. Visual points are proportional to assets actually integrated in both language versions; briefs and placeholders earn zero. The evidence component reflects the depth of documented source checks, not a full sentence-by-sentence audit.

## Cross-chapter status

| Workstream | Verified status | Remaining work |
|---|---|---|
| Chapter inventory | 26/26 numbered chapters present | None for chapter count |
| Structural audit | 26/26 received an initial structural pass; Chapter 19 subsection-order defect found and corrected on 2 Nov | Final copyedit and depth review |
| Russian/English structure | 26/26 contain substantial Russian and English teaching material; some chapters use parallel blocks, others section-by-section pairs | Full line-by-line translation parity and proofreading |
| Visual planning | 220/220 unique IDs indexed | Create, label, source-check and approve each asset |
| Visual brief language | 220/220 IDs have Russian and English production instructions | Final design and typesetting |
| Bibliography presence | Reference section present in all 26 chapters; Chapter 09 gap closed | Open and verify every citation against each adjacent claim |
| Bibliography placeholder scan | No explicit TODO/TBD/incomplete DOI/URL instruction found in reference sections | Link availability and source relevance still require review |
| Numbering integrity | No duplicate numbered section identifiers across 26 chapters | Normalise Chapter 17's distinct label 17.14а during final style pass |
| Repository structure | One active Geography branch: `workspace/geography` | Keep using this branch only |
| Website | Bilingual RU/EN landing-page toggle and 26 chapter links | In-chapter language filter, rendered Markdown reader, accessibility and deployment tests |
| Created and embedded visuals | 20 local SVG assets are embedded in both language versions: five in Chapter 01, eleven in Chapter 02 and four in Chapters 18–20. Chapter 02 also includes nine remote source images. Chapter 01 includes four original bilingual diagrams and one adapted CC BY 4.0 diagram. | Final scientific/editorial sign-off for the integrated assets; create and integrate the remaining planned visuals; deployed accessibility/rendering QA remains separate |

## Chapter-by-chapter matrix

| Ch. | Chapter | Visual IDs | Structure / bilingual pass | Selected source or calculation checks | Priority remaining |
|---:|---|---:|---|---|---|
| 01 | Geography as a Science | 5 | **Content and editorial package complete: 100% (4 Nov 2026).** Final RU/EN proofread completed; 18 references and bilingual claim-to-source map; MAUP/ecological-fallacy coverage; scale arithmetic checked; seven oblasts and separate city status of Bishkek/Osh verified in both languages; all five visuals (01-A–01-E) created/adapted and embedded in RU/EN (10 embeds, five local SVGs) with bilingual alt text and source/rights notes. Static SVG source checks passed: viewBox, title, description, role=img, bilingual labels and escaped entities. | RGS, National Geographic Standards 1 and 3, UN-GGIM, ICA, Longley et al., National Research Council, NSC regional/city publications and quarterly bulletin, USGS projection guidance, Buzzelli (2020), Holt et al. (1996), National Geographic Geo-Inquiry, GeogSage (CC BY 4.0) | Outside the 100% content scope: rendered-browser visual inspection, responsive/mobile, keyboard and screen-reader checks after deployment; school trials/community feedback remain a separate event |
| 02 | Earth's Geographic Envelope | 19 | **Chapter content and editorial package complete: 100%** (4 Nov 2026). RU/EN scientific copy-edit, dated-value/source verification, bilingual visual integration and static asset/alt-text checks are complete. | Corrected four-component vs five-sphere Earth-system classification; clarified cryosphere/hydrosphere overlap and lithosphere/geosphere relation; confirmed USGS water table is based on Shiklomanov 1993; checked average continental/oceanic crust-thickness values and the greater thickness beneath major collision mountain belts against USGS and 2025 crustal synthesis; clarified that the “about 4 billion years” age applies to rare preserved rocks, not all continental crust, and that oceanic crust is renewed at ridges and recycled at subduction zones; mapped distinct divergent, convergent, collision and transform outcomes; clarified diffuse plate-boundary zones, intraplate earthquakes and limits of a single-factor explanation of plate motion; expanded the bilingual water-cycle explanation to include evapotranspiration, snowmelt, infiltration/percolation, groundwater recharge and discharge, sublimation, temporary storage and human alterations; distinguished resistance, recovery and ecological resilience in RU/EN; clarified that resilience does not require a return to the former state; refined positive/negative feedback definitions and added paired examples with source mapping; replaced an ambiguous cloud-feedback illustration in the worked feedback section with a clearer predator–prey example and cited a 2024 ecological feedback synthesis; added NASA Earth-system spheres, USGS water-cycle and plate-motion, NOAA dry-air composition/carbon-cycle, NASA energy-budget, UNEP nitrogen-cycle, Missouri Extension nitrogen-cycle and Open University phosphorus-cycle references; retained separate NOAA marine-site and WMO global CO₂ series; added English equivalents for subsections 2.14.1–2.14.3, including the worked mountain-catchment example and feedback-recognition activity; planetary-boundary assessment updated to PIK Planetary Health Check 2026 (seven of nine boundaries transgressed; DOI 10.48485/pik.2026.25) | Outside the chapter-completion percentage: school-based trials and community feedback are a separate event, not a completion gate. After deployment, live rendering, responsive/mobile, keyboard and screen-reader checks belong to separate technical release QA; they have not yet been performed. Static image/alt-text checks and source-image fetch checks are complete; live rendering and assistive-technology behaviour are not yet verified. Chapter 02 has 19 unique visual IDs and all 19 now have integrated imagery or original diagrams. The missing 2.10-A and 2.10-B visuals now use existing My NASA Data/DOE carbon-cycle, My NASA Data/NCAR nitrogen-cycle and Wikimedia Commons phosphorus-cycle (CC0 1.0) images; 2.15-A uses the existing NASA Earth System Diagram as the integrated summary. These established science visuals were preferred to newly created replacements in line with the image-first policy. The 2.13-A provisional Nature Data Lab JPEG was replaced on 4 November 2026 with Figure 10 from Theobald et al. (2025), “Global extent and change in human modification of terrestrial ecosystems from 1990 to 2022”, *Scientific Data* 12, Article 606, DOI 10.1038/s41597-025-04892-2. The article's Rights and permissions statement applies CC BY 4.0 to article images unless a separate credit line states otherwise; no separate restrictive credit line appears for Figure 10. The replacement figure depicts the 2022 cumulative human-modification map at 300 m resolution; Antarctica is excluded. Attribution, DOI, licence link and no-changes statement are included in the chapter. There are 40 Markdown image embeds representing 20 unique assets: nine remote images and eleven original bilingual SVG diagrams; the 2026 planetary-boundaries SVG is intentionally embedded in both language sections. All 40 Markdown image embeds have non-empty bilingual alt text; all 11 local SVGs include title, description and role=img metadata. The new 2.14-A original bilingual SVG reports the 2026 assessment (7/9 transgressed) and cites PBScience/PIK, DOI 10.48485/pik.2026.25. Browser image checks rendered NASA, both NOAA images, USGS water distribution, both My NASA Data diagrams, the USGS water-cycle image (after replacing its inaccessible original CDN URL with the verified full-width image endpoint), and the Wikimedia phosphorus-cycle image (original file and CC0 licence verified on Commons). The replacement Figure 10 image from Scientific Data was opened and visually verified in the browser; the article-level CC BY 4.0 terms and absence of a separate restrictive credit line for Figure 10 were checked. GitHub-hosted SVG is committed but no deployed site URL or deployment workflow is established in this branch; live-site, mobile-device and screen-reader tests therefore remain outstanding. |
| 03 | Lithosphere and Geological Processes | 13 | Text audit complete (100%). All 13 visual IDs now integrated in RU/EN: ten original bilingual SVGs plus three sourced images (USGS minerals, USGS I-2800 plate map, ICS chart 2026/06). No visual placeholders remain. | References include USGS, BGS, ICS 2026/06, Halla et al. (2024), USGS OFR 94-636 and USGS I-2800. | Remaining: final scientific/editorial artwork sign-off, visual/layout review, and separate browser/device/accessibility/deployment QA. These technical tests are not claimed complete.
| 04 | Earth's Landforms and Relief | 16 | Text audit complete (100%). All 16 visual IDs now integrated in RU/EN as bilingual SVGs, including coastal/ocean-floor relief, slope processes, weathering, DEM/DSM/DTM, vertical extremes and a topographic exercise with worked gradient key. No visual placeholders remain. | Bibliography includes Fujii et al. (2026) Challenger Deep multibeam study, distinguishing its preferred 10,927 m gridded estimate from the 2021 pressure-based 10,935 ± 6 m estimate; USGS supports map-reading guidance. | Remaining: final scientific/editorial artwork and exercise sign-off, visual/layout review, and separate browser/device/accessibility/deployment QA. These technical tests are not claimed complete.
| 05 | Atmosphere and Climatology | 20 | **90%** — основной RU/EN текст и учебный аппарат готовы; 16 уникальных визуалов интегрированы, включая 5.17-A — двуязычные климатограммы с условными учебными данными; остаётся 1 учебный визуал — 5.18-A | NOAA marine-surface 2025 preliminary mean (425.62 ppm) distinguished from WMO GAW global surface mean (426.8 ± 0.2 ppm); WMO-No. 1203 (2017), WMO-No. 1245 (2020) homogenisation guidance, the distinction between the operational 1991–2020 normal and fixed 1961–1990 climate-change reference period, the distinction between the 6.5°C/km International Standard Atmosphere model lapse rate and the variable observed environmental lapse rate, a relative-humidity definition/formula based on actual versus saturation vapour pressure added; cloud-formation text aligned with WMO's ten cloud genera and clarified liquid droplets, ice crystals and supercooled water; RU/EN explanations of cold, warm, occluded (cold/warm variants) and stationary fronts expanded and checked against NOAA/WMO references; a bilingual 5.18.2 synoptic-chart reading method added; all eight local Chapter 05 SVG assets re-fetched and structurally checked for valid SVG boundaries, title, description, role=img and bilingual labels; 2026 WMO-No. 8 explicitly marked provisional pending INFCOM-4 approval; scientific proofreading of Chapter 5 claims completed, with source checks/links covering atmospheric circulation, cloud genera, air masses and fronts, climate controls, Köppen–Geiger map methodology, tropical-cyclone formation, drought and heatwave definitions, fog and dust, urban heat islands, and solid-precipitation measurement; 5.18.1 climate-anomaly comparison is now separately present in the English-language chapter as well as the Russian section, alongside the bilingual 5.18.2 synoptic-chart method; worked-example arithmetic verified (377 mm annual precipitation; 29°C annual temperature range); synthetic 5.17-A climate graphs checked (A: 364 mm with a large annual temperature range; B: 925 mm with year-round precipitation and a smaller temperature range); 16 integrated visuals include CC0 atmospheric layers, NOAA circulation, UCAR-hosted IPCC AR6 energy budget (2021), NWS pressure system, original dry-air composition SVG, ERA5 1991–2020 mean temperature (CC BY-SA 4.0), NOAA hydrologic cycle, original cloud-lifting-processes SVG (adapted under CC BY-SA 4.0), Köppen–Geiger 1991–2020 map (CC0), NOAA front symbols plus cold-occlusion cross-section, original weather-versus-climate SVG, global climate-belts SVG, atmospheric-hazards infographic, climate-change drivers/evidence/responses infographic, and weather-observations-to-forecast SVG (5.16-A); ECMWF data-assimilation and modelling guidance and WMO observing-system sources added | Only the 5.18-A synoptic-map and climate-analysis visual remains for editorial completion; desktop/mobile browser and published-site rendering checks are tracked separately as a later QA activity and do not gate editorial completion
| 06 | Hydrosphere and World Ocean | 4 | **73%** — основной RU/EN текст и учебный аппарат готовы; ключевые источники и расчёты проверены; визуалы не интегрированы | USGS global water table, NOAA, UNESCO WWDR, IHO S-23/S-44/S-102/S-100, NSIDC, TEOS-10 and USDA watershed water-budget source checked; global water-share category error corrected | No numerical trench/depth dataset is asserted in current text; future bathymetry maps must identify survey/product, date, resolution and vertical datum |
| 07 | Biosphere and Natural Biomes | 9 | **73%** — основной RU/EN текст и учебный аппарат готовы; базовые источники проверены; визуалы не интегрированы | CBD Targets 2–3, IPBES, IUCN criteria/guidelines and assessment metadata, UNESCO MAB, Olson et al. and Millennium Assessment sources checked; Chapin book metadata completed | Final biome/ecoregion classification consistency check; no named species-status claims occur in the current text, and any future species case must cite its dated individual Red List assessment |
| 08 | Soils and Landscape Geography | 7 | **73%** — основной RU/EN текст и учебный аппарат готовы; базовые источники проверены; визуалы не интегрированы | WRB 2022/2024 correction, FAO/ITPS 2026 assessment, FAO salinity methods, USDA Soil Survey Manual and NRCS Field Book v4 (2024) checked; Turner book metadata completed | Final terminology consistency check; no country-level soil statistics are claimed in current text, and future regional maps/measurements require full dataset and sampling metadata |
| 09 | Population and Demography | 6 | **73%** — основной RU/EN текст и учебный аппарат готовы; методологические источники проверены; визуалы не интегрированы | UN WPP 2024 and methodology, WUP 2025 and methodology, census Rev.4, UNSD methods, IOM WMR 2024, UN-Habitat, WDI and UNDP data portals checked; demographic formulas and hypothetical examples recalculated | Current numerical examples are explicitly hypothetical; before adding real demographic maps/data, attach exact table/indicator, scenario, territory, reference year and extraction date |
| 10 | Political Geography | 7 | **73%** — основной RU/EN текст и учебный аппарат готовы; основные правовые источники проверены; визуалы не интегрированы | UN Charter, UNCLOS Parts II/V/VI/VII, VCLT, UNGA 1514 (XV), Montevideo Convention, M49 and ICJ Statute sources checked; legal books' editions/metadata completed | Current chapter is conceptual and makes no named disputed-territory status claims; any future country case study requires primary legal instruments, applicable agreements and court/tribunal decisions with date and geographic scope |
| 11 | Economic Geography | 7 | **69%** — основной RU/EN текст и учебный аппарат готовы; проверка источников и страновых примеров не завершена; визуалы не интегрированы | Location quotient checked; 2025 SNA added alongside 2008 SNA; core data references linked | Update and verify any country examples |
| 12 | Geography of World Regions | 10 | **69%** — основной RU/EN текст и учебный аппарат готовы; региональные данные и карты требуют проверки; визуалы не интегрированы | M49 statistical grouping source linked; regional references refreshed | Check regional data dates and map classifications |
| 13 | Ecology and Global Change | 11 | **69%** — основной RU/EN текст и учебный аппарат готовы; требуется полная проверка экологических индикаторов; визуалы не интегрированы | 2023 assessment (six of nine planetary boundaries) added in RU/EN; Nature DOI verified | Full environmental-indicator proofread |
| 14 | Geographic Information Systems | 9 | **69%** — основной RU/EN текст и учебный аппарат готовы; остаётся проверка версий ПО и метаданных геоданных; визуалы не интегрированы | OGC, ISO/TC 211, EPSG, QGIS, Esri and UN-GGIM references refreshed; Digital Code No. 178 (2025), Chapter 12, Articles 92–98 reviewed; UNESCAP 2020 baseline and 2026 AIP cross-checked for Kyrg-06/WGS 84 and Baltic-based vertical reference | Software-version and workflow validation; verify dataset-specific horizontal/vertical realization, transformation parameters, metadata and reuse conditions |
| 15 | Remote Sensing of the Earth | 11 | **69%** — основной RU/EN текст и учебный аппарат готовы; остаётся проверка сенсорных метаданных и точности; визуалы не интегрированы | NASA, USGS, ESA and Copernicus sources linked; broken Sentinel-1 URL replaced | Sensor/product metadata and accuracy review |
| 16 | Geographic Research and Cartography | 9 | **69%** — основной RU/EN текст и учебный аппарат готовы; методологическая проверка не завершена; визуалы не интегрированы | ICA Cartographic Body of Knowledge and UN census-methodology references linked | Full methodology and assessment review |
| 17 | Geographic Location and Geological Evolution of Kyrgyzstan | 9 | **73%** — основной RU/EN текст и учебный аппарат готовы; источники геоданных частично проверены; 0/9 визуалов интегрировано | Area, border-demarcation and 2026 treaty updates checked; added Law No. 58 (2026), AIS Geographical Names, official 2025 WGS 84 pilot and UNESCAP 2020 national geodetic baseline | Extreme-point coordinates; obtain transformation/control-point metadata and verify dataset-specific vertical datum, legacy-map migration, national boundary geometry and toponyms |
| 18 | Geology, Mountain Systems and Relief of Kyrgyzstan | 10 | **75%** — основной RU/EN текст и учебный аппарат готовы; источники частично проверены; 1/10 визуалов интегрирован | Peak heights and country-specific Lenin/Ibn Sina naming checked; incomplete geological citations corrected; DEM vertical-reference guidance added; CAIAG ASTER GDEM 30 m candidate, RESILAND 3 m/14-site procurement, 2026 national geological-atlas project and historical glacier-source limits documented | Obtain licensed/validated DEMs and full CRS/vertical metadata; verify glacier outlines against current imagery; review national geological atlas when published; validate peak heights and map sources |
| 19 | Climate and Altitudinal Zonation of Kyrgyzstan | 10 | **67%** — требуется завершить структурную проверку; климатические ряды изучены частично; 1/10 визуалов интегрирован | UNEP +1.2°C 1960–2023 estimate cross-checked with Kyrgyzhydromet: 22 homogenised stations (1980–2021), +0.28°C/decade countrywide; separate 13-station climate indices (1980–2022), growing-season trends and method limits documented | Obtain station-level series/metadata; reconcile climate-normal periods; validate high-mountain spatial interpolation and future projections |
| 20 | Glaciers, Rivers, Lakes and Water Resources of Kyrgyzstan | 10 | **76%** — основной RU/EN текст и учебный аппарат готовы; источники частично проверены; 2/10 визуалов интегрировано | River-runoff range, renewable water resources, glacier mass balance, Chu–Talas transfer and Issyk-Kul morphometry checked; 2025 research inventory reports >2,000 glacial lakes (Sentinel-2 2022–2024); 2026 Kyrgyz Range study quantifies lake/glacier change 1968–2021; NSC 2025 water-use indicators and WIS scope documented; 2025 national mudflow/flood hazard atlas reviewed | Obtain/verify lake polygons and reuse rights; obtain station-level discharge series and metadata; validate basin/reservoir records, current glacier outlines and GLOF hazard layers; inspect hazard-atlas map scale, legend and layer licensing |
| 21 | Flora and Fauna of Kyrgyzstan | 10 | **71%** — основной RU/EN текст и учебный аппарат готовы; видовые оценки и популяционные тренды требуют проверки; 0/10 визуалов интегрировано | Red List counts checked; 2040 biodiversity programme correctly labelled as draft pending approval | Species taxonomy, population trends and sensitive-location review |
| 22 | Natural Zones, Protected Areas and National Parks of Kyrgyzstan | 10 | **71%** — основной RU/EN текст и учебный аппарат готовы; правовой статус и геометрии ООПТ требуют проверки; 0/10 визуалов интегрировано | NSC protected-area series, UNDP 7.4%, UNESCO MAB areas and 2025 management figures checked | Legal status and official protected-area geometries |
| 23 | Population and Settlement of Kyrgyzstan | 12 | **71%** — основной RU/EN текст и учебный аппарат готовы; остаётся финальная вычитка миграции и урбанизации; 0/12 визуалов интегрировано | NSC 2026 population, regional totals, 2025 births/deaths and migration; IOM Round 7 checked | Final migration, urbanisation and settlement proofread |
| 24 | Seven Regions of Kyrgyzstan | 12 | **71%** — основной RU/EN текст и учебный аппарат готовы; нужна углублённая проверка профилей областей и карт; 0/12 визуалов интегрировано | Administrative reform law, Manas renaming, 2026 population table and 27 Oct proposal checked | Deep profile-by-profile source and map validation |
| 25 | Cities, Economy, Transport and Natural Resources of Kyrgyzstan | 12 | **71%** — основной RU/EN текст и учебный аппарат готовы; статус инфраструктурных проектов требует проверки; 0/12 визуалов интегрировано | GDP, road transport, energy import planning and mining indicators checked | Verify operational status of each infrastructure project |
| 26 | Environmental Challenges and Future of Kyrgyzstan | 12 | **71%** — основной RU/EN текст и учебный аппарат готовы; требуется сверка станционных данных по воздуху и инвентаризации ледников; 0/12 визуалов интегрировано | NDC 3.0, Climate Law, water, wastewater, forests, pastures and waste figures checked; visual IDs normalised | Air-quality station data and glacier-inventory reconciliation |

## Chapters 06–10 — focused follow-up — 5 November 2026

A focused scientific/editorial correction pass was saved across Chapters 06–10: Chapter 06 now distinguishes dimensionless Practical Salinity (PSS-78) from Absolute Salinity (g/kg) under TEOS-10; Chapter 07 explains the limits of IUCN Red List categories and the meaning of Data Deficient / Not Evaluated; Chapter 08 identifies the 2026 FAO global soil assessment and its Europe/Central Asia regional chapter; Chapter 09 requires WPP table/scenario/extraction-date metadata and distinguishes international from national urban definitions; Chapter 10 expands the UNCLOS EEZ explanation to distinguish coastal-state sovereign rights/jurisdiction from other states' retained freedoms. The source-by-source findings are in `SOURCE_EVIDENCE_CLOSURE_REGISTER.md`.

**Progress remains 73% for each of Chapters 06–10.** This pass improves specific scientific claims and bibliography traceability but does not close the full editorial scope: planned visual assets remain unintegrated, complete claim-to-source mapping and final RU/EN proofreading remain open. No browser/device/deployment QA is claimed.

**Bilingual structure check completed:** numbered teaching-section headings match RU/EN counts in Chapters 06–10 (17/17, 15/15, 15/15, 16/16 and 15/15 respectively). Review-question counts also match (16/16, 15/15, 15/15, 15/15 and 14/14). This verifies section/question inventory only; it is not a line-by-line semantic translation audit.

**Second focused pass (5 November 2026):** Chapter 07 now distinguishes CBD Kunming–Montreal Framework Targets 2 (restoration of degraded ecosystems) and 3 (area-based conservation); Chapter 08 specifies ECe saturated-paste salinity measurements and warns against comparing them directly with 1:5 extracts or field apparent EC; Chapter 09 distinguishes migration flows from point-in-time migrant stock; Chapter 10 specifies the UNCLOS contiguous-zone 24-nautical-mile limit and the narrow enforcement purpose under Article 33. Exact source checks and commits are recorded in `SOURCE_EVIDENCE_CLOSURE_REGISTER.md`. Progress remains **73% each**; this is not a full editorial sign-off.

## Priority queue

1. Continue source-by-source review of Chapters 01–16, including dated data and bibliographic relevance. Initial targeted evidence pass completed for Chapters 01–10; see `geography/SOURCE_EVIDENCE_CLOSURE_REGISTER.md` (2 Nov 2026).
2. Finish the remaining map-source checks for Kyrgyzstan's administrative, geological, climate, hydrological, biodiversity and protected-area layers.
3. Perform final Russian/English proofreading and resolve terminology/translation asymmetries.
4. Build the bilingual web reader and test chapter navigation, accessibility and mobile layout.
5. Produce visual assets in controlled batches; each image must retain its ID, bilingual caption, data source, licence and approval status.
6. Run final editorial, scientific, accessibility and deployment checks before describing the atlas as publication-ready.

**Important:** “Complete” in the chapter matrix means the structural and bilingual production pass is complete. It does not mean every scientific claim has been independently verified or that the chapter is ready for final publication.


## Additional legal-source review — 1 November 2026

- Chapter 14 cross-check: the Digital Code of the Kyrgyz Republic, 31 July 2025, No. 178, Chapter 12 (Articles 92–98), establishes the national legal framework for spatial data, metadata, the Georesource and geosite. A separate audit note is stored at `geography/NATIONAL_SPATIAL_DATA_FRAMEWORK_KG_2026-11-01.md` (commit `599a9fd7521a515d919e71e46a205c50f3c1a0a1`).
- This legal framework is not evidence that individual national datasets are already downloadable or validated. Dataset-level source, metadata, CRS, licence, date and access conditions remain to be checked.


- Chapter 17 map-source audit extended with the State Agency's 11 November 2025 report on the WGS 84 transformation pilot, including partial map reprojection and deployment of transformation/control-point systems. Public numerical parameters, accuracy, epoch, vertical model and full migration status remain unverified. Audit commit: `fe89e0398e8eb41d4e50062a796f064274651c5d`.


- UNESCAP December 2020 report (section 5.1.2) added as a dated national geospatial baseline: Kyrg-06/ITRF-2005, 1977 Baltic Altitude System and legacy SK-42/Gauss–Krüger map series. Cross-checked against AIP GEN 2.1 effective 6 August 2026. This strengthens metadata requirements but does not certify individual dataset realizations or map migration. Audit commit: `99eec93e822470b07848c9fa73c24d6ca6310c54`.

- Chapter 18 now documents specific DEM and geological/glacier sources with explicit coverage, licensing, metadata and date limitations. It does not promote the CAIAG 30 m layer or the 14-site RESILAND DEM procurement to validated nationwide base data. Update commit: `308a879c3c040cdef76776ea4f8c870eae196b27`.

- Chapters 19–20 updated using Kyrgyzhydromet's official climate series and recent glacial-lake research. Important distinction retained between the 22-station monthly trend dataset and the 13-station daily climate-index dataset; the 2025 national lake inventory is labelled research/conference evidence, not a government register. Audit commits: `1034c40f72ac648db116fc43a6749c13eced2e61`; chapter commits: `ab355d723d6224728250626832551a02bf49f994` and `53cfee209ff6bbf83f0241f7208d7cb06b0ecf24`.


## Shared editorial standard adoption — 2 November 2026

- Read the mandatory root `EDITORIAL_STANDARD.md` from `atlas-of-knowledge-integration` (blob SHA `38294a18c47e8127fdd25669d5d15b10b1887256`) and the current `PROJECT_REGISTRY.md` (blob SHA `03537236951f30b0a6f3b79d011bcfd04cd5b652`).
- Recorded Geography's adoption and chapter-level review criteria in `geography/EDITORIAL_STANDARD_ADOPTION.md`. The shared root files were not copied or modified.
- Initial Chapter 01 bilingual review found that the glossary table had Russian definitions only. Added an English-language Key Terms table as section 1.12 in the English chapter text. Commit: `8ce1a147f3dfc1b07689355cd84658046501ae61`.
- Historical note (superseded 4 November 2026): the initial targeted repair did not constitute a full source review. The later Chapter 01 claim-to-source map is now recorded in the chapter; final line-by-line bilingual proofreading and five visual integrations remain open.

- Historical note (superseded 4 November 2026): ICA retrieval initially timed out. The official ICA Commission on Education and Training page was subsequently retrieved and recorded in the editorial audit log; it is no longer an unresolved link.


## Chapter 01–02 visual inventory correction — 4 November 2026

- Chapter 01 contains **5** distinct visual briefs: 01-A (geography as a spatial system), 01-B (location/place/territory), 01-C (research cycle), 01-D (branches of geography) and 01-E (local-to-global scale).
- Chapter 02 contains **19** distinct visual IDs: 2-A, 2.1-A, 2.2-A, 2-B, 2.3-A, 2-C, 2.4-A, 2.5-A, 2.6-A, 2.8-A, 2.9-A, 2-D, 2.10-A, 2.10-B, 2.11-A, 2.12-A, 2.13-A, 2.14-A and 2.15-A.
- The earlier figure of 9 for Chapter 02 was an undercount caused by counting only a subset of the placeholder naming patterns. The repository-wide cross-check confirms **19** Chapter 02 IDs and 220 unique IDs across all 26 chapters; all 19 Chapter 02 IDs now have integrated imagery in both language versions.
- Chapter 01's five IDs remain briefs without integrated imagery. Chapter 02's 19 IDs have images in both language versions; current source and licence details are recorded in `geography/VISUAL_ASSET_REGISTER.md`.


- Visual-source follow-up, 4 November 2026: the initial six-candidate stage was superseded by the final Chapter 02 integration. The current set comprises nine remote science images and 11 local original bilingual SVGs (20 unique assets, 40 Markdown embeds). Rights and source details are recorded in `geography/VISUAL_ASSET_REGISTER.md` and the chapter captions.


### Visual inventory clarification — 4 November 2026

The four additional SVG files in `geography/assets/` are referenced from Chapters 18–20: `18-J-mountain-slope-processes.svg`, `19-H-mountain-valley-circulation.svg`, `20-I-glacier-anatomy.svg` and `20-K-national-water-use-2025.svg`. Chapter 01 has five bilingual visual briefs; none is yet integrated as a finished image. Chapter 02 has 19 bilingual visual IDs, 40 image embeds and 20 unique assets (nine remote science images and 11 local SVGs); the phosphorus-cycle and integrated-system visuals are no longer missing. Live rendering, mobile layout and accessibility remain untested because this branch is not deployed.


### Chapter 02 — primary-source spot check — 4 November 2026

- **Dry-air composition:** NOAA JetStream's live atmospheric-composition table confirms the chapter's rounded nitrogen (78.08%), oxygen (20.95%) and argon (0.93%) values and explicitly excludes water vapour from the dry-air percentages. The chapter's CO₂ figure is separately tied to the preliminary 2025 NOAA marine-surface annual mean (425.6 ppm), rather than treating the static JetStream rounded value as a current annual observation. Source: https://www.noaa.gov/jetstream/atmosphere.
- **Plate boundaries:** USGS *This Dynamic Earth* confirms the distinctions used in the chapter: divergent boundaries create new crust as plates separate; convergent boundaries involve crustal destruction/recycling, commonly by subduction; transform boundaries involve horizontal sliding without net crust creation or destruction. USGS also distinguishes diffuse plate-boundary zones, which should not be forced into the three idealised types. Source: https://pubs.usgs.gov/gip/dynamic/understanding.html.
- **Scope:** this is a focused primary-source check of two claim groups, not a complete geological-process audit or full sentence-by-sentence verification of Chapter 02.


## Chapter 01–02 targeted source review — 4 November 2026

- **Chapter 01, administrative geography:** the Russian and English introductory text now names Batken, Jalal-Abad, Issyk-Kul, Naryn, Osh, Talas and Chui oblasts. It explicitly distinguishes Bishkek and Osh as cities of republican significance, rather than implying that Osh city is the same administrative unit as Osh oblast. The National Statistical Committee's regional-publications index lists seven oblast bulletins and separate Bishkek/Osh city publications; its city profiles confirm the two city statuses.
- **Chapter 01, cartographic literacy:** added a bilingual explanation that projecting Earth's curved surface onto a plane inevitably distorts one or more properties. USGS confirms that no flat projection preserves true direction, distance, area and shape simultaneously; projection choice depends on map purpose.
- **Chapter 02, lithosphere:** the approximate mean thickness values (continental crust about 35–40 km; oceanic crust about 6–7 km) are consistent with USGS syntheses. Added a caveat that thickness varies substantially and can exceed 60–70 km beneath some high mountain systems. The new sources include Mooney (2025; DOI 10.1029/2025JB031907) and NOAA Ocean Exploration's explanation of subduction, oceanic crust formation, trenches and volcanic arcs.
- **Chapter 02, crustal age:** revised the table to distinguish the age of rare preserved ancient continental rocks from the age of continental crust as a whole. Added USGS sources on oceanic-crust recycling and the limits of preserved primordial rocks; the text now explains that oceanic crust forms at mid-ocean ridges and is recycled at subduction zones.
- **Chapter 02, plate-boundary processes:** replaced a broad list of associated landforms and hazards with a bilingual explanation distinguishing divergent spreading, oceanic subduction, continental collision and transform motion. Added a note that deformation can be distributed across broad boundary zones and that intraplate earthquakes also occur. The source note avoids presenting mantle convection as the single settled driver: USGS describes mantle flow, ridge push and slab pull while acknowledging that details remain under study.
- **Scope limitation:** these are targeted checks of the named claims, not a complete source-by-source scientific audit of either chapter. No image has been approved or embedded for Chapters 01–02, and no browser/mobile/deployment test is claimed.


### Chapter 02 — planetary boundaries update — 4 November 2026

- Expanded section 2.14.1 in Russian and English to clarify that planetary boundaries are a global scientific risk framework, not a ready-made set of local or national legal standards; applying the framework below global scale requires appropriate regional data and methods.
- At this intermediate stage, the chapter cited *Planetary Health Check 2025*. This was superseded by the 4 November 2026 update to *Planetary Health Check 2026*: seven of nine boundaries are transgressed and all seven show increasing pressure; the chapter and 2.14-A diagram now use the 2026 assessment (DOI 10.48485/pik.2026.25).
- Added the 2025 report (Sakschewski et al., DOI 10.48485/PIK.2025.017) and the Stockholm Resilience Centre framework page to the chapter bibliography. The visual brief now requires source and assessment year wherever status is displayed.
- Scope: targeted update and source alignment; not a full audit of all global-change indicators. Chapter 02 visual remains a brief only, not an integrated image.


- **Chapter 02, practical assignment — 4 November 2026:** strengthened the RU/EN mountain-lake systems task. Students now trace inflows and outflows, connect all four spheres, identify causal links and propose observations/datasets for testing. Added an explicit distinction between observed evidence and hypotheses, and a warning not to diagnose pollution from water appearance alone. This improves the assessment task but does not substitute for classroom testing.


- **Chapter 02, integrated model — 4 November 2026:** expanded section 2.15 in Russian and English. It now explicitly distinguishes energy flow from matter cycling; identifies system components and permeable boundaries; gives a cross-sphere precipitation–river–erosion–vegetation example; explains feedbacks, scale, time delays, human influence and model limitations. Added NASA My NASA Data and U.S. Department of Energy sources (references 30–31). This was an intermediate content checkpoint. The former KGEO-01 placeholder was subsequently replaced by 2.15-A, using NASA Goddard's Earth System Diagram with source credit and NASA media-use guidance.

- **Chapter 02, review-question alignment — 4 November 2026:** added matching Russian and English questions on the distinction between energy flow and matter cycling, and on explaining/test­ing cross-sphere causal links. The questions now assess the key concepts introduced in the expanded integrated model.


### Chapter 02 — image-first integration — 4 November 2026

- The initial four-image integration (NOAA atmospheric layers and temperature profile; USGS water distribution and water cycle) was extended to a complete image-first set for all 19 Chapter 02 visual IDs.
- Rights review: both USGS individual media records explicitly state Public Domain. The NOAA page identifies NOAA/JetStream and no third-party credit; NOAA's official reuse guidance states that NOAA content is generally public domain unless otherwise credited and requests NOAA attribution.
- Scientific captions preserve the key limits: water-distribution percentages trace to Shiklomanov (1993), while the USGS 2022 water-cycle diagram includes human water use and water-quality effects. Atmospheric heights/profile are presented as approximate/representative.
- Final inventory: 40 Markdown image embeds, 20 unique assets (nine remote images and 11 local SVGs). All 40 embeds have non-empty bilingual alt text; live loading, page performance, responsive behavior and accessibility remain untested. No deployment test is claimed.


### Chapter 02 — additional source-linked visuals — 4 November 2026

- NASA Goddard's Earth System Diagram was moved from a supplementary position near 2-A to 2.15-A, where it serves as the integrated-system summary. The four-sphere model remains represented by the original 2-A diagram. NASA credit, designer and educational-use guidance are recorded.
- Added the existing My NASA Data carbon-cycle image (adapted from U.S. DOE), the My NASA Data/NCAR nitrogen-cycle image (nonprofit/media reuse note confirmed at the original NCAR page), and the Wikimedia phosphorus-cycle image (CC0 1.0). Each caption records its source and credit.
- The three-cycle illustration set is complete: carbon, nitrogen and phosphorus are all represented with sourced images; the 2.10-B nitrogen and phosphorus images are paired in both language sections.
- These source images are remotely hosted. No local binary copies, live-site rendering tests, mobile performance checks or accessibility validation are claimed.

## Chapters 06, 08–10 — third focused follow-up — 5 November 2026

- **Chapter 06:** added a mass-conservation formulation for catchment water budgets in both languages; distinguished the general inflow/outflow/storage balance from the simplified natural-catchment equation and added a USDA Forest Service methodology source.
- **Chapter 08:** clarified that O/A/E/B/C/R profile labels are a simplified morphological scheme, not a formal WRB classification key or a universal sequence. WRB 4th edition (2022; corrected 2024) remains the classification reference.
- **Chapter 09:** added formulas for natural-change and net-migration rates per 1,000 average residents, plus the exponential annual population-growth formula used by international datasets where applicable. Added UN Population Division metadata as a source.
- **Chapter 10:** clarified that cartographic generalisation on small-scale maps is not a legal boundary record; added a caution against inferring river/lake boundary status from current shorelines or satellite imagery.
- **Progress remains 73% for each of Chapters 06–10.** This pass closes selected scientific/terminological points only. Visual assets remain scheduled for the next work session; complete claim-to-source mapping and final sentence-level RU/EN proofreading remain open. Browser/device/deployment QA remains separate.
- Commit references: Chapters 06 `207f09f`, `93811b5`; 08 `f56dac3`; 09 `8f192a4`, `7a82a55`; 10 `468d576`; source register `fb1cb53`.

- **Chapter 07 additional correction:** distinguished traditional climate/vegetation-based biome maps from the IUCN Global Ecosystem Typology's six-level, function-aware hierarchy; clarified that the frameworks complement but do not replace one another. Added the IUCN GET 2.0 reference. Commit: `15fa5a4`.

- **Chapter 06 final consistency note:** clarified the assumptions behind the simplified catchment-balance example and made the English/Russian explanation consistent about groundwater exchange and external transfers. Commit: `adcb611` (source-register follow-up `2a56c83`).


### Chapter 06 — catchment accounting clarification — 5 November 2026

- Refined the Russian and English water-budget explanation to distinguish external inflows/outflows from internal water withdrawals and return flows. Clarified that an in-basin reservoir belongs to the storage term (ΔS), preventing double counting as a separate inflow/outflow. Added explicit examples of boundary-crossing fluxes and clarified when abstraction is a net loss from the selected catchment control volume.
- This is a targeted conceptual correction, not a full source-by-source or bilingual line-by-line sign-off. Visual production and technical QA remain separate.
- Commit: `59c525339d8b00dcedd08cb26a733ed1fa6b3ebf`.


### Chapters 06–10 — focused bilingual corrections — 5 November 2026

A further targeted correction pass was committed across all five chapters: catchment control-volume accounting (06), restoration-target interpretation (07), interpretation limits of electrical conductivity (08), migration-flow counting units (09), and contiguous-zone measurement geometry (10). The paired RU/EN passages were updated together. Detailed commit references are recorded in `geography/SOURCE_EVIDENCE_CLOSURE_REGISTER.md`. **The chapter scores remain 73% each**: the corrections improve specific concepts but do not close the remaining source-to-claim audit, full bilingual line edit, planned visual integration, or release QA. No 80% milestone is claimed on this evidence alone.


### Chapter 06 — unit consistency follow-up — 5 November 2026

- The worked catchment-balance example now explicitly states that outlet discharge is converted to runoff depth over the catchment area before it is compared with precipitation and evapotranspiration. Russian and English wording are paired; the arithmetic remains 600 − 350 − 220 = 30 mm.
- This closes one dimensional-consistency ambiguity in the exercise, but does not by itself justify changing the Chapter 06 score. The existing 73% remains pending broader source-to-claim review, full bilingual line editing, visual integration and release QA.
- Commit: `884fbdeeac9d07d6791a4bb172f66918a275198b`.


### Chapters 06 and 10 — focused follow-up — 5 November 2026

- **Chapter 06:** made the basin practical assignment internally continuous: the mean-discharge calculation now uses the 2.5 km³ runoff volume derived from 250 mm over 10,000 km², yielding approximately 79.3 m³/s over a 365-day year. Russian and English steps and worked calculations are aligned. Commit: `3c2f61d1cca4add4f68974f7ca18edc374b2a23f`.
- **Chapter 10:** strengthened the statehood and recognition explanation in both languages with the Montevideo Convention's four often-cited qualifications, its Article 3 position, the Convention's regional scope, and a concise distinction between declaratory and constitutive approaches without presenting either as a complete mechanical test. Added a treaty source and current scholarly reference. Commit: `6edda39164e53fbc7f68380135cd27d42c26bdde`.
- These are substantive improvements to pedagogical coherence and legal accuracy. Chapter scores are not changed by this note; reassessment remains conditional on the complete rubric, not on the number of commits.


### Chapter 07 — IUCN guidance reference update — 5 November 2026

- Added the IUCN Red List Guidelines, Version 16 (March 2024), alongside the 2012 Categories and Criteria standard, so the chapter distinguishes the core category framework from current application guidance. Commit: `bb8dbba6a65c311b56902b171c6d538f12b96ac1`.


### Chapter 09 — urban/rural classification method — 5 November 2026

- Added a bilingual explanation of the UN Degree of Urbanization methodology (1 km² grid classification followed by classification of smaller spatial units), its first-level classes and its distinction from national legal definitions. Added the direct WUP 2025 methodology-report reference. Commit: `5537ae858eecadda2bec2982ff9bfd7ace2bcdaa`.


### Chapter 09 — WUP 2025 bibliography clean-up — 5 November 2026

- Removed a duplicate WUP 2025 methodology citation and corrected the methodology report publication date to 27 January 2026 using the official UN Population Division record. Commit: `f6615bc9f58bad6693cd87b9f0e8154f19e9c7fd`.


### Chapter 10 — UNCLOS source precision — 5 November 2026

- Added direct official UN links for UNCLOS Part VI (continental shelf) and Part VII (high seas), strengthening traceability for the chapter's legal distinctions between seabed rights, superjacent waters and high-seas freedoms. Commit: `aeecc0a1f4aff9e2f6adfca03c2abfa5ef13f59a`.


### Chapter 07 — CBD Target 2 and Target 3 wording — 5 November 2026

- Matched the bilingual wording to the official CBD guidance, including the distinction between areas under effective restoration (Target 2) and areas effectively conserved and managed (Target 3), plus the monitoring/resourcing and completion-time caveat. Commit: `9adc9ecaaf124cc1b91d0dc22b0a395495ec5a9b`.

- Chapter 07 bibliography now points directly to the CBD's official Target 2 and Target 3 guidance pages. Commit: `33f2c927650531e92e8577480ed9863e3af3ea77`.


### Chapters 06–10 — worked-example arithmetic audit — 5 November 2026

- Independently recomputed the river-discharge and catchment-balance examples (06), energy-transfer examples (07), soil bulk-density/porosity examples (08), demographic ratios and balance examples (09), and nautical-mile and weighted-turnout examples (10). All stated results agree with the calculations. The examples using population and election data are explicitly hypothetical.
- Detailed arithmetic is recorded in the Source and Evidence Closure Register. This closes the arithmetic recheck for the currently included worked examples, not the separate visual or final release QA.


### Chapter 06 — exact global water-distribution source — 5 November 2026

- Replaced reliance on a broad USGS portal alone with the direct USGS page supporting the chapter's 1.386 billion km³ estimate and global water-distribution proportions; retained the portal as a general reference. Bibliography numbering was normalized and verified. Commits: `e4c03dd3c16379cc32f3b113d94e4d659782551e`, `a25f6b5d9fc3ea7ad83733fdfea3565935e254be`.


### Chapters 06–10 — bilingual structure and exercise inventory recheck — 5 November 2026

- Re-ran the RU/EN structural check against the current branch after the latest edits. Main numbered teaching-section headings match exactly: 06 (17/17), 07 (15/15), 08 (15/15), 09 (16/16), 10 (15/15). English heading labels match the bilingual Russian-section heading labels for every numbered main section.
- Review-question counts match in both languages: 06 (16/16), 07 (15/15), 08 (15/15), 09 (15/15), 10 (14/14).
- Practical activity inventories match: 06 (1/1), 07 (4/4), 08 (4/4), 09 (5/5), 10 (5/5).
- This verifies heading, question and activity inventory; it is not a claim that every sentence has passed semantic translation proofreading.


### Chapter 10 — ICJ Statute source-access issue resolved — 5 November 2026

- Replaced the ICJ-hosted Statute URL, which returned HTTP 403, with the official UN full-text Statute page. The new source is part of the UN Charter resource set and provides the complete annexed Statute. Commit: `5f43b92078b7b9f7351dc95b293009e378889555`.


### Chapter 10 — Montevideo Convention source cross-check — 5 November 2026

- Separated treaty text references from treaty metadata by adding the U.S. Department of State and University of Oslo text records plus OAS and UN Treaty Collection metadata records. Articles 1 and 3 were checked against the treaty text. Commit: `f2a8d5c3f3845166700f11be255f1c59280967f4`.


### Chapter 10 — M49 statistical/legal distinction — 5 November 2026

- Added a bilingual statement that UN M49 is a statistical classification and does not establish sovereignty, statehood, recognition or legal boundary lines. Checked against the UN Statistics Division methodology overview. Commit: `cf70c9c4d7875dd643956b11811c9ccc73fb9f0c`.


### Chapter 09 — population-density denominator clarification — 5 November 2026

- Clarified in both languages that population-density comparisons must identify whether the denominator is land area, total area or inhabited area, and must align population, area and reference date. Commit: `63becbe6080cdd4adb21c198686312f02961bf05`.


### Chapter 09 — population-density source definition — 5 November 2026

- Added the direct World Bank EN.POP.DNST indicator reference, whose definition explicitly uses land area as the denominator. This supports the chapter's note on denominator comparability. Commit: `9bc90598c64ad4dc6a75224abf9f604de3d51e1b`.


### Chapter 09 — demographic-rate denominator consistency — 5 November 2026

- Harmonised RU/EN notation and wording for annual demographic rates, using mid-year population as the commonly used approximation to average annual population and retaining a source-method caveat. Updated examples and practical task wording. Commit: `5c1bfc245381922f300ed1758618f7ddf75919d0`.


### Chapter 06 — global water-share distinction corrected — 5 November 2026

- Corrected the bilingual statement to distinguish ocean and sea water (~96.5% of total) from all saline reservoirs combined (~97.5%, including saline groundwater and lakes); freshwater remains ~2.5%. Verified against the direct USGS distribution table. Commit: `1d91a7bc57da482095fb0f5541a6ea1387bcc316`.


### Chapter 06 — IHO standard edition check — 5 November 2026

- Replaced the generic IHO reference with specific publications and editions: S-23, S-44 Edition 6.2.0, S-102 Edition 3.0.0 and S-100 Edition 5.2.1, checked against the current IHO catalogue (last modified 30 October 2026). Commit: `80cd391382cdeceddbb5f048938e904ddab1324c`.


### Chapter 07 — IPBES and IUCN source access — 5 November 2026

- Added the 2023 IPBES invasive-species assessment DOI and updated IUCN bibliography links to the official resource pages for criteria, current guidelines and assessment supporting information. The latter provides the fields needed to cite a species assessment accurately. Commit: `2b3c9e30926342edbc4c8e75800ec41550026171`.


### Chapter 07 — scope of species-status evidence — 5 November 2026

- Confirmed that no named species is assigned an IUCN category in the current chapter. Added a bilingual rule for citing any future named-species case with its scientific name, assessment scope, category/criteria, dates and database version. This narrows the remaining species-evidence task to future case studies rather than an unsupported current claim. Commit: `251f251e8fe4e336db39d3a1e6c1e250a0e6f49b`.


### Chapter 08 — scope of soil-data claims — 5 November 2026

- Added a bilingual note that numerical examples are instructional rather than country-level measurements, and that any future regional maps/measurements require dataset, year, scale, classification system, sampling depth and method. This clarifies the evidence boundary of the current chapter. Commit: `ddbd9df53ed25ad4f15bad1215e81ea7db4d8ea8`.


### Chapter 09 — scope of demographic numerical claims — 5 November 2026

- Confirmed and documented that current numerical examples are hypothetical rather than real country statistics. Added a bilingual rule requiring exact table/indicator, scenario, territory, reference year and extraction date for future factual maps or comparisons. Commit: `4680bc04e9eb002a57d9d52e98ddf7970baab20d`.


### Chapter 10 — scope of current legal claims — 5 November 2026

- Added a bilingual statement that the chapter does not claim current legal status for named disputed territories or pending delimitations. Any future country case study must cite primary legal sources and relevant court/tribunal decisions, with date and geographic scope. Commit: `f73567233ea467c5118c5bc5cd7b9c3ccdab10d2`.


### Chapter 06 — scope of oceanographic data claims — 5 November 2026

- Current numerical global-water claims are tied to the USGS distribution table; salinity/thermodynamic terminology is tied to TEOS-10; ocean/sea classification and hydrographic/bathymetric products are tied to IHO S-23, S-44, S-102 and S-100. The current text does not assert specific trench-depth or mean-depth measurements. Future bathymetry maps require a named survey/product, date, resolution and vertical datum.


### Chapter 09 — World Bank vital-rate metadata — 5 November 2026

- Added direct World Bank metadata links for crude birth and death rate indicators; their definitions support use of mid-year population as the annual denominator. Population-density land-area metadata remains separately cited. Commit: `16649e8552437b4ed962f8f9410125bbd32220b3`.


### Chapter 08 — soil pH measurement comparability — 5 November 2026

- Added a bilingual explanation of the logarithmic pH scale and a protocol caveat for water versus salt extracts and soil-to-solution ratios; comparisons require compatible methods. Commit: `d4650bc368a48150168240b64056d32b879e8372`.


### Chapter 08 — WRB organic horizon coverage — 5 November 2026

- Added H horizon to the bilingual profile description and illustration specification, distinguishing peat/organic material from O horizons. Checked against WRB Fourth Edition 2022, Annex 3 (corrected 2024). Commit: `9bae5672e0a7568f098d1c590d72b72cbb8bfe33`.
