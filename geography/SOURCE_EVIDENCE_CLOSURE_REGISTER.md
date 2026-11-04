# Geography — Source and Evidence Closure Register

**Snapshot:** 4 November 2026  
**Canonical branch:** `workspace/geography`  
**Purpose:** record source-link checks, bibliographic corrections and claim-to-source checks. This is a working evidence register, not a claim that every sentence or every bibliography entry has been exhaustively verified.

## Status definitions

- **Verified — access and relevance:** the source was reached or independently confirmed, and its subject is relevant to the cited material.
- **Verified by authoritative search record:** direct page retrieval was blocked or timed out, but a publisher/institutional search record confirmed the publication and bibliographic metadata.
- **Corrected:** the original link or citation metadata was wrong or misleading and has been repaired in the chapter.
- **Needs follow-up:** the source is useful but its precise claim coverage, data version, reuse terms or underlying dataset still requires inspection.
- **Not a dead-link finding:** an HTTP 403, timeout or parser failure is recorded as a retrieval limitation, not automatically as a broken source.

## First tranche — Chapters 01–05 (initial targeted evidence pass)

### Chapter 01 — Geography as a Science

| Source / evidence | Result | Action / limitation |
|---|---|---|
| American Association of Geographers, GeoWeek | Verified — access and relevance | The live page is a Geography Awareness Week education/outreach page, not a definitional article. Corrected the bibliography title so it no longer claims to be “What Is Geography?”. |
| Royal Geographical Society, “What is geography?” | Verified — access and relevance | The page explicitly describes geography as bridging social and natural sciences and explains human and physical geography. Suitable for the chapter's introductory framing. |
| National Geographic Society, “What Is Geography?” | Corrected | The previous URL was replaced with the current `/resource/geography-article/` page, which directly defines geography and discusses physical, human and biological systems and spatial perspective. |
| UN Statistics Division / UN-GGIM | Verified — access and relevance | The page identifies the UN geospatial-information-management initiative and its workstreams. Use it for geospatial governance/context, not as a general definition of geography. |
| ICA Cartographic Body of Knowledge | Verified — access and relevance | The official ICA Commission on Education and Training page is linked for cartographic education context; it is not treated as a substitute for a detailed map-projection or cartographic-standard source. |
| Longley et al., *Geographic Information Science and Systems* | Corrected | Completed the incomplete book reference with 4th edition, 2015, Wiley and ISBN 978-1-118-67695-0 using the publisher's catalogue. |
| National Research Council, *Rediscovering Geography* | Verified by authoritative publication record | National Academies Press record confirms the 1997 consensus report and DOI 10.17226/4913. Direct DOI retrieval by the browser was not successful, so the publisher landing page is the preferred verification route. |

**Chapter 01 edits saved:**
- AAG citation title made accurate.
- National Geographic URL repaired and its two geography standards linked.
- UN-GGIM and ICA links updated to current institutional pages.
- Longley et al. bibliographic details completed.
- The chapter's own note now maps each source to the specific sections it supports; remaining claim-level mapping is still open.

### Chapter 02 — Earth's Geographic Envelope

| Source / evidence | Result | Action / limitation |
|---|---|---|
| NASA Earth Observatory, “The Water Cycle” | Verified — access and relevance; dated source | Page is an older 2010 conceptual explainer. It remains useful for the basic water-cycle mechanism, but its old global water-distribution values must not be used as current figures without a newer dataset. |
| NOAA JetStream, “Layers of the Atmosphere” and “The Atmosphere” | Verified — access and relevance | Both pages are accessible; they support atmospheric layering and dry-air composition. The dry-air table explicitly excludes water vapour. |
| Stockholm Resilience Centre, Planetary Boundaries Framework | Verified — access and relevance; dynamic status | Current page reports seven of nine boundaries transgressed. Chapter material must identify its assessment year and should not silently replace the 2023 six-of-nine result with the newer status. |
| Richardson et al. (2023), *Science Advances* | Needs follow-up at claim level | Bibliographic reference is present and chapter wording is date-specific. Preserve the distinction between the 2023 assessment (six of nine) and later updates. Verify each visual/status statement against the named assessment edition. |
| NOAA GML, global CO₂ annual mean | Corrected | The previous bibliography title described the annual-mean trend, but linked to the Annual Greenhouse Gas Index page. Replaced it with NOAA's global CO₂ data page, which explicitly provides globally averaged marine-surface monthly and annual means. NOAA's 2025 annual value is preliminary (425.62 ppm; version 2026-10). |
| WMO Greenhouse Gas Bulletin No. 22 | Verified — access and relevance | Official bulletin dated 27 October 2026 reports 2025 global surface CO₂ at 426.8 ± 0.2 ppm. This is a distinct WMO GAW global-surface series, not the NOAA marine-site annual mean. |
| USGS, “How Much Water Is There on Earth?” | Verified — access and relevance | Official USGS page is accessible and distinguishes oceans, fresh/saline groundwater, ice, lakes and rivers. Appropriate support for the corrected water-reservoir treatment. |

**Chapter 02 edit saved:** NOAA reference now points to the global monthly/annual mean CO₂ data page rather than the AGGI page. The chapter's distinction between NOAA 425.6 ppm and WMO 426.8 ppm is retained.

### Chapter 03 — Lithosphere and Geological Processes

