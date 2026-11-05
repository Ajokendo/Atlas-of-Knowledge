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


### Chapter 09 — WUP 2025 bibliography de-duplication — 5 November 2026

- Consolidated duplicate World Urbanization Prospects 2025 methodology entries into the main WUP reference and corrected the methodology report's publication date to 27 January 2026, as shown on the official UN Population Division page. The WUP 2025 method report confirms the 1 km² grid-based Degree of Urbanization approach and its harmonised international comparison purpose. Commit: `f6615bc9f58bad6693cd87b9f0e8154f19e9c7fd`.


### Chapter 10 — UNCLOS claim-level source precision — 5 November 2026

- Added direct official UN texts for UNCLOS Part VI (continental shelf, Articles 76–78) and Part VII (high seas, Articles 86–89). These provide section-level support for the chapter's distinction between seabed/subsoil rights, the legal status of superjacent waters, high-seas freedoms and the prohibition on sovereignty claims over the high seas. Both official UN texts were checked. Commit: `aeecc0a1f4aff9e2f6adfca03c2abfa5ef13f59a`.


### Chapter 07 — CBD Target 2 and Target 3 wording — 5 November 2026

- Refined both language versions to match the official CBD wording more closely: Target 3 concerns effective conservation and management of at least 30% of terrestrial/inland-water and coastal/marine areas, with governance, connectivity and rights safeguards; Target 2 concerns at least 30% of degraded ecosystem areas being **under effective restoration** by 2030. Added the distinction that effective restoration must be resourced and monitored but need not be completed by 2030. Checked against the official CBD Target 2 and Target 3 guidance pages. Commit: `9adc9ecaaf124cc1b91d0dc22b0a395495ec5a9b`.

- Chapter 07 bibliography now links directly to the official CBD Target 2 and Target 3 guidance pages rather than only to the framework landing page. Commit: `33f2c927650531e92e8577480ed9863e3af3ea77`.


### Chapters 06–10 — worked-example arithmetic audit — 5 November 2026

The numerical teaching examples in the five chapters were independently recomputed. Results agree with the working text:

| Chapter | Recalculation | Result |
|---|---|---|
| 06 | 8 m × 0.75 m × 0.6 m/s; 600 − 350 − 220; 250 mm over 10,000 km²; 2.5 km³ over 31,536,000 seconds | 3.6 m³/s; 30 mm; 2.5 km³; 79.3 m³/s |
| 07 | 1,200/12,000; 90/1,200; 60/800 | 10%; 7.5%; 7.5% |
| 08 | 1,300 g/1,000 cm³; porosity using 2.65 g/cm³ particle density; 700 g/500 cm³ | 1.3 g/cm³; 50.9%; 1.4 g/cm³ |
| 09 | Dependency ratio; migration balance; demographic balance; crude birth/death rates | 50 per 100 (36 child + 14 older); 5 per 1,000; final population 504,000; CBR 13‰ and CDR 8‰ |
| 10 | 12 × 1.852; 200 × 1.852; 9,600/13,000 | 22.224 km; 370.4 km; 73.8% weighted regional turnout (not the unweighted 70%) |

All population and election examples are explicitly hypothetical; they are not presented as current country statistics. The calculation continuity defect in Chapter 06 was corrected separately (commit `3c2f61d1cca4add4f68974f7ca18edc374b2a23f`).


### Chapter 06 — exact global water-distribution source — 5 November 2026

- Added the direct USGS *How Much Water Is There on Earth?* page for the 1.386 billion km³ estimate and the rounded distribution of global water. The page explicitly identifies the figures as estimates and traces the underlying distribution table to published global water-resource estimates. The broader USGS Water Science School portal remains as a separate general reference. Commit: `e4c03dd3c16379cc32f3b113d94e4d659782551e`; bibliography numbering was normalized and checked in commit `a25f6b5d9fc3ea7ad83733fdfea3565935e254be`.


### Chapters 06–10 — bilingual structure and exercise inventory recheck — 5 November 2026

- Current-branch automated check confirms matching numbered main-section headings and English labels in all five chapters: 06 (17/17), 07 (15/15), 08 (15/15), 09 (16/16), 10 (15/15).
- Review-question counts match RU/EN: 06 (16/16), 07 (15/15), 08 (15/15), 09 (15/15), 10 (14/14).
- Practical activity counts match RU/EN: 06 (1/1), 07 (4/4), 08 (4/4), 09 (5/5), 10 (5/5).
- This is a structural inventory check only; it does not replace semantic line-by-line proofreading.


### Chapter 10 — ICJ Statute alternate-access closure — 5 November 2026

- The original ICJ-hosted Statute URL returned HTTP 403 during direct retrieval. Replaced it with the official UN full-text page for the Statute of the International Court of Justice, which is annexed to the UN Charter and forms an integral part of it under Article 92. The UN page was checked and provides the complete Statute text. Commit: `5f43b92078b7b9f7351dc95b293009e378889555`.


### Chapter 10 — Montevideo Convention source cross-check — 5 November 2026

- Added separate links for the treaty text (U.S. Department of State historical record; University of Oslo Law Faculty treaty library) and treaty metadata (OAS record; UN Treaty Collection record). Articles 1 and 3 were checked against the text. Commit: `f2a8d5c3f3845166700f11be255f1c59280967f4`.


### Chapter 10 — M49 statistical versus legal geography distinction — 5 November 2026

- Added a bilingual clarification that UN M49 classifies countries and areas for statistical reporting and comparison; it does not determine sovereignty, statehood, recognition or the legal course of state boundaries. Checked against the UN Statistics Division M49 methodology overview and its explanation of statistical identity. Commit: `cf70c9c4d7875dd643956b11811c9ccc73fb9f0c`.


### Chapter 09 — population-density denominator clarification — 5 November 2026

- Added a bilingual note requiring users to distinguish land area, total area and inhabited area when comparing arithmetic population density. It also requires population, area and reference date to refer to the same territory and comparable period. Commit: `63becbe6080cdd4adb21c198686312f02961bf05`.


### Chapter 09 — population-density source definition — 5 November 2026

