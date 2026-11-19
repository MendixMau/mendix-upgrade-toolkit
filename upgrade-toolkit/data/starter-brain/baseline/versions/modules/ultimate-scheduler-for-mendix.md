# Ultimate Scheduler for Mendix (Marketplace component 208890)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Module, Ciphix, Partner, [marketplace](https://marketplace.mendix.com/link/component/208890)

| version | published | min Mendix |
|---|---|---|
| 3.12.4 | 2026-08-13 | 11.0.0 |
| 3.12.1 | 2026-04-16 | 10.0.0 |
| 3.12.0 | 2026-04-09 | 10.0.0 |
| 3.11.0 | 2025-09-26 | 11.0.0 |
| 2.12.4 | 2026-08-13 | 10.0.0 |
| 2.12.3 | 2026-07-10 | 10.0.0 |
| 2.12.2 | 2026-06-11 | 10.0.0 |
| 2.12.0 | 2026-04-08 | 11.0.0 |
| 2.11.1 | 2026-04-03 | 10.0.0 |
| 2.11.0 | 2025-09-26 | 10.0.0 |
| 2.7.1 | 2025-07-11 | 10.0.0 |
| 2.7.0 | 2025-06-26 | 10.0.0 |
| 2.6.0 | 2025-01-29 | 9.24.12 |
| 2.5.5 | 2024-11-29 | 9.24.12 |
| 2.5.4 | 2024-11-22 | 9.24.12 |
| 2.5.3 | 2024-10-01 | 9.24.12 |
| 2.5.2 | 2024-09-19 | 9.24.12 |
| 2.5.1 | 2024-08-07 | 9.24.0 |
| 2.5.0 | 2024-07-17 | 9.24.0 |
| 2.4.8 | 2025-01-29 | 10.0.0 |
| 2.4.7 | 2024-11-29 | 10.0.0 |
| 2.4.6 | 2024-11-22 | 10.0.0 |
| 2.4.5 | 2024-10-02 | 10.0.0 |
| 2.4.4 | 2024-10-01 | 9.24.12 |
| 2.4.3 | 2024-09-19 | 10.0.0 |
| 2.4.2 | 2024-06-19 | 10.0.0 |
| 2.4.1 | 2024-05-03 | 10.0.0 |
| 2.4.0 | 2024-04-17 | 10.0.0 |
| 2.3.2 | 2023-12-08 | 10.0.0 |
| 2.3.1 | 2023-11-17 | 10.0.0 |
| 2.3.0 | 2023-10-20 | 10.0.0 |
| 2.2.0 | 2023-09-13 | 10.0.0 |
| 2.1.0 | 2023-09-01 | 10.0.0 |
| 2.0.0 | 2023-07-24 | 10.0.0 |
| 1.12.4 | 2026-08-13 | 9.24.12 |
| 1.11.0 | 2025-09-26 | 9.24.12 |
| 1.10.1 | 2025-07-11 | 9.24.12 |
| 1.10.0 | 2025-06-26 | 9.24.12 |
| 1.9.2 | 2024-06-19 | 9.24.0 |
| 1.9.1 | 2024-05-03 | 9.24.0 |
| … 15 older versions | | |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 3.12.1 | improvement | Updated the stretch events feature | stretch events feature |  |
| 3.11.0 | requirement | Major upgrade for Bryntum library version. Update gantt and calendar widgets to latest version. | Bryntum library |  |
| 3.11.0 | improvement | Reduced flickering for Mendix events in Mendix 10 and 11 |  |  |
| 3.11.0 | fix | Fixed edge case where resources wouldn't refresh with multiple event datasources |  |  |
| 2.11.1 | fix | Fixed datasource loading issue when many event datasources are used |  |  |
| 2.11.0 | requirement | Major upgrade for Bryntum library version. Update gantt and calendar widgets to latest version. | Bryntum library |  |
| 2.11.0 | improvement | Reduced flickering for Mendix events in Mendix 10 and 11 |  |  |
| 2.11.0 | fix | Fixed edge case where resources wouldn't refresh with multiple event datasources |  |  |
| 2.7.1 | fix | Fixed issue with translations for the dojo client |  |  |
| 2.7.1 | migration-step | Delete old widget files bizzomate.BizzomateScheduler.mpk and bizzomate.BizzomateSchedulerDragHelper.mpk. Rename module from BizzomateScheduler to CiphixScheduler before loading new version. | bizzomate.BizzomateScheduler.mpk, bizzomate.BizzomateSchedulerDragHelper.mpk, BizzomateScheduler, CiphixScheduler |  |
| 2.7.0 | improvement | Updated Dompurify to 3.2.6 | Dompurify |  |
| 2.7.0 | removal | Removed community commons dependency | community commons dependency |  |
| 2.7.0 | migration-step | Delete old widget files bizzomate.BizzomateScheduler.mpk and bizzomate.BizzomateSchedulerDragHelper.mpk. Rename module from BizzomateScheduler to CiphixScheduler before loading new version. | bizzomate.BizzomateScheduler.mpk, bizzomate.BizzomateSchedulerDragHelper.mpk, BizzomateScheduler, CiphixScheduler |  |
| 2.6.0 | migration-step | Delete old BizzomateScheduler widgets from widgets directory before loading module. | bizzomate.BizzomateScheduler.mpk, bizzomate.BizzomateSchedulerDragHelper.mpk |  |
| 2.5.5 | fix | Fixed incorrect duration for custom view in combination with disabling floor dates. |  |  |
| 2.5.4 | improvement | Updated DomPurify. | DomPurify |  |
| 2.5.3 | fix | Fixed issue with default week view shift increment. |  |  |
| 2.5.3 | fix | Fixed issue when using numeric values on the context object. |  |  |
| 2.5.2 | fix | Fixed issue with multiple event sources. |  |  |
| 2.5.1 | migration-step | When upgrading, read upgrade guide: https://bizzomate.atlassian.net/wiki/spaces/Docs/pages/2664890380/1.7+Upgrade+guide |  |  |
| 2.5.1 | fix | Fixed missing scheduler drag helper widget from last release. | scheduler drag helper widget |  |
| 2.5.0 | migration-step | When upgrading, read upgrade guide: https://bizzomate.atlassian.net/wiki/spaces/Docs/pages/2664890380/1.7+Upgrade+guide |  |  |
| 2.5.0 | fix | Fixed issue where saving column filters would not work properly. |  |  |
| 2.5.0 | fix | Fixed issue where resources were not being properly refreshed. |  |  |
| 2.4.0 | improvement | Improved CSS support for multi product scenarios with Gantt and Scheduler |  |  |
| 2.3.0 | fix | Fixed refresh behavior when using Mendix widgets within events for Mendix version 10 and above |  |  |
| 2.2.0 | improvement | Modified infinite scroll start date to align properly with context object start date |  |  |
| 2.1.0 | fix | Tooltips with Mendix widgets using event data properly refresh when edited from outside scheduler |  |  |
| 2.1.0 | removal | Removed community commons requirement | community commons |  |
| 2.0.0 | feature | Added support for Mendix 10 |  |  |
| 1.11.0 | requirement | Major upgrade for Bryntum library version. Update gantt and calendar widgets to latest version. | Bryntum library |  |
| 1.11.0 | improvement | Reduced flickering for Mendix events in Mendix 10 and 11 |  |  |
| 1.11.0 | fix | Fixed edge case where resources wouldn't refresh with multiple event datasources |  |  |
| 1.10.1 | fix | Fixed issue with translations for the dojo client |  |  |
| 1.10.1 | migration-step | Delete old widget files bizzomate.BizzomateScheduler.mpk and bizzomate.BizzomateSchedulerDragHelper.mpk. Rename module from BizzomateScheduler to CiphixScheduler before loading new version. | bizzomate.BizzomateScheduler.mpk, bizzomate.BizzomateSchedulerDragHelper.mpk, BizzomateScheduler, CiphixScheduler |  |
| 1.10.0 | migration-step | Delete old BizzomateScheduler widgets from widgets folder before upgrading. | bizzomate.BizzomateScheduler.mpk, bizzomate.BizzomateSchedulerDragHelper.mpk |  |
| 1.10.0 | migration-step | Rename module from BizzomateScheduler to CiphixScheduler before loading new version. | BizzomateScheduler, CiphixScheduler |  |
| 1.10.0 | fix | Fixed double click action for schedulers that don't use the Event entity GUID. |  |  |
| 1.10.0 | improvement | Updated Dompurify to 3.2.6. | Dompurify |  |
| 1.10.0 | removal | Removed Community Commons dependency. | Community Commons |  |
| 1.9.2 | fix | Fixed view skip attribute is now properly passed down. |  |  |
| 1.9.1 | requirement | Moved minimum supported version of Mendix to 9.24.0. | Mendix |  |
| 1.9.1 | fix | Fixed event creation bug introduced in last version. |  |  |
| 1.9.1 | fix | Fixed issue relating to new styling - visible width and related infinite scroll issue. |  |  |
| 1.9.0 | improvement | Improved CSS support for multi product scenarios - Gantt + Scheduler. |  |  |
| 1.9.0 | fix | Fixed missing CSS issue. |  |  |
| 1.9.0 | fix | Fixed view skip attribute of views. |  |  |
| 1.9.0 | fix | Fixed edge case for license check. |  |  |
| 1.8.2 | fix | Fixed issue where events could no longer be created if context object was refreshed. |  |  |
| 1.8.1 | fix | Fixed issue where you can no longer drag create events after specific conditions. |  |  |
| 1.8.1 | fix | Fixed issue where events would display at wrong time if rolled back multiple times. |  |  |
| 1.8.0 | improvement | Right-click menu actions now apply to all selected events only if Ctrl (Windows) or Cmd (Mac) held. |  |  |
| 1.7.0 | fix | Modified infinite scroll start date to align properly with start date set on context object. |  |  |
| 1.6.0 | fix | Tooltips with Mendix widgets using event data now properly refresh when edited from outside scheduler. |  |  |
| 1.6.0 | removal | Removed Community Commons requirement. | Community Commons |  |
| 1.5.2 | fix | Reverted version 1.5.0 due to unnecessary console messages being logged. |  |  |
| 1.5.2 | fix | Resolved known issue affecting refreshing of resource entities when using nested resources in 1.5.0. |  |  |
| 1.5.2 | fix | Fixed: Something prevented widget from being detected when adding module. |  |  |
| 1.4.0 | fix | Resolved peculiar issues that arose in latest versions of Mendix. |  |  |
| 1.3.2 | fix | Fixed issue introduced in 1.3.1 causing events not to refresh properly when changed in Mendix. |  |  |
| 1.3.1 | fix | Fixed event layout feature not always working correctly. |  |  |
| 1.3.0 | fix | Implemented workaround for studio pro preview in versions prior to 9.18 that had a bug. |  |  |
| 1.3.0 | breaking | Resource ID attribute no longer mandatory for timespans; if empty, timespan applied to all rows. | timespans |  |
| 1.3.0 | improvement | Made license check for sandbox.mxapps.io domain more flexible to accommodate page URLs like /p/my-url. |  |  |
| 1.2.0 | breaking | Added control over view flooring to beginning of day, week, month; offset must now be defined in widget. |  |  |
| 1.2.0 | breaking | Made changes to tree expander logic - may affect custom styling overrides. |  |  |
| 1.2.0 | fix | Fixed refresh issue in recent versions of Mendix. |  |  |
| 1.2.0 | fix | Prevented resource on-click microflow from triggering when clicking sub-resource expand icon. |  |  |
| 1.1.6 | fix | SelectedView attribute is now always set even if not initialized on first render. | SelectedView |  |
| 1.1.6 | fix | End date is now always set. |  |  |
| 1.1.6 | fix | Event style & color for drag creating events now uses default color and style of first event source. |  |  |
| 1.1.6 | breaking | Renamed event color enum. |  |  |
| 1.1.5 | fix | Fixed instance where scheduler did not update end date when start date was set in Mendix. |  |  |
| 1.1.5 | fix | Added missing Roboto fonts for material theme. |  |  |
| 1.1.4 | fix | Fixed: Widget was not properly added when importing module. |  |  |
