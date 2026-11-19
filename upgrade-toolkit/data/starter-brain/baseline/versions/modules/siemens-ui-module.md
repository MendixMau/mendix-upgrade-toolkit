# Siemens UI Module (Marketplace component 239207)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Module, Siemens, Platform, [marketplace](https://marketplace.mendix.com/link/component/239207)

| version | published | min Mendix |
|---|---|---|
| 2.1.0 | 2026-09-23 | 11.12.2 |
| 2.0.2 | 2026-08-26 | 11.12.2 |
| 2.0.1 | 2026-08-12 | 11.12.0 |
| 2.0.0 | 2026-07-31 | 11.12.0 |
| 1.10.0 | 2026-08-12 | 10.24.13 |
| 1.9.0 | 2026-06-30 | 10.24.13 |
| 1.8.0 | 2026-05-08 | 10.24.13 |
| 1.7.0 | 2026-03-13 | 10.24.13 |
| 1.6.0 | 2026-01-28 | 10.24.13 |
| 1.5.0 | 2025-12-03 | 10.12.12 |
| 1.4.1 | 2025-11-19 | 10.12.12 |
| 1.4.0 | 2025-11-05 | 10.12.12 |
| 1.3.0 | 2025-09-19 | 10.12.12 |
| 1.2.0 | 2025-08-14 | 10.12.12 |
| 1.1.0 | 2025-08-06 | 10.12.12 |
| 1.0.1 | 2025-07-09 | 10.12.12 |
| 1.0.0 | 2025-06-26 | 10.12.12 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.1.0 | requirement | Siemens UI Module v2.1.0 follows Siemens guidelines v2604. | Siemens guidelines |  |
| 2.0.2 | requirement | Siemens UI Module v2.0.2 has moved to 11.12.2 LTS due to nanoflow issue in version 11.12.0. | Mendix |  |
| 2.0.2 | fix | Card design property conflict on building blocks solved by clearing cached design properties from Mendix 10. | DISW_complex_card_with_actions, DISW_complex_card_with_actions_compact |  |
| 2.0.1 | fix | Page templates and building blocks cleared from cached design property styles causing errors in new Mendix 11 projects. | Page templates, Building blocks, Card, Tiles |  |
| 2.0.0 | requirement | Siemens UI Module v2.0.0 is in Mendix LTS 11.12.0. Update will fix design property conflict on Card Style when updating Atlas 3 to 4. | Mendix |  |
| 2.0.0 | migration-step | Follow migration steps documented in reference guide to migrate your project to Mendix 11. | project |  |
| 2.0.0 | removal | Siemens UI Module v1.10.x will remain in Mendix LTS 10.24.13. No new updates after this version, only critical UI fixes. | Siemens UI Module v1.10.x |  |
| 1.10.0 | removal | Siemens UI Module version 1.x will remain in Mendix LTS 10.24. No new updates after this version, only critical UI fixes. | Siemens UI Module v1.x |  |
| 1.9.0 | improvement | Siemens UI Module is UI compatible with GenAI Commons, Agent Commons and Conversational UI. SASS/CSS variable clashes resolved. | GenAI Commons, Agent Commons, Conversational UI |  |
| 1.9.0 | improvement | Panel component (v1.3.1) included: Refactoring + accessibility fixes. | Panel component |  |
| 1.8.0 | improvement | Preparations for move to Mendix public Marketplace completed. Siemens UI Module will reach larger target audience. | Marketplace |  |
| 1.8.0 | fix | Column selector had a11y issue due to missing aria-selected on menu item. Resolved with Data Widgets module v3.9.0 update. | Table, Grid, DataGrid 2, Data Widgets |  |
| 1.8.0 | known-issue | Button is missing ARIA-HasPopup. Web Content team notified to resolve issue. | Popup Menu, button |  |
| 1.8.0 | known-issue | Options are still not keyboard accessible. Web Content team notified to resolve issue. | Popup Menu, options |  |
| 1.8.0 | feature | Added Splitter component (v1.0.0) with dependency react-resizable-panels ^4.7.3. Cleared in Export Control and SCP One Tool. | Splitter component, react-resizable-panels |  |
| 1.7.0 | removal | Removed TreeNode Indicator building block; checkboxes in custom implementation didn't work as expected due to nesting. | TreeNode Indicator |  |
| 1.7.0 | removal | Removed Editable Table building block; functionality should be available out of box like DataGrid 1. | Editable Table |  |
| 1.7.0 | known-issue | DataGrid 2 column filters still has issues; Web Content team notified. | DataGrid 2 |  |
| 1.7.0 | removal | Removed Comparison view building block; updated all Tiles & Cards building blocks. | Comparison view |  |
| 1.6.0 | requirement | Upgraded Siemens UI Module to LTS version 10.24.13. |  |  |
| 1.6.0 | breaking | Improved and aligned folder structure; renamed snippets, microflows, nanoflows, building blocks per Mendix best practices. | snippets, microflows, nanoflows, building blocks |  |
| 1.6.0 | breaking | Starting v1.6.0, only pluggable components from Siemens team included; platform components must be downloaded separately. | Siemens UI Checkbox, Siemens UI Panel, Siemens UI Dynamic tabs, Siemens UI Toast Notifications |  |
| 1.6.0 | migration-step | Before updating, download/update modules and widgets to supported versions from dependencies page. |  |  |
| 1.6.0 | migration-step | Migrate from Dojo client to React Client for easier migration to Mendix 11, as Dojo client is deprecated. |  |  |
| 1.6.0 | removal | Removed JQuery 3.5.1 (login animation) dependency from Siemens UI Module. | JQuery 3.5.1 |  |
| 1.6.0 | improvement | Updated pluggable components: Siemens UI Panel v.1.2.1 and Siemens UI Tabs v.1.1.0. | Siemens UI Panel, Siemens UI Tabs |  |
| 1.5.0 | breaking | Card/Tile no longer affected by input states; moved capability to separate Card and Tile building blocks. | Card, Tile |  |
| 1.5.0 | improvement | Updated pluggable components: Siemens UI Panel v.1.2.1 and Siemens UI Tabs v.1.1.0. | Siemens UI Panel, Siemens UI Tabs |  |
| 1.4.0 | breaking | Reset Card and Tile default width to 100%; added design property max-width (Tile 150px, Card 250px). | Card, Tile |  |
| 1.4.0 | improvement | Updated Siemens UI Panel v 1.1.1 with Inline Panel variation; Panel closes on Esc key press. | Siemens UI Panel |  |
| 1.3.0 | requirement | Updated jquery-3.5.1.min.js to JQuery 3.7.1 in login page, using CDN now to load it. | JQuery |  |
| 1.3.0 | requirement | Updated support Atlas Core version to 3.16.5. | Atlas Core |  |
| 1.3.0 | requirement | Updated support Combobox to V 2.4.3. | Combobox |  |
| 1.3.0 | requirement | Updated support DataWidgets to v. 2.30.9. | DataWidgets |  |
| 1.3.0 | requirement | Updated support Events to V 1.1.0. | Events |  |
| 1.2.0 | removal | Removed iX_App_Frame page template. | iX_App_Frame |  |
| 1.1.0 | improvement | Replaced font files for compression (ttf to woff2). | font files |  |
| 1.1.0 | breaking | Removed the focus-within state of cards (dev request). | cards |  |
