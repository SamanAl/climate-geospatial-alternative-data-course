# File-by-file guide

[Back to the course overview](README.md)

The following inventory describes every included course file, including data companions, outputs and administrative files. Notebook checkpoint backups and runtime installations are not teaching deliverables. `publication-manifest.json` records hashes of the copied course files; `README.md` introduces the course; `FILE_GUIDE.md` is this inventory; the root `.gitignore` excludes runtime and credential files.


### Alternative Data - Climate and Geospatial

| File | Purpose |
|---|---|
| [.gitignore](Alternative%20Data%20-%20Climate%20and%20Geospatial/.gitignore) | Git ignore rules for local runtime files or tutorial-generated data. |
| [README.md](Alternative%20Data%20-%20Climate%20and%20Geospatial/README.md) | Entry point for the new module: audience, sequence, setup, folder guide and scope. |
| [VALIDATION.md](Alternative%20Data%20-%20Climate%20and%20Geospatial/VALIDATION.md) | Recorded execution and semantic validation of the six new notebooks; not a validation of the older collection. |
| [requirements-tested.txt](Alternative%20Data%20-%20Climate%20and%20Geospatial/requirements-tested.txt) | Exact package versions from the Windows Python environment used for the recorded validation. |
| [requirements.txt](Alternative%20Data%20-%20Climate%20and%20Geospatial/requirements.txt) | Direct Python package requirements for running the new teaching module. |
| [student-pack.zip](Alternative%20Data%20-%20Climate%20and%20Geospatial/student-pack.zip) | Ready-to-share student archive of the new notebooks, reading copies, data and setup instructions; excludes instructor answers. |

### Alternative Data - Climate and Geospatial/data

| File | Purpose |
|---|---|
| [DATA_DICTIONARY.md](Alternative%20Data%20-%20Climate%20and%20Geospatial/data/DATA_DICTIONARY.md) | Definitions, units, synthetic-data generation recipe, missingness, provenance and reference links for the new case. |
| [PLANET_REPOSITORY_LICENSE](Alternative%20Data%20-%20Climate%20and%20Geospatial/data/PLANET_REPOSITORY_LICENSE) | Original Planet repository license retained with the copied real raster sample. |
| [assets.csv](Alternative%20Data%20-%20Climate%20and%20Geospatial/data/assets.csv) | Fictional 12-asset portfolio with location, sector, equity and backup-verification attributes. |
| [assets.geojson](Alternative%20Data%20-%20Climate%20and%20Geospatial/data/assets.geojson) | The same fictional assets as WGS84 point features with properties. |
| [assets.gpkg](Alternative%20Data%20-%20Climate%20and%20Geospatial/data/assets.gpkg) | The same fictional asset points stored in a GeoPackage layer named assets. |
| [corridor.geojson](Alternative%20Data%20-%20Climate%20and%20Geospatial/data/corridor.geojson) | Fictional line geometry used for distance and buffer exercises. |
| [manifest.json](Alternative%20Data%20-%20Climate%20and%20Geospatial/data/manifest.json) | SHA-256 checksums and byte sizes for the teaching data at build time. |
| [real_satellite_example.tif](Alternative%20Data%20-%20Climate%20and%20Geospatial/data/real_satellite_example.tif) | Real satellite raster copied from the local Planet example for structural inspection; not used to infer climate values. |
| [service_areas.geojson](Alternative%20Data%20-%20Climate%20and%20Geospatial/data/service_areas.geojson) | Two adjacent fictional service-area polygons for spatial-join exercises. |
| [synthetic_daily_temperature.nc](Alternative%20Data%20-%20Climate%20and%20Geospatial/data/synthetic_daily_temperature.nc) | Generated 1991–2024 daily maximum temperatures on a 6×6 grid, in kelvin; includes deliberate missingness. |
| [synthetic_hot_days_2024.tif](Alternative%20Data%20-%20Climate%20and%20Geospatial/data/synthetic_hot_days_2024.tif) | Derived 2024 count of daily maximum temperatures ≥35°C on the same synthetic grid; nodata is −9999. |

### Alternative Data - Climate and Geospatial/data/shapefile_example

| File | Purpose |
|---|---|
| [assets.cpg](Alternative%20Data%20-%20Climate%20and%20Geospatial/data/shapefile_example/assets.cpg) | Shapefile companion for fictional asset points: text encoding declaration. Keep all companions together. |
| [assets.dbf](Alternative%20Data%20-%20Climate%20and%20Geospatial/data/shapefile_example/assets.dbf) | Shapefile companion for fictional asset points: attribute table. Keep all companions together. |
| [assets.prj](Alternative%20Data%20-%20Climate%20and%20Geospatial/data/shapefile_example/assets.prj) | Shapefile companion for fictional asset points: coordinate reference system definition. Keep all companions together. |
| [assets.shp](Alternative%20Data%20-%20Climate%20and%20Geospatial/data/shapefile_example/assets.shp) | Shapefile companion for fictional asset points: geometry records. Keep all companions together. |
| [assets.shx](Alternative%20Data%20-%20Climate%20and%20Geospatial/data/shapefile_example/assets.shx) | Shapefile companion for fictional asset points: geometry index. Keep all companions together. |

