# Charts (Marketplace component 105695)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Widget, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/105695)

| version | published | min Mendix |
|---|---|---|
| 6.3.2 | 2026-08-03 | 10.6.0 |
| 6.3.1 | 2026-05-12 | 10.6.0 |
| 6.3.0 | 2026-02-20 | 10.6.0 |
| 6.2.3 | 2025-10-15 | 10.6.0 |
| 6.2.2 | 2025-09-23 | 10.6.0 |
| 6.2.1 | 2025-07-15 | 10.6.0 |
| 6.2.0 | 2025-06-03 | 10.6.0 |
| 6.1.3 | 2026-01-05 | 9.24.0 |
| 6.1.2 | 2025-09-23 | 9.24.0 |
| 6.1.1 | 2025-07-15 | 9.24.0 |
| 6.1.0 | 2025-06-04 | 9.24.0 |
| 6.0.1 | 2025-05-14 | 10.6.0 |
| 6.0.0 | 2025-02-28 | 10.6.0 |
| 5.1.2 | 2025-01-21 | 10.6.0 |
| 5.1.1 | 2024-12-12 | 9.6.0 |
| 5.1.0 | 2024-10-28 | 9.6.0 |
| 5.0.3 | 2024-10-15 | 9.6.0 |
| 5.0.2 | 2024-09-20 | 9.6.0 |
| 5.0.1 | 2024-07-02 | 9.6.0 |
| 5.0.0 | 2024-06-14 | 9.6.0 |
| 4.2.4 | 2023-11-30 | 9.6.0 |
| 4.2.3 | 2023-11-21 | 9.6.0 |
| 4.2.2 | 2023-10-27 | 9.6.0 |
| 4.2.1 | 2023-09-27 | 9.6.0 |
| 4.2.0 | 2023-08-16 | 9.6.0 |
| 4.1.0 | 2023-06-06 | 9.6.0 |
| 4.0.4 | 2023-04-13 | 9.6.0 |
| 4.0.3 | 2023-01-09 | 9.6.0 |
| 4.0.2 | 2022-11-22 | 9.6.0 |
| 4.0.1 | 2022-11-10 | 9.6.0 |
| 4.0.0 | 2022-10-27 | 9.6.0 |
| 3.0.1 | 2022-08-30 | 9.6.0 |
| 3.0.0 | 2022-07-29 | 9.6.0 |
| 2.0.1 | 2022-05-10 | 9.6.0 |
| 2.0.0 | 2021-09-28 | 9.6.0 |
| 1.4.13 | 2022-05-10 | 7.23.0 |
| 1.4.12 | 2021-08-05 | 7.23.0 |
| 1.4.11 | 2021-04-28 | 7.13.1 |
| 1.4.10 | 2020-04-20 | 7.13.1 |
| 1.4.9 | 2020-03-09 | 7.13.1 |
| … 9 older versions | | |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 6.3.1 | breaking | Disabled code-mirror from playground widget for compatibility. Only basic editor available now. | ChartPlayground |  |
| 6.3.0 | breaking | Changed how Static data and Source attribute data are merged. Traces now merged by index with source attribute values overriding static values. | CustomChart |  |
| 6.2.3 | breaking | Changed event data to return more properties instead of only bbox coordinates. | CustomChart |  |
| 6.2.1 | improvement | Updated shared charts dependency. | AreaChart |  |
| 6.2.0 | improvement | Increased version to update shared code. | CustomChart |  |
| 6.1.3 | breaking | Changed event data to return more properties instead of only bbox coordinates. | CustomChart |  |
| 6.1.1 | improvement | Updated shared charts dependency. | AreaChart |  |
| 6.1.0 | improvement | Increased version to update shared code. | CustomChart |  |
| 6.0.0 | requirement | Updated plotly.js library to version 3.0. | plotly.js |  |
| 6.0.0 | feature | Added new widget called custom charts. | CustomChart |  |
| 6.0.0 | feature | Introduced custom chart widget. | CustomChart |  |
| 5.0.0 | removal | Removed the Enable developer mode property. Drag Chart playground widget to chart to edit instead. | Enable developer mode property | ChartPlayground widget |
| 5.0.0 | breaking | Migrated from Ace code editor to CodeMirror editor. New editor compatible with legacy and new widget runtime. | code editor | CodeMirror |
| 4.2.0 | breaking | Line color (LineChart), Marker color (LineChart), On click action (all except PieChart/HeatMap) properties lose configured values. Must reconfigure manually. | Line color, Marker color, On click action, LineChart |  |
| 4.2.0 | migration-step | Reconfigure Line color, Marker color (LineChart), and On click action properties after update. | Line color, Marker color, On click action |  |
| 4.0.3 | improvement | Updated fast-json-patch dependency. | fast-json-patch |  |
| 4.0.2 | security | Updated d3-color library to 3.1.0 to prevent ReDoS. | d3-color |  |
| 4.0.0 | removal | Removed all deprecated chart widgets. Apps must manually replace deprecated widgets with new ones. |  |  |
| 4.0.0 | migration-step | Replace deprecated chart widgets (v2) with new reworked widgets with improved simplified configuration. |  |  |
| 3.0.0 | deprecation | Release Charts v3.0 deprecates old widgets (v2) and brings reworked widgets with improved simplified configuration. |  |  |
| 1.4.12 | removal | Removed deprecated APIs warnings. |  |  |
| 1.4.11 | improvement | Updated plotly.js dependency. | plotly.js |  |
| 1.4.11 | improvement | Updated react-ace dependency and switched brace for ace-builds. | react-ace, ace-builds, brace |  |
| 1.4.11 | security | Patched lodash vulnerability. | lodash |  |
| 1.4.11 | security | Updated fast-json-patch dependency. | fast-json-patch |  |