| Source / evidence | Result | Action / limitation |
|---|---|---|
| USGS, “How Fast Do Tectonic Plates Move?” | Verified — access and relevance | Official FAQ accessible; supports the variation in plate speeds and GPS/geological measurement methods. |
| National Park Service, “Minerals” | Verified — access and relevance | Official page accessible; supports mineral characteristics and Mohs hardness. |
| NSF SAGE / IRIS earthquake-location lesson | Verified — access and relevance | Educational resource accessible; supports seismic-location teaching. |
| International Commission on Stratigraphy chart | Verified — site responds; content extraction limited | Official chart URL resolves, but the browser returned no readable text. Do not infer a detailed chart audit from link availability alone. |
| British Geological Survey, “Geological Processes” | Verified — access and relevance | Official page distinguishes weathering in place, erosion/transport and deposition; useful for the chapter's process definitions. |
| USGS, “What is a landslide and what causes one?” | Verified — access and relevance | Official FAQ explicitly identifies falls, topples, slides, spreads and flows and describes common triggers. |
| Halla et al. (2024), Hadean lower boundary | Verified by authoritative publication record | Episodes / IUGS publication record confirms DOI, authorship, publication details and GSSA age 4567.30 ± 0.16 Ma. |
| Thomson et al. (2026), USGS Geochron Data Report 1227 | Verified by authoritative publication record | USGS Publications record confirms title, authors, publication date (3 September 2026), report number and DOI 10.3133/dr1227. Direct page retrieval timed out, but the publisher's indexed record is complete. |
| USGS *This Dynamic Earth: Inside the Earth* | Not a dead-link finding | Direct retrieval returned 403. Treat as a source-access restriction, not proof that the source is broken; retain pending alternate access or replacement. |

### Chapter 04 — Earth's Landforms and Relief

| Source / evidence | Result | Action / limitation |
|---|---|---|
| NOAA NCEI, ETOPO 2022 | Verified — access and relevance | Official page confirms current ETOPO 2022 version and 15-arc-second products, including ice-surface and bedrock variants. Dataset-specific vertical metadata still must be inspected before quantitative use. |
| NOAA National Ocean Service, “How Deep Is the Ocean?” | Verified — access and relevance; dated | Official page gives average ocean depth and a Challenger Deep value. The chapter correctly retains distinct dated estimates rather than treating this overview figure as the final word. |
| USGS Landslide Maps | Verified — access and relevance | Official USGS page accessible; supports the landslide mapping context, but its inventory is US-focused and is not evidence for Kyrgyzstan susceptibility. |
| NPS, “Mass Wasting” | Verified — access and relevance | Official page accessible; supports slope movement terminology and examples. |
| NPS, “Plateaus and Mesas” | Verified — access and relevance | Official page accessible; supports the basic geomorphic distinction. |
| Fujii et al. (2026), Challenger Deep multibeam study | Verified by authoritative publication record | Nature *Scientific Data* record confirms publication 16 September 2026, DOI 10.1038/s41597-026-08267-z, preferred eastern-basin gridded value 10,927 m and sound-velocity sensitivity range 10,914–10,932 m. The chapter accurately describes 10,927 m as a preferred gridded estimate, not a definitive redetermination. |
| USGS Fact Sheet 2004–3072, *Landslide Types and Processes* | Verified — official record and DOI | Final check resolved the legacy endpoint concern. The USGS Publications Warehouse record confirms Lynn Highland, 2004, Fact Sheet 2004–3072, 4 pages, DOI 10.3133/fs20043072. Chapter 04 bibliography now cites the canonical DOI. A 403 or redirect restriction on an older URL is not evidence that the publication is invalid. |

### Chapter 05 — Atmosphere and Climatology

| Source / evidence | Result | Action / limitation |
|---|---|---|
| WMO Guide and climate resources | Needs follow-up | The broad WMO landing page is an institutional entry point, not a specific instrument-methods edition. A precise edition/URL should be attached wherever a technical observation-method claim depends on it. |
| NOAA Climate Data Online | Verified — access and relevance | Official page accessible; documents historical station observations and 30-year climate normals. |
| NASA Earth Observatory, Earth's Energy Budget | Needs follow-up | Broad landing page is not a precise article citation. Confirm the exact page or figure used for any numerical energy-budget claim. |
| IPCC AR6 WGI | Verified by authoritative search record | The Working Group I report landing page and title are confirmed; direct page retrieval returned 403, so use the official report page/downloads as the reference route. |
| Copernicus Climate Data Store | Verified — access and relevance | Portal accessible and provides datasets, documentation and applications. Dataset-specific record, version, period and licence still required for any extracted value. |
| NOAA GML, global CO₂ annual mean | Corrected | Replaced the AGGI URL with the NOAA global monthly/annual mean CO₂ data page. |
| WMO Greenhouse Gas Bulletin No. 22 | Verified — access and relevance | Official bulletin confirms the 2025 global surface mean (426.8 ± 0.2 ppm). The chapter correctly distinguishes it from NOAA's 425.62 ppm marine-site mean. |

**Chapter 05 edit saved:** NOAA CO₂ reference corrected to the appropriate global monthly/annual data page.

## Cross-chapter evidence controls applied in this tranche

1. A source page being live does not establish that it supports every adjacent claim; claim relevance is recorded separately.
2. A browser 403, timeout or parser failure is not classified as a dead link without independent evidence.
3. Dynamic indicators carry their source, year, metric and spatial coverage. NOAA's marine-site annual mean (425.62 ppm) and WMO's global-surface mean (426.8 ppm) remain separate series.
4. A dated conceptual explainer may support a stable mechanism but should not be reused as a current quantitative dataset.
5. International or national portals are not treated as proof that a particular spatial dataset is licensed, complete or fit for map production.

## Milestone and next actions

- Initial targeted source/evidence pass: **5/26 chapters (approximately 20%)**.
- Chapter files changed in this tranche: Chapters 01, 02 and 05.
- No claim is made that every bibliography item or every claim in Chapters 01–05 has received a full line-by-line citation audit.
- Next tranche: Chapters 06–10. Prioritise hydrology/ocean datasets, biodiversity and biome classification sources, soil classification and soil-data sources, demographic global series, and primary legal references for political geography.
- Separate remaining work includes all-claim citation mapping, live link rechecks at release, dataset-level metadata/licence checks, cartographic validation, visuals, browser/interactive tests, screen-reader/manual accessibility and physical-device testing.


