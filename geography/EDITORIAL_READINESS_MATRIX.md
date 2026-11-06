# Atlas of Geography — Editorial Readiness Matrix
**Snapshot:** 6 November 2026  
**Canonical branch:** `workspace/geography`  
**Purpose:** auditable status of the 26 chapters and the remaining work. This matrix deliberately does not invent one overall completion percentage.



## Quantitative chapter progress — 6 November 2026

**Working production score: 82.4% average across all 26 chapters (82% rounded; equal chapter weighting).** This is a progress estimate for the editorial/content-production scope, not a publication-readiness or deployment score. Chapters 01–04 are recorded at 100% in that scope; Chapters 05–26 have been rescored using a weighted rubric: content/structure 30 points; Russian/English development 20; pedagogical apparatus 15; sources/evidence 20; visual integration 15. The 22 rescored chapters average 79.2% (79% rounded), recalculated from the current chapter rows. The bilingual component remains 18/20 for Chapters 11–20: all numbered sections now pass the structural English/Russian word-coverage check, including glossary sections with an explicit English introduction. Two points remain withheld for sentence-level semantic equivalence, terminology consistency and independent proofreading. Other rescored chapters retain their previous bilingual score until equivalent audits are completed. Visual points are proportional to assets actually integrated in chapter text with bilingual labels/captions; briefs and placeholders earn zero. The evidence component reflects the depth of documented source checks, not a full sentence-by-sentence audit.

## Cross-chapter status

| Workstream | Verified status | Remaining work |
|---|---|---|
| Chapter inventory | 26/26 numbered chapters present | None for chapter count |
| Structural audit | 26/26 received an initial structural pass; Chapter 19 subsection-order defect found and corrected on 2 Nov | Final copyedit and depth review |
| Russian/English structure | 26/26 contain substantial Russian and English teaching material; some chapters use parallel blocks, others section-by-section pairs | Full line-by-line translation parity and proofreading |
| Visual planning | Unreconciled: legacy headline 231; chapter inventory rows sum to 283; unique IDs and duplicate aliases not yet reconciled | Reconcile chapter files, in-text markers, production briefs and assets before calculating repository-wide coverage |
| Visual brief language | Bilingual briefs are present across the indexed chapters, but full unique-ID coverage cannot be certified until the 231/283 inventory discrepancy is resolved | Reconcile all IDs and verify RU/EN briefs; then complete design and typesetting |
| Bibliography presence | Reference section present in all 26 chapters; Chapter 09 gap closed | Open and verify every citation against each adjacent claim |
| Bibliography placeholder scan | No explicit TODO/TBD/incomplete DOI/URL instruction found in reference sections | Link availability and source relevance still require review |
| Numbering integrity | No duplicate numbered section identifiers across 26 chapters | Chapter 17 uses the numbered subsection 17.14.1; no duplicate section identifiers found in the current heading scan |
| Repository structure | One active Geography branch: `workspace/geography` | Keep using this branch only |
| Website | Bilingual RU/EN landing-page toggle and 26 chapter links | In-chapter language filter, rendered Markdown reader, accessibility and deployment tests |
| Created and embedded visuals | 56 new local SVG assets have now been integrated in the 5 November tranches: forty-three across Chapters 11–16 and thirteen across Chapters 18–20. Existing visuals 18-J, 19-H, 20-I and 20-K were also re-audited. Chapter 20.6.7 adds one supplementary CC BY 4.0 research figure. Chapter 12-A's local SVG uses a remote Wikimedia relief-map dependency. The repository-wide local/remote asset total remains under reconciliation in VISUAL_ASSET_REGISTER.md. | Final scientific/editorial sign-off and project-licence assignment for original assets; create and integrate the remaining planned visuals; test remote dependencies, deployed accessibility and rendering |

## Chapter-by-chapter matrix

