# Geography — Source and Evidence Closure Register

**Snapshot:** 2 November 2026  
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
| National Geographic Society, “What Is Geography?” | Corrected | The previous `/resource/geography/` URL returned 404. Replaced it with the current `/resource/what-geography/` page, which directly defines geography and discusses physical, human and biological systems and spatial perspective. |
| UN Statistics Division / UN-GGIM | Verified — access and relevance | The page identifies the UN geospatial-information-management initiative and its workstreams. Use it for geospatial governance/context, not as a general definition of geography. |
| ICA Cartographic Body of Knowledge | Verified — access and relevance | The working-group site and its Definitions page are available. Definitions page provides explicit definitions of map, cartography and cartographic mapping. |
| Longley et al., *Geographic Information Science and Systems* | Corrected | Completed the incomplete book reference with 4th edition, 2015, Wiley and ISBN 978-1-118-67695-0 using the publisher's catalogue. |
| National Research Council, *Rediscovering Geography* | Verified by authoritative publication record | National Academies Press record confirms the 1997 consensus report and DOI 10.17226/4913. Direct DOI retrieval by the browser was not successful, so the publisher landing page is the preferred verification route. |

**Chapter 01 edits saved:**
- AAG citation title made accurate.
- National Geographic URL repaired.
- Longley et al. bibliographic details completed.

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
| Legacy USGS fact-sheet / DOI endpoints in bibliography | Needs follow-up | Some direct endpoints were not retrievable in this pass. A 403/redirect failure is not enough to call them dead; retain the alternatives already documented in the chapter audit and resolve at the final reference-by-reference pass. |

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
