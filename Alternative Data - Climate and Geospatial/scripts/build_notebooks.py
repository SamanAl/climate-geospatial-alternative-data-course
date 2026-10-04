"""Author the teaching notebooks; all analysis stays visible in notebook cells."""
from pathlib import Path
from textwrap import dedent
import sys
import nbformat as nbf

ROOT = Path(__file__).resolve().parents[1]
NB = ROOT / 'notebooks'
NB.mkdir(exist_ok=True)

def md(s): return nbf.v4.new_markdown_cell(dedent(s).strip())
def code(s): return nbf.v4.new_code_cell(dedent(s).strip())
def save(name, cells):
    if len(sys.argv)>1 and name not in sys.argv[1:]:
        return
    nb = nbf.v4.new_notebook(cells=cells, metadata={
        'kernelspec':{'display_name':'Python 3','language':'python','name':'python3'},
        'language_info':{'name':'python','version':'3.12'}})
    # Preserve verified outputs for wording-only revisions, never for changed code.
    existing = NB / (name+'.ipynb')
    if existing.exists():
        previous = nbf.read(existing, as_version=4)
        old_code = [c for c in previous.cells if c.cell_type=='code']
        new_code = [c for c in nb.cells if c.cell_type=='code']
        if [c.source for c in old_code] == [c.source for c in new_code]:
            for before, after in zip(old_code,new_code):
                after.outputs = before.outputs
                after.execution_count = before.execution_count
                after.metadata = before.metadata
    nbf.validate(nb)
    nbf.write(nb, NB / (name+'.ipynb'))

setup = code('''
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display

# Works when Jupyter starts in the project root or a subfolder.
ROOT = next((p for p in [Path.cwd(), *Path.cwd().parents]
             if (p / 'data/assets.csv').exists()), None)
if ROOT is None:
    raise FileNotFoundError('Keep the notebooks and data folders together; open this project in Jupyter.')
DATA = ROOT / 'data'
OUT = ROOT / 'outputs'
OUT.mkdir(exist_ok=True)
plt.rcParams.update({'figure.figsize': (9, 5), 'font.size': 11,
                     'axes.spines.top': False, 'axes.spines.right': False,
                     'axes.titleweight': 'bold', 'figure.dpi': 110})
print('Ready. Core lessons use bundled local data; no API key needed.')
''')

save('00_Start_Here_Alternative_Data', [
md('''
# 00 | A different lens on an asset
### Alternative data, climate and geospatial foundations
**15 minutes · Basic Python and pandas assumed; no geospatial or climate background needed**

You are helping a private-markets team review a portfolio of buildings and infrastructure.
A spreadsheet tells you the sector and capital invested. What else would you want to know about the places where those assets operate?

**By the end:** distinguish a measurement from a proxy; explain why location links datasets; frame a spatial question using familiar portfolio analysis.

> All assets and climate values in our portfolio case are **fictional teaching data** at real-world coordinates near Houston. They describe no actual properties or local climate. One separate satellite image is a real file used to examine raster structure.
'''),
md('''
## 1. What makes data “alternative”?
In this class, alternative data means information outside the conventional financial statements and transaction records used by an analyst. The boundary depends on the team: an engineer's routine sensor reading can be an investor's alternative dataset.

| Example | What it directly records | Possible question | What it cannot establish alone |
|---|---|---|---|
| Satellite image | Reflected or emitted energy recorded by a sensor | Has land cover around a site changed? | Revenue, occupancy, or causation |
| Building footprints | Mapped outlines | Where is the physical exposure? | Exact ownership or replacement cost |
| Temperature history | Observed or estimated temperature over time | How often is a threshold exceeded? | Asset damage or future losses |
| Mobility counts | Recorded device activity | Has activity around a site changed? | All visitors, spending, or a representative population |

**Discuss (2 minutes):** Would a brighter night-time image mean a more profitable company? Name two competing explanations.
'''),
md('''
## 2. Build on the Python you know
We assume you can import a package, filter a DataFrame, group rows and read a plot. Our focus is what changes when records have **geometry** and measurements have **space and time dimensions**.

GeoPandas extends tables with geometry; Rasterio reads spatial grids; xarray works with named multidimensional arrays. We introduce each as needed. Run cells in order and use **Restart Kernel and Run All** after changes to check reproducibility. Saved outputs and the `html` folder are available for reference.
'''), setup,
code('''
assets = pd.read_csv(DATA / 'assets.csv')  # A DataFrame is a table.
display(assets[['asset_id','asset_name','sector','equity_usd_m']].head())
print(f'{len(assets)} fictional assets; total equity ${assets.equity_usd_m.sum():.0f} million')
'''),
md('''
## 3. Inspect the portfolio before adding another dataset
The familiar pandas filter below selects a sector. Compare `"Housing"` and `"Logistics"`: would one climate indicator answer the same operational question for both?
`equity_usd_m` means millions of US dollars invested as equity in this fictional example; it is not a loss estimate or property value.
'''),
code('''
sector_to_view = 'Housing'  # TRY: 'Logistics' or 'Energy'
display(assets.loc[assets.sector == sector_to_view,
                   ['asset_name','sector','equity_usd_m']])
'''),
code('''
by_sector = assets.groupby('sector').equity_usd_m.sum().sort_values()
ax = by_sector.plot.barh(color='#147d92')
ax.set(xlabel='Fictional equity invested (USD millions)', ylabel='',
       title='What the financial table shows us')
plt.tight_layout()
plt.show()
'''),
md('''
## 4. From a question to evidence
**Question → location → measurement → quality check → comparison → decision to investigate.**

Before using a new dataset ask: Who produced it? When? What area and population does it cover? What are its units? What is missing? Are the dates and locations aligned with our asset? Can we explain the link to operations? Do we have permission to use it?

**Exit ticket:** Write one operational question about an asset, one useful alternative dataset, and one reason that dataset could mislead you.

**Coding extension:** calculate each sector's share of total equity with pandas. Explain why its share of asset count may differ, and which denominator you would use for your question.

Next: open **01_Data_Formats_and_First_Map.ipynb**. We will turn two spreadsheet columns into geometry.
''')])