### Alternative Data - Climate and Geospatial/html

| File | Purpose |
|---|---|
| [00_Start_Here_Alternative_Data.html](Alternative%20Data%20-%20Climate%20and%20Geospatial/html/00_Start_Here_Alternative_Data.html) | Executed HTML reading copy of 00_Start_Here_Alternative_Data.ipynb; use the notebook to change code. |
| [01_Data_Formats_and_First_Map.html](Alternative%20Data%20-%20Climate%20and%20Geospatial/html/01_Data_Formats_and_First_Map.html) | Executed HTML reading copy of 01_Data_Formats_and_First_Map.ipynb; use the notebook to change code. |
| [02_Location_Joins_and_Distance.html](Alternative%20Data%20-%20Climate%20and%20Geospatial/html/02_Location_Joins_and_Distance.html) | Executed HTML reading copy of 02_Location_Joins_and_Distance.ipynb; use the notebook to change code. |
| [03_Rasters_Images_and_Exposure.html](Alternative%20Data%20-%20Climate%20and%20Geospatial/html/03_Rasters_Images_and_Exposure.html) | Executed HTML reading copy of 03_Rasters_Images_and_Exposure.ipynb; use the notebook to change code. |
| [04_Climate_Time_and_Uncertainty.html](Alternative%20Data%20-%20Climate%20and%20Geospatial/html/04_Climate_Time_and_Uncertainty.html) | Executed HTML reading copy of 04_Climate_Time_and_Uncertainty.ipynb; use the notebook to change code. |
| [05_Private_Markets_Due_Diligence_Lab.html](Alternative%20Data%20-%20Climate%20and%20Geospatial/html/05_Private_Markets_Due_Diligence_Lab.html) | Executed HTML reading copy of 05_Private_Markets_Due_Diligence_Lab.ipynb; use the notebook to change code. |
| [index.html](Alternative%20Data%20-%20Climate%20and%20Geospatial/html/index.html) | No-install HTML lesson index. |

### Alternative Data - Climate and Geospatial/instructor

| File | Purpose |
|---|---|
| [ANSWER_GUIDE.md](Alternative%20Data%20-%20Climate%20and%20Geospatial/instructor/ANSWER_GUIDE.md) | Instructor explanations, exercise guidance and memo scaffold; includes coding-extension expectations. |
| [TEACHING_GUIDE.md](Alternative%20Data%20-%20Climate%20and%20Geospatial/instructor/TEACHING_GUIDE.md) | Audience assumptions, learning objectives, workshop/week schedules, facilitation prompts, glossary and grading rubric. |
| [WORKED_RESULTS.md](Alternative%20Data%20-%20Climate%20and%20Geospatial/instructor/WORKED_RESULTS.md) | Default synthetic portfolio results, coverage, review categories and interview shortlist. |

### Alternative Data - Climate and Geospatial/notebooks

| File | Purpose |
|---|---|
| [00_Start_Here_Alternative_Data.ipynb](Alternative%20Data%20-%20Climate%20and%20Geospatial/notebooks/00_Start_Here_Alternative_Data.ipynb) | Introduces alternative data and proxies; examines a fictional portfolio and frames an operational question. |
| [01_Data_Formats_and_First_Map.ipynb](Alternative%20Data%20-%20Climate%20and%20Geospatial/notebooks/01_Data_Formats_and_First_Map.ipynb) | Builds a map from coordinates and compares CSV, GeoJSON, Shapefile and GeoPackage representations. |
| [02_Location_Joins_and_Distance.ipynb](Alternative%20Data%20-%20Climate%20and%20Geospatial/notebooks/02_Location_Joins_and_Distance.ipynb) | Assigns sites to areas with spatial joins; examines boundary cases and measures corridor proximity in a projected CRS. |
| [03_Rasters_Images_and_Exposure.ipynb](Alternative%20Data%20-%20Climate%20and%20Geospatial/notebooks/03_Rasters_Images_and_Exposure.ipynb) | Reads GeoTIFF metadata, maps a synthetic heat grid, samples assets and preserves unknown values; inspects a separate real image. |
| [04_Climate_Time_and_Uncertainty.ipynb](Alternative%20Data%20-%20Climate%20and%20Geospatial/notebooks/04_Climate_Time_and_Uncertainty.ipynb) | Opens a NetCDF climate cube, converts units, compares time periods and counts hot days with coverage checks. |
| [05_Private_Markets_Due_Diligence_Lab.ipynb](Alternative%20Data%20-%20Climate%20and%20Geospatial/notebooks/05_Private_Markets_Due_Diligence_Lab.ipynb) | Combines exposure data and asset attributes into a transparent operational review rule; tests thresholds and asks for a short memo. |

