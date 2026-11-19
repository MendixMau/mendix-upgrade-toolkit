# Global Inbox Connector (Marketplace component 259155)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/259155)

| version | published | min Mendix |
|---|---|---|
| 0.3.0 | 2026-04-28 | 11.6.0 |
| 0.2.0 | 2026-04-20 | 11.6.0 |
| 0.1.0 | 2026-03-31 | 11.6.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 0.3.0 | migration-step | Updated ASU_GlobalInboxConnector_Startup microflow to migrate existing WorkflowUserTask objects to Global Inbox. Only in-progress tasks included; synchronous execution may take time. | ASU_GlobalInboxConnector_Startup, WorkflowUserTask |  |
| 0.3.0 | breaking | Removed AppId constant; now configured automatically in startup microflow. | AppId |  |
| 0.3.0 | breaking | Renamed GlobalInboxEventService event names, related entities, and microflows. | GlobalInboxEventService |  |
| 0.3.0 | fix | Fixed issue where multiple objects could be created for a single Workflow Definition. | Workflow Definition |  |
| 0.3.0 | requirement | Update and deploy Global Inbox module to version 0.3.0 before deploying Global Inbox Connector module. | Global Inbox |  |