save('01_Data_Formats_and_First_Map', [
md('''
# 01 | What does geospatial data look like?
**35 minutes · Table → geometry → map → file format**

**By the end:** recognize points, lines, polygons and grids; inspect five common formats; build a map from longitude and latitude.

**Case question:** How can we connect an asset spreadsheet to information about its surroundings?
All portfolio features are synthetic. We build on DataFrames and plotting; geometry and coordinate systems are introduced here.
'''), setup,
md('''
## 1. Two ways to describe space
**Vector:** distinct objects. A point might represent a warehouse; a line a road; a polygon a service area.
**Raster:** a grid of cells. Each cell holds a value, such as temperature or a sensor reading. A raster can have multiple bands, and a climate dataset can add a time dimension.

A **format** is the container, not a guarantee of quality. A beautifully mapped CSV can still contain a wrong address.
'''),
code('''
import geopandas as gpd
assets = pd.read_csv(DATA / 'assets.csv')
display(assets.head(3))

# GeoJSON and points_from_xy use longitude (x) first, then latitude (y).
points = gpd.GeoDataFrame(assets,
    geometry=gpd.points_from_xy(assets.longitude, assets.latitude), crs='EPSG:4326')
display(points[['asset_id','geometry']].head(3))
print('CRS:', points.crs)
'''),
md('''
The **coordinate reference system (CRS)** tells us how numbers correspond to locations on Earth. `EPSG:4326` uses longitude/latitude in degrees here. Longitude is east–west; latitude is north–south. Negative longitude places these example points west of Greenwich.

**Predict:** What happens if the two columns are reversed? A numeric range check is useful, but cannot catch every location mistake.
'''),
code('''
assert points.longitude.between(-180,180).all()
assert points.latitude.between(-90,90).all()
assert points.asset_id.is_unique
zones = gpd.read_file(DATA / 'service_areas.geojson')
roads = gpd.read_file(DATA / 'corridor.geojson')
fig, ax = plt.subplots()
zones.plot(ax=ax, facecolor='#edf3f4', edgecolor='#52757e')
roads.plot(ax=ax, color='#db8426', linewidth=3, label='Fictional corridor')
points.plot(ax=ax, color='#126f87', markersize=55, label='Fictional assets')
for row in points.itertuples():
    ax.annotate(row.asset_id,(row.geometry.x,row.geometry.y),xytext=(4,4),textcoords='offset points',fontsize=9)
ax.set(xlabel='Longitude (degrees)', ylabel='Latitude (degrees)', title='Points, a line, and polygons — synthetic portfolio')
from matplotlib.ticker import MaxNLocator
ax.xaxis.set_major_locator(MaxNLocator(5))
ax.legend(loc='lower right')
plt.tight_layout()
plt.show()
'''),
md('''
## 2. Open the container
**Predict:** Will GeoJSON look like a spreadsheet or nested text? A **Feature** stores geometry alongside descriptive **properties**. A **FeatureCollection** holds features together.
'''),
code('''
import json
geojson = json.loads((DATA / 'assets.geojson').read_text())
print(json.dumps(geojson['features'][0], indent=2))
'''),
md('''
## 3. A small format museum

| Format | Useful mental picture | Often used for | Watch for |
|---|---|---|---|
| CSV | Plain table | Addresses or coordinates, attributes | Geometry and CRS are not automatically encoded |
| GeoJSON | Nested text containing shapes | Small vector datasets and web exchange | Longitude before latitude; large files can be bulky |
| Shapefile | A set of companion files | Legacy vector delivery | Keep `.shp`, `.shx`, `.dbf`, `.prj` and other supplied companions together; field names are limited |
| GeoPackage | One SQLite database file | One or more geospatial layers | Choose the correct layer |
| GeoTIFF | Image/grid with location metadata | Imagery or a mapped measurement | CRS, grid size, units, missing-data marker |
| NetCDF | Named arrays with dimensions and metadata | Time × latitude × longitude climate data | Variable, units, calendar, time aggregation |

You will open actual examples below and in Notebooks 03–04. GeoPackage and NetCDF can store more than the simple examples shown here.
'''),
code('''
from_geopackage = gpd.read_file(DATA / 'assets.gpkg', layer='assets')
from_shapefile = gpd.read_file(DATA / 'shapefile_example/assets.shp')
display(pd.DataFrame({
    'container':['CSV','GeoJSON','GeoPackage','Shapefile'],
    'features':[len(assets),len(geojson['features']),len(from_geopackage),len(from_shapefile)]}))
print('Shapefile companions:', [p.name for p in sorted((DATA/'shapefile_example').glob('*'))])
print('GeoPackage CRS:', from_geopackage.crs)
assert set(from_geopackage.asset_id) == set(assets.asset_id)
'''),
md('''
## Try it · 5 minutes
1. Show only housing assets on the map. Does filtering change the geography or only the selected records?
2. Choose a file format for (a) sharing 12 asset locations, (b) handing over several boundary layers, (c) storing daily temperature for 30 years.
3. A supplier sends only `assets.shp`. What would you request?

**Coding extension:** export a filtered GeoJSON into `outputs/` with `points.to_file(...)`, reload it and check IDs and CRS. Add a coordinate-quality check for missing values and the expected study extent; explain why global latitude/longitude bounds alone are insufficient.

**Takeaway:** location is data, not decoration. Inspect geometry, metadata and attributes before trusting the map.

Sources: [GeoJSON specification](https://www.rfc-editor.org/rfc/rfc7946), [GeoPackage](https://www.ogc.org/standards/geopackage/), [GeoTIFF](https://www.ogc.org/standards/geotiff/), [NetCDF](https://docs.unidata.ucar.edu/nug/current/).
''')])

