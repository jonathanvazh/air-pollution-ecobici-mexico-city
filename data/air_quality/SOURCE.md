# Data source — air quality (RAMA daily averages)

- **Dataset:** Red Automática de Monitoreo Atmosférico (RAMA), SIMAT / SEDEMA
- **Content:** City-wide daily averages per pollutant (CO, NO, NO2, NOX, O3, PM10, PM25, SO2)
- **Source URL:** [https://datos.cdmx.gob.mx/dataset/72f6b09e-30c5-4b1e-9090-80717e6aedef/resource/ebc079e5-bd11-4830-b595-14292f753575/download/rama_2023_05.csv]
- **Downloaded on:** [2026-06-27]
- **Downloaded by:** manual download (to be replaced by a scripted fetch — see decisions.md)
- **File name caveat:** the file is named `rama_2023_05.csv`, but its contents are the FULL daily series from 2015-01-01 to 2023 (3073 rows), NOT May 2023.
  The portal's own file name is misleading — verify content, not the name.
- **Scale note:** PM25 in correct range (~12–78 µg/m³), confirmed against forensic review.
- **Granularity note:** city-wide only, NO per-station breakdown. Spatial analysis
  (station mapping) will require hourly/by-zone or per-station data later.