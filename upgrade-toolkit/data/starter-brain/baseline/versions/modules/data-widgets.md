# Data Widgets (Marketplace component 116540)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/116540)

| version | published | min Mendix |
|---|---|---|
| 3.11.7 | 2026-10-06 | 10.24.0 |
| 3.11.6 | 2026-09-21 | 10.24.0 |
| 3.11.5 | 2026-09-17 | 10.24.0 |
| 3.11.4 | 2026-08-25 | 10.24.0 |
| 3.11.3 | 2026-07-28 | 10.24.0 |
| 3.11.2 | 2026-07-03 | 10.24.0 |
| 3.11.1 | 2026-06-18 | 10.24.0 |
| 3.11.0 | 2026-06-03 | 10.24.0 |
| 3.10.0 | 2026-05-07 | 10.24.0 |
| 3.9.0 | 2026-03-24 | 10.24.0 |
| 3.8.1 | 2026-02-19 | 10.24.0 |
| 3.8.0 | 2026-01-26 | 10.24.0 |
| 3.7.0 | 2025-11-11 | 10.24.0 |
| 3.6.1 | 2025-10-15 | 10.24.0 |
| 3.6.0 | 2025-10-01 | 10.24.0 |
| 3.5.0 | 2025-09-16 | 10.24.0 |
| 3.4.0 | 2025-09-12 | 10.24.0 |
| 3.3.0 | 2025-08-28 | 10.24.0 |
| 3.2.0 | 2025-08-18 | 10.24.0 |
| 3.1.1 | 2025-08-05 | 10.24.0 |
| 3.1.0 | 2025-07-24 | 10.24.0 |
| 3.0.2 | 2025-07-11 | 10.24.0 |
| 3.0.1 | 2025-07-01 | 10.24.0 |
| 3.0.0 | 2025-06-27 | 10.24.0 |
| 2.32.4 | 2025-08-27 | 10.21.0 |
| 2.32.3 | 2025-08-14 | 10.21.0 |
| 2.32.2 | 2025-07-01 | 10.21.0 |
| 2.32.1 | 2025-05-28 | 10.21.0 |
| 2.32.0 | 2025-05-26 | 10.21.0 |
| 2.31.1 | 2025-05-19 | 10.21.0 |
| 2.31.0 | 2025-04-16 | 10.21.0 |
| 2.30.9 | 2025-08-27 | 10.12.6 |
| 2.30.8 | 2025-08-14 | 10.12.6 |
| 2.30.7 | 2025-07-01 | 10.12.6 |
| 2.30.6 | 2025-06-03 | 10.12.6 |
| 2.30.5 | 2025-04-16 | 10.12.6 |
| 2.30.4 | 2025-04-01 | 10.12.6 |
| 2.30.3 | 2025-03-20 | 10.12.6 |
| 2.30.2 | 2025-03-17 | 10.12.6 |
| 2.30.1 | 2025-02-25 | 10.12.6 |
| … 96 older versions | | |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 3.11.6 | fix | Fixed custom pagination ignoring 'Position of pagination' setting and always rendering below grid. | Datagrid |  |
| 3.11.6 | fix | Fixed exporting date column to Excel writing previous calendar day or adding unshown time; now matches grid display. | Datagrid |  |
| 3.11.5 | fix | Fixed top bar not stacking content vertically in narrow containers. | Datagrid |  |
| 3.11.5 | improvement | Updated pagination alignment design property to offer Left, Center, Right; applied above and below gallery. | Gallery |  |
| 3.11.5 | fix | Fixed pagination alignment design property having no effect on pagination control position. | Gallery |  |
| 3.11.5 | fix | Fixed custom pagination widgets always rendering below gallery, ignoring 'Position of pagination' setting. | Gallery |  |
| 3.11.4 | fix | Fixed Gallery widget crash with 'invalid attribute id' error when stored sort order referenced unavailable attribute. | Gallery |  |
| 3.11.2 | fix | Fixed Data Widgets not working in Dojo client in some cases. | Data Widgets |  |
| 3.11.0 | fix | Fixed vertical scrollbar disappearing after hiding wide column while virtual scrolling enabled. | Datagrid |  |
| 3.11.0 | fix | Fixed only first page loading when grid had columns requiring horizontal scrolling. | Datagrid |  |
| 3.9.0 | improvement | Changed gallery settings structure to align with data grid. | Gallery |  |
| 3.8.0 | breaking | Changed 'hasChildren' configuration from boolean to expression. | TreeNode |  |
| 3.7.0 | breaking | Widget settings have been reorganized to make configuration easier. | Datagrid |  |
| 3.6.0 | breaking | Changed datagrid styling display to use grid instead of contents with grid-template-column: subgrid for column alignment and proper scrollbar positioning. | Datagrid, widget-datagrid-head, widget-datagrid-body |  |
| 3.5.0 | migration-step | Consolidated all SCSS variables from individual files into variables.scss. Please validate data widgets stylings after update. | SCSS variables |  |
| 3.2.0 | breaking | Removed all metadata stored in xpath to improve integration with other services. | Datagrid |  |
| 3.1.1 | breaking | Text configurations for empty option, empty selection, and input placeholder need to be reviewed and reconfigured. | DatagridDropdownFilter |  |
| 3.0.0 | breaking | Grid-wide filtering is now configurable directly within filter widget settings. Existing configurations will be automatically converted to new setup when updating. | Datagrid, Gallery |  |
| 2.32.3 | breaking | Text configurations for empty option, empty selection, and input placeholder need to be reviewed and reconfigured. | DatagridDropdownFilter |  |
| 2.31.0 | requirement | Updated studio pro minimum version to 10.21 to support Mendix 11. |  |  |
| 2.30.8 | breaking | Text configurations for empty option, empty selection, and input placeholder need to be reviewed and reconfigured. | DatagridDropdownFilter |  |
| 2.30.0 | improvement | HTML changed to meet modern accessibility requirements. | DatagridDropdownFilter |  |
| 2.30.0 | improvement | Column settings related to drop-down filter moved into dedicated group. | Datagrid |  |
| 2.30.0 | breaking | Drop-down filter rewritten with new HTML for accessibility, may break existing CSS styling. | DatagridDropdownFilter |  |
| 2.30.0 | breaking | HTML structure changed, may affect CSS and styling. | DatagridDropdownFilter |  |
| 2.27.9 | improvement | Updated internal dependencies. | DatagridDateFilter |  |
| 2.27.7 | breaking | Text configurations for empty option, empty selection, input placeholder need review and reconfiguration. | DatagridDropdownFilter |  |
| 2.27.5 | removal | Removed support for reference set associations to allow data grid to work on SP 9.24. | Datagrid |  |
| 2.23.0 | removal | Removed 'Filter groups' properties. | Datagrid, Gallery |  |
| 2.23.0 | removal | Removed 'Group key' property. | DatagridDateFilter |  |
| 2.22.0 | improvement | Improved filters in data widgets. | DatagridDateFilter, DatagridDropdownFilter, DatagridNumberFilter, DatagridTextFilter, Datagrid, Gallery |  |
| 2.22.0 | breaking | Major filter improvement. Filter values and operators are now stored as part of personalization. | Datagrid |  |
| 2.22.0 | known-issue | Due to filter changes, current saved personalization will be reset in this version. | Datagrid |  |
| 2.20.0 | feature | Updated JS actions for resetting filters with option to reset to default filter's value. | Reset_All_Filters, Reset_Filter |  |
| 2.20.0 | feature | Added new JS action Set_Filter to set single filter to specific value in Data grid 2 or Gallery. | Set_Filter |  |
| 2.20.0 | breaking | Data widgets now use Atlas variables for styling. This may change widget appearance based on custom variables. | Data Widgets |  |
| 2.20.0 | improvement | Updated event listener for Reset_Filter to allow reset to default value. | DatagridDateFilter |  |
| 2.20.0 | improvement | Updated event listener for Reset_All_Filters to allow reset to default value. | Datagrid |  |
| 2.18.0 | removal | Removed sorting console warnings that were being triggered incorrectly. | Datagrid |  |
| 2.17.0 | improvement | Enhanced swap behavior of columns with slight adjustment to classnames applied to swapped elements. | Datagrid |  |
| 2.17.0 | feature | Added ability to store personalization configuration in browser's local storage or attribute. | Datagrid |  |
| 2.16.0 | feature | Expanded pagination options with new 'Load more' feature enabling users to load additional data. | Datagrid |  |
| 2.16.0 | improvement | Data grid now automatically re-reads and applies personalization settings when underlying attribute changes. | Datagrid |  |
| 2.16.0 | breaking | Made Visible property of columns required. Explicitly set boolean value to set visibility. | Datagrid |  |
| 2.11.0 | improvement | Improved keyboard navigation for accessibility per WAI ARIA guide. Arrows, page up/down, home, end, ctrl+home, ctrl+end now navigate focus within grid. | Datagrid |  |
| 2.10.0 | breaking | Changed keyboard selection behavior: use 'shift+space' to select/deselect items when selection is enabled. | Gallery |  |
| 2.10.0 | breaking | Changed widget HTML and CSS: new div element wraps each item if 'On click' event is enabled. Some CSS selectors may be affected. | Gallery |  |
| 2.9.0 | breaking | Changed DOM structure to allow sticky header on virtual scrolling pagination mode. | Datagrid |  |
| 2.8.6 | breaking | Changed widget HTML. Some CSS selectors may be affected. Check custom styles after updating. | TreeNode |  |
| 2.8.5 | breaking | Changed DOM structure for date filter to appear inline with container for better accessibility. | DatagridDateFilter |  |
| 2.8.5 | breaking | Changed DOM structure for dropdown filter to appear inline with container for better accessibility. | DatagridDropdownFilter |  |
| 2.8.5 | improvement | Improved accessibility of the Datagrid widget. | Datagrid |  |
| 2.8.5 | breaking | Changed DOM structure for filter options to appear inline with container for better accessibility. | Datagrid |  |
| 2.8.5 | improvement | Improved accessibility of the Gallery widget. | Gallery |  |
| 2.7.1 | fix | Fixed an issue with widget rendering and performance. | DatagridDateFilter |  |
| 2.7.1 | breaking | Default value attribute now used only as initial value; further changes are ignored. | DatagridDateFilter |  |
| 2.6.0 | breaking | Property renamed: Filtering tab to Grid wide filtering. | Datagrid |  |
| 2.6.0 | breaking | Property renamed: Show header filters to Grid wide filters. | Datagrid |  |
| 2.3.1 | fix | Fixed this widget to be compatible with strict CSP mode. | DatagridDropdownFilter |  |
| 2.2.1 | improvement | Changed style variables to use to allow value overriding with Atlas. |  |  |
| 2.0.3 | removal | Removed Snippet, Example enumeration and version constant from the module. | Snippet, Example enumeration, version constant |  |
| 2.0.2 | breaking | Made "Enable advanced options" available only for Studio users; advanced features available by default in Studio Pro. | Data Grid 2, Gallery, Tree Node |  |
| 2.0.1 | fix | Fixed widgets getting duplicate identifiers assigned causing accessibility inconsistencies. | Filter widgets |  |
| 2.0.0 | breaking | Renamed Datagrid date filter to Date filter. | Datagrid date filter | Date filter |
| 2.0.0 | breaking | Renamed Datagrid drop-down filter to Drop-down filter. | Datagrid drop-down filter | Drop-down filter |
| 2.0.0 | breaking | Renamed Datagrid number filter to Number filter. | Datagrid number filter | Number filter |
| 2.0.0 | breaking | Renamed Datagrid text filter to Text filter. | Datagrid text filter | Text filter |
| 2.0.0 | migration-step | If updating from v1 (DataGrid module), rename Marketplace module to DataWidgets before update to v2. |  |  |
| 1.3.2 | breaking | Moved resource assets from themesource/datagrid/web to themesource/datagrid/public folder. | themesource/datagrid |  |
| 1.1.2 | breaking | Removed inner styles from widgets and moved to module themesource. | themesource/datagrid |  |
| 1.1.0 | breaking | Removed default styles from widgets; styles now located in themesource/datagrid/web. | themesource/datagrid/web |  |
| 1.1.0 | breaking | Borders moved to design properties; please reconfigure. |  |  |
| 1.1.0 | migration-step | Module update requires properties to be updated and reconfigured. |  |  |