| Ch. | Chapter | Visual IDs | Structure / bilingual pass | Selected source or calculation checks | Priority remaining |
|---:|---|---:|---|---|---|
| 01 | Geography as a Science | 5 | **ChatGPT internal editorial/conceptual review PASS (5 Nov 2026); publication readiness remains subject to technical release QA.** RU/EN text, glossary, map-scale arithmetic, seven-oblast/city distinction, claim-to-source map and all five diagrams checked. Five visual IDs integrated in both languages (10 embeds; 5/5 coverage = 100%). 01-B title corrected to match its actual absolute/relative-location content. | RGS, National Geographic Standards 1 and 3, UN-GGIM, ICA, Longley et al., National Research Council, NSC regional/city publications and quarterly bulletin, USGS projection guidance, Buzzelli (2020), Holt et al. (1996), National Geographic Geo-Inquiry, GeogSage (CC BY 4.0); current spot-checks of RGS, USGS, National Geographic and NSC sources | **Internal content review: 5/5 visuals PASS.** Rights: 01-A/B/C/E PASS on project-owner authority representation; 01-D source/CC BY 4.0 attribution PASS. Static SVG QA 5/5 PASS. **Still untested:** deployed browser/device rendering, keyboard operation and actual screen-reader output; the Pages workflow on this branch deploys only from `main`, so no branch preview is configured; do not report these as passed. ChatGPT review is internal AI review, not independent expert validation. External teacher/expert review is outside this development workflow. |
| 02 | Earth's Geographic Envelope | 19 | **Chapter content and editorial package complete: 100%** (4 Nov 2026). RU/EN scientific copy-edit, dated-value/source verification, bilingual visual integration and static asset/alt-text checks are complete. | Corrected four-component vs five-sphere Earth-system classification; clarified cryosphere/hydrosphere overlap and lithosphere/geosphere relation; confirmed USGS water table is based on Shiklomanov 1993; checked average continental/oceanic crust-thickness values and the greater thickness beneath major collision mountain belts against USGS and 2025 crustal synthesis; clarified that the “about 4 billion years” age applies to rare preserved rocks, not all continental crust, and that oceanic crust is renewed at ridges and recycled at subduction zones; mapped distinct divergent, convergent, collision and transform outcomes; clarified diffuse plate-boundary zones, intraplate earthquakes and limits of a single-factor explanation of plate motion; expanded the bilingual water-cycle explanation to include evapotranspiration, snowmelt, infiltration/percolation, groundwater recharge and discharge, sublimation, temporary storage and human alterations; distinguished resistance, recovery and ecological resilience in RU/EN; clarified that resilience does not require a return to the former state; refined positive/negative feedback definitions and added paired examples with source mapping; replaced an ambiguous cloud-feedback illustration in the worked feedback section with a clearer predator–prey example and cited a 2024 ecological feedback synthesis; added NASA Earth-system spheres, USGS water-cycle and plate-motion, NOAA dry-air composition/carbon-cycle, NASA energy-budget, UNEP nitrogen-cycle, Missouri Extension nitrogen-cycle and Open University phosphorus-cycle references; retained separate NOAA marine-site and WMO global CO₂ series; added English equivalents for subsections 2.14.1–2.14.3, including the worked mountain-catchment example and feedback-recognition activity; planetary-boundary assessment updated to PIK Planetary Health Check 2026 (seven of nine boundaries transgressed; DOI 10.48485/pik.2026.25) | Outside the chapter-completion percentage: school-based trials and community feedback are a separate event, not a completion gate. After deployment, live rendering, responsive/mobile, keyboard and screen-reader checks belong to separate technical release QA; they have not yet been performed. Static image/alt-text checks and source-image fetch checks are complete; live rendering and assistive-technology behaviour are not yet verified. Chapter 02 has 19 unique visual IDs and all 19 now have integrated imagery or original diagrams. The missing 2.10-A and 2.10-B visuals now use existing My NASA Data/DOE carbon-cycle, My NASA Data/NCAR nitrogen-cycle and Wikimedia Commons phosphorus-cycle (CC0 1.0) images; 2.15-A uses the existing NASA Earth System Diagram as the integrated summary. These established science visuals were preferred to newly created replacements in line with the image-first policy. The 2.13-A provisional Nature Data Lab JPEG was replaced on 4 November 2026 with Figure 10 from Theobald et al. (2025), “Global extent and change in human modification of terrestrial ecosystems from 1990 to 2022”, *Scientific Data* 12, Article 606, DOI 10.1038/s41597-025-04892-2. The article's Rights and permissions statement applies CC BY 4.0 to article images unless a separate credit line states otherwise; no separate restrictive credit line appears for Figure 10. The replacement figure depicts the 2022 cumulative human-modification map at 300 m resolution; Antarctica is excluded. Attribution, DOI, licence link and no-changes statement are included in the chapter. There are 40 Markdown image embeds representing 20 unique assets: nine remote images and eleven original bilingual SVG diagrams; the 2026 planetary-boundaries SVG is intentionally embedded in both language sections. All 40 Markdown image embeds have non-empty bilingual alt text; all 11 local SVGs include title, description and role=img metadata. The new 2.14-A original bilingual SVG reports the 2026 assessment (7/9 transgressed) and cites PBScience/PIK, DOI 10.48485/pik.2026.25. Browser image checks rendered NASA, both NOAA images, USGS water distribution, both My NASA Data diagrams, the USGS water-cycle image (after replacing its inaccessible original CDN URL with the verified full-width image endpoint), and the Wikimedia phosphorus-cycle image (original file and CC0 licence verified on Commons). The replacement Figure 10 image from Scientific Data was opened and visually verified in the browser; the article-level CC BY 4.0 terms and absence of a separate restrictive credit line for Figure 10 were checked. GitHub-hosted SVG is committed but no deployed site URL or deployment workflow is established in this branch; live-site, mobile-device and screen-reader tests therefore remain outstanding. |
| 03 | Lithosphere and Geological Processes | 13 | Text audit complete (100%). All 13 visual IDs now integrated in RU/EN: ten original bilingual SVGs plus three sourced images (USGS minerals, USGS I-2800 plate map, ICS chart 2026/06). No visual placeholders remain. | References include USGS, BGS, ICS 2026/06, Halla et al. (2024), USGS OFR 94-636 and USGS I-2800. | Remaining: final scientific/editorial artwork sign-off, visual/layout review, and separate browser/device/accessibility/deployment QA. These technical tests are not claimed complete.
| 04 | Earth's Landforms and Relief | 16 | Text audit complete (100%). All 16 visual IDs now integrated in RU/EN as bilingual SVGs, including coastal/ocean-floor relief, slope processes, weathering, DEM/DSM/DTM, vertical extremes and a topographic exercise with worked gradient key. No visual placeholders remain. | Bibliography includes Fujii et al. (2026) Challenger Deep multibeam study, distinguishing its preferred 10,927 m gridded estimate from the 2021 pressure-based 10,935 ± 6 m estimate; USGS supports map-reading guidance. | Remaining: final scientific/editorial artwork and exercise sign-off, visual/layout review, and separate browser/device/accessibility/deployment QA. These technical tests are not claimed complete.
| 05 | Atmosphere and Climatology | 19 | **100% — editorial/content-production package complete (6 Nov 2026).** RU/EN text, scientific explanations, worked calculations, learning apparatus and all 19 unique visual IDs are complete; all 19 IDs are represented in both language sections (46 total Markdown image embeds across 23 distinct URLs; grouped ID 5.8-A contains multiple source images). The former missing needs 5.10-A (climate controls) and 5.13-A (urban microclimate/heat island) are now original bilingual SVGs with source-backed captions and alt text. The 5.18-A synoptic/climate exercise was corrected so graph bars match the monthly table (A 364 mm; B 925 mm). Legacy 5-A is an alias for 5.2-A, not a separate visual. | NOAA marine-surface 2025 preliminary mean (425.62 ppm) distinguished from WMO GAW global surface mean (426.8 ± 0.2 ppm); WMO-No. 1203 (2017), WMO-No. 1245 (2020) homogenisation guidance, 1991–2020 operational normal vs fixed 1961–1990 reference period, 6.5°C/km ISA model lapse rate vs variable observed lapse rate, relative-humidity definition/formula, WMO cloud genera, liquid droplets/ice/supercooled water, NOAA/WMO front definitions and types, NOAA climate controls, EPA urban heat-island mechanisms, Köppen–Geiger map methodology, tropical-cyclone formation, drought/heatwave definitions, fog/dust, solid precipitation and urban heat islands. Worked example: 377 mm annual precipitation; 29°C annual temperature range. Climate graph data: A 364 mm/32°C; B 925 mm/14°C. All 12 local SVGs pass static structure checks; 46 Markdown embeds have non-empty alt text and RU/EN URL parity. | **Editorial scope: 100%.** Rights: owner-authorised CC BY-NC 4.0 for the 11 original SVGs; adapted 5.7-B is separately attributed and shared under CC BY-SA 4.0. Automated technical acceptance PASS on 6 Nov 2026 (GitHub Actions run 42209245792): 46/46 bilingual embeds, 12/12 local SVG XML/ARIA checks, exact 11-file licence scope, seven unchanged NOAA mirrors, 46/46 images decoded in the actual GitHub Markdown view at 390 px and 1365 px, no horizontal overflow, isolated preview axe WCAG 2.1 A/AA scan 0 violations and keyboard skip-link PASS. Remaining human release gates: screen-reader session, human contrast/legibility review of text embedded in SVG artwork, and testing on the eventual deployed Atlas reader/site. This is not a claim that a production reader has been deployed or tested. |
| 06 | Hydrosphere and World Ocean | 15 | **95%** — RU/EN sentence-level scientific/editorial pass and source-to-claim sweep closed; worked calculations checked; **15/15 unique visual IDs integrated in both languages** (32 Markdown embeds across 16 distinct image targets; 6.7-A intentionally has two visual targets). Eight new bilingual SVGs added 6 Nov and basic SVG structural metadata/non-empty alt text checked. | USGS global water distribution and water-cycle references; NOAA surface-current map; Wikimedia Commons five-ocean map (Pinpin / Wikigraphists, CC BY-SA 3.0); separate Flanders Marine Institute dataset candidate not used; IHO S-23 status; TEOS-10; NSIDC sea ice; USDA catchment water-budget guidance. RU/EN terminology and worked calculations aligned. | Remaining 5% is release verification, not missing chapter text or missing visual IDs: confirm project rights/licences for original SVGs; final cartographic review of the Commons ocean-boundary convention map; inspect rendered labels/contrast and screen-reader output; run browser/mobile and deployed-site QA. A precise GIS-derived ocean-boundary map remains a possible enhancement, not represented as complete. |
| 07 | Biosphere and Natural Biomes | 9 | **85%** — RU/EN scientific and sentence-level editorial pass and focused source-to-claim sweep completed; key conceptual corrections integrated; 0/9 visual assets integrated | CBD official wording for GBF Targets 2–3; IUCN Global Ecosystem Typology six-level hierarchy; IUCN Red List 2026-1 (9 July 2026); SER restoration standards Third Edition (2026); NCBI molecular-biology reference for O₂ source in photosynthesis; 2026 eDNA methods review; existing IPBES, UNESCO, Olson et al. and Millennium Assessment sources retained | Create/integrate nine visuals; then complete figure/source licensing review, layout/rendering, browser/mobile/accessibility and deployment QA. Any future named species-status example must cite the individual dated IUCN assessment, scope, category and criteria |
| 08 | Soils and Landscape Geography | 7 | **78%** — RU/EN структура выровнена; тематическая построчная вычитка и проверка ключевых научных утверждений выполнены; 0/7 визуалов интегрировано | WRB 4th ed. (2022; corrected 2024): 32 RSGs and qualifier-based naming; master horizons distinguished from classification key; SoilGrids 2.0: 250 m grid cells, six depth intervals, 90% prediction intervals (Q05–Q95), Central Asian data gaps; UNCCD Article 1 desertification definition; FAO/ITPS 2026 global and Europe/Central Asia assessments; ECe versus other extract ratios and field apparent EC; salinity versus sodicity; pH methods; calcification and landscape morphology terminology checked | Final integrated editorial pass after visual production; scientific review of seven generated assets; browser/mobile/accessibility and deployment QA; no country-level soil statistics are asserted without a regional dataset and sampling metadata |
| 09 | Population and Demography | 7 | **90%** — non-visual scientific and editorial work completed for this pass: corrected infant-mortality probability definition; added the five-year-age-group TFR calculation; clarified the population-balance adjustment term and HDI education-index calculation; aligned the English 9.16.1 subsection; checked bilingual headings, summaries, questions, practical tasks, glossary and 18 references. Seven visual assets (09-A–09-G) remain placeholders and are excluded from completion | UN WPP 2024 methodology and indicator metadata; WUP 2025 methodology and Degree of Urbanization thresholds; census Rev.4; UNSD 2025 migration recommendations and 2026 vital statistics; DemoData (updated 3 Nov 2026); WHO infant-mortality definition; IOM WMR 2024; UN-Habitat; World Bank density and crude-rate metadata; UNDP 2025 HDI methodology; UNHCR IDP definition; all chapter arithmetic examples recalculated | Remaining: seven visual assets 09-A–09-G, their scientific review and accessibility text after creation; rendered-site/mobile/browser checks must follow visual integration. No live country statistics or maps were inserted; all numerical exercises remain explicitly hypothetical and real comparisons require indicator, territory, reference date, method/scenario and extraction date |
| 10 | Political Geography | 7 | **85% overall; non-visual scientific/editorial scope 100%** — завершены двуязычная научная и юридико-методологическая вычитка, выравнивание 17 парных учебных заголовков, расширение определений и глоссария, проверка примеров, 16/16 вопросов, 5/5 практических заданий и 20 источников. Все семь визуальных ID 10-A–10-G остаются плейсхолдерами | UN Charter; UNCLOS Parts II, V, VI, VII, X and XI; Montevideo Convention; UN M49; ICJ Statute; UN Watercourses Convention 1997; UNGA Resolution 63/124 on transboundary aquifers; OSCE/ODIHR 2023 election-administration handbook; 2024 recognition-of-states monograph. Clarified maritime-zone baselines, continental-shelf criteria, landlocked-state transit, ICJ consent jurisdiction, electoral-boundary principles, watercourse/aquifer distinctions and GIS aggregation limits | Remaining: create/integrate seven visual assets and complete their scientific, licensing and bilingual alt-text review; then perform rendered-site, mobile, keyboard and screen-reader QA. No named disputed-territory status claims are made; future country cases require dated primary legal instruments and applicable court/tribunal decisions |
| 11 | Economic Geography | 7 | **77%** — структурная проверка RU/EN пройдена (20/20 разделов); добавлены прямые ссылки на ISIC Rev. 5 и СНС 2025; все 7/7 визуалов интегрированы (11-A–11-G) | Location quotient checked; 2025 SNA added alongside 2008 SNA; ISIC Rev. 5 (2024) distinguished from legacy Rev. 4; clarified gross value added/GDP production identity and PPP versus current/constant-price concepts; UNCTAD/UNIDO value-chain sources added; Kyrgyz energy-sector structure and 2025 production/consumption/import figures checked; tourism destination system grounded in UNESCO/UN Tourism guidance | Complete source-to-claim and country-example review; final scientific, rights and accessibility review of all seven visuals |
| 12 | Geography of World Regions | 10 | **74%** — структурная проверка RU/EN пройдена (16/16 разделов); интегрировано 3/10 визуалов (12-A, 12-B, 12-D); 7 визуалов остаются открытыми | M49 statistical grouping distinguished from physical/cultural regionalisation; Oceania subregions aligned with M49; Antarctic Treaty Article IV and Treaty Area scope clarified; Caucasus regional qualification aligned RU/EN; regional-data comparability checklist integrated | Verify regional data dates and map classifications; complete source-to-claim review; create and review seven remaining visual assets |
| 13 | Ecology and Global Change | 11 | **79%** — структурная проверка RU/EN пройдена (18/18 разделов); оценка планетарных границ обновлена до отчёта 2026 года; интегрировано 11/11 визуалов (13-A–13-K), включая четыре новые двуязычные схемы деградации земель, экологического мониторинга, циркулярной экономики и экологической справедливости | Richardson et al. (2023) retained as dated historical assessment; Planetary Health Check 2025/2026 checked; 2026 report (DOI 10.48485/pik.2026.25) reports seven of nine boundaries transgressed; five direct biodiversity-loss drivers aligned with IPBES; IPBES six-element conceptual framework, IPCC observed/projected impact scope and OECD context-dependent adaptation indicators checked; UNCCD land-degradation response hierarchy, EPA environmental QA/QC, Ellen MacArthur technical-cycle concepts and Berkeley environmental-justice mapping methods reviewed; urban example uses fictional data | Full environmental-indicator and source-to-claim proofread; verify dated indicators; complete project licence assignment, independent scientific review, accessibility and browser/device QA for all eleven visuals |
| 14 | Geographic Information Systems | 9 | **76%** — структурная проверка RU/EN пройдена (20/20 разделов); уточнены OGC API и правовые требования к пространственным данным; интегрировано 8/9 визуалов (14-A, 14-B, 14-C, 14-D, 14-E, 14-F, 14-H, 14-I); 14-G остаётся открытым до получения проверенного DEM с разрешением, CRS и метаданными | OGC API – Features and OGC API – Maps added as modern web APIs; Digital Code No. 178 (2025), Chapter 12, Articles 92–98 reviewed; QGIS references support overlay, network service area, topology and reproducible workflows; GDAL geometry-validity limits distinguished from coverage topology; sequential/diverging/qualitative map palettes checked against Scottish Government and QGIS guidance | Software-version and workflow validation; verify dataset-specific horizontal/vertical realization, transformation parameters, metadata and reuse conditions; source a real DEM with known resolution/CRS and integrate slope/aspect derivatives for 14-G |
| 15 | Remote Sensing of the Earth | 11 | **79%** — структурная проверка RU/EN пройдена (18/18 разделов); уточнены Sentinel-1 и Landsat Collection 2 Level-2; интегрировано 11/11 визуалов (15-A–15-K), включая четыре новые схемы классификации/проверки, SAR, LiDAR и многовременного анализа | Sentinel-1A end of operations (30 Jun 2026), Sentinel-1B end of mission (2022), Sentinel-1C/D operational; Landsat C2 L2 surface-reflectance scale factor/offset and QA bands checked; NDVI, NDMI, McFeeters NDWI, NDBI and NBR formulas/band mappings added; NASA remote-sensing principle, spectral signatures, four resolution dimensions and Level-2 correction workflow checked; supervised/unsupervised classification, independent validation, SAR geometry, LiDAR DSM/DTM and multitemporal co-registration checked against USGS, Natural Resources Canada, Google Earth Engine, NEON and open EO teaching resources | Sensor/product metadata and accuracy review; verify local index thresholds and independent validation methods; complete rights assignment, independent scientific review, accessibility and browser/device QA for all eleven visuals |
| 16 | Geographic Research and Cartography | 9 | **82%** — структурная проверка RU/EN пройдена (21/21 разделов); добавлены актуальные источники ICA 2026, USGS, UNSD Rev. 4, Statistics Canada, Ordnance Survey, UCGIS и Roth (2017); интегрировано 9/9 визуалов (16-A–16-I), включая пять новых оригинальных двуязычных схем; Image Coverage 100%, Image Verification 0/9 | Thematic map types, visual variables and classification methods checked against UCGIS GIS&T Body of Knowledge, Penn State GEOG 486, Roth (2017) and Esri guidance; five new SVGs passed static source and embed checks; the Jenks example explicitly marks its class breaks as illustrative, not computed | Full methodology and assessment review; verify sampling/statistical examples; complete project licence assignment, independent scientific review, accessibility and browser/device QA for all nine visuals |
| 17 | Geographic Location and Geological Evolution of Kyrgyzstan | 9 | **85%** — содержательная и структурная проверка расширена; уточнены источники национальных геоданных и статус проекта геологического атласа; выровнены девять визуальных ID и production briefs; 3/9 визуалов интегрировано (Image Coverage 33,3%; Image Verification 0/3, права и техническая проверка ожидают подтверждения); полная построчная RU/EN вычитка не завершена | Corrected area arithmetic; ICS Chart 2026/06; Manas renaming and 2025–2026 border instruments; Kyrgyz AIP WGS 84 scope; national seismic-hazard research; World Bank Central Asia Earthquake Catalogue and Seismic Fault Database metadata/licences (CC BY 4.0) checked; Poggi et al. (2024) regional seismicity context figure reproduced under CC BY 4.0 with scope note; archival 2018 WIS boundary-layer metadata (WGS 84, not legal-currentness); Ministry's 2026 announcement of a planned bilingual national geological atlas; CIA 2005 maps and academic tectonic figures screened but not approved for current map reuse; 2019 administrative classifier has no licence and no boundary geometry; historical Kyrgyzmap/nsdi.kg portal access not confirmed on 5 Nov 2026; AF NWRMP map catalogue inspected (2017 terrain/admin/seismic/geology images, 2022 basin maps), but dated maps and image-specific reuse rights prevent current reuse | Obtain current authoritative boundary and administrative geometries with metadata/licence and a confirmed official portal endpoint; derive verified extreme-point coordinates; inspect transformation/control-point metadata and vertical datum; review the national geological atlas when actually published; confirm rights and metadata for AF NWRMP historical map images before any reuse; inspect World Bank seismic dataset packages and validate clipping boundary/filter before completing 17-F; complete sentence-level RU/EN proofreading; complete the remaining 6 visuals; close rights, scientific, bilingual, accessibility and technical checks for the three integrated SVGs and all subsequent assets |
| 18 | Geology, Mountain Systems and Relief of Kyrgyzstan | 10 | **84%** — структурная проверка RU/EN пройдена (19/19 разделов); обновлён PCGN Factfile 2025; интегрировано 5/10 визуалов (18-B, 18-C, 18-D, 18-H, 18-J); 18-C содержит три фотографии с проверенными индивидуальными лицензиями и двуязычными подписями | Peak heights and country-specific Lenin/Ibn Sina naming checked; incomplete geological citations corrected; DEM vertical-reference guidance added; CAIAG ASTER GDEM 30 m candidate, RESILAND 3 m/14-site procurement, 2026 national geological-atlas project and historical glacier-source limits documented; 18-C photos checked at individual Commons file pages (CC BY-SA 4.0, CC BY 2.0, CC0 1.0) | Obtain licensed/validated DEMs and full CRS/vertical metadata; verify glacier outlines against current imagery; review national geological atlas when published; validate peak heights and map sources; browser/mobile/accessibility test the three remote photographs |
| 19 | Climate and Altitudinal Zonation of Kyrgyzstan | 10 | **75%** — структурная проверка RU/EN пройдена (19/19 разделов); климатические ряды и различия 22- и 13-станционных наборов документированы; интегрировано 6/10 визуалов (19-C, 19-D, 19-E, 19-F, 19-H, 19-J); 4 визуала, включая карты климатических полей, остаются открытыми | UNEP +1.2°C 1960–2023 estimate cross-checked with Kyrgyzhydromet: 22 homogenised stations (1980–2021), +0.28°C/decade countrywide; official seasonal trend chart integrated (annual +0.28, spring +0.59°C/decade); source table period ambiguity (1981–2020 vs narrative 1981–2021) explicitly flagged; separate 13-station climate indices (1980–2022); seasonal circulation sources and adaptation sectors checked | Obtain station-level series/metadata; resolve source period discrepancy; reconcile climate-normal periods; validate high-mountain spatial interpolation and future projections; create four remaining visual assets |
| 20 | Glaciers, Rivers, Lakes and Water Resources of Kyrgyzstan | 11 | **82%** — структурная проверка RU/EN пройдена (19/19 разделов); проверены данные НСК 2025 и современные исследования озёр; интегрировано 8/11 визуалов (20-C, 20-D, 20-E, 20-F, 20-H, 20-I, 20-J, 20-K) плюс отдельная карта исследования 2019 года CC BY 4.0; 3 визуала остаются открытыми | River-runoff range, renewable water resources, glacier mass balance, Chu–Talas transfer and Issyk-Kul morphometry checked; 2025 EGU inventory reports >2,000 lakes; 2026 EGUsphere preprint reports 2,592 lakes / 77.6 km² in 2024 (10 m Sentinel-2; preprint status and comparability caveat added); separate peer-reviewed 2026 Kyrgyz Range study quantifies lake/glacier change 1968–2021; NSC 2025 water-use indicators and WIS scope documented; CAIAG/President/AF NWRMP lake-area sources checked; AF NWRMP confirms five Lower Naryn HPPs and 2,870 MW aggregate installed capacity; UNH historical Naryn gauge candidate (station 16055, 1931–2006, mean 92.117 m³/s) identified, but raw values and reuse terms remain unconfirmed; UNECE and CAWater-Info sources support the Chu–Talas coordination schematic | Obtain/verify lake polygons, thresholds and reuse rights; obtain station-level discharge series and metadata (UNH station 16055 candidate requires raw values/licence); validate basin/reservoir records, current glacier outlines and GLOF hazard layers; complete the full lake morphometry map and remaining three visuals; inspect hazard-atlas map scale, legend and layer licensing |
| 21 | Flora and Fauna of Kyrgyzstan | 10 | **71%** — основной RU/EN текст и учебный аппарат готовы; выполнена адресная проверка национального Красного списка и оценок снежного барса; 0/10 визуалов интегрировано | VNR 2025: 87 высших растений и грибов; сообщение Минприроды 2026: 89 (расхождение не объяснено); обновление Красной книги запущено в 2026 году, выпуск планируется в 2028-м. PASK 2020–2024: около 300 взрослых особей (95% ДИ 246–366); публичные заявления Минприроды 2026: 500–550/свыше 550 — методики и единицы учёта недостаточно раскрыты для прямого сравнения | Полная таксономическая и популяционная проверка; проверка чувствительных местообитаний; визуалы и их научное утверждение |
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