### Alternative Data - Climate and Geospatial/outputs

| File | Purpose |
|---|---|
| [synthetic_portfolio_screen.csv](Alternative%20Data%20-%20Climate%20and%20Geospatial/outputs/synthetic_portfolio_screen.csv) | Worked output of Notebook 05: asset attributes, sampled heat days, coverage flags and follow-up categories. |

### Alternative Data - Climate and Geospatial/scripts

| File | Purpose |
|---|---|
| [build_data.py](Alternative%20Data%20-%20Climate%20and%20Geospatial/scripts/build_data.py) | Deterministically creates the synthetic assets, vector formats, climate NetCDF and derived heat GeoTIFF; copies the real local raster when available. |
| [build_notebooks.py](Alternative%20Data%20-%20Climate%20and%20Geospatial/scripts/build_notebooks.py) | Authors the six teaching notebooks, preserving executed outputs only when all code cells are unchanged. |
| [validate_and_export.py](Alternative%20Data%20-%20Climate%20and%20Geospatial/scripts/validate_and_export.py) | Executes notebooks, checks dataset semantics, exports HTML, records dependencies and assembles the student archive. |

### Geospatial Learning

| File | Purpose |
|---|---|
| [CATALOG.md](Geospatial%20Learning/CATALOG.md) | Links the 38 supporting geospatial notebooks; excludes checkpoint backups. |
| [README.md](Geospatial%20Learning/README.md) | Study sequence, provenance and dependency notes for the supporting geospatial collection. |
| [file-manifest.csv](Geospatial%20Learning/file-manifest.csv) | Historical move/copy inventory with original local paths, destination paths and checksums; some checkpoint entries describe local-only backups. |

### Geospatial Learning/00-Source-Reference

| File | Purpose |
|---|---|
| [LICENSE](Geospatial%20Learning/00-Source-Reference/LICENSE) | Original license retained from the Planet notebook repository. |
| [README.md](Geospatial%20Learning/00-Source-Reference/README.md) | Original setup and context instructions for 00-Source-Reference. |
| [environment.yml](Geospatial%20Learning/00-Source-Reference/environment.yml) | Original Planet environment specification; historical reference rather than the new module environment. |

### Geospatial Learning/01-Course/01-Geospatial-Foundations-and-Spatial-Analysis

| File | Purpose |
|---|---|
| [Lecture Eight -  GeoPandas & MapClassify.ipynb](Geospatial%20Learning/01-Course/01-Geospatial-Foundations-and-Spatial-Analysis/Lecture%20Eight%20-%20%20GeoPandas%20%26%20MapClassify.ipynb) | Original lecture on Shapely geometry, GeoPandas plotting and thematic map classification. |
| [Lecture Eight - GeoPlot.ipynb](Geospatial%20Learning/01-Course/01-Geospatial-Foundations-and-Spatial-Analysis/Lecture%20Eight%20-%20GeoPlot.ipynb) | Original GeoPlot lecture covering geographic plotting and projection examples. |
| [Lecture Eight - Geospatial Data.ipynb](Geospatial%20Learning/01-Course/01-Geospatial-Foundations-and-Spatial-Analysis/Lecture%20Eight%20-%20Geospatial%20Data.ipynb) | Original introduction to geometries, GeoDataFrames, geospatial file operations and plotting. |
| [Lecture Eight - Spatial Joins.ipynb](Geospatial%20Learning/01-Course/01-Geospatial-Foundations-and-Spatial-Analysis/Lecture%20Eight%20-%20Spatial%20Joins.ipynb) | Original spatial-join tutorial explaining geometry relationships and combining point/polygon attributes. |

### Geospatial Learning/01-Course/02-Geocoding-and-Interactive-Maps

