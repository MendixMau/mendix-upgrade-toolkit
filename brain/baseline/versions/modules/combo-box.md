# Combo box (Marketplace component 219304)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Widget, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/219304)

| version | published | min Mendix |
|---|---|---|
| 2.10.0 | 2026-09-21 | 10.22.0 |
| 2.9.0 | 2026-07-28 | 10.22.0 |
| 2.8.2 | 2026-07-22 | 10.22.0 |
| 2.8.1 | 2026-05-08 | 10.22.0 |
| 2.8.0 | 2026-03-12 | 10.22.0 |
| 2.7.2 | 2026-01-30 | 10.22.0 |
| 2.7.1 | 2026-01-27 | 10.22.0 |
| 2.7.0 | 2026-01-15 | 10.22.0 |
| 2.6.2 | 2025-11-03 | 10.22.0 |
| 2.6.1 | 2025-10-09 | 10.22.0 |
| 2.6.0 | 2025-09-26 | 10.22.0 |
| 2.5.1 | 2025-09-19 | 10.22.0 |
| 2.5.0 | 2025-08-12 | 10.22.0 |
| 2.4.3 | 2025-07-22 | 10.7.0 |
| 2.4.2 | 2025-06-10 | 10.7.0 |
| 2.4.1 | 2025-06-06 | 10.7.0 |
| 2.4.0 | 2025-05-19 | 10.7.0 |
| 2.3.1 | 2025-05-08 | 10.7.0 |
| 2.3.0 | 2025-03-19 | 10.7.0 |
| 2.2.0 | 2025-02-04 | 10.7.0 |
| 2.1.4 | 2025-01-29 | 10.7.0 |
| 2.1.3 | 2024-12-12 | 10.7.0 |
| 2.1.2 | 2024-12-09 | 10.7.0 |
| 2.1.1 | 2024-11-15 | 10.7.0 |
| 2.1.0 | 2024-10-29 | 10.7.0 |
| 2.0.2 | 2024-10-03 | 10.7.0 |
| 2.0.1 | 2024-08-16 | 10.7.0 |
| 2.0.0 | 2024-08-09 | 10.7.0 |
| 1.7.4 | 2026-01-27 | 9.24.0 |
| 1.7.3 | 2025-10-09 | 9.24.0 |
| 1.7.2 | 2025-07-31 | 9.24.0 |
| 1.7.1 | 2025-01-28 | 9.24.0 |
| 1.7.0 | 2024-12-17 | 9.24.0 |
| 1.6.3 | 2024-08-08 | 9.24.0 |
| 1.6.2 | 2024-07-16 | 9.24.0 |
| 1.6.1 | 2024-06-28 | 9.24.0 |
| 1.6.0 | 2024-06-19 | 9.24.0 |
| 1.5.0 | 2024-05-06 | 9.24.0 |
| 1.4.0 | 2024-04-19 | 9.24.0 |
| 1.3.1 | 2024-04-08 | 9.24.0 |
| … 7 older versions | | |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.10.0 | improvement | Improved reliability of the On change action. | On change |  |
| 2.9.0 | breaking | Fixed inverted editability setting: false now means read-only, true means editable. Workarounds must be removed. | editability |  |
| 2.8.0 | feature | Introduced new On change action in Database mode firing only when selection changes, not on initialization. | On change |  |
| 2.8.0 | breaking | Renamed On change action in Database mode to On selection to reflect actual behavior. | On selection | On selection |
| 2.7.1 | improvement | Made it possible to clear selection in single selection mode with Backspace key. |  |  |
| 2.7.1 | improvement | Improved keyboard navigation for multi selection. |  |  |
| 2.6.0 | migration-step | Moved debounce interval for filtering operations from Events tab to Advanced tab. | debounce interval |  |
| 2.5.0 | feature | Added On change filter input event triggering when users type in filter field, passing filter text to actions. | On change filter input |  |
| 2.4.0 | breaking | Implemented custom editability configuration for readOnly mode when no target attribute for database source. | editability |  |
| 2.3.0 | breaking | Changed Aria required setting from boolean to expression; previously set values reset to false on update. | Aria required |  |
| 2.2.0 | feature | Added Selected items sorting property to set display order of selected items in multi-selection. | Selected items sorting |  |
| 2.2.0 | breaking | Database multi selection no longer displays selected values sorted by caption; now displays by selection order unless configured otherwise. |  |  |
| 2.1.4 | breaking | Removed default value from database source configuration. |  |  |
| 2.1.0 | feature | Added support for attribute with Long type. |  |  |
| 2.1.0 | breaking | Made Value no longer required if Target attribute is not set for database datasource. | Value, Target attribute |  |
| 2.1.0 | migration-step | Restructured Attribute group configuration and renamed it as Store value. | Attribute, Store value | Store value |
| 2.0.0 | feature | Implemented selection API for combobox using database datasource, allowing widget selection to be listened into. |  |  |
| 1.7.4 | improvement | Updated internal dependencies. |  |  |
| 1.7.1 | fix | Fixed database onChange failing to trigger; onChange event using database source will clear on upgrade. |  |  |
| 1.7.0 | feature | Added support for attribute with Long type. |  |  |
| 1.7.0 | migration-step | Restructured Attribute group configuration and renamed it as Store value. | Attribute, Store value | Store value |
| 1.6.2 | breaking | Removed lazy loading for caption type = expression due to technical limitation. |  |  |
| 1.6.1 | breaking | Changed default value for lazy loading from false to true by default. |  |  |
| 1.6.0 | breaking | Changed input filtering for lazy loading: if true, filter retrieves from datasource; if false, scans loaded data. |  |  |
| 1.6.0 | feature | Added lazy loading feature; off by default. When on, items load in batches when scrolling. |  |  |
| 1.4.0 | breaking | Accessibility text is now optional (previously required). | accessibility text |  |
| 1.4.0 | improvement | No longer retrieving full dropdown options list if combobox is readonly. | readonly combobox |  |
| 1.4.0 | fix | Fixed sorting of selected items in Multi Selection to match menu sorting. | Multi Selection sorting |  |
| 1.3.0 | feature | Added static values feature support. | static values |  |
| 1.3.0 | breaking | Renamed database attribute source key definition; existing database sources will reset to none. | database attribute source key definition |  |
| 1.2.0 | feature | Added database list feature support. | database list |  |
| 1.1.1 | breaking | Changed Select/Unselect button caption to Show Select all for easier understanding. | Select/Unselect button caption |  |
| 1.1.0 | feature | Added Show footer property enabling combobox to display footer with custom content. | Show footer property |  |
| 1.1.0 | feature | Added Select/Unselect button property to display select/unselect all button on menu top. | Select/Unselect button property |  |
| 1.1.0 | fix | Removed clear button on selected item labels in read-only state. | clear button in read-only state |  |