save('02_Location_Joins_and_Distance', [
md('''
# 02 | Where is this asset, and what is nearby?
**35 minutes · Spatial joins and distance**

**By the end:** attach area attributes to points, retain unmatched assets, and measure distance using a suitable projected CRS.

**Case question:** Which service area contains each asset, and which sites lie close to a transport corridor?
The corridor and areas are fictional and are **not flood zones** or evidence of transport access.
'''), setup,
code('''
import geopandas as gpd
from shapely.geometry import Point
points = gpd.read_file(DATA / 'assets.geojson')
zones = gpd.read_file(DATA / 'service_areas.geojson')
roads = gpd.read_file(DATA / 'corridor.geojson')
assert points.crs == zones.crs == roads.crs
assert zones.geometry.is_valid.all()
'''),
md('''
## 1. Join by place rather than by a shared name
A spreadsheet join matches an ID. A **spatial join** matches a relationship such as “point lies inside polygon.”
`how='left'` keeps every asset; `predicate='within'` requires the point to be in the polygon's interior.

**Predict:** Should an asset outside both polygons disappear from our portfolio?
'''),
code('''
joined = gpd.sjoin(points, zones[['zone_name','geometry']], how='left', predicate='within')
joined['zone_name'] = joined.zone_name.fillna('Outside supplied areas')
assert len(joined) == len(points)  # Our example polygons do not overlap.
display(joined[['asset_id','asset_name','zone_name']])
summary = joined.groupby('zone_name').agg(assets=('asset_id','count'), equity_usd_m=('equity_usd_m','sum'))
display(summary)
assert summary.equity_usd_m.sum() == points.equity_usd_m.sum()
'''),
md('''
## 2. A boundary is a decision, too
A point exactly on a shared boundary is not `within` either polygon. `intersects` can match it to both. Overlapping polygons can also duplicate rows. Before summing money, inspect match counts and define an explicit assignment rule.
'''),
code('''
boundary_point = Point(-95.35,29.75)
display(pd.DataFrame({'zone':zones.zone_name,
                     'within':[boundary_point.within(g) for g in zones.geometry],
                     'intersects':[boundary_point.intersects(g) for g in zones.geometry]}))
'''),
md('''
## 3. Degrees are not metres
For this compact example near Houston we use **UTM zone 15N (`EPSG:32615`)**, a projected coordinate system whose units are metres. It is a local choice, not a universal solution.

`set_crs` labels what coordinates already mean; `to_crs` transforms the coordinates. Relabelling degrees as metres would be wrong. See the [GeoPandas projection guide](https://geopandas.org/en/stable/docs/user_guide/projections.html).
'''),
code('''
points_m = points.to_crs('EPSG:32615')
roads_m = roads.to_crs(points_m.crs)
corridor = roads_m.geometry.union_all()
points_m['distance_km'] = points_m.geometry.distance(corridor)/1000
nearby_km = 3.0  # TRY: 1.0 or 5.0
points_m['near_corridor'] = points_m.distance_km <= nearby_km
display(points_m[['asset_id','distance_km','near_corridor']].round(2))
'''),
code('''
fig, ax = plt.subplots()
gpd.GeoSeries([corridor.buffer(nearby_km*1000)],crs=points_m.crs).plot(ax=ax,color='#dfedf0')
roads_m.plot(ax=ax,color='#d67b27',linewidth=2,label='Fictional corridor')
points_m.plot(ax=ax,column='near_corridor',categorical=True,legend=True,cmap='coolwarm',markersize=65)
ax.set(xlabel='Easting (metres)',ylabel='Northing (metres)',
       title=f'Synthetic sites within {nearby_km:g} km straight-line distance')
from matplotlib.ticker import MaxNLocator
ax.xaxis.set_major_locator(MaxNLocator(4))
plt.tight_layout()
plt.show()
'''),
md('''
## Try it · 5 minutes
1. Change the distance threshold from 3 km to 1 km. Does the selected group grow or shrink?
2. Explain why straight-line proximity is not driving time, road access, or a causal explanation of asset performance.
3. Why is “outside supplied areas” different from “no exposure”?

**Coding extension:** calculate equity by area using an inner join, compare the total with the left join, and explain what went missing. Build a table of asset counts and equity within 1, 3 and 5 km of the corridor. Check that counts cannot fall as the radius increases.

**Takeaway:** spatial matching is an analytical choice. Boundaries, projection and missing matches can change portfolio summaries.
''')])