| File | Purpose |
|---|---|
| [Folium-mpld3.ipynb](Geospatial%20Learning/01-Course/02-Geocoding-and-Interactive-Maps/Folium-mpld3.ipynb) | Combines interactive plotting and Folium choropleth/time-slider examples; includes a machine-specific election CSV dependency. |
| [Folium_and_mplleaflet.ipynb](Geospatial%20Learning/01-Course/02-Geocoding-and-Interactive-Maps/Folium_and_mplleaflet.ipynb) | Maps a GPX track and explores Matplotlib-to-Leaflet mapping. |
| [Lecture Eight - APIs & JSON and GeoPy.ipynb](Geospatial%20Learning/01-Course/02-Geocoding-and-Interactive-Maps/Lecture%20Eight%20-%20APIs%20%26%20JSON%20and%20GeoPy.ipynb) | Original API/JSON and geocoding lecture; includes historical Twitter API examples requiring separate credentials. |
| [Lecture Eight - Folium.ipynb](Geospatial%20Learning/01-Course/02-Geocoding-and-Interactive-Maps/Lecture%20Eight%20-%20Folium.ipynb) | Original interactive-mapping lecture with geocoding, markers, clusters and choropleths. |
| [MarkerCluster.ipynb](Geospatial%20Learning/01-Course/02-Geocoding-and-Interactive-Maps/MarkerCluster.ipynb) | Examples of grouping interactive-map markers into clusters. |
| [Polygons_from_list_of_points.ipynb](Geospatial%20Learning/01-Course/02-Geocoding-and-Interactive-Maps/Polygons_from_list_of_points.ipynb) | Constructs a bounding polygon from points using a convex hull and displays it on a map. |
| [Strip.ipynb](Geospatial%20Learning/01-Course/02-Geocoding-and-Interactive-Maps/Strip.ipynb) | Additional Folium examples, including map controls and styled state geometries. |
| [addresses.csv](Geospatial%20Learning/01-Course/02-Geocoding-and-Interactive-Maps/addresses.csv) | Original lecture address table used for geocoding demonstrations. |
| [df_addresses.csv](Geospatial%20Learning/01-Course/02-Geocoding-and-Interactive-Maps/df_addresses.csv) | Original lecture geocoded-coordinate table used for mapping demonstrations. |

### Geospatial Learning/01-Course/02-Geocoding-and-Interactive-Maps/data

| File | Purpose |
|---|---|
| [2014_08_05_farol.gpx](Geospatial%20Learning/01-Course/02-Geocoding-and-Interactive-Maps/data/2014_08_05_farol.gpx) | GPS track used in the GPX/Leaflet mapping example. |
| [Mercator_projection_SW.jpg](Geospatial%20Learning/01-Course/02-Geocoding-and-Interactive-Maps/data/Mercator_projection_SW.jpg) | Mercator projection illustration supplied with the original lecture. |
| [Mercator_projection_SW.png](Geospatial%20Learning/01-Course/02-Geocoding-and-Interactive-Maps/data/Mercator_projection_SW.png) | PNG version of the supplied Mercator projection illustration. |
| [NOAA_46041.csv](Geospatial%20Learning/01-Course/02-Geocoding-and-Interactive-Maps/data/NOAA_46041.csv) | Bundled NOAA station 46041 example time-series table. |
| [NOAA_46050_WS.csv](Geospatial%20Learning/01-Course/02-Geocoding-and-Interactive-Maps/data/NOAA_46050_WS.csv) | Bundled NOAA station 46050 example time-series table. |
| [NOAA_46243.csv](Geospatial%20Learning/01-Course/02-Geocoding-and-Interactive-Maps/data/NOAA_46243.csv) | Bundled NOAA station 46243 example time-series table. |
| [US_Unemployment_Oct2012.csv](Geospatial%20Learning/01-Course/02-Geocoding-and-Interactive-Maps/data/US_Unemployment_Oct2012.csv) | October 2012 state unemployment sample used in Folium choropleths. |
| [antarctic_ice_edge.json](Geospatial%20Learning/01-Course/02-Geocoding-and-Interactive-Maps/data/antarctic_ice_edge.json) | Bundled Antarctic ice-edge geometry for map examples. |
| [antarctic_ice_shelf_topo.json](Geospatial%20Learning/01-Course/02-Geocoding-and-Interactive-Maps/data/antarctic_ice_shelf_topo.json) | Bundled Antarctic ice-shelf TopoJSON geometry. |
| [consonants_vowels.csv](Geospatial%20Learning/01-Course/02-Geocoding-and-Interactive-Maps/data/consonants_vowels.csv) | Bundled categorical sample table retained with the original Folium example data. |
| [data.json](Geospatial%20Learning/01-Course/02-Geocoding-and-Interactive-Maps/data/data.json) | Original bundled JSON example payload retained with the mapping lecture. |
| [data2.json](Geospatial%20Learning/01-Course/02-Geocoding-and-Interactive-Maps/data/data2.json) | Second original bundled JSON example payload retained with the mapping lecture. |
| [data3.json](Geospatial%20Learning/01-Course/02-Geocoding-and-Interactive-Maps/data/data3.json) | Third original bundled JSON example payload retained with the mapping lecture. |
| [highlight_flight_trajectories.csv](Geospatial%20Learning/01-Course/02-Geocoding-and-Interactive-Maps/data/highlight_flight_trajectories.csv) | Sample flight trajectories for geographic line-display examples. |
| [mercator_temperature.mat](Geospatial%20Learning/01-Course/02-Geocoding-and-Interactive-Maps/data/mercator_temperature.mat) | MATLAB-format temperature sample retained with the original map examples. |
| [nybb.zip](Geospatial%20Learning/01-Course/02-Geocoding-and-Interactive-Maps/data/nybb.zip) | Bundled New York borough boundary archive for vector/spatial-join examples. |
| [or_counties_topo.json](Geospatial%20Learning/01-Course/02-Geocoding-and-Interactive-Maps/data/or_counties_topo.json) | Oregon county boundaries in TopoJSON for map examples. |
| [search_bars_rome.json](Geospatial%20Learning/01-Course/02-Geocoding-and-Interactive-Maps/data/search_bars_rome.json) | Bundled Rome search-result geometry sample for map/search examples. |
| [search_states.json](Geospatial%20Learning/01-Course/02-Geocoding-and-Interactive-Maps/data/search_states.json) | Bundled state geometry sample for map/search examples. |
| [subwaystations.geojson](Geospatial%20Learning/01-Course/02-Geocoding-and-Interactive-Maps/data/subwaystations.geojson) | Subway station point features for map examples. |
| [us-states.json](Geospatial%20Learning/01-Course/02-Geocoding-and-Interactive-Maps/data/us-states.json) | US state GeoJSON boundaries used for choropleth layers. |
| [us_counties_20m_topo.json](Geospatial%20Learning/01-Course/02-Geocoding-and-Interactive-Maps/data/us_counties_20m_topo.json) | US county TopoJSON geometry for choropleth examples. |
| [us_county_data.csv](Geospatial%20Learning/01-Course/02-Geocoding-and-Interactive-Maps/data/us_county_data.csv) | County-level attribute table bundled with choropleth examples. |
| [vis1.json](Geospatial%20Learning/01-Course/02-Geocoding-and-Interactive-Maps/data/vis1.json) | First visualization sample JSON payload bundled with the original lecture. |
| [vis2.json](Geospatial%20Learning/01-Course/02-Geocoding-and-Interactive-Maps/data/vis2.json) | Second visualization sample JSON payload bundled with the original lecture. |
| [vis3.json](Geospatial%20Learning/01-Course/02-Geocoding-and-Interactive-Maps/data/vis3.json) | Third visualization sample JSON payload bundled with the original lecture. |
| [world-countries.json](Geospatial%20Learning/01-Course/02-Geocoding-and-Interactive-Maps/data/world-countries.json) | World country boundaries bundled for geographic map examples. |