1. Continue source-by-source review of Chapters 01–26, including dated data and bibliographic relevance. Targeted checks are now recorded for Chapters 01–16, with uneven depth and no claim of exhaustive claim-by-claim verification; see the current milestone in `geography/SOURCE_EVIDENCE_CLOSURE_REGISTER.md` (5 Nov 2026). Next block: Chapters 17–21.
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
- The earlier figure of 9 for Chapter 02 was an undercount caused by counting only a subset of the placeholder naming patterns. The repository-wide cross-check confirms **19** Chapter 02 IDs and 231 unique IDs across all 26 chapters; all 19 Chapter 02 IDs now have integrated imagery in both language versions.
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


- Bilingual QA after the H-horizon addition caught and corrected a duplicated English symbol and aligned the classification caveat. The RU/EN lists now match and explicitly distinguish master horizon/layer designations from WRB diagnostic criteria. Commits: `616affb021a9729a8355d51048a622348f3547f8`, `6727ea73c466ab38ed0b9b192c67cfee6ae856c3`.


### Chapter 07 — GBF Target 3 geographic scope — 5 November 2026

- Added the distinction that Target 3's 30% objective is global, not an automatic quota for 30% of every country's territory. RU/EN wording also retains the distinction between effective conservation and strict protection. Commit: `44e95d29e79d5b8731c94ffd4a568c92e593b66a`.


