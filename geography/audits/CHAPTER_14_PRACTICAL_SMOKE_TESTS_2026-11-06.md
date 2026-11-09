# Chapter 14 — computational smoke tests for six practical activities

**Date:** 6 November 2026  
**Branch:** `workspace/geography`  
**Scope:** computational checks of the underlying GIS concepts using small synthetic fixtures. These are not QGIS Processing execution tests and do not validate the official QGIS training-data files.

## Environment and boundary

The available runtime had Python 3, GeoPandas 1.1.2, Shapely 2.1.2, Rasterio 1.5.0 and NetworkX 3.6.1. QGIS Desktop, `qgis_process`, PyQGIS and GDAL command-line utilities were not available. Therefore no `native:*` or `gdal:*` QGIS Processing algorithm was launched. No official training ZIP or project was downloaded/opened. Results below are synthetic logic checks only.

## Results

| Activity | Synthetic check | Result | Status |
|---|---|---|---|
| 1. Thematic map / join | Three polygon features joined to a CSV-like table by stable key; one polygon key and one table key deliberately unmatched | 2 matched records; unmatched polygon key C and unmatched table key X both detected; no match silently converted into a value | PASS — join logic only |
| 2. Vector and raster | 2×2 synthetic GeoTIFF in EPSG:3857 inspected alongside one polygon | Raster dimensions 2×2, cell size 1×1, bounds 0–2 in both axes, NoData −9999, CRS preserved | PASS — raster metadata/overlay fixture only |
| 3. Service accessibility | Synthetic undirected graph with five nodes and five weighted edges; Euclidean buffer also calculated | Shortest route S–A–B–T, cost 3; nodes reachable from S within cost 2: S, A, B, C; radius-1 buffer area ≈3.136548 | PASS — graph and buffer concepts only; not QGIS routing |
| 4. Terrain | Analytical plane z = 2x + y | Slope = 65.905157°; downslope aspect azimuth = 243.434949° | PASS — analytical formula only; not a DEM-processing comparison |
| 5. Data quality | Self-intersecting bow-tie polygon and separate adjacent-polygon gap/overlap fixtures | Bow-tie geometry invalid (self-intersection); 0.1-unit gap and 0.1-unit overlap separately detected | PASS — validates the distinction between geometry validity and coverage topology |
| 6. Reproducible project | Project-like manifest with relative path `./data/input.csv`; project folder copied to a different directory | Referenced data file remained resolvable after moving the folder | PASS — relative-path portability principle only |

## Interpretation

- The six conceptual smoke tests passed.
- The tests support the chapter's safeguards: stable join keys and explicit unmatched records; no accuracy inference from raster cell size; network reachability distinct from straight-line buffers; explicit slope units; geometry validity distinct from inter-feature coverage topology; and relative-path portability.
- These tests do **not** prove that the named QGIS 3.44 algorithms, dialogs, output schemas or official sample projects work as described in QGIS Desktop.
- Before this chapter can receive a software-execution sign-off, run the six activities in QGIS 3.44 against the official training package, record software/provider versions, retain output layers and screenshots, and test the moved QGZ project on a clean machine/profile.
- No Kyrgyzstan-specific network, DEM, administrative-boundary or service-location dataset was tested.

**Readiness decision:** Chapter 14 remains **78%**. The computational smoke tests improve confidence in the underlying concepts but do not close live QGIS execution, local-data validation, full source-to-claim review, bilingual line editing or release accessibility/device QA.