### Geospatial Learning/02-Vector-and-Web-Maps/coverage

| File | Purpose |
|---|---|
| [calculate_coverage.ipynb](Geospatial%20Learning/02-Vector-and-Web-Maps/coverage/calculate_coverage.ipynb) | Computes imagery coverage of an area of interest using a projected coordinate system. |
| [calculate_coverage_wgs84.ipynb](Geospatial%20Learning/02-Vector-and-Web-Maps/coverage/calculate_coverage_wgs84.ipynb) | Explores imagery coverage over an Iowa area of interest in a geographic-coordinate workflow. |
| [iowa.geojson](Geospatial%20Learning/02-Vector-and-Web-Maps/coverage/iowa.geojson) | Iowa area-of-interest geometry for the coverage examples. |
| [iowa_state.png](Geospatial%20Learning/02-Vector-and-Web-Maps/coverage/iowa_state.png) | Iowa reference image supporting the coverage examples. |

### Geospatial Learning/02-Vector-and-Web-Maps/vector

| File | Purpose |
|---|---|
| [shapefile.ipynb](Geospatial%20Learning/02-Vector-and-Web-Maps/vector/shapefile.ipynb) | Reads and draws a bundled Natural Earth shapefile using Python and Matplotlib. |

### Geospatial Learning/02-Vector-and-Web-Maps/vector/ne_110m_admin_0_countries

| File | Purpose |
|---|---|
| [ne_110m_admin_0_countries.README.html](Geospatial%20Learning/02-Vector-and-Web-Maps/vector/ne_110m_admin_0_countries/ne_110m_admin_0_countries.README.html) | Original Natural Earth dataset documentation supplied with the country shapefile. |
| [ne_110m_admin_0_countries.VERSION.txt](Geospatial%20Learning/02-Vector-and-Web-Maps/vector/ne_110m_admin_0_countries/ne_110m_admin_0_countries.VERSION.txt) | Original Natural Earth country dataset version marker. |
| [ne_110m_admin_0_countries.cpg](Geospatial%20Learning/02-Vector-and-Web-Maps/vector/ne_110m_admin_0_countries/ne_110m_admin_0_countries.cpg) | Shapefile companion for Natural Earth 1:110m country boundaries: text encoding declaration. Keep all companions together. |
| [ne_110m_admin_0_countries.dbf](Geospatial%20Learning/02-Vector-and-Web-Maps/vector/ne_110m_admin_0_countries/ne_110m_admin_0_countries.dbf) | Shapefile companion for Natural Earth 1:110m country boundaries: attribute table. Keep all companions together. |
| [ne_110m_admin_0_countries.prj](Geospatial%20Learning/02-Vector-and-Web-Maps/vector/ne_110m_admin_0_countries/ne_110m_admin_0_countries.prj) | Shapefile companion for Natural Earth 1:110m country boundaries: coordinate reference system definition. Keep all companions together. |
| [ne_110m_admin_0_countries.shp](Geospatial%20Learning/02-Vector-and-Web-Maps/vector/ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp) | Shapefile companion for Natural Earth 1:110m country boundaries: geometry records. Keep all companions together. |
| [ne_110m_admin_0_countries.shx](Geospatial%20Learning/02-Vector-and-Web-Maps/vector/ne_110m_admin_0_countries/ne_110m_admin_0_countries.shx) | Shapefile companion for Natural Earth 1:110m country boundaries: geometry index. Keep all companions together. |