- Clarified that GBF Target 2 is a global objective measured against degraded ecosystem areas, not a 30% restoration quota for every country's total territory. RU/EN distinction between Targets 2 and 3 now explicit. Commit: `d8892146b1d3d58a8bcd6bfc4e9c46d18a08802e`.


### Chapter 09 — WUP 2025 Degree of Urbanization thresholds — 5 November 2026

- Added the level-1 grid-density and cluster-population thresholds for cities and towns/semi-dense areas in RU/EN; explicitly labelled them WUP 2025 statistical thresholds rather than national legal definitions. Checked against the 2025 methodology report. Commit: `e459800f4a7d7aa04a0cc9659b93048136858ca7`.


### Chapter 06 — Southern Ocean boundary status — 5 November 2026

- Clarified that 60°S is commonly used but not a universally adopted IHO boundary; official S-23 remains the 1953 edition and the 2002 fourth-edition draft was not approved. Added direct IHO source and updated both languages. Commit: `57e0739a6893b2377a05e2f7b1055c066f54f5e9`.


- Added the NOAA National Ocean Service explainer alongside the IHO draft to substantiate the five-ocean convention and the non-ratification caveat for the Southern Ocean boundary. Commit: `b32e9ece268f789c95f322d343e32e68236e4a5d`.


