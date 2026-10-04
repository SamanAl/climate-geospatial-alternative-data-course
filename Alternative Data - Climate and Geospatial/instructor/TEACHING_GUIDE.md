# Teaching guide

## Intended group

Mixed disciplines in a private-market analysis class. Assume basic Python and pandas: imports, variables, filtering, groupby and plotting. Students are new to GIS, remote sensing and climate analytics. Check Python comfort briefly rather than teaching it from scratch. Have students work in pairs: one implements, the other checks spatial assumptions and interpretation. Swap roles halfway through.

The objective is to extend familiar analysis skills to spatial and climate data. Each notebook includes a business question, definitions, visible short code, a figure/table, a parameter experiment, and an interpretation task. Spend explanation time on geometry, CRS, spatial matching, raster support, units and time aggregation. Use the coding extensions for students who finish guided cells quickly.

## Outcomes

Students should be able to:

1. Identify a proxy and propose a competing explanation.
2. Recognize vector, raster and time-dimensional data and choose a suitable format.
3. Explain why coordinate systems and missing spatial matches matter.
4. Read climate units and periods and distinguish history from a projection.
5. Present a reproducible screen with explicit coverage and limitations.

## A 3-hour workshop

| Time | Activity |
|---|---|
| 0–15 | Notebook 00: question, proxy, and portfolio coverage; quick Python readiness check |
| 15–45 | Notebook 01: geometry and format museum; one exercise |
| 45–65 | Notebook 02: spatial join and boundary demonstration; distance as instructor demo |
| 65–75 | Break |
| 75–100 | Notebook 03: grid, nodata, sampling; real image as quick demonstration |
| 100–130 | Notebook 04: cube, units and monthly comparison; missing-year example |
| 130–165 | Notebook 05: screen, sensitivity and paired memo |
| 165–180 | Compare memos and complete exit tickets |

For two 90-minute classes, pause after the raster metadata demonstration and begin the second class by recapping cells and missingness. Assign any omitted exercises for independent work.

## A full week

- **Before class (20 min):** Notebook 00; read the glossary below; one paragraph on a possible proxy.
- **Session 1 (90 min):** Notebooks 01 and 02, plus map critique.
- **Independent lab (45–60 min):** Notebook 03 and stretch activity.
- **Session 2 (90 min):** Notebooks 04 and 05, plus memo discussion.
- **After class (30 min):** revise the memo and propose one real-data replacement, naming its metadata requirements.

## Five-minute preflight

Open Notebook 00 in the project environment. Run a cell. Open Notebook 03 and confirm its raster map renders. Keep HTML copies available for participants who cannot install packages. Do not spend the lesson repairing student environments; pair them or use reading copies.

All core data are bundled. The lessons do not call APIs or download basemaps. Precomputed notebook outputs are visible. Have students rerun from a clean kernel when they finish changing parameters.

## Facilitation prompts

### Use existing Python skills

Ask students to explain how an ordinary `merge` differs from a spatial join, how raster sampling becomes a new table column, and why an xarray time dimension requires a different aggregation from a pandas groupby. Keep the geospatial concepts explicit even for strong coders. If pandas needs a refresher, pair students or recap only the operation needed for the current question.

The optional coding extensions ask students to check coordinate quality, implement a distance sensitivity table, retain raster coverage flags, compare climate-period assumptions, and test a portfolio rule. They are suitable for independent work during the week.

- **00:** “If parking-lot activity rises, what else could explain it besides revenue?”
- **01:** “Is a point the building itself, its entrance or an approximate address?”
- **02:** “Which portfolio money disappears if unmatched locations are dropped?”
- **03:** “Can two buildings in one coarse grid cell have different indoor temperatures?”
- **04:** “Would one unusually hot year tell us what 2040 will look like?”
- **05:** “What would you ask the property manager before assigning a dollar impact?”

## Instructor cautions tied to the case

- Repeatedly name the data **synthetic**. The plot location is near Houston; the temperature values are not Houston estimates.
- An unverified cooling backup is a documentation gap. Do not let students convert it to a proven absence of protection.
- The classes of the portfolio screen are action categories, not hazard probabilities or ratings.
- The shortlist changes with a rule. That is a sensitivity exercise, not proof that one threshold is correct.
- The real image is for file inspection. No supported climate variable or band calibration is asserted.
- A distance in degrees is not kilometres. Avoid a universal “best CRS”; explain the local UTM choice.

## Memo assessment (10 points)

| Criterion | Points |
|---|---:|
| Specific question and reproducible selection rule | 2 |
| Correct findings, units and denominator | 2 |
| Unknown assets retained and coverage reported | 2 |
| Synthetic nature, resolution, time and threshold limitations | 2 |
| Two targeted operational evidence requests | 2 |

Accept different shortlists when assumptions and calculations support them. Deduct for converting capital into “expected loss” without an impact model or declaring unknown assets safe.

## Plain-language glossary

- **Alternative data:** information beyond the conventional financial sources used in a particular analysis.
- **Proxy:** an indirect indicator for something else we want to know.
- **Geometry:** a point, line or shape represented by coordinates.
- **CRS:** the rules connecting coordinates to locations on Earth.
- **Spatial join:** a match based on a geographic relationship.
- **Raster:** a regular grid of values.
- **Resolution:** the spatial or temporal detail represented by the data.
- **Nodata:** no valid value, not a measured zero.
- **Band:** one layer of raster values.
- **Reanalysis:** a reconstruction of past conditions using observations and a model.
- **Baseline:** a stated reference period used for comparison.
- **Anomaly:** a difference from that reference, with a stated aggregation and unit.
- **Hazard / exposure / vulnerability:** threatening conditions / what is in their way / susceptibility to their effects.

See `ANSWER_GUIDE.md` for suggested responses and `WORKED_RESULTS.md` for results from the executed default case.
