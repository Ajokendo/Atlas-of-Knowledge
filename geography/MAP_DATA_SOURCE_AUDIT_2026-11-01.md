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
