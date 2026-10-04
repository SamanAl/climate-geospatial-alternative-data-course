"""Reproducible fictional teaching data. No observations or investment forecasts."""
from pathlib import Path
import json
import shutil
import hashlib
import numpy as np
import pandas as pd
import geopandas as gpd
from shapely.geometry import box, LineString
import rasterio
from rasterio.transform import from_origin
import xarray as xr

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data'
DATA.mkdir(exist_ok=True)
rng = np.random.default_rng(42)

assets = pd.DataFrame({
    'asset_id': [f'A{i:02}' for i in range(1, 13)],
    'asset_name': ['Bay warehouse','Canal apartments','Cedar logistics','Delta solar',
                   'Elm housing','Foundry storage','Grove office','Harbor data center',
                   'Ivy apartments','Juniper depot','Kestrel logistics','Lagoon storage'],
    'sector': ['Logistics','Housing','Logistics','Energy','Housing','Logistics',
               'Office','Digital infrastructure','Housing','Logistics','Logistics','Logistics'],
    'longitude': [-95.48,-95.42,-95.33,-95.26,-95.45,-95.37,-95.30,-95.22,-95.40,-95.28,-95.12,-95.485],
    'latitude': [29.65,29.70,29.72,29.67,29.79,29.81,29.86,29.78,29.88,29.83,29.76,29.89],
    'equity_usd_m': [20,35,28,18,42,16,33,60,25,22,30,12],
    'cooling_backup_verified': [False,True,False,True,False,False,True,False,True,False,False,False],
})
assets.to_csv(DATA / 'assets.csv', index=False)
points = gpd.GeoDataFrame(assets, geometry=gpd.points_from_xy(assets.longitude, assets.latitude), crs=4326)
points.to_file(DATA / 'assets.geojson', driver='GeoJSON')
points.to_file(DATA / 'assets.gpkg', layer='assets', driver='GPKG')
shp = DATA / 'shapefile_example'
shp.mkdir(exist_ok=True)
points[['asset_id','sector','geometry']].to_file(shp / 'assets.shp', driver='ESRI Shapefile')

zones = gpd.GeoDataFrame({'zone_id':['Z1','Z2'], 'zone_name':['West service area','East service area']},
                         geometry=[box(-95.50,29.60,-95.35,29.90),box(-95.35,29.60,-95.20,29.90)],crs=4326)
zones.to_file(DATA / 'service_areas.geojson', driver='GeoJSON')
roads = gpd.GeoDataFrame({'route':['Teaching corridor']},geometry=[LineString([(-95.49,29.64),(-95.35,29.75),(-95.21,29.86)])],crs=4326)
roads.to_file(DATA / 'corridor.geojson',driver='GeoJSON')

# Latitude descends so row 0 is the north edge, as in the accompanying GeoTIFF.
lat = np.linspace(29.875,29.625,6)
lon = np.linspace(-95.475,-95.225,6)
time = pd.date_range('1991-01-01','2024-12-31',freq='D')
season = 9*np.cos(2*np.pi*(time.dayofyear.to_numpy()-205)/365.25)
trend = 0.045*(time.year.to_numpy()-1991)
spatial = np.linspace(-1.5,2.5,36).reshape(6,6)
values = (27+season[:,None,None]+trend[:,None,None]+spatial[None,:,:]
          +rng.normal(0,2.2,(len(time),1,1))+rng.normal(0,0.6,(len(time),6,6))).astype('float32')
values[:,0,0] = np.nan  # A12: unknown climate coverage, never interpreted as zero heat.
values[time.year==2005,1,1] = np.nan  # Entire missing year at one other cell.
ds = xr.Dataset({'tasmax': (('time','latitude','longitude'), values+273.15)},
    coords={'time':time,'latitude':lat,'longitude':lon},
    attrs={'title':'SYNTHETIC daily maximum air temperature for teaching',
           'source':'Seed 42; sinusoidal season + imposed 0.045 C/year trend + noise; NOT observations',
           'geospatial_crs':'EPSG:4326','Conventions':'CF-1.8'})
ds.tasmax.attrs = {'units':'K','long_name':'Synthetic daily maximum near-surface air temperature','standard_name':'air_temperature','cell_methods':'time: maximum'}
ds.latitude.attrs={'units':'degrees_north','standard_name':'latitude'}
ds.longitude.attrs={'units':'degrees_east','standard_name':'longitude'}
ds.to_netcdf(DATA / 'synthetic_daily_temperature.nc',engine='scipy')
recent = ds.tasmax.sel(time='2024')-273.15
days = (recent>=35).sum('time').where(recent.count('time')>=0.9*recent.sizes['time']).values.astype('float32')
with rasterio.open(DATA / 'synthetic_hot_days_2024.tif','w',driver='GTiff',height=6,width=6,count=1,
                   dtype='float32',crs='EPSG:4326',transform=from_origin(-95.5,29.9,0.05,0.05),nodata=-9999) as dst:
    dst.write(np.nan_to_num(days,nan=-9999),1)
    dst.set_band_description(1,'Synthetic days with daily maximum >=35 C in 2024')
    dst.update_tags(source='SYNTHETIC teaching data',units='days',threshold_c='35',year='2024')

# A real local image is used only to inspect the file structure, not to infer climate.
source = ROOT.parent / 'Geospatial Learning/03-Raster-Fundamentals/getting-to-know-sat-imagery/example.tif'
if source.exists():
    shutil.copy2(source,DATA / 'real_satellite_example.tif')
    license_path = ROOT.parent / 'Geospatial Learning/00-Source-Reference/LICENSE'
    shutil.copy2(license_path,DATA / 'PLANET_REPOSITORY_LICENSE')
manifest = []
for path in sorted(DATA.rglob('*')):
    if path.is_file() and path.name!='manifest.json':
        manifest.append({'file':str(path.relative_to(DATA)), 'bytes':path.stat().st_size,
                         'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
(DATA/'manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
print(f'Created {len(manifest)} data files in {DATA}')
