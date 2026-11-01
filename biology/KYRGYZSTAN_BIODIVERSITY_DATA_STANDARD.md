# Kyrgyzstan biodiversity records: editorial data standard

**Version:** 1.0  
**Date:** 1 November 2026  
**Applies to:** `flora-kyrgyzstan.html`, `fauna-kyrgyzstan.html`, future regional species profiles, maps, tables and illustrations.

This is an editorial standard for how the Atlas describes evidence. It is not a national monitoring protocol, legal classification or replacement for taxonomic and conservation assessments.

## 1. Keep five evidence labels distinct

Use one of the following labels in a species profile or locality record. The labels describe the strength and geographic scope of evidence; they are not conservation categories.

| Editorial label | Meaning | What the Atlas may claim |
|---|---|---|
| **Confirmed local record** | Dated primary evidence (diagnostic photograph, specimen/voucher, validated camera-trap record, sound record or equivalent) with a locality that can be checked. | Presence at the documented site and date, within the stated uncertainty. |
| **Verified published local record** | A traceable scientific or official source reports the taxon at a named site or defined area. | Presence as reported by that source; retain its date, method and limitations. |
| **Historical record** | A credible older publication, collection or survey reports the taxon, but no recent confirmation is available in the material reviewed. | Historical occurrence only; do not imply current occupancy. |
| **National checklist record** | A national or country-level checklist includes the taxon without establishing an oblast, reserve, basin or site. | Country-level inclusion only; do not assign the taxon to a local chapter subsection or image. |
| **Unverified report / potential habitat** | An anecdotal report, broad habitat suitability statement or record lacking sufficient taxonomic or locality evidence. | A research lead or potential habitat, never a confirmed occurrence or species count. |

If the evidence is mixed, use the more cautious label and explain why. A blank field is preferable to an invented locality, date or confidence score.

## 2. Minimum record fields

For each occurrence or field survey, capture as many of these fields as the source permits:

- Accepted scientific name, taxonomic rank, naming authority where available, and synonym used by the original source.
- Observation/event identifier and evidence type (human observation, preserved specimen, photograph/video, camera trap, acoustic record, track/sign, genetic sample or eDNA).
- Date or date interval, observer/collector, identifier and date of identification.
- Country, oblast, district, named site, drainage basin/ecoregion and coordinates where safe to publish.
- Coordinate reference system and coordinate uncertainty; use generalized coordinates or withhold sensitive locations when disclosure could increase disturbance or collection risk.
- Elevation and measurement method, habitat description and relevant season/weather context.
- Number of individuals only where the method supports counting individuals; distinguish individual count from number of records/detections.
- Sampling protocol and effort (route length/time, camera-days, trap effort, number of samples or survey area).
- Source citation, dataset/collection identifier, access date and known limitations.

GBIF's occurrence-data guidance identifies fields such as `occurrenceID`, `basisOfRecord`, `scientificName` and `eventDate` as core record elements; coordinates and coordinate uncertainty are strongly recommended where available. Sampling-event data additionally need the event date, protocol and sampling effort. The Atlas uses this as a data-quality reference, not as a claim that every historical source supplies every field.

## 3. Taxonomy and naming

1. Display one accepted scientific name consistently in the main text and image captions.
2. Retain an older or alternate name as a synonym only when it helps readers connect the Atlas entry to the cited source.
3. State the taxonomic authority or database and the date checked for disputed or recently revised taxa.
4. Do not silently convert subspecies or species-complex names into a more precise taxon than the source supports.
5. A DNA barcode or eDNA signal is evidence to be interpreted with reference libraries, contamination controls, sampling design and taxonomic expertise; it does not automatically settle every identification.

## 4. Counts, trends and survey results

Always distinguish:
- **records/detections** — how many times evidence was recorded;
- **individuals counted** — how many organisms were distinguished during a survey;
- **index of activity/relative abundance** — a standardized measure tied to a stated method;
- **population estimate** — an estimate with method, area, date, assumptions and uncertainty;
- **national checklist total** — a taxonomic compilation whose scope and version must be stated.

Do not compare figures from different areas, years or methods as if they were one time series. A camera-trap image count is not a population estimate. A short field sample is not a complete inventory. A country-level total is not an oblast total.

## 5. Conservation categories are separate systems

- State the assessment system: national Red Data Book, IUCN global Red List, or another named regional assessment.
- Give the category, assessment year/version and source.
- Do not transfer an IUCN global category into a national legal status, or vice versa.
- A species being legally protected does not by itself establish its global threat category; a global IUCN category does not automatically establish the exact wording of Kyrgyz national law.
- Where the national Red Data Book is being revised (2026–2028 project), identify the edition/date behind any quoted national listing.

The IUCN Red List categories and criteria are a formal global extinction-risk assessment system. They are not a substitute for documenting a local sighting or local population trend.

## 6. Plant and animal safeguards

### Plants
- Photograph the whole plant and diagnostic parts without uprooting or damaging it.
- Record flowering/fruiting stage and microhabitat.
- A herbarium voucher should be collected only when scientifically justified and all permits and site rules allow it.
- Do not publish exact coordinates for vulnerable populations if this could facilitate collection or trampling.

### Animals
- Keep direct sightings, camera-trap records, tracks, scat, acoustic records and eDNA results as separate evidence types.
- Record survey effort and independence rules for repeated detections.
- Do not approach nests, dens or young, bait wildlife, or disclose sensitive den/nest locations.
- Do not infer sex, age, breeding or individual identity unless diagnostic evidence supports it.

## 7. Map and illustration rules

- A distribution map must distinguish confirmed points, historical points, broad range polygons and potential habitat in its legend.
- Never derive a precise range boundary from a few occurrence points.
- Do not plot sensitive localities publicly at full precision.
- A regional habitat illustration may combine several representative ecological settings only if captioned as a composite/illustrative scene.
- A species may appear in an oblast illustration only when the chapter provides evidence at an appropriate geographic scale.

## 8. Review checklist before publication

- [ ] Evidence label matches the source and its geographic precision.
- [ ] Scientific name, synonym and rank are consistent.
- [ ] Date, locality and method are retained from the source.
- [ ] Detections, individuals, estimates and checklist totals are not conflated.
- [ ] National and global conservation categories are clearly distinguished.
- [ ] Sensitive coordinates and vulnerable populations are protected.
- [ ] Map, caption, alt text and illustration do not imply unsupported co-occurrence or distribution.
- [ ] Russian and English versions communicate the same level of certainty.

## Reference standards

- GBIF, [Data quality requirements: occurrence datasets](https://www.gbif.org/data-quality-requirements-occurrences).
- GBIF, [Data quality requirements: sampling-event datasets](https://www.gbif.org/data-quality-requirements-sampling-events).
- GBIF, [Occurrence download formats and Darwin Core fields](https://techdocs.gbif.org/en/data-use/download-formats).
- IUCN, [Guidelines for Using the Red List Categories and Criteria](https://nrl.iucnredlist.org/resources/redlistguidelines).

**Editorial status:** adopted as the working standard for the two Kyrgyzstan biodiversity chapters. It does not certify individual species records; each record still needs source-level verification.