- Added the direct World Bank EN.POP.DNST indicator page to the bibliography. Its label explicitly defines the denominator as land area (people per square kilometre of land area), supporting the chapter's instruction to distinguish land area from total or inhabited area. Commit: `9bc90598c64ad4dc6a75224abf9f604de3d51e1b`.


### Chapter 09 — mid-year population denominator consistency — 5 November 2026

- Harmonised the Russian and English wording and notation for crude birth, crude death, natural-change and migration rates. Both language versions now identify mid-year population as the denominator commonly used as an approximation to average annual population, while requiring the source's exact definition to be checked. Updated the hypothetical examples and practical task wording to match. Commit: `5c1bfc245381922f300ed1758618f7ddf75919d0`.


### Chapter 06 — global water shares corrected — 5 November 2026

- Corrected a subtle category error in both language versions. Oceans and seas account for about 96.5% of total water; all saline reservoirs together account for about 97.5% when saline groundwater and saline lakes are included; freshwater is about 2.5%. The prior wording incorrectly assigned the 97.5% figure to oceans and seas alone. Checked against the USGS global water-distribution table. Commit: `1d91a7bc57da482095fb0f5541a6ea1387bcc316`.


### Chapter 06 — IHO source specificity and edition check — 5 November 2026

- Replaced the broad IHO standards portal citation with the relevant publication identifiers and current catalogue editions: S-23 (limits of oceans and seas, 1953), S-44 Edition 6.2.0 (October 2024), S-102 Edition 3.0.0 (December 2024) and S-100 Edition 5.2.1 (December 2025). Checked against the IHO Standards and Specifications catalogue, last modified 30 October 2026. Commit: `80cd391382cdeceddbb5f048938e904ddab1324c`.


### Chapter 07 — IPBES and IUCN direct-source access — 5 November 2026

- Added the DOI record for the 2023 IPBES Invasive Alien Species Assessment and replaced IUCN Red List root/library links with current official resource pages on the `nrl.iucnredlist.org` subdomain. The supporting-information page explicitly identifies the assessment date, scope, criteria version and publication details that should accompany a species-status claim. Current Red List guidance page confirms Version 16 (March 2024). Commit: `2b3c9e30926342edbc4c8e75800ec41550026171`.


### Chapter 07 — scope of species-status evidence — 5 November 2026

- Confirmed that the current chapter contains no named species with an asserted IUCN Red List category; therefore no individual species assessment is being implied or cited. Added a bilingual editorial rule requiring scientific name, global/regional scope, category/criteria, assessment and publication dates, and Red List version if a species-status example is introduced later. Commit: `251f251e8fe4e336db39d3a1e6c1e250a0e6f49b`.


### Chapter 08 — scope of soil-data claims — 5 November 2026

- Clarified in both languages that numerical examples are instructional and are not country-level soil statistics or field-study results. Added explicit provenance requirements for future regional soil maps and measurements: dataset, year, scale, classification system, sampling depth and method. This separates current conceptual material from future regional data work. Commit: `ddbd9df53ed25ad4f15bad1215e81ea7db4d8ea8`.


### Chapter 09 — scope of demographic numerical claims — 5 November 2026

- Added a bilingual statement that the chapter's numerical examples are hypothetical and do not represent actual country or regional population values. Real maps/comparisons must identify the exact table/indicator, scenario, territory, reference year and extraction date. Existing WPP 2024 and WUP 2025 sources support the methods and dataset context. Commit: `4680bc04e9eb002a57d9d52e98ddf7970baab20d`.


### Chapter 10 — scope of current legal claims — 5 November 2026

- Added a bilingual scope statement that the chapter presents general principles and does not assert current legal status for named disputed territories or pending delimitations. Any future country case study must cite primary legal instruments, applicable treaties/agreements and relevant court or tribunal decisions, with date and geographic scope. Commit: `f73567233ea467c5118c5bc5cd7b9c3ccdab10d2`.


### Chapter 06 — scope of oceanographic data claims — 5 November 2026

- Documented the source mapping for current numeric/technical claims: USGS global water distribution; TEOS-10 salinity and seawater properties; IHO S-23 ocean/sea limits, S-44 hydrographic surveys, S-102 bathymetric surfaces and S-100 data model; NSIDC glacier basics; NOAA ocean acidification; UNESCO WWDR and USDA watershed water budget. No specific trench-depth or mean-depth measurement is asserted in the current text; future bathymetry maps require product/survey, date, resolution and vertical datum metadata.


### Chapter 09 — World Bank vital-rate metadata — 5 November 2026

- Added direct metadata records for World Bank crude birth and death rate indicators. Both definitions specify mid-year population as the divisor when annual population changes, supporting the chapter's denominator wording. Retained the direct land-area definition for the population-density indicator. Commit: `16649e8552437b4ed962f8f9410125bbd32220b3`.


### Chapter 08 — soil pH measurement comparability — 5 November 2026

- Expanded the bilingual pH explanation: logarithmic scale, approximate tenfold hydrogen-ion activity difference per pH unit, and the need to identify the extraction solution and soil-to-solution ratio. This prevents direct comparison of pH values obtained by different laboratory protocols without qualification. Commit: `d4650bc368a48150168240b64056d32b879e8372`.


### Chapter 08 — WRB organic horizon coverage — 5 November 2026

- Expanded the bilingual soil-profile overview to include the WRB H horizon for organic/peat material, distinguished from the O horizon; updated the profile illustration specification accordingly. Checked against WRB Fourth Edition 2022, Annex 3 (corrected 2024). Commit: `9bae5672e0a7568f098d1c590d72b72cbb8bfe33`.


- Follow-up verification caught and corrected a duplicated H symbol in the English horizon list and aligned the English classification note with the Russian text. Both versions now list H, O, A, E, B, C and R once and distinguish master horizon/layer designations from the diagnostic criteria used for formal WRB classification. Commits: `616affb021a9729a8355d51048a622348f3547f8`, `6727ea73c466ab38ed0b9b192c67cfee6ae856c3`.


### Chapter 07 — GBF Target 3 geographic scope — 5 November 2026

