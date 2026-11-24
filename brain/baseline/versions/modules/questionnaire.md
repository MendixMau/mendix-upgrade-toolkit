# Questionnaire (Marketplace component 234)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/234)

| version | published | min Mendix |
|---|---|---|
| 7.0.0 | 2025-07-30 | 10.24.1 |
| 6.2.4 | 2024-05-02 | 9.24.21 |
| 6.2.3 | 2024-05-01 | 9.24.21 |
| 6.2.2 | 2024-04-28 | 9.24.21 |
| 6.2.1 | 2024-04-27 | 9.24.21 |
| 6.2.0 | 2024-04-26 | 9.24.21 |
| 6.1.3 | 2024-03-19 | 9.24.17 |
| 6.1.2 | 2024-03-18 | 9.24.17 |
| 6.1.1 | 2024-03-17 | 9.24.17 |
| 6.1.0 | 2024-03-11 | 9.24.16 |
| 6.0.1 | 2024-03-05 | 9.24.16 |
| 6.0.0 | 2024-02-27 | 9.24.16 |
| 5.0.4 | 2021-08-11 | 8.12.7 |
| 5.0.3 | 2020-12-31 | 8.6.9 |
| 5.0.2 | 2020-10-26 | 8.6.6 |
| 5.0.1 | 2020-10-19 | 8.6.6 |
| 5.0.0 | 2020-09-16 | 8.6.6 |
| 4.0.4 | 2020-09-09 | 7.23.16 |
| 4.0.3 | 2018-09-17 | 7.16.0 |
| 4.0.2 | 2018-09-07 | 7.16.0 |
| 4.0.1 | 2018-08-27 | 7.16.0 |
| 4.0.0 | 2018-08-24 | 7.16.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 7.0.0 | requirement | Upgraded to Mendix 10.24.1, Java 21 support, React client support. | Mendix, Java, React client |  |
| 7.0.0 | migration-step | Update required widgets and modules before installing this version. |  |  |
| 6.2.4 | fix | Fixed database retrieve that could prevent questionnaire from updating properly. |  |  |
| 6.2.3 | improvement | Updated list input element to use datagrid 2 for grid or field selection configuration. | list input element, datagrid 2 |  |
| 6.2.3 | fix | Updated permissions for Reviewer and User role to ensure proper functioning of questionnaire. | Reviewer role, User role |  |
| 6.2.2 | feature | Added exposed workflow actions for creating and submitting Questionnaires. |  |  |
| 6.2.2 | improvement | Updated Rich Text and HTML Element widgets. | Rich Text widget, HTML Element widget |  |
| 6.2.2 | known-issue | Option popups currently cannot show depending options. |  |  |
| 6.2.1 | fix | Fixed dependencies not updating properly. |  |  |
| 6.2.1 | breaking | Questionnaires no longer committed during conduction, only when submitted. Started but unsubmitted questionnaires may break. |  |  |
| 6.2.0 | breaking | Questionnaires no longer committed during conduction, only when submitted. Started but unsubmitted questionnaires may break. |  |  |
| 6.1.1 | requirement | Upgraded to Mendix 9.24.17. | Mendix |  |
| 6.0.1 | migration-step | Update widgets to modern alternatives (Data Widgets, Combo Box, Rich Text, Accordion) before importing. |  |  |
| 6.0.1 | removal | Removed old/deprecated styling. |  |  |
| 6.0.0 | requirement | Upgraded to Mendix 9.24.16 for compatibility with Studio Pro 10. | Mendix |  |
| 6.0.0 | improvement | Upgraded dependencies and widgets for compatibility with Studio Pro 10. |  |  |
| 5.0.4 | requirement | Upgraded to Mendix 8.12.7 for compatibility with Studio Pro 9.x.x. | Mendix |  |
| 5.0.3 | breaking | Removed default value for attributes of NumberOptionConfig. | NumberOptionConfig |  |
| 5.0.1 | improvement | Updated Checkbox and Radio button widgets to latest versions to solve client errors. | Checkbox widget, Radio button widget |  |
| 5.0.0 | requirement | Upgraded to Mendix 8.6.6. | Mendix |  |
| 5.0.0 | removal | Removed unnecessary pages to use snippets instead. |  |  |
| 5.0.0 | improvement | Upgraded widgets. |  |  |
| 4.0.4 | requirement | Upgraded to Mendix 7.23.16 for compatibility with Studio Pro 8.x.x. | Mendix |  |
| 4.0.4 | breaking | Converted Float attributes to Decimals. | Float attributes |  |
| 4.0.4 | requirement | Added dependency to Community Commons for RefreshClass Java action. | Community Commons |  |
| 4.0.0 | improvement | Updated widgets. |  |  |