save('03_Rasters_Images_and_Exposure', [
md('''
# 03 | A map made of numbers
**35 minutes · GeoTIFFs, grid cells and asset sampling**

**By the end:** read raster metadata; explain resolution and nodata; extract a cell value at an asset; distinguish an image from a climate measurement.

**Case question:** What does a gridded heat indicator say at each asset location?
Our heat grid is **synthetic** and stores the number of days in 2024 with daily maximum air temperature ≥35°C. The threshold is a teaching choice, not an engineering standard.
'''), setup,
code('''
import rasterio
from rasterio.plot import plotting_extent
import geopandas as gpd
points = gpd.read_file(DATA / 'assets.geojson')
with rasterio.open(DATA / 'synthetic_hot_days_2024.tif') as src:
    heat = src.read(1, masked=True)
    extent = plotting_extent(src)
    display(pd.Series({'CRS':str(src.crs),'rows':src.height,'columns':src.width,
                       'bands':src.count,'cell size (degrees)':src.res,'nodata marker':src.nodata}))
    print('Metadata:', src.tags())
    print('Top-left 3 by 3 cells ( -- means missing):')
    print(heat[:3,:3])
'''),
md('''
## 1. Read the grid before reading the colors
The dataset is just 6 × 6 cells. Its 0.05-degree spacing is several kilometres here, not rooftop resolution. The top-left cell is deliberately missing. A **nodata** marker represents “no valid value,” not zero days.

The same grid could be colored many ways. The legend's variable, units, period and threshold matter more than the palette. [Rasterio's mask guide](https://rasterio.readthedocs.io/en/stable/topics/masks.html) explains how missing cells are represented.
'''),
code('''
fig, ax = plt.subplots()
cmap = plt.colormaps['YlOrRd'].copy()
cmap.set_bad('#c9cfd2')
im = ax.imshow(heat, extent=extent, origin='upper', cmap=cmap, vmin=0, vmax=150)
points.plot(ax=ax,color='#113748',markersize=30)
for row in points.itertuples():
    ax.annotate(row.asset_id,(row.geometry.x,row.geometry.y),xytext=(3,3),textcoords='offset points',fontsize=8)
fig.colorbar(im,ax=ax,label='Synthetic days with daily maximum ≥35°C in 2024')
ax.set(xlabel='Longitude (degrees)',ylabel='Latitude (degrees)',title='Synthetic heat grid — gray means no data')
from matplotlib.ticker import MaxNLocator
ax.xaxis.set_major_locator(MaxNLocator(5))
plt.tight_layout()
plt.show()
'''),
md('''
## 2. Put the grid value back into a table
Sampling chooses the cell containing a coordinate; it does not measure conditions inside the building.
We explicitly check the extent and nodata. A11 is outside the grid; A12 is inside a missing cell. Both remain **unknown**.
'''),
code('''
records = []
with rasterio.open(DATA / 'synthetic_hot_days_2024.tif') as src:
    projected = points.to_crs(src.crs)
    for row in projected.itertuples():
        x, y = row.geometry.x, row.geometry.y
        inside = src.bounds.left <= x < src.bounds.right and src.bounds.bottom < y <= src.bounds.top
        value = np.nan
        status = 'outside grid'
        if inside:
            sample = next(src.sample([(x,y)],masked=True))[0]
            if np.ma.is_masked(sample) or not np.isfinite(sample):
                status = 'missing cell'
            else:
                value, status = float(sample), 'available'
        records.append({'asset_id':row.asset_id,'hot_days':value,'coverage':status})
sampled = pd.DataFrame(records)
display(sampled)
assert sampled.hot_days.isna().sum() == 2
'''),
md('''
## 3. A real satellite file: inspect, do not over-interpret
The separate `real_satellite_example.tif` was copied from your local Planet teaching repository. We inspect its metadata and first band. The acquisition date, calibration and interpretation have not been independently verified here. A sensor band's pixel values are not automatically air temperature, vegetation health or asset value.
'''),
code('''
real_path = DATA / 'real_satellite_example.tif'
if real_path.exists():
    with rasterio.open(real_path) as src:
        print('Real example:', src.width, 'columns x', src.height, 'rows;', src.count, 'bands')
        print('CRS:', src.crs, '| Pixel size in CRS units:', src.res)
        print('Band descriptions:', src.descriptions)
        band = src.read(1,out_shape=(min(400,src.height),min(400,src.width)),masked=True)
    valid = band.compressed()
    low, high = np.percentile(valid,[2,98])
    fig, ax = plt.subplots(figsize=(7,5))
    im = ax.imshow(band,cmap='gray',vmin=low,vmax=high)
    ax.set(title='Real satellite file · first band, display stretch only',xlabel='Preview column',ylabel='Preview row')
    fig.colorbar(im,ax=ax,label='Stored band value (calibration not established here)')
    plt.tight_layout()
    plt.show()
else:
    print('Optional real image not bundled. The synthetic raster lesson remains complete.')
'''),
md('''
## Try it · 5 minutes
1. What could differ between two buildings in the same heat-grid cell?
2. Why would replacing missing values with zero be misleading?
3. Compare the real image's dimensions with the 6 × 6 heat grid. Does more detail always mean more useful evidence for your question?

**Coding extension:** merge the sampled values back to the asset table using `validate='one_to_one'`. Calculate data coverage by sector, retaining both unknown statuses. Explain why averaging only available values answers a different question from treating unknowns as zero.

**Takeaway:** a cell is a spatial summary. A map's apparent precision can exceed the precision of the data.
''')])

