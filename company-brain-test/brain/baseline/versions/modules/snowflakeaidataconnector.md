# SnowflakeAIDataConnector (Marketplace component 225717)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/225717)

| version | published | min Mendix |
|---|---|---|
| 5.3.0 | 2026-09-08 | 10.21.0 |
| 5.2.0 | 2026-08-17 | 10.21.0 |
| 5.1.0 | 2026-06-09 | 10.21.0 |
| 5.0.0 | 2026-04-28 | 10.21.0 |
| 4.0.1 | 2026-03-12 | 10.21.0 |
| 3.1.1 | 2026-03-02 | 10.21.0 |
| 3.0.0 | 2025-11-06 | 10.21.0 |
| 2.0.0 | 2025-04-24 | 10.21.0 |
| 1.4.0 | 2025-04-22 | 9.24.2 |
| 1.3.2 | 2025-01-08 | 9.24.2 |
| 1.2.2 | 2024-09-19 | 9.18.0 |
| 1.1.0 | 2024-05-10 | 9.18.0 |
| 1.0.0 | 2024-04-26 | 9.18.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 5.3.0 | breaking | ContentType and ToolType fields migrated from fixed enumeration to unlimited string type. | ContentType, ToolType |  |
| 5.0.0 | breaking | Cortex Analyst now uses semantic model view instead of YAML file specification. | Cortex Analyst |  |
| 4.0.1 | migration-step | Snowflake REST SQL Connector rebranded to Snowflake AI Data Connector. Not backwards compatible with previous versions. |  |  |
| 4.0.1 | breaking | Decoupled from the GenAICommons module. | GenAICommons |  |
| 3.0.0 | requirement | Module made compatible with latest version of GenAICommons marketplace module. | GenAICommons |  |
| 2.0.0 | requirement | Upgraded to Mendix version 10.21.0. |  |  |
| 2.0.0 | migration-step | All third-party JAR dependencies now configured in module; removed from user lib. |  |  |
| 2.0.0 | requirement | Dependency on GenAICommons is version 3.x, not higher major version. | GenAICommons |  |
| 1.2.2 | migration-step | Added folder and renamed microflows for key-pair authentication, separate from OAuth. |  |  |