- Clarified in both languages that the 30% conservation objective in Target 3 is a global target, not an automatic 30% national-territory quota for every country. Retained the distinction between effective conservation, strict protection and rights-compatible sustainable use. Commit: `44e95d29e79d5b8731c94ffd4a568c92e593b66a`.


- Extended the geographic-scope clarification to GBF Target 2: the 30% restoration objective is global and applies to degraded ecosystem areas, not an automatic requirement to restore 30% of each country's total territory. RU/EN wording now distinguishes Targets 2 and 3 clearly. Commit: `d8892146b1d3d58a8bcd6bfc4e9c46d18a08802e`.


### Chapter 09 — WUP 2025 Degree of Urbanization thresholds — 5 November 2026

- Added the exact level-1 thresholds to both language versions: cities use contiguous 1 km² cells at ≥1,500 people/km² and cluster population ≥50,000; towns and semi-dense areas use ≥300 people/km² and cluster population ≥5,000; remaining cells are rural. Clarified that these are WUP 2025 international statistical thresholds, not national legal definitions, and that level 2 adds detail. Checked against the WUP 2025 methodology report. Commit: `e459800f4a7d7aa04a0cc9659b93048136858ca7`.


### Chapter 06 — Southern Ocean boundary status — 5 November 2026

- Replaced the overgeneralised phrase “current international practice” with a precise caveat: 60°S is a commonly used boundary in modern sources, but it is not a universally adopted IHO boundary. The current official IHO S-23 is the 1953 edition and excludes the Southern Ocean; the 2002 fourth-edition draft is explicitly a working document that was not approved. Added the direct IHO draft source. Checked against IHO S-23 catalogue, the 2002 draft and NOAA's explanation of the differing practices. Commit: `57e0739a6893b2377a05e2f7b1055c066f54f5e9`.


- Added NOAA National Ocean Service's direct explainer as a second source for the widely used five-ocean convention and the non-ratification caveat for the 60°S Southern Ocean boundary. Commit: `b32e9ece268f789c95f322d343e32e68236e4a5d`.


### Chapter 09 — WUP 2025 grid-level implementation nuance — 5 November 2026

- Refined the bilingual description of the Degree of Urbanization: the full methodology has a two-stage process, but WUP 2025's global dataset relies primarily on the 1 km² grid classification because no open worldwide boundary dataset exists for small spatial units. This avoids implying that the global WUP dataset applies the second-stage administrative-unit assignment everywhere. Checked against the WUP 2025 methodology report, Box II.2. Commit: `12d32b88bbdf4f14f9be1eddeb927897c7daacc8`.


### Chapter 10 — UNCLOS Area versus high seas — 5 November 2026

- Added the UNCLOS “Area” (seabed and subsoil beyond national jurisdiction) as a separate concept from the high-seas water column. The bilingual text explains the common-heritage principle under Articles 136–137 and notes that the legal status of superjacent waters is not changed by the seabed's status (Article 135). Added official UN Part XI Sections 1 and 2 links. Commit: `c2412eed3ab7f6fb6f1acc6d8d0baf6b452fdcda`.


- Updated the Chapter 10 maritime-zones illustration brief to depict the Area as seabed beyond national jurisdiction and high seas as the overlying water column; added the matching English production brief. Commit: `aef5597993c6f40abad063be6574fa489f23870b`.


### Chapter 07 — IUCN Red List release date check — 5 November 2026

- Dated the Red List bibliography entry to version 2026-1, released 9 July 2026, which is the latest published release as of this audit date. IUCN's planned 2026-2 release is scheduled for 19 November 2026 and is not yet published; the chapter therefore does not prematurely cite it. Added the official IUCN update-history page. Commit: `25ed8d2b4929f6b02e15eb4955a322b4890a2cd7`.


### Chapter 09 — current UN vital-statistics source — 5 November 2026

- Added the UN Statistics Division Population and Vital Statistics Report, Volume LXXVIII (January 2026), including its periodically updated Tables 2 and 3 and technical notes, as a current source for national census/estimate and vital-event data. The page showed tables last updated 5 October 2026 at the time of checking. Commit: `4c51e53870866cd5a6be2476228ec4151af5c82c`.


### Chapter 10 — bilingual visual production briefs — 5 November 2026

- Added English production briefs alongside the Russian specifications for the six chapter figure concepts; the maritime-zones brief explicitly distinguishes the Area seabed from the high-seas water column. The seven in-text visual IDs remain placeholders; no images were created today. Commit: `75fee48be53b237ed9fd78e8b2b79acbd19f5725`.


### Chapter 09 — bilingual visual production briefs — 5 November 2026

- Added English production counterparts for all six Chapter 09 figure briefs (data sources, demographic transition, population pyramids, migration, density mapping and urban agglomeration growth). Visual IDs remain placeholders; no images were created. Commit: `a600bebbc6a9ba290accf03ab9a6006a0f49ce9f`.


### Chapter 08 — bilingual visual production briefs — 5 November 2026

- Added English production instructions for all seven Chapter 08 visual concepts: soil/geosphere interface, soil-forming factors, WRB profile horizons, global soil map, erosion, landscape morphology and landscape mosaic/connectivity. Visuals remain placeholders. Commit: `b2e366f31e5af78e547a274278264a7eb1634718`.


### Chapter 07 — bilingual visual production briefs — 5 November 2026

- Added English production instructions for all nine Chapter 07 figure concepts: biosphere cross-section, tolerance curve, food web/energy pyramid, biogeographical realms, latitudinal/altitudinal zonation, biome panorama, aquatic zonation, ecological connectivity and carbon/nitrogen cycles. No images were created; placeholders remain for the next visual-production stage. Commit: `1452297ed18f0554cdf831bbebc4d238d72e8a33`.


### Chapter 06 — bilingual visual production briefs — 5 November 2026

- Added English production instructions for the four registered core visuals: hydrological cycle, five-ocean map, ocean-floor profile and ocean-motion diagrams. The ocean-map brief incorporates the revised non-universal Southern Ocean boundary caveat. No images were created. Commit: `4282a32dd93779c6635027748584c3d5ed686ca2`.