save('04_Climate_Time_and_Uncertainty', [
md('''
# 04 | Weather becomes a climate question
**40 minutes · NetCDF, units, time and comparison periods**

**By the end:** inspect a climate data cube; convert kelvin to Celsius; compare a baseline with a recent period; count threshold days while retaining missingness.

**Case question:** Is a hot year the same as a change in climate?
Our 1991–2024 temperatures are **generated teaching data**, not Houston observations, reanalysis, or projections. A trend was deliberately built into them. They cannot demonstrate real climate change.
'''), setup,
md('''
## 1. Know what kind of evidence you have
**Weather** describes conditions at a particular time. **Climate** describes their longer-term distribution: averages, seasonality, extremes and variability.

| Data type | What it is | Question to ask |
|---|---|---|
| Observation | Instrument measurement | Where is the instrument and how is it calibrated? |
| Reanalysis | Past conditions reconstructed using observations and a model | What are the grid scale and uncertainties? |
| Projection | Modelled future under specified assumptions | Which scenario, horizon, model and baseline? |
| Our synthetic data | Values created for this exercise | What did the generator deliberately build in? |

ERA5 is an example of reanalysis, not a future forecast. [Copernicus explains the distinction](https://climate.copernicus.eu/what-copernicus-climate-change-services-era5-reanalysis-dataset).
'''),
code('''
import xarray as xr
with xr.open_dataset(DATA / 'synthetic_daily_temperature.nc',engine='scipy') as source:
    climate = source.load()
display(climate)
print('Variable metadata:', climate.tasmax.attrs)
print('First date:', str(climate.time.values[0])[:10], '| Last:', str(climate.time.values[-1])[:10])
'''),
md('''
NetCDF stores named variables and dimensions. Here `tasmax` means daily maximum air temperature, measured in kelvin. The array dimensions are **time × latitude × longitude**.

Selecting one grid cell gives a time series. Selecting one date gives a map. We use one of the bundled cells, not a city-wide observation.
'''),
code('''
temperature_c = climate.tasmax - 273.15
temperature_c.attrs = {'units':'degC','long_name':'Synthetic daily maximum air temperature'}
series = temperature_c.sel(latitude=29.725,longitude=-95.325,method='nearest')
print('Selected cell center:',float(series.latitude),float(series.longitude))
recent = series.sel(time='2024')
fig, ax = plt.subplots()
ax.plot(recent.time.values,recent.values,color='#167b8d',linewidth=1)
ax.axhline(35,color='#c56433',linestyle='--',label='Teaching threshold: 35°C')
ax.set(title='A synthetic year of weather',xlabel='Date',ylabel='Daily maximum air temperature (°C)')
ax.legend()
plt.tight_layout()
plt.show()
'''),
md('''
## 2. Compare like with like
We use 1991–2020 as a 30-year reference period and 2020–2024 as a recent five-year period. They overlap by one year, which we state explicitly. The five-year mean is **not** a new 30-year climate normal.
We compare monthly means with the same months to avoid mistaking seasonality for change. Here the quantity is the mean of daily maxima, not the all-hours mean temperature.
'''),
code('''
baseline = series.sel(time=slice('1991','2020')).groupby('time.month').mean()
recent_mean = series.sel(time=slice('2020','2024')).groupby('time.month').mean()
fig, axes = plt.subplots(1,2,figsize=(11,4))
axes[0].plot(baseline.month,baseline,label='1991–2020',color='#167b8d')
axes[0].plot(recent_mean.month,recent_mean,label='2020–2024',color='#d37535')
axes[0].set(title='Same months, two periods',xlabel='Month',ylabel='Mean daily maximum (°C)')
axes[0].legend()
anomaly = recent_mean - baseline
axes[1].bar(anomaly.month,anomaly,color='#d37535')
axes[1].axhline(0,color='gray',linewidth=0.8)
axes[1].set(title='Synthetic recent-minus-baseline difference',xlabel='Month',ylabel='Difference (°C)')
plt.tight_layout()
plt.show()
'''),
md('''
## 3. Count hot days without turning missing data into “cool” days
Comparing a missing number to 35 returns false. A naive sum can therefore report zero hot days for an entirely missing year. We require at least 90% of the year's daily values. This is an illustrative completeness rule, not a climate-data standard.
For partially missing accepted years, the result counts **observed available hot days**, not an imputed full-year total. Missingness can still bias it.
'''),
code('''
threshold_c = 35  # TRY: 32 or 38, then rerun this cell and inspect the chart.
def annual_hot_days(temperatures, threshold):
    valid_days = temperatures.resample(time='YS').count()
    # Actual number of calendar days, including leap years.
    calendar_days = xr.ones_like(temperatures).resample(time='YS').sum()
    observed_hot = (temperatures >= threshold).resample(time='YS').sum()
    return observed_hot.where(valid_days/calendar_days >= 0.9)

annual = annual_hot_days(series, threshold_c)
fig, ax = plt.subplots()
ax.plot(annual.time.dt.year,annual,marker='o',markersize=3,color='#d37535')
ax.set(title=f'Synthetic days ≥{threshold_c}°C by year',xlabel='Year',ylabel='Hot days with adequate data coverage')
plt.tight_layout()
plt.show()

# Inspect the deliberately missing year at a different cell.
gap_cell = temperature_c.isel(latitude=1,longitude=1)
naive = int((gap_cell.sel(time='2005') >= threshold_c).sum())
checked = float(annual_hot_days(gap_cell,threshold_c).sel(time='2005').item())
print('Entirely missing 2005: naive count =',naive,'; coverage-aware result =',checked)
assert np.isnan(checked)
'''),
md('''
## Try it · 5 minutes
1. Does raising the temperature threshold increase or decrease the number of hot days?
2. Explain why one hot year cannot by itself establish a climate trend.
3. Before using a future heat projection, name four pieces of metadata you would request.

**Coding extension:** change the recent period to 2021–2024 to remove the overlap, and compare monthly anomalies with the original result. Repeat hot-day counts at 32, 35 and 38°C. Explain how changes in the threshold and comparison period affect the interpretation.

**Takeaway:** the period, aggregation, units, scenario and missingness are part of the number's meaning.
Reference for the array operations: [xarray time-series guide](https://docs.xarray.dev/en/stable/user-guide/time-series.html).
''')])

