# Atlas of Geography — Editorial Readiness Matrix
**Snapshot:** 2 November 2026  
**Canonical branch:** `workspace/geography`  
**Purpose:** auditable status of the 26 chapters and the remaining work. This matrix deliberately does not invent one overall completion percentage.

## Cross-chapter status

| Workstream | Verified status | Remaining work |
|---|---|---|
| Chapter inventory | 26/26 numbered chapters present | None for chapter count |
| Structural audit | 26/26 received an initial structural pass; Chapter 19 subsection-order defect found and corrected on 2 Nov | Final copyedit and depth review |
| Russian/English structure | 26/26 contain substantial Russian and English teaching material; some chapters use parallel blocks, others section-by-section pairs | Full line-by-line translation parity and proofreading |
| Visual planning | 217/217 unique IDs indexed | Create, label, source-check and approve each asset |
| Visual brief language | 217/217 IDs have Russian and English production instructions | Final design and typesetting |
| Bibliography presence | Reference section present in all 26 chapters; Chapter 09 gap closed | Open and verify every citation against each adjacent claim |
| Bibliography placeholder scan | No explicit TODO/TBD/incomplete DOI/URL instruction found in reference sections | Link availability and source relevance still require review |
| Numbering integrity | No duplicate numbered section identifiers across 26 chapters | Normalise Chapter 17's distinct label 17.14а during final style pass |
| Repository structure | One active Geography branch: `workspace/geography` | Keep using this branch only |
| Website | Bilingual RU/EN landing-page toggle and 26 chapter links | In-chapter language filter, rendered Markdown reader, accessibility and deployment tests |
| Generated visuals | 4 SVG assets created and embedded; all 4 pending final scientific/editorial sign-off | Scientific, source, bilingual and accessibility review; further production |

## Chapter-by-chapter matrix