### Geospatial Learning/02-Vector-and-Web-Maps/webtiles

| File | Purpose |
|---|---|
| [osm_basemap.ipynb](Geospatial%20Learning/02-Vector-and-Web-Maps/webtiles/osm_basemap.ipynb) | Introduces web map tiles and displaying an OpenStreetMap basemap. |
| [visualize_imagery_over_time.ipynb](Geospatial%20Learning/02-Vector-and-Web-Maps/webtiles/visualize_imagery_over_time.ipynb) | Uses Planet data and tile APIs for a time-based imagery visualization; requires an API key. |

### Geospatial Learning/03-Raster-Fundamentals/getting-to-know-sat-imagery

| File | Purpose |
|---|---|
| [Inspecting_Satellite_Imagery.ipynb](Geospatial%20Learning/03-Raster-Fundamentals/getting-to-know-sat-imagery/Inspecting_Satellite_Imagery.ipynb) | Inspects the bundled satellite raster with Rasterio: metadata, bands and array values. |
| [Visualizing_Satellite_Imagery.ipynb](Geospatial%20Learning/03-Raster-Fundamentals/getting-to-know-sat-imagery/Visualizing_Satellite_Imagery.ipynb) | Visualizes satellite bands and imagery using Matplotlib. |
| [example.tif](Geospatial%20Learning/03-Raster-Fundamentals/getting-to-know-sat-imagery/example.tif) | Bundled real satellite image used by the Planet inspection and visualization tutorials. |
| [pixels2.png](Geospatial%20Learning/03-Raster-Fundamentals/getting-to-know-sat-imagery/pixels2.png) | Illustration accompanying the satellite imagery tutorials. |

### Geospatial Learning/03-Raster-Fundamentals/scipy-2022-workshop

| File | Purpose |
|---|---|
| [0_download_data.ipynb](Geospatial%20Learning/03-Raster-Fundamentals/scipy-2022-workshop/0_download_data.ipynb) | Provides the SciPy workshop data download/preparation instructions. |
| [1_rasterio_firstlook.ipynb](Geospatial%20Learning/03-Raster-Fundamentals/scipy-2022-workshop/1_rasterio_firstlook.ipynb) | Introduces opening satellite raster data with Rasterio. |
| [2_rasterbands.ipynb](Geospatial%20Learning/03-Raster-Fundamentals/scipy-2022-workshop/2_rasterbands.ipynb) | Explores and displays individual raster bands. |
| [3_Compute_NDWI.ipynb](Geospatial%20Learning/03-Raster-Fundamentals/scipy-2022-workshop/3_Compute_NDWI.ipynb) | Computes a water index and introduces pixel classification. |
| [4_masks_and_filters.ipynb](Geospatial%20Learning/03-Raster-Fundamentals/scipy-2022-workshop/4_masks_and_filters.ipynb) | Introduces raster masking and filtering. |
| [5_plotting_a_histogram.ipynb](Geospatial%20Learning/03-Raster-Fundamentals/scipy-2022-workshop/5_plotting_a_histogram.ipynb) | Examines raster-value distributions with histograms. |
| [README.md](Geospatial%20Learning/03-Raster-Fundamentals/scipy-2022-workshop/README.md) | Original setup and context instructions for scipy-2022-workshop. |
| [coastline_analysis.ipynb](Geospatial%20Learning/03-Raster-Fundamentals/scipy-2022-workshop/coastline_analysis.ipynb) | Applies raster/time-series analysis to a coastal-recession case study in Bangladesh. |

### Geospatial Learning/03-Raster-Fundamentals/scipy-2022-workshop/assets

| File | Purpose |
|---|---|
| [coastal_erosion_Bangladesh.geojson](Geospatial%20Learning/03-Raster-Fundamentals/scipy-2022-workshop/assets/coastal_erosion_Bangladesh.geojson) | Bangladesh study-area geometry for the coastline analysis workshop. |
| [region.png](Geospatial%20Learning/03-Raster-Fundamentals/scipy-2022-workshop/assets/region.png) | Study-region illustration for the coastline workshop. |

### Geospatial Learning/04-Remote-Sensing-Practice/in-class-exercises/band-math-generate-ndvi

