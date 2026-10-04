# Validation

Completed 2026-09-16 01:08 UTC.

Python 3.12.14; Windows local project environment.

| Notebook | Executed code cells | Rendered figures |
| --- | --- | --- |
| 00_Start_Here_Alternative_Data.ipynb | 4 | 1 |
| 01_Data_Formats_and_First_Map.ipynb | 5 | 1 |
| 02_Location_Joins_and_Distance.ipynb | 6 | 1 |
| 03_Rasters_Images_and_Exposure.ipynb | 5 | 2 |
| 04_Climate_Time_and_Uncertainty.ipynb | 5 | 3 |
| 05_Private_Markets_Due_Diligence_Lab.ipynb | 5 | 1 |

All notebooks ran independently in fresh kernels with zero error outputs. HTML reading copies were exported from those executed versions.

Semantic checks passed: unique asset IDs; matching vector formats and CRS; 2024 leap-year length; deliberate missing climate year; GeoTIFF counts agree with NetCDF; 35 valid raster cells; A11/A12 preserved as unknown; full $341m portfolio retained; threshold counts monotone; all data checksums intact.

This verifies the bundled synthetic workflow, not scientific validity for real assets, live services, or installation on every student device. No live data service is called by the notebooks.

Audience revision: assumes basic Python/pandas and no geospatial or climate background. Only narrative and exercise prompts changed; every executable cell was compared with its previously executed version and was unchanged. Verified outputs were retained, semantic checks passed again, and HTML/student ZIP were refreshed.
