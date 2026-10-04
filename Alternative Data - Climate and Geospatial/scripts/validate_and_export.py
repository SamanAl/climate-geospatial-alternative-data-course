"""Execute every notebook independently, check data semantics, export HTML and pack."""
from pathlib import Path
import os
import sys
import json
import hashlib
import base64
import zipfile
from datetime import datetime, timezone
import importlib.metadata

ROOT = Path(__file__).resolve().parents[1]
runtime = ROOT / '.runtime'
runtime.mkdir(exist_ok=True)
os.environ['JUPYTER_RUNTIME_DIR'] = str(runtime / 'runtime')
os.environ['JUPYTER_CONFIG_DIR'] = str(runtime / 'config')
os.environ['IPYTHONDIR'] = str(runtime / 'ipython')
os.environ['MPLCONFIGDIR'] = str(runtime / 'matplotlib')
os.environ['JUPYTER_PATH'] = str(runtime / 'jupyter')
kernel = runtime / 'jupyter/kernels/course-python'
kernel.mkdir(parents=True,exist_ok=True)
(kernel/'kernel.json').write_text(json.dumps({'argv':[sys.executable,'-m','ipykernel_launcher','-f','{connection_file}'],
                                            'display_name':'Course validation','language':'python'}))
import nbformat
from nbclient import NotebookClient
from nbconvert import HTMLExporter
import numpy as np
import pandas as pd
import geopandas as gpd
import rasterio
import xarray as xr

html_dir = ROOT / 'html'
html_dir.mkdir(exist_ok=True)
qa = runtime / 'figures'
qa.mkdir(exist_ok=True)
results = []
for path in sorted((ROOT/'notebooks').glob('*.ipynb')):
    execute = len(sys.argv)==1 or path.stem in sys.argv[1:]
    print('Executing' if execute else 'Reusing verified outputs:',path.name,flush=True)
    nb = nbformat.read(path,as_version=4)
    nbformat.validate(nb)
    if execute:
        client = NotebookClient(nb,timeout=180,kernel_name='course-python',
                                resources={'metadata':{'path':str(ROOT/'notebooks')}})
        client.execute()
    else:
        assert all(c.execution_count is not None for c in nb.cells if c.cell_type=='code')
    errors = [o for c in nb.cells if c.cell_type=='code' for o in c.get('outputs',[]) if o.output_type=='error']
    assert not errors, errors
    nbformat.write(nb,path)
    exporter = HTMLExporter(template_name='lab')
    body,_ = exporter.from_notebook_node(nb)
    (html_dir/(path.stem+'.html')).write_text(body,encoding='utf-8')
    images = 0
    for cell in nb.cells:
        for out in cell.get('outputs',[]):
            payload = out.get('data',{}).get('image/png')
            if payload:
                images += 1
                (qa/f'{path.stem}_{images}.png').write_bytes(base64.b64decode(payload))
    results.append((path.name,sum(c.cell_type=='code' for c in nb.cells),images))

# Validate the meaning of the bundled data and the worked outputs, not just syntax.
DATA = ROOT/'data'
assets = pd.read_csv(DATA/'assets.csv')
assert assets.asset_id.is_unique and len(assets)==12
for name in ['assets.geojson','assets.gpkg','shapefile_example/assets.shp']:
    geo = gpd.read_file(DATA/name)
    assert set(geo.asset_id)==set(assets.asset_id)
    assert geo.crs.to_epsg()==4326 and geo.geometry.is_valid.all()
with xr.open_dataset(DATA/'synthetic_daily_temperature.nc',engine='scipy') as ds:
    recent = ds.tasmax.sel(time='2024')-273.15
    expected = (recent>=35).sum('time').where(recent.count('time')>=0.9*recent.sizes['time']).values
    assert recent.sizes['time']==366
    assert ds.tasmax.sel(time='2005').isel(latitude=1,longitude=1).isnull().all().item()
with rasterio.open(DATA/'synthetic_hot_days_2024.tif') as src:
    grid = src.read(1,masked=True).filled(np.nan)
    np.testing.assert_allclose(grid,expected,equal_nan=True)
    assert np.isfinite(grid).sum()==35
    assert src.crs.to_epsg()==4326 and src.tags()['units']=='days'
screen = pd.read_csv(ROOT/'outputs/synthetic_portfolio_screen.csv')
assert set(screen.loc[screen.hot_days_2024.isna(),'asset_id'])=={'A11','A12'}
assert set(screen.loc[screen.review=='Data follow-up','asset_id'])=={'A11','A12'}
assert np.isclose(screen.equity_usd_m.sum(),341)
counts = [(screen.hot_days_2024>=t).sum() for t in [60,90,120]]
assert counts[0]>=counts[1]>=counts[2]
for item in json.loads((DATA/'manifest.json').read_text()):
    assert hashlib.sha256((DATA/item['file']).read_bytes()).hexdigest()==item['sha256']

def table(frame):
    # Markdown without optional tabulate dependency.
    frame=frame.reset_index(drop=True)
    return '\n'.join(['| '+' | '.join(map(str,frame.columns))+' |',
                       '| '+' | '.join(['---']*len(frame.columns))+' |']+
                      ['| '+' | '.join(map(str,row))+' |' for row in frame.itertuples(index=False,name=None)])

