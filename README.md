# Climate, geospatial and alternative data course

## General objective

Help students with basic Python/pandas experience, but no geospatial or climate-analytics background, understand spatial data, inspect climate measurements, and apply them to transparent questions in private-market analysis. Students learn to choose formats, connect assets to locations, preserve missing-data information, compare climate periods, and explain the limits of a screening result.

## Two parts

1. **[Alternative Data - Climate and Geospatial](<Alternative Data - Climate and Geospatial/README.md>)** is the newly authored teaching module. Six independently runnable notebooks follow a fictional property/infrastructure portfolio from tables to maps, climate grids and an operational due-diligence screen. It includes student exercises, instructor answers, HTML reading copies and bundled data.
2. **[Geospatial Learning](<Geospatial Learning/README.md>)** is the supporting collection: 11 original Week 8–9 lecture notebooks and 27 selected Planet tutorials. It extends the course into interactive maps, remote sensing, raster processing, COGs and STAC.

## Start here

- Open [the introductory notebook](<Alternative Data - Climate and Geospatial/notebooks/00_Start_Here_Alternative_Data.ipynb>), then proceed through 01–05.
- For reading without installation, download the repository and open [the HTML index](<Alternative Data - Climate and Geospatial/html/index.html>) locally. GitHub displays HTML as source rather than running it as a lesson page.
- Share [student-pack.zip](<Alternative Data - Climate and Geospatial/student-pack.zip>) for the new course without instructor answers.
- Teachers: use [the teaching guide](<Alternative Data - Climate and Geospatial/instructor/TEACHING_GUIDE.md>) for a three-hour workshop or a week with independent exercises.

## What students should learn

1. Distinguish a direct measurement from a proxy and an investment inference.
2. Recognize CSV, GeoJSON, Shapefile, GeoPackage, GeoTIFF and NetCDF.
3. Use geometry, coordinate reference systems, spatial joins and distances correctly.
4. Inspect raster resolution, metadata and missing cells before sampling assets.
5. Distinguish weather, climate, reanalysis and projections; state units and reference periods.
6. Communicate portfolio data coverage, test an explicit screening rule and identify the next evidence needed.

## Setup and status

The new module's README explains environment installation and Jupyter startup. Create your own environment; no local `.venv` is tracked. Its six notebooks have recorded successful execution and semantic checks in [VALIDATION.md](<Alternative Data - Climate and Geospatial/VALIDATION.md>). The supporting historical notebooks have been organized and integrity-checked, but have not all been execution-tested with current packages. Some require additional data, credentials or updates to old APIs.

All portfolio and climate values in the new case are **synthetic teaching data**; they do not describe actual properties or Houston climate. A separate real satellite image is used only to inspect raster structure. See the [data dictionary](<Alternative Data - Climate and Geospatial/data/DATA_DICTIONARY.md>) for provenance and limitations.

Original third-party licenses and source documentation are retained. No new license is asserted over all collected materials. API keys, virtual environments, runtime caches and notebook checkpoint backups are excluded. Original source files remain in the local working collections; the publication copy keeps the two course folders together so relative paths continue to work.

One embedded Google API key in the historical COG part 3 notebook was replaced with `REDACTED_API_KEY` in the publication copy. The publication manifest records the change and both original and published hashes. The older move/copy manifest remains a historical record of the local originals.

## File guide

See [FILE_GUIDE.md](FILE_GUIDE.md) for a description of every included file.
