# Maps (Marketplace component 108261)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Widget, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/108261)

| version | published | min Mendix |
|---|---|---|
| 5.0.0 | 2026-09-15 | 10.24.0 |
| 4.1.0 | 2025-11-05 | 9.6.0 |
| 4.0.0 | 2024-05-02 | 9.6.0 |
| 3.2.2 | 2023-09-27 | 9.6.0 |
| 3.2.1 | 2023-08-11 | 9.6.0 |
| 3.2.0 | 2023-06-05 | 9.6.0 |
| 3.1.3 | 2023-01-04 | 9.6.0 |
| 3.1.2 | 2022-04-25 | 9.6.0 |
| 3.1.1 | 2022-01-31 | 9.6.0 |
| 3.1.0 | 2021-12-23 | 9.6.0 |
| 3.0.3 | 2021-11-18 | 9.6.0 |
| 3.0.2 | 2021-10-28 | 9.6.0 |
| 3.0.1 | 2021-10-13 | 9.6.0 |
| 3.0.0 | 2021-09-28 | 9.6.0 |
| 2.0.3 | 2021-08-05 | 9.0.5 |
| 2.0.2 | 2021-07-13 | 9.0.5 |
| 2.0.1 | 2021-04-26 | 9.0.5 |
| 2.0.0 | 2021-04-08 | 9.0.5 |
| 1.0.11 | 2022-05-05 | 7.23.0 |
| 1.0.10 | 2021-05-10 | 7.23.0 |
| 1.0.9 | 2020-01-23 | 7.13.1 |
| 1.0.8 | 2019-11-28 | 7.13.1 |
| 1.0.7 | 2019-11-28 | 7.13.1 |
| 1.0.6 | 2019-10-30 | 7.13.1 |
| 1.0.5 | 2019-08-13 | 7.13.1 |
| 1.0.4 | 2019-04-30 | 7.13.1 |
| 1.0.3 | 2019-04-11 | 7.13.1 |
| 1.0.2 | 2019-03-12 | 7.13.1 |
| 1.0.1 | 2019-02-05 | 7.13.1 |
| 1.0.0 | 2018-12-14 | 7.13.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 5.0.0 | breaking | Replaced react-leaflet dependency with direct Leaflet integration due to licensing considerations. | react-leaflet, Leaflet |  |
| 5.0.0 | requirement | Raised minimum Mendix version to 10.24.0 because default markers rely on client resource serving. | Mendix |  |
| 4.0.0 | breaking | Updated Google Maps component, removing deprecated marker and adding advanced marker element. | marker, advanced marker | advanced marker |
| 4.0.0 | removal | Removed mapsStyles property used in Google Maps. | mapsStyles |  |
| 4.0.0 | requirement | Added mapId property that is required with the advanced marker element. | mapId |  |
| 3.1.3 | improvement | Updated the dependencies. | dependencies |  |
| 3.0.1 | breaking | Renamed property Google maps API Key to Geo Location API key. | Google maps API Key | Geo Location API key |
| 3.0.1 | requirement | Made Geo Location API key property required when using location based on Address. | Geo Location API key |  |
| 3.0.0 | breaking | Renamed advanced options property to emphasize it is about advanced properties activation. | advanced options |  |
| 2.0.3 | breaking | Renamed Markers and Marker list properties to Static and Dynamic markers. | Markers, Marker list | Static markers, Dynamic markers |
| 2.0.1 | breaking | Changed anchor of custom marker icons to be center of icon instead of top left corner. | custom marker icons |  |
| 2.0.0 | breaking | Updated widget away from deprecated Mapbox API. | Mapbox API |  |
| 2.0.0 | improvement | Updated widget consistency checks to be compatible with Mendix 9. | consistency checks |  |
| 1.0.10 | breaking | Updated widget away from deprecated Mapbox API. (Fixes Ticket #121474) | Mapbox API |  |
