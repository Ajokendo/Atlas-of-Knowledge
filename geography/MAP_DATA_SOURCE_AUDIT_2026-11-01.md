# Kyrgyzstan map-data source audit — 1 November 2026

**Repository:** `Ajokendo/Atlas-of-Knowledge`  
**Branch:** `workspace/geography`  
**Scope:** source discovery and cartographic reference-system controls. This note does not certify any boundary, geological, hydrological, climate, biodiversity or protected-area geometry.

## Findings

### 1. Published geographic coordinates and vertical reference

The Kyrgyz Republic's Aeronautical Information Publication, GEN 2.1, effective 6 August 2026, states that published geographic latitude/longitude coordinates are expressed in WGS 84. It also describes the vertical reference for international aeronautical purposes and notes the use of the long-term mean Baltic Sea level as the vertical reference in Kyrgyzstan. This is an authoritative, dated national publication, but its vertical-reference statement is explicitly in the aeronautical context; it must not be generalized to every elevation dataset without checking metadata.

Source: https://ais.ansp.kg/eaip/2026-08-06-AIRAC/html/eAIP/UC-GEN-2.1-en-GB.html

### 2. National projected coordinate system

Government Resolution No. 235 of 7 October 2010 establishes the national Kyrg-06 coordinate system, based on ITRF2005 and a multi-zone Transverse Mercator arrangement. The accessible legal reproduction describes five 3-degree zones and their central meridians. This is a projected national mapping system and must not be confused with the WGS 84 geographic-coordinate convention stated in the AIP.

Accessible legal text: https://prg.kz/document/?doc_id=30830262

A government land-resources agency notice about the geospatial infrastructure pilot describes coordinate transformation between the state coordinate system and WGS 84 and a central control-point information system. This supports treating transformation parameters and control-point metadata as a required part of any overlay workflow, not assuming that similarly named coordinates are interchangeable.

Government source: https://gosreg.gov.kg/ru/?p=8013

### 3. Administrative-boundary data availability

The UN Geospatial Information Section / Statistics Division SALB country page identifies the State Agency of Cartography & Geodesy as Kyrgyzstan's National Geospatial Information Authority, but currently lists no downloadable geospatial datasets. Therefore, the page is useful for identifying the national authority, not as a boundary-data source.

Source: https://salb.un.org/en/data/kgz

The UN OCHA/HDX Common Operational Dataset of subnational administrative boundaries is described in the 2026 source catalogue as sourced from the Kyrgyz Republic Ministry of Emergency Situations, with P-codes and CC BY 3.0 IGO licensing. It is a useful candidate for operational/reference comparison, but the actual dataset version, administrative date, geometry and licence record must be inspected before production use. It must not automatically be labelled as the legally authoritative national boundary layer.

Catalogue: https://www.technicalgis.com/data-sources/kyrgyzstan/

The World Bank Official Boundaries catalogue records an update on 21 October 2026 and provides Admin 0/1/2 formats plus maintenance logs. This is a current international comparison source, not a substitute for legal confirmation by the Kyrgyz national authority.

Source: https://datacatalog.worldbank.org/search/dataset/0038272/world-bank-official-boundaries

### 4. National geospatial portals

The State Agency for Land Resources' GISMSU portal identifies itself as an information system for municipal resource management. Its presence does not, by itself, establish that all national-level boundaries or thematic layers are downloadable or legally certified for atlas publication.

Portal: https://geoaymak.gov.kg/

The Government land-resources agency has also described the Kyrgyzmap and NSDI geoinformation/climate-data portals as part of the national geospatial infrastructure. Availability, metadata, layer dates, access terms and download endpoints must be checked directly for each intended layer.

Government notice: https://gosreg.gov.kg/ru/?p=2002

## Cartographic controls to apply to the atlas