### Chapter 09 — WUP 2025 grid-level implementation nuance — 5 November 2026

- Clarified that the full Degree of Urbanization method has two stages, while WUP 2025's global dataset relies primarily on 1 km² grid classifications due the lack of an open worldwide small-unit boundary dataset. Checked against Box II.2 of the WUP 2025 methodology report. Commit: `12d32b88bbdf4f14f9be1eddeb927897c7daacc8`.


### Chapter 10 — UNCLOS Area versus high seas — 5 November 2026

- Added the missing distinction between the Area (seabed/subsoil beyond national jurisdiction) and high seas (water column), including the common-heritage principle and Article 135's separation of the status of overlying waters. Official UN Part XI sources added. Commit: `c2412eed3ab7f6fb6f1acc6d8d0baf6b452fdcda`.


- Updated the maritime-zones visual specification to distinguish the Area seabed from the high-seas water column and added English production instructions, maintaining bilingual asset requirements. Commit: `aef5597993c6f40abad063be6574fa489f23870b`.


### Chapter 07 — IUCN Red List release date check — 5 November 2026

- Updated the dynamic Red List source to version 2026-1 (published 9 July 2026), the latest available release on the audit date; the planned 2026-2 release is not yet published. Added IUCN's official update-history page. Commit: `25ed8d2b4929f6b02e15eb4955a322b4890a2cd7`.


