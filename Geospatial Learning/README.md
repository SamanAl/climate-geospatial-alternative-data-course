# Geospatial learning

Start with the course notebooks, then work from vector maps to satellite imagery and raster analysis. All original notebook contents and filenames are preserved.

## Suggested learning order

| Stage | Folder | Study order and learning goal |
|---|---|---|
| 1. Geospatial foundations | [Geospatial foundations and spatial analysis](<01-Course/01-Geospatial-Foundations-and-Spatial-Analysis>) | **Geospatial Data**, then **GeoPandas & MapClassify**, **Spatial Joins**, and **GeoPlot**. Learn geometries, coordinate systems, GeoDataFrames, spatial relationships, and thematic maps. The original filenames say Lecture Eight even though these came from Week 9. |
| 2. Geocoding and interactive maps | [Geocoding and interactive maps](<01-Course/02-Geocoding-and-Interactive-Maps>) | **APIs & JSON and GeoPy**, then **Folium**, **MarkerCluster**, and **Polygons_from_list_of_points**. Finish with **Folium_and_mplleaflet**, **Folium-mpld3**, and **Strip** as extra examples. Focus on the geocoding sections of the API lecture; its Twitter sections are optional background. |
| 3. Vector practice | [Vector and web maps](02-Vector-and-Web-Maps) | Start with `vector/shapefile.ipynb`, then `webtiles/osm_basemap.ipynb`. Use the two `coverage` notebooks to explore area of interest and image coverage; finish with imagery-over-time web tiles as an optional API exercise. |
| 4. Raster fundamentals | [Raster fundamentals](03-Raster-Fundamentals) | In `getting-to-know-sat-imagery`, do **Inspecting** before **Visualizing**. Then follow `scipy-2022-workshop` notebooks **0 through 5**: data preparation, Rasterio, bands, water index (NDWI), masks, and histograms. Finish with `coastline_analysis.ipynb`. |
| 5. Remote sensing exercises | [Remote sensing practice](04-Remote-Sensing-Practice) | Read `ndvi/ndvi_planetscope.ipynb`, then `ndvi-from-sr/ndvi_planetscope_sr.ipynb`. Practice vegetation index (NDVI), radiance-to-reflectance conversion, and mosaicing/masking in `in-class-exercises`. Attempt each exercise before opening its `-key` notebook. |
| 6. Cloud formats | [Cloud geospatial](05-Cloud-Geospatial/cloud-native-geospatial) | Start with `intro-to-cogs/introduction-to-cogs.ipynb` and `intro-to-stac/introduction-to-stac-part1.ipynb`. These introduce Cloud Optimized GeoTIFFs and imagery catalogs. COG parts 2/3 and STAC part 2 are optional historical service-integration examples. |

## Practice milestones

1. Load points and polygons, inspect their coordinate systems, and count points within polygons using a spatial join.
2. Build a Folium map with markers, clusters, and a choropleth; explain what the colors represent.
3. Inspect a raster's bounds, bands, resolution, and missing-data values, then plot a color composite.
4. Calculate a vegetation or water index and explain how masking changes the result.
5. Explain when you would use a shapefile, GeoJSON, a GeoTIFF, a COG, or a STAC catalog.

## Running the notebooks

- Open notebooks in Jupyter with their own containing folder as the working directory so relative data paths resolve.
- The Week 8 CSV files and `data` folder moved with the lectures. Copied Planet tutorial folders include their bundled data, images, and helper files, including the vector shapefile components and satellite `example.tif`.
- These are existing teaching materials, not a newly tested software environment. Notebook execution, package installation, external downloads, and service availability were not tested during organization.
- The course uses GeoPandas, Shapely, GeoPlot, MapClassify, Folium, GeoPy, and several optional plotting packages. Planet notebooks also use Rasterio and other dependencies. The original Planet [environment file](00-Source-Reference/environment.yml) and [setup instructions](00-Source-Reference/README.md) are included as references; their repository/Docker commands refer to the original repository layout.
- Some notebooks require external imagery or API credentials. The SciPy workshop has a data preparation notebook and its own README; the NDVI examples have data directories that do not contain the required source imagery.
- Existing course code includes library-provided sample datasets, online URLs, and a hardcoded `C:\Users\sarma\Downloads\1976-2020-president.csv` path in `Folium-mpld3.ipynb`. These dependencies may need adjustment before execution. The API lecture references a Twitter secrets file that was not present in Week 8.
- STAC part 2 contains its own notice recommending another workflow; treat that notebook as historical reference. COG part 3 demonstrates Google Cloud upload/public access and belongs in the optional advanced stage.

## Organization and provenance

- **Moved:** all Week 8 and Week 9 materials from `E:\DataViz Course`, including supporting data and existing checkpoints, into `01-Course`.
- **Copied:** selected learning folders from `E:\notebooks-master\jupyter-notebooks`; the source repository remains intact.
- Included one of the similar 2022 raster workshops (SciPy) to keep the study path focused. Specialized tasking, ordering, platform migration, and larger machine-learning workflows remain in the source repository.
- [CATALOG.md](CATALOG.md) links every learning notebook; checkpoints are excluded from the catalog.
- [file-manifest.csv](file-manifest.csv) records original and destination paths and SHA-256 checksums for transferred course/tutorial files. Every recorded destination was checked against its source checksum.
- Planet's original [license](00-Source-Reference/LICENSE) is retained.