1. Record coordinate reference system (CRS), datum, projection, zone, units and transformation for every source layer.
2. Do not conflate WGS 84 latitude/longitude with the national projected Kyrg-06 system.
3. Record the vertical datum and elevation source independently from the horizontal CRS.
4. For administrative maps, record source authority, legal/administrative effective date, level, P-codes, version, licence and any disputed/undetermined boundary treatment.
5. Compare operational datasets (e.g. OCHA/HDX) with national-authority records; do not call a third-party boundary file legally authoritative without confirmation.
6. For thematic layers, record dataset version/date, scale or resolution, generalisation, classification method and known omissions.
7. Preserve a source/data note in each finished map's metadata and bilingual caption.

## Open items

- Obtain or verify the current official national administrative-boundary dataset and its legal effective date.
- Confirm access to the official national geodetic control-point and coordinate-transformation metadata.
- Verify the precise official source and datum for the extreme-point coordinates in Chapter 17.
- Validate geological, hydrographic, climate, biodiversity and protected-area geometries against their responsible national agencies and dated source metadata.
- Do not mark any map asset complete until the data, geometry, projection, licence, bilingual labels and scientific review have been recorded.

**Status:** authoritative reference-system sources identified and cross-distinguished; official thematic map geometries remain unverified.

## Legal and national toponymic-source update — 1 November 2026

### Law No. 58 of 29 April 2026

The Kyrgyz Republic adopted Law No. 58, “On Geodesy, Cartography and Spatial Data”, dated 29 April 2026. The accessible text confirms that it regulates the collection, storage, processing, provision and dissemination of spatial data and defines an atlas, basic spatial data, a vertical reference system, geoportals and geoservices. The legal reference is now included in Chapter 17. The law's entry-into-force date should be taken from the official consolidated legal record; secondary reproductions surfaced inconsistent dates, so this audit does not state an effective date.

Official legal database: https://cbd.minjust.gov.kg/230045410/edition/52293/ru
Readable text / article preview: https://prg.kz/document/?doc_id=39403056

### National geographical-names information system