### Chapter 06 — visual ID reconciliation — 5 November 2026

- Reconciled the chapter's production briefs with its in-text markers: 11 previously unmarked visual concepts now have stable bilingual IDs and teaching-location markers; four redundant aliases were normalised to 6-A–6-D. The chapter now has 15 unique planned assets, all still placeholders. The visual register total is 231 across 26 chapters. Commits: `57ec4a27d8ba80b013a388e434df784b907b074b`, `57b7b9a6d59c1e3b070adf1d5d45c8e70e3f0b31`, `1bd3a384212a6ae893834e6ba5a748d30887dff4`.


- Added the missing bilingual production brief for visual ID 10-A (world political map), specifying data date, projection, scale, boundary provenance, treatment of disputed territories and the distinction between de facto control and legal status. Commit: `ea7107c8b2c927b14927568e0e71539afd34dd82`.


### Chapters 06–10 — visual marker and brief parity QA — 5 November 2026

- Verified the in-text visual ID and English production-brief counts against the chapter inventory: Ch06 15/15, Ch07 9/9, Ch08 7/7, Ch09 6/6 and Ch10 7/7. Chapter 06's four repeated brief aliases were normalised so each unique asset has one production brief; Chapter 10's 10-A world political map received its missing brief. All assets remain uncreated placeholders. Final clean-up commit for duplicate Chapter 06 marker briefs: `32b0e02e2454d085ca7878abd1bbe1c80246b541`; Chapter 10 10-A brief: `ea7107c8b2c927b14927568e0e71539afd34dd82`.


### Chapters 06–10 — English-copy worked-example parity — 5 November 2026

- Restored the English-only chapter copies for the numbered worked examples and methods subsections that previously existed only in the paired bilingual teaching block: Ch06 6.13.1 and 6.17.1; Ch07 7.4.1 and 7.15.1; Ch08 8.4.1 and 8.15.1; Ch09 9.8.1 and 9.16.1; Ch10 10.5.1 and 10.15.1. The English-only versions now contain the corresponding full explanations, examples and activities rather than relying on the mixed-language block. Automated heading-ID comparison now has zero missing or extra teaching headings in all five chapters (29/29, 17/17, 17/17, 18/18 and 17/17 respectively). Commits: Ch06 `c3a1edc174e07675bf01d7652b849cc5710e8e2c`, `6712350daa8638657d27f17dc8294936932a8f14`; Ch07 `f409a4a858a225ee9c3df76b54e7a6ec196302f9`; Ch08 `4628c2a6b67e972b196d96973c626105f0d1a5d2`; Ch09 `922b4a88e8f6e559ac10a1178b3206fb42bd3dde`; Ch10 `099b6049041236519fe7b602ff53862a27bdba5b`.


### Chapter 06 — bilingual key-term glossary — 5 November 2026

- Added a bilingual glossary of 25 core terms covering water stores and cycle processes, catchment hydrology, oceanographic properties and circulation, marine chemistry, groundwater and water scarcity. The glossary is placed before the review questions and uses the terminology already defined in the chapter. Commit: `f827509fd7b9bba5c2d7ff441017fab4cd66a708`.


- Updated the Chapter 10 bilingual key-term list to include the newly clarified maritime concepts: baseline, contiguous zone, the Area (seabed beyond national jurisdiction) and high seas. Commit: `bb34acbf677af3a78ccffaa4d4ca30ebb195a6d4`.


- Updated the Russian and English self-check question on soil horizons to include the newly added WRB H horizon and to refer to master horizons/layers rather than imply a fixed sequence. Commit: `0b0bde34740ed99d720cfa54ece4080e83c81e91`.


- Updated the Chapter 06 review question on ocean classification to reflect the non-universal Southern Ocean boundary and require students to identify the classification source. Updated the Chapter 10 maritime-law review question to cover internal waters, territorial sea, contiguous zone, EEZ, continental shelf, high seas and the Area. Both RU/EN question pairs now align with the corrected content. Commits: Ch06 `7c616f8cb2ea1fe3adb40286162897b37ff00eb7`; Ch10 `e7f0577ac6598b0a9147a3a77d646878451d2d59`.


- Extended the Chapter 08 bilingual glossary with H and O organic horizons and saturated-paste extract electrical conductivity (ECe), matching the revised WRB profile and salinity-measurement sections. Commit: `3cf71c280f48410c92a0ddd3f9c4f818c861d3d9`.


- Extended the Chapter 09 bilingual key-term list with migration flow, migrant stock, mid-year population and Degree of Urbanization, matching the revised indicator and WUP methodology sections. Commit: `67146954a2dd5e87a3ee03ca5d700b6f274756ba`.

## Consolidated focused audit findings — Chapters 06–10 — 5 November 2026

The chapter-level audit records were added to each source chapter. Findings and integration status:

- **Chapter 06 — Hydrosphere and World Ocean:** runoff discharge is converted to equivalent catchment depth before comparison with precipitation/evapotranspiration; catchment storage and residual are explained; Southern Ocean boundary convention and source are disclosed. Review question/glossary aligned. Fifteen unique bilingual visual IDs reconciled; placeholders only. Chapter note commit: `80b943ab01acf5252337f16357337c36ca72eafb`.
- **Chapter 07 — Biosphere and Natural Biomes:** the 10% trophic-transfer example is explicitly local to its stated calculation, not a universal law; GBF Target 2 is correctly described as effective restoration coverage, not completed restoration of 30% of every country; restoration monitoring includes ecological baselines and local land-user considerations. Nine unique bilingual visual IDs checked; placeholders only. Chapter note commit: `9cedac6a335991d1c4e2d82b1fdf9ab2ff483198`.
- **Chapter 08 — Soils and Landscape Geography:** WRB profile horizons H/O and their non-universal sequence are clarified; bulk-density/porosity calculation is labelled an estimate with stated particle-density assumption; ECe, 1:5 extracts and field apparent EC are not conflated; salinity and sodicity are diagnostically distinguished. Seven unique bilingual visual IDs checked; placeholders only. Chapter note commit: `c9e15fbfaced0112de5bfa97ac7fc3020fc656fb`.
- **Chapter 09 — Population and Demography:** migration flow (including event-counting) is separated from migrant stock; definitions and registration rules are required; worked net migration example verified (+500; +5 per 1,000); age dependency is distinguished from actual economic dependency; Degree of Urbanization is distinguished from national urban definitions. Six unique bilingual visual IDs checked; placeholders only. Chapter note commit: `0a99a30208117cbdef96996f60f57d0e8afbf28c`.
- **Chapter 10 — Political Geography:** 12/24/200 nautical-mile limits are measured from baselines as appropriate; sovereignty, sovereign rights and jurisdiction across maritime zones are distinguished; boundary delimitation/demarcation and de facto control/legal status are not conflated. Seven unique bilingual visual IDs checked; placeholders only. Chapter note commit: `2600b84914889e34e3261d6b27aefcb7580c39a3`.