## Second tranche — Chapters 06–10 (initial targeted evidence pass)

| Chapter | Source / evidence | Result | Action / limitation |
|---:|---|---|---|
| 06 | USGS Water Science School | Corrected and verified | Replaced the broad `/special-topics/water-science-school` URL with the live “Water Basics Information by Topic” page. It links to water facts, water distribution, hydrology and the water cycle. |
| 06 | NOAA Ocean Facts | Verified — access and relevance | The portal is live and contains ocean facts, geography/geodesy, tides, currents and ocean observations. It is a broad portal; use a specific NOAA fact/data page for individual numerical claims. |
| 06 | UNESCO World Water Development Report | Verified — access and relevance | Official UNESCO page identifies WWDR as the UN flagship assessment of freshwater state, use and management and links to annual editions. Select the exact report year when supporting a dated claim. |
| 06 | International Hydrographic Organization, Standards and Specifications | Verified — access and relevance | Official IHO page is live and lists hydrographic standards, including S-100 work. For bathymetric or charting claims, cite the specific standard and edition, not only the general index. |
| 06 | NSIDC, Glaciers | Verified — access and relevance | NSIDC page is live and provides cryosphere/glacier educational and data links. Dataset-level claims still require a named product and date. |
| 07 | Convention on Biological Diversity | Verified — access and relevance | CBD Secretariat treaty page is live and current; it is the primary legal framework, not a species-status dataset. |
| 07 | IPBES Global Assessment (2019) | Verified by authoritative report record | Official Zenodo record confirms the 2019 global assessment and its report chapters. The IPBES site itself returned 403 in direct retrieval; this is recorded as a crawler restriction, not a dead link. |
| 07 | IPBES Invasive Alien Species Assessment (2023) | Verified by authoritative report record | IPBES page/record confirms plenary acceptance in 2023, six-chapter assessment and Summary for Policymakers. |
| 07 | IUCN Red List | Verified by authoritative search record; direct retrieval restricted | The Red List FAQ record confirms the database's extinction-risk purpose, assessment categories, update frequency and limitations. The main site returned 403; do not interpret that as a dead link. Species-level use must cite the exact taxon assessment and its assessment date/version. |
| 07 | UNESCO Man and the Biosphere Programme | Verified — access and relevance | Official UNESCO page confirms the MAB programme and World Network of Biosphere Reserves. This designation is not interchangeable with national protected-area status. |
| 07 | Olson et al. (2001), terrestrial ecoregions | Verified — access and relevance | Oxford Academic record confirms BioScience 51(11), pp. 933–938 and DOI. The paper defines ecoregions and supports the chapter's mapping/classification discussion. |
| 07 | Millennium Ecosystem Assessment (2005) | Verified — access and relevance | Official assessment site exposes the synthesis and a regional assessment for Central Asian mountain ecosystems. |
| 07 | Chapin, Matson & Vitousek, *Principles of Terrestrial Ecosystem Ecology* | Corrected | Completed missing authors, year, second edition, publisher and DOI using Springer metadata. |
| 08 | IUSS Working Group WRB, fourth edition | Verified by authoritative publication record | WRB documents page confirms the 2022 fourth edition and corrected 2024 PDF; the 2024 correction must be used rather than an uncorrected earlier PDF. |
| 08 | FAO/ITPS, *Status of the World's Soil Resources 2026* | Verified — access and relevance | Official FAO page confirms the 2026 global assessment, launch date and DOI 10.4060/ce0792en. It is distinct from the 2015 assessment. |
| 08 | FAO Voluntary Guidelines for Sustainable Soil Management (2017) | Corrected and verified | Replaced a direct PDF endpoint that returned 403 with the current official FAO landing page. The page confirms the publication date (2017) and the guidelines' voluntary/non-binding character. |
| 08 | USDA NRCS, *Soil Survey Manual* | Verified — access and relevance | Official page identifies the 2017 manual and its field description, soil-profile and survey methods. |
| 08 | IPCC, *Climate Change and Land* (2019) | Verified by authoritative report record; direct retrieval restricted | Official IPCC report path returned 403 to the browser; treat as a retrieval restriction. Preserve the report title/year and use the official report PDF/landing record when checking specific claims. |
| 08 | UNCCD, *Global Land Outlook* | Verified — access and relevance | Official UNCCD page identifies GLO as its flagship publication and links to the 2017 and 2022 editions. Name the edition used for any dated statistic. |
| 08 | European Commission JRC, ESDAC | Verified — access and relevance | Official ESDAC portal is live and identifies itself as the European Soil Data Centre. Its European datasets are not automatically representative of Central Asia. |
| 08 | Turner, Gardner & O'Neill, *Landscape Ecology in Theory and Practice* | Corrected | Completed missing authorship, year, first edition, publisher and DOI using Springer metadata. |
| 09 | UN World Population Prospects 2024 | Verified — portal access; data-version follow-up required | UN Population Division portal resolves. Record the specific WPP 2024 dataset/table and variant for each numerical claim; the landing page alone is not a citation to a particular series. |
| 09 | UN World Urbanization Prospects 2025 | Verified by authoritative publication record | UN DESA record confirms 2025 revision, country/area estimates, methodology and city/town/rural categories. Direct retrieval returned 403; this is not treated as a dead link. The chapter must preserve its distinction between the Degree of Urbanization and national definitions. |
| 09 | UN Principles and Recommendations for Population and Housing Censuses, Revision 4 (2025) | Verified — access and relevance | UNSD census page confirms Rev. 4, endorsement/adoption for the 2030 census programme and recommendation as the international standard. |
| 09 | UNSD demographic standards and methods | Verified — access and relevance | Official standards page lists current census, migration and vital-statistics methods. Select a named manual/edition when supporting a technical definition. |
| 09 | IOM World Migration Report 2024 | Verified by authoritative report record; direct portal retrieval restricted | Official IOM-hosted report summary/data PDFs are indexed and accessible via search results. The chapter should cite the exact report table and data year; for example, the report's 281 million migrant figure refers to 2020 estimates, not 2024 observations. |
| 09 | UN-Habitat World Cities Report 2024 | Verified by authoritative publication record | Publisher record confirms the 2024 report and its urban climate focus. Direct retrieval returned 403; use the publisher record and specific report chapter/table for claims. |
| 09 | World Bank WDI population indicator | Verified — access and relevance | WDI page is live, lists source agencies and CC BY 4.0 licensing. The indicator page is a dynamic series; retain the extraction date and source metadata. |
| 09 | UNDP Human Development Data Center | Verified — access and relevance | Official data center page describes global, regional and country-level data and links to HDI methodology and documentation. |
| 10 | UN Charter | Verified by authoritative publication record | Official UN full-text record confirms Article 2 on sovereign equality, peaceful settlement and prohibition on force against territorial integrity/political independence. Direct page retrieval returned 403. |
| 10 | UNCLOS (1982) | Corrected and verified | Replaced the direct PDF URL that returned 403 with the UN Treaty Collection depositary record. It identifies the 1982 Convention, entry into force, treaty status and links to certified authentic texts in six languages. |
| 10 | Vienna Convention on the Law of Treaties (1969) | Verified — access and relevance | UN Treaty Collection record is live and confirms adoption, entry into force, treaty number and parties. |
| 10 | UN General Assembly Resolution 1514 (XV) | Corrected and verified by authoritative record | Added the previously missing official UN Digital Library record for the 1960 Declaration on independence. The UN record confirms the resolution number and adoption date. |
| 10 | ICJ Statute | Needs follow-up — direct retrieval restricted | The official ICJ URL returned 403. Retain as a primary legal reference but recheck via an alternate official text source before publication. |
| 10 | Agnew, *Geopolitics: Re-Visioning World Politics* | Corrected | Completed 2nd edition, 2004, Routledge and ISBN 978-0-415-31007-9 using publisher/catalogue metadata. |
| 10 | Flint, *Introduction to Geopolitics* | Corrected | Completed 4th edition, 2021, Routledge and ISBN 978-0-367-68675-8 using publisher metadata. |
| 10 | Taylor & Flint, *Political Geography* | Corrected | Completed 6th edition, 2014, Routledge and ISBN 978-1-138-83708-9 using bibliographic metadata. |
| 10 | UN Statistics Division M49 | Verified — access and relevance | Official M49 page explicitly says the regional groupings are for statistical convenience and do not imply political/legal status or boundary delimitation. This qualification is consistent with the chapter's wording. |

