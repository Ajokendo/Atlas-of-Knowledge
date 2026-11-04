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