**Structural bilingual check:** numbered teaching-heading IDs were previously checked with zero missing/extra IDs: Ch06 29, Ch07 17, Ch08 17, Ch09 18, Ch10 17 matched. This is structural parity, not final sentence-level translation proofing. Visual brief parity is Ch06 15/15, Ch07 9/9, Ch08 7/7, Ch09 6/6 and Ch10 7/7; assets have not yet been generated or integrated.

**Remaining closure work:** sentence-level RU/EN proofread, source-to-claim verification for all numerical and legal statements, verify dates/current datasets before release, and visual generation/integration. These items remain open and chapter readiness percentages are not raised solely because the findings have been documented.


### Chapter 06 — final bilingual text and source closure — 5 November 2026

- Completed the sentence-level review of the 17 numbered teaching sections and paired examples, summary, glossary, review questions and practical assignment in Russian and English.
- Corrected a RU/EN definition mismatch between natural lakes and artificial reservoirs; clarified that surface-water and groundwater divides can differ; qualified the orbital motion of water particles in deep- and shallow-water waves; and added the classification caveat for marine ecological zones.
- Replaced the unevenly ordered bibliography with 14 topic-specific institutional references. Newly explicit source coverage includes USGS global water distribution, streamflow and aquifers; NASA's hydrological cycle; NOAA ocean classification, currents and acidification; NSIDC sea ice; IHO S-23 and current standards catalogue; TEOS-10; and the USDA watershed water-budget guide.
- Verified calculations: river cross-section example = 3.6 m³/s; basin exercise = 250 mm runoff, 2.5 km³ annual volume and approximately 79.3 m³/s annual mean discharge; residual example = 30 mm. Units and time periods are stated consistently.
- The 15 unique bilingual visual IDs and briefs remain placeholders. This entry does not claim image integration, browser/device accessibility QA or deployment validation.
- Chapter content commit: `e8e6abe30366cf2d64844ace8c5ce0c8d421836a`.


### Chapter 07 — final bilingual text and source closure — 5 November 2026

- Completed a focused RU/EN scientific and editorial pass over the numbered teaching sections, methods, restoration activity, summary, glossary, review questions and bibliography.
- Corrected a fundamental explanatory imprecision in the oxygen cycle: in oxygenic photosynthesis, CO₂ supplies carbon for organic-matter formation, while molecular O₂ is released through water oxidation in the light-dependent reactions. Reworded carbon stores and fluxes to distinguish stocks from transfers.
- Refined biome classification: named all six levels of the IUCN Global Ecosystem Typology; added temperate rainforests; described deserts as hot or cold; and clarified that savanna fire regimes vary rather than forming a universal climate descriptor.
- Added methodological cautions for camera-trap abundance interpretation and eDNA detection, including detection probability, contamination, false positives/negatives, and spatial/temporal transport or persistence of DNA.
- Rechecked CBD GBF Targets 2 and 3 against the official framework text: both are global 2030 targets, not automatic national-territory quotas. Target 2 concerns degraded ecosystem areas under effective restoration; Target 3 concerns areas effectively conserved and managed.
- Strengthened the restoration exercise with baseline and reference-ecosystem requirements and indicators covering native species, community structure, soil/water conditions, ecological functions, connectivity and social context.
- Added the current SER Third Edition (2026) standards resource, a molecular-biology source for photosynthetic oxygen origin, and a 2026 eDNA methods review. The chapter bibliography now contains 15 references. IUCN Red List version 2026-1 remains the latest published release recorded as of 5 November 2026.
- Nine unique bilingual visual IDs and their production briefs remain placeholders; no images have been generated or integrated.
- Chapter content commit: `b9c41e71706d3b9a33cd8258e8e00ab70bc40bff`.



### Chapter 08 — WRB classification and digital soil-map limitations — 5 November 2026

- Checked the current WRB document set: the fourth edition (2022; corrections through 24 September 2024) is the current edition and recognises 32 Reference Soil Groups. Chapter 08 now distinguishes these formal classification units from broad teaching descriptions such as “steppe soils”, “alluvial valley soils” and “mountain soils”; the bilingual map brief prohibits mixing WRB units, national classes and general landscape descriptions in one legend. Sources: IUSS Working Group WRB official documents and FAO Soils Portal.
- Checked ISRIC's SoilGrids 2.0 documentation: modelled soil-property predictions are provided at 250 m for six standard depth intervals (0–5, 5–15, 15–30, 30–60, 60–100 and 100–200 cm), with pixel-level uncertainty information. The documentation notes uneven observation coverage and data gaps in Central Asia. Chapter text now makes clear that these are model predictions, not field measurements at every pixel, and requires field validation before local decisions in Kyrgyzstan.
- Added the official SoilGrids documentation and Poggio et al. (2021) to the chapter bibliography. Revised the visual brief so a WRB soil-group map and a SoilGrids soil-property map are treated as different products with separate legends, units, depth intervals and provenance.
- Chapter content commits: `f5b45a26ff48d72dac956343b6f55c26c66e2080` (scientific text and map-method additions); `d3c1e879e4e6293e324b7d9ffa8f7f195c3af5de` (brief and bilingual summary alignment).
- **Limit:** this is a targeted evidence closure, not a complete sentence-level bilingual proofread or full claim-to-source audit. Seven visual assets remain placeholders; no visual integration or browser/device/deployment QA is claimed.