### Chapter 09 — current UN vital-statistics source — 5 November 2026

- Added the 2026 UN Population and Vital Statistics Report as a source for current national estimates and vital-event data; the UNSD page showed Tables 2 and 3 updated 5 October 2026. Commit: `4c51e53870866cd5a6be2476228ec4151af5c82c`.


### Chapter 10 — bilingual visual production briefs — 5 November 2026

- Added English counterparts for the six figure-production specifications in Chapter 10, including the maritime-zones distinction. Visuals remain deferred and no image integration is claimed. Commit: `75fee48be53b237ed9fd78e8b2b79acbd19f5725`.


### Chapter 09 — bilingual visual production briefs — 5 November 2026

- Added English production instructions for all six figure briefs, matching the Russian requirements for data provenance, schematic status, scales and boundaries. Images remain deferred. Commit: `a600bebbc6a9ba290accf03ab9a6006a0f49ce9f`.


### Chapter 08 — bilingual visual production briefs — 5 November 2026

- Added English counterparts for all seven visual production briefs, including the revised H–O–A–E–B–C–R soil profile and the distinction between structural and functional landscape connectivity. Visual integration remains deferred. Commit: `b2e366f31e5af78e547a274278264a7eb1634718`.


### Chapter 07 — bilingual visual production briefs — 5 November 2026

