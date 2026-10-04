# Suggested answers

These are discussion anchors, not a script. `WORKED_RESULTS.md` contains numeric results from the executed notebooks using default parameters.

## 00 — Alternative data

- Night-time brightness may reflect lighting upgrades, a temporary event, a different sensor, seasonality, or industrial activity. It does not directly measure profit.
- Housing and logistics filters change rows, not the underlying assets. Asset equity is capital invested, not asset value or loss.
- A good exit ticket links an operational question to a measurable feature and names a plausible coverage, measurement or interpretation limitation.

## 01 — Formats

- CSV has rows but needs coordinate interpretation. GeoJSON stores geometry plus properties. GeoPackage holds layers in a database. The example shapefile contains a subset of attributes, intentionally.
- Small location exchange: GeoJSON is reasonable. Multiple layers: GeoPackage. Daily gridded climate: NetCDF. Other answers can work if limitations are explained.
- Request all shapefile companions and CRS documentation. A `.shp` alone is insufficient for the intended workflow.
- Reversing x/y misplaces the data. These Houston-like values make reversed latitude invalid, but a swap can pass bounds checks elsewhere.
- Filtering housing changes which assets are shown, not their coordinates.

## 02 — Spatial joins

- A11 is outside both areas and must remain in a left join. An inner join would omit its $30 million of fictional equity.
- A boundary point at −95.35, 29.75 is within neither rectangle and intersects both. A naïve intersecting join can duplicate capital.
- Reducing the buffer radius cannot increase the count of points selected under the same rule.
- Euclidean distance ignores network access, junctions, barriers, congestion and legal entry points. Proximity is not evidence of causation.
- `to_crs` transforms coordinates; `set_crs` declares their existing meaning.

## 03 — Raster

- A11 is outside the heat grid; A12 falls in nodata. Both are unknown. Zero would assert an observed absence of threshold days.
- Buildings in one cell can differ in insulation, ventilation, occupants, heat sensitivity, cooling and backup power.
- The heat grid has 36 cells and one masked cell. More pixels do not guarantee the right measurement or time period for a question.
- Changing the palette changes perception, not the stored values. Always retain a labeled color scale and distinguish missing values.
- The real image's first-band preview is not an air-temperature map. Without calibration and band metadata, do not infer physical units from the appearance.

## 04 — Climate

- Kelvin to Celsius: subtract 273.15. Differences in kelvin and Celsius have the same magnitude, but absolute values do not.
- Raising the threshold cannot increase hot-day counts for the same valid observations.
- A single hot year is weather variability within a longer record. Our imposed trend is known by construction; this synthetic series cannot support empirical climate attribution.
- Future projections: request scenario, horizon, model/ensemble, variable, units, calendar, spatial resolution, baseline, downscaling method and uncertainty.
- A missing year must be unknown, not zero hot days. The 90% completeness rule is illustrative, and accepted incomplete years can still undercount hot days.
- Removing 2020 from the recent period removes overlap but shortens the recent sample. It does not magically make the result a climate normal.

## 05 — Application

- Report count coverage and capital coverage; they need not match. Preserve A11 and A12 in the denominator and put them in data follow-up.
- A threshold of 90 hot days with no verified backup is transparent, but unvalidated. Different thresholds should change the operations shortlist while unknown assets remain unknown.
- Ask about cooling design and maintenance, outage logs, worker exposure, occupancy schedules, backup verification, site-specific measurements and business interruption dependencies.
- A higher equity amount can affect which interview gets scheduled, but does not establish higher expected climate loss. Criticality, vulnerability and operations matter too.

### Memo scaffold

“Using the stated [cutoff]-day rule, we suggest interviewing [assets] first. The climate indicator is available for [count]/12 assets and [percentage] of total fictional equity. [Unknown assets] require a separate data check. This is a synthetic, single-year, coarse-grid screen; the cutoff and backup attribute are not a calibrated risk model. Before estimating operational or financial effects, request [specific evidence] and [specific evidence].”

## Useful next assignment

### Guidance for the Python coding extensions

- **00:** group equity by sector and divide by total equity. Count shares and capital shares have different denominators and can differ substantially.
- **01:** compare asset-ID sets and CRS after export/reload; flag missing coordinates before testing the study extent. A location outside that extent is a review flag, not automatically an error.
- **02:** evaluate each distance cutoff using the same projected coordinates. Counts must be nondecreasing with radius. The same is true of summed nonnegative equity.
- **03:** retain one row per asset after the merge. Report both counts and available counts by sector; do not fill unknown heat values with zero.
- **04:** use a common cell and validity rule when comparing thresholds. Hot-day counts must be nonincreasing as the temperature threshold rises. Removing a year changes both the period and the sample size.
- **05:** compare ID sets as well as totals. Unknowns must retain their data-follow-up status regardless of the proposed operations rule; the full-portfolio equity total remains $341 million.

Ask students to propose replacing **one** synthetic layer with real data. Require a one-page data specification: question, provider, date range, geography, units, CRS, missingness, usage terms, validation plan and the claim they will avoid making. Downloading large datasets is not necessary to evaluate their reasoning.