- **Chapter 08 SoilGrids detail:** recorded the six explicit depth intervals (0–5, 5–15, 15–30, 30–60, 60–100 and 100–200 cm) and clarified that 250 m is grid-cell size, not a guarantee of 250 m local predictive accuracy. Bilingual text and map metadata requirements were updated. Commit: `458cc4715c1357649cf89d904419a9fc590daf06`.



### Chapter 08 — bilingual proofread and claim-source audit, continued — 5 November 2026

- **WRB:** rechecked the current fourth edition and 24 September 2024 corrections against the official IUSS/ISRIC publication. Confirmed 32 Reference Soil Groups, qualifier-based detailed naming and the distinction between profile master horizons and the full classification key. Official source: https://wrb.isric.org/documents.html
- **SoilGrids 2.0:** rechecked ISRIC's current documentation. The six intervals are 0–5, 5–15, 15–30, 30–60, 60–100 and 100–200 cm; the 90% prediction interval is represented by the 5th and 95th percentiles. The documentation explicitly notes sparse profile coverage in Central Asia. The text now distinguishes grid-cell size from predictive accuracy and requires local field validation. Sources: https://docs.isric.org/globaldata/soilgrids/ and https://docs.isric.org/globaldata/soilgrids/SoilGrids_faqs_01.html
- **UNCCD:** checked the formal Convention definition in Article 1. Both languages now distinguish the chapter's broad educational description of land degradation from the Convention's definition of desertification in arid, semi-arid and dry sub-humid areas. Official source: https://www.unccd.int/article-1-use-terms
- **FAO/ITPS 2026:** verified the current global soil assessment, its 2026 publication and the separate Europe and Central Asia regional chapter. The chapter does not infer country-level conditions from global averages. Source: https://www.fao.org/global-soil-partnership/Scientific-and-technical-support/itps/status-of-the-worlds-soil-resources/en
- **Soil salinity:** checked the distinction between saturated-paste extract conductivity (ECe), other soil-to-water extract ratios and field apparent conductivity against the FAO salinity-assessment manual and NRCS field guidance. The text retains the 4 dS/m figure only as a historical reference, not a universal crop threshold.
- **Bilingual editing:** relocated the English salinity subsection, summary, review questions and practical activities to mirror the Russian chapter sequence; aligned the 15 review questions and four practical activities; clarified calcification and landscape-facies terminology; qualified the A horizon description to avoid implying that humus accumulation is universal.
- **Chapter content commits:** `959db9f2b6dde194df9807e558377dcf65fb6a26` (bilingual order, UNCCD and soil-process terminology); `09d99b723414bf0d80405c4092f2ed06de270663` (horizon and glossary refinement); `b6c399cc35b3f85ea25ca25d935e35113f3bdf5d` (landscape-morphology terminology).
- **Remaining release work:** seven visual assets are still placeholders; no image integration, full visual science review, browser/mobile/accessibility testing or deployment validation is claimed.


### Chapter 09 — migration definitions, forced displacement and HDI methodology — 5 November 2026

- Updated the Russian and English migration sections against the UN Statistics Division's 2025 *Recommendations on Statistics of International Migration and Temporary Mobility* (unedited version, with revisions noted through 24 March 2026). The chapter now distinguishes international migration (change of country of residence) from international temporary mobility (other international border crossings), explains the two recommended residence-duration criteria and intended duration, and warns that national implementation may differ. The recommendation is not misrepresented as a universal national rule. Source: https://unstats.un.org/go/migrrec
- Clarified that forced displacement is a broader concept; internally displaced persons (IDPs) remain within their country's internationally recognised borders, while refugee status requires crossing an international border and meeting the applicable legal definition. Added UNHCR's IDP definition source and aligned the RU/EN summaries and glossary. Source: https://emergency.unhcr.org/protection/legal-framework/idp-definition
- Expanded the bilingual Human Development Index explanation to identify its three dimensions and indicators: life expectancy at birth; expected and mean years of schooling; and PPP-adjusted GNI per capita. Added normalized dimension indices, geometric-mean aggregation and logarithmic income transformation, retaining the limitations of an average composite measure. Source: https://hdr.undp.org/sites/default/files/2025_HDR/hdr2025_technical_notes.pdf
- Added the UN Population Division DemoData portal as a source for underlying empirical demographic series. Its portal reports data through 2026 and a last update of 3 November 2026; the chapter now requires the exact series and extraction date. Source: https://population.un.org/demodata/
- Chapter content commits: `fd0cade68e49b8d41a6a5cbd92cc5b545586d265` (migration/HDI source additions and bilingual revisions); `061f315d757495b3b5140a1d24726da13520d69a` (English migration alignment); `05b4e8a4f337592fba7420bb0afe9a8f84eff02e` (IDP/refugee distinction, glossary and summary parity).
- **Limit:** the work closes specific source and concept gaps, not the full sentence-level bilingual line edit or all claim-to-source verification. Six visual assets remain placeholders; no image integration, final visual review, accessibility/browser/mobile testing or release QA is claimed.


### Chapter 09 — final structural and bilingual inventory recheck — 5 November 2026

- Rechecked the current branch after the migration, HDI, forced-displacement and glossary edits. The Russian and English teaching-heading inventories match: 18/18 IDs (sections 9.1–9.16 plus worked/method subsections 9.8.1 and 9.16.1).
- Review-question inventories match: 15 Russian / 15 English. Practical-activity inventories match: 5 / 5. The bibliography contains 15 numbered sources. Six unique visual IDs (09-A–09-F) remain placeholders; no images were generated or integrated.
- Verified the chapter end marker precedes the focused audit record. The audit record explicitly leaves sentence-level RU/EN proofreading, full claims-to-source closure, visual creation/review and accessibility/release QA open.
- Final chapter content commit in this pass: `4ccde56c905c5b80262f42ef3297c1b9c44ad609` (bilingual glossary punctuation and terminology). Earlier content commits in this pass: `fd0cade68e49b8d41a6a5cbd92cc5b545586d265`, `061f315d757495b3b5140a1d24726da13520d69a`, `05b4e8a4f337592fba7420bb0afe9a8f84eff02e`.
- Readiness matrix updated to **75%**; this reflects targeted concept/source closures, not visual completion or final publication readiness. Matrix commit: `945e8c8d45671a4973224b5852a4c82a30fb1472`.