The state register of information systems identifies the AIS “Geographical Names of the Kyrgyz Republic” (AIS GN), with Goskartografia recorded as owner and technical operator. Its registry description reports 10,281 georeferenced geographical features and identifies Kyrgyzmap (https://www.kyrgyzmap.kg) as the portal. The record shows registration on 23 August 2023, operation start on 30 April 2022, and last modernisation on 31 December 2022. This is useful evidence of a national toponymic resource and its institutional ownership, but the record's old modernisation date means it does not prove that every entry is current or that every layer is openly downloadable today.

State register record: https://bgir.tunduk.kg/Category/InformationSystem/Details?id=223

### Editorial implications

- Chapter 17 now cites the 2026 law and the state-register record for AIS GN in both language versions.
- Use AIS GN/Kyrgyzmap as a national toponymic verification route; check each name, spelling, location and record date rather than copying a bulk count as current fact.
- Do not use the toponymic database as proof of state-border geometry or extreme-point coordinates.
- Every finished map must retain source metadata, coordinate reference system, vertical reference where relevant, source date, licence/conditions and review status.
- Extreme-point coordinates remain unapproved until confirmed against a national geodetic/cartographic source.


## National geodetic transformation infrastructure — official update

On 11 November 2025, the State Agency for Land Resources, Cadastre, Geodesy and Cartography reported completion of a pilot consulting project on transition to a global geodetic system and improvement of land-information management. The agency states that geodetic, gravimetric and levelling measurements were carried out; coordinate-transformation parameters were determined; **maps were partially reprojected**; and two information systems were created and introduced:

- a system for transforming the state coordinate system to WGS 84;
- a control-point management system, described as a centralised geodetic-control database with updating and real-time visualisation capability.

Official agency report (11 November 2025): https://gosreg.gov.kg/ru/?p=8013

### Interpretation and limitations

This is stronger national evidence than merely citing the 2010 Kyrg-06 resolution: it confirms that transformation parameters and a control-point information system have been developed and that a pilot implementation was reported. However, the agency explicitly says that map reprojection was **partial**. The announcement does not publish the numerical transformation parameters, accuracy statistics, epoch details, geoid/height model, control-point coordinates, service endpoint or dataset-level migration status.

Therefore:
1. Do not assume that every legacy Kyrg-06 layer has already been converted to WGS 84.
2. Do not perform an ad hoc datum transformation using generic software defaults when national parameters are available or required.
3. For each layer, record its source CRS, target CRS, transformation operation and parameter/version, coordinate epoch where applicable, horizontal accuracy, vertical reference and transformation date.
4. Request or verify the authoritative transformation parameters and control-point metadata from the national agency before precision mapping or survey-grade use.
5. Treat the 2025 announcement as evidence of implemented pilot infrastructure, not as a public release of all transformation data or proof that every national dataset has migrated.

## Other discovered spatial-data catalogues — availability is not authority

- The CAIAG GeoNode landing page advertises 52 layers, 5 maps and 6 documents, with OGC-connected data and downloadable standard formats. This is a useful research/discovery repository, but the landing-page count does not establish that each layer is official, current, complete or suitable for national boundary depiction. Inspect each layer's owner, metadata, licence, CRS, date and lineage. Portal: https://geonode.caiag.kg/
- The GISMSU portal identifies itself as a municipal-resource management information system. Do not assume it is a complete national boundary or thematic-data download service without layer-specific evidence. Portal: https://geoaymak.gov.kg/
- The state-register entry for AIS “Geographical Names of the Kyrgyz Republic” remains a separate national toponymic source. Its recorded last modernisation date is 31 December 2022; verify individual names and current portal functionality before relying on the entries.

## Revised status of the coordinate-system workstream

**Confirmed:** Kyrg-06 is established by Resolution No. 235; the national agency reported a WGS 84 transformation pilot, derived parameters, partial map reprojection and deployment of transformation/control-point systems.

**Not yet confirmed from public source material:** numerical transformation parameters, control-point dataset/service, transformation accuracy and epoch, vertical model, and full migration status of national map layers.

**Cartographic decision:** retain the CRS/transformation blocker for precision maps until the required official metadata are obtained. Do not downgrade this blocker merely because the pilot project was announced.


## Historical national geospatial baseline and vertical datum — UNESCAP cross-check

A UNESCAP analytical report, *Current state of land statistics and its relevant challenges in leveraging statistical and geospatial data in Central Asia* (December 2020), provides a useful dated baseline for Kyrgyzstan's national geospatial reference framework. In its Kyrgyz Republic analysis (section 5.1.2, printed page 16), it records:

- Kyrg-06 was introduced in 2010, based on ITRF-2005 and described as compatible with WGS-84;
- the national geodetic network includes points of different accuracy classes, including GNSS-based networks;
- the **1977 Baltic Altitude System** was reported as operating in Kyrgyzstan, implemented by high-precision levelling networks;
- Soviet-era topographic maps existed in SK-42 / Gauss–Krüger, based on the Krasovsky ellipsoid, at scales from 1:10,000 to 1:1,000,000;
- a transition to Kyrg-06 / five three-degree Transverse Mercator zones was underway, and the report noted that public information on map-update status and regulatory update dates was unavailable at the time.

Report: UNESCAP, December 2020, *Current state of land statistics and its relevant challenges in leveraging statistical and geospatial data in Central Asia*, section 5.1.2, pp. 15–16 (PDF pages 15–16): https://www.unescap.org/sites/default/d8files/knowledge-products/Analytical%20Report_Current%20state%20of%20land%20statistics%20and%20its%20relevant%20challenges%20in%20leveraging%20statistical%20and%20geospatial%20data%20in%20Central%20Asia%20_ENG_0.pdf

### Cross-check against the current national AIP

The Kyrgyz AIP, GEN 2.1, effective 6 August 2026, states that published latitude/longitude coordinates are expressed in WGS 84. Its vertical-reference note says that the geoid model is not used and that the long-term mean Baltic Sea level is used as the vertical reference in the Kyrgyz Republic. The AIP presents this in its aeronautical reference context; it should not be generalized automatically to every DEM, engineering survey or historical height dataset.

AIP GEN 2.1 (effective 6 August 2026), sections 3–4: https://ais.ansp.kg/eaip/2026-08-06-AIRAC/html/eAIP/UC-GEN-2.1-en-GB.html

### Editorial interpretation

1. The 2020 UNESCAP report is a **historical baseline**, not proof of the current status of every national network or map series. The 2025 national-agency announcement of the WGS 84 transformation pilot is newer evidence of implementation, but says map reprojection was partial.
2. The report's “1977 Baltic Altitude System” and the 2026 AIP's “long-term mean Baltic Sea level” are consistent at a broad datum-family level, but the sources do not establish that every national vertical dataset uses an identical realization, benchmark network, epoch or conversion model. Verify the exact vertical datum and benchmark lineage for each dataset.
3. Keep horizontal CRS and vertical reference as separate metadata fields. A dataset may use WGS 84 horizontal coordinates while retaining heights referenced to a national Baltic-based vertical datum; this does not make its heights ellipsoidal WGS 84 heights.
4. Legacy SK-42 / Gauss–Krüger maps must not be assigned Kyrg-06 or WGS 84 merely by relabelling. Their original zone, sheet metadata, datum, map edition, control points and transformation method must be identified.
5. For DEM comparison, glacier change, river gradients, engineering or hazard mapping, record whether heights are orthometric/normal/ellipsoidal as applicable, the vertical datum, geoid/quasigeoid model if used, and the source's vertical accuracy. Do not mix vertical references without a documented conversion.
6. The five-zone Kyrg-06 framework established by Resolution No. 235 must be distinguished from the six-degree Gauss–Krüger legacy mapping system. Zone boundaries and the correct EPSG CRS must be selected from the source metadata, not guessed from the location alone.

**Status update:** the broad national vertical-reference family and the existence of legacy SK-42 mapping are now supported by a dated UNESCAP report and cross-checked against the 2026 AIP. Dataset-level vertical realization, benchmark lineage, map-sheet migration and transformation accuracy remain open.


## DEM, geological-map and glacier-data availability check — 1 November 2026

### CAIAG GeoNode: a specific 30 m DEM layer

The CAIAG GeoNode catalogue exposes a raster layer titled `Kyrg_AsterTM2_DEM_utm`, described as **ASTER GDEM 30 m**, published 10 December 2021. Its metadata identifies CAIAG and a responsible contact, shows a projected CRS as EPSG:32643 in the detailed metadata, and provides WMS/WCS and GeoTIFF download options. However:
- the licence is explicitly **Not Specified**;
- the abstract contains only the short product label;
- no vertical datum, geoid model, vertical accuracy, processing lineage, source version or validation report is supplied on the public metadata page;
- the layer is not currently used in any published map in that GeoNode record.

Therefore, treat it as a discoverable candidate for exploratory terrain visualisation, not as a cleared or validated authoritative DEM for quantitative elevation, glacier-change, engineering or hazard analysis. Confirm the CRS against the actual raster's GeoTIFF tags before use; the EPSG entry in the catalogue alone does not establish the vertical reference.

Metadata page: https://geonode.caiag.kg/layers/geonode:Kyrg_AsterTM2_DEM_utm/metadata_detail

### RESILAND: higher-resolution DEM procurement for priority sites

CAREC reported on 16 April 2026 that DEMs had been procured for the Department for Monitoring and Forecasting of Emergency Situations under the Kyrgyz Ministry of Emergency Situations. The report describes coverage of approximately **6,000 hectares across 14 priority sites**, with spatial resolution **up to 3 m**, for debris-flow, flood and landslide modelling.

This is important evidence that high-resolution terrain data are being acquired for operational disaster-risk work. It is not evidence of a seamless national 3 m DEM, nor does the public announcement provide downloadable rasters, site polygons, acquisition dates, sensor/survey method, horizontal CRS, vertical datum, accuracy statistics or licence. Do not extrapolate these 14 sites to countrywide coverage.

Source: CAREC, 16 April 2026, RESILAND Kyrgyz Republic DEM procurement announcement: https://carececo.org/en/main/news/news/proekt-resiland-kyrgyzstan-usilivaet-potentsial-dmpchs-priobreteny-tsifrovye-modeli-relefa/

### National Geological Atlas project — current publication status

The Ministry of Natural Resources announced on 11 March 2026 that it and the M. M. Adyshev Institute of Geology of the National Academy of Sciences were preparing a two-volume **Atlas of Geological, Geophysical and Mineragenic Maps of the Kyrgyz Republic**, in Russian and English. The announcement describes a working meeting and the project objectives; it does not announce completed publication or open GIS data delivery.

This is a promising national reference project. Until the volumes and their map legends/metadata are publicly available and reviewed, it should be cited as a work in preparation, not as an already published atlas or downloadable national geodatabase.

Source: Ministry of Natural Resources, 11 March 2026: https://mnr.gov.kg/ky/posts/news/minprirody-iniciiruet-izdanie-atlasa-geologiceskix-kart-kyrgyzstana

### Glacier inventory and chronology caution

CAIAG's glaciology page notes that the USSR Glacier Catalogue (1968–1982) and the 1:500,000 “Present Glaciation” map based on 1977–1980 satellite imagery remain important historical references, but that the information was rarely updated in later years and only for some glaciers. The page explicitly identifies remote sensing and renewed large-scale observation as necessary for contemporary glacier-dynamics assessment.

Accordingly, the historical catalogue/map may support historical context and baseline comparisons only when dates and inventory definitions are explicit. It must not be represented as a current glacier inventory. For contemporary maps, record imagery date/season, cloud/snow conditions, glacier delineation criteria, debris-covered ice treatment, minimum mapping unit, positional uncertainty and validation method.

Source: CAIAG, Glaciology: https://caiag.kg/en/2/142-glaciology

### Geological-map access route

The Ministry's current website links to the Kyrgyz Geological Survey (https://www.geology.kg/) as its subordinate specialist body. The Kyrgyzstan Geoportal's geological-maps page says maps can be ordered from the Kyrgyz Methodological Expedition of Geological and Economic Research; this is an access route, not proof that the maps are freely downloadable or licensed for republication. The Ministry's March 2026 national-atlas announcement is the stronger current signal of a coordinated geological cartography initiative.

### Editorial and cartographic decisions

1. Use the CAIAG ASTER GDEM layer only as a provisional 30 m candidate, pending licence and raster-level metadata verification.
2. Describe the RESILAND 3 m DEMs as high-resolution, site-specific datasets (14 priority sites; approx. 6,000 ha), not as national coverage.
3. Mark the national Geological/Geophysical/Mineragenic Atlas as **in preparation** on the basis of the 11 March 2026 Ministry announcement; do not cite unpublished maps as if consulted.
4. Treat the 1968–1982 glacier catalogue and 1977–1980 map as historical sources; do not use them alone for present-day glacier counts, areas or change rates.
5. Every production DEM used in the Atlas must pass a metadata gate: licence, source/edition, acquisition date, spatial resolution, horizontal CRS, vertical datum/height type, geoid model, vertical and horizontal accuracy, processing lineage, and validation against suitable control data.

**Status:** a specific public 30 m candidate and a documented 3 m/14-site operational procurement have been identified. Neither provides sufficient public metadata to clear a DEM for quantitative national Atlas production. The national geological atlas is confirmed as a project, not yet as a published source in the inspected announcement.


## Climate observation and glacial-lake datasets — 1 November 2026

### Kyrgyzhydromet national climate products

The official Kyrgyzhydromet climate-products page publishes two distinct analyses that should not be conflated:

**A. Homogenised monthly station series, 1980–2021.** The temperature/precipitation trend analysis uses monthly homogenised data from 22 stations for 1980–2021. For 1981–2021, it reports a countrywide mean annual temperature trend of about +0.28 °C/decade (regional values about +0.25 to +0.32 °C/decade) and a spring trend of about +0.59 °C/decade. Annual precipitation trends are described as small, mixed by region and statistically insignificant; the countrywide estimate is around +4 mm/decade. The page explicitly warns that Naryn regional estimates use only two stations.

**B. Climate indices, 1980–2022.** A separate set of 11 climate products uses daily Tmin, Tmax, precipitation and relative humidity from 13 stations. It includes frost/cold days, growing-season dates and duration, accumulated temperatures, heat/cold waves, operational meteorological drought, zero-degree crossings and forest-fire danger. The service reports positive trends in growing-season duration and accumulated warmth, most of which are statistically significant; cold-season indicator trends are not statistically significant in this analysis. Statistical trend assessment of forest-fire danger was not possible because humidity records covered only 2013–2022. The operational drought definition is method-specific and must not be confused with SPI/SPEI, agricultural drought or hydrological drought.

Official source: Kyrgyzhydromet, Climate Products: https://www.meteo.kg/ru/pages/ClimateProducts

### Editorial implications for climate maps

1. Keep the 22-station monthly series and 13-station daily-index series separate, stating period, station count, variables, homogeneity processing and method.
2. Do not portray +0.28 °C/decade as the warming rate at every elevation or for every later period. It is a countrywide station-based estimate for 1981–2021.
3. Do not state that precipitation is uniformly increasing or decreasing: the official analysis describes regional differences and statistically insignificant trends.
4. Maps of climate indices must publish the exact threshold/definition. The national operational drought index is not a substitute for SPI/SPEI or soil-moisture/hydrological drought.
5. For interpolation, document station elevation and distribution; sparse high-mountain coverage limits confidence in gridded values across complex terrain.

### National glacial-lake inventory research, 2022–2024

A 2025 EGU contribution by Piroton and Havenith describes a polygon-based research inventory from Sentinel-2 imagery acquired in July–October 2022–2024. The authors report more than 2,000 glacial lakes across Kyrgyzstan, with 1,137 in the Terskey range and 323 in the Kyrgyz Range. The record describes manual polygon review and field validation at selected sites, while also identifying false-positive risks from shadows, clouds, residual snow, seasonal depressions and water turbidity.

This is a research/conference contribution, not a state-adopted register. The public record does not itself establish open reuse rights for the full vector inventory. Cite the lake count with its study dates, method and publication status; do not call it an official permanent total.

Source: https://doi.org/10.5194/egusphere-egu25-19362

### 2026 peer-reviewed Kyrgyz Range lake dynamics

A 2026 *Natural Hazards and Earth System Sciences* paper analyses the Kyrgyz Range over 1968–2021. It reports lake count rising from 274 to 412 and total lake area from 0.80 to 1.42 km² (+76%), while glacier area fell from 378.5 to 262.0 km² (−31%). Many lakes disappeared and others formed on degrading glacier-moraine complexes and buried-ice terrain. The findings are range-specific, not a national Tien Shan-wide estimate.

Source: https://doi.org/10.5194/nhess-26-1001-2026

**Cartographic implication:** separate glacier polygons, glacier-moraine complexes and glacial-lake polygons; preserve observation dates and inventory definitions. GLOF risk mapping must additionally consider dam type/stability, drainage pathways, downstream exposure and uncertainty; lake presence or area alone is not a risk classification.
