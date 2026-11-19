# Mx Model Reflection (Marketplace component 69)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/69)

| version | published | min Mendix |
|---|---|---|
| 9.1.0 | 2026-01-21 | 10.24.0 |
| 9.0.1 | 2025-04-30 | 10.21.0 |
| 9.0.0 | 2025-04-17 | 10.21.0 |
| 8.0.4 | 2025-04-03 | 9.24.24 |
| 8.0.3 | 2024-12-03 | 9.24.24 |
| 8.0.2 | 2024-07-18 | 9.24.11 |
| 7.1.1 | 2024-03-14 | 9.18.0 |
| 7.1.0 | 2024-03-08 | 9.18.0 |
| 7.0.0 | 2023-04-19 | 9.18.0 |
| 6.2.0 | 2020-12-17 | 8.12.0 |
| 6.1.2 | 2020-03-03 | 7.23.0 |
| 6.1.1 | 2019-11-25 | 7.23.0 |
| 6.1.0 | 2019-10-29 | 7.23.0 |
| 6.0.0 | 2019-06-12 | 7.23.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 9.1.0 | requirement | Minimum Mendix version upgraded to 10.24.0 |  |  |
| 9.1.0 | removal | Removed deprecated pages |  |  |
| 9.0.0 | requirement | Upgraded to Mendix version 10.21.0 |  |  |
| 9.0.0 | removal | Removed deprecated pages |  |  |
| 8.0.3 | requirement | Upgraded Mendix version to 9.24.24 |  |  |
| 8.0.3 | improvement | Replaced old UI components with new ones supporting React Client |  |  |
| 8.0.3 | breaking | Layouts from Atlas used instead of custom ones; popup windows now modal |  |  |
| 8.0.3 | migration-step | Select pages not React compatible; manually remove if React Client enabled |  |  |
| 8.0.3 | breaking | Configured cascade delete; MxObjectEnumValue deleted when MxObjectEnum deleted | MxObjectEnumValue, MxObjectEnum |  |
| 8.0.3 | removal | Removed support for deprecated Float and Currency types | Float, Currency |  |
| 8.0.2 | requirement | Upgraded Mendix version to 9.24.11 |  |  |
| 8.0.2 | improvement | Replaced old UI components with new ones supporting React Client |  |  |
| 7.1.1 | fix | TokenReplacer now supports System.owner and System.changedBy associations correctly. (Ticket 202682) | TokenReplacer, System.owner, System.changedBy |  |
| 7.1.1 | fix | TokenReplacer handles many-to-many associations by taking the first object | TokenReplacer |  |
| 7.1.1 | fix | Fixed issue where IVK_RecalculateSize caused issues building native app. (Ticket 204735, 207239) | IVK_RecalculateSize |  |
| 7.1.0 | fix | Handle non-localized datetimes correctly |  |  |
| 7.0.0 | requirement | Updated to Studio Pro 9.18; usable in Studio Pro 10 |  |  |
| 6.2.0 | requirement | Upgraded to Studio Pro version 8.12.0 |  |  |
| 6.1.2 | fix | Fixed IVK_RecalculateSize to correctly set CalculatedSizeInKiloBytes field. (Ticket 95995) | IVK_RecalculateSize, CalculatedSizeInKiloBytes |  |
| 6.1.1 | fix | Syncing correctly cleans up enum values and captions. Unused values/captions not auto-deleted; manually delete via microflow. (Ticket #63310) | MxObjectEnumValue, MxObjectEnumCaption |  |
| 6.1.0 | improvement | FindMember, FindMicroflow, FindObjectType, FindReference return exact matches first. (Ticket #90020) | FindMember, FindMicroflow, FindObjectType, FindReference |  |
| 6.0.0 | requirement | Updated to Mendix 7.23; also usable in Mendix 8 |  |  |
| 6.0.0 | removal | Support for deprecated Float and Currency types dropped | Float, Currency |  |