### Chapter 09 — non-visual editorial and methodological closure — 5 November 2026

- Corrected infant mortality in RU and EN: it is the probability of dying before exact age one, derived from a life table or specified estimation method and expressed per 1,000 live births. It is not simply the same-calendar-year ratio of infant deaths to births. WHO indicator metadata and UN IGME methods were checked. Source: https://www.who.int/data/gho/data/indicators/indicator-details/GHO/infant-mortality-rate-%28probability-of-dying-between-birth-and-age-1-per-1000-live-births%29 and https://childmortality.org/all-cause-mortality/methods?reportType=tools
- Added the age-specific fertility-rate definition and five-year age-group TFR calculation in both languages. Verified the formula's unit conversion when age-specific rates are expressed per 1,000 women.
- Clarified the demographic balance equation as start population + births − deaths + arrivals − departures + statistical adjustments. Classroom examples explicitly assume adjustments equal zero. Checked the annual exponential growth-rate description against WPP 2024 metadata.
- Clarified HDI education calculation: expected-years and mean-years-of-schooling indices are averaged arithmetically to form the education index; health, education and income indices are then combined geometrically. Source: https://hdr.undp.org/sites/default/files/2025_HDR/hdr2025_technical_notes.pdf
- Moved the English 9.16.1 migration-measurement subsection under English 9.16, aligned to Russian 9.16.1. Confirmed 18/18 matching RU/EN teaching-heading IDs, 15/15 review questions, 5/5 practical activities and 18 numbered bibliography references.
- Recalculated all worked numerical examples and checked results: demographic balance 504,000; natural increase 3,500; net migration +500; CBR 13‰; CDR 8‰; age dependency ratio 50 per 100 (child 36, old-age 14); migration rate +5 per 1,000; hypothetical density 50 people/km².
- Verified the WUP 2025 grid methodology against its official methodological report, including the two-stage classification, 1 km² grid and caveats on global grid-level use. Source: https://population.un.org/wup/assets/Publications/undesa_pd_2025_wup2025_methodological_report.pdf
- **Non-visual work status:** scientific definitions, formula explanations, RU/EN section alignment, glossary, learning questions, practical tasks, references and arithmetic checks completed for this editorial pass. Readiness matrix set to 90%; the remaining 10% is reserved for six visual assets 09-A–09-F and their subsequent scientific/accessibility review. Browser/mobile/rendered-site checks are deferred until the visual assets are integrated; no such checks are claimed.
- Chapter commits: `a4d2564b0acdac441a7ca4cd4dbdef5e8343e988` (scientific definitions and bilingual structure); `012746e940b94c508f67ff35ccc5983e7641a03b` (close non-visual audit record). Matrix commit: `ac5ddaa42e9228a1d5868f441f141ea39e5a417a`.


### Chapter 09 — visual inventory and figure numbering correction — 5 November 2026

- A final audit of the illustration briefs found that Figure 9.1 (demographic data sources) already had a bilingual production brief but lacked an explicit placeholder ID, while the world-population trend placeholder 09-A lacked its numbered figure caption. Added the missing 09-G placeholder for Figure 9.1, added Figure 9.2 for the world-population trend and renumbered the remaining captions sequentially through Figure 9.7.
- Updated the Russian and English age-sex-pyramid practical activity references from Figure 9.3 to Figure 9.4.
- The complete visual backlog is therefore **seven** assets: 09-A–09-G, with seven numbered figure captions 9.1–9.7. None has been generated or integrated. Readiness remains 90% pending those assets and their later scientific/accessibility review.
- Chapter commits: `e7ffa637cc08292c6313e7041fae2938a6c937e6` (figure inventory and numbering); `c18fb8c999f4a815d5aecef9b7b90d5351ec9b6f` (corrected remaining-work count). Matrix commit: `769b4e4b67f798efe15aaba3147b6f2b84a3d4eb`.

- Follow-up matrix correction: updated the visual-count column from 6 to **7** to match the seven distinct figure briefs and placeholders 09-A–09-G. Matrix commit: `0840b05e77a41a9b86954860d40ac54cffbe6511`.

### Chapter 10 — political geography: final non-visual scientific and editorial closure — 5 November 2026