| Ch. | Chapter | Visual IDs | Structure / bilingual pass | Selected source or calculation checks | Priority remaining |
|---:|---|---:|---|---|---|
| 01 | Geography as a Science | 3 | Initial bilingual pass; English Key Terms table added 2 Nov | Map-scale example; AAG, RGS and UN-GGIM links refreshed; ICA source still to be confirmed | Verify all references and complete final bilingual prose proofread |
| 02 | Earth's Geographic Envelope | 4 | Initial structural/bilingual pass; targeted science check 2 Nov | NOAA 2025 CO₂ series verified against WMO's distinct 426.8 ppm series; USGS water-reservoir table corrected to separate fresh and saline groundwater; atmospheric-layer ranges and dry-air trace-gas wording checked against NOAA | Full source-by-source review of remaining Earth-system, geological, biogeochemical and planetary-boundary claims; final RU/EN prose proofread |
| 03 | Lithosphere and Geological Processes | 4 | Initial structural/bilingual pass; English seismic-location and worked-example parity added 2 Nov | USGS interior/plate-motion references, NPS mineral properties, IRIS epicentre lesson and ICS 2026/06 timescale checked; hypocentre wording corrected; age rounded to ~4.57 Ga | Claim-by-claim review of volcanism, structures, geochronology, resources and hazards; final RU/EN proofread |
| 04 | Earth's Landforms and Relief | 4 | Complete | Slope example recalculated; USGS/NASA/ETOPO/OpenTopography/BGS references | DEM and geomorphology data validation |
| 05 | Atmosphere and Climatology | 4 | Complete | CO₂ updated to NOAA 2025 mean; WMO series distinction | Full climate-data proofread |
| 06 | Hydrosphere and World Ocean | 4 | Complete | Water-balance, runoff-volume and discharge calculations checked; bilingual catchment task added | Full ocean and hydrological source review |
| 07 | Biosphere and Natural Biomes | 9 | Complete | CBD, IPBES, IUCN, UNESCO and ecoregion references linked | Full taxonomic and classification review |
| 08 | Soils and Landscape Geography | 7 | Complete | WRB 2022 corrected 2024; FAO/ITPS 2026 global soil assessment added; porosity example checked | Full soil-data and terminology review |
| 09 | Population and Demography | 6 | Complete | Dependency-ratio example checked; missing bibliography added (8 authoritative sources) | Verify any remaining global series and final proofread |
| 10 | Political Geography | 7 | Complete | UNCLOS distance conversions and weighted turnout example checked; legal references linked | Legal interpretation and case-study review |
| 11 | Economic Geography | 7 | Complete | Location quotient checked; 2025 SNA added alongside 2008 SNA; core data references linked | Update and verify any country examples |
| 12 | Geography of World Regions | 10 | Complete | M49 statistical grouping source linked; regional references refreshed | Check regional data dates and map classifications |
| 13 | Ecology and Global Change | 11 | Complete | 2023 assessment (six of nine planetary boundaries) added in RU/EN; Nature DOI verified | Full environmental-indicator proofread |
| 14 | Geographic Information Systems | 9 | Complete | OGC, ISO/TC 211, EPSG, QGIS, Esri and UN-GGIM references refreshed; Digital Code No. 178 (2025), Chapter 12, Articles 92–98 reviewed; UNESCAP 2020 baseline and 2026 AIP cross-checked for Kyrg-06/WGS 84 and Baltic-based vertical reference | Software-version and workflow validation; verify dataset-specific horizontal/vertical realization, transformation parameters, metadata and reuse conditions |
| 15 | Remote Sensing of the Earth | 11 | Complete | NASA, USGS, ESA and Copernicus sources linked; broken Sentinel-1 URL replaced | Sensor/product metadata and accuracy review |
| 16 | Geographic Research and Cartography | 9 | Complete | ICA Cartographic Body of Knowledge and UN census-methodology references linked | Full methodology and assessment review |
| 17 | Geographic Location and Geological Evolution of Kyrgyzstan | 9 | Complete | Area, border-demarcation and 2026 treaty updates checked; added Law No. 58 (2026), AIS Geographical Names, official 2025 WGS 84 pilot and UNESCAP 2020 national geodetic baseline | Extreme-point coordinates; obtain transformation/control-point metadata and verify dataset-specific vertical datum, legacy-map migration, national boundary geometry and toponyms |
| 18 | Geology, Mountain Systems and Relief of Kyrgyzstan | 10 | Complete | Peak heights and country-specific Lenin/Ibn Sina naming checked; incomplete geological citations corrected; DEM vertical-reference guidance added; CAIAG ASTER GDEM 30 m candidate, RESILAND 3 m/14-site procurement, 2026 national geological-atlas project and historical glacier-source limits documented | Obtain licensed/validated DEMs and full CRS/vertical metadata; verify glacier outlines against current imagery; review national geological atlas when published; validate peak heights and map sources |
| 19 | Climate and Altitudinal Zonation of Kyrgyzstan | 10 | Initial structure reviewed; misplaced 19.10.5 moved back into section 19.10 on 2 Nov | UNEP +1.2°C 1960–2023 estimate cross-checked with Kyrgyzhydromet: 22 homogenised stations (1980–2021), +0.28°C/decade countrywide; separate 13-station climate indices (1980–2022), growing-season trends and method limits documented | Obtain station-level series/metadata; reconcile climate-normal periods; validate high-mountain spatial interpolation and future projections |
| 20 | Glaciers, Rivers, Lakes and Water Resources of Kyrgyzstan | 10 | Complete | River-runoff range, renewable water resources, glacier mass balance, Chu–Talas transfer and Issyk-Kul morphometry checked; 2025 research inventory reports >2,000 glacial lakes (Sentinel-2 2022–2024); 2026 Kyrgyz Range study quantifies lake/glacier change 1968–2021; NSC 2025 water-use indicators and WIS scope documented; 2025 national mudflow/flood hazard atlas reviewed | Obtain/verify lake polygons and reuse rights; obtain station-level discharge series and metadata; validate basin/reservoir records, current glacier outlines and GLOF hazard layers; inspect hazard-atlas map scale, legend and layer licensing |
| 21 | Flora and Fauna of Kyrgyzstan | 10 | Complete | Red List counts checked; 2040 biodiversity programme correctly labelled as draft pending approval | Species taxonomy, population trends and sensitive-location review |
| 22 | Natural Zones, Protected Areas and National Parks of Kyrgyzstan | 10 | Complete | NSC protected-area series, UNDP 7.4%, UNESCO MAB areas and 2025 management figures checked | Legal status and official protected-area geometries |
| 23 | Population and Settlement of Kyrgyzstan | 12 | Complete | NSC 2026 population, regional totals, 2025 births/deaths and migration; IOM Round 7 checked | Final migration, urbanisation and settlement proofread |
| 24 | Seven Regions of Kyrgyzstan | 12 | Complete | Administrative reform law, Manas renaming, 2026 population table and 27 Oct proposal checked | Deep profile-by-profile source and map validation |
| 25 | Cities, Economy, Transport and Natural Resources of Kyrgyzstan | 12 | Complete | GDP, road transport, energy import planning and mining indicators checked | Verify operational status of each infrastructure project |
| 26 | Environmental Challenges and Future of Kyrgyzstan | 12 | Complete | NDC 3.0, Climate Law, water, wastewater, forests, pastures and waste figures checked; visual IDs normalised | Air-quality station data and glacier-inventory reconciliation |

## Priority queue

1. Complete source-by-source review of Chapters 01–16, including dated data and bibliographic relevance.
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
- Chapter 01 still requires source-by-source verification and final bilingual proofreading; this targeted repair does not imply that the chapter has passed the full audit.

- Chapter 01 references reviewed: AAG, RGS and UN-GGIM links refreshed; ICA site timed out and remains unresolved. Chapter update commit: `80c82d47fdf86d8d0c50da5254787f636c2ed10f`.
