# Audittrail (Marketplace component 138)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/138)

| version | published | min Mendix |
|---|---|---|
| 10.2.2 | 2026-06-19 | 10.21.0 |
| 10.2.1 | 2026-02-18 | 10.21.0 |
| 10.2.0 | 2025-07-04 | 10.21.0 |
| 10.1.1 | 2025-07-04 | 10.21.0 |
| 10.1.0 | 2025-04-08 | 10.21.0 |
| 10.0.1 | 2025-04-04 | 10.18.0 |
| 10.0.0 | 2025-02-07 | 10.18.0 |
| 9.1.6 | 2025-04-04 | 9.18.4 |
| 9.1.5 | 2024-11-12 | 9.18.4 |
| 9.1.4 | 2024-06-17 | 9.18.4 |
| 9.1.3 | 2024-05-10 | 9.18.4 |
| 9.1.0 | 2023-03-24 | 9.18.4 |
| 9.0.3 | 2023-03-03 | 9.0.5 |
| 9.0.2 | 2023-02-21 | 9.0.5 |
| 9.0.1 | 2022-04-08 | 9.0.5 |
| 9.0.0 | 2021-07-22 | 9.0.5 |
| 8.1.3 | 2023-03-03 | 8.18.22 |
| 8.1.2 | 2023-02-16 | 8.18.22 |
| 8.1.1 | 2022-04-08 | 8.12.4 |
| 8.1.0 | 2021-07-22 | 8.12.4 |
| 8.0.0 | 2020-12-21 | 8.12.0 |
| 7.6.0 | 2020-08-04 | 7.23.8 |
| 7.5.0 | 2020-07-15 | 7.23.8 |
| 7.4.0 | 2019-10-03 | 7.23.8 |
| 7.3.0 | 2019-05-27 | 7.23.4 |
| 7.2.0 | 2017-09-20 | 7.2.0 |
| 7.1.0 | 2017-08-28 | 7.2.0 |
| 7.0 | 2017-05-30 | 7.2.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 10.2.2 | improvement | Removed usage of deprecated method to make module compatible with future Studio Pro releases |  |  |
| 10.2.0 | feature | Upgraded all widgets to pluggable widgets using React |  |  |
| 10.2.0 | breaking | Removed CSV export capability in LogOverviewSnippet due to data grid 2 limitations; Excel export still available | LogOverviewSnippet |  |
| 10.1.1 | improvement | Removed usages of deprecated methods in com.mendix.core.Core missed in previous version | com.mendix.core.Core |  |
| 10.1.0 | requirement | Upgraded module to Mendix 10.21.0 for compatibility with future versions | Mendix |  |
| 10.1.0 | improvement | Removed usages of deprecated methods in com.mendix.core.Core implementation | com.mendix.core.Core |  |
| 10.0.1 | improvement | Updated HTML Element widget dependency to version 1.2.2 | HTML Element widget |  |
| 10.0.0 | requirement | Upgraded module to Mendix 10.18.0 for compatibility with future versions | Mendix |  |
| 9.1.6 | improvement | Updated HTML Element widget dependency to version 1.2.2 | HTML Element widget |  |
| 9.1.5 | security | Updated HTML Element widget to version 1.2.1 with DOMPurify 2.5.6 to prevent cross-site scripting vulnerability | HTML Element widget |  |
| 9.1.4 | migration-step | Replaced deprecated Format String widget with HTML Element widget (Ticket 217759) | Format String widget, HTML Element widget | HTML Element widget |
| 9.1.0 | requirement | Upgraded module to Mendix 9.18.4 for compatibility with future versions | Mendix |  |
| 9.0.0 | requirement | Upgraded module to Mendix 9.0.5 compatible with Atlas UI 3; Version 9 for Mendix 9, Version 8 for Mendix 8 and 9 | Mendix, Atlas UI |  |
| 8.1.0 | migration-step | Wrapped all pop-up windows in Layout Grid containers to prepare for Atlas UI 3 support |  |  |
| 8.0.0 | requirement | Updated Mendix framework to 8.12.0, which is Mendix 9 compatible | Mendix |  |
| 8.0.0 | improvement | Removed and rewrote deprecated code |  |  |
| 8.0.0 | improvement | Updated format string widget to be compatible with Mendix 8 and 9 (Ticket 108303) |  |  |
| 8.0.0 | requirement | Using Atlas UI is now mandatory | Atlas UI |  |
| 7.6.0 | migration-step | Module configuration now done through constants replacing Configuration non-persistable entity attributes (Ticket 82048) | Configuration |  |
| 7.4.0 | requirement | Updated module to Mendix 7.23.8 | Mendix |  |
| 7.3.0 | improvement | Removed usages of deprecated APIs |  |  |
