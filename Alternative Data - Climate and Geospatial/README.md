# Alternative Data: Climate and Geospatial

## A practical introduction for private-markets students

Six guided notebooks for students from finance, business, policy, engineering and other disciplines who have basic Python experience but are new to geospatial and climate analytics. Assume familiarity with variables, imports, DataFrames, filtering, groupby and basic plotting; no GIS, remote-sensing or climate-science background is needed. Students learn to inspect geospatial data, ask climate questions and communicate what the evidence can and cannot support.

**Start with [00 — Alternative data](notebooks/00_Start_Here_Alternative_Data.ipynb).** For a no-install reading experience, open the corresponding file in [html](html). These HTML versions include executed tables and figures; changing code requires Jupyter.

## Learning path

| Notebook | Approx. time | What students do |
|---|---:|---|
| [00 — A different lens on an asset](notebooks/00_Start_Here_Alternative_Data.ipynb) | 15 min | Frame a question, inspect portfolio coverage, separate proxy from measurement |
| [01 — Formats and first map](notebooks/01_Data_Formats_and_First_Map.ipynb) | 35 min | Inspect CSV, GeoJSON, Shapefile and GeoPackage; map points, a line and polygons |
| [02 — Location joins and distance](notebooks/02_Location_Joins_and_Distance.ipynb) | 35 min | Match assets to areas and measure proximity in a projected CRS |
| [03 — Rasters, images and exposure](notebooks/03_Rasters_Images_and_Exposure.ipynb) | 35 min | Open GeoTIFFs, inspect metadata, sample values, retain missing data |
| [04 — Climate, time and uncertainty](notebooks/04_Climate_Time_and_Uncertainty.ipynb) | 40 min | Open NetCDF, convert units, compare periods and count hot days |
| [05 — Due-diligence lab](notebooks/05_Private_Markets_Due_Diligence_Lab.ipynb) | 35 min | Test a screening rule and write a short evidence-based memo |

The full guided path is about **195 minutes**, plus breaks. Each notebook imports its own inputs and can run independently. Optional stretch tasks extend the week. [The teaching guide](instructor/TEACHING_GUIDE.md) includes a 3-hour selection and a week-long plan.

## The case

A fictional portfolio of 12 property and infrastructure assets sits at geographic coordinates near Houston. Students connect it to a fictional transport corridor, service areas and a generated temperature record. They decide which operational questions to ask next.

**All portfolio and climate case data are synthetic.** The coordinates are real-world coordinates, but these records describe no actual properties or local climate. A separate real satellite image is included to inspect raster structure, with its local source and limits documented. No lesson needs a paid service, API key, tile server or live data download after setup.

## Run locally

This project already has a local `.venv` used for validation on this computer. From PowerShell in this folder:

```powershell
.\.venv\Scripts\python.exe -m jupyterlab
```

Open `notebooks/00_Start_Here_Alternative_Data.ipynb`. Select the Python kernel from this environment. Use **Shift+Enter** to run cells and **Restart Kernel and Run All** to reproduce the notebook from a clean state.

### On another computer

Use Python 3.12 for the closest match to the tested environment. Install once while online:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m jupyterlab
```

On macOS/Linux, use `python3` to create the environment and `.venv/bin/python` for the next commands. Keep `data/` and `notebooks/` together. `requirements-tested.txt` records the exact validation environment; `requirements.txt` lists the direct requirements with broader compatible ranges.

If a classroom computer cannot install packages, use the saved notebook outputs or HTML copies, pair with someone running Jupyter, and complete the interpretation exercises. No web map background is required.

## Folder guide

- `notebooks/`: six student notebooks with executed outputs.
- `html/`: reading copies of those notebooks.
- `data/`: small case datasets, a real raster sample, data dictionary, sources and checksums.
- `instructor/`: teaching plan, discussion prompts, answer guidance and example results.
- `outputs/`: the worked portfolio screen produced by Notebook 05.
- `scripts/`: reproducible data/notebook builders and execution checks.
- `VALIDATION.md`: run status and verification details.

The shareable `student-pack.zip` excludes the local Python environment, build tools and instructor answers. It includes notebooks, HTML, data, setup instructions and dependencies.

## Scope

The class builds on basic Python and pandas, with guided introductions to GeoPandas, Rasterio and xarray. Students extend familiar table operations to geometry and multidimensional arrays, then interpret the results. It does not teach production climate modelling, remote-sensing calibration, asset valuation or financial loss estimation. No conclusion about an actual asset follows from the fictional data.

The existing Week 8–9 and Planet collections remain separate. These are newly authored lessons designed for this audience, with shorter cells and a consistent case.