- Added English counterparts for all nine visual specifications, preserving conceptual-model caveats, flow/stock distinctions and regional ecological variation. Visual integration remains deferred. Commit: `1452297ed18f0554cdf831bbebc4d238d72e8a33`.


### Chapter 06 — bilingual visual production briefs — 5 November 2026

- Added English production counterparts for all four registered visual IDs, including the hydrological flux/stock distinction and Southern Ocean boundary caveat. Images remain deferred. Commit: `4282a32dd93779c6635027748584c3d5ed686ca2`.


### Chapter 06 — visual ID reconciliation — 5 November 2026

- Corrected the visual inventory from four to 15 unique Chapter 06 assets. Eleven additional figure concepts received bilingual in-text markers; four redundant figure aliases were normalised to the existing core IDs. The geography-wide visual register now contains 231 unique IDs rather than 220. All Chapter 06 visuals remain uncreated placeholders and do not earn integration points. Register commit: `1bd3a384212a6ae893834e6ba5a748d30887dff4`.


- Added a bilingual production specification for visual ID 10-A (world political map), including dated source data, projection, scale, boundary provenance and neutral treatment of disputed territories. Commit: `ea7107c8b2c927b14927568e0e71539afd34dd82`.


### Chapters 06–10 — visual marker and brief parity QA — 5 November 2026

- Verified exact bilingual production-brief parity against the stable visual IDs: Ch06 15/15, Ch07 9/9, Ch08 7/7, Ch09 6/6 and Ch10 7/7. Duplicate Chapter 06 aliases were removed and Chapter 10's missing world political map brief was added. All remain placeholders; no image integration is claimed.


### Chapters 06–10 — English-copy worked-example parity — 5 November 2026

- Added the missing worked examples and methods subsections to the standalone English chapter copies: Ch06 6.13.1/6.17.1; Ch07 7.4.1/7.15.1; Ch08 8.4.1/8.15.1; Ch09 9.8.1/9.16.1; Ch10 10.5.1/10.15.1. Rechecked numbered teaching-heading parity: zero missing or extra IDs across all five chapters (29, 17, 17, 18 and 17 matched headings). This closes a structural bilingual gap, but does not replace sentence-level translation proofreading.


### Chapter 06 — bilingual key-term glossary — 5 November 2026