### Corrections saved in Chapters 06–10

1. Chapter 06 — replaced the broad USGS Water Science School URL with the live “Water Basics Information by Topic” page. Commit: `94db71522ef52d6020b3c22bc8321645cb6ef7d8`.
2. Chapter 07 — completed Chapin, Matson & Vitousek textbook metadata and DOI. Commit: `a5c0d149b4f5e5db912775c46f3c8b36f4b19c96`.
3. Chapter 08 — replaced the restricted FAO PDF link with the official landing page and completed Turner et al. book metadata/DOI. Commit: `ee7e8bb104a737ca270d587492f8f32c385f376f`.
4. Chapter 10 — replaced the direct UNCLOS PDF with the UN Treaty Collection record, added the official UN Digital Library record for Resolution 1514 (XV), and completed bibliographic details for Agnew, Flint, and Taylor & Flint. Commit: `55197bae98112b750ac569392e73c4f4bc2ab46a`.
5. Chapter 09 — no text edits required in this tranche; remaining data-version and exact-table mapping requirements are recorded above.

### Cross-chapter evidence controls reinforced

- Do not treat international statistical regions (UN M49) as legal boundary determinations.
- Do not treat IUCN Red List categories, CBD treaty obligations, UNESCO MAB designations and national protected-area categories as interchangeable.
- Do not treat the UN WPP/WUP landing pages as sufficient citations for a particular extracted series; record variant, table, reference year and extraction date.
- Distinguish soil classification (WRB) from soil survey/measurement manuals and from global soil-status assessments.
- Distinguish treaty text, treaty depositary/status records and political-geography interpretation.

**Milestone:** initial targeted source/evidence pass now covers Chapters 01–10 (10/26, approximately 40%). This remains a targeted evidence review, not an exhaustive sentence-by-sentence citation audit. Next block: Chapters 11–15.


### Chapter 04 closure — 4 November 2026

- Final reference-by-reference pass completed for all 34 bibliography entries; each entry was checked for topical relevance to the chapter and publication identity. The USGS Fact Sheet 2004–3072 legacy URL was replaced with the canonical DOI record (10.3133/fs20043072).
- Final numerical/terminology sweep completed. The contour-slope example and self-check calculations were independently recomputed; dated Everest and Challenger Deep measurements remain distinguished by method, reference and uncertainty; DEM/DSM/DTM wording retains the dataset-metadata caveat.
- Textual scientific/editorial audit is closed at 100%. This does not close visual production, map-data licensing/validation, layout, accessibility, browser/device or deployment testing.


### Chapter 01 — targeted evidence-map update — 4 November 2026

| Claim group | Evidence checked | Result and remaining limitation |
|---|---|---|
| What geography studies; links between physical and human geography | RGS, *What is geography?*; National Geographic, *Geography* | Both sources support the interdisciplinary definition and the study of places, processes and human–environment relationships. |
| Spatial thinking, maps and geospatial representations | National Geographic Geography Standards 1 and 3 | Standards directly support spatial thinking, map/representation literacy, scale and spatial-pattern analysis. They are educational standards, not empirical research sources. |
| Geospatial information and public decision-making | UN-GGIM programme overview | Official UN description supports the role of geospatial information in policy, governance and sustainable development. |
| Cartographic education | ICA Commission on Education and Training (2023–2027 terms) | Replaced the previously timing-out CartoBoK endpoint with the live official ICA education commission page. It supports education/training context; it does not independently validate every cartographic technical statement. |
| GIS and spatial analysis textbook | Longley et al. (2015), 4th edition | Bibliographic metadata retained; use chapter/page-level citations in a final scholarly edition where a specific technical claim depends on it. |

