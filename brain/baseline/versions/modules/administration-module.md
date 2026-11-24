# Administration module (Marketplace component 23513)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/23513)

| version | published | min Mendix |
|---|---|---|
| 4.5.0 | 2026-05-13 | 10.24.0 |
| 4.4.0 | 2025-10-15 | 10.24.0 |
| 4.3.2 | 2025-07-07 | 10.21.0 |
| 4.3.1 | 2025-06-18 | 10.21.0 |
| 4.3.0 | 2025-05-12 | 10.21.0 |
| 4.2.0 | 2025-04-22 | 10.21.0 |
| 4.1.0 | 2024-02-06 | 10.6.0 |
| 4.0.0 | 2024-01-26 | 10.6.0 |
| 3.0.1 | 2025-07-07 | 9.18.0 |
| 3.0.0 | 2023-04-14 | 9.18.0 |
| 2.1.2 | 2022-11-23 | 9.0.5 |
| 2.1.1 | 2022-05-11 | 9.0.5 |
| 2.1.0 | 2022-01-05 | 9.0.5 |
| 2.0.1 | 2021-10-14 | 9.0.5 |
| 2.0.0 | 2021-10-01 | 9.0.5 |
| 1.4.0 | 2023-04-14 | 8.18.11 |
| 1.3.2 | 2022-11-23 | 8.18.11 |
| 1.3.0 | 2022-01-05 | 8.18.11 |
| 1.2.1 | 2020-02-19 | 8.0.0 |
| 1.2.0 | 2020-02-19 | 8.0.0 |
| 1.1.1 | 2019-10-30 | 8.0.0 |
| 1.1.0 | 2019-10-30 | 8.0.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 4.5.0 | requirement | Upgraded Data Widgets compatibility to v3.10.0 | Data Widgets |  |
| 4.4.0 | requirement | Upgraded the module to Mendix 10.24.0 |  |  |
| 4.4.0 | requirement | Upgraded Data Widgets module compatibility to v3.6.0 | Data Widgets |  |
| 4.3.0 | breaking | Moved away from List View for role assignment to using DG2 reference set supported feature. | List View, role assignment, DG2 | DG2 |
| 4.2.0 | requirement | Upgraded the module to Mendix version 10.21.0 for compatibility with Mendix 11 |  |  |
| 4.2.0 | requirement | Updated Data Widgets compatibility to version 2.31.0 | Data Widgets |  |
| 4.2.0 | requirement | Updated Atlas Web Content compatibility to version 3.8.0 | Atlas Web Content |  |
| 4.2.0 | requirement | Updated Combo Box compatibility to version 2.8.0. Ensure Combo Box widget is installed in your project. | Combo Box |  |
| 4.1.0 | breaking | Switched to new Combo Box widget for Language and Time zone fields to add type-ahead filtering. Ensure Combo Box widget is installed. | Language field, Time zone field, Combo Box | Combo Box |
| 4.0.0 | requirement | Upgraded the module to Mendix version 10.6.0 |  |  |
| 4.0.0 | breaking | Replaced Data Grid widget with Data Grid 2 widget for React client compatibility, introduced in Mendix 10.7.0 | Data Grid, Data Grid 2 | Data Grid 2 |
| 4.0.0 | breaking | Replaced Input Reference Set Selector widget with Combo Box widget for React client compatibility, introduced in Mendix 10.7.0. Ensure Combo Box widget is installed. | Input Reference Set Selector, Combo Box | Combo Box |
| 3.0.0 | requirement | Upgraded the module to Mendix version 9.18.0 for compatibility with Mendix 10 |  |  |
| 3.0.0 | removal | Removed supporting microflows for Mendix SSO introduced in version 2.1.0. Move them to customized module before upgrade. | Mendix SSO, supporting microflows |  |
| 3.0.0 | migration-step | If Mendix SSO is currently part of your project but not used, remove Mendix SSO module and delete related dependencies in userlib folder. | Mendix SSO |  |
| 2.1.1 | migration-step | If Mendix SSO v3.0.0 not needed, delete folder Mendix SSO from module or exclude all its microflows. | Mendix SSO |  |
| 2.0.0 | requirement | Updated to Mendix 9. Compatible with Atlas 3.0. |  |  |
| 1.4.0 | removal | Removed supporting microflows for Mendix SSO introduced in version 1.3.0. Move them to customized module before upgrade. | Mendix SSO, supporting microflows |  |
| 1.4.0 | migration-step | If Mendix SSO is currently part of your project but not used, remove Mendix SSO module and delete related dependencies in userlib folder. | Mendix SSO |  |
| 1.1.0 | requirement | Upgraded to Mendix 8.0.0 |  |  |
