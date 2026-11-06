# OData Connector for SAP solutions (Marketplace component 74525)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/74525)

| version | published | min Mendix |
|---|---|---|
| 7.1.6 | 2026-06-25 | 10.21.0 |
| 7.1.5 | 2026-02-10 | 10.21.0 |
| 7.1.4 | 2025-12-03 | 10.21.0 |
| 7.1.3 | 2025-10-23 | 10.21.0 |
| 7.1.2 | 2025-09-09 | 10.21.0 |
| 7.1.1 | 2025-07-30 | 10.21.0 |
| 7.1.0 | 2025-07-30 | 10.21.0 |
| 7.0.0 | 2025-07-08 | 10.21.0 |
| 6.1.3 | 2026-06-18 | 9.24.33 |
| 6.1.2 | 2025-12-03 | 9.24.33 |
| 6.1.1 | 2025-10-14 | 9.24.33 |
| 6.1.0 | 2025-07-17 | 9.24.33 |
| 6.0.6 | 2025-05-06 | 9.24.33 |
| 6.0.5 | 2025-03-27 | 9.24.4 |
| 6.0.4 | 2024-11-08 | 9.24.4 |
| 6.0.3 | 2024-05-02 | 9.24.4 |
| 6.0.2 | 2023-10-31 | 9.24.4 |
| 6.0.1 | 2023-05-30 | 9.24.0 |
| 6.0.0 | 2023-04-03 | 9.24.0 |
| 5.6.2 | 2023-10-06 | 8.18.25 |
| 5.6.1 | 2023-05-18 | 8.18.10 |
| 5.6.0 | 2023-02-01 | 8.18.10 |
| 5.5.5 | 2022-09-07 | 8.18.10 |
| 5.5.4 | 2022-07-29 | 8.18.10 |
| 5.5.3 | 2022-07-05 | 8.18.10 |
| 5.5.2 | 2022-03-22 | 8.18.10 |
| 5.5.1 | 2022-03-14 | 8.18.10 |
| 5.5.0 | 2021-09-29 | 8.18.10 |
| 5.4.0 | 2021-08-19 | 8.15.1 |
| 5.3.0 | 2021-06-16 | 8.15.1 |
| 5.2.4 | 2021-02-26 | 8.15.1 |
| 5.2.3 | 2021-02-04 | 8.15.1 |
| 5.2.2 | 2021-01-12 | 8.15.1 |
| 5.2.1 | 2020-12-04 | 8.15.1 |
| 5.2.0 | 2020-10-13 | 7.23.3 |
| 5.1.3 | 2020-10-07 | 7.23.3 |
| 5.1.2 | 2020-06-29 | 7.23.3 |
| 5.1.1 | 2020-05-29 | 7.23.3 |
| 5.1.0 | 2020-05-06 | 7.23.3 |
| 5.0.6 | 2020-04-01 | 7.23.3 |
| … 18 older versions | | |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 7.1.5 | removal | Removed deprecated dependencies to ensure compatibility with Mendix 11. |  |  |
| 7.1.4 | security | Security vulnerabilities were identified and fixed. |  |  |
| 7.1.2 | fix | Harmonized internal module dependencies to prevent compilation issues. |  |  |
| 7.1.1 | fix | Harmonized internal module dependencies to prevent compilation issues. |  |  |
| 7.0.0 | requirement | Upgrade to Mx 10.21. |  |  |
| 6.1.2 | security | Security vulnerabilities were identified and fixed. |  |  |
| 6.0.6 | requirement | Released on Mx v9.24.33. |  |  |
| 6.0.5 | fix | Updated serializer for OData action calls. |  |  |
| 6.0.3 | fix | Updated length for meta_objectURL attribute. | meta_objectURL |  |
| 6.0.2 | security | Security Fixes. Please remove duplicate jars from your project after taking latest release. |  |  |
| 6.0.1 | fix | Modified Java Action for Mx10 readiness. |  |  |
| 6.0.1 | fix | Updated logic for OData URL creation for delete action. |  |  |
| 6.0.0 | requirement | Upgraded to Mendix v9.24.0. |  |  |
| 5.6.2 | security | Security Fixes. Please remove duplicate jars from your project after taking latest release. |  |  |
| 5.6.1 | fix | Updated OData URL creation logic. |  |  |
| 5.5.4 | security | Upgrade OkHTTP jar to fix security vulnerability. | OkHTTP |  |
| 5.5.3 | security | Updated vulnerable okhttp jar. | okhttp |  |
| 5.5.0 | requirement | Upgraded to Mendix Studio Pro v8.18.10. |  |  |
| 5.3.0 | fix | Updated OData request creation. |  |  |
| 5.2.3 | fix | Update in request creation. |  |  |
| 5.2.3 | fix | Update in response parsing. |  |  |
| 5.2.2 | fix | Updated deprecated function Core.execute() to Core.microflowcall() for Mendix 9 compatibility. |  |  |
| 5.2.1 | requirement | Upgraded to Mendix 8. |  |  |
| 5.1.3 | fix | Remove unused libraries. |  |  |
| 5.0.0 | requirement | Migrated SAP OData Connector to Mendix 7.23.3 to support Mendix Studio Pro 8. |  |  |
| 4.0.4 | fix | Added missing javax.json jar. | javax.json |  |
| 3.6.0 | breaking | Change the life cycle of cookies and CSRF tokens to be dependent on the Mendix sessions. |  |  |