### Chapter 02 — targeted evidence-map update — 4 November 2026

| Claim group | Evidence checked | Result and remaining limitation |
|---|---|---|
| Earth-system spheres | NASA Science, Earth System Science Research | NASA identifies five research spheres: atmosphere, biosphere, cryosphere, geosphere and hydrosphere. Chapter wording now distinguishes this model from the traditional four-component educational model. |
| Four traditional components and cryosphere terminology | NASA Earth-system sphere classification; National Geographic, *Earth's Systems* | Clarified that ice/snow may be included in hydrosphere in a four-component model while cryosphere is separately named in Earth-system science; lithosphere is a part of geosphere. A textbook-specific definition of the geographic envelope may vary by curriculum tradition. |
| Global water distribution | USGS, *How Much Water Is There on Earth?* | The displayed percentages match the USGS table; its cited underlying estimate is Shiklomanov (1993). Chapter notes now identify this as a rounded legacy global estimate, not a newly measured 2026 dataset. |
| Atmospheric vertical structure | NOAA JetStream, *Layers of the Atmosphere* | Official NOAA source identifies five principal thermal layers and gives approximate, latitude-dependent layer boundaries. Exact heights in diagrams must remain approximate. |
| Planetary boundaries | Richardson et al. (2023), *Science Advances*, DOI 10.1126/sciadv.adh2458 | Publication identity and nine-process framework verified. Its finding that six of nine boundaries were transgressed is specific to the 2023 assessment; do not label it as a 2026 status without a newer named assessment. |
| Carbon, nitrogen and phosphorus cycles | Chapter explanations reviewed for internal scientific consistency; existing NASA/USGS and Earth-system references checked | Basic pathway descriptions are sound at school level. Dedicated process-level source mapping is still required before the chapter can be marked fully audited. |
| CO₂ values | NOAA Global Monitoring Laboratory and WMO Greenhouse Gas Bulletin No. 22 | Keep the NOAA marine-site annual mean (425.6 ppm, preliminary for 2025) distinct from the WMO global surface estimate (426.8 ppm for 2025); they are not interchangeable series. |

**Scope note:** These updates close specific source and terminology defects; they do not constitute exhaustive sentence-by-sentence verification of either chapter. Visual briefs, final artwork, full translation proofread and browser/device/accessibility checks remain separate workstreams.


### Chapter 02 — additional claim-matched references — 4 November 2026

| Claim group | Additional source | Evidence and limitation |
|---|---|---|
| Carbon reservoirs, photosynthesis, respiration, decomposition, ocean exchange and fossil-fuel emissions | NOAA, *Carbon Cycle* | Supports the qualitative pathways in the chapter; no annual flux values are imported from this page. |
| Solar heating, atmospheric/ocean circulation and planetary energy balance | NASA Earth Observatory, *Climate and Earth's Energy Budget* | Supports the explanation that incoming solar energy is redistributed and balanced by outgoing thermal radiation. Numerical energy-budget fractions should retain their own source/date if later added to figures. |
| Nitrogen fixation, nitrification and denitrification | UNEP, *Beat Nitrogen Pollution*; University of Missouri Extension, *Nitrogen in the Environment: Nitrogen Cycle* | Supports the school-level sequence and microbial role. The chapter's table is a simplified cycle, not an exhaustive list of all soil nitrogen transformations or fluxes. |
| Phosphorus cycle and eutrophication | Open University, *Eutrophication: Phosphorus* | Supports phosphorus's sedimentary/biological pathway, lack of a major gaseous phase and eutrophication connection. |
| Planetary-boundary status | Richardson et al. (2023), *Science Advances* | The “six of nine boundaries transgressed” result is a 2023 assessment. It must not be presented as the current 2026 status; chapter text currently names the framework's nine processes without assigning a present-day status. |

**Outstanding scientific checks for Chapter 02:** verify detailed claims on lithosphere/tectonic processes against a named geology source; trace atmospheric composition percentages to a specific NOAA table or equivalent primary data page; ensure any future planetary-boundary graphic is explicitly labelled with the assessment publication/year and its own reuse terms.


## Visual-source workflow — Chapters 01–02 (4 November 2026)

- A visual-brief inventory was extracted directly from the two chapter files: 3 briefs in Chapter 01 and 18 in Chapter 02 (21 total).
- A first candidate-source search identified USGS educational media as explicitly labelled Public Domain, and NASA / National Geographic educational resources as scientifically relevant reference material. These are candidate discovery routes, not blanket permission to reuse every image on those sites.
- National Geographic's *Earth's Systems* is a relevant school-level conceptual source for the five-sphere model; its page credits photograph authorship, so reuse must follow the specific asset's displayed rights/credit terms.
- No image has been approved, downloaded, generated or integrated in this pass. Each asset must be checked individually for scientific fit, source metadata, rights, required attribution, bilingual caption and alt text before integration.
- The detailed per-ID register is `geography/IMAGE_SOURCES.md`.


## Chapter 02 targeted source follow-up — 4 November 2026