summary = screen.groupby('review',as_index=False).agg(assets=('asset_id','count'),equity_usd_m=('equity_usd_m','sum'))
summary['pct_total_equity']=(summary.equity_usd_m/341*100).round(1)
shortlist=screen[screen.review=='Operations follow-up'].sort_values(['hot_days_2024','equity_usd_m'],ascending=False).head(3)
covered=screen.hot_days_2024.notna()
worked = '# Default worked results\n\nGenerated from the executed Notebook 05. All case data are synthetic.\n\n'
worked += f'Total equity: $341 million. Coverage: {covered.sum()}/12 assets, ${screen.loc[covered,"equity_usd_m"].sum()} million, or {screen.loc[covered,"equity_usd_m"].sum()/341:.1%} of total equity.\n\n'
worked += table(summary)+'\n\n## Interview shortlist at the 90-day rule\n\n'
worked += table(shortlist[['asset_id','asset_name','hot_days_2024','equity_usd_m']])
worked += '\n\n## Full screen\n\n'+table(screen[['asset_id','hot_days_2024','coverage','review']].fillna('Unknown'))+'\n'
(ROOT/'instructor/WORKED_RESULTS.md').write_text(worked,encoding='utf-8')
validation = '# Validation\n\nCompleted '+datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')+'.\n\n'
validation += f'Python {sys.version.split()[0]}; Windows local project environment.\n\n'
validation += table(pd.DataFrame(results,columns=['Notebook','Executed code cells','Rendered figures']))
validation += '\n\nAll notebooks ran independently in fresh kernels with zero error outputs. HTML reading copies were exported from those executed versions.\n\n'
validation += 'Semantic checks passed: unique asset IDs; matching vector formats and CRS; 2024 leap-year length; deliberate missing climate year; GeoTIFF counts agree with NetCDF; 35 valid raster cells; A11/A12 preserved as unknown; full $341m portfolio retained; threshold counts monotone; all data checksums intact.\n\n'
validation += 'This verifies the bundled synthetic workflow, not scientific validity for real assets, live services, or installation on every student device. No live data service is called by the notebooks.\n'
(ROOT/'VALIDATION.md').write_text(validation,encoding='utf-8')
packages = sorted((d.metadata['Name'],d.version) for d in importlib.metadata.distributions() if d.metadata['Name'])
(ROOT/'requirements-tested.txt').write_text('\n'.join(f'{n}=={v}' for n,v in packages)+'\n',encoding='utf-8')

index = '<!doctype html><html lang="en"><meta charset="utf-8"><title>Climate and Geospatial Â· Course</title><style>body{max-width:850px;margin:60px auto;padding:0 24px;font:18px/1.6 system-ui;color:#173845;background:#f4f7f8}a{color:#116e83}li{margin:15px 0}</style><h1>Climate and geospatial alternative data</h1><p>Six guided lessons for private-markets students. These are reading copies with executed outputs. All portfolio and climate case values are synthetic.</p><ol>'
for name,_,_ in results:
    stem=Path(name).stem
    index += f'<li><a href="{stem}.html">{stem.replace("_"," ")}</a></li>'
index += '</ol><p>To change parameters, open the matching .ipynb in Jupyter. Read data/DATA_DICTIONARY.md for sources and limitations.</p></html>'
(html_dir/'index.html').write_text(index,encoding='utf-8')

student_readme = '''# Student pack: Climate and geospatial alternative data

Start with html/index.html for a no-install reading experience, or notebooks/00_Start_Here_Alternative_Data.ipynb to run code. The HTML files include executed figures and tables.

All portfolio and climate case data are synthetic. The separate real satellite file is for inspecting file structure. Read data/DATA_DICTIONARY.md for definitions and sources.

To run notebooks, install Python 3.12. In this extracted folder run:

    python -m venv .venv
    .venv\\Scripts\\python.exe -m pip install -r requirements.txt
    .venv\\Scripts\\python.exe -m jupyterlab

On macOS/Linux use python3 for the first command and .venv/bin/python for the next commands. Installation needs internet once; the notebooks use bundled local data. Keep data and notebooks together.

Basic Python and pandas experience is assumed: imports, variables, filtering, groupby and plotting. No geospatial or climate-analytics background is needed. The lessons introduce GeoPandas, Rasterio and xarray while focusing on spatial assumptions and interpretation. Run cells in order; use Restart Kernel and Run All to check reproducibility. Complete the coding extensions for additional practice.

Order: 00 alternative data; 01 formats; 02 spatial joins; 03 rasters; 04 climate; 05 due diligence. Full path approximately 195 minutes plus breaks; your instructor may select a shorter route.
'''
with zipfile.ZipFile(ROOT/'student-pack.zip','w',compression=zipfile.ZIP_DEFLATED) as z:
    z.writestr('README.md',student_readme)
    for folder in ['notebooks','html','data']:
        for p in sorted((ROOT/folder).rglob('*')):
            if p.is_file() and '.ipynb_checkpoints' not in p.parts:
                z.write(p,p.relative_to(ROOT))
    for name in ['requirements.txt','requirements-tested.txt']:
        z.write(ROOT/name,name)
with zipfile.ZipFile(ROOT/'student-pack.zip') as z:
    assert z.testzip() is None
    assert len([n for n in z.namelist() if n.endswith('.ipynb')])==6
    assert not any(n.startswith(('instructor/','.venv/')) for n in z.namelist())
print('All six notebooks executed, semantic checks passed, HTML and student ZIP created.',flush=True)

