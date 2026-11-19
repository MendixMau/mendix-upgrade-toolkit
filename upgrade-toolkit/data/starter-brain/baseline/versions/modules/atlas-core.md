# Atlas Core (Marketplace component 117187)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/117187)

| version | published | min Mendix |
|---|---|---|
| 4.5.0 | 2026-09-16 | 11.0.0 |
| 4.4.0 | 2026-08-14 | 11.0.0 |
| 4.3.8 | 2026-08-06 | 11.0.0 |
| 4.3.7 | 2026-06-24 | 11.0.0 |
| 4.3.6 | 2026-04-28 | 11.0.0 |
| 4.3.5 | 2026-03-26 | 11.0.0 |
| 4.3.4 | 2026-02-26 | 11.0.0 |
| 4.3.3 | 2026-02-02 | 11.0.0 |
| 4.3.2 | 2026-01-21 | 11.0.0 |
| 4.3.0 | 2025-10-15 | 11.0.0 |
| 4.1.3 | 2025-07-28 | 11.0.0 |
| 4.1.2 | 2025-07-17 | 11.0.0 |
| 4.1.1 | 2025-07-02 | 11.0.0 |
| 4.1.0 | 2025-06-26 | 11.0.0 |
| 4.0.1 | 2025-06-02 | 11.0.0 |
| 4.0.0 | 2025-05-08 | 11.0.0 |
| 3.20.0 | 2026-01-21 | 10.21.0 |
| 3.19.0 | 2025-10-16 | 10.21.0 |
| 3.18.2 | 2025-08-07 | 10.21.0 |
| 3.18.1 | 2025-07-17 | 10.21.0 |
| 3.18.0 | 2025-05-27 | 10.21.0 |
| 3.17.0 | 2025-04-16 | 10.21.0 |
| 3.16.5 | 2025-06-02 | 10.12.6 |
| 3.16.4 | 2025-02-12 | 10.12.6 |
| 3.16.3 | 2025-01-30 | 10.12.6 |
| 3.16.2 | 2024-12-13 | 10.12.6 |
| 3.16.1 | 2024-12-09 | 10.12.6 |
| 3.15.0 | 2024-11-04 | 10.6.0 |
| 3.14.5 | 2024-10-02 | 10.6.0 |
| 3.14.4 | 2024-09-12 | 10.6.0 |
| 3.14.3 | 2024-07-31 | 10.6.0 |
| 3.14.2 | 2024-04-25 | 10.6.0 |
| 3.14.1 | 2024-04-04 | 10.6.0 |
| 3.14.0 | 2024-01-26 | 10.6.0 |
| 3.13.1 | 2024-01-17 | 10.6.0 |
| 3.13.0 | 2023-12-21 | 10.6.0 |
| 3.12.6 | 2026-01-28 | 9.24.0 |
| 3.12.5 | 2024-11-01 | 9.24.0 |
| 3.12.4 | 2024-10-02 | 9.24.0 |
| 3.12.3 | 2024-04-04 | 9.24.0 |
| … 37 older versions | | |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 4.3.7 | breaking | Removed legacy styling for switch widget below version 3.0. | switch widget |  |
| 4.3.0 | breaking | Behavioral changes in layouts, particularly concerning topbar component. | layouts, topbar |  |
| 4.3.0 | breaking | Changed language selector to use combobox instead of language selector widget. | language selector | combobox |
| 4.1.0 | breaking | Design properties updates: introduced group names, form orientation on document level, label width on document level, properties on layout grid columns and rows. | design properties |  |
| 4.1.0 | breaking | Theme variables updates for accessibility, consistency and flexibility improvements. | theme variables |  |
| 4.0.0 | breaking | Atlas major changes. Atlas 4 fully utilizes CSS variables instead of SASS variables. |  |  |
| 3.20.0 | breaking | Replaced Language selector widget with Combobox widget in layouts acting like language selector. | Language selector, Combobox | Combobox |
| 3.17.0 | requirement | Updated Studio Pro minimum version to 10.21 to support Mendix 11. |  |  |
| 3.16.3 | improvement | Changed import order of custom variable to make it work with CSS variables. | custom variable, CSS variables |  |
| 3.16.1 | requirement | Updated Atlas Core minimum version to Studio Pro 10.12.6. |  |  |
| 3.13.0 | migration-step | Updated feedback widget to Mendix Feedback Module; download or update Feedback Module from Marketplace. | Feedback Module | Mendix Feedback Module |
| 3.10.0 | requirement | Minimum required version of Studio Pro set to v9.24.0. |  |  |
| 3.9.0 | requirement | Minimal required version of Studio Pro is v9.18.4 and above. |  |  |
| 3.8.0 | improvement | Migrated from Google Fonts to locally hosted fonts. | fonts |  |
| 3.6.0 | requirement | Minimal required version of Studio Pro is v9.12.0 and above. |  |  |
| 3.5.0 | improvement | Updated Feedback widget to the latest version. | Feedback widget |  |
| 3.2.1 | fix | Fixed this module to be compatible with strict CSP mode. |  |  |
| 3.0.7 | improvement | Updated all widgets. |  |  |
| 3.0.5 | migration-step | Moved resource files from web/resources to public folder. | resource files |  |
| 3.0.4 | breaking | Removed restrictions to show toggle sidebar widget only on phones. | toggle sidebar widget |  |
| 3.0.4 | removal | Removed San Francisco font from default font variable. | default font variable |  |
| 3.0.3 | breaking | Changed default web responsive layout sidebar to be initially open. | Atlas_topbar responsive layout sidebar |  |
| 3.0.3 | breaking | Removed maxWidth property of dropdown widget to fix issue on large screens. | dropdown widget |  |
| 3.0.2 | improvement | Updated Feedback widget. | Feedback widget |  |
| 3.0.1 | breaking | Changed Scroll Container widget behaviour on Atlas_topbar to per region. | Scroll Container widget, Atlas_topbar |  |
| 3.0.1 | breaking | Renamed class name from .statuspage-subtite to .statuspage-subtitle. | .statuspage-subtite | .statuspage-subtitle |
