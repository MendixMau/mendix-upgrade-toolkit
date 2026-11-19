# Ultimate Gantt for Mendix (Marketplace component 213186)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Module, Ciphix, Partner, [marketplace](https://marketplace.mendix.com/link/component/213186)

| version | published | min Mendix |
|---|---|---|
| 3.6.0 | 2025-09-26 | 11.0.0 |
| 2.6.0 | 2025-09-26 | 10.0.0 |
| 2.4.3 | 2025-07-11 | 10.0.0 |
| 2.4.2 | 2025-06-16 | 10.0.0 |
| 2.4.1 | 2025-04-16 | 10.0.0 |
| 2.4.0 | 2025-03-19 | 10.0.0 |
| 2.3.1 | 2025-02-12 | 10.0.0 |
| 2.3.0 | 2025-01-30 | 10.0.0 |
| 2.2.2 | 2024-11-25 | 10.0.0 |
| 2.2.1 | 2024-04-19 | 10.0.0 |
| 2.2.0 | 2024-04-09 | 10.0.0 |
| 2.1.0 | 2024-02-09 | 10.0.0 |
| 2.0.2 | 2024-01-12 | 10.0.0 |
| 2.0.1 | 2023-09-08 | 10.0.0 |
| 2.0.0 | 2023-07-25 | 10.0.0 |
| 1.6.0 | 2025-09-26 | 9.24.12 |
| 1.4.3 | 2025-07-11 | 9.24.12 |
| 1.4.2 | 2025-06-16 | 9.24.12 |
| 1.4.1 | 2025-04-16 | 9.24.12 |
| 1.4.0 | 2025-03-19 | 9.24.12 |
| 1.3.1 | 2025-02-12 | 10.0.0 |
| 1.3.0 | 2025-01-30 | 9.24.12 |
| 1.2.2 | 2024-11-25 | 9.24.12 |
| 1.2.1 | 2024-04-19 | 9.12.0 |
| 1.2.0 | 2024-04-09 | 9.12.0 |
| 1.1.0 | 2024-02-09 | 9.12.0 |
| 1.0.2 | 2024-01-12 | 9.12.0 |
| 1.0.1 | 2023-09-08 | 9.12.0 |
| 1.0.0 | 2023-07-10 | 9.12.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 3.6.0 | requirement | Major upgrade for Bryntum library version. Update scheduler and calendar widgets to latest version. | Bryntum library, scheduler, calendar |  |
| 3.6.0 | feature | Added React client support with skeleton loaders. |  |  |
| 3.6.0 | improvement | Dependencies are now read-only when either associated task is non-editable. | Dependencies |  |
| 2.6.0 | requirement | Major upgrade for Bryntum library version. Update scheduler and calendar widgets to latest version. | Bryntum library, scheduler, calendar |  |
| 2.6.0 | feature | Added React client support with skeleton loaders. |  |  |
| 2.6.0 | improvement | Dependencies are now read-only when either associated task is non-editable. | Dependencies |  |
| 2.4.3 | fix | Fixed an issue with translations for the dojo client. | dojo client, translations |  |
| 2.4.3 | migration-step | Delete old widget bizzomate.BizzomateGantt.mpk from widgets folder. Rename BizzomateGantt module to CiphixGantt before loading new version. | BizzomateGantt, CiphixGantt | CiphixGantt |
| 2.4.1 | fix | Fixed an edge case sync loop. | sync |  |
| 2.4.0 | fix | Fixed a custom column sync issue for booleans. | custom column, booleans |  |
| 2.3.0 | improvement | Significantly improved localization support. | localization |  |
| 2.3.0 | feature | Added dynamic theme support, allowing themes to be set or changed using a string or dynamically through an expression. | theme |  |
| 2.3.0 | migration-step | Delete old widget bizzomate.BizzomateGantt.mpk from widgets directory before loading module. | BizzomateGantt, bizzomate.BizzomateGantt.mpk |  |
| 2.2.2 | fix | Updated Dom purify. | Dom purify |  |
| 2.2.1 | fix | Fixed an issue with conditional task delete introduced in 2.2.0. | task delete |  |
| 2.2.0 | breaking | Column editability is now an expression with the task as a parameter instead of a simple Boolean. | Column editability |  |
| 2.2.0 | breaking | Task editability is now an expression with the task as a parameter instead of defined globally. | Task editability |  |
| 2.2.0 | feature | Added "thin" CSS files to allow for better compatibility when multiple products (e.g. Scheduler and Gantt) are used in same project. | CSS |  |
| 2.2.0 | fix | Fixed a sync issue with assignments when Gantt was filtered from outside the widget (so in the datasource). | assignments, sync, datasource |  |
| 2.1.0 | breaking | Write the id of newly created task, dependency or assignment on respective CRUD object id when adding items to server. See upgrade guide for details. | sync mechanism, CRUD, task, dependency, assignment |  |
| 2.1.0 | fix | Fixed an issue where assignments would not be synced or updated properly. | assignments, sync |  |
| 2.1.0 | removal | Removed PhantomId requirement on task entity. | PhantomId |  |
| 2.1.0 | improvement | The task entity no longer needs to be refreshed after creating a new task, improving performance. | task |  |
| 2.0.2 | improvement | Prevent unnecessary sync of tasks on first load when not all features are enabled. | tasks, sync |  |
| 2.0.2 | improvement | Sync improvements. | sync |  |
| 2.0.0 | requirement | Added support for Mendix 10. | Mendix |  |
| 1.6.0 | requirement | Major upgrade for Bryntum library version. Update scheduler and calendar widgets to latest version. | Bryntum library, scheduler, calendar |  |
| 1.6.0 | feature | Added React client support with skeleton loaders. |  |  |
| 1.6.0 | improvement | Dependencies are now read-only when either associated task is non-editable. | Dependencies |  |
| 1.4.3 | fix | Fixed an issue with translations for the dojo client. | dojo client, translations |  |
| 1.4.3 | migration-step | Delete old widget bizzomate.BizzomateGantt.mpk from widgets folder. Rename BizzomateGantt module to CiphixGantt before loading new version. | BizzomateGantt, CiphixGantt | CiphixGantt |
| 1.4.1 | fix | Fixed an edge case sync loop. | sync |  |
| 1.4.0 | fix | Fixed a custom column sync issue for booleans. | custom column, booleans |  |
| 1.3.0 | improvement | Significantly improved localization support. | localization |  |
| 1.3.0 | feature | Added dynamic theme support, allowing themes to be set or changed using a string or dynamically through an expression. | theme |  |
| 1.3.0 | migration-step | Delete old widget bizzomate.BizzomateGantt.mpk from widgets directory before loading module. | BizzomateGantt, bizzomate.BizzomateGantt.mpk |  |
| 1.2.2 | fix | Updated Dom purify. | Dom purify |  |
| 1.2.1 | fix | Fixed an issue with conditional task delete introduced in 2.2.0. | task delete |  |
| 1.2.0 | breaking | Column editability is now an expression with the task as a parameter instead of a simple Boolean. | Column editability |  |
| 1.2.0 | breaking | Task editability is now an expression with the task as a parameter instead of defined globally. | Task editability |  |
| 1.2.0 | feature | Added "thin" CSS files to allow for better compatibility when multiple products (e.g. Scheduler and Gantt) are used in same project. | CSS |  |
| 1.2.0 | fix | Fixed a sync issue with assignments when Gantt was filtered from outside the widget (so in the datasource). | assignments, sync, datasource |  |
| 1.1.0 | migration-step | Write the id of newly created task, dependency or assignment on respective CRUD object id when adding items to server. | CRUD object id, task, dependency, assignment |  |
| 1.1.0 | fix | Fixed issue where assignments would not be synced or updated properly. | assignments |  |
| 1.1.0 | fix | Fixed issue where assignments would not show initially with large dataset. | assignments |  |
| 1.1.0 | removal | Removed PhantomId requirement on task entity. | PhantomId, task entity |  |
| 1.1.0 | improvement | Task entity no longer needs refresh after creating new task, improving performance. | task entity |  |
| 1.0.2 | improvement | Prevent unnecessary sync of tasks on first load when not all features enabled. | tasks |  |
| 1.0.2 | improvement | Sync improvements. |  |  |