| Claim area | Source | Verification result | Scope / limitation |
|---|---|---|---|
| Dry-air composition | NOAA JetStream, *The Atmosphere* | The live NOAA table gives nitrogen 78.084%, oxygen 20.946%, argon 0.934% and CO₂ about 0.042%; it explicitly excludes water vapour and separately explains its variability. | Appropriate support for the chapter's rounded composition values. CO₂'s annual mean remains separately tied to the NOAA observing series/year, not treated as a fixed atmospheric percentage. |
| Plate-boundary types | USGS, *Understanding Plate Motions* (This Dynamic Earth) | The official USGS explainer defines divergent, convergent and transform boundaries and explains crust creation, destruction and horizontal sliding. | Supports the school-level definitions and corresponding visual brief. More detailed regional tectonic claims still need their own geological sources. |
| Visual-source candidate | USGS Educational Resources / Middle and High School Geology | USGS search records label the Plate Tectonics Globe Activity and its map/globe cut-out as Public Domain. | A strong candidate for 2.5-A, but the exact media record and required credit must be inspected before integration. |

**Chapter 02 remaining source work:** detailed geologic processes and any regional examples; audit every other numerical claim against its exact source table/edition; final RU/EN proofreading; then individual asset rights checks and visual integration.


## Chapter 01 follow-up — regional source and bibliography integrity (4 November 2026)

- Added the National Statistical Committee of the Kyrgyz Republic's official Regional Statistics page as a country-level data portal for oblast-level examples: https://www.stat.gov.kg/ru/regionalnaya-statistika/ . The chapter does not yet introduce unsupported numeric regional claims; any future values must cite a specific table, period and update date.
- Corrected duplicate bibliography numbering: National Research Council is now reference 9; the Kyrgyz NSC regional statistics portal is reference 10. This is a citation-structure correction, not a claim that all Kyrgyzstan examples have been fully sourced.
- Remaining: trace each specific regional example to a dated official table/map; verify map projection examples and any technical claims individually; final bilingual proofread.


## Chapter 02 — visual evidence follow-up (4 November 2026)

- **Water distribution (2-C):** the exact USGS chart media record labels the asset Public Domain and attributes the rounded global distribution values to Igor Shiklomanov's 1993 chapter in *Water in Crisis*. The graphic must preserve the nested denominators (all water / freshwater / surface freshwater) and must not be presented as a 2026 measurement.
- **Water cycle (2.4-A):** the USGS 2022 global water-cycle diagram is Public Domain and was created by USGS VizLab with the USGS Water Resources Mission Area Web Communications Branch. It includes human water use, water quality and climate influences; caption it as a human-influenced global water-cycle view, not as a natural-only cycle.
- **Atmospheric layers (2-B, 2.3-A):** NOAA JetStream provides a five-layer diagram and a temperature profile. NOAA's education FAQ says nearly all NOAA educational content and images are public domain unless otherwise noted; verify the individual image credit line and retain NOAA attribution. Layer heights are approximate; the troposphere varies with latitude.
- These are source/rights findings for candidate visuals only. No candidate is approved or integrated until image-specific credit, bilingual labels/captions, alt text, scale/accuracy and repository embedding are checked.


## Chapters 06–10 — focused scientific follow-up — 5 November 2026

| Chapter | Claim / editorial point | Source checked | Result and remaining limit |
|---:|---|---|---|
| 06 | Practical versus Absolute Salinity | IOC, SCOR and IAPSO, *TEOS-10 Manual*, IOC Manuals and Guides No. 56 (2010); official TEOS-10 site | Corrected both RU and EN text: Practical Salinity on PSS-78 is dimensionless and should not be labelled PSU in technically precise writing; TEOS-10 uses Absolute Salinity in g/kg for thermodynamic calculations. Added the TEOS-10 manual and NOAA ocean-acidification page. The mean value near 35 is described as typical for open-ocean Practical Salinity, not a universal constant. |
| 07 | Interpretation of extinction-risk categories | IUCN, *The IUCN Red List Categories and Criteria*, Version 3.1, Second edition (2012), and Red List portal | Added an explicit warning that Red List categories apply to assessed taxa and are not a census of all biodiversity; Data Deficient and Not Evaluated do not mean low risk. Species examples still require taxon-specific assessment dates and versions. |
| 08 | Current global soil-status evidence and regional transfer | FAO/ITPS, *Status of the World's Soil Resources 2026*, DOI 10.4060/ce0792en | Updated the citation wording to identify the 2026 edition and its dedicated Europe and Central Asia regional chapter. Global findings must not be presented as local measurements; country-level claims still need national soil datasets and methods. |
| 09 | Population-estimate vintage and projection scenarios | UN DESA Population Division, *World Population Prospects 2024* and its Methodology Report; *World Urbanization Prospects 2025* | Added the methodology report and clarified that WPP values must identify the dataset/table, scenario, territory and extraction date. Estimates and projections are distinguished from observations; international Degree of Urbanization is not interchangeable with every national urban definition. Added the WUP 2025 methodology report to the chapter bibliography. |
| 10 | Legal regime of the exclusive economic zone | UNCLOS 1982, Part V, especially Articles 55–58 | Expanded the RU/EN explanation of coastal-state sovereign rights and specified jurisdiction, while noting that other states retain Convention-based freedoms. The EEZ is not territorial sea or full state sovereignty. Added the official Part V text as a distinct bibliography entry. |

**Bilingual structure validation:** numbered teaching-section headings match between Russian and English in Chapters 06–10 (17/17; 15/15; 15/15; 16/16; 15/15). Review-question counts match as well (16/16; 15/15; 15/15; 15/15; 14/14). This is a structural inventory check, not a sentence-level translation-quality sign-off.

**Scope and status:** these are five focused claim-level corrections, not exhaustive sentence-by-sentence audits. The existing chapter scores remain **73% each** because the visual assets are still placeholders and the remaining claim-to-source, language-parity, cartographic and editorial checks are not closed. Browser/device/deployment QA remains a separate later activity.