save('05_Private_Markets_Due_Diligence_Lab', [
md('''
# 05 | Which assets deserve the next question?
**35 minutes · Applied portfolio screening and a short memo**

**By the end:** combine asset attributes with a spatial indicator; report coverage; test a decision rule; communicate an evidence gap.

**Scenario:** Your team has time for three initial operational interviews. Use the fictional heat screen to recommend questions and a shortlist. This is an educational triage exercise, not valuation or an estimated loss model.
This notebook runs independently using the bundled data; no previous notebook outputs are required.
'''), setup,
md('''
## 1. Separate hazard, exposure and vulnerability
**Hazard:** potentially harmful climate conditions. **Exposure:** assets or people in places affected. **Vulnerability:** how susceptible they are, including operational sensitivity and capacity to respond.
The [IPCC risk framework](https://www.ipcc.ch/site/assets/uploads/2021/01/The-concept-of-risk-in-the-IPCC-Sixth-Assessment-Report.pdf) connects these concepts. Our hot-day grid supplies only a simplified hazard-related indicator. Locations identify exposure; an unverified backup system is a question about vulnerability, not proof of failure.

Actual financial consequences also require evidence on operations, asset condition, contracts, insurance, adaptation and costs. We will not multiply a heat value by equity and call it loss.
'''),
code('''
import geopandas as gpd
import rasterio
assets = gpd.read_file(DATA / 'assets.geojson')
rows = []
with rasterio.open(DATA / 'synthetic_hot_days_2024.tif') as src:
    for asset in assets.to_crs(src.crs).itertuples():
        x,y = asset.geometry.x,asset.geometry.y
        inside = src.bounds.left <= x < src.bounds.right and src.bounds.bottom < y <= src.bounds.top
        value, coverage = np.nan, 'outside grid'
        if inside:
            sampled = next(src.sample([(x,y)],masked=True))[0]
            if np.ma.is_masked(sampled) or not np.isfinite(sampled):
                coverage = 'missing cell'
            else:
                value, coverage = float(sampled), 'available'
        rows.append({'asset_id':asset.asset_id,'hot_days_2024':value,'coverage':coverage})
screen = pd.DataFrame(assets.drop(columns='geometry')).merge(pd.DataFrame(rows),on='asset_id',validate='one_to_one')
assert len(screen) == len(assets)
display(screen[['asset_id','sector','equity_usd_m','hot_days_2024','coverage','cooling_backup_verified']])
'''),
md('''
## 2. State your rule before looking at the shortlist
Illustrative rule: send assets with **at least 90 hot days and no verified cooling backup** to an operations review. Send missing climate values to a separate data follow-up. The 90-day cutoff is an analyst's classroom choice, not a validated safety threshold.

“No verified backup” includes unknown documentation. It does not establish that a system is absent. “Below review rule” does not mean safe from climate hazards.
'''),
code('''
review_threshold_days = 90  # TRY: 60 or 120
def assign_review(table, threshold):
    result = table.copy()
    result['review'] = 'Below rule / backup verified'
    needs_review = (result.hot_days_2024 >= threshold) & ~result.cooling_backup_verified.astype(bool)
    result.loc[needs_review,'review'] = 'Operations follow-up'
    result.loc[result.hot_days_2024.isna(),'review'] = 'Data follow-up'
    return result

screen = assign_review(screen,review_threshold_days)
summary = screen.groupby('review').agg(assets=('asset_id','count'),equity_usd_m=('equity_usd_m','sum'))
summary['share_of_total_equity_pct'] = 100*summary.equity_usd_m/screen.equity_usd_m.sum()
display(summary.round(1))
assert summary.assets.sum() == len(screen)
assert np.isclose(summary.share_of_total_equity_pct.sum(),100)
covered = screen.hot_days_2024.notna()
print(f'Climate data covers {covered.sum()}/{len(screen)} assets and '
      f'{screen.loc[covered,"equity_usd_m"].sum()/screen.equity_usd_m.sum():.1%} of total equity.')
'''),
code('''
fig, ax = plt.subplots()
summary.equity_usd_m.plot.barh(ax=ax,color='#167b8d')
ax.set(title='Synthetic portfolio · equity by review category',
       xlabel='Equity invested (USD millions), not estimated loss',ylabel='')
plt.tight_layout()
plt.show()

shortlist = screen.loc[screen.review == 'Operations follow-up'].sort_values(
    ['hot_days_2024','equity_usd_m'],ascending=False).head(3)
display(shortlist[['asset_id','asset_name','hot_days_2024','equity_usd_m']])
'''),
md('''
## 3. How much does the answer depend on our rule?
Change the days cutoff while keeping the ≥35°C hot-day definition fixed. These are two different thresholds: one defines a hot day, the other defines our review rule.
Ranking by hot days first and equity second is another classroom choice. A small critical facility might warrant more attention than a large less-sensitive property.
'''),
code('''
sensitivity = []
for cutoff in [60,90,120]:
    variant = assign_review(screen,cutoff)
    follow = variant.review == 'Operations follow-up'
    sensitivity.append({'review_cutoff_days':cutoff,'assets_for_operations':int(follow.sum()),
                        'equity_for_operations_usd_m':variant.loc[follow,'equity_usd_m'].sum(),
                        'unknown_assets':int(variant.hot_days_2024.isna().sum())})
display(pd.DataFrame(sensitivity))
screen.to_csv(OUT / 'synthetic_portfolio_screen.csv',index=False)
print('Saved outputs/synthetic_portfolio_screen.csv')
'''),
md('''
## Your investment-team memo · 8 minutes
Write **120–180 words**. Address:

1. **Finding:** Which assets would you interview first, using the stated rule?
2. **Evidence:** Report count and equity coverage; distinguish the full-portfolio denominator from the covered subset.
3. **Limitation:** Explain the synthetic data, grid resolution, single-year indicator and arbitrary threshold.
4. **Next questions:** Request two pieces of asset-level evidence before estimating financial effects.

Do not conclude “safe,” “uninsurable,” or “expected loss” from this screen.

**Discuss:** If a site lacks climate data, should it receive less attention or a different kind of attention?

**Coding extension:** implement an alternative screening function and compare its selected asset IDs with the original rule. Assert that unknown assets remain in data follow-up and total equity is unchanged. Propose a sector-specific rule or multi-year metric and state what evidence would justify it.

**Takeaway:** a useful screen makes the next question more specific and makes uncertainty visible.
''')])
print('Authored six notebooks in',NB)