- Added a bilingual list of 25 key terms spanning hydrology, oceanography, groundwater and water scarcity to strengthen the chapter's independent study and review apparatus. Commit: `f827509fd7b9bba5c2d7ff441017fab4cd66a708`.


- Extended the Chapter 10 bilingual glossary with baseline, contiguous zone, the Area and high seas so the new UNCLOS distinction is reflected in the review vocabulary. Commit: `bb34acbf677af3a78ccffaa4d4ca30ebb195a6d4`.


- Aligned the bilingual review question with the revised WRB profile description by including H alongside O, A, E, B, C and R. Commit: `0b0bde34740ed99d720cfa54ece4080e83c81e91`.


- Aligned the RU/EN review questions in Ch06 and Ch10 with the corrected ocean-boundary and UNCLOS maritime-zone content; the Ch10 question now explicitly distinguishes the Area from the high seas. Commits: `7c616f8cb2ea1fe3adb40286162897b37ff00eb7`, `e7f0577ac6598b0a9147a3a77d646878451d2d59`.


- Updated the Chapter 08 key-term list with H/O organic horizons and ECe, aligning the glossary with the WRB and salinity-method refinements. Commit: `3cf71c280f48410c92a0ddd3f9c4f818c861d3d9`.


- Added migration flow/stock, mid-year population and Degree of Urbanization to the Chapter 09 bilingual glossary. Commit: `67146954a2dd5e87a3ee03ca5d700b6f274756ba`.

## Consolidated chapter findings log — Chapters 06–10 — 5 November 2026

| Chapter | Findings documented and integrated | Verified visual brief parity | Structural RU/EN heading parity |
|---|---|---:|---:|
| 06 Hydrosphere and World Ocean | Runoff-depth unit consistency; catchment storage/residual; Southern Ocean classification caveat; glossary/review alignment | 15/15 | 29/29 |
| 07 Biosphere and Natural Biomes | Trophic transfer not a universal 10% rule; GBF Target 2 interpretation; outcome-based restoration monitoring | 9/9 | 17/17 |
| 08 Soils and Landscape Geography | WRB H/O horizons; porosity estimate assumptions; ECe versus 1:5/field EC; salinity versus sodicity | 7/7 | 17/17 |
| 09 Population and Demography | Migration flow versus stock/event counts; worked rate calculation; dependency ratio interpretation; urban classification comparability | 6/6 | 18/18 |
| 10 Political Geography | Maritime distances from baselines; legal status of maritime zones; boundary cartography and disputed-status neutrality | 7/7 | 17/17 |

- Each chapter now contains its own focused audit record with findings and integration status. The detailed chapter commits are recorded in `SOURCE_EVIDENCE_CLOSURE_REGISTER.md`.
- Heading parity and visual-brief parity are structural checks only. They do not constitute complete sentence-level translation proofreading, source-to-claim closure, image creation or release QA.
- **Progress scores remain unchanged** pending closure of those remaining tasks. Do not treat audit-log documentation or placeholder briefs as completed visual integration.


## Chapter 01 — final internal reconciliation and visual reflow — 5 November 2026

- The earlier 4 November inventory notes that Chapter 01 visual briefs had not yet been integrated are historical and are superseded by this update.
- All five planned visual IDs (01-A–01-E) are now integrated in both Russian and English chapter sections: 10 image embeds, five unique local SVG files, Image Coverage 5/5 (100%).
- The five SVGs were re-composed with portrait-oriented viewBoxes and larger bilingual labels to improve readability at narrow screen widths. Static source QA passed for all five: SVG root, viewBox, balanced/nested tags, unique IDs, valid ARIA label references, bilingual metadata/text and closing SVG element; no script, foreignObject or externally linked image content was found. Browser/device rendering and assistive-technology output remain untested.
- Chapter text reconciliation also completed: learning objectives now appear in both languages; the English heading for section 1.10.2 is explicit; the scale worked example has self-check answers in both languages; the 01-C alternative text now accurately groups interpretation and communication as the sixth stage.
- Internal ChatGPT review: PASS for all five visuals (5/5), recorded in IMAGE_AUDIT.md. Rights: 01-D PASS under CC BY 4.0 with attribution and changes disclosed; 01-A, 01-B, 01-C and 01-E have owner-confirmed authority to apply CC BY-NC 4.0 (owner representation; attribution: Atlas of Knowledge project). Provenance and AI-review method are documented.
- Accessibility and technical verification remain PARTIAL until rendered browser/device, keyboard and assistive-technology checks can be performed. Do not call these tests passed or mark the assets independently VERIFIED.
- No external teacher review or independent expert assessment was performed or included in this development stage.


### Chapter 01 verification-level clarification — project-owner instruction, 5 November 2026

For Chapter 01, the project owner explicitly defined internal review as review by ChatGPT. ChatGPT GPT-6 completed and documented the conceptual/pedagogical review of 01-A–01-E on 5 November 2026. This is the project's designated internal AI review, not independent human or external expert validation. Browser/device rendering, keyboard operation and actual screen-reader output remain separate technical checks and are not claimed as complete. This chapter-specific instruction does not change the review records or requirements for other chapters.


### Chapter 01 — licence authority confirmation — 5 November 2026

The project owner confirmed on 5 Nov 2026 that they or an authorised project organisation have authority to act as licensor and apply CC BY-NC 4.0 to 01-A, 01-B, 01-C and 01-E. Rights status is PASS on the basis of this owner representation (not an independent legal opinion); attribution: Atlas of Knowledge project. 01-D retains its separate source CC BY 4.0.