**Saved chapter commits:** Chapter 06 `547c389e073b4df638440fb2fbda990657d9466a`; Chapter 07 `9800d8319118a3357fd2a609a40738c83e5c6361` and final bibliography normalization `ecd041bab78aa2399f899d9ad5006fe092e47733`; Chapter 08 `d08997cfc24b4550bc30e7a10e4a4d6b69a19f96`; Chapter 09 `b3f1f9c5f8136b76c45d9a3edf0ae2df5f24f194`, intermediate reference normalization `0c821f33b033b5de675f42b6ffdd5f277b65ed6e`, final bibliography correction `3e8eae8a30bfcc62f9492b56f9ebd7f665dd7c1c`, and WUP methodology source addition `5ea41d543f7a2dd8b528b6f981bde8f46f33e7d2`; Chapter 10 `b4744e11feaa97c4685d9f66d20314c8143accb7` and bibliography normalization `df6f4ec8273c9444b5328e43c0e7d5bdfac4a4a7`.


## Chapters 07–10 — second focused scientific pass — 5 November 2026

| Chapter | Claim / editorial point | Source checked | Result and remaining limit |
|---:|---|---|---|
| 07 | Global biodiversity conservation and restoration targets | Convention on Biological Diversity, *Kunming–Montreal Global Biodiversity Framework* (2022), Targets 2 and 3 | Added bilingual distinction: Target 3 concerns effective conservation and management of at least 30% of land, inland waters, coasts and seas by 2030 through connected and equitably governed systems; Target 2 separately concerns restoration measures across at least 30% of degraded ecosystems. Clarified that the 30% target does not mean every included area is automatically strictly protected. |
| 08 | Comparability of soil salinity measurements | FAO, *Soil Salinity Assessment: Methods and Interpretation of Electrical Conductivity Measurements*; USDA NRCS, *Field Book for Describing and Sampling Soils*, Version 4.0 (2024) | Added bilingual distinction between saturated-paste extract ECe and EC values from 1:5 extracts or field apparent-conductivity instruments. Added the commonly cited ECe near 4 dS/m at 25°C as a historical reference, not a universal crop-damage threshold; warned against transferring it to other extract ratios without validated conversion. |
| 09 | Migration stock versus migration flow | UN demographic-statistics definitions and the chapter's existing migration indicator methodology | Added bilingual distinction: arrivals/departures are flows over a period; migrant stock is a point-in-time count based on the source's operational definition (for example, country of birth or citizenship). Added the distinction to editorial controls. |
| 10 | Contiguous-zone legal extent and powers | UNCLOS 1982, Part II, Article 33; official UN text | Added the 24-nautical-mile maximum measured from baselines, and clarified that the specified control concerns preventing and punishing customs, fiscal, immigration and sanitary-law infringements committed within the state's territory or territorial sea. Added Part II to the bibliography. |

**Saved commits for this pass:** Chapter 07 `39efced037245be630b3411c72a535757e8c5460`; Chapter 08 `ddd59f28fc04f798761eaacd05f12bac1bd627e8`; Chapter 09 `3d97c66d052333f85a40831142a6a6c6aa0679da`; Chapter 10 `e110cc0d6570e72b8e0dfd78827be78c76946c4e`.

**Status:** these are additional targeted corrections, not full chapter closure. Chapter 06 received no new text change in this pass; its previous TEOS-10 salinity and water-balance controls remain recorded above. Chapter progress therefore remains 73% each until the remaining visual, complete claim-source, and sentence-level RU/EN checks are completed. Browser/device/deployment QA remains separate.

## Chapters 06, 08–10 — third focused scientific follow-up — 5 November 2026

| Chapter | Claim / editorial point | Source checked | Result and remaining limit |
|---:|---|---|---|
| 06 | Catchment water-budget equation and storage residual | USDA Forest Service, *Technical Guide to Ground Water Resource Management* (FS-881, 2007), watershed water-budget section | Expanded the RU/EN explanation from a three-term shorthand to the general mass-balance principle (inflow − outflow = change in storage). The simplified P = ET + R + ΔS form is explicitly restricted to a natural catchment with negligible groundwater exchange and no external transfers. Added a source reference. Basin-specific balances still require all relevant fluxes and consistent boundaries/periods. |
| 08 | Soil-profile morphology versus formal classification | IUSS Working Group WRB, *World Reference Base for Soil Resources*, 4th edition (2022; corrected 2024); FAO Soils Portal | Clarified in both languages that O/A/E/B/C/R is a simplified morphological description, not a complete WRB classification key or a universal sequence. Formal classification requires diagnostic horizons, properties and materials under the selected system. Existing WRB reference retained; visual profile remains a brief for tomorrow. |
| 09 | Natural-change and migration rates; population growth rate | UN Population Division, *World Population Prospects 2024* Data Portal metadata; UNdata demographic glossary | Added bilingual formulas for natural change and net migration per 1,000 average residents, and the exponential annual growth-rate formula used by international datasets where applicable. Added a methodological warning: periods, boundaries, denominators and source definitions must match. Added the UN Data Portal metadata reference. |
| 10 | Legal boundary versus cartographic generalisation | Chapter's existing legal/cartographic source framework; editorial control added | Added bilingual warning that a small-scale map line does not replace treaty descriptions, agreed coordinates or demarcation records. Added caution for river/lake boundaries: do not infer legal status from the current shoreline or satellite image alone; apply the relevant treaty and rules. This is an editorial/cartographic safeguard, not a review of any specific bilateral boundary. |

**Saved commits:** Chapter 06 `207f09f5031a5d2c21b02932330ab8367c3c0679` (water-budget text) and `93811b5e03b7f1ae99553ba39806c3ec106d516b` (source addition); Chapter 08 `f56dac3bf202d0ad76afead1acbead0d2be9acd7`; Chapter 09 `8f192a4daf137d7618b7297b76db46068da6f927` (formulas) and `7a82a557f227fc9b967bc0033639f9c8fdc23030` (UN metadata reference); Chapter 10 `468d57625514ec1f81d33c787c90697e9d9701b7`.