| File | Purpose |
|---|---|
| [generate-ndvi-exercise-key.ipynb](Geospatial%20Learning/04-Remote-Sensing-Practice/in-class-exercises/band-math-generate-ndvi/generate-ndvi-exercise-key.ipynb) | Worked answer notebook: Student exercise deriving a vegetation index from satellite bands. |
| [generate-ndvi-exercise.ipynb](Geospatial%20Learning/04-Remote-Sensing-Practice/in-class-exercises/band-math-generate-ndvi/generate-ndvi-exercise.ipynb) | Student exercise deriving a vegetation index from satellite bands. |

### Geospatial Learning/04-Remote-Sensing-Practice/in-class-exercises/band-math-generate-ndvi/data

| File | Purpose |
|---|---|
| [ndvi-equation.png](Geospatial%20Learning/04-Remote-Sensing-Practice/in-class-exercises/band-math-generate-ndvi/data/ndvi-equation.png) | Illustration of the NDVI formula used by vegetation-index tutorials/exercises. |

### Geospatial Learning/04-Remote-Sensing-Practice/in-class-exercises/convert-radiance-to-reflectance

| File | Purpose |
|---|---|
| [convert-radiance-to-reflectance-key.ipynb](Geospatial%20Learning/04-Remote-Sensing-Practice/in-class-exercises/convert-radiance-to-reflectance/convert-radiance-to-reflectance-key.ipynb) | Worked answer notebook: Student exercise converting radiance to reflectance. |
| [convert-radiance-to-reflectance.ipynb](Geospatial%20Learning/04-Remote-Sensing-Practice/in-class-exercises/convert-radiance-to-reflectance/convert-radiance-to-reflectance.ipynb) | Student exercise converting radiance to reflectance. |

### Geospatial Learning/04-Remote-Sensing-Practice/in-class-exercises/mosaicing-and-masking

| File | Purpose |
|---|---|
| [mosaicing-and-masking-key.ipynb](Geospatial%20Learning/04-Remote-Sensing-Practice/in-class-exercises/mosaicing-and-masking/mosaicing-and-masking-key.ipynb) | Worked answer notebook: Student exercise combining scenes and masking imagery to an area of interest. |
| [mosaicing-and-masking.ipynb](Geospatial%20Learning/04-Remote-Sensing-Practice/in-class-exercises/mosaicing-and-masking/mosaicing-and-masking.ipynb) | Student exercise combining scenes and masking imagery to an area of interest. |

### Geospatial Learning/04-Remote-Sensing-Practice/in-class-exercises/mosaicing-and-masking/data

| File | Purpose |
|---|---|
| [mt-dana-small.geojson](Geospatial%20Learning/04-Remote-Sensing-Practice/in-class-exercises/mosaicing-and-masking/data/mt-dana-small.geojson) | Mount Dana area-of-interest geometry for the mosaicing/masking exercise. |

### Geospatial Learning/04-Remote-Sensing-Practice/in-class-exercises/mosaicing-and-masking/images

| File | Purpose |
|---|---|
| [explorer-data-order.png](Geospatial%20Learning/04-Remote-Sensing-Practice/in-class-exercises/mosaicing-and-masking/images/explorer-data-order.png) | Reference screenshot illustrating an imagery data-order step. |
| [explorer-mt-dana.gif](Geospatial%20Learning/04-Remote-Sensing-Practice/in-class-exercises/mosaicing-and-masking/images/explorer-mt-dana.gif) | Animated reference illustration for the Mount Dana imagery workflow. |
| [final_in_qgis.png](Geospatial%20Learning/04-Remote-Sensing-Practice/in-class-exercises/mosaicing-and-masking/images/final_in_qgis.png) | Reference image of the mosaicing exercise result displayed in QGIS. |
| [pe-mtdana.gif](Geospatial%20Learning/04-Remote-Sensing-Practice/in-class-exercises/mosaicing-and-masking/images/pe-mtdana.gif) | Reference animation illustrating the Mount Dana imagery example. |

### Geospatial Learning/04-Remote-Sensing-Practice/ndvi

| File | Purpose |
|---|---|
| [.gitignore](Geospatial%20Learning/04-Remote-Sensing-Practice/ndvi/.gitignore) | Git ignore rules for local runtime files or tutorial-generated data. |
| [ndvi_planetscope.ipynb](Geospatial%20Learning/04-Remote-Sensing-Practice/ndvi/ndvi_planetscope.ipynb) | Computes and visualizes NDVI from PlanetScope imagery; source imagery must be supplied. |

### Geospatial Learning/04-Remote-Sensing-Practice/ndvi-from-sr

| File | Purpose |
|---|---|
| [.gitignore](Geospatial%20Learning/04-Remote-Sensing-Practice/ndvi-from-sr/.gitignore) | Git ignore rules for local runtime files or tutorial-generated data. |
| [ndvi_planetscope_sr.ipynb](Geospatial%20Learning/04-Remote-Sensing-Practice/ndvi-from-sr/ndvi_planetscope_sr.ipynb) | Computes NDVI from surface-reflectance imagery; source imagery must be supplied. |

