# Deep link module (Marketplace component 43)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Module, Mendix, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/43)

| version | published | min Mendix |
|---|---|---|
| 10.0.10 | 2025-03-03 | 10.0.0 |
| 10.0.9 | 2024-10-15 | 10.0.0 |
| 10.0.8 | 2024-02-09 | 10.0.0 |
| 10.0.6 | 2023-11-27 | 10.0.0 |
| 10.0.5 | 2023-10-13 | 10.0.0 |
| 10.0.4 | 2023-09-08 | 10.0.0 |
| 9.0.17 | 2025-03-03 | 9.6.10 |
| 9.0.16 | 2024-11-07 | 9.6.10 |
| 9.0.15 | 2024-02-09 | 9.6.10 |
| 9.0.14 | 2023-12-19 | 9.6.10 |
| 9.0.12 | 2023-10-13 | 9.6.10 |
| 9.0.11 | 2023-07-06 | 9.6.10 |
| 9.0.10 | 2023-06-20 | 9.6.10 |
| 9.0.9 | 2023-02-20 | 9.6.10 |
| 9.0.8 | 2023-01-06 | 9.6.10 |
| 9.0.7 | 2023-01-04 | 9.6.10 |
| 9.0.6 | 2022-11-18 | 9.6.10 |
| 9.0.5 | 2022-09-16 | 9.6.10 |
| 9.0.4 | 2022-08-17 | 9.6.10 |
| 9.0.3 | 2022-07-11 | 9.6.10 |
| 9.0.2 | 2022-04-12 | 9.6.10 |
| 9.0.1 | 2022-03-25 | 9.6.10 |
| 8.0.9 | 2024-02-09 | 8.12.5 |
| 8.0.8 | 2023-11-30 | 8.12.5 |
| 8.0.7 | 2023-10-13 | 8.12.5 |
| 8.0.6 | 2022-11-18 | 8.12.5 |
| 8.0.5 | 2022-09-16 | 8.12.5 |
| 8.0.4 | 2022-08-17 | 8.12.5 |
| 8.0.3 | 2022-07-11 | 8.12.5 |
| 8.0.2 | 2022-04-12 | 8.12.5 |
| 8.0.1 | 2022-03-25 | 8.12.5 |
| 7.0.1 | 2022-05-05 | 7.23.0 |
| 7.0.0 | 2022-03-18 | 7.23.0 |
| 6.1.3 | 2022-01-28 | 8.12.0 |
| 6.1.2 | 2022-01-27 | 8.12.0 |
| 6.1.1 | 2021-12-21 | 8.12.0 |
| 6.1.0 | 2021-11-16 | 8.12.0 |
| 6.0.5 | 2021-01-20 | 8.12.0 |
| 6.0.4 | 2021-01-05 | 8.12.0 |
| 6.0.3 | 2019-10-16 | 7.23.0 |
| … 3 older versions | | |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 10.0.9 | breaking | Make DeepLink React Client compatible by using Combo Box widget instead of Reference Selector | Reference Selector, Combo Box widget | Combo Box widget |
| 10.0.6 | breaking | Switched to using DataGrid2 | DataGrid2 | DataGrid2 |
| 9.0.9 | requirement | Reverts the module Studio Pro requirements back to version 9.6.10 |  |  |
| 9.0.7 | fix | Use the new addCookie API with 'isHostOnly=true' when available. This fixes an issue with faulty redirects to the login page in Mendix >9.20 |  |  |
| 9.0.6 | removal | Removed user setting for the DeepLink argument type, as this is handled internally |  |  |
| 9.0.5 | fix | Fix for continuation after login. Requires 9.6.13+, 9.12.6+, or 9.18 and up |  |  |
| 9.0.5 | removal | Remove unused microflows |  |  |
| 8.0.6 | removal | Removed user setting for the DeepLink argument type, as this is handled internally |  |  |
| 8.0.5 | fix | Fix for continuation after login. Requires 8.18.20 and up |  |  |
| 8.0.5 | removal | Remove unused microflows |  |  |
| 7.0.0 | improvement | Updated libraries to the latest versions |  |  |
| 6.1.2 | requirement | Added RequiredLib file to clarify dependency on commons-lang library | commons-lang |  |
| 6.0.5 | improvement | Update Apache Commons libraries | Apache Commons |  |
| 6.0.4 | requirement | Upgrade to Mendix Studio Pro 8.12 |  |  |
| 6.0.3 | removal | Remove superfluous .RequiredLib file |  |  |
| 6.0.0 | requirement | Update to Mendix 7.23.0 to make it compatible with Mendix 8 |  |  |
| 6.0.0 | removal | Remove usage of deprecated APIs |  |  |