**Scope:** focused corrections only. The chapter scores remain 73% each; image/map integration, complete claim-to-source mapping and final line-by-line RU/EN proofreading remain open. Browser/device/deployment QA is separate.

## Chapter 07 — biome and ecosystem classification follow-up — 5 November 2026

| Claim / editorial point | Source checked | Result and remaining limit |
|---|---|---|
| Traditional biome maps versus functional ecosystem typologies | IUCN, *Global Ecosystem Typology 2.0* (2020), DOI 10.2305/IUCN.CH.2020.13.en; IUCN Global Ecosystem Typology portal | Added bilingual explanation that traditional terrestrial biome maps often emphasise climate and vegetation structure, while IUCN GET uses six hierarchical levels and incorporates ecosystem functions and community composition. The frameworks complement one another but are not interchangeable category-for-category. Added the IUCN publication to the bibliography. The chapter's visual map still requires a named classification and legend. |

**Saved commit:** Chapter 07 `15fa5a4a48786efcd93fa840a0f4c140d6495c77`.


- **Chapter 06 clarification:** the worked catchment-balance example now explicitly states the assumptions behind the shortened storage-change equation and requires groundwater inflow/outflow, abstractions, discharges and transfers to be represented separately when relevant. Commit: `adcb61103b4724b1a9ee04cd317c2c6f34417432`.


## Third focused follow-up — Chapters 06–10 — 5 November 2026

- **Chapter 06:** refined the catchment control-volume explanation in both languages. External inflows/outflows are distinguished from internal withdrawals and return flows; reservoirs inside the catchment are assigned to storage change (ΔS), avoiding double counting. Commit: `59c525339d8b00dcedd08cb26a733ed1fa6b3ebf`.
- **Chapter 07:** clarified in both languages that Kunming–Montreal Framework Target 2 is a target for the coverage of effective restoration measures, not a guarantee that all ecosystems covered will have returned to their original condition by 2030. Commit: `af85b5dccc24d78fc07caea2ae162f4883767ebe`.
- **Chapter 08:** clarified that electrical conductivity reflects total dissolved ions but cannot by itself identify salt composition or diagnose sodicity; separate chemical and exchange-related measurements are required. The warning against transferring ECe thresholds to 1:5 extracts remains. Commit: `1979993d09b1885909e02bddf5c57c3b5b4da1c6`.
- **Chapter 09:** clarified that migration-flow datasets may count movement events rather than unique persons, depending on registration rules; users must check the statistical unit before comparing populations. Commit: `e1d2d9474269e012440aa31fdb65b79836a0f95a`.
- **Chapter 10:** clarified the geometry of the contiguous zone: the 24-nautical-mile limit is measured from baselines; where the territorial sea is 12 nautical miles, the contiguous zone may extend at most a further 12 nautical miles. Commit: `5ac1a2a5eab3aedde6332df29cae2af22b4bb223`.

These are focused bilingual conceptual corrections. They do not close full claim-to-source mapping, complete sentence-level RU/EN proofreading, visual integration or deployment/device QA. Chapter scores therefore remain unchanged pending a rubric-based reassessment rather than being raised solely because edits were committed.


### Chapter 06 — runoff-depth unit consistency — 5 November 2026

- Clarified in both Russian and English that the 220 mm outlet-runoff value in the worked catchment balance is runoff depth: measured discharge must first be converted to an equivalent depth over the catchment area. This makes the precipitation, evapotranspiration and runoff terms dimensionally comparable (mm over the same period).
- The numerical residual remains 30 mm (600 − 350 − 220); no change to the exercise result.
- Commit: `884fbdeeac9d07d6791a4bb172f66918a275198b`.


### Chapters 06 and 10 — calculation continuity and statehood/recognition — 5 November 2026

- **Chapter 06:** revised the bilingual river-basin practical assignment so the mean-discharge calculation uses the runoff volume derived in the preceding water-balance steps. For 250 mm runoff over 10,000 km², the volume is 2.5 km³; divided by 31,536,000 seconds, the annual mean discharge is approximately 79.3 m³/s. This removes the unrelated 3.78 km³ example that had interrupted the exercise's logic. Commit: `3c2f61d1cca4add4f68974f7ca18edc374b2a23f`.
- **Chapter 10:** expanded the bilingual statehood/recognition section with the four qualifications listed in Article 1 of the 1933 Montevideo Convention, its Article 3 statement on political existence and recognition, and a caveat that the Convention is regional and does not mechanically resolve every contested case. Added the treaty text and a 2024 Oxford University Press discussion of recognition theories. Treaty text checked against the U.S. Department of State historical document and University of Oslo Law Faculty treaty transcription; scholarly context checked against Kilibarda (2024). Commit: `6edda39164e53fbc7f68380135cd27d42c26bdde`.


### Chapter 07 — IUCN assessment-guidance currency — 5 November 2026

- Added the IUCN Standards and Petitions Committee's *Guidelines for Using the IUCN Red List Categories and Criteria*, Version 16 (March 2024), as a distinct source from the 2012 Version 3.1 criteria standard. The current guidance page was checked; it instructs users to verify for newer versions before formal assessments. The chapter's existing warning about Data Deficient and Not Evaluated remains consistent with IUCN category definitions. Commit: `bb8dbba6a65c311b56902b171c6d538f12b96ac1`.


### Chapter 09 — urban/rural classification method — 5 November 2026

- Expanded the bilingual explanation of the UN Degree of Urbanization used in World Urbanization Prospects 2025: 1 km² grid cells are classified using population density, contiguity and population-size thresholds; smaller administrative/statistical units are then assigned according to where most residents live. Clarified the first-level classes and that the harmonised method does not replace national legal definitions. Added the direct UN methodology-report link. Checked against the official WUP 2025 methodology report and UN Population Division summary. Commit: `5537ae858eecadda2bec2982ff9bfd7ace2bcdaa`.