### Geospatial Learning/04-Remote-Sensing-Practice/ndvi-from-sr/data

| File | Purpose |
|---|---|
| [.gitkeep](Geospatial%20Learning/04-Remote-Sensing-Practice/ndvi-from-sr/data/.gitkeep) | Empty marker preserving a required data or output directory; does not contain imagery. |

### Geospatial Learning/04-Remote-Sensing-Practice/ndvi-from-sr/images

| File | Purpose |
|---|---|
| [ndvi-equation.png](Geospatial%20Learning/04-Remote-Sensing-Practice/ndvi-from-sr/images/ndvi-equation.png) | Illustration of the NDVI formula used by vegetation-index tutorials/exercises. |

### Geospatial Learning/04-Remote-Sensing-Practice/ndvi-from-sr/output

| File | Purpose |
|---|---|
| [.gitkeep](Geospatial%20Learning/04-Remote-Sensing-Practice/ndvi-from-sr/output/.gitkeep) | Empty marker preserving a required data or output directory; does not contain imagery. |
| [ndvi-fig.png](Geospatial%20Learning/04-Remote-Sensing-Practice/ndvi-from-sr/output/ndvi-fig.png) | Previously generated NDVI result image retained with the surface-reflectance tutorial. |
| [ndvi-histogram.png](Geospatial%20Learning/04-Remote-Sensing-Practice/ndvi-from-sr/output/ndvi-histogram.png) | Previously generated NDVI histogram retained with the surface-reflectance tutorial. |

### Geospatial Learning/04-Remote-Sensing-Practice/ndvi/data

| File | Purpose |
|---|---|
| [.gitkeep](Geospatial%20Learning/04-Remote-Sensing-Practice/ndvi/data/.gitkeep) | Empty marker preserving a required data or output directory; does not contain imagery. |

### Geospatial Learning/04-Remote-Sensing-Practice/ndvi/images

| File | Purpose |
|---|---|
| [ndvi-equation.png](Geospatial%20Learning/04-Remote-Sensing-Practice/ndvi/images/ndvi-equation.png) | Illustration of the NDVI formula used by vegetation-index tutorials/exercises. |

### Geospatial Learning/04-Remote-Sensing-Practice/ndvi/output

| File | Purpose |
|---|---|
| [.gitkeep](Geospatial%20Learning/04-Remote-Sensing-Practice/ndvi/output/.gitkeep) | Empty marker preserving a required data or output directory; does not contain imagery. |
| [ndvi_cmap.png](Geospatial%20Learning/04-Remote-Sensing-Practice/ndvi/output/ndvi_cmap.png) | Previously generated NDVI color-map image retained with the original tutorial. |

### Geospatial Learning/05-Cloud-Geospatial/cloud-native-geospatial

| File | Purpose |
|---|---|
| [README.md](Geospatial%20Learning/05-Cloud-Geospatial/cloud-native-geospatial/README.md) | Original setup and context instructions for cloud-native-geospatial. |

### Geospatial Learning/05-Cloud-Geospatial/cloud-native-geospatial/intro-to-cogs

| File | Purpose |
|---|---|
| [introduction-to-cogs-part2.ipynb](Geospatial%20Learning/05-Cloud-Geospatial/cloud-native-geospatial/intro-to-cogs/introduction-to-cogs-part2.ipynb) | Historical service workflow to obtain imagery and create COGs; uses Planet APIs. |
| [introduction-to-cogs-part3.ipynb](Geospatial%20Learning/05-Cloud-Geospatial/cloud-native-geospatial/intro-to-cogs/introduction-to-cogs-part3.ipynb) | Optional advanced example uploading COGs to Google Cloud and exposing them for remote access. |
| [introduction-to-cogs.ipynb](Geospatial%20Learning/05-Cloud-Geospatial/cloud-native-geospatial/intro-to-cogs/introduction-to-cogs.ipynb) | Introduces TIFFs, georeferencing and Cloud Optimized GeoTIFF concepts. |

### Geospatial Learning/05-Cloud-Geospatial/cloud-native-geospatial/intro-to-stac

| File | Purpose |
|---|---|
| [introduction-to-stac-part1.ipynb](Geospatial%20Learning/05-Cloud-Geospatial/cloud-native-geospatial/intro-to-stac/introduction-to-stac-part1.ipynb) | Introduces STAC catalog components and metadata for satellite imagery. |
| [introduction-to-stac-part2.ipynb](Geospatial%20Learning/05-Cloud-Geospatial/cloud-native-geospatial/intro-to-stac/introduction-to-stac-part2.ipynb) | Historical STAC workflow; the source notebook itself includes a notice recommending a newer workflow. |