- **Statehood, territory and recognition:** retained the Montevideo Convention as a regional treaty and added the caveat that a disputed or incompletely delimited boundary does not by itself decide statehood. The definition of state territory now explicitly includes archipelagic waters where applicable and distinguishes territorial sovereignty from the more limited rights in an EEZ and on the continental shelf. Sources: Montevideo Convention, Articles 1 and 3; UN Charter; UNCLOS Parts II, V and VI.
- **Boundary concepts:** corrected the imprecise “vertical surface” wording; distinguished geometric, astronomical and geographic boundary descriptions; retained the rule that a map line cannot substitute for treaty text, agreed coordinates or official demarcation records. The text explains that boundary categories are a teaching classification and legal instruments determine the actual course.
- **Maritime law:** rechecked the 12/24/200-nautical-mile distances from the relevant baselines; clarified the continental-shelf entitlement to at least 200 nautical miles and the Article 76 criteria/constraints for an outer limit beyond 200 nautical miles; reiterated that shelf rights concern the seabed/subsoil and do not change the status of the superjacent water column. Added the landlocked-state access/transit provisions of UNCLOS Part X (Articles 124–132). Sources: UNCLOS Parts II, V, VI, VII, X and XI; ITLOS UNCLOS overview.
- **Administrative systems:** distinguished confederations from federations and clarified decentralisation, deconcentration and devolution. Added definitions of free-trade area, customs union and common market while noting that actual integration agreements need not follow a single linear sequence.
- **Electoral geography:** qualified the equal-suffrage principle by national legal context; distinguished malapportionment from gerrymandering; strengthened impartiality, transparency and public-consultation safeguards. Added the OSCE/ODIHR 2023 *Handbook for the Observation of Election Administration*, section V.2, as a source for electoral-boundary delineation guidance.
- **International water governance:** distinguished groundwater physically connected to an international watercourse from separate transboundary aquifers. The 1997 Watercourses Convention definition and scope (Articles 1–2) and its cooperation/equitable-use principles (Articles 5–8) were checked. The separate aquifer reference is the UN General Assembly's 2008 Resolution 63/124 and annexed Draft Articles; the chapter does not imply that those Draft Articles are themselves a binding treaty.
- **Dispute settlement and decolonisation:** clarified that ICJ contentious jurisdiction is not automatically compulsory for every inter-state dispute and requires an applicable consent basis. Expanded peaceful-settlement methods in line with UN Charter Article 33. Added the self-determination context of UNGA Resolution 1514 (XV) while avoiding the claim that decolonisation automatically redraws all boundaries.
- **GIS and cartography:** defined ecological fallacy and the modifiable areal unit problem (MAUP) in both languages; retained UN M49 as a statistical grouping standard, not a determination of sovereignty or legal boundaries. Added safeguards against inferring individual political views from aggregated spatial data.
- **Pedagogy and bilingual parity:** checked the 17 paired teaching headings and corrected subsection order; expanded the glossary with bilingual definitions; aligned the worked turnout example, table, calculation steps and methodological caution in both languages; review questions 16/16, practical activities 5/5 and summary points 10/10.
- **Visual inventory:** seven unique bilingual IDs (10-A–10-G) remain placeholders. Added the missing Figure 10.1 caption for the world political map, renumbered the full set sequentially to Figures 10.1–10.7 and corrected the maritime-zones practical reference to Figure 10.3. No images were generated, fetched or integrated.
- **Chapter completion status:** non-visual scientific, legal-methodological, pedagogical and bilingual editorial work is complete for this pass. Overall chapter readiness is 85% because the seven visual assets and their subsequent asset review remain outstanding. Rendered-site/mobile/keyboard/screen-reader QA is deferred until visual integration and has not been claimed as complete.
- **Chapter commits:** `72b7f556f3c9e1de7bee7720a40d24f6dbff1635` (main editorial closure); `d8f7f389078c82ea2eeb903356292598b5ff5712` (final sovereignty/subsoil and decentralisation terminology refinement). **Readiness matrix commit:** `6736ba3c616416d9fe071a19f2d03e420253ed19`.
- **Primary source URLs checked:** https://www.un.org/depts/los/convention_agreements/texts/unclos/part2.htm ; https://www.un.org/depts/los/convention_agreements/texts/unclos/part5.htm ; https://www.un.org/Depts/los/convention_agreements/texts/unclos/part6.htm ; https://www.un.org/Depts/los/convention_agreements/texts/unclos/part7.htm ; https://www.un.org/depts/los/convention_agreements/texts/unclos/part10.htm ; https://www.un.org/depts/los/convention_agreements/texts/unclos/part11-1.htm ; https://mandates.un.org/mandate/A/RES/51/229 ; https://undocs.org/A/RES/63/124 ; https://odihr.osce.org/sites/default/files/f/documents/0/4/544240.pdf ; https://unstats.un.org/unsd/methodology/m49/ .


### Chapter 11 — Economic Geography: focused statistical-methods check — 5 November 2026

| Source / evidence | Result | Action / limitation |
|---|---|---|
| UN Statistics Division, ISIC Revision 5 | Verified — official classification record | UNSD records ISIC Rev. 5 as adopted in 2024 and explains that it updates activity categories to reflect structural changes and new activities. Chapter 11 now distinguishes Rev. 5 from the still-common Rev. 4 and requires classification/correspondence checks before cross-country or time-series comparisons. [Official classification record](https://unstats.un.org/unsd/classifications/Family/Detail/2095) |
| UN Statistics Division, System of National Accounts 2025 | Verified — official standard record | 2025 SNA was adopted by the UN Statistical Commission in 2025 as the update to 2008 SNA. Chapter 11 retains the warning to identify the SNA edition actually used by each national series; adoption does not mean every country has completed implementation. [2025 SNA](https://unstats.un.org/unsd/econstats/national-accounts/sna2025) |
| World Bank, current and constant price series | Verified — official methodological explanation | Chapter 11 now explicitly distinguishes the temporal price adjustment (current vs constant prices) from the spatial conversion by PPP, and requires the international-dollar basis/reference year to be stated. [World Bank explanation](https://datahelpdesk.worldbank.org/knowledgebase/articles/114942-what-is-the-difference-between-current-and-constan) |
| World Bank, value added and GDP | Verified — official methodological explanation | Added a bilingual explanation that GDP by the production approach sums gross value added and adds taxes less subsidies on products; the text warns against treating gross sales or exports as domestic value added. [World Bank explanation](https://datahelpdesk.worldbank.org/knowledgebase/articles/114948-what-is-the-difference-between-total-value-added-a) |
| World Bank ICP 2021 concepts and definitions | Verified — official methodology | Supports the distinction between market-exchange-rate comparisons and PPP-based volume comparisons. Chapter 11 now explains PPP as a spatial price-level adjustment rather than a synonym for real/constant-price GDP. [ICP concepts](https://www.worldbank.org/en/brief/2021/04/30/icp2021-concepts-definitions) |

**Chapter 11 corrections saved:** added ISIC Rev. 5 (2024) context in Russian and English; added a bilingual value-added/GDP explanation to prevent double counting; clarified that PPP and current/constant prices answer different comparison questions; updated the bibliography to place ISIC Rev. 5 first while retaining Rev. 4 as a legacy edition. This was a focused statistical-methods pass, not a full audit of every economic example, source or claim in Chapter 11. Country-specific numerical examples and all source-to-claim mappings remain to be checked.
