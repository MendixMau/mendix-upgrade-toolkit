# Marketplace modules: compatibility and upgrade notes

Source: marketplace-api.mendix.com per-version release notes, layer baseline.


##  Coherent Spark <a id="207855"></a>
Module, Coherent, Partner, [marketplace](https://marketplace.mendix.com/link/component/207855)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2023-03-03 | 9.21.0 |

## 3D Printing management <a id="211866"></a>
Industry Template, TOCnDix, Partner, [marketplace](https://marketplace.mendix.com/link/component/211866)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2023-06-27 | 9.24.2 |

## 3D Viewer <a id="118345"></a>
Service, Siemens, Siemens, [marketplace](https://marketplace.mendix.com/link/component/118345)

| version | published | min Mendix |
|---|---|---|
| 7.1.2 | 2026-09-11 | 11.12.2 |
| 7.0.0 | 2026-06-09 | 10.24.13 |
| 6.0.7 | 2026-04-29 | 10.0.0 |
| 6.0.6 | 2026-02-19 | 10.0.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 7.1.2 | requirement | Requires Mendix 11.12.2 or higher. | Mendix |  |
| 7.0.0 | breaking | 3D Viewer rebuilt with React client mode. Manually update widgets: copy 3DViewer package from '3DViewer.mpk/widgets' to 'yourMendixApp/widgets'. | 3D Viewer, React client |  |
| 7.0.0 | requirement | Requires Mendix 10.24.13 or higher. Supports both Mendix 10 and Mendix 11. | Mendix |  |
| 7.0.0 | known-issue | Widgets must be updated manually. Copy 3DViewer package from '3DViewer.mpk/widgets' to 'yourMendixApp/widgets'. | 3D Viewer widgets |  |
| 6.0.6 | security | Updated Axios to latest stable version to patch security vulnerabilities. | Axios |  |
| 6.0.6 | improvement | Upgraded Kotlin compiler and runtime for improved build stability and security fixes. | Kotlin compiler, Kotlin runtime |  |

## A2A Agent Connector <a id="202543"></a>
Solution, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/202543)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2026-04-28 | 11.0.0 |

## ABBYY Vantage Connector <a id="209147"></a>
Module, ABBYY, Partner, [marketplace](https://marketplace.mendix.com/link/component/209147)

| version | published | min Mendix |
|---|---|---|
| 2.0.1 | 2024-04-22 | 9.24.1 |
| 1.0.0 | 2023-03-30 | 9.24.0 |

## Access Provider Template <a id="229790"></a>
Service, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/229790)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2024-08-13 | 9.24.2 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.0.0 | requirement | Requires Mendix 9.24.2 or above. |  |  |

## Accessibility Helper <a id="114803"></a>
Widget, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/114803)

| version | published | min Mendix |
|---|---|---|
| 2.2.2 | 2026-02-10 | 9.6.0 |
| 2.2.1 | 2023-09-27 | 9.6.0 |
| 2.2.0 | 2023-06-05 | 9.6.0 |
| 2.1.0 | 2021-12-23 | 9.6.0 |
| 2.0.0 | 2021-09-28 | 9.6.0 |
| 1.1.0 | 2021-07-27 | 9.0.5 |
| 1.0.1 | 2021-03-31 | 9.0.5 |
| 1.0.0 | 2020-07-13 | 8.10.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.0.1 | fix | Updated widget's consistency checks to be compatible with Mendix 9. |  |  |

## Accordion <a id="117895"></a>
Widget, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/117895)

| version | published | min Mendix |
|---|---|---|
| 2.3.6 | 2026-09-15 | 9.6.0 |
| 2.3.5 | 2026-02-10 | 9.6.0 |
| 2.3.4 | 2025-02-13 | 9.6.0 |
| 2.3.3 | 2024-08-28 | 9.6.0 |
| 2.3.2 | 2024-08-09 | 9.6.0 |
| 2.3.1 | 2023-09-27 | 9.6.0 |
| 2.3.0 | 2023-06-05 | 9.6.0 |
| 2.2.0 | 2023-01-30 | 9.6.0 |
| 2.1.2 | 2022-07-14 | 9.6.0 |
| 2.1.1 | 2022-04-01 | 9.6.0 |
| 2.1.0 | 2021-12-23 | 9.6.0 |
| 2.0.2 | 2021-10-12 | 9.6.0 |
| 2.0.1 | 2021-10-06 | 9.6.0 |
| 2.0.0 | 2021-09-28 | 9.6.0 |
| 1.1.1 | 2021-08-17 | 9.0.5 |
| 1.1.0 | 2021-07-22 | 9.0.5 |
| 1.0.0 | 2021-06-29 | 9.0.5 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.3.6 | fix | Fixed accordion content reloading when collapsed state attribute changed or was updated by microflow. |  |  |
| 2.3.4 | fix | Fixed issue where initial collapsed state sometimes wouldn't update accordion. |  |  |
| 2.3.2 | fix | Fixed nested mode display collapse/uncollapse content sync with accordion state. |  |  |
| 2.1.2 | fix | Fixed issue related to rotating icons (180deg) when animations are switched off. |  |  |
| 2.1.1 | fix | Fixed widget compatibility with strict CSP mode. |  |  |
| 2.1.0 | breaking | Made 'Enable advanced options' available only for Studio users; all advanced features available by default in Studio Pro. | Enable advanced options |  |
| 2.0.2 | breaking | Made 'Enable advanced options' available only for Studio users; all advanced features available by default in Studio Pro. | Enable advanced options |  |
| 2.0.1 | fix | Fixed issue where widgets get duplicate identifiers assigned causing accessibility inconsistencies. |  |  |
| 2.0.0 | breaking | Renamed advanced options property to emphasize it is about advanced properties' activation. |  |  |
| 1.1.1 | fix | Fixed display issue in Structure and Design Mode/Studio when no group configured. |  |  |

## Administration module <a id="23513"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/23513)

| version | published | min Mendix |
|---|---|---|
| 4.5.0 | 2026-05-13 | 10.24.0 |
| 4.4.0 | 2025-10-15 | 10.24.0 |
| 4.3.2 | 2025-07-07 | 10.21.0 |
| 4.3.1 | 2025-06-18 | 10.21.0 |
| 4.3.0 | 2025-05-12 | 10.21.0 |
| 4.2.0 | 2025-04-22 | 10.21.0 |
| 4.1.0 | 2024-02-06 | 10.6.0 |
| 4.0.0 | 2024-01-26 | 10.6.0 |
| 3.0.1 | 2025-07-07 | 9.18.0 |
| 3.0.0 | 2023-04-14 | 9.18.0 |
| 2.1.2 | 2022-11-23 | 9.0.5 |
| 2.1.1 | 2022-05-11 | 9.0.5 |
| 2.1.0 | 2022-01-05 | 9.0.5 |
| 2.0.1 | 2021-10-14 | 9.0.5 |
| 2.0.0 | 2021-10-01 | 9.0.5 |
| 1.4.0 | 2023-04-14 | 8.18.11 |
| 1.3.2 | 2022-11-23 | 8.18.11 |
| 1.3.0 | 2022-01-05 | 8.18.11 |
| 1.2.1 | 2020-02-19 | 8.0.0 |
| 1.2.0 | 2020-02-19 | 8.0.0 |
| 1.1.1 | 2019-10-30 | 8.0.0 |
| 1.1.0 | 2019-10-30 | 8.0.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 4.5.0 | requirement | Upgraded Data Widgets compatibility to v3.10.0 | Data Widgets |  |
| 4.4.0 | requirement | Upgraded the module to Mendix 10.24.0 |  |  |
| 4.4.0 | requirement | Upgraded Data Widgets module compatibility to v3.6.0 | Data Widgets |  |
| 4.3.0 | breaking | Moved away from List View for role assignment to using DG2 reference set supported feature. | List View, role assignment, DG2 | DG2 |
| 4.2.0 | requirement | Upgraded the module to Mendix version 10.21.0 for compatibility with Mendix 11 |  |  |
| 4.2.0 | requirement | Updated Data Widgets compatibility to version 2.31.0 | Data Widgets |  |
| 4.2.0 | requirement | Updated Atlas Web Content compatibility to version 3.8.0 | Atlas Web Content |  |
| 4.2.0 | requirement | Updated Combo Box compatibility to version 2.8.0. Ensure Combo Box widget is installed in your project. | Combo Box |  |
| 4.1.0 | breaking | Switched to new Combo Box widget for Language and Time zone fields to add type-ahead filtering. Ensure Combo Box widget is installed. | Language field, Time zone field, Combo Box | Combo Box |
| 4.0.0 | requirement | Upgraded the module to Mendix version 10.6.0 |  |  |
| 4.0.0 | breaking | Replaced Data Grid widget with Data Grid 2 widget for React client compatibility, introduced in Mendix 10.7.0 | Data Grid, Data Grid 2 | Data Grid 2 |
| 4.0.0 | breaking | Replaced Input Reference Set Selector widget with Combo Box widget for React client compatibility, introduced in Mendix 10.7.0. Ensure Combo Box widget is installed. | Input Reference Set Selector, Combo Box | Combo Box |
| 3.0.0 | requirement | Upgraded the module to Mendix version 9.18.0 for compatibility with Mendix 10 |  |  |
| 3.0.0 | removal | Removed supporting microflows for Mendix SSO introduced in version 2.1.0. Move them to customized module before upgrade. | Mendix SSO, supporting microflows |  |
| 3.0.0 | migration-step | If Mendix SSO is currently part of your project but not used, remove Mendix SSO module and delete related dependencies in userlib folder. | Mendix SSO |  |
| 2.1.1 | migration-step | If Mendix SSO v3.0.0 not needed, delete folder Mendix SSO from module or exclude all its microflows. | Mendix SSO |  |
| 2.0.0 | requirement | Updated to Mendix 9. Compatible with Atlas 3.0. |  |  |
| 1.4.0 | removal | Removed supporting microflows for Mendix SSO introduced in version 1.3.0. Move them to customized module before upgrade. | Mendix SSO, supporting microflows |  |
| 1.4.0 | migration-step | If Mendix SSO is currently part of your project but not used, remove Mendix SSO module and delete related dependencies in userlib folder. | Mendix SSO |  |
| 1.1.0 | requirement | Upgraded to Mendix 8.0.0 |  |  |

## Advanced Audit Trail <a id="120943"></a>
Solution, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/120943)

| version | published | min Mendix |
|---|---|---|
| 2.0.0 | 2024-03-11 | 9.12.0 |
| 1.0.0 | 2022-08-11 | 9.12.0 |

## Advanced Audit Trail - Core <a id="120237"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/120237)

| version | published | min Mendix |
|---|---|---|
| 4.1.1 | 2026-09-22 | 11.12.0 |
| 4.0.0 | 2026-07-01 | 11.12.0 |
| 3.0.2 | 2026-02-11 | 10.21.0 |
| 3.0.1 | 2025-11-12 | 10.21.0 |
| 3.0.0 | 2025-08-22 | 10.21.0 |
| 2.0.6 | 2026-02-06 | 9.24.27 |
| 2.0.5 | 2025-11-12 | 9.24.27 |
| 2.0.4 | 2025-08-22 | 9.24.27 |
| 2.0.2 | 2025-04-01 | 9.24.18 |
| 2.0.1 | 2025-03-17 | 9.24.18 |
| 2.0.0 | 2026-02-11 | 9.24.18 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 4.0.0 | requirement | Added support for Mendix 11.12.0 |  |  |
| 3.0.0 | requirement | Upgraded the Advanced Audit Trail - Core to Mendix Studio Pro 10.21.0 |  |  |
| 2.0.1 | breaking | Use snippets instead of popups for configuration in Settings_Edit and CachedSnapshot_Overview. | Settings_Edit, CachedSnapshot_Overview |  |
| 2.0.0 | requirement | Added support for Mendix 10 |  |  |
| 2.0.0 | removal | Removed licensing mechanism | licensing mechanism |  |

## Advanced Audit Trail UI <a id="120204"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/120204)

| version | published | min Mendix |
|---|---|---|
| 4.1.0 | 2026-08-24 | 11.12.0 |
| 4.0.0 | 2026-07-01 | 11.12.0 |
| 3.0.2 | 2026-03-18 | 10.21.0 |
| 3.0.1 | 2025-11-12 | 10.21.0 |
| 3.0.0 | 2025-08-22 | 10.21.0 |
| 2.0.6 | 2026-02-06 | 9.24.27 |
| 2.0.5 | 2025-11-12 | 9.24.27 |
| 2.0.4 | 2025-08-22 | 9.24.27 |
| 2.0.2 | 2025-04-01 | 9.24.18 |
| 2.0.1 | 2025-03-17 | 9.24.18 |
| 2.0.0 | 2026-02-11 | 9.24.18 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 4.1.0 | feature | Advanced Audit Trail now supports React client in Mendix 11 and newer applications. | React client |  |
| 4.0.0 | requirement | Added support for Mendix 11.12.0. | Mendix |  |
| 3.0.2 | fix | Resolved an issue where searches by Transaction ID and Execution ID were not returning results. | Transaction ID search, Execution ID search |  |
| 3.0.0 | requirement | Upgraded the Advanced Audit Trail - Core to Mendix Studio Pro 10.21.0. | Advanced Audit Trail - Core, Mendix |  |
| 2.0.6 | fix | Resolved an issue where searches by Transaction ID and Execution ID were not returning results. | Transaction ID search, Execution ID search |  |
| 2.0.2 | improvement | Updated search functionality now supports exact matches for Execution ID, Transaction ID, Object Code, GUID and flexible filtering for Entity, Username, Role. | search functionality, Execution ID, Transaction ID, Object Code, GUID, Entity, Username, Role |  |
| 2.0.1 | migration-step | Use snippets instead of popups for configuration in Settings_Edit and CachedSnapshot_Overview. | Settings_Edit, CachedSnapshot_Overview |  |
| 2.0.0 | requirement | Added support for Mendix 10. | Mendix |  |
| 2.0.0 | breaking | Removed licensing mechanism. | licensing mechanism |  |
| 2.0.0 | feature | Added default timeout to REST calls to Advanced Audit Trail service. | REST calls |  |

## Aelion - DTAP Environment information <a id="110921"></a>
Module, Blue Green, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/110921)

| version | published | min Mendix |
|---|---|---|
| 1.1.0 | 2021-04-21 | 8.0.0 |
| 1.0.0 | 2019-08-26 | 8.0.0 |

## Agent Builder Starter App <a id="240369"></a>
Starter App, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/240369)

| version | published | min Mendix |
|---|---|---|
| 2.1.1 | 2026-09-07 | 11.12.3 |
| 2.0.0 | 2026-07-02 | 10.24.13 |
| 1.10.0 | 2026-05-12 | 10.24.13 |
| 1.9.0 | 2026-04-17 | 10.24.13 |
| 1.8.0 | 2026-02-02 | 10.24.13 |
| 1.7.0 | 2025-12-24 | 10.24.13 |
| 1.6.0 | 2025-11-27 | 10.24.0 |
| 1.5.0 | 2025-10-20 | 10.24.0 |
| 1.4.0 | 2025-09-23 | 10.24.0 |
| 1.3.0 | 2025-09-01 | 10.24.0 |
| 1.2.0 | 2025-08-25 | 10.24.0 |
| 1.1.0 | 2025-07-08 | 10.24.0 |
| 1.0.0 | 2025-04-25 | 10.21.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.1.1 | requirement | Upgrade to Mendix 11.12.3. |  |  |
| 2.1.1 | improvement | Marketplace modules upgraded to latest versions enabling streaming capability for agent responses in Conversational UI. | Marketplace modules, Conversational UI |  |
| 2.1.1 | breaking | Draft tickets are now committed to maintain support ticket availability in UI required for new streaming capability. | Draft tickets |  |
| 2.0.0 | requirement | App upgraded to Mendix 11.12 and Atlas 4. |  |  |
| 2.0.0 | feature | Agent editor extension added to the application. | Agent editor extension |  |
| 2.0.0 | improvement | All marketplace modules updated to their latest versions. | Marketplace modules |  |
| 1.10.0 | improvement | Marketplace modules upgraded to their latest versions. | Marketplace modules |  |
| 1.9.0 | improvement | Marketplace modules upgraded to their latest versions enabling Human-In-The-Loop capabilities. | Marketplace modules |  |
| 1.9.0 | feature | Default agent updated to use Human-In-The-Loop; tool calls shown in chat UI with user confirmation requirement. | GenAICommons, ConversationalUI |  |
| 1.8.0 | improvement | Marketplace modules upgraded to their latest versions. | Marketplace modules |  |
| 1.8.0 | feature | Google Gemini connector added to the application. | Google Gemini connector |  |
| 1.7.0 | improvement | Marketplace modules upgraded to their latest versions. | Marketplace modules |  |
| 1.7.0 | requirement | Application upgraded to Mendix SP 10.24.13. |  |  |
| 1.7.0 | removal | Dependency required for XSS Sanitization removed from CommunityCommons module. | CommunityCommons |  |
| 1.6.0 | improvement | All marketplace modules updated to their latest versions. | Marketplace modules |  |
| 1.5.0 | improvement | GenAI modules and Encryption upgraded to their latest versions. | GenAI modules, Encryption |  |
| 1.4.0 | improvement | GenAI modules and encryption module upgraded. | GenAI modules, Encryption module |  |
| 1.3.0 | feature | App now supports adding all tools from MCP server to agent version enabling LLM tool utilization. | Agent Commons, MCP server |  |
| 1.3.0 | requirement | New dependency added on MCP Client module. | MCP Client |  |
| 1.3.0 | improvement | Updated modules: Agent Commons 2.1.1, Amazon Bedrock Connector 9.2.0, Atlas Core 3.18.2, Atlas Web Content 4.1.0, AWS Authentication 4.1.1, CommunityCommons 11.3.0, DatabaseConnector 7.0.1, DataWidgets 3.3.0, GenAI Commons 5.2.0, MCP Client 2.0.0, OpenAI Connector 7.2.0. | Agent Commons, Amazon Bedrock Connector, Atlas Core, Atlas Web Content, AWS Authentication, CommunityCommons, DatabaseConnector, DataWidgets, GenAI Commons, MCP Client, OpenAI Connector |  |
| 1.2.0 | improvement | Updated marketplace modules: Administration 4.3.2, Agent Commons 2.0.0, Amazon Bedrock 9.1.0, AWS Authentication 4.1.1, Community Commons 11.3.0, Conversational UI 5.0.1, Data widgets 3.1.1, GenAI Commons 5.1.0, MxGenAI Connector 5.1.0, OpenAI Connector 7.1.0, PgVector Knowledge base 5.1.0. | Administration, Agent Commons, Amazon Bedrock, AWS Authentication, Community Commons, Conversational UI, Data widgets, GenAI Commons, MxGenAI Connector, OpenAI Connector, PgVector Knowledge base |  |
| 1.1.0 | improvement | Updated marketplace modules to: Agent Commons 1.3.0, Amazon Bedrock 8.2.0, Atlas Core 3.18.0, Atlas Web Content 3.8.0, AWS Authentication 4.1.1, Community Commons 11.2.0, ConversationalUI 4.0.0, Data widgets 2.32.1, Database Connector 7.0.0, Encryption 11.0.1, Feedback Module 4.0.1, GenAI Commons 4.2.0, Mendix Cloud GenAI Connector 4.2.0, Nanoflow Commons 6.0.0, Object Handling 5.0.0, OpenAI Connector 6.0.0, PgVector Knowledge Base 4.2.0, WebActions 2.11.0. | Agent Commons, Amazon Bedrock, Atlas Core, Atlas Web Content, AWS Authentication Connector, Community Commons, ConversationalUI, Data widgets, Database Connector, Encryption, Feedback Module, GenAI Commons, Mendix Cloud GenAI Connector, Nanoflow Commons, Object Handling, OpenAI Connector, PgVector Knowledge Base, WebActions |  |

## Agent Commons <a id="240371"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/240371)

| version | published | min Mendix |
|---|---|---|
| 4.3.1 | 2026-10-05 | 11.12.4 |
| 4.3.0 | 2026-08-31 | 11.12.3 |
| 4.2.0 | 2026-08-07 | 11.12.2 |
| 4.1.0 | 2026-07-22 | 11.12.1 |
| 4.0.0 | 2026-07-02 | 11.12.0 |
| 3.2.0 | 2026-05-28 | 10.24.13 |
| 3.1.0 | 2026-03-27 | 10.24.13 |
| 3.0.1 | 2026-03-10 | 10.24.13 |
| 2.7.0 | 2026-01-19 | 10.24.13 |
| 2.6.0 | 2025-12-22 | 10.24.13 |
| 2.5.0 | 2025-11-21 | 10.24.0 |
| 2.4.1 | 2025-11-07 | 10.24.0 |
| 2.4.0 | 2025-10-29 | 10.24.0 |
| 2.3.0 | 2025-10-16 | 10.24.0 |
| 2.2.0 | 2025-09-19 | 10.24.0 |
| 2.1.1 | 2025-09-01 | 10.24.0 |
| 2.1.0 | 2025-08-29 | 10.24.0 |
| 2.0.0 | 2025-08-08 | 10.24.0 |
| 1.4.0 | 2025-07-21 | 10.21.0 |
| 1.3.0 | 2025-06-24 | 10.21.0 |
| 1.2.0 | 2025-05-21 | 10.21.0 |
| 1.1.0 | 2025-05-09 | 10.21.0 |
| 1.0.0 | 2025-03-25 | 10.21.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 4.3.0 | requirement | Upgraded to Mendix 11.12.3. |  |  |
| 4.2.0 | requirement | Upgrade to Mendix 11.12.2. |  |  |
| 4.1.0 | requirement | Upgrade to Mendix 11.12.1. |  |  |
| 4.0.0 | requirement | Module upgraded to Mendix 11.12. |  |  |
| 4.0.0 | removal | Deprecated associations to MCPClient.MCPTool and GenAICommons.DeployedKnowledgeBase and corresponding migration microflows removed. | MCPClient.MCPTool, GenAICommons.DeployedKnowledgeBase |  |
| 3.2.0 | breaking | Styling consolidated from AgentCommons to ConversationalUI to fix inconsistent rendering. Update ConversationalUI module. | ConversationalUI |  |
| 3.1.0 | fix | Changed message addition order to prevent incorrect message ordering passed to the model. |  |  |
| 3.0.1 | breaking | Module aligned with latest changes in ConsumedKnowledgeBase and ConsumedMCPService. Breaking change requiring migration. | ConsumedKnowledgeBase, ConsumedMCPService |  |
| 3.0.1 | breaking | Call agent operations behave differently: tool call response sent to microflow without final assistant response. |  |  |
| 3.0.1 | requirement | Compatible with GenAI Commons 6.0.0, ConversationalUI 6.0.0 and MCPClient 3.0.1 versions. | GenAI Commons, ConversationalUI, MCPClient |  |
| 2.7.0 | breaking | Duplicated styling classes moved to ConversationalUI and renamed to prevent Atlas class overwriting. Update ConversationalUI. | ConversationalUI |  |
| 2.6.0 | requirement | Module upgraded to Mendix 10.24.13. |  |  |
| 2.2.0 | breaking | ToolChoice can no longer be set for MCP server tools in the UI. |  |  |
| 2.2.0 | improvement | Agents registered with requests by internally passing AgentVersionId to support GenAICommons traceability capabilities. |  |  |
| 2.1.0 | requirement | New dependency on MCP Client module added. | MCPClient |  |
| 2.1.0 | breaking | Context entities can no longer be edited once an agent version is saved to prevent breaking in-use versions. |  |  |
| 2.0.0 | requirement | Module upgraded to Mendix Studio Pro version 10.24. |  |  |
| 1.3.0 | breaking | Model selection made part of agent versioning. Existing agents require manual model setting for in-use version. |  |  |
| 1.3.0 | improvement | Improved support for knowledge bases in Amazon Bedrock and custom knowledge bases. Fully compatible with Deployed Knowledge Base entity. | DeployedKnowledgeBase |  |

## Agent Editor <a id="257918"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/257918)

| version | published | min Mendix |
|---|---|---|
| 2.4.0 | 2026-09-25 | 11.12.4 |
| 2.3.0 | 2026-08-31 | 11.12.3 |
| 2.2.1 | 2026-08-07 | 11.12.2 |
| 2.1.0 | 2026-07-22 | 11.12.1 |
| 2.0.0 | 2026-07-02 | 11.12.0 |
| 1.3.0 | 2026-06-25 | 11.11.0 |
| 1.2.0 | 2026-06-01 | 11.11.0 |
| 1.1.0 | 2026-04-30 | 11.9.1 |
| 1.0.1 | 2026-04-17 | 11.9.1 |
| 1.0.0 | 2026-03-31 | 11.9.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.4.0 | feature | Maia can now set up all building blocks: Models, Knowledge Bases, Consumed MCP Services, microflow tools, and Published MCP Services. | Maia, Models, Knowledge Bases, Consumed MCP Services, Published MCP Services |  |
| 2.4.0 | migration-step | Set checkmark next to register-ai-tools permission in View > Extensions in Studio Pro. | register-ai-tools |  |
| 2.3.0 | feature | New document type 'Published MCP service' lets you configure MCP servers and tools in Studio Pro. Servers start automatically on app startup. | Published MCP service |  |
| 2.2.1 | requirement | Upgrade to Mendix 11.12.2. |  |  |
| 2.2.1 | improvement | Agent Editor now supports response streaming and user permissions configuration for tools and knowledge bases in running app. | Agent Editor |  |
| 2.1.0 | feature | Model documents can now use Microsoft Azure AI Foundry as text generation platform. | Model, Azure AI Foundry |  |
| 2.1.0 | requirement | Mendix Cloud GenAI Connector no longer strictly required; use GenAI Connector or OpenAI Connector depending on Model provider. | Mendix Cloud GenAI Connector, OpenAI Connector |  |
| 2.0.0 | requirement | Agent Editor 2.0.0 requires Studio Pro 11.12. |  |  |
| 2.0.0 | migration-step | Ensure all module dependencies are up to date via Extensions > Agent Editor > Compatibility. |  |  |
| 1.3.0 | breaking | Model document for Mendix Cloud GenAI changed; now displays available model versions in list for selection. | Model, Mendix Cloud GenAI |  |
| 1.3.0 | requirement | Requires Mendix Cloud GenAI Connector version 6.2.0. | Mendix Cloud GenAI Connector |  |
| 1.1.0 | feature | Added support for chat-type agents with conversation-based playground functionality in Studio Pro. | Agent, chat-type agents |  |
| 1.1.0 | feature | Added two new toolbox actions: 'Call Agent with History' and 'New Chat for Agent'. | Call Agent with History, New Chat for Agent |  |

## Agent Registry <a id="202088"></a>
Solution, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/202088)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2026-04-28 | 11.0.0 |

## AI Bot Starter App <a id="227926"></a>
Starter App, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/227926)

| version | published | min Mendix |
|---|---|---|
| 4.6.0 | 2026-05-12 | 10.24.13 |
| 4.5.0 | 2026-04-17 | 10.24.13 |
| 4.4.0 | 2026-02-02 | 10.24.13 |
| 4.3.0 | 2025-12-24 | 10.24.13 |
| 4.2.0 | 2025-11-27 | 10.24.0 |
| 4.1.0 | 2025-10-16 | 10.24.0 |
| 4.0.0 | 2025-08-08 | 10.24.0 |
| 3.1.0 | 2025-04-23 | 10.21.0 |
| 3.0.0 | 2025-04-11 | 10.21.0 |
| 2.1.1 | 2025-02-21 | 10.12.4 |
| 2.1.0 | 2025-02-18 | 10.12.4 |
| 2.0.0 | 2025-01-13 | 10.12.4 |
| 1.4.0 | 2024-10-18 | 10.12.4 |
| 1.3.0 | 2024-09-25 | 10.12.4 |
| 1.2.0 | 2024-08-29 | 10.12.4 |
| 1.1.0 | 2024-08-01 | 10.12.2 |
| 1.0.0 | 2024-06-25 | 10.12.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 4.6.0 | requirement | Marketplace modules upgraded to latest versions. |  |  |
| 4.5.0 | requirement | Marketplace modules upgraded to latest versions. Knowledge base retrievals can be configured visible in chat interface. |  |  |
| 4.4.0 | requirement | Marketplace modules upgraded to latest versions. Gemini connector added to app. | Gemini connector |  |
| 4.3.0 | requirement | Marketplace modules upgraded to latest versions. |  |  |
| 4.3.0 | requirement | Application upgraded to Mendix SP 10.24.13. |  |  |
| 4.3.0 | removal | Dependency required for XSS Sanitization removed from CommunityCommons module. | CommunityCommons |  |
| 4.2.0 | requirement | All marketplace modules updated to latest versions. |  |  |
| 4.2.0 | feature | Traceability capability added to navigation. Traces not stored per default, enable via StoreTraces constant. |  |  |
| 4.2.0 | feature | PDFExtraction module re-added to enable document upload for models not supporting documents natively. | PDFExtraction |  |
| 4.1.0 | requirement | GenAI modules and Encryption upgraded to latest versions. | GenAI modules, Encryption |  |
| 4.0.0 | feature | Application extended to enable multiple knowledge base additions to BotConfig objects. | BotConfig |  |
| 4.0.0 | requirement | All GenAI marketplace assets updated to latest versions. |  |  |
| 4.0.0 | requirement | App upgraded to Mendix Studio Pro version 10.24.0. |  |  |
| 3.1.0 | requirement | Starter App updated to support React Client. |  |  |
| 3.0.0 | requirement | Starter App updated to Mendix Studio Pro 10.21.0. |  |  |
| 3.0.0 | requirement | App contains Amazon Bedrock Connector v7.0.0, GenAI Commons v3.0.0, ConversationalUi v3.0.0, Mx GenAI Connector v3.0.0, OpenAI Connector v5.0.0. | Amazon Bedrock Connector, GenAI Commons, ConversationalUi, Mx GenAI Connector, OpenAI Connector |  |
| 2.1.0 | breaking | Retrieve and Generate logic replaced with new action Tools: Add Mendix Cloud Knowledge Base. | MxCloudGenAI | Tools: Add Mendix Cloud Knowledge Base |
| 2.1.0 | breaking | Fixed bug: Chat conversations based on deactivated Bot Configuration no longer usable. Active configuration selection required before sending message. | Chat conversations |  |
| 2.1.0 | migration-step | Custom existing implementations may need patching. See ChatContext_RemoveOldBotconfigs for handling deactivated Bot Configurations. | ChatContext_RemoveOldBotconfigs |  |
| 2.0.0 | feature | New MxGenAIConnector implemented to power AI Bot including chatting with knowledge base. | MxGenAIConnector |  |
| 2.0.0 | requirement | Marketplace modules updated: Amazon Bedrock Connector 6.0.0, CommunityCommons 10.1.0, Conversational UI 2.0.0, GenAI Commons 2.0.0, OpenAI Connector 4.0.0. | Amazon Bedrock Connector, CommunityCommons, Conversational UI, GenAI Commons, OpenAI Connector |  |
| 1.4.0 | feature | Chat with documents enabled for Amazon Bedrock models. Users can upload up to five documents for model analysis. | Amazon Bedrock |  |
| 1.4.0 | requirement | Marketplace modules updated: GenAI Commons 1.5.0, OpenAI Connector 3.4.1, AWS Authentication Connector 3.2.0, Amazon Bedrock Connector 5.3.0, Conversational UI 1.5.1, CommunityCommons 10.0.7, Encryption 10.0.3, DataWidgets 2.23.0. | GenAI Commons, OpenAI Connector, AWS Authentication Connector, Amazon Bedrock Connector, Conversational UI, CommunityCommons, Encryption, DataWidgets |  |
| 1.3.0 | requirement | GenAI marketplace modules updated: GenAI Commons 1.3.0, OpenAI Connector 3.3.0, AWS Authentication Connector 3.1.3, Amazon Bedrock Connector 5.2.1, Conversational UI 1.4.0. | GenAI Commons, OpenAI Connector, AWS Authentication Connector, Amazon Bedrock Connector, Conversational UI |  |
| 1.2.0 | requirement | GenAI marketplace modules updated: GenAI Commons 1.2.0, OpenAI Connector 3.2.0, AWS Authentication Connector 3.1.2, Amazon Bedrock Connector 5.2.0, Conversational UI 1.3.0. | GenAI Commons, OpenAI Connector, AWS Authentication Connector, Amazon Bedrock Connector, Conversational UI |  |
| 1.2.0 | requirement | Studio Pro version upgraded to 10.12.4. |  |  |
| 1.1.0 | requirement | GenAI marketplace modules updated: GenAI Commons 1.1.0, OpenAI Connector 3.1.1, AWS Authentication Connector 3.1.1, Amazon Bedrock Connector 5.0.1, Conversational UI 1.2.1. | GenAI Commons, OpenAI Connector, AWS Authentication Connector, Amazon Bedrock Connector, Conversational UI |  |
| 1.1.0 | requirement | Studio Pro version upgraded to 10.12.2. |  |  |

## Aircraft Fleet Retrofit Planning <a id="208719"></a>
Industry Template, TOCnDix, Partner, [marketplace](https://marketplace.mendix.com/link/component/208719)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2023-03-22 | ? |

## Amazon Bedrock Connector <a id="215042"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/215042)

| version | published | min Mendix |
|---|---|---|
| 11.2.0 | 2026-09-07 | 11.12.3 |
| 11.1.0 | 2026-07-22 | 11.12.1 |
| 11.0.0 | 2026-07-02 | 11.12.0 |
| 10.1.0 | 2026-03-27 | 10.24.13 |
| 10.0.2 | 2026-03-18 | 10.24.13 |
| 10.0.1 | 2026-03-10 | 10.24.13 |
| 9.4.0 | 2026-01-19 | 10.24.13 |
| 9.3.0 | 2025-12-22 | 10.24.13 |
| 9.2.1 | 2025-11-25 | 10.24.0 |
| 9.2.0 | 2025-08-29 | 10.24.0 |
| 9.1.0 | 2025-08-13 | 10.24.0 |
| 9.0.0 | 2025-08-08 | 10.24.0 |
| 8.3.0 | 2025-07-21 | 10.21.0 |
| 8.2.0 | 2025-07-02 | 10.21.0 |
| 8.1.0 | 2025-06-24 | 10.21.0 |
| 8.0.1 | 2025-06-17 | 10.21.0 |
| 8.0.0 | 2025-06-13 | 10.21.0 |
| 7.0.0 | 2025-04-07 | 10.21.0 |
| 6.3.0 | 2025-04-01 | 9.24.2 |
| 6.2.1 | 2025-03-13 | 9.24.2 |
| 6.2.0 | 2025-03-12 | 9.24.2 |
| 6.1.0 | 2025-02-14 | 9.24.2 |
| 6.0.0 | 2025-01-13 | 9.24.2 |
| 5.4.0 | 2024-11-28 | 9.24.2 |
| 5.3.2 | 2024-10-23 | 9.24.2 |
| 5.3.1 | 2024-10-22 | 9.24.2 |
| 5.3.0 | 2024-09-27 | 9.24.2 |
| 5.2.1 | 2024-09-04 | 9.24.2 |
| 5.2.0 | 2024-08-28 | 9.24.2 |
| 5.1.0 | 2024-08-22 | 9.24.2 |
| 5.0.1 | 2024-08-01 | 9.24.2 |
| 5.0.0 | 2024-07-30 | 9.24.2 |
| 4.0.0 | 2024-07-25 | 9.24.2 |
| 2.3.0 | 2024-03-14 | 9.18.0 |
| 2.2.0 | 2024-03-05 | 9.18.0 |
| 2.1.3 | 2024-02-09 | 9.18.0 |
| 2.1.2 | 2024-02-07 | 9.18.0 |
| 2.1.0 | 2024-01-29 | 9.18.0 |
| 2.0.0 | 2023-12-18 | 9.18.0 |
| 1.0.3 | 2023-10-16 | 9.18.0 |
| … 2 older versions | | |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 11.2.0 | requirement | Upgrade to Mendix 11.12.3. |  |  |
| 11.1.0 | requirement | Upgrade to Mendix 11.12.1. |  |  |
| 11.1.0 | fix | Bug fixed: tool choice 'tool' now applied correctly in multi-turn conversations. |  |  |
| 11.0.0 | requirement | Module upgraded to Mendix 11.12. |  |  |
| 11.0.0 | removal | Removed support for Embeddings generation with Titan models. Cohere Embeddings models support remains. | Titan models |  |
| 11.0.0 | breaking | GetCredentials microflow redesigned. Sync operations now expect Credentials object as input to allow more credential types. | GetCredentials, AmazonBedrockAgent_Sync, BedrockDeployedModel_Sync, AmazonBedrockKnowledgeBase_Sync, BedrockDeployedModel_KnowledgeBase_Agent_SyncAll |  |
| 11.0.0 | migration-step | To use Credentials object in operations (optional): associate Credentials object to ChatCompletionsRequest_Extension, CohereEmbedOptions_Extension, TitanImageOptions_Extension, RetrieveRequest_Extension, or RetrieveAndGenerateRequest_Extension. | ChatCompletionsRequest_Extension, CohereEmbedOptions_Extension, TitanImageOptions_Extension, RetrieveRequest_Extension, RetrieveAndGenerateRequest_Extension |  |
| 11.0.0 | removal | Data migration microflows from previous major version removed. For multi-major-version upgrades, consult migration guide. |  |  |
| 10.0.2 | fix | Bug fixed: tool inputs left empty causing repetitive tool calling. |  |  |
| 10.0.1 | breaking | Module aligned with latest ConsumedKnowledgeBase and ConsumedMCPService changes. Breaking change requiring migration. | ConsumedKnowledgeBase, ConsumedMCPService |  |
| 10.0.1 | improvement | Internal error handling changed so error passed to GenAI Commons operations for chat completions. |  |  |
| 10.0.1 | requirement | Module version compatible with GenAI Commons 6.0.0 version. | GenAI Commons |  |
| 9.4.0 | requirement | Module now compatible with latest GenAI Commons version. | GenAI Commons |  |
| 9.3.0 | requirement | Module upgraded to Mendix LTS version 10.24.13. |  |  |
| 9.2.1 | fix | Bug fixed: displayed Bedrock models now update after region change. |  |  |
| 9.2.0 | requirement | Module updated compatible with AWS Authentication 4.1.1, which introduces mx-central-1 (Mexico Central) region. | AWS Authentication |  |
| 9.1.0 | improvement | Tool calling: GenAICommons ArgumentInput objects mapped to Bedrock API expected input schema for MCP Client use cases. | GenAICommons ArgumentInput |  |
| 9.0.0 | requirement | Module upgraded to Mendix Studio Pro version 10.24. |  |  |
| 8.3.0 | requirement | Connector compatible with newest GenAI Commons version. Tool microflows accept multiple primitive input parameters of various types. | GenAI Commons |  |
| 8.1.0 | improvement | Minor entity access changes (AmazonBedrockKnowledgeBase) support agent configuration at runtime using AgentCommons. | AmazonBedrockKnowledgeBase |  |
| 8.0.0 | breaking | AmazonBedrockKnowledgeBase inherits from new DeployedKnowledgeBase entity. Re-sync Bedrock configurations. | AmazonBedrockKnowledgeBase |  |
| 8.0.0 | breaking | Retrieve and Generate operations now use AmazonBedrockKnowledgeBase as input. | Retrieve and Generate |  |
| 8.0.0 | improvement | New _ID entity for sessions now used for Retrieve and Generate operations. |  |  |
| 7.0.0 | requirement | Module updated to Mendix Studio Pro 10.21.0. |  |  |
| 6.1.0 | improvement | Function microflows updated to accept 'Tool' and/or 'Request' as optional input parameters. |  |  |
| 6.1.0 | fix | Function calling bug for microflows without input parameters fixed. |  |  |
| 6.0.0 | breaking | Connector made compatible with simplified GenAI Commons toolbox. Chat Completions, Embeddings, Image Generation moved to GenAI Commons operations. Pass DeployedModel instead of Connection object. | Chat Completions, Embeddings, Image Generation |  |
| 6.0.0 | migration-step | Sync new Deployed Models in UI using SNIP_Settings_Admin_MetaDataOverview on custom page. | Deployed Models |  |
| 6.0.0 | migration-step | Replace Amazon Bedrock operations in custom microflows with GenAI Commons equivalent operations from Toolbox. |  |  |
| 6.0.0 | migration-step | New operations require DeployedModel input; for Bedrock use BedrockDeployedModel type. | BedrockDeployedModel |  |
| 5.3.0 | requirement | Amazon Bedrock Connector updated to Mendix version 9.24.2. |  |  |
| 5.3.0 | requirement | Bedrock SDK updated to version 2.27.17 to align with AWS Authentication 3.2.0 SDK version. |  |  |
| 5.3.0 | improvement | Some jar files centralized to AWS Authentication connector. |  |  |
| 5.2.0 | requirement | Compatibility with latest GenAICommons version: FileContent.FileExtension instead of MediaType enumeration. | GenAICommons |  |
| 5.0.1 | fix | Bug fixed: error for Retrieve/Retrieve and Generate/Invoke Agent with non-S3 knowledge base datasources in Mendix 10. |  |  |
| 5.0.0 | fix | Bug fixed: using knowledge base with non-S3 datasource no longer causes error. Non-S3 datasources not fully supported. |  |  |
| 5.0.0 | requirement | Retrieve operation now depends on GenAICommons module. | GenAICommons |  |
| 4.0.0 | feature | Operations added depending on GenAICommons to generate embeddings. | GenAICommons |  |
| 4.0.0 | feature | Logic added depending on GenAICommons to generate images with Amazon Titan. | GenAICommons |  |
| 4.0.0 | breaking | ChatCompletions: invokeModel call replaced with Converse API call. | ChatCompletions |  |
| 2.0.0 | requirement | Connector updated to work with Authentication Connector 3.0 and newer versions | Authentication Connector |  |

## Amazon Bedrock Showcase App <a id="223535"></a>
Service, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/223535)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2024-09-11 | 9.24.2 |

## Amazon Cognito <a id="207106"></a>
Service, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/207106)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2023-03-06 | 9.0.5 |

## Amazon Cognito Connector <a id="203363"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/203363)

| version | published | min Mendix |
|---|---|---|
| 2.0.0 | 2023-03-24 | 9.14.0 |
| 1.0.2 | 2023-01-16 | 9.13.0 |
| 1.0.0 | 2022-11-02 | 9.13.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.0.0 | removal | AWS Services module dependency removed. | AWS Services module | AWSAuthentication module |
| 2.0.0 | removal | AWS Services module related .Jar files removed. | AWS Services module .Jar files |  |
| 2.0.0 | requirement | AWSAuthentication module is now required as a dependency. | AWSAuthentication module |  |
| 2.0.0 | requirement | Cognito related .Jar files now included with the module. | Cognito related .Jar files |  |
| 2.0.0 | breaking | Static credentials storage in AWS Services module removed. Update breaks existing AWS credentials configuration. | AWS credentials configuration, Static credentials storage |  |
| 2.0.0 | feature | App configuration extended with credential choice (Static/Session) and storage capability. | App configuration |  |
| 2.0.0 | migration-step | Reconfigure AWS credentials following documentation guidance due to breaking changes. | AWS credentials configuration |  |

## Amazon DynamoDB Connector <a id="204872"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/204872)

| version | published | min Mendix |
|---|---|---|
| 3.2.1 | 2026-02-23 | 10.21.0 |
| 3.1.0 | 2025-07-24 | 10.21.0 |
| 3.0.0 | 2025-04-24 | 10.21.0 |
| 2.1.0 | 2024-09-27 | 9.24.2 |
| 2.0.1 | 2024-03-06 | 9.18.0 |
| 1.0.3 | 2024-01-24 | 9.18.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 3.0.0 | requirement | Upgraded to Mx version 10.21.0 |  |  |
| 3.0.0 | breaking | All third party jar dependencies are now configured in module itself and removed from user lib | third party jar dependencies |  |
| 2.1.0 | requirement | Upgraded to Mendix version 9.24.2 |  |  |
| 2.1.0 | requirement | Upgraded sdk to version 2.27.17 to align with AWS Authentication Connector 3.2.0 | AWS SDK |  |
| 1.0.3 | migration-step | Added migration file for Mendix 10.3+ to rebuild dependencies with Java Dependency Management | dependencies |  |

## Amazon EventBridge Connector <a id="208548"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/208548)

| version | published | min Mendix |
|---|---|---|
| 3.0.1 | 2026-02-23 | 10.21.0 |
| 2.1.0 | 2024-09-27 | 9.24.2 |
| 2.0.1 | 2023-12-19 | 9.18.0 |
| 1.0.1 | 2023-10-13 | 9.18.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 3.0.1 | requirement | Upgraded to Mendix version 10.21.0 (minimum requirement). |  |  |
| 3.0.1 | migration-step | All third-party JAR dependencies now configured in module itself; removed from user lib. |  |  |
| 2.1.0 | requirement | Updated to Mendix version 9.24.2 (minimum requirement). |  |  |
| 2.1.0 | improvement | EventBridge SDK updated to version 2.27.17 to align with AWS Authentication 3.2.0. | EventBridge SDK |  |
| 2.1.0 | migration-step | Some JAR files centralized to AWS Authentication Connector. | AWS Authentication Connector |  |
| 2.1.0 | improvement | Improved handling of enumerations. |  |  |
| 2.0.1 | requirement | Module now compatible with AWS Authentication Connector version 3.0.0. | AWS Authentication Connector |  |

## Amazon Location Service Connector <a id="209124"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/209124)

| version | published | min Mendix |
|---|---|---|
| 3.0.1 | 2026-02-19 | 10.21.0 |
| 2.1.0 | 2024-09-27 | 9.24.2 |
| 2.0.1 | 2024-09-19 | 9.18.0 |
| 1.0.1 | 2024-07-10 | 9.18.0 |
| 1.0.0 | 2023-04-12 | 9.18.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 3.0.1 | requirement | Upgraded to Mendix version 10.21.0. Minimum Mendix version is now 10.21.0. | Mendix |  |
| 3.0.1 | migration-step | All third party jar dependencies are now configured in the module itself and have been removed from the user lib. Remove jar files from user lib. | third party jar dependencies |  |
| 2.1.0 | requirement | Upgraded to Mendix version 9.24.2. Minimum Mendix version is now 9.24.2. | Mendix |  |
| 2.1.0 | improvement | Upgraded Amazon Location Service Connector SDK to version 2.27.17 to align with AWS Authentication Connector. | Amazon Location Service SDK, AWS Authentication Connector |  |
| 2.0.1 | fix | Removed duplicated jars with AWS Authentication Connector. | AWS Authentication Connector |  |

## Amazon Polly Connector <a id="205068"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/205068)

| version | published | min Mendix |
|---|---|---|
| 3.0.1 | 2026-02-23 | 10.21.0 |
| 2.1.0 | 2024-09-27 | 9.24.2 |
| 2.0.0 | 2023-12-18 | 9.18.0 |
| 1.1.2 | 2023-08-04 | 9.18.0 |
| 1.0.1 | 2022-11-29 | 9.18.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 3.0.1 | requirement | Upgraded to Mendix version 10.21.0. Minimum Mendix version is now 10.21.0. |  |  |
| 3.0.1 | breaking | All third party jar dependencies are now configured in the module itself and have been removed from user lib. |  |  |
| 2.1.0 | requirement | Amazon Polly Connector upgraded to Mendix version 9.24.2. Minimum Mendix version is now 9.24.2. |  |  |
| 2.1.0 | improvement | SDK upgraded to version 2.27.17 to align with AWS Authentication version 3.2.0. |  |  |
| 2.0.0 | requirement | Connector updated to work with Authentication Connector 3.0 and newer versions. | Authentication Connector |  |
| 1.0.1 | fix | Updated userlibs to contain the right dependencies. |  |  |

## Amazon Polly Example Implementation <a id="213229"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/213229)

| version | published | min Mendix |
|---|---|---|
| 3.0.0 | 2025-05-26 | 10.21.0 |
| 2.1.0 | 2024-09-27 | 9.24.2 |
| 2.0.0 | 2024-01-10 | 9.18.0 |
| 1.0.0 | 2023-07-12 | 9.18.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 3.0.0 | removal | Remove dependency on module PlayAudio | PlayAudio |  |
| 3.0.0 | requirement | Update dependency Mendix 9.24.2 to Mendix Studio Pro 10.21.0 or higher | Mendix Studio Pro |  |
| 3.0.0 | breaking | Remove the text '[optional]' as the dependencies are not optional |  |  |
| 3.0.0 | migration-step | Configure AWS credentials for AWS Authentication Connector in Configuration section step 4 | AWS Authentication Connector |  |
| 3.0.0 | requirement | Updated to Studio Pro version 10.21 | Studio Pro |  |
| 2.1.0 | requirement | Upgraded to Mendix version 9.24.2 for compatibility with latest Amazon Polly Connector | Mendix |  |
| 2.0.0 | requirement | Compatible with Amazon Polly Connector 2.0.0 and Amazon Authentication Connector 3.0.0 | Amazon Polly Connector, Amazon Authentication Connector |  |

## Amazon RDS <a id="206672"></a>
Service, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/206672)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2023-02-03 | ? |

## Amazon Rekognition Connector <a id="204717"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/204717)

| version | published | min Mendix |
|---|---|---|
| 3.0.1 | 2026-02-19 | 10.21.0 |
| 2.0.0 | 2023-12-18 | 9.18.0 |
| 1.2.2 | 2023-08-01 | 9.18.0 |
| 1.1.0 | 2022-12-19 | 9.12.2 |
| 1.0.1 | 2022-11-24 | 9.12.2 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 3.0.1 | requirement | Minimum Mendix version raised to 10.21.0 |  |  |
| 3.0.1 | migration-step | All third party jar dependencies now configured in module; remove them from user lib |  |  |
| 2.0.0 | requirement | Connector requires Authentication Connector 3.0 or newer versions | Authentication Connector |  |
| 1.1.0 | fix | Fixed 400 bad request issue for authentication through session-based credentials |  |  |
| 1.0.1 | fix | Fixed issue that occurred when using the latest version of AWSAuthentication | AWSAuthentication |  |

## Amazon S3 Connector <a id="120340"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/120340)

| version | published | min Mendix |
|---|---|---|
| 5.2.0 | 2026-04-28 | 10.21.0 |
| 5.1.0 | 2026-02-12 | 10.21.0 |
| 5.0.2 | 2025-11-06 | 10.21.0 |
| 4.2.1 | 2025-04-09 | 9.24.2 |
| 4.1.0 | 2024-09-27 | 9.24.2 |
| 4.0.1 | 2024-08-08 | 9.18.0 |
| 3.1.0 | 2024-07-23 | 9.18.0 |
| 3.0.0 | 2024-03-08 | 9.18.0 |
| 2.0.2 | 2024-01-23 | 9.18.0 |
| 1.1.1 | 2023-04-07 | 9.18.0 |
| 1.0.1 | 2022-09-15 | 9.12.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 5.2.0 | breaking | Client-side encryption upgraded to AWS V4 algorithm; not backwards compatible with V3 encryption. Check AWS documentation for migration scenarios. | client-side encryption |  |
| 5.2.0 | fix | Bugfix in client-side encryption when using AWS temporary credentials. | client-side encryption, AWS temporary credentials |  |
| 5.2.0 | security | Fixed vulnerabilities in dependencies of client-side encryption. | client-side encryption dependencies |  |
| 5.1.0 | feature | Created ClientsideEncryptionConfig object that enables KMS Clientside Encryption for S3 files. | ClientsideEncryptionConfig |  |
| 5.1.0 | improvement | GetObject updated to look for ClientsideEncryptionConfig and use KMS encryption if it exists. | GetObject |  |
| 5.1.0 | improvement | PutObject updated to look for ClientsideEncryptionConfig and use KMS encryption if it exists. | PutObject |  |
| 5.0.2 | breaking | Renamed HeadObject caption in Toolbox from "Head Bucket" to "Head Object". | HeadObject |  |
| 5.0.2 | fix | Bug fix: file reading from Mendix core API now uses BufferedInputStream for better retry and buffering support. | file reading |  |
| 5.0.2 | requirement | Upgraded to Mendix version 10.21.0. | Mendix |  |
| 5.0.2 | migration-step | Third party jar dependencies now configured in module; removed from user lib. Manual cleanup of user lib required. | jar dependencies |  |
| 4.2.1 | improvement | HeadBucket action updated to use up-to-date AWS regions from Authentication module. | HeadBucket, Authentication module |  |
| 4.1.0 | improvement | Upgraded S3 SDK to version 2.27.17. | S3 SDK |  |
| 4.0.1 | migration-step | Migration file added for Mendix 10 support. | Mendix 10 |  |
| 3.1.0 | feature | Added HeadBucket operation. | HeadBucket |  |
| 3.0.0 | breaking | Connector updated to work with Authentication Connector 3.0+. Region must be specified as input for CreateBucket. | Authentication Connector, CreateBucket |  |
| 2.0.2 | migration-step | Migration file added for Mendix 10.3+ to rebuild dependencies with Mendix Java Dependency Management feature. | Mendix 10.3+, Java Dependency Management |  |
| 1.1.1 | requirement | Module upgraded to Mendix Studio Pro 9.18.0. | Mendix Studio Pro |  |
| 1.1.1 | improvement | Upgraded json-smart Java library from version 2.4.8 to 2.4.10. | json-smart |  |
| 1.0.1 | security | Security fix: updated userlib and removed unused jar files. | userlib |  |

## Amazon SageMaker AI <a id="215041"></a>
Service, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/215041)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2023-10-03 | 9.18.0 |

## Amazon SES <a id="206104"></a>
Service, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/206104)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2023-01-05 | 8.18.22 |

## Amazon SNS Connector <a id="204715"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/204715)

| version | published | min Mendix |
|---|---|---|
| 4.0.1 | 2026-02-19 | 10.21.0 |
| 3.1.0 | 2024-09-27 | 9.24.2 |
| 3.0.0 | 2023-12-18 | 9.18.0 |
| 2.0.2 | 2023-10-13 | 9.18.0 |
| 1.0.0 | 2022-11-24 | 9.18.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 4.0.1 | requirement | Upgraded to Mendix version 10.21.0 | Mendix |  |
| 4.0.1 | migration-step | All third party (jar) dependencies now configured in module; removed from user lib |  |  |
| 3.1.0 | improvement | Upgraded SNS SDK to 2.27.17 | SNS SDK |  |
| 3.0.0 | requirement | Updated to work with Authentication Connector 3.0 and newer versions | Authentication Connector |  |
| 1.0.0 | deprecation | Version 1.0.0 is deprecated |  |  |

## Amazon SQS Connector <a id="112424"></a>
Module, Ciphix, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/112424)

| version | published | min Mendix |
|---|---|---|
| 1.1.1 | 2026-02-09 | 10.24.1 |
| 1.1.0 | 2021-08-13 | 8.17.0 |
| 1.0.0 | 2020-01-08 | 8.4.2 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.1.1 | deprecation | Component still deprecated; use version from Mendix instead. | Amazon SQS Connector | Mendix Amazon SQS Connector |
| 1.1.1 | fix | One time fix for use in Mx11. | Amazon SQS Connector |  |
| 1.1.0 | requirement | Updated to Mx 8.17 for Mx 9 compatibility with new AWS dependency versions. | Mendix, AWS dependencies |  |

## Amazon SQS Connector <a id="214699"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/214699)

| version | published | min Mendix |
|---|---|---|
| 3.0.1 | 2026-02-23 | 10.21.0 |
| 2.1.1 | 2025-04-22 | 9.24.2 |
| 2.0.0 | 2023-12-18 | 9.18.0 |
| 1.0.0 | 2023-08-10 | 9.18.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 3.0.1 | requirement | Upgraded to Mendix version 10.21.0 (minimum requirement). |  |  |
| 3.0.1 | migration-step | All third party JAR dependencies now configured in module itself; removed from user lib. |  |  |
| 2.1.1 | fix | Removed semicolon from Java code that resulted in errors for some users. |  |  |
| 2.0.0 | requirement | Connector updated to work with Authentication Connector 3.0 and newer versions. | Authentication Connector |  |

## Amazon Textract Connector <a id="205646"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/205646)

| version | published | min Mendix |
|---|---|---|
| 3.0.1 | 2025-09-15 | 10.21.0 |
| 2.1.0 | 2024-09-27 | 9.24.2 |
| 2.0.0 | 2023-12-18 | 9.18.0 |
| 1.2.2 | 2023-11-27 | 9.18.0 |
| 1.0.3 | 2023-08-15 | 9.18.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 3.0.1 | requirement | Upgraded to Mendix version 10.21.0 | Mendix |  |
| 3.0.1 | breaking | All third party jar dependencies now configured in module and removed from user lib | jar dependencies |  |
| 2.1.0 | requirement | Updated to Mendix version 9.24.2 | Mendix |  |
| 2.1.0 | improvement | Textract SDK updated to version 2.27.17 to align with AWS Authentication modules SDK version | textract sdk |  |
| 2.1.0 | migration-step | Some jar files centralized to AWS Authentication connector | jar files, AWS Authentication connector |  |
| 2.1.0 | improvement | Improved handling of enumerations introduced | enumerations |  |
| 2.0.0 | breaking | Connector updated to work with Authentication Connector 3.0 and newer versions | Authentication Connector |  |
| 1.2.2 | feature | New actions available to work with multipage documents |  |  |

## Amazon Translate Connector <a id="204706"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/204706)

| version | published | min Mendix |
|---|---|---|
| 3.1.1 | 2026-02-19 | 10.21.0 |
| 3.0.0 | 2025-04-24 | 10.21.0 |
| 2.1.0 | 2024-09-27 | 9.24.2 |
| 2.0.0 | 2024-03-08 | 9.18.0 |
| 1.0.3 | 2024-01-23 | 9.18.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 3.0.0 | requirement | Upgraded to Mendix version 10.21.0. Minimum Mendix version is now 10.21.0. |  |  |
| 3.0.0 | migration-step | All third party jar dependencies now configured in module itself and removed from user lib. Update your setup accordingly. |  |  |
| 2.1.0 | improvement | Upgraded Translate SDK to 2.27.17. | Translate SDK |  |
| 2.0.0 | requirement | Connector updated to work with Authentication Connector 3.0 and newer versions. | Authentication Connector |  |
| 1.0.3 | migration-step | Migration file added for Mendix 10.3+ to rebuild dependencies with Mendix Java Dependency Management. |  |  |

## Amorph.pro SMARTUNIFIER <a id="208936"></a>
Service, Amorphsys, Partner, [marketplace](https://marketplace.mendix.com/link/component/208936)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2023-03-27 | 9.20.0 |

## Anonymous account activation <a id="120301"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/120301)

| version | published | min Mendix |
|---|---|---|
| 1.0.1 | 2022-06-09 | 9.12.1 |
| 1.0.0 | 2022-05-11 | 9.12.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.0.1 | breaking | Removed dependency on Administration.Account. | Administration.Account |  |

## Antd Date Picker <a id="207912"></a>
Widget, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/207912)

| version | published | min Mendix |
|---|---|---|
| 1.2.0 | 2023-11-14 | 9.0.5 |
| 1.0.0 | 2023-03-02 | 9.0.5 |

## Antd Date Range Picker <a id="207911"></a>
Widget, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/207911)

| version | published | min Mendix |
|---|---|---|
| 1.0.3 | 2023-03-02 | 9.0.5 |
| 1.0.0 | 2023-03-02 | 9.0.5 |

## Antd Dropdown Menu <a id="210812"></a>
Widget, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/210812)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2023-05-15 | 9.0.5 |

## Antd Icon <a id="210819"></a>
Widget, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/210819)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2023-05-15 | 9.0.5 |

## AnyChart <a id="106517"></a>
Module, Mendix, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/106517)

| version | published | min Mendix |
|---|---|---|
| 3.0.4 | 2024-10-21 | 9.18.4 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 3.0.4 | fix | Fixed relative path to avoid importing issues when application root URL is not base domain. |  |  |
| 3.0.4 | improvement | Updated plotly to version 2.35.2. | plotly |  |

## Apex Charts <a id="220921"></a>
Service, Kinetech, Partner, [marketplace](https://marketplace.mendix.com/link/component/220921)

| version | published | min Mendix |
|---|---|---|
| 2.1.0 | 2024-05-03 | 9.6.12 |
| 1.0.1 | 2024-02-09 | 9.6.12 |
| 1.0.0 | 2024-01-15 | 9.6.12 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.0.1 | fix | Adding handlers for NULL values in Combo and Dynamic widgets so that data labels are not displayed as NaN | Combo, Dynamic |  |

## Approval App <a id="117472"></a>
Starter App, Mendix, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/117472)

| version | published | min Mendix |
|---|---|---|
| 2.3.1 | 2022-12-12 | 9.20.0 |
| 2.3.0 | 2022-11-03 | 9.19.0 |
| 2.2.10 | 2023-01-11 | 9.18.0 |
| 2.2.8 | 2022-09-05 | 9.17.0 |
| 2.2.7 | 2022-08-24 | 9.16.1 |
| 2.2.6 | 2022-07-29 | 9.16.0 |
| 2.2.4 | 2022-07-19 | 9.15.1 |
| 2.2.3 | 2022-07-06 | 9.15.0 |
| 2.2.2 | 2022-06-20 | 9.14.1 |
| 2.2.1 | 2022-06-16 | 9.14.1 |
| 2.2.0 | 2022-06-14 | 9.14.0 |
| 2.1.0 | 2022-05-06 | 9.13.0 |
| 2.0.0 | 2022-04-14 | 9.12.1 |
| 1.4.1 | 2021-09-17 | 9.5.1 |
| 1.4.0 | 2021-09-13 | 9.5.0 |
| 1.3.1 | 2021-08-26 | 9.4.0 |
| 1.3.0 | 2021-08-24 | 9.4.0 |
| 1.2.0 | 2021-06-30 | 9.3.0 |
| 1.1.0 | 2021-05-28 | 9.2.0 |
| 1.0.1 | 2021-05-07 | 9.1.1 |
| 1.0.0 | 2021-05-06 | 9.1.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.3.1 | requirement | Add support for Mendix 9.20 | Mendix |  |
| 2.3.0 | requirement | Add support for Mendix 9.19 | Mendix |  |
| 2.2.10 | requirement | Support for Mendix 9.18 | Mendix |  |
| 2.2.8 | requirement | Add support for Mendix 9.17.0 | Mendix |  |
| 2.2.7 | requirement | Add support for Mendix 9.16.1 | Mendix |  |
| 2.2.6 | requirement | Add support for Mendix 9.16.0 | Mendix |  |
| 2.2.4 | requirement | Add support for Mendix 9.15.1 | Mendix |  |
| 2.2.3 | requirement | Add support for Mendix 9.15.0 | Mendix |  |
| 2.2.2 | requirement | Add support for Mendix 9.14.1 | Mendix |  |
| 2.2.2 | removal | Remove example workflow | example workflow |  |
| 2.2.1 | requirement | Add support for Mendix 9.14.1 | Mendix |  |
| 2.2.0 | requirement | Add support for Mendix 9.14 | Mendix |  |
| 2.1.0 | requirement | Added Mendix 9.13.0 support | Mendix |  |
| 2.0.0 | requirement | Mx 9.12.1 support | Mendix |  |
| 1.4.1 | requirement | Mx 9.5.1 support | Mendix |  |
| 1.4.0 | requirement | Add support for Mx9.5 | Mendix |  |
| 1.3.0 | requirement | Add version for Mx9.4 | Mendix |  |
| 1.2.0 | requirement | Updated for Mendix 9.3.0 and WorkflowCommons 1.2.1 | Mendix, WorkflowCommons |  |
| 1.1.0 | requirement | Updated to Mendix 9.2.0 | Mendix |  |
| 1.0.1 | removal | Removed the Users navigation item | Users navigation item |  |

## ArcGIS - Demo Project (DEPRECATED) <a id="106095"></a>
Module, Valcon, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/106095)

| version | published | min Mendix |
|---|---|---|
| 2.1.0 | 2021-02-12 | 8.6.4 |
| 1.2.0 | 2020-07-24 | 8.6.4 |
| 1.1.1 | 2020-07-24 | 7.23.14 |
| 1.1.0 | 2018-08-12 | 7.13.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.1.0 | migration-step | ProRail stations layer index upgraded due to featurelayer move and rename. | ProRail stations layer |  |
| 1.2.0 | requirement | Upgraded to Mendix 8.6.4 minimum requirement. | Mendix |  |
| 1.2.0 | improvement | Upgraded to Atlas_UI. | Atlas_UI |  |
| 1.2.0 | removal | Removed AppCloudServices module. | AppCloudServices |  |
| 1.1.1 | requirement | Upgraded to Mendix 7.23.14 minimum requirement. | Mendix |  |
| 1.1.1 | migration-step | Upgraded Stations layer due to URL change. | Stations layer |  |
| 1.1.0 | requirement | Upgraded project to Mendix 7.13.1 minimum requirement. | Mendix |  |
| 1.1.0 | improvement | Included widget version 1.1.1. | widget |  |

## ArcGIS Widget (DEPRECATED) <a id="106094"></a>
Widget, Valcon, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/106094)

| version | published | min Mendix |
|---|---|---|
| 1.3.0 | 2020-07-24 | 8.6.4 |
| 1.2.2 | 2019-08-04 | 7.23.6 |
| 1.2.1 | 2019-01-30 | 7.22.2 |
| 1.2.0 | 2018-12-13 | 7.16.0 |
| 1.1.1 | 2018-08-12 | 7.13.1 |
| 1.1.0 | 2018-08-11 | 7.13.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.3.0 | requirement | Upgraded to Mendix 8.6.4 |  |  |
| 1.2.1 | migration-step | Changed relative path for dojox folders to ArcGIS/lib/dojox due to Mendix 7.22 removal | dojox folders |  |
| 1.1.0 | fix | Change in lib/esri/kernel.js file | lib/esri/kernel.js |  |
| 1.1.0 | fix | Introduced relative paths for all libraries to prevent Mendix 7 retrieving from clientsystem |  |  |
| 1.1.0 | breaking | Removed deprecated store.caller, changed to origin | store.caller | origin |

## Asset Manager App <a id="69674"></a>
Sample, Mendix, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/69674)

| version | published | min Mendix |
|---|---|---|
| 3.12.10 | 2020-10-27 | 8.14.0 |
| 3.12.9 | 2020-09-30 | 8.14.0 |
| 3.12.8 | 2020-09-29 | 8.14.0 |
| 3.12.7 | 2020-09-11 | 8.13.1 |
| 3.12.6 | 2020-07-28 | 8.12.0 |
| 3.12.5 | 2020-07-28 | 8.12.0 |
| 3.12.4 | 2020-07-07 | 8.11.0 |
| 3.12.3 | 2020-07-07 | 8.11.0 |
| 3.12.2 | 2020-05-27 | 8.10.0 |
| 3.12.1 | 2020-05-06 | 8.9.0 |
| 3.12.0 | 2020-04-30 | 8.9.0 |
| 3.11.3 | 2020-04-17 | 8.8.1 |
| 3.11.2 | 2020-04-14 | 8.8.1 |
| 3.11.1 | 2020-04-01 | 8.8.0 |
| 3.11.0 | 2020-03-16 | 8.7.0 |
| 3.10.17 | 2020-03-16 | 7.23.12 |
| 3.10.16 | 2020-03-04 | 8.7.0 |
| 3.10.15 | 2020-03-04 | 8.7.0 |
| 3.10.14 | 2020-03-03 | 8.7.0 |
| 3.10.13 | 2020-03-03 | 8.7.0 |
| 3.10.12 | 2020-03-02 | 8.7.0 |
| 3.10.11 | 2020-02-27 | 8.7.0 |
| 3.10.10 | 2020-02-27 | 8.7.0 |
| 3.10.9 | 2020-02-10 | 8.6.0 |
| 3.10.8 | 2020-02-07 | 8.6.0 |
| 3.10.7 | 2020-02-06 | 8.6.0 |
| 3.10.6 | 2020-02-05 | 8.6.0 |
| 3.10.5 | 2019-12-20 | 8.5.0 |
| 3.10.4 | 2019-12-12 | 8.4.2 |
| 3.10.3 | 2019-11-28 | 8.4.1 |
| 3.10.2 | 2019-11-27 | 8.4.0 |
| 3.10.1 | 2019-11-27 | 8.4.0 |
| 3.10.0 | 2019-11-26 | 8.4.0 |
| 3.9.23 | 2019-10-30 | 8.3.0 |
| 3.9.22 | 2019-10-29 | 8.3.0 |
| 3.9.21 | 2019-10-29 | 8.3.0 |
| 3.9.20 | 2019-10-17 | 8.2.2 |
| 3.9.19 | 2019-10-16 | 8.2.2 |
| 3.9.18 | 2019-09-12 | 8.1.1 |
| 3.9.17 | 2019-09-10 | 8.1.1 |
| … 48 older versions | | |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 3.11.3 | requirement | Update Mendix Feedback Widget to version 8.2.1 | Mendix Feedback Widget |  |
| 3.9.12 | improvement | Updated feedback widget | feedback widget |  |
| 3.9.7 | requirement | Converted to 7.23.3 |  |  |
| 3.9.5 | requirement | Converted to 7.23.2 |  |  |
| 3.9.4 | requirement | Converted to v7.23.1 |  |  |
| 3.9.4 | requirement | Updated Atlas Resources to v1.2.4 | Atlas Resources |  |
| 3.9.3 | requirement | Converted to 7.22.2 |  |  |
| 3.9.2 | requirement | Converted to 7.22.1 |  |  |
| 3.9.1 | requirement | Converted to 7.22.0 |  |  |
| 3.9.0 | requirement | Updated Atlas Resources to v1.2.2 | Atlas Resources |  |
| 3.8.4 | requirement | Upgraded to 7.20.0 |  |  |
| 3.8.3 | requirement | Upgraded to 7.19.0 |  |  |
| 3.8.2 | requirement | Upgraded to 7.18.1 |  |  |
| 3.8.1 | requirement | Upgrade to 7.17.2 |  |  |
| 3.8.0 | requirement | Upgrade to 7.17.0 |  |  |
| 3.7.0 | improvement | Updated framework |  |  |
| 3.7.0 | improvement | Updated widgets |  |  |
| 3.6.0 | requirement | Upgrade to 7.15.1 |  |  |
| 3.5.1 | requirement | Upgrade to 7.14.1 |  |  |
| 3.5.0 | requirement | Upgrade to 7.14.0 |  |  |
| 3.4.1 | requirement | Updated Atlas UI Resources to version 1.1.1 | Atlas UI Resources |  |
| 3.4.0 | improvement | Update Atlas UI Resources module | Atlas UI Resources |  |
| 3.3.0 | requirement | Upgrade to 7.12.0 |  |  |
| 3.2.0 | requirement | Upgrade to 7.11.0 |  |  |
| 3.1.0 | requirement | Upgrade to 7.10.0 |  |  |
| 3.0.0 | feature | Official release with the Atlas UI Resources module | Atlas UI Resources |  |
| 2.0.4 | requirement | converted to 7.8.0 |  |  |
| 2.0.3 | requirement | converted to new Mendix Modeler |  |  |
| 2.0.2 | breaking | changed configuration default setting |  |  |
| 2.0.1 | requirement | converted to new mendix modeler |  |  |
| 2.0.1 | improvement | updated atlas ui library | atlas ui library |  |
| 2.0.0 | requirement | Upgraded Mendix Version |  |  |
| 2.0.0 | improvement | Update Atlas UI Library | Atlas UI Library |  |
| 1.0.8 | removal | removed userlib | userlib |  |
| 1.0.8 | feature | new library for Atlas UI | Atlas UI |  |

## Atlas Core <a id="117187"></a>
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

## Atlas Design System <a id="117469"></a>
Starter App, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/117469)

| version | published | min Mendix |
|---|---|---|
| 2.0.0 | 2026-03-05 | 11.6.0 |
| 1.4.0 | 2025-04-16 | 10.21.0 |
| 1.3.0 | 2024-03-07 | 10.6.0 |
| 1.2.1 | 2023-05-01 | 9.18.4 |
| 1.2.0 | 2023-04-04 | 9.18.4 |
| 1.1.0 | 2022-11-10 | 9.12.8 |
| 1.0.0 | 2021-05-06 | 9.1.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.0.0 | requirement | Minimum Mendix version raised to 11.6.0 | Mendix |  |
| 2.0.0 | improvement | Updated atlas design system template to include latest widgets and atlas design style with Studio Pro 11 | Atlas Core, widgets |  |
| 1.4.0 | requirement | Minimum version upgraded to 10.21 to support Studio Pro 11 | Mendix |  |
| 1.3.0 | improvement | Updated Atlas Core | Atlas Core |  |
| 1.3.0 | requirement | Changed project minimum Studio Pro version to 10.6 | Mendix |  |
| 1.2.1 | improvement | Updated atlas-core to version 3.9.1 | atlas-core |  |
| 1.2.0 | improvement | Updated app to Mendix v9.18.4 | Mendix |  |
| 1.1.0 | improvement | Updated widgets and Atlas | widgets, Atlas |  |

## Atlas Extension <a id="211495"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/211495)

| version | published | min Mendix |
|---|---|---|
| 1.0.1 | 2023-06-06 | 9.18.3 |
| 1.0.0 | 2023-06-05 | 9.18.3 |

## Atlas Native Content <a id="117175"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/117175)

| version | published | min Mendix |
|---|---|---|
| 3.2.1 | 2026-02-18 | 10.21.0 |
| 3.1.0 | 2023-03-23 | 9.18.4 |
| 3.0.2 | 2021-09-28 | 9.6.0 |
| 3.0.1 | 2021-06-29 | 9.3.0 |
| 3.0.0 | 2021-03-31 | 9.0.5 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 3.2.1 | requirement | Updated Studio Pro minimum version to 10.21.0 to support Mendix 11. | Studio Pro |  |
| 3.1.0 | requirement | Minimal required version of Studio Pro is v9.18.4 and above. | Studio Pro |  |

## Atlas UI 2 Reference / Custom Styling App <a id="72335"></a>
Module, Mendix, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/72335)

| version | published | min Mendix |
|---|---|---|
| 3.0.0 | 2018-10-22 | 7.18.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 3.0.0 | feature | Added data generator module. | data generator module |  |
| 3.0.0 | improvement | Updated Atlas Resources. | Atlas Resources |  |

## Atlas UI Resources (Atlas 2) <a id="104730"></a>
Module, Mendix, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/104730)

| version | published | min Mendix |
|---|---|---|
| 2.7.3 | 2021-12-21 | 8.18.8 |
| 2.7.2 | 2021-07-05 | 8.18.8 |
| 2.7.1 | 2021-02-26 | 8.18.1 |
| 2.7.0 | 2021-01-26 | 8.18.0 |
| 2.6.7 | 2021-01-26 | 8.18.0 |
| 2.6.6 | 2020-12-24 | 8.17.0 |
| 2.6.4 | 2020-10-27 | 8.15.0 |
| 2.6.3 | 2020-09-30 | 8.14.0 |
| 2.6.2 | 2020-09-29 | 8.14.0 |
| 2.6.1 | 2020-09-14 | 8.13.1 |
| 2.6.0 | 2020-07-28 | 8.12.0 |
| 2.5.7 | 2020-07-07 | 8.11.0 |
| 2.5.6 | 2020-05-27 | 8.10.0 |
| 2.5.5 | 2020-05-06 | 8.9.0 |
| 2.5.4 | 2020-04-01 | 8.8.0 |
| 2.5.3 | 2020-03-04 | 8.7.0 |
| 2.5.2 | 2020-03-03 | 8.7.0 |
| 2.5.1 | 2020-03-02 | 8.7.0 |
| 2.5.0 | 2020-02-27 | 8.7.0 |
| 2.4.1 | 2020-02-10 | 8.6.0 |
| 2.4.0 | 2020-02-06 | 8.6.0 |
| 2.3.1 | 2019-11-27 | 8.4.0 |
| 2.3.0 | 2019-10-30 | 8.3.0 |
| 2.2.0 | 2019-10-29 | 8.3.0 |
| 2.1.4 | 2019-10-25 | 8.1.1 |
| 2.1.3 | 2019-09-06 | 8.1.0 |
| 2.1.2 | 2019-09-05 | 8.1.0 |
| 2.1.1 | 2019-08-28 | 8.0.0 |
| 2.1.0 | 2019-08-01 | 8.0.0 |
| 2.0.0 | 2019-08-01 | 8.0.0 |
| 1.2.4 | 2019-05-23 | 7.23.1 |
| 1.2.3 | 2019-02-20 | 7.23.0 |
| 1.2.2 | 2018-11-28 | 7.20.1 |
| 1.2.1 | 2018-11-26 | 7.20.1 |
| 1.2.0 | 2018-11-26 | 7.16.0 |
| 1.1.4 | 2018-06-28 | 7.15.1 |
| 1.1.3 | 2018-04-26 | 7.14.1 |
| 1.1.2 | 2018-04-26 | 7.14.1 |
| 1.1.1 | 2018-04-13 | 7.13.1 |
| 1.1.0 | 2018-03-28 | 7.13.1 |
| … 1 older versions | | |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.7.0 | removal | Removed hybrid phone content | hybrid phone content |  |
| 2.6.0 | requirement | Update native mobile resources module to v1.2.0 so native popup menu has correct style property names | native mobile resources module |  |
| 2.5.2 | removal | Native: Removed the TopLevel layout | TopLevel layout |  |
| 2.5.2 | removal | Native: Removed the Feedback Confirmation page template | Feedback Confirmation page template |  |
| 2.4.0 | improvement | Web: Updated building blocks to use the new layoutgrid | building blocks, page templates |  |
| 2.4.0 | improvement | Web: Updated page templates to use the new layoutgrid | building blocks, page templates |  |
| 2.4.0 | improvement | Native: Updated building blocks to use the new layoutgrid | building blocks, page templates |  |
| 2.4.0 | improvement | Native: Updated page templates to use the new layoutgrid | building blocks, page templates |  |
| 2.3.1 | removal | Native: Removed the page template Transport Routes | Transport Routes page template |  |
| 2.3.1 | improvement | Native: Updated the login page template | login page template |  |
| 2.3.1 | improvement | Native: Updated the sign up page template | sign up page template |  |
| 2.1.2 | improvement | Updated the charts widget to a newer version | charts widget |  |
| 2.1.1 | breaking | Changed scroll behavior of scroll container widget in Atlas_TopBar layout to scroll Per Region instead of Full Widget | scroll container widget, Atlas_TopBar layout |  |
| 2.1.0 | breaking | Changed profile value of simple menu bar widget from Hybrid Phone to Responsive in HybridPhone_Default and HybridPhone_Sidebar | HybridPhone_Default, HybridPhone_Sidebar |  |
| 2.0.0 | breaking | Renamed Page Layout Phone_Default to HybridPhone_Default | Phone_Default, HybridPhone_Default | HybridPhone_Default |
| 2.0.0 | breaking | Renamed Page Layout Phone_Sidebar to HybridPhone_Sidebar | Phone_Sidebar, HybridPhone_Sidebar | HybridPhone_Sidebar |
| 2.0.0 | breaking | Replaced the Google Maps widget with the Maps widget | Google Maps widget, Maps widget | Maps widget |
| 2.0.0 | breaking | Replaced the old Feedback widget with the new Feedback widget | Feedback widget | new Feedback widget |
| 1.2.3 | breaking | Replaced Google Maps widget with new Maps widget | Google Maps widget, Maps widget | Maps widget |
| 1.1.1 | improvement | Moved feedback widgets in Layouts so nesting Layout Grids is possible | Feedback widgets, Layouts |  |
| 1.1.0 | improvement | Updated the look and feel for the default Mendix Image Upload Widget | Mendix Image Upload Widget |  |

## Atlas Web Content <a id="117183"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/117183)

| version | published | min Mendix |
|---|---|---|
| 4.4.0 | 2026-10-01 | 11.0.0 |
| 4.3.0 | 2026-02-25 | 11.0.0 |
| 4.2.0 | 2025-10-15 | 11.0.0 |
| 4.1.0 | 2025-08-19 | 11.0.0 |
| 4.0.0 | 2025-05-08 | 11.0.0 |
| 3.9.0 | 2025-07-15 | 10.21.0 |
| 3.8.0 | 2025-04-16 | 10.21.0 |
| 3.7.0 | 2024-11-14 | 10.12.6 |
| 3.6.1 | 2024-10-18 | 10.6.0 |
| 3.6.0 | 2024-06-11 | 10.6.0 |
| 3.5.1 | 2024-01-18 | 10.6.0 |
| 3.5.0 | 2023-12-21 | 10.6.0 |
| 3.4.2 | 2024-10-18 | 9.24.0 |
| 3.4.1 | 2023-12-07 | 9.24.0 |
| 3.4.0 | 2023-05-17 | 9.24.0 |
| 3.3.0 | 2023-03-15 | 9.18.4 |
| 3.1.2 | 2022-11-01 | 9.12.6 |
| 3.1.1 | 2022-04-01 | 9.6.0 |
| 3.1.0 | 2022-02-25 | 9.6.0 |
| 3.0.6 | 2021-09-28 | 9.6.0 |
| 3.0.5 | 2021-08-03 | 9.4.0 |
| 3.0.4 | 2021-07-27 | 9.4.0 |
| 3.0.3 | 2021-06-29 | 9.3.0 |
| 3.0.2 | 2021-04-28 | 9.0.5 |
| 3.0.1 | 2021-04-21 | 9.0.5 |
| 3.0.0 | 2021-03-31 | 9.0.5 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 4.4.0 | requirement | Minimum Mendix version raised to 11.0.0 |  |  |
| 4.4.0 | improvement | Updated widgets versions |  |  |
| 4.3.0 | removal | Maps widget removed from module due to dependencies license issues. Will be restored after new development. | Maps widget |  |
| 4.2.0 | requirement | Design properties from Data Widgets 3.5.0 and above required for page templates and building blocks using galleries. | Data Widgets |  |
| 4.2.0 | breaking | Lists templates renamed to Galleries / Lists to reflect modern client support gallery widget usage. | Lists templates | Galleries / Lists |
| 4.1.0 | removal | Removed select entity page templates still using dojo core widget (template grid). | select entity page templates, template grid |  |
| 4.1.0 | breaking | Updated Data Widgets module to version 3.0. See Data Widgets module upgrade notice. | Data Widgets |  |
| 4.0.0 | breaking | Atlas 4 major changes. Will fully utilize CSS variables instead of SASS variables. | Atlas |  |
| 3.9.0 | improvement | Updated Data Widgets module to version 2.32.2. | Data Widgets |  |
| 3.8.0 | requirement | Updated Studio Pro minimum version to 10.21 to support Mendix 11. | Studio Pro |  |
| 3.7.0 | breaking | Updated Pageheader_WithSearch building block to use Combobox instead of Dropdown for modern client support. | Pageheader_WithSearch |  |
| 3.7.0 | requirement | Updated Atlas Web Content minimum version to Studio Pro 10.12.6. | Atlas Web Content |  |
| 3.6.1 | improvement | Updated data widgets. | data widgets |  |
| 3.6.0 | breaking | Updated login page for modern client. Validation Message widget no longer used; now uses LoginContext entity. | login page, Validation Message widget |  |
| 3.5.0 | requirement | Minimum required version of Studio Pro set to v10.6.0. | Studio Pro |  |
| 3.4.2 | improvement | Updated data widgets. | data widgets |  |
| 3.4.0 | breaking | Replaced all glyph icons with new icons from atlas-core 3.10. | glyph icons |  |
| 3.4.0 | requirement | Minimum required version of Studio Pro set to v9.24.0. | Studio Pro |  |
| 3.3.0 | requirement | Minimum required version of Studio Pro set to v9.18.4 and above. | Studio Pro |  |
| 3.1.2 | improvement | Updated all widgets. | all widgets |  |
| 3.1.1 | fix | Fixed module to be compatible with strict CSP mode. | module |  |
| 3.0.6 | improvement | Updated all widgets. | all widgets |  |
| 3.0.6 | breaking | Changed building blocks to contain new Image widget. | building blocks |  |
| 3.0.4 | improvement | Updated all widgets. | all widgets |  |
| 3.0.2 | improvement | Updated Maps widget to v2.0.1. | Maps widget |  |
| 3.0.1 | removal | Removed workflow templates. | workflow templates |  |

## Audittrail <a id="138"></a>
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

## Avola Decision Connector <a id="33257"></a>
Module, Ciphix, Partner, [marketplace](https://marketplace.mendix.com/link/component/33257)

| version | published | min Mendix |
|---|---|---|
| 3.7.0 | 2024-06-12 | 10.6.1 |
| 3.6.0 | 2024-04-02 | 10.6.1 |
| 3.5.0 | 2024-04-02 | 9.24.16 |
| 3.4.0 | 2023-05-17 | 9.12.6 |
| 3.3.0 | 2022-10-21 | 9.1.1 |
| 3.2.0 | 2022-05-06 | 9.1.1 |
| 3.1.0 | 2021-11-09 | 9.1.1 |
| 3.0.0 | 2021-08-18 | 9.1.1 |
| 2.2.0 | 2021-11-09 | 8.18.1 |
| 2.1.0 | 2020-09-21 | 8.1.1 |
| 2.0.0 | 2020-09-15 | 8.1.1 |
| 1.9.0 | 2020-09-21 | 7.15.1 |
| 1.8.0 | 2020-09-15 | 7.15.1 |
| 1.7.0 | 2020-03-19 | 7.15.1 |
| 1.6.0 | 2020-03-13 | 7.15.1 |
| 1.5.1 | 2019-06-14 | 7.15.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 3.6.0 | requirement | Upgraded to Mendix 10.6.1 (MTS), Encryption module 9.0.2, Atlas Core 3.14.0, Atlas Web Content 3.5.1. | Mendix, Encryption module, Atlas Core, Atlas Web Content |  |
| 3.5.0 | requirement | Upgraded to Mendix 9.24 LTS. | Mendix |  |
| 3.4.0 | requirement | Updated to Encryption module version 8.0.4. | Encryption module |  |
| 3.3.0 | requirement | Updated to MTS. Compatible with Atlas 3. | Mendix, Atlas |  |
| 3.3.0 | migration-step | Renamed module. |  |  |
| 3.2.0 | requirement | Updated dependent module Encryption to version 4.0.2. | Encryption module |  |
| 3.1.0 | improvement | Improved the method to get the token endpoint, using the authority server details. |  |  |
| 3.1.0 | feature | Added support for a seamless migration of an authority during runtime and running executions. |  |  |
| 3.0.0 | requirement | Upgraded to Mendix 9.1.1. | Mendix |  |
| 3.0.0 | requirement | Upgraded support for Atlas UI to 2.7. | Atlas UI |  |
| 2.2.0 | improvement | Improved the method to get the token endpoint, using the authority server details. |  |  |
| 2.2.0 | feature | Added support for a seamless migration of an authority during runtime and running executions. |  |  |
| 2.1.0 | improvement | All TimeOuts on REST calls can now be configured using the TimeOut_Short and TimeOut_Long constants. | TimeOut_Short, TimeOut_Long |  |
| 2.0.0 | requirement | Updated for new identity server implementation in Avola Decision. |  |  |
| 1.9.0 | improvement | All REST call timeouts can now be configured using the TimeOut_Short and TimeOut_Long constants. | TimeOut_Short, TimeOut_Long |  |
| 1.8.0 | requirement | Updated for new identity server implementation in Avola Decision. |  |  |
| 1.7.0 | improvement | Added extra logic to refreshing token, making sure the expiry date will be valid. |  |  |
| 1.7.0 | feature | Added time-outs on requests for getting token and execution of single decision request. |  |  |
| 1.6.0 | improvement | Improved logging functionality. |  |  |
| 1.6.0 | improvement | Tokens are requested in a subtransaction which cannot be executed concurrently. |  |  |
| 1.6.0 | feature | Added scheduled event to delete old execution request logs with a retention setup. |  |  |

## AWS Authentication Connector <a id="120333"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/120333)

| version | published | min Mendix |
|---|---|---|
| 4.1.4 | 2026-04-29 | 10.21.0 |
| 4.0.0 | 2025-04-14 | 10.21.0 |
| 3.2.3 | 2025-09-30 | 9.24.2 |
| 3.1.3 | 2024-09-19 | 9.18.0 |
| 3.0.2 | 2024-03-05 | 9.18.0 |
| 2.3.2 | 2023-11-27 | 9.18.0 |
| 2.1.2 | 2023-03-28 | 9.12.1 |
| 2.0.1 | 2022-11-15 | 9.12.1 |
| 1.0.1 | 2022-09-15 | 9.12.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 4.1.4 | breaking | Changed fixed length String attributes in Domain Model to unlimited, including Sig4Header calculation entity. | String attributes in Domain Model |  |
| 4.1.4 | fix | Bugfix in calculating Sig4 Header by encoding canonical path, excluded forward slashes, before signing. | Sig4Header calculation |  |
| 4.0.0 | requirement | Upgraded to Mendix 10.21.0, added Java dependencies to module settings. | Mendix |  |
| 3.2.3 | security | Fixed vulnerabilities in netty-handler and netty-commons libraries. | netty-handler, netty-commons |  |
| 3.2.3 | breaking | Removed widgets folder from package, no longer forcing widget definitions on project download. | widgets folder |  |
| 2.3.2 | fix | Bug fix to make Authentication compatible with textract 1.2.2. | textract |  |
| 2.0.1 | fix | Bug fix - Update in Domain model. | Domain model |  |
| 1.0.1 | security | Security fix - updated userlib removed unused jar files. | userlib |  |

## AWS IoT SiteWise Connector <a id="215633"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/215633)

| version | published | min Mendix |
|---|---|---|
| 3.0.1 | 2026-02-23 | 10.21.0 |
| 2.1.2 | 2025-04-22 | 9.24.2 |
| 1.1.0 | 2023-11-07 | 9.18.0 |
| 1.0.1 | 2023-09-07 | 9.18.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 3.0.1 | requirement | Upgraded to Mx version 10.21.0 |  |  |
| 3.0.1 | migration-step | All third party jar dependencies now configured in module itself; removed from user lib. |  |  |
| 2.1.2 | fix | ListAssets action is now correctly retrieved from team server | ListAssets |  |
| 1.0.1 | fix | Fixed bug where dependencies did not bundle as expected |  |  |

## AWS IoT Twinmaker Connector <a id="209624"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/209624)

| version | published | min Mendix |
|---|---|---|
| 4.0.1 | 2026-02-23 | 10.21.0 |
| 3.1.0 | 2024-09-27 | 9.24.2 |
| 3.0.1 | 2024-02-19 | 9.18.3 |
| 2.0.1 | 2024-02-19 | 9.18.3 |
| 1.0.1 | 2023-05-15 | 9.18.3 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 4.0.1 | requirement | Minimum Mendix version upgraded to 10.21.0 |  |  |
| 4.0.1 | migration-step | All third party jar dependencies now configured in module itself; removed from user lib. |  |  |
| 3.1.0 | improvement | Upgraded IoT TwinMaker SDK to version 2.27.17 |  |  |
| 3.0.1 | fix | Fixed GetPropertyValueHistory action bug where some AWS time formats caused errors | GetPropertyValueHistory |  |
| 2.0.1 | fix | Fixed GetPropertyValueHistory action bug where some AWS time formats caused errors | GetPropertyValueHistory |  |
| 1.0.1 | deprecation | Version 1.0.1 is deprecated |  |  |
| 1.0.1 | fix | Fixed issue that prevented the client from being created |  |  |

## AWS Lambda Connector <a id="204511"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/204511)

| version | published | min Mendix |
|---|---|---|
| 3.0.1 | 2026-02-19 | 10.21.0 |
| 2.1.0 | 2024-09-27 | 9.24.2 |
| 2.0.0 | 2024-03-08 | 9.18.0 |
| 1.1.2 | 2024-01-23 | 9.18.0 |
| 1.0.0 | 2022-11-22 | 9.18.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 3.0.1 | requirement | Minimum Mendix version upgraded to 10.21.0 | Mendix |  |
| 3.0.1 | breaking | All third party jar dependencies now configured in module itself; removed from user lib | third party jar dependencies |  |
| 2.1.0 | improvement | Upgraded Lambda SDK to 2.27.17 | Lambda SDK |  |
| 2.0.0 | requirement | Connector now requires Authentication Connector 3.0 or newer | Authentication Connector |  |
| 2.0.0 | breaking | IsAsynchonous replaced with InvocationType enum | IsAsynchonous | InvocationType |
| 1.1.2 | migration-step | Migration file added for Mendix 10.3+ to rebuild dependencies with Java Dependency Management | Java Dependency Management |  |

## Azure Blob Storage Connector <a id="244401"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/244401)

| version | published | min Mendix |
|---|---|---|
| 2.2.0 | 2025-11-25 | 10.21.0 |
| 2.1.0 | 2025-09-25 | 10.21.0 |
| 2.0.0 | 2025-09-15 | 10.21.0 |
| 1.0.0 | 2025-09-03 | 9.24.10 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.0.0 | requirement | Upgraded minimum Mendix version from 9.24.10 to 10.21.0. | Azure Blob Storage Connector |  |

## Azure Blob Storage Connector Example Implementation <a id="247092"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/247092)

| version | published | min Mendix |
|---|---|---|
| 1.1.0 | 2025-11-24 | 10.21.0 |
| 1.0.0 | 2025-11-13 | 10.21.0 |

## Badge <a id="50325"></a>
Widget, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/50325)

| version | published | min Mendix |
|---|---|---|
| 3.2.3 | 2026-02-10 | 9.6.0 |
| 3.2.2 | 2024-08-28 | 9.6.0 |
| 3.2.1 | 2023-09-27 | 9.6.0 |
| 3.2.0 | 2023-06-05 | 9.6.0 |
| 3.1.0 | 2021-12-23 | 9.6.0 |
| 3.0.0 | 2021-09-29 | 9.6.0 |
| 2.0.0 | 2021-03-31 | 9.0.5 |
| 1.4.0 | 2018-05-11 | 7.13.1 |
| 1.3.2 | 2018-03-01 | 7.4.0 |
| 1.3.1 | 2017-10-26 | 7.4.0 |
| 1.3.0 | 2017-10-26 | 7.4.0 |
| 1.2.1 | 2017-08-02 | 7.4.0 |
| 1.2.0 | 2017-07-06 | 7.2.0 |
| 1.1.2 | 2017-06-21 | 7.2.0 |
| 1.1.1 | 2017-05-30 | 7.2.0 |
| 1.1 | 2017-05-10 | 7.1.0 |
| 1.0 | 2017-04-21 | 7.1.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.0.0 | breaking | Added style design property replacing brand style widget configuration property. |  | style design property |
| 2.0.0 | migration-step | Moved styles to Atlas 3. |  |  |
| 2.0.0 | breaking | Widget needs to be reconfigured. |  |  |
| 1.3.0 | breaking | Removed additional wrapper div in Mendix 7.6, may affect custom styling. |  |  |
| 1.1 | removal | Removed label feature. |  |  |
| 1.1 | removal | Removed dynamic bootstrap styles. |  |  |

## Badge Button <a id="52705"></a>
Widget, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/52705)

| version | published | min Mendix |
|---|---|---|
| 3.3.0 | 2026-03-26 | 9.6.0 |
| 3.2.2 | 2026-02-10 | 9.6.0 |
| 3.2.1 | 2023-09-27 | 9.6.0 |
| 3.2.0 | 2023-06-05 | 9.6.0 |
| 3.1.0 | 2021-12-23 | 9.6.0 |
| 3.0.1 | 2021-12-03 | 9.6.0 |
| 3.0.0 | 2021-09-28 | 9.6.0 |
| 2.0.0 | 2021-03-31 | 9.0.5 |
| 1.3.0 | 2018-05-11 | 7.13.1 |
| 1.2.1 | 2018-03-01 | 7.6.0 |
| 1.2.0 | 2017-08-29 | 7.6.0 |
| 1.1.1 | 2017-08-02 | 7.2.0 |
| 1.1.0 | 2017-07-06 | 7.2.0 |
| 1.0.2 | 2017-06-21 | 7.2.0 |
| 1.0.1 | 2017-05-30 | 7.2.0 |
| 1.0 | 2017-05-13 | 7.1.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.0.0 | feature | Improved widget configuration properties, added style design property, page editor previews, moved styles to Atlas 3, applied 8px grid system. | widget configuration properties, style design property, page editor design mode preview, page editor structure preview, Atlas 3, 8px grid system |  |
| 2.0.0 | breaking | Widget needs to be reconfigured. Button style widget configuration property replaced by style design property. | button style widget configuration property | style design property |
| 1.3.0 | fix | Fixed open page for Mendix 7.14.1. |  |  |
| 1.2.0 | breaking | Removed additional wrapper div in Mendix 7.6, may slightly affect custom styling but benefits custom styling ability. | wrapper div |  |
| 1.1.1 | requirement | Made widget React 16 compatible. | React |  |

## BAPI Connector of SAP Solutions <a id="119810"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/119810)

| version | published | min Mendix |
|---|---|---|
| 3.0.3 | 2025-12-03 | 10.21.0 |
| 3.0.2 | 2025-10-24 | 10.21.0 |
| 3.0.1 | 2025-09-09 | 10.21.0 |
| 3.0.0 | 2025-09-09 | 10.21.0 |
| 2.1.2 | 2025-12-03 | 9.24.33 |
| 2.1.1 | 2025-10-24 | 9.24.33 |
| 2.1.0 | 2025-05-06 | 9.24.33 |
| 2.0.5 | 2025-03-26 | 9.24.4 |
| 2.0.4 | 2023-10-06 | 9.24.4 |
| 2.0.3 | 2023-08-02 | 9.24.0 |
| 2.0.2 | 2023-06-20 | 9.24.0 |
| 2.0.1 | 2023-06-01 | 9.24.0 |
| 2.0.0 | 2023-04-11 | 9.24.0 |
| 1.2.4 | 2023-10-06 | 8.18.25 |
| 1.2.3 | 2023-08-02 | 9.24.0 |
| 1.2.2 | 2023-06-21 | 8.18.24 |
| 1.2.1 | 2023-06-01 | 8.18.10 |
| 1.2.0 | 2023-04-11 | 8.18.10 |
| 1.1.0 | 2022-11-22 | 8.18.10 |
| 1.0.1 | 2022-04-26 | 8.18.10 |
| 1.0.0 | 2022-03-02 | 8.18.10 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 3.0.3 | security | Security vulnerabilities were identified and fixed. |  |  |
| 3.0.2 | improvement | Added support for Mendix 10 Atlas styles. |  |  |
| 3.0.2 | fix | Fixed structure mapping and null association issues. |  |  |
| 3.0.1 | fix | Harmonized internal module dependencies to prevent compilation issues. |  |  |
| 3.0.0 | requirement | Upgrade to Mendix 10.21. |  |  |
| 2.1.2 | security | Security vulnerabilities were identified and fixed. |  |  |
| 2.1.1 | fix | Fixed structure mapping and creation of null associations. |  |  |
| 2.1.0 | requirement | Released on Mendix v9.24.33. |  |  |
| 2.0.4 | security | Security fixes and jar updates. |  |  |
| 2.0.4 | migration-step | Remove duplicate old jars from userlib folder after this update. | userlib |  |
| 2.0.1 | security | Updated userlib jar files to fix security vulnerabilities. |  |  |
| 2.0.0 | requirement | Upgrade to Mendix 9.24. |  |  |
| 2.0.0 | feature | Added support to call SAP BAPI using RFC Destination defined on SAP BTP. |  |  |
| 2.0.0 | feature | Mendix applications can now call SAP BAPI using SAP Cloud Connector. |  |  |
| 2.0.0 | requirement | bapi-service component is required to use RFC Destination. | bapi-service |  |
| 1.2.4 | security | Security fix and jars update. |  |  |
| 1.2.4 | migration-step | Remove older duplicate jars from userlib folder after this update. | userlib |  |
| 1.2.1 | security | Updated userlib jar files to fix vulnerabilities. |  |  |
| 1.2.0 | feature | Added support to call SAP BAPI using RFC Destination defined on SAP BTP. |  |  |
| 1.2.0 | feature | Mendix application can call SAP BAPI using SAP Cloud Connector. |  |  |
| 1.2.0 | requirement | bapi-service component is required to use RFC Destination. | bapi-service |  |
| 1.1.0 | feature | Added support for datatype 'RAW' in SAP BAPI. RAW properties created as String in Mendix entity. |  |  |

## Barcode Display <a id="117536"></a>
Widget, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/117536)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2021-05-19 | 9.1.1 |

## Barcode Generator <a id="200681"></a>
Widget, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/200681)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2026-04-28 | 10.24.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.0.0 | requirement | Minimum Mendix version requirement: 10.24.0 |  |  |

## Barcode Scanner <a id="117627"></a>
Widget, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/117627)

| version | published | min Mendix |
|---|---|---|
| 2.5.1 | 2026-02-10 | 9.6.0 |
| 2.5.0 | 2025-09-15 | 9.6.0 |
| 2.4.2 | 2024-08-30 | 9.6.0 |
| 2.4.1 | 2024-07-01 | 9.6.0 |
| 2.3.1 | 2023-09-27 | 9.6.0 |
| 2.3.0 | 2023-06-05 | 9.6.0 |
| 2.2.4 | 2023-04-04 | 9.6.0 |
| 2.2.3 | 2023-01-04 | 9.6.0 |
| 2.2.2 | 2022-10-28 | 9.6.0 |
| 2.2.1 | 2022-07-27 | 9.6.0 |
| 2.2.0 | 2021-12-23 | 9.6.0 |
| 2.1.0 | 2021-12-16 | 9.6.0 |
| 2.0.1 | 2021-12-03 | 9.6.0 |
| 2.0.0 | 2021-09-28 | 9.6.0 |
| 1.0.0 | 2021-05-28 | 9.0.5 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.5.0 | improvement | Added logic to switch to native browser BarcodeDetector API if available instead of using zxing library. | zxing library, BarcodeDetector API |  |
| 2.2.3 | improvement | Updated the dependencies. |  |  |

## Barcode Scanner for Hybrid Mobile <a id="1469"></a>
Widget, Mendix, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/1469)

| version | published | min Mendix |
|---|---|---|
| 3.2.3 | 2019-09-18 | 7.13.1 |
| 3.2.2 | 2018-12-19 | 7.13.1 |
| 3.2.1 | 2018-05-23 | 7.13.1 |
| 3.2.0 | 2018-05-12 | 7.13.1 |
| 3.1.0 | 2018-05-11 | 7.13.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 3.2.0 | feature | Widget can now be run offline, powerful combination with nanoflows |  |  |
| 3.1.0 | breaking | Widget renamed to Barcode Scanner | Barcode Scanner |  |

## BidSuite <a id="202970"></a>
Solution, Intelizign, Partner, [marketplace](https://marketplace.mendix.com/link/component/202970)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2022-10-07 | 9.6.2 |

## Bizzomate Number Input [deprecated] <a id="230908"></a>
Widget, Ciphix, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/230908)

| version | published | min Mendix |
|---|---|---|
| 1.5.0 | 2024-12-17 | 10.12.1 |
| 1.4.0 | 2024-12-13 | 10.12.1 |
| 1.3.2 | 2024-12-09 | 10.12.1 |
| 1.3.1 | 2024-10-10 | 10.12.1 |
| 1.3.0 | 2024-09-23 | 10.12.1 |
| 1.2.0 | 2024-09-09 | 10.12.1 |
| 1.1.0 | 2024-09-05 | 10.12.1 |
| 1.0.1 | 2024-09-05 | 10.12.1 |
| 1.0.0 | 2024-09-03 | 10.12.1 |

## Bizzomate React Select <a id="215760"></a>
Widget, Ciphix, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/215760)

| version | published | min Mendix |
|---|---|---|
| 1.3.0 | 2023-10-20 | 9.22.0 |
| 1.2.5 | 2023-10-20 | 9.22.0 |
| 1.2.4 | 2023-10-12 | 9.22.0 |
| 1.2.3 | 2023-09-05 | 9.22.0 |
| 1.0.0 | 2023-09-05 | 9.22.0 |

## Blank GenAI App <a id="227934"></a>
Starter App, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/227934)

| version | published | min Mendix |
|---|---|---|
| 5.3.0 | 2026-09-08 | 11.12.3 |
| 5.2.0 | 2026-08-13 | 11.12.2 |
| 5.1.0 | 2026-08-04 | 11.12.1 |
| 5.0.0 | 2026-07-02 | 11.12.0 |
| 4.9.0 | 2026-05-12 | 10.24.13 |
| 4.8.0 | 2026-04-17 | 10.24.13 |
| 4.7.0 | 2026-02-02 | 10.24.13 |
| 4.6.0 | 2025-12-29 | 10.24.13 |
| 4.5.0 | 2025-12-10 | 10.24.0 |
| 4.4.0 | 2025-11-25 | 10.24.0 |
| 4.3.1 | 2025-11-11 | 10.24.0 |
| 4.3.0 | 2025-11-04 | 10.24.0 |
| 4.2.0 | 2025-09-23 | 10.24.0 |
| 4.1.0 | 2025-08-14 | 10.24.0 |
| 4.0.0 | 2025-07-04 | 10.24.0 |
| 3.1.0 | 2025-05-27 | 10.21.1 |
| 3.0.0 | 2025-04-10 | 10.21.0 |
| 2.1.0 | 2025-03-18 | 10.12.4 |
| 2.0.0 | 2025-01-13 | 10.12.4 |
| 1.5.1 | 2024-10-17 | 10.12.4 |
| 1.5.0 | 2024-10-17 | 10.12.4 |
| 1.4.0 | 2024-09-20 | 10.12.4 |
| 1.3.0 | 2024-08-29 | 10.12.4 |
| 1.2.0 | 2024-08-01 | 10.12.2 |
| 1.1.1 | 2024-07-04 | 10.12.0 |
| 1.0.0 | 2024-06-26 | 10.12.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 5.3.0 | requirement | Upgraded to Mendix SP 11.12.3 |  |  |
| 5.3.0 | improvement | Upgraded marketplace components |  |  |
| 5.2.0 | requirement | Upgraded to 11.12.2 |  |  |
| 5.2.0 | improvement | Marketplace modules upgraded to latest versions |  |  |
| 5.1.0 | requirement | Upgraded to 11.12.1 |  |  |
| 5.1.0 | improvement | All marketplace modules were upgraded to their latest versions |  |  |
| 5.0.0 | requirement | Upgraded to 11.12 as part of Agents Kit 2 release |  |  |
| 5.0.0 | feature | Supports Atlas 4 if enabled on application level | Atlas 4 |  |
| 5.0.0 | improvement | All marketplace modules (apart from Atlas Core) updated to latest versions if applicable |  |  |
| 4.9.0 | improvement | Marketplace modules were upgraded to their latest versions |  |  |
| 4.8.0 | improvement | Marketplace modules were upgraded to their latest versions |  |  |
| 4.7.0 | improvement | Marketplace modules were upgraded to their latest versions |  |  |
| 4.6.0 | improvement | Marketplace modules were upgraded to their latest versions |  |  |
| 4.6.0 | requirement | Upgraded to Mendix SP 10.24.13 |  |  |
| 4.5.0 | improvement | Mendix Cloud GenAI Connector upgraded to 5.4.0 for Cohere 4 embeddings support | Mendix Cloud GenAI Connector |  |
| 4.5.0 | removal | Deleted unused CommunityCommons dependency for XSS Sanitization to fix vulnerability | CommunityCommons |  |
| 4.4.0 | improvement | Updated all marketplace modules to their latest versions |  |  |
| 4.3.1 | improvement | Upgraded modules: AgentCommons 2.4.1, MCP Client 2.2.1, ConversationalUI 5.2.1 | AgentCommons, MCP Client, ConversationalUI |  |
| 4.3.0 | improvement | GenAI modules were upgraded to their latest versions |  |  |
| 4.3.0 | improvement | Encryption module was upgraded to 11.0.3 | Encryption |  |
| 4.2.0 | improvement | Upgraded GenAI modules and encryption module |  |  |
| 4.1.0 | improvement | All modules were updated to the latest version |  |  |
| 4.0.0 | requirement | Starter app was upgraded to 10.24.0 |  |  |
| 4.0.0 | improvement | Updated all GenAI and related modules to latest versions: Admin 4.3.1, Atlas Core 3.18.0, Atlas Web Content 3.8.0, Agent Commons 1.3.0, Amazon Bedrock 8.2.0, AWS Auth 4.1.1, Community Commons 11.2.0, ConversationalUI 4.0.0, Database 7.0.0, Data Widgets 3.0.1, Encryption 11.0.1, GenAI Commons 4.2.0, Feedback 4.0.1, GenAI Connector 4.2.0, Nanoflow Commons 6.0.0, OpenAI 6.0.0, PgVector 4.2.0, Web Actions 2.11.0 | Administration, Atlas Core, Atlas Web Content, Agent Commons, Amazon Bedrock Connector, AWS Authentication, Community Commons, ConversationalUI, Data Base Connector, Data Widgets, Encryption, GenAI Commons, Mendix Feedback Module, Mendix Cloud GenAI Connector, Nanoflow Commons, OpenAI Connector, PgVector Knowledge Base, Web Actions |  |
| 3.1.0 | requirement | Updated to Mendix Studio Pro 10.21.1 |  |  |
| 3.1.0 | improvement | AgentCommons and MCPServer modules were downloaded and existing modules updated | AgentCommons, MCPServer |  |
| 3.0.0 | requirement | Updated to Mendix Studio Pro 10.21.0 |  |  |
| 3.0.0 | improvement | Updated Connector modules: Amazon Bedrock 7.0.0, GenAI Commons 3.0.0, ConversationalUI 3.0.0, Mx GenAI Connector 3.0.0, OpenAI 5.0.0, PgVector 3.0.0 | Amazon Bedrock Connector, GenAI Commons, ConversationalUI, Mendix GenAI Connector, OpenAI Connector, PgVector Knowledge Base |  |
| 2.1.0 | improvement | Updated modules: Amazon Bedrock 6.2.1, AWS Auth 3.2.2, GenAIForMendix 2.3.1, NanoflowCommons 4.0.4, OpenAI 4.3.0, PgVector 2.4.1 | Amazon Bedrock Connector, AWS Authentication Module, GenAIForMendix, Nanoflow Commons, OpenAI Connector, PgVector Knowledge Base |  |
| 2.0.0 | improvement | Updated modules: Amazon Bedrock 6.0.0, AWS Auth 3.2.0, Community Commons 10.1.0, ConversationalUI 2.0.0, GenAI Commons 2.0.0, MxGenAIConnector 2.0.0, OpenAI 4.0.0, PgVector 2.3.0 | Amazon Bedrock Connector, AWS Authentication Module, Community Commons, ConversationalUI, GenAI Commons, Mendix GenAI Connector, OpenAI Connector, PgVector Knowledge Base |  |
| 1.5.1 | improvement | Updated modules: Amazon Bedrock 5.3.0, AWS Auth 3.2.0, Community Commons 10.0.7, ConversationalUI 1.5.1, Encryption 10.0.3, GenAI Commons 1.5.0, OpenAI 3.4.1, PgVector 2.2.0 | Amazon Bedrock Connector, AWS Authentication Module, Community Commons, ConversationalUI, Encryption, GenAI Commons, OpenAI Connector, PgVector Knowledge Base |  |
| 1.5.0 | improvement | Updated modules: Amazon Bedrock 5.3.0, AWS Auth 3.2.0, Community Commons 10.0.7, ConversationalUI 1.5.0, Encryption 10.0.3, GenAI Commons 1.5.0, OpenAI 3.4.1, PgVector 2.2.0 | Amazon Bedrock Connector, AWS Authentication Module, Community Commons, ConversationalUI, Encryption, GenAI Commons, OpenAI Connector, PgVector Knowledge Base |  |
| 1.4.0 | improvement | Updated modules: Amazon Bedrock 5.2.1, AWS Auth 3.1.3, ConversationalUI 1.4.0, Datawidgets 2.23.0, Feedback 3.0.0, Nanoflow Commons 4.0.4, OpenAI 3.3.0, GenAI Commons 1.3.0 | Amazon Bedrock Connector, AWS Authentication Module, ConversationalUI, Data Widgets, Mendix Feedback Module, Nanoflow Commons, OpenAI Connector, GenAI Commons |  |
| 1.3.0 | improvement | Updated GenAI modules: GenAI Commons 1.2.0, OpenAI 3.2.0, AWS Auth 3.1.2, Amazon Bedrock 5.2.0, ConversationalUI 1.3.0, PgVector 2.1.0 | GenAI Commons, OpenAI Connector, AWS Authentication Connector, Amazon Bedrock Connector, Conversational UI, PgVector Knowledge Base |  |
| 1.3.0 | requirement | Studio Pro version is now 10.12.4 |  |  |
| 1.2.0 | improvement | Updated GenAI modules: GenAI Commons 1.1.0, OpenAI 3.1.1, AWS Auth 3.1.1, Amazon Bedrock 5.0.1, ConversationalUI 1.2.1, PgVector 2.0.0 | GenAI Commons, OpenAI Connector, AWS Authentication Connector, Amazon Bedrock Connector, Conversational UI, PgVector Knowledge Base |  |
| 1.2.0 | requirement | Studio Pro version is now 10.12.2 |  |  |
| 1.1.1 | improvement | Updated ConversationalUI module to version 1.1.1 | ConversationalUI |  |

## Blank Native Mobile App <a id="109511"></a>
Starter App, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/109511)

| version | published | min Mendix |
|---|---|---|
| 11.15.0 | 2026-09-30 | 11.15.0 |
| 11.14.0 | 2026-08-26 | 11.14.0 |
| 11.13.0 | 2026-08-10 | 11.13.0 |
| 11.12.5 | 2026-09-25 | 11.12.5 |
| 11.12.4 | 2026-08-31 | 11.12.4 |
| 11.12.3 | 2026-08-14 | 11.12.3 |
| 11.12.2 | 2026-08-10 | 11.12.2 |
| 11.12.1 | 2026-07-17 | 11.12.1 |
| 11.12.0 | 2026-07-03 | 11.12.0 |
| 11.11.1 | 2026-06-16 | 11.11.0 |
| 11.11.0 | 2026-06-09 | 11.11.0 |
| 11.10.0 | 2026-05-15 | 11.10.0 |
| 11.9.1 | 2026-05-04 | 11.9.1 |
| 11.9.0 | 2026-04-10 | 11.9.0 |
| 11.8.0 | 2026-03-05 | 11.8.0 |
| 11.7.0 | 2026-01-30 | 11.7.0 |
| 11.6.11 | 2026-09-09 | 11.14.0 |
| 11.6.4 | 2026-03-09 | 11.6.4 |
| 11.6.3 | 2026-01-30 | 11.6.3 |
| 11.6.2 | 2026-01-12 | 11.6.2 |
| 11.6.1 | 2026-01-08 | 11.6.1 |
| 11.6.0 | 2025-12-24 | 11.6.0 |
| 11.5.0 | 2025-11-25 | 11.5.0 |
| 11.4.83498 | 2025-11-04 | 11.4.0 |
| 11.3.80734 | 2025-10-01 | 11.3.0 |
| 11.2.77998 | 2025-08-29 | 11.0.0 |
| 11.1.75979 | 2025-07-30 | 11.1.0 |
| 11.0.73100 | 2025-06-26 | 11.0.0 |
| 11.0.70205 | 2025-05-28 | 11.0.0 |
| 11.0.68828 | 2025-05-08 | 11.0.0 |
| 10.24.75382 | 2026-03-09 | 10.24.2 |
| 10.24.73019 | 2025-06-25 | 10.24.0 |
| 10.23.70273 | 2025-05-28 | 10.23.0 |
| 10.22.68245 | 2025-05-02 | 10.22.0 |
| 10.21.64969 | 2025-03-31 | 10.21.1 |
| 10.21.64362 | 2025-03-25 | 10.21.0 |
| 10.20.60519 | 2025-02-26 | 10.20.0 |
| 10.19.57669 | 2025-01-28 | 10.19.0 |
| 10.18.58475 | 2025-02-04 | 10.18.2 |
| 10.18.55792 | 2025-01-10 | 10.18.1 |
| … 151 older versions | | |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 11.6.11 | requirement | Minimum Mendix version requirement is 11.14.0 | Mendix |  |
| 3.0.23 | removal | Remove Mendix SSO module | Mendix SSO module |  |
| 3.0.23 | improvement | Update all included modules to latest |  |  |
| 3.0.4 | improvement | Update Atlas Core to 3.0.2, update Atlas Web Content to 3.0.2 | Atlas Core, Atlas Web Content |  |
| 3.0.3 | requirement | Release for Mendix 9.1.1 | Mendix |  |
| 3.0.0 | feature | New blank native mobile app with Atlas 3 for Mendix 9, including Atlas Core, Web Content & Native Content | Atlas Core, Atlas Web Content, Atlas Native Content |  |
| 2.2.42 | requirement | Convert to 8.18.9, update Native Mobile Resources to 1.3.0 | Mendix, Native Mobile Resources |  |
| 1.2.18 | improvement | Update Mendix Feedback Widget to version 8.2.1 | Mendix Feedback Widget |  |
| 1.0.0-beta4 | improvement | Updated Atlas Resources to 2.0.0, NanoflowCommons, NativeMobileActions | Atlas Resources, NanoflowCommons, NativeMobileActions |  |
| 1.0.0-beta2 | improvement | Update app store modules (widgets and nanoflow actions) |  |  |

## Blank Web App <a id="51830"></a>
Starter App, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/51830)

| version | published | min Mendix |
|---|---|---|
| 11.15.0 | 2026-09-30 | 11.15.0 |
| 11.14.0 | 2026-08-26 | 11.14.0 |
| 11.13.0 | 2026-07-28 | 11.13.0 |
| 11.12.5 | 2026-09-28 | 11.12.5 |
| 11.12.4 | 2026-08-31 | 11.12.4 |
| 11.12.2 | 2026-07-27 | 11.12.2 |
| 11.12.1 | 2026-07-15 | 11.12.1 |
| 11.12.0 | 2026-06-30 | 11.12.0 |
| 11.11.0 | 2026-05-29 | 11.11.0 |
| 11.10.0 | 2026-04-28 | 11.10.0 |
| 11.9.1 | 2026-04-17 | 11.9.1 |
| 11.9.0 | 2026-04-07 | 11.9.0 |
| 11.8.0 | 2026-03-02 | 11.8.0 |
| 11.7.0 | 2026-01-30 | 11.7.0 |
| 11.6.11 | 2026-09-09 | 11.6.11 |
| 11.6.4 | 2026-03-04 | 11.6.4 |
| 11.6.3 | 2026-01-29 | 11.6.3 |
| 11.6.2 | 2026-01-12 | 11.6.2 |
| 11.6.1 | 2026-01-07 | 11.6.1 |
| 11.6.0 | 2025-12-23 | 11.6.0 |
| 11.5.0 | 2025-11-25 | 11.5.0 |
| 11.4.1 | 2025-11-04 | 11.4.0 |
| 11.4.0 | 2025-11-04 | 11.4.0 |
| 11.3.80734 | 2025-10-01 | 11.3.0 |
| 11.2.77998 | 2025-08-29 | 11.2.0 |
| 11.1.75979 | 2025-07-30 | 11.1.0 |
| 11.0.73100 | 2025-07-23 | 11.0.0 |
| 11.0.70205 | 2025-05-28 | 11.0.0 |
| 11.0.68828 | 2025-05-08 | 11.0.0 |
| 11.0.5 | 2025-09-23 | 11.0.0 |
| 11.0.4 | 2025-09-23 | 11.0.0 |
| 10.24.113362 | 2026-07-03 | 10.24.22 |
| 10.24.75382 | 2025-07-25 | 10.24.2 |
| 10.24.73019 | 2025-06-25 | 10.24.0 |
| 10.23.70273 | 2025-05-28 | 10.23.0 |
| 10.22.68245 | 2025-05-02 | 10.22.0 |
| 10.21.64969 | 2025-03-31 | 10.21.1 |
| 10.21.64362 | 2025-03-25 | 10.21.0 |
| 10.20.60519 | 2025-02-26 | 10.20.0 |
| 10.19.57669 | 2025-01-28 | 10.19.0 |
| … 191 older versions | | |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 11.15.0 | requirement | Minimum Mendix Studio Pro version requirement: 11.15.0 | Mendix Studio Pro |  |
| 11.15.0 | requirement | Administration module updated to 4.5.0 | Administration module |  |
| 11.15.0 | requirement | Atlas Core updated to 4.5.0 | Atlas Core |  |
| 11.15.0 | requirement | Atlas Web Content updated to 4.3.0 | Atlas Web Content |  |
| 11.15.0 | requirement | Data Widgets updated to 3.11.6 | Data Widgets |  |
| 11.15.0 | requirement | Mendix Feedback Module updated to 5.0.0 | Mendix Feedback Module |  |
| 11.15.0 | requirement | Nanoflow Commons updated to 7.4.0 | Nanoflow Commons |  |
| 11.15.0 | requirement | Web Actions updated to 2.11.2 | Web Actions |  |
| 11.15.0 | requirement | Accessibility Helper updated to 2.2.2 | Accessibility Helper |  |
| 11.15.0 | requirement | Accordion updated to 2.3.6 | Accordion |  |
| 11.15.0 | requirement | Badge updated to 3.2.3 | Badge |  |
| 11.15.0 | requirement | Badge Button updated to 3.3.0 | Badge Button |  |
| 11.15.0 | requirement | Barcode Scanner updated to 2.5.1 | Barcode Scanner |  |
| 11.15.0 | requirement | Charts updated to 6.3.2 | Charts |  |
| 11.15.0 | requirement | Combo box updated to 2.10.0 | Combo box |  |
| 11.15.0 | requirement | Fieldset updated to 3.2.2 | Fieldset |  |
| 11.15.0 | requirement | HTML Element updated to 1.2.12 | HTML Element |  |
| 11.15.0 | requirement | Image updated to 1.6.1 | Image |  |
| 11.15.0 | requirement | Language Selector updated to 1.1.4 | Language Selector |  |
| 11.15.0 | requirement | Maps updated to 5.0.0 | Maps |  |
| 11.15.0 | requirement | Pop-up Menu updated to 4.3.1 | Pop-up Menu |  |
| 11.15.0 | requirement | Progress Bar updated to 3.2.3 | Progress Bar |  |
| 11.15.0 | requirement | Progress Circle updated to 3.3.3 | Progress Circle |  |
| 11.15.0 | requirement | Range Slider updated to 3.0.3 | Range Slider |  |
| 11.15.0 | requirement | Rating updated to 3.2.2 | Rating |  |
| 11.15.0 | requirement | Slider updated to 3.0.4 | Slider |  |
| 11.15.0 | requirement | Switch updated to 4.3.0 | Switch |  |
| 11.15.0 | requirement | Timeline updated to 3.2.3 | Timeline |  |
| 11.15.0 | requirement | Tooltip updated to 1.5.1 | Tooltip |  |
| 11.15.0 | requirement | Video Player updated to 3.2.4 | Video Player |  |
| 11.14.0 | requirement | Atlas Core upgraded from 4.3.7 to 4.4.0 | Atlas Core |  |
| 11.14.0 | requirement | Data Widgets upgraded from 3.11.2 to 3.11.4 | Data Widgets |  |
| 11.14.0 | requirement | HTML Element upgraded from 1.2.11 to 1.2.12 | HTML Element |  |
| 11.14.0 | requirement | Image upgraded from 1.5.1 to 1.6.1 | Image |  |
| 11.14.0 | requirement | Charts upgraded from 6.3.1 to 6.3.2 | Charts |  |
| 11.13.0 | requirement | Atlas Core upgraded to 4.3.7 | Atlas Core |  |
| 11.13.0 | requirement | Data Widgets upgraded to 3.11.2 | Data Widgets |  |
| 11.13.0 | requirement | HTML Element upgraded to 1.2.11 | HTML Element |  |
| 11.13.0 | requirement | Charts upgraded to 6.3.1 | Charts |  |
| 11.12.4 | requirement | Atlas Core upgraded to 4.4.0 | Atlas Core |  |
| 11.12.4 | requirement | Data Widgets upgraded to 3.11.4 | Data Widgets |  |
| 11.12.4 | requirement | HTML Element upgraded to 1.2.12 | HTML Element |  |
| 11.12.4 | requirement | Image upgraded to 1.6.1 | Image |  |
| 11.12.4 | requirement | Charts upgraded to 6.3.2 | Charts |  |
| 11.12.2 | requirement | Atlas Core upgraded to 4.3.7 | Atlas Core |  |
| 11.12.2 | requirement | Data Widgets upgraded to 3.11.2 | Data Widgets |  |
| 11.12.2 | requirement | Combo box upgraded from 2.8.1 to 2.8.2 | Combo box |  |
| 11.12.2 | requirement | HTML Element upgraded from 1.2.9 to 1.2.10 | HTML Element |  |
| 11.12.2 | requirement | Charts upgraded to 6.3.1 | Charts |  |
| 11.12.1 | requirement | Nanoflow Commons upgraded from 7.0.0 to 7.2.0 | Nanoflow Commons |  |
| 11.12.1 | requirement | Data Widgets upgraded to 3.11.2 | Data Widgets |  |
| 11.12.1 | requirement | HTML Element upgraded from 1.2.7 to 1.2.9 | HTML Element |  |
| 11.12.1 | requirement | Combo box upgraded from 2.8.0 to 2.8.1 | Combo box |  |
| 11.12.1 | requirement | Pop-up Menu upgraded from 4.2.0 to 4.3.0 | Pop-up Menu |  |
| 11.12.1 | requirement | Range Slider upgraded from 3.0.1 to 3.0.2 | Range Slider |  |
| 11.12.1 | requirement | Slider upgraded from 3.0.2 to 3.0.3 | Slider |  |
| 11.12.0 | requirement | Data Widgets upgraded from 3.10.0 to 3.11.1 | Data Widgets |  |
| 11.12.0 | requirement | Nanoflow Commons upgraded from 6.3.1 to 7.1.0 | Nanoflow Commons |  |
| 11.12.0 | requirement | Atlas Core upgraded to 4.3.7 | Atlas Core |  |
| 11.12.0 | requirement | HTML Element upgraded to 1.2.9 | HTML Element |  |
| 11.12.0 | requirement | Charts upgraded to 6.3.1 | Charts |  |
| 11.11.0 | requirement | Data Widgets upgraded from 3.9.0 to 3.10.0 | Data Widgets |  |
| 11.11.0 | requirement | Mendix Feedback Module upgraded from 4.1.1 to 5.0.0 | Mendix Feedback Module |  |
| 11.11.0 | requirement | Nanoflow Commons upgraded from 6.3.1 to 7.0.0 | Nanoflow Commons |  |
| 11.11.0 | requirement | Atlas Core upgraded from 4.3.5 to 4.3.6 | Atlas Core |  |
| 11.11.0 | requirement | HTML Element upgraded from 1.2.7 to 1.2.7 | HTML Element |  |
| 11.11.0 | requirement | Range Slider upgraded from 3.0.1 to 3.0.1 | Range Slider |  |
| 11.11.0 | requirement | Slider upgraded from 3.0.2 to 3.0.2 | Slider |  |
| 11.11.0 | requirement | Pop-up Menu upgraded from 4.1.0 to 4.2.0 | Pop-up Menu |  |
| 11.10.0 | requirement | Administration module upgraded from 4.4.0 to 4.4.0 | Administration module |  |
| 11.10.0 | requirement | Data Widgets upgraded from 3.8.0 to 3.9.0 | Data Widgets |  |
| 11.10.0 | requirement | Atlas Core upgraded from 4.3.4 to 4.3.5 | Atlas Core |  |
| 11.10.0 | requirement | Charts upgraded from 6.2.0 to 6.3.0 | Charts |  |
| 11.10.0 | requirement | Combo box upgraded from 2.7.0 to 2.8.0 | Combo box |  |
| 11.10.0 | requirement | Pop-up Menu upgraded from 4.0.0 to 4.1.0 | Pop-up Menu |  |
| 11.9.1 | requirement | HTML Element upgraded from 1.2.6 to 1.2.6 | HTML Element |  |
| 11.9.0 | requirement | Minimum Mendix version is now 11.9.0 | Mendix Studio Pro |  |
| 11.9.0 | requirement | Atlas Core updated to 4.3.5 | Atlas Core |  |
| 11.9.0 | requirement | Data Widgets updated to 3.9.0 | Data Widgets |  |
| 11.9.0 | requirement | Badge Button updated to 3.3.0 | Badge Button |  |
| 11.8.0 | requirement | Minimum Mendix version is now 11.8.0 | Mendix Studio Pro |  |
| 11.8.0 | requirement | Atlas Core updated to 4.3.4 | Atlas Core |  |
| 11.8.0 | requirement | Data Widgets updated to 3.8.1 | Data Widgets |  |
| 11.8.0 | requirement | Nanoflow Commons updated to 6.3.0 | Nanoflow Commons |  |
| 11.8.0 | requirement | Combo box updated to 2.7.2 | Combo box |  |
| 11.8.0 | requirement | Badge Button updated to 3.2.2 | Badge Button |  |
| 11.8.0 | requirement | HTML Element updated to 1.2.5 | HTML Element |  |
| 11.8.0 | requirement | Language Selector updated to 1.1.4 | Language Selector |  |
| 11.7.0 | requirement | Minimum Mendix version is now 11.7.0 | Mendix Studio Pro |  |
| 11.7.0 | requirement | Atlas Core updated to 4.3.2 | Atlas Core |  |
| 11.7.0 | requirement | Atlas Web Content updated to 4.2.0 | Atlas Web Content |  |
| 11.7.0 | requirement | Data Widgets updated to 3.8.0 | Data Widgets |  |
| 11.7.0 | requirement | Mendix Feedback Module updated to 4.0.4 | Mendix Feedback Module |  |
| 11.7.0 | requirement | Nanoflow Commons updated to 6.2.1 | Nanoflow Commons |  |
| 11.7.0 | requirement | Web Actions updated to 2.11.1 | Web Actions |  |
| 11.7.0 | requirement | Accessibility Helper updated to 2.2.1 | Accessibility Helper |  |
| 11.7.0 | requirement | Accordion updated to 2.3.4 | Accordion |  |
| 11.7.0 | requirement | Badge updated to 3.2.2 | Badge |  |
| 11.7.0 | requirement | Badge Button updated to 3.2.1 | Badge Button |  |
| 11.7.0 | requirement | Barcode Scanner updated to 2.5.0 | Barcode Scanner |  |
| 11.7.0 | requirement | Charts updated to 6.2.3 | Charts |  |
| 11.7.0 | requirement | Combo box updated to 2.7.2 | Combo box |  |
| 11.7.0 | requirement | Fieldset updated to 3.2.1 | Fieldset |  |
| 11.7.0 | requirement | HTML Element updated to 1.2.4 | HTML Element |  |
| 11.7.0 | requirement | Language Selector updated to 1.1.3 | Language Selector |  |
| 11.7.0 | requirement | Pop-up Menu updated to 4.0.2 | Pop-up Menu |  |
| 11.7.0 | requirement | Progress Bar updated to 3.2.2 | Progress Bar |  |
| 11.7.0 | requirement | Progress Circle updated to 3.3.2 | Progress Circle |  |
| 11.7.0 | requirement | Range Slider updated to 3.0.0 | Range Slider |  |
| 11.7.0 | requirement | Rating updated to 3.2.1 | Rating |  |
| 11.7.0 | requirement | Slider updated to 3.0.0 | Slider |  |
| 11.7.0 | requirement | Timeline updated to 3.2.2 | Timeline |  |
| 11.7.0 | requirement | Tooltip updated to 1.4.2 | Tooltip |  |
| 11.7.0 | requirement | Video Player updated to 3.2.3 | Video Player |  |
| 11.6.4 | requirement | Minimum Mendix version is now 11.6.4 | Mendix Studio Pro |  |
| 11.6.4 | requirement | Atlas Core updated to 4.3.4 | Atlas Core |  |
| 11.6.4 | requirement | Atlas Web Content updated to 4.3.0 | Atlas Web Content |  |
| 11.6.4 | requirement | Data Widgets updated to 3.8.1 | Data Widgets |  |
| 11.6.4 | requirement | Mendix Feedback Module updated to 4.1.1 | Mendix Feedback Module |  |
| 11.6.4 | requirement | Web Actions updated to 2.11.2 | Web Actions |  |
| 11.6.4 | requirement | Accessibility Helper updated to 2.2.2 | Accessibility Helper |  |
| 11.6.4 | requirement | Accordion updated to 2.3.5 | Accordion |  |
| 11.6.4 | requirement | Badge updated to 3.2.3 | Badge |  |
| 11.6.4 | requirement | Badge Button updated to 3.2.2 | Badge Button |  |
| 11.6.4 | requirement | Barcode Scanner updated to 2.5.1 | Barcode Scanner |  |
| 11.6.4 | requirement | Charts updated to 6.3.0 | Charts |  |
| 11.6.4 | requirement | Fieldset updated to 3.2.2 | Fieldset |  |
| 11.6.4 | requirement | HTML Element updated to 1.2.5 | HTML Element |  |
| 11.6.4 | requirement | Language Selector updated to 1.1.4 | Language Selector |  |
| 11.6.4 | requirement | Pop-up Menu updated to 4.0.3 | Pop-up Menu |  |
| 11.6.4 | requirement | Progress Bar updated to 3.2.3 | Progress Bar |  |
| 11.6.4 | requirement | Progress Circle updated to 3.3.3 | Progress Circle |  |
| 11.6.4 | requirement | Range Slider updated to 3.0.1 | Range Slider |  |
| 11.6.4 | requirement | Rating updated to 3.2.2 | Rating |  |
| 11.6.4 | requirement | Slider updated to 3.0.2 | Slider |  |
| 11.6.4 | requirement | Timeline updated to 3.2.3 | Timeline |  |
| 11.6.4 | requirement | Tooltip updated to 1.5.1 | Tooltip |  |
| 11.6.4 | requirement | Video Player updated to 3.2.4 | Video Player |  |
| 11.6.3 | requirement | Minimum Mendix version is now 11.6.3 | Mendix Studio Pro |  |
| 11.6.3 | requirement | Atlas Core updated to 4.3.2 | Atlas Core |  |
| 11.6.3 | requirement | Atlas Web Content updated to 4.2.0 | Atlas Web Content |  |
| 11.6.3 | requirement | Data Widgets updated to 3.8.0 | Data Widgets |  |
| 11.6.3 | requirement | Mendix Feedback Module updated to 4.0.4 | Mendix Feedback Module |  |
| 11.6.3 | requirement | Web Actions updated to 2.11.1 | Web Actions |  |
| 11.6.3 | requirement | Accessibility Helper updated to 2.2.1 | Accessibility Helper |  |
| 11.6.3 | requirement | Accordion updated to 2.3.4 | Accordion |  |
| 11.6.3 | requirement | Badge updated to 3.2.2 | Badge |  |
| 11.6.3 | requirement | Badge Button updated to 3.2.1 | Badge Button |  |
| 11.6.3 | requirement | Barcode Scanner updated to 2.5.0 | Barcode Scanner |  |
| 11.6.3 | requirement | Charts updated to 6.2.3 | Charts |  |
| 11.6.3 | requirement | Combo box updated to 2.7.1 | Combo box |  |
| 11.6.3 | requirement | Fieldset updated to 3.2.1 | Fieldset |  |
| 11.6.3 | requirement | HTML Element updated to 1.2.4 | HTML Element |  |
| 11.6.3 | requirement | Language Selector updated to 1.1.3 | Language Selector |  |
| 11.6.3 | requirement | Pop-up Menu updated to 4.0.2 | Pop-up Menu |  |
| 11.6.3 | requirement | Progress Bar updated to 3.2.2 | Progress Bar |  |
| 11.6.3 | requirement | Progress Circle updated to 3.3.2 | Progress Circle |  |
| 11.6.3 | requirement | Range Slider updated to 3.0.0 | Range Slider |  |
| 11.6.3 | requirement | Rating updated to 3.2.1 | Rating |  |
| 11.6.3 | requirement | Slider updated to 3.0.0 | Slider |  |
| 11.6.3 | requirement | Timeline updated to 3.2.2 | Timeline |  |
| 11.6.3 | requirement | Tooltip updated to 1.4.2 | Tooltip |  |
| 11.6.3 | requirement | Video Player updated to 3.2.3 | Video Player |  |
| 11.6.2 | requirement | Minimum Mendix version is now 11.6.2 | Mendix Studio Pro |  |
| 11.6.2 | requirement | Atlas Core updated to 4.3.0 | Atlas Core |  |
| 11.6.2 | requirement | Atlas Web Content updated to 4.2.0 | Atlas Web Content |  |
| 11.6.2 | requirement | Data Widgets updated to 3.7.0 | Data Widgets |  |
| 11.6.2 | requirement | Nanoflow Commons updated to 6.2.0 | Nanoflow Commons |  |
| 11.6.2 | requirement | Web Actions updated to 2.11.1 | Web Actions |  |
| 11.6.2 | requirement | Accessibility Helper updated to 2.2.1 | Accessibility Helper |  |
| 11.6.2 | requirement | Accordion updated to 2.3.4 | Accordion |  |
| 11.6.2 | requirement | Badge updated to 3.2.2 | Badge |  |
| 11.6.2 | requirement | Badge Button updated to 3.2.1 | Badge Button |  |
| 11.6.2 | requirement | Barcode Scanner updated to 2.5.0 | Barcode Scanner |  |
| 11.6.2 | requirement | Charts updated to 6.2.3 | Charts |  |
| 11.6.2 | requirement | Combo box updated to 2.6.2 | Combo box |  |
| 11.6.2 | requirement | Fieldset updated to 3.2.1 | Fieldset |  |
| 11.6.2 | requirement | HTML Element updated to 1.2.4 | HTML Element |  |
| 11.6.2 | requirement | Language Selector updated to 1.1.3 | Language Selector |  |
| 11.6.2 | requirement | Pop-up Menu updated to 4.0.2 | Pop-up Menu |  |
| 11.6.2 | requirement | Progress Bar updated to 3.2.2 | Progress Bar |  |
| 11.6.2 | requirement | Progress Circle updated to 3.3.2 | Progress Circle |  |
| 11.6.2 | requirement | Range Slider updated to 3.0.0 | Range Slider |  |
| 11.6.2 | requirement | Rating updated to 3.2.1 | Rating |  |
| 11.6.2 | requirement | Slider updated to 3.0.0 | Slider |  |
| 11.6.2 | requirement | Timeline updated to 3.2.2 | Timeline |  |
| 11.6.2 | requirement | Tooltip updated to 1.4.2 | Tooltip |  |
| 11.6.2 | requirement | Video Player updated to 3.2.3 | Video Player |  |
| 11.6.1 | requirement | Minimum Mendix version is now 11.6.1 | Mendix Studio Pro |  |
| 11.6.1 | requirement | Atlas Core updated to 4.3.0 | Atlas Core |  |
| 11.6.1 | requirement | Atlas Web Content updated to 4.2.0 | Atlas Web Content |  |
| 11.6.1 | requirement | Data Widgets updated to 3.7.0 | Data Widgets |  |
| 11.6.1 | requirement | Nanoflow Commons updated to 6.2.0 | Nanoflow Commons |  |
| 11.6.1 | requirement | Web Actions updated to 2.11.1 | Web Actions |  |
| 11.6.1 | requirement | Accessibility Helper updated to 2.2.1 | Accessibility Helper |  |
| 11.6.1 | requirement | Accordion updated to 2.3.4 | Accordion |  |
| 11.6.1 | requirement | Badge updated to 3.2.2 | Badge |  |
| 11.6.1 | requirement | Badge Button updated to 3.2.1 | Badge Button |  |
| 11.6.1 | requirement | Barcode Scanner updated to 2.5.0 | Barcode Scanner |  |
| 11.6.1 | requirement | Charts updated to 6.2.3 | Charts |  |
| 11.6.1 | requirement | Combo box updated to 2.6.2 | Combo box |  |
| 11.6.1 | requirement | Fieldset updated to 3.2.1 | Fieldset |  |
| 11.6.1 | requirement | HTML Element updated to 1.2.4 | HTML Element |  |
| 11.6.1 | requirement | Language Selector updated to 1.1.3 | Language Selector |  |
| 11.6.1 | requirement | Pop-up Menu updated to 4.0.2 | Pop-up Menu |  |
| 11.6.1 | requirement | Progress Bar updated to 3.2.2 | Progress Bar |  |
| 11.6.1 | requirement | Progress Circle updated to 3.3.2 | Progress Circle |  |
| 11.6.1 | requirement | Range Slider updated to 3.0.0 | Range Slider |  |
| 11.6.1 | requirement | Rating updated to 3.2.1 | Rating |  |
| 11.6.1 | requirement | Slider updated to 3.0.0 | Slider |  |
| 11.6.1 | requirement | Timeline updated to 3.2.2 | Timeline |  |
| 11.6.1 | requirement | Tooltip updated to 1.4.2 | Tooltip |  |
| 11.6.1 | requirement | Video Player updated to 3.2.3 | Video Player |  |
| 11.6.0 | requirement | Minimum Mendix version is now 11.6.0 | Mendix Studio Pro |  |
| 11.6.0 | requirement | Atlas Core updated to 4.3.0 | Atlas Core |  |
| 11.6.0 | requirement | Atlas Web Content updated to 4.2.0 | Atlas Web Content |  |
| 11.6.0 | requirement | Data Widgets updated to 3.7.0 | Data Widgets |  |
| 11.6.0 | requirement | Nanoflow Commons updated to 6.2.0 | Nanoflow Commons |  |
| 11.6.0 | requirement | Web Actions updated to 2.11.1 | Web Actions |  |
| 11.6.0 | requirement | Accessibility Helper updated to 2.2.1 | Accessibility Helper |  |
| 11.6.0 | requirement | Accordion updated to 2.3.4 | Accordion |  |
| 11.6.0 | requirement | Badge updated to 3.2.2 | Badge |  |
| 11.6.0 | requirement | Badge Button updated to 3.2.1 | Badge Button |  |
| 11.6.0 | requirement | Barcode Scanner updated to 2.5.0 | Barcode Scanner |  |
| 11.6.0 | requirement | Charts updated to 6.2.3 | Charts |  |
| 11.6.0 | requirement | Combo box updated to 2.6.2 | Combo box |  |
| 11.6.0 | requirement | Fieldset updated to 3.2.1 | Fieldset |  |
| 11.6.0 | requirement | HTML Element updated to 1.2.4 | HTML Element |  |
| 11.6.0 | requirement | Language Selector updated to 1.1.3 | Language Selector |  |
| 11.6.0 | requirement | Pop-up Menu updated to 4.0.2 | Pop-up Menu |  |
| 11.6.0 | requirement | Progress Bar updated to 3.2.2 | Progress Bar |  |
| 11.6.0 | requirement | Progress Circle updated to 3.3.2 | Progress Circle |  |
| 11.6.0 | requirement | Range Slider updated to 2.1.4 | Range Slider |  |
| 11.6.0 | requirement | Rating updated to 3.2.1 | Rating |  |
| 11.6.0 | requirement | Slider updated to 2.1.4 | Slider |  |
| 11.6.0 | requirement | Timeline updated to 3.2.2 | Timeline |  |
| 11.6.0 | requirement | Tooltip updated to 1.4.2 | Tooltip |  |
| 11.6.0 | requirement | Video Player updated to 3.2.3 | Video Player |  |
| 11.4.1 | requirement | Minimum Mendix version is now 11.4.0 | Mendix Studio Pro |  |
| 11.4.1 | requirement | Atlas Core updated to 4.3.0 | Atlas Core |  |
| 11.4.1 | requirement | Atlas Web Content updated to 4.2.0 | Atlas Web Content |  |
| 11.4.0 | requirement | Minimum Mendix version required: 11.4.0 |  |  |
| 11.4.0 | requirement | Administration module updated to 4.4.0 | Administration module |  |
| 11.4.0 | requirement | Atlas Core updated to 4.3.0 | Atlas Core |  |
| 11.4.0 | requirement | Atlas Web Content updated to 4.2.0 | Atlas Web Content |  |
| 11.4.0 | requirement | Data Widgets updated to 3.6.1 | Data Widgets |  |
| 11.4.0 | requirement | Mendix Feedback Module updated to 4.0.3 | Mendix Feedback Module |  |
| 11.4.0 | requirement | Nanoflow Commons updated to 6.1.1 | Nanoflow Commons |  |
| 11.4.0 | requirement | Web Actions updated to 2.11.1 | Web Actions |  |
| 11.4.0 | requirement | Accessibility Helper updated to 2.2.1 | Accessibility Helper |  |
| 11.4.0 | requirement | Accordion updated to 2.3.4 | Accordion |  |
| 11.4.0 | requirement | Badge updated to 3.2.2 | Badge |  |
| 11.4.0 | requirement | Badge Button updated to 3.2.1 | Badge Button |  |
| 11.4.0 | requirement | Barcode Scanner updated to 2.5.0 | Barcode Scanner |  |
| 11.4.0 | requirement | Charts updated to 6.2.3 | Charts |  |
| 11.4.0 | requirement | Combo box updated to 2.6.2 | Combo box |  |
| 11.4.0 | requirement | Fieldset updated to 3.2.1 | Fieldset |  |
| 11.4.0 | requirement | HTML Element updated to 1.2.2 | HTML Element |  |
| 11.4.0 | requirement | Image updated to 1.5.1 | Image |  |
| 11.4.0 | requirement | Language Selector updated to 1.1.3 | Language Selector |  |
| 11.4.0 | requirement | Maps updated to 4.0.0 | Maps |  |
| 11.4.0 | requirement | Pop-up Menu updated to 4.0.2 | Pop-up Menu |  |
| 11.4.0 | requirement | Progress Bar updated to 3.2.2 | Progress Bar |  |
| 11.4.0 | requirement | Progress Circle updated to 3.3.2 | Progress Circle |  |
| 11.4.0 | requirement | Range Slider updated to 2.1.4 | Range Slider |  |
| 11.4.0 | requirement | Rating updated to 3.2.1 | Rating |  |
| 11.4.0 | requirement | Slider updated to 2.1.4 | Slider |  |
| 11.4.0 | requirement | Switch updated to 4.3.0 | Switch |  |
| 11.4.0 | requirement | Timeline updated to 3.2.2 | Timeline |  |
| 11.4.0 | requirement | Tooltip updated to 1.4.2 | Tooltip |  |
| 11.4.0 | requirement | Video Player updated to 3.2.3 | Video Player |  |
| 11.0.5 | requirement | Administration module updated to 4.3.2 | Administration module |  |
| 11.0.5 | requirement | Atlas Core updated to 4.1.3 | Atlas Core |  |
| 11.0.5 | requirement | Atlas Web Content updated to 4.1.0 | Atlas Web Content |  |
| 11.0.5 | requirement | Data Widgets updated to 3.5.0 | Data Widgets |  |
| 11.0.5 | requirement | Mendix Feedback Module updated to 4.0.2 | Mendix Feedback Module |  |
| 11.0.5 | requirement | Nanoflow Commons updated to 6.0.0 | Nanoflow Commons |  |
| 11.0.5 | requirement | Web Actions updated to 2.11.0 | Web Actions |  |
| 11.0.5 | requirement | Accessibility Helper updated to 2.2.1 | Accessibility Helper |  |
| 11.0.5 | requirement | Accordion updated to 2.3.4 | Accordion |  |
| 11.0.5 | requirement | Badge updated to 3.2.2 | Badge |  |
| 11.0.5 | requirement | Badge Button updated to 3.2.1 | Badge Button |  |
| 11.0.5 | requirement | Barcode Scanner updated to 2.5.0 | Barcode Scanner |  |
| 11.0.5 | requirement | Charts updated to 6.2.2 | Charts |  |
| 11.0.5 | requirement | Combo box updated to 2.5.1 | Combo box |  |
| 11.0.5 | requirement | Fieldset updated to 3.2.1 | Fieldset |  |
| 11.0.5 | requirement | HTML Element updated to 1.2.2 | HTML Element |  |
| 11.0.5 | requirement | Image updated to 1.5.0 | Image |  |
| 11.0.5 | requirement | Language Selector updated to 1.1.3 | Language Selector |  |
| 11.0.5 | requirement | Maps updated to 4.0.0 | Maps |  |
| 11.0.5 | requirement | Pop-up Menu updated to 4.0.2 | Pop-up Menu |  |
| 11.0.5 | requirement | Progress Bar updated to 3.2.2 | Progress Bar |  |
| 11.0.5 | requirement | Progress Circle updated to 3.3.2 | Progress Circle |  |
| 11.0.5 | requirement | Range Slider updated to 2.1.4 | Range Slider |  |
| 11.0.5 | requirement | Rating updated to 3.2.1 | Rating |  |
| 11.0.5 | requirement | Slider updated to 2.1.4 | Slider |  |
| 11.0.5 | requirement | Switch updated to 4.2.2 | Switch |  |
| 11.0.5 | requirement | Timeline updated to 3.2.2 | Timeline |  |
| 11.0.5 | requirement | Tooltip updated to 1.4.2 | Tooltip |  |
| 11.0.5 | requirement | Video Player updated to 3.2.3 | Video Player |  |
| 11.0.4 | requirement | Administration module updated to 4.3.2 | Administration module |  |
| 11.0.4 | requirement | Atlas Core updated to 4.1.3 | Atlas Core |  |
| 11.0.4 | requirement | Atlas Web Content updated to 4.1.0 | Atlas Web Content |  |
| 11.0.4 | requirement | Data Widgets updated to 3.5.0 | Data Widgets |  |
| 11.0.4 | requirement | Mendix Feedback Module updated to 4.0.2 | Mendix Feedback Module |  |
| 11.0.4 | requirement | Nanoflow Commons updated to 6.0.0 | Nanoflow Commons |  |
| 11.0.4 | requirement | Web Actions updated to 2.11.0 | Web Actions |  |
| 11.0.4 | requirement | Accessibility Helper updated to 2.2.1 | Accessibility Helper |  |
| 11.0.4 | requirement | Accordion updated to 2.3.4 | Accordion |  |
| 11.0.4 | requirement | Badge updated to 3.2.2 | Badge |  |
| 11.0.4 | requirement | Badge Button updated to 3.2.1 | Badge Button |  |
| 11.0.4 | requirement | Barcode Scanner updated to 2.5.0 | Barcode Scanner |  |
| 11.0.4 | requirement | Charts updated to 6.2.1 | Charts |  |
| 11.0.4 | requirement | Combo box updated to 2.5.1 | Combo box |  |
| 11.0.4 | requirement | Fieldset updated to 3.2.1 | Fieldset |  |
| 11.0.4 | requirement | HTML Element updated to 1.2.2 | HTML Element |  |
| 11.0.4 | requirement | Image updated to 1.5.0 | Image |  |
| 11.0.4 | requirement | Language Selector updated to 1.1.3 | Language Selector |  |
| 11.0.4 | requirement | Maps updated to 4.0.0 | Maps |  |
| 11.0.4 | requirement | Pop-up Menu updated to 4.0.2 | Pop-up Menu |  |
| 11.0.4 | requirement | Progress Bar updated to 3.2.2 | Progress Bar |  |
| 11.0.4 | requirement | Progress Circle updated to 3.3.2 | Progress Circle |  |
| 11.0.4 | requirement | Range Slider updated to 2.1.4 | Range Slider |  |
| 11.0.4 | requirement | Rating updated to 3.2.1 | Rating |  |
| 11.0.4 | requirement | Slider updated to 2.1.4 | Slider |  |
| 11.0.4 | requirement | Switch updated to 4.2.2 | Switch |  |
| 11.0.4 | requirement | Timeline updated to 3.2.2 | Timeline |  |
| 11.0.4 | requirement | Tooltip updated to 1.4.2 | Tooltip |  |
| 11.0.4 | requirement | Video Player updated to 3.2.3 | Video Player |  |
| 10.12.0 | requirement | Minimum Mendix version required: 10.12.0 |  |  |
| 10.12.0 | requirement | Administration module updated to 4.1.0 | Administration module |  |
| 10.12.0 | requirement | Atlas Core updated to 3.15.0 | Atlas Core |  |
| 10.12.0 | requirement | Atlas Web Content updated to 3.6.1 | Atlas Web Content |  |
| 10.12.0 | requirement | Data Widgets updated to 2.24.0 | Data Widgets |  |
| 10.12.0 | requirement | Mendix Feedback Module updated to 3.0.0 | Mendix Feedback Module |  |
| 10.12.0 | requirement | Nanoflow Commons updated to 4.0.4 | Nanoflow Commons |  |
| 10.12.0 | requirement | Web Actions updated to 2.10.0 | Web Actions |  |
| 10.12.0 | requirement | Accessibility Helper updated to 2.2.1 | Accessibility Helper |  |
| 10.12.0 | requirement | Accordion updated to 2.3.4 | Accordion |  |
| 10.12.0 | requirement | Badge updated to 3.2.2 | Badge |  |
| 10.12.0 | requirement | Badge Button updated to 3.2.1 | Badge Button |  |
| 10.12.0 | requirement | Barcode Scanner updated to 2.4.2 | Barcode Scanner |  |
| 10.12.0 | requirement | Charts updated to 6.0.0 | Charts |  |
| 10.12.0 | requirement | Combo box updated to 2.2.0 | Combo box |  |
| 10.12.0 | requirement | Fieldset updated to 3.2.1 | Fieldset |  |
| 10.12.0 | requirement | HTML Element updated to 1.2.1 | HTML Element |  |
| 10.12.0 | requirement | Image updated to 1.4.3 | Image |  |
| 10.12.0 | requirement | Language Selector updated to 1.1.3 | Language Selector |  |
| 10.12.0 | requirement | Maps updated to 4.0.0 | Maps |  |
| 10.12.0 | requirement | Pop-up Menu updated to 4.0.2 | Pop-up Menu |  |
| 10.12.0 | requirement | Progress Bar updated to 3.2.2 | Progress Bar |  |
| 10.12.0 | requirement | Progress Circle updated to 3.3.2 | Progress Circle |  |
| 10.12.0 | requirement | Range Slider updated to 2.1.4 | Range Slider |  |
| 10.12.0 | requirement | Rating updated to 3.2.1 | Rating |  |
| 10.12.0 | requirement | Slider updated to 2.1.4 | Slider |  |
| 10.12.0 | requirement | Switch updated to 4.2.2 | Switch |  |
| 10.12.0 | requirement | Timeline updated to 3.2.2 | Timeline |  |
| 10.12.0 | requirement | Tooltip updated to 1.4.2 | Tooltip |  |
| 10.12.0 | requirement | Video Player updated to 3.2.2 | Video Player |  |
| 5.0.14 | breaking | Changed minimum length password policy setting from 6 to 12. | password policy minimum length |  |
| 5.0.13 | feature | Added AnyChart module. | AnyChart |  |
| 5.0.9 | improvement | Updated the Atlas Web Contents module. | Atlas Web Contents |  |
| 5.0.8 | improvement | Updated widgets and modules. | widgets, modules |  |
| 5.0.8 | fix | Added missing com.mendix.charts.json files in theme folder to avoid 404 errors. | com.mendix.charts.json |  |
| 5.0.7 | improvement | Updated Atlas Core and Data Grid 2 module. | Atlas Core, Data Grid 2 |  |
| 5.0.6 | improvement | Updated Ratings, Switch and Charts widgets. | Ratings, Switch, Charts |  |
| 5.0.0 | feature | Including Atlas Core, Atlas Web Content and Data Grid 2. | Atlas Core, Atlas Web Content, Data Grid 2 |  |
| 3.11.3 | improvement | Updated Mendix Feedback Widget to version 8.2.1. | Mendix Feedback Widget |  |
| 3.9.12 | improvement | Updated Feedback Widget. | Feedback Widget |  |
| 3.9.4 | improvement | Updated Atlas Resources to v1.2.4. | Atlas Resources |  |
| 3.9.0 | improvement | Updated Atlas Resources to v1.2.2. | Atlas Resources |  |
| 3.7.0 | improvement | Updated framework. | framework |  |
| 3.7.0 | improvement | Updated widgets. | widgets |  |
| 3.4.1 | improvement | Updated Atlas UI Resources module to version 1.1.1. | Atlas UI Resources |  |
| 3.4.0 | improvement | Updated Atlas UI Resources module. | Atlas UI Resources |  |
| 3.0.0 | feature | Official release with the Atlas UI Resources module. | Atlas UI Resources |  |
| 2.0.2 | migration-step | Changed configuration setting. |  |  |
| 2.0.1 | improvement | Updated atlas ui library. | atlas ui library |  |
| 2.0.0 | improvement | Updated Atlas UI Library. | Atlas UI Library |  |
| 2.0.0 | improvement | Updated Navigation Layouts. | Navigation Layouts |  |
| 1.2.5 | removal | Removed userlib. | userlib |  |
| 1.2.5 | improvement | New library for Atlas UI. | Atlas UI library |  |
| 1.2.2 | improvement | Theme and modeler update. | theme, modeler |  |
| 1.2.1 | improvement | Updated theme folder. | theme folder |  |

## Blockbax Connector <a id="205725"></a>
Service, Blockbax, Partner, [marketplace](https://marketplace.mendix.com/link/component/205725)

| version | published | min Mendix |
|---|---|---|
| 3.0.1 | 2023-08-02 | 8.18.13 |
| 3.0.0 | 2023-07-31 | 8.18.13 |
| 2.0.0 | 2023-01-03 | 8.18.13 |
| 1.0.0 | 2022-12-30 | 8.18.13 |

## Blockbax Line Chart <a id="214704"></a>
Service, Blockbax, Partner, [marketplace](https://marketplace.mendix.com/link/component/214704)

| version | published | min Mendix |
|---|---|---|
| 2.1.0 | 2024-08-28 | 9.24.2 |
| 1.0.0 | 2023-08-16 | 9.24.2 |

## Bonsure Suite \| Claims Management <a id="208846"></a>
Industry Template, Bonjoy, Partner, [marketplace](https://marketplace.mendix.com/link/component/208846)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2023-03-27 | 9.23.0 |

## Bonsure Suite \| Underwriter <a id="211705"></a>
Industry Template, Bonjoy, Partner, [marketplace](https://marketplace.mendix.com/link/component/211705)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2023-06-14 | ? |

## Bootstrap Tooltip <a id="1939"></a>
Widget, Mendix, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/1939)

| version | published | min Mendix |
|---|---|---|
| 3.2.5 | 2020-11-13 | 7.0.2 |
| 3.2.2 | 2020-08-21 | ? |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 3.2.5 | fix | Fixed bug where selecting attribute over association for Bootstrap Context widget resulted in no data (Ticket #110055). | Bootstrap Context widget |  |
| 3.2.2 | fix | Fixed bug where BootstrapTooltip (context) initialized before widgets available, throwing error and blocking app. | BootstrapTooltip (context) |  |

## Building X Connector <a id="240566"></a>
Module, Siemens, Siemens, [marketplace](https://marketplace.mendix.com/link/component/240566)

| version | published | min Mendix |
|---|---|---|
| 1.0.4 | 2025-05-12 | 10.12.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.0.4 | requirement | Minimum Mendix version requirement is 10.12.1 |  |  |

## Calendar <a id="107954"></a>
Widget, Mendix, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/107954)

| version | published | min Mendix |
|---|---|---|
| 1.0.15 | 2024-04-29 | 7.14.1 |
| 1.0.14 | 2022-11-23 | 7.14.1 |
| 1.0.13 | 2021-06-24 | 7.14.1 |
| 1.0.12 | 2021-05-14 | 7.14.1 |
| 1.0.11 | 2021-04-21 | 7.14.1 |
| 1.0.10 | 2021-04-01 | 7.14.1 |
| 1.0.9 | 2021-02-03 | 7.14.1 |
| 1.0.8 | 2021-01-20 | 7.14.1 |
| 1.0.7 | 2020-11-20 | 7.14.1 |
| 1.0.6 | 2020-07-08 | 7.14.1 |
| 1.0.5 | 2020-06-26 | 7.14.1 |
| 1.0.4 | 2020-06-26 | 7.14.1 |
| 1.0.3 | 2020-04-17 | 7.14.1 |
| 1.0.2 | 2019-05-28 | 7.14.1 |
| 1.0.1 | 2018-12-20 | 7.14.1 |
| 1.0.0 | 2018-11-09 | 7.14.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.0.14 | improvement | Updated moment.js to version 2.29.4 | moment.js |  |
| 1.0.13 | removal | Removed the option 'Show truncated events' | Show truncated events |  |
| 1.0.13 | breaking | Changed behavior when clicking '+ more' to redirect to day view. |  |  |
| 1.0.11 | removal | Removed ability to configure attribute over association attributes for View start/end attributes. | View start attribute, View end attribute |  |

## Calendar <a id="245304"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/245304)

| version | published | min Mendix |
|---|---|---|
| 2.6.0 | 2026-08-24 | 10.22.0 |
| 2.5.0 | 2026-08-05 | 10.22.0 |
| 2.4.0 | 2026-03-25 | 10.22.0 |
| 2.3.0 | 2026-02-19 | 10.22.0 |
| 2.2.0 | 2025-11-13 | 10.22.0 |
| 2.0.0 | 2025-08-14 | 10.22.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.6.0 | breaking | Year view is now part of standard view and will be directly visible if currently using standard view mode. | Year view, standard view mode |  |
| 2.2.0 | breaking | When event time range is disabled, events no longer display start/end time text. | event time range |  |
| 2.2.0 | breaking | Custom view buttons and their captions are now set inside Custom top bar views configuration. | Custom view buttons, Custom top bar views configuration |  |
| 2.0.0 | breaking | Upgrading from v1.x to v2.0.0 requires re-configuring widget. Property panel reorganised; missing/renamed properties reset to defaults. | Calendar widget, property panel, View settings, Custom work-week options |  |

## Camera (deprecated) <a id="1377"></a>
Widget, Mendix, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/1377)

| version | published | min Mendix |
|---|---|---|
| 4.0.3 | 2019-09-18 | 7.13.1 |
| 4.0.2 | 2018-12-19 | 7.13.1 |
| 4.0.1 | 2018-11-09 | 7.13.1 |
| 4.0.0 | 2018-08-24 | 7.13.1 |
| 3.3.2 | 2018-07-05 | 7.13.1 |
| 3.3.1 | 2018-06-08 | 7.13.1 |
| 3.3.0 | 2018-05-15 | 7.13.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 4.0.0 | breaking | Make button text translatable string; reset your caption after update | button text |  |
| 3.3.0 | breaking | Change widget name to Camera |  |  |

## Campaign Lifecycle Management Professional ( CLMPro) <a id="223567"></a>
Solution, Expleogroup, Partner, [marketplace](https://marketplace.mendix.com/link/component/223567)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2024-03-12 | ? |

## Capital Connector <a id="247337"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/247337)

| version | published | min Mendix |
|---|---|---|
| 2512.0.1 | 2026-08-31 | 10.24.8 |
| 2512.0.0 | 2026-05-06 | 10.24.8 |
| 1.1.0 | 2026-02-09 | 10.24.3 |
| 1.0.0 | 2025-09-29 | 10.24.3 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2512.0.1 | fix | Upgrade Jackson databind to version 2.22.2. | Jackson databind |  |
| 2512.0.0 | breaking | DELETE_Task now returns a boolean instead of the response body, or throws an error when operation fails. | DELETE_Task |  |
| 2512.0.0 | breaking | Changed Metadata/ModifiedTime attribute from integer to long. | Metadata/ModifiedTime |  |
| 2512.0.0 | fix | Updated Jackson Databind & Jackson Core to version 2.21.2. | Jackson Databind, Jackson Core |  |

## Carousel <a id="47784"></a>
Widget, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/47784)

| version | published | min Mendix |
|---|---|---|
| 2.3.2 | 2026-04-13 | 9.6.0 |
| 2.3.1 | 2026-02-13 | 9.6.0 |
| 2.3.0 | 2025-08-19 | 9.24.0 |
| 2.2.1 | 2023-09-27 | 9.6.0 |
| 2.2.0 | 2023-06-29 | 9.6.0 |
| 2.1.0 | 2023-06-05 | 9.6.0 |
| 2.0.0 | 2022-03-07 | 9.6.0 |
| 1.4.1 | 2018-07-19 | 7.13.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.3.2 | security | Updated underlying dependencies to mitigate potential security vulnerabilities. |  |  |
| 2.3.0 | requirement | Updated swiper library dependency from v9 to v11. | swiper |  |
| 2.2.0 | requirement | Updated swiper package version to 9.4. | swiper |  |
| 2.2.0 | breaking | DOM changes from wrapper to new structure. |  |  |
| 2.0.0 | feature | Added new properties: autoplay, animation, pagination, navigation, infinite loop, delay. | autoplay, animation, pagination, navigation, infinite loop, delay |  |
| 2.0.0 | breaking | Changed the widget to a pluggable widget. |  |  |
| 2.0.0 | breaking | Changed the library for Carousel widget to use Swiper. | Swiper |  |
| 2.0.0 | breaking | Changed data source selection; now you can put preferred widget inside carousel content. | data source |  |

## CBP Insight Platform  <a id="121223"></a>
Solution, Creativebuildingperformance.co, Partner, [marketplace](https://marketplace.mendix.com/link/component/121223)

| version | published | min Mendix |
|---|---|---|
| 2.0.0 | 2022-10-04 | ? |
| 1.0.0 | 2022-08-17 | ? |

## Charts <a id="105695"></a>
Widget, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/105695)

| version | published | min Mendix |
|---|---|---|
| 6.3.2 | 2026-08-03 | 10.6.0 |
| 6.3.1 | 2026-05-12 | 10.6.0 |
| 6.3.0 | 2026-02-20 | 10.6.0 |
| 6.2.3 | 2025-10-15 | 10.6.0 |
| 6.2.2 | 2025-09-23 | 10.6.0 |
| 6.2.1 | 2025-07-15 | 10.6.0 |
| 6.2.0 | 2025-06-03 | 10.6.0 |
| 6.1.3 | 2026-01-05 | 9.24.0 |
| 6.1.2 | 2025-09-23 | 9.24.0 |
| 6.1.1 | 2025-07-15 | 9.24.0 |
| 6.1.0 | 2025-06-04 | 9.24.0 |
| 6.0.1 | 2025-05-14 | 10.6.0 |
| 6.0.0 | 2025-02-28 | 10.6.0 |
| 5.1.2 | 2025-01-21 | 10.6.0 |
| 5.1.1 | 2024-12-12 | 9.6.0 |
| 5.1.0 | 2024-10-28 | 9.6.0 |
| 5.0.3 | 2024-10-15 | 9.6.0 |
| 5.0.2 | 2024-09-20 | 9.6.0 |
| 5.0.1 | 2024-07-02 | 9.6.0 |
| 5.0.0 | 2024-06-14 | 9.6.0 |
| 4.2.4 | 2023-11-30 | 9.6.0 |
| 4.2.3 | 2023-11-21 | 9.6.0 |
| 4.2.2 | 2023-10-27 | 9.6.0 |
| 4.2.1 | 2023-09-27 | 9.6.0 |
| 4.2.0 | 2023-08-16 | 9.6.0 |
| 4.1.0 | 2023-06-06 | 9.6.0 |
| 4.0.4 | 2023-04-13 | 9.6.0 |
| 4.0.3 | 2023-01-09 | 9.6.0 |
| 4.0.2 | 2022-11-22 | 9.6.0 |
| 4.0.1 | 2022-11-10 | 9.6.0 |
| 4.0.0 | 2022-10-27 | 9.6.0 |
| 3.0.1 | 2022-08-30 | 9.6.0 |
| 3.0.0 | 2022-07-29 | 9.6.0 |
| 2.0.1 | 2022-05-10 | 9.6.0 |
| 2.0.0 | 2021-09-28 | 9.6.0 |
| 1.4.13 | 2022-05-10 | 7.23.0 |
| 1.4.12 | 2021-08-05 | 7.23.0 |
| 1.4.11 | 2021-04-28 | 7.13.1 |
| 1.4.10 | 2020-04-20 | 7.13.1 |
| 1.4.9 | 2020-03-09 | 7.13.1 |
| … 9 older versions | | |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 6.3.1 | breaking | Disabled code-mirror from playground widget for compatibility. Only basic editor available now. | ChartPlayground |  |
| 6.3.0 | breaking | Changed how Static data and Source attribute data are merged. Traces now merged by index with source attribute values overriding static values. | CustomChart |  |
| 6.2.3 | breaking | Changed event data to return more properties instead of only bbox coordinates. | CustomChart |  |
| 6.2.1 | improvement | Updated shared charts dependency. | AreaChart |  |
| 6.2.0 | improvement | Increased version to update shared code. | CustomChart |  |
| 6.1.3 | breaking | Changed event data to return more properties instead of only bbox coordinates. | CustomChart |  |
| 6.1.1 | improvement | Updated shared charts dependency. | AreaChart |  |
| 6.1.0 | improvement | Increased version to update shared code. | CustomChart |  |
| 6.0.0 | requirement | Updated plotly.js library to version 3.0. | plotly.js |  |
| 6.0.0 | feature | Added new widget called custom charts. | CustomChart |  |
| 6.0.0 | feature | Introduced custom chart widget. | CustomChart |  |
| 5.0.0 | removal | Removed the Enable developer mode property. Drag Chart playground widget to chart to edit instead. | Enable developer mode property | ChartPlayground widget |
| 5.0.0 | breaking | Migrated from Ace code editor to CodeMirror editor. New editor compatible with legacy and new widget runtime. | code editor | CodeMirror |
| 4.2.0 | breaking | Line color (LineChart), Marker color (LineChart), On click action (all except PieChart/HeatMap) properties lose configured values. Must reconfigure manually. | Line color, Marker color, On click action, LineChart |  |
| 4.2.0 | migration-step | Reconfigure Line color, Marker color (LineChart), and On click action properties after update. | Line color, Marker color, On click action |  |
| 4.0.3 | improvement | Updated fast-json-patch dependency. | fast-json-patch |  |
| 4.0.2 | security | Updated d3-color library to 3.1.0 to prevent ReDoS. | d3-color |  |
| 4.0.0 | removal | Removed all deprecated chart widgets. Apps must manually replace deprecated widgets with new ones. |  |  |
| 4.0.0 | migration-step | Replace deprecated chart widgets (v2) with new reworked widgets with improved simplified configuration. |  |  |
| 3.0.0 | deprecation | Release Charts v3.0 deprecates old widgets (v2) and brings reworked widgets with improved simplified configuration. |  |  |
| 1.4.12 | removal | Removed deprecated APIs warnings. |  |  |
| 1.4.11 | improvement | Updated plotly.js dependency. | plotly.js |  |
| 1.4.11 | improvement | Updated react-ace dependency and switched brace for ace-builds. | react-ace, ace-builds, brace |  |
| 1.4.11 | security | Patched lodash vulnerability. | lodash |  |
| 1.4.11 | security | Updated fast-json-patch dependency. | fast-json-patch |  |

## Checkbox set selector (Table) <a id="121"></a>
Widget, Mendix, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/121)

| version | published | min Mendix |
|---|---|---|
| 6.7.2 | 2021-04-19 | 9.6.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 6.7.2 | removal | Removed all deprecated methods throwing warnings |  |  |
| 6.7.2 | breaking | Renamed Appearance tab to Display | Appearance tab | Display |

## Ciphix Chat <a id="231492"></a>
Module, Ciphix, Partner, [marketplace](https://marketplace.mendix.com/link/component/231492)

| version | published | min Mendix |
|---|---|---|
| 3.4.2 | 2026-04-16 | 11.0.0 |
| 3.4.0 | 2025-10-30 | 11.0.0 |
| 3.3.0 | 2025-09-26 | 11.0.0 |
| 2.4.2 | 2026-04-10 | 10.0.0 |
| 2.4.0 | 2025-10-29 | 10.0.0 |
| 2.3.0 | 2025-09-26 | 10.0.0 |
| 2.2.1 | 2025-08-13 | 10.0.0 |
| 2.1.2 | 2025-03-20 | 10.0.0 |
| 2.1.1 | 2025-02-14 | 10.0.0 |
| 2.1.0 | 2025-02-12 | 10.0.0 |
| 1.4.0 | 2026-04-03 | 9.24.12 |
| 1.3.0 | 2025-09-26 | 9.24.12 |
| 1.2.1 | 2025-08-13 | 9.24.12 |
| 1.1.2 | 2025-03-20 | 9.24.12 |
| 1.1.1 | 2025-02-14 | 9.24.12 |
| 1.1.0 | 2025-01-29 | 9.24.12 |
| 1.0.1 | 2024-10-01 | 9.24.12 |
| 1.0.0 | 2024-09-24 | 9.24.12 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 3.4.0 | breaking | b-message-avatar-initials was renamed to b-avatar-initials | b-message-avatar-initials, b-avatar-initials | b-avatar-initials |
| 3.4.0 | breaking | b-message-avatar-custom was renamed to b-avatar-custom | b-message-avatar-custom, b-avatar-custom | b-avatar-custom |
| 3.3.0 | improvement | Updated dependencies |  |  |
| 2.4.0 | breaking | b-message-avatar-initials was renamed to b-avatar-initials | b-message-avatar-initials, b-avatar-initials | b-avatar-initials |
| 2.4.0 | breaking | b-message-avatar-custom was renamed to b-avatar-custom | b-message-avatar-custom, b-avatar-custom | b-avatar-custom |
| 2.3.0 | improvement | Updated dependencies |  |  |
| 2.2.1 | migration-step | Delete old Bizzomate widgets from project widgets directory before loading module: bizzomate.Chat.mpk, bizzomate.ChatChannels.mpk, bizzomate.ChatFloatingActionButton.mpk | bizzomate.Chat.mpk, bizzomate.ChatChannels.mpk, bizzomate.ChatFloatingActionButton.mpk |  |
| 2.1.0 | breaking | Rebranded to Ciphix |  |  |
| 2.1.0 | migration-step | Delete old Bizzomate widgets from project widgets directory before loading module: bizzomate.Chat.mpk, bizzomate.ChatChannels.mpk, bizzomate.ChatFloatingActionButton.mpk | bizzomate.Chat.mpk, bizzomate.ChatChannels.mpk, bizzomate.ChatFloatingActionButton.mpk |  |
| 1.4.0 | breaking | b-message-avatar-initials was renamed to b-avatar-initials | b-message-avatar-initials, b-avatar-initials | b-avatar-initials |
| 1.4.0 | breaking | b-message-avatar-custom was renamed to b-avatar-custom | b-message-avatar-custom, b-avatar-custom | b-avatar-custom |
| 1.3.0 | improvement | Updated dependencies |  |  |
| 1.2.1 | migration-step | Delete old Bizzomate widgets from project widgets directory before loading module: bizzomate.Chat.mpk, bizzomate.ChatChannels.mpk, bizzomate.ChatFloatingActionButton.mpk | bizzomate.Chat.mpk, bizzomate.ChatChannels.mpk, bizzomate.ChatFloatingActionButton.mpk |  |
| 1.1.0 | breaking | Rebranded to Ciphix |  |  |
| 1.1.0 | migration-step | Delete old Bizzomate widgets from project widgets directory before loading module: bizzomate.Chat.mpk, bizzomate.ChatChannels.mpk, bizzomate.ChatFloatingActionButton.mpk | bizzomate.Chat.mpk, bizzomate.ChatChannels.mpk, bizzomate.ChatFloatingActionButton.mpk |  |

## Circuit Breaker <a id="119289"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/119289)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2022-01-17 | 8.12.5 |

## Cleanup Test Data <a id="113440"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/113440)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2020-03-19 | 8.5.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.0.0 | requirement | Minimum Mendix version requirement: 8.5.0 |  |  |

## Color Converter <a id="117725"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/117725)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2021-06-14 | 8.18.1 |

## Color Picker <a id="107044"></a>
Widget, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/107044)

| version | published | min Mendix |
|---|---|---|
| 2.1.8 | 2026-07-22 | 9.6.0 |
| 2.1.7 | 2026-06-22 | 9.6.0 |
| 2.1.6 | 2026-05-12 | 9.6.0 |
| 2.1.5 | 2026-03-09 | 9.6.0 |
| 2.1.4 | 2026-02-10 | 9.6.0 |
| 2.1.3 | 2025-03-21 | 9.6.0 |
| 2.1.2 | 2024-08-28 | 9.6.0 |
| 2.1.1 | 2023-09-27 | 9.6.0 |
| 2.1.0 | 2023-06-06 | 9.6.0 |
| 2.0.1 | 2022-02-25 | 9.6.0 |
| 2.0.0 | 2022-02-10 | 9.6.0 |
| 1.1.3 | 2020-01-24 | 7.13.1 |
| 1.1.1 | 2019-08-22 | 7.13.1 |
| 1.1.0 | 2018-11-22 | 7.13.1 |
| 1.0.1 | 2018-07-05 | 7.13.1 |
| 1.0.0 | 2018-06-22 | 7.13.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.1.8 | fix | Fixed issue where widget was not loading in Dojo client due to broken JavaScript bundle. | Color Picker widget |  |
| 2.1.7 | fix | Fixed color picker stuck in drag mode inside popup pages, causing color changes on mouse move. | Color Picker widget |  |
| 2.1.6 | fix | Fixed issue where On change action was not triggering in some cases. | On change action |  |
| 2.1.5 | fix | Fixed widget still changing values in previous Data View context after context switch. | listen to widget setup |  |
| 2.1.3 | fix | Fixed Color Picker not working in React client. | Color Picker widget, React client |  |
| 2.0.1 | breaking | Reorganized widget configuration structure. | widget configuration structure |  |
| 2.0.0 | breaking | Converted into pluggable widget for use with Data grid 2, Gallery and other widgets. | Color Picker widget |  |
| 1.1.1 | fix | Fixed style problem with vertical alignment using AtlasUI v2.x.x. | AtlasUI |  |

## Combo box <a id="219304"></a>
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

## Community Commons <a id="170"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/170)

| version | published | min Mendix |
|---|---|---|
| 11.5.1 | 2026-05-19 | 10.24.0 |
| 11.5.0 | 2026-01-13 | 10.24.0 |
| 11.4.0 | 2025-11-19 | 10.24.0 |
| 11.3.0 | 2025-07-24 | 10.21.0 |
| 11.2.0 | 2025-07-03 | 10.21.0 |
| 11.1.0 | 2025-04-28 | 10.21.0 |
| 11.0.0 | 2025-04-10 | 10.21.0 |
| 10.4.2 | 2026-05-19 | 9.24.36 |
| 10.4.1 | 2026-01-15 | 9.24.36 |
| 10.4.0 | 2025-07-25 | 9.24.36 |
| 10.3.0 | 2025-07-18 | 9.24.36 |
| 10.2.0 | 2025-04-28 | 9.18.0 |
| 10.1.3 | 2025-04-10 | 9.18.0 |
| 10.1.2 | 2025-03-27 | 9.18.0 |
| 10.1.1 | 2025-03-18 | 9.18.0 |
| 10.1.0 | 2025-01-06 | 9.18.0 |
| 10.0.7 | 2024-10-14 | 9.18.0 |
| 10.0.6 | 2024-07-04 | 9.18.0 |
| 10.0.5 | 2024-01-04 | 9.18.0 |
| 10.0.2 | 2023-08-22 | 9.18.0 |
| 10.0.1 | 2023-06-30 | 9.18.0 |
| 10.0.0 | 2023-04-14 | 9.18.0 |
| 9.0.4 | 2023-12-06 | 8.12.0 |
| 9.0.3 | 2023-06-30 | 8.12.0 |
| 9.0.2 | 2022-10-10 | 8.12.0 |
| 9.0.1 | 2022-06-22 | 8.12.0 |
| 9.0.0 | 2022-01-12 | 8.12.0 |
| 8.8.2 | 2023-07-11 | 7.23.22 |
| 8.8.1 | 2023-02-16 | 7.23.22 |
| 8.8.0 | 2022-01-13 | 7.23.22 |
| 8.7.0 | 2021-11-08 | 8.12.0 |
| 8.6.0 | 2021-09-27 | 8.12.0 |
| 8.5.0 | 2021-06-28 | 8.12.0 |
| 8.4.0 | 2021-05-24 | 8.12.0 |
| 8.3.1 | 2020-12-21 | 8.12.0 |
| 8.3.0 | 2020-12-18 | 8.12.0 |
| 8.2.1 | 2021-07-01 | 7.23.22 |
| 8.2.0 | 2019-12-20 | 7.23.6 |
| 8.1.0 | 2019-08-29 | 7.23.6 |
| 8.0.1 | 2019-06-27 | 7.23.4 |
| … 12 older versions | | |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 11.5.1 | improvement | Upgraded pdfbox to 3.0.7 | pdfbox |  |
| 11.5.0 | improvement | Upgraded guava to 33.5.0-jre | guava |  |
| 11.5.0 | improvement | Upgraded owasp-java-html-sanitizer to 20260101.1 | owasp-java-html-sanitizer |  |
| 11.5.0 | improvement | Upgraded commons-io to 2.21.0 | commons-io |  |
| 11.5.0 | improvement | Upgraded pdfbox to 3.0.6 | pdfbox |  |
| 11.5.0 | improvement | Upgraded commons-lang3 to 3.20.0 | commons-lang3 |  |
| 11.5.0 | improvement | Upgraded commons-text to 1.14.0 | commons-text |  |
| 11.5.0 | feature | Added the pdfbox-io 3.0.6 dependency | pdfbox-io |  |
| 11.4.0 | requirement | Upgraded the module to 10.24.0 |  |  |
| 11.3.0 | security | Upgraded Commons-lang3 library to version 3.18.0 to resolve CVE-2025-48924 | commons-lang3 |  |
| 11.1.0 | improvement | Upgraded Guava dependency to 33.4.7, removes jsr305 version 3.0.2 dependency causing code quality scanning issues | guava, jsr305 |  |
| 11.0.0 | requirement | Upgraded the Community Commons module to Mendix version 10.21.0 |  |  |
| 11.0.0 | deprecation | Deprecated Misc.getRuntimeVersion Java method, use Core.getRuntimeVersion instead | Misc.getRuntimeVersion | Core.getRuntimeVersion |
| 11.0.0 | deprecation | Deprecated Misc.getModelVersion Java method, use Core.getModelVersion instead | Misc.getModelVersion | Core.getModelVersion |
| 10.4.2 | improvement | Upgraded pdfbox to 2.0.36 | pdfbox |  |
| 10.4.1 | improvement | Upgraded owasp-java-html-sanitizer to 20260101.1 | owasp-java-html-sanitizer |  |
| 10.4.0 | security | Upgraded Commons-lang3 library to version 3.18.0 to resolve CVE-2025-48924 | commons-lang3 |  |
| 10.3.0 | requirement | Upgraded the Community Commons module to Mendix version 9.24.36 |  |  |
| 10.2.0 | improvement | Upgraded Guava dependency to 33.4.7, removes jsr305 version 3.0.2 dependency causing code quality scanning issues | guava, jsr305 |  |
| 10.1.0 | deprecation | Deprecated the 'length' parameter of the StringUtils Hash java action. Hash length will always be 32 bytes, 64 hex characters | StringUtils Hash |  |
| 10.0.7 | improvement | Updated the Apache Commons IO dependency to 2.17.0 | commons-io |  |
| 10.0.5 | improvement | Updated the Apache PDFBox dependency to 2.0.30 | pdfbox |  |
| 10.0.2 | migration-step | Included a migration file for the Java dependencies for Studio Pro 10 compatibility |  |  |
| 10.0.1 | improvement | Updated the Guava dependency to 32.0.1 | guava |  |
| 10.0.0 | requirement | Updated the module to Studio Pro 9.18, so it can be used in Studio Pro 10 |  |  |
| 10.0.0 | improvement | Updated the Apache Commons Lang dependency to version 3.12.0 | commons-lang |  |
| 10.0.0 | feature | Added a dependency on Apache Commons Text version 1.10.0 because some Apache Commons Lang functionality moved there | commons-text |  |
| 9.0.4 | improvement | Updated the Apache PDFBox dependency to 2.0.30 | pdfbox |  |
| 9.0.3 | improvement | Updated the Guava dependency to 32.0.1 | guava |  |
| 9.0.1 | improvement | Upgrade commons-io dependency from 2.8.0 to 2.11.0 | commons-io |  |
| 9.0.0 | removal | Removed encrypt/decrypt functionality. Java Actions EncryptString, DecryptString, and encryptMembersIfChanged have been removed | EncryptString, DecryptString, encryptMembersIfChanged |  |
| 8.8.2 | improvement | Updated the Guava dependency to 32.0.1 | guava |  |
| 8.8.1 | improvement | Updated Apache Commons from 2.8.0 to 2.11.0 | commons-io |  |
| 8.8.0 | improvement | Updated the OWASP Java HTML Sanitizer dependency | owasp-java-html-sanitizer |  |
| 8.7.0 | improvement | Updated owasp-java-html-sanitizer to 20211018.2 | owasp-java-html-sanitizer |  |
| 8.7.0 | deprecation | Deprecated all encryption related functionality. Use the encryption-module instead |  |  |
| 8.5.0 | improvement | Updated Guava to 30.1.1 to be the same version as used by the SSO module | guava |  |
| 8.5.0 | security | Updated PDFBox to 2.0.24 because of a vulnerability in that library | pdfbox |  |
| 8.4.0 | improvement | Updated library dependencies. Community Commons ships with Apache Commons IO 2.8, Apache Commons Lang 3.11, Guava 30.0 | commons-io, commons-lang, guava |  |
| 8.3.1 | requirement | Updated the Community Commons module to support Mendix Studio Version 9 |  |  |
| 8.3.0 | requirement | Updated the Community Commons module to Mendix Studio Pro 8.12.0 |  |  |
| 8.2.1 | improvement | Updated library dependencies. Community Commons ships with Apache Commons IO 2.8, Apache Commons Lang 3.11, Guava 30.0, PDFBox 2.0.24 | commons-io, commons-lang, guava, pdfbox |  |
| 8.1.0 | requirement | Minimum required Mendix version is 7.23.6 |  |  |
| 8.1.0 | breaking | Changed Logging.java so TimerEnd now returns the time taken in milliseconds | Logging.TimerEnd |  |
| 8.0.1 | removal | Removed the deprecated RegexTest action. Use the isMatch() function in microflow expressions instead | RegexTest | isMatch() |
| 8.0.1 | breaking | Changed Java references to the LogNodes.CommunityCommons enum to point to the name instead of the caption |  |  |
| 8.0.0 | requirement | Converted to Mendix 7.23.4 |  |  |
| 7.4.0 | security | Updated Guava dependency to 27.0 in order to fix a security vulnerability warning | guava |  |
| 7.4.0 | migration-step | Delete all jar files that have a `.CommunityCommons.Required` flag before upgrading |  |  |
| 7.3.0 | removal | Removed deprecated Log action | Log |  |
| 7.3.0 | removal | Removed deprecated SimpleLog action | SimpleLog |  |
| 7.3.0 | removal | Removed deprecated StringLength action | StringLength |  |
| 7.3.0 | improvement | Upgraded PDFBox dependency to 2.0.13. Delete pdfbox-2.0.11.jar and fontbox-2.0.11.jar from userlib before upgrading | pdfbox |  |
| 7.2.0 | migration-step | Delete all `.jar` files from userlib with accompanying `.CommunityCommons.RequiredLib` file before upgrading |  |  |
| 7.2.0 | improvement | Updated and reduced dependencies on third-party libraries to mitigate potential security vulnerabilities |  |  |
| 7.2.0 | breaking | Re-implemented the XSSSanitize action which will require you to re-implement the call if you use it | XSSSanitize |  |
| 7.1.0 | removal | Removed session based locking mechanism as it has become obsolete in Mx7 |  |  |
| 6.3.1 | fix | Added Batik library not provided by Mendix Runtime for Mendix 7. Fixes NoClassDefined error when using Sanitize function. | Batik library |  |
| 6.3.0 | requirement | Module converted to Mendix 7.1.0. |  |  |
| 6.3.0 | migration-step | Added jar which is not provided by runtime anymore in Mendix 7. |  |  |

## Company Search <a id="212748"></a>
Industry Template, TOCnDix, Partner, [marketplace](https://marketplace.mendix.com/link/component/212748)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2023-06-30 | 9.22.0 |

## Confluence Connector <a id="117622"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/117622)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2021-06-07 | 8.18.4 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.0.0 | requirement | Installation requires Deep link module, Encryption, and Community Commons dependencies. | Deep link module, Encryption, Community Commons |  |

## Control Tower <a id="121124"></a>
Solution, CAPE, Partner, [marketplace](https://marketplace.mendix.com/link/component/121124)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2022-08-04 | ? |

## Conversational UI <a id="239450"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/239450)

| version | published | min Mendix |
|---|---|---|
| 7.3.1 | 2026-10-05 | 11.12.4 |
| 7.3.0 | 2026-08-31 | 11.12.3 |
| 7.2.0 | 2026-08-07 | 11.12.2 |
| 7.1.0 | 2026-07-22 | 11.12.1 |
| 7.0.0 | 2026-07-02 | 11.12.0 |
| 6.3.0 | 2026-05-28 | 10.24.13 |
| 6.2.0 | 2026-04-15 | 10.24.13 |
| 6.1.0 | 2026-04-17 | 10.24.13 |
| 6.0.2 | 2026-03-18 | 10.24.13 |
| 6.0.1 | 2026-03-11 | 10.24.13 |
| 6.0.0 | 2026-03-09 | 10.24.13 |
| 5.5.0 | 2026-01-19 | 10.24.13 |
| 5.4.0 | 2025-12-22 | 10.24.13 |
| 5.3.0 | 2025-11-21 | 10.24.0 |
| 5.2.1 | 2025-11-07 | 10.24.0 |
| 5.2.0 | 2025-10-29 | 10.24.0 |
| 5.1.0 | 2025-09-19 | 10.24.0 |
| 5.0.1 | 2025-08-13 | 10.24.0 |
| 5.0.0 | 2025-08-08 | 10.24.0 |
| 4.1.0 | 2025-07-21 | 10.21.0 |
| 4.0.0 | 2025-07-02 | 10.21.0 |
| 3.2.0 | 2025-06-13 | 10.21.0 |
| 3.1.0 | 2025-05-09 | 10.21.0 |
| 3.0.0 | 2025-04-08 | 10.21.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 7.3.0 | requirement | Upgraded to Mendix 11.12.3. |  |  |
| 7.3.0 | improvement | Messages sent with tool calls from assistant now returned to model as part of request, preventing content repetition in final response. |  |  |
| 7.2.0 | requirement | Upgrade to Mendix 11.12.2. |  |  |
| 7.2.0 | feature | Agent Chats now support streaming for real-time model responses. Requires text generation model support and Streaming (Frontend) enabled by AgentAdmin. |  |  |
| 7.1.0 | requirement | Upgrade to Mendix 11.12.1. |  |  |
| 7.0.0 | requirement | Upgraded to Mendix 11.12 and supports Atlas 4 if enabled. |  |  |
| 6.3.0 | improvement | GenAI components styling consolidated from AgentCommons and ConversationalUI into ConversationalUI to resolve inconsistent rendering. | AgentCommons |  |
| 6.0.0 | feature | User Access and Approval feature added for GenAI Commons and ConversationalUI to make tool calls visible and allow user control for execution or rejection. | GenAI Commons, AgentCommons |  |
| 6.0.0 | breaking | Tool call response now sent back to microflow without final assistant response; tool messages persisted and sent with next messages. |  |  |
| 6.0.0 | breaking | SaveToolCallHistory boolean on request object controls tool call history persistence; ignored if any tool set for user visibility. |  |  |
| 6.0.0 | breaking | Custom styling application changed to make module more compatible with different design systems than Atlas. |  |  |
| 6.0.0 | requirement | Compatible with GenAI Commons 6.0.0 and AgentCommons 3.0.0. | GenAI Commons, AgentCommons |  |
| 5.4.0 | requirement | Upgraded to Mendix LTS version 10.24.13. |  |  |
| 5.3.0 | feature | New capability and role added to inspect agent and AI interaction traces at runtime for observability and troubleshooting. |  |  |
| 5.3.0 | requirement | AgentCommons module is now a dependency for ConversationalUI to filter agents in UI. | AgentCommons |  |
| 5.1.0 | improvement | ConversationId of ChatContext automatically set when GenAICommons.Response contains an Id for trace linkage. | GenAI Commons |  |
| 5.0.0 | requirement | Upgraded to Mendix Studio Pro version 10.24. |  |  |
| 4.0.0 | removal | Prompt Management removed; capabilities now in AgentCommons. Export existing prompts from Prompt_Overview before updating. | Prompt Management | AgentCommons |
| 4.0.0 | migration-step | Existing prompts must be exported from Prompt_Overview page and imported into Agent_Overview for migration. | Prompt Management |  |
| 4.0.0 | migration-step | To replace prompt variables with Context Object values, use PromptToUse_GetAndReplace microflow from AgentCommons or call agent directly. |  |  |
| 4.0.0 | breaking | Styling variables made compatible with Atlas 4 in Mendix Studio Pro 11. |  |  |
| 3.2.0 | feature | New _ID attribute implemented in GenAICommons for use. | GenAI Commons, _ID |  |
| 3.0.0 | removal | Module no longer bundled with GenAICommons and MxGenAIConnector. | GenAICommons, MxGenAIConnector |  |
| 3.0.0 | requirement | Updated to Mendix Studio Pro 10.21.0. |  |  |

## Core Delta <a id="213912"></a>
Module, Mendix, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/213912)

| version | published | min Mendix |
|---|---|---|
| 1.1.0 | 2024-05-28 | 10.6.9 |
| 1.0.6 | 2024-05-03 | 9.6.10 |
| 1.0.5 | 2024-03-12 | 9.6.10 |
| 1.0.0 | 2023-07-24 | 9.6.10 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.1.0 | requirement | Minimum Mendix version raised to 10.6.9 |  |  |
| 1.0.6 | fix | Images were loaded with base64 encoding instead of direct images from resource directory | mx_ui images |  |
| 1.0.5 | improvement | Updated to latest 9.24 LTS version |  |  |

## Count Down Timer with Action <a id="117645"></a>
Widget, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/117645)

| version | published | min Mendix |
|---|---|---|
| 1.0.2 | 2021-08-17 | 8.12.7 |
| 1.0.1 | 2021-06-11 | 8.12.7 |
| 1.0.0 | 2021-06-11 | 8.12.7 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.0.2 | requirement | Upgrade for Mendix 9 and up |  |  |

## CoverSuite <a id="225249"></a>
Solution, Infosistema, Partner, [marketplace](https://marketplace.mendix.com/link/component/225249)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2024-04-24 | ? |

## Crashlytics <a id="119621"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/119621)

| version | published | min Mendix |
|---|---|---|
| 3.0.0 | 2022-08-17 | 9.6.8 |
| 2.0.0 | 2022-02-26 | 9.6.8 |
| 1.0.0 | 2022-02-11 | 9.6.8 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 3.0.0 | requirement | Logging API updated for compatibility with Mendix 9.16+. Use this version if running Mendix 9.16 or later. | logging API |  |
| 2.0.0 | migration-step | JavaScript libraries moved from themesource to javascriptsource directory. Re-import the module after upgrade. | JavaScript libraries |  |

## CsvServices <a id="1911"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/1911)

| version | published | min Mendix |
|---|---|---|
| 2.5.0 | 2023-06-22 | 9.24.0 |
| 2.4.0 | 2022-10-10 | 9.18.0 |
| 2.3.0 | 2019-10-21 | 7.23.8 |
| 2.2.1 | 2019-10-20 | 7.23.8 |
| 2.2.0 | 2019-10-18 | 7.23.8 |
| 2.1 | 2017-06-01 | 7.0.2 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.5.0 | requirement | Update to Mendix 9.24 |  |  |
| 2.4.0 | requirement | Upgrade to Mendix 9.18 |  |  |
| 2.2.0 | requirement | Upgrade to mendix 7.23.8 |  |  |
| 2.1 | requirement | Upgrade to Mendix 7 |  |  |

## DALL-E 2 Connector <a id="206059"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/206059)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2023-01-09 | 9.21.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.0.0 | requirement | Minimum Mendix version requirement: 9.21.0 | Mendix |  |

## Data Importer <a id="219833"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/219833)

| version | published | min Mendix |
|---|---|---|
| 1.6.3 | 2026-08-04 | 10.24.11 |
| 1.6.2 | 2026-04-23 | 10.24.11 |
| 1.6.1 | 2026-03-16 | 10.24.11 |
| 1.6.0 | 2025-12-12 | 10.24.11 |
| 1.5.3 | 2025-11-10 | 10.21.0 |
| 1.5.2 | 2025-07-02 | 10.21.0 |
| 1.5.1 | 2025-07-01 | 10.21.0 |
| 1.5.0 | 2025-04-29 | 10.21.0 |
| 1.4.1 | 2025-06-10 | 10.7.0 |
| 1.4.0 | 2025-04-28 | 10.7.0 |
| 1.3.1 | 2024-12-18 | 10.7.0 |
| 1.3.0 | 2024-10-30 | 10.7.0 |
| 1.2.3 | 2024-08-02 | 10.7.0 |
| 1.2.2 | 2024-07-23 | 10.7.0 |
| 1.2.1 | 2024-03-27 | 10.7.0 |
| 1.2.0 | 2024-02-27 | 10.7.0 |
| 1.1.0 | 2024-01-30 | 10.7.0 |
| 1.0.0 | 2023-12-06 | 10.4.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.6.3 | requirement | Upgraded Log4j API to version 2.25.x | Log4j API |  |
| 1.6.2 | requirement | Upgraded log4j api to v2.25.3 | log4j-api |  |
| 1.6.1 | requirement | Update log4j-api v2.24.3 to v2.25.3 | log4j-api |  |
| 1.6.0 | requirement | Updated module to Studio Pro v 10.24.11 | Studio Pro |  |
| 1.5.2 | requirement | Updated apache commons csv to v1.14.0 | apache commons csv |  |
| 1.5.0 | requirement | Updated studio pro minimum version to 10.21.0 to support Mendix 11 | Studio Pro |  |
| 1.5.0 | requirement | Updated POI library to version 5.4.0 | POI library |  |
| 1.4.1 | requirement | Upgraded Apache POI version to 5.4.0 | Apache POI |  |
| 1.4.0 | improvement | Entity access rules applied for Data Importer runtime module. |  |  |
| 1.2.3 | requirement | Apache POI library update from 5.2.5 to 5.3.0 | Apache POI |  |
| 1.2.1 | security | Fixed vulnerability in data-importer caused by Apache commons-compress v1.21 | Apache commons-compress |  |

## Data Protection for Mendix <a id="214497"></a>
Module, Emixa, Partner, [marketplace](https://marketplace.mendix.com/link/component/214497)

| version | published | min Mendix |
|---|---|---|
| 4.0.0 | 2026-08-05 | 11.6.6 |
| 1.1.0 | 2025-04-30 | 9.18.0 |
| 1.0.0 | 2023-08-04 | 9.12.6 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 4.0.0 | requirement | Minimum Mendix version requirement updated to 11.6.6 |  |  |
| 1.1.0 | requirement | Mendix version updated to 9.18.0 minimum |  |  |

## Data Widgets <a id="116540"></a>
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

## Database Connector <a id="2888"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/2888)

| version | published | min Mendix |
|---|---|---|
| 7.0.5 | 2026-09-09 | 10.24.11 |
| 7.0.4 | 2026-08-12 | 10.24.11 |
| 7.0.3 | 2026-05-11 | 10.24.11 |
| 7.0.2 | 2025-12-12 | 10.24.11 |
| 7.0.1 | 2025-07-30 | 10.21.0 |
| 7.0.0 | 2025-04-02 | 10.21.0 |
| 6.0.3 | 2024-02-26 | 9.18.4 |
| 6.0.2 | 2023-12-27 | 9.18.4 |
| 6.0.1 | 2023-09-21 | 9.18.4 |
| 6.0.0 | 2023-03-24 | 9.18.4 |
| 5.0.7 | 2024-05-14 | 8.18.29 |
| 5.0.6 | 2022-12-13 | 8.18.20 |
| 5.0.5 | 2022-11-23 | 8.18.20 |
| 5.0.4 | 2022-10-31 | 8.18.20 |
| 5.0.3 | 2022-09-15 | 8.18.19 |
| 5.0.2 | 2022-03-22 | 8.12.4 |
| 5.0.1 | 2022-03-08 | 8.12.4 |
| 5.0.0 | 2021-08-03 | 8.12.4 |
| 4.0.0 | 2020-12-21 | 8.12.4 |
| 3.1.0 | 2020-04-07 | 8.8.0 |
| 3.0.0 | 2020-04-07 | 8.6.0 |
| 2.3.0 | 2019-11-21 | 7.23.8 |
| 2.2.1 | 2019-07-25 | 7.23.7 |
| 2.2.0 | 2019-07-24 | 7.23.7 |
| 2.1.0 | 2019-07-24 | 7.0.2 |
| 2.0.0 | 2019-06-11 | 7.23.5 |
| 1.0.2 | 2017-06-20 | 7.0.2 |
| 1.0.1 | 2017-03-13 | 7.0.2 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 7.0.5 | security | Resolved CVE-2026-55856 through CVE-2026-55860 and CVE-2026-61700 by upgrading mariadb to 2.7.14 | mariadb |  |
| 7.0.4 | security | Fixed CVE 2026-54291 by upgrading postgresql version to 42.7.12 | postgresql |  |
| 7.0.3 | security | Resolved CVE-2026-42198 by upgrading postgresql to 42.7.11 | postgresql |  |
| 7.0.2 | security | Resolved CVE-2025-59250 by upgrading the Microsoft SQL Server JDBC driver to version 12.10.2.jre11 | Microsoft SQL Server JDBC driver |  |
| 7.0.2 | fix | Fixed issue where Callable Statement failed to process null DATE values in cursor result set, causing query execution errors [#241877] | Callable Statement |  |
| 7.0.1 | security | Fixed CVE-2024-1597, upgraded to PostgreSQL 42.4.4 | PostgreSQL |  |
| 7.0.0 | requirement | Updated the module to Studio-Pro version 10.21.0 |  |  |
| 6.0.3 | security | Fixed CVE-2024-1597, upgraded to postgresql@42.4.4 | postgresql |  |
| 6.0.2 | security | Fixed CVE-2014-8314, upgraded ngdbc to 2.19.15 | ngdbc |  |
| 6.0.2 | improvement | Upgraded slf4j to 2.0.7 | slf4j |  |
| 6.0.1 | migration-step | Included a migration file for the Java dependencies for Studio Pro 10 compatibility | Java dependencies |  |
| 6.0.0 | requirement | Updated module to Framework version 9.18.4 |  |  |
| 5.0.7 | security | Fixed CVE-2024-1597, upgraded PostgreSQL jar to 42.4.4.jar | PostgreSQL |  |
| 5.0.6 | security | Fixed CVE-2022-41946, upgraded postgresql to 42.4.3 | postgresql |  |
| 5.0.5 | migration-step | Removed unwanted jar files from the userlib [#169589] | userlib |  |
| 5.0.4 | security | Fixed CVE-2022-41853, updated hsqldb (HyperSQL DataBase) to 2.7.1 | hsqldb |  |
| 5.0.3 | security | Upgraded to postgresql-42.4.1 to fix high severity vulnerability in 42.3.3 | postgresql |  |
| 5.0.2 | fix | Fixed issue where some database drivers would not load [#144326] | database drivers |  |
| 5.0.2 | improvement | Upgraded some database drivers | database drivers |  |
| 5.0.1 | improvement | Upgraded module dependencies |  |  |
| 4.0.0 | requirement | Updated module to Framework version 8.12.4 |  |  |
| 4.0.0 | improvement | Updated drivers to match those of Framework version 8.12.4 | drivers |  |
| 4.0.0 | breaking | Removed calls to deprecated methods |  |  |
| 3.1.0 | requirement | Updated to Mendix 8.8.0 |  |  |
| 3.0.0 | requirement | Updated to Mendix 8.6.0 |  |  |
| 2.3.0 | requirement | Updated to be compatible with Mendix Studio Pro version 7.23.8 |  |  |
| 2.2.1 | requirement | Minor update to be compatible with 7.23.7 (Build 55882) |  |  |
| 2.2.0 | requirement | Updated to be compatible with Mendix 7.23.7 |  |  |
| 2.2.0 | removal | Removed unused jackson libraries: jackson-core-2.6.6.jar, jackson-databind-2.6.6.jar, jackson-annotations-2.6.0.jar | jackson-core-2.6.6.jar, jackson-databind-2.6.6.jar, jackson-annotations-2.6.0.jar |  |
| 2.1.0 | removal | Removed unused jackson libraries: jackson-core-2.6.6.jar, jackson-databind-2.6.6.jar, jackson-annotations-2.6.0.jar | jackson-core-2.6.6.jar, jackson-databind-2.6.6.jar, jackson-annotations-2.6.0.jar |  |
| 2.0.0 | breaking | Removed references to Float and Currency, as they are deprecated | Float, Currency |  |
| 2.0.0 | removal | Removed support to HashedString as an attribute type | HashedString |  |
| 2.0.0 | removal | Removed support for testing against Redshift | Redshift |  |
| 2.0.0 | requirement | Supported for Mendix 7 LTS (from 7.23.5) and Mendix 8 |  |  |
| 1.0.2 | fix | HikaryCP no longer requires to write into System Properties, fixing java.security.AccessControlException [#4] | HikaryCP |  |
| 1.0.1 | fix | Fixed Mendix 7 compatibility by adding org.slf4j.slf4j-api.jar (dependency of HikariCP) | org.slf4j.slf4j-api.jar |  |
| 1.0.1 | improvement | Upgraded HikariCP database connection pooling library to version 2.6.1 (was 2.4.6) | HikariCP |  |

## Database Scrambler <a id="208693"></a>
Module, Ciphix, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/208693)

| version | published | min Mendix |
|---|---|---|
| 2.1.2 | 2024-07-19 | 10.0.0 |
| 2.0.0 | 2023-08-03 | 10.0.0 |
| 1.0.0 | 2023-03-24 | 9.12.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.0.0 | feature | Added support for Mendix 10. |  |  |

## DatabaseReplication <a id="160"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/160)

| version | published | min Mendix |
|---|---|---|
| 9.3.2 | 2026-09-24 | 10.24.11 |
| 9.3.1 | 2026-02-18 | 10.24.11 |
| 9.3.0 | 2025-12-10 | 10.24.11 |
| 9.2.1 | 2025-11-07 | 10.21.0 |
| 9.2.0 | 2025-08-05 | 10.21.0 |
| 9.1.0 | 2025-04-16 | 10.21.0 |
| 9.0.0 | 2025-02-10 | 10.18.0 |
| 8.2.2 | 2025-04-04 | 9.18.4 |
| 8.2.1 | 2024-11-25 | 9.18.4 |
| 8.2.0 | 2024-07-26 | 9.18.4 |
| 8.1.4 | 2024-05-24 | 9.18.4 |
| 8.1.3 | 2023-08-31 | 9.18.4 |
| 8.1.2 | 2023-07-10 | 9.18.4 |
| 8.1.1 | 2023-06-01 | 9.18.4 |
| 8.1.0 | 2023-04-18 | 9.18.4 |
| 8.0.2 | 2023-03-17 | 9.0.5 |
| 8.0.1 | 2021-08-10 | 9.0.5 |
| 8.0.0 | 2021-07-19 | 9.0.5 |
| 7.1.5 | 2024-05-27 | 8.18.23 |
| 7.1.4 | 2023-07-10 | 8.18.23 |
| 7.1.3 | 2023-06-01 | 8.18.23 |
| 7.1.2 | 2023-03-17 | 8.18.23 |
| 7.1.1 | 2021-08-10 | 8.12.4 |
| 7.1.0 | 2021-07-19 | 8.12.4 |
| 7.0.1 | 2021-05-05 | 8.12.4 |
| 7.0.0 | 2020-12-22 | 8.12.4 |
| 6.1.1 | 2020-11-19 | 7.23.7 |
| 6.1.0 | 2020-08-28 | 7.23.7 |
| 6.0.2 | 2020-04-10 | 7.23.7 |
| 6.0.1 | 2019-08-19 | 7.23.7 |
| 6.0.0 | 2019-06-20 | 7.23.5 |
| 4.13.0 | 2019-02-11 | 7.1.1 |
| 4.11.0 | 2018-01-05 | 7.1.1 |
| 4.10.1 | 2017-02-24 | 7.0.2 |
| 4.10 | 2017-02-22 | 7.0.2 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 9.3.2 | security | Fixed CVE 2026-54291 by upgrading postgresql version to 42.7.12 | postgresql |  |
| 9.3.0 | requirement | Upgraded module to Mendix version 10.24.11 | Mendix |  |
| 9.2.1 | improvement | Upgraded widgets in TableMapping_Edit page to pluggable widgets using React | TableMapping_Edit, widgets |  |
| 9.2.0 | improvement | Upgraded all widgets to pluggable widgets using React | widgets |  |
| 9.1.0 | requirement | Upgraded module to Mendix version 10.21.0 for compatibility with future versions | Mendix |  |
| 9.1.0 | improvement | Removed usages of deprecated methods in com.mendix.core.Core from implementation | com.mendix.core.Core |  |
| 9.1.0 | improvement | Updated replication library to version 1.0.6 without deprecated com.mendix.core.Core methods | replication library |  |
| 9.0.0 | requirement | Upgraded module to Mendix version 10.18.0 for compatibility with future versions | Mendix |  |
| 8.2.2 | breaking | Removed usages of enum values for Float and Currency data types no longer supported with mx model reflection module 8.0.3+ | Float, Currency, mx model reflection module |  |
| 8.2.1 | fix | Fixed issue with Oracle DB template imports where unlimited string comparison threw database error | Oracle DB, template imports |  |
| 8.2.0 | breaking | Now explicitly disallow adding object parameters when manually executing import calls using Import and Run scheduled events buttons | object parameters, Import call, Planned import action |  |
| 8.1.4 | improvement | Updated replication library to 1.0.4; fixes rollback failure in Mendix 10 due to rollbackTransAction rename | replication library, MFValueParser, rollbackTransAction |  |
| 8.1.3 | migration-step | Included migration file for Java dependencies for Studio Pro 10 compatibility | Java dependencies |  |
| 8.1.2 | fix | Updated replication library to 1.0.3; fixes reference sets with Overwrite being overwritten multiple times, accidentally deleting imports | replication library, reference sets, Overwrite setting |  |
| 8.1.1 | breaking | Renamed URL to Host on database creation form to avoid confusion | URL, Host, database creation form | Host |
| 8.1.0 | requirement | Upgraded module to Mendix version 9.18.4 for compatibility with future versions | Mendix |  |
| 8.0.2 | improvement | Refactored replication library shared with Excel Importer to version 1.0.2 | replication library |  |
| 8.0.2 | improvement | Updated drivers: SQL Server 9.4.0, PostgreSQL 42.5.4, Oracle JDBC 21.9.0.0 | SQL Server, PostgreSQL, Oracle JDBC |  |
| 8.0.0 | requirement | Upgraded module to Mendix 9.0.5 and made compatible with Atlas 3. Version 8 only for Mendix 9; Version 7 for Mendix 8 and 9 | Mendix, Atlas UI |  |
| 7.1.5 | improvement | Updated replication library to 1.0.4; fixes rollback failure in Mendix 10 due to rollbackTransAction rename | replication library, MFValueParser, rollbackTransAction |  |
| 7.1.4 | fix | Updated replication library to 1.0.3; fixes reference sets with Overwrite being overwritten multiple times, accidentally deleting imports | replication library, reference sets, Overwrite setting |  |
| 7.1.3 | breaking | Renamed URL to Host on database creation form to avoid confusion | URL, Host, database creation form | Host |
| 7.1.2 | improvement | Refactored replication library shared with Excel Importer to version 1.0.2 | replication library |  |
| 7.1.2 | improvement | Updated drivers: SQL Server 9.4.0, PostgreSQL 42.5.1, Oracle JDBC 21.5.0.0 | SQL Server, PostgreSQL, Oracle JDBC |  |
| 7.1.0 | improvement | Wrapped all pop-up windows in Layout Grid containers to prepare for Atlas 3 support | pop-up windows, Layout Grid, Atlas 3 |  |
| 7.0.1 | security | Fixed CVE-2021-31341 |  |  |
| 7.0.0 | requirement | Updated to Mendix framework 8.12.4, SQL Server drivers to JRE11 variant, and Atlas UI | Mendix, SQL Server, Atlas UI |  |
| 6.1.1 | improvement | Updated replication.jar to latest version | replication.jar |  |
| 6.1.0 | improvement | Improved memory use: separate context skips user session reuse; load data in batches instead of all at once | memory use, database-replication, session, user context |  |
| 6.1.0 | improvement | Upgraded JDBC driver for PostgreSQL | PostgreSQL, JDBC driver |  |
| 6.0.1 | requirement | Updated to Mendix Studio Pro 7.23.7 | Mendix |  |
| 6.0.0 | removal | Removed deprecated APIs | deprecated APIs |  |
| 6.0.0 | removal | Removed Float and Currency data types; Decimal is used instead | Float, Currency | Decimal |
| 4.13.0 | improvement | Upgraded ojdbc6-11.2.0 to ojdbc8-12.2.0.1 and sqljdbc4-4.0 to mssql-jdbc-7.0.0 | ojdbc8, mssql-jdbc |  |
| 4.13.0 | improvement | Removed axis2-kernel-1.0.jar and use Java 8 API for encoding and decoding instead | axis2-kernel, Java 8 API |  |
| 4.10 | requirement | Made DatabaseReplication module compatible with Mendix 7 release | Mendix |  |

## Databricks JDBC Connector <a id="237990"></a>
Service, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/237990)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2025-03-11 | ? |

## Deep link module <a id="43"></a>
Module, Mendix, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/43)

| version | published | min Mendix |
|---|---|---|
| 10.0.10 | 2025-03-03 | 10.0.0 |
| 10.0.9 | 2024-10-15 | 10.0.0 |
| 10.0.8 | 2024-02-09 | 10.0.0 |
| 10.0.6 | 2023-11-27 | 10.0.0 |
| 10.0.5 | 2023-10-13 | 10.0.0 |
| 10.0.4 | 2023-09-08 | 10.0.0 |
| 9.0.17 | 2025-03-03 | 9.6.10 |
| 9.0.16 | 2024-11-07 | 9.6.10 |
| 9.0.15 | 2024-02-09 | 9.6.10 |
| 9.0.14 | 2023-12-19 | 9.6.10 |
| 9.0.12 | 2023-10-13 | 9.6.10 |
| 9.0.11 | 2023-07-06 | 9.6.10 |
| 9.0.10 | 2023-06-20 | 9.6.10 |
| 9.0.9 | 2023-02-20 | 9.6.10 |
| 9.0.8 | 2023-01-06 | 9.6.10 |
| 9.0.7 | 2023-01-04 | 9.6.10 |
| 9.0.6 | 2022-11-18 | 9.6.10 |
| 9.0.5 | 2022-09-16 | 9.6.10 |
| 9.0.4 | 2022-08-17 | 9.6.10 |
| 9.0.3 | 2022-07-11 | 9.6.10 |
| 9.0.2 | 2022-04-12 | 9.6.10 |
| 9.0.1 | 2022-03-25 | 9.6.10 |
| 8.0.9 | 2024-02-09 | 8.12.5 |
| 8.0.8 | 2023-11-30 | 8.12.5 |
| 8.0.7 | 2023-10-13 | 8.12.5 |
| 8.0.6 | 2022-11-18 | 8.12.5 |
| 8.0.5 | 2022-09-16 | 8.12.5 |
| 8.0.4 | 2022-08-17 | 8.12.5 |
| 8.0.3 | 2022-07-11 | 8.12.5 |
| 8.0.2 | 2022-04-12 | 8.12.5 |
| 8.0.1 | 2022-03-25 | 8.12.5 |
| 7.0.1 | 2022-05-05 | 7.23.0 |
| 7.0.0 | 2022-03-18 | 7.23.0 |
| 6.1.3 | 2022-01-28 | 8.12.0 |
| 6.1.2 | 2022-01-27 | 8.12.0 |
| 6.1.1 | 2021-12-21 | 8.12.0 |
| 6.1.0 | 2021-11-16 | 8.12.0 |
| 6.0.5 | 2021-01-20 | 8.12.0 |
| 6.0.4 | 2021-01-05 | 8.12.0 |
| 6.0.3 | 2019-10-16 | 7.23.0 |
| … 3 older versions | | |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 10.0.9 | breaking | Make DeepLink React Client compatible by using Combo Box widget instead of Reference Selector | Reference Selector, Combo Box widget | Combo Box widget |
| 10.0.6 | breaking | Switched to using DataGrid2 | DataGrid2 | DataGrid2 |
| 9.0.9 | requirement | Reverts the module Studio Pro requirements back to version 9.6.10 |  |  |
| 9.0.7 | fix | Use the new addCookie API with 'isHostOnly=true' when available. This fixes an issue with faulty redirects to the login page in Mendix >9.20 |  |  |
| 9.0.6 | removal | Removed user setting for the DeepLink argument type, as this is handled internally |  |  |
| 9.0.5 | fix | Fix for continuation after login. Requires 9.6.13+, 9.12.6+, or 9.18 and up |  |  |
| 9.0.5 | removal | Remove unused microflows |  |  |
| 8.0.6 | removal | Removed user setting for the DeepLink argument type, as this is handled internally |  |  |
| 8.0.5 | fix | Fix for continuation after login. Requires 8.18.20 and up |  |  |
| 8.0.5 | removal | Remove unused microflows |  |  |
| 7.0.0 | improvement | Updated libraries to the latest versions |  |  |
| 6.1.2 | requirement | Added RequiredLib file to clarify dependency on commons-lang library | commons-lang |  |
| 6.0.5 | improvement | Update Apache Commons libraries | Apache Commons |  |
| 6.0.4 | requirement | Upgrade to Mendix Studio Pro 8.12 |  |  |
| 6.0.3 | removal | Remove superfluous .RequiredLib file |  |  |
| 6.0.0 | requirement | Update to Mendix 7.23.0 to make it compatible with Mendix 8 |  |  |
| 6.0.0 | removal | Remove usage of deprecated APIs |  |  |

## Deprecated - Queue <a id="106628"></a>
Module, Ciphix, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/106628)

| version | published | min Mendix |
|---|---|---|
| 2.2.4 | 2021-11-19 | 8.12.0 |
| 2.2.3 | 2021-06-04 | 8.12.0 |
| 2.2.2 | 2021-05-21 | 8.12.0 |
| 2.2.1 | 2021-05-05 | 8.12.0 |
| 2.2.0 | 2021-02-12 | 8.4.2 |
| 2.1.0 | 2020-02-28 | 8.4.2 |
| 2.0.0 | 2019-12-23 | 8.4.2 |
| 1.3.2 | 2019-07-11 | 7.13.1 |
| 1.3.1 | 2019-02-12 | 7.13.1 |
| 1.3.0 | 2019-02-11 | 7.13.1 |
| 1.2.0 | 2018-12-17 | 7.13.1 |
| 1.1.2 | 2018-10-31 | 7.13.1 |
| 1.1.1 | 2018-10-29 | 7.13.1 |
| 1.1.0 | 2018-10-26 | 7.13.1 |
| 1.0.2 | 2018-07-20 | 7.13.1 |
| 1.0.1 | 2018-05-08 | 7.13.1 |
| 1.0.0 | 2018-04-26 | 7.13.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.2.3 | removal | Removed dependencies with junit and mockito | junit, mockito |  |
| 2.2.2 | migration-step | Renamed folder to have correct name |  |  |
| 2.2.2 | removal | Removed dependencies which were included incorrectly |  |  |
| 2.2.0 | requirement | Update to Mendix 8.12, results in compatibility with Mendix 9 |  |  |
| 2.0.0 | requirement | Upgrade to Mendix 8.4.2 |  |  |
| 1.3.2 | breaking | Changed all Java action input parameters to small caps |  |  |
| 1.1.2 | improvement | Input parameter naming with Job entity no longer required; Queue looks for first Object parameter with Queue.Job entity |  |  |

## Designcenter X Cloud Services Connector <a id="306304"></a>
Module, Siemens, Siemens, [marketplace](https://marketplace.mendix.com/link/component/306304)

| version | published | min Mendix |
|---|---|---|
| 2606.0.0 | 2026-09-15 | 10.24.2 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2606.0.0 | requirement | Minimum Mendix version is 10.24.2 |  |  |

## Device Status Code Manager <a id="121163"></a>
Solution, P&PM, Partner, [marketplace](https://marketplace.mendix.com/link/component/121163)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2022-08-12 | 9.14.1 |

## Document Generation for Mendix <a id="2026"></a>
Module, Emixa, Partner, [marketplace](https://marketplace.mendix.com/link/component/2026)

| version | published | min Mendix |
|---|---|---|
| 10.4.1 | 2026-06-17 | 10.21.0 |
| 10.4.0 | 2026-02-25 | 10.21.0 |
| 10.3.0 | 2026-01-30 | 10.21.0 |
| 10.2.0 | 2026-01-14 | 10.21.0 |
| 10.1.0 | 2025-12-01 | 10.21.0 |
| 9.0.0 | 2025-10-08 | 10.18.11 |
| 8.0.1 | 2025-08-20 | 9.18.0 |
| 8.0.0 | 2025-04-15 | 9.18.0 |
| 7.0.1 | 2024-05-21 | 9.18.0 |
| 7.0.0 | 2022-07-08 | 8.18.1 |
| 5.5.0 | 2020-04-09 | 7.23.10 |
| 5.4.0 | 2020-03-19 | 7.23.10 |
| 5.3.1 | 2020-02-13 | 7.23.10 |
| 5.2.1 | 2019-12-19 | 7.23.8 |
| 5.2.0 | 2019-12-12 | 7.23.8 |
| 5.1.0 | 2019-10-24 | 7.23.8 |
| 5.0.1 | 2019-03-04 | 7.2.0 |
| 5.0.0 | 2018-11-30 | 7.2.0 |
| 4.2.2 | 2017-09-12 | 7.2.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 10.4.1 | requirement | Added dependency on Nanoflow Commons module. | Nanoflow Commons |  |
| 10.4.1 | improvement | Improved flexibility by allowing changes in the connected microflow without blocking the save action. | Table_Save |  |
| 10.4.0 | fix | Fixed document generation issue where attributes accessed through 1-1 associations were not resolved correctly, causing XPath validation errors and failed merges. |  |  |
| 10.3.0 | improvement | Enhanced XPath validation to correctly handle associations targeting a generalized entity, including all underlying specializations as valid targets. |  |  |
| 10.2.0 | improvement | Added correct many-to-many validation for XPath processing using bidirectional navigability. |  |  |
| 10.1.0 | requirement | Module updated to Mendix 10.21.0. |  |  |
| 10.1.0 | feature | Fully compatible with Mendix 11, ensuring a smooth migration to the latest version. |  |  |
| 10.1.0 | fix | Fixed XPath validation issue that occurred when the same entity name was used across different modules. |  |  |
| 10.1.0 | fix | Fixed problem where quotation marks in Word IF/ELSE statements caused errors, now correctly escaped using {QUOTE 34}. |  |  |
| 10.1.0 | migration-step | Clean up userlib to avoid conflicts with old or duplicate libraries. |  |  |
| 9.0.0 | requirement | Upgrade to Mendix 10 (version 10.18.11 or higher) with React client compatibility. |  |  |
| 8.0.1 | removal | Removed commons-lang-2.5.jar dependency. | commons-lang-2.5.jar |  |
| 8.0.0 | removal | Removed the dependency on the Mx Model Reflection module. | Mx Model Reflection |  |
| 8.0.0 | feature | Introduced configuration validation for templates, ensuring that required tables and fields are correctly defined. |  |  |
| 8.0.0 | feature | Added support for validating fields using XPath expressions. |  |  |
| 8.0.0 | migration-step | Replace the afterstartup ASU_DocumentGenerationForMendix_ActivateLicense with ASU_DocumentGenerationForMendix. | ASU_DocumentGenerationForMendix_ActivateLicense, ASU_DocumentGenerationForMendix | ASU_DocumentGenerationForMendix |
| 7.0.1 | migration-step | Clean up userlib; documentgenerationformendix-1.0.0.jar is added. |  |  |
| 7.0.1 | feature | This release is Mendix 10 compatible. |  |  |
| 5.2.1 | migration-step | Rename TemplateType to TemplateConfiguration first, do not run the model, download new version, update Community Commons if needed, and fix references to layouts and pages. | TemplateType, TemplateConfiguration | TemplateConfiguration |
| 5.2.0 | breaking | TemplateType has been renamed to TemplateConfiguration. | TemplateType | TemplateConfiguration |
| 5.1.0 | feature | Compatible with Mendix 8. |  |  |
| 5.1.0 | requirement | Use newest version of CommunityCommons and MxModelreflection. | CommunityCommons, MxModelreflection |  |
| 5.0.0 | requirement | Upgraded to Mendix 7.18.1 to make use of native REST capabilities. |  |  |
| 5.0.0 | feature | Full compatibility with MS Word Add-in from Microsoft Office Appstore. |  |  |

## Document Viewer <a id="240853"></a>
Widget, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/240853)

| version | published | min Mendix |
|---|---|---|
| 1.3.0 | 2026-09-02 | 9.24.0 |
| 1.2.2 | 2026-07-22 | 9.24.0 |
| 1.2.1 | 2026-07-15 | 9.24.0 |
| 1.2.0 | 2025-11-03 | 9.24.0 |
| 1.1.1 | 2025-09-26 | 9.24.0 |
| 1.0.0 | 2025-05-12 | 9.24.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.3.0 | requirement | Updated library dependencies version of document viewer. | document viewer |  |
| 1.2.2 | fix | Fixed issue where widget was not loading in Dojo client due to broken JavaScript bundle. | Dojo client |  |
| 1.2.1 | breaking | Changed internal structure of the widget. |  |  |
| 1.2.1 | fix | Fixed issue where checkmarks and other special characters in PDFs were not displayed correctly. | PDF |  |

## Drag and Drop (Updated) <a id="116604"></a>
Widget, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/116604)

| version | published | min Mendix |
|---|---|---|
| 3.0.4 | 2022-10-20 | 9.6.0 |
| 3.0.3 | 2022-10-18 | 9.6.0 |
| 3.0.2 | 2022-07-21 | 9.6.0 |
| 3.0.0 | 2022-04-05 | 9.6.0 |
| 2.0.3 | 2021-09-01 | 8.12.0 |
| 2.0.2 | 2021-08-24 | 8.12.0 |
| 2.0.1 | 2021-08-17 | 8.12.0 |
| 2.0.0 | 2021-08-09 | 8.12.0 |
| 1.0.1 | 2021-04-06 | 8.12.0 |
| 1.0.0 | 2021-01-12 | 8.12.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 3.0.0 | requirement | Requires Mendix 9.6 and up. | Mendix |  |
| 3.0.0 | breaking | Complete rewrite. No longer uses custom JavaScript actions, uses verbose microflows instead. | Drag and Drop Widget |  |

## Dunning <a id="212750"></a>
Industry Template, TOCnDix, Partner, [marketplace](https://marketplace.mendix.com/link/component/212750)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2023-06-30 | 9.23.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.0.0 | requirement | Minimum Mendix version requirement is 9.23.0 | Mendix |  |

## Dynamic Case Management <a id="242816"></a>
Solution, CaseFabric, Partner, [marketplace](https://marketplace.mendix.com/link/component/242816)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2025-09-24 | 11.12.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.0.0 | requirement | Requires minimum Mendix version 11.12.0 | Mendix |  |

## Dynamic Case Management Commons <a id="247271"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/247271)

| version | published | min Mendix |
|---|---|---|
| 1.1.0 | 2026-09-30 | 11.12.4 |

## E-mail module with templates <a id="259"></a>
Service, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/259)

| version | published | min Mendix |
|---|---|---|
| 11.2.0 | 2022-08-10 | 8.18.19 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 11.2.0 | requirement | Updated javax-mail to 1.6.2. | javax-mail |  |
| 11.2.0 | requirement | Updated javax-activation to 1.1.1. | javax-activation |  |
| 11.2.0 | requirement | Updated commons-codec to 1.15. | commons-codec |  |

## Email Connector <a id="120739"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/120739)

| version | published | min Mendix |
|---|---|---|
| 6.4.3 | 2026-08-24 | 10.24.11 |
| 6.4.2 | 2026-07-29 | 10.24.11 |
| 6.4.1 | 2026-05-21 | 10.24.11 |
| 6.4.0 | 2025-12-12 | 10.24.11 |
| 6.3.2 | 2025-11-18 | 10.21.0 |
| 6.3.1 | 2025-09-24 | 10.21.0 |
| 6.3.0 | 2025-08-14 | 10.21.0 |
| 6.2.2 | 2025-06-03 | 10.21.0 |
| 6.2.1 | 2025-05-16 | 10.21.0 |
| 6.2.0 | 2025-04-25 | 10.21.0 |
| 6.1.0 | 2025-03-04 | 10.12.10 |
| 6.0.0 | 2025-01-28 | 10.12.10 |
| 5.9.10 | 2026-08-24 | 9.24.21 |
| 5.9.9 | 2025-12-15 | 9.24.21 |
| 5.9.8 | 2025-12-03 | 9.24.21 |
| 5.9.7 | 2025-11-13 | 9.24.21 |
| 5.9.6 | 2025-09-23 | 9.24.21 |
| 5.9.5 | 2025-06-23 | 9.24.21 |
| 5.9.4 | 2025-05-06 | 9.24.21 |
| 5.9.3 | 2024-12-24 | 9.24.21 |
| 5.9.2 | 2024-11-18 | 9.24.21 |
| 5.9.1 | 2024-09-09 | 9.24.21 |
| 5.9.0 | 2024-08-07 | 9.24.21 |
| 5.8.0 | 2024-05-16 | 9.24.21 |
| 5.7.0 | 2024-02-09 | 9.24.11 |
| 5.6.0 | 2024-01-03 | 9.24.11 |
| 5.5.0 | 2023-12-13 | 9.24.11 |
| 5.4.1 | 2023-11-08 | 9.24.11 |
| 5.4.0 | 2023-11-07 | 9.24.11 |
| 5.3.0 | 2023-10-16 | 9.24.9 |
| 5.2.0 | 2023-09-22 | 9.18.4 |
| 5.1.1 | 2023-07-26 | 9.18.4 |
| 5.1.0 | 2023-06-09 | 9.18.4 |
| 5.0.0 | 2023-05-24 | 9.18.4 |
| 4.1.0 | 2023-04-20 | 9.18.4 |
| 4.0.0 | 2023-04-12 | 9.18.4 |
| 3.0.2 | 2025-06-03 | 8.18.22 |
| 3.0.1 | 2023-03-13 | 8.18.22 |
| 3.0.0 | 2022-12-19 | 8.18.22 |
| 2.0.0 | 2022-12-01 | 8.18.22 |
| … 5 older versions | | |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 6.4.3 | requirement | Upgraded BouncyCastle jar to v1.85 | BouncyCastle |  |
| 6.4.3 | requirement | Upgraded HTMLElement widget to v1.2.12 | HTMLElement widget |  |
| 6.4.3 | requirement | Upgraded Data Widgets to v3.11.3 | Data Widgets |  |
| 6.4.2 | requirement | Upgraded HTMLElement widget to v1.2.9 | HTMLElement widget |  |
| 6.4.2 | requirement | Upgraded Data Widgets to v3.11.2 | Data Widgets |  |
| 6.4.1 | requirement | Upgraded bouncy castle jar to v1.84.0 | bouncy castle jar |  |
| 6.4.1 | requirement | Upgraded Rich Text widget to v4.12.0 | Rich Text widget |  |
| 6.4.1 | requirement | Upgraded HTML Element widget to v1.2.7 | HTML Element widget |  |
| 6.4.1 | requirement | Upgraded Data Widgets to v3.10.0 | Data Widgets |  |
| 6.4.0 | requirement | Upgraded module to Studio Pro version 10.24.11 | Studio Pro |  |
| 6.3.1 | requirement | Upgraded bouncycastle jar to v1.81.0 [#227116] | bouncycastle jar |  |
| 6.3.1 | requirement | Upgraded simple-java-mail jar to v8.12.6 [#258039] | simple-java-mail jar |  |
| 6.3.1 | requirement | Upgraded smime-module jar to v8.12.6 | smime-module jar |  |
| 6.3.1 | requirement | Upgraded angus-mail jar to v2.0.4 | angus-mail jar |  |
| 6.3.0 | breaking | Feature: Remove validation for password field. |  |  |
| 6.3.0 | requirement | Added dependency on Community Commons module. | Community Commons module |  |
| 6.3.0 | requirement | Upgraded Rich Text, Data Widgets, Combo box widget to latest version. | Rich Text, Data Widgets, Combo box widget |  |
| 6.2.2 | requirement | Upgraded Mx Reflection module to v9.0.1 | Mx Reflection module |  |
| 6.2.2 | requirement | Upgraded Encryption module to v11.0.1 | Encryption module |  |
| 6.2.2 | requirement | Upgraded Data Widgets to v2.31.1 | Data Widgets |  |
| 6.2.2 | requirement | Upgraded Combo box widget to v2.4.0 | Combo box widget |  |
| 6.2.1 | requirement | Upgraded Event tracking library to v1.0.3 | Event tracking library |  |
| 6.2.0 | requirement | Updated studio pro minimum version to 10.21.0 to support Mendix 11 | Studio Pro |  |
| 6.2.0 | requirement | Updated Rich text, HTML element, ComboBox widgets to latest available version | Rich text, HTML element, ComboBox widgets |  |
| 6.0.0 | requirement | Upgraded the module to Mendix version 10.12.10 | Mendix |  |
| 6.0.0 | breaking | Replaced old UI components with new ones compatible with the React Client | UI components |  |
| 6.0.0 | requirement | Upgraded the Combobox widget to v2.1.3 | Combobox widget |  |
| 6.0.0 | requirement | Upgraded Data Widgets to v2.29.0 | Data Widgets |  |
| 5.9.10 | requirement | Upgraded BouncyCastle jar to v1.85 | BouncyCastle jar |  |
| 5.9.6 | requirement | Upgraded simple-java-mail jar to v8.12.0 | simple-java-mail jar |  |
| 5.9.6 | requirement | Upgraded smime-module jar to v8.12.6 | smime-module jar |  |
| 5.9.6 | requirement | Upgraded angus-mail jar to v2.0.4 [#258039] | angus-mail jar |  |
| 5.9.6 | requirement | Upgraded bouncycastle jar to v1.81 [#257116] | bouncycastle jar |  |
| 5.9.5 | requirement | Upgraded Rich text widget to v4.7.0 | Rich text widget |  |
| 5.9.4 | requirement | Updated vulnerable HTML element widget to latest version | HTML element widget |  |
| 5.9.4 | requirement | Updated Rich Text widget to latest version | Rich Text widget |  |
| 5.9.3 | requirement | Upgraded Rich text widget to v4.1.0 (Ticket #229892) | Rich text widget |  |
| 5.9.3 | requirement | Upgraded Combo box widget to v1.7.0 | Combo box widget |  |
| 5.9.2 | requirement | Upgraded the HTML Element widget to version 1.2.1 (Tickets: #229892, #23272). | HTML Element widget |  |
| 5.9.1 | requirement | Upgraded slf4j jar to v2.0.7 | slf4j jar |  |
| 5.9.1 | requirement | Upgraded Rich text widget to v3.3.0 | Rich text widget |  |
| 5.9.0 | requirement | Upgraded Rich Text widget to v3.2.4 | Rich Text widget |  |
| 5.8.0 | requirement | Upgraded platform version to 9.24.21 and latest versions of Mx Model reflection and Encryption modules. | Mx Model reflection, Encryption modules |  |
| 5.8.0 | requirement | Upgraded rich-text widget. | rich-text widget |  |
| 5.8.0 | requirement | Upgraded Bouncy Castle version to 1.78.1 | Bouncy Castle |  |
| 5.8.0 | requirement | Upgraded simple-java-mail to 8.9.0 (This replaces jakarta.mail by angus-mail) | simple-java-mail, angus-mail | angus-mail |
| 5.5.0 | breaking | removed inline styling from pages. |  |  |
| 5.5.0 | removal | removed FileDocumentViewer widget which is community-supported and will be deprecated in near future. | FileDocumentViewer widget |  |
| 5.4.0 | requirement | Upgraded Studio Pro version to 9.24.11 | Studio Pro |  |
| 5.3.0 | requirement | Upgraded module to Mendix version 9.24.9. | Mendix |  |
| 5.2.0 | requirement | Upgraded Encryption module from version 9.0.0 to 9.0.2 | Encryption module |  |
| 5.1.1 | requirement | Upgraded Bounty Castle from 1.70 to 1.75 | Bounty Castle |  |
| 5.1.1 | requirement | Upgraded Core-module from 8.0.0 to 8.1.3 | Core-module |  |
| 5.1.1 | requirement | Upgraded Simple-java-mail from 8.0.0 to 8.1.3 | Simple-java-mail |  |
| 5.1.1 | requirement | Upgraded Smime-module from 8.0.0 to 8.1.3 | Smime-module |  |
| 5.1.1 | requirement | Upgraded Utils-mail-smime from 2.0.1 to 2.1.2 | Utils-mail-smime |  |
| 5.1.1 | migration-step | Please remove below jar from userlib before upgrading to this version- Jakarta.mail-api-2.1.1.jar | Jakarta.mail-api-2.1.1.jar |  |
| 5.0.0 | migration-step | Use the 'ACT_EmailAccount_LaunchEmailConnectorOverview' microflow in 'Navigation' rather than the 'EmailConnector_Overview' page. | ACT_EmailAccount_LaunchEmailConnectorOverview, EmailConnector_Overview |  |
| 5.0.0 | breaking | Removed custom styling from the module. |  |  |
| 5.0.0 | requirement | Upgraded Encryption module from version 8.0.4 to 9.0.0 | Encryption module |  |
| 5.0.0 | requirement | Upgraded MxModelReflection module from version 6.2.0 to 7.0.0 | MxModelReflection module |  |
| 5.0.0 | requirement | Upgraded Rich Text widget from version 2.1.5 to 2.1.6 | Rich Text widget |  |
| 5.0.0 | breaking | Replaced deprecated 'Format String' widget with 'HTML Element' version 1.0.1 | Format String widget, HTML Element | HTML Element |
| 4.0.0 | requirement | Upgraded module to Mendix version 9.18.4 | Mendix |  |
| 4.0.0 | requirement | Upgraded RichText widget from 1.3.9 to 2.1.5 | RichText widget |  |
| 4.0.0 | requirement | Upgraded core-module from 7.5.0 to 8.0.0 | core-module |  |
| 4.0.0 | migration-step | Kindly delete below mentioned old version jars from userlib folder: core-module 7.5.0 | core-module |  |
| 4.0.0 | requirement | Upgraded jakarta.mail-api from 2.1.0 to 2.1.1 | jakarta.mail-api |  |
| 4.0.0 | migration-step | Kindly delete below mentioned old version jars from userlib folder: jakarta.mail-api 2.1.0 | jakarta.mail-api |  |
| 4.0.0 | requirement | Upgraded jmail from 1.2.1 to  1.4.1 | jmail |  |
| 4.0.0 | migration-step | Kindly delete below mentioned old version jars from userlib folder: jmail 1.2.1 | jmail |  |
| 4.0.0 | requirement | Upgraded jsoup from 1.15.3 to 1.15.4 | jsoup |  |
| 4.0.0 | migration-step | Kindly delete below mentioned old version jars from userlib folder: jsoup 1.15.3 | jsoup |  |
| 4.0.0 | requirement | Upgraded simple-java-mail from 7.5.0 to 8.0.0 | simple-java-mail |  |
| 4.0.0 | migration-step | Kindly delete below mentioned old version jars from userlib folder: simple-java-mail 7.5.0 | simple-java-mail |  |
| 4.0.0 | requirement | Upgraded slf4j-api from 2.0.0-alpha1 to 2.0.6 | slf4j-api |  |
| 4.0.0 | migration-step | Kindly delete below mentioned old version jars from userlib folder: slf4j-api 2.0.0-alpha1 | slf4j-api |  |
| 4.0.0 | requirement | Upgraded slf4j-simple from 2.0.0-alpha1 to 2.0.6 | slf4j-simple |  |
| 4.0.0 | migration-step | Kindly delete below mentioned old version jars from userlib folder: slf4j-simple 2.0.0-alpha1 | slf4j-simple |  |
| 4.0.0 | requirement | Upgraded smime-module from 7.5.0 to 8.0.0 | smime-module |  |
| 4.0.0 | migration-step | Kindly delete below mentioned old version jars from userlib folder: smime-module 7.5.0 | smime-module |  |
| 3.0.2 | requirement | updated HTML Snippet and Rich Text widgets to latest version. | HTML Snippet, Rich Text widgets |  |
| 3.0.0 | breaking | Updated the module role name and settings. |  |  |
| 3.0.0 | breaking | Renamed and rearranged Microflows, Constants, Java actions etc. per Mendix naming conventions. | Microflows, Constants, Java actions |  |
| 1.3.0 | breaking | Removed UI activity from ACT_SendEmail & SE_SendQueuedEmails microflows | ACT_SendEmail, SE_SendQueuedEmails microflows |  |
| 1.3.0 | requirement | Upgraded module to Mendix 8.18.22 | Mendix |  |
| 1.2.0 | breaking | Removed language translation other than en_US. |  |  |
| 1.1.0 | requirement | Added Encryption module as dependency | Encryption module |  |
| 1.1.0 | requirement | Upgraded jsoup jar to 1.15.3 | jsoup jar |  |
| 1.1.0 | requirement | Upgraded simple-java-mail jar to 7.5.0 | simple-java-mail jar |  |

## Email Connector migration utility <a id="205008"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/205008)

| version | published | min Mendix |
|---|---|---|
| 3.0.0 | 2026-06-04 | 9.24.43 |
| 2.0.0 | 2022-12-21 | 8.18.22 |
| 1.0.0 | 2022-11-29 | 8.18.22 |

## Emixa Redis Connector <a id="3087"></a>
Module, Emixa, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/3087)

| version | published | min Mendix |
|---|---|---|
| 3.0.0 | 2022-11-11 | 8.18.19 |
| 2.0.0 | 2021-08-31 | 7.23.19 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 3.0.0 | migration-step | Delete jars first: jedis, commons-pool2, slf4j-api before upgrading to new library versions. | jedis, commons-pool2, slf4j-api |  |
| 2.0.0 | requirement | Upgrade Jedis and Mendix to required versions. | Jedis, Mendix |  |

## Empty List Placeholder <a id="118329"></a>
Widget, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/118329)

| version | published | min Mendix |
|---|---|---|
| 1.1.2 | 2022-02-04 | 8.18.1 |
| 1.1.1 | 2021-11-16 | 8.18.1 |
| 1.1.0 | 2021-09-10 | 8.18.1 |
| 1.0.0 | 2021-09-01 | 8.18.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.1.2 | fix | Fixed issue with opening widget more than once from navigation; widget now listens to last occurrence of class name. |  |  |
| 1.1.2 | breaking | Widget now listens to last occurrence of class name instead of first occurrence. |  |  |

## Encryption <a id="1011"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/1011)

| version | published | min Mendix |
|---|---|---|
| 11.1.2 | 2026-08-18 | 10.24.0 |
| 11.1.1 | 2026-05-21 | 10.24.0 |
| 11.1.0 | 2025-11-19 | 10.24.0 |
| 11.0.3 | 2025-09-08 | 10.21.0 |
| 11.0.2 | 2025-07-08 | 10.21.0 |
| 11.0.1 | 2025-05-12 | 10.21.0 |
| 11.0.0 | 2025-04-10 | 10.21.0 |
| 10.0.9 | 2026-08-18 | 9.24.18 |
| 10.0.8 | 2026-05-21 | 9.24.18 |
| 10.0.7 | 2025-09-08 | 9.24.18 |
| 10.0.6 | 2025-05-12 | 9.24.18 |
| 10.0.5 | 2025-04-03 | 9.24.18 |
| 10.0.4 | 2025-03-18 | 9.24.18 |
| 10.0.3 | 2024-10-14 | 9.24.18 |
| 10.0.2 | 2024-06-21 | 9.24.18 |
| 9.0.3 | 2024-05-29 | 9.18.0 |
| 9.0.2 | 2023-08-23 | 9.18.0 |
| 9.0.1 | 2023-07-14 | 9.18.0 |
| 9.0.0 | 2023-04-19 | 9.18.0 |
| 8.0.6 | 2024-05-22 | 8.12.0 |
| 8.0.5 | 2023-07-14 | 8.12.0 |
| 8.0.4 | 2023-02-15 | 8.12.0 |
| 8.0.3 | 2022-10-24 | 8.12.0 |
| 8.0.2 | 2022-02-28 | 8.12.0 |
| 8.0.1 | 2022-02-16 | 8.12.0 |
| 8.0.0 | 2022-02-10 | 8.12.0 |
| 7.0.3 | 2023-07-14 | 7.23.22 |
| 7.0.2 | 2023-02-15 | 7.23.22 |
| 7.0.1 | 2022-02-28 | 7.23.22 |
| 7.0.0 | 2022-02-10 | 7.23.22 |
| 2.5.0 | 2022-01-12 | 8.12.0 |
| 2.4.0 | 2022-01-03 | 8.12.0 |
| 2.3.0 | 2021-09-01 | 8.12.0 |
| 2.2.0 | 2021-07-22 | 8.12.0 |
| 2.1.3 | 2021-07-02 | 8.12.0 |
| 2.1.1 | 2020-12-23 | 8.12.0 |
| 2.1.0 | 2020-12-18 | 8.12.0 |
| 2.0.1 | 2020-03-03 | 7.23.0 |
| 2.0.0 | 2019-06-14 | 7.23.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 11.1.2 | requirement | Upgraded BouncyCastle dependency to 1.85 | BouncyCastle |  |
| 11.1.1 | requirement | Upgraded BouncyCastle dependency to 1.84 | BouncyCastle |  |
| 11.1.0 | requirement | Upgraded module to Mendix 10.24.0 | Mendix |  |
| 11.1.0 | fix | Fixed issue where module could not be used when Gradle synchronization was disabled | Gradle synchronization |  |
| 11.0.3 | requirement | Upgraded Bouncy Castle dependency to 1.81 | BouncyCastle |  |
| 11.0.2 | fix | Fixed issue where 'not flagged for encryption' error occurred reading public key (Ticket 253606) | public key encryption |  |
| 11.0.1 | fix | Fixed issue where document encryption did not clean up temporary files (Ticket #247796) | document encryption |  |
| 11.0.0 | requirement | Upgraded Encryption module to Mendix 10.21.0 | Mendix |  |
| 10.0.9 | requirement | Upgraded BouncyCastle dependency to 1.85 | BouncyCastle |  |
| 10.0.8 | requirement | Upgraded BouncyCastle dependency to 1.84 | BouncyCastle |  |
| 10.0.7 | requirement | Upgraded Bouncy Castle dependency to 1.81 | BouncyCastle |  |
| 10.0.6 | fix | Fixed issue where document encryption did not clean up temporary files (Ticket #247796) | document encryption |  |
| 10.0.3 | requirement | Updated Apache Commons IO dependency to 2.17.0 (Tickets 230717, 230797) | Apache Commons IO |  |
| 10.0.3 | breaking | Changed AES/GCM/PKCS5PADDING to AES/GCM/NoPadding for Java 21 compatibility (Ticket 225806) | AES/GCM encryption |  |
| 10.0.2 | requirement | Upgraded Mendix version to 9.24.18 | Mendix |  |
| 10.0.2 | requirement | Upgraded Bouncy Castle version to 1.78.1 | BouncyCastle |  |
| 10.0.2 | breaking | Removed default value for EncryptionKey that was mistakenly introduced in 10.0.0 | EncryptionKey |  |
| 9.0.3 | requirement | Upgraded Bouncy Castle version to 1.78.1 | BouncyCastle |  |
| 9.0.2 | migration-step | Included migration file for Java dependencies for Studio Pro 10 compatibility | Java dependencies |  |
| 9.0.1 | requirement | Updated Bouncy Castle from version 1.70 to 1.75 | BouncyCastle |  |
| 9.0.0 | requirement | Updated module to Studio Pro 9.18 for use in Studio Pro 10 | Mendix |  |
| 8.0.6 | requirement | Upgraded Bouncy Castle version to 1.78.1 | BouncyCastle |  |
| 8.0.6 | migration-step | Remove jar files from userlib: bcpg-jdk18on-1.75.jar, bcpkix-jdk18on-1.75.jar, bcprov-jdk18on-1.75.jar | bcpg-jdk18on-1.75.jar, bcpkix-jdk18on-1.75.jar, bcprov-jdk18on-1.75.jar |  |
| 8.0.5 | requirement | Updated Bouncy Castle from version 1.70 to 1.75 | BouncyCastle |  |
| 8.0.4 | requirement | Updated Bouncy Castle from version 1.69 to 1.70 | BouncyCastle |  |
| 8.0.4 | migration-step | Remove jar files from userlib: bcpg-jdk15on-1.69.jar, bcpkix-jdk15on-1.69.jar, bcprov-jdk15on-1.69.jar | bcpg-jdk15on-1.69.jar, bcpkix-jdk15on-1.69.jar, bcprov-jdk15on-1.69.jar |  |
| 8.0.3 | requirement | Updated Apache Commons IO from version 2.8.0 to 2.11.0 | Apache Commons IO |  |
| 8.0.3 | migration-step | Remove jar file from userlib: commons-io-2.8.jar | commons-io-2.8.jar |  |
| 8.0.2 | requirement | Updated Apache Commons IO from version 2.7 to 2.8.0 | Apache Commons IO |  |
| 8.0.2 | migration-step | Remove jar file from userlib: commons-io-2.7.jar | commons-io-2.7.jar |  |
| 7.0.3 | requirement | Updated Bouncy Castle from version 1.69 to 1.75 | BouncyCastle |  |
| 7.0.2 | requirement | Updated Apache Commons IO from version 2.8.0 to 2.11.0 | Apache Commons IO |  |
| 7.0.2 | migration-step | Remove jar file from userlib if it exists: commons-io-2.8.0.jar | commons-io-2.8.0.jar |  |
| 7.0.1 | requirement | Updated Apache Commons IO from version 2.7 to 2.8.0 | Apache Commons IO |  |
| 7.0.1 | migration-step | Remove jar file from userlib if it exists: commons-io-2.7.jar | commons-io-2.7.jar |  |
| 7.0.0 | removal | Removed PGP document signing; removed SigningCertificate and SigningPrivateKey_Optional parameters | SigningCertificate, SigningPrivateKey_Optional, PGPEncryptDocument, Encrypt_Document |  |
| 7.0.0 | feature | Added new encryption algorithm with {AES3} prefix; encryption key now required to be 32 characters |  |  |
| 7.0.0 | migration-step | Decrypt and re-encrypt all database values; set LegacyEncryptionKey to 16-char key, EncryptionKey to 32-char key | EncryptionKey, LegacyEncryptionKey |  |
| 7.0.0 | improvement | Made encryption module stricter to disallow legacy encryption; legacy algorithms still decryptable |  |  |
| 7.0.0 | requirement | Updated dependencies |  |  |
| 7.0.0 | migration-step | Remove jar files from userlib if they exist: bcpg-jdk15on-164.jar, bcpkix-jdk15on-164.jar, bcprov-jdk15on-164.jar, commons-io-2.6.jar | bcpg-jdk15on-164.jar, bcpkix-jdk15on-164.jar, bcprov-jdk15on-164.jar, commons-io-2.6.jar |  |
| 2.4.0 | removal | Removed PGP document signing; removed SigningCertificate and SigningPrivateKey_Optional parameters | SigningCertificate, SigningPrivateKey_Optional, PGPEncryptDocument, Encrypt_Document |  |
| 2.3.0 | breaking | Reverted change where already-encrypted strings were encrypted again | Encrypt |  |
| 2.2.0 | feature | Added new encryption algorithm with {AES3} prefix; encryption key now required to be 32 characters |  |  |
| 2.2.0 | migration-step | Decrypt and re-encrypt all database values; set LegacyEncryptionKey to 16-char key, EncryptionKey to 32-char key | EncryptionKey, LegacyEncryptionKey |  |
| 2.2.0 | improvement | Strings now encrypted even if starting with prefix; legacy algorithms still decryptable |  |  |
| 2.2.0 | migration-step | Remove jar file from userlib: commons-io-2.6.jar | commons-io-2.6.jar |  |
| 2.1.3 | breaking | Made encryption module stricter to disallow legacy encryption |  |  |
| 2.1.3 | requirement | Updated dependencies |  |  |
| 2.1.1 | requirement | Upgraded BouncyCastle dependency | BouncyCastle |  |
| 2.1.1 | migration-step | Remove jar files from userlib if they exist: bcpg-jdk15on-164.jar, bcpkix-jdk15on-164.jar, bcprov-jdk15on-164.jar | bcpg-jdk15on-164.jar, bcpkix-jdk15on-164.jar, bcprov-jdk15on-164.jar |  |
| 2.1.0 | requirement | Updated Encryption module to Mendix 8.12.0 | Mendix |  |
| 2.0.1 | security | Updated dependencies fixing various vulnerabilities (Ticket 96070) |  |  |
| 2.0.1 | migration-step | Remove jar files from userlib: bcpg-jdk15on-150.jar, bcpkix-jdk15on-150.jar, bcprov-jdk15on-150.jar | bcpg-jdk15on-150.jar, bcpkix-jdk15on-150.jar, bcprov-jdk15on-150.jar |  |
| 2.0.0 | requirement | Updated to Mendix Studio Pro 7.23.0 for use in Mendix 7.23 and Mendix 8 projects | Mendix |  |

## EnumClass <a id="2641"></a>
Widget, Valcon, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/2641)

| version | published | min Mendix |
|---|---|---|
| 1.3.0 | 2021-01-26 | 8.12.5 |
| 1.2.1 | 2020-07-16 | 8.0.0 |
| 1.2.0 | 2020-07-16 | 8.0.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.2.0 | improvement | Made compatible with Mendix 8 in combination with list view |  |  |

## ESG Scoring and Assessment for Corporates <a id="208717"></a>
Industry Template, TOCnDix, Partner, [marketplace](https://marketplace.mendix.com/link/component/208717)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2023-03-22 | 9.20.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.0.0 | requirement | Minimum Mendix version requirement is 9.20.0 | Mendix |  |

## Event App <a id="36793"></a>
Starter App, Mendix, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/36793)

| version | published | min Mendix |
|---|---|---|
| 3.12.10 | 2020-10-27 | 8.14.0 |
| 3.12.9 | 2020-09-30 | 8.14.0 |
| 3.12.8 | 2020-09-29 | 8.14.0 |
| 3.12.7 | 2020-09-11 | 8.13.1 |
| 3.12.6 | 2020-07-28 | 8.12.0 |
| 3.12.5 | 2020-07-28 | 8.12.0 |
| 3.12.4 | 2020-07-07 | 8.11.0 |
| 3.12.3 | 2020-07-07 | 8.11.0 |
| 3.12.2 | 2020-05-27 | 8.10.0 |
| 3.12.1 | 2020-05-06 | 8.9.0 |
| 3.12.0 | 2020-04-30 | 8.9.0 |
| 3.11.3 | 2020-04-17 | 8.8.1 |
| 3.11.2 | 2020-04-14 | 8.8.1 |
| 3.11.1 | 2020-04-01 | 8.8.0 |
| 3.11.0 | 2020-03-16 | 8.7.0 |
| 3.10.17 | 2020-03-16 | 7.23.12 |
| 3.10.16 | 2020-03-04 | 8.7.0 |
| 3.10.15 | 2020-03-04 | 8.7.0 |
| 3.10.14 | 2020-03-03 | 8.7.0 |
| 3.10.13 | 2020-03-03 | 8.7.0 |
| 3.10.12 | 2020-03-02 | 8.7.0 |
| 3.10.11 | 2020-02-27 | 8.7.0 |
| 3.10.10 | 2020-02-27 | 8.7.0 |
| 3.10.9 | 2020-02-10 | 8.6.0 |
| 3.10.8 | 2020-02-07 | 8.6.0 |
| 3.10.7 | 2020-02-06 | 8.6.0 |
| 3.10.6 | 2020-02-05 | 8.6.0 |
| 3.10.5 | 2019-12-20 | 8.5.0 |
| 3.10.4 | 2019-12-12 | 8.4.2 |
| 3.10.3 | 2019-11-28 | 8.4.1 |
| 3.10.2 | 2019-11-27 | 8.4.0 |
| 3.10.1 | 2019-11-27 | 8.4.0 |
| 3.10.0 | 2019-11-26 | 8.4.0 |
| 3.9.22 | 2019-10-30 | 8.3.0 |
| 3.9.21 | 2019-10-29 | 8.3.0 |
| 3.9.20 | 2019-10-29 | 8.3.0 |
| 3.9.19 | 2019-10-17 | 8.2.2 |
| 3.9.18 | 2019-10-16 | 8.2.2 |
| 3.9.17 | 2019-09-12 | 8.1.1 |
| 3.9.16 | 2019-09-10 | 8.1.1 |
| … 48 older versions | | |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 3.11.3 | improvement | Update Mendix Feedback Widget to version 8.2.1 | Mendix Feedback Widget |  |
| 3.9.11 | improvement | Updated feedback widget | feedback widget |  |
| 3.9.4 | improvement | Updated Atlas Resources to v1.2.4 | Atlas Resources |  |
| 3.9.0 | improvement | Updated Atlas Resources to v1.2.2 | Atlas Resources |  |
| 3.7.0 | improvement | Updated framework and widgets | framework, widgets |  |
| 3.4.1 | improvement | Updated Atlas UI Resources module to version 1.1.1 | Atlas UI Resources |  |
| 3.4.0 | improvement | Update Atlas UI Resources module | Atlas UI Resources |  |
| 3.0.0 | feature | Official release with the Atlas UI Resources module | Atlas UI Resources |  |
| 2.0.5 | breaking | Changed default config |  |  |
| 2.0.4 | removal | Removed file in lib | lib |  |
| 2.0.0 | improvement | Upgraded Mendix Version and Atlas UI Library | Atlas UI Library, Navigation Layouts |  |
| 1.4.7 | removal | Removed userlib | userlib |  |
| 1.4.7 | improvement | New library for Atlas UI | Atlas UI library |  |
| 1.4.5 | removal | Removed not used widgets | widgets |  |

## Event Mesh Connector of SAP Solutions <a id="217434"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/217434)

| version | published | min Mendix |
|---|---|---|
| 2.0.0 | 2025-07-08 | 10.21.0 |
| 1.1.0 | 2025-05-06 | 9.24.33 |
| 1.0.0 | 2023-10-16 | 9.24.4 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.0.0 | requirement | Minimum Mendix version requirement increased to 10.21.0 | Mendix |  |
| 2.0.0 | improvement | Upgraded to Mendix 10.21 | Event Mesh Connector |  |

## Events <a id="224259"></a>
Widget, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/224259)

| version | published | min Mendix |
|---|---|---|
| 1.3.1 | 2026-07-22 | 9.24.0 |
| 1.3.0 | 2026-02-25 | 9.24.0 |
| 1.2.0 | 2025-11-10 | 9.24.0 |
| 1.1.0 | 2025-08-12 | 9.24.0 |
| 1.0.1 | 2024-04-25 | 9.24.0 |
| 1.0.0 | 2024-03-20 | 9.24.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.2.0 | breaking | Repeated execution is not executing next action if previous execution is not yet finished. |  |  |
| 1.1.0 | feature | Added support for using expressions to configure both delay and repeat interval values during component load and for delay values when attributes change dynamically. |  |  |

## Excel Exporter <a id="726"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/726)

| version | published | min Mendix |
|---|---|---|
| 8.3.2 | 2026-07-29 | 10.24.11 |
| 8.3.1 | 2026-06-09 | 10.24.11 |
| 8.3.0 | 2026-05-18 | 10.24.11 |
| 8.2.3 | 2026-04-27 | 10.24.11 |
| 8.2.2 | 2026-03-16 | 10.24.11 |
| 8.2.1 | 2026-01-28 | 10.24.11 |
| 8.2.0 | 2025-12-15 | 10.24.11 |
| 8.1.3 | 2025-11-07 | 10.21.0 |
| 8.1.2 | 2025-07-15 | 10.21.0 |
| 8.1.1 | 2025-06-06 | 10.21.0 |
| 8.1.0 | 2025-04-28 | 10.21.0 |
| 8.0.0 | 2025-01-31 | 10.12.10 |
| 7.5.9 | 2026-06-09 | 9.24.11 |
| 7.5.8 | 2026-04-27 | 9.24.11 |
| 7.5.7 | 2025-11-07 | 9.24.11 |
| 7.5.6 | 2025-07-21 | 9.24.11 |
| 7.5.5 | 2025-06-12 | 9.24.11 |
| 7.5.4 | 2025-01-15 | 9.24.11 |
| 7.5.3 | 2025-01-07 | 9.24.11 |
| 7.5.2 | 2024-11-22 | 9.24.11 |
| 7.5.1 | 2024-08-09 | 9.24.11 |
| 7.5.0 | 2024-08-02 | 9.24.11 |
| 7.4.1 | 2024-03-07 | 9.24.11 |
| 7.4.0 | 2023-11-08 | 9.24.11 |
| 7.3.0 | 2023-09-27 | 9.18.4 |
| 7.2.0 | 2023-08-02 | 9.18.4 |
| 7.1.1 | 2023-05-30 | 9.18.4 |
| 7.1.0 | 2023-04-07 | 9.18.4 |
| 7.0.5 | 2022-11-29 | 9.0.5 |
| 7.0.4 | 2022-05-27 | 9.0.5 |
| 7.0.3 | 2022-02-09 | 9.0.5 |
| 7.0.2 | 2021-11-02 | 9.0.5 |
| 7.0.1 | 2021-09-20 | 9.0.5 |
| 7.0.0 | 2021-06-01 | 9.0.5 |
| 6.1.6 | 2025-07-09 | 8.12.5 |
| 6.1.5 | 2023-05-30 | 8.12.5 |
| 6.1.4 | 2022-06-01 | 8.12.5 |
| 6.1.3 | 2021-09-20 | 8.12.5 |
| 6.1.2 | 2021-02-05 | 8.12.5 |
| 6.1.1 | 2020-12-31 | 8.12.0 |
| … 11 older versions | | |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 8.3.1 | requirement | Updated log4j-api to latest 2.25.+ version. | log4j-api |  |
| 8.3.1 | requirement | Upgraded Data Widgets to v3.10.0. | Data Widgets |  |
| 8.3.0 | security | Added sanitization for formula injection in excel/csv export to prevent security vulnerabilities [#277915]. |  |  |
| 8.2.2 | requirement | Update log4j-api v2.24.3 to v2.25.3 [#271452]. | log4j-api |  |
| 8.2.0 | requirement | Upgraded module to Studio Pro v10.24.11. |  |  |
| 8.1.2 | requirement | Upgraded opencsv jar to v5.11.2. | opencsv |  |
| 8.1.0 | requirement | Updated studio pro minimum version to 10.21.0 to support Mendix 11. |  |  |
| 8.1.0 | requirement | Updated Atlas core, Data widgets, Nanoflow commons to latest version. | Atlas Core, Data Widgets, Nanoflow Commons |  |
| 8.0.0 | requirement | Upgraded the module to Mendix version 10.12.10. |  |  |
| 8.0.0 | breaking | Replaced old UI components with new ones compatible with the React Client. |  |  |
| 8.0.0 | requirement | Upgraded the Combobox widget to v2.1.3. | Combobox |  |
| 8.0.0 | requirement | Upgraded Data Widgets to v2.29.1. | Data Widgets |  |
| 7.5.8 | security | Fix vulnerability CVE-2025-68161 log4j-api jar [#275070]. | log4j-api |  |
| 7.5.6 | requirement | Upgraded opencsv jar to v5.11.2. | opencsv |  |
| 7.5.6 | requirement | Upgraded commons-lang3 jar to v3.18.0. | commons-lang3 |  |
| 7.5.5 | requirement | Upgraded Apache poi ooxml jar version to v5.4.0. | poi-ooxml |  |
| 7.5.5 | requirement | Upgraded combo box to v1.7.1. | Combobox |  |
| 7.5.2 | requirement | Updated the Apache Commons IO dependency to 2.17.0. | Apache Commons IO |  |
| 7.5.0 | requirement | Apache poi library update to 5.3.0 mitigate vulnerabilities in 5.2.5 due to commons-compress. | Apache poi |  |
| 7.5.0 | improvement | Improved performance for exporting Excel (2007 and higher) including Macro enabled files. |  |  |
| 7.4.1 | security | Mitigated CVE-2024-25710 by updating third-party dependencies. |  |  |
| 7.4.0 | requirement | Upgraded module to Mendix version 9.24.11. |  |  |
| 7.3.0 | migration-step | Introduction of migration file for JDM. |  |  |
| 7.2.0 | breaking | Sheet name is now a mandatory field during template creation. |  |  |
| 7.2.0 | breaking | Naming of JARs in userlib is aligned to only have JAR name without prefix of package. |  |  |
| 7.1.1 | requirement | Upgraded MxModelReflection module from version 6.2.0 to 7.0.0. | MxModelReflection |  |
| 7.1.0 | requirement | Updated module to Mendix version 9.18.4. |  |  |
| 7.0.5 | security | Upgraded opencsv-5.7.1.jar to fix CVE-2022-42889. | opencsv |  |
| 7.0.4 | removal | Removed unused attribute NameAsHeader from MxColumn entity. | MxColumn |  |
| 7.0.4 | requirement | Upgraded poi-ooxml from 4.1.2 to 5.2.2 to fix common vulnerabilities and exposures. | poi-ooxml |  |
| 7.0.2 | requirement | Upgraded joda-time from 2.10.9 to 2.10.10. | joda-time |  |
| 7.0.2 | requirement | Upgraded opencsv from 5.3 to 5.4. | opencsv |  |
| 7.0.1 | requirement | Using commons-compress 1.21 and updated dependencies. | commons-compress |  |
| 7.0.1 | breaking | Removed Excel Importer, re-imported Atlas Core. | Excel Importer |  |
| 7.0.0 | requirement | This version supports Mendix 9.0.5 and higher. |  |  |
| 7.0.0 | requirement | This version is compatible with Atlas Core 3.0.2. | Atlas Core |  |
| 6.1.6 | requirement | Upgraded opencsv jar to v5.11.2. | opencsv |  |
| 6.1.6 | requirement | Upgraded poi-ooxml to v5.4.0. | poi-ooxml |  |
| 6.1.5 | security | Upgraded opencsv JAR to version 5.7.1 to fix CVE-2022-42889. | opencsv |  |
| 6.1.4 | requirement | Upgraded poi-ooxml from 4.1.2 to 5.2.2 to fix common vulnerabilities and exposures. | poi-ooxml |  |
| 6.1.4 | requirement | Related dependencies were also upgraded. |  |  |
| 6.1.4 | removal | Removed unused attribute NameAsHeader from MxColumn entity. | MxColumn |  |
| 6.1.3 | requirement | Jars updated. |  |  |
| 6.1.2 | requirement | Upgraded apache poi from 4.1.1 to 4.1.2. | poi |  |
| 6.1.2 | requirement | Upgraded joda time from 2.10.5 to 2.10.9. | joda-time |  |
| 6.1.2 | requirement | Upgraded opencsv from 5.0 to 5.3. | opencsv |  |
| 6.1.2 | breaking | Renamed userlib jars: commons-codec-1.13.jar to commons-codec.commons-codec-1.13.jar. |  |  |
| 6.1.2 | breaking | Renamed userlib jars: commons-collections4-4.4.jar to org.apache.commons.commons-collections4-4.4.jar. |  |  |
| 6.1.2 | breaking | Renamed userlib jars: commons-compress-1.19.jar to org.apache.commons.commons-compress-1.19.jar. |  |  |
| 6.1.2 | breaking | Renamed userlib jars: commons-math3-3.6.1.jar to org.apache.commons.commons-math3-3.6.1.jar. |  |  |
| 6.1.1 | requirement | Upgraded replication.jar. |  |  |
| 6.1.0 | requirement | This version is compatible with Mendix 8.12.0 and later versions. |  |  |
| 6.0.6 | requirement | Jars updated. |  |  |
| 6.0.5 | requirement | Updated commons-codec 1.11 to 1.13 (used by poi 4.1.1). | commons-codec |  |
| 6.0.5 | requirement | Updated commons-collections4 4.2 to 4.4 (used by poi 4.1.1). | commons-collections4 |  |
| 6.0.5 | security | Updated commons-compress 1.18 (CVE) to 1.19. | commons-compress |  |
| 6.0.5 | requirement | Updated commons-io 2.3 to 2.6. | commons-io |  |
| 6.0.5 | requirement | Updated commons-lang3 3.1.0 to 3.9 (used by commons-codec and commons-collections4). | commons-lang3 |  |
| 6.0.5 | requirement | Updated joda-time 2.9.6 to 2.10.5. | joda-time |  |
| 6.0.5 | requirement | Updated opencsv 4.6 to 5.0. | opencsv |  |
| 6.0.5 | requirement | Updated poi 4.0.0 to 4.1.1 (used by poi-ooxml 4.1.1). | poi |  |
| 6.0.5 | security | Updated poi-ooxml 4.0.0 (CVE) to 4.1.1. | poi-ooxml |  |
| 6.0.5 | requirement | Updated poi-ooxml-schemas 4.0.0 to 4.1.1 (used by poi-ooxml 4.1.1). | poi-ooxml-schemas |  |
| 6.0.5 | requirement | Updated xmlbeans 3.0.1 to 3.1.0 (used by poi-ooxml-schemas 4.1.1). | xmlbeans |  |
| 6.0.5 | requirement | Updated MxModelReflection 5.6.2 to 6.1.1. | MxModelReflection |  |
| 6.0.5 | requirement | Use Atlas UI Resources. | Atlas UI Resources |  |
| 6.0.1 | requirement | Includes the required commons-compress.jar. | commons-compress |  |
| 6.0.0 | breaking | Migrate to Mx 7.23 and fix deprecated warnings including FileDocuments and Float/Currency usages for Mx 8 compatibility. |  |  |
| 6.0.0 | breaking | Use non-deprecated CSVWriter. |  |  |
| 5.2.1 | requirement | Now it includes the required commons-compress.jar. | commons-compress |  |
| 5.2.0 | requirement | Update opencsv from version 2.3 to version 4.6. | opencsv |  |
| 5.2.0 | requirement | Make compatible with Excel Importer 8.0.0. | Excel Importer |  |
| 5.1.0 | requirement | Upgraded poi, poi-ooxml, and poi-ooxml-schemas to 4.0.0. | poi, poi-ooxml, poi-ooxml-schemas |  |
| 5.1.0 | requirement | Upgraded commons-codec to 1.11. | commons-codec |  |
| 5.1.0 | requirement | Upgraded commons-collections4 to 4.2. | commons-collections4 |  |
| 5.1.0 | requirement | Upgraded commons-math to 3.6.1. | commons-math |  |
| 5.1.0 | requirement | Upgraded replication to 7. |  |  |
| 5.1.0 | requirement | Upgraded xmlbeans to 3.0.1. | xmlbeans |  |

## Excel Exporter Template Manager <a id="16873"></a>
Module, Conclusion Low Code Company, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/16873)

| version | published | min Mendix |
|---|---|---|
| 3.0.0 | 2023-08-11 | 9.24.5 |
| 2.1.0 | 2023-02-20 | 8.12.5 |
| 2.0.1 | 2021-12-09 | 8.12.0 |
| 2.0.0 | 2021-04-20 | 8.0.0 |
| 1.1.2 | 2018-09-10 | 7.0.2 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 3.0.0 | requirement | Support for Excel Exporter version 7.2.0 | Excel Exporter |  |
| 3.0.0 | requirement | Support for Mendix 9 and Mendix 10 |  |  |
| 2.1.0 | requirement | Support for Excel Exporter module v6.1.4 | Excel Exporter |  |
| 2.1.0 | breaking | Breaking changes in the domain model; re-export older templates |  |  |
| 2.0.1 | requirement | Upgrade to Mendix 8.12 for compatibility with Mendix 9 |  |  |
| 2.0.0 | requirement | Upgrade for Mendix 8 |  |  |

## Excel Importer <a id="72"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/72)

| version | published | min Mendix |
|---|---|---|
| 11.2.2 | 2026-08-18 | 10.24.11 |
| 11.2.1 | 2026-03-16 | 10.24.11 |
| 11.2.0 | 2025-12-15 | 10.24.11 |
| 11.1.3 | 2025-11-06 | 10.21.0 |
| 11.1.2 | 2025-07-25 | 10.21.0 |
| 11.1.1 | 2025-06-06 | 10.21.0 |
| 11.1.0 | 2025-04-28 | 10.21.0 |
| 11.0.0 | 2025-01-30 | 10.12.10 |
| 10.7.9 | 2026-05-29 | 9.24.11 |
| 10.7.8 | 2026-04-27 | 9.24.11 |
| 10.7.7 | 2025-11-07 | 9.24.11 |
| 10.7.6 | 2025-07-25 | 9.24.11 |
| 10.7.5 | 2025-06-10 | 9.24.11 |
| 10.7.4 | 2024-11-22 | 9.24.11 |
| 10.7.3 | 2024-11-19 | 9.24.11 |
| 10.7.2 | 2024-08-02 | 9.24.11 |
| 10.7.1 | 2024-07-15 | 9.24.11 |
| 10.7.0 | 2024-04-29 | 9.24.11 |
| 10.6.2 | 2024-03-07 | 9.24.11 |
| 10.6.1 | 2024-02-14 | 9.24.11 |
| 10.6.0 | 2023-11-02 | 9.24.11 |
| 10.5.0 | 2023-09-27 | 9.18.4 |
| 10.4.0 | 2023-07-25 | 9.18.4 |
| 10.3.0 | 2023-04-13 | 9.18.4 |
| 10.2.0 | 2023-03-20 | 9.0.5 |
| 10.1.3 | 2022-07-06 | 9.0.5 |
| 10.1.2 | 2022-06-22 | 9.0.5 |
| 10.1.1 | 2022-05-31 | 9.0.5 |
| 10.1.0 | 2022-03-29 | 9.0.5 |
| 10.0.2 | 2021-09-22 | 9.0.5 |
| 10.0.1 | 2021-08-10 | 9.0.5 |
| 10.0.0 | 2021-07-19 | 9.0.5 |
| 9.2.7 | 2024-11-19 | 8.18.21 |
| 9.2.6 | 2024-08-02 | 8.18.21 |
| 9.2.5 | 2024-03-11 | 8.18.21 |
| 9.2.4 | 2023-02-16 | 8.12.4 |
| 9.2.3 | 2022-07-06 | 8.12.4 |
| 9.2.2 | 2022-06-22 | 8.12.4 |
| 9.2.1 | 2022-05-31 | 8.12.4 |
| 9.2.0 | 2022-03-29 | 8.12.4 |
| … 24 older versions | | |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 11.2.2 | requirement | Upgraded log4j-api jar to v2.25.+ | log4j-api |  |
| 11.2.1 | requirement | Update log4j-api v2.24.3 to v2.25.3 | log4j-api |  |
| 11.2.0 | requirement | Upgraded module version to SP 10.24.11 |  |  |
| 11.1.2 | requirement | Upgraded commons-lang3 jar version to v3.18.0 | commons-lang3 |  |
| 11.1.2 | requirement | Upgraded MxReflection, Community commons to the latest available | MxReflection, Community commons |  |
| 11.1.0 | requirement | Updated studio pro minimum version to 10.21.0 to support Mendix 11 version |  |  |
| 11.1.0 | requirement | Upgraded replication jar, Community commons, MxReflection, Unit Test widgets to latest available | replication jar, Community commons, MxReflection, Unit Test widgets |  |
| 11.0.0 | breaking | Replaced old UI components with new ones compatible with the React Client | UI components |  |
| 11.0.0 | requirement | Upgraded the Combobox widget to v2.1.3 | Combobox widget |  |
| 11.0.0 | requirement | Upgraded Data Widgets to v2.29.1 | Data Widgets |  |
| 10.7.9 | requirement | Updated log4j-api from 2.24.3 to 2.25.4 | log4j-api |  |
| 10.7.9 | removal | Removed unused published web service document | published web service document |  |
| 10.7.8 | requirement | Updated log4j-api from 2.24.3 to 2.25.4 | log4j-api |  |
| 10.7.6 | requirement | Upgraded commons-lang3 jar version to v3.18.0 | commons-lang3 |  |
| 10.7.5 | requirement | Upgraded Apache poi ooxml jar version to v5.4.0 | Apache poi ooxml |  |
| 10.7.5 | requirement | Upgraded combo box widget to v1.7.1 | combo box widget |  |
| 10.7.3 | requirement | Updated the Apache Commons IO dependency to 2.17.0 | Apache Commons IO |  |
| 10.7.2 | security | Upgraded Apache POI OOXML to 5.3.0 mitigate the vulnerabilities in 5.2.5 | Apache POI OOXML |  |
| 10.7.0 | breaking | The selection of deprecated argument types like 'Float' and 'Currency' in enumeration has been removed from the UI |  |  |
| 10.6.2 | security | Mitigated CVE-2024-25710 by updating third-party dependencies. No known exploit available. |  |  |
| 10.6.1 | requirement | Updated the replication jar to version 1.0.4 | replication jar |  |
| 10.6.0 | requirement | Upgraded module to Mendix version 9.24.11 |  |  |
| 10.5.0 | migration-step | Introduction of migration file for JDM |  |  |
| 10.5.0 | requirement | Upgraded Mx Model Reflection module from version 6.2.0 to 7.0.0 | Mx Model Reflection |  |
| 10.4.0 | requirement | Replication jar upgraded from 1.0.2 to 1.0.3 | replication jar |  |
| 10.3.0 | requirement | Upgraded Excel Importer to Studio Pro v 9.18.4 |  |  |
| 10.3.0 | requirement | Upgraded Atlas Core 3.0.2 to 3.9.0 | Atlas Core |  |
| 10.3.0 | requirement | Upgraded Mx Model Reflection 6.1.2 to 6.2.0 | Mx Model Reflection |  |
| 10.1.2 | security | We fixed a security vulnerability (6.5 - CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H) |  |  |
| 10.1.1 | requirement | We have upgraded Apache POI to version 5.2.2. Related dependencies were also upgraded. | Apache POI |  |
| 10.1.1 | requirement | If you use Excel Exporter in your app, you should also upgrade that module | Excel Exporter |  |
| 10.0.2 | requirement | Updated commons-compress from version 1.19 to 1.21 | commons-compress |  |
| 10.0.0 | requirement | We upgraded the module to Mendix 9.0.5 and made it compatible with Atlas 3 |  |  |
| 9.2.7 | requirement | Updated the Apache Commons IO dependency to 2.17.0 | Apache Commons IO |  |
| 9.2.6 | security | Upgraded Apache POI OOXML to 5.3.0 to mitigate the vulnerabilities in 5.2.5 | Apache POI OOXML |  |
| 9.2.5 | security | Mitigated CVE-2024-25710 by updating third-party dependencies. No known exploit available. |  |  |
| 9.2.2 | security | We fixed a security vulnerability (6.5 - CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H) |  |  |
| 9.2.1 | requirement | We have upgraded Apache POI to version 5.2.2. Related dependencies were also upgraded. | Apache POI |  |
| 9.2.1 | requirement | If you use Excel Exporter in your app, you should also upgrade that module | Excel Exporter |  |
| 9.1.2 | requirement | Updated commons-compress from version 1.19 to 1.21 | commons-compress |  |
| 9.0.3 | requirement | We have upgraded the apache poi libraries. Manually remove versions older than 4.1.2 from userlib folder. | Apache poi libraries |  |
| 9.0.3 | security | We fixed CVE-2021-31339 |  |  |
| 9.0.0 | requirement | Updated to Mendix framework 8.12.4 |  |  |
| 9.0.0 | requirement | Updated Apache POI to 4.1.2 | Apache POI |  |
| 9.0.0 | requirement | Updated to Atlas UI |  |  |
| 8.2.4 | security | We fixed a security vulnerability (6.5 - CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H) |  |  |
| 8.2.3 | requirement | Updated commons-compress from version 1.19 to 1.21 | commons-compress |  |
| 8.2.3 | requirement | Updated Apache POI to 4.1.2 | Apache POI |  |
| 8.1.1 | requirement | Updated libraries: POI 4.0.0 -> 4.1.1, codec 1.11 -> 1.13, collections4 4.2 -> 4.4, OOXML 4.0.0 -> 4.1.1, compress 1.18 -> 1.19, io 2.3.0 -> 2.6, Schemas 4.0.0 -> 4.1.1, xmlbeans 3.0.1 -> 3.1.0 | Apache POI, Apache commons codec, Apache commons collections4, Apache POI OOXML, Apache commons compress, Apache commons io, Apache POI OOXML Schemas, xmlbeans |  |
| 8.1.0 | requirement | Updated Mendix Studio Pro version to 7.23.7 |  |  |
| 5.19.0 | requirement | Upgrade the replication jar to use StringUtils from apache-commons-lang3 | replication jar |  |
| 5.18.0 | requirement | Upgraded ojdbc6-11.2.0 jdbc driver to ojdbc8-12.2.0.1 | ojdbc6, sqljdbc4 |  |
| 5.18.0 | requirement | Upgraded sqljdbc4-4.0 jdbc driver to mssql-jdbc-7.0.0 | sqljdbc4 |  |
| 5.18.0 | removal | Removed axis2-kernel-1.0.jar and instead use Java 8 API for encoding and decoding | axis2-kernel-1.0.jar |  |
| 5.16.0 | removal | Removed third-party libraries dom4j, javax.xml.streams and xalan | dom4j, javax.xml.streams, xalan |  |
| 5.16.0 | security | Updated Apache POI to 4.0.0 to remove vulnerability CVE-2017-12626 | Apache POI |  |
| 5.16.0 | requirement | Updated poi-ooxml, poi-ooxml-schemas, xmlbeans and new libraries commons-coded, commons-collections4, commons-compress and commons-math | poi-ooxml, poi-ooxml-schemas, xmlbeans, commons-coded, commons-collections4, commons-compress, commons-math |  |

## Exit Intent (Wait Don't Go) <a id="21721"></a>
Widget, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/21721)

| version | published | min Mendix |
|---|---|---|
| 1.1.0 | 2021-02-02 | ? |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.1.0 | requirement | Add Mendix 8 Support |  |  |

## extension mcp server <a id="244441"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/244441)

| version | published | min Mendix |
|---|---|---|
| 3.2.2 | 2025-08-07 | 10.24.2 |
| 3.2.1 | 2025-08-06 | 10.24.2 |
| 3.2.0 | 2025-08-05 | 10.24.1 |
| 3.1.0 | 2025-08-04 | 10.24.1 |
| 3.0.0 | 2025-08-02 | 10.24.1 |
| 1.0.0 | 2025-07-30 | 10.24.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 3.0.0 | breaking | Refactor with python |  |  |

## External Database Connector <a id="219862"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/219862)

| version | published | min Mendix |
|---|---|---|
| 6.3.3 | 2026-09-23 | 11.12.0 |
| 6.3.2 | 2026-09-09 | 11.12.0 |
| 6.3.1 | 2026-08-11 | 11.12.0 |
| 6.3.0 | 2026-07-01 | 11.12.0 |
| 6.2.5 | 2026-05-21 | 11.4.0 |
| 6.2.4 | 2026-04-06 | 11.4.0 |
| 6.2.3 | 2026-02-18 | 11.4.0 |
| 6.2.2 | 2026-01-27 | 11.4.0 |
| 6.2.1 | 2025-11-27 | 11.4.0 |
| 6.2.0 | 2025-11-04 | 11.4.0 |
| 6.1.0 | 2025-09-30 | 11.3.0 |
| 6.0.0 | 2025-08-29 | 11.0.0 |
| 5.4.0 | 2026-09-23 | 10.24.0 |
| 5.3.9 | 2026-09-09 | 10.24.0 |
| 5.3.8 | 2026-08-12 | 10.24.0 |
| 5.3.7 | 2026-05-21 | 10.24.0 |
| 5.3.6 | 2026-04-03 | 10.24.0 |
| 5.3.5 | 2026-01-09 | 10.24.0 |
| 5.3.4 | 2025-11-24 | 10.24.0 |
| 5.3.3 | 2025-11-04 | 10.24.0 |
| 5.3.2 | 2025-10-20 | 10.24.0 |
| 5.3.1 | 2025-07-30 | 10.23.0 |
| 5.3.0 | 2025-05-29 | 10.23.0 |
| 5.2.0 | 2025-05-05 | 10.22.0 |
| 5.1.2 | 2025-06-05 | 10.21.0 |
| 5.1.1 | 2025-02-26 | 10.20.0 |
| 5.1.0 | 2025-01-28 | 10.19.0 |
| 5.0.1 | 2025-02-04 | 10.18.0 |
| 5.0.0 | 2024-12-18 | 10.18.0 |
| 4.1.1 | 2024-11-11 | 10.16.0 |
| 4.1.0 | 2024-10-30 | 10.16.0 |
| 4.0.2 | 2024-09-24 | 10.15.0 |
| 4.0.1 | 2024-08-28 | 10.14.0 |
| 4.0.0 | 2024-07-30 | 10.13.0 |
| 3.0.2 | 2024-11-13 | 10.12.4 |
| 3.0.1 | 2024-08-27 | 10.12.4 |
| 3.0.0 | 2024-06-25 | 10.12.0 |
| 2.0.1 | 2024-04-29 | 10.9.0 |
| 2.0.0 | 2024-03-27 | 10.9.0 |
| 1.0.2 | 2024-08-16 | 10.6.12 |
| … 2 older versions | | |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 6.3.3 | security | Resolved CVE-2026-85525 by upgrading snowflake jar to 4.3.4 | snowflake jar |  |
| 6.3.2 | security | Resolved CVE-2026-55856 through CVE-2026-55860 and CVE-2026-61700 by upgrading mariadb to 2.7.14 | mariadb |  |
| 6.3.2 | security | Resolved CVE-2026-59645 by upgrading Bouncy Castle libraries to 1.85 | Bouncy Castle libraries |  |
| 6.3.1 | security | Fixed CVE 2026-54291 by upgrading postgresql version to 42.7.12 | postgresql |  |
| 6.3.0 | breaking | Implementation of AdminAction is now replaced with HttpServelet | AdminAction | HttpServelet |
| 6.2.5 | security | Resolved CVE-2026-42198 by upgrading PostgreSQL JDBC driver to version 42.7.11 | PostgreSQL JDBC driver |  |
| 6.2.5 | improvement | Upgraded Bouncy Castle libraries (bcprov-jdk18on and bcpkix-jdk18on) to 1.84 | Bouncy Castle libraries |  |
| 6.2.5 | improvement | Now we use JVM-managed TLS versions | TLS |  |
| 6.2.4 | security | Resolved CVE-2026-3293 by upgrading Snowflake jar to version 4.0.2 | Snowflake jar |  |
| 6.2.1 | security | Resolved CVE-2025-59250 by upgrading Microsoft SQL Server JDBC driver to version 12.10.2.jre11 | Microsoft SQL Server JDBC driver |  |
| 6.2.0 | improvement | Upgraded Bouncy Castle libraries (bcprov-jdk18on and bcpkix-jdk18on) to 1.81 | Bouncy Castle libraries |  |
| 6.0.0 | security | Fixed CVE-2025-8916 by upgrading Bouncy Castle libraries (bcprov-jdk18on and bcpkix-jdk18on) to 1.79 | Bouncy Castle libraries |  |
| 5.4.0 | security | Fixed CVE-2026-85525 by upgrading snowflake-jdbc version to 4.3.4 | snowflake-jdbc |  |
| 5.3.9 | security | Resolved CVE-2026-55856 through CVE-2026-55860 and CVE-2026-61700 by upgrading mariadb to 2.7.14 | mariadb |  |
| 5.3.9 | security | Resolved CVE-2026-59645 by upgrading Bouncy Castle libraries to 1.85 | Bouncy Castle libraries |  |
| 5.3.8 | security | Fixed CVE 2026-54291 by upgrading postgresql version to 42.7.12 | postgresql |  |
| 5.3.7 | security | Resolved CVE-2026-42198 by upgrading PostgreSQL JDBC driver to version 42.7.11 | PostgreSQL JDBC driver |  |
| 5.3.7 | improvement | Upgraded Bouncy Castle libraries (bcprov-jdk18on and bcpkix-jdk18on) to 1.84 | Bouncy Castle libraries |  |
| 5.3.7 | improvement | Now we use JVM-managed TLS versions | TLS |  |
| 5.3.6 | security | Resolved CVE-2026-3293 by upgrading Snowflake jar to version 4.0.2 | Snowflake jar |  |
| 5.3.4 | security | Resolved CVE-2025-59250 by upgrading Microsoft SQL Server JDBC driver to version 12.10.2.jre11 | Microsoft SQL Server JDBC driver |  |
| 5.3.3 | improvement | Upgraded Bouncy Castle libraries (bcprov-jdk18on and bcpkix-jdk18on) to 1.81 | Bouncy Castle libraries |  |
| 5.3.2 | security | Fixed CVE-2025-8916 by upgrading Bouncy Castle libraries (bcprov-jdk18on and bcpkix-jdk18on) to 1.79 | Bouncy Castle libraries |  |
| 5.3.1 | security | Fixed CVE-2025-27496: Upgraded Snowflake to 3.24.2 | Snowflake |  |
| 5.3.1 | improvement | Upgraded GSON to 2.13.1 | GSON |  |
| 5.1.2 | requirement | Updated the module to Studio-Pro version 10.21.0 | Studio-Pro |  |
| 5.1.0 | feature | v5.1.0 introduces new feature using updated approach for connecting to databases during design time. Run app locally with latest connector before connecting |  |  |
| 5.0.1 | security | Fix CVE-2025-24789, Upgrade net.snowflake:snowflake-jdbc to version 3.22.0 | snowflake-jdbc |  |
| 5.0.0 | feature | External Database Connector introduces new beta feature using different approach for connecting to databases during design time with --enable-live-preview flag |  |  |
| 4.1.1 | security | Fix CVE-2024-43382: Upgrade net.snowflake:snowflake-jdbc to version 3.20.0 | snowflake-jdbc |  |
| 3.0.2 | security | Fix CVE-2024-43382: Upgrade net.snowflake:snowflake-jdbc to version 3.20.0 | snowflake-jdbc |  |
| 1.0.1 | security | Fixed CVE-2024-1597: Upgraded to postgresql@42.4.4 | postgresql |  |

## Fabric Canvas <a id="229582"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/229582)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2024-08-08 | 10.6.6 |

## Fake Data <a id="112021"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/112021)

| version | published | min Mendix |
|---|---|---|
| 2.0.0 | 2022-02-10 | 9.0.5 |
| 1.4.0 | 2021-01-15 | 8.0.0 |
| 1.3.1 | 2019-12-02 | 8.0.0 |
| 1.3.0 | 2019-11-27 | 8.0.0 |
| 1.2.0 | 2019-11-22 | 8.0.0 |
| 1.1.0 | 2019-11-22 | 8.0.0 |
| 1.0.0 | 2019-11-22 | 8.0.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.0.0 | requirement | Upgrade to MX 9.0.5 minimum required version. |  |  |
| 2.0.0 | improvement | Update libraries. |  |  |
| 1.1.0 | breaking | Refactored Java Action names. |  |  |

## FDS Gateway Login Connector <a id="303885"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/303885)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2026-08-21 | 10.24.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.0.0 | requirement | Minimum Mendix version required: 10.24.0 | Mendix |  |
| 1.0.0 | migration-step | Module builds upon earlier Siemens Access Management (SAM) module, bringing functionality to Marketplace using current FDS terminology. | Siemens Access Management (SAM) |  |

## Fieldset <a id="113922"></a>
Widget, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/113922)

| version | published | min Mendix |
|---|---|---|
| 3.2.2 | 2026-02-10 | 9.6.0 |
| 3.2.1 | 2023-09-27 | 9.6.0 |
| 3.2.0 | 2023-06-05 | 9.6.0 |
| 3.1.1 | 2022-10-15 | 9.6.0 |
| 3.1.0 | 2021-12-23 | 9.6.0 |
| 3.0.1 | 2021-12-03 | 9.6.0 |
| 3.0.0 | 2021-09-28 | 9.6.0 |
| 2.0.0 | 2021-07-28 | 9.0.5 |
| 1.0.0 | 2020-04-22 | 8.3.1 |

## File Dropper <a id="111497"></a>
Widget, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/111497)

| version | published | min Mendix |
|---|---|---|
| 1.4.0 | 2022-01-07 | 8.0.0 |
| 1.3.2 | 2021-05-21 | 8.0.0 |
| 1.3.1 | 2020-08-31 | 8.0.0 |
| 1.3.0 | 2020-04-16 | 8.0.0 |
| 1.2.2 | 2020-03-24 | 8.0.0 |
| 1.2.1 | 2020-03-04 | 8.0.0 |
| 1.2.0 | 2020-02-26 | 8.0.0 |
| 1.1.1 | 2020-01-08 | 8.0.0 |
| 1.1.0 | 2019-11-22 | 8.0.0 |
| 1.0.0 | 2019-10-15 | 8.0.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.4.0 | feature | Adding before commit MF/NF to commit context object before committing files |  |  |
| 1.3.0 | improvement | Update dependencies |  |  |
| 1.2.2 | breaking | Replace the success color |  |  |
| 1.1.0 | improvement | Moved methods to @jeltemx/mendix-react-widget-utils for reuse in other projects | @jeltemx/mendix-react-widget-utils |  |

## File Type Checker <a id="108388"></a>
Module, Ciphix, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/108388)

| version | published | min Mendix |
|---|---|---|
| 1.0.2 | 2019-03-01 | 7.8.0 |
| 1.0.1 | 2019-02-01 | 7.8.0 |
| 1.0.0 | 2019-01-21 | 7.8.0 |

## File Uploader <a id="235351"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/235351)

| version | published | min Mendix |
|---|---|---|
| 2.5.0 | 2026-06-29 | 10.22.0 |
| 2.4.2 | 2026-04-24 | 10.22.0 |
| 2.4.1 | 2026-02-13 | 10.22.0 |
| 2.4.0 | 2025-12-11 | 10.22.0 |
| 2.3.0 | 2025-08-15 | 10.22.0 |
| 2.2.2 | 2025-07-01 | 10.22.0 |
| 2.2.1 | 2025-05-28 | 10.22.0 |
| 2.2.0 | 2025-05-07 | 10.22.0 |
| 2.1.0 | 2025-04-16 | 10.21.0 |
| 2.0.0 | 2025-03-14 | 10.15.0 |
| 1.0.3 | 2025-02-28 | 9.24.0 |
| 1.0.2 | 2025-02-14 | 9.24.0 |
| 1.0.1 | 2024-12-19 | 9.24.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.5.0 | fix | Fixed validation errors persisting after uploading valid file. | validation errors |  |
| 2.5.0 | fix | Fixed dropping more files than allowed rejecting entire batch; now only excess rejected. | file upload |  |
| 2.5.0 | fix | Fixed files rejected due to total limit with no recovery; now show retry button. | file limit, retry |  |
| 2.5.0 | breaking | Maximum number of files property now optional; 0/empty means unlimited (default 10). | Maximum number of files |  |
| 2.5.0 | improvement | Files now upload in queue instead of marked as errors; queued files show 'Waiting...' state. | file queue, concurrent uploads |  |
| 2.5.0 | improvement | Removing file with default button now removes from list immediately, not greyed out. | remove button, file list |  |
| 2.4.2 | fix | Fixed Download button not working on Mendix 11.8. | Download button |  |
| 2.3.0 | fix | Fixed file uploader allowing more files on refresh despite maximum reached. | maximum uploaded files |  |
| 2.3.0 | improvement | Changed max file configuration to set maximum uploaded files through expression. | max file configuration |  |
| 2.1.0 | requirement | Updated minimum Mendix version to 10.21.0 to support Mendix 11. | Mendix Studio Pro |  |
| 2.0.0 | requirement | Bumped minimum supported version to 10.15.0. | Mendix |  |
| 1.0.2 | fix | Fixed error when uploading multiple files on newly created context object. | multiple files, context object |  |
| 1.0.2 | fix | Fixed users uploading unsupported image formats in image mode. | image mode |  |
| 1.0.2 | feature | Added timeout functionality to abort upload if object not created within timeout. | File/Image creation action |  |

## FileDropper_Widget <a id="201367"></a>
Module, Mendix, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/201367)

| version | published | min Mendix |
|---|---|---|
| 1.1.1 | 2026-05-07 | 10.24.1 |

## FileHandling <a id="63667"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/63667)

| version | published | min Mendix |
|---|---|---|
| 1.4.0 | 2020-09-23 | 8.5.1 |
| 1.3.0 | 2019-11-27 | 7.23.1 |
| 1.2.0 | 2019-07-25 | 7.23.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.4.0 | requirement | Updated module to 8.5.1, requires minimum Mendix 8.5.1 |  |  |
| 1.2.0 | requirement | Converted module to 7.23.1, requires minimum Mendix 7.23.1 |  |  |
| 1.2.0 | removal | Removed library dependencies apache commons fileupload 1.2.1 and codec 1.10, can be removed from project if unused elsewhere | apache commons fileupload 1.2.1, apache commons codec 1.10 |  |

## FilterView <a id="116768"></a>
Widget, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/116768)

| version | published | min Mendix |
|---|---|---|
| 1.2.0 | 2021-08-02 | 8.0.0 |
| 1.1.0 | 2021-07-15 | 9.1.0 |
| 1.0.0 | 2021-02-01 | 8.12.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.2.0 | requirement | Widget documented for use with Mendix 8 and below only. |  |  |
| 1.1.0 | fix | Update to remove deprecated client API warning. |  |  |

## FiServ (cardpointe) Connector <a id="208930"></a>
Service, Kinetech, Partner, [marketplace](https://marketplace.mendix.com/link/component/208930)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2023-03-27 | 8.0.0 |

## Fix document names <a id="234097"></a>
Module, Siemens, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/234097)

| version | published | min Mendix |
|---|---|---|
| 1.2.1 | 2025-07-04 | 10.12.0 |
| 1.1.0 | 2025-05-28 | 10.12.0 |
| 1.0.0 | 2024-11-25 | 10.12.0 |

## FontAwesome for Mendix <a id="119189"></a>
Module, Mariusvanderknaap, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/119189)

| version | published | min Mendix |
|---|---|---|
| 2.0.0 | 2022-04-19 | 9.6.2 |
| 1.0.0 | 2021-12-15 | 9.6.2 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.0.0 | requirement | Upgraded to FontAwesome 6.1.1. | FontAwesome |  |

## Forgot Password module <a id="1296"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/1296)

| version | published | min Mendix |
|---|---|---|
| 6.5.1 | 2026-07-14 | 10.21.1 |
| 6.5.0 | 2026-04-30 | 10.21.1 |
| 6.4.0 | 2025-09-29 | 10.21.1 |
| 6.3.0 | 2025-05-15 | 10.21.1 |
| 6.2.0 | 2025-05-15 | 10.12.10 |
| 6.1.0 | 2024-11-28 | 10.12.10 |
| 6.0.0 | 2024-04-11 | 10.6.0 |
| 5.6.1 | 2025-09-29 | 9.24.2 |
| 5.6.0 | 2025-05-15 | 9.24.2 |
| 5.5.0 | 2024-01-18 | 9.24.2 |
| 5.4.1 | 2023-12-13 | 9.24.2 |
| 5.4.0 | 2023-09-20 | 9.24.2 |
| 5.3.1 | 2023-06-15 | 9.24.2 |
| 5.3.0 | 2023-05-15 | 9.24.2 |
| 5.2.0 | 2023-03-15 | 9.22.0 |
| 5.1.1 | 2023-03-09 | 9.12.7 |
| 5.1.0 | 2023-01-19 | 9.12.7 |
| 5.0.0 | 2022-10-19 | 9.12.7 |
| 4.1.3 | 2023-09-20 | 8.18.22 |
| 4.1.2 | 2023-05-15 | 8.18.22 |
| 4.1.1 | 2023-03-09 | 8.18.22 |
| 4.1.0 | 2023-01-19 | 8.18.22 |
| 4.0.0 | 2022-10-19 | 8.18.21 |
| 3.7.3 | 2023-09-20 | 7.23.33 |
| 3.7.2 | 2023-05-15 | 7.23.33 |
| 3.7.1 | 2023-03-09 | 7.23.22 |
| 3.7.0 | 2023-01-19 | 7.23.33 |
| 3.6.0 | 2022-10-19 | 7.23.33 |
| 3.5.1 | 2022-02-26 | 8.18.13 |
| 3.2.2 | 2022-03-04 | 7.23.19 |
| 3.2.1 | 2021-01-14 | 7.23.19 |
| 3.2.0 | 2019-11-08 | 7.23.3 |
| 3.1.0 | 2019-05-15 | 7.3.0 |
| 3.0.0 | 2019-03-26 | 7.3.0 |
| 2.0.0 | 2017-11-17 | 7.3.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 6.5.1 | fix | Fixed the LoginContext reference for validation messages in ACT_Login | ACT_Login, LoginContext |  |
| 6.5.0 | improvement | Added org.apache.velocity:velocity-engine-core to version 2.4.1 | org.apache.velocity:velocity-engine-core |  |
| 6.5.0 | improvement | Anonymous userrole no longer needed for password reset functionality to mitigate unintended access risk |  |  |
| 6.4.0 | requirement | Added Community Commons module as dependency if Email Connector module is upgraded to v6.3.0 and above | Community Commons |  |
| 6.3.0 | requirement | v.6.3.0 version for apps on Mx10.21.1 or higher |  |  |
| 6.1.0 | requirement | v.6.1.0 version for apps on Mx10.12.10 or higher |  |  |
| 5.5.0 | fix | Fixed Mendix 10 compatibility issue |  |  |
| 5.4.0 | security | Fixed security vulnerability (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N) |  |  |
| 5.2.0 | requirement | Upgraded to Mendix Studio Pro v9.22.0 |  |  |
| 5.1.1 | security | Fixed security vulnerability (5.3 - CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N) |  |  |
| 5.1.0 | breaking | Replaced Email Module with Templates with Email connector (Ticket #169522, #169643, #170709, #169160) | Email Module with Templates | Email connector |
| 5.1.0 | fix | Fixed issue related to cookies in Mendix studio pro-9.20 (Ticket #174456, #173282) |  |  |
| 5.1.0 | migration-step | Changed License to MIT |  |  |
| 5.0.0 | fix | Fixed issues related to Deep Link module. Now compatible with latest Deep Link module from Marketplace (Ticket #149147, #152032) | Deep Link module |  |
| 4.1.3 | security | Fixed security vulnerability (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N) |  |  |
| 4.1.1 | security | Fixed security vulnerability (5.3 - CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N) |  |  |
| 4.1.0 | breaking | Replaced Email Module with Templates with Email connector (Ticket #169522, #169643, #170709, #169160) | Email Module with Templates | Email connector |
| 4.1.0 | migration-step | Changed License to MIT |  |  |
| 4.0.0 | fix | Fixed issues related to Deep Link module. Now compatible with latest Deep Link module from Marketplace (Ticket #149147, #152032) | Deep Link module |  |
| 3.7.3 | security | Fixed security vulnerability (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N) |  |  |
| 3.7.1 | security | Fixed security vulnerability (5.3 - CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N) |  |  |
| 3.7.0 | migration-step | Changed License to MIT |  |  |
| 3.6.0 | fix | Fixed issues related to Deep Link module. Now compatible with latest Deep Link module from Marketplace (Ticket #149147, #152032) | Deep Link module |  |
| 3.5.1 | requirement | Upgrade to Studio 8.18.13 |  |  |
| 3.5.1 | security | Fixed CVE-2022-26313 and CVE-2022-26314 |  |  |
| 3.2.2 | security | Fixed CVE-2022-26314 |  |  |
| 3.2.1 | security | Fixed security exploit |  |  |
| 3.2.0 | requirement | Upgrade to 7.23.3 |  |  |
| 3.1.0 | fix | Fixed issue where ValidUntil and IsSignUp attributes would be empty due to user lacking entity access | ValidUntil, IsSignUp |  |
| 3.0.0 | security | This release includes an important security fix. All users strongly advised to update to latest release |  |  |

## Format String <a id="264"></a>
Widget, Mendix, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/264)

| version | published | min Mendix |
|---|---|---|
| 6.0.1 | 2021-08-04 | 7.23.0 |
| 6.0.0 | 2019-08-01 | 7.23.0 |
| 5.8.1 | 2019-07-29 | 7.23.0 |
| 5.8.0 | 2019-07-25 | 7.23.0 |
| 5.7.1 | 2018-02-12 | ? |
| 5.7.0 | 2017-11-16 | ? |
| 5.6.0 | 2017-07-04 | ? |
| 5.5.2 | 2017-02-13 | ? |
| 5.5.1 | 2016-12-29 | ? |
| 5.5 | 2016-11-14 | ? |
| 5.4 | 2016-03-10 | ? |
| 5.3 | 2016-01-18 | ? |
| 5.2 | 2015-11-20 | ? |
| 5.1 | 2015-10-27 | ? |
| 5.0 | 2015-05-20 | ? |
| 4.1 | 2015-03-06 | ? |
| 4.0 | 2015-03-02 | ? |
| 3.2 | 2015-02-23 | ? |
| 3.1.1 | 2014-10-15 | ? |
| 3.1 | 2014-10-08 | ? |
| 3.0.2 | 2014-03-21 | ? |
| 3.0.1 | 2014-01-23 | ? |
| 3.0 | 2014-01-17 | ? |
| 2.1 | 2013-09-05 | ? |
| 2.0 | 2013-08-16 | ? |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 6.0.1 | removal | Removed deprecated warnings |  |  |
| 6.0.0 | fix | Fix for Mendix 8 compatibility |  |  |
| 5.7.0 | feature | Offline capable |  |  |
| 5.6.0 | breaking | getReferences now done asynchronously instead of synchronously | getReferences |  |
| 5.3 | breaking | Renamed laguagePack.json to .js | laguagePack.json |  |
| 5.2 | fix | Fix deprecations for MX6 release |  |  |
| 5.0 | removal | Removed option to render text as javascript |  |  |
| 4.0 | requirement | Version for Mx 5.14 and up |  |  |
| 3.2 | requirement | Compatible with 5.10 and up |  |  |
| 3.1 | breaking | This version breaks with previous versions of this widget in your project |  |  |
| 3.0.1 | requirement | MX5 version - not for use in MX4 |  |  |
| 3.0 | fix | Fixed to handle associations in MX5 |  |  |
| 3.0 | requirement | Version compatible with MX5, not MX4 or earlier |  |  |
| 2.1 | requirement | MX4 compatible, NOT compatible with MX5 |  |  |
| 2.0 | requirement | Version compatible with MX5 |  |  |

## Forms Template <a id="118330"></a>
Starter App, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/118330)

| version | published | min Mendix |
|---|---|---|
| 11.19.0 | 2026-10-05 | 11.15.0 |
| 11.18.0 | 2026-08-26 | 11.14.0 |
| 11.17.0 | 2026-08-03 | 11.13.0 |
| 11.16.0 | 2026-07-28 | 11.12.2 |
| 11.15.0 | 2026-07-16 | 11.12.1 |
| 11.14.0 | 2026-07-01 | 11.12.0 |
| 11.13.0 | 2026-06-01 | 11.11.0 |
| 11.12.0 | 2026-04-29 | 11.10.0 |
| 11.11.1 | 2026-04-17 | 11.9.1 |
| 11.11.0 | 2026-04-17 | 11.9.1 |
| 11.10.0 | 2026-04-07 | 11.9.0 |
| 11.9.0 | 2026-03-02 | 11.8.0 |
| 11.8.1 | 2026-02-11 | 11.7.0 |
| 11.8.0 | 2026-01-30 | 11.7.0 |
| 11.7.0 | 2026-01-29 | 11.6.3 |
| 11.6.0 | 2026-01-12 | 11.6.2 |
| 11.5.0 | 2026-01-07 | 11.6.1 |
| 11.4.0 | 2025-12-23 | 11.6.0 |
| 11.3.0 | 2025-11-25 | 11.5.0 |
| 11.2.0 | 2025-11-04 | 11.4.0 |
| 11.1.0 | 2025-07-31 | 11.1.0 |
| 11.0.0 | 2025-07-17 | 11.0.0 |
| 2.35.0 | 2025-06-25 | 10.24.0 |
| 2.34.0 | 2025-05-28 | 10.23.0 |
| 2.33.0 | 2025-05-02 | 10.22.0 |
| 2.32.0 | 2025-04-25 | 10.21.0 |
| 2.31.0 | 2025-02-04 | 10.18.2 |
| 2.30.0 | 2025-01-28 | 10.19.0 |
| 2.29.0 | 2025-01-10 | 10.18.1 |
| 2.28.0 | 2024-12-18 | 10.18.0 |
| 2.27.0 | 2024-11-27 | 10.17.0 |
| 2.26.0 | 2024-11-11 | 10.16.1 |
| 2.25.0 | 2024-10-30 | 10.16.0 |
| 2.24.0 | 2024-09-24 | 10.15.0 |
| 2.23.0 | 2024-08-27 | 10.14.0 |
| 2.22.0 | 2024-08-07 | 10.13.1 |
| 2.21.0 | 2024-07-30 | 10.13.0 |
| 2.19.0 | 2024-07-05 | 10.12.1 |
| 2.18.0 | 2024-06-25 | 10.12.0 |
| 2.17.0 | 2024-05-31 | 10.11.0 |
| … 24 older versions | | |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 11.19.0 | requirement | Minimum Mendix version upgraded to 11.15.0 |  |  |
| 11.19.0 | removal | MxSSO has been removed | MxSSO |  |
| 11.18.0 | requirement | Upgraded to 11.14.0 | Mendix |  |
| 11.17.0 | requirement | Upgraded to 11.13.0 | Mendix |  |
| 11.16.0 | requirement | Upgraded to Mx 11.12.2 | Mendix |  |
| 11.15.0 | requirement | Upgraded to Mendix 11.12.1 | Mendix |  |
| 11.14.0 | requirement | Upgraded to Mx 11.12.0 | Mendix |  |
| 11.13.0 | requirement | Upgraded to 11.11.0 | Mendix |  |
| 11.12.0 | requirement | Upgraded to Mx 11.10.0 | Mendix |  |
| 11.11.0 | requirement | Upgraded to version 11.9.1 | Mendix |  |
| 11.10.0 | requirement | Upgraded to version 11.9.0 | Mendix |  |
| 11.9.0 | requirement | Upgraded to 11.9.0 | Mendix |  |
| 11.8.0 | requirement | Upgraded to version 11.7.0 | Mendix |  |
| 11.7.0 | requirement | Upgraded to version 11.6.3 | Mendix |  |
| 11.6.0 | requirement | Upgraded to version 11.6.2 | Mendix |  |
| 11.5.0 | requirement | Upgraded to version 11.6.1 | Mendix |  |
| 11.4.0 | requirement | Upgraded to version 11.6.0 | Mendix |  |
| 11.3.0 | requirement | Upgraded to version 11.5.0 | Mendix |  |
| 11.2.0 | requirement | Upgraded to version 11.4.0 | Mendix |  |
| 11.1.0 | requirement | Upgraded to version 11.1.0 | Mendix |  |
| 11.0.0 | requirement | Upgraded to 11.0.0 | Mendix |  |
| 11.0.0 | requirement | Upgraded MendixSSO to 10.4.0 | MendixSSO |  |
| 2.35.0 | requirement | Upgraded to 10.24.0 | Mendix |  |
| 2.34.0 | requirement | Upgraded to version 10.23.0 | Mendix |  |
| 2.33.0 | requirement | Upgraded to version 10.22.0 | Mendix |  |
| 2.32.0 | requirement | Upgraded to Mx 10.21.0 | Mendix |  |
| 2.31.0 | requirement | Upgraded to version 10.18.2 | Mendix |  |
| 2.30.0 | requirement | Upgraded to version 10.19.0 | Mendix |  |
| 2.29.0 | requirement | Upgraded to version 10.18.1 | Mendix |  |
| 2.28.0 | requirement | Upgraded to version 10.18.0 | Mendix |  |
| 2.27.0 | requirement | Upgraded to version 10.17.0 | Mendix |  |
| 2.26.0 | requirement | Upgraded to version 10.16.1 | Mendix |  |
| 2.25.0 | requirement | Upgraded to version 10.16.0 | Mendix |  |
| 2.24.0 | requirement | Upgraded to version 10.15.0 | Mendix |  |
| 2.23.0 | requirement | Upgraded to version 10.14.0 | Mendix |  |
| 2.22.0 | requirement | Upgraded to version 10.13.1 | Mendix |  |
| 2.21.0 | requirement | Upgraded to version 10.13.0 | Mendix |  |
| 2.19.0 | requirement | Upgraded to version 10.12.1 | Mendix |  |
| 2.18.0 | requirement | Upgraded to version 10.12.0 | Mendix |  |
| 2.17.0 | requirement | Upgraded to 10.11.0 | Mendix |  |
| 2.16.0 | requirement | Upgraded to 10.9.0 | Mendix |  |
| 2.15.0 | requirement | Upgraded to 10.8.1 | Mendix |  |
| 2.15.0 | improvement | Updated all modules to the latest version |  |  |
| 2.14.0 | requirement | Upgraded to 10.8.0 | Mendix |  |
| 2.13.0 | requirement | Upgraded to 10.7.0 | Mendix |  |
| 2.12.0 | requirement | Upgraded to version 10.6.2 | Mendix |  |
| 2.11.0 | requirement | Upgraded to version 10.6.1 | Mendix |  |
| 2.10.0 | requirement | Upgraded to version 10.6.0 | Mendix |  |
| 2.9.0 | requirement | Upgraded to 10.5.0 | Mendix |  |
| 2.9.0 | improvement | Upgraded modules and widgets |  |  |
| 2.8.0 | requirement | Upgraded to version 10.4.1 | Mendix |  |
| 2.6.0 | requirement | Upgraded to version 10.4.0 | Mendix |  |
| 2.5.0 | requirement | Upgraded to version 10.3.1 | Mendix |  |
| 2.4.0 | requirement | Upgraded to version 10.3.0 | Mendix |  |
| 2.3.0 | requirement | Upgraded to version 10.2.0 | Mendix |  |
| 2.2.0 | requirement | Upgraded to version 10.1.1 | Mendix |  |
| 2.1.0 | requirement | Upgraded to version 10.1.0 | Mendix |  |
| 2.0.0 | requirement | Upgraded to Mendix 10.0.0 | Mendix |  |
| 1.9.0 | requirement | Upgraded to version 9.24.3 | Mendix |  |
| 1.8.0 | requirement | Upgraded to version 9.24.2 | Mendix |  |
| 1.7.0 | requirement | Upgraded to version 9.24.1 | Mendix |  |
| 1.6.0 | requirement | Upgraded to version 9.24.0 | Mendix |  |
| 1.5.0 | requirement | Upgraded to version 9.23.0 | Mendix |  |
| 1.4.0 | requirement | Upgraded to version 9.20.0 | Mendix |  |
| 1.3.0 | requirement | Upgraded to version 9.19.0 | Mendix |  |
| 1.2.0 | requirement | Upgraded to version 9.18.1 | Mendix |  |

## Fullscreen <a id="216857"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/216857)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2023-09-29 | 9.24.5 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.0.0 | requirement | Minimum Mendix version requirement: 9.24.5 | Mendix |  |

## GenAI Commons <a id="239448"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/239448)

| version | published | min Mendix |
|---|---|---|
| 7.2.0 | 2026-08-07 | 11.12.2 |
| 7.1.1 | 2026-07-24 | 11.12.1 |
| 7.0.0 | 2026-07-02 | 11.12.0 |
| 6.2.1 | 2026-04-28 | 10.24.13 |
| 6.2.0 | 2026-04-15 | 10.24.13 |
| 6.1.0 | 2026-03-27 | 10.24.13 |
| 6.0.1 | 2026-03-18 | 10.24.13 |
| 6.0.0 | 2026-03-09 | 10.24.13 |
| 5.6.0 | 2026-01-19 | 10.24.13 |
| 5.5.0 | 2025-12-22 | 10.24.13 |
| 5.4.1 | 2025-11-24 | 10.24.0 |
| 5.4.0 | 2025-11-21 | 10.24.0 |
| 5.3.0 | 2025-09-19 | 10.24.0 |
| 5.2.0 | 2025-08-29 | 10.24.0 |
| 5.1.0 | 2025-08-13 | 10.24.0 |
| 5.0.0 | 2025-08-08 | 10.24.0 |
| 4.3.0 | 2025-07-21 | 10.21.0 |
| 4.2.0 | 2025-07-02 | 10.21.0 |
| 4.1.0 | 2025-06-24 | 10.21.0 |
| 4.0.1 | 2025-06-17 | 10.21.0 |
| 4.0.0 | 2025-06-13 | 10.21.0 |
| 3.0.0 | 2025-04-08 | 10.21.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 7.2.0 | requirement | Upgrade to Mendix 11.12.2. | Mendix |  |
| 7.2.0 | improvement | Internal domain model and code changes to support streaming across providers. |  |  |
| 7.1.1 | requirement | Upgrade to Mendix 11.12.1. | Mendix |  |
| 7.1.1 | improvement | Changes in Model documents to support Azure (AI Foundry) as model provider for text generation. | Model documents |  |
| 7.1.1 | fix | Fixed bug where primitive 'Request' or 'Tool' input parameters did not work for tool microflows, especially via MCP Client module. | Request, Tool, tool microflows, MCP Client |  |
| 7.1.1 | fix | Version 7.1.1 removed a dependency that was introduced by accident in 7.1.0. |  |  |
| 7.0.0 | requirement | Module upgraded to Mendix 11.12. Small changes applied to resolve warnings from deprecated Java method. | Mendix |  |
| 6.2.1 | improvement | Changed how jackson library is declared in module dependencies for automatic updates. Fixes severe vulnerability in jackson library. | jackson |  |
| 6.2.0 | feature | Introduced new attribute InternalToolType to create correct UI per type. | InternalToolType |  |
| 6.1.0 | fix | Changed order in which messages are added to request to prevent incorrect message ordering passed to model. |  |  |
| 6.1.0 | feature | Added ModelDocumentID and _QualifiedName attributes to ConsumedKnowledgeBases to improve UI for Mendix Cloud GenAI configuration. | ConsumedKnowledgeBases, ModelDocumentID, _QualifiedName |  |
| 6.0.1 | fix | Fixed bug where chat completions with tool calling caused errors if following assistant response was empty. | tool calling |  |
| 6.0.0 | feature | New User Access and Approval feature makes tool calls visible to users and provides control to execute or reject tools. | User Access, Approval, tool calls |  |
| 6.0.0 | breaking | Chat completions behavior changed: tool call response sent to microflow without final assistant response unless SaveToolCallHistory is false. | SaveToolCallHistory |  |
| 6.0.0 | improvement | Moved logic from Java code to microflows, especially tool execution, for easier debugging. | tool execution |  |
| 6.0.0 | breaking | 'Add Message to Request' action now returns the added message; existing code may require updates. | Add Message to Request |  |
| 6.0.0 | removal | Removed entity 'Argument' associated to ToolCall. Use 'Input' attribute of ToolCall instead. | Argument, ToolCall | Input |
| 6.0.0 | migration-step | Domain modules adjusted for future functionalities. Related modules may require data migration per migration guide. | Agent Commons, Connectors |  |
| 5.6.0 | feature | Added Schema attribute to Tool entity and Input attribute to ToolCall entity for external tools like MCP. | Tool, Schema, ToolCall, Input |  |
| 5.6.0 | removal | Removed ArgumentInput and EnumValue entities and related microflows; no longer needed. | ArgumentInput, EnumValue |  |
| 5.6.0 | migration-step | Update connector modules, especially MCP Client, to be compatible with this version. | MCP Client, connectors |  |
| 5.5.0 | feature | Added Agent version information to trace entity to persist even after agent version deletion. | trace entity, Agent version |  |
| 5.5.0 | requirement | Module upgraded to Mendix 10.24.13. | Mendix |  |
| 5.4.0 | feature | Added MCPSpan entity and MCPServerName attribute for Tools to support ConversationalUI v5.3.0 observability. | MCPSpan, MCPServerName, Tools |  |
| 5.4.0 | known-issue | Traces created in version 5.3.0 might not display correctly after update due to data inconsistencies. |  |  |
| 5.3.0 | feature | Enabled traceability by storing each LLM invocation including tool calling in database for TraceMonitoring role. | traceability, LLM invocation, tool calling |  |
| 5.3.0 | feature | Storing traces enabled by default; can be disabled via StoreTraces constant. | StoreTraces |  |
| 5.3.0 | feature | Response objects now contain random GUID if connector did not map Id from model response. TraceCleanUpAfterDays constant enables cleanup. | Response, TraceCleanUpAfterDays |  |
| 5.2.0 | migration-step | Request_AddTool Java action moved to MCP Client module and renamed to Request_AddMCPTool. | Request_AddTool, Request_AddMCPTool, MCP Client | Request_AddMCPTool |
| 5.2.0 | feature | Added several smaller actions to support connector building for MCP Clients. | MCP Client |  |
| 5.1.0 | feature | Added entities and actions for connector builders: ArgumentInput, EnumValue, Request_AddTool, and related actions for tool calling. | ArgumentInput, EnumValue, Request_AddTool, ArgumentInput_CreateAndAdd, EnumValue_CreateAndAdd |  |
| 5.0.0 | requirement | Module upgraded to Mendix Studio Pro version 10.24. | Mendix |  |
| 4.3.0 | feature | Tool microflows can now accept multiple primitive input parameters of various types (Boolean, Enumeration, Integer, DateTime, Decimal). | Tool microflows |  |
| 4.3.0 | feature | When tool microflow call fails, model receives error message and chat interaction continues. | tool microflow calls |  |
| 4.3.0 | breaking | 'Arguments' attribute of ToolCall entity replaced by new entity 'Argument'. | ToolCall, Arguments, Argument | Argument |
| 4.3.0 | breaking | Embeddings_ChunkCollection now creates Usage object and adds request duration to EmbeddingsResponse. | Embeddings_ChunkCollection, Usage, EmbeddingsResponse |  |
| 4.2.0 | feature | Several actions removed from connectors and centralized in this module for knowledge base retrieval operations. | knowledge base retrieval |  |
| 4.1.0 | improvement | Minor changes (granted entity access for DeployedKnowledgeBase) to support runtime agent configuration via AgentCommons. | DeployedKnowledgeBase |  |
| 4.0.0 | feature | New entity DeployedKnowledgeBase represents knowledge base utilized by Mendix app with connection info and retrieval microflow name. | DeployedKnowledgeBase |  |
| 4.0.0 | migration-step | Update GenAI connectors to newest version and ensure new entities are being used for existing implementations. | DeployedKnowledgeBase, GenAI connectors |  |
| 4.0.0 | breaking | Toolbox actions have been renamed and restructured. | Toolbox actions |  |
| 4.0.0 | feature | New attribute added to store name of FileDocuments added to FileCollection. | FileCollection |  |
| 4.0.0 | feature | Moved _ID attribute for session to GenAICommons for connector agnostic use. | _ID, session |  |
| 3.0.0 | breaking | Module converted from Add-On module to App module. |  |  |
| 3.0.0 | requirement | Module updated to Mendix Studio Pro 10.21.0. | Mendix |  |
| 3.0.0 | migration-step | Backup data; delete Add-On module; download marketplace module (now in Marketplace category); test and restore data. |  |  |

## GenAI For Mendix (Mx 9) <a id="227931"></a>
Module, Mendix, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/227931)

| version | published | min Mendix |
|---|---|---|
| 2.4.1 | 2025-08-06 | 9.24.2 |
| 2.4.0 | 2025-04-01 | 9.24.2 |
| 2.3.1 | 2025-03-13 | 9.24.2 |
| 2.3.0 | 2025-03-12 | 9.24.2 |
| 2.2.0 | 2025-02-14 | 9.24.2 |
| 2.1.0 | 2025-02-03 | 9.24.2 |
| 2.0.0 | 2025-01-13 | 9.24.2 |
| 1.5.1 | 2024-10-17 | 9.24.2 |
| 1.5.0 | 2024-10-16 | 9.24.2 |
| 1.4.0 | 2024-09-19 | 9.24.2 |
| 1.3.0 | 2024-08-28 | 9.24.2 |
| 1.2.1 | 2024-07-31 | 9.24.2 |
| 1.2.0 | 2024-07-25 | 9.24.2 |
| 1.1.1 | 2024-07-04 | 9.24.2 |
| 1.0.0 | 2024-06-24 | 9.24.2 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.3.0 | breaking | Renamed 'File' to 'Document' in ENUM_ModelModality. | GenAICommons, ENUM_ModelModality | Document |
| 2.2.0 | feature | Function microflows updated to accept 'Tool' and/or 'Request' as optional input parameters. | GenAICommons |  |
| 2.2.0 | removal | Removed 'retrieve' and 'generate' actions. New 'Tools: Add Mendix Cloud Knowledge Base' action introduced for knowledge base retrieval. | MxGenAIConnector, retrieve, generate | Tools: Add Mendix Cloud Knowledge Base |
| 2.1.0 | feature | Pages updated to support React client: unsupported widgets replaced with supported ones. Module now usable with React client enabled (SP 10.18 onwards). | ConversationalUI |  |
| 2.0.0 | requirement | Modules MxGenAIConnector, GenAICommons and ConversationalUI bundled into one listing, downloaded at once. | MxGenAIConnector, GenAICommons, ConversationalUI |  |
| 2.0.0 | feature | GenAICommons now provides Chat Completions, Embeddings and Image Generation operations expecting DeployedModel as input. ConversationalUI microflows compatible with DeployedModel. | GenAICommons |  |
| 2.0.0 | breaking | Toolbox actions renamed and restructured. | ConversationalUI, Toolbox actions |  |
| 2.0.0 | migration-step | Update GenAI connectors to newest version and follow migration steps in release notes. | GenAI connectors |  |
| 2.0.0 | migration-step | Update ConversationalUI toolbox actions parameters and pass DeployedModel or specialization. See examples. | ConversationalUI, toolbox actions |  |
| 1.4.0 | requirement | Latest version of GenAI Commons module required; latest OpenAI Connector version supports token consumption monitoring. | GenAI Commons, OpenAI Connector |  |

## Global Inbox <a id="259162"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/259162)

| version | published | min Mendix |
|---|---|---|
| 0.3.0 | 2026-04-28 | 11.6.0 |
| 0.2.0 | 2026-04-20 | 11.6.0 |
| 0.1.0 | 2026-03-31 | 11.6.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 0.3.0 | breaking | Renamed GlobalInboxEventService event names, related entities, and microflows. | GlobalInboxEventService, event names, entities, microflows |  |
| 0.3.0 | migration-step | Update and deploy Global Inbox module to 0.3.0 before deploying Global Inbox Connector module. | Global Inbox, Global Inbox Connector |  |

## Global Inbox Connector <a id="259155"></a>
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

## Global Search <a id="115019"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/115019)

| version | published | min Mendix |
|---|---|---|
| 6.2.1 | 2025-03-11 | 9.24.28 |
| 6.2.0 | 2025-01-24 | 9.24.28 |
| 6.1.0 | 2024-10-02 | 9.24.28 |
| 6.0.1 | 2024-08-30 | 8.18.30 |
| 6.0.0 | 2024-08-29 | 8.18.30 |
| 5.0.0 | 2023-10-03 | 8.15.1 |
| 4.0.0 | 2022-09-28 | 8.12.7 |
| 3.0.0 | 2021-12-10 | 8.12.7 |
| 2.0.0 | 2021-02-16 | 8.6.4 |
| 1.0.0-beta2 | 2020-08-18 | 8.6.4 |
| 1.0.0-beta | 2020-08-17 | 8.6.4 |
| 1.0.0 | 2020-09-02 | 8.6.4 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 6.2.1 | breaking | Last remaining getParent() replaced by getPath(). | getParent(), getPath() | getPath() |
| 6.2.0 | requirement | Upgrade to latest 9.x version of Lucene, with 9.12.1 jar files included. | Lucene |  |
| 6.1.0 | requirement | Upgrade to latest Mx9 LTS version, making module compatible with Mx10. | Mendix |  |
| 6.0.1 | requirement | Upgrade to latest Mx8 LTS version. | Mendix |  |
| 6.0.1 | requirement | Major upgrade to Lucene 9.11.1 (latest version). | Lucene |  |
| 6.0.1 | feature | Extra Administrator module role for managing index data. | Administrator |  |
| 6.0.1 | breaking | getParent() method replaced by getPath(). | getParent(), getPath() | getPath() |
| 6.0.1 | migration-step | IndexWriter gets closed before zip-file creation (preferably in Bsd-flow). | IndexWriter |  |
| 6.0.1 | migration-step | Event handler for Indexing moved to AfterCommit. | Event handler |  |
| 6.0.1 | breaking | Implicit cast to String replaced by x.toString() for Advanced search. | Advanced search |  |
| 6.0.1 | known-issue | Sorting by weight/lucene score result not yet sorted out. | Sorting |  |
| 6.0.1 | known-issue | Deprecations from upgrading Lucene core not yet fixed. Will be done in future release. | Lucene |  |
| 6.0.0 | requirement | Upgrade to latest Mx8 LTS version. | Mendix |  |
| 6.0.0 | requirement | Major upgrade to Lucene 9.11.1 (latest version). | Lucene |  |
| 6.0.0 | feature | Extra Administrator module role for managing index data. | Administrator |  |
| 6.0.0 | breaking | getParent() method replaced by getPath(). | getParent(), getPath() | getPath() |
| 6.0.0 | migration-step | IndexWriter gets closed before zip-file creation (preferably in Bsd-flow). | IndexWriter |  |
| 6.0.0 | migration-step | Event handler for Indexing moved to AfterCommit. | Event handler |  |
| 6.0.0 | breaking | Implicit cast to String replaced by x.toString() for Advanced search. | Advanced search |  |
| 6.0.0 | known-issue | Sorting by weight/lucene score result not yet sorted out. | Sorting |  |
| 6.0.0 | known-issue | Deprecations from upgrading Lucene core not yet fixed. Will be done in future release. | Lucene |  |
| 5.0.0 | requirement | Upgrade to Mx 8.15.1. | Mendix |  |
| 5.0.0 | feature | Two new Java actions: IndexDataToFileDocument and FileDocumentToIndexData. | IndexDataToFileDocument, FileDocumentToIndexData |  |
| 5.0.0 | feature | Two new constants: IndexFileRestoreAfterStartup and IndexFileStoreBeforeShutdown. | IndexFileRestoreAfterStartup, IndexFileStoreBeforeShutdown |  |
| 5.0.0 | breaking | Changed behaviour of After startup flow and Before shutdown microflow to store index data in database. | After startup flow, Before shutdown microflow |  |
| 5.0.0 | migration-step | Index data management either on BSd and ASu or manually. | Index data |  |
| 5.0.0 | breaking | ACO on SearchableObject instead of BCO, allows use in task queues. Potential breaking change. | SearchableObject |  |
| 4.0.0 | breaking | Reworked module set-up. No more runtime configuration; everything reflected in Mendix model during development. |  |  |
| 4.0.0 | breaking | Entities searchable must inherit from SearchableObject. | SearchableObject |  |
| 4.0.0 | removal | Highlighting removed as it reduces search performance and introduces overhead. | Highlighting |  |
| 3.0.0 | feature | Compatibility with Mendix 9. | Mendix |  |
| 3.0.0 | requirement | Upgraded to Lucene 8.9. | Lucene |  |
| 2.0.0 | breaking | Wildcard search option replaced with advanced search query builder combining exact match, phrase search, wildcard search. | wildcard search | advanced search query builder |
| 2.0.0 | feature | After startup microflow to refresh indexes when restarting. | After startup microflow |  |

## Google Authenticator Connector <a id="2948"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/2948)

| version | published | min Mendix |
|---|---|---|
| 4.0.0 | 2026-07-17 | 11.6.7 |
| 3.0.0 | 2026-07-17 | 10.14.0 |
| 2.3.0 | 2023-11-06 | 9.24.2 |
| 2.2.0 | 2021-09-17 | 9.3.0 |
| 2.1.0 | 2021-03-10 | 7.23.19 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 4.0.0 | requirement | Requires Mendix 11.6.7 or higher. |  |  |
| 3.0.0 | requirement | Requires Mendix 10.14.0 or higher. |  |  |
| 2.3.0 | requirement | Requires Mendix 9.24.2 or higher. |  |  |
| 2.3.0 | improvement | Updated commons-codec to 1.16.0. | commons-codec |  |
| 2.2.0 | requirement | Requires Mendix 9.3.0 or higher. |  |  |
| 2.1.0 | requirement | Requires Mendix 7.23.19 or higher. |  |  |
| 2.1.0 | improvement | Upgraded libraries. |  |  |

## Google Gemini Connector <a id="254741"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/254741)

| version | published | min Mendix |
|---|---|---|
| 2.1.0 | 2026-08-07 | 11.12.2 |
| 2.0.0 | 2026-07-02 | 11.12.0 |
| 1.0.0 | 2026-01-30 | 10.24.13 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.1.0 | requirement | Upgrade to Mendix 11.12.2 |  |  |
| 2.0.0 | requirement | Module upgraded to Mendix 11.12 |  |  |
| 2.0.0 | breaking | Available models creation updated to create latest models only. Models can now be added manually in configuration UI. |  |  |

## Google Maps <a id="48911"></a>
Widget, Mendix, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/48911)

| version | published | min Mendix |
|---|---|---|
| 1.5.2 | 2018-12-20 | 7.13.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.5.2 | feature | Static locations no longer require adding a location; empty maps can now be shown | static locations |  |

## Google Place Autocomplete Connector <a id="120329"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/120329)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2022-05-30 | 9.12.1 |

## Google Tag <a id="207519"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/207519)

| version | published | min Mendix |
|---|---|---|
| 2.4.1 | 2026-02-16 | 10.21.0 |
| 2.4.0 | 2025-04-16 | 10.21.0 |
| 2.3.0 | 2024-10-18 | 9.18.4 |
| 2.2.0 | 2023-06-28 | 9.18.4 |
| 2.1.0 | 2023-06-05 | 9.18.4 |
| 2.0.0 | 2023-03-15 | 9.18.4 |
| 1.0.0 | 2023-02-22 | 8.18.17 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.4.0 | requirement | Updated studio pro minimum version to 10.21 to support Mendix 11. | Studio Pro |  |
| 2.3.0 | feature | Introduced new functionality allowing to optionally share authenticated user ID with Google Analytics. |  |  |
| 2.2.0 | improvement | Now possible to configure additional tags via 'config' command in Advanced mode. |  |  |

## Google Tag Manager - Custom Page View <a id="120751"></a>
Widget, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/120751)

| version | published | min Mendix |
|---|---|---|
| 1.1.0 | 2023-01-23 | 9.9.1 |
| 1.0.0 | 2022-07-06 | 9.9.1 |

## gRPC Connector <a id="232798"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/232798)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2024-10-24 | 10.6.11 |

## GSK PDF Viewer <a id="257805"></a>
Widget, GSK, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/257805)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2026-03-13 | 9.6.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.0.0 | requirement | Minimum Mendix Studio Pro version is 9.6.0 or higher. | Mendix Studio Pro |  |
| 1.0.0 | requirement | Entity must be generalized from System.FileDocument. |  |  |
| 1.0.0 | known-issue | Advanced DOCX formatting (custom fonts, tracked changes, floating objects) may not render exactly as authored. |  |  |
| 1.0.0 | known-issue | XLSX renders cell text only; charts, images, and formulas are not supported. |  |  |
| 1.0.0 | known-issue | Offline mode is not supported. |  |  |

## HarmonyOS NEXT Wrapper (Beta) <a id="243288"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/243288)

| version | published | min Mendix |
|---|---|---|
| 0.3.0 | 2025-09-29 | 10.24.0 |
| 0.1.1 | 2025-08-20 | 10.24.0 |
| 0.1.0 | 2025-07-21 | 10.18.0 |

## HaveIBeenPwned <a id="117164"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/117164)

| version | published | min Mendix |
|---|---|---|
| 1.3.0 | 2026-08-06 | 11.12.2 |
| 1.2.0 | 2023-10-26 | 10.3.1 |
| 1.1.0 | 2023-10-26 | 9.18.7 |
| 1.0.1 | 2021-04-29 | 8.12.6 |
| 1.0.0 | 2021-03-29 | 8.12.6 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.3.0 | requirement | Minimum Mendix version updated to 11.12.2 |  |  |
| 1.2.0 | requirement | Minimum Mendix version updated to 10.3.1 |  |  |
| 1.1.0 | requirement | Minimum Mendix version updated to 9.18.7 |  |  |
| 1.0.1 | breaking | Consistent naming of modules and microflows |  |  |

## Hellosign Module <a id="108973"></a>
Module, eXp Realty, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/108973)

| version | published | min Mendix |
|---|---|---|
| 2.0.0 | 2022-01-06 | 8.18.14 |
| 1.0.0 | 2019-07-16 | 7.20.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.0.0 | requirement | Upgraded to Studio Pro 8.18.14, minimum Mendix version is now 8.18.14. | Mendix |  |
| 2.0.0 | removal | Removed dependencies on Community Commons and Rest Services Modules. | Community Commons, Rest Services Modules |  |

## HR Interviews <a id="216869"></a>
Industry Template, TOCnDix, Partner, [marketplace](https://marketplace.mendix.com/link/component/216869)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2023-10-06 | 9.24.3 |

## HTML Element <a id="204843"></a>
Widget, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/204843)

| version | published | min Mendix |
|---|---|---|
| 1.2.12 | 2026-08-12 | 9.12.0 |
| 1.2.11 | 2026-07-28 | 9.12.0 |
| 1.2.10 | 2026-07-22 | 9.12.0 |
| 1.2.9 | 2026-06-24 | 9.12.0 |
| 1.2.8 | 2026-06-18 | 9.12.0 |
| 1.2.7 | 2026-04-20 | 9.12.0 |
| 1.2.6 | 2026-04-01 | 9.12.0 |
| 1.2.5 | 2026-02-10 | 9.12.0 |
| 1.2.4 | 2025-12-08 | 9.12.0 |
| 1.2.2 | 2025-03-14 | 9.12.0 |
| 1.2.1 | 2024-08-23 | 9.12.0 |
| 1.2.0 | 2024-02-01 | 9.12.0 |
| 1.1.1 | 2023-09-27 | 9.12.0 |
| 1.1.0 | 2023-06-05 | 9.12.0 |
| 1.0.1 | 2023-01-05 | 9.12.0 |
| 1.0.0 | 2022-11-24 | 9.12.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.2.12 | security | Updated dompurify library to version 3.4.13 to incorporate latest security fixes. | dompurify |  |
| 1.2.11 | security | Updated dompurify library to version 3.4.12 to incorporate latest security fixes. | dompurify |  |
| 1.2.10 | fix | Fixed issue where widget was not loading in the Dojo client due to broken JavaScript bundle. |  |  |
| 1.2.9 | security | Updated dompurify library to version 3.4.11 to incorporate latest security fixes. | dompurify |  |
| 1.2.8 | security | Updated dompurify library to version 3.4.10 to incorporate latest security fixes. | dompurify |  |
| 1.2.7 | security | Updated dompurify library to version 3.4.0 to incorporate latest improvements and security fixes. | dompurify |  |
| 1.2.6 | security | Updated dompurify library to version 3.3.3 to incorporate latest improvements and security fixes. | dompurify |  |
| 1.2.2 | security | Updated dompurify library to version 3.2.4 to incorporate latest improvements and security fixes. | dompurify |  |
| 1.2.1 | security | Updated dompurify library to version 2.5.6 to prevent template injection. | dompurify |  |
| 1.0.1 | fix | Fixed issue with HTML Element widget producing errors in Studio Pro versions below 9.18. |  |  |

## HTML/ JavaScript Snippet <a id="56"></a>
Widget, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/56)

| version | published | min Mendix |
|---|---|---|
| 4.0.0 | 2026-02-24 | 10.24.0 |
| 3.9.9 | 2024-09-16 | 7.23.0 |
| 3.9.8 | 2023-12-07 | 7.23.0 |
| 3.9.7 | 2021-08-04 | 7.23.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 4.0.0 | breaking | Content property will lose its configured value and must be reconfigured manually after update. | content property |  |
| 4.0.0 | breaking | HTML content field is no longer a translatable string. | HTML content field |  |
| 3.9.9 | security | Updated core-js dependency to version 3.38.0. | core-js |  |
| 3.9.7 | removal | Removed deprecated warnings. | deprecated warnings |  |

## HumbleBee Claims Management <a id="207496"></a>
Industry Template, Valcon, Partner, [marketplace](https://marketplace.mendix.com/link/component/207496)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2023-02-22 | 9.24.2 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.0.0 | requirement | Requires minimum Mendix version 9.24.2 | Mendix |  |

## HumbleBee for digital insurance <a id="118342"></a>
Solution, Valcon, Partner, [marketplace](https://marketplace.mendix.com/link/component/118342)

| version | published | min Mendix |
|---|---|---|
| 4.0.0 | 2022-08-09 | ? |
| 3.0.0 | 2022-08-09 | ? |
| 2.0.0 | 2022-08-09 | ? |
| 1.0.0 | 2021-09-02 | ? |

## HumbleBee Policy Management <a id="207476"></a>
Industry Template, Valcon, Partner, [marketplace](https://marketplace.mendix.com/link/component/207476)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2023-02-22 | 9.24.2 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.0.0 | requirement | Minimum Mendix version required is 9.24.2 | Mendix |  |

## Hybrid Mobile Actions <a id="112063"></a>
Module, Mendix, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/112063)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2019-11-27 | 8.4.0 |

## IFrame Component <a id="117308"></a>
Widget, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/117308)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2021-04-14 | 8.18.1 |

## Image <a id="118579"></a>
Widget, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/118579)

| version | published | min Mendix |
|---|---|---|
| 1.6.1 | 2026-08-18 | 9.24.0 |
| 1.6.0 | 2026-08-03 | 9.24.0 |
| 1.5.1 | 2025-11-03 | 9.24.0 |
| 1.5.0 | 2025-09-02 | 9.24.0 |
| 1.4.3 | 2023-10-05 | 9.24.0 |
| 1.4.2 | 2023-09-27 | 9.24.0 |
| 1.4.1 | 2023-07-11 | 9.24.0 |
| 1.4.0 | 2023-06-05 | 9.24.0 |
| 1.3.0 | 2023-03-29 | 9.24.0 |
| 1.2.1 | 2022-04-01 | 9.6.0 |
| 1.2.0 | 2021-12-23 | 9.6.0 |
| 1.1.0 | 2021-12-03 | 9.6.0 |
| 1.0.0 | 2021-09-28 | 9.6.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.6.0 | breaking | Changed default maximum height to 250 pixels for new Image widgets. Existing widgets unaffected. | maximum height |  |
| 1.2.1 | fix | Fixed widget compatibility with strict CSP mode. | CSP |  |
| 1.1.0 | breaking | Simplified widget properties. | widget properties |  |
| 1.0.0 | breaking | Converted into a pluggable widget. |  |  |

## Image Carousel Widget <a id="116966"></a>
Widget, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/116966)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2021-03-17 | 8.12.5 |

## Image Crop <a id="254"></a>
Module, Mendix, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/254)

| version | published | min Mendix |
|---|---|---|
| 5.0.2 | 2026-03-06 | 9.18.4 |
| 5.0.1 | 2024-07-09 | 9.18.4 |
| 5.0.0 | 2023-04-05 | 9.18.4 |
| 4.0.7 | 2023-03-22 | 8.18.15 |
| 4.0.6 | 2023-03-10 | 8.18.15 |
| 4.0.5 | 2022-10-25 | 8.18.15 |
| 4.0.4 | 2022-01-06 | 8.18.15 |
| 4.0.3 | 2021-06-21 | 8.18.7 |
| 4.0.2 | 2021-05-17 | 8.0.0 |
| 4.0.1 | 2021-01-14 | 8.0.0 |
| 4.0.0 | 2020-04-06 | 8.0.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 5.0.0 | requirement | Updated minimum Mendix version to 9.18.4. |  |  |
| 4.0.7 | fix | Fixed issue with widget not working with Mendix 9.24. |  |  |
| 4.0.3 | fix | Updated module to be compatible with Mendix 9. |  |  |
| 4.0.3 | removal | Removed Atlas dependencies. | Atlas |  |
| 4.0.1 | improvement | Upgraded dependent libraries. |  |  |
| 4.0.0 | migration-step | Migrated widget module to 8.0.0. |  |  |
| 4.0.0 | security | Merged small vulnerability fixes. |  |  |

## Image Cropper <a id="302076"></a>
Widget, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/302076)

| version | published | min Mendix |
|---|---|---|
| 1.1.0 | 2026-08-18 | 11.12.0 |
| 1.0.0 | 2026-07-16 | 11.12.0 |

## Image Hosting <a id="120706"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/120706)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2022-06-28 | 9.1.1 |

## Image Markup <a id="118912"></a>
Widget, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/118912)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2021-12-08 | 9.7.0 |

## IMAP/POP3 incoming email <a id="1042"></a>
Service, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/1042)

| version | published | min Mendix |
|---|---|---|
| 7.0.0 | 2022-12-20 | 9.1.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 7.0.0 | breaking | Updated the module role name and settings. | module role |  |
| 7.0.0 | breaking | Renamed and rearranged Microflows, Constants, Java actions etc. per Mendix naming conventions. | Microflows, Constants, Java actions |  |
| 7.0.0 | improvement | Upgraded jsoup library to 1.15.3 | jsoup |  |
| 7.0.0 | improvement | Upgraded slf4j-api library to 2.0.5 | slf4j-api |  |

## IMask - Masked Input <a id="114482"></a>
Widget, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/114482)

| version | published | min Mendix |
|---|---|---|
| 2.1.0 | 2020-11-16 | 8.6.3 |
| 1.0.0 | 2020-06-10 | 8.6.3 |

## Industrial Edge - Device API Connector <a id="229678"></a>
Module, Siemens, Siemens, [marketplace](https://marketplace.mendix.com/link/component/229678)

| version | published | min Mendix |
|---|---|---|
| 1.0.2 | 2026-08-14 | 10.24.22 |
| 1.0.1 | 2024-08-16 | 10.6.11 |
| 1.0.0 | 2024-08-08 | 10.6.11 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.0.2 | requirement | API updated to IE Device API 2.4.2 | IE Device API |  |

## Industrial Edge - IIH Essentials Connector <a id="229534"></a>
Module, Siemens, Siemens, [marketplace](https://marketplace.mendix.com/link/component/229534)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2024-08-01 | 10.6.11 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.0.0 | requirement | Minimum Mendix version required is 10.6.11. | Mendix |  |

## Industrial Edge Plugin (Mendix 10) <a id="222639"></a>
Module, Siemens, Siemens, [marketplace](https://marketplace.mendix.com/link/component/222639)

| version | published | min Mendix |
|---|---|---|
| 1.11.2 | 2026-09-21 | 10.12.15 |
| 1.10.4 | 2026-07-20 | 10.12.15 |
| 1.10.3 | 2026-07-07 | 10.12.15 |
| 1.6.7 | 2025-11-24 | 10.12.15 |
| 1.6.6 | 2025-07-01 | 10.12.15 |
| 1.4.0 | 2024-11-06 | 10.12.8 |
| 1.3.0 | 2024-07-11 | 10.6.11 |
| 1.0.0 | 2024-02-19 | 10.6.3 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.11.2 | security | Vulnerabilities and small bug fixes |  |  |
| 1.10.4 | fix | User unable to publish application to Industrial Edge Management in Docker Engine environment |  |  |
| 1.10.3 | improvement | Implemented major changes to ensure full compatibility with IEM v2 | Industrial Edge Management V2 |  |
| 1.10.3 | fix | Addressed and resolved various reported bugs to enhance reliability |  |  |
| 1.10.3 | fix | Applied specific fixes to improve VTS module functionality and stability | VTS module |  |
| 1.10.3 | improvement | Introduced optimizations to boost system performance and responsiveness |  |  |
| 1.6.7 | fix | Fixed Mendix app image build issue - requests module not found error during build process |  |  |
| 1.6.6 | deprecation | This version officially deprecated as of November 2025. Upgrade to latest version recommended. |  |  |
| 1.6.6 | improvement | Added default restart: unless-stopped policy in Docker Compose templates to prevent service disruptions | Docker Compose templates |  |
| 1.6.6 | feature | Added automatic tenant URL detection and parsing feature for IEHUB authentication | IEHUB authentication |  |
| 1.6.6 | improvement | Updated pre-defined template resulting in more efficient application creation journey |  |  |
| 1.6.6 | improvement | License cleanup on switching between multiple tenants of IEHUB |  |  |
| 1.6.6 | fix | Bugs and UI improvements |  |  |
| 1.4.0 | deprecation | This version officially deprecated as of November 2025. Upgrade to latest version recommended. |  |  |
| 1.4.0 | requirement | Upgraded Mendix build pack >= 5.0.5 | Mendix build pack |  |
| 1.4.0 | feature | Added support for Mendix Studio 10.12 |  |  |
| 1.4.0 | feature | Implemented feature to download logs |  |  |
| 1.4.0 | fix | Bug fixes |  |  |
| 1.3.0 | deprecation | This version officially deprecated as of November 2025. Upgrade to latest version recommended. |  |  |
| 1.3.0 | fix | Validation regarding nginx https reverse proxy issue fixed | nginx https reverse proxy |  |
| 1.3.0 | improvement | Enhanced general error messages |  |  |
| 1.0.0 | deprecation | This version officially deprecated as of November 2025. Upgrade to latest version recommended. |  |  |
| 1.0.0 | feature | Docker Application Deployment - Simplify IE application creation |  |  |
| 1.0.0 | feature | Docker Image Creation - Streamline containerization process for Industrial Edge |  |  |
| 1.0.0 | feature | Template YAML Support - Accelerate deployment using pre-defined docker-compose templates |  |  |
| 1.0.0 | feature | Application Catalog Integration - Simplify distribution and access through Industrial Edge Catalog | Industrial Edge Catalog |  |
| 1.0.0 | feature | App Configuration Support - Add application-specific configurations |  |  |

## Industrial Edge Plugin (Mendix 9) <a id="218436"></a>
Module, Siemens, Siemens, [marketplace](https://marketplace.mendix.com/link/component/218436)

| version | published | min Mendix |
|---|---|---|
| 1.1.0 | 2023-12-19 | 9.24.3 |
| 1.0.0 | 2023-11-06 | 9.24.3 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.1.0 | deprecation | This version of the plugin is officially deprecated as of November 2025. Users are strongly recommended to upgrade to the latest available version. |  |  |
| 1.1.0 | known-issue | Due to known issues, this version may not function as intended. Users should upgrade to ensure proper functionality. |  |  |
| 1.0.0 | deprecation | This version of the plugin is officially deprecated as of November 2025. Users are strongly recommended to upgrade to the latest available version. |  |  |
| 1.0.0 | known-issue | Due to known issues, this version may not function as intended. Users should upgrade to ensure proper functionality. |  |  |

## IP Range Validation <a id="1752"></a>
Module, Mendix, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/1752)

| version | published | min Mendix |
|---|---|---|
| 1.5.0 | 2021-07-20 | 9.0.5 |
| 1.4.1 | 2021-07-20 | 8.16.0 |
| 1.4.0 | 2020-04-24 | 8.1.1 |
| 1.3.0 | 2019-11-15 | 8.1.1 |
| 1.2.0 | 2019-11-15 | 7.23.3 |
| 1.1.0 | 2019-11-15 | 7.5.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.5.0 | requirement | Minimum Mendix version raised to 9.0.5 | Mendix |  |
| 1.4.1 | fix | Fixed IPv6 compatibility issue | IPv6 |  |
| 1.4.1 | requirement | Minimum Mendix version raised to 8.16.0 | Mendix |  |
| 1.4.0 | fix | Fixed bugs for checking matching rules | matching rules |  |
| 1.4.0 | breaking | Model changed to only allow single matched rule instead of multiple | model |  |
| 1.3.0 | requirement | Upgraded to Mendix 8.1.1 | Mendix |  |
| 1.3.0 | improvement | Compatible with latest Atlas UI layouts | Atlas UI |  |
| 1.2.0 | requirement | Upgraded to Mendix 7.23.3 | Mendix |  |
| 1.2.0 | improvement | Updated Atlas UI package to support latest project layouts | Atlas UI |  |
| 1.1.0 | requirement | Upgraded to Mendix 7.5.0 | Mendix |  |

## Java List Interface Java Actions <a id="218623"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/218623)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2023-11-07 | 10.4.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.0.0 | requirement | Mendix version 10.4 or above required. |  |  |

## JFree Charts (.png images) <a id="3011"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/3011)

| version | published | min Mendix |
|---|---|---|
| 2.0.1 | 2022-10-03 | 9.6.0 |
| 1.3.1 | 2022-04-05 | 7.0.2 |
| 1.3.0 | 2020-01-30 | ? |
| 1.2.0 | 2020-01-29 | ? |
| 1.1.0 | 2020-01-29 | ? |
| 1.0 | 2016-07-25 | ? |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.0.1 | requirement | Updated to require Mendix 9.6.0 minimum. | Mendix |  |

## JSON Path <a id="107685"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/107685)

| version | published | min Mendix |
|---|---|---|
| 2.3.0 | 2025-10-28 | 10.24.9 |
| 2.2.0 | 2025-03-28 | 9.24.30 |
| 2.1.0 | 2024-07-03 | 9.24.24 |
| 2.0.3 | 2024-07-03 | 8.18.30 |
| 2.0.2 | 2023-03-27 | 8.18.6 |
| 2.0.1 | 2021-09-27 | 8.18.6 |
| 2.0.0 | 2021-09-27 | 8.18.6 |
| 1.1.0 | 2020-02-15 | 7.23.7 |
| 1.0.1 | 2019-08-08 | 7.23.7 |
| 1.0.0 | 2018-10-15 | 7.13.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.3.0 | requirement | Minimum Mendix version upgraded to 10.24.9 | Mendix |  |
| 2.3.0 | requirement | Java version upgraded to 21 | Java |  |
| 2.3.0 | migration-step | Migrated to Mendix Managed Dependencies. See documentation for additional cleanup steps when upgrading from versions <2.3.0 |  |  |
| 2.2.0 | security | Upgraded JSON Smart library to 2.5.1 to fix CVE-2024-57699 | JSON Smart |  |
| 2.2.0 | requirement | Upgraded to Mendix 9.24.30 | Mendix |  |
| 2.1.0 | requirement | Upgraded Mendix version to 9.24.24 LTS | Mendix |  |
| 2.0.3 | security | Upgraded JSON Path library to 2.9.0 to fix security vulnerability | JSON Path library |  |
| 2.0.3 | improvement | Upgraded JSON Smart library to 2.5.1 | JSON Smart library |  |
| 2.0.2 | security | Patched JSON Smart to 2.4.10 to fix vulnerability | JSON Smart |  |
| 2.0.0 | requirement | Upgraded to Mendix 8.18.6 | Mendix |  |
| 2.0.0 | improvement | Updated Java dependencies and cleaned up unnecessary dependencies | Java dependencies |  |
| 1.0.1 | requirement | Upgraded to 7.23.7 | Mendix |  |

## JSON Structure <a id="113010"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/113010)

| version | published | min Mendix |
|---|---|---|
| 1.1.0 | 2021-05-21 | 8.12.7 |
| 1.0.1 | 2020-03-17 | 8.5.0 |
| 1.0.0 | 2020-02-26 | 8.5.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.1.0 | requirement | Module now compatible with Mendix 9 |  |  |

## JWT <a id="106447"></a>
Module, Ciphix, Community, [marketplace](https://marketplace.mendix.com/link/component/106447)

| version | published | min Mendix |
|---|---|---|
| 3.4.0 | 2026-06-09 | 11.6.6 |
| 3.3.3 | 2025-12-19 | 10.24.0 |
| 3.3.2 | 2024-03-13 | 9.18.4 |
| 3.3.1 | 2024-02-20 | 9.18.4 |
| 3.3.0 | 2023-07-26 | 8.12.5 |
| 3.2.2 | 2023-01-13 | 8.12.5 |
| 3.2.1 | 2021-06-04 | 8.12.5 |
| 3.2.0 | 2019-11-20 | 8.1.1 |
| 3.1.0 | 2019-10-30 | 8.1.1 |
| 3.0.0 | 2019-09-11 | 8.1.1 |
| 2.0.0 | 2019-05-29 | 7.13.1 |
| 1.6.0 | 2019-04-11 | 7.13.1 |
| 1.5.0 | 2018-11-02 | 7.13.1 |
| 1.4.1 | 2018-10-31 | 7.13.1 |
| 1.4.0 | 2018-10-26 | 7.13.1 |
| 1.3.0 | 2018-10-24 | 7.13.1 |
| 1.2.2 | 2018-06-12 | 7.13.1 |
| 1.2.1 | 2018-06-08 | 7.13.1 |
| 1.2.0 | 2018-06-08 | 7.13.1 |
| 1.1.0 | 2018-05-04 | 7.13.1 |
| 1.0.0 | 2018-04-05 | 7.13.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 3.4.0 | requirement | Minimum Mendix version raised to 11.6.6 | Mendix |  |
| 3.3.3 | requirement | Minimum Mendix version raised to 10.24.0 | Mendix |  |
| 3.3.2 | fix | Fixed hardcoded 3-year validity in generated public certificate; now respects specified years validity variable | public certificate validity |  |
| 3.3.1 | requirement | Updated to Mendix 9.18.4 minimum for Mendix 10 compatibility | Mendix |  |
| 3.3.1 | security | Resolved vulnerabilities |  |  |
| 3.3.0 | security | Upgraded Guava due to vulnerability | Guava |  |
| 3.2.2 | security | Updated JARs to fix security threat |  |  |
| 3.2.1 | requirement | Updated to Mendix 8.12.5 minimum for Mendix 9 compatibility | Mendix |  |
| 3.2.0 | improvement | Updated all dependencies to latest versions |  |  |
| 3.0.0 | requirement | Mendix 8 compatibility | Mendix |  |
| 2.0.0 | breaking | Fixed incomplete public key specification; now incompatible with public keys generated in previous versions | public keys |  |
| 2.0.0 | fix | Fixed import of X.509 public key certificates in key generation and key imports using signed certificates | X.509 public key certificates |  |
| 1.6.0 | improvement | Updated dependencies |  |  |
| 1.6.0 | known-issue | Jackson Core dependency uses system property; incompatible with Mendix free sandbox; disable Emulate Cloud security feature | Jackson Core |  |
| 1.4.1 | fix | Solved stream handling issues when reading RSA key pairs from S3 object store | S3 object store |  |
| 1.4.0 | breaking | Changed private key specification from PKCS8 to PKCS1 for JWT RS algorithms compatibility; added bouncycastle dependencies | private key specification |  |
| 1.2.2 | migration-step | Renamed public and private key entities for compatibility with Mendix Encryption module | public key entities, private key entities |  |

## Kanban <a id="225360"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/225360)

| version | published | min Mendix |
|---|---|---|
| 1.0.6 | 2026-07-29 | 11.12.1 |
| 1.0.3 | 2026-07-14 | 9.24.4 |
| 1.0.1 | 2024-04-30 | 9.24.4 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.0.6 | requirement | Upgraded for Mendix 11. Widget is now compatible with Studio Pro 11. | Mendix |  |
| 1.0.3 | fix | Resolved ClickLock-style drag issue on desktop browsers (Chrome, Edge, Safari) where dragged item would stick to cursor. | drag-and-drop |  |
| 1.0.3 | improvement | Desktop mouse drag-and-drop now handled by native HTML5 backend; touch devices use touch backend; keyboard/accessibility dragging unchanged. | drag-and-drop |  |
| 1.0.3 | improvement | Drag image is now the browser's native drag preview, consistent with existing Firefox behavior. | drag-and-drop |  |

## KvK Connector <a id="120182"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/120182)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2022-05-10 | 9.12.1 |

## Label Selector <a id="292"></a>
Widget, Mendix, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/292)

| version | published | min Mendix |
|---|---|---|
| 4.6.2 | 2024-08-23 | 7.23.0 |
| 4.6.1 | 2023-10-06 | 7.23.0 |
| 4.6.0 | 2023-05-04 | 7.23.0 |
| 4.5.9 | 2023-02-23 | 7.23.0 |
| 4.5.8 | 2022-09-07 | 7.23.0 |
| 4.5.7 | 2022-07-25 | 7.23.0 |
| 4.5.6 | 2021-09-22 | 7.23.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 4.5.9 | improvement | Updated mx.logger calls to console. | mx.logger |  |
| 4.5.8 | improvement | Updated jQuery UI to 1.13.2. | jQuery UI |  |
| 4.5.7 | improvement | Made CSP compatible. |  |  |
| 4.5.6 | improvement | Updated jQuery to 3.5.1. | jQuery |  |
| 4.5.6 | improvement | Updated jQuery UI to 1.12.1. | jQuery UI |  |

## Language Selector <a id="202738"></a>
Widget, Mendix, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/202738)

| version | published | min Mendix |
|---|---|---|
| 1.1.4 | 2026-02-13 | 9.12.6 |
| 1.1.3 | 2024-11-29 | 9.12.6 |
| 1.1.2 | 2024-09-20 | 9.12.6 |
| 1.1.1 | 2023-09-27 | 9.12.6 |
| 1.1.0 | 2023-06-05 | 9.12.6 |
| 1.0.1 | 2022-10-28 | 9.12.6 |
| 1.0.0 | 2022-09-26 | 9.12.6 |

## Language Switcher (en/zh) <a id="119701"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/119701)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2022-02-15 | 9.9.1 |

## LDAP <a id="210270"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/210270)

| version | published | min Mendix |
|---|---|---|
| 2.2.2 | 2026-09-24 | 10.21.1 |
| 2.2.1 | 2026-08-13 | 10.21.1 |
| 2.2.0 | 2026-04-30 | 10.21.1 |
| 2.1.2 | 2026-02-25 | 10.21.1 |
| 2.1.1 | 2025-05-28 | 10.21.1 |
| 2.1.0 | 2025-05-05 | 10.21.1 |
| 2.0.1 | 2025-05-05 | 10.12.10 |
| 2.0.0 | 2025-01-20 | 10.12.10 |
| 1.2.2 | 2026-09-24 | 9.24.35 |
| 1.2.1 | 2026-08-13 | 9.24.35 |
| 1.2.0 | 2026-04-30 | 9.24.35 |
| 1.1.3 | 2025-05-05 | 9.24.8 |
| 1.1.2 | 2025-01-08 | 9.24.8 |
| 1.1.1 | 2024-01-18 | 9.24.8 |
| 1.1.0 | 2023-09-25 | 9.24.8 |
| 1.0.0 | 2023-04-28 | 9.22.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.2.2 | requirement | Added io.micrometer:micrometer-core to 1.17.1 | io.micrometer:micrometer-core |  |
| 2.2.2 | requirement | Upgraded org.springframework:spring-core to 7.0.9 | org.springframework:spring-core |  |
| 2.2.2 | requirement | Upgraded org.springframework:spring-tx to 7.0.9 | org.springframework:spring-tx |  |
| 2.2.2 | requirement | Upgraded org.springframework:spring-beans to 7.0.9 | org.springframework:spring-beans |  |
| 2.2.2 | requirement | Upgraded org.springframework.ldap:spring-ldap-core to 4.1.1 | org.springframework.ldap:spring-ldap-core |  |
| 2.2.1 | improvement | Improved LDAP synchronization performance and prevented duplication when group or user names change |  |  |
| 2.2.1 | requirement | Upgraded org.springframework:spring-core to 7.0.8 | org.springframework:spring-core |  |
| 2.2.1 | requirement | Upgraded org.springframework:spring-tx to 7.0.8 | org.springframework:spring-tx |  |
| 2.2.1 | requirement | Upgraded org.springframework:spring-beans to 7.0.8 | org.springframework:spring-beans |  |
| 2.2.1 | requirement | Upgraded org.springframework.ldap:spring-ldap-core to 4.0.4 | org.springframework.ldap:spring-ldap-core |  |
| 2.2.1 | migration-step | Remove unique constraint on ObjectGUID attribute of LDAP Group entity, run Ldap.MF_DeleteDuplicateGroups, add constraint back, refresh groups | LDAP Group |  |
| 2.2.1 | known-issue | Duplicate LDAP Group records may exist during upgrade. Role mappings may break if groups deleted or renamed | LDAP Group, LDAP role mappings |  |
| 2.2.0 | improvement | Improved LDAP synchronization to prevent duplication when group or user names change |  |  |
| 2.2.0 | requirement | Upgraded org.springframework:spring-core to 6.2.18 | org.springframework:spring-core |  |
| 2.2.0 | requirement | Upgraded org.springframework:spring-tx to 6.2.18 | org.springframework:spring-tx |  |
| 2.2.0 | requirement | Upgraded org.springframework:spring-beans to 6.2.18 | org.springframework:spring-beans |  |
| 2.2.0 | breaking | Module now uses objectGUID as primary identifier for users and groups instead of name | objectGUID |  |
| 2.2.0 | known-issue | Upgrade from earlier versions may create duplicates if legacy data inconsistent. Role mappings break if LDAP group deleted or renamed | LDAP Group, LDAP role mappings |  |
| 2.2.0 | known-issue | Version 2.2.0 may create duplicate LDAP group records during upgrade. Use version 2.2.1 or later. Version will be removed from marketplace soon |  |  |
| 2.1.2 | requirement | Upgraded org.springframework:spring-core to 6.2.16 | org.springframework:spring-core |  |
| 2.1.2 | requirement | Upgraded org.springframework:spring-tx to 6.2.16 | org.springframework:spring-tx |  |
| 2.1.2 | requirement | Upgraded org.springframework:spring-beans to 6.2.16 | org.springframework:spring-beans |  |
| 2.1.1 | improvement | Ensures compatibility with Mendix 11 |  |  |
| 2.1.0 | requirement | Version 2.1.0 for apps on Mendix 10.21.1 or higher |  |  |
| 2.1.0 | requirement | Upgraded org.springframework:spring-core to 6.2.2 | org.springframework:spring-core |  |
| 2.1.0 | requirement | Upgraded org.springframework:spring-tx to 6.2.2 | org.springframework:spring-tx |  |
| 2.1.0 | requirement | Upgraded org.springframework:spring-beans to 6.2.2 | org.springframework:spring-beans |  |
| 2.0.0 | requirement | Version 2.0.0 for apps on Mendix 10.12.10 or higher |  |  |
| 2.0.0 | requirement | Upgraded org.springframework.ldap:spring-ldap-core to 2.4.4 | org.springframework.ldap:spring-ldap-core |  |
| 2.0.0 | migration-step | Delete all Java libraries used by old LDAP module from userlib folder before upgrading to avoid conflicts |  |  |
| 1.2.2 | requirement | Upgraded org.springframework:spring-core to 7.0.9 | org.springframework:spring-core |  |
| 1.2.2 | requirement | Upgraded org.springframework:spring-tx to 7.0.9 | org.springframework:spring-tx |  |
| 1.2.2 | requirement | Upgraded org.springframework:spring-beans to 7.0.9 | org.springframework:spring-beans |  |
| 1.2.1 | requirement | Upgraded org.springframework:spring-core to 7.0.8 | org.springframework:spring-core |  |
| 1.2.1 | requirement | Upgraded org.springframework:spring-tx to 7.0.8 | org.springframework:spring-tx |  |
| 1.2.1 | requirement | Upgraded org.springframework:spring-beans to 7.0.8 | org.springframework:spring-beans |  |
| 1.2.1 | requirement | Upgraded org.springframework.ldap:spring-ldap-core to 4.0.4 | org.springframework.ldap:spring-ldap-core |  |
| 1.2.0 | requirement | Upgraded to Studio Pro v9.24.35 |  |  |
| 1.2.0 | requirement | Upgraded org.springframework:spring-core to 6.2.17 | org.springframework:spring-core |  |
| 1.2.0 | requirement | Upgraded org.springframework:spring-tx to 6.2.17 | org.springframework:spring-tx |  |
| 1.2.0 | requirement | Upgraded org.springframework:spring-beans to 6.2.17 | org.springframework:spring-beans |  |
| 1.2.0 | requirement | Recommended to set runtime to Java 21 for compatibility |  |  |
| 1.1.2 | security | Fixed LDAP injection vulnerability. CVSS v3.1: 7.4 (Ticket #235264) |  |  |
| 1.1.2 | requirement | Upgraded org.springframework.ldap:spring-ldap-core to 2.4.4 | org.springframework.ldap:spring-ldap-core |  |
| 1.1.2 | migration-step | Delete all Java libraries used by old LDAP module from userlib folder before upgrading to avoid conflicts |  |  |
| 1.1.1 | requirement | Upgraded org.springframework:spring-core to 5.3.31 (Ticket #202474) | org.springframework:spring-core |  |
| 1.1.1 | requirement | Upgraded org.springframework:spring-tx to 5.3.31 | org.springframework:spring-tx |  |
| 1.1.1 | requirement | Upgraded org.springframework:spring-beans to 5.3.31 | org.springframework:spring-beans |  |
| 1.1.1 | migration-step | Delete all Java libraries used by old LDAP module from userlib folder before upgrading to avoid conflicts |  |  |
| 1.1.0 | requirement | Upgraded to Studio Pro v9.24.8 |  |  |
| 1.1.0 | fix | Fixed Mendix 10 compatibility issue |  |  |
| 1.1.0 | migration-step | Included migration file for Java dependencies for Studio Pro 10 compatibility |  |  |
| 1.0.0 | requirement | Added org.slf4j:slf4j-api to 2.0.5 | org.slf4j:slf4j-api |  |
| 1.0.0 | requirement | Added org.springframework:spring-core to 5.3.24 | org.springframework:spring-core |  |
| 1.0.0 | requirement | Added org.springframework.ldap:spring-ldap-core to 2.4.1 | org.springframework.ldap:spring-ldap-core |  |
| 1.0.0 | requirement | Added org.springframework:spring-tx to 5.3.23 | org.springframework:spring-tx |  |
| 1.0.0 | requirement | Added org.springframework:spring-beans to 5.3.24 | org.springframework:spring-beans |  |
| 1.0.0 | migration-step | Delete all Java libraries used by old LDAP module from userlib folder before upgrading to avoid conflicts |  |  |

## LDAP Synchronization module <a id="24"></a>
Module, Mendix, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/24)

| version | published | min Mendix |
|---|---|---|
| 8.0.0 | 2020-01-21 | 7.23.4 |
| 7.2.1 | 2018-11-29 | 7.16.0 |
| 7.1.0 | 2017-09-25 | 7.1.1 |
| 7.0 | 2017-06-12 | 7.1.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 8.0.0 | requirement | Upgraded LDAP module to be Mendix 8 compatible. Minimum Mendix version is now 7.23.4. |  |  |
| 8.0.0 | migration-step | Updated all Java libraries to latest versions. Delete old libraries from userlib folder if compilation or runtime errors occur. | spring-beans-4.3.9.RELEASE.jar, spring-core-4.3.9.RELEASE.jar, spring-ldap-core-2.3.1.RELEASE.jar, spring-tx-4.3.9.RELEASE.jar, org.slf4j.slf4j-api-1.7.25.jar, commons-lang-2.5.jar |  |
| 7.2.1 | requirement | Upgraded to Mendix 7.16.0 or later. Minimum Mendix version is now 7.16.0. |  |  |
| 7.2.1 | migration-step | Cleanup included Java libraries from userlib folder after importing this update. |  |  |
| 7.0 | requirement | Upgraded to Mendix 7 for compatibility. Minimum Mendix version is now 7.1.1. |  |  |
| 7.0 | migration-step | Remove old Java libraries from userlib folder after importing this update as they are no longer needed. | spring-beans-4.0.4.RELEASE.jar, spring-core-4.0.4.RELEASE.jar, spring-ldap-core-2.0.1.RELEASE.jar, spring-tx-4.0.4.RELEASE.jar |  |

## List view controls <a id="105694"></a>
Widget, Mendix, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/105694)

| version | published | min Mendix |
|---|---|---|
| 1.3.16 | 2021-09-20 | 7.23.21 |
| 1.3.15 | 2021-06-28 | 7.23.21 |
| 1.3.14 | 2021-06-22 | 7.23.21 |
| 1.3.13 | 2021-06-02 | 7.23.21 |
| 1.3.10 | 2021-01-08 | 7.20.0 |
| 1.3.9 | 2020-12-16 | 7.20.0 |
| 1.3.8 | 2020-07-09 | 7.20.0 |
| 1.3.7 | 2020-05-20 | 7.20.0 |
| 1.3.6 | 2020-04-24 | 7.20.0 |
| 1.3.5 | 2020-02-19 | 7.20.0 |
| 1.3.4 | 2019-11-13 | 7.20.0 |
| 1.3.3 | 2019-05-21 | 7.20.0 |
| 1.3.2 | 2019-05-08 | 7.20.0 |
| 1.3.1 | 2019-04-02 | 7.20.0 |
| 1.3.0 | 2018-12-14 | 7.20.0 |
| 1.2.3 | 2018-09-26 | 7.13.1 |
| 1.2.2 | 2018-08-28 | 7.13.1 |
| 1.2.1 | 2018-07-13 | 7.13.1 |
| 1.2.0 | 2018-05-23 | 7.13.1 |
| 1.1.2 | 2018-03-22 | 7.9.0 |
| 1.1.1 | 2018-03-13 | 7.9.0 |
| 1.1.0 | 2018-02-16 | 7.9.0 |
| 1.0.2 | 2018-01-25 | 7.9.0 |
| 1.0.1 | 2018-01-19 | 7.9.0 |
| 1.0.0 | 2017-11-24 | 7.8.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.3.15 | fix | Fixed regression in v1.3.10 where Header Sort and Drop down Sort did not keep list view sorted when pressing back button. | Header Sort, Drop down Sort |  |
| 1.3.13 | fix | Fixed issue in v1.3.12 where widget would error on list view control interaction if search not enabled. | search |  |
| 1.3.10 | fix | Fixed issue where pagination widget would change corresponding listview's ordering in particular scenario. | pagination widget |  |
| 1.3.8 | fix | Fixed unexpected regression in v1.3.7 where you could not combine filters. | filters |  |
| 1.3.6 | fix | Fixed issue when combining multiple filters and sortings where only last applied was considered. | filters, sortings |  |
| 1.3.5 | removal | Removed use of deprecated mendix.lang.delay. | mendix.lang.delay |  |
| 1.3.4 | fix | Sorting now works in combination with standard Load more functionality. | sorting, Load more |  |
| 1.3.3 | fix | Fixed issue where initial sorting of list view header was not being respected. | list view header sorting |  |
| 1.3.1 | fix | Persists original sort of list view when no sorting control used to sort. | sorting |  |
| 1.3.1 | fix | Offset preserved for non-paged list views; Load more items show when navigating back to list view. | Load more, pagination |  |
| 1.3.1 | fix | Can now find list view when navigating back to page with same layout. | list view detection |  |
| 1.3.0 | feature | Persist filters, search and sort state when navigating to detail page; restored on back/close. | filters, search, sort |  |
| 1.2.3 | fix | Filter and text box search now cleared correctly when conditional visibility changes. | filter, text box search, conditional visibility |  |
| 1.2.1 | fix | When lists are sorted, sorting is maintained when filter is applied. | sorting, filter |  |
| 1.2.1 | fix | List view controls can now be used in container that is initially invisible. | list view controls, conditional visibility |  |
| 1.1.2 | fix | Paging buttons now show when initially hidden and new items added to list. | paging buttons |  |
| 1.1.2 | fix | Sorting drop down persists selection when moving to next page. | Sorting drop down |  |
| 1.1.0 | feature | Added support for mobile offline; widgets can be used in offline apps, though XPath cannot be used. | list view controls |  |
| 1.1.0 | fix | Added support for multiple reference [%CurrentObject%] in XPath constraint. | XPath constraint |  |

## List view swipe <a id="47781"></a>
Widget, Mendix, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/47781)

| version | published | min Mendix |
|---|---|---|
| 1.2.0 | 2019-08-30 | 7.13.1 |
| 1.1.1 | 2018-10-26 | 7.13.1 |
| 1.1.0 | 2018-09-26 | 7.13.1 |
| 1.0.2 | 2018-04-17 | ? |
| 1.0.1 | 2017-04-17 | ? |
| 1.0 | 2017-04-06 | ? |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.2.0 | breaking | Mendix 8 support requires adding class widget-listview-swipe-foreground to foreground container. | background containers, widget-listview-swipe-foreground |  |
| 1.2.0 | requirement | Minimum Mendix version increased to 7.13.1. | Mendix |  |

## ListenListviewSetter <a id="107207"></a>
Widget, Mendix, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/107207)

| version | published | min Mendix |
|---|---|---|
| 1.0.1 | 2019-05-28 | 7.9.0 |
| 1.0.0 | 2018-07-18 | 7.9.0 |

## Loan Underwriting Process <a id="208720"></a>
Industry Template, TOCnDix, Partner, [marketplace](https://marketplace.mendix.com/link/component/208720)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2023-03-22 | ? |

## Locale Switcher <a id="2558"></a>
Module, Mendix, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/2558)

| version | published | min Mendix |
|---|---|---|
| 2.2.0 | 2020-01-28 | 8.1.1 |
| 2.1.0 | 2018-02-14 | 7.11.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.2.0 | requirement | Upgraded the model for Mendix 8.1.1 compatibility. Requires Mendix 8.1.1 or higher. |  |  |
| 2.1.0 | requirement | Upgraded and tested in Mendix 7.11.0. |  |  |

## Maps <a id="108261"></a>
Widget, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/108261)

| version | published | min Mendix |
|---|---|---|
| 5.0.0 | 2026-09-15 | 10.24.0 |
| 4.1.0 | 2025-11-05 | 9.6.0 |
| 4.0.0 | 2024-05-02 | 9.6.0 |
| 3.2.2 | 2023-09-27 | 9.6.0 |
| 3.2.1 | 2023-08-11 | 9.6.0 |
| 3.2.0 | 2023-06-05 | 9.6.0 |
| 3.1.3 | 2023-01-04 | 9.6.0 |
| 3.1.2 | 2022-04-25 | 9.6.0 |
| 3.1.1 | 2022-01-31 | 9.6.0 |
| 3.1.0 | 2021-12-23 | 9.6.0 |
| 3.0.3 | 2021-11-18 | 9.6.0 |
| 3.0.2 | 2021-10-28 | 9.6.0 |
| 3.0.1 | 2021-10-13 | 9.6.0 |
| 3.0.0 | 2021-09-28 | 9.6.0 |
| 2.0.3 | 2021-08-05 | 9.0.5 |
| 2.0.2 | 2021-07-13 | 9.0.5 |
| 2.0.1 | 2021-04-26 | 9.0.5 |
| 2.0.0 | 2021-04-08 | 9.0.5 |
| 1.0.11 | 2022-05-05 | 7.23.0 |
| 1.0.10 | 2021-05-10 | 7.23.0 |
| 1.0.9 | 2020-01-23 | 7.13.1 |
| 1.0.8 | 2019-11-28 | 7.13.1 |
| 1.0.7 | 2019-11-28 | 7.13.1 |
| 1.0.6 | 2019-10-30 | 7.13.1 |
| 1.0.5 | 2019-08-13 | 7.13.1 |
| 1.0.4 | 2019-04-30 | 7.13.1 |
| 1.0.3 | 2019-04-11 | 7.13.1 |
| 1.0.2 | 2019-03-12 | 7.13.1 |
| 1.0.1 | 2019-02-05 | 7.13.1 |
| 1.0.0 | 2018-12-14 | 7.13.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 5.0.0 | breaking | Replaced react-leaflet dependency with direct Leaflet integration due to licensing considerations. | react-leaflet, Leaflet |  |
| 5.0.0 | requirement | Raised minimum Mendix version to 10.24.0 because default markers rely on client resource serving. | Mendix |  |
| 4.0.0 | breaking | Updated Google Maps component, removing deprecated marker and adding advanced marker element. | marker, advanced marker | advanced marker |
| 4.0.0 | removal | Removed mapsStyles property used in Google Maps. | mapsStyles |  |
| 4.0.0 | requirement | Added mapId property that is required with the advanced marker element. | mapId |  |
| 3.1.3 | improvement | Updated the dependencies. | dependencies |  |
| 3.0.1 | breaking | Renamed property Google maps API Key to Geo Location API key. | Google maps API Key | Geo Location API key |
| 3.0.1 | requirement | Made Geo Location API key property required when using location based on Address. | Geo Location API key |  |
| 3.0.0 | breaking | Renamed advanced options property to emphasize it is about advanced properties activation. | advanced options |  |
| 2.0.3 | breaking | Renamed Markers and Marker list properties to Static and Dynamic markers. | Markers, Marker list | Static markers, Dynamic markers |
| 2.0.1 | breaking | Changed anchor of custom marker icons to be center of icon instead of top left corner. | custom marker icons |  |
| 2.0.0 | breaking | Updated widget away from deprecated Mapbox API. | Mapbox API |  |
| 2.0.0 | improvement | Updated widget consistency checks to be compatible with Mendix 9. | consistency checks |  |
| 1.0.10 | breaking | Updated widget away from deprecated Mapbox API. (Fixes Ticket #121474) | Mapbox API |  |

## Markdown viewer <a id="230248"></a>
Widget, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/230248)

| version | published | min Mendix |
|---|---|---|
| 1.1.0 | 2026-09-18 | 9.24.0 |
| 1.0.3 | 2026-07-22 | 9.24.0 |
| 1.0.2 | 2026-04-13 | 9.24.0 |
| 1.0.1 | 2026-02-11 | 9.24.0 |
| 1.0.0 | 2024-08-19 | 9.24.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.1.0 | security | Updated markdown-it dependencies to mitigate potential security vulnerabilities. | markdown-it |  |
| 1.0.3 | security | Updated markdown-it library to version 14.3.0 to incorporate latest security fixes. | markdown-it |  |
| 1.0.2 | security | Updated underlying dependencies to mitigate potential security vulnerabilities. |  |  |

## Marketo Connector <a id="113760"></a>
Module, Mendix, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/113760)

| version | published | min Mendix |
|---|---|---|
| 2.1.0 | 2022-01-02 | 9.0.5 |
| 2.0.0 | 2021-08-31 | 8.12.7 |
| 1.0.0 | 2020-04-21 | 8.8.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.1.0 | requirement | Upgrade to support Atlas 3 and Mendix 9 | Atlas, Mendix |  |
| 2.0.0 | improvement | Improved encryption implementation | encryption |  |

## Math Module <a id="112522"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/112522)

| version | published | min Mendix |
|---|---|---|
| 2.0.0 | 2022-02-11 | 9.0.5 |
| 1.1.0 | 2020-01-17 | 8.0.0 |
| 1.0.0 | 2020-01-15 | 8.0.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.0.0 | requirement | Requires Mendix 9.0.5 or higher |  |  |
| 2.0.0 | improvement | Updated mXparser to version 4.4.2 | mXparser |  |
| 1.1.0 | breaking | Domain model updated for clear distinction between results with overlapping attributes for validation |  |  |

## Matrix <a id="112555"></a>
Widget, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/112555)

| version | published | min Mendix |
|---|---|---|
| 1.4.0 | 2021-09-07 | 8.0.0 |
| 1.3.4 | 2020-07-19 | 8.0.0 |
| 1.3.3 | 2020-07-15 | 8.0.0 |
| 1.3.2 | 2020-04-29 | 8.0.0 |
| 1.3.1 | 2020-04-23 | 8.0.0 |
| 1.3.0 | 2020-04-03 | 8.0.0 |
| 1.2.1 | 2020-03-03 | 8.0.0 |
| 1.2.0 | 2020-02-05 | 8.0.0 |
| 1.1.0 | 2020-02-03 | 8.0.0 |
| 1.0.0 | 2020-01-20 | 8.0.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.4.0 | fix | Fix for MX9 compatibility (issues #13 #14) |  |  |
| 1.3.3 | improvement | Improved rendering to fix issues with large data sets (#9) |  |  |
| 1.3.2 | fix | Fixed column microflow/nanoflow expecting wrong parameter (#7) |  |  |
| 1.3.1 | fix | Rewrote state reset table so data reloads when context object changes |  |  |
| 1.2.1 | improvement | Updated TemplateComponent to react-mustache-template-component@1.0.0 | react-mustache-template-component |  |
| 1.1.0 | improvement | Replaced sanitize-html with dompurify, reducing widget size by 25% | sanitize-html, dompurify | dompurify |

## MCP Client <a id="244893"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/244893)

| version | published | min Mendix |
|---|---|---|
| 4.3.0 | 2026-09-25 | 11.12.4 |
| 4.2.0 | 2026-08-31 | 11.12.3 |
| 4.1.1 | 2026-08-07 | 11.12.2 |
| 4.1.0 | 2026-07-22 | 11.12.1 |
| 4.0.0 | 2026-07-02 | 11.12.0 |
| 3.1.0 | 2026-05-13 | 10.24.13 |
| 3.0.1 | 2026-03-10 | 10.24.13 |
| 2.5.0 | 2026-01-19 | 10.24.13 |
| 2.4.0 | 2026-01-02 | 10.24.13 |
| 2.3.0 | 2025-11-21 | 10.24.0 |
| 2.2.1 | 2025-11-07 | 10.24.0 |
| 2.2.0 | 2025-10-15 | 10.24.0 |
| 2.1.0 | 2025-09-19 | 10.24.0 |
| 2.0.0 | 2025-08-29 | 10.24.0 |
| 1.0.0 | 2025-08-13 | 10.24.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 4.3.0 | improvement | Tool result object isError = true is now reflected in subsequent microflows and visible in UI. | tool result object |  |
| 4.2.0 | requirement | Upgraded to Mendix 11.12.3 | Mendix |  |
| 4.1.1 | requirement | Upgrade to Mendix 11.12.2 | Mendix |  |
| 4.1.1 | fix | Fixed bug that made 'version' field mandatory for ConsumedMCPServices. | ConsumedMCPServices, version field |  |
| 4.1.1 | fix | Fixed bug that caused second MCP tool call with user approval setting within same agent loop to fail. | MCP tool call |  |
| 4.1.0 | requirement | Upgraded module to Mendix 11.12.1 | Mendix |  |
| 4.1.0 | requirement | Upgraded Java SDK to v2.0.0 | Java SDK |  |
| 4.0.0 | requirement | Upgraded module to Mendix 11.12 | Mendix |  |
| 4.0.0 | removal | Deprecated entities were removed. Refer to migration guide for multi-version upgrades. |  |  |
| 3.1.0 | requirement | Upgraded MCP Java SDK version to 1.1.1 | Java SDK |  |
| 3.1.0 | breaking | No longer append endpoint with /mcp or /sse; ensure endpoint is set correctly with /mcp or /sse if applicable. | endpoint |  |
| 3.0.1 | migration-step | Module aligned with latest ConsumedKnowledgeBase and ConsumedMCPService changes requiring migration. Refer to migration guide. | ConsumedKnowledgeBase, ConsumedMCPService |  |
| 3.0.1 | feature | User Access and Approval feature added for tool calls visibility and user control. Display title and description optional fields now available. | MCP tools |  |
| 3.0.1 | requirement | Compatible with GenAI Commons 6.0.0 version | GenAI Commons |  |
| 2.5.0 | feature | Support for complex tools with array parameters and descriptive schemas. MCP tools contain exact schema from server. | MCP tools |  |
| 2.5.0 | requirement | Compatible with latest GenAI Commons version. Update applicable LLM connectors. | GenAI Commons, LLM connectors |  |
| 2.4.0 | feature | Added Streamable HTTP transport method support with 2025-03-26 protocol version. | HTTP transport |  |
| 2.4.0 | breaking | Create MCP Client action now throws error when unable to connect. Implement error handling in all places. | Create MCP Client action |  |
| 2.4.0 | feature | Added ConnectionTimeOutInSeconds to MCPServerConfiguration. Default timeout 10 seconds. | MCPServerConfiguration |  |
| 2.4.0 | requirement | Module upgraded to Mendix 10.24.13 | Mendix |  |
| 2.3.0 | improvement | Internal change for compatibility with ConversationalUI v5.3.0 Observability for AI Traces. | ConversationalUI |  |
| 2.2.0 | improvement | MCP tool sync process improved. Sync added to task queue and completed in background. | MCP tool sync process |  |
| 2.1.0 | feature | Added logic to persist tools information from MCP servers. Admin actions for manual sync and scheduled event added. | MCP server |  |
| 2.1.0 | feature | New toolbox action to add specific MCP tool from server to request. | toolbox action |  |
| 2.0.0 | breaking | Refactored module to persist MCP server configurations. Toolbox operations now require MCPServerConfiguration object. | toolbox operations, MCPServerConfiguration |  |

## MCP for Studio Pro <a id="258524"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/258524)

| version | published | min Mendix |
|---|---|---|
| 1.1.1 | 2026-04-01 | 10.24.13 |
| 1.1.0 | 2026-04-01 | 10.24.13 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.1.0 | feature | Connect AI assistants like Claude, Cursor, and GitHub Copilot directly to Mendix Studio Pro modeling environment via MCP server. | MCP, Studio Pro Extensions API |  |
| 1.1.0 | requirement | Requires Mendix Studio Pro 10.24.13 or higher. | Mendix Studio Pro |  |
| 1.1.0 | known-issue | Page editing is limited to overview page generation; no widget-level creation/editing available. | Page editing |  |
| 1.1.0 | known-issue | Nanoflows and Workflows are read-only; cannot be created or modified. | Nanoflows, Workflows |  |
| 1.1.0 | known-issue | Log Message activity is not available in the Extensions API. | Log Message activity |  |
| 1.1.0 | known-issue | Some microflow activities (retrieve, change_object) may need post-creation correction via modify_microflow_activity. | retrieve, change_object |  |

## MCP Server <a id="240380"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/240380)

| version | published | min Mendix |
|---|---|---|
| 5.3.0 | 2026-09-25 | 11.12.4 |
| 5.2.0 | 2026-08-31 | 11.12.3 |
| 5.1.0 | 2026-07-22 | 11.12.1 |
| 5.0.0 | 2026-07-02 | 11.12.0 |
| 4.1.1 | 2026-04-28 | 10.24.13 |
| 4.0.0 | 2026-01-19 | 10.24.13 |
| 3.2.0 | 2026-01-02 | 10.24.13 |
| 3.1.0 | 2025-10-15 | 10.24.0 |
| 3.0.0 | 2025-08-13 | 10.24.0 |
| 2.1.1 | 2025-07-22 | 10.21.1 |
| 2.0.0 | 2025-06-26 | 10.21.1 |
| 1.0.0 | 2025-04-25 | 10.21.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 5.3.0 | breaking | Integer parameters of tools now declared as integers in automatic schema creation (previously: numbers). | tools, schema creation |  |
| 5.3.0 | security | Fixed bug where unauthorized requests came through without user context. Smaller request handling changes implemented. | request handling, user context |  |
| 5.3.0 | requirement | MCP Server path validation: no support for additional path segments (no / allowed in path). | MCP Server path |  |
| 5.2.0 | requirement | Upgraded to Mendix 11.12.3. | Mendix |  |
| 5.2.0 | improvement | Setting Authentication Microflow during server initialization is now optional (previously required). | Authentication Microflow |  |
| 5.1.0 | requirement | Upgraded to Mendix 11.12.1. | Mendix |  |
| 5.1.0 | fix | Fixed bug affecting MCP Server creation during after-startup logic due to Root URL fetch failure. | MCP Server, Root URL |  |
| 5.0.0 | requirement | Module upgraded to Mendix 11.12. | Mendix |  |
| 5.0.0 | feature | MCP Server endpoint is now part of object and gets logged in console. | MCP Server, endpoint |  |
| 4.1.1 | security | Changed jackson library dependency declaration for automatic updates, fixing severe vulnerability. | jackson library |  |
| 4.0.0 | breaking | Added Streamable HTTP transport support. Legacy HTTP+SSE transport v2024-11-05 no longer available. | HTTP transport, protocol version |  |
| 4.0.0 | fix | Fixed issue where Mendix/MCP session was not reused with authentication enabled, causing session limit errors. | Mendix session, MCP session, authentication |  |
| 4.0.0 | fix | Fixed bug blocking multiple servers running in same Mendix app; last started server no longer overwrites previous tools. | multiple servers |  |
| 4.0.0 | requirement | MCP server paths validated; path cannot be 'mcp'. | MCP server path |  |
| 3.2.0 | requirement | MCP SDK version upgraded to 0.16.0. | MCP SDK |  |
| 3.2.0 | improvement | Thread sleep setting removed from request handler; now handled by Studio Pro Runtime. | request handler |  |
| 3.1.0 | feature | User and session now in scope of tool and prompt microflows for role/user-based access control. | tool microflows, prompt microflows, user, session |  |
| 3.0.0 | requirement | MCP Java SDK version upgraded to 0.11.1. | MCP Java SDK |  |
| 3.0.0 | requirement | Module upgraded to Mendix Studio Pro version 10.24. | Mendix |  |
| 2.1.0 | feature | Schema input for AddTool action now optional; auto-created from microflow input or overwritten if provided. | AddTool, schema |  |
| 2.0.0 | feature | MCP Server now accepts optional authentication microflow executed on client connection for custom auth methods. | MCP Server, authentication microflow |  |
| 2.0.0 | requirement | MCP Server creation now requires specifying MCP version; currently only 2024_11_05 allowed. | MCP Server, MCP version |  |

## Menditect - Microflow Call Hierarchy <a id="225211"></a>
Module, Menditect, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/225211)

| version | published | min Mendix |
|---|---|---|
| 3.0.0 | 2024-06-27 | 10.12.0 |
| 2.12.4 | 2024-04-16 | 10.6.3 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 3.0.0 | requirement | Minimum Mendix version requirement increased to 10.12.0. Use version 2.12.4 for older Mendix versions. | Mendix |  |
| 2.12.4 | requirement | Minimum Mendix version requirement is 10.6.3. | Mendix |  |

## Menditect Test Automation (MTA) <a id="120116"></a>
Solution, Menditect, Partner, [marketplace](https://marketplace.mendix.com/link/component/120116)

| version | published | min Mendix |
|---|---|---|
| 2.0.0 | 2023-05-03 | ? |

## Mendix Application Performance Diagnostics <a id="6127"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/6127)

| version | published | min Mendix |
|---|---|---|
| 3.77.92 | 2026-01-13 | 11.0.0 |
| 3.76.92 | 2026-01-13 | 10.0.0 |
| 3.75.92 | 2026-01-13 | 9.0.5 |
| 3.74.91 | 2025-05-14 | 10.0.0 |
| 3.73.91 | 2025-05-14 | 9.0.5 |
| 3.72.91 | 2025-05-14 | 8.0.0 |
| 3.71.90 | 2025-02-07 | 10.0.0 |
| 3.70.90 | 2025-02-07 | 9.0.5 |
| 3.69.90 | 2025-02-07 | 8.0.0 |
| 3.68.89 | 2024-10-02 | 10.0.0 |
| 3.67.89 | 2024-10-02 | 9.0.5 |
| 3.66.89 | 2024-10-02 | 8.0.0 |
| 3.65.88 | 2024-02-08 | ? |
| 3.64.88 | 2024-02-08 | 9.0.5 |
| 3.62.88 | 2024-02-08 | 8.0.0 |
| 3.61.87 | 2024-01-10 | 10.0.0 |
| 3.60.87 | 2024-01-10 | 9.0.5 |
| 3.59.87 | 2024-01-10 | 8.0.0 |
| 3.58.86 | 2023-07-27 | 10.0.0 |
| 3.57.86 | 2023-07-27 | 9.0.5 |
| 3.56.86 | 2023-07-27 | 8.0.0 |
| 3.45.82 | 2022-03-16 | 9.0.5 |
| 3.44.82 | 2022-03-16 | 8.0.0 |
| 3.43.82 | 2022-03-16 | 7.0.2 |
| 3.41.81 | 2022-02-23 | 9.0.5 |
| 3.40.81 | 2022-02-23 | 8.0.0 |
| 3.39.81 | 2022-02-23 | 7.0.2 |
| 3.37.80 | 2022-02-22 | 9.0.5 |
| 3.36.80 | 2022-02-22 | 8.0.0 |
| 3.33.80 | 2022-02-22 | 7.0.2 |
| 3.33.79 | 2021-10-25 | 9.0.5 |
| 3.32.79 | 2021-10-25 | 8.0.0 |
| 3.31.79 | 2021-10-25 | 7.0.2 |
| 3.25.77 | 2021-10-06 | 9.0.5 |
| 3.24.77 | 2021-10-06 | 8.0.0 |
| 3.23.77 | 2021-10-06 | 7.0.2 |
| 3.0.54 | 2023-02-26 | 9.0.5 |
| 3.0.53 | 2023-02-26 | 8.0.0 |
| 3.0.52 | 2023-02-26 | 7.0.2 |
| 3.0.51 | 2022-09-13 | 9.0.5 |
| … 33 older versions | | |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 3.77.92 | fix | Mendix 11.6.0 compatibility |  |  |
| 3.76.92 | fix | Mendix 11.6.0 compatibility |  |  |
| 3.75.92 | fix | Mendix 11.6.0 compatibility |  |  |
| 3.71.90 | fix | Mx 10.18 compatibility |  |  |
| 3.71.90 | deprecation | Database profiler is deprecated in Mx 10.18 and is now disabled in the APD Agent. Use AdvancedSettings 'useprofiler=true' to re-enable. | Database profiler |  |
| 3.71.90 | removal | Browser agent has been discontinued. Please remove the widget 'Mansystems.APDBrowserAgent.mpk' from the project 'widgets' folder. | Browser agent |  |
| 3.70.90 | removal | Browser agent has been discontinued. Please remove the widget 'Mansystems.APDBrowserAgent.mpk' from the project 'widgets' folder. | Browser agent |  |
| 3.69.90 | removal | Browser agent has been discontinued. Please remove the widget 'Mansystems.APDBrowserAgent.mpk' from the project 'widgets' folder. | Browser agent |  |
| 3.68.89 | improvement | Agent now logs running microflows, when memory protection lock is initially set. |  |  |
| 3.67.89 | improvement | Agent now logs running microflows, when memory protection lock is initially set. |  |  |
| 3.66.89 | improvement | Agent now logs running microflows, when memory protection lock is initially set. |  |  |
| 3.61.87 | improvement | Improved capturing and linking of submicrolfows, when using the same context. |  |  |
| 3.61.87 | improvement | Client API calls for microflow now also capture and specify the time needed before and after microflow execution. |  |  |
| 3.61.87 | fix | Added Mx 10.6 compatibility |  |  |
| 3.60.87 | improvement | Improved capturing and linking of submicrolfows, when using the same context. |  |  |
| 3.60.87 | improvement | Client API calls for microflow now also capture and specify the time needed before and after microflow execution. |  |  |
| 3.60.87 | fix | Added Mx 10.6 compatibility |  |  |
| 3.59.87 | improvement | Improved capturing and linking of submicrolfows, when using the same context. |  |  |
| 3.59.87 | improvement | Client API calls for microflow now also capture and specify the time needed before and after microflow execution. |  |  |
| 3.59.87 | fix | Added Mx 10.6 compatibility |  |  |
| 3.58.86 | security | Updated dependencies for security fixes |  |  |
| 3.58.86 | fix | Added Mx 9.24 compatibility |  |  |
| 3.57.86 | security | Updated dependencies for security fixes |  |  |
| 3.57.86 | fix | Added Mx 9.24 compatibility |  |  |
| 3.56.86 | security | Updated dependencies for security fixes |  |  |
| 3.56.86 | fix | Added Mx 9.24 compatibility |  |  |
| 3.37.80 | breaking | Renamed snippet to be inline with ACR naming convention |  |  |
| 3.36.80 | breaking | Renamed snippet to be inline with ACR naming convention |  |  |
| 3.33.80 | migration-step | Renamed snippet to align with ACR naming convention. | snippet |  |
| 3.31.79 | fix | Fixed deprecation warnings due to usage of logger object instead of mx.logger in Mx9. | Mx 9 agent, logger, mx.logger |  |
| 3.23.77 | improvement | Separate channel for manual statistics from hourly statistics prevents one blocking process queue. | manual statistics, hourly statistics |  |
| 3.0.49 | fix | Log node DataStorage_QueryPlan excluded by default for trap collection to prevent 'explain analyze' queries. | Log node DataStorage_QueryPlan |  |
| 3.0.49 | fix | Fix loop iterations not linked to microflow due to missing type for Loop actions in Mx9. | APD Agent, Loop actions, Mendix 9.17.0 |  |
| 3.0.48 | feature | Added option to use a microflow to return the API key instead of a constant. |  |  |
| 3.0.47 | feature | Added option to use a microflow to return the API key instead of a constant. |  |  |
| 3.0.20 | fix | A VerifyError was thrown when using the APD agent and Datadog agent together. | Datadog agent |  |
| 3.0.19 | fix | Fixed VerifyError thrown when using APD agent and Datadog agent together. | APD agent, Datadog agent |  |
| 3.0.17 | security | Admin features to execute queries and create heap dumps disabled by default. |  |  |
| 3.0.17 | breaking | Load test recording default disabled. |  |  |
| 3.0.16 | requirement | Admin features to execute queries and create heap dumps disabled by default. | Admin features |  |
| 3.0.16 | requirement | Load test recording default disabled. | Load test recording |  |
| 3.0.16 | fix | Log levels set from Mx Modeler/Studio/Cloud no longer affect APD agent log level. | log levels, APD agent |  |
| 3.0.2 | breaking | Renamed components to match the APD name. |  |  |
| 3.0.2 | breaking | Advanced settings should now be lowercase. This mainly affects 'proxy' settings, as these were camel case. |  |  |
| 3.0.2 | breaking | Advanced setting behavior changed for 'Memory Protection Time' to no longer stop the agent after the defined time. Instead it will repeat the sleep. |  |  |
| 3.0.1 | migration-step | Renamed components to match APD name. | component names |  |
| 3.0.1 | breaking | Advanced settings should now be lowercase; affects camel case proxy settings. | advanced settings, proxy |  |
| 3.0.1 | breaking | Memory Protection Time behavior changed: no longer stops agent; repeats sleep until memory reduced. | Memory Protection Time |  |
| 2.0.21 | improvement | Added check on startup to detect if proper agent jar file has been loaded. | agent jar file |  |
| 2.0.19 | breaking | Changed behavior for advanced setting 'memoryagentstoplimit'; stops processing log messages/recording for a set timeframe instead of instantly. |  |  |
| 2.0.18 | breaking | Advanced setting memoryagentstoplimit behavior changed: agent stops processing for set timeframe. | memoryagentstoplimit |  |
| 2.0.16 | breaking | Removed CORS headers from 'apm'-request handler |  |  |
| 2.0.15 | removal | Removed CORS headers from 'apm' request handler. | CORS headers, apm request handler |  |
| 2.0.13 | improvement | Merged statistics and recording collecting, reducing overhead and resource usage. | Browser agent, Runtime agent |  |
| 2.0.13 | improvement | Improved support for Mendix 7.6 and newer. | Browser agent |  |
| 2.0.13 | migration-step | JSON Logging set behind advanced setting. | JSON Logging, Runtime agent |  |
| 2.0.12 | improvement | Merged statistics and recording collecting, reducing overhead and resource usage. | Browser agent, Runtime agent |  |
| 2.0.12 | improvement | Improved support for Mendix 7.6 and newer. | Browser agent |  |
| 2.0.12 | migration-step | JSON Logging set behind advanced setting. | JSON Logging |  |
| 2.0.10-beta | migration-step | JSON Logging set behind advanced setting. | JSON Logging |  |
| 2.0.9 | migration-step | JSON Logging set behind advanced setting. | JSON Logging |  |
| 2.0.7 | improvement | Memory improvement: default 80% heap clear buffers, 90% stops agent; configurable via advanced settings. | memory |  |
| 2.0.7 | improvement | Performance improvement: max depth for microflow statistics with manual created loop reduced. | microflow statistics |  |
| 2.0.6 | improvement | Memory improvement: default 80% heap clear buffers, 90% stops agent; configurable via advanced settings. | memory |  |
| 2.0.6 | improvement | Performance improvement: max depth for microflow statistics with manual created loop reduced. | microflow statistics |  |
| 2.0.5 | known-issue | Buffer limit between Mendix log thread and APM threads; fast delivery causes message drops. | buffer, APM threads |  |
| 2.0.5 | feature | Advanced settings added for profiler, recorder, maxtrap, maxstatistics to tune agent. | profiler, recorder, maxtrap, maxstatistics |  |
| 2.0.5 | requirement | Hard-coded maximum for messages accepted by APM Agent/manager from Mendix log thread. | message, stack trace |  |
| 2.0.5 | improvement | Hourly purge of performance tool memory structures during statistics snapshot to prevent OOM. | memory |  |
| 2.0.5 | improvement | Extra clearing of memory structures to faster release memory and ease garbage collection. | memory |  |
| 2.0.3 | improvement | When connection lost with APM Manager, agent delays subsequent calls; max delay 5 min. | APM Manager connection |  |
| 2.0.3 | improvement | Performance optimizations. |  |  |
| 2.0.1 | improvement | Reduced logging from Agent; full JSON messages logging on error default disabled. | Agent logging |  |
| 2.0.1 | improvement | When Browser Agent disabled per APM Manager config, agent no longer logs error. | Browser Agent |  |
| 1.12.0 | improvement | Protection in logtool to configure 'Max messages to store' default 100.000 records. | logtool, Max messages |  |
| 1.12.0 | improvement | Fallback level protection sets logging to INFO when logtool notices excessive data processing. | logtool, Fallback level |  |
| 1.12.0 | fix | Fixed behavior preventing application from running out of heap memory on excessive INFO logging. | heap memory |  |
| 1.12 | fix | Upgrade function on low-memory environments now commits statistics, measurements, and traps data in chunks to prevent out of memory. |  |  |
| 1.12 | removal | Removed fixed duration function from trap and statistics tool as unused and not fitting module scope. | fixed duration function |  |
| 1.12 | improvement | Default trap tool buffer setting in production now stops tool to prevent continuous load from high error volumes. | trap tool buffer default settings |  |
| 1.12 | fix | Fixed incorrect default JDBC settings for MSSQL after installation. | JDBC settings for MSSQL |  |
| 1.12 | fix | Renamed Java action parameters to prevent errors from Mendix generating different names across versions. | Java action parameters |  |
| 1.10.1 | requirement | First version fully available for Mendix 7 with separate package; Mendix 6 package available on All Versions tab. |  |  |

## Mendix Business Events <a id="202649"></a>
Service, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/202649)

| version | published | min Mendix |
|---|---|---|
| 3.12.1 | 2026-05-12 | 10.21.1 |
| 3.12.0 | 2026-03-24 | 10.21.1 |
| 3.11.0 | 2025-06-19 | 10.21.1 |
| 3.10.1 | 2025-01-16 | 9.18.7 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 3.12.1 | security | Upgraded kotlin to 2.3.21 to address transitive dependency vulnerabilities. | kotlin |  |
| 3.11.0 | breaking | Replaced deprecated Mendix Java APIs to support Mendix v10.21+. | Mendix Java APIs |  |
| 3.10.1 | security | Fixed the Kafka client vulnerability by upgrading the lib. | Kafka client |  |
| 3.10.1 | requirement | Upgraded to SP 9.18.7. | Mendix |  |

## Mendix Cloud Client Certificate Verification Module <a id="208293"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/208293)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2023-03-08 | 9.18.0 |

## Mendix Cloud GenAI Connector <a id="239449"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/239449)

| version | published | min Mendix |
|---|---|---|
| 7.2.1 | 2026-08-13 | 11.12.2 |
| 7.2.0 | 2026-08-07 | 11.12.2 |
| 7.1.0 | 2026-07-22 | 11.12.1 |
| 7.0.0 | 2026-07-02 | 11.12.0 |
| 6.2.0 | 2026-06-25 | 10.24.13 |
| 6.1.0 | 2026-03-27 | 10.24.13 |
| 6.0.1 | 2026-03-10 | 10.24.13 |
| 5.5.0 | 2026-01-19 | 10.24.13 |
| 5.4.0 | 2025-12-22 | 10.24.13 |
| 5.3.0 | 2025-12-03 | 10.24.0 |
| 5.2.0 | 2025-09-19 | 10.24.0 |
| 5.1.0 | 2025-08-13 | 10.24.0 |
| 5.0.0 | 2025-08-08 | 10.24.0 |
| 4.3.1 | 2025-08-06 | 10.21.0 |
| 4.3.0 | 2025-07-21 | 10.21.0 |
| 4.2.0 | 2025-07-02 | 10.21.0 |
| 4.1.0 | 2025-06-24 | 10.21.0 |
| 4.0.0 | 2025-06-13 | 10.21.0 |
| 3.1.1 | 2025-08-06 | 10.21.0 |
| 3.1.0 | 2025-05-09 | 10.21.0 |
| 3.0.0 | 2025-04-08 | 10.21.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 7.2.1 | fix | Fixed bug causing invocation of default model instead of selected model for streaming API requests. | streaming API |  |
| 7.2.0 | requirement | Upgrade to Mendix 11.12.2. | Mendix |  |
| 7.2.0 | feature | Streaming responses now supported for text generation models. Model responses appear word-by-word in real time. | text generation models, streaming, ConversationalUI |  |
| 7.1.0 | requirement | Upgrade to Mendix 11.12.1. | Mendix |  |
| 7.1.0 | fix | Fixed bug preventing tool choice 'tool' from being applied correctly in multi-turn conversations. | tool choice, multi-turn conversations |  |
| 7.0.0 | requirement | Module upgraded to Mendix 11.12.0. | Mendix |  |
| 7.0.0 | removal | Data migration microflows from previous major version removed. Use migration guide for multi-version upgrades. | data migration microflows |  |
| 6.2.0 | feature | Connector now supports multi-model capability. All available models created on key creation; select preferred model per job. | GenAI resources, multi-model capability |  |
| 6.0.1 | breaking | Module aligned with latest ConsumedKnowledgeBase and ConsumedMCPService changes. Breaking change requiring migration to prevent data loss. | ConsumedKnowledgeBase, ConsumedMCPService |  |
| 6.0.1 | improvement | Internal error handling changed so errors passed to calling GenAI Commons operations for chat completions. | error handling, GenAI Commons operations |  |
| 6.0.1 | requirement | Compatible with GenAI Commons 6.0.0 version. | GenAI Commons |  |
| 5.5.0 | improvement | Module now compatible with latest version of GenAI Commons. | GenAI Commons |  |
| 5.4.0 | feature | Changes made to support showing agents origin, e.g., 'In App' in overview pages. | agents origin |  |
| 5.4.0 | improvement | Provider information and non-technical name now updated in Configuration Overview when using or importing key, enabling model version synchronization. | key import, Configuration Overview |  |
| 5.4.0 | requirement | Module upgraded to Mendix 10.24.13. | Mendix |  |
| 5.3.0 | feature | Cohere Embed 4 now supported. | Cohere Embed 4 |  |
| 5.2.0 | fix | Fixed issue where tool message content was not mapped correctly in response. | tool message, response mapping |  |
| 5.1.0 | improvement | GenAICommons ArgumentInput objects mapped to Mendix Cloud GenAI API input schema, enabling MCP Client use cases. | tool calling, GenAICommons ArgumentInput, Mendix Cloud GenAI API |  |
| 5.0.0 | requirement | Module upgraded to Mendix Studio Pro version 10.24. | Mendix Studio Pro |  |
| 4.3.0 | improvement | Connector compatible with newest GenAI Commons. Tool microflows accept multiple primitive input parameters (Boolean, Enumeration, Integer, DateTime, Decimal). | GenAI Commons, tool microflows |  |
| 4.3.0 | fix | Fixed bug where collections missing microflow for knowledge base retrieval selection. Collection object reuse prevents recreation. | Collection, knowledge base retrieval |  |
| 4.2.0 | improvement | All knowledge base references now added to final assistant response in Tools: Add Knowledge Base action use cases. | knowledge base references, Tools: Add Knowledge Base |  |
| 4.2.0 | fix | Fixed bug preventing admins from testing knowledge base keys on configuration page. | knowledge base keys, configuration page |  |
| 4.1.0 | improvement | Minor changes (granted Collection entity access) to support runtime agent configuration via AgentCommons module. | Collection, AgentCommons |  |
| 4.0.0 | breaking | Collection entity now inherits from new DeployedKnowledgeBase entity. Microflows reconfigured for new entity. | Collection, DeployedKnowledgeBase |  |
| 4.0.0 | improvement | Collections automatically synced when new token imported. | Collections |  |
| 3.1.0 | feature | ToolChoice can now be added to request via Request_SetToolChoice to control tool usage in chat interactions. | ToolChoice, Request_SetToolChoice, GenAICommons |  |
| 3.0.0 | breaking | Add-On module converted to App module. Requires migration when updating. | module type |  |
| 3.0.0 | requirement | Module updated to Mendix Studio Pro 10.21.0. | Mendix Studio Pro |  |
| 3.0.0 | migration-step | Backup data; delete Add-On MxGenAIConnector; download marketplace module; re-import keys; restore lost data on deployed environments. | MxGenAIConnector, data, keys, associations |  |

## Mendix Event Broker <a id="202907"></a>
Service, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/202907)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2022-09-28 | 9.18.0 |

## Mendix Feedback Module <a id="205506"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/205506)

| version | published | min Mendix |
|---|---|---|
| 5.0.0 | 2026-06-16 | 10.24.0 |
| 4.1.1 | 2026-02-06 | 10.21.0 |
| 4.0.4 | 2025-12-04 | 10.21.0 |
| 4.0.3 | 2025-10-14 | 10.21.0 |
| 4.0.2 | 2025-07-18 | 10.21.0 |
| 4.0.1 | 2025-05-20 | 10.21.0 |
| 4.0.0 | 2025-04-25 | 10.21.0 |
| 3.1.0 | 2025-04-25 | 9.24.0 |
| 3.0.0 | 2024-09-20 | 9.24.0 |
| 2.0.1 | 2024-08-12 | 9.24.0 |
| 2.0.0 | 2024-07-26 | 9.24.0 |
| 1.4.1 | 2024-03-14 | 9.18.6 |
| 1.4.0 | 2024-02-02 | 9.18.6 |
| 1.3.2 | 2023-11-03 | 9.18.6 |
| 1.3.1 | 2023-10-31 | 9.18.6 |
| 1.3.0 | 2023-10-27 | 9.18.6 |
| 1.2.1 | 2023-09-27 | 9.18.6 |
| 1.2.0 | 2023-07-13 | 9.18.6 |
| 1.1.1 | 2023-04-14 | 9.18.5 |
| 1.1.0 | 2023-04-11 | 9.18.5 |
| 1.0.0 | 2022-12-13 | 9.12.2 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 5.0.0 | requirement | Minimum LTS support is now Mendix Studio Pro 10.24.0 |  |  |
| 5.0.0 | improvement | Updated XSS_Sanitizer & ValidateEmail java actions to remove unwanted console log runtime messages on app startup. | XSS_Sanitizer, ValidateEmail |  |
| 4.1.1 | fix | Resolved issue where Feedback widget could break Mendix page layout when React client was disabled. | Feedback widget |  |
| 4.1.1 | breaking | PopulateAttributes microflow has been updated; may need to reassign attributes within it. | PopulateAttributes |  |
| 4.0.2 | fix | Default Feedback button did not open modal pop-up in Mendix Studio Pro 10.24+ due to hidden nanoflow configuration being ignored. | Feedback button |  |
| 4.0.2 | fix | Local storage JavaScript actions in DS_Feedback_Populate nanoflow did not function properly, causing failures in retrieving feedback metadata. | DS_Feedback_Populate |  |
| 4.0.2 | fix | Exposing custom JavaScript actions as nanoflow actions caused conflicts with default actions. |  |  |
| 4.0.1 | fix | When Strict Mode is enabled, feedback local storage meta data is now correctly captured and saved. |  |  |
| 4.0.0 | improvement | Feedback Module is now compatible with React client enabled in Mendix apps. | Feedback Module |  |
| 4.0.0 | breaking | Feedback widget now uses new functionality to open modal form; no longer backwards compatible with Mendix Studio Pro versions earlier than v10.15.0. | Feedback widget |  |
| 3.1.0 | known-issue | Not compatible with Strict Mode (Mendix 10.12.0+). Use Feedback Module v4.0.1 or higher. |  |  |
| 3.0.0 | removal | Removed all example translation pages; translations now handled using batch translations tool. |  |  |
| 3.0.0 | migration-step | Feedback widget must be manually deleted and re-added on page to re-sync Studio Pro localization with new XML translation definitions. | Feedback widget |  |
| 3.0.0 | migration-step | Use batch translate tool to change translations on ShareFeedback modal pages or Screenshot & Annotation button labels. | ShareFeedback, Screenshot, Annotation |  |
| 2.0.1 | fix | Fixed incorrectly assigned nanoflows used in translated ShareFeedback modal pop-up pages. | ShareFeedback |  |
| 2.0.0 | feature | Feedback widget reengineered using Mendix; extensive customization options for button placement, form triggering, styling, and copy. | Feedback widget |  |
| 1.2.0 | feature | Added compatibility with Mendix SSO 4.0.2 and above. |  |  |
| 1.2.0 | improvement | Submitting user details now provided via datasource attributes. |  |  |
| 1.2.0 | removal | Removed DS_GetCurrentIDToken microflow from module. | DS_GetCurrentIDToken |  |
| 1.2.0 | breaking | Renamed Authentication tab to User Info and made configuration more intuitive. | Authentication tab | User Info |
| 1.1.1 | breaking | Removed default App ID from Feedback Widget Building Block. | Feedback Widget |  |
| 1.1.0 | breaking | Feedback submit success image is now optional instead of having default fallback. |  |  |

## Mendix Google Material Icons 2024 (Rounded, Outline, Sharp and Filled versions) <a id="230338"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/230338)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2024-08-26 | 9.24.12 |

## Mendix Mini Surveys <a id="205483"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/205483)

| version | published | min Mendix |
|---|---|---|
| 4.0.1 | 2025-05-09 | 10.21.0 |
| 4.0.0 | 2025-04-28 | 10.21.0 |
| 3.0.4 | 2025-02-12 | 9.24.0 |
| 3.0.2 | 2024-11-14 | 9.24.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 4.0.0 | requirement | Upgraded for Mendix Studio 10.21.0+ with React fully enabled. Minimum Mendix version 10.21.0 required. | Mini Survey module, Mini Survey widget |  |
| 4.0.0 | known-issue | If React not fully enabled: page path metadata not saved and developer console errors may occur. | Mini Survey module, Mini Survey widget |  |
| 4.0.0 | improvement | SurveySubmission_Overview administration page upgraded from DataGrid 1 to DataGrid 2. | SurveySubmission_Overview |  |
| 3.0.2 | breaking | Top-level module name changed from 'AppInsights_MiniSurvey' to 'MiniSurveys'. Manually delete old module. | AppInsights_MiniSurvey, MiniSurveys | MiniSurveys |

## Mendix Service Console <a id="223425"></a>
Service, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/223425)

| version | published | min Mendix |
|---|---|---|
| 4.8.3 | 2026-04-14 | 8.18.34 |
| 4.8.2 | 2025-11-28 | 8.18.34 |
| 4.8.1 | 2025-03-20 | 8.18.34 |
| 4.8.0 | 2024-06-27 | 7.0.2 |
| 4.7.4 | 2024-03-01 | 7.0.2 |
| 4.7.3 | 2024-03-01 | 7.0.2 |
| 4.7.2 | 2024-03-01 | 7.0.2 |
| 4.7.1 | 2024-03-01 | 7.0.2 |
| 4.7.0 | 2024-03-01 | 7.0.2 |
| 4.6.1 | 2024-03-01 | 7.0.2 |
| 4.6.0 | 2024-03-01 | 7.0.2 |
| 4.5.1 | 2024-03-01 | 7.0.2 |
| 4.5.0 | 2024-03-01 | 7.0.2 |
| 4.4.0 | 2024-03-01 | 7.0.2 |
| 4.3.0 | 2024-03-01 | 7.0.2 |
| 4.2.1 | 2024-03-01 | 7.0.2 |
| 4.2.0 | 2024-03-01 | 7.0.2 |
| 4.1.1 | 2024-03-01 | 7.0.2 |
| 4.1.0 | 2024-03-01 | 7.0.2 |
| 4.0.0 | 2024-03-01 | 7.0.2 |
| 3.0.0 | 2024-03-01 | 7.0.2 |
| 2.2.0 | 2024-03-01 | 7.0.2 |
| 2.1.1 | 2024-03-01 | 7.0.2 |
| 2.1.0 | 2024-03-01 | 7.0.2 |
| 2.0.0 | 2024-03-01 | 7.0.2 |
| 1.0.7 | 2024-03-01 | 7.0.2 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 4.8.2 | fix | Fixed issue that updating an app via Update-MxApp cmdlet was slower than via Service Console UI. (Ticket 250362) | Update-MxApp |  |
| 4.8.1 | removal | Removed 'Import old app...' button from Service Settings window for importing apps configured with Mendix Service Console 3.0 and earlier. | Import old app button |  |
| 4.8.1 | breaking | Replaced 'DotNetZip' library by official .NET functionality as it isn't maintained and has vulnerability. | DotNetZip |  |
| 4.8.0 | requirement | Now require at least Microsoft .NET Framework version 4.7.2 instead of 4.6.2 to fix 'netstandard' assembly loading error. | Microsoft .NET Framework |  |
| 4.8.0 | breaking | Installer file name now contains underscores instead of spaces due to Marketplace restrictions. |  |  |
| 4.8.0 | fix | Fixed problem that error occurs when opening window to set levels for log file. Service must be reinstalled. (Ticket 219042) |  |  |
| 4.8.0 | improvement | Updated YamlDotNet library from version 15.1.1 to 15.3.0. | YamlDotNet |  |
| 4.7.4 | improvement | Updated Newtonsoft Json.NET library from version 13.0.2 to 13.0.3. | Newtonsoft Json.NET |  |
| 4.7.4 | improvement | Updated YamlDotNet library from version 12.3.1 to 15.1.1. | YamlDotNet |  |
| 4.7.3 | breaking | Changed default installation directory to 64-bit program files (C:\Program Files) instead of 32-bit directory. | installation directory |  |
| 4.7.1 | improvement | Replaced modified YAML parser YamlSerializer 0.9.0.2 with YamlDotNet 12.3.1. | YamlSerializer, YamlDotNet | YamlDotNet |
| 4.7.1 | improvement | Updated Newtonsoft Json.NET library from version 13.0.1 to 13.0.2. | Newtonsoft Json.NET |  |
| 4.7.0 | requirement | Now requires Microsoft .NET Framework version 4.6.2 instead of 4.5.2. | Microsoft .NET Framework |  |
| 4.7.0 | removal | Removed license ID check in Service Console; this check is done by server. | license ID check |  |
| 4.7.0 | improvement | Updated DotNetZip library from version 1.13.3 to 1.16.0. | DotNetZip |  |
| 4.7.0 | improvement | Updated Newtonsoft Json.NET library from version 12.0.2 to 13.0.1. | Newtonsoft Json.NET |  |
| 4.7.0 | improvement | Updated Tulpep.ActiveDirectoryObjectPicker library from version 2.3.133 to 3.0.11. | Tulpep.ActiveDirectoryObjectPicker |  |
| 4.7.0 | improvement | Replaced old Ookii.Dialogs source code with Ookii.Dialogs.Wpf 5.0.1 library. | Ookii.Dialogs | Ookii.Dialogs.Wpf |
| 4.6.1 | breaking | Update-MxApp cmdlet no longer applies file access rights automatically. Use checkbox on Update App form instead. | Update-MxApp cmdlet |  |
| 4.6.0 | feature | Added support for Studio Pro 8. |  |  |
| 4.6.0 | improvement | Updated Newtonsoft Json.NET library from 5.0.3 to 12.0.2. | Newtonsoft Json.NET |  |
| 4.6.0 | improvement | Updated DotNetZip library from version 1.11.0 to 1.13.3. | DotNetZip |  |
| 4.6.0 | improvement | Replaced old Active Directory Common Dialogs library with Tulpep.ActiveDirectoryObjectPicker 2.3.133. | Tulpep.ActiveDirectoryObjectPicker |  |
| 4.6.0 | known-issue | Oracle Java 8 selected by default for Mendix 8 apps. Select JRE/JDK 11 from Oracle or OpenJDK. Fixed in 4.6.1. |  |  |
| 4.5.1 | requirement | Upgraded target Microsoft .NET Framework version from 4.5 to 4.5.2. |  |  |
| 4.5.1 | improvement | Updated DotNetZip library from version 1.10.1 to 1.11.0. | DotNetZip |  |
| 4.5.1 | removal | Removed dependency on Microsoft.VisualBasic.PowerPacks library. | Microsoft.VisualBasic.PowerPacks |  |
| 4.5.0 | feature | Added support for Mendix 7. |  |  |
| 4.4.0 | breaking | Old app no longer copied to backup file when updated with deployment archive; checkbox enables backup. |  |  |
| 4.4.0 | feature | Added DB2 and MariaDB as database types, useful when supported by app server version. |  |  |
| 4.4.0 | improvement | Updated DotNetZip library from version 1.9.1.8 to 1.10.1. | DotNetZip |  |
| 4.3.0 | feature | Added support for Mendix 6.3. Service must be reinstalled if app upgraded from earlier version. |  |  |
| 4.3.0 | requirement | .NET Framework 4.5 now required. Dropped support for Windows Server 2003/2003 R2/XP. |  |  |
| 4.2.1 | fix | Prevented shared runtime mxclientsystem folder from being emptied when app removed. |  |  |
| 4.2.1 | feature | Added MySQL as new database type, supported since Mendix 5.12. |  |  |
| 4.2.0 Beta 1 | removal | Disabled possibility to set environment to deprecated 'Acceptance' runtime configuration mode for Mendix 5+ apps. |  |  |
| 4.2.0 | migration-step | All service user passwords and database passwords will be encrypted in settings files after opening Mendix Service Console for first time. |  |  |
| 4.2.0 | breaking | Service must be reinstalled with this version for Start service button to handle database synchronizations. |  |  |
| 4.2.0 | security | Deployment packages and server distribution files now checked on directory traversal attacks. |  |  |
| 4.0.0 | feature | Mendix Service Console 4 manages all Mendix 3 and 4 apps in one application with unified left bar. |  |  |
| 4.0.0 | requirement | Execute new installer to install Mendix Service Console; do not use old ZIP extraction locations. |  |  |
| 4.0.0 | migration-step | Import old apps one by one; all files remain in old locations, settings saved to new location. |  |  |
| 4.0.0 | migration-step | Must reinstall service after confirming app runs successfully with normal start. |  |  |
| 4.0.0 | migration-step | Remove old Mendix Service Console after service reinstall succeeds. | old Mendix Service Console |  |
| 4.0.0 | breaking | Each app now has its own license, even under same user account; old imports limited to first per user. |  |  |
| 4.0.0 | feature | Added possibility to manage all Mendix 3 and 4 apps in one Service Console instance. |  |  |
| 4.0.0 | feature | Ticket 9960, 11133: Each app now has its own license on one machine. |  |  |
| 4.0.0 | breaking | Symbolic link to runtime's mxclientsystem folder always created/updated; checkbox removed. | mxclientsystem |  |
| 4.0.0 | migration-step | Moved settings to Advanced Settings form via Configuration, Advanced. | project path, log path, backup path, custom Mendix settings, Jetty settings |  |
| 4.0.0 | breaking | Two Jetty options configurable by textboxes instead of custom key-value list. | Jetty options |  |
| 4.0.0 | breaking | Changed new default M2EE admin server passwords to 32 character length. | M2EE admin server passwords |  |
| 4.0.0 | breaking | Changed database type choice text 'Oracle 10.2 and later' to 'Oracle 11.2 and later'. | Oracle |  |
| 4.0.0 | breaking | Set SQL Server as default database type. |  |  |
| 3.0.0 | improvement | Improved support for Mendix 4. | Mendix 4 |  |
| 2.2.0 | requirement | Service cannot be uninstalled when service is running. | service |  |
| 2.1.0 | requirement | UAC administrator level now required to prevent UAC requests on service installation/uninstallation. |  |  |
| 2.1.0 | removal | Removed Informix database type as it is no longer supported by Mendix. | Informix database type |  |
| 2.1.0 | breaking | Removed Stop button. Start button changes to Stop after starting the project. | Stop button |  |
| 2.1.0 | migration-step | Moved Service panel content, Project path, and Mendix path to Management panel. | Service panel, Project path, Mendix path |  |
| 2.1.0 | requirement | Application always started under specific service user account; mandatory before project can run. | service user account |  |
| 2.1.0 | breaking | Removed setting for user account type; system accounts like Local System no longer supported. | user account type, system accounts |  |
| 2.1.0 | breaking | Default folder of project path changed from 'Application' to 'Project'. | project path |  |
| 2.1.0 | breaking | Changed PostgreSQL database type option text from '8.2 and later' to '8.3 and later'. | PostgreSQL |  |

## MendixSSO <a id="111349"></a>
Module, Mendix, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/111349)

| version | published | min Mendix |
|---|---|---|
| 10.6.2 | 2026-08-25 | 10.24.0 |
| 10.6.1 | 2026-05-11 | 10.24.0 |
| 10.6.0 | 2026-02-26 | 10.24.0 |
| 10.5.0 | 2025-07-21 | 10.21.0 |
| 10.4.0 | 2025-06-27 | 10.21.0 |
| 10.3.0 | 2025-04-28 | 10.21.0 |
| 10.2.0 | 2025-03-07 | 10.6.15 |
| 10.1.0 | 2025-02-04 | 10.6.15 |
| 10.0.0 | 2024-10-03 | 10.6.15 |
| 9.4.2 | 2026-08-26 | 9.24.0 |
| 9.4.1 | 2026-05-11 | 9.24.0 |
| 9.4.0 | 2025-10-08 | 9.24.0 |
| 9.3.0 | 2025-07-21 | 9.24.0 |
| 9.2.0 | 2025-03-07 | 9.24.0 |
| 9.1.0 | 2025-02-04 | 9.24.0 |
| 9.0.0 | 2024-03-20 | 9.24.0 |
| 4.2.0 | 2023-10-25 | 9.24.0 |
| 4.1.0 | 2023-04-17 | 9.24.0 |
| 4.0.2 | 2023-03-27 | 9.20.0 |
| 4.0.1 | 2023-01-24 | 9.20.0 |
| 4.0.0 | 2023-01-24 | 9.18.3 |
| 3.4.0 | 2025-03-10 | 8.18.28 |
| 3.3.0 | 2025-02-04 | 8.18.28 |
| 3.2.0 | 2024-03-20 | 8.18.28 |
| 3.1.1 | 2022-10-20 | 8.18.11 |
| 3.1.0 | 2022-08-10 | 8.18.11 |
| 3.0.0 | 2021-10-19 | 8.18.11 |
| 2.4.0 | 2021-05-27 | 8.12.5 |
| 2.3.1 | 2021-03-19 | 8.12.5 |
| 2.3.0 | 2020-12-23 | 8.12.5 |
| 2.2.2 | 2020-12-23 | 7.23.19 |
| 2.2.1 | 2020-06-19 | 7.23.3 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 10.6.2 | requirement | Upgraded io.netty:netty-codec-http to 4.2.17.Final and org.apache.httpcomponents.client5:http-client-version to 5.6.3 | io.netty:netty-codec-http, org.apache.httpcomponents.client5:http-client-version |  |
| 10.6.1 | requirement | netty-codec-http library upgraded to version 4.2.12.Final | netty-codec-http |  |
| 10.6.1 | removal | decryptUsingLegacyAlgorithm method removed to improve module security posture | decryptUsingLegacyAlgorithm |  |
| 10.6.1 | improvement | Multi domain platform session support improved |  |  |
| 10.6.0 | requirement | Mendix runtime upgraded to 10.24.0 | Mendix runtime |  |
| 10.6.0 | requirement | Netty codec-http library upgraded to version 4.2.5.Final | netty codec-http |  |
| 10.6.0 | requirement | Apache commons-lang3 library upgraded to version 3.18.0 | Apache commons-lang3 |  |
| 10.6.0 | requirement | Nimbus oauth2-oidc-sdk library upgraded to version 11.28 | Nimbus oauth2-oidc-sdk |  |
| 10.6.0 | requirement | Nimbus nimbus-jose-jwt library upgraded to version 10.4.2 | Nimbus nimbus-jose-jwt |  |
| 10.4.0 | improvement | Deprecated runtime methods replaced to ensure full compatibility with Mendix 11 |  |  |
| 10.3.0 | requirement | Mendix runtime upgraded to 10.21.0 for Mendix 11 support | Mendix runtime |  |
| 10.3.0 | requirement | Apache commons-text library upgraded to version 1.13.1 | Apache commons-text |  |
| 10.3.0 | requirement | Netty codec-http library upgraded to version 4.2.0.Final | Netty codec-http |  |
| 10.2.0 | requirement | Nimbus oauth2-oidc-sdk library upgraded to version 11.23.1 | Nimbus oauth2-oidc-sdk |  |
| 10.1.0 | migration-step | Page URLs support added. Replace login.html with resources/mendixsso/templates/login-with-mendixsso-automatically.html | login.html |  |
| 10.1.0 | requirement | Nimbus oauth2-oidc-sdk library upgraded to version 11.21 | Nimbus oauth2-oidc-sdk |  |
| 10.1.0 | requirement | Nimbus nimbus-jose-jwt library upgraded to version 10.0.1 | Nimbus nimbus-jose-jwt |  |
| 10.1.0 | known-issue | Module contains vulnerable version of nimbus-jose-jwt library. Update to v10.2.0 or higher | Nimbus nimbus-jose-jwt |  |
| 10.0.0 | fix | Stale data cleanup logic refactored and fixed based on Mendix 10 behavioral/structural changes |  |  |
| 10.0.0 | known-issue | Module contains vulnerable version of nimbus-jose-jwt library. Update to v10.2.0 or higher | Nimbus nimbus-jose-jwt |  |
| 9.4.2 | security | Fixed CVE-2026-42584, CVE-2026-42579, CVE-2026-42581 |  |  |
| 9.4.2 | requirement | Upgraded io.netty:netty-codec-http to 4.2.17.Final and org.apache.httpcomponents.client5:http-client-version to 5.6.3 | io.netty:netty-codec-http, org.apache.httpcomponents.client5:http-client-version |  |
| 9.4.1 | requirement | netty-codec-http library upgraded to version 4.2.12.Final | netty-codec-http |  |
| 9.4.1 | removal | decryptUsingLegacyAlgorithm method removed to improve module security posture | decryptUsingLegacyAlgorithm |  |
| 9.4.1 | improvement | Multi domain platform session support improved |  |  |
| 9.4.0 | requirement | Netty codec-http library upgraded to version 4.1.125.Final | Netty codec-http |  |
| 9.4.0 | requirement | Apache commons-lang3 library upgraded to version 3.18.0 | Apache commons-lang3 |  |
| 9.4.0 | requirement | Nimbus oauth2-oidc-sdk library upgraded to version 11.28 | Nimbus oauth2-oidc-sdk |  |
| 9.4.0 | requirement | Nimbus nimbus-jose-jwt library upgraded to version 10.4.2 | Nimbus nimbus-jose-jwt |  |
| 9.2.0 | requirement | Nimbus oauth2-oidc-sdk library upgraded to version 11.23.1 | Nimbus oauth2-oidc-sdk |  |
| 9.1.0 | requirement | Nimbus oauth2-oidc-sdk library upgraded to version 11.21 | Nimbus oauth2-oidc-sdk |  |
| 9.1.0 | requirement | Nimbus nimbus-jose-jwt library upgraded to version 10.0.1 | Nimbus nimbus-jose-jwt |  |
| 9.1.0 | known-issue | Module contains vulnerable version of nimbus-jose-jwt library. Update to v9.2.0 or higher | Nimbus nimbus-jose-jwt |  |
| 9.0.0 | requirement | Nimbus oauth2-oidc-sdk library upgraded to version 11.10.1 | Nimbus oauth2-oidc-sdk |  |
| 9.0.0 | requirement | Nimbus nimbus-jose-jwt library upgraded to version 9.37.3 | Nimbus nimbus-jose-jwt |  |
| 9.0.0 | breaking | Cipher algorithm changed to AES/GCM/NoPadding to support Mendix 10.6.0 or newer |  |  |
| 9.0.0 | known-issue | Module contains vulnerable version of nimbus-jose-jwt library. Update to v9.2.0 or higher | Nimbus nimbus-jose-jwt |  |
| 4.2.0 | breaking | ContinuationURL parameter now validated before redirecting. Custom domains require MendixSSO_AllowedContinuationURLs environment variable | ContinuationURL |  |
| 4.2.0 | breaking | EmailAddress and OpenID removed from UserProfile entity. EmailAddress available as $EmailAddress parameter, OpenID via GetLegacyOpenIDForSSOUser | UserProfile, EmailAddress, OpenID |  |
| 4.2.0 | migration-step | Update customized MendixSSO_CreateUser and MendixSSO_UpdateUser microflows to add $EmailAddress parameter | MendixSSO_CreateUser, MendixSSO_UpdateUser |  |
| 4.2.0 | breaking | User UUID and EmailAddress now parsed from ID token subject and email claims instead of Mendix profile claim |  |  |
| 4.2.0 | migration-step | Internal microflow GetSignupHint renamed to GetDefaultSignupHint | GetSignupHint | GetDefaultSignupHint |
| 4.2.0 | known-issue | Module contains vulnerable version of nimbus-jose-jwt library. Update to v9.0.0 or higher | Nimbus nimbus-jose-jwt |  |
| 4.1.0 | requirement | Solved deprecations to make module Mendix 10 compatible |  |  |
| 4.1.0 | requirement | Nimbus oauth2-oidc-sdk library updated to 10.7.1 including json-smart 2.4.10 | Nimbus oauth2-oidc-sdk |  |
| 4.1.0 | migration-step | Updated pom.xml dependency manager file | pom.xml |  |
| 4.1.0 | known-issue | Module contains vulnerable version of nimbus-jose-jwt library. Update to v9.0.0 or higher | Nimbus nimbus-jose-jwt |  |
| 4.0.2 | security | Solved security concern where regular user role had access to decrypted access tokens via XAS request access rules |  |  |
| 4.0.2 | requirement | Nimbus oauth2-oidc-sdk library upgraded to 10.7 | Nimbus oauth2-oidc-sdk |  |
| 4.0.2 | requirement | json-smart library upgraded to 2.4.10, resolving CVE-2023-1370 | json-smart |  |
| 4.0.2 | known-issue | Module contains vulnerable version of nimbus-jose-jwt library. Update to v9.0.0 or higher | Nimbus nimbus-jose-jwt |  |
| 4.0.1 | requirement | Module upgraded to Mendix version 9.20.0 | Mendix version |  |
| 4.0.1 | improvement | Module prepends __Host parameter to cookie names if app uses HTTPS connection |  |  |
| 4.0.1 | known-issue | Module contains vulnerable version of nimbus-jose-jwt library. Update to v9.0.0 or higher | Nimbus nimbus-jose-jwt |  |
| 4.0.0 | requirement | Module upgraded to Mendix version 9.18.3 | Mendix version |  |
| 4.0.0 | requirement | Nimbus oauth2-oidc-sdk library upgraded to 10.5 | Nimbus oauth2-oidc-sdk |  |
| 4.0.0 | requirement | Nimbus nimbus-jose-jwt library upgraded to 9.24.4 | Nimbus nimbus-jose-jwt |  |
| 4.0.0 | known-issue | Module contains vulnerable version of nimbus-jose-jwt library. Update to v9.0.0 or higher | Nimbus nimbus-jose-jwt |  |
| 3.4.0 | requirement | Nimbus oauth2-oidc-sdk library upgraded to version 11.23.1 | Nimbus oauth2-oidc-sdk |  |
| 3.2.0 | requirement | Nimbus oauth2-oidc-sdk library upgraded to version 11.10.1 | Nimbus oauth2-oidc-sdk |  |
| 3.2.0 | requirement | Nimbus nimbus-jose-jwt library upgraded to version 9.37.3 | Nimbus nimbus-jose-jwt |  |
| 3.1.1 | requirement | Updated commons-text to version 1.10 and commons-lang3 to version 3.12 | commons-text, commons-lang3 |  |
| 3.1.0 | improvement | Updated /userlib/ folder jar libraries, readded utility functions, improved error pages, tightened security rules, bug fixes |  |  |
| 3.0.0 | removal | All UI pages and snippets for displaying OIDC token details were removed. Move them from previous versions before upgrading. | UI pages, snippets |  |
| 3.0.0 | breaking | Updated jar libraries incompatible with previous versions. Clean /userlib/ folder, remove old .jar.MendixSSO.RequiredLib versions, keep only .jar.MendixSSO.3.0.0. | userlib, jar libraries |  |
| 3.0.0 | known-issue | Silent Authentication feature is not compatible with the Deeplink module. | Silent Authentication, Deeplink module |  |
| 2.4.0 | requirement | Made module compatible with Mendix 9.1.1. | Mendix |  |
| 2.3.0 | requirement | Converted to Mendix 8.12.5. | Mendix |  |
| 2.3.0 | fix | Fixed deprecated Core.execute() calls in Java logic for Mendix 9 compatibility. | Core.execute() |  |
| 2.2.2 | requirement | Converted to Mendix 7.23.19. | Mendix |  |
| 2.2.2 | improvement | Updated commons-text and oauth2-oidc-sdk module libraries and sub-dependencies. | commons-text, oauth2-oidc-sdk |  |
| 2.2.2 | migration-step | Updated NotifyRolesChanged API published location to avoid conflict with old REST module implementation. | NotifyRolesChanged API |  |
| 2.2.1 | breaking | DS_GetForeignIdentity microflow now accepts generic System.User object as input. | DS_GetForeignIdentity |  |
| 2.2.1 | breaking | Renamed GetOpenIDForSSOUser microflow to GetLegacyOpenIDForSSOUser. | GetOpenIDForSSOUser | GetLegacyOpenIDForSSOUser |
| 2.2.1 | improvement | Refactored some microflows in Identity Propagation default implementation for consistency between REST and oData. | Identity Propagation |  |
| 2.2.1 | known-issue | Deprecated Rest Services module is incompatible with MendixSSO 2.2.0+. | Rest Services module |  |

## Menu Helper <a id="106253"></a>
Widget, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/106253)

| version | published | min Mendix |
|---|---|---|
| 2.0.0 | 2021-12-16 | 9.5.0 |
| 1.0.0 | 2021-12-15 | 8.18.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.0.0 | requirement | Minimum Mendix version changed to 9.5.0. Mendix menu widgets became pluggable/react-based. |  |  |
| 2.0.0 | breaking | Old code no longer works. Menu Helper rewritten as pluggable widget for Mendix 9.5+. |  |  |

## Microflow Scheduled Event Manager <a id="1750"></a>
Module, Mendix, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/1750)

| version | published | min Mendix |
|---|---|---|
| 1.6.1 | 2024-10-24 | 9.0.5 |
| 1.6.0 | 2021-07-20 | 9.0.5 |
| 1.5.0 | 2021-07-20 | 8.12.7 |
| 1.4.0 | 2019-11-18 | 7.3.0 |
| 1.3.1 | 2019-11-18 | 7.3.0 |
| 1.3.0 | 2019-04-09 | 7.3.0 |
| 1.2.0 | 2018-02-14 | 7.3.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.6.1 | security | Upgraded quartz library and dependencies to address all known CVEs. | quartz |  |
| 1.6.0 | requirement | Minimum Mendix version requirement: 9.0.5 |  |  |
| 1.5.0 | requirement | Minimum Mendix version requirement: 8.12.7 |  |  |
| 1.4.0 | requirement | Model upgraded to 8.3.0 |  |  |
| 1.3.1 | improvement | Userlib upgraded to same version as used in other common modules. | userlib |  |
| 1.3.1 | requirement | Modeler upgraded to 7.16 to prevent annoying issues when downloading module. |  |  |
| 1.3.1 | improvement | Improved model UI components for improved Atlas UI compatibility. |  |  |
| 1.3.0 | improvement | Userlib upgraded to same version as used in other common modules. | userlib |  |
| 1.3.0 | requirement | Modeler upgraded to 7.16 to prevent annoying issues when downloading module. |  |  |

## Microflow Timer <a id="27"></a>
Widget, Mendix, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/27)

| version | published | min Mendix |
|---|---|---|
| 4.0.4 | 2023-05-30 | 7.13.1 |
| 4.0.3 | 2021-06-29 | 7.13.1 |
| 4.0.2 | 2019-12-20 | 7.13.1 |
| 4.0.1 | 2019-01-02 | 7.13.1 |
| 4.0.0 | 2018-08-15 | 7.13.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 4.0.2 | improvement | Removed popup UI error messages when server is offline; errors logged to console only. |  |  |

## MicroflowUtils <a id="202355"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/202355)

| version | published | min Mendix |
|---|---|---|
| 2.0.0 | 2022-09-07 | 8.18.18 |
| 1.0.0 | 2022-09-07 | 7.23.31 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.0.0 | requirement | Minimum Mendix version upgraded to 8.18.18 | Mendix |  |

## Microsoft Sharepoint <a id="119305"></a>
Module, Siemens, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/119305)

| version | published | min Mendix |
|---|---|---|
| 1.1.0 | 2024-04-03 | 9.24.0 |
| 1.0.0 | 2021-12-30 | 8.12.7 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.1.0 | requirement | Minimum Mendix version raised to 9.24.0 |  |  |

## Microsoft sharepoint connector   <a id="257451"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/257451)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2026-03-13 | 10.24.2 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.0.0 | requirement | Requires Mendix 10.24.2 or higher. |  |  |

## Mistral Connector <a id="248276"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/248276)

| version | published | min Mendix |
|---|---|---|
| 2.1.0 | 2026-08-07 | 11.12.2 |
| 2.0.0 | 2026-07-02 | 11.12.0 |
| 1.0.0 | 2025-10-30 | 10.24.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.1.0 | requirement | Upgrade to Mendix 11.12.2 or later. |  |  |
| 2.0.0 | requirement | Module upgraded to Mendix 11.12.0. |  |  |

## Mobile Device <a id="65139"></a>
Widget, Mendix, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/65139)

| version | published | min Mendix |
|---|---|---|
| 1.1.0 | 2019-01-03 | 7.13.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.1.0 | fix | Widget not working with empty data sources |  |  |
| 1.1.0 | fix | Widget not working with empty context |  |  |

## Mobile features <a id="48902"></a>
Widget, Mendix, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/48902)

| version | published | min Mendix |
|---|---|---|
| 1.5.0 | 2019-10-04 | 7.0.2 |
| 1.4.3 | 2019-06-27 | 7.0.2 |
| 1.4.2 | 2019-06-03 | 7.0.2 |
| 1.4.1 | 2019-02-13 | 7.0.2 |
| 1.4.0 | 2019-02-13 | 7.0.2 |
| 1.3.5 | 2018-04-20 | 7.0.2 |
| 1.3.4 | 2018-04-19 | 7.0.2 |
| 1.3.3 | 2018-03-02 | 7.0.2 |
| 1.3.2 | 2017-10-05 | 7.0.2 |
| 1.3.1 | 2017-10-03 | 7.0.2 |
| 1.3.0 | 2017-09-22 | 7.0.2 |
| 1.2.1 | 2017-09-21 | 7.0.2 |
| 1.2.0 | 2017-07-17 | 7.0.2 |
| 1.1 | 2017-04-25 | 7.0.2 |
| 1.0 | 2017-04-14 | 7.0.2 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.4.2 | improvement | Improved online/offline detection (Support Tickets #80756, #80369). | online/offline detection |  |

## Mobile SSO <a id="223516"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/223516)

| version | published | min Mendix |
|---|---|---|
| 2.3.0 | 2026-06-11 | 10.24.0 |
| 2.2.0 | 2026-03-25 | 10.24.0 |
| 2.1.1 | 2026-02-09 | 10.12.10 |
| 2.1.0 | 2024-09-18 | 10.12.3 |
| 2.0.0 | 2024-04-23 | 10.9.0 |
| 1.1.0 | 2024-09-18 | 9.24.2 |
| 1.0.1 | 2024-04-23 | 9.24.2 |
| 1.0.0 | 2024-03-04 | 9.24.2 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.3.0 | requirement | Updated for compatibility with v4.5.0 of the OIDC SSO module | OIDC SSO |  |
| 2.2.0 | requirement | Upgraded core to Mx10.24.0 | Mendix |  |
| 2.2.0 | requirement | OIDC SSO compatibility ensured for version 4.3.0 and above | OIDC SSO |  |
| 2.2.0 | requirement | Compatibility with Mx11 versions (Ticket #272846) | Mendix |  |
| 2.2.0 | fix | Fixed the Sub-path issue (Ticket #265448) |  |  |
| 2.2.0 | fix | Resolved an iOS network connectivity issue (Ticket #261565) |  |  |
| 2.1.1 | requirement | Ensure Compatibility with OIDC SSO Version 4.0.0 and Above | OIDC SSO |  |
| 2.1.1 | requirement | Upgraded to Mx10.12.10 | Mendix |  |
| 2.1.0 | requirement | Ensure Compatibility with OIDC SSO Version 3.0.0 and Above (Ticket#227495, Ticket#226013) | OIDC SSO |  |
| 2.1.0 | requirement | Upgraded to Mx10.12.3 | Mendix |  |
| 2.0.0 | requirement | Supports Mendix 10.9 and above | Mendix |  |
| 1.1.0 | requirement | Ensure Compatibility with OIDC SSO Version 3.0.0 and Above (Ticket#227495, Ticket#226013) | OIDC SSO |  |

## Model Creator For SAP Integrations <a id="119968"></a>
Service, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/119968)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2022-03-28 | 8.18.10 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.0.0 | feature | New module replacing OData Model Creator for SAP Solutions with added support for creating BAPI models. | Model Creator for SAP Integration | Model Creator for SAP Integration |
| 1.0.0 | requirement | Minimum Mendix version requirement: 8.18.10 | Mendix |  |

## Model Quality Tool <a id="120207"></a>
Solution, Conclusion Low Code Company, Partner, [marketplace](https://marketplace.mendix.com/link/component/120207)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2022-07-29 | ? |

## MQTT Connector <a id="119508"></a>
Service, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/119508)

| version | published | min Mendix |
|---|---|---|
| 3.0.1 | 2026-09-15 | 10.24.11 |
| 3.0.0 | 2026-08-18 | 10.24.11 |
| 2.2.1 | 2026-05-21 | 10.24.11 |
| 2.2.0 | 2025-12-15 | 10.24.11 |
| 2.1.1 | 2025-10-08 | 10.21.0 |
| 2.1.0 | 2025-04-25 | 10.21.0 |
| 2.0.0 | 2025-01-22 | 10.12.10 |
| 1.7.2 | 2026-05-21 | 9.24.11 |
| 1.7.1 | 2025-12-15 | 9.24.11 |
| 1.7.0 | 2024-05-27 | 9.24.11 |
| 1.6.0 | 2023-11-10 | 9.24.11 |
| 1.5.0 | 2023-10-25 | 9.24.9 |
| 1.4.0 | 2023-09-26 | 9.18.4 |
| 1.3.0 | 2023-04-05 | 9.18.4 |
| 1.2.0 | 2022-10-13 | 9.1.1 |
| 1.1.1 | 2022-09-06 | 9.1.1 |
| 1.1.0 | 2022-05-02 | 9.1.1 |
| 1.0.0 | 2022-01-24 | 9.1.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 3.0.1 | improvement | Updated MQTT Connector userlib jars | userlib jars |  |
| 3.0.0 | breaking | Upgraded MQTT client from Eclipse Paho v3 to v5 | Eclipse Paho MQTT client |  |
| 3.0.0 | improvement | Upgraded BouncyCastle jar to v1.85 | BouncyCastle jar |  |
| 2.2.1 | improvement | Upgraded bouncy castle jar to v1.84 | bouncy castle jar |  |
| 2.2.1 | improvement | Removed TLSv1.2 constraint from MQTT | MQTT |  |
| 2.2.0 | requirement | Upgraded module to Studio Pro version 10.24.11 | Studio Pro |  |
| 2.2.0 | improvement | Upgraded data widget to latest available version | data widget |  |
| 2.1.1 | fix | Fixed event tracking library missing error (#255814), delete eventTrackingLibrary*.jar from userlib | eventTrackingLibrary jar |  |
| 2.1.1 | improvement | Upgraded bouncycastle jar to v1.81 | bouncycastle jar |  |
| 2.1.0 | requirement | Updated studio pro minimum version to 10.21.0 to support Mendix 11 | Studio Pro |  |
| 2.1.0 | improvement | Upgraded 3rd party jars and widgets | 3rd party jars, widgets |  |
| 2.0.0 | requirement | Upgraded the module to Mendix version 10.12.10 | Mendix |  |
| 2.0.0 | breaking | Replaced old UI components with new ones compatible with the React Client | UI components |  |
| 2.0.0 | improvement | Upgraded the Combobox widget to version 2.1.3 | Combobox widget |  |
| 2.0.0 | improvement | Upgraded Data Widgets to version 2.29.0 | Data Widgets |  |
| 1.7.2 | improvement | Upgraded bouncy castle jar to v1.84 | bouncy castle jar |  |
| 1.7.2 | improvement | Removed TLSv1.2 constraint from MQTT | MQTT |  |
| 1.7.1 | improvement | Upgraded bouncycastle to 1.81 along with some other test dependencies | bouncycastle jar |  |
| 1.7.1 | improvement | Upgraded Switch widget to latest available version | Switch widget |  |
| 1.6.0 | requirement | Upgraded module to Mendix version 9.24.11 | Mendix |  |
| 1.5.0 | requirement | Upgraded module to Mendix version 9.24.9 | Mendix |  |
| 1.4.0 | migration-step | Introduction of migration file for JDM | JDM |  |
| 1.3.0 | requirement | Updated module to Mendix version 9.18.4 | Mendix |  |
| 1.1.1 | migration-step | Before updating delete MqttConnector-1.0.0-all.jar file from userlib folder | MqttConnector-1.0.0-all.jar |  |
| 1.1.1 | improvement | Upgraded Bouncy Castle jars to 1.70 | Bouncy Castle jars |  |

## MUI Avatar Group <a id="219410"></a>
Widget, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/219410)

| version | published | min Mendix |
|---|---|---|
| 1.3.0 | 2026-06-26 | 10.24.0 |
| 1.2.0 | 2024-04-25 | 9.24.2 |
| 1.1.0 | 2023-11-28 | 9.24.2 |
| 1.0.0 | 2023-11-28 | 9.24.2 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.3.0 | feature | New pluggable widget upgrade |  |  |
| 1.3.0 | security | Vulnerability fixes |  |  |
| 1.3.0 | feature | React client support |  |  |
| 1.2.0 | breaking | Removed percentage sizing |  |  |

## Multi-factor Authentication For Mendix (MFA/2FA) <a id="116892"></a>
Module, Emixa, Community, [marketplace](https://marketplace.mendix.com/link/component/116892)

| version | published | min Mendix |
|---|---|---|
| 7.0.0 | 2026-08-06 | 11.12.1 |
| 6.0.0 | 2026-01-23 | 11.6.2 |
| 5.1.0 | 2026-08-06 | 11.6.2 |
| 5.0.0 | 2025-12-24 | 9.24.0 |
| 4.0.0 | 2025-07-08 | 9.24.0 |
| 3.1.1 | 2025-01-09 | 9.18.6 |
| 3.1.0 | 2025-01-08 | 9.18.6 |
| 3.0.0 | 2023-09-06 | 9.18.4 |
| 2.1.0 | 2023-09-06 | 8.18.8 |
| 2.0.0 | 2022-12-29 | 8.18.8 |
| 1.5.0 | 2021-12-24 | 8.18.8 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 7.0.0 | requirement | Minimum Mendix version raised to 11.12.1 | Mendix |  |
| 6.0.0 | requirement | Minimum Mendix version raised to 11.6.2 for Mendix 11 compatibility | Mendix |  |
| 6.0.0 | breaking | Several Java actions changed | Java actions |  |
| 5.0.0 | requirement | Minimum Mendix version raised to 9.24.0 | Mendix |  |
| 4.0.0 | breaking | Module architecture redesigned. Configure required microflows via ASU_SetMicroflows and ASU_v2 in after startup | ASU_SetMicroflows, ASU_v2 |  |
| 3.1.0 | security | Security fix for After startup: Access rights removed | After startup |  |
| 3.1.0 | migration-step | Check changed microflows SUB_MFA_CreateCode, SUB_MFA_UserDisabledCheck, SUB_MFA_ValidateCode to avoid startup errors | SUB_MFA_CreateCode, SUB_MFA_UserDisabledCheck, SUB_MFA_ValidateCode |  |
| 2.0.0 | breaking | Removed capability to use MFA from login.html due to complexity | login.html |  |
| 2.0.0 | migration-step | Remove MFA directory from resources directory | MFA directory |  |
| 2.0.0 | fix | BlockSince attribute on User entity fixed for Mendix 9 compatibility | BlockSince |  |

## Mx Model Reflection <a id="69"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/69)

| version | published | min Mendix |
|---|---|---|
| 9.1.0 | 2026-01-21 | 10.24.0 |
| 9.0.1 | 2025-04-30 | 10.21.0 |
| 9.0.0 | 2025-04-17 | 10.21.0 |
| 8.0.4 | 2025-04-03 | 9.24.24 |
| 8.0.3 | 2024-12-03 | 9.24.24 |
| 8.0.2 | 2024-07-18 | 9.24.11 |
| 7.1.1 | 2024-03-14 | 9.18.0 |
| 7.1.0 | 2024-03-08 | 9.18.0 |
| 7.0.0 | 2023-04-19 | 9.18.0 |
| 6.2.0 | 2020-12-17 | 8.12.0 |
| 6.1.2 | 2020-03-03 | 7.23.0 |
| 6.1.1 | 2019-11-25 | 7.23.0 |
| 6.1.0 | 2019-10-29 | 7.23.0 |
| 6.0.0 | 2019-06-12 | 7.23.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 9.1.0 | requirement | Minimum Mendix version upgraded to 10.24.0 |  |  |
| 9.1.0 | removal | Removed deprecated pages |  |  |
| 9.0.0 | requirement | Upgraded to Mendix version 10.21.0 |  |  |
| 9.0.0 | removal | Removed deprecated pages |  |  |
| 8.0.3 | requirement | Upgraded Mendix version to 9.24.24 |  |  |
| 8.0.3 | improvement | Replaced old UI components with new ones supporting React Client |  |  |
| 8.0.3 | breaking | Layouts from Atlas used instead of custom ones; popup windows now modal |  |  |
| 8.0.3 | migration-step | Select pages not React compatible; manually remove if React Client enabled |  |  |
| 8.0.3 | breaking | Configured cascade delete; MxObjectEnumValue deleted when MxObjectEnum deleted | MxObjectEnumValue, MxObjectEnum |  |
| 8.0.3 | removal | Removed support for deprecated Float and Currency types | Float, Currency |  |
| 8.0.2 | requirement | Upgraded Mendix version to 9.24.11 |  |  |
| 8.0.2 | improvement | Replaced old UI components with new ones supporting React Client |  |  |
| 7.1.1 | fix | TokenReplacer now supports System.owner and System.changedBy associations correctly. (Ticket 202682) | TokenReplacer, System.owner, System.changedBy |  |
| 7.1.1 | fix | TokenReplacer handles many-to-many associations by taking the first object | TokenReplacer |  |
| 7.1.1 | fix | Fixed issue where IVK_RecalculateSize caused issues building native app. (Ticket 204735, 207239) | IVK_RecalculateSize |  |
| 7.1.0 | fix | Handle non-localized datetimes correctly |  |  |
| 7.0.0 | requirement | Updated to Studio Pro 9.18; usable in Studio Pro 10 |  |  |
| 6.2.0 | requirement | Upgraded to Studio Pro version 8.12.0 |  |  |
| 6.1.2 | fix | Fixed IVK_RecalculateSize to correctly set CalculatedSizeInKiloBytes field. (Ticket 95995) | IVK_RecalculateSize, CalculatedSizeInKiloBytes |  |
| 6.1.1 | fix | Syncing correctly cleans up enum values and captions. Unused values/captions not auto-deleted; manually delete via microflow. (Ticket #63310) | MxObjectEnumValue, MxObjectEnumCaption |  |
| 6.1.0 | improvement | FindMember, FindMicroflow, FindObjectType, FindReference return exact matches first. (Ticket #90020) | FindMember, FindMicroflow, FindObjectType, FindReference |  |
| 6.0.0 | requirement | Updated to Mendix 7.23; also usable in Mendix 8 |  |  |
| 6.0.0 | removal | Support for deprecated Float and Currency types dropped | Float, Currency |  |

## MxValidator <a id="210472"></a>
Module, Blackbelt Technology, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/210472)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2023-05-09 | 9.24.0 |

## MxWebhookSignatureValidation <a id="210319"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/210319)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2023-04-28 | 9.24.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.0.0 | requirement | Minimum Mendix version 9.24.0 required | Mendix |  |

## Nanoflow Commons <a id="109515"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/109515)

| version | published | min Mendix |
|---|---|---|
| 7.4.0 | 2026-09-22 | 11.12.3 |
| 7.3.0 | 2026-09-02 | 11.12.3 |
| 7.2.1 | 2026-07-22 | 11.12.0 |
| 7.2.0 | 2026-07-03 | 11.11.0 |
| 7.1.0 | 2026-06-05 | 11.11.0 |
| 7.0.0 | 2026-05-12 | 11.10.0 |
| 6.3.1 | 2026-03-05 | 11.7.0 |
| 6.3.0 | 2026-02-18 | 11.7.0 |
| 6.2.3 | 2026-09-02 | 11.6.0 |
| 6.2.2 | 2026-03-05 | 11.6.0 |
| 6.2.1 | 2026-02-18 | 11.3.0 |
| 6.2.0 | 2025-12-15 | 11.3.0 |
| 6.1.2 | 2025-11-18 | 11.3.0 |
| 6.1.1 | 2025-10-07 | 11.3.0 |
| 5.2.1 | 2026-03-04 | 10.24.0 |
| 5.2.0 | 2026-02-18 | 10.24.0 |
| 5.1.6 | 2025-12-05 | 10.24.0 |
| 5.1.5 | 2025-12-02 | 10.24.0 |
| 5.1.4 | 2025-11-18 | 10.24.0 |
| 5.1.3 | 2025-09-24 | 10.24.0 |
| 5.1.2 | 2025-03-27 | 10.17.0 |
| 5.0.0 | 2024-12-03 | 10.17.0 |
| 4.0.4 | 2024-08-30 | 10.6.5 |
| 4.0.3 | 2024-03-19 | 10.6.5 |
| 4.0.2 | 2024-01-17 | 10.0.0 |
| 4.0.1 | 2023-10-13 | 10.0.0 |
| 4.0.0 | 2023-06-09 | 10.0.0 |
| 3.0.2 | 2024-01-17 | 9.24.1 |
| 3.0.1 | 2023-10-13 | 9.24.1 |
| 3.0.0 | 2023-03-28 | 9.24.0 |
| 2.6.1 | 2022-09-23 | 9.10.0 |
| 2.6.0 | 2022-08-31 | 9.10.0 |
| 2.5.0 | 2022-07-25 | 9.10.0 |
| 2.4.0 | 2022-06-28 | 9.10.0 |
| 2.3.1 | 2022-03-22 | 9.10.0 |
| 2.3.0 | 2022-03-09 | 9.10.0 |
| 2.2.0 | 2022-02-21 | 9.10.0 |
| 2.1.2 | 2021-10-25 | 9.6.0 |
| 2.1.0 | 2021-09-28 | 9.6.0 |
| 2.0.1 | 2021-04-02 | 9.0.5 |
| … 9 older versions | | |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 7.4.0 | migration-step | Migrated geolocation actions from @react-native-community/geolocation to react-native-nitro-geolocation. | geolocation actions, react-native-community/geolocation, react-native-nitro-geolocation |  |
| 7.3.0 | fix | Removed visible changes in NC and NMR modules during first build of app. | NC module, NMR module |  |
| 7.2.0 | improvement | Close offline database connection before navigating between pages with OpenURL nanoflow action. | offline database connection, OpenURL nanoflow action |  |
| 7.1.0 | requirement | Updated react-native from version 0.83.4 to 0.84.1. | react-native |  |
| 7.0.0 | requirement | Updated @react-native-async-storage/async-storage from version v2.0.0 to v2.2.0. | @react-native-async-storage/async-storage |  |
| 7.0.0 | requirement | Updated react-native-permissions from version v5.4.2 to v5.5.1. | react-native-permissions |  |
| 6.3.1 | fix | Fixed synchronization issue with Base64 images generated by Signature widget. | Base64 images, Signature widget |  |
| 6.3.0 | breaking | Changed caption for existing 'Download file' action to 'Download native file'. | Download file action |  |
| 6.2.3 | fix | Removed visible changes in NC and NMR modules during first build of app. | NC module, NMR module |  |
| 6.2.2 | fix | Fixed synchronization issue with Base64 images generated by Signature widget. | Base64 images, Signature widget |  |
| 6.2.1 | migration-step | Migrated from @react-native-community/geolocation to react-native-permissions for handling location permissions. | @react-native-community/geolocation, react-native-permissions |  |
| 6.2.0 | requirement | Release compatible with Studio Pro 11.3.0 and above. | Studio Pro |  |
| 6.1.2 | requirement | Updated react-native-firebase to v20.1.0. Ensure Native Template and Native Builder are updated accordingly. | react-native-firebase, Native Template, Native Builder |  |
| 6.1.1 | fix | Fixed location permission issue on iOS. | location permission, iOS |  |
| 6.1.1 | fix | Fixed isConnectedToServer succeeding without internet on offline apps when service worker is enabled. | isConnectedToServer, offline apps, service worker |  |
| 6.1.1 | requirement | Updated minimum Mendix version to 10.21. | Mendix |  |
| 5.2.1 | fix | Fixed issue where Android devices had difficulty obtaining precise location data with @react-native-community/geolocation. | @react-native-community/geolocation, Android |  |
| 5.2.1 | fix | Fixed synchronization issue with Base64 images generated by Signature widget. | Base64 images, Signature widget |  |
| 5.2.0 | migration-step | Migrated from @react-native-community/geolocation to react-native-permissions for handling location permissions. | @react-native-community/geolocation, react-native-permissions |  |
| 5.1.5 | fix | Fixed isConnectedToServer succeeding without internet on offline apps when service worker is enabled. | isConnectedToServer, offline apps, service worker |  |
| 5.1.4 | requirement | Updated react-native-firebase to v20.1.0. Ensure Native Template and Native Builder are updated accordingly. | react-native-firebase, Native Template, Native Builder |  |
| 5.1.3 | fix | Fixed location permission issue on iOS. | location permission, iOS |  |
| 5.1.3 | requirement | Updated minimum Mendix version to 10.21. | Mendix |  |
| 5.1.2 | requirement | Updated @react-native-community/geolocation to version 3.4.0 to resolve location-related issues. | @react-native-community/geolocation |  |
| 5.0.0 | requirement | Updated @mendix/pluggable-widgets-tools from version v9.0.0 to v10.0.1. | @mendix/pluggable-widgets-tools |  |
| 5.0.0 | breaking | Updated react-native from version 0.73.8 to 0.75.4. | react-native |  |
| 5.0.0 | breaking | Updated react-native-device-info from version v11.1.0 to v13.0.0. | react-native-device-info |  |
| 5.0.0 | breaking | Updated react-native-localize from version v1.4.2 to v3.2.1. | react-native-localize |  |
| 4.0.2 | removal | Removed constant holding version number from within module. | version number constant |  |
| 3.0.2 | removal | Removed constant holding version number from within module. | version number constant |  |
| 3.0.1 | requirement | Minimum Mendix version set to 9.24.1. | Mendix |  |
| 3.0.0 | breaking | Made module compatible with React Native 0.70.7. | React Native |  |
| 2.6.0 | removal | Removed SetCookie, ReadCookie, SetFavicon actions (available in Web Actions module). | SetCookie, ReadCookie, SetFavicon |  |
| 2.6.0 | removal | Removed ScrollToClass, AddMilliseconds, AddTime actions. | ScrollToClass, AddMilliseconds, AddTime |  |
| 2.6.0 | breaking | 'Is connected' action renamed to 'Is connected to server'. | Is connected action | Is connected to server |
| 2.6.0 | breaking | Parameter names changed for Base64Decode, Base64DecodeToImage, Base64Encode, GetStraightLineDistance actions. | Base64Decode, Base64DecodeToImage, Base64Encode, GetStraightLineDistance |  |
| 2.4.0 | breaking | Action would only be compatible with Mendix client or above. | Mendix client |  |
| 2.3.0 | fix | Fixed timeout error while getting current location. | current location |  |
| 2.3.0 | fix | Fixed timeout issue while getting current location with minimum accuracy. | current location, minimum accuracy |  |
| 2.3.0 | breaking | Changed location library from android.location API to Google Location Services API. Use action before using location actions. | iOS, location API |  |
| 2.3.0 | known-issue | Get current location with minimum accuracy: disable nanoflow during action execution for good user experience. | Get current location, minimum accuracy |  |
| 2.2.0 | fix | Fixed bug where variable was not being defined while using action. | variable definition |  |
| 2.1.2 | fix | Fixed problem with toggle sidebar action when executed in Native apps. | toggle sidebar action, Native apps |  |
| 2.0.0 | feature | New native dependency management system. Libraries packaged with dependencies allowing custom dependency additions. | native dependency management, library dependencies |  |
| 2.0.0 | fix | Library updates and security fixes. | libraries, security |  |
| 1.1.0 | requirement | Updated JS Actions to be compatible with React Native 0.61. | React Native |  |
| 1.0.2 | breaking | JSActions now exported as 'nothing' instead of boolean. | JSActions |  |
| 1.0.0 | fix | Fixed LocalStorage actions. | LocalStorage actions |  |

## Native Mobile Resources <a id="109513"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/109513)

| version | published | min Mendix |
|---|---|---|
| 12.5.0 | 2026-09-24 | 11.12.3 |
| 12.4.0 | 2026-09-02 | 11.12.3 |
| 12.3.0 | 2026-08-06 | 11.12.0 |
| 12.2.2 | 2026-07-21 | 11.12.0 |
| 12.2.1 | 2026-07-17 | 11.11.0 |
| 12.2.0 | 2026-07-03 | 11.11.0 |
| 12.1.0 | 2026-06-10 | 11.11.0 |
| 12.0.1 | 2026-06-01 | 11.10.0 |
| 12.0.0 | 2026-05-15 | 11.10.0 |
| 11.4.2 | 2026-05-28 | 11.7.0 |
| 11.4.1 | 2026-03-14 | 11.7.0 |
| 11.4.0 | 2026-03-05 | 11.7.0 |
| 11.3.13 | 2026-09-24 | 11.6.0 |
| 11.3.12 | 2026-09-02 | 11.6.0 |
| 11.3.11 | 2026-08-05 | 11.6.0 |
| 11.3.10 | 2026-07-02 | 11.6.0 |
| 11.3.9 | 2026-06-02 | 11.6.0 |
| 11.3.8 | 2026-05-28 | 11.6.0 |
| 11.3.7 | 2026-03-14 | 11.6.0 |
| 11.3.6 | 2026-03-05 | 11.6.0 |
| 11.3.5 | 2026-02-17 | 11.7.0 |
| 11.3.4 | 2026-02-17 | 11.3.0 |
| 11.3.3 | 2026-01-20 | 11.3.0 |
| 11.3.2 | 2025-12-23 | 11.3.0 |
| 11.3.1 | 2025-12-15 | 11.3.0 |
| 11.3.0 | 2025-12-15 | 11.3.0 |
| 11.2.1 | 2025-11-07 | 11.3.0 |
| 11.2.0 | 2025-10-17 | 11.3.0 |
| 11.1.1 | 2025-10-07 | 11.3.0 |
| 11.1.0 | 2025-10-02 | 11.3.0 |
| 11.0.3 | 2025-08-21 | 11.0.0 |
| 11.0.2 | 2025-08-11 | 11.0.0 |
| 11.0.0 | 2025-07-07 | 11.0.0 |
| 10.1.17 | 2026-05-12 | 10.24.0 |
| 10.1.16 | 2026-03-14 | 10.24.0 |
| 10.1.15 | 2026-03-04 | 10.24.0 |
| 10.1.14 | 2026-02-18 | 10.24.0 |
| 10.1.13 | 2026-01-20 | 10.24.0 |
| 10.1.11 | 2025-12-19 | 10.24.0 |
| 10.1.10 | 2025-12-11 | 10.24.0 |
| … 124 older versions | | |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 12.5.0 | breaking | Removed react-native-linear-gradient library in favor of react-native View with linear-gradient type background. | BackgroundGradient, react-native-linear-gradient |  |
| 12.5.0 | feature | Added On change event that triggers when Trigger attribute value changes, allowing detection of bottom sheet dismissal. | BottomSheet |  |
| 12.5.0 | breaking | Replaced deprecated prop containerHeight with containerLayoutState option. | BottomSheet, containerHeight | containerLayoutState |
| 12.5.0 | feature | Added direct image upload to System.Image object using type image with allowUpload set to true. | Signature, System.Image |  |
| 12.5.0 | breaking | Renamed onSave action to onSignEnd to match web signature widget naming convention. | Signature, onSave | onSignEnd |
| 12.4.0 | improvement | Updated react-native-animatable to 1.4.0. | Animation, react-native-animatable |  |
| 12.4.0 | improvement | Updated victory-native to 36.9.2. | BarChart, victory-native |  |
| 12.4.0 | improvement | Updated deprecated-react-native-prop-types to 4.2.3. | Carousel, deprecated-react-native-prop-types |  |
| 12.4.0 | improvement | Pinned react-native-snap-carousel to 3.9.1. | Carousel, react-native-snap-carousel |  |
| 12.4.0 | improvement | Pinned react-native-color to 0.0.10. | ColorPicker, react-native-color |  |
| 12.4.0 | improvement | Pinned react-native-slider to 0.11.0. | ColorPicker, react-native-slider |  |
| 12.4.0 | improvement | Updated tinycolor2 to 1.6.0. | ColorPicker, tinycolor2 |  |
| 12.4.0 | improvement | Pinned querystringify to 2.2.0. | Feedback, querystringify |  |
| 12.4.0 | breaking | Removed react-native-reanimated library and used Animated API of react native for animation. | FloatingActionButton, react-native-reanimated |  |
| 12.4.0 | improvement | Pinned prop-types to 15.8.1. | Maps, prop-types |  |
| 12.4.0 | improvement | Pinned react-native-material-menu to 1.2.0. | PopupMenu, react-native-material-menu |  |
| 12.4.0 | improvement | Pinned react-native-progress to 5.0.1. | ProgressBar, react-native-progress |  |
| 12.4.0 | improvement | Pinned @miblanchard/react-native-slider to 2.6.0. | RangeSlider, @miblanchard/react-native-slider |  |
| 12.4.0 | breaking | Removed @react-native-vector-icons/common and @react-native-vector-icons/get-image dependencies. | Rating, @react-native-vector-icons/common, @react-native-vector-icons/get-image |  |
| 12.4.0 | improvement | Added react-native-svg dependency and fixed rating icons not visible if user sets empty and selected star as none. | Rating, react-native-svg |  |
| 12.4.0 | improvement | Updated react-native-segmented-control-tab to 3.4.1. | ToggleButtons, react-native-segmented-control-tab |  |
| 12.3.0 | breaking | Replaced @notifee/react-native with react-native-notify-kit library. | @notifee/react-native, react-native-notify-kit | react-native-notify-kit |
| 12.3.0 | feature | Added support for QR of available remaining types including pdf417 in barcode scanner functionality. | BarcodeScanner |  |
| 12.2.1 | breaking | Switched to new sound library for Play sound action to support react-native 0.84+. | Play sound action |  |
| 12.2.1 | improvement | Play sound action now plays audio from online documents on Android by downloading to version-based cache. | Play sound action |  |
| 12.1.0 | requirement | Updated react-native from version 0.83.4 to 0.84.1. | react-native |  |
| 12.1.0 | improvement | Updated @sbaiahmed1/react-native-biometrics from version v0.10.0 to v0.15.0. | @sbaiahmed1/react-native-biometrics |  |
| 12.1.0 | improvement | Updated react-native-gesture-handler from version v2.30.0 to v2.31.2. | BottomSheet, react-native-gesture-handler |  |
| 12.1.0 | improvement | Updated react-native-reanimated from version v4.2.2 to v4.3.1. | BottomSheet, react-native-reanimated |  |
| 12.1.0 | improvement | Updated react-native-worklets from version v0.7.4 to v0.8.3. | BottomSheet, react-native-worklets |  |
| 12.1.0 | improvement | Updated @gorhom/bottom-sheet from version v5.2.8 to v5.2.14. | BottomSheet, @gorhom/bottom-sheet |  |
| 12.1.0 | improvement | Updated @shopify/flash-list from version v2.2.2 to v2.3.1. | BottomSheet, @shopify/flash-list |  |
| 12.1.0 | improvement | Updated react-native-view-shot from version v4.0.3 to 5.1.0. | Feedback, react-native-view-shot |  |
| 12.1.0 | breaking | Replaced react-native-action-button library with custom implementation using React Native Animated API. | FloatingActionButton, react-native-action-button |  |
| 12.1.0 | removal | Removed deprecated react-native-prop-types dependency. | FloatingActionButton, react-native-prop-types |  |
| 12.1.0 | improvement | Updated react-native-svg from version v15.15.3 to v15.15.4. | GalleryTextFilter, react-native-svg |  |
| 12.1.0 | improvement | Updated @react-native-vector-icons/common from version v12.4.0 to v12.4.2. | Image, @react-native-vector-icons/common |  |
| 12.1.0 | improvement | Updated react-native-video from version v6.19.0 to v6.19.2. | VideoPlayer, react-native-video |  |
| 12.0.1 | improvement | Updated @sbaiahmed1/react-native-biometrics from version v0.10.0 to v0.15.0. | @sbaiahmed1/react-native-biometrics |  |
| 12.0.0 | breaking | Replaced deprecated CameraRoll.saveToCameraRoll with CameraRoll.saveAsset in SaveToPictureLibrary activity. | SaveToPictureLibrary, CameraRoll.saveToCameraRoll | CameraRoll.saveAsset |
| 12.0.0 | improvement | Add await to API calls updated to async in recent update. |  |  |
| 12.0.0 | improvement | Updated @react-native-camera-roll/camera-roll from version v7.4.0 to v7.10.2. | @react-native-camera-roll/camera-roll |  |
| 12.0.0 | improvement | Updated @sbaiahmed1/react-native-biometrics from version v0.4.0 to v0.10.0. | @sbaiahmed1/react-native-biometrics |  |
| 12.0.0 | improvement | Updated @swan-io/react-native-browser from version v0.4.1 to v1.0.1. | @swan-io/react-native-browser |  |
| 12.0.0 | improvement | Updated react-native-blob-util from version v0.21.2 to v0.24.7. | react-native-blob-util |  |
| 12.0.0 | improvement | Updated react-native-device-info from version v14.0.4 to v15.0.2. | react-native-device-info |  |
| 12.0.0 | improvement | Updated react-native-file-viewer-turbo from version v0.6.0 to v0.7.4. | react-native-file-viewer-turbo |  |
| 12.0.0 | improvement | Updated react-native-localize from version v3.2.1 to v3.7.0. | react-native-localize |  |
| 12.0.0 | improvement | Updated react-native-permissions from version v5.4.2 to v5.5.1. | react-native-permissions |  |
| 12.0.0 | improvement | Updated @react-native-community/netinfo from version v11.4.1 to v11.5.2. | AppEvents, @react-native-community/netinfo |  |
| 12.0.0 | breaking | Replaced deprecated InteractionManager in Feedback widget. | Feedback, InteractionManager |  |
| 12.0.0 | feature | Translation support for all widget text through configurable properties in Studio Pro. | Feedback |  |
| 12.0.0 | improvement | Visible label above feedback input field to ensure WCAG compliance. | Feedback |  |
| 12.0.0 | improvement | Updated react-native-svg from version v15.12.1 to v15.15.3. | GalleryTextFilter, react-native-svg |  |
| 12.0.0 | improvement | Updated @d11/react-native-fast-image from version v8.11.1 to v8.13.0. | Image, @d11/react-native-fast-image |  |
| 12.0.0 | improvement | Updated react-native-gesture-handler from version v2.24.0 to v2.30.0. | ListViewSwipe, react-native-gesture-handler |  |
| 12.0.0 | improvement | Updated react-native-maps from version v1.14.0 to v1.20.1. | Maps, react-native-maps |  |
| 12.0.0 | improvement | Updated @react-navigation/bottom-tabs from version v6.6.1 to v7.15.2. | SafeAreaView, @react-navigation/bottom-tabs |  |
| 12.0.0 | improvement | Updated react-native-safe-area-context from version v5.2.0 to v5.7.0. | SafeAreaView, react-native-safe-area-context |  |
| 12.0.0 | improvement | Updated react-native-webview from version v13.13.2 to v13.16.1. | Signature, react-native-webview |  |
| 12.0.0 | improvement | Updated react-native-video from version v6.10.2 to v6.19.0. | VideoPlayer, react-native-video |  |
| 11.4.2 | improvement | BottomSheet now uses BottomSheetScrollView instead of BottomSheetView, enabling proper scrolling in expanded states. | BottomSheet |  |
| 11.4.2 | improvement | NativeBottomSheet explicitly calculates snapPoints with 90% screen height cap for predictable sizing. | BottomSheet |  |
| 11.4.2 | improvement | CustomModalSheet measures content height dynamically with 90% screen height cap, removing offscreen SafeAreaView measurement. | BottomSheet |  |
| 11.4.2 | improvement | Migrated from using native FlatList to @shopify/flash-list. | Gallery |  |
| 11.3.11 | fix | Fixed biometric authentication issue not working on Android and crashing on iOS. | biometric authentication |  |
| 11.3.11 | breaking | Replaced @notifee/react-native with react-native-notify-kit library. | @notifee/react-native, react-native-notify-kit | react-native-notify-kit |
| 11.3.10 | fix | Fixed flickering issue on Android when opening bottom sheet (both basic and custom render types). | BottomSheet |  |
| 11.3.9 | fix | Fixed the non-worklet function called on the UI thread error in bottom sheet from @gorhom/bottom-sheet usage. | BottomSheet, @gorhom/bottom-sheet |  |
| 11.3.8 | breaking | Migrated from using the native FlatList to @shopify/flash-list. | Gallery, @shopify/flash-list | @shopify/flash-list |
| 11.3.6 | fix | Fixed native file system module reference. | native file system module |  |
| 11.3.5 | requirement | Upgraded Native Mobile Resources to Studio Pro 11.7.0. |  |  |
| 11.3.3 | fix | Fixed an issue where the background-gradient-native widget would not render correctly with the new RN architecture upgrade. | BackgroundGradient |  |
| 11.3.2 | feature | Expanded the barcode-scanner configuration in Vision Camera to support all available CodeType formats, including QR, Aztec, Data Matrix, PDF-417, EAN, UPC, GS1 DataBar, ITF, and Code barcodes. | BarcodeScanner, Vision Camera |  |
| 11.3.2 | requirement | Updated react-native-vision-camera from version v4.7.1 to v4.7.3. | react-native-vision-camera |  |
| 11.3.1 | requirement | Updated react-native-reanimated to v3.17.5. Addresses compatibility issues with React Native 0.78 and later versions. | BottomSheet, react-native-reanimated |  |
| 11.3.1 | requirement | Updated react-native-svg to v15.12.1. Addresses compatibility issues with React Native 0.78 and later versions. | GalleryTextFilter, react-native-svg |  |
| 11.3.0 | breaking | Updated react-native-firebase to v20.1.0. Ensure Native Template and Native Builder are updated accordingly. | Notifications, react-native-firebase |  |
| 11.2.1 | breaking | Updated react-native-firebase to v20.1.0. Ensure Native Template and Native Builder are updated accordingly. | Notifications, react-native-firebase |  |
| 11.2.0 | requirement | Updated react-native-video version to 6.10.2. | VideoPlayer, react-native-video |  |
| 11.1.1 | breaking | Migrated to react-native-vision-camera from react-native-camera. | BarcodeScanner, react-native-camera, react-native-vision-camera | react-native-vision-camera |
| 11.1.0 | breaking | Migrated from react-native-sound to react-native-track-player. | react-native-sound, react-native-track-player | react-native-track-player |
| 11.1.0 | requirement | Updated react-native-permissions to 5.4.2. | react-native-permissions |  |
| 11.1.0 | removal | Removed react-native-schedule-exact-alarm-permission since it's no longer required. | react-native-schedule-exact-alarm-permission |  |
| 11.1.0 | requirement | Updated react-native from version 0.75.4 to 0.77.3. | react-native |  |
| 11.1.0 | breaking | Migrated from react-native-file-viewer to react-native-file-viewer-turbo for new architecture compatibility. | react-native-file-viewer, react-native-file-viewer-turbo | react-native-file-viewer-turbo |
| 11.1.0 | breaking | File viewer now uses modal to display content. | File viewer |  |
| 11.1.0 | breaking | Migrated from react-native-biometrics to @sbaiahmed1/react-native-biometrics for new architecture compatibility. | react-native-biometrics, @sbaiahmed1/react-native-biometrics | @sbaiahmed1/react-native-biometrics |
| 11.1.0 | requirement | Updated react-native-reanimated to v3.16.7. | BottomSheet, react-native-reanimated |  |
| 11.1.0 | breaking | Migrated from react-native-fast-image to @d11/react-native-fast-image for new architecture compatibility. | Image, react-native-fast-image, @d11/react-native-fast-image | @d11/react-native-fast-image |
| 11.1.0 | removal | Removed react-native-system-navigation-bar and deprecated-react-native-prop-types dependencies. Navigation bar visibility now handled by react-native-video package. | VideoPlayer, react-native-system-navigation-bar, deprecated-react-native-prop-types |  |
| 11.0.3 | requirement | Updated React Native from version 0.75.4 to 0.77.3. | React Native |  |
| 11.0.3 | requirement | Updated react-native-video to version 6.10.0. | VideoPlayer, react-native-video |  |
| 11.0.0 | requirement | Updated react-native-linear-gradient to latest version. | BackgroundGradient, react-native-linear-gradient |  |
| 11.0.0 | requirement | Updated react-native-device-info to latest version. | BottomSheet, react-native-device-info |  |
| 11.0.0 | breaking | The widget has been migrated to notifee. | Notifications |  |
| 11.0.0 | requirement | Updated react-native-webview from version v13.12.5 to latest. | Signature, react-native-webview |  |
| 11.0.0 | requirement | Updated react-native-webview from version v13.12.5 to latest to support react-native 0.77. | WebView, react-native-webview |  |
| 10.1.17 | breaking | Replaced the deprecated CameraRoll.saveToCameraRoll with CameraRoll.saveAsset in SaveToPictureLibrary activity. | SaveToPictureLibrary, CameraRoll | CameraRoll.saveAsset |
| 10.1.11 | feature | Expanded the barcode-scanner configuration in Vision Camera to support all available CodeType formats, including QR, Aztec, Data Matrix, PDF-417, EAN, UPC, GS1 DataBar, ITF, and Code barcodes. | BarcodeScanner, Vision Camera |  |
| 10.1.10 | requirement | Updated react-native-vision-camera from version v4.7.1 to v4.7.3. | BarcodeScanner, react-native-vision-camera |  |
| 10.1.9 | breaking | Migrated to react-native-vision-camera from react-native-camera. | BarcodeScanner, react-native-camera, react-native-vision-camera | react-native-vision-camera |
| 10.1.8 | breaking | Updated react-native-firebase to v20.1.0. Ensure Native Template and Native Builder are updated accordingly. | Notifications, react-native-firebase |  |
| 10.1.6 | requirement | Updated react-native-video version to 6.10.2. | VideoPlayer, react-native-video |  |
| 10.1.4 | fix | Fixed location permission issue on iOS. | react-native-community/geolocation |  |
| 10.1.1 | requirement | Updated react-native-video version from 6.4.5 to 6.10.0. | VideoPlayer, react-native-video |  |
| 10.1.0 | requirement | Updated react-native-webview to latest version to support react native 0.77. | Signature, react-native-webview |  |
| 10.0.0 | breaking | Migrated from react-native-inappbrowser-reborn to @swan-io/react-native-browser to prevent issues for next rn upgrade. | react-native-inappbrowser-reborn, @swan-io/react-native-browser | @swan-io/react-native-browser |
| 10.0.0 | breaking | Migrated from @react-native-community/cameraroll to @react-native-camera-roll/camera-roll to prevent issues for next rn upgrade. | @react-native-community/cameraroll, @react-native-camera-roll/camera-roll | @react-native-camera-roll/camera-roll |
| 10.0.0 | requirement | Updated several dependencies such as react-native-blob-util and react-native-image-picker to their latest version. | react-native-blob-util, react-native-image-picker |  |
| 10.0.0 | requirement | Updated @react-native-community/netinfo from version v5.9.7 to v11.4.1. | AppEvents, @react-native-community/netinfo |  |
| 10.0.0 | breaking | Rewrote all bottomsheet widgets (customModalSheet, ExpandingDrawer, and NativeBottomSheet) using @gorhom/bottom-sheet. | BottomSheet, @gorhom/bottom-sheet | @gorhom/bottom-sheet |
| 10.0.0 | requirement | Updated react-native-view-shot from version v3.1.2 to v4.0.3. | Feedback, react-native-view-shot |  |
| 10.0.0 | requirement | Updated react-native-gesture-handler from version v2.16.2 to 2.24.0. | ListViewSwipe, react-native-gesture-handler |  |
| 10.0.0 | requirement | Updated react-native-webview from version v9.0.0 to v10.15.0. | Signature, react-native-webview |  |
| 10.0.0 | requirement | Updated react-native-webview from version v11.26.1 to v13.13.2. | WebView, react-native-webview |  |
| 9.3.5 | improvement | Updated react-native-svg from 15.7.1 to 15.11.2. | gallery-text-filter-native, image-native, qr-code-native, react-native-svg |  |
| 9.3.4 | improvement | Started using react-native-safe-area-context to improve edge-to-edge boundaries on Android. | SafeAreaView, react-native-safe-area-context |  |
| 9.3.0 | improvement | Updated react-native-modal from v11.4.5 to v13.0.1 to fix random crashes in custom-bottom-sheet widget. | BottomSheet, react-native-modal |  |
| 9.2.0 | fix | Bumped react-native-progress version to fix black background issues. | ProgressBar, react-native-progress |  |
| 9.0.0 | improvement | Updated @mendix/pluggable-widgets-tools from v9.0.0 to v10.0.1. | @mendix/pluggable-widgets-tools |  |
| 9.0.0 | breaking | Updated react-native from 0.73.8 to 0.75.4. | react-native |  |
| 9.0.0 | breaking | Switched from @react-native-community/async-storage to @react-native-async-storage/async-storage. | @react-native-community/async-storage, @react-native-async-storage/async-storage | @react-native-async-storage/async-storage |
| 9.0.0 | feature | Upgraded React Native Permissions to 4.5.1. | React Native Permissions |  |
| 9.0.0 | breaking | Updated react-native-device-info from v11.1.0 to v13.0.0. | BottomSheet, react-native-device-info |  |
| 9.0.0 | breaking | Updated react-native-svg from v12.3.0 to v15.7.1. | GalleryTextFilter, react-native-svg |  |
| 9.0.0 | improvement | Updated react-native-vector-icons from v10.0.3 to v10.2.0. | Image, react-native-vector-icons |  |
| 9.0.0 | improvement | Updated react-native-maps version to 1.14.0. | Maps, react-native-maps |  |
| 9.0.0 | breaking | Renamed renderMode property to popupRenderMode to avoid conflicts with new renderMode system option. | PopupMenu, renderMode, popupRenderMode | popupRenderMode |
| 9.0.0 | migration-step | Update PopupMenu renderMode property to popupRenderMode in Studio Pro. | PopupMenu, renderMode, popupRenderMode |  |
| 9.0.0 | feature | Added support for device font size for responsive progress circle sizing. | ProgressCircle |  |
| 9.0.0 | improvement | Updated react-native-video version to 6.4.5. | VideoPlayer, react-native-video |  |
| 8.0.3 | feature | Upgraded React Native Permissions to 4.5.1. | React Native Permissions |  |
| 8.0.3 | improvement | Updated react-native-maps version to 1.14.0. | Maps, react-native-maps |  |
| 8.0.3 | feature | Added support for device font size for responsive progress circle sizing. | ProgressCircle |  |
| 8.0.3 | improvement | Updated react-native-video version to 6.4.5. | VideoPlayer, react-native-video |  |
| 8.0.2 | improvement | Updated react-native-maps version to 1.14.0. | Maps, react-native-maps |  |
| 8.0.2 | improvement | Updated react-native-video version to 6.4.5. | VideoPlayer, react-native-video |  |
| 8.0.1 | feature | Upgraded React Native Device Info to version 11.1.0. | BottomSheet, react-native-device-info |  |
| 8.0.1 | feature | Upgraded React Native Gesture Handler to version 2.16.2. | ListViewSwipe, react-native-gesture-handler |  |
| 8.0.1 | improvement | Updated Rating widget to replace AnimatableProps from react-native-animatable with AnimatableProperties. | Rating, react-native-animatable |  |
| 8.0.1 | breaking | Made Rating widget compatible with React Native 0.73.8. | Rating, react-native |  |
| 8.0.0 | breaking | Upgraded React Native to version 0.73.8. | react-native |  |
| 6.1.0 | fix | Added CheckGenericPermission and updated RequestGenericPermission to use SCHEDULE_EXACT_ALARM. | CheckGenericPermission, RequestGenericPermission, SCHEDULE_EXACT_ALARM |  |
| 6.0.0 | breaking | Upgraded React Native to version 0.72.7. | React Native |  |
| 6.0.0 | breaking | Made Image widget compatible with React Native 0.72.7. | Image |  |
| 6.0.0 | requirement | Updated react-native-vector-icons dependency from 9.1.0 to 10.0.3. | react-native-vector-icons |  |
| 6.0.0 | breaking | Made Rating widget compatible with React Native 0.72.7. | Rating |  |
| 6.0.0 | breaking | Upgraded react-native-system-navigation-bar to version 2.6.3. | VideoPlayer |  |
| 5.2.0 | breaking | Replaced @notifee/react-native with react-native-notify-kit library. | @notifee/react-native, react-native-notify-kit | react-native-notify-kit |
| 5.1.2 | improvement | Added push notification permission request support for Android API level>=33. | push notifications |  |
| 4.1.5 | requirement | Updated react-native-permissions to version 3.6.1. | react-native-permissions |  |
| 4.1.4 | requirement | Updated react-native-permissions to version 3.6.1. | react-native-permissions |  |
| 4.1.2 | fix | Fixed issue with missing react-native-schedule-exact-alarm-permission dependency. | react-native-schedule-exact-alarm-permission |  |
| 4.1.0 | improvement | Added CheckGenericPermission and updated RequestGenericPermission to use SCHEDULE_EXACT_ALARM. | CheckGenericPermission, RequestGenericPermission |  |
| 4.0.5 | improvement | Added push notification permission request support for Android API level>=33. | push notifications |  |
| 4.0.4 | requirement | Minimum Mendix version set to 9.24.1. | Mendix |  |
| 4.0.3 | fix | Updated react-native-device-info library. | react-native-device-info |  |
| 4.0.0 | breaking | Made AppEvents widget compatible with React Native 0.70.7. | AppEvents |  |
| 4.0.0 | breaking | Made BarChart widget compatible with React Native 0.70.7. | BarChart |  |
| 4.0.0 | breaking | Made BarcodeScanner widget compatible with React Native 0.70.7. | BarcodeScanner |  |
| 4.0.0 | breaking | Made Carousel widget compatible with React Native 0.70.7. | Carousel |  |
| 4.0.0 | breaking | Made ColorPicker widget compatible with React Native 0.70.7. | ColorPicker |  |
| 4.0.0 | breaking | Made ColumnChart widget compatible with React Native 0.70.7. | ColumnChart |  |
| 4.0.0 | breaking | Made FloatingActionButton widget compatible with React Native 0.70.7. | FloatingActionButton |  |
| 4.0.0 | breaking | Made LineChart widget compatible with React Native 0.70.7. | LineChart |  |
| 4.0.0 | breaking | Made ListViewSwipe widget compatible with React Native 0.70.7. | ListViewSwipe |  |
| 4.0.0 | breaking | Made Maps widget compatible with React Native 0.70.7. | Maps |  |
| 4.0.0 | breaking | Made Notifications widget compatible with React Native 0.70.7. | Notifications |  |
| 4.0.0 | breaking | Made PieDoughnutChart widget compatible with React Native 0.70.7. | PieDoughnutChart |  |
| 4.0.0 | breaking | Made PopupMenu widget compatible with React Native 0.70.7. | PopupMenu |  |
| 4.0.0 | improvement | Bumped react-native-progress dependency. | ProgressBar |  |
| 4.0.0 | breaking | Made Rating widget compatible with React Native 0.70.7. | Rating |  |
| 4.0.0 | breaking | Made Signature widget compatible with React Native 0.70.7. | Signature |  |
| 4.0.0 | breaking | Made Slider widget compatible with React Native 0.70.7. | Slider |  |
| 4.0.0 | breaking | Made VideoPlayer widget compatible with React Native 0.70.7. | VideoPlayer |  |
| 4.0.0 | breaking | Made WebView widget compatible with React Native 0.70.7. | WebView |  |
| 3.13.0 | breaking | Fixed Android 12 push notifications issue; native template must match module version. | Notifications |  |
| 3.11.1 | feature | Introduced new Download File action for Mendix document files to native device storage. | Download File |  |
| 3.11.1 | removal | Removed animated GIFs from README file. | Animation |  |
| 3.11.0 | feature | Introduced new RequestGenericPermission action for requesting any available device permission. | RequestGenericPermission |  |
| 3.10.0 | breaking | Added Atlas styling support; update Background gradient widgets design properties per Mendix Docs. | BackgroundGradient |  |
| 3.8.0 | fix | Fixed issue on Android devices when using Make it Native app to preview page containing Notifications widget. | Notifications |  |
| 3.7.1 | fix | Fixed issue on Android devices when using Make it Native app to preview page containing Notifications widget. | Notifications |  |
| 3.5.2 | fix | Reduced module size by removing unused dependencies to speed up Team Server interaction. |  |  |
| 3.5.1 | improvement | Updated the feedback API. | Feedback |  |
| 3.5.0 | fix | Updated action to prevent incorrect result when permission not yet requested on iOS due to hasPermission method change in react-native-firebase. |  |  |
| 3.4.3 | fix | Updated action to prevent incorrect result when permission not yet requested on iOS due to hasPermission method change in react-native-firebase. |  |  |
| 3.4.2 | fix | The version of react-native-vector-icons now matches that included in Native Template. | Image |  |
| 3.4.2 | fix | Widget refactored and now includes react-native-vector-icons version matching Native Template. | Rating |  |
| 3.1.4 | breaking | Version now stored in `themesource/.version` file instead of constant in Studio Pro Project Explorer. |  |  |
| 3.1.4 | fix | Fixed issue with some widget bundles erroneously including react-dom and being very large. |  |  |
| 3.1.4 | fix | Fixed issue with native release production bundles being mangled incorrectly, causing runtime errors. |  |  |
| 3.1.4 | fix | Fixed data source consistency check for MX 9.2 and above. | BarChart |  |
| 3.0.0 | breaking | TakePicture and TakePictureAdvanced no longer support 'either' as pictureSource parameter value. | TakePicture, TakePictureAdvanced |  |
| 3.0.0 | requirement | TakePicture and TakePictureAdvanced actions now support Android 11. | TakePicture, TakePictureAdvanced |  |
| 3.0.0 | fix | Fixed dynamic marker data source consistency check for Mendix 9.2 and above. | Maps |  |
| 2.0.0 | requirement | New native dependency management system. Every library now packaged with its dependencies. | Native dependency management system |  |
| 2.0.0 | security | Library updates and security fixes. |  |  |
| 2.0.0 | improvement | Updated WebView and Signature widgets. | WebView, Signature |  |
| 1.4.1 | fix | Added missing dependency to avoid bundling error. |  |  |
| 1.3.0 | breaking | TakePicture and TakePictureAdvanced no longer support 'either' as pictureSource parameter value. | TakePicture, TakePictureAdvanced |  |
| 1.3.0 | requirement | TakePicture and TakePictureAdvanced actions now support Android 11. | TakePicture, TakePictureAdvanced |  |
| 1.2.7 | improvement | Improved Native Webview widget's security measurements. | Native Webview |  |
| 1.2.0 | breaking | Renamed popup menu style property from containerStyle to container in basic and custom items. | Popup menu |  |
| 1.1.7 | breaking | Changed name from 'Popup menu' to 'Pop-up menu'. | Popup menu |  |
| 1.1.6 | security | Fixed security issue where captured image was saved instead of used temporarily. | TakePicture |  |
| 1.1.5 | fix | Fixed issue where some JS actions were not aligned with module name changes. |  |  |
| 1.1.4 | breaking | Removed extra arguments (widget & height attribute name) from TakePicture action. | TakePicture |  |
| 1.1.2 | breaking | Renamed module package name to Native Mobile Actions. |  |  |
| 1.1.1 | fix | Removed icon dependency on Nanoflow Commons added by mistake. | Nanoflow Commons |  |
| 1.1.0 | improvement | Updated widgets to be compatible with React Native upgrade to 0.61. |  |  |
| 1.0.10 | fix | Fixed DeviceInfo JS Action for compatibility with Studio Pro 8.6.3. | DeviceInfo |  |
| 1.0.8 | improvement | Updated Web view library. | Web view |  |
| 1.0.5 | fix | Fixed compatibility problem in GetDeviceInfo action. | GetDeviceInfo |  |

## Native parallax scroll view <a id="120093"></a>
Widget, Siemens, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/120093)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2022-04-18 | 9.0.5 |

## Native Status bar <a id="216567"></a>
Widget, Siemens, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/216567)

| version | published | min Mendix |
|---|---|---|
| 1.1.0 | 2023-09-27 | 9.12.14 |
| 1.0.0 | 2023-09-27 | 9.12.14 |

## Number to Vietnamese text <a id="254506"></a>
Module, EVNCPC, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/254506)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2026-01-27 | 10.24.9 |

## Object List Operations <a id="117715"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/117715)

| version | published | min Mendix |
|---|---|---|
| 4.1.0 | 2026-04-10 | 11.9.0 |
| 4.0.0 | 2026-02-07 | 10.24.9 |
| 3.1.0 | 2024-09-13 | 9.18.0 |
| 3.0.0 | 2024-05-28 | 9.18.0 |
| 2.0.0 | 2024-04-04 | 8.18.1 |
| 1.1.0 | 2021-11-23 | 8.18.1 |
| 1.0.1 | 2021-10-26 | 8.18.1 |
| 1.0.0 | 2021-06-14 | 8.18.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 4.1.0 | migration-step | Replace deprecated IMendixObject.getMember(IContext, String) calls with IMendixObject.getMember(String). | IMendixObject.getMember(IContext, String), IMendixObject.getMember(String) | IMendixObject.getMember(String) |
| 4.1.0 | migration-step | Replace IMendixObjectMember.getState() == MemberState.CHANGED with IMendixObjectMember.isChanged(). | IMendixObjectMember.getState(), IMendixObjectMember.isChanged() | IMendixObjectMember.isChanged() |
| 4.0.0 | requirement | Mendix project version raised to 10.24.9 to make utilities available in Mx11. |  |  |
| 3.0.0 | requirement | Mendix project version raised to 9.18.0 to make utilities available in Mx10. |  |  |
| 2.0.0 | migration-step | Sample data pages, logic and entities moved to separate ListOperationsExamples module; no longer shipped with Java actions. | ListOperationsExamples |  |
| 2.0.0 | deprecation | V1 sorting versions moved to Deprecated folder; functionality unchanged to prevent breaking changes. | V1 sorting operations |  |
| 2.0.0 | breaking | V2 sorting Java actions renamed; V1 versions renamed to new names. | JA_List_MoveObjectToPosition, JA_List_PerformSortingAction, JA_List_SanitizeSorting |  |
| 2.0.0 | breaking | V2 sorting Java actions now return list of objects changed during execution. | JA_List_MoveObjectToPosition, JA_List_PerformSortingAction, JA_List_SanitizeSorting |  |
| 2.0.0 | breaking | Parameter AffectedList renamed to ProvidedList in sorting operations. | AffectedList, ProvidedList | ProvidedList |
| 2.0.0 | improvement | Sorting attribute now also accepts Long attributes. | sorting operations |  |
| 2.0.0 | breaking | New required parameter StartingIndex added to JA_List_SanitizeSorting; previously fixed at 1. | JA_List_SanitizeSorting, StartingIndex |  |
| 2.0.0 | breaking | New position parameter reworked; now must equal sorting attribute value of another object in provided list. | JA_List_MoveObjectToPosition, New position |  |
| 1.0.1 | fix | Fixed issue where Commit = false didn't update standalone object instance with new sort value. |  |  |

## ObjectHandling <a id="37114"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/37114)

| version | published | min Mendix |
|---|---|---|
| 5.2.0 | 2025-11-19 | 10.24.0 |
| 5.1.0 | 2025-07-25 | 10.21.0 |
| 5.0.0 | 2025-04-10 | 10.21.0 |
| 4.1.0 | 2025-07-25 | 9.18.0 |
| 4.0.3 | 2025-03-27 | 9.18.0 |
| 4.0.2 | 2024-07-04 | 9.18.0 |
| 4.0.1 | 2023-08-22 | 9.18.0 |
| 4.0.0 | 2023-04-21 | 9.18.0 |
| 3.2.0 | 2021-11-15 | 8.12.0 |
| 3.1.0 | 2020-12-17 | 8.12.0 |
| 3.0.1 | 2020-02-14 | 8.1.0 |
| 3.0.0 | 2019-09-25 | 8.1.0 |
| 2.0 | 2017-02-22 | 7.0.2 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 5.2.0 | requirement | Module upgraded to Mendix 10.24.0 |  |  |
| 5.1.0 | security | Upgraded Commons-lang3 library to version 3.18.0 to resolve CVE-2025-48924 | Commons-lang3 |  |
| 5.0.0 | requirement | Module upgraded to Mendix version 10.21.0 |  |  |
| 4.1.0 | security | Upgraded Commons-lang3 library to version 3.18.0 to resolve CVE-2025-48924 | Commons-lang3 |  |
| 4.0.1 | migration-step | Included migration file for Java dependencies for Studio Pro 10 compatibility |  |  |
| 4.0.0 | requirement | Module updated to Studio Pro 9.18 for use in Studio Pro 10 |  |  |
| 4.0.0 | requirement | Updated Apache Commons Lang dependency to version 3.12.0 | Apache Commons Lang |  |
| 4.0.0 | requirement | Added dependency on Apache Commons Text version 1.10.0 for moved functionality | Apache Commons Text |  |
| 3.1.0 | requirement | Upgraded minimum Mendix version to 8.12.0 for Mendix 9 compatibility |  |  |
| 3.1.0 | requirement | Set Commons Lang3 dependency to v3.7 to avoid conflicts with Community Commons | Commons Lang3 |  |
| 3.0.0 | requirement | Converted to Mendix version 8.1 |  |  |
| 2.0 | requirement | Converted to Mendix 7 and removed Java code for locking |  |  |

## OCR file <a id="302828"></a>
Module, EVNCPC, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/302828)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2026-07-28 | 11.11.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.0.0 | requirement | Minimum Mendix version requirement: 11.11.0 | Mendix |  |

## OData Connector for SAP solutions <a id="74525"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/74525)

| version | published | min Mendix |
|---|---|---|
| 7.1.6 | 2026-06-25 | 10.21.0 |
| 7.1.5 | 2026-02-10 | 10.21.0 |
| 7.1.4 | 2025-12-03 | 10.21.0 |
| 7.1.3 | 2025-10-23 | 10.21.0 |
| 7.1.2 | 2025-09-09 | 10.21.0 |
| 7.1.1 | 2025-07-30 | 10.21.0 |
| 7.1.0 | 2025-07-30 | 10.21.0 |
| 7.0.0 | 2025-07-08 | 10.21.0 |
| 6.1.3 | 2026-06-18 | 9.24.33 |
| 6.1.2 | 2025-12-03 | 9.24.33 |
| 6.1.1 | 2025-10-14 | 9.24.33 |
| 6.1.0 | 2025-07-17 | 9.24.33 |
| 6.0.6 | 2025-05-06 | 9.24.33 |
| 6.0.5 | 2025-03-27 | 9.24.4 |
| 6.0.4 | 2024-11-08 | 9.24.4 |
| 6.0.3 | 2024-05-02 | 9.24.4 |
| 6.0.2 | 2023-10-31 | 9.24.4 |
| 6.0.1 | 2023-05-30 | 9.24.0 |
| 6.0.0 | 2023-04-03 | 9.24.0 |
| 5.6.2 | 2023-10-06 | 8.18.25 |
| 5.6.1 | 2023-05-18 | 8.18.10 |
| 5.6.0 | 2023-02-01 | 8.18.10 |
| 5.5.5 | 2022-09-07 | 8.18.10 |
| 5.5.4 | 2022-07-29 | 8.18.10 |
| 5.5.3 | 2022-07-05 | 8.18.10 |
| 5.5.2 | 2022-03-22 | 8.18.10 |
| 5.5.1 | 2022-03-14 | 8.18.10 |
| 5.5.0 | 2021-09-29 | 8.18.10 |
| 5.4.0 | 2021-08-19 | 8.15.1 |
| 5.3.0 | 2021-06-16 | 8.15.1 |
| 5.2.4 | 2021-02-26 | 8.15.1 |
| 5.2.3 | 2021-02-04 | 8.15.1 |
| 5.2.2 | 2021-01-12 | 8.15.1 |
| 5.2.1 | 2020-12-04 | 8.15.1 |
| 5.2.0 | 2020-10-13 | 7.23.3 |
| 5.1.3 | 2020-10-07 | 7.23.3 |
| 5.1.2 | 2020-06-29 | 7.23.3 |
| 5.1.1 | 2020-05-29 | 7.23.3 |
| 5.1.0 | 2020-05-06 | 7.23.3 |
| 5.0.6 | 2020-04-01 | 7.23.3 |
| … 18 older versions | | |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 7.1.5 | removal | Removed deprecated dependencies to ensure compatibility with Mendix 11. |  |  |
| 7.1.4 | security | Security vulnerabilities were identified and fixed. |  |  |
| 7.1.2 | fix | Harmonized internal module dependencies to prevent compilation issues. |  |  |
| 7.1.1 | fix | Harmonized internal module dependencies to prevent compilation issues. |  |  |
| 7.0.0 | requirement | Upgrade to Mx 10.21. |  |  |
| 6.1.2 | security | Security vulnerabilities were identified and fixed. |  |  |
| 6.0.6 | requirement | Released on Mx v9.24.33. |  |  |
| 6.0.5 | fix | Updated serializer for OData action calls. |  |  |
| 6.0.3 | fix | Updated length for meta_objectURL attribute. | meta_objectURL |  |
| 6.0.2 | security | Security Fixes. Please remove duplicate jars from your project after taking latest release. |  |  |
| 6.0.1 | fix | Modified Java Action for Mx10 readiness. |  |  |
| 6.0.1 | fix | Updated logic for OData URL creation for delete action. |  |  |
| 6.0.0 | requirement | Upgraded to Mendix v9.24.0. |  |  |
| 5.6.2 | security | Security Fixes. Please remove duplicate jars from your project after taking latest release. |  |  |
| 5.6.1 | fix | Updated OData URL creation logic. |  |  |
| 5.5.4 | security | Upgrade OkHTTP jar to fix security vulnerability. | OkHTTP |  |
| 5.5.3 | security | Updated vulnerable okhttp jar. | okhttp |  |
| 5.5.0 | requirement | Upgraded to Mendix Studio Pro v8.18.10. |  |  |
| 5.3.0 | fix | Updated OData request creation. |  |  |
| 5.2.3 | fix | Update in request creation. |  |  |
| 5.2.3 | fix | Update in response parsing. |  |  |
| 5.2.2 | fix | Updated deprecated function Core.execute() to Core.microflowcall() for Mendix 9 compatibility. |  |  |
| 5.2.1 | requirement | Upgraded to Mendix 8. |  |  |
| 5.1.3 | fix | Remove unused libraries. |  |  |
| 5.0.0 | requirement | Migrated SAP OData Connector to Mendix 7.23.3 to support Mendix Studio Pro 8. |  |  |
| 4.0.4 | fix | Added missing javax.json jar. | javax.json |  |
| 3.6.0 | breaking | Change the life cycle of cookies and CSRF tokens to be dependent on the Mendix sessions. |  |  |

## OData Query Builder Connector for SAP solutions <a id="110732"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/110732)

| version | published | min Mendix |
|---|---|---|
| 1.1.5 | 2022-11-15 | 8.18.10 |
| 1.1.4 | 2021-08-26 | 8.15.1 |
| 1.1.3 | 2021-05-21 | 8.15.1 |
| 1.1.2 | 2020-12-08 | 8.15.1 |
| 1.1.1 | 2020-08-19 | 8.9.0 |
| 1.1.0 | 2020-06-30 | 8.9.0 |
| 1.0.0 | 2019-08-06 | 7.23.3 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.1.5 | requirement | Updated to Mendix v8.18.10 | Mendix |  |
| 1.1.2 | requirement | Upgraded Mendix Studio Pro version to 8.15.1 | Mendix |  |
| 1.1.1 | improvement | Remove unused libraries |  |  |

## Odin - AI assisted Mendix development <a id="242538"></a>
Module, Siemens, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/242538)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2025-07-09 | 10.12.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.0.0 | requirement | Requires minimum Mendix version 10.12.0. | Mendix |  |
| 1.0.0 | known-issue | Only works with OpenAI models in this beta version. | OpenAI |  |

## OIDC Provider <a id="244687"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/244687)

| version | published | min Mendix |
|---|---|---|
| 5.0.0 | 2025-08-04 | 10.24.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 5.0.0 | requirement | Supports Studio Pro v10.24.0 and above | Mendix Studio Pro |  |
| 5.0.0 | breaking | Custom-Claim Microflow selection requires the 'OIDCP_CustClaim' prefix for proper dropdown selection | Custom-Claim Microflow selection |  |
| 5.0.0 | removal | Beta feature SSOBridge removed from v5.0.0 | SSOBridge |  |
| 5.0.0 | removal | Beta feature Implicit Flow removed from v5.0.0 | Implicit Flow |  |
| 5.0.0 | removal | Beta feature Hybrid Flow removed from v5.0.0 | Hybrid Flow |  |
| 5.0.0 | removal | Beta feature Mendix App Registration removed from v5.0.0 | Mendix App Registration |  |
| 5.0.0 | removal | Beta feature Password Grant Type removed from v5.0.0 | Password Grant Type |  |
| 5.0.0 | removal | Beta feature Change Password Functionality removed from v5.0.0 | Change Password Functionality |  |

## OIDC SSO <a id="120371"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/120371)

| version | published | min Mendix |
|---|---|---|
| 4.7.0 | 2026-08-24 | 10.24.0 |
| 4.6.0 | 2026-07-10 | 10.24.0 |
| 4.5.0 | 2026-06-11 | 10.24.0 |
| 4.4.0 | 2026-04-13 | 10.24.0 |
| 4.3.0 | 2026-03-09 | 10.24.0 |
| 4.2.1 | 2026-01-26 | 10.24.0 |
| 4.2.0 | 2025-10-17 | 10.21.1 |
| 4.1.2 | 2025-08-05 | 10.21.1 |
| 4.1.1 | 2025-05-29 | 10.21.0 |
| 4.1.0 | 2025-05-15 | 10.21.1 |
| 4.0.1 | 2025-05-21 | 10.12.10 |
| 4.0.0 | 2024-12-24 | 10.12.10 |
| 3.6.0 | 2026-07-14 | 9.24.18 |
| 3.5.1 | 2026-06-24 | 9.24.18 |
| 3.5.0 | 2026-04-13 | 9.24.18 |
| 3.4.0 | 2026-03-09 | 9.24.18 |
| 3.3.1 | 2026-01-26 | 9.24.18 |
| 3.3.0 | 2025-10-20 | 9.24.18 |
| 3.2.1 | 2025-05-21 | 9.24.18 |
| 3.2.0 | 2024-11-05 | 9.24.18 |
| 3.1.0 | 2024-07-29 | 9.24.2 |
| 3.0.1 | 2024-06-11 | 9.24.2 |
| 3.0.0 | 2024-05-14 | 9.24.2 |
| 2.4.0 | 2024-03-27 | 9.24.2 |
| 2.3.2 | 2023-12-19 | 9.24.2 |
| 2.3.1 | 2023-11-15 | 9.24.2 |
| 2.3.0 | 2023-09-07 | 9.24.2 |
| 2.2.0 | 2023-07-13 | 9.24.2 |
| 2.1.1 | 2023-05-10 | 9.22.0 |
| 2.1.0 | 2023-03-15 | 9.22.0 |
| 2.0.0 | 2022-12-23 | 9.12.7 |
| 1.1.1 | 2022-12-02 | 9.12.5 |
| 1.1.0 | 2022-08-19 | 9.12.5 |
| 1.0.1 | 2022-06-15 | 9.8.1 |
| 1.0.0 | 2022-05-17 | 9.8.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 4.7.0 | requirement | Upgraded org.bouncycastle:bcpg-jdk18on, bcpkix-jdk18on, bcprov-jdk18on to version 1.85 | org.bouncycastle:bcpg-jdk18on, org.bouncycastle:bcpkix-jdk18on, org.bouncycastle:bcprov-jdk18on |  |
| 4.6.0 | removal | Dependency on netty library removed to reduce risk of transitive CVEs (Tickets #280205, #280754, #281745, #282429) | netty |  |
| 4.6.0 | improvement | Improved microflow call chain and dependencies to separate configuration business logic from UI actions |  |  |
| 4.5.0 | breaking | PKCE now enabled by default to improve security, without dependency on IdP's well-known endpoint | PKCE |  |
| 4.5.0 | breaking | Removed Anonymous user-role and related artifacts to simplify security model and reduce configuration dependencies | Anonymous user-role |  |
| 4.5.0 | requirement | Upgraded netty-codec-http to version 4.2.14.Final | netty-codec-http |  |
| 4.5.0 | security | Fixed CVE-2026-3505 |  |  |
| 4.4.0 | removal | Removed dependencies on Encryption module and Nanoflow. See documentation for migration | Encryption module, Nanoflow |  |
| 4.4.0 | removal | Ready-to-use token view page removed; UI snippet provided as template for custom implementations | token view page |  |
| 4.4.0 | breaking | Admins can only view decrypted content of their own token (Tickets #275225, #275311, #275327, #275656) |  |  |
| 4.4.0 | security | Fixed CVE-2025-40571. See Siemens Security Advisory SSA-726617 (Ticket #243660) |  |  |
| 4.4.0 | requirement | Upgraded netty-codec-http to version 4.2.12.Final | netty-codec-http |  |
| 4.2.1 | removal | MxReflection module dependency removed for better developer/upgrade experience | MxReflection module |  |
| 4.2.1 | removal | UserCommons migration logic removed | UserCommons migration logic |  |
| 4.2.1 | breaking | Translations removed; custom translations not overwritten when upgrading |  |  |
| 4.2.1 | improvement | AuthAttempt clean up logic refactored | AuthAttempt |  |
| 4.2.1 | breaking | Unlimited entity attributes lengths lowered down |  |  |
| 4.2.1 | breaking | Admin and User role Token entity access revised | Token entity |  |
| 4.2.1 | requirement | Upgraded io.netty:netty-codec-http to version 4.2.9.Final | io.netty:netty-codec-http |  |
| 4.2.1 | requirement | Upgraded com.nimbusds:nimbus-jose-jwt to version 10.5 | com.nimbusds:nimbus-jose-jwt |  |
| 4.2.1 | requirement | Upgraded commons-codec to version 1.19.0 | commons-codec |  |
| 4.2.0 | improvement | Easier to upgrade: ASU_STARTUP microflow moved under _USE ME folder and no longer includes automated user commons migration | ASU_STARTUP |  |
| 4.2.0 | migration-step | Migration logic for upgrading from versions below v3.0.0 moved to dedicated microflow under _USE ME → Migration |  |  |
| 4.2.0 | requirement | Upgraded org.apache.velocity:velocity-engine-core to version 2.4.1 | org.apache.velocity:velocity-engine-core |  |
| 4.2.0 | requirement | Upgraded com.nimbusds:nimbus-jose-jwt to version 10.4.1 | com.nimbusds:nimbus-jose-jwt |  |
| 4.2.0 | requirement | Upgraded org.apache.commons:commons-lang3 to version 3.19.0 | org.apache.commons:commons-lang3 |  |
| 4.2.0 | requirement | Added io.netty:netty-codec-http version 4.2.5.Final | io.netty:netty-codec-http |  |
| 4.2.0 | removal | Removed com.auth0:jwks-rsa and com.auth0:java-jwt dependencies | com.auth0:jwks-rsa, com.auth0:java-jwt |  |
| 4.2.0 | migration-step | Delete all Java libraries from userlib folder of old OIDC SSO module version before upgrading to avoid conflicting Java libraries |  |  |
| 4.1.1 | requirement | Version 4.1.1 for apps on Mendix 10.21.0; ensures compatibility with Mendix 11 |  |  |
| 4.1.0 | requirement | Version 4.1.0 for apps on Mendix 10.21.1 or higher |  |  |
| 4.1.0 | breaking | Anonymous user access no longer required; end-users can authenticate via /oauth/v2/login endpoint with multiple IdPs support | Anonymous user |  |
| 4.1.0 | breaking | Removed dependency on Administration module by replacing Administration.Account references with System.User (Ticket #229453) | Administration module |  |
| 4.1.0 | improvement | Improved ASU_OIDC_Startup to auto-create UserProvisioning objects for ClientConfigurations with empty UserProvisioningFlow (Ticket #238161) | ASU_OIDC_Startup |  |
| 4.1.0 | breaking | Fixed ReturnURL length in ClientConfig to 2048 characters to resolve login errors (Ticket #240374) | ReturnURL |  |
| 4.1.0 | security | Fixed CVE-2025-40571. See Siemens Security Advisory SSA-726617 (Ticket #243660) |  |  |
| 4.0.1 | breaking | Removed dependency on Administration module by replacing Administration.Account references with System.User (Ticket #229453) | Administration module |  |
| 4.0.1 | improvement | Improved ASU_OIDC_Startup to auto-create UserProvisioning objects for ClientConfigurations with empty UserProvisioningFlow (Ticket #238161) | ASU_OIDC_Startup |  |
| 4.0.1 | breaking | Fixed ReturnURL length in ClientConfig to 2048 characters to resolve login errors (Ticket #240374) | ReturnURL |  |
| 4.0.1 | security | Fixed CVE-2025-40571. See Siemens Security Advisory SSA-726617 (Ticket #243660) |  |  |
| 4.0.0 | requirement | Version 4.0.0 for apps on Mendix 10.12.10 or higher |  |  |
| 4.0.0 | removal | Removed OIDC.ACT_Account_RetrieveAccount microflow from _USE ME folder; now handled within module | OIDC.ACT_Account_RetrieveAccount |  |
| 3.6.0 | removal | Dependency on netty library removed to reduce risk of transitive CVEs (Tickets #280205, #280754, #281745, #282429) | netty |  |
| 3.5.1 | requirement | Upgraded io.netty:netty-codec-http to version 4.2.15.Final | io.netty:netty-codec-http |  |
| 3.5.0 | removal | Ready-to-use token view page removed; UI snippet provided as template for custom implementations | token view page |  |
| 3.5.0 | breaking | Admins can only view decrypted content of their own token (Tickets #275225, #275311, #275327, #275656) |  |  |
| 3.5.0 | security | Fixed CVE-2025-40571. See Siemens Security Advisory SSA-726617 (Ticket #243660) |  |  |
| 3.5.0 | requirement | Upgraded netty-codec-http to version 4.2.12.Final | netty-codec-http |  |
| 3.5.0 | requirement | Upgraded jackson-core to version 2.21.2 | jackson-core |  |
| 3.5.0 | migration-step | Delete all Java libraries from userlib folder of old OIDC SSO module version before upgrading to avoid conflicting Java libraries |  |  |
| 3.4.0 | requirement | Upgraded jackson-annotations to version 2.21.0 | jackson-annotations |  |
| 3.4.0 | requirement | Upgraded jackson-core to version 2.21.1 | jackson-core |  |
| 3.4.0 | migration-step | Delete all Java libraries from userlib folder of old OIDC SSO module version before upgrading to avoid conflicting Java libraries |  |  |
| 3.3.1 | improvement | AuthAttempt clean up logic refactored | AuthAttempt |  |
| 3.3.1 | breaking | Admin and User role Token entity access revised | Token entity |  |
| 3.3.1 | breaking | Translations removed; custom translations not overwritten when upgrading |  |  |
| 3.3.1 | breaking | Unlimited entity attributes lengths lowered down |  |  |
| 3.3.0 | feature | Token Encryption support has been added for compliance (Ticket #258462) |  |  |
| 3.3.0 | improvement | Improved XPath constraint for admin access to persisted tokens (Ticket #243660) |  |  |
| 3.3.0 | improvement | Improved implementation of nonce features |  |  |
| 3.3.0 | requirement | Upgraded com.nimbusds:nimbus-jose-jwt to version 10.4.1 | com.nimbusds:nimbus-jose-jwt |  |
| 3.3.0 | requirement | Added io.netty:netty-codec-http:4.2.5.Final | io.netty:netty-codec-http |  |
| 3.3.0 | migration-step | Delete all Java libraries used by old OIDC SSO module from userlib folder before upgrading |  |  |
| 3.2.1 | improvement | Improved ASU_OIDC_Startup to auto-create UserProvisioning objects for ClientConfigurations with empty UserProvisioningFlow (Ticket #238161) | ASU_OIDC_Startup |  |
| 3.2.1 | fix | Fixed ReturnURL length in ClientConfig to 2048 characters to resolve login errors (Ticket #240374) | ReturnURL |  |
| 3.2.0 | feature | Support of Microflow URLs with Query Parameters for continuation after login redirection |  |  |
| 3.2.0 | improvement | Enhanced user login by preventing logins for inactive users |  |  |
| 3.2.0 | feature | Supporting apps with subpath routing |  |  |
| 3.2.0 | fix | Fixed issue related to selected scope in deploytime Configuration (Ticket #224987) |  |  |
| 3.2.0 | requirement | Upgraded to Studio Pro version 9.24.18 |  |  |
| 3.2.0 | improvement | Improved MxModelReflection handling by refreshing modules to ensure backward compatibility | MxModelReflection |  |
| 3.2.0 | feature | New Cookie to clear cached session data during user login (Ticket #201728) |  |  |
| 3.2.0 | fix | Fixed issue related to Progressive Web App offline (Ticket #229872) |  |  |
| 3.2.0 | requirement | Upgraded com.nimbusds:nimbus-jose-jwt to version 9.41.2 (Ticket #224507,#224508,#224815,#229247) | com.nimbusds:nimbus-jose-jwt |  |
| 3.2.0 | requirement | Upgraded com.auth0:jwks-rsa to version 0.22.1 | com.auth0:jwks-rsa |  |
| 3.2.0 | migration-step | Delete all Java libraries used by old OIDC SSO module from userlib folder before upgrading |  |  |
| 3.1.0 | feature | Capability to validate Access Tokens (OAuth bearer tokens, JWT tokens) issued via OAuth Client Credential grant |  |  |
| 3.1.0 | feature | Configurations can be done from CI/CD pipeline at deploy-time using Application Constants or via Admin configuration UI at runtime |  |  |
| 3.1.0 | breaking | Renamed OIDC.Startup microflow as OIDC.ASU_OIDC_Startup | OIDC.Startup, OIDC.ASU_OIDC_Startup | OIDC.ASU_OIDC_Startup |
| 3.0.1 | security | Enhanced security by resolving weak sha1 algorithm detection in package-lock.json (Ticket#215455) |  |  |
| 3.0.1 | fix | Fixed base64 decoding issue in AzureRoleParse to handle JWT payloads with underscores (Ticket#217222) | AzureRoleParse |  |
| 3.0.1 | fix | Fixed auto-commit issue in OIDC.CodeChallengeMethodsSet during Automated Deploy-time SSO Configuration (Ticket#217387) | OIDC.CodeChallengeMethodsSet |  |
| 3.0.1 | removal | Removed Snip_Login_Automatic snippet from module; recommend using Snip_Login_Button snippet instead | Snip_Login_Automatic | Snip_Login_Button |
| 3.0.0 | feature | Users can be provisioned to Custom user entity without customizing the module |  |  |
| 3.0.0 | feature | When using Entra ID, default attribute mapping can be used; no need to configure attribute mapping |  |  |
| 3.0.0 | feature | User provisioning can set user_type (internal/external) based on IdP-level configuration |  |  |
| 3.0.0 | feature | User provisioning allows setting user's preferred language and timezone based on SSO response |  |  |
| 3.0.0 | feature | User provisioning can set default userrole, regardless of Access Token |  |  |
| 3.0.0 | feature | JIT user provisioning can be disabled, e.g. when users provisioned only via Administration module |  |  |
| 3.0.0 | feature | Select any custom microflow prefixed with 'OIDC_CustomUserParsing' for user provisioning |  |  |
| 3.0.0 | feature | Forward-compatible with Upcoming SCIM Module |  |  |
| 3.0.0 | requirement | Added UserCommons Module as new dependency for OIDC SSO | UserCommons |  |
| 3.0.0 | requirement | Mandatory to Set OIDC.Startup microflow as After Startup within settings | OIDC.Startup |  |
| 3.0.0 | fix | Fixed issue related to access token parsing microflow (Ticket#177243) |  |  |
| 3.0.0 | fix | Fixed issue related to Scope Value Attribute |  |  |
| 2.4.0 | feature | Support of Progressive Web App (PWA) |  |  |
| 2.4.0 | feature | Support of Page and Microflow URLs |  |  |
| 2.4.0 | feature | Support for Additional Scopes on deploytime Configuration |  |  |
| 2.4.0 | fix | Fixed issue with Token expires_in attribute (Ticket#206386) |  |  |
| 2.4.0 | requirement | Upgraded com.nimbusds:nimbus-jose-jwt to version 9.37.3 | com.nimbusds:nimbus-jose-jwt |  |
| 2.4.0 | migration-step | Delete all Java libraries used by old OIDC SSO module from userlib folder before upgrading |  |  |
| 2.3.2 | fix | Encoded the escaping special characters in URL for OIDC |  |  |
| 2.3.2 | requirement | Upgraded com.fasterxml.jackson.core:jackson-databind to 2.16.0 | com.fasterxml.jackson.core:jackson-databind |  |
| 2.3.2 | requirement | Upgraded com.fasterxml.jackson.core:jackson-annotations to 2.16.0 | com.fasterxml.jackson.core:jackson-annotations |  |
| 2.3.2 | requirement | Upgraded com.fasterxml.jackson.core:jackson-core to 2.16.0 | com.fasterxml.jackson.core:jackson-core |  |
| 2.3.2 | migration-step | Delete all Java libraries used by old OIDC SSO module from userlib folder before upgrading |  |  |
| 2.3.1 | fix | Fixed Java dependency issue in migration file for Mendix 10 compatibility |  |  |
| 2.3.1 | requirement | Upgraded org.json:json from 20230227 to 20231013 | org.json:json |  |
| 2.3.1 | migration-step | Delete all Java libraries used by old OIDC SSO module from userlib folder before upgrading |  |  |
| 2.3.0 | feature | Automation of SSO configuration via Application Constants set in CI/CD pipeline at deploytime |  |  |
| 2.3.0 | feature | Influence authentication at IDP using ACR feature |  |  |
| 2.3.0 | feature | Out-of-the-box microflow for standardized access token parsing for interaction with OIDC Provider module |  |  |
| 2.3.0 | requirement | Included migration file for Java dependencies for Studio Pro 10 compatibility |  |  |
| 2.3.0 | improvement | Enhanced error handling messages for authorized API calls (Ticket#173297) |  |  |
| 2.3.0 | removal | Dependency on 'Native Mobile Resources' module has been removed | Native Mobile Resources |  |
| 2.2.0 | improvement | Improvement for redirect URLs which may or may not have trailing slash '/' |  |  |
| 2.2.0 | fix | Fixed Mendix 10 compatibility issue (Ticket#190175) |  |  |
| 2.2.0 | requirement | Upgraded to Studio Pro v9.24.2 |  |  |
| 2.2.0 | requirement | Upgraded com.nimbusds:nimbus-jose-jwt to version 9.31 | com.nimbusds:nimbus-jose-jwt |  |
| 2.2.0 | migration-step | Delete all Java libraries used by old OIDC SSO module from userlib folder before upgrading |  |  |
| 2.1.1 | requirement | Upgraded org.json:json from 20220924 to 20230227 | org.json:json |  |
| 2.1.1 | migration-step | Delete all Java libraries used by old OIDC SSO module from userlib folder before upgrading |  |  |
| 2.1.0 | requirement | Upgraded to Mendix Studio Pro v9.22.0 |  |  |
| 2.0.0 | feature | Added support for authorizing access to Mendix back-end app using access token |  |  |
| 2.0.0 | breaking | Simplified structure for access token parsing microflows; breaking change for custom access token parsing microflows | ACT_Token_CustomATPRetrieveRoles |  |
| 2.0.0 | feature | Added introspection of Access Tokens and introspection endpoint field on OIDC configuration screen |  |  |
| 2.0.0 | feature | Added two out-of-the-box microflows for access token parsing (PIB and AzureAD) |  |  |
| 2.0.0 | improvement | Improved conditional check of handleAuthorizationCode microflow (Ticket#170579) |  |  |
| 2.0.0 | fix | Fixed issue related to cookies in Mendix studio pro-9.20 (Ticket#173282) |  |  |
| 1.1.1 | feature | Automatic Redirect to login page of Client if only one OIDC Client configured |  |  |
| 1.1.1 | requirement | Replaced org.json with org.json:json-20220924 | org.json:json |  |
| 1.1.1 | requirement | Upgraded com.fasterxml.jackson.core:jackson-core to 2.14.1 | com.fasterxml.jackson.core:jackson-core |  |
| 1.1.1 | requirement | Upgraded com.fasterxml.jackson.core:jackson-databind to 2.14.1 (Ticket #169884,#171349) | com.fasterxml.jackson.core:jackson-databind |  |
| 1.1.1 | requirement | Upgraded com.fasterxml.jackson.core:jackson-annotations to 2.14.1 | com.fasterxml.jackson.core:jackson-annotations |  |
| 1.1.1 | migration-step | Delete all Java libraries used by old OIDC SSO module from userlib folder before upgrading |  |  |
| 1.1.0 | feature | Added support for 'client_secret_basic' client authentication method; preferred over 'client_secret_post' |  |  |
| 1.1.0 | removal | Removed beta implementation of private_key_jwt client authentication | private_key_jwt |  |
| 1.1.0 | improvement | Configuration experience improved; now enforces mandatory fields: client_id and client_secret |  |  |
| 1.1.0 | feature | Added support for OIDC nonce parameter; usage mitigates replay attacks |  |  |
| 1.1.0 | removal | Removed PKCE configuration from UI; module auto-detects PKCE support through well-known endpoint |  |  |
| 1.1.0 | requirement | Upgraded url-parse package to 1.5.10 (Ticket #152019) | url-parse |  |
| 1.1.0 | requirement | Upgraded querystringify to 2.2.0 | querystringify |  |
| 1.0.1 | requirement | Jackson libraries upgraded to version 2.13.3 (Ticket #150849) | com.fasterxml.jackson.core: jackson-databind, com.fasterxml.jackson.core: jackson-annotations, com.fasterxml.jackson.core: jackson-core |  |
| 1.0.1 | migration-step | Delete all Java libraries used by old OIDC SSO module from userlib folder before upgrading |  |  |
| 1.0.0 | requirement | OIDC SSO supported for Mendix 9 onwards; no version available for Mendix 8 or 7 |  |  |
| 1.0.0 | known-issue | Usage with native mobile apps is not yet supported |  |  |

## OIL - Omnichannel Integration Layer <a id="118344"></a>
Solution, Magnus Green B.V., Partner, [marketplace](https://marketplace.mendix.com/link/component/118344)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2021-09-02 | ? |

## Okta Connector <a id="119164"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/119164)

| version | published | min Mendix |
|---|---|---|
| 2.0.3 | 2024-10-30 | 9.24.29 |
| 2.0.2 | 2023-11-17 | 9.24.12 |
| 2.0.1 | 2023-11-09 | 9.24.10 |
| 2.0.0 | 2023-10-30 | 9.24.10 |
| 1.0.0 | 2021-12-20 | 8.12.7 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.0.3 | requirement | Upgrade to Studio Pro 9.24.29 |  |  |
| 2.0.2 | requirement | Upgrade to Studio Pro 9.24.12 |  |  |
| 2.0.2 | feature | Added support for next links to retrieve paginated results |  |  |
| 2.0.0 | breaking | Cleaned up module, potentially breaking changes |  |  |
| 2.0.0 | requirement | Upgrade to Studio Pro 9.24.10 |  |  |

## OPC UA Client Connector <a id="117391"></a>
Service, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/117391)

| version | published | min Mendix |
|---|---|---|
| 1.1.0 | 2022-03-29 | 9.6.10 |
| 1.0.0 | 2021-04-27 | 8.17.0 |

## OPC UA Connector <a id="230843"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/230843)

| version | published | min Mendix |
|---|---|---|
| 2.3.0 | 2026-08-13 | 10.24.0 |
| 2.2.0 | 2026-04-02 | 10.24.0 |
| 2.1.0 | 2026-02-18 | 10.24.0 |
| 2.0.3 | 2025-09-25 | 10.21.0 |
| 2.0.2 | 2025-08-20 | 10.21.0 |
| 2.0.1 | 2025-06-12 | 10.21.0 |
| 2.0.0 | 2025-05-12 | 10.21.0 |
| 1.3.0 | 2026-08-13 | 9.24.3 |
| 1.2.0 | 2026-04-02 | 9.24.3 |
| 1.1.3 | 2026-02-18 | 9.24.3 |
| 1.1.2 | 2025-09-25 | 9.24.3 |
| 1.1.1 | 2025-08-20 | 9.24.3 |
| 1.1.0 | 2025-04-10 | 9.24.3 |
| 1.0.1 | 2024-11-20 | 9.24.3 |
| 1.0.0 | 2024-09-23 | 9.24.3 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.3.0 | improvement | Improved automatic recovery from stale OPC UA sessions. | OPC UA sessions |  |
| 2.3.0 | feature | Added automatic recreation of missing subscriptions after reconnection or transfer failures. | subscriptions |  |
| 2.3.0 | improvement | Improved validation, error handling, logging, and thread safety. |  |  |
| 2.3.0 | security | Updated Netty and Bouncy Castle dependencies to address known vulnerabilities. | Netty, Bouncy Castle |  |
| 2.3.0 | improvement | Improved certificate handling, browsing, and monitored-item state management. | certificate handling, browsing, monitored-item state management |  |
| 2.2.0 | feature | Added advanced configuration options to influence the server's certificate validation. | certificate validation |  |
| 2.1.0 | requirement | Updated to Mendix version 10.24.0. | Mendix |  |
| 2.1.0 | improvement | Updated netty-io dependencies. | netty-io |  |
| 2.0.3 | improvement | Updated dependencies of bouncycastle and netty. | bouncycastle, netty |  |
| 2.0.2 | breaking | Removed Before delete event from Subscription entity. | Subscription |  |
| 2.0.2 | fix | Fixed dependencies in module settings. | module settings |  |
| 2.0.1 | migration-step | Replaced deprecated context() method with getContext(). | context() | getContext() |
| 2.0.0 | requirement | Upgraded to Mendix version 10.21.0. | Mendix |  |
| 1.3.0 | improvement | Improved automatic recovery from stale OPC UA sessions. | OPC UA sessions |  |
| 1.3.0 | feature | Added automatic recreation of missing subscriptions after reconnection or transfer failures. | subscriptions |  |
| 1.3.0 | improvement | Improved validation, error handling, logging, and thread safety. |  |  |
| 1.3.0 | security | Updated Netty and Bouncy Castle dependencies to address known vulnerabilities. | Netty, Bouncy Castle |  |
| 1.3.0 | improvement | Improved certificate handling, browsing, and monitored-item state management. | certificate handling, browsing, monitored-item state management |  |
| 1.2.0 | feature | Added advanced configuration options to influence the server's certificate validation. | certificate validation |  |
| 1.1.3 | improvement | Updated bouncycastle and netty-io dependencies. | bouncycastle, netty-io |  |
| 1.1.2 | improvement | Updated dependencies of bouncycastle and netty. | bouncycastle, netty |  |
| 1.1.1 | breaking | Removed Before delete event from Subscription entity. | Subscription |  |
| 1.1.1 | fix | Fixed dependencies so correct libraries load when upgrading to Mendix 10 or importing to Mendix 10. |  |  |
| 1.1.0 | security | Fixed vulnerabilities in used libraries. |  |  |
| 1.0.1 | improvement | Connector is now fully compatible with React client in 10.12+. | React client |  |

## Opcenter Execution Foundation Starter Kit <a id="208792"></a>
Industry Template, Siemens, Siemens, [marketplace](https://marketplace.mendix.com/link/component/208792)

| version | published | min Mendix |
|---|---|---|
| 8.0.0 | 2026-07-29 | 11.12.0 |
| 7.0.0 | 2026-02-19 | 11.6.3 |
| 6.0.0 | 2025-09-01 | 10.24.0 |
| 5.1.0 | 2025-05-27 | 10.18.4 |
| 5.0.0 | 2025-02-07 | 10.18.0 |
| 4.1.0 | 2024-11-14 | 10.12.5 |
| 4.0.0 | 2024-08-02 | 10.12.0 |
| 3.1.0 | 2024-05-27 | 10.6.5 |
| 3.0.0 | 2024-02-08 | 10.6.3 |
| 2.1.0 | 2023-11-13 | 9.24.4 |
| 2.0.0 | 2023-06-15 | 9.24.0 |
| 1.0.0 | 2023-04-06 | 9.18.2 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 8.0.0 | requirement | Upgraded to Mendix Studio Pro 11.12.0 minimum requirement |  |  |
| 8.0.0 | requirement | Updated Administration module to 4.3.2, Atlas Core to 3.19.0, Community Commons to 11.5.1, Data Widgets to 3.10.0, Nanoflow Commons to 6.2.1, Web Actions to 2.11.2 | Administration module, Atlas Core, Community Commons, Data Widgets, Nanoflow Commons, Web Actions |  |
| 7.0.0 | requirement | Upgraded to Mendix Studio Pro 11.6.3 minimum requirement |  |  |
| 7.0.0 | requirement | Updated Administration module to 4.3.2, Atlas Core to 3.19.0, Community Commons to 11.3.0, Data Widgets to 2.31.0, Nanoflow Commons to 6.1.1, Web Actions to 2.11.1 | Administration module, Atlas Core, Community Commons, Data Widgets, Nanoflow Commons, Web Actions |  |
| 6.0.0 | requirement | Upgraded to Mendix Studio Pro 10.24.0 minimum requirement |  |  |
| 5.1.0 | requirement | Upgraded to Mendix Studio Pro 10.18.4 minimum requirement |  |  |
| 5.0.0 | requirement | Upgraded to Mendix Studio Pro 10.18.0 minimum requirement |  |  |
| 4.1.0 | requirement | Upgraded to Mendix Studio Pro 10.12.5 minimum requirement |  |  |
| 4.0.0 | requirement | Upgraded to Mendix Studio Pro 10.12.0 minimum requirement |  |  |
| 3.1.0 | requirement | Upgraded to Mendix 10.6.5 minimum requirement |  |  |
| 3.0.0 | requirement | Upgraded to Mendix 10.6.3 minimum requirement |  |  |
| 3.0.0 | breaking | Replaced existing Get/invoke command example with complete implementation example of UoM screen |  |  |
| 3.0.0 | requirement | Upgraded Add-ons EXFN_Authentication, EX_FN_ServiceLayer, and EX_FN_CrossNavigation to version 3.0.0 | EXFN_Authentication, EX_FN_ServiceLayer, EX_FN_CrossNavigation |  |
| 3.0.0 | requirement | Updated OpcenterEXFN_DISW_DesignSystem module | OpcenterEXFN_DISW_DesignSystem |  |
| 2.1.0 | requirement | Upgraded to Mendix 9.24.4 minimum requirement |  |  |
| 2.1.0 | fix | Fixed 404 error returned when refreshing a page |  |  |
| 2.1.0 | fix | Fixed issue about reloading the same page; now redirects user to specific page after login or page refresh |  |  |
| 2.1.0 | requirement | Upgraded Add-ons EXFN_Authentication and EX_FN_ServiceLayer to version 2.1.0 | EXFN_Authentication, EX_FN_ServiceLayer |  |
| 2.1.0 | feature | Added new Add-on EXFN_CrossNavigation | EXFN_CrossNavigation |  |
| 2.1.0 | requirement | Updated OpcenterEXFN_DISW_DesignSystem module | OpcenterEXFN_DISW_DesignSystem |  |
| 2.0.0 | requirement | App rebuilt with Mendix 9.24.0 |  |  |
| 2.0.0 | improvement | Fixes and improvements to Authentication Module | Authentication Module |  |
| 2.0.0 | requirement | Upgraded versions of marketplace modules |  |  |

## OpenAI Connector <a id="220472"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/220472)

| version | published | min Mendix |
|---|---|---|
| 9.2.0 | 2026-08-13 | 11.12.2 |
| 9.1.0 | 2026-07-22 | 11.12.1 |
| 9.0.0 | 2026-07-02 | 11.12.0 |
| 8.1.0 | 2026-05-28 | 10.24.13 |
| 8.0.1 | 2026-03-10 | 10.24.13 |
| 7.4.0 | 2026-01-19 | 10.24.0 |
| 7.3.0 | 2025-10-29 | 10.24.0 |
| 7.2.0 | 2025-08-29 | 10.24.0 |
| 7.1.0 | 2025-08-13 | 10.24.0 |
| 7.0.0 | 2025-08-08 | 10.24.0 |
| 6.1.0 | 2025-07-21 | 10.21.0 |
| 6.0.0 | 2025-07-02 | 10.21.0 |
| 5.2.0 | 2025-06-13 | 10.21.0 |
| 5.1.0 | 2025-05-09 | 10.21.0 |
| 5.0.0 | 2025-04-07 | 10.21.0 |
| 4.3.0 | 2025-03-14 | 9.24.2 |
| 4.2.0 | 2025-02-14 | 9.24.2 |
| 4.1.0 | 2025-02-03 | 9.24.2 |
| 4.0.0 | 2025-01-13 | 9.24.2 |
| 3.4.1 | 2024-10-16 | 9.24.2 |
| 3.3.0 | 2024-09-19 | 9.24.2 |
| 3.2.0 | 2024-08-28 | 9.24.2 |
| 3.1.1 | 2024-07-31 | 9.24.2 |
| 3.1.0 | 2024-07-25 | 9.24.2 |
| 3.0.0 | 2024-06-24 | 9.24.2 |
| 2.7.1 | 2024-05-16 | 9.24.0 |
| 2.2.0 | 2024-02-26 | 9.24.0 |
| 2.0.0 | 2024-01-25 | 9.24.0 |
| 1.3.0 | 2024-01-11 | 9.24.0 |
| 1.2.0 | 2023-12-28 | 9.24.0 |
| 1.1.0 | 2023-12-21 | 9.24.0 |
| 1.0.0 | 2023-12-20 | 9.24.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 9.2.0 | requirement | Upgrade to Mendix 11.12.2. |  |  |
| 9.2.0 | feature | Streaming responses now supported for text generation models with ConversationalUI, displaying response word by word in real time. |  |  |
| 9.2.0 | improvement | Default deployed model objects during configuration setup updated to contain gpt-5.6 models. Reasoning not active for 5.6 models due to API limitations. |  |  |
| 9.1.0 | requirement | Upgrade to Mendix 11.12.1. |  |  |
| 9.1.0 | feature | Model documents in Agent Editor now support Azure (AI Foundry) as model provider for text generation. Module required for Agent Editor with these Model documents. |  |  |
| 9.0.0 | requirement | Module upgraded to Mendix 11.12.0. |  |  |
| 9.0.0 | removal | Data migration microflows from previous major version removed. For multi-version upgrades, consult migration guide. |  |  |
| 8.1.0 | improvement | Request headers added to text, embeddings and image generation operations to support Snowflake Cortex through OpenAI-compatible API. |  |  |
| 8.0.1 | breaking | Module aligned with latest ConsumedKnowledgeBase and ConsumedMCPService changes. Breaking change requiring migration to prevent data/functionality loss. | ConsumedKnowledgeBase, ConsumedMCPService |  |
| 8.0.1 | requirement | Module version compatible with GenAI Commons 6.0.0. | GenAI Commons |  |
| 7.4.0 | improvement | Module compatible with latest GenAI Commons version. Newer models GPT-5.2, o1, o3, o4-mini now supported and added by default. | GenAI Commons |  |
| 7.1.0 | feature | For tool calling, GenAICommons ArgumentInput objects mapped to OpenAI API expected input schema, enabling connector use in MCP Client cases. | GenAICommons ArgumentInput |  |
| 7.0.0 | requirement | Module upgraded to Mendix Studio Pro version 10.24. |  |  |
| 6.1.0 | improvement | Connector compatible with newest GenAI Commons. Tool microflows can accept multiple primitive input parameters of various types. | GenAI Commons |  |
| 6.0.0 | feature | Added support for Azure AI Search. Configure Azure resources in UI, retrieve available indexes, persisted in database. Index entity specializes GenAICommons.DeployedKnowledgeBase. |  |  |
| 6.0.0 | removal | Model gpt-4.5-preview removed from default models due to upcoming OpenAI deprecation. | gpt-4.5-preview |  |
| 5.2.0 | breaking | Renamed OpenAIFileContent entity to OpenAIImageContent since attributes only relevant for images. Toolbox actions renamed accordingly. | OpenAIFileContent, OpenAIImageContent | OpenAIImageContent |
| 5.0.0 | requirement | Module updated to Mendix Studio Pro 10.21.0. |  |  |
| 4.1.0 | feature | Module pages updated to support React client. Unsupported widgets replaced by supported ones. Module usable in React client enabled apps from SP 10.18 onwards. |  |  |
| 4.0.0 | breaking | Connector compatible with simplified GenAI Commons toolbox. Chat Completions, Embeddings and Image Generation operations moved to GenAICommons. Pass DeployedModel instead of Connection. | Chat Completions, Embeddings, Image Generation |  |
| 4.0.0 | migration-step | In custom microflows, replace OpenAI operations for chat completions, image generation and embeddings with equivalent GenAI Commons operations from Toolbox 'GenAI (Generate)' category. |  |  |
| 4.0.0 | migration-step | New operations require DeployedModel input, type OpenAIDeployedModel for OpenAI. Admin user must redo configuration for these objects to exist in database. | DeployedModel, OpenAIDeployedModel |  |
| 3.4.1 | migration-step | Added migration file missing in release 3.4.0. |  |  |
| 3.4.1 | improvement | Many chat completions operations replaced by new GenAICommons action. Requires newest GenAICommons version. Improved log messages for failed operations. | GenAICommons |  |
| 3.3.0 | requirement | Updating GenAI Commons module required for this connector version to compile. | GenAI Commons |  |
| 3.2.0 | improvement | Connector compatible with newest GenAI Commons version 1.2.0. Domain model documentation updated. | GenAI Commons |  |
| 3.1.0 | improvement | Module compatible with new GenAI Commons version for Embeddings and Image Generations. Enables easy model provider switching and PgVector Knowledge Base integration. | GenAI Commons, Embeddings, Image Generations |  |
| 3.0.0 | breaking | OpenAI connector reuses generic entities and operations from GenAI Commons. Updating causes errors in existing chat completions implementations. | Chat Completions |  |
| 3.0.0 | migration-step | Change input parameters of chat completions operations and post-processing of response. See OpenAI Showcase App for examples. |  |  |
| 3.0.0 | removal | Complex 'Chat Completions (advanced)' operation removed. Replace with regular 'Chat Completions (with history)' operation. | Chat Completions (advanced) | Chat Completions (with history) |
| 2.7.1 | migration-step | Added userlibs missing in release 2.7.0. |  |  |
| 2.2.0 | breaking | Removed all 'Show message' activities from exposed operations, replaced with log messages. |  |  |
| 2.0.0 | breaking | Removed default models per operation from Configuration entity. Changed Model input parameters from Enumeration to String for flexibility. | Configuration, Model |  |
| 2.0.0 | breaking | Introduced AbstractUsage and ConfigurationTest entities. ChatCompletionsUsage is now specialization of AbstractUsage. Removed entity access from ChatCompletionsSession and ChatCompletionsSessionMessage. | AbstractUsage, ConfigurationTest, ChatCompletionsUsage, ChatCompletionsSession, ChatCompletionsSessionMessage |  |
| 1.2.0 | requirement | Added dependency on Community Commons Marketplace module; must be included if not already in app. | Community Commons |  |
| 1.2.0 | breaking | ChatCompletions_Execute_WithHistory now returns response text (string) directly instead of complex structure. | ChatCompletions_Execute_WithHistory |  |

## OpenIDConnect Single Sign-on Community Support (OIDC, OAuth2, SSO) <a id="117529"></a>
Module, Mendix, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/117529)

| version | published | min Mendix |
|---|---|---|
| 3.3.3 | 2023-01-25 | 9.8.1 |
| 3.3.1 | 2022-05-02 | 9.8.1 |
| 3.3.0 | 2022-04-27 | 9.8.1 |
| 3.2.0 | 2022-04-16 | 9.8.1 |
| 3.1.0 | 2021-11-29 | 8.18.0 |
| 2.2.0 | 2021-07-30 | 8.12.0 |
| 2.1.0 | 2021-07-23 | 8.12.0 |
| 1.0.0 | 2021-05-24 | 8.12.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 3.3.3 | requirement | Added support for Mendix 9.20+ | Java dependencies |  |
| 3.3.3 | migration-step | Updated Java dependencies - CLEAN UP YOUR USERLIB FOLDER | userlib |  |
| 3.3.1 | fix | Fix for race condition bug during native mobile login | native mobile login |  |
| 3.3.0 | fix | Fix for native login error | native login |  |
| 3.2.0 | requirement | Added support for Mendix 9.8 and up, where AuthTokens are now encrypted | AuthTokens |  |
| 3.1.0 | feature | Added support for the DeepLink module | DeepLink module |  |
| 2.2.0 | fix | Scopes were getting double-url-encoded causing errors during login | scopes |  |
| 2.1.0 | removal | Removes dependency on Administration module by moving OIDC.Token association from Administration.Account to System.User | Administration module |  |
| 2.1.0 | breaking | Replaces configuration pages with snippets to improve portability and dependency on specific page layouts | configuration pages |  |
| 2.1.0 | removal | Removes Native Mobile Resources widgets from package - correct version installed from Marketplace for Mendix 8 or 9 | Native Mobile Resources widgets |  |

## Option Selector <a id="245825"></a>
Widget, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/245825)

| version | published | min Mendix |
|---|---|---|
| 1.2.0 | 2026-09-18 | 10.7.0 |
| 1.1.2 | 2026-06-08 | 10.7.0 |
| 1.1.1 | 2026-02-24 | 10.7.0 |
| 1.1.0 | 2025-10-22 | 10.7.0 |
| 1.0.0 | 2025-08-25 | 10.7.0 |

## OQLModule <a id="66876"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/66876)

| version | published | min Mendix |
|---|---|---|
| 5.1.0 | 2026-07-15 | 11.6.0 |
| 5.0.0 | 2026-03-23 | 11.6.0 |
| 4.2.0 | 2026-07-15 | 10.21.0 |
| 4.1.2 | 2026-03-05 | 10.21.0 |
| 4.1.1 | 2025-12-18 | 10.21.0 |
| 4.1.0 | 2025-09-26 | 10.21.0 |
| 4.0.0 | 2025-06-24 | 10.21.0 |
| 3.1.0 | 2026-07-15 | 9.24.36 |
| 3.0.0 | 2025-06-24 | 9.18.4 |
| 2.17.1 | 2025-06-16 | 9.18.0 |
| 2.17.0 | 2024-08-12 | 9.18.0 |
| 2.16.0 | 2024-06-19 | 9.18.0 |
| 2.15.0 | 2024-05-31 | 9.18.0 |
| 2.14.0 | 2024-05-02 | 9.18.0 |
| 2.13.0 | 2024-01-29 | 9.18.0 |
| 2.12.0 | 2023-05-19 | 9.18.0 |
| 2.11.0 | 2023-04-17 | 9.18.0 |
| 2.10.1 | 2025-06-16 | 8.14.0 |
| 2.10.0 | 2022-12-02 | 8.14.0 |
| 2.9.0 | 2022-08-12 | 8.14.0 |
| 2.8.0 | 2021-10-06 | 8.14.0 |
| 2.7.0 | 2021-09-17 | 8.14.0 |
| 2.6.0 | 2021-05-11 | 8.14.0 |
| 2.5.0 | 2021-04-14 | 8.14.0 |
| 2.4.0 | 2020-08-05 | 8.0.0 |
| 2.3.0 | 2020-07-01 | 8.0.0 |
| 2.2.0 | 2019-10-24 | 8.0.0 |
| 2.1.0 | 2019-07-03 | 8.0.0 |
| 2.0.0 | 2019-05-09 | 8.0.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 5.1.0 | removal | Removed CsvAsTable widget; use Markdown viewer from marketplace instead. | CsvAsTable | Markdown viewer |
| 5.1.0 | removal | Removed dependency on Community Commons module. | Community Commons |  |
| 5.0.0 | requirement | Upgraded module to require Mendix version 11.6.0. | Mendix |  |
| 4.2.0 | removal | Removed CsvAsTable widget; use Markdown viewer from marketplace instead. | CsvAsTable | Markdown viewer |
| 4.2.0 | removal | Removed dependency on Community Commons module. | Community Commons |  |
| 4.0.0 | requirement | Upgraded module to require Mendix version 10.21.0. | Mendix |  |
| 4.0.0 | improvement | Upgraded all widgets to be React compatible. |  |  |
| 3.1.0 | requirement | Upgraded module to require Mendix version 9.24.36. | Mendix |  |
| 3.1.0 | removal | Removed CsvAsTable widget; use Markdown viewer from marketplace instead. | CsvAsTable | Markdown viewer |
| 3.1.0 | removal | Removed dependency on Community Commons module. | Community Commons |  |
| 3.0.0 | requirement | Upgraded module to require Mendix version 9.18.4. | Mendix |  |
| 3.0.0 | improvement | Upgraded Atlas UI to version 3. | Atlas UI |  |
| 2.17.1 | security | Upgraded commons-beanutils to 1.11.0 to fix vulnerability CVE-2025-48734. | commons-beanutils |  |
| 2.15.0 | improvement | Improved migration to JDM; upgraded lang3 library. | lang3 |  |
| 2.14.0 | improvement | Upgraded CSV as Table widget to version 1.3 (pluggable widget). | CsvAsTable |  |
| 2.13.0 | migration-step | When imported in 10.3, dependencies must be managed per Mendix documentation. |  |  |
| 2.11.0 | improvement | Prepared module for Mendix 10. |  |  |
| 2.10.1 | security | Upgraded commons-beanutils to 1.11.0 to fix vulnerability CVE-2025-48734. | commons-beanutils |  |
| 2.10.0 | security | Migrated to OpenCSV library 5.7.1 to fix CVEs. | OpenCSV |  |
| 2.8.0 | improvement | Updated CSVAsTable widget per release 1.1. | CsvAsTable |  |
| 2.5.0 | improvement | Added Atlas UI and new version of Community Commons; usable in Mendix 9.x. | Atlas UI, Community Commons |  |
| 2.0.0 | removal | Removed Float datatype. | Float |  |

## Orientation (Native) <a id="116401"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/116401)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2020-12-16 | 8.12.0 |

## PDF Document Generation <a id="211553"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/211553)

| version | published | min Mendix |
|---|---|---|
| 2.1.4 | 2025-09-04 | 10.21.0 |
| 2.1.3 | 2025-08-06 | 10.21.0 |
| 2.1.2 | 2025-07-17 | 10.21.0 |
| 2.1.1 | 2025-07-04 | 10.21.0 |
| 2.1.0 | 2025-06-23 | 10.21.0 |
| 2.0.1 | 2025-05-26 | 10.21.0 |
| 2.0.0 | 2025-05-02 | 10.21.0 |
| 1.11.4 | 2025-09-04 | 9.24.0 |
| 1.11.3 | 2025-08-06 | 9.24.0 |
| 1.11.2 | 2025-07-17 | 9.24.0 |
| 1.11.1 | 2025-07-03 | 9.24.0 |
| 1.11.0 | 2025-06-23 | 9.24.0 |
| 1.10.3 | 2025-05-26 | 9.24.0 |
| 1.10.2 | 2025-03-31 | 9.24.0 |
| 1.10.1 | 2025-02-20 | 9.24.0 |
| 1.10.0 | 2024-11-01 | 9.24.0 |
| 1.9.0 | 2024-06-05 | 9.24.0 |
| 1.8.0 | 2024-04-25 | 9.18.0 |
| 1.7.0 | 2024-03-14 | 9.18.0 |
| 1.6.0 | 2024-03-01 | 9.18.0 |
| 1.5.0 | 2024-01-23 | 9.18.0 |
| 1.4.0 | 2024-01-12 | 9.18.0 |
| 1.3.0 | 2023-12-04 | 9.18.0 |
| 1.2.1 | 2023-10-24 | 9.18.0 |
| 1.2.0 | 2023-09-18 | 9.18.0 |
| 1.1.1 | 2023-09-07 | 9.18.0 |
| 1.1.0 | 2023-08-29 | 9.18.0 |
| 1.0.0 | 2023-05-31 | 9.18.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.1.4 | fix | Fixed document generation failing with wait for content exception if any network request fails while navigating to document page. |  |  |
| 2.1.4 | known-issue | Cloud service media queries evaluated incorrectly, resulting in unexpected widths for layout grids and widgets in PDF. | layout grids |  |
| 2.1.3 | improvement | Updated commons-lang3 dependency to version 3.18.0. | commons-lang3 |  |
| 2.1.3 | improvement | Updated local service to version 2.3.4. | local service |  |
| 2.1.3 | known-issue | Cloud service media queries evaluated incorrectly, resulting in unexpected widths for layout grids and widgets in PDF. | layout grids |  |
| 2.1.2 | fix | Fixed issue introduced in 2.1.1 where updating would not replace Redirect widget and fail document generation. | Redirect widget |  |
| 2.1.2 | known-issue | Cloud service media queries evaluated incorrectly, resulting in unexpected widths for layout grids and widgets in PDF. | layout grids |  |
| 2.1.1 | fix | Fixed document generation failing with client error 'mx.data.action is disabled' when running with Strict mode enabled for React client. |  |  |
| 2.1.1 | known-issue | Cloud service media queries evaluated incorrectly, resulting in unexpected widths for layout grids and widgets in PDF. | layout grids |  |
| 2.1.0 | feature | Added new service type 'Private' supporting private PDF document generation service hosted and managed by customer. |  |  |
| 2.1.0 | known-issue | Cloud service media queries evaluated incorrectly, resulting in unexpected widths for layout grids and widgets in PDF. | layout grids |  |
| 2.1.0 | known-issue | Document generation fails with client error 'mx.data.action is disabled' when running with Strict mode enabled for React client. |  |  |
| 2.0.1 | fix | Fixed issue where document generation could intermittently result in runtime exception whilst processing document result. |  |  |
| 2.0.1 | known-issue | Cloud service media queries evaluated incorrectly, resulting in unexpected widths for layout grids and widgets in PDF. | layout grids |  |
| 2.0.1 | known-issue | Document generation fails with client error 'mx.data.action is disabled' when running with Strict mode enabled for React client. |  |  |
| 2.0.0 | requirement | Upgraded module to Mendix version 10.21.0 for compatibility with Mendix 11. |  |  |
| 2.0.0 | improvement | Updated Atlas Core compatibility to version 3.17.0. | Atlas Core |  |
| 2.0.0 | improvement | Updated Atlas Web Content compatibility to version 3.8.0. | Atlas Web Content |  |
| 2.0.0 | improvement | Updated Data Widgets compatibility to version 2.31.0. | Data Widgets |  |
| 2.0.0 | improvement | Updated Combo Box widget compatibility to version 2.3.0. | Combo Box widget |  |
| 2.0.0 | known-issue | Cloud service media queries evaluated incorrectly, resulting in unexpected widths for layout grids and widgets in PDF. | layout grids |  |
| 2.0.0 | known-issue | Document generation fails with client error 'mx.data.action is disabled' when running with Strict mode enabled for React client. |  |  |
| 1.11.4 | fix | Fixed document generation failing with wait for content exception if any network request fails while opening document page. |  |  |
| 1.11.3 | improvement | Updated commons-lang3 dependency to version 3.18.0. | commons-lang3 |  |
| 1.11.3 | improvement | Updated local service to version 2.3.4. | local service |  |
| 1.11.2 | fix | Fixed issue introduced in 1.11.1 where updating would not replace Redirect widget and fail document generation. | Redirect widget |  |
| 1.11.1 | fix | Fixed document generation failing with client error 'mx.data.action is disabled' when running with Strict mode enabled for React client. |  |  |
| 1.11.1 | known-issue | Cloud service media queries evaluated incorrectly, resulting in unexpected widths for layout grids and widgets in PDF. | layout grids |  |
| 1.11.0 | feature | Added new service type 'Private' supporting private PDF document generation service hosted and managed by customer. |  |  |
| 1.11.0 | known-issue | Cloud service media queries evaluated incorrectly, resulting in unexpected widths for layout grids and widgets in PDF. | layout grids |  |
| 1.11.0 | known-issue | Document generation fails with client error 'mx.data.action is disabled' when running with Strict mode enabled for React client. |  |  |
| 1.10.3 | fix | Fixed issue where document generation could intermittently result in runtime exception whilst processing document result. |  |  |
| 1.10.3 | known-issue | Cloud service media queries evaluated incorrectly, resulting in unexpected widths for layout grids and widgets in PDF. | layout grids |  |
| 1.10.2 | improvement | Updated Combo Box compatibility to v1.7.1. | Combo Box |  |
| 1.10.2 | known-issue | Cloud service media queries evaluated incorrectly, resulting in unexpected widths for layout grids and widgets in PDF. | layout grids |  |
| 1.10.1 | known-issue | Testing PDF document generation locally using Chrome or Chromium version 117 or 118 might result in different scaling compared to Chromium version 112. |  |  |
| 1.10.1 | known-issue | Cloud service media queries evaluated incorrectly, resulting in unexpected widths for layout grids and widgets in PDF. | layout grids |  |
| 1.10.0 | feature | Added support for custom 'URL prefix' runtime setting for apps running in Mendix 10.5.0 or higher. |  |  |
| 1.10.0 | improvement | Upgraded 'axios' library used in local service to v1.7.7. | axios |  |
| 1.10.0 | removal | Removed dependency on 'commons-io' library; remove corresponding files from userlib folder after upgrading. | commons-io |  |
| 1.10.0 | migration-step | Remove 'commons-io-2.11.0.DocumentGeneration' files and 'commons-io-2.11.0.jar' from userlib folder if not used by other modules. | commons-io |  |
| 1.10.0 | known-issue | Testing PDF document generation locally using Chrome or Chromium version 117 or 118 might result in different scaling compared to Chromium version 112. |  |  |
| 1.10.0 | known-issue | Cloud service media queries evaluated incorrectly, resulting in unexpected widths for layout grids and widgets in PDF. | layout grids |  |
| 1.9.0 | requirement | Upgraded module to Mendix 9.24.0. |  |  |
| 1.9.0 | feature | Added support for React client, introduced as public beta in Mendix 10.7.0. |  |  |
| 1.9.0 | breaking | Switched to new Combo Box widget for selecting deployment type when registering app environment. | Combo Box widget | Combo Box widget |
| 1.9.0 | requirement | Ensure Combo Box widget is installed in project. | Combo Box widget |  |
| 1.9.0 | known-issue | Importing module in Mendix 10.6.0+ might raise consistency error CE6087 for renamed design properties; update all renamed design properties. |  |  |
| 1.9.0 | known-issue | Testing PDF document generation locally using Chrome or Chromium version 117 or 118 might result in different scaling compared to Chromium version 112. |  |  |
| 1.9.0 | known-issue | Cloud service media queries evaluated incorrectly, resulting in unexpected widths for layout grids and widgets in PDF. | layout grids |  |
| 1.8.0 | known-issue | Testing PDF document generation locally using Chrome or Chromium version 117 or 118 might result in different scaling compared to Chromium version 112. |  |  |
| 1.7.0 | known-issue | Chrome/Chromium 117-118 local testing produces different PDF scaling than service's Chromium 112. Fixed in Chrome 119. |  |  |
| 1.6.0 | known-issue | Chrome/Chromium 117-118 local testing produces different PDF scaling than service's Chromium 112. Fixed in Chrome 119. |  |  |
| 1.5.0 | known-issue | Chrome/Chromium 117-118 local testing produces different PDF scaling than service's Chromium 112. Fixed in Chrome 119. |  |  |
| 1.4.0 | known-issue | Chrome/Chromium 117-118 local testing produces different PDF scaling than service's Chromium 112. Fixed in Chrome 119. |  |  |
| 1.3.0 | breaking | App environment registration now requires personal access token (PAT) instead of developer API key. Existing registrations remain valid. |  |  |
| 1.3.0 | known-issue | Chrome/Chromium 117-118 local testing produces different PDF scaling than service's Chromium 112. Fixed in Chrome 119. |  |  |
| 1.2.1 | breaking | Aligned behavior between local and online service: redirects to external URLs are no longer allowed. |  |  |
| 1.2.1 | known-issue | Chrome/Chromium 117-118 local testing produces different PDF scaling than service's Chromium 112. Fixed in Chrome 119. |  |  |
| 1.2.0 | migration-step | Included migration file for Java dependencies for Studio Pro 10 compatibility. |  |  |
| 1.2.0 | known-issue | Chrome/Chromium 117-118 local testing produces different PDF scaling than service's Chromium 112. Fixed in Chrome 119. |  |  |
| 1.1.1 | fix | Fixed timeout issue when generating document with custom Mendix Runtime setting ApplicationRootURL to custom domain. | ApplicationRootURL |  |
| 1.1.1 | known-issue | Chrome/Chromium 117+ local testing produces different PDF scaling than cloud service. Use recommended Chromium version locally. |  |  |
| 1.1.0 | improvement | Use time zone of 'Generate as user' for date/time localization; fall back to App Settings or UTC. |  |  |
| 1.1.0 | improvement | No longer require Create and Write access rights for 'Generate as user' property user. |  |  |
| 1.1.0 | removal | Remove dependency on FieldSet widget. | FieldSet widget |  |
| 1.1.0 | removal | Remove RedirectLayout from the module. | RedirectLayout |  |
| 1.1.0 | removal | Remove constants UseCustomApplicationUrl and CustomApplicationUrl; use Application Root URL or App URL. | UseCustomApplicationUrl, CustomApplicationUrl |  |
| 1.1.0 | breaking | Cannot use @media print for PDF-specific styles; use document-generation-body-injected or document-content classes instead. | @media print | document-generation-body-injected |
| 1.1.0 | breaking | Wait until no pending network requests remain; long polling network requests no longer supported. |  |  |
| 1.1.0 | breaking | Rename DocumentLayout layout to DocumentGeneration_Default. | DocumentLayout | DocumentGeneration_Default |
| 1.1.0 | migration-step | Update layout for all pages using DocumentLayout to DocumentGeneration_Default and set 'Enable PDF export' to Yes. |  |  |
| 1.1.0 | breaking | Introduce design property 'Enable PDF export'; set to Yes for pages to export as PDF. |  |  |
| 1.1.0 | migration-step | When migrating from v1.0.0, set 'Enable PDF export' to Yes for all pages previously using DocumentLayout. |  |  |
| 1.1.0 | breaking | Rename included widgets; delete mendix.DocGenRedirect.mpk and mendix.PageBreak.mpk from widgets directory. | mendix.DocGenRedirect.mpk, mendix.PageBreak.mpk |  |
| 1.1.0 | migration-step | Delete old widget files mendix.DocGenRedirect.mpk and mendix.PageBreak.mpk; update pages to use new widgets. | mendix.DocGenRedirect.mpk, mendix.PageBreak.mpk |  |
| 1.1.0 | breaking | Rename theme variable $default-margin to $document-section-padding; use @page rule for page margin. | $default-margin | $document-section-padding |
| 1.1.0 | breaking | Rename remove-margin classes to remove-padding in stylesheet; update usage accordingly. | remove-margin | remove-padding |
| 1.1.0 | known-issue | Chrome/Chromium 117+ locally may scale PDF differently than Mendix Public Cloud service. |  |  |
| 1.1.0 | fix | Support apps including Responsive Web Offline navigation profile. (Ticket #190165) |  |  |
| 1.0.0 | known-issue | Chrome/Chromium 117+ locally may scale PDF differently than Mendix Public Cloud service. |  |  |

## Pdf Fill Form Fields <a id="116692"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/116692)

| version | published | min Mendix |
|---|---|---|
| 4.0.0 | 2026-05-06 | 10.24.0 |
| 3.0.0 | 2025-05-20 | 10.21.0 |
| 2.0.0 | 2024-07-08 | 10.12.0 |
| 1.2.0 | 2023-12-11 | 9.18.0 |
| 1.1.0 | 2022-09-06 | 8.12.3 |
| 1.0.1 | 2021-02-18 | 8.12.3 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 4.0.0 | breaking | Upgraded pdfbox from version 2.x to version 3.x, not backwards compatible with 2.x. | pdfbox |  |
| 4.0.0 | requirement | Minimum Mendix version raised to 10.24.0. | Mendix |  |
| 4.0.0 | migration-step | If application or other modules use pdfbox 2.x, must use module version 3.0.0 instead. | pdfbox |  |
| 3.0.0 | requirement | Updated to Studio Pro version 10.21.0. | Mendix |  |
| 2.0.0 | requirement | Upgraded to Studio Pro version 10.12.0. | Mendix |  |
| 1.2.0 | improvement | Updated jar files: pdfbox-2.0.30.jar, fontbox-2.0.30.jar, commons-logging-1.3.0.jar. | pdfbox, fontbox, commons-logging |  |
| 1.2.0 | migration-step | Added migration file. |  |  |

## PgVector Knowledge Base <a id="225063"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/225063)

| version | published | min Mendix |
|---|---|---|
| 7.0.0 | 2026-07-02 | 11.12.0 |
| 6.0.1 | 2026-03-10 | 10.24.0 |
| 5.1.0 | 2025-08-13 | 10.24.0 |
| 5.0.0 | 2025-08-08 | 10.24.0 |
| 4.2.0 | 2025-07-02 | 10.21.0 |
| 4.1.0 | 2025-06-24 | 10.21.0 |
| 4.0.0 | 2025-06-13 | 10.21.0 |
| 3.0.0 | 2025-04-07 | 10.21.0 |
| 2.4.1 | 2025-03-12 | 9.24.2 |
| 2.4.0 | 2025-02-03 | 9.24.2 |
| 2.3.0 | 2025-01-13 | 9.24.2 |
| 2.2.0 | 2024-10-16 | 9.24.2 |
| 2.1.0 | 2024-08-28 | 9.24.2 |
| 2.0.0 | 2024-07-25 | 9.24.2 |
| 1.2.1 | 2024-06-24 | 9.24.2 |
| 1.2.0 | 2024-05-15 | 9.24.0 |
| 1.1.0 | 2024-04-30 | 9.24.0 |
| 1.0.0 | 2024-04-08 | 9.24.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 7.0.0 | removal | Data migration microflows from previous major version removed. Multi-version upgrades require migration guide. | Data migration microflows |  |
| 7.0.0 | requirement | Module upgraded to Mendix 11.12.0 minimum requirement. |  |  |
| 6.0.1 | breaking | Module aligned with latest ConsumedKnowledgeBase and ConsumedMCPService changes. Breaking change requiring migration to prevent data/functionality loss. | ConsumedKnowledgeBase, ConsumedMCPService |  |
| 6.0.1 | requirement | Compatible with GenAI Commons 6.0.0 version. | GenAI Commons |  |
| 5.1.0 | requirement | Module made compatible with GenAI Commons 5.1.0. | GenAI Commons |  |
| 5.0.0 | requirement | Module upgraded to Mendix Studio Pro 10.24. |  |  |
| 4.2.0 | feature | PgVector knowledge bases can now be used with vendor-agnostic Tools Add Knowledge Base action requiring embeddings model selection. | Tools Add Knowledge Base action |  |
| 4.2.0 | migration-step | Existing PgVectorKnowledgeBase objects must be recreated for tool use registration via reinsertion or PgVectorKnowledgeBase_GetOrCreate microflow. | PgVectorKnowledgeBase |  |
| 4.1.0 | improvement | Granted entity access for PgVectorKnowledgeBase to support runtime agent configuration via AgentCommons module. | PgVectorKnowledgeBase |  |
| 4.0.0 | breaking | PgVectorKnowledgeBase entity now inherits from DeployedKnowledgeBase. Microflows reconfigured accordingly. | PgVectorKnowledgeBase, DeployedKnowledgeBase |  |
| 3.0.0 | requirement | Module updated to Mendix Studio Pro 10.21.0. |  |  |
| 2.4.0 | improvement | Configuration page updated for React client support. Unsupported widgets replaced with supported alternatives. | configuration page, widgets |  |
| 2.0.0 | requirement | Module updated for GenAI Commons compatibility with shared domain model for embeddings and knowledge base interactions. | GenAI Commons |  |
| 2.0.0 | migration-step | Update OpenAI connector or Amazon Bedrock connector to use combined setup. | OpenAI connector, Amazon Bedrock connector |  |
| 2.0.0 | breaking | Database schema changed. Knowledge base must be repopulated after upgrade. | database schema |  |
| 2.0.0 | feature | Retrieve operation now has optional input parameter for a Mendix object. | retrieve operation |  |
| 1.2.0 | feature | Added Replace operation to replace existing chunks for chunks based on Mendix Object, keeping knowledge base in sync with application database. | Replace operation |  |
| 1.2.0 | feature | Added operation to insert list of Chunks into existing knowledge base. | insert operation |  |
| 1.2.0 | feature | Added two operations to delete chunks and labels by providing a Mendix object or list of Mendix objects. | delete operation |  |
| 1.1.0 | feature | Added two operations to retrieve chunks and automatically associate to Mendix object via nearest neighbor search or regular retrieve with offset/limit. | retrieve operation |  |
| 1.1.0 | feature | Added operation to delete a knowledge base. | delete operation |  |
| 1.0.0 | feature | Initial release with operations to populate knowledge bases and retrieve data with/without vector similarity calculation. |  |  |

## Policysense Sales <a id="212193"></a>
Solution, In Motion, Partner, [marketplace](https://marketplace.mendix.com/link/component/212193)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2023-06-27 | ? |

## Pop-up Menu <a id="115826"></a>
Widget, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/115826)

| version | published | min Mendix |
|---|---|---|
| 4.3.1 | 2026-07-22 | 9.24.0 |
| 4.3.0 | 2026-06-19 | 9.24.0 |
| 4.2.0 | 2026-05-08 | 9.24.0 |
| 4.1.0 | 2026-04-13 | 9.24.0 |
| 4.0.3 | 2026-02-10 | 9.24.0 |
| 4.0.2 | 2025-02-20 | 9.24.0 |
| 4.0.1 | 2024-12-13 | 9.24.0 |
| 4.0.0 | 2024-11-13 | 9.24.0 |
| 3.6.1 | 2024-09-18 | 9.6.0 |
| 3.6.0 | 2024-08-23 | 9.6.0 |
| 3.5.3 | 2024-01-08 | 9.6.0 |
| 3.5.2 | 2023-09-27 | 9.6.0 |
| 3.5.1 | 2023-08-18 | 9.6.0 |
| 3.5.0 | 2023-06-28 | 9.6.0 |
| 3.4.0 | 2023-06-05 | 9.6.0 |
| 3.3.0 | 2023-01-04 | 9.6.0 |
| 3.2.2 | 2022-02-01 | 9.6.0 |
| 3.2.1 | 2022-01-19 | 9.6.0 |
| 3.2.0 | 2021-12-23 | 9.6.0 |
| 3.1.1 | 2021-12-03 | 9.6.0 |
| 3.1.0 | 2021-11-18 | 9.6.0 |
| 3.0.0 | 2021-09-28 | 9.6.0 |
| 2.0.1 | 2021-06-03 | 9.0.5 |
| 2.0.0 | 2021-04-15 | 9.0.5 |
| 1.0.2 | 2021-03-31 | 9.0.5 |
| 1.0.0 | 2020-10-27 | 8.15.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 4.3.1 | fix | Fixed widget not loading in Dojo client due to broken JavaScript bundle. | JavaScript bundle, Dojo client |  |
| 4.0.1 | breaking | 'The area to open or close the menu' field is now required. | area to open or close the menu |  |
| 4.0.0 | requirement | Widget styling moved to Atlas core; update atlas-core to minimum 3.15.0 for Studio Pro 10.6.0+ or 3.12.5 below to keep styling. | atlas-core |  |
| 3.6.0 | breaking | Default behavior for closing popup set to open on 'hover' is now 'hover leave'. | hover closing behavior |  |
| 3.5.0 | breaking | Changed DOM structure from div to ul-li for accessibility purposes; custom styling may be affected. | DOM structure |  |
| 1.0.2 | fix | Updated widget consistency checks to be compatible with Mendix 9. | consistency checks |  |

## Power BI Embedded <a id="220920"></a>
Service, Kinetech, Partner, [marketplace](https://marketplace.mendix.com/link/component/220920)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2024-01-15 | 9.0.5 |

## PrintClass <a id="203450"></a>
Module, Mendixlabs, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/203450)

| version | published | min Mendix |
|---|---|---|
| 1.1.0 | 2024-01-26 | 9.18.0 |
| 1.0.0 | 2022-11-08 | 9.18.0 |

## Process Queue <a id="393"></a>
Module, Mendix, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/393)

| version | published | min Mendix |
|---|---|---|
| 8.0.0 | 2022-03-30 | 8.12.0 |
| 7.0.0 | 2022-03-31 | 7.23.22 |
| 4.2.0 | 2021-02-11 | 8.12.0 |
| 4.1.2 | 2019-08-02 | 7.23.0 |
| 4.1.1 | 2019-03-01 | 7.1.0 |
| 4.1.0 | 2018-02-16 | 7.1.0 |
| 4.0.0 | 2017-11-02 | 7.1.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 7.0.0 | requirement | Upgraded project to Mendix 7.23.22 |  |  |
| 4.2.0 | requirement | Updated to Mendix Studio Pro 8.12.0 |  |  |
| 4.1.2 | requirement | Module is now Mendix 8 compatible |  |  |
| 4.1.1 | fix | Fixed thread leak when calling InitializeQueue.java | InitializeQueue.java |  |
| 4.1.1 | improvement | Improved memory management due to differing IContext behavior in Mx7 vs Mx6 |  |  |
| 4.1.0 | removal | Removed Queue monitor information from QueueOverview page; information was outdated and misaligned with actual queue state | QueueOverview |  |
| 4.1.0 | breaking | Completely replaced retry mechanism with pre-processing mechanism ensuring FIFO ordering |  |  |
| 4.1.0 | improvement | Pre-processing mechanism reduces error-prone handling and processes large queued action batches quicker |  |  |
| 4.1.0 | fix | Removed while loop in ObjectQueueExecutor Java action that might cause queue to hang | ObjectQueueExecutor |  |
| 4.1.0 | removal | Removed full retry mechanism, replaced by preprocessing of actions before appending to queue |  |  |
| 4.1.0 | improvement | Modified _QueueAppenderThread Java functionality to enable thread restart capability | _QueueAppenderThread |  |
| 4.0.0 | requirement | Upgraded to Mendix 7.1.0 |  |  |

## Progress Bar <a id="48910"></a>
Widget, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/48910)

| version | published | min Mendix |
|---|---|---|
| 3.2.3 | 2026-02-11 | 9.6.0 |
| 3.2.2 | 2024-08-28 | 9.6.0 |
| 3.2.1 | 2023-09-27 | 9.6.0 |
| 3.2.0 | 2023-06-05 | 9.6.0 |
| 3.1.0 | 2021-12-23 | 9.6.0 |
| 3.0.1 | 2021-12-03 | 9.6.0 |
| 3.0.0 | 2021-09-28 | 9.6.0 |
| 2.1.0 | 2021-07-07 | 9.0.5 |
| 2.0.0 | 2021-03-31 | 9.0.5 |
| 1.2.1 | 2019-09-10 | 7.13.1 |
| 1.2.0 | 2018-10-02 | 7.13.1 |
| 1.1.0 | 2018-05-11 | 7.13.1 |
| 1.0.4 | 2018-03-01 | 7.4.0 |
| 1.0.3 | 2017-08-02 | 7.4.0 |
| 1.0.2 | 2017-07-06 | 7.3.0 |
| 1.0.1 | 2017-06-12 | 7.1.0 |
| 1.0 | 2017-04-17 | 7.1.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.0.0 | breaking | Reorganization of properties and design properties. | properties, design properties |  |
| 2.0.0 | breaking | Removed inner styles from widgets and moved to module themesource. | inner styles, module themesource |  |
| 2.0.0 | breaking | Progress values outside of the provided range are clamped onto the minimum or maximum value depending on which one is closer. | progress values |  |

## Progress Circle <a id="47783"></a>
Widget, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/47783)

| version | published | min Mendix |
|---|---|---|
| 3.3.3 | 2026-02-18 | 9.6.0 |
| 3.3.2 | 2024-08-28 | 9.6.0 |
| 3.3.1 | 2023-09-27 | 9.6.0 |
| 3.3.0 | 2023-08-02 | 9.6.0 |
| 3.2.0 | 2023-06-06 | 9.6.0 |
| 3.1.0 | 2021-12-23 | 9.6.0 |
| 3.0.1 | 2021-12-03 | 9.6.0 |
| 3.0.0 | 2021-09-29 | 9.6.0 |
| 2.1.0 | 2021-07-07 | 9.0.5 |
| 2.0.0 | 2021-04-01 | 9.0.5 |
| 1.7.0 | 2019-01-04 | 7.13.1 |
| 1.6.0 | 2018-10-02 | 7.13.1 |
| 1.5.1 | 2018-06-19 | 7.13.1 |
| 1.5.0 | 2018-05-11 | 7.13.1 |
| 1.4.1 | 2018-03-01 | 7.5.0 |
| 1.4.0 | 2017-09-27 | 7.5.0 |
| 1.3.0 | 2017-09-13 | 7.5.0 |
| 1.2.3 | 2017-08-02 | 7.3.0 |
| 1.2.2 | 2017-07-10 | 7.3.0 |
| 1.2.1 | 2017-06-21 | 7.2.0 |
| 1.2 | 2017-05-30 | 7.2.0 |
| 1.1 | 2017-05-13 | 7.2.0 |
| 1.0 | 2017-04-06 | 7.1.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 3.3.0 | security | Fixed security issues on 3rd party components. |  |  |
| 2.0.0 | breaking | Removed inner styles from widgets and moved to module themesource. |  |  |
| 2.0.0 | breaking | Progress values outside of the provided range are clamped onto the minimum or maximum value depending on which one is closer. |  |  |
| 1.2.1 | removal | Removed desktop modeler preview. |  |  |
| 1.2 | breaking | Removed style max-width: 300. |  |  |

## Pull to refresh <a id="47782"></a>
Widget, Mendix, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/47782)

| version | published | min Mendix |
|---|---|---|
| 1.1.0 | 2020-06-19 | 7.13.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.1.0 | requirement | Minimum Mendix Studio Pro version raised to 7.13.1. | Mendix Studio Pro |  |

## Pull To Refresh <a id="117208"></a>
Widget, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/117208)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2021-04-06 | 8.18.2 |

## Purchase Request <a id="118328"></a>
Starter App, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/118328)

| version | published | min Mendix |
|---|---|---|
| 11.19.0 | 2026-10-05 | 11.15.0 |
| 11.18.3 | 2026-09-15 | 11.14.0 |
| 11.17.0 | 2026-08-03 | 11.13.0 |
| 11.16.0 | 2026-07-28 | 11.12.2 |
| 11.15.0 | 2026-07-16 | 11.12.1 |
| 11.14.0 | 2026-07-01 | 11.12.0 |
| 11.13.0 | 2026-06-01 | 11.11.0 |
| 11.12.0 | 2026-04-29 | 11.10.0 |
| 11.11.0 | 2026-04-17 | 11.9.1 |
| 11.10.0 | 2026-04-07 | 11.9.0 |
| 11.9.0 | 2026-03-02 | 11.8.0 |
| 11.8.1 | 2026-02-11 | 11.7.0 |
| 11.8.0 | 2026-01-30 | 11.7.0 |
| 11.7.0 | 2026-01-29 | 11.6.3 |
| 11.6.0 | 2026-01-12 | 11.6.2 |
| 11.5.0 | 2026-01-07 | 11.6.1 |
| 11.4.0 | 2025-12-23 | 11.6.0 |
| 11.3.0 | 2025-11-25 | 11.5.0 |
| 11.2.0 | 2025-11-04 | 11.4.0 |
| 11.1.0 | 2025-07-31 | 11.1.0 |
| 11.0.0 | 2025-07-17 | 11.0.0 |
| 3.3.0 | 2025-06-25 | 10.24.0 |
| 3.2.0 | 2025-05-28 | 10.23.0 |
| 3.1.0 | 2025-05-02 | 10.22.0 |
| 3.0.0 | 2025-04-25 | 10.21.0 |
| 2.31.2 | 2025-02-04 | 10.18.2 |
| 2.30.2 | 2025-01-28 | 10.19.0 |
| 2.29.2 | 2025-01-10 | 10.18.1 |
| 2.28.2 | 2024-12-18 | 10.18.0 |
| 2.27.2 | 2024-12-13 | 10.17.0 |
| 2.26.0 | 2024-11-11 | 10.16.1 |
| 2.25.0 | 2024-10-30 | 10.16.0 |
| 2.24.0 | 2024-09-24 | 10.15.0 |
| 2.23.0 | 2024-08-27 | 10.14.0 |
| 2.22.0 | 2024-08-07 | 10.13.1 |
| 2.21.0 | 2024-07-30 | 10.13.0 |
| 2.20.0 | 2024-07-05 | 10.12.1 |
| 2.19.0 | 2024-06-25 | 10.12.0 |
| 2.18.0 | 2024-05-31 | 10.11.0 |
| 2.17.0 | 2024-03-26 | 10.9.0 |
| … 21 older versions | | |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 11.19.0 | requirement | Minimum Mendix version raised to 11.15.0 |  |  |
| 11.19.0 | removal | MxSSO removed | MxSSO |  |
| 11.18.3 | requirement | Minimum Mendix version requirement changed to 11.14.0 | Mendix |  |
| 11.17.0 | requirement | Minimum Mendix version requirement changed to 11.13.0 | Mendix |  |
| 11.16.0 | requirement | Minimum Mendix version requirement changed to 11.12.2 | Mendix |  |
| 11.15.0 | requirement | Minimum Mendix version requirement changed to 11.12.1 | Mendix |  |
| 11.14.0 | requirement | Minimum Mendix version requirement changed to 11.12.0 | Mendix |  |
| 11.13.0 | requirement | Minimum Mendix version requirement changed to 11.11.0 | Mendix |  |
| 11.12.0 | requirement | Minimum Mendix version requirement changed to 11.10.0 | Mendix |  |
| 11.11.0 | requirement | Minimum Mendix version requirement changed to 11.9.1 | Mendix |  |
| 11.10.0 | requirement | Minimum Mendix version requirement changed to 11.9.0 | Mendix |  |
| 11.9.0 | requirement | Minimum Mendix version requirement changed to 11.8.0 | Mendix |  |
| 11.8.0 | requirement | Minimum Mendix version requirement changed to 11.7.0 | Mendix |  |
| 11.7.0 | requirement | Minimum Mendix version requirement changed to 11.6.3 | Mendix |  |
| 11.6.0 | requirement | Minimum Mendix version requirement changed to 11.6.2 | Mendix |  |
| 11.5.0 | requirement | Minimum Mendix version requirement changed to 11.6.1 | Mendix |  |
| 11.4.0 | requirement | Minimum Mendix version requirement changed to 11.6.0 | Mendix |  |
| 11.3.0 | requirement | Minimum Mendix version requirement changed to 11.5.0 | Mendix |  |
| 11.2.0 | requirement | Minimum Mendix version requirement changed to 11.4.0 | Mendix |  |
| 11.1.0 | requirement | Minimum Mendix version requirement changed to 11.1.0 | Mendix |  |
| 11.0.0 | requirement | Minimum Mendix version requirement changed to 11.0.0 | Mendix |  |
| 3.3.0 | requirement | Minimum Mendix version requirement changed to 10.24.0 | Mendix |  |
| 3.2.0 | requirement | Minimum Mendix version requirement changed to 10.23.0 | Mendix |  |
| 3.1.0 | requirement | Minimum Mendix version requirement changed to 10.22.0 | Mendix |  |
| 3.0.0 | requirement | Minimum Mendix version requirement changed to 10.21.0 | Mendix |  |
| 3.0.0 | feature | React Client enabled | React Client |  |
| 2.31.2 | requirement | Minimum Mendix version requirement changed to 10.18.2 | Mendix |  |
| 2.30.2 | requirement | Minimum Mendix version requirement changed to 10.19.0 | Mendix |  |
| 2.29.2 | requirement | Minimum Mendix version requirement changed to 10.18.1 | Mendix |  |
| 2.28.2 | requirement | Minimum Mendix version requirement changed to 10.18.0 | Mendix |  |
| 2.27.2 | requirement | Minimum Mendix version requirement changed to 10.17.0 | Mendix |  |
| 2.27.2 | requirement | Workflow Commons module updated to version 3.12.0 | Workflow Commons |  |
| 2.26.0 | requirement | Minimum Mendix version requirement changed to 10.16.1 | Mendix |  |
| 2.25.0 | requirement | Minimum Mendix version requirement changed to 10.16.0 | Mendix |  |
| 2.24.0 | requirement | Minimum Mendix version requirement changed to 10.15.0 | Mendix |  |
| 2.23.0 | requirement | Minimum Mendix version requirement changed to 10.14.0 | Mendix |  |
| 2.22.0 | requirement | Minimum Mendix version requirement changed to 10.13.1 | Mendix |  |
| 2.21.0 | requirement | Minimum Mendix version requirement changed to 10.13.0 | Mendix |  |
| 2.20.0 | requirement | Minimum Mendix version requirement changed to 10.12.1 | Mendix |  |
| 2.19.0 | requirement | Minimum Mendix version requirement changed to 10.12.0 | Mendix |  |
| 2.18.0 | requirement | Minimum Mendix version requirement changed to 10.11.0 | Mendix |  |
| 2.17.0 | requirement | Minimum Mendix version requirement changed to 10.9.0 | Mendix |  |
| 2.16.0 | requirement | Minimum Mendix version requirement changed to 10.8.1 | Mendix |  |
| 2.16.0 | improvement | All modules updated to the latest version |  |  |
| 2.15.0 | requirement | Minimum Mendix version requirement changed to 10.8.0 | Mendix |  |
| 2.14.0 | requirement | Minimum Mendix version requirement changed to 10.7.0 | Mendix |  |
| 2.13.0 | requirement | Minimum Mendix version requirement changed to 10.6.2 | Mendix |  |
| 2.12.0 | requirement | Minimum Mendix version requirement changed to 10.6.1 | Mendix |  |
| 2.11.0 | requirement | Minimum Mendix version requirement changed to 10.6.0 | Mendix |  |
| 2.10.0 | requirement | Minimum Mendix version requirement changed to 10.5.0 | Mendix |  |
| 2.10.0 | fix | Solved errors and updated modules |  |  |
| 2.5.0 | requirement | Minimum Mendix version requirement changed to 10.3.1 | Mendix |  |
| 2.4.0 | requirement | Minimum Mendix version requirement changed to 10.3.0 | Mendix |  |
| 2.3.0 | requirement | Minimum Mendix version requirement changed to 10.2.0 | Mendix |  |
| 2.2.0 | requirement | Minimum Mendix version requirement changed to 10.1.1 | Mendix |  |
| 2.1.0 | requirement | Minimum Mendix version requirement changed to 10.1.0 | Mendix |  |
| 2.0.0 | requirement | Minimum Mendix version requirement changed to 10.0.0 | Mendix |  |
| 1.9.0 | requirement | Minimum Mendix version requirement changed to 9.24.3 | Mendix |  |
| 1.8.0 | requirement | Minimum Mendix version requirement changed to 9.24.2 | Mendix |  |
| 1.7.0 | requirement | Minimum Mendix version requirement changed to 9.24.1 | Mendix |  |
| 1.6.0 | requirement | Minimum Mendix version requirement changed to 9.24.0 | Mendix |  |
| 1.5.0 | requirement | Minimum Mendix version requirement changed to 9.23.0 | Mendix |  |
| 1.4.0 | requirement | Minimum Mendix version requirement changed to 9.20.0 | Mendix |  |
| 1.3.0 | requirement | Minimum Mendix version requirement changed to 9.19.0 | Mendix |  |
| 1.2.0 | requirement | Minimum Mendix version requirement changed to 9.18.1 | Mendix |  |

## Push Notifications Connector <a id="3003"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/3003)

| version | published | min Mendix |
|---|---|---|
| 8.0.6 | 2026-10-05 | 10.21.0 |
| 8.0.5 | 2026-08-21 | 10.21.0 |
| 8.0.4 | 2026-06-12 | 10.21.0 |
| 8.0.3 | 2026-04-17 | 10.21.0 |
| 8.0.2 | 2025-11-21 | 10.21.0 |
| 8.0.1 | 2025-07-01 | 10.21.0 |
| 8.0.0 | 2025-05-01 | 10.21.0 |
| 7.4.4 | 2026-04-17 | 9.24.0 |
| 7.4.3 | 2025-11-21 | 9.24.0 |
| 7.4.2 | 2025-04-11 | 9.24.0 |
| 7.4.1 | 2024-10-23 | 9.24.0 |
| 7.4.0 | 2024-07-26 | 9.24.0 |
| 7.3.0 | 2024-06-11 | 9.24.0 |
| 7.2.4 | 2024-05-15 | 9.18.0 |
| 7.2.3 | 2024-01-09 | 9.18.0 |
| 7.2.2 | 2023-12-20 | 9.18.0 |
| 7.2.1 | 2023-09-26 | 9.18.0 |
| 7.2.0 | 2023-09-22 | 9.18.0 |
| 7.1.3 | 2023-07-17 | 9.18.0 |
| 7.1.2 | 2023-07-04 | 9.18.0 |
| 7.1.1 | 2023-06-27 | 9.18.0 |
| 7.1.0 | 2023-01-18 | 9.18.0 |
| 7.0.0 | 2022-11-30 | 9.18.0 |
| 6.3.1 | 2023-06-27 | 9.6.0 |
| 6.3.0 | 2023-01-18 | 9.6.0 |
| 6.2.0 | 2022-06-27 | 9.0.5 |
| 6.1.2 | 2022-05-25 | 9.0.5 |
| 6.1.1 | 2022-03-03 | 9.0.5 |
| 6.1.0 | 2022-02-02 | 9.0.5 |
| 6.0.1 | 2022-01-10 | 9.0.5 |
| 6.0.0 | 2021-12-16 | 9.0.5 |
| 5.4.4 | 2025-04-11 | 8.18.0 |
| 5.4.3 | 2024-10-23 | 8.18.0 |
| 5.4.2 | 2024-05-15 | 8.18.0 |
| 5.4.1 | 2024-01-09 | 8.18.0 |
| 5.4.0 | 2022-06-27 | 8.18.0 |
| 5.3.3 | 2022-05-31 | 8.18.0 |
| 5.3.2 | 2022-01-10 | 8.18.0 |
| 5.3.1 | 2021-12-16 | 8.18.0 |
| 5.3.0 | 2021-11-22 | 8.18.0 |
| … 14 older versions | | |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 8.0.6 | improvement | Updated static images to image widgets for React client compatibility. | images |  |
| 8.0.5 | fix | Fixed issue where Push Notifications was using wrong Pushy library introduced in v8.0.4 | Pushy library |  |
| 8.0.4 | fix | Updated dependencies to fix direct APNS push notifications. netty libraries to 4.1.133.Final, pushy to 0.15.4 | io.netty:netty-codec-http2, io.netty:netty-handler-proxy, io.netty:netty-resolver-dns, com.eatthepath:pushy |  |
| 8.0.3 | improvement | Updated netty dependencies to version 4.2.12.Final | io.netty:netty-codec-http2, io.netty:netty-handler-proxy, io.netty:netty-resolver-dns |  |
| 8.0.2 | improvement | Updated netty dependencies to version 4.2.5.Final | io.netty:netty-codec-http2, io.netty:netty-handler-proxy, io.netty:netty-resolver-dns |  |
| 8.0.0 | requirement | Upgraded module to Mendix version 10.21.0 for compatibility with Mendix 11 |  |  |
| 8.0.0 | improvement | Updated Atlas Core compatibility to version 3.17.0 | Atlas Core |  |
| 8.0.0 | improvement | Updated Atlas Web Content compatibility to version 3.8.0 | Atlas Web Content |  |
| 8.0.0 | improvement | Updated Data Widgets compatibility to version 2.31.0 | Data Widgets |  |
| 8.0.0 | improvement | Updated Combo Box widget compatibility to version 2.3.0 | Combo Box widget |  |
| 7.4.4 | improvement | Updated netty dependencies from 4.2.5.Final to 4.2.12.Final | netty-buffer, netty-codec-base, netty-codec-compression, netty-codec-dns, netty-codec-http2, netty-codec-http, netty-codec-socks, netty-common, netty-handler, netty-handler-proxy, netty-resolver, netty-resolver-dns, netty-transport, netty-transport-native-unix-common |  |
| 7.4.4 | migration-step | After upgrading, remove old versions of updated libraries and their '.PushNotifications.RequiredLib' from userlib folder | netty libraries |  |
| 7.4.3 | improvement | Updated netty dependencies from 4.2.0.Final to 4.2.5.Final | netty-buffer, netty-codec-base, netty-codec-compression, netty-codec-dns, netty-codec-http2, netty-codec-http, netty-codec-socks, netty-common, netty-handler, netty-handler-proxy, netty-resolver, netty-resolver-dns, netty-transport, netty-transport-native-unix-common |  |
| 7.4.3 | migration-step | After upgrading, remove old versions of updated libraries and their '.PushNotifications.RequiredLib' from userlib folder | netty libraries |  |
| 7.4.3 | removal | Deleted netty-codec, netty-codec-marshalling, and netty-codec-protobuf 4.2.0.Final files | netty-codec-4.2.0.Final.jar, netty-codec-marshalling-4.2.0.Final.jar, netty-codec-protobuf-4.2.0.Final.jar |  |
| 7.4.2 | improvement | Updated netty dependencies to version 4.2.0.Final | netty-buffer, netty-codec, netty-codec-dns, netty-codec-http, netty-codec-http2, netty-codec-socks, netty-common, netty-handler, netty-handler-proxy, netty-resolver, netty-resolver-dns, netty-transport, netty-transport-native-unix-common |  |
| 7.4.2 | migration-step | After upgrading, remove old versions of updated libraries and their '.PushNotifications.RequiredLib' from userlib folder | netty libraries |  |
| 7.4.2 | improvement | Added new netty libraries: codec-base, codec-compression, codec-marshalling, codec-protobuf 4.2.0.Final | netty-codec-base, netty-codec-compression, netty-codec-marshalling, netty-codec-protobuf |  |
| 7.4.0 | feature | Added support for Web Push notifications for progressive web apps |  |  |
| 7.3.0 | requirement | Upgraded module to Mendix 9.24.0 |  |  |
| 7.3.0 | feature | Added support for React client introduced as public beta in Mendix 10.7.0 |  |  |
| 7.3.0 | improvement | Updated all dropdown widgets to new Combo Box widget | dropdown widgets | Combo Box widget |
| 7.3.0 | improvement | Updated Atlas Core module compatibility to v3.12.3 replacing Static image widget with Image widget | Atlas Core |  |
| 7.3.0 | improvement | Updated Data Widgets module compatibility to v2.19.1 | Data Widgets |  |
| 7.3.0 | improvement | Updated Switch widget compatibility to v4.2.1 | Switch widget |  |
| 7.3.0 | removal | Excluded snippets related to hybrid mobile as deprecated in Mendix 9 and incompatible with React client | hybrid mobile snippets |  |
| 7.2.4 | improvement | Updated netty dependencies to version 4.1.109.Final | netty-buffer, netty-codec, netty-codec-dns, netty-codec-http2, netty-codec-http, netty-codec-socks, netty-common, netty-handler, netty-handler-proxy, netty-resolver, netty-resolver-dns, netty-transport, netty-transport-native-unix-common |  |
| 7.2.4 | migration-step | After upgrading, remove old versions of updated libraries and their '.PushNotifications.RequiredLib' from userlib folder | netty libraries |  |
| 7.2.3 | migration-step | Migrated from legacy FCM APIs to HTTP v1 for hybrid device notifications. Update before 2024-06-20 | FCM APIs |  |
| 7.2.2 | improvement | Updated netty dependencies to 4.1.101.Final and slf4j-api to 2.0.7 | netty-buffer, netty-codec, netty-codec-dns, netty-codec-http2, netty-codec-http, netty-codec-socks, netty-common, netty-handler, netty-handler-proxy, netty-resolver, netty-resolver-dns, netty-transport, netty-transport-native-unix-common, slf4j-api |  |
| 7.2.2 | migration-step | After upgrading, remove old versions of updated libraries and their '.PushNotifications.RequiredLib' from userlib folder | netty libraries |  |
| 7.2.0 | migration-step | Included migration file for Java dependencies for Studio Pro 10 compatibility | Java dependencies |  |
| 7.1.3 | improvement | Updated netty dependencies to version 4.1.94.Final | netty-buffer, netty-codec, netty-codec-dns, netty-codec-http2, netty-codec-http, netty-codec-socks, netty-common, netty-handler, netty-handler-proxy, netty-resolver, netty-resolver-dns, netty-transport, netty-transport-native-unix-common |  |
| 7.1.3 | migration-step | After upgrading, remove old versions of updated libraries and their '.PushNotifications.RequiredLib' from userlib folder | netty libraries |  |
| 7.1.2 | improvement | Updated dependencies: checker-qual to 3.33.0, j2objc-annotations to 2.8, error_prone_annotations to 2.18.0 | checker-qual, j2objc-annotations, error_prone_annotations |  |
| 7.1.2 | removal | Removed checker-compat-qual-2.5.5 | checker-compat-qual-2.5.5 |  |
| 7.1.2 | migration-step | After upgrading, remove old versions of updated libraries and their '.PushNotifications.RequiredLib' from userlib folder | libraries |  |
| 7.1.1 | improvement | Updated guava library to 32.0.1-android, remove old version 31.0.1-android from userlib | guava |  |
| 7.1.0 | improvement | Updated all netty libraries from version 4.1.78 to 4.1.86, delete older versions with '.PushNotifications.RequiredLib' | netty libraries |  |
| 7.1.0 | improvement | Added index on DeviceID attribute in Device entity | Device entity |  |
| 7.1.0 | improvement | Updated Pop-up Menu widget compatibility to v3.3.0 | Pop-up Menu widget |  |
| 7.1.0 | improvement | Updated Data Widgets compatibility to v2.5.9 | Data Widgets |  |
| 7.0.0 | requirement | Updated module to Mendix 9.18.0 |  |  |
| 7.0.0 | improvement | Switched to task queue implementation for sending notifications in background |  |  |
| 7.0.0 | fix | Fixed issue where notifications were sent multiple times in multi-instance deployment scenario |  |  |
| 6.3.1 | improvement | Updated guava library to 32.0.1-android, remove old version 31.0.1-android from userlib | guava |  |
| 6.3.0 | improvement | Updated all netty libraries from version 4.1.78 to 4.1.86, delete older versions with '.PushNotifications.RequiredLib' | netty libraries |  |
| 6.3.0 | improvement | Added index on DeviceID attribute in Device entity | Device entity |  |
| 6.3.0 | improvement | Updated Pop-up Menu widget compatibility to v3.3.0 | Pop-up Menu widget |  |
| 6.3.0 | improvement | Updated Data Widgets compatibility to v2.5.9 | Data Widgets |  |
| 6.2.0 | breaking | Removed all write access to Device entity for User/Anonymous roles (restricted to owner only). | Device |  |
| 6.2.0 | requirement | Updated dependencies: auto-value-annotations 1.8.2→1.9, commons-codec 1.13→1.15, google-auth-library-credentials 1.4.0→1.7.0, google-http-client 1.41.0→1.41.8, gson 2.8.9→2.9.0, netty 4.1.74→4.1.78, opencensus-api 0.28.0→0.31.0, pushy 0.13.9→0.13.10, slf4j-api 1.7.28→1.7.36, and others. | auto-value-annotations, commons-codec, google-auth-library-credentials, google-auth-library-oauth2-http, google-http-client, google-http-client-gson, gson, netty-buffer, netty-codec, netty-codec-dns, netty-codec-http, netty-codec-http2, netty-codec-socks, netty-common, netty-handler, netty-handler-proxy, netty-resolver, netty-resolver-dns, netty-transport, opencensus-api, opencensus-contrib-http-util, pushy, slf4j-api |  |
| 6.2.0 | migration-step | Review userlib folder after updating due to dependency changes: removed netty-tcnative-classes-2.0.48.Final.jar, added netty-transport-native-unix-common-4.1.78.Final.jar. | userlib |  |
| 6.1.2 | requirement | Updated dependencies: deleted 5 libraries, added checker-qual-3.12.0, guava-31.0.1-android, netty-tcnative-classes-2.0.48.Final. | animal-sniffer-annotations, guava, jackson-core, netty-all, netty-tcnative, checker-qual, netty-tcnative-classes |  |
| 6.1.2 | migration-step | Review userlib folder after updating due to dependency changes. | userlib |  |
| 6.1.1 | requirement | Updated all netty libraries to 4.1.74.Final. Delete netty libraries marked with .PushNotifications.RequiredLib below 4.1.74.Final from userlib. | netty |  |
| 6.1.1 | migration-step | Delete old netty libraries from userlib marked with .PushNotifications.RequiredLib below 4.1.74.Final. | userlib |  |
| 6.1.0 | breaking | Switched from deprecated google-oauth-client to google-auth-library. | google-oauth-client, google-auth-library | google-auth-library |
| 6.1.0 | requirement | Updated dependencies: added auto-value-annotations-1.8.2, google-auth-library-credentials-1.4.0, google-auth-library-oauth2-http-1.4.0, google-http-client-gson-1.41.0; updated multiple others; removed google-api-client, google-http-client-jackson2, google-oauth-client. | auto-value-annotations, google-auth-library-credentials, google-auth-library-oauth2-http, google-http-client-gson, error_prone_annotations, google-http-client, grpc-context, gson, httpclient, httpcore, opencensus-api, opencensus-contrib-http-util |  |
| 6.1.0 | migration-step | Review userlib folder after updating due to dependency changes. | userlib |  |
| 6.0.0 | requirement | Upgraded module to Mendix 9 and Atlas 3. |  |  |
| 5.4.4 | requirement | Updated netty dependencies to version 4.2.0.Final. Added 4 new codecs, updated 15 existing libraries. | netty-buffer, netty-codec, netty-codec-dns, netty-codec-http, netty-codec-http2, netty-codec-socks, netty-common, netty-handler, netty-handler-proxy, netty-resolver, netty-resolver-dns, netty-transport, netty-transport-native-unix-common, netty-codec-base, netty-codec-compression, netty-codec-marshalling, netty-codec-protobuf |  |
| 5.4.4 | migration-step | Remove old versions of updated libraries and corresponding .PushNotifications.RequiredLib from userlib folder. | userlib |  |
| 5.4.2 | requirement | Updated netty dependencies to version 4.1.109.Final. | netty-buffer, netty-codec, netty-codec-dns, netty-codec-http, netty-codec-http2, netty-codec-socks, netty-common, netty-handler, netty-handler-proxy, netty-resolver, netty-resolver-dns, netty-transport, netty-transport-native-unix-common |  |
| 5.4.2 | migration-step | Remove old versions of updated libraries and corresponding .PushNotifications.RequiredLib from userlib folder. | userlib |  |
| 5.4.1 | breaking | Migrated from legacy FCM APIs to HTTP v1 for hybrid devices. Update before 2024-06-20. |  |  |
| 5.4.1 | breaking | Switched from deprecated google-oauth-client to google-auth-library. | google-oauth-client, google-auth-library | google-auth-library |
| 5.4.1 | requirement | Updated dependencies: removed 6 libraries, added 6, updated 22 others including netty to 4.1.101.Final, slf4j-api to 2.0.7. | animal-sniffer-annotations, checker-compat-qual, google-api-client, google-http-client-jackson2, google-oauth-client, netty-all, auto-value-annotations, checker-qual, google-auth-library-credentials, google-auth-library-oauth2-http, google-http-client-gson, netty-transport-native-unix-common, commons-codec, error_prone_annotations, google-http-client, grpc-context, gson, guava, httpclient, httpcore, j2objc-annotations, netty-buffer, netty-codec, netty-codec-dns, netty-codec-http, netty-codec-http2, netty-codec-socks, netty-common, netty-handler, netty-handler-proxy, netty-resolver, netty-resolver-dns, netty-transport, opencensus-api, opencensus-contrib-http-util, pushy, slf4j-api |  |
| 5.4.1 | migration-step | Remove old versions of updated libraries and corresponding .PushNotifications.RequiredLib from userlib folder. | userlib |  |
| 5.4.0 | breaking | Removed all owner write access to device entity for User/Anonymous roles (restricted to owner only). | Device |  |
| 5.2.0 | requirement | Upgrade to Mendix 8.18.0 to ensure compatibility with Mendix 9. |  |  |
| 5.0.0 | requirement | Requires Studio Pro 8.0.0 for native mobile push notification support. |  |  |
| 4.0.4 | improvement | Notifications now play default sound when application is in background. |  |  |
| 4.0.0 | requirement | Requires Modeler Version 7.23.4 or higher to be used in 8.00. |  |  |
| 4.0.0 | breaking | Layouts now based on AtlasUI instead of NavigationsLayout Module. | Layouts, AtlasUI, NavigationsLayout | AtlasUI |
| 4.0.0 | breaking | Removed default actions for snippets to prevent errors on first imports. | snippets |  |
| 4.0.0 | improvement | Updated all dependent modules to latest versions. |  |  |
| 4.0.0 | fix | Fixed missing SLF4j library when using APNS. | SLF4j, APNS |  |

## Pusher <a id="107957"></a>
Service, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/107957)

| version | published | min Mendix |
|---|---|---|
| 4.0.0 | 2026-07-22 | 11.11.0 |
| 3.5.1 | 2026-03-18 | 10.21.1 |
| 3.5.0 | 2025-07-10 | 10.21.1 |
| 3.4.0 | 2025-07-10 | 9.18.4 |
| 3.3.0 | 2025-04-16 | 10.21.1 |
| 3.2.0 | 2025-04-14 | 9.18.4 |
| 3.1.0 | 2023-09-01 | 9.18.4 |
| 3.0.0 | 2023-04-05 | 9.18.4 |
| 2.2.1 | 2023-02-22 | 8.12.5 |
| 2.2.0 | 2022-10-26 | 8.12.5 |
| 2.1.1 | 2022-09-21 | 8.12.5 |
| 2.1.0 | 2022-07-19 | 8.12.5 |
| 2.0.1 | 2022-04-14 | 8.12.5 |
| 2.0.0 | 2020-12-21 | 8.12.5 |
| 1.0.7 | 2020-12-21 | 7.23.3 |
| 1.0.6 | 2020-12-11 | 7.23.3 |
| 1.0.5 | 2019-10-16 | 7.23.3 |
| 1.0.4 | 2019-07-29 | 7.23.3 |
| 1.0.3 | 2019-06-03 | 7.23.3 |
| 1.0.2 | 2019-05-02 | 7.23.3 |
| 1.0.1 | 2018-11-12 | 7.16.0 |
| 1.0.0 | 2018-11-09 | 7.16.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 4.0.0 | requirement | Minimum Mendix version changed to 11.11.0 |  |  |
| 4.0.0 | feature | New version of Pusher widget v4.0.0 compatible with React client | Pusher widget |  |
| 3.5.0 | improvement | Updated Java dependencies to the latest versions |  |  |
| 3.4.0 | improvement | Updated Java dependencies to the latest versions |  |  |
| 3.3.0 | improvement | Made the module compatible with Mendix 11 |  |  |
| 3.2.0 | improvement | Updated Java dependencies |  |  |
| 3.1.0 | breaking | Renamed _version folder to _internal | _version | _internal |
| 3.1.0 | migration-step | Added migration file for module dependencies |  |  |
| 3.1.0 | feature | Added .version file located at themesource/pusher/.version | .version |  |
| 3.0.0 | requirement | Minimum Mendix version changed to 9.18.4 |  |  |
| 2.2.1 | improvement | Upgraded Java libraries: commons-codec to 1.16, commons-io to 2.11.0, commons-logging to 1.2, httpclient to 4.5.13 | commons-codec, commons-io, commons-logging, httpclient |  |
| 2.2.0 | improvement | Updated gson library to v2.9.1 and included RequiredLib files | gson |  |
| 2.0.0 | migration-step | Exported module as Mendix 8.12.5 module for conversion to Mendix 9 |  |  |
| 1.0.7 | fix | Fixed module to support Mendix 7.23.3 and above |  |  |
| 1.0.6 | fix | Upgraded httpcore Java dependency to fix NoClassDefFoundError for org/apache/http/ssl/SSLContexts | httpcore |  |
| 1.0.4 | improvement | Updated widgets dependencies |  |  |
| 1.0.4 | breaking | Renamed widget to Pusher Listen for easier discovery in Select widget dialog | Listen widget | Pusher Listen |
| 1.0.2 | migration-step | Updated module to Mendix version 7.23.3 to support Mendix 8 |  |  |

## PWA Wrapper <a id="259272"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/259272)

| version | published | min Mendix |
|---|---|---|
| 1.1.0 | 2026-09-16 | 10.24.14 |
| 1.0.0 | 2026-07-17 | 10.24.14 |
| 0.1.2 | 2026-05-28 | 10.24.14 |
| 0.1.1 | 2026-05-06 | 10.24.14 |
| 0.1.0 | 2026-04-02 | 10.24.14 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.1.0 | security | Hardened WebView and native bridge security. | WebView, native bridge |  |
| 1.1.0 | improvement | Improved Node.js, Android device, ADB, and signing configuration handling. | Node.js, Android device, ADB, signing |  |

## QR Code Widget <a id="2891"></a>
Widget, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/2891)

| version | published | min Mendix |
|---|---|---|
| 1.1.0 | 2020-07-30 | 8.6.0 |

## QSM <a id="260132"></a>
Module, SIG, Partner, [marketplace](https://marketplace.mendix.com/link/component/260132)

| version | published | min Mendix |
|---|---|---|
| 1.0.1 | 2026-07-24 | 11.7.0 |
| 1.0.0 | 2026-04-16 | 11.7.0 |

## Questionnaire <a id="234"></a>
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

## Questionnaire Assistant Starter App <a id="235940"></a>
Solution, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/235940)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2025-01-14 | ? |

## QZ.io - Print to popular hardware <a id="117330"></a>
Module, Emixa, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/117330)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2021-06-02 | 8.13.2 |

## Radiobutton List <a id="20"></a>
Widget, Mendix, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/20)

| version | published | min Mendix |
|---|---|---|
| 7.1.4 | 2023-09-12 | 8.0.0 |
| 7.1.3 | 2023-01-18 | 8.0.0 |
| 7.1.2 | 2022-09-22 | 8.0.0 |
| 7.1.1 | 2020-04-23 | 8.0.0 |
| 7.1.0 | 2020-02-06 | 8.0.0 |
| 7.0.0 | 2019-11-27 | 8.0.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 7.1.3 | improvement | Remove partial deprecation, update logger messages to console instead |  |  |
| 7.1.2 | fix | Replace deprecated function to get rid of errors when using the widget in Mendix Studio Pro v8.14 or higher |  |  |
| 7.1.0 | breaking | Radio button option labels now apply HTML escape by default. Set Attribute Content to Unsecure HTML to allow HTML markup. | Attribute Content |  |
| 7.0.0 | breaking | Changed DOM structure to align with Mendix Core Radio Buttons widget |  |  |
| 7.0.0 | deprecation | Deprecated Attribute Radiobutton List. Use core Radio Buttons shipped with the platform instead. | Attribute Radiobutton List | Radio Buttons |

## Randomix <a id="115289"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/115289)

| version | published | min Mendix |
|---|---|---|
| 2.0.0 | 2023-04-18 | 9.24.0 |
| 1.0.0 | 2020-09-03 | 8.12.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.0.0 | requirement | Minimum Mendix version raised to 9.24.0. Upgrade release to support Mendix 9 and 10. |  |  |

## Range Slider <a id="52704"></a>
Widget, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/52704)

| version | published | min Mendix |
|---|---|---|
| 3.0.3 | 2026-07-22 | 9.6.0 |
| 3.0.2 | 2026-06-17 | 9.6.0 |
| 3.0.1 | 2026-02-11 | 9.6.0 |
| 3.0.0 | 2026-01-07 | 9.6.0 |
| 2.1.4 | 2024-08-28 | 9.6.0 |
| 2.1.3 | 2024-07-15 | 9.6.0 |
| 2.1.2 | 2024-06-25 | 9.6.0 |
| 2.1.1 | 2023-09-27 | 9.6.0 |
| 2.1.0 | 2023-06-06 | 9.6.0 |
| 2.0.0 | 2021-12-23 | 9.6.0 |
| 1.3.1 | 2018-12-14 | 7.13.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 3.0.3 | fix | Fixed issue where widget was not loading in Dojo client due to broken JavaScript bundle. | JavaScript bundle, Dojo client |  |
| 3.0.2 | fix | Mark labels and numeric tooltips now respect decimalPlaces and user session locale (decimal separator and thousands grouping). | mark labels, numeric tooltips, decimalPlaces, locale |  |
| 3.0.0 | breaking | Updated rc-slider library to @rc-component/slider (major version). May break current custom styling. | rc-slider, @rc-component/slider |  |
| 2.1.3 | fix | Fixed issue with initial value being reset to default min value. | initial value |  |
| 2.1.2 | fix | Fixed issue where slider tooltip would not position correctly when scrolling page. | tooltip positioning |  |
| 2.0.0 | breaking | Converted into a pluggable widget. | widget architecture |  |
| 1.3.1 | fix | On change events now triggered only when value changed; no longer double trigger on loose focus. | on change events |  |
| 1.3.1 | fix | Value no longer updated when value, upper bound or lower bound is invalid. | value update |  |
| 1.3.1 | fix | Added validation for decimal steps incompatible with lower, upper value. | decimal steps |  |

## Rating <a id="54611"></a>
Widget, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/54611)

| version | published | min Mendix |
|---|---|---|
| 3.2.2 | 2026-02-11 | 9.6.0 |
| 3.2.1 | 2023-09-27 | 9.6.0 |
| 3.2.0 | 2023-06-06 | 9.6.0 |
| 3.1.2 | 2023-05-25 | 9.6.0 |
| 3.1.1 | 2022-04-01 | 9.6.0 |
| 3.1.0 | 2021-12-23 | 9.6.0 |
| 3.0.0 | 2021-09-28 | 9.6.0 |
| 2.0.0 | 2021-05-10 | 9.0.5 |
| 1.3.2 | 2021-03-02 | 7.13.1 |
| 1.3.0 | 2018-05-11 | 7.13.1 |
| 1.2.1 | 2018-03-15 | 7.2.0 |
| 1.2.0 | 2017-08-31 | 7.2.0 |
| 1.1.3 | 2017-08-02 | 7.2.0 |
| 1.1.2 | 2017-07-20 | 7.2.0 |
| 1.1.1 | 2017-07-05 | 7.2.0 |
| 1.1 | 2017-05-30 | 7.2.0 |
| 1.0 | 2017-05-13 | 7.2.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.0.0 | breaking | DOM structure changed to allow usage of custom icons/images. |  |  |
| 2.0.0 | breaking | Editability property converted to system property and moved to common group/tab. | Editability |  |
| 2.0.0 | removal | Removed elements containing inline styles. |  |  |
| 1.3.2 | security | Fixed vulnerability issue. |  |  |

## React Swipeable <a id="232012"></a>
Widget, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/232012)

| version | published | min Mendix |
|---|---|---|
| 1.0.1 | 2024-10-18 | 9.24.24 |
| 1.0.0 | 2024-10-11 | 9.24.24 |

## Reconciliations Tool <a id="211750"></a>
Industry Template, TOCnDix, Partner, [marketplace](https://marketplace.mendix.com/link/component/211750)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2023-06-12 | 9.20.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.0.0 | requirement | Requires Mendix 9.20.0 or higher. | Mendix |  |

## Refill Demonstrator <a id="117054"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/117054)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2021-04-08 | 8.18.3 |

## Repair Manager - by Openclaims <a id="224291"></a>
Solution, Openclaims, Partner, [marketplace](https://marketplace.mendix.com/link/component/224291)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2024-04-08 | ? |

## REST DeepLink module <a id="116642"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/116642)

| version | published | min Mendix |
|---|---|---|
| 1.2.0 | 2021-01-08 | 8.12.0 |
| 1.0.0 | 2021-01-07 | 8.1.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.2.0 | requirement | Converted to 8.12.0 for Mendix 9 compatibility. Minimum Mendix version is now 8.12.0. |  |  |

## REST Responses <a id="118687"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/118687)

| version | published | min Mendix |
|---|---|---|
| 2.1.0 | 2025-11-05 | 10.21.1 |
| 2.0.0 | 2025-07-04 | 10.21.1 |
| 1.3.1 | 2025-10-27 | 9.24.2 |
| 1.3.0 | 2025-10-17 | 9.24.2 |
| 1.2.0 | 2024-12-11 | 9.24.2 |
| 1.1.2 | 2024-07-11 | 9.24.2 |
| 1.1.1 | 2023-10-26 | 9.24.2 |
| 1.1.0 | 2022-05-25 | 8.18.8 |
| 1.0.3 | 2022-01-26 | 8.18.8 |
| 1.0.2 | 2021-11-12 | 8.18.8 |
| 1.0.1 | 2021-10-27 | 8.18.8 |
| 1.0.0 | 2021-10-25 | 8.18.8 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.0.0 | breaking | Updated Java actions to the MX10 Java action setup way. | Java actions |  |
| 1.1.1 | requirement | Converted module to Mx9.24.2. | Mendix |  |
| 1.1.1 | breaking | Content-type value depends on MxErrorFormat constant and will be either application/json or application/problem+json. | Content-type |  |

## Retail Sales Configurator <a id="212755"></a>
Industry Template, TOCnDix, Partner, [marketplace](https://marketplace.mendix.com/link/component/212755)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2023-07-04 | 9.21.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.0.0 | requirement | Minimum Mendix version required is 9.21.0 | Mendix |  |

## RFP Assistant Starter App <a id="235917"></a>
Starter App, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/235917)

| version | published | min Mendix |
|---|---|---|
| 4.0.1 | 2026-07-03 | 11.12.0 |
| 3.1.0 | 2026-04-17 | 10.24.0 |
| 3.0.0 | 2026-02-10 | 10.24.0 |
| 2.0.0 | 2025-04-10 | 10.21.0 |
| 1.1.0 | 2025-03-05 | 9.24.2 |
| 1.0.0 | 2025-01-14 | 9.24.2 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 4.0.1 | requirement | Minimum Mendix version requirement increased to 11.12.0 |  |  |
| 4.0.1 | migration-step | Application configuration moved from Administration section to Studio Pro Agent Editor extension; reconfigure agents accordingly | Administration section |  |
| 4.0.1 | known-issue | Only Mendix Cloud GenAI is currently supported for text generation |  |  |
| 3.1.0 | requirement | Minimum Mendix version requirement increased to 10.24.0 |  |  |
| 3.1.0 | improvement | Application upgraded to Mendix 10.24.13 and all marketplace modules upgraded to latest versions |  |  |
| 3.1.0 | feature | Google Gemini and Mistral added as additional providers for RFP Assistant configuration |  |  |
| 3.1.0 | requirement | pdf-box dependency upgraded from version 2 to 3 for PDF questionnaire reading | pdf-box |  |
| 3.0.0 | requirement | Minimum Mendix version requirement increased to 10.24.0 |  |  |
| 3.0.0 | improvement | Application upgraded to Mendix Studio Pro 10.24.0 and all modules upgraded to latest marketplace versions |  |  |
| 2.0.0 | requirement | Minimum Mendix version requirement increased to 10.21.0 |  |  |
| 2.0.0 | requirement | Connector modules updated: Amazon Bedrock v7.0.0, GenAI Commons v3.0.0, ConversationalUi v3.0.0, Mx GenAI Connector v3.0.0, OpenAI Connector v5.0.0, PgVectorKnowledgeBase v3.0.0 | Amazon Bedrock Connector, GenAI Commons, ConversationalUi, Mx GenAI Connector, OpenAI Connector, PgVectorKnowledgeBase |  |
| 1.1.0 | requirement | React Client support added; upgrading to Mendix 10+ with react mode may require updating marketplace modules like Administration, Atlas Core, Atlas Web Content, Encryption |  |  |
| 1.1.0 | improvement | Modules updated for React Client: Amazon Bedrock v6.1.0, AWS Authentication v3.2.1, GenAI For Mendix v2.2.0, OpenAI Connector v4.2.0, PgVectorKnowledgeBase v2.4.0 | Amazon Bedrock Connector, AWS Authentication, GenAI For Mendix, OpenAI Connector, PgVectorKnowledgeBase |  |

## Rich Text <a id="74889"></a>
Widget, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/74889)

| version | published | min Mendix |
|---|---|---|
| 5.1.0 | 2026-10-01 | 9.24.0 |
| 5.0.0 | 2026-08-21 | 9.24.0 |
| 4.12.0 | 2026-04-23 | 9.24.0 |
| 4.11.2 | 2026-03-09 | 9.24.0 |
| 4.11.1 | 2026-01-30 | 9.24.0 |
| 4.11.0 | 2025-11-10 | 9.24.0 |
| 4.10.0 | 2025-10-08 | 9.24.0 |
| 4.9.0 | 2025-09-04 | 9.24.0 |
| 4.8.1 | 2025-07-29 | 9.24.0 |
| 4.8.0 | 2025-07-01 | 9.24.0 |
| 4.7.0 | 2025-06-02 | 9.24.0 |
| 4.6.1 | 2025-05-21 | 9.24.0 |
| 4.5.0 | 2025-04-03 | 9.24.0 |
| 4.4.0 | 2025-04-01 | 9.24.0 |
| 4.3.1 | 2025-03-19 | 9.24.0 |
| 4.3.0 | 2025-02-14 | 9.24.0 |
| 4.2.0 | 2025-01-16 | 9.24.0 |
| 4.1.0 | 2024-12-13 | 9.24.0 |
| 4.0.0 | 2024-10-29 | 9.24.0 |
| 3.3.1 | 2024-08-28 | 9.24.0 |
| 3.3.0 | 2024-08-16 | 9.24.0 |
| 3.2.4 | 2024-07-16 | 9.24.0 |
| 3.2.3 | 2024-06-25 | 9.24.0 |
| 3.2.2 | 2024-06-05 | 9.24.0 |
| 3.2.1 | 2024-05-27 | 9.24.0 |
| 3.2.0 | 2024-05-21 | 9.24.0 |
| 3.1.2 | 2024-05-10 | 9.24.0 |
| 3.1.1 | 2024-05-02 | 9.24.0 |
| 3.1.0 | 2024-04-23 | 9.24.0 |
| 3.0.2 | 2024-04-04 | 9.24.0 |
| 3.0.1 | 2024-03-12 | 9.24.0 |
| 3.0.0 | 2024-02-28 | 9.24.0 |
| 2.3.0 | 2024-02-08 | 9.6.0 |
| 2.2.4 | 2023-11-29 | 9.6.0 |
| 2.2.3 | 2023-10-30 | 9.6.0 |
| 2.2.2 | 2023-10-12 | 9.6.0 |
| 2.2.1 | 2023-09-27 | 9.6.0 |
| 2.2.0 | 2023-06-06 | 9.6.0 |
| 2.1.6 | 2023-04-18 | 9.6.0 |
| 2.1.5 | 2023-03-24 | 9.6.0 |
| … 22 older versions | | |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 5.1.0 | fix | Fixed issue where images resized in version 4 lost their size after upgrading to version 5. |  |  |
| 5.0.0 | breaking | Changed rich text internal WYSIWYG engine from Quill to Tiptap for better nested table support. Users should review configurations. | WYSIWYG engine | Tiptap |
| 5.0.0 | removal | Removed codemirror from code dialog viewer due to unsupported strict CSP policy, replaced with internally built code editor using highlightjs. | codemirror | highlightjs-based internal code editor |
| 4.12.0 | improvement | Added trimEnd functionality to make character count on status bar correctly count characters without new line and empty character. |  |  |
| 4.11.0 | breaking | Changed Tab keyboard behavior to add indentation instead of exiting focus from editor. | Tab keyboard behavior |  |
| 4.11.0 | breaking | Changed empty line mark from space to <br> break tag. | empty line mark |  |
| 4.10.0 | improvement | Allow white-space inline styling parsing in the widget. |  |  |
| 4.3.0 | fix | Fixed rich text accessibility with tab keypress allowing direct focus on editor. |  |  |
| 4.2.0 | breaking | Changed dimension configurations to better match CSS formats. | dimension configurations |  |
| 4.2.0 | improvement | Changed DOM order to show editor before toolbar for easier focus order. | DOM order |  |
| 4.0.0 | breaking | Updated Rich Text widget to use Quill V2 due to license change in TinyMCE. Review and adjust widget configurations after updating. | WYSIWYG engine | Quill V2 |
| 3.2.4 | improvement | Allow users to turn off sandbox_iframes through configurations. |  |  |
| 3.2.3 | security | Upgraded TinyMCE dependency to version 6.8.4 to solve CVE-2024-38357. | TinyMCE |  |
| 3.2.2 | improvement | Optimized rich text bundle size. |  |  |
| 3.1.2 | improvement | Added more options to rich text context menu with option to use native context menu. |  |  |
| 3.1.1 | security | Fixed security issue by setting sandbox_iframes and convert_unsafe_embeds to true. |  |  |
| 3.1.0 | improvement | Allow user to disable quick toolbar. |  |  |
| 3.0.0 | breaking | Built new rich text editor using TinyMCE editor replacing CKEditor 4 which reached end of life. Review configuration after updating. | editor engine | TinyMCE |
| 2.2.2 | breaking | Added Insert toolbar group as option for custom toolbar. | toolbar configuration |  |
| 2.1.6 | security | Updated ckeditor4 to version 4.21.0. | ckeditor4 |  |
| 2.1.3 | improvement | Added 1MB file size limit for pasted and dropped images. |  |  |
| 2.1.2 | breaking | Changed openlink action to open links just on mouse click without ctrl. | link behavior |  |
| 2.1.0 | security | Updated ckeditor4 to version 4.20.0 to prevent XSS. | ckeditor4 |  |
| 2.1.0 | removal | Removed CSS file for WebSpellChecker Dialog plugin as it reached end of support from ckeditor4. | CSS file for WebSpellChecker Dialog plugin |  |
| 2.0.1 | breaking | Changed behavior on clicking links in rich text editor. CMD/CTRL + Click will open link in new tab. | link behavior |  |
| 2.0.0 | breaking | Core library changed from Quill to CKEditor4. | core library |  |
| 1.3.9 | fix | Changed behavior where Rich Text could steal focus while updating content. |  |  |
| 1.3.8 | security | Improved security to comply with latest exploits. |  |  |
| 1.3.1 | known-issue | Content translatable by Chrome when Readonly-style is Rich text and Editable is Never, or Data view Editable is No. |  |  |

## Rive Animation Controller <a id="227171"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/227171)

| version | published | min Mendix |
|---|---|---|
| 1.1.0 | 2024-08-07 | 9.24.31 |
| 1.0.3 | 2025-06-09 | 9.24.31 |
| 1.0.0 | 2024-06-12 | 9.24.21 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.1.0 | requirement | Added dependency for Nanoflow Commons. | Nanoflow Commons |  |

## Runtime Core Wrapper <a id="116722"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/116722)

| version | published | min Mendix |
|---|---|---|
| 2.0.0 | 2021-09-06 | 9.3.0 |
| 1.0.1 | 2021-03-10 | 8.6.2 |
| 1.0.0 | 2021-01-26 | 8.6.2 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.0.0 | requirement | Converted to Mx9. Minimum Mendix version now 9.3.0. |  |  |

## SAML <a id="1174"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/1174)

| version | published | min Mendix |
|---|---|---|
| 4.2.3 | 2026-09-01 | 10.21.1 |
| 4.2.2 | 2026-08-20 | 10.21.1 |
| 4.2.1 | 2026-02-12 | 10.21.1 |
| 4.2.0 | 2025-10-22 | 10.21.1 |
| 4.1.2 | 2025-08-13 | 10.21.1 |
| 4.1.1 | 2025-05-29 | 10.21.1 |
| 4.1.0 | 2025-05-07 | 10.21.1 |
| 4.0.4 | 2025-10-22 | 10.12.10 |
| 4.0.3 | 2025-08-13 | 10.12.10 |
| 4.0.2 | 2025-05-07 | 10.12.10 |
| 4.0.1 | 2025-03-07 | 10.12.10 |
| 4.0.0 | 2025-01-09 | 10.12.10 |
| 3.6.27 | 2026-09-01 | 9.24.18 |
| 3.6.25 | 2026-08-20 | 9.24.18 |
| 3.6.23 | 2025-10-22 | 9.24.18 |
| 3.6.21 | 2025-08-07 | 9.24.18 |
| 3.6.19 | 2025-05-07 | 9.24.18 |
| 3.6.17 | 2025-03-07 | 9.24.18 |
| 3.6.15 | 2024-11-15 | 9.24.18 |
| 3.6.13 | 2024-10-09 | 9.24.18 |
| 3.6.11 | 2024-06-04 | 9.24.18 |
| 3.6.9 | 2024-04-11 | 9.24.1 |
| 3.6.8 | 2024-04-11 | 9.24.1 |
| 3.6.7 | 2023-11-09 | 9.24.1 |
| 3.6.6 | 2023-11-09 | 9.24.1 |
| 3.6.5 | 2023-09-25 | 9.24.1 |
| 3.6.4 | 2023-09-25 | 9.24.1 |
| 3.6.3 | 2023-05-25 | 9.24.1 |
| 3.6.2 | 2023-05-25 | 9.24.1 |
| 3.6.1 | 2023-05-10 | 9.24.1 |
| 3.6.0 | 2023-05-10 | 9.24.1 |
| 3.5.1 | 2023-04-27 | 9.22.0 |
| 3.5.0 | 2023-04-27 | 9.22.0 |
| 3.4.1 | 2023-03-30 | 9.22.0 |
| 3.4.0 | 2023-03-30 | 9.22.0 |
| 3.3.15 | 2023-07-12 | 9.12.14 |
| 3.3.14 | 2023-07-12 | 9.12.14 |
| 3.3.13 | 2023-02-20 | 9.12.5 |
| 3.3.12 | 2023-02-20 | 9.12.5 |
| 3.3.11 | 2023-01-19 | 9.12.5 |
| … 88 older versions | | |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 4.2.3 | security | Fixed account hijacking vulnerability in SAML-based authentication. Fixed CVE-2026-80465. |  |  |
| 4.2.2 | improvement | Updated Mobile Auth Token handling to use Mendix Runtime APIs for token and cookie management. | Mobile Auth Token |  |
| 4.2.2 | fix | Fixed TLS connection issue when connecting to DigiD using Artifact Binding. | DigiD, Artifact Binding |  |
| 4.2.2 | security | Fixed CVE-2026-71497. |  |  |
| 4.2.2 | requirement | Upgraded org.bouncycastle:bcpkix-jdk18on to 1.85. | org.bouncycastle:bcpkix-jdk18on |  |
| 4.2.2 | requirement | Upgraded org.bouncycastle:bcprov-jdk18on to 1.85. | org.bouncycastle:bcprov-jdk18on |  |
| 4.2.2 | requirement | Upgraded org.bouncycastle:bcutil-jdk18on to 1.85. | org.bouncycastle:bcutil-jdk18on |  |
| 4.2.2 | requirement | Upgraded org.jsoup:jsoup to 1.23.1. | org.jsoup:jsoup |  |
| 4.2.1 | feature | Enhanced SAML provisioning to support deploy-time population of named-user identifier for consistent multi-app user metering. | SAML provisioning |  |
| 4.2.1 | fix | Fixed SAML configuration issue when react client is enabled. | react client |  |
| 4.2.1 | requirement | SAML 4.2.1 requires UserCommons Module version 2.2.0 or higher. | UserCommons |  |
| 4.2.0 | feature | Enhancement for upgrades where Custom_IdPConfiguration microflow was removed and IdPConfiguration_MicroflowName constant introduced. | Custom_IdPConfiguration, IdPConfiguration_MicroflowName |  |
| 4.2.0 | fix | Fixed TLS connection issue when connected with DigiD via Artifact Binding. | DigiD, Artifact Binding |  |
| 4.2.0 | requirement | Upgraded org.bouncycastle:bcpkix-jdk18on to 1.81. | org.bouncycastle:bcpkix-jdk18on |  |
| 4.2.0 | requirement | Upgraded org.bouncycastle:bcprov-jdk18on to 1.81. | org.bouncycastle:bcprov-jdk18on |  |
| 4.2.0 | requirement | Upgraded org.bouncycastle:bcutil-jdk18on to 1.81. | org.bouncycastle:bcutil-jdk18on |  |
| 4.2.0 | deprecation | Deprecated saml1-post-binding.vm, saml2-post-artifact-binding.vm, saml2-post-simplesign-binding.vm. | saml1-post-binding.vm, saml2-post-artifact-binding.vm, saml2-post-simplesign-binding.vm |  |
| 4.1.2 | fix | Fixed resource path handling for SAML to support ApplicationRootUrl with subpath. | ApplicationRootUrl |  |
| 4.1.2 | security | Fixed CVE-2025-40758. |  |  |
| 4.1.2 | requirement | Upgraded org.apache.commons:commons-lang3 to version 3.18.0. | org.apache.commons:commons-lang3 |  |
| 4.1.0 | requirement | Version 4.1.0 for apps on Mendix 10.21.1 or higher. |  |  |
| 4.1.0 | fix | Fixed SAML20.X509Certificate.SerialNumber length. | SAML20.X509Certificate.SerialNumber |  |
| 4.1.0 | fix | Fixed deprecations to make module compatible with Mendix 10.21.1. |  |  |
| 4.0.4 | fix | Fixed TLS connection issue when connected with DigiD via Artifact Binding. | DigiD, Artifact Binding |  |
| 4.0.4 | requirement | Upgraded org.bouncycastle:bcpkix-jdk18on to 1.81. | org.bouncycastle:bcpkix-jdk18on |  |
| 4.0.4 | requirement | Upgraded org.bouncycastle:bcprov-jdk18on to 1.81. | org.bouncycastle:bcprov-jdk18on |  |
| 4.0.4 | requirement | Upgraded org.bouncycastle:bcutil-jdk18on to 1.81. | org.bouncycastle:bcutil-jdk18on |  |
| 4.0.4 | deprecation | Deprecated saml1-post-binding.vm, saml2-post-artifact-binding.vm, saml2-post-simplesign-binding.vm. | saml1-post-binding.vm, saml2-post-artifact-binding.vm, saml2-post-simplesign-binding.vm |  |
| 4.0.3 | fix | Fixed resource path handling for SAML to support ApplicationRootUrl with subpath. | ApplicationRootUrl |  |
| 4.0.3 | security | Fixed CVE-2025-40758. |  |  |
| 4.0.3 | requirement | Upgraded org.apache.commons:commons-lang3 to version 3.18.0. | org.apache.commons:commons-lang3 |  |
| 4.0.2 | fix | Fixed SAML20.X509Certificate.SerialNumber length. | SAML20.X509Certificate.SerialNumber |  |
| 4.0.1 | fix | Increased SAML20.X509Certificate.SerialNumber length to 1000 to support larger certificates. | SAML20.X509Certificate.SerialNumber |  |
| 4.0.1 | removal | Removed deprecated Model Reflection page. | Model Reflection page |  |
| 4.0.1 | requirement | Removed listenablefuture:9999.0-empty to avoid conflict with guava. | listenablefuture |  |
| 4.0.1 | deprecation | Deprecation for upcoming release: saml1-post-binding.vm, saml2-post-artifact-binding.vm, saml2-post-simplesign-binding.vm. | saml1-post-binding.vm, saml2-post-artifact-binding.vm, saml2-post-simplesign-binding.vm |  |
| 4.0.0 | feature | Allows SSO configurations to be set at design time or deploy time using Application Constants. |  |  |
| 4.0.0 | feature | Java Dependency Management (JDM) is supported. |  |  |
| 4.0.0 | feature | New mechanism for creating custom user-provisioning with enhanced similarity to OIDC SSO module. |  |  |
| 4.0.0 | breaking | evaluateMultipleUserMatches is migrated from SAML to usercommons. | evaluateMultipleUserMatches |  |
| 4.0.0 | requirement | SAML 4.0.0 requires Studio Pro version 10.12.10 or higher. |  |  |
| 4.0.0 | requirement | Added UserCommons Module as dependency for SAML. | UserCommons |  |
| 4.0.0 | migration-step | To resolve UI errors in upgrade scenario, upgrade Atlas Core to latest version. | Atlas Core |  |
| 4.0.0 | deprecation | Previous mechanism for user provisioning is deprecated and will not be supported in next SAML release. |  |  |
| 4.0.0 | breaking | Pre-configured possibility to use InCommon Federation is no longer supported. | InCommon Federation |  |
| 3.6.27 | security | Fixed account hijacking vulnerability in SAML-based authentication. Fixed CVE-2026-80465. |  |  |
| 3.6.25 | security | Fixed CVE-2026-71497. |  |  |
| 3.6.25 | requirement | Upgraded org.bouncycastle:bcpkix-jdk18on to 1.85. | org.bouncycastle:bcpkix-jdk18on |  |
| 3.6.25 | requirement | Upgraded org.bouncycastle:bcprov-jdk18on to 1.85. | org.bouncycastle:bcprov-jdk18on |  |
| 3.6.25 | requirement | Upgraded org.bouncycastle:bcutil-jdk18on to 1.85. | org.bouncycastle:bcutil-jdk18on |  |
| 3.6.25 | requirement | Upgraded org.jsoup:jsoup to 1.23.1. | org.jsoup:jsoup |  |
| 3.6.25 | migration-step | Delete all Java libraries from userlib folder of old SAML module before upgrading to avoid conflicts. |  |  |
| 3.6.23 | fix | Fixed TLS connection issue when connected with DigiD via Artifact Binding. | DigiD, Artifact Binding |  |
| 3.6.23 | fix | Increased SAML20.X509Certificate.SerialNumber length to 1000 to support larger certificates. | SAML20.X509Certificate.SerialNumber |  |
| 3.6.23 | requirement | Upgraded org.bouncycastle:bcpkix-jdk18on to 1.81. | org.bouncycastle:bcpkix-jdk18on |  |
| 3.6.23 | requirement | Upgraded org.bouncycastle:bcprov-jdk18on to 1.81. | org.bouncycastle:bcprov-jdk18on |  |
| 3.6.23 | requirement | Upgraded org.bouncycastle:bcutil-jdk18on to 1.81. | org.bouncycastle:bcutil-jdk18on |  |
| 3.6.23 | migration-step | Delete all Java libraries from userlib folder of old SAML module before upgrading to avoid conflicts. |  |  |
| 3.6.23 | deprecation | Deprecated saml1-post-binding.vm, saml2-post-artifact-binding.vm, saml2-post-simplesign-binding.vm. | saml1-post-binding.vm, saml2-post-artifact-binding.vm, saml2-post-simplesign-binding.vm |  |
| 3.6.21 | fix | Improved URL validation to fix redirect issues during SAML login. |  |  |
| 3.6.21 | security | Fixed CVE-2025-40758. |  |  |
| 3.6.21 | requirement | Upgraded org.apache.commons:commons-lang3 to version 3.18.0. | org.apache.commons:commons-lang3 |  |
| 3.6.21 | migration-step | Delete all Java libraries from userlib folder of old SAML module before upgrading to avoid conflicts. |  |  |
| 3.6.19 | fix | Fixed SAML20.X509Certificate.SerialNumber length. | SAML20.X509Certificate.SerialNumber |  |
| 3.6.17 | deprecation | Deprecation for upcoming release: saml1-post-binding.vm, saml2-post-artifact-binding.vm, saml2-post-simplesign-binding.vm. | saml1-post-binding.vm, saml2-post-artifact-binding.vm, saml2-post-simplesign-binding.vm |  |
| 3.6.15 | improvement | Enhanced XML parsing and improved handling of entity expansion and external entity resolution (Ticket #232023). | XML parsing, entity expansion, external entity resolution |  |
| 3.6.15 | requirement | Upgraded commons-io library to its latest version. | commons-io |  |
| 3.6.15 | migration-step | Delete all Java libraries used by the old SAML module from the userlib folder before upgrading. | userlib |  |
| 3.6.15 | removal | No longer supporting v.3.6.14 for Mx9 apps using Atlas UI v2 (e.g. Mx8 apps upgraded to Mx9). | 3.6.14, Atlas UI v2 |  |
| 3.6.11 | requirement | Upgraded Bouncy Castle version to 1.78.1 (Ticket #217944). | Bouncy Castle |  |
| 3.6.11 | migration-step | Delete all Java libraries used by the old SAML module from the userlib folder before upgrading. | userlib |  |
| 3.6.11 | removal | SAML module no longer supporting Mx9 apps using Atlas UI v2. | Atlas UI v2 |  |
| 3.6.11 | removal | Not planning to release v.3.6.10 for Mx9 apps using Atlas UI v2 (e.g. Mx8 apps upgraded to Mx9). | 3.6.10, Atlas UI v2 |  |
| 3.6.9 | security | Fixed Vulnerability - Cleartext Transmission of Sensitive Information (Ticket #204774). |  |  |
| 3.6.9 | requirement | Upgraded xmlsec library to its latest version. | xmlsec |  |
| 3.6.9 | migration-step | Delete all Java libraries used by the old SAML module from the userlib folder before upgrading. | userlib |  |
| 3.6.8 | security | Fixed Vulnerability - Cleartext Transmission of Sensitive Information (Ticket #204774). |  |  |
| 3.6.8 | requirement | Upgraded xmlsec library to its latest version. | xmlsec |  |
| 3.6.8 | migration-step | Delete all Java libraries used by the old SAML module from the userlib folder before upgrading. | userlib |  |
| 3.6.5 | requirement | Upgraded few libraries to latest versions (Ticket#194306). |  |  |
| 3.6.5 | removal | Removed unused libraries (Ticket#194306). |  |  |
| 3.6.5 | migration-step | Delete all Java libraries used by the old SAML module from the userlib folder before upgrading. | userlib |  |
| 3.6.4 | requirement | Upgraded few libraries to latest versions (Ticket#194306). |  |  |
| 3.6.4 | removal | Removed unused libraries (Ticket#194306). |  |  |
| 3.6.4 | migration-step | Delete all Java libraries used by the old SAML module from the userlib folder before upgrading. | userlib |  |
| 3.6.3 | deprecation | Solved deprecations to make the module Mendix 10 compatible. |  |  |
| 3.6.3 | requirement | Few java libraries updated to latest versions. |  |  |
| 3.6.3 | migration-step | Delete all Java libraries used by the old SAML module from the userlib folder before upgrading. | userlib |  |
| 3.6.2 | deprecation | Solved deprecations to make the module Mendix 10 compatible. |  |  |
| 3.6.2 | requirement | Few java libraries updated to latest versions. |  |  |
| 3.6.2 | migration-step | Delete all Java libraries used by the old SAML module from the userlib folder before upgrading. | userlib |  |
| 3.6.1 | breaking | Renamed ReadOnly role to Admin_ReadSAMLEntities. | ReadOnly | Admin_ReadSAMLEntities |
| 3.6.1 | security | Added fix of CVE-2023-25957 that prevents configuration mistakes when using POST binding on SAML responses. | POST binding, SAML responses |  |
| 3.6.1 | requirement | Upgraded to Studio Pro v9.24.1. | Studio Pro |  |
| 3.6.1 | improvement | SAML Module userlib includes only its dependency libraries (Ticket # 184521). | userlib |  |
| 3.6.1 | migration-step | If ReadOnly role used in App security, then update to Admin_ReadSAMLEntities role. | ReadOnly |  |
| 3.6.0 | breaking | Renamed ReadOnly role to Admin_ReadSAMLEntities. | ReadOnly | Admin_ReadSAMLEntities |
| 3.6.0 | security | Added fix of CVE-2023-25957 that prevents configuration mistakes when using POST binding on SAML responses. | POST binding, SAML responses |  |
| 3.6.0 | requirement | Upgraded to Studio Pro v9.24.1. | Studio Pro |  |
| 3.6.0 | improvement | SAML Module userlib includes only its dependency libraries (Ticket # 184521). | userlib |  |
| 3.6.0 | migration-step | If ReadOnly role used in App security, then update to Admin_ReadSAMLEntities role. | ReadOnly |  |
| 3.5.1 | feature | Support for independent keypairs per IDP that can be uploaded or self-generated; keystore configuration moved to IDP tab with automatic migration. | keypairs, IDP configuration |  |
| 3.5.1 | requirement | Require Encryption module as a dependency for v3.5.0 and above. | Encryption |  |
| 3.5.0 | feature | Support for independent keypairs per IDP that can be uploaded or self-generated; keystore configuration moved to IDP tab with automatic migration. | keypairs, IDP configuration |  |
| 3.5.0 | requirement | Require Encryption module as a dependency for v3.5.0 and above. | Encryption |  |
| 3.4.1 | requirement | Upgraded to Studio Pro v9.22.0. | Studio Pro |  |
| 3.4.1 | requirement | Upgraded com.fasterxml.woodstox:woodstox-core from 6.2.4.jar to 6.5.0.jar (Ticket # 180852). | woodstox-core |  |
| 3.4.1 | migration-step | Delete all Java libraries used by the old SAML module from the userlib folder before upgrading. | userlib |  |
| 3.4.0 | requirement | Upgraded to Studio Pro v9.22.0. | Studio Pro |  |
| 3.4.0 | requirement | Upgraded com.fasterxml.woodstox:woodstox-core from 6.2.4.jar to 6.5.0.jar (Ticket # 180852). | woodstox-core |  |
| 3.4.0 | migration-step | Delete all Java libraries used by the old SAML module from the userlib folder before upgrading. | userlib |  |
| 3.3.15 | breaking | Renamed ReadOnly role to Admin_ReadSAMLEntities. | ReadOnly | Admin_ReadSAMLEntities |
| 3.3.15 | security | Fixed CVE-2023-25957. |  |  |
| 3.3.15 | requirement | Few java libraries updated to latest versions. |  |  |
| 3.3.15 | migration-step | Delete all Java libraries used by the old SAML module from the userlib folder before upgrading. | userlib |  |
| 3.3.15 | migration-step | If ReadOnly role used in App security, then update to Admin_ReadSAMLEntities role. | ReadOnly |  |
| 3.3.14 | breaking | Renamed ReadOnly role to Admin_ReadSAMLEntities. | ReadOnly | Admin_ReadSAMLEntities |
| 3.3.14 | security | Fixed CVE-2023-25957. |  |  |
| 3.3.14 | requirement | Few java libraries updated to latest versions. |  |  |
| 3.3.14 | migration-step | Delete all Java libraries used by the old SAML module from the userlib folder before upgrading. | userlib |  |
| 3.3.14 | migration-step | If ReadOnly role used in App security, then update to Admin_ReadSAMLEntities role. | ReadOnly |  |
| 3.3.13 | requirement | Upgraded commons-io from 2.8.0 to 2.11.0 (Ticket #176198) | commons-io |  |
| 3.3.13 | breaking | Renamed all .Required file names to .RequiredLib in the userlib folder |  |  |
| 3.3.13 | migration-step | Delete all Java libraries used by the old SAML module from userlib folder before upgrading |  |  |
| 3.3.12 | requirement | Upgraded commons-io from 2.8.0 to 2.11.0 (Ticket #176198) | commons-io |  |
| 3.3.12 | breaking | Renamed all .Required file names to .RequiredLib in the userlib folder |  |  |
| 3.3.12 | migration-step | Delete all Java libraries used by the old SAML module from userlib folder before upgrading |  |  |
| 3.3.11 | requirement | Upgraded org.bouncycastle bcpkix-jdk15on-1.69 to jdk15to18-1.70 (Ticket #172523, #173264, #175781) | org.bouncycastle:bcpkix-jdk15on, org.bouncycastle:bcrov-jdk15on, org.bouncycastle:bcutil-jdk15on |  |
| 3.3.11 | requirement | Upgraded org.bouncycastle bcrov-jdk15on-1.69 to jdk15to18-1.70 (Ticket #172523, #173264, #175781) | org.bouncycastle:bcrov-jdk15on |  |
| 3.3.11 | requirement | Upgraded org.bouncycastle bcutil-jdk15on-1.69 to jdk15to18-1.70 (Ticket #172523, #173264, #175781) | org.bouncycastle:bcutil-jdk15on |  |
| 3.3.11 | migration-step | Delete all Java libraries used by the old SAML module from userlib folder before upgrading |  |  |
| 3.3.10 | requirement | Upgraded org.bouncycastle bcpkix-jdk15on-1.69 to jdk15to18-1.70 (Ticket #172523, #173264, #175781) | org.bouncycastle:bcpkix-jdk15on, org.bouncycastle:bcrov-jdk15on, org.bouncycastle:bcutil-jdk15on |  |
| 3.3.10 | requirement | Upgraded org.bouncycastle bcrov-jdk15on-1.69 to jdk15to18-1.70 (Ticket #172523, #173264, #175781) | org.bouncycastle:bcrov-jdk15on |  |
| 3.3.10 | requirement | Upgraded org.bouncycastle bcutil-jdk15on-1.69 to jdk15to18-1.70 (Ticket #172523, #173264, #175781) | org.bouncycastle:bcutil-jdk15on |  |
| 3.3.10 | migration-step | Delete all Java libraries used by the old SAML module from userlib folder before upgrading |  |  |
| 3.3.9 | security | Fixed security vulnerability (9.3 - CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:N/E:P/RL:O/RC:C) affecting v3.3.0 to v3.3.7 |  |  |
| 3.3.8 | security | Fixed security vulnerability (9.3 - CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:N/E:P/RL:O/RC:C) affecting v3.3.0 to v3.3.7 |  |  |
| 3.3.7 | breaking | Moved Authentication related configuration options from Provisioning tab to Request Authn context tab |  |  |
| 3.3.7 | requirement | Upgraded org.slf4j slf4j-api to 2.0.3 (Ticket #167757) | org.slf4j:slf4j-api, org.slf4j:slf4j-simple |  |
| 3.3.7 | requirement | Upgraded org.slf4j slf4j-simple to 2.0.3 (Ticket #167757) | org.slf4j:slf4j-simple |  |
| 3.3.7 | migration-step | Delete all Java libraries used by the old SAML module from userlib folder before upgrading |  |  |
| 3.3.6 | breaking | Moved Authentication related configuration options from Provisioning tab to Request Authn context tab |  |  |
| 3.3.6 | requirement | Upgraded org.slf4j slf4j-api to 2.0.3 (Ticket #167757) | org.slf4j:slf4j-api, org.slf4j:slf4j-simple |  |
| 3.3.6 | requirement | Upgraded org.slf4j slf4j-simple to 2.0.3 (Ticket #167757) | org.slf4j:slf4j-simple |  |
| 3.3.6 | migration-step | Delete all Java libraries used by the old SAML module from userlib folder before upgrading |  |  |
| 3.3.5 | security | Fixed CVE-2022-44457 |  |  |
| 3.3.4 | security | Fixed CVE-2022-44457 |  |  |
| 3.3.1 | requirement | Upgraded to latest LTS/MTS Studio pro v9.12.5 |  |  |
| 3.3.1 | security | Fixed CVE-2022-37011 |  |  |
| 3.3.1 | security | Fixed security vulnerability (9.1 – CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N) |  |  |
| 3.3.1 | requirement | Upgraded org.bouncycastle bcpkix-jdk15on to 1.69 (Ticket #152939) | org.bouncycastle:bcpkix-jdk15on, org.bouncycastle:bcrov-jdk15on, org.bouncycastle:bcutil-jdk15on |  |
| 3.3.1 | requirement | Upgraded org.bouncycastle bcrov-jdk15on to 1.69 (Ticket #152939) | org.bouncycastle:bcrov-jdk15on |  |
| 3.3.1 | requirement | Upgraded org.bouncycastle bcutil-jdk15on to 1.69 (Ticket #152939) | org.bouncycastle:bcutil-jdk15on |  |
| 3.3.1 | migration-step | Delete all Java libraries used by the old SAML module from userlib folder before upgrading |  |  |
| 3.3.0 | requirement | Upgraded to latest LTS/MTS Studio pro v9.12.5 |  |  |
| 3.3.0 | improvement | Improved message validation to better handle different parts of message being signed and/or encrypted |  |  |
| 3.3.0 | security | Fixed CVE-2022-37011 |  |  |
| 3.3.0 | security | Fixed security vulnerability (9.1 – CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N) |  |  |
| 3.3.0 | feature | In-Session Authentication |  |  |
| 3.3.0 | feature | Artifact binding on SAML responses |  |  |
| 3.3.0 | feature | Requesting user attributes at IDP via SAML's AttributeConsumingService concept |  |  |
| 3.3.0 | feature | Separate SP-metadata can be exported per IDP; SP-Metadata download moved from SP Configuration tab to IDP Configuration Overview tab |  |  |
| 3.3.0 | feature | Handling of encrypted nameID |  |  |
| 3.3.0 | requirement | Library upgrade: org.bouncycastle libraries (bcpkix-jdk15on, bcrov-jdk15on, bcutil-jdk15on) to 1.69 | org.bouncycastle:bcpkix-jdk15on, org.bouncycastle:bcrov-jdk15on, org.bouncycastle:bcutil-jdk15on |  |
| 3.3.0 | migration-step | Delete all Java libraries used by old SAML module from userlib folder before upgrading due to potential library conflicts |  |  |
| 3.2.7 | breaking | Renamed ReadOnly role to Admin_ReadSAMLEntities | ReadOnly | Admin_ReadSAMLEntities |
| 3.2.7 | security | Fixed CVE-2023-25957 |  |  |
| 3.2.7 | security | Fixed CVE-2022-37011 |  |  |
| 3.2.7 | requirement | Few Java libraries updated to latest versions |  |  |
| 3.2.7 | migration-step | Delete all Java libraries used by old SAML module from userlib folder before upgrading due to potential library conflicts |  |  |
| 3.2.7 | migration-step | If ReadOnly role used in App security, update to Admin_ReadSAMLEntities role | ReadOnly |  |
| 3.2.6 | breaking | Renamed ReadOnly role to Admin_ReadSAMLEntities | ReadOnly | Admin_ReadSAMLEntities |
| 3.2.6 | security | Fixed CVE-2023-25957 |  |  |
| 3.2.6 | security | Fixed CVE-2022-37011 |  |  |
| 3.2.6 | requirement | Few Java libraries updated to latest versions |  |  |
| 3.2.6 | migration-step | Delete all Java libraries used by old SAML module from userlib folder before upgrading due to potential library conflicts |  |  |
| 3.2.6 | migration-step | If ReadOnly role used in App security, update to Admin_ReadSAMLEntities role | ReadOnly |  |
| 3.2.5 | requirement | Library upgrades: woodstox-core to 6.2.4, stax2-api to 4.2.1 | com.fasterxml.woodstox:woodstox-core, org.codehaus.woodstox:stax2-api |  |
| 3.2.5 | migration-step | Delete all Java libraries used by old SAML module from userlib folder before upgrading due to potential library conflicts |  |  |
| 3.2.4 | requirement | Library upgrades: woodstox-core to 6.2.4, stax2-api to 4.2.1 | com.fasterxml.woodstox:woodstox-core, org.codehaus.woodstox:stax2-api |  |
| 3.2.4 | migration-step | Delete all Java libraries used by old SAML module from userlib folder before upgrading due to potential library conflicts |  |  |
| 3.2.3 | security | Fixed CVE-2022-32285 |  |  |
| 3.2.3 | security | Fixed CVE-2022-32286 |  |  |
| 3.2.2 | improvement | Expiry date for TokenInformation object can be set by overriding HybridAppLoginTimeOutInMinutes constant | TokenInformation, HybridAppLoginTimeOutInMinutes |  |
| 3.2.2 | improvement | Improved creation of mobile tokens to get consistent re-login on iOS devices |  |  |
| 3.2.2 | security | Fixed CVE-2022-32285 |  |  |
| 3.2.2 | security | Fixed CVE-2022-32286 |  |  |
| 3.2.1 | improvement | Logging made consistent with Mx7 version |  |  |
| 3.2.1 | fix | Fixed missing HttpOnly flag on cookies set by SAML Module |  |  |
| 3.2.1 | breaking | Removed library javax.xml.soap-api-1.4.0.jar and upgraded jakarta.xml.soap-api to version 2.0.1 | javax.xml.soap-api-1.4.0.jar, jakarta.xml.soap-api | jakarta.xml.soap-api-2.0.1 |
| 3.2.1 | migration-step | Delete all Java libraries used by old SAML module from userlib folder before upgrading due to potential library conflicts |  |  |
| 3.2.0 | improvement | Logging made consistent with Mx7 version |  |  |
| 3.2.0 | fix | Fixed missing HttpOnly flag on cookies set by SAML Module |  |  |
| 3.2.0 | breaking | Removed library javax.xml.soap-api-1.4.0.jar and upgraded jakarta.xml.soap-api to version 2.0.1 | javax.xml.soap-api-1.4.0.jar, jakarta.xml.soap-api | jakarta.xml.soap-api-2.0.1 |
| 3.2.0 | migration-step | Delete all Java libraries used by old SAML module from userlib folder before upgrading due to potential library conflicts |  |  |
| 3.1.9 | breaking | Increased the Value attribute's character limit in AssertionAttribute Entity | AssertionAttribute |  |
| 3.1.9 | improvement | Added AuthnRequestsSigned and WantAssertionsSigned attributes to SPSSODescriptor in SPMetadata when encryption is enabled | SPSSODescriptor |  |
| 3.1.9 | improvement | Custom provisioning and signing microflows are now configurable on IDP level in IDP Configuration |  |  |
| 3.1.8 | breaking | Increased the Value attribute's character limit in AssertionAttribute Entity | AssertionAttribute |  |
| 3.1.8 | improvement | Added AuthnRequestsSigned and WantAssertionsSigned attributes to SPSSODescriptor in SPMetadata when encryption is enabled | SPSSODescriptor |  |
| 3.1.8 | improvement | Custom provisioning and signing microflows are now configurable on IDP level in IDP Configuration |  |  |
| 3.1.7 | requirement | Library upgrade owasp-java-html-sanitizer from 20200713.1 to version 20211018.2 | owasp-java-html-sanitizer |  |
| 3.1.7 | migration-step | Delete all Java libraries used by old SAML module from userlib folder before upgrading due to potential library conflicts |  |  |
| 3.1.6 | requirement | Library upgrade owasp-java-html-sanitizer from 20200713.1 to version 20211018.2 | owasp-java-html-sanitizer |  |
| 3.1.6 | migration-step | Delete all Java libraries used by old SAML module from userlib folder before upgrading due to potential library conflicts |  |  |
| 3.1.5 | requirement | Library upgrades: org.apache.santuario:xmlsec to 2.2.3, org.apache.velocity:velocity-1.7 to velocity-engine-core 2.3 | org.apache.santuario:xmlsec, org.apache.velocity:velocity-engine-core |  |
| 3.1.5 | migration-step | Delete all Java libraries used by old SAML module from userlib folder before upgrading due to potential library conflicts |  |  |
| 3.1.4 | requirement | Library upgrades: org.apache.santuario:xmlsec to 2.2.3, org.apache.velocity:velocity-1.7 to velocity-engine-core 2.3 | org.apache.santuario:xmlsec, org.apache.velocity:velocity-engine-core |  |
| 3.1.4 | migration-step | Delete all Java libraries used by old SAML module from userlib folder before upgrading due to potential library conflicts |  |  |
| 3.1.3 | requirement | Mx9 New version supports Atlas 3.0 UI for apps newly developed in Mx9, compatible with Studio Pro 9.1.0 through 9.3.0 |  |  |
| 3.1.3 | improvement | Logging confirming to the LogLevel settings and Mendix standard |  |  |
| 3.1.2 | requirement | Mx9 Upgrade version supports Atlas 2.0 UI for apps upgrading from Mx8/Mx7 to Mx9, compatible with Studio Pro 9.1.0 through 9.3.0 |  |  |
| 3.1.2 | improvement | Logging confirming to the LogLevel settings and Mendix standard |  |  |
| 3.1.1 | requirement | Supports Atlas 3.0 UI, compatible with Studio Pro 9.1.0 through 9.3.0 | Atlas 3.0 |  |
| 3.0.5 | requirement | Supports Atlas 2.0 UI, compatible with Studio Pro 9.1.0 through 9.3.0 | Atlas 2.0 |  |
| 2.4.8 | security | Fixed CVE-2025-40758 |  |  |
| 2.4.7 | improvement | Improvement to index file to work with CSP headers (Ticket #240984) | index file |  |
| 2.4.7 | requirement | Upgraded commons-pool to 2.11.1 | commons-pool |  |
| 2.4.7 | requirement | Upgraded cryptacular to 1.2.5 | cryptacular |  |
| 2.4.7 | requirement | Upgraded httpclient to 4.5.14 | httpclient |  |
| 2.4.7 | requirement | Upgraded httpcore to 4.4.16 | httpcore |  |
| 2.4.7 | requirement | Upgraded jakarta.xml.soap-api to 3.0.0 | jakarta.xml.soap-api |  |
| 2.4.7 | requirement | Upgraded java-support to 7.5.2 | java-support |  |
| 2.4.7 | requirement | Upgraded joda-time to 2.12.5 | joda-time |  |
| 2.4.7 | requirement | Upgraded jsoup to 1.16.1 | jsoup |  |
| 2.4.7 | requirement | Upgraded metrics-core to 4.2.18 | metrics-core |  |
| 2.4.7 | requirement | Upgraded opensaml to 3.4.6 | opensaml |  |
| 2.4.7 | requirement | Upgraded slf4j-api to 2.0.7 | slf4j-api |  |
| 2.4.7 | requirement | Upgraded txw2 to 4.0.2 | txw2 |  |
| 2.4.7 | requirement | Upgraded xercesImpl to 2.12.2-sp1 | xercesImpl |  |
| 2.4.7 | migration-step | Delete all Java libraries used by old SAML module from userlib folder before upgrading |  |  |
| 2.4.7 | deprecation | Following files will be deprecated: saml1-post-binding.vm, saml2-post-artifact-binding.vm, saml2-post-simplesign-binding.vm | saml1-post-binding.vm, saml2-post-artifact-binding.vm, saml2-post-simplesign-binding.vm |  |
| 2.4.6 | improvement | Enhanced XML parsing and improved entity expansion and external entity resolution (Ticket #232023) | XML parsing |  |
| 2.4.6 | requirement | Upgraded commons-io library to latest version | commons-io |  |
| 2.4.6 | migration-step | Delete all Java libraries used by old SAML module from userlib folder before upgrading |  |  |
| 2.4.4 | requirement | Upgraded Bouncy Castle version to 1.78.1 (Ticket #217944) | Bouncy Castle |  |
| 2.4.4 | migration-step | Delete all Java libraries used by old SAML module from userlib folder before upgrading |  |  |
| 2.4.3 | improvement | Removed static nonce and inline scripts in SAML Custom Login page (Ticket #207361) | SAML Custom Login page |  |
| 2.4.3 | security | Fixed vulnerability - Cleartext Transmission of Sensitive Information (Ticket #204774) |  |  |
| 2.4.3 | requirement | Upgraded xmlsec library to latest version | xmlsec |  |
| 2.4.3 | migration-step | Delete all Java libraries used by old SAML module from userlib folder before upgrading |  |  |
| 2.4.1 | improvement | Improvement to index file to work with CSP headers (Ticket #184978) | index file |  |
| 2.4.1 | requirement | Upgraded several libraries to latest versions (Ticket #194306) |  |  |
| 2.4.1 | improvement | Removed unused libraries (Ticket #194306) |  |  |
| 2.4.1 | migration-step | Delete all Java libraries used by old SAML module from userlib folder before upgrading |  |  |
| 2.4.0 | breaking | Renamed ReadOnly role to Admin_ReadSAMLEntities | ReadOnly role | Admin_ReadSAMLEntities |
| 2.4.0 | security | Added fix of CVE-2023-25957 preventing configuration mistakes using POST binding on SAML responses | POST binding |  |
| 2.4.0 | migration-step | If ReadOnly role used in App security, update to Admin_ReadSAMLEntities role | ReadOnly role |  |
| 2.3.7 | requirement | Upgraded woodstox-core from 6.2.4 to 6.5.0 (Ticket #180852) | woodstox-core |  |
| 2.3.7 | migration-step | Delete all Java libraries used by old SAML module from userlib folder before upgrading |  |  |
| 2.3.6 | requirement | Upgraded commons-io from 2.8.0 to 2.11.0 (Ticket #176198) | commons-io |  |
| 2.3.6 | migration-step | Renamed all .Required file names to .RequiredLib in userlib folder |  |  |
| 2.3.6 | migration-step | Delete all Java libraries used by old SAML module from userlib folder before upgrading |  |  |
| 2.3.5 | requirement | Upgraded bcpkix-jdk15on from 1.69 to jdk15to18-1.70 (Ticket #172523) | bcpkix-jdk15on |  |
| 2.3.5 | requirement | Upgraded bcrov-jdk15on from 1.69 to jdk15to18-1.70 (Ticket #173264) | bcrov-jdk15on |  |
| 2.3.5 | requirement | Upgraded bcutil-jdk15on from 1.69 to jdk15to18-1.70 (Ticket #175781) | bcutil-jdk15on |  |
| 2.3.5 | migration-step | Delete all Java libraries used by old SAML module from userlib folder before upgrading |  |  |
| 2.3.4 | security | Fixed security vulnerability (9.3 - CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:N/E:P/RL:O/RC:C) |  |  |
| 2.3.3 | breaking | Moved Authentication related configuration options from Provisioning tab to Request Authn context tab | Provisioning tab, Request Authn context tab |  |
| 2.3.3 | requirement | Upgraded slf4j-api to 2.0.3 (Ticket #167757) | slf4j-api |  |
| 2.3.3 | requirement | Upgraded slf4j-simple to 2.0.3 (Ticket #167757) | slf4j-simple |  |
| 2.3.3 | migration-step | Delete all Java libraries used by old SAML module from userlib folder before upgrading |  |  |
| 2.3.2 | security | Fixed CVE-2022-44457 |  |  |
| 2.3.0 | requirement | Upgraded to latest LTS/MTS Studio Pro v8.18.19 |  |  |
| 2.3.0 | improvement | Improved message validation to better handle different parts being signed/encrypted | message validation |  |
| 2.3.0 | security | Fixed CVE-2022-37011 |  |  |
| 2.3.0 | security | Fixed security vulnerability (9.1 – CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N) |  |  |
| 2.3.0 | requirement | Upgraded bcpkix-jdk15on to 1.69 (Ticket #152939) | bcpkix-jdk15on |  |
| 2.3.0 | requirement | Upgraded bcrov-jdk15on to 1.69 (Ticket #152939) | bcrov-jdk15on |  |
| 2.3.0 | requirement | Upgraded bcutil-jdk15on to 1.69 (Ticket #152939) | bcutil-jdk15on |  |
| 2.3.0 | migration-step | Delete all Java libraries used by old SAML module from userlib folder before upgrading |  |  |
| 2.2.3 | requirement | com.fasterxml.woodstox:woodstox-core upgraded to 6.2.4; org.codehaus.woodstox:stax2-api upgraded to 4.2.1 | com.fasterxml.woodstox:woodstox-core, org.codehaus.woodstox:stax2-api |  |
| 2.2.3 | migration-step | Delete all Java libraries from old SAML module in userlib folder before upgrading due to potential conflicts |  |  |
| 2.2.2 | improvement | Expiry date for TokenInformation can be set by overriding HybridAppLoginTimeOutInMinutes constant | TokenInformation, HybridAppLoginTimeOutInMinutes |  |
| 2.2.2 | migration-step | Renamed lognode SAML to SAML_SSO in example microflows to prevent extra unused lognode | SAML, SAML_SSO | SAML_SSO |
| 2.2.2 | security | Fixed CVE-2022-32285 |  |  |
| 2.2.2 | security | Fixed CVE-2022-32286 |  |  |
| 2.2.1 | requirement | Removed javax.xml.soap-api-1.4.0.jar; upgraded jakarta.xml.soap-api to 2.0.1 | javax.xml.soap-api, jakarta.xml.soap-api | jakarta.xml.soap-api-2.0.1 |
| 2.2.1 | migration-step | Delete all Java libraries from old SAML module in userlib folder before upgrading due to potential conflicts |  |  |
| 2.2.0 | improvement | Increased Value attribute character limit in AssertionAttribute Entity | AssertionAttribute |  |
| 2.2.0 | improvement | Added AuthnRequestsSigned and WantAssertionsSigned attributes to SPSSODescriptor in SPMetadata when encryption enabled | SPSSODescriptor, SPMetadata |  |
| 2.2.0 | improvement | Custom provisioning and signing microflows now configurable on IDP level in IDP Configuration |  |  |
| 2.1.9 | requirement | Library upgrade owasp-java-html-sanitizer to version 20211018.2 | owasp-java-html-sanitizer |  |
| 2.1.9 | migration-step | Delete all Java libraries from old SAML module in userlib folder before upgrading due to potential conflicts |  |  |
| 2.1.8 | requirement | Library upgrade org.apache.santuario:xmlsec to version 2.2.3 | org.apache.santuario:xmlsec |  |
| 2.1.8 | requirement | Upgraded org.apache.velocity:velocity-1.7 to org.apache.velocity:velocity-engine-core version 2.3 | org.apache.velocity:velocity-engine-core | org.apache.velocity:velocity-engine-core-2.3 |
| 2.1.8 | migration-step | Delete all Java libraries from old SAML module in userlib folder before upgrading due to potential conflicts |  |  |
| 2.1.6 | requirement | Library upgrades bcpkix-jdk15on and bcprov-jdk15on to version 1.67 | bcpkix-jdk15on, bcprov-jdk15on |  |
| 2.1.6 | migration-step | Delete all Java libraries from old SAML module in userlib folder; especially BountyCastle libraries may conflict |  |  |
| 2.1.5 | improvement | MxSAMLAssertion ValidationLevel configuration always considered as ValidationLevel.Strict as security measure | MxSAMLAssertion, ValidationLevel |  |
| 2.1.5 | migration-step | Delete all Java libraries from old SAML module; especially opensaml-2.6.6.jar may cause conflicts |  |  |
| 2.1.4 | requirement | Library update commons-lang to version 2.6 | commons-lang |  |
| 2.1.4 | requirement | Library update jakarta.xml.soap-api to version 1.4.1 | jakarta.xml.soap-api |  |
| 2.1.3 | requirement | Update to xercesImpl-2.12.1-sp1 | xercesImpl |  |
| 2.1.2 | security | SAML20 JAR library upgrade fixing multiple important vulnerabilities |  |  |
| 2.1.2 | requirement | requiredLib folder updates | requiredLib |  |
| 2.1.2 | requirement | Library upgrade Gauva from version 27 to 31 | Gauva |  |
| 2.0.0 | requirement | Converted module to Mendix 8.0.0.56467 |  |  |
| 1.18.0 | breaking | Renamed ReadOnly role to Admin_ReadSAMLEntities; update in App security if used | ReadOnly | Admin_ReadSAMLEntities |
| 1.18.0 | security | Fixed CVE-2023-25957 preventing configuration mistakes when using POST binding on SAML responses |  |  |
| 1.17.5 | requirement | Library upgrade com.fasterxml.woodstox:woodstox-core from 6.2.4 to 6.5.0 | com.fasterxml.woodstox:woodstox-core |  |
| 1.17.5 | migration-step | Delete all Java libraries from old SAML module in userlib folder before upgrading due to potential conflicts |  |  |
| 1.17.3 | security | Fixed security vulnerability CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N |  |  |
| 1.17.3 | requirement | Library upgrade commons-io from 2.8.0 to 2.11.0 | commons-io |  |
| 1.17.3 | migration-step | Renamed all .Required file names to .RequiredLib in userlib folder |  |  |
| 1.17.3 | migration-step | Delete all Java libraries from old SAML module in userlib folder before upgrading due to potential conflicts |  |  |
| 1.17.2 | security | Fixed CVE-2022-44457 |  |  |
| 1.17.2 | improvement | Added Force Authentication as configurable option in Request Authn context tab |  |  |
| 1.17.2 | breaking | Moved Authentication configuration options from Provisioning tab to Request Authn context tab |  |  |
| 1.17.2 | requirement | Library upgrade org.slf4j:slf4j-api and slf4j-simple to 2.0.3 | org.slf4j:slf4j-api, org.slf4j:slf4j-simple |  |
| 1.17.2 | migration-step | Delete all Java libraries from old SAML module in userlib folder before upgrading due to potential conflicts |  |  |
| 1.17.0 | requirement | Upgraded to latest LTS/MTS Studio Pro v7.23.32 |  |  |
| 1.17.0 | security | Fixed CVE-2022-37011 |  |  |
| 1.17.0 | requirement | Library upgrade org.bouncycastle:bcpkix-jdk15on, bcprov-jdk15on, bcutil-jdk15on to 1.69 | org.bouncycastle:bcpkix-jdk15on, org.bouncycastle:bcprov-jdk15on, org.bouncycastle:bcutil-jdk15on |  |
| 1.17.0 | migration-step | Delete all Java libraries from old SAML module in userlib folder before upgrading due to potential conflicts |  |  |
| 1.16.7 | migration-step | Delete all Java libraries from userlib folder before upgrading due to potential conflicts between old and new versions. | Java libraries |  |
| 1.16.7 | improvement | Upgraded com.fasterxml.woodstox:woodstox-core to 6.2.4 and org.codehaus.woodstox:stax2-api to 4.2.1. | com.fasterxml.woodstox:woodstox-core, org.codehaus.woodstox:stax2-api |  |
| 1.16.6 | breaking | Renamed lognode SAML to SAML_SSO in example microflows to prevent unused lognode. | lognode, SAML | SAML_SSO |
| 1.16.6 | security | Fixed CVE-2022-32285. |  |  |
| 1.16.6 | security | Fixed CVE-2022-32286. |  |  |
| 1.16.5 | migration-step | Delete all Java libraries from userlib folder before upgrading due to potential conflicts. | javax.xml.soap-api-1.4.0.jar |  |
| 1.16.5 | improvement | Removed javax.xml.soap-api-1.4.0.jar and upgraded jakarta.xml.soap-api-1.4.1.jar to 2.0.1. | javax.xml.soap-api, jakarta.xml.soap-api |  |
| 1.16.4 | breaking | Increased character limit in AssertionAttribute Entity's Value attribute. | AssertionAttribute, Value |  |
| 1.16.3 | improvement | Upgraded owasp-java-html-sanitizer to version 20211018.2. | owasp-java-html-sanitizer |  |
| 1.16.3 | migration-step | Delete all Java libraries from userlib folder before upgrading due to potential conflicts. | Java libraries |  |
| 1.16.2 | improvement | Upgraded org.apache.santuario:xmlsec to 2.2.3 and org.apache.velocity:velocity-engine-core to 2.3. | org.apache.santuario:xmlsec, org.apache.velocity:velocity-engine-core |  |
| 1.16.2 | migration-step | Delete all Java libraries from userlib folder before upgrading due to potential conflicts. | Java libraries |  |
| 1.16.0 | improvement | Upgraded bcpkix-jdk15on and bcprov-jdk15on to v1.67 to fix Eclipse environment issues. | bcpkix-jdk15on, bcprov-jdk15on |  |
| 1.16.0 | migration-step | Delete all Java libraries from userlib folder before upgrading; BountyCastle versions may conflict. | Java libraries, BountyCastle |  |
| 1.15.5 | migration-step | Delete all Java libraries from userlib folder; opensaml library conflicts may occur. | Java libraries, opensaml |  |
| 1.15.4 | improvement | Updated commons-lang to 2.6 and jakarta.xml.soap-api to 1.4.1. | commons-lang, jakarta.xml.soap-api |  |
| 1.15.3 | improvement | Updated xercesImpl to 2.12.1-sp1. | xercesImpl |  |
| 1.15.2 | security | Upgraded SAML20 JAR library to fix multiple vulnerabilities. | SAML20 JAR library |  |
| 1.15.2 | improvement | Updated requiredLib folder. | requiredLib folder |  |
| 1.15.2 | improvement | Upgraded Guava library from 27 to 31. | Guava |  |
| 1.13.0 | migration-step | Domain model update requires migration: click migration button on Request Authn Context tab for all IdP settings. | Request Authn Context, IdP Configuration |  |
| 1.12.0 | requirement | Upgraded to Mx7.9; Atlas UI requires at least Mx7.9. | Mendix |  |
| 1.11.0 | improvement | Updated to OpenSAML version 2.6.6. | OpenSAML |  |
| 1.11.0 | improvement | Updated various JAR libraries with known vulnerabilities to more recent versions. | Java libraries |  |
| 1.10.1 | requirement | Upgraded to Mx7.5.1. | Mendix |  |
| 1.10.0 | security | Two security fixes implemented; all customers recommended to update. |  |  |
| 1.9 | requirement | Updated to Mendix 7.0.2. | Mendix |  |

## SAP Blank App <a id="91947"></a>
Starter App, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/91947)

| version | published | min Mendix |
|---|---|---|
| 6.0.0 | 2026-09-02 | 11.12.3 |
| 5.0.1 | 2025-08-18 | 10.21.0 |
| 5.0.0 | 2025-04-29 | 10.21.0 |
| 4.0.0 | 2024-12-12 | 10.12.10 |
| 3.0.1 | 2023-11-23 | 9.24.4 |
| 3.0.0 | 2023-04-10 | 9.24.0 |
| 2.6.2 | 2023-01-03 | 9.12.2 |
| 2.6.1 | 2022-07-08 | 9.12.2 |
| 2.6.0 | 2022-01-13 | 9.6.6 |
| 2.5.1 | 2021-12-16 | 9.2.0 |
| 2.5.0 | 2021-06-28 | 9.2.0 |
| 2.4.1 | 2021-01-28 | 8.15.1 |
| 2.4.0 | 2020-12-09 | 8.15.1 |
| 2.3.1 | 2020-11-11 | 8.9.0 |
| 2.3.0 | 2020-07-16 | 8.9.0 |
| 2.2.1 | 2020-06-29 | 8.9.0 |
| 2.2.0 | 2020-06-03 | 8.9.0 |
| 2.1.0 | 2020-05-15 | 8.9.0 |
| 2.0.2 | 2020-05-04 | 8.0.0 |
| 2.0.1 | 2020-03-17 | 8.0.0 |
| 2.0.0 | 2020-01-03 | 8.0.0 |
| 1.6.0 | 2019-08-27 | 7.23.3 |
| 1.5.0 | 2019-05-09 | 7.23.3 |
| 1.4.3 | 2018-10-04 | 7.16.0 |
| 1.4.2 | 2018-10-03 | 7.16.0 |
| 1.4.1 | 2018-09-26 | 7.16.0 |
| 1.4.0 | 2018-09-20 | 7.16.0 |
| 1.3.0 | 2018-09-18 | 7.18.1 |
| 1.2.0 | 2018-07-18 | 7.5.1 |
| 1.1.0 | 2018-07-13 | 7.5.1 |
| 1.0.1 | 2018-01-15 | 7.5.1 |
| 1.0.0 | 2017-09-22 | 7.5.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 6.0.0 | requirement | Requires Mendix 11.12.3 or higher | Mendix |  |
| 5.0.1 | improvement | Updated SAP connectors to latest | SAP connectors |  |
| 5.0.0 | requirement | Requires Mendix 10.21.0 or higher | Mendix |  |
| 4.0.0 | requirement | Requires Mendix 10.12.10 or higher | Mendix |  |
| 3.0.1 | requirement | Requires Mendix 9.24.4 or higher | Mendix |  |
| 3.0.1 | improvement | Upgraded to Mendix SSO v.4.2.0 | Mendix SSO |  |
| 3.0.1 | improvement | Updated SAP OData Connector and SAP XSUAA Connector | SAP OData Connector, SAP XSUAA Connector |  |
| 3.0.0 | requirement | Requires Mendix 9.24.0 or higher | Mendix |  |
| 3.0.0 | improvement | Upgraded to Atlas 3 | Atlas |  |
| 2.6.2 | improvement | Updated marketplace modules | marketplace modules |  |
| 2.6.2 | improvement | Removed unused jars | jars |  |
| 2.6.1 | requirement | Requires Mendix v9.12.2 or higher | Mendix |  |
| 2.6.0 | requirement | Requires Mendix v9.6.6 or higher | Mendix |  |
| 2.5.1 | security | log4j vulnerability fix | Log4j-core.jar |  |
| 2.5.1 | improvement | Removed unused jars including vulnerable Log4j-core.jar | jars |  |
| 2.5.0 | requirement | Requires Mendix Studio Pro 9.2.0 or higher | Mendix Studio Pro |  |
| 2.5.0 | improvement | Updated SAPODataConnector & SapAuthentication module | SAPODataConnector, SapAuthentication |  |
| 2.4.1 | improvement | Updated MendixSSO modules | MendixSSO modules |  |
| 2.4.1 | improvement | Updated SAPODataConnector modules | SAPODataConnector modules |  |
| 2.4.0 | improvement | Updated SAP Connector modules | SAP Connector modules |  |
| 2.4.0 | requirement | Requires Mendix Studio Pro 8.15.1 or higher | Mendix Studio Pro |  |
| 2.3.1 | improvement | Updated XSUAA module to version 2.1.1 | XSUAA module |  |
| 2.3.0 | improvement | Updated XSUAA module to version 2.1.0 | XSUAA module |  |
| 2.2.1 | improvement | Updated SAP OData Connector to version v5.1.2 | SAP OData Connector |  |
| 2.2.0 | improvement | Updated SAP OData connector version to 5.1.1 | SAP OData connector |  |
| 2.1.0 | improvement | Updated Atlas UI version 2.5.5 and SAP OData Connector v5.1.0 | Atlas UI, SAP OData Connector |  |
| 2.0.1 | improvement | Updated the OData Connector to version 5.0.4 | OData Connector |  |
| 2.0.0 | requirement | Requires Mendix 8 or higher | Mendix |  |
| 1.6.0 | improvement | Update XSUAA and SAP OData connector modules | XSUAA, SAP OData connector |  |
| 1.5.0 | requirement | Requires Mendix version 7.23.3 or higher | Mendix |  |
| 1.4.3 | breaking | turned off security | security |  |
| 1.4.2 | feature | added on startup microflow for SAP XSUAA | SAP XSUAA |  |
| 1.4.1 | feature | Return Xsuaa login | Xsuaa login |  |
| 1.4.0 | feature | Added Odata Connector | Odata Connector |  |
| 1.3.0 | requirement | Requires version 7.17.2 or higher | Mendix |  |
| 1.2.0 | feature | Added OData Connector | OData Connector |  |
| 1.0.1 | improvement | Updated Userlib and cloud security | Userlib, cloud security |  |
| 1.0.0 | feature | atlas UI theme for SAP users | atlas UI theme |  |

## SAP Fiori Web Starter App <a id="116366"></a>
Starter App, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/116366)

| version | published | min Mendix |
|---|---|---|
| 3.0.1 | 2026-02-09 | 10.21.0 |
| 3.0.0 | 2025-05-26 | 10.21.0 |
| 2.0.2 | 2023-11-24 | 9.24.4 |
| 2.0.1 | 2023-10-20 | 9.24.4 |
| 2.0.0 | 2023-04-12 | 9.24.0 |
| 1.3.2 | 2023-01-03 | 9.12.2 |
| 1.3.1 | 2022-07-08 | 9.12.2 |
| 1.3.0 | 2022-01-03 | 9.6.6 |
| 1.2.1 | 2021-12-20 | 9.2.0 |
| 1.2.0 | 2021-06-28 | 9.2.0 |
| 1.1.2 | 2021-12-22 | 8.18.10 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 3.0.1 | improvement | Updated SAP connectors to latest | SAP connectors |  |
| 3.0.0 | requirement | Upgraded to Mx10.21.0 |  |  |
| 3.0.0 | improvement | Updated all marketplace modules |  |  |
| 2.0.2 | improvement | Upgraded to Mendix SSO v4.2.0 | Mendix SSO |  |
| 2.0.1 | improvement | Updated Fiori Web UI package with latest horizon themes | Fiori Web UI package |  |
| 2.0.1 | improvement | Updated SAP OData & XSUAA Connector with latest | SAP OData & XSUAA Connector |  |
| 2.0.1 | requirement | Upgraded to Mendix v9.24.4 |  |  |
| 2.0.0 | breaking | Renamed to SAP Fiori Web Starter App |  |  |
| 2.0.0 | requirement | Updated to Mendix v9.24.0 |  |  |
| 2.0.0 | improvement | Updated SAP UI resources, authentication, OData connector, and application logs modules to latest | SAP UI resources, SAP authentication, SAP OData connector, SAP application logs |  |
| 1.3.2 | improvement | Updated marketplace modules |  |  |
| 1.3.1 | requirement | Upgraded to Mendix v9.12.2 |  |  |
| 1.3.1 | improvement | Upgraded the Fiori UI package to Atlas 3 | Fiori UI package |  |
| 1.3.0 | requirement | Upgraded to Mendix Studio Pro v9.6.6 |  |  |
| 1.3.0 | improvement | Updated SAP Fiori 3 UI Resources module | SAP Fiori 3 UI Resources |  |
| 1.2.1 | security | log4j vulnerability fix | Log4j |  |
| 1.2.0 | requirement | Upgraded to Mendix Studio Pro 9.2.0 |  |  |
| 1.2.0 | improvement | Updated SapAuthentication & SAPODataConnector module | SapAuthentication, SAPODataConnector |  |
| 1.1.2 | security | log4j vulnerability fix | Log4j |  |

## SAP Horizon Native Starter App <a id="214601"></a>
Sample, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/214601)

| version | published | min Mendix |
|---|---|---|
| 2.0.1 | 2025-08-19 | 10.21.0 |
| 2.0.0 | 2025-05-20 | 10.21.0 |
| 1.0.1 | 2023-11-24 | 9.24.4 |
| 1.0.0 | 2023-08-08 | 9.24.3 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.0.1 | improvement | Updated SAP connectors to latest | SAP connectors |  |
| 2.0.0 | requirement | Upgraded to Mx 10.21.0 | Mendix |  |
| 1.0.1 | requirement | Upgraded to Mendix v9.24.4 | Mendix |  |
| 1.0.1 | improvement | Upgraded to Mendix SSO v4.2.0 | Mendix SSO |  |
| 1.0.1 | improvement | Updated Marketplace Modules with the latest |  |  |

## SAP Horizon Native UI Resources <a id="210026"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/210026)

| version | published | min Mendix |
|---|---|---|
| 2.0.0 | 2025-07-08 | 10.21.0 |
| 1.0.1 | 2023-05-15 | 9.24.0 |
| 1.0.0 | 2023-04-25 | 9.24.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.0.0 | requirement | Upgraded to Mendix 10.21.0. Minimum Mendix version is now 10.21.0. |  |  |

## SAP Logging Connector <a id="110219"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/110219)

| version | published | min Mendix |
|---|---|---|
| 3.1.0 | 2025-07-17 | 10.21.0 |
| 3.0.0 | 2025-07-08 | 10.21.0 |
| 2.2.0 | 2025-07-17 | 9.24.33 |
| 2.1.0 | 2025-05-06 | 9.24.33 |
| 2.0.0 | 2023-03-30 | 9.24.0 |
| 1.1.1 | 2022-11-15 | 8.18.10 |
| 1.1.0 | 2020-12-04 | 8.15.1 |
| 1.0.1 | 2019-07-05 | 7.23.3 |
| 1.0.0 | 2019-07-01 | 7.23.3 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 3.1.0 | feature | Updated to support SAP Cloud Logging service |  |  |
| 3.0.0 | requirement | Upgraded to Mendix 10.21 | Mendix |  |
| 2.2.0 | feature | Updated to support SAP Cloud Logging service |  |  |
| 2.1.0 | requirement | Released on Mendix v9.24.33 | Mendix |  |
| 2.0.0 | requirement | Upgraded to Mendix v9.24.0 | Mendix |  |
| 1.1.1 | requirement | Updated to Mendix v8.18.10 | Mendix |  |
| 1.1.0 | requirement | Upgraded to Mendix 8 | Mendix |  |
| 1.0.1 | breaking | Enumeration LogLevels replaced with constant SapLogLevel; RegisterSubscriber LogLevel input parameter now String | LogLevels, SapLogLevel, RegisterSubscriber | SapLogLevel |

## SAP Supply Chain Mobility <a id="118346"></a>
Solution, The Config Team, Partner, [marketplace](https://marketplace.mendix.com/link/component/118346)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2021-09-02 | ? |

## Scadea LMS <a id="223273"></a>
Solution, Scadea, Partner, [marketplace](https://marketplace.mendix.com/link/component/223273)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2024-02-27 | ? |

## Scheduling <a id="208026"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/208026)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2023-03-09 | 9.18.4 |

## SCIM <a id="229630"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/229630)

| version | published | min Mendix |
|---|---|---|
| 4.1.0 | 2026-06-22 | 10.24.0 |
| 4.0.1 | 2026-01-14 | 10.24.0 |
| 4.0.0 | 2025-10-10 | 10.24.0 |
| 3.0.0 | 2025-10-10 | 9.24.2 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 4.1.0 | fix | Fixed SCIM user filtering response and resource creation status handling to improve SCIM compliance. |  |  |
| 4.1.0 | fix | Fixed compatibility issues with UserCommons v2.2.1 and later versions. | UserCommons |  |
| 4.1.0 | requirement | It is recommended to use UserCommons v2.2.1 or higher due to compatibility updates in this release. | UserCommons |  |
| 4.0.0 | requirement | v.4.0.0 version for apps on Mx10.24.0 or higher. |  |  |
| 4.0.0 | removal | Protected SCIM module versions (1.0.0 to 2.0.0) are no longer available in the Marketplace. |  |  |
| 4.0.0 | migration-step | Migration from protected to unprotected versions is not supported and requires manual reconfiguration. |  |  |
| 3.0.0 | requirement | Supported for Mendix 9.24.2 and above. |  |  |
| 3.0.0 | requirement | Dependency Modules are Encryption, Community Commons, UserCommons and Mx Model Reflection. | Encryption, Community Commons, UserCommons, Mx Model Reflection |  |
| 3.0.0 | deprecation | Protected SCIM module versions (1.0.0 to 2.0.0) are now deprecated. |  |  |
| 3.0.0 | migration-step | Migration from protected to unprotected versions is not supported and requires manual reconfiguration. |  |  |

## Screen Shot \| Print Screen \| PDF Widget <a id="119983"></a>
Widget, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/119983)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2022-04-01 | 9.6.9 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.0.0 | known-issue | Front-end PDF generation results may vary due to unforeseen changes in user devices affecting end output. |  |  |
| 1.0.0 | known-issue | Security risk: users can easily change values in browser before printing important documents from front-end. |  |  |

## SEO Sitemaps <a id="116718"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/116718)

| version | published | min Mendix |
|---|---|---|
| 1.1.0 | 2022-06-20 | 9.9.1 |
| 1.0.2 | 2021-03-10 | 8.17.0 |
| 1.0.1 | 2021-01-28 | 8.17.0 |
| 1.0.0 | 2021-01-27 | 8.17.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.1.0 | feature | HTTPRequest entity objects now passed to configured Robots.txt and sitemap.xml microflows when available as input parameter. | Robots.txt microflow, sitemap.xml microflow |  |

## SERVALX <a id="116421"></a>
Solution, PLAIN IT AG, Partner, [marketplace](https://marketplace.mendix.com/link/component/116421)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2021-09-15 | 9.4.0 |

## Shopfloor Operational Excellence Platform <a id="213394"></a>
Solution, Factorise-software, Partner, [marketplace](https://marketplace.mendix.com/link/component/213394)

| version | published | min Mendix |
|---|---|---|
| 2.0.0 | 2023-12-11 | ? |
| 1.0.0 | 2023-08-22 | ? |

## Show More/Less <a id="114739"></a>
Widget, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/114739)

| version | published | min Mendix |
|---|---|---|
| 1.1.0 | 2020-09-25 | 8.9.0 |
| 1.0.0 | 2020-07-20 | 8.9.0 |

## Siemens SCD Connector <a id="120106"></a>
Module, Siemens, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/120106)

| version | published | min Mendix |
|---|---|---|
| 2.0.0 | 2022-05-13 | 8.12.5 |
| 1.0.0 | 2022-04-11 | 8.12.5 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.0.0 | removal | Removed custom Java Actions. | custom Java Actions |  |
| 2.0.0 | improvement | Improved encryption based on latest Encryption marketplace module from Mendix. | Encryption |  |

## Siemens UI Module <a id="239207"></a>
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

## Siemens UI Resources (Mendix 8) <a id="118671"></a>
Module, Siemens, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/118671)

| version | published | min Mendix |
|---|---|---|
| 1.0.6 | 2022-05-04 | 8.18.15 |
| 1.0.5 | 2022-03-25 | 8.18.15 |
| 1.0.4 | 2022-01-26 | 8.18.15 |
| 1.0.3 | 2022-01-21 | 8.18.15 |
| 1.0.1 | 2021-10-15 | 8.18.10 |
| 1.0.0 | 2021-10-11 | 8.18.10 |

## Siemens UI Resources (Mendix 9 & 10) <a id="118672"></a>
Module, Siemens, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/118672)

| version | published | min Mendix |
|---|---|---|
| 2.2.4 | 2025-05-15 | 9.24.31 |
| 2.2.3 | 2025-01-10 | 9.24.31 |
| 2.2.2 | 2025-01-02 | 9.24.31 |
| 2.2.1 | 2024-09-17 | 9.24.14 |
| 2.2.0 | 2024-09-04 | 9.24.14 |
| 2.1.2 | 2024-08-22 | 9.24.14 |
| 2.1.1 | 2024-05-28 | 9.24.14 |
| 2.0.9 | 2024-05-09 | 9.24.14 |
| 2.0.8 | 2024-05-06 | 9.24.14 |
| 2.0.7 | 2024-04-24 | 9.24.12 |
| 2.0.6 | 2024-02-16 | 9.24.12 |
| 2.0.5 | 2024-02-02 | 9.24.12 |
| 2.0.4 | 2024-01-04 | 9.24.12 |
| 2.0.3 | 2023-08-01 | 9.24.2 |
| 2.0.2 | 2023-06-27 | 9.24.2 |
| 2.0.1 | 2023-05-31 | 9.24.2 |
| 2.0.0 | 2023-05-23 | 9.18.7 |
| 1.0.6 | 2022-05-04 | 9.6.6 |
| 1.0.5 | 2022-03-25 | 9.6.6 |
| 1.0.4 | 2022-01-26 | 9.6.6 |
| 1.0.3 | 2022-01-21 | 9.6.6 |
| 1.0.1 | 2021-10-15 | 9.4.0 |
| 1.0.0 | 2021-10-11 | 9.4.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.2.0 | improvement | Siemens Sans Pro font updated to version 7. | Siemens Sans Pro |  |
| 2.0.1 | improvement | Datawidgets Module update. | Datawidgets Module |  |
| 2.0.0 | improvement | Atlas modules updated. | Atlas modules |  |
| 2.0.0 | improvement | Mendix version upgraded. |  |  |
| 2.0.0 | improvement | Data widgets module updated and fixed. | Data widgets module |  |

## Signature <a id="107984"></a>
Widget, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/107984)

| version | published | min Mendix |
|---|---|---|
| 2.1.0 | 2026-08-31 | 11.8.0 |
| 2.0.1 | 2026-07-22 | 11.8.0 |
| 2.0.0 | 2026-06-24 | 11.8.0 |
| 1.0.8 | 2026-03-05 | 8.0.0 |
| 1.0.7 | 2025-01-15 | 8.0.0 |
| 1.0.4 | 2020-02-17 | 7.13.1 |
| 1.0.3 | 2019-10-01 | 7.13.1 |
| 1.0.2 | 2019-01-02 | 7.13.1 |
| 1.0.1 | 2018-12-19 | 7.13.1 |
| 1.0.0 | 2018-11-20 | 7.13.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.0.0 | breaking | Complete rewrite using Pluggable Widget API. Migrated from Custom Widget (v1.x) to Pluggable Widget architecture. | Signature |  |
| 2.0.0 | requirement | Minimum Mendix version increased to 11.8.0 (previously 7.13.1). |  |  |
| 2.0.0 | migration-step | No backward compatibility. Existing v1.x implementations must be reconfigured. | Signature |  |
| 2.0.0 | breaking | Widget ID changed from com.mendix.widget.custom.signature.Signature to com.mendix.widget.web.signature.Signature. | com.mendix.widget.custom.signature.Signature | com.mendix.widget.web.signature.Signature |
| 2.0.0 | migration-step | Widget MPK renamed from Signature.mpk to com.mendix.widget.web.Signature.mpk. Remove old Signature.mpk manually after migration. | Signature.mpk | com.mendix.widget.web.Signature.mpk |
| 2.0.0 | breaking | Widget category changed from Add-ons to Input elements. | Signature |  |

## SignIn microflow for Mx7 / Mx8 <a id="66443"></a>
Module, Emixa, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/66443)

| version | published | min Mendix |
|---|---|---|
| 2.0.0 | 2019-11-08 | 8.4.0 |
| 1.0.0 | 2017-07-03 | 7.0.2 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.0.0 | requirement | Updated for Mendix 8, minimum version 8.4.0 required | Mendix |  |

## Simple Checkbox Set Selector <a id="2349"></a>
Widget, Mendix, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/2349)

| version | published | min Mendix |
|---|---|---|
| 1.4.0 | 2024-03-26 | 7.23.0 |
| 1.3.1 | 2023-12-12 | 7.23.0 |
| 1.3.0 | 2022-01-27 | 7.23.0 |
| 1.2.0 | 2018-06-04 | 7.23.0 |

## Simple CSV Exporter <a id="1573"></a>
Module, Emixa, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/1573)

| version | published | min Mendix |
|---|---|---|
| 4.1.0 | 2025-07-02 | 10.6.24 |
| 3.2.0 | 2022-05-16 | 9.6.11 |
| 2.1.1 | 2021-03-26 | 8.4.4 |
| 2.0.0 | 2020-12-17 | 8.4.4 |
| 1.4.1 | 2021-03-18 | 8.4.4 |
| 1.4.0 | 2017-07-19 | 7.2.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 4.1.0 | fix | Fix for Java deprecation caused by upgrade to Mendix 10. |  |  |
| 3.2.0 | requirement | Mendix 9 upgrade. | Mendix |  |
| 2.1.1 | requirement | Upgrade necessary if updating Reporting4Mendix module version 2.5.1. | Reporting4Mendix |  |
| 2.1.1 | requirement | Community Commons is required for some String operations. | Community Commons |  |
| 2.0.0 | requirement | Upgrade Mendix 8. | Mendix |  |
| 1.4.1 | requirement | Upgrade necessary if updating Reporting4Mendix module version 2.5.1. | Reporting4Mendix |  |
| 1.4.0 | requirement | Mendix 7.2.0 release. | Mendix |  |

## Simple Export to Excel <a id="218196"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/218196)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2023-10-30 | 10.3.1 |

## SimpleRulesEngine <a id="217749"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/217749)

| version | published | min Mendix |
|---|---|---|
| 1.0.1 | 2023-10-23 | 9.18.4 |
| 1.0.0 | 2023-10-19 | 9.18.4 |

## Slider <a id="48786"></a>
Widget, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/48786)

| version | published | min Mendix |
|---|---|---|
| 3.0.4 | 2026-07-22 | 9.6.0 |
| 3.0.3 | 2026-06-17 | 9.6.0 |
| 3.0.2 | 2026-02-20 | 9.6.0 |
| 3.0.1 | 2026-02-11 | 9.6.0 |
| 3.0.0 | 2026-01-07 | 9.6.0 |
| 2.1.4 | 2024-08-28 | 9.6.0 |
| 2.1.3 | 2024-07-15 | 9.6.0 |
| 2.1.2 | 2024-06-25 | 9.6.0 |
| 2.1.1 | 2023-09-27 | 9.6.0 |
| 2.1.0 | 2023-06-06 | 9.6.0 |
| 2.0.1 | 2022-05-04 | 9.6.0 |
| 2.0.0 | 2021-12-23 | 9.6.0 |
| 1.3.2 | 2020-05-01 | 7.13.1 |
| 1.3.1 | 2018-12-14 | 7.13.1 |
| 1.3.0 | 2018-10-12 | 7.13.1 |
| 1.2.1 | 2018-10-02 | 7.13.1 |
| 1.2.0 | 2018-05-11 | 7.13.1 |
| 1.1.4 | 2018-04-09 | 7.3.0 |
| 1.1.3 | 2018-03-01 | 7.3.0 |
| 1.1.2 | 2017-08-02 | 7.3.0 |
| 1.1.1 | 2017-07-06 | 7.1.0 |
| 1.1 | 2017-06-12 | 7.1.0 |
| 1.0 | 2017-04-17 | 7.1.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 3.0.0 | breaking | Updated rc-slider library to @rc-component/slider major version upgrade that might break current custom styling. | rc-slider, @rc-component/slider | @rc-component/slider |
| 2.0.0 | breaking | Converted into a pluggable widget. | widget architecture |  |
| 1.3.2 | fix | Removed usage of deprecated mx client api endpoint. | mx client api endpoint |  |
| 1.1.2 | requirement | Made React 16 compatible. | React |  |

## Snackbar (Native) <a id="116404"></a>
Service, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/116404)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2021-03-01 | 8.16.0 |

## Snowflake Conversational UI Bridge <a id="202837"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/202837)

| version | published | min Mendix |
|---|---|---|
| 1.1.1 | 2026-09-07 | 10.24.13 |
| 1.1.0 | 2026-08-19 | 10.24.13 |
| 1.0.0 | 2026-06-11 | 10.24.13 |

## Snowflake JDBC Connector <a id="225828"></a>
Service, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/225828)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2024-05-06 | 10.10.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.0.0 | requirement | Minimum Mendix version requirement: 10.10.0 | Mendix |  |

## Snowflake LLM Connector <a id="202233"></a>
Service, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/202233)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2026-05-28 | 10.24.13 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.0.0 | requirement | Minimum Mendix version is 10.24.13 | Mendix |  |

## Snowflake Mendix Data Loader <a id="226564"></a>
Solution, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/226564)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2024-05-23 | ? |

## SnowflakeAIDataConnector <a id="225717"></a>
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

## Socotra Connector (specific) <a id="207482"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/207482)

| version | published | min Mendix |
|---|---|---|
| 1.0.1 | 2023-03-14 | 9.18.4 |
| 1.0.0 | 2023-02-24 | 9.18.3 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.0.1 | security | Replaced vulnerable jackson.core:jackson.databind-2.14.0-rc1 dependency | jackson.core:jackson.databind |  |

## Sphera SCRM Connector <a id="216898"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/216898)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2023-10-10 | 9.18.2 |

## Split Screen <a id="258022"></a>
Widget, GSK, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/258022)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2026-03-17 | 9.6.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.0.0 | requirement | Minimum Mendix version requirement: 9.6.0 | Mendix |  |

## Spotlight Search For Mendix <a id="2398"></a>
Module, Emixa, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/2398)

| version | published | min Mendix |
|---|---|---|
| 5.1.0 | 2022-08-10 | 8.18.18 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 5.1.0 | requirement | Minimum Mendix version is 8.18.18. Java libraries upgraded for security bugfixes. | Java libraries |  |
| 5.1.0 | security | Java libraries upgraded inline with Community Commons for security bugfixes. | Java libraries |  |

## Stable Diffusion AI (Replicate) <a id="207143"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/207143)

| version | published | min Mendix |
|---|---|---|
| 1.1.0 | 2026-08-13 | 10.21.0 |
| 1.0.0 | 2023-02-14 | 9.18.2 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.1.0 | requirement | Updated to Mendix 10.21.0; minimum required version is 10.21.0 | Mendix |  |

## Sticky Notes <a id="237035"></a>
Module, Comotion, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/237035)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2025-02-11 | 10.6.6 |

## String2MD5 <a id="212660"></a>
Module, Mendixmasters, Community, [marketplace](https://marketplace.mendix.com/link/component/212660)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2023-06-30 | 9.0.5 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.0.0 | requirement | Requires Mendix version 9.0.5 or above. |  |  |

## StringUtils <a id="66804"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/66804)

| version | published | min Mendix |
|---|---|---|
| 3.0.0 | 2026-09-21 | 11.6.7 |
| 2.0.0 | 2021-04-13 | 8.12.5 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 3.0.0 | requirement | Minimum Mendix version requirement raised to 11.6.7 |  |  |
| 2.0.0 | requirement | Minimum Mendix version requirement raised to 8.12.5 |  |  |
| 2.0.0 | improvement | Upgraded used libraries |  |  |
| 2.0.0 | improvement | Upgraded/replicated methods from Community Commons module |  |  |

## Stripe Checkout Connector <a id="207076"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/207076)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2023-02-14 | 9.18.2 |

## StudioPro Python Extension <a id="244625"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/244625)

| version | published | min Mendix |
|---|---|---|
| 2.3.0 | 2025-09-24 | 10.24.4 |
| 2.2.0 | 2025-09-12 | 10.24.4 |
| 2.1.0 | 2025-09-03 | 10.24.4 |
| 2.0.0 | 2025-09-02 | 10.24.4 |
| 1.0.0 | 2025-07-30 | 10.24.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.1.0 | fix | Fixed Python detection logic and added logs to Studio Pro. |  |  |

## Supplyframe Connector  <a id="222195"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/222195)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2024-02-02 | 9.24.10 |

## Support Assistant Starter App <a id="231035"></a>
Solution, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/231035)

| version | published | min Mendix |
|---|---|---|
| 3.0.0 | 2025-04-10 | 10.21.0 |
| 2.1.0 | 2025-02-28 | 10.12.4 |
| 2.0.0 | 2025-01-13 | 10.12.4 |
| 1.2.0 | 2024-10-17 | 10.12.4 |
| 1.1.0 | 2024-09-25 | 10.12.4 |
| 1.0.0 | 2024-09-09 | 10.12.4 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.1.0 | improvement | Starter App updated to support React Client. Multiple modules updated: Amazon Bedrock Connector v6.1.0, Atlas Core v3.16.4, AWS Authentication v3.2.1, GenAI For Mendix v2.2.0, OpenAI Connector v4.2.0, PgVectorKnowledgeBase v2.4.0. | Amazon Bedrock Connector, Atlas Core, AWS Authentication, GenAI For Mendix, OpenAI Connector, PgVectorKnowledgeBase |  |
| 2.0.0 | feature | Mendix Cloud added as GenAI provider. Support assistant can run against LLMs and Knowledge Bases deployed in Mendix Cloud. | Mendix Cloud, GenAI provider |  |
| 2.0.0 | breaking | Assistant infrastructure changed to be compatible with Deployed Model entity of GenAI Commons, aligning admin model selection for OpenAI, Azure OpenAI, and AmazonBedrock. | assistant infrastructure, Deployed Model entity, GenAI Commons |  |
| 2.0.0 | improvement | App contains latest connector module versions and simplified toolbox of GenAI Commons: Amazon Bedrock Connector 6.0.0, AWS Authentication 3.2.0, ConversationalUI 2.0.0, GenAI Commons 2.0.0, MxGenAIConnector 2.0.0, OpenAI Connector 4.0.0, PgVector Knowledge Base 2.3.0. | Amazon Bedrock Connector, AWS Authentication Module, ConversationalUI, GenAI Commons, MxGenAIConnector, OpenAI Connector, PgVector Knowledge Base |  |
| 1.2.0 | improvement | Updated modules: Amazon Bedrock Connector 5.3.0, AWS Authentication Module 3.2.0, Community Commons 10.0.7, ConversationalUI 1.5.1, Encryption 10.0.3, GenAI Commons 1.5.0, OpenAI Connector 3.4.1, PgVector Knowledge Base 2.2.0. | Amazon Bedrock Connector, AWS Authentication Module, Community Commons, ConversationalUI, Encryption, GenAI Commons, OpenAI Connector, PgVector Knowledge Base |  |
| 1.1.0 | improvement | Updated marketplace modules: AWS Authentication Connector 3.1.3, ConversationalUI 1.4.0, Data widgets 2.23.0, Feedback Module 3.0.0, OpenAI connector 3.3.0, GenAICommons 1.3.0. | AWS Authentication Connector, ConversationalUI, Data widgets, Feedback Module, OpenAI connector, GenAICommons |  |

## Switch <a id="50324"></a>
Widget, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/50324)

| version | published | min Mendix |
|---|---|---|
| 4.3.0 | 2025-10-22 | 9.24.0 |
| 4.2.2 | 2024-08-28 | 9.6.0 |
| 4.2.1 | 2023-09-27 | 9.6.0 |
| 4.2.0 | 2023-06-06 | 9.6.0 |
| 4.1.0 | 2021-12-23 | 9.6.0 |
| 4.0.0 | 2021-09-28 | 9.6.0 |
| 3.0.0 | 2021-04-23 | 9.0.5 |
| 2.1.3 | 2020-05-01 | 7.13.1 |
| 2.1.2 | 2020-03-26 | 7.13.1 |
| 2.1.1 | 2018-07-20 | 7.13.1 |
| 2.1.0 | 2018-05-23 | 7.13.1 |
| 2.0.3 | 2018-03-01 | 7.4.0 |
| 2.0.2 | 2018-01-26 | 7.4.0 |
| 2.0.1 | 2017-09-13 | 7.4.0 |
| 2.0.0 | 2017-08-31 | 7.4.0 |
| 1.2.2 | 2017-08-03 | 7.4.0 |
| 1.2.1 | 2017-07-11 | 7.3.0 |
| 1.2 | 2017-06-12 | 7.2.0 |
| 1.1.1 | 2017-05-30 | 7.2.0 |
| 1.1 | 2017-05-13 | 7.2.0 |
| 1.0 | 2017-04-21 | 7.1.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 4.3.0 | breaking | Clicking the label now toggles the switch, improving accessibility and input handling. | label, input tag |  |
| 4.3.0 | requirement | Hidden input tag added to widget HTML DOM. Update to atlas-core 3.19+ or 4.3.0+ for proper styling. | atlas-core |  |
| 3.0.0 | breaking | Changed from small to div element for improved semantics. | HTML semantics |  |
| 3.0.0 | breaking | Converted Style and Device style properties to design-properties. | Style, Device style |  |
| 3.0.0 | breaking | Label and Editability properties converted to system properties, moved to common tab. | Label, Editability |  |
| 3.0.0 | removal | Removed input element. | input element |  |
| 3.0.0 | removal | Removed info and inverse Style property options. | Style |  |
| 3.0.0 | removal | Removed label width property. | label width |  |
| 2.0.0 | breaking | Made label of Switch translatable. Current label caption values will be lost and must be reset. | label |  |

## T-Synch Email <a id="203633"></a>
Module, Blackbelt Technology, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/203633)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2023-04-07 | 8.18.22 |

## T-Synch ExcelExport <a id="204454"></a>
Module, Blackbelt Technology, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/204454)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2023-04-10 | 8.18.22 |

## Tab Swipe <a id="78620"></a>
Widget, Mendix, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/78620)

| version | published | min Mendix |
|---|---|---|
| 1.0.2 | 2018-10-03 | 7.0.2 |

## TabPageSelector <a id="204732"></a>
Widget, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/204732)

| version | published | min Mendix |
|---|---|---|
| 1.1.0 | 2023-10-26 | 8.18.19 |
| 1.0.1 | 2023-01-13 | 8.18.19 |
| 1.0.0 | 2022-11-22 | 8.18.19 |

## TabSwitcher <a id="2964"></a>
Widget, Valcon, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/2964)

| version | published | min Mendix |
|---|---|---|
| 1.4.2 | 2021-09-28 | 8.11.1 |
| 1.4.0 | 2020-08-24 | 8.11.1 |
| 1.3.0 | 2019-07-09 | 7.21.0 |
| 1.2.0 | 2019-01-31 | 7.21.0 |
| 1.1.1 | 2019-01-12 | 7.21.0 |
| 1.1.0 | 2017-10-12 | 7.5.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.4.0 | fix | Fixed reloading page not maintaining attribute updated when 'Keep Tab Attribute Updated' is selected | Keep Tab Attribute Updated |  |
| 1.2.0 | requirement | CSS Class of Tab Container is now required in widget configuration | Tab Container CSS Class |  |
| 1.1.0 | requirement | Upgraded to Mendix 7 compatibility | Mendix |  |

## Task Queue Helpers <a id="117272"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/117272)

| version | published | min Mendix |
|---|---|---|
| 3.1.0 | 2025-11-17 | 10.24.0 |
| 3.0.0 | 2025-04-08 | 10.21.0 |
| 2.0.2 | 2025-04-10 | 9.18.0 |
| 2.0.1 | 2025-02-10 | 9.18.0 |
| 2.0.0 | 2023-04-21 | 9.18.0 |
| 1.1.0 | 2022-01-13 | 9.6.0 |
| 1.0.0 | 2021-04-14 | 9.0.5 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 3.1.0 | requirement | Module upgraded to require Mendix 10.24.0 minimum. |  |  |
| 3.1.0 | improvement | Upgraded widgets to latest versions. |  |  |
| 3.0.0 | requirement | Upgraded Mx Model Reflection module to Mendix version 10.21.0. | Mx Model Reflection |  |
| 2.0.1 | improvement | Updated OQL queries to be compatible with both OQL v1 and v2. |  |  |
| 2.0.0 | requirement | Updated module to Studio Pro 9.18 for use in Studio Pro 10. |  |  |
| 2.0.0 | improvement | Updated Chart widget to version 4.0.4. | Chart |  |
| 1.1.0 | breaking | Disabled scheduled cleanup by default. |  |  |

## Tasks & Planning <a id="108938"></a>
Starter App, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/108938)

| version | published | min Mendix |
|---|---|---|
| 11.21.0 | 2026-10-05 | 11.15.0 |
| 11.20.0 | 2026-08-26 | 11.14.0 |
| 11.19.0 | 2026-08-07 | 11.13.0 |
| 11.18.0 | 2026-07-28 | 11.12.2 |
| 11.17.0 | 2026-07-16 | 11.12.1 |
| 11.16.0 | 2026-07-01 | 11.12.0 |
| 11.15.0 | 2026-06-01 | 11.11.0 |
| 11.14.0 | 2026-04-29 | 11.10.0 |
| 11.13.1 | 2026-04-17 | 11.9.1 |
| 11.13.0 | 2026-04-17 | 11.9.1 |
| 11.12.0 | 2026-04-07 | 11.9.0 |
| 11.11.0 | 2026-03-02 | 11.8.0 |
| 11.10.1 | 2026-02-11 | 11.7.0 |
| 11.10.0 | 2026-01-30 | 11.7.0 |
| 11.9.0 | 2026-01-29 | 11.6.3 |
| 11.8.0 | 2026-01-12 | 11.6.2 |
| 11.7.0 | 2026-01-07 | 11.6.1 |
| 11.6.0 | 2025-12-23 | 11.6.0 |
| 11.5.0 | 2025-11-25 | 11.5.0 |
| 11.4.0 | 2025-11-05 | 11.4.0 |
| 11.1.0 | 2025-07-31 | 11.1.0 |
| 11.0.0 | 2025-07-17 | 11.0.0 |
| 10.35.0 | 2025-07-07 | 10.24.0 |
| 10.34.0 | 2025-05-28 | 10.23.0 |
| 10.32.0 | 2025-04-25 | 10.21.0 |
| 10.31.0 | 2025-02-04 | 10.18.2 |
| 10.30.0 | 2025-01-28 | 10.19.0 |
| 10.29.0 | 2025-01-10 | 10.18.1 |
| 10.28.0 | 2024-12-18 | 10.18.0 |
| 10.27.0 | 2024-11-27 | 10.17.0 |
| 10.26.0 | 2024-11-11 | 10.16.1 |
| 10.25.0 | 2024-10-30 | 10.16.0 |
| 10.24.0 | 2024-09-24 | 10.15.0 |
| 10.23.0 | 2024-08-27 | 10.14.0 |
| 10.22.0 | 2024-08-07 | 10.13.1 |
| 10.21.0 | 2024-07-30 | 10.13.0 |
| 10.20.0 | 2024-07-05 | 10.12.1 |
| 10.19.0 | 2024-06-25 | 10.12.0 |
| 10.18.0 | 2024-05-31 | 10.11.0 |
| 10.17.0 | 2024-03-26 | 10.9.0 |
| … 24 older versions | | |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 11.21.0 | requirement | Minimum Mendix version raised to 11.15.0 |  |  |
| 11.21.0 | removal | MxSSO removed | MxSSO |  |
| 11.20.0 | requirement | Upgraded to 11.14.0 |  |  |
| 11.19.0 | requirement | Upgraded to 11.13.0 |  |  |
| 11.18.0 | requirement | Upgraded to Mx 11.12.2 |  |  |
| 11.17.0 | requirement | Upgraded to Mendix 11.12.1 |  |  |
| 11.16.0 | requirement | Upgraded to Mx 11.12.0 |  |  |
| 11.15.0 | requirement | Upgraded to 11.11.0 |  |  |
| 11.14.0 | requirement | Upgraded to Mx 11.10.0 |  |  |
| 11.13.0 | requirement | Upgraded to version 11.9.1 |  |  |
| 11.12.0 | requirement | Upgraded to version 11.9.0 |  |  |
| 11.11.0 | requirement | Upgraded to 11.8.0 |  |  |
| 11.10.0 | requirement | Upgraded to version 11.7.0 |  |  |
| 11.9.0 | requirement | Upgraded to version 11.6.3 |  |  |
| 11.8.0 | requirement | Upgraded to version 11.6.2 |  |  |
| 11.7.0 | requirement | Upgraded to version 11.6.1 |  |  |
| 11.6.0 | requirement | Upgraded to version 11.6.0 |  |  |
| 11.5.0 | requirement | Upgraded to version 11.5.0 |  |  |
| 11.4.0 | requirement | Upgrade to version 11.4.0 |  |  |
| 11.1.0 | requirement | Upgraded to version 11.1.0 |  |  |
| 11.0.0 | requirement | Upgraded to 11.0.0 |  |  |
| 11.0.0 | requirement | Upgraded MendixSSO to 10.4.0 | MendixSSO |  |
| 10.35.0 | requirement | Upgraded to 10.24.0 |  |  |
| 10.34.0 | requirement | Upgraded to version 10.23.0 |  |  |
| 10.32.0 | requirement | Upgraded to Mx 10.21.0 |  |  |
| 10.31.0 | requirement | Upgraded to version 10.18.2 |  |  |
| 10.30.0 | requirement | Upgraded to version 10.19.0 |  |  |
| 10.29.0 | requirement | Upgraded to version 10.18.1 |  |  |
| 10.28.0 | requirement | Upgraded to version 10.18.0 |  |  |
| 10.27.0 | requirement | Upgraded to version 10.17.0 |  |  |
| 10.26.0 | requirement | Upgraded to version 10.16.1 |  |  |
| 10.25.0 | requirement | Upgraded to version 10.16.0 |  |  |
| 10.24.0 | requirement | Upgraded to version 10.15.0 |  |  |
| 10.23.0 | requirement | Upgraded to version 10.14.0 |  |  |
| 10.22.0 | requirement | Upgraded to version 10.13.1 |  |  |
| 10.21.0 | requirement | Upgraded to 10.13.0 |  |  |
| 10.20.0 | requirement | Upgraded to version 10.12.1 |  |  |
| 10.19.0 | requirement | Upgraded to version 10.12.0 |  |  |
| 10.18.0 | requirement | Upgraded to 10.11.0 |  |  |
| 10.17.0 | requirement | Upgraded to 10.9.0 |  |  |
| 10.16.0 | requirement | Upgraded to 10.8.1 |  |  |
| 10.16.0 | improvement | Updated all modules to the latest version |  |  |
| 10.15.0 | requirement | Upgraded to 10.8.0 |  |  |
| 10.14.0 | requirement | Upgraded to 10.7.0 |  |  |
| 10.13.0 | requirement | Upgraded to version 10.6.2 |  |  |
| 10.12.0 | requirement | Upgraded to version 10.6.1 |  |  |
| 10.11.0 | requirement | Upgraded to version 10.6.0 |  |  |
| 10.10.0 | improvement | Upgraded the modules and widgets |  |  |
| 10.8.0 | requirement | Upgraded to version 10.4.1 |  |  |
| 10.6.0 | requirement | Upgraded to version 10.4.0 |  |  |
| 10.5.0 | requirement | Upgraded to version 10.3.1 |  |  |
| 10.4.0 | requirement | Upgraded to version 10.3.0 |  |  |
| 10.3.0 | requirement | Upgraded to version 10.2.0 |  |  |
| 10.2.0 | requirement | Upgraded to version 10.1.1 |  |  |
| 10.1.0 | requirement | Upgraded to version 10.1.0 |  |  |
| 10.0.0 | requirement | Updated template to Mendix 10 |  |  |
| 9.15.0 | requirement | Upgraded to version 9.24.3 |  |  |
| 9.14.0 | requirement | Upgraded to version 9.24.2 |  |  |
| 9.13.0 | requirement | Upgraded to version 9.24.1 |  |  |
| 9.12.0 | requirement | Upgraded to version 9.24.0 |  |  |
| 9.10.0 | requirement | Upgraded to version 9.20.0 |  |  |
| 9.9.0 | requirement | Upgraded to version 9.19.0 |  |  |
| 9.8.0 | requirement | Upgraded to 9.18.1 |  |  |
| 9.2.4 | security | Updated security |  |  |
| 8.1.0 | fix | Fixed the MendixSSO module | MendixSSO |  |

## Teamcenter BOM Component <a id="259697"></a>
Module, Siemens, Siemens, [marketplace](https://marketplace.mendix.com/link/component/259697)

| version | published | min Mendix |
|---|---|---|
| 2512.1.0 | 2026-08-19 | 10.24.12 |
| 2512.0.0 | 2026-04-09 | 10.24.12 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2512.1.0 | requirement | Requires minimum Teamcenter 2512 version. | Teamcenter BOM Component |  |
| 2512.1.0 | requirement | Requires Mendix version 10.24.12 or higher. | Teamcenter BOM Component |  |
| 2512.1.0 | known-issue | Not yet supported for Mendix 11. | Teamcenter BOM Component |  |
| 2512.1.0 | fix | Resolved issue where apps with Teamcenter BOM Component fail while creating deployment packages for cloud. | Teamcenter BOM Component |  |
| 2512.1.0 | improvement | Teamcenter BOM Component now supported with RsPack Appbundler for cloud deployment. | Teamcenter BOM Component, RsPack Appbundler |  |
| 2512.1.0 | removal | Rollup Appbundler will no longer be supported for Teamcenter BOM Component deployment. | Rollup Appbundler | RsPack Appbundler |
| 2512.0.0 | requirement | Requires minimum Teamcenter 2512 version. | Teamcenter BOM Component |  |
| 2512.0.0 | known-issue | Component fails to load in apps built in Mendix 11. | Teamcenter BOM Component |  |
| 2512.0.0 | known-issue | Apps with BOM component fail while creating deployment packages for cloud. | Teamcenter BOM Component |  |

## Teamcenter Connector <a id="111627"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/111627)

| version | published | min Mendix |
|---|---|---|
| 2606.0.1 | 2026-09-23 | 11.12.1 |
| 2606.0.0 | 2026-07-31 | 11.12.1 |
| 2512.1.2 | 2026-09-11 | 10.24.8 |
| 2512.1.1 | 2026-05-22 | 10.24.8 |
| 2512.1.0 | 2026-03-30 | 10.24.8 |
| 2512.0.1 | 2026-02-23 | 10.24.8 |
| 2512.0.0 | 2026-02-16 | 10.24.8 |
| 2506.0.1 | 2026-05-22 | 10.24.8 |
| 2506.0.0 | 2025-08-21 | 10.20.0 |
| 2412.225.0 | 2025-05-13 | 10.4.0 |
| 2412.3.0 | 2026-05-22 | 10.24.8 |
| 2412.0.0 | 2025-02-11 | 10.4.0 |
| 2406.3.1 | 2026-05-22 | 10.24.8 |
| 2406.3.0 | 2024-09-13 | 10.0.0 |
| 3.7.0 | 2026-04-28 | 9.24.41 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2606.0.1 | improvement | Upgraded to latest version of Studio Pro Design System for better alignment and accessibility. | Studio Pro Design System |  |
| 2606.0.1 | fix | Fixed BOM component unable to retrieve Teamcenter information due to incorrect session cookie lookup on Mendix Cloud. | Connector, BOM component |  |
| 2606.0.1 | fix | Fixed regression where Operation Mapping could no longer be supplied as JSON document. | Connector, Operation Mapping |  |
| 2606.0.1 | security | Updated Java dependencies to resolve vulnerabilities. | Java dependencies |  |
| 2606.0.1 | fix | Fixed bug where integration linked to excluded microflow could not be edited or regenerated. | Service document |  |
| 2606.0.1 | breaking | ConfigurationName parameter of RULE_TeamcenterConfiguration_IsLoggedIn is required again (was optional in 2606.0.0). | RULE_TeamcenterConfiguration_IsLoggedIn |  |
| 2606.0.0 | requirement | Mendix Studio Pro 11.12.1 or higher required. |  |  |
| 2606.0.0 | breaking | Removed Create and Delete rights from all entities. Administrator role no longer has direct entity-level access except Teamcenter Configuration. | Create rights, Delete rights |  |
| 2606.0.0 | improvement | Improved SSO configuration error logging with field names and messages matching Teamcenter Extension behavior. | SSO configuration error logging |  |
| 2606.0.0 | improvement | Rebuilt Teamcenter Extension using Mendix Web Extensibility Framework (TypeScript) replacing discontinued C# framework for future compatibility. | Teamcenter Extension |  |
| 2606.0.0 | fix | Fixed blocking (locked) state when calling multiple Teamcenter Java actions within one transaction preventing user operations. | Teamcenter Java actions, transaction |  |
| 2606.0.0 | fix | Fixed error when Teamcenter response contained array mixing empty strings and valid Model Object UIDs. (Ticket 269666) | Teamcenter response |  |
| 2606.0.0 | breaking | Updated entity attributes to match Teamcenter defaults: BOMLine bl_rev_object_name (128), bl_quantity (24), bl_plmxml_abs_xform (240); ReviseItemRevision.item_revision_id (32); User.userid (32); WorkspaceObject.checked_out (32). | BOMLine, BOMLine.bl_rev_object_name, BOMLine.bl_quantity, BOMLine.bl_plmxml_abs_xform, ReviseItemRevision.item_revision_id, User.userid, WorkspaceObject.checked_out |  |
| 2606.0.0 | fix | Fixed misleading error "Entity does not exist: ListOfValues" from GetAttachedLOV and GetAttachedPropDescs2. | GetAttachedLOV, GetAttachedPropDescs2 |  |
| 2606.0.0 | breaking | Renamed FileType/File Type to NamedReference/Named Reference for consistency with Teamcenter naming conventions. | FileType, File Type | NamedReference |
| 2606.0.0 | deprecation | Deprecated DownloadFile microflow; use DownloadFile/DownloadImage Java actions instead. | DownloadFile | DownloadFile |
| 2606.0.0 | deprecation | Deprecated ExecuteLogin microflow; use Login microflow instead. | ExecuteLogin | Login |
| 2606.0.0 | deprecation | Deprecated ExecuteLogout microflow; use Logout microflow instead. | ExecuteLogout | Logout |
| 2606.0.0 | deprecation | Deprecated AreMultipleTcConfigActive microflow; see annotation for guidance. | AreMultipleTcConfigActive |  |
| 2606.0.0 | deprecation | Deprecated CloseBOMWindow microflow; see annotation for guidance. | CloseBOMWindow |  |
| 2606.0.0 | deprecation | Deprecated HandleActiveConfigErrors microflow; see annotation for guidance. | HandleActiveConfigErrors |  |
| 2606.0.0 | deprecation | Deprecated HandleServiceErrors microflow; see annotation for guidance. | HandleServiceErrors |  |
| 2606.0.0 | deprecation | Deprecated RetrieveConfigNameFromSingleActiveConfiguration microflow; see annotation for guidance. | RetrieveConfigNameFromSingleActiveConfiguration |  |
| 2606.0.0 | deprecation | Deprecated RetrieveHttpHeaderList microflow; see annotation for guidance. | RetrieveHttpHeaderList |  |
| 2606.0.0 | deprecation | Deprecated RetrieveTcSessionBasedOnConfigName microflow; see annotation for guidance. | RetrieveTcSessionBasedOnConfigName |  |
| 2606.0.0 | deprecation | Deprecated RetrieveTeamcenterConfigurationByName microflow; see annotation for guidance. | RetrieveTeamcenterConfigurationByName |  |
| 2606.0.0 | deprecation | Deprecated RetrieveTeamcenterConfigurationFromTcSession microflow; see annotation for guidance. | RetrieveTeamcenterConfigurationFromTcSession |  |
| 2606.0.0 | deprecation | Deprecated ShowPartialErrors microflow; see annotation for guidance. | ShowPartialErrors |  |
| 2606.0.0 | deprecation | Deprecated UpdateSession microflow; see annotation for guidance. | UpdateSession |  |
| 2606.0.0 | deprecation | Deprecated CreateBOMWindows Java action; see documentation for successor. | CreateBOMWindows |  |
| 2606.0.0 | deprecation | Deprecated CreateBOMWindows2 Java action; see documentation for successor. | CreateBOMWindows2 |  |
| 2606.0.0 | deprecation | Deprecated ExpandPSOneLevel Java action; see documentation for successor. | ExpandPSOneLevel |  |
| 2606.0.0 | deprecation | Deprecated GetItemFromId Java action; see documentation for successor. | GetItemFromId |  |
| 2606.0.0 | deprecation | Deprecated GetTcSessionInfo Java action; see documentation for successor. | GetTcSessionInfo |  |
| 2606.0.0 | deprecation | Deprecated GetWorkflowTemplates Java action; see documentation for successor. | GetWorkflowTemplates |  |
| 2606.0.0 | deprecation | Deprecated PerformAction Java action; see documentation for successor. | PerformAction |  |
| 2606.0.0 | deprecation | Deprecated RetrieveCookie Java action; see documentation for successor. | RetrieveCookie |  |
| 2606.0.0 | deprecation | Deprecated WhereUsed Java action; see documentation for successor. | WhereUsed |  |
| 2606.0.0 | deprecation | Deprecated CreateBomWindowInput entity (renamed with underscore prefix). | CreateBomWindowInput |  |
| 2606.0.0 | deprecation | Deprecated CreateBomWindowInput_CreateBomWindowResponse entity (renamed with underscore prefix). | CreateBomWindowInput_CreateBomWindowResponse |  |
| 2606.0.0 | deprecation | Deprecated CreateBomWindowResponse entity (renamed with underscore prefix). | CreateBomWindowResponse |  |
| 2606.0.0 | deprecation | Deprecated ExpandPSOneLevelResponse entity (renamed with underscore prefix). | ExpandPSOneLevelResponse |  |
| 2606.0.0 | deprecation | Deprecated GetItemFromIdInput entity (renamed with underscore prefix). | GetItemFromIdInput |  |
| 2606.0.0 | deprecation | Deprecated GetItemFromIdResponse entity (renamed with underscore prefix). | GetItemFromIdResponse |  |
| 2606.0.0 | deprecation | Deprecated GetWorkflowTemplatesInput entity (renamed with underscore prefix). | GetWorkflowTemplatesInput |  |
| 2606.0.0 | deprecation | Deprecated ItemRevisionOutput entity (renamed with underscore prefix). | ItemRevisionOutput |  |
| 2606.0.0 | deprecation | Deprecated RevisionIDs entity (renamed with underscore prefix). | RevisionIDs |  |
| 2606.0.0 | deprecation | Deprecated SessionUser entity (renamed with underscore prefix). | SessionUser |  |
| 2606.0.0 | deprecation | Deprecated TcServerInfo entity (renamed with underscore prefix). | TcServerInfo |  |
| 2606.0.0 | deprecation | Deprecated WhereUsedInput entity (renamed with underscore prefix). | WhereUsedInput |  |
| 2606.0.0 | deprecation | Deprecated WhereUsedResponseInfo entity (renamed with underscore prefix). | WhereUsedResponseInfo |  |
| 2606.0.0 | breaking | Moved Login Java action to private; use Login microflow instead. | Login Java action | Login |
| 2606.0.0 | breaking | Moved Logout Java action to private; use Logout microflow instead. | Logout Java action | Logout |
| 2606.0.0 | breaking | Moved LoginSSO Java action to private; set up SSO login flow as described in documentation. | LoginSSO Java action |  |
| 2606.0.0 | migration-step | Move all custom Operation Mapping JSONs to Resources/TcConnector/OperationMapping and remove old Resources/OperationMapping folder. | Resources/OperationMapping |  |
| 2606.0.0 | migration-step | Remove Resources/TeamcenterCommon folder after upgrade. | Resources/TeamcenterCommon |  |
| 2606.0.0 | migration-step | Remove Resources/TeamcenterConnector folder after upgrade. | Resources/TeamcenterConnector |  |
| 2606.0.0 | migration-step | Regenerate integration with Teamcenter Extension to resolve references to Toolkit microflows and entities now in Connector. | Teamcenter Toolkit |  |
| 2606.0.0 | removal | Removed ModelObject_AddToExistingOrNewList microflow; retain old TeamcenterToolkit module until migrated. | ModelObject_AddToExistingOrNewList |  |
| 2606.0.0 | removal | Removed JA_CopyModelObjectToNewCreateInput Java action; retain old TeamcenterToolkit module until migrated. | JA_CopyModelObjectToNewCreateInput |  |
| 2606.0.0 | removal | Removed JA_CreateDatasetSpecialization Java action; retain old TeamcenterToolkit module until migrated. | JA_CreateDatasetSpecialization |  |
| 2606.0.0 | removal | Removed pre-configured CreateBOMWindow variants; use CreateBOMWindow or CreateBOMWindow_ByConfigurationContext instead. | CreateBOMWindow_Default, CreateBOMWindow_RevisionRule, CreateBOMWindow_VariantRule | CreateBOMWindow |
| 2606.0.0 | breaking | Removed Create and Delete rights on all entities. Administrator role now has access only to Teamcenter Configuration; use User role for integrations. | Administrator role, Teamcenter Configuration |  |
| 2606.0.0 | breaking | Changed error handling behavior: Connector no longer shows in-app error messages; all errors throw exceptions for microflow control. | error handling |  |
| 2606.0.0 | breaking | Fixed bug where ConfigurationName parameter changes behavior; ModelObject Java class now consistently requires ConfigurationName in all cases. | ModelObject Java class, ConfigurationName |  |
| 2606.0.0 | breaking | Removed LastError attribute from Credentials entity; use exception handling instead. | Credentials, LastError |  |
| 2606.0.0 | breaking | Introduced new naming convention for CreateInput and CompoundCreateInput specializations; regenerate integrations by creating new Teamcenter Service document. | CreateInput, CompoundCreateInput |  |
| 2512.1.2 | security | Updated Java Dependencies to remove vulnerabilities |  |  |
| 2512.1.1 | security | Updated com.fasterxml.jackson.core:jackson-databind com.fasterxml.jackson.core:jackson-core to 2.21.2 to resolve vulnerabilities | com.fasterxml.jackson.core:jackson-databind, com.fasterxml.jackson.core:jackson-core |  |
| 2512.1.0 | improvement | Added TC SSO compatibility with TC2406 and TC2312 |  |  |
| 2512.1.0 | security | Updated Java Dependencies to remove vulnerabilities in the dependencies |  |  |
| 2512.1.0 | breaking | User provisioning for TC SSO has changed. TcSSOUserInformation now only contains User and Locale. Use 'User' instead of 'sub' for Teamcenter Username | TcSSOUserInformation |  |
| 2512.0.1 | breaking | Made the FMS URL configuration field optional | FMS URL configuration |  |
| 2512.0.0 | improvement | Reimplemented Teamcenter X SSO to remove the OIDC module dependency | Teamcenter X SSO, OIDC module |  |
| 2512.0.0 | improvement | Reimplemented Teamcenter SSO to be consistent with Teamcenter X SSO | Teamcenter SSO |  |
| 2512.0.0 | improvement | Improved the overall SSO setup experience to remove the need for startup microflow and custom home pages |  |  |
| 2512.0.0 | improvement | Teamcenter SSO now supports user provisioning and anonymous user authentication from the login page | Teamcenter SSO |  |
| 2512.0.0 | improvement | Aligned and simplified the authentication process - Credentials, Tc SSO and TcX SSO are now consistent | Credentials, Tc SSO, TcX SSO |  |
| 2512.0.0 | breaking | Updated fmsutils.jar to Tc2512 compatible version | fmsutils.jar |  |
| 2512.0.0 | removal | Removed UserLogin microflow, use NAV_UserLogin navigation microflow instead | UserLogin | NAV_UserLogin |
| 2512.0.0 | removal | Removed ShowLoginPage microflow, use NAV_UserLogin navigation microflow instead | ShowLoginPage | NAV_UserLogin |
| 2512.0.0 | removal | Removed LoginToMultipleTeamcenters microflow, use NAV_UserLoginMultipleActive navigation microflow instead | LoginToMultipleTeamcenters | NAV_UserLoginMultipleActive |
| 2512.0.0 | removal | Removed AdminLogin microflow, use User module role instead | AdminLogin | User module role |
| 2512.0.0 | removal | Removed AdminHomePage page, use NAV_AdminHomePage navigation microflow instead | AdminHomePage | NAV_AdminHomePage |
| 2512.0.0 | removal | Removed SSO_RegisterRequestHandlers after startup microflow, no longer required | SSO_RegisterRequestHandlers |  |
| 2512.0.0 | breaking | Removed TeamcenterConfiguration event handlers, if you have custom logic for TeamcenterConfiguration objects, confirm it has the correct validations | TeamcenterConfiguration |  |
| 2512.0.0 | removal | Deleted HomePage entity, no longer required | HomePage |  |
| 2512.0.0 | breaking | Multiple microflows and pages deleted from the Private folder |  |  |
| 2512.0.0 | breaking | Multiple microflows and pages moved from Public to Private folder, check these are no longer directly referenced |  |  |
| 2506.0.1 | requirement | Upgraded to Mendix 10.24.8 |  |  |
| 2506.0.1 | security | Updated Java dependencies to resolve vulnerabilities |  |  |
| 2506.0.1 | improvement | Ensured compatibility with OIDC 4.3.0 and OIDC 4.4.0 | OIDC |  |
| 2506.0.0 | improvement | Cleaned up unused jars |  |  |
| 2506.0.0 | improvement | Upgraded FMS/TcSS jars to 2506 version | fmsutils.jar |  |
| 2506.0.0 | feature | Added support for using authenticated FSC for TcX |  |  |
| 2506.0.0 | improvement | Updated string property length of TcConnector Domain Model entities to align with corresponding Teamcenter property length |  |  |
| 2506.0.0 | improvement | Configured Managed dependencies for jackson-annotations-2.19.0.jar, jackson-core-2.19.0.jar, jackson-databind-2.19.0.jar, log4j-api-2.24.3.jar, log4j-core-2.24.3.jar and Apache HTTP Components | jackson-annotations, jackson-core, jackson-databind, log4j-api, log4j-core, httpmime, httpcore, httpclient |  |
| 2506.0.0 | migration-step | Userlib exclusions: TcLogging.jar, fmsutil.jar, fscjavaclientproxy.jar, teamcenter_sso_applib.jar, teamcenter_sso_common.jar | TcLogging.jar, fmsutil.jar, fscjavaclientproxy.jar, teamcenter_sso_applib.jar, teamcenter_sso_common.jar |  |
| 2506.0.0 | known-issue | When setting up Teamcenter X, if error occurs about FriendlyName being required, add an empty check as workaround at CreateClaimwithFriendlyName microflow | CreateClaimwithFriendlyName |  |
| 2412.225.0 | improvement | Cleaned up some unused jars |  |  |
| 2412.225.0 | fix | Fixed Mendix-Teamcenter SSO connection issue by upgrading TCSS jars to TCSS2412 |  |  |
| 2412.225.0 | improvement | Updated log4j from 2.17.1 to 2.23.1 for managing conflicts with Excel Export Module | log4j |  |
| 2412.225.0 | known-issue | When setting up Teamcenter X, if error occurs about FriendlyName being required, add an empty check as workaround at CreateClaimwithFriendlyName microflow | CreateClaimwithFriendlyName |  |
| 2412.3.0 | requirement | Upgraded to Mendix 10.24.8 |  |  |
| 2412.3.0 | security | Updated Java dependencies to remove unused jar files and to resolve vulnerabilities |  |  |
| 2412.3.0 | improvement | Ensured compatibility with OIDC 4.3.0 and OIDC 4.4.0 | OIDC |  |
| 2412.0.0 | feature | Provided support for connection to TcX using SAM Auth |  |  |
| 2412.0.0 | improvement | Cleaned up some unused jars |  |  |
| 2412.0.0 | known-issue | Due to limitations with SAMAuth registration in 2412, TcConnector is not supported with Teamcenter X version 2412 and lower |  |  |
| 2412.0.0 | known-issue | When setting up Teamcenter X, if error occurs about FriendlyName being required, add an empty check as workaround at CreateClaimwithFriendlyName microflow | CreateClaimwithFriendlyName |  |
| 2406.3.1 | requirement | Upgraded to Mendix 10.24.8 |  |  |
| 2406.3.1 | security | Updated Java dependencies to remove unused jar files and to resolve vulnerabilities |  |  |
| 2406.3.1 | improvement | Dependencies now implemented using managed dependencies (vendorlib) |  |  |
| 2406.3.1 | migration-step | Before updating this module, make sure to remove all old .jar files of the previous version from the userlib folder |  |  |
| 2406.3.0 | improvement | Upgraded TcSS jars and modified SSORedirectRequestHandler.processCallback to allow create SSO App session using JSON type |  |  |
| 2406.3.0 | breaking | XML Type is no more supported for SSO App session creation |  |  |
| 2406.3.0 | improvement | Added Access Rules for TcConnector.Image and TcConnector.ImanFile entity | TcConnector.Image, TcConnector.ImanFile |  |
| 2406.3.0 | breaking | Changed length of POM_application_object.object_string and BOMLine.object_string to 4000 to match with Teamcenter data model | POM_application_object.object_string, BOMLine.object_string |  |
| 2406.3.0 | improvement | Cleaned up userlib folder by removing unrequired jars |  |  |
| 3.7.0 | requirement | Upgraded to 9.24.41 |  |  |
| 3.7.0 | improvement | Updated Java Dependencies to remove unused jar files and remove vulnerabilities in the dependencies |  |  |

## Teamcenter Connector Sample Application <a id="111688"></a>
Sample, Siemens, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/111688)

| version | published | min Mendix |
|---|---|---|
| 2506.0.0 | 2025-08-21 | 10.20.0 |
| 2412.0.0 | 2025-02-12 | 10.0.0 |
| 2406.0.0 | 2024-07-19 | 10.0.0 |
| 3.6.0 | 2023-07-25 | 9.18.2 |
| 3.5.0 | 2022-07-14 | 9.4.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2506.0.0 | requirement | Minimum Mendix version requirement is 10.20.0 | Mendix |  |
| 2506.0.0 | improvement | Updated with TC Connector v2506 | TC Connector |  |
| 2412.0.0 | requirement | Minimum Mendix version requirement is 10.0.0 | Mendix |  |
| 2412.0.0 | improvement | Updated with TC Connector v2412 | TC Connector |  |
| 2406.0.0 | requirement | Updated to support Mendix Studio Pro v10 | Mendix |  |
| 2406.0.0 | improvement | Updated with latest TC Connector 2406 | TC Connector |  |
| 3.6.0 | requirement | Minimum Mendix version requirement is 9.18.2 | Mendix |  |
| 3.6.0 | improvement | Updated to use the latest connector | TC Connector |  |
| 3.5.0 | requirement | Minimum Mendix version requirement is 9.4.0 | Mendix |  |
| 3.5.0 | improvement | Uses the latest connector | TC Connector |  |

## Teamcenter Extension <a id="225544"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/225544)

| version | published | min Mendix |
|---|---|---|
| 4.2.1 | 2026-09-30 | 10.24.8 |
| 4.2.0 | 2026-02-16 | 10.24.8 |
| 4.1.1 | 2025-07-09 | 10.24.0 |
| 4.1.0 | 2025-07-09 | 10.12.6 |
| 4.0.1 | 2025-04-09 | 10.21.0 |
| 4.0.0 | 2025-04-09 | 10.12.6 |
| 3.3.0 | 2025-03-06 | 10.12.6 |
| 3.2.1 | 2025-01-07 | 10.12.6 |
| 3.2.0 | 2024-12-12 | 10.12.6 |
| 3.1.0 | 2024-12-04 | 10.12.6 |
| 3.0.0 | 2024-10-24 | 10.12.6 |
| 2.0.0 | 2024-07-19 | 10.12.1 |
| 1.0.0 | 2024-04-22 | 10.6.5 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 4.2.1 | known-issue | Entities from add-on modules or with add-on module generalizations cannot be used in object mapping. | object mapping |  |
| 4.2.1 | known-issue | Teamcenter properties with spaces in names cannot be mapped to Mendix attributes which disallow spaces. |  |  |
| 4.2.0 | requirement | Upgraded Teamcenter extension to Mendix 10.24.8 (minimum required version). | Mendix |  |
| 4.2.0 | fix | Fixed bug where it was not possible to attach a dataset to an Item Revision. | Item Revision, dataset |  |
| 4.2.0 | fix | Updated version checker to allow using extension with Mendix 11. | version checker, Mendix 11 |  |
| 4.2.0 | known-issue | Entities from add-on modules or entities with generalizations from add-on modules cannot be used in object mapping. | add-on modules, object mapping |  |
| 4.2.0 | known-issue | Teamcenter properties with spaces in names cannot be used as Mendix attributes do not support spaces. | Teamcenter properties, Mendix attributes |  |
| 4.1.1 | requirement | Upgraded Teamcenter extension to Mendix 10.24.0 (minimum required version). | Mendix |  |
| 4.1.1 | known-issue | Teamcenter extension not compatible with Mendix Studio Pro 10.13.0, 10.13.1, 10.14.0, 10.15.0. | Mendix Studio Pro 10.13.0, Mendix Studio Pro 10.13.1, Mendix Studio Pro 10.14.0, Mendix Studio Pro 10.15.0 |  |
| 4.1.1 | known-issue | Entities from add-on modules or entities with generalizations from add-on modules cannot be used in object mapping. | add-on modules, object mapping |  |
| 4.1.1 | known-issue | Teamcenter properties with spaces in names cannot be used as Mendix attributes do not support spaces. | Teamcenter properties, Mendix attributes |  |
| 4.1.0 | known-issue | Teamcenter extension not compatible with Mendix Studio Pro 10.13.0, 10.13.1, 10.14.0, 10.15.0. | Mendix Studio Pro 10.13.0, Mendix Studio Pro 10.13.1, Mendix Studio Pro 10.14.0, Mendix Studio Pro 10.15.0 |  |
| 4.1.0 | known-issue | Entities from add-on modules or entities with generalizations from add-on modules cannot be used in object mapping. | add-on modules, object mapping |  |
| 4.1.0 | known-issue | Teamcenter properties with spaces in names cannot be used as Mendix attributes do not support spaces. | Teamcenter properties, Mendix attributes |  |
| 4.0.1 | requirement | Upgraded Teamcenter extension to Mendix 10.21.0 (minimum required version). | Mendix |  |
| 4.0.1 | known-issue | Teamcenter extension not compatible with Mendix Studio Pro 10.13.0, 10.13.1, 10.14.0, 10.15.0. | Mendix Studio Pro 10.13.0, Mendix Studio Pro 10.13.1, Mendix Studio Pro 10.14.0, Mendix Studio Pro 10.15.0 |  |
| 4.0.1 | known-issue | Entities from add-on modules or entities with generalizations from add-on modules cannot be used in object mapping. | add-on modules, object mapping |  |
| 4.0.1 | known-issue | Teamcenter properties with spaces in names cannot be used as Mendix attributes do not support spaces. | Teamcenter properties, Mendix attributes |  |
| 4.0.0 | breaking | Changed credentials-based login flow: user prompted in login dialog instead of storing credentials on Teamcenter configuration. | login flow, credentials |  |
| 4.0.0 | known-issue | Teamcenter extension not compatible with Mendix Studio Pro 10.13.0, 10.13.1, 10.14.0, 10.15.0. | Mendix Studio Pro 10.13.0, Mendix Studio Pro 10.13.1, Mendix Studio Pro 10.14.0, Mendix Studio Pro 10.15.0 |  |
| 4.0.0 | known-issue | Entities from add-on modules or entities with generalizations from add-on modules cannot be used in object mapping. | add-on modules, object mapping |  |
| 4.0.0 | known-issue | Teamcenter properties with spaces in names cannot be used as Mendix attributes do not support spaces. | Teamcenter properties, Mendix attributes |  |
| 3.3.0 | known-issue | Teamcenter extension not compatible with Mendix Studio Pro 10.13.0, 10.13.1, 10.14.0, 10.15.0. | Mendix Studio Pro 10.13.0, Mendix Studio Pro 10.13.1, Mendix Studio Pro 10.14.0, Mendix Studio Pro 10.15.0 |  |
| 3.3.0 | known-issue | Entities from add-on modules or entities with generalizations from add-on modules cannot be used in object mapping. | add-on modules, object mapping |  |
| 3.3.0 | known-issue | Teamcenter properties with spaces in names cannot be used as Mendix attributes do not support spaces. | Teamcenter properties, Mendix attributes |  |
| 3.2.1 | fix | Fixed duplication of integrations when multiple developers work with extension simultaneously. | integration duplication |  |
| 3.2.1 | known-issue | Teamcenter extension not compatible with Mendix Studio Pro 10.13.0, 10.13.1, 10.14.0, 10.15.0. | Mendix Studio Pro 10.13.0, Mendix Studio Pro 10.13.1, Mendix Studio Pro 10.14.0, Mendix Studio Pro 10.15.0 |  |
| 3.2.1 | known-issue | Entities from add-on modules or entities with generalizations from add-on modules cannot be used in object mapping. | add-on modules, object mapping |  |
| 3.2.1 | known-issue | Teamcenter properties with spaces in names cannot be used as Mendix attributes do not support spaces. | Teamcenter properties, Mendix attributes |  |
| 3.2.0 | known-issue | Teamcenter extension not compatible with Mendix Studio Pro 10.13.0, 10.13.1, 10.14.0, 10.15.0. | Mendix Studio Pro 10.13.0, Mendix Studio Pro 10.13.1, Mendix Studio Pro 10.14.0, Mendix Studio Pro 10.15.0 |  |
| 3.2.0 | known-issue | Entities from add-on modules or entities with generalizations from add-on modules cannot be used in object mapping. | add-on modules, object mapping |  |
| 3.2.0 | known-issue | Teamcenter properties with spaces in names cannot be used as Mendix attributes do not support spaces. | Teamcenter properties, Mendix attributes |  |
| 3.2.0 | known-issue | When multiple developers work with extension simultaneously and commit changes, duplication of integrations may occur. | integration duplication |  |
| 3.1.0 | improvement | Improved validation of integrations where validations pass when deleting and restoring microflows or entities. | integrations |  |
| 3.1.0 | known-issue | Teamcenter extension not compatible with Mendix Studio Pro 10.13.0, 10.13.1, 10.14.0, and 10.15.0. | Mendix Studio Pro |  |
| 3.1.0 | known-issue | Entities from add-on modules or with generalizations from add-on modules cannot be used in object mapping. | object mapping |  |
| 3.1.0 | known-issue | Teamcenter properties with spaces in names cannot be used as Mendix attributes cannot have spaces. |  |  |
| 3.0.0 | requirement | Teamcenter Extension 3.0.0 requires minimum Mendix Studio Pro 10.12.6. | Mendix Studio Pro |  |
| 3.0.0 | requirement | Teamcenter Extension 3.0.0 requires minimum TcConnector 2406.3.0. | TcConnector |  |
| 3.0.0 | breaking | Change to way Teamcenter extension integrations are stored on disk; upgrade logic ensures existing integrations work. | integrations |  |
| 3.0.0 | improvement | Improved way extension checks if editing or duplication of integrations is allowed. | integrations |  |
| 3.0.0 | improvement | Improved compatibility checks; extension works with minimum versions instead of exact versions. | Mendix Studio Pro, TcConnector |  |
| 3.0.0 | known-issue | Teamcenter extension not compatible with Mendix Studio Pro 10.13.0, 10.13.1, 10.14.0, and 10.15.0. | Mendix Studio Pro |  |
| 3.0.0 | known-issue | Entities from add-on modules or with generalizations from add-on modules not visible and cannot be used in object mapping. | object mapping |  |
| 3.0.0 | known-issue | Teamcenter properties with spaces in names result in errors in generated/updated domain model. |  |  |
| 2.0.0 | requirement | Teamcenter Extension 2.0.0 requires minimum Mendix Studio Pro 10.12.1. | Mendix Studio Pro |  |
| 2.0.0 | requirement | Teamcenter Extension 2.0.0 requires minimum TcConnector 2406.0.0. | TcConnector |  |
| 2.0.0 | removal | Removed FMS URL from Teamcenter settings as not actively used by extension. | FMS URL |  |
| 2.0.0 | removal | Removed dependence on Community Commons module. | Community Commons |  |
| 2.0.0 | known-issue | Entities from add-on modules or with generalizations from add-on modules not visible in object mapping dialog. | object mapping |  |
| 2.0.0 | known-issue | Teamcenter properties with spaces in names result in errors in generated/updated domain model. |  |  |

## Teams, Time and Project Management <a id="118347"></a>
Solution, TOCnDix, Partner, [marketplace](https://marketplace.mendix.com/link/component/118347)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2021-09-02 | ? |

## The Sustaira Platform: The Sustainability and ESG App Platform <a id="212971"></a>
Solution, Sustaira, Partner, [marketplace](https://marketplace.mendix.com/link/component/212971)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2023-08-16 | ? |

## Time Input <a id="113044"></a>
Widget, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/113044)

| version | published | min Mendix |
|---|---|---|
| 1.1.0 | 2020-02-26 | 8.5.0 |
| 1.0.0 | 2020-02-19 | 8.5.0 |

## Timeline <a id="115852"></a>
Widget, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/115852)

| version | published | min Mendix |
|---|---|---|
| 3.2.3 | 2026-02-11 | 9.6.0 |
| 3.2.2 | 2024-06-26 | 9.6.0 |
| 3.2.1 | 2023-09-27 | 9.6.0 |
| 3.2.0 | 2023-06-06 | 9.6.0 |
| 3.1.1 | 2022-12-12 | 9.6.0 |
| 3.1.0 | 2021-12-23 | 9.6.0 |
| 3.0.1 | 2021-10-06 | 9.6.0 |
| 3.0.0 | 2021-09-28 | 9.6.0 |
| 2.0.0 | 2021-04-08 | 9.0.5 |
| 1.0.0 | 2020-10-28 | 8.14.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 3.2.2 | fix | Fixed issue where widget was missing data when retrieving data via association. |  |  |
| 3.1.1 | fix | Fixed incorrect month grouping in custom visualization mode. |  |  |
| 3.0.1 | fix | Fixed issue causing design properties to not be applied to widget. | design properties |  |

## Timer Module <a id="121312"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/121312)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2022-09-06 | 9.12.4 |

## Toastify <a id="238556"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/238556)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2025-03-17 | 10.0.0 |

## Tooltip <a id="119160"></a>
Widget, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/119160)

| version | published | min Mendix |
|---|---|---|
| 1.5.1 | 2026-02-11 | 9.6.0 |
| 1.5.0 | 2026-02-04 | 9.6.0 |
| 1.4.2 | 2024-10-31 | 9.6.0 |
| 1.4.1 | 2024-10-09 | 9.6.0 |
| 1.4.0 | 2024-08-14 | 9.6.0 |
| 1.3.4 | 2024-05-23 | 9.6.0 |
| 1.3.3 | 2023-09-28 | 9.6.0 |
| 1.3.2 | 2023-08-10 | 9.6.0 |
| 1.3.1 | 2023-08-03 | 9.6.0 |
| 1.3.0 | 2023-06-06 | 9.6.0 |
| 1.2.1 | 2022-08-30 | 9.6.0 |
| 1.2.0 | 2022-05-11 | 9.6.0 |
| 1.1.0 | 2021-12-23 | 9.6.0 |
| 1.0.0 | 2021-12-10 | 9.6.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.5.0 | fix | Fixed issue where tooltip would cause scrollbars to appear in some cases. |  |  |
| 1.4.2 | fix | Fixed issue where tooltip content would flicker on hover. |  |  |
| 1.4.1 | fix | Fixed placement issues with tooltip when placed inside a layout container by adjusting trigger's container width. |  |  |
| 1.4.0 | fix | Fixed placement issues with tooltip occasionally overflowing off the screen. |  |  |
| 1.3.4 | fix | Fixed issue where content inside tooltip was forced to have fit to content width. |  |  |
| 1.3.2 | fix | Fixed issue where Tooltip not closing on escape key press. |  |  |
| 1.3.1 | fix | Fixed issue with Tooltip widget not displaying correctly when close to a datagrid table header. |  |  |
| 1.3.1 | fix | Fixed issue with Tooltip widget triggering unexpectedly due to width of trigger element. |  |  |
| 1.3.1 | fix | Fixed issue with Tooltip widget hover event not closing tooltip when attached to a disabled input. |  |  |
| 1.2.1 | fix | Fixed issue with Tooltip widget having positioning issues on a specific placement. |  |  |
| 1.2.0 | fix | Fixed issue with Tooltip widget preventing contained widgets from rendering in full width. |  |  |

## TradeDotGov Sanctions Search <a id="119041"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/119041)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2021-12-16 | 9.8.0 |

## Tree Table <a id="111095"></a>
Widget, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/111095)

| version | published | min Mendix |
|---|---|---|
| 2.3.1 | 2021-05-05 | 8.0.0 |
| 2.3.0 | 2021-02-11 | 8.0.0 |
| 2.2.0 | 2020-11-26 | 8.0.0 |
| 2.1.0 | 2020-11-26 | 8.0.0 |
| 2.0.8 | 2020-07-20 | 8.0.0 |
| 2.0.7 | 2020-05-29 | 8.0.0 |
| 2.0.6 | 2020-05-28 | 8.0.0 |
| 2.0.5 | 2020-05-28 | 8.0.0 |
| 2.0.4 | 2020-05-18 | 8.0.0 |
| 2.0.3 | 2020-05-06 | 8.0.0 |
| 2.0.2 | 2020-04-30 | 8.0.0 |
| 2.0.1 | 2020-04-17 | 8.0.0 |
| 2.0.0 | 2020-04-16 | 8.0.0 |
| 1.5.4 | 2020-03-10 | 8.0.0 |
| 1.5.3 | 2020-02-03 | 8.0.0 |
| 1.5.2 | 2019-12-11 | 8.0.0 |
| 1.5.1 | 2019-12-11 | 8.0.0 |
| 1.5.0 | 2019-11-27 | 8.0.0 |
| 1.4.0 | 2019-11-22 | 8.0.0 |
| 1.3.0 | 2019-10-17 | 8.0.0 |
| 1.2.1 | 2019-09-16 | 8.0.0 |
| 1.2.0 | 2019-09-16 | 8.0.0 |
| 1.1.1 | 2019-09-08 | 8.0.0 |
| 1.1.0 | 2019-09-07 | 8.0.0 |
| 1.0.0 | 2019-09-07 | 8.0.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.3.1 | fix | Update @jeltemx/mendix-react-widget-utils to 0.9.0 to fix MX9 deprecations | @jeltemx/mendix-react-widget-utils |  |
| 2.2.0 | improvement | Updated Ant.design table to latest version | Ant.design table |  |
| 2.0.0 | breaking | Rewrote whole internal state management (MobX@4) |  |  |
| 2.0.0 | improvement | Updated dependencies |  |  |
| 1.5.1 | removal | Removed sizes option, as this should be done in your theming | sizes option |  |
| 1.5.0 | improvement | Updated @jeltemx/mendix-react-widget-utils to latest version | @jeltemx/mendix-react-widget-utils |  |
| 1.4.0 | breaking | Breaking change: Use of a Helper object (with reference to Context and reference set to Nodes) when doing a selection or on-click | Helper object |  |
| 1.3.0 | breaking | Actions for Buttons in Selection have changed. You can now choose 3 type of microflows: None, Single, Multi. Button can be hidden when not applicable | Button Actions for Selection |  |
| 1.3.0 | removal | Removed lodash.findIndex, this is automatically transpiled | lodash.findIndex |  |

## Tree, Organogram, Pert diagram - TreeGraphWidgets collection  <a id="212053"></a>
Module, Mendixlabs, Community, [marketplace](https://marketplace.mendix.com/link/component/212053)

| version | published | min Mendix |
|---|---|---|
| 1.2.1 | 2024-09-13 | 9.18.4 |
| 1.2.0 | 2024-05-31 | 9.18.4 |
| 1.1.2 | 2024-02-12 | 9.18.4 |
| 1.1.1 | 2023-11-16 | 9.18.4 |
| 1.1.0 | 2023-08-25 | 9.18.4 |
| 1.0.0 | 2023-06-15 | 9.18.4 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.2.0 | improvement | Improved zoom behavior for OrgChart and PertChart | OrgChart, PertChart |  |
| 1.1.2 | improvement | Improved the behavior when setting focus to nodes in OrgChart and PertChart | OrgChart, PertChart |  |
| 1.1.0 | fix | Fixed a bug in the placement of nodes in a Pert diagram, where nodes were superimposed on each other | PertChart |  |
| 1.1.0 | breaking | Simplified domain model for the sample implementation; breaking change if building on top of example implementation | domain model |  |

## TS Audio Video Player <a id="116262"></a>
Module, Mendix, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/116262)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2020-12-07 | 7.23.11 |

## TS MultiFormatScanner (QR & Barcodes) <a id="116254"></a>
Module, Mendix, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/116254)

| version | published | min Mendix |
|---|---|---|
| 1.0.1 | 2021-04-16 | 7.23.11 |
| 1.0.0 | 2020-12-03 | 7.23.11 |

## Ultimate Calendar for Mendix <a id="229489"></a>
Module, Ciphix, Partner, [marketplace](https://marketplace.mendix.com/link/component/229489)

| version | published | min Mendix |
|---|---|---|
| 3.3.3 | 2026-08-13 | 11.0.0 |
| 3.3.0 | 2025-09-26 | 11.0.0 |
| 2.3.3 | 2026-08-13 | 10.0.0 |
| 2.3.2 | 2026-04-08 | 10.0.0 |
| 2.3.1 | 2026-04-03 | 10.0.0 |
| 2.3.0 | 2025-09-26 | 10.0.0 |
| 2.2.0 | 2025-09-09 | 10.0.0 |
| 2.1.0 | 2025-01-30 | 10.0.0 |
| 1.3.3 | 2026-08-13 | 9.24.12 |
| 1.3.0 | 2025-09-26 | 9.24.12 |
| 1.2.0 | 2025-09-09 | 9.24.12 |
| 1.1.0 | 2025-01-30 | 9.24.12 |
| 1.0.0 | 2024-08-12 | 9.24.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 3.3.0 | requirement | Major upgrade for Bryntum library version; ensure gantt or scheduler widgets updated to latest | Bryntum library |  |
| 3.3.0 | feature | Added React client support with skeleton loaders | React client |  |
| 2.3.0 | requirement | Major upgrade for Bryntum library version; ensure gantt or scheduler widgets updated to latest | Bryntum library |  |
| 2.3.0 | feature | Added React client support with skeleton loaders | React client |  |
| 2.2.0 | feature | Added support for the react client | React client |  |
| 2.2.0 | improvement | Updated dependencies |  |  |
| 2.1.0 | migration-step | Delete old widgets from widgets directory before loading module due to Bizzomate rebrand to Ciphix | bizzomate.BizzomateCalendar.mpk |  |
| 1.3.0 | requirement | Major upgrade for Bryntum library version; ensure gantt or scheduler widgets updated to latest | Bryntum library |  |
| 1.3.0 | feature | Added React client support with skeleton loaders | React client |  |
| 1.2.0 | feature | Added support for the react client | React client |  |
| 1.2.0 | improvement | Updated dependencies |  |  |
| 1.1.0 | migration-step | Delete old widgets from widgets directory before loading module due to Bizzomate rebrand to Ciphix | bizzomate.Calendar.mpk |  |

## Ultimate Gantt for Mendix <a id="213186"></a>
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

## Ultimate Scheduler for Mendix <a id="208890"></a>
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

## Unit Testing <a id="390"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/390)

| version | published | min Mendix |
|---|---|---|
| 10.0.8 | 2026-09-16 | 10.21.0 |
| 10.0.7 | 2026-08-06 | 10.21.0 |
| 10.0.6 | 2026-04-10 | 10.21.0 |
| 10.0.5 | 2025-10-15 | 10.21.0 |
| 10.0.4 | 2025-08-14 | 10.21.0 |
| 10.0.3 | 2025-08-07 | 10.21.0 |
| 10.0.2 | 2025-06-20 | 10.21.0 |
| 10.0.1 | 2025-05-16 | 10.21.0 |
| 10.0.0 | 2025-04-24 | 10.21.0 |
| 9.6.6 | 2026-09-16 | 9.24.0 |
| 9.6.5 | 2026-08-06 | 9.24.0 |
| 9.6.4 | 2025-10-15 | 9.24.0 |
| 9.6.3 | 2025-08-14 | 9.24.0 |
| 9.6.2 | 2025-08-07 | 9.24.0 |
| 9.6.1 | 2025-05-16 | 9.24.0 |
| 9.6.0 | 2025-03-21 | 9.24.0 |
| 9.5.2 | 2024-10-15 | 9.18.0 |
| 9.5.1 | 2024-07-04 | 9.18.0 |
| 9.5.0 | 2024-05-28 | 9.18.0 |
| 9.4.3 | 2024-05-01 | 9.18.0 |
| 9.4.2 | 2024-02-07 | 9.18.0 |
| 9.4.1 | 2023-11-14 | 9.18.0 |
| 9.4.0 | 2023-09-20 | 9.18.0 |
| 9.3.0 | 2023-04-14 | 9.18.0 |
| 9.2.0 | 2023-01-04 | 9.0.5 |
| 9.1.0 | 2022-11-07 | 9.0.5 |
| 9.0.5 | 2022-11-01 | 9.0.5 |
| 9.0.4 | 2022-03-10 | 9.0.5 |
| 9.0.3 | 2021-07-09 | 9.0.5 |
| 9.0.2 | 2021-07-07 | 9.0.5 |
| 9.0.1 | 2021-05-10 | 9.0.5 |
| 9.0.0 | 2021-05-03 | 9.0.5 |
| 8.0.6 | 2022-11-01 | 8.12.0 |
| 8.0.5 | 2022-04-13 | 8.12.0 |
| 8.0.4 | 2020-12-21 | 8.12.0 |
| 8.0.3 | 2020-12-21 | 8.1.0 |
| 8.0.1 | 2020-03-13 | 8.1.0 |
| 8.0.0 | 2019-09-26 | 8.1.0 |
| 7.0.2 | 2022-12-21 | 7.0.2 |
| 7.0.1 | 2022-12-21 | 7.0.2 |
| … 1 older versions | | |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 10.0.8 | requirement | Updated httpclient5 dependency to 5.6.4 | httpclient5 |  |
| 10.0.7 | requirement | Updated httpclient5 dependency to 5.6.2 | httpclient5 |  |
| 10.0.6 | migration-step | Migrated from SASS to CSS variables for Atlas 4 compatibility | Atlas 4 |  |
| 10.0.5 | breaking | Increased length of Name, DisplayName, Module, and TestName attributes to align with platform limits | UnitTest.Name, UnitTest.DisplayName, TestSuite.Module, UnitTestContext.TestName |  |
| 10.0.3 | requirement | Updated commons-lang3 dependency to 3.18.0 | commons-lang3 |  |
| 10.0.0 | requirement | Upgraded module to Mendix version 10.21.0 for compatibility with Mendix 11 | Mendix |  |
| 10.0.0 | requirement | Updated Atlas Core compatibility to version 3.17.0 | Atlas Core |  |
| 10.0.0 | requirement | Updated Atlas Web Content compatibility to version 3.8.0 | Atlas Web Content |  |
| 10.0.0 | requirement | Updated Data Widgets compatibility to version 2.31.0 | Data Widgets |  |
| 9.6.6 | requirement | Updated httpclient5 dependency to 5.6.4 | httpclient5 |  |
| 9.6.5 | requirement | Updated httpclient5 dependency to 5.6.2 | httpclient5 |  |
| 9.6.4 | breaking | Increased length of Name, DisplayName, Module, and TestName attributes to align with platform limits | UnitTest.Name, UnitTest.DisplayName, TestSuite.Module, UnitTestContext.TestName |  |
| 9.6.2 | requirement | Updated commons-lang3 dependency to 3.18.0 | commons-lang3 |  |
| 9.6.0 | requirement | Upgraded module to Mendix version 9.24.0 | Mendix |  |
| 9.6.0 | requirement | Added Accordion widget as dependency, compatible with v2.3.4 | Accordion |  |
| 9.6.0 | requirement | Updated Atlas Core module compatibility to v3.12.5 | Atlas Core |  |
| 9.6.0 | requirement | Added Atlas Web Content module as dependency, compatible with v3.4.2 | Atlas Web Content |  |
| 9.6.0 | requirement | Added Data Widgets module as dependency, compatible with v2.27.3 | Data Widgets |  |
| 9.5.2 | requirement | Updated Apache Commons IO dependency to 2.17.0 | commons-io |  |
| 9.5.0 | improvement | Updated unit test details page for React client compatibility, introduced in Mendix 10.7.0 |  |  |
| 9.4.3 | breaking | Changed Name attribute in UnitTest entity length to limited (#213295) | UnitTest.Name |  |
| 9.4.2 | requirement | Updated slf4j-api from 1.7.36 to 2.0.9; review userlib and match other slf4j library versions | slf4j-api |  |
| 9.4.1 | requirement | Updated httpclient5 from 5.0.3 to 5.2.1 | httpclient5 |  |
| 9.4.1 | requirement | Updated httpcore5 from 5.0.2 to 5.2 | httpcore5 |  |
| 9.4.1 | requirement | Updated httpcore5-h2 from 5.0.2 to 5.2 | httpcore5-h2 |  |
| 9.4.1 | requirement | Updated slf4j-api from 1.7.25 to 1.7.36 | slf4j-api |  |
| 9.4.1 | removal | Removed dependency on commons-codec-1.13; review userlib after upgrade | commons-codec-1.13 |  |
| 9.4.0 | migration-step | Switched from hamcrest-2.2.jar to hamcrest-core-1.3.jar and downgraded httpcore5 to 5.0.2; remove old files from userlib | hamcrest-2.2.jar, httpcore5-5.0.3.jar |  |
| 9.4.0 | requirement | Included Java dependency migration file for Studio Pro 10 compatibility | Mendix |  |
| 9.3.0 | requirement | Upgraded module to Mendix version 9.18.0 for compatibility with Mendix 10 | Mendix |  |
| 9.3.0 | breaking | Replaced IContext.rollbackTransAction with IContext.rollbackTransaction |  | IContext.rollbackTransaction |
| 9.2.0 | removal | Removed dependency on Community Commons module; review userlib and remove if unused | Community Commons |  |
| 9.2.0 | requirement | Updated commons-lang3 dependency from 3.11 to 3.12.0; remove old 3.11 jar files from userlib | commons-lang3 |  |
| 9.1.0 | requirement | Replaced Object Handling module dependency with Community Commons module; download from marketplace | Community Commons | Community Commons |
| 9.0.5 | requirement | Updated commons-io dependency from 2.8.0 to 2.11.0 to align with Community Commons | commons-io |  |
| 9.0.4 | migration-step | Fixed file naming conventions in userlib folder |  |  |
| 9.0.4 | requirement | Updated commons-lang from 3.7 to 3.11 to align with Mendix Community Commons | commons-lang |  |
| 9.0.1 | security | Updated commons-io to 2.8.0 due to directory traversal vulnerability in 2.6 | commons-io |  |
| 9.0.0 | requirement | Mendix 9.0.0 support | Mendix |  |
| 8.0.6 | requirement | Updated commons-io dependency from 2.8.0 to 2.11.0 to align with Community Commons | commons-io |  |
| 8.0.5 | requirement | Updated dependencies/userlib folder for Mendix 8 to sync with v9.0.4 |  |  |
| 8.0.4 | requirement | Mendix 8.12.0 support | Mendix |  |
| 8.0.0 | requirement | Updated module to Mendix 8 | Mendix |  |
| 7.0.2 | requirement | Updated commons-io dependency from 2.8.0 to 2.11.0 to align with Community Commons | commons-io |  |
| 7.0.1 | requirement | Updated dependencies/userlib folder for Mendix 7 to sync with v9.0.4 |  |  |

## Unsplash Photo Connector <a id="116977"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/116977)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2021-04-08 | 8.18.1 |

## User Classification <a id="245015"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/245015)

| version | published | min Mendix |
|---|---|---|
| 2.0.0 | 2025-12-04 | 10.24.0 |
| 1.0.1 | 2025-11-27 | 9.24.0 |
| 1.0.0 | 2025-08-06 | 9.24.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.0.0 | requirement | Requires Mendix 10.24.0 or higher for version 2.0.0. |  |  |
| 1.0.1 | improvement | Improved user classification logic to enhance consistency and reliability (Ticket #261169). |  |  |
| 1.0.0 | requirement | Requires Mendix 9.24.0 or higher. |  |  |

## User Migration <a id="118015"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/118015)

| version | published | min Mendix |
|---|---|---|
| 2.0.2 | 2024-07-04 | 9.24.0 |
| 2.0.1 | 2024-06-25 | 9.24.0 |
| 2.0.0 | 2023-04-19 | 9.24.0 |
| 1.0.1 | 2023-04-19 | 8.18.10 |
| 1.0.0 | 2021-07-16 | 8.15.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.0.0 | requirement | Upgraded to Mendix v9.24.0 | Mendix |  |

## UserCommons <a id="223053"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/223053)

| version | published | min Mendix |
|---|---|---|
| 2.4.0 | 2026-07-10 | 10.24.0 |
| 2.3.0 | 2026-06-11 | 10.24.0 |
| 2.2.1 | 2026-02-09 | 10.24.0 |
| 2.2.0 | 2025-11-20 | 10.21.1 |
| 2.1.3 | 2025-07-02 | 10.21.1 |
| 2.1.2 | 2025-05-29 | 10.21.1 |
| 2.1.1 | 2025-05-29 | 10.21.0 |
| 2.1.0 | 2025-05-07 | 10.21.1 |
| 2.0.2 | 2025-06-30 | 10.12.10 |
| 2.0.1 | 2025-05-07 | 10.12.10 |
| 2.0.0 | 2024-12-24 | 10.12.10 |
| 1.0.4 | 2026-01-26 | 9.24.2 |
| 1.0.3 | 2025-05-07 | 9.24.2 |
| 1.0.2 | 2024-07-29 | 9.24.2 |
| 1.0.1 | 2024-03-07 | 9.24.2 |
| 1.0.0 | 2024-02-22 | 9.24.2 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.4.0 | improvement | Forward compatibility improved for usage in Mendix 11.12 applications with react client enabled |  |  |
| 2.3.0 | requirement | Updated for compatibility with v4.5.0 of the OIDC SSO module | OIDC SSO module |  |
| 2.3.0 | removal | Removed dependency on Nanoflow module | Nanoflow module |  |
| 2.2.0 | feature | New user-related entity introduced for storing named user identifier consistently across multiple apps for correct multi-app user metering |  |  |
| 2.1.2 | requirement | Ensures compatibility with Mendix 11 |  |  |
| 2.1.1 | requirement | Ensures compatibility with Mendix 11 |  |  |
| 2.1.1 | known-issue | Compatibility Warning for Mendix 10.21.1 Users: v2.1.1 is for Mendix 10.21.0 only, use v2.1.0 or upgrade to v2.1.2 |  |  |
| 2.1.0 | requirement | v.2.1.0 version for apps on Mx10.21.1 or higher |  |  |
| 2.0.0 | requirement | v.2.0.0 version for apps on Mx10.12.10 or higher |  |  |
| 2.0.0 | improvement | Language and timezone now set to user based on default App settings when not provided by IDP (Ticket #231488) |  |  |
| 1.0.3 | improvement | Language and timezone now set to user based on default App settings when not provided by IDP (Ticket #231488, #241569) |  |  |
| 1.0.3 | improvement | Enhanced UserProvisioning to eliminate redundant return value (Ticket #230774) | UserProvisioning |  |
| 1.0.2 | breaking | Extended length of UserClaim.Value attribute to be unlimited | UserClaim.Value |  |
| 1.0.1 | feature | Support of FriendlyName in CustomClaims Configuration |  |  |
| 1.0.1 | feature | Support of TimeZone in UserProvisioning |  |  |
| 1.0.1 | feature | Support of Language in UserProvisioning |  |  |
| 1.0.0 | requirement | UserCommons supported for Mendix 9.24.2 onwards |  |  |
| 1.0.0 | feature | Introduces ability to utilize custom user entities alongside default Administration.Account entity |  |  |
| 1.0.0 | feature | Facilitates accurate synchronization of Identity Provider attributes with entity attributes for enhanced data integrity |  |  |
| 1.0.0 | feature | Introduces possibility to configure UserType for provisioned users from same IdP source without custom microflow |  |  |
| 1.0.0 | feature | Facilitates setting default user role for any user created in app |  |  |
| 1.0.0 | feature | Empowers administrators with runtime configuration options for default user roles, types, and custom provisioning logic |  |  |

## Vibe Transcribe <a id="244525"></a>
Module, Siemens, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/244525)

| version | published | min Mendix |
|---|---|---|
| 1.1.0 | 2026-03-20 | 10.24.2 |
| 1.0.0 | 2025-08-28 | 10.24.2 |

## Vibing Audio Recorder <a id="244303"></a>
Widget, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/244303)

| version | published | min Mendix |
|---|---|---|
| 1.2.0 | 2026-03-20 | 11.7.0 |
| 1.1.0 | 2025-07-24 | 9.6.0 |
| 1.0.0 | 2025-07-24 | 9.6.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.2.0 | requirement | Minimum Mendix version requirement increased to 11.7.0 | Mendix |  |

## Video Player <a id="110700"></a>
Widget, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/110700)

| version | published | min Mendix |
|---|---|---|
| 3.2.4 | 2026-02-11 | 9.6.0 |
| 3.2.3 | 2025-05-22 | 9.6.0 |
| 3.2.2 | 2023-09-27 | 9.6.0 |
| 3.2.1 | 2023-08-08 | 9.6.0 |
| 3.2.0 | 2023-06-06 | 9.6.0 |
| 3.1.1 | 2022-03-29 | 9.6.0 |
| 3.1.0 | 2021-12-23 | 9.6.0 |
| 3.0.2 | 2021-12-03 | 9.6.0 |
| 3.0.1 | 2021-11-17 | 9.6.0 |
| 3.0.0 | 2021-09-28 | 9.6.0 |
| 2.0.1 | 2021-08-17 | 8.0.0 |
| 2.0.0 | 2021-07-12 | 9.0.5 |
| 1.2.0 | 2021-07-12 | 8.0.0 |
| 1.1.0 | 2021-07-02 | 8.0.0 |
| 1.0.1 | 2020-07-16 | 8.0.0 |
| 1.0.0 | 2019-08-01 | 8.0.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 3.0.1 | breaking | Changed default value for video data source to dynamic. | video data source |  |
| 2.0.1 | breaking | Renamed video Link and Poster Link widget properties. | video Link property, Poster Link property |  |
| 1.1.0 | breaking | Renamed video URL and Poster URL widget properties. | video URL property, Poster URL property |  |

## Virus Scan For Mendix <a id="29130"></a>
Module, Emixa, Partner, [marketplace](https://marketplace.mendix.com/link/component/29130)

| version | published | min Mendix |
|---|---|---|
| 7.0.0 | 2026-08-05 | 11.12.1 |
| 6.0.1 | 2026-04-13 | 10.24.0 |
| 6.0.0 | 2026-02-06 | 10.24.0 |
| 5.2.1 | 2023-06-15 | 8.18.24 |
| 5.2.0 | 2023-06-01 | 8.18.24 |
| 5.1.0 | 2022-12-06 | 8.18.18 |
| 5.0.0 | 2022-07-06 | 8.18.18 |
| 4.0.0 | 2021-04-23 | 8.14.1 |
| 3.1.0 | 2021-02-08 | 7.23.17 |
| 3.0.0 | 2019-12-18 | 7.2.0 |
| 2.0.1 | 2019-04-24 | 7.2.0 |
| 2.0.0 | 2019-04-05 | 7.2.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 7.0.0 | requirement | Minimum Mendix version upgraded to 11.12.1 |  |  |
| 6.0.1 | fix | Fixed issues with parameters, versioning and leftover jars | parameters, versioning |  |
| 6.0.0 | breaking | Changed parameters for synchronous scanning; jar no longer needed | parameters, synchronous scanning |  |
| 5.2.1 | breaking | Updated to work with latest ApprontoLicencer; license name must be 'VirusScan4Mendix'. Fixed InputParamter | ASU_VirusScan4Mendix, ApprontoLicencer, InputParamter |  |
| 5.2.1 | requirement | Recommended to update Appronto Licensing module for compatibility | Appronto Licensing |  |
| 5.2.0 | requirement | Minimum Mendix version upgraded to 8.18.24 |  |  |
| 5.2.0 | improvement | Jackson Java libraries updated to 2.15.2 | Jackson |  |
| 5.2.0 | improvement | Scanii Java library updated to 5.0.0 | Scanii |  |
| 5.1.0 | security | Updated jackson libraries to 2.13.4 series, slf4j-api to 2.0.5, added slf4j-nop-2.0.5, removed http-request-6.0 | jackson-databind, jackson-annotations, jackson-core, jackson-datatype-jsr310, slf4j-api, slf4j-nop, http-request |  |
| 5.0.0 | fix | Fixed bug in closing thread after scanning file resulting in thread overflow | thread management |  |
| 4.0.0 | removal | Removed dependencies on ProcessQueue module | ProcessQueue |  |
| 4.0.0 | breaking | AfterStartup flow now returns a boolean value | AfterStartup |  |
| 4.0.0 | breaking | Input parameter name of scan Java action has been changed | scan Java action |  |
| 4.0.0 | migration-step | Include excluded ProcessQueue microflows if you want to keep using ProcessQueue | ProcessQueue |  |
| 3.1.0 | requirement | Minimum Mendix version upgraded to 7.23.17 |  |  |
| 3.0.0 | removal | Removed dependencies on other modules except ApprontoLicenser |  |  |
| 3.0.0 | breaking | Default behavior changed to NOT use ProcessQueue; include excluded flows if required | ProcessQueue |  |
| 2.0.1 | improvement | Updated com.fasterxml.jackson.* jar files | com.fasterxml.jackson |  |
| 2.0.0 | requirement | Upgraded to Mendix 7 |  |  |

## Web Actions <a id="114337"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/114337)

| version | published | min Mendix |
|---|---|---|
| 2.11.2 | 2026-02-16 | 10.21.0 |
| 2.11.1 | 2025-10-31 | 10.21.0 |
| 2.11.0 | 2025-04-16 | 10.21.0 |
| 2.10.0 | 2024-01-29 | 9.24.0 |
| 2.9.0 | 2023-10-27 | 9.24.0 |
| 2.8.0 | 2023-06-06 | 9.18.4 |
| 2.7.0 | 2023-03-15 | 9.18.4 |
| 2.6.0 | 2022-11-10 | 9.12.0 |
| 2.5.0 | 2022-08-31 | 9.10.0 |
| 2.4.0 | 2022-01-25 | 9.10.0 |
| 2.3.0 | 2021-09-28 | 9.6.0 |
| 2.2.0 | 2021-08-11 | 9.0.5 |
| 2.1.1 | 2021-07-01 | 9.0.5 |
| 2.1.0 | 2021-05-28 | 9.0.5 |
| 2.0.0 | 2021-04-20 | 9.0.5 |
| 1.0.0 | 2020-05-22 | 8.6.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.11.0 | requirement | Updated studio pro minimum version to 10.21 to support Mendix 11. |  |  |
| 2.10.0 | requirement | Recommended minimum atlas-core version is now version 3. | atlas-core |  |
| 2.7.0 | requirement | Updated minimal supported version to Mendix Studio Pro 9.18.4 and above. |  |  |
| 2.4.0 | removal | Removed icon collections from the module. | icon collections |  |
| 2.4.0 | breaking | Changed javascript actions to be exclusive for Web platform. | javascript actions |  |
| 2.0.0 | requirement | Added compatibility with Studio Pro 9. |  |  |

## Web UI Package for SAP Fiori theme <a id="116359"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/116359)

| version | published | min Mendix |
|---|---|---|
| 4.1.0 | 2026-09-02 | 10.21.0 |
| 4.0.0 | 2025-07-08 | 10.21.0 |
| 3.2.0 | 2025-05-23 | 9.24.33 |
| 3.1.0 | 2023-09-29 | 9.24.0 |
| 3.0.0 | 2023-04-10 | 9.24.0 |
| 2.0.0 | 2022-06-20 | 9.6.11 |
| 1.0.3 | 2021-12-20 | 8.14.1 |
| 1.0.2 | 2021-12-17 | 8.14.1 |
| 1.0.1 | 2021-12-08 | 8.14.1 |
| 1.0.0 | 2020-12-19 | 8.14.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 4.0.0 | requirement | Upgraded to Mendix 10.21.0, minimum required version is now 10.21.0 | Mendix |  |
| 3.2.0 | requirement | Upgraded to Mendix 9.24.33, minimum required version is now 9.24.33 | Mendix |  |
| 3.0.0 | requirement | Upgraded to Mendix 9.24, minimum required version is now 9.24.0 | Mendix |  |
| 2.0.0 | requirement | Upgraded to Mendix 9.6.11, minimum required version is now 9.6.11. Refer documentation for upgrade. | Mendix |  |

## Webhook Producer <a id="119821"></a>
Service, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/119821)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2022-03-02 | 9.6.6 |

## WebXR Widgets <a id="225425"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/225425)

| version | published | min Mendix |
|---|---|---|
| 1.0.2 | 2026-02-18 | 11.0.0 |
| 1.0.1 | 2025-11-28 | 11.0.0 |
| 0.0.2 | 2024-07-11 | 10.9.0 |
| 0.0.1 | 2024-04-16 | 10.9.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.0.1 | fix | Fixed compatibility issues with react version. | react |  |

## what3words <a id="207463"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/207463)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2023-02-21 | 9.22.0 |

## Wizard widget <a id="204970"></a>
Widget, Mendixlabs, Community, [marketplace](https://marketplace.mendix.com/link/component/204970)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2022-11-25 | 9.0.5 |

## WizardSteps <a id="2651"></a>
Widget, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/2651)

| version | published | min Mendix |
|---|---|---|
| 1.0.1 | 2021-07-12 | 8.12.0 |
| 1.0.0 | 2016-03-16 | 8.12.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 1.0.1 | improvement | Test on Mendix 9 |  |  |

## Workflow Commons <a id="117066"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/117066)

| version | published | min Mendix |
|---|---|---|
| 4.11.1 | 2026-10-02 | 11.13.0 |
| 4.11.0 | 2026-07-28 | 11.13.0 |
| 4.10.0 | 2026-05-29 | 11.11.0 |
| 4.9.0 | 2026-04-29 | 11.10.0 |
| 4.8.0 | 2026-04-20 | 11.9.0 |
| 4.7.0 | 2026-04-08 | 11.9.0 |
| 4.6.0 | 2026-03-03 | 11.8.0 |
| 4.5.0 | 2026-01-27 | 11.6.0 |
| 4.4.0 | 2025-12-24 | 11.6.0 |
| 4.3.0 | 2025-10-03 | 11.2.0 |
| 4.2.0 | 2025-09-18 | 11.2.0 |
| 4.1.0 | 2025-08-29 | 11.2.0 |
| 4.0.1 | 2025-06-17 | 11.0.0 |
| 4.0.0 | 2025-05-28 | 11.0.0 |
| 3.12.1 | 2025-01-06 | 10.17.0 |
| 3.12.0 | 2024-11-27 | 10.17.0 |
| 3.11.0 | 2024-11-08 | 10.14.0 |
| 3.10.0 | 2024-09-24 | 10.14.0 |
| 3.9.0 | 2024-08-27 | 10.14.0 |
| 3.8.1 | 2024-08-15 | 10.12.0 |
| 3.8.0 | 2024-08-13 | 10.12.0 |
| 3.7.0 | 2024-07-22 | 10.11.0 |
| 3.6.0 | 2024-06-28 | 10.11.0 |
| 3.5.0 | 2024-06-24 | 10.11.0 |
| 3.4.0 | 2024-06-05 | 10.11.0 |
| 3.3.1 | 2024-03-15 | 10.6.0 |
| 3.3.0 | 2023-12-21 | 10.6.0 |
| 3.2.0 | 2023-09-26 | 10.3.0 |
| 3.1.1 | 2023-10-19 | 10.1.0 |
| 3.1.0 | 2023-06-28 | 10.0.0 |
| 3.0.0 | 2023-06-01 | 10.0.0 |
| 2.6.0 | 2024-04-16 | 9.24.0 |
| 2.5.0 | 2022-11-30 | 9.20.0 |
| 2.4.0 | 2022-10-26 | 9.19.0 |
| 2.3.2 | 2022-12-21 | 9.18.0 |
| 2.3.1 | 2022-09-30 | 9.17.0 |
| 2.3.0 | 2022-09-01 | 9.17.0 |
| 2.2.1 | 2022-08-22 | 9.16.1 |
| 2.2.0 | 2022-07-06 | 9.15.0 |
| 2.1.4 | 2022-12-21 | 9.12.6 |
| … 15 older versions | | |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 4.11.0 | requirement | Upgraded module to Mendix 11.13.0 | Mendix |  |
| 4.11.0 | requirement | Updated Data Widgets module compatibility to v3.11.2 | Data Widgets |  |
| 4.11.0 | requirement | Updated Atlas Core module compatibility to v4.3.7 | Atlas Core |  |
| 4.10.0 | requirement | Upgraded module to Mendix 11.11.0 | Mendix |  |
| 4.9.0 | requirement | Upgraded module to Mendix 11.10.0 | Mendix |  |
| 4.8.0 | requirement | Updated Data Widgets module compatibility to v3.9.0 | Data Widgets |  |
| 4.8.0 | requirement | Updated Atlas Core module compatibility to v4.3.5 | Atlas Core |  |
| 4.8.0 | requirement | Updated Atlas Web Content module compatibility to v4.3.0 | Atlas Web Content |  |
| 4.8.0 | improvement | Reduced dependency on Administration module in microflows, snippets, and pages | Administration module, microflows, snippets, pages |  |
| 4.7.0 | requirement | Upgraded module to Mendix 11.9.0 | Mendix |  |
| 4.6.0 | requirement | Upgraded module to Mendix 11.8.0 | Mendix |  |
| 4.6.0 | requirement | Updated Data Widgets module compatibility to v3.8.0 | Data Widgets |  |
| 4.4.0 | requirement | Upgraded module to Mendix 11.6.0 | Mendix |  |
| 4.3.0 | requirement | Updated Data Widgets module compatibility to v3.5.0 | Data Widgets |  |
| 4.3.0 | requirement | Updated Atlas Core module compatibility to v4.1.3 | Atlas Core |  |
| 4.3.0 | requirement | Updated Atlas Web Content module compatibility to v4.1.0 | Atlas Web Content |  |
| 4.1.0 | requirement | Upgraded module to Mendix 11.2.0 | Mendix |  |
| 4.0.0 | requirement | Upgraded module to Mendix 11.0.0-beta.2 | Mendix |  |
| 4.0.0 | removal | Removed state change events microflows OCh_Workflow_State and OCh_WorkflowUserTask_State | OCh_Workflow_State, OCh_WorkflowUserTask_State |  |
| 4.0.0 | removal | Removed assignee and key migration microflows from versions 3.0.0 and 3.6.0 | assignee migration microflows, key migration microflows |  |
| 4.0.0 | migration-step | Added migration logic for one-off data migration when upgrading to Mendix 11 |  |  |
| 4.0.0 | breaking | Replaced List View for displaying assignees with Data Grid 2 reference set support | assignees display | Data Grid 2 |
| 4.0.0 | requirement | Updated Atlas Core module compatibility to v3.17.0 | Atlas Core |  |
| 4.0.0 | requirement | Updated Atlas Web Content module compatibility to v3.8.0 | Atlas Web Content |  |
| 4.0.0 | requirement | Updated Data Widgets module compatibility to v2.31.0 | Data Widgets |  |
| 4.0.0 | migration-step | Must be on Workflow Commons v3.6.0+ before upgrading to v4.0.0. Use Mendix 10 if upgrading from earlier version. |  |  |
| 4.0.0 | migration-step | Replace microflow ACT_UserTaskView_ShowUserTask Page with ACT_WorkflowUserTaskView_ShowUserTaskPage |  | ACT_WorkflowUserTaskView_ShowUserTaskPage |
| 4.0.0 | migration-step | Replace microflow ACT_UserTaskView_ShowWorkflowAdminPage with ACT_WorkflowUserTaskView_ShowDefaultAdminPage |  | ACT_WorkflowUserTaskView_ShowDefaultAdminPage |
| 4.0.0 | migration-step | Replace microflow ACT_WorkflowView_ShowWorkflowAdminPage with ACT_Workflow_ShowWorkflowAdminPage |  | ACT_Workflow_ShowWorkflowAdminPage |
| 4.0.0 | migration-step | Replace snippet Snip_UserTaskView_Assignees with Snip_WorkflowUserTaskView_Assignees |  | Snip_WorkflowUserTaskView_Assignees |
| 4.0.0 | migration-step | Replace snippet Snip_UserTaskView_Assignees_Aggregated with Snip_WorkflowUserTaskView_Assignees |  | Snip_WorkflowUserTaskView_Assignees |
| 4.0.0 | migration-step | Replace snippet Snip_UserTaskView_Details with Snip_WorkflowUserTaskView_Details |  | Snip_WorkflowUserTaskView_Details |
| 4.0.0 | migration-step | Replace snippet Snip_UserTaskView_Header with Snip_UserTask_Header or Snip_WorfkflowEndedUserTask_Header |  | Snip_UserTask_Header or Snip_WorfkflowEndedUserTask_Header |
| 4.0.0 | migration-step | Replace snippet Snip_UserTaskView_IncompatibleWarning with Snip_WorkflowUserTaskView_IncompatibleWarning |  | Snip_WorkflowUserTaskView_IncompatibleWarning |
| 4.0.0 | migration-step | Replace snippet Snip_UserTaskView_NameColumn with Snip_WorkflowUserTaskView_NameColumn |  | Snip_WorkflowUserTaskView_NameColumn |
| 4.0.0 | migration-step | Replace snippet Snip_UserTaskView_NameColumnWithIcon with Snip_WorkflowUserTaskView_NameColumnWithIcon |  | Snip_WorkflowUserTaskView_NameColumnWithIcon |
| 4.0.0 | migration-step | Replace snippet Snip_UserTaskView_State with Snip_WorkflowUserTaskView_State |  | Snip_WorkflowUserTaskView_State |
| 4.0.0 | migration-step | Replace snippet Snip_UserTaskView_TargetUsers with Snip_UserTask_TargetUsers or Snip_WorkflowEndedUserTask_TargetUsers |  | Snip_UserTask_TargetUsers or Snip_WorkflowEndedUserTask_TargetUsers |
| 4.0.0 | migration-step | Replace snippet Snip_WorkflowView_ActivityTimeline with Snip_Workflow_ActivityTimeline |  | Snip_Workflow_ActivityTimeline |
| 4.0.0 | migration-step | Replace snippet Snip_WorkflowView_ActivityTimelineOnly_Full with Snip_Workflow_ActivityTimelineOnly_Full |  | Snip_Workflow_ActivityTimelineOnly_Full |
| 4.0.0 | migration-step | Replace snippet Snip_WorkflowView_ActivityTimelineOnly_Tasks with Snip_Workflow_ActivityTimelineOnly_Tasks |  | Snip_Workflow_ActivityTimelineOnly_Tasks |
| 4.0.0 | migration-step | Replace snippet Snip_WorkflowView_AuditTrail with Snip_Workflow_AuditTrail |  | Snip_Workflow_AuditTrail |
| 4.0.0 | migration-step | Replace snippet Snip_WorkflowView_CommentsAndAttachments with Snip_Workflow_CommentsAndAttachments |  | Snip_Workflow_CommentsAndAttachments |
| 4.0.0 | migration-step | Replace snippet Snip_WorkflowView_CommentsAndAttachments_Admin with Snip_Workflow_CommentsAndAttachments_Admin |  | Snip_Workflow_CommentsAndAttachments_Admin |
| 4.0.0 | migration-step | Replace snippet Snip_WorkflowView_CompletedTaskDetails with Snip_Workflow_TaskDetails |  | Snip_Workflow_TaskDetails |
| 4.0.0 | migration-step | Replace snippet Snip_WorkflowView_Detail with Snip_Workflow_Detail |  | Snip_Workflow_Detail |
| 4.0.0 | migration-step | Replace snippet Snip_WorkflowView_Header with Snip_Workflow_Header |  | Snip_Workflow_Header |
| 4.0.0 | migration-step | Replace snippet Snip_WorkflowView_NotificationArea with Snip_Workflow_NotificationArea |  | Snip_Workflow_NotificationArea |
| 4.0.0 | migration-step | Replace snippet Snip_WorkflowView_State with Snip_Workflow_State |  | Snip_Workflow_State |
| 4.0.0 | migration-step | Replace snippet Snip_WorkflowView_StateCircleOnly with Snip_Workflow_StateCircleOnly |  | Snip_Workflow_StateCircleOnly |
| 4.0.0 | migration-step | Replace snippet Snip_WorkflowView_TaskTimeline with Snip_Workflow_TaskTimeline |  | Snip_Workflow_TaskTimeline |
| 4.0.0 | migration-step | Replace snippet Snip_WorkflowView_TaskTimeline_WithoutNameandDescription with Snip_Workflow_TaskTimeline_WithoutName |  | Snip_Workflow_TaskTimeline_WithoutName |
| 4.0.0 | migration-step | Replace snippet Snip_WorkflowView_TaskTimelineOnly with Snip_Workflow_TaskTimelineOnly |  | Snip_Workflow_TaskTimelineOnly |
| 3.12.1 | breaking | Changed length of Reason attribute in WorkflowAuditTrailRecord entity to unlimited | WorkflowAuditTrailRecord.Reason |  |
| 3.12.0 | requirement | Upgraded module to Mendix 10.17.0 | Mendix |  |
| 3.12.0 | requirement | Updated Data Widgets module compatibility to v2.28.1 | Data Widgets |  |
| 3.12.0 | requirement | Added compatibility for changes in System module introduced with Mendix 10.17.0 | System module |  |
| 3.11.0 | requirement | Updated Data Widgets module compatibility to v2.26.0 | Data Widgets |  |
| 3.9.0 | requirement | Upgraded module to Mendix 10.14.0 | Mendix |  |
| 3.9.0 | requirement | Added compatibility for changes in System module introduced with Mendix 10.14.0 | System module |  |
| 3.8.0 | requirement | Upgraded module to Mendix 10.12.0 | Mendix |  |
| 3.8.0 | requirement | Updated Data Widgets module compatibility to v2.21.2 | Data Widgets |  |
| 3.6.0 | migration-step | Run migration microflow ACT_Key_Migrate or add ASu_Key_Migrate to after startup microflow to populate keys in existing data. | WorkflowView, UserTaskView, ACT_Key_Migrate, ASu_Key_Migrate |  |
| 3.5.0 | improvement | Added React client support; updated dropdown and reference selector widgets to Combo Box. | Combo Box |  |
| 3.5.0 | requirement | Combo Box widget must be installed in project for React client support. | Combo Box |  |
| 3.5.0 | breaking | Updated Atlas Core compatibility to v3.14.2; Static image widget replaced with Image widget. | Atlas Core | Image |
| 3.5.0 | requirement | Updated Data Widgets module compatibility to v2.20.0. | Data Widgets |  |
| 3.5.0 | requirement | Updated Charts widget compatibility to v5.0.0. | Charts |  |
| 3.5.0 | migration-step | When importing in Mendix 10.6.0+, right-click and update all renamed design properties to resolve consistency error CE6087. |  |  |
| 3.4.0 | requirement | Upgraded module to Mendix 10.11.0. |  |  |
| 3.4.0 | removal | Removed unused charts configuration file from module. |  |  |
| 3.4.0 | requirement | Updated Data Widgets compatibility to v2.19.1. | Data Widgets |  |
| 3.3.1 | known-issue | Activity timeline might show 'Merge of parallel split' activity in wrong position; will be fixed in future Studio Pro release. |  |  |
| 3.3.0 | requirement | Upgraded module to Mendix 10.6.0. |  |  |
| 3.3.0 | breaking | Replaced activity timeline in UserTask_Extended and My initiated workflows pages; now filters out non-task activities. | UserTask_Extended, My initiated workflows |  |
| 3.3.0 | requirement | Updated Atlas Web Content compatibility to 3.4.1. | Atlas Web Content |  |
| 3.3.0 | requirement | Updated Data Widgets compatibility to v2.11.0. | Data Widgets |  |
| 3.3.0 | known-issue | Activity timeline might show 'Merge of parallel split' activity in wrong position; will be fixed in future Studio Pro release. |  |  |
| 3.2.0 | requirement | Upgraded module to Mendix 10.3.0. |  |  |
| 3.2.0 | removal | Removed dependency on List view controls widget. | List view controls |  |
| 3.1.1 | requirement | Upgraded module to Mendix 10.1.0. |  |  |
| 3.1.0 | requirement | Upgraded module to Mendix 10.0.0. |  |  |
| 3.1.0 | breaking | Changed how target users are displayed on workflow admin page for consistency with assignees list. |  |  |
| 3.1.0 | breaking | Changed how decision method is retrieved on workflow admin page. |  |  |
| 3.0.0 | requirement | Upgraded module to Mendix 10.0.0-beta2. |  |  |
| 3.0.0 | breaking | With multi-user tasks, assignees now reference set; existing assignee data requires migration. | UserTaskView_Assignees |  |
| 3.0.0 | migration-step | Run migration microflow ACT_Assignee_Migration or add ASu_Assignee_Migrate to after startup to migrate assignee data. | ACT_Assignee_Migration, ASu_Assignee_Migrate, UserTaskView_Assignees |  |
| 3.0.0 | deprecation | UserTaskView_Assignee association is deprecated; use UserTaskView_Assignees instead. | UserTaskView_Assignee | UserTaskView_Assignees |
| 2.6.0 | requirement | Upgraded module to Mendix 9.24.0. |  |  |
| 2.6.0 | requirement | Updated Atlas Web Content compatibility to v3.4.1. | Atlas Web Content |  |
| 2.6.0 | requirement | Updated Atlas Core compatibility to v3.12.3. | Atlas Core |  |
| 2.5.0 | requirement | Upgraded module to Mendix 9.20.0. |  |  |
| 2.5.0 | requirement | Updated Refresh action to use Nanoflow Commons module; ensure Nanoflow Commons is imported when upgrading. | Nanoflow Commons |  |
| 2.4.0 | requirement | Upgraded module to Mendix 9.19.0. |  |  |
| 2.4.0 | breaking | Attachments outside comment scope must be part of own domain model and associated to workflow context entity. |  |  |
| 2.4.0 | breaking | Attachments in Workflow Commons are now optional part of comments; migration creates comment for each workflow. |  |  |
| 2.4.0 | migration-step | Execute migration microflow in Workflow Admin Center to link existing attachments to comments before viewing. |  |  |
| 2.4.0 | security | Fixed CVE-2022-46664; see security advisory at https://cert-portal.siemens.com/productcert/pdf/ssa-210822.pdf. |  |  |
| 2.3.2 | security | Fixed CVE-2022-46664; see security advisory at https://cert-portal.siemens.com/productcert/pdf/ssa-210822.pdf. |  |  |
| 2.3.1 | requirement | Updated Charts module compatibility to version 3.0.1. | Charts |  |
| 2.3.0 | breaking | Moved Workflow Definition View page from Workflow dashboard to Workflow management. |  |  |
| 2.3.0 | requirement | Updated Charts module compatibility to version 3.0.0. | Charts |  |
| 2.3.0 | requirement | Updated Data Widgets module compatibility to version 2.5.4. | Data Widgets |  |
| 2.2.1 | requirement | Updated Charts module compatibility to version 3.0.0. | Charts |  |
| 2.2.1 | requirement | Upgraded module to Mx 9.16.1. |  |  |
| 2.2.0 | requirement | Updated Data Widgets module compatibility to version 2.5.3. | Data Widgets |  |
| 2.1.4 | security | Fixed CVE-2022-46664; see security advisory at https://cert-portal.siemens.com/productcert/pdf/ssa-210822.pdf. |  |  |
| 2.1.2 | requirement | Updated Data Widgets module compatibility to version 2.5.0. | Data Widgets |  |
| 2.1.0 | requirement | Updated module to use state change events for Workflow introduced in Mendix 9.12.0; requires 9.12.0 or higher. |  |  |
| 2.1.0 | migration-step | Requires set-up of event microflows in App Settings; follow steps in Readme snippet included in module. |  |  |
| 2.0.1 | requirement | Updated Data Widgets module to version 2.3.0. | Data Widgets |  |
| 2.0.0 | requirement | Workflow Commons now requires Mendix 9.10.0 or higher due to Workflow changes. |  |  |
| 2.0.0 | removal | Removed the 'Task Dashboard' page and template. Will be re-introduced in later releases. | Task Dashboard page, Task Dashboard template |  |
| 2.0.0 | removal | Removed the 'My Initiated Workflows' page and template. Will be re-introduced in later releases. | My Initiated Workflows page, My Initiated Workflows template |  |
| 2.0.0 | removal | Removed the 'Activity Timeline' snippets. | Activity Timeline snippets |  |
| 2.0.0 | removal | Removed the tabs and columns related to completed tasks from the Task Inbox. | Task Inbox |  |
| 2.0.0 | removal | Removed metrics related to completed tasks from the Workflow Dashboard. | Workflow Dashboard |  |
| 2.0.0 | requirement | Updated Data Widgets module dependency to v2.2.2. | Data Widgets |  |
| 1.4.1 | requirement | Updated Data Widgets module compatibility to version 2.1.1. | Data Widgets |  |
| 1.4.0 | requirement | Updated support for DataWidgets 2.0.2. | Data Widgets |  |
| 1.4.0 | requirement | Updated support for administration module V2.0.1. | Administration module |  |
| 1.3.0 | requirement | Upgraded to Mendix 9.6. |  |  |
| 1.3.0 | removal | Removed Mendix SSO dependency. Workflow Commons now relies on Administration module for account details. | Mendix SSO | Administration module |
| 1.3.0 | breaking | Renamed usage of 'Instance' as the system module workflow entities since 9.6 will not append that anymore. |  |  |
| 1.3.0 | requirement | Module now requires the Administration module. | Administration module |  |
| 1.3.0 | requirement | Module now relies on DataWidgets instead of DataGrid as Data Grid 2 has moved to that module. | Data Widgets, DataGrid | Data Widgets |
| 1.2.1 | requirement | Strongly advised to update Data grid 2 module to version 1.2.0+. | Data grid 2 |  |
| 1.2.0 | requirement | Updated minimum required Mendix version to 9.3.0. |  |  |

## Workflow Extension module <a id="117678"></a>
Module, Mendixmagic, Community, [marketplace](https://marketplace.mendix.com/link/component/117678)

| version | published | min Mendix |
|---|---|---|
| 2.0.0 | 2021-10-25 | 9.4.0 |
| 1.0.0 | 2021-06-11 | 9.2.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.0.0 | known-issue | Version 2.0.0 does not support workflows as redesigned in Mendix 9.6. Version 3 planned for Q1 2022. |  |  |

## Workstation Client <a id="247448"></a>
Service, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/247448)

| version | published | min Mendix |
|---|---|---|
| 4.2.1 | 2026-09-15 | 9.24.11 |
| 4.2.0 | 2026-09-10 | 9.24.11 |
| 4.1.0 | 2026-08-13 | 9.24.11 |
| 4.0.0 | 2026-07-16 | 9.24.11 |
| 3.8.0 | 2026-06-18 | 9.24.11 |
| 3.7.0 | 2026-05-21 | 9.24.11 |
| 3.6.0 | 2026-04-23 | 9.24.11 |
| 3.5.0 | 2026-03-12 | 9.24.11 |
| 3.4.0 | 2026-02-12 | 9.24.11 |
| 3.3.0 | 2026-01-08 | 9.24.11 |
| 3.2.0 | 2025-12-04 | 9.24.11 |
| 3.1.0 | 2025-11-07 | 9.24.11 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 4.1.0 | improvement | Client now sends detailed installation information (Client Type) to Management system for better deployment visibility. |  |  |
| 4.1.0 | improvement | Refactored device management to ensure consistent reporting of status as available, connected, or in error state. |  |  |
| 4.0.0 | fix | Fixed non-UTF-8 delimiter/suffix encoding issues in serial, TCP-IP client, and TCP-IP server devices. | serial devices, TCP-IP client, TCP-IP server devices |  |
| 3.6.0 | improvement | Updated underlying dependencies for smart card reader functionality, enhancing stability and compatibility. | smart card reader |  |
| 3.1.0 | fix | Fixed Workstation Client connection to Management over networks requiring certificates using OS certificates. |  |  |

## Workstation Client Linux ARM64 <a id="247459"></a>
Service, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/247459)

| version | published | min Mendix |
|---|---|---|
| 4.2.1 | 2026-09-15 | 9.24.11 |
| 4.2.0 | 2026-09-10 | 9.24.11 |
| 4.1.0 | 2026-08-13 | 9.24.11 |
| 4.0.0 | 2026-07-16 | 9.24.11 |
| 3.8.0 | 2026-06-18 | 9.24.11 |
| 3.7.0 | 2026-05-21 | 9.24.11 |
| 3.6.0 | 2026-04-23 | 9.24.11 |
| 3.5.0 | 2026-03-12 | 9.24.11 |
| 3.4.0 | 2026-02-12 | 9.24.11 |
| 3.3.0 | 2026-01-08 | 9.24.11 |
| 3.2.0 | 2025-12-04 | 9.24.11 |
| 3.1.0 | 2025-11-07 | 9.24.11 |
| 3.0.0 | 2025-09-30 | 9.24.11 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 4.2.0 | known-issue | The Keyboard wedge connector is not supported on the Workstation Client for Linux ARM64 | Keyboard wedge connector |  |
| 4.0.0 | fix | Fixed issues with non-UTF-8 delimiter/suffix encoding in serial, TCP-IP client, and TCP-IP server devices, ensuring reliable data transmission | Serial/TCP-IP, delimiter/suffix encoding |  |
| 3.6.0 | improvement | We've updated the underlying dependencies for the smart card reader functionality, enhancing stability and compatibility | smart card reader dependencies |  |
| 3.2.0 | improvement | Spaces have been removed from the Workstation Client Linux ARM64 version executable name for improved consistency | Linux ARM64, executable name |  |

## Workstation Client macOS <a id="253905"></a>
Service, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/253905)

| version | published | min Mendix |
|---|---|---|
| 4.2.1 | 2026-09-15 | 9.24.11 |
| 4.2.0 | 2026-09-10 | 9.24.11 |
| 4.1.0 | 2026-08-13 | 9.24.11 |
| 4.0.0 | 2026-07-16 | 9.24.11 |
| 3.8.0 | 2026-06-22 | 9.24.11 |
| 3.7.0 | 2026-05-21 | 9.24.11 |
| 3.6.0 | 2026-04-23 | 9.24.11 |
| 3.5.0 | 2026-03-12 | 9.24.11 |
| 3.4.0 | 2026-02-12 | 9.24.11 |
| 3.3.0 | 2026-01-19 | 9.24.11 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 4.0.0 | fix | Fixed issues with non-UTF-8 delimiter/suffix encoding in serial, TCP-IP client, and TCP-IP server devices | Serial/TCP-IP Encoding, serial devices, TCP-IP client, TCP-IP server devices |  |
| 3.8.0 | fix | Fixed issue where client blocked sign-in to Studio Pro when six or more devices were configured due to port overlap | Studio Pro Login |  |
| 3.6.0 | requirement | Updated underlying dependencies for smart card reader functionality, enhancing stability and compatibility | smart card reader dependencies |  |
| 3.4.0 | fix | BLE characteristics and services are no longer case-sensitive and now accept standard UUID formats with dashes | BLE characteristics, BLE services |  |

## Workstation Client Portable <a id="247456"></a>
Service, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/247456)

| version | published | min Mendix |
|---|---|---|
| 4.2.1 | 2026-09-15 | 9.24.11 |
| 4.2.0 | 2026-09-10 | 9.24.11 |
| 4.1.0 | 2026-08-13 | 9.24.11 |
| 4.0.0 | 2026-07-16 | 9.24.11 |
| 3.8.0 | 2026-06-18 | 9.24.11 |
| 3.7.0 | 2026-05-21 | 9.24.11 |
| 3.6.0 | 2026-04-23 | 9.24.11 |
| 3.5.0 | 2026-03-12 | 9.24.11 |
| 3.4.0 | 2026-02-12 | 9.24.11 |
| 3.3.0 | 2026-01-08 | 9.24.11 |
| 3.2.0 | 2025-12-04 | 9.24.11 |
| 3.1.0 | 2025-11-07 | 9.24.11 |
| 3.0.0 | 2025-09-30 | 9.24.11 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 4.1.0 | improvement | Client now sends detailed installation information (Client Type) to the Management system, providing better visibility into your deployment | client reporting, Management system |  |
| 4.1.0 | improvement | Refactored how devices are managed to ensure they consistently report their status as available, connected, or in an error state | device states, management |  |
| 4.0.0 | feature | Workstation Client now generates and sends an anonymized Client ID, derived from the machine's hardware/OS identifier, to the Management server | Client ID Reporting |  |
| 4.0.0 | feature | Workstation Client can now connect to multiple devices over a single WebSocket connection, improving efficiency and reducing overhead | WebSocket Connection |  |
| 4.0.0 | feature | Client now supports the new SendDeviceRequest API, allowing for more direct and streamlined communication with devices | SendDeviceRequest API |  |
| 4.0.0 | fix | Fixed issues with non-UTF-8 delimiter/suffix encoding in serial, TCP-IP client, and TCP-IP server devices, ensuring reliable data transmission | Serial, TCP-IP client, TCP-IP server |  |
| 3.8.0 | fix | Fixed an issue where the client blocked sign-in to Studio Pro when six or more devices were configured, due to an overlap in port usage | Studio Pro Login, port usage |  |
| 3.6.0 | improvement | Updated the underlying dependencies for the smart card reader functionality, enhancing stability and compatibility | smart card reader, dependencies |  |
| 3.1.0 | fix | Fixed an issue where the Workstation Client could not connect to Workstation Management over a network connection that required a certificate. Client now uses the operating system's certificates | Computer registration, certificate |  |

## Workstation Commons <a id="305490"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/305490)

| version | published | min Mendix |
|---|---|---|
| 4.2.1 | 2026-09-15 | 10.21.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 4.2.1 | fix | Included missing sticky scroll widget snippet dependency. | sticky scroll widget |  |

## Workstation Commons (Mx 9) <a id="305502"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/305502)

| version | published | min Mendix |
|---|---|---|
| 4.2.1 | 2026-09-15 | 9.24.11 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 4.2.1 | fix | Included missing sticky scroll widget snippet dependency. | sticky scroll widget |  |

## Workstation Connector <a id="254335"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/254335)

| version | published | min Mendix |
|---|---|---|
| 4.2.0 | 2026-09-10 | 10.21.1 |
| 4.1.0 | 2026-08-13 | 10.21.1 |
| 4.0.0 | 2026-07-16 | 10.21.1 |
| 3.8.0 | 2026-06-18 | 10.21.1 |
| 3.6.0 | 2026-04-23 | 10.21.1 |
| 3.3.0 | 2026-01-23 | 10.21.1 |
| 3.2.0 | 2026-01-23 | 10.21.1 |
| 3.1.0 | 2026-01-23 | 10.21.1 |
| 3.0.0 | 2026-01-23 | 10.21.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 4.1.0 | fix | Fixed an issue that occasionally prevented the connector from successfully reconnecting to devices after Workstation Client downtime. | Connection stability |  |
| 4.0.0 | feature | Workstation Connector now supports communication over a single WebSocket connection, enhancing performance and simplifying network configurations. | WebSocket Communication |  |
| 4.0.0 | feature | New SendDeviceRequest JSA introduced. Returns device response or error directly, not passed to onMessage channel. Requires Workstation Client 4.0 or later. | SendDeviceRequest JSA |  |
| 4.0.0 | requirement | SendDeviceRequest JSA requires Workstation Client 4.0 or later for full utilization. | Workstation Client |  |
| 3.8.0 | breaking | Get/Create Device action now returns an empty object instead of throwing an error when no matching device is found. | Get/Create Device action |  |
| 3.6.0 | feature | New GetCreateDevice action to initialize and manage peripheral object creation in one single action. | GetCreateDevice, Initialize peripheral object |  |
| 3.6.0 | feature | Setup callbacks: On connect, On message, On disconnect to manage peripheral object events. | On connect, On message, On disconnect |  |
| 3.6.0 | feature | New widgets to trigger application level logic on device events: On change, On equal, On true, On load/unload actions. | On change, On equal, On true, On load/unload |  |
| 3.6.0 | feature | New SubscribeToObjectChanges JSA nanoflow action to react to object changes in real-time. | SubscribeToObjectChanges JSA |  |
| 3.6.0 | feature | New WaitForObjectChanges JSA nanoflow action to wait for specific object changes before proceeding. | WaitForObjectChanges JSA |  |
| 3.6.0 | feature | New Connect device nanoflow action for managing device connections. | Connect device |  |
| 3.6.0 | feature | New SendDeviceMessage and WaitForDeviceMessage nanoflow actions for easier configuration of most used cases. | SendDeviceMessage, WaitForDeviceMessage | SendMessage |
| 3.6.0 | improvement | Model peripheral entity as specialization of device entity; no association required. | peripheral entity, device entity |  |
| 3.6.0 | improvement | Calling GetStation is not required anymore to initiate station connector; only required for reading station configuration. | GetStation |  |
| 3.6.0 | deprecation | SendMessage deprecated; its wait for response behavior was misleading or unnecessary. Replaced by SendDeviceMessage and WaitForDeviceMessage. | SendMessage | SendDeviceMessage |
| 3.6.0 | deprecation | SubscribeToMessages and SubscribeToErrors deprecated and replaced by GetCreateDevice. | SubscribeToMessages, SubscribeToErrors | GetCreateDevice |
| 3.6.0 | breaking | Removed Station_User association. Object garbage collection now handled internally for more robust object management. | Station_User association |  |
| 3.6.0 | fix | Fixed an issue related to the timing of initial connections. | initial connections |  |
| 3.6.0 | fix | Fixed an issue when devices were sometimes discovered with a delay. | device discovery |  |

## Workstation Connector (Mx 9) <a id="247460"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/247460)

| version | published | min Mendix |
|---|---|---|
| 4.2.0 | 2026-09-10 | 9.24.11 |
| 4.1.0 | 2026-08-13 | 9.24.11 |
| 4.0.0 | 2026-07-16 | 9.24.11 |
| 3.8.0 | 2026-06-18 | 9.24.11 |
| 3.6.0 | 2026-04-23 | 9.24.11 |
| 3.3.0 | 2026-01-08 | 9.24.11 |
| 3.2.0 | 2025-12-04 | 9.24.11 |
| 3.1.0 | 2025-11-07 | 9.24.11 |
| 3.0.0 | 2025-09-30 | 9.24.11 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 4.0.0 | feature | Workstation Connector now supports communication over a single WebSocket connection, enhancing performance. |  |  |
| 4.0.0 | feature | New SendDeviceRequest JSA introduced. Returns device response or error directly; requires Workstation Client 4.0 or later. | SendDeviceRequest JSA |  |
| 3.8.0 | breaking | Get/Create Device action now returns empty object instead of throwing error when no matching device found. | Get/Create Device action |  |
| 3.6.0 | feature | New set of Nanoflow Actions and Widget to simplify creation of reusable peripheral modules. | GetCreateDevice, SubscribeToObjectChanges JSA, WaitForObjectChanges JSA |  |
| 3.6.0 | feature | New nanoflow actions: Connect device, SendDeviceMessage, WaitForDeviceMessage for easier configuration. | Connect device, SendDeviceMessage, WaitForDeviceMessage |  |
| 3.6.0 | improvement | Model peripheral entity as specialization of device entity; no need for association. |  |  |
| 3.6.0 | improvement | Calling GetStation is not required anymore to initiate station connector; only required for reading configuration. | GetStation |  |
| 3.6.0 | deprecation | SendMessage has been deprecated; its wait for response behavior was often misleading or unnecessary. | SendMessage | SendDeviceMessage and WaitForDeviceMessage |
| 3.6.0 | deprecation | SubscribeToMessages and SubscribeToErrors deprecated; replaced by single action GetCreateDevice. | SubscribeToMessages, SubscribeToErrors | GetCreateDevice |
| 3.6.0 | breaking | Removed Station_User association; object garbage collection now handled internally for robust object management. | Station_User association |  |

## XSUAA Connector for SAP Solutions <a id="78091"></a>
Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/78091)

| version | published | min Mendix |
|---|---|---|
| 4.0.1 | 2025-12-03 | 10.21.0 |
| 4.0.0 | 2025-06-30 | 10.21.0 |
| 3.2.1 | 2025-12-03 | 9.24.33 |
| 3.2.0 | 2025-05-06 | 9.24.33 |
| 3.1.1 | 2025-03-28 | 9.24.4 |
| 3.1.0 | 2024-07-03 | 9.24.4 |
| 3.0.1 | 2023-05-18 | 9.24.0 |
| 3.0.0 | 2023-03-30 | 9.24.0 |
| 2.1.9 | 2022-11-15 | 8.18.10 |
| 2.1.8 | 2022-07-28 | 8.18.10 |
| 2.1.7 | 2022-06-15 | 8.18.10 |
| 2.1.6 | 2022-04-05 | 8.18.10 |
| 2.1.5 | 2022-03-09 | 8.18.10 |
| 2.1.4 | 2021-12-13 | 8.18.10 |
| 2.1.3 | 2021-05-27 | 8.15.1 |
| 2.1.2 | 2020-12-07 | 8.15.1 |
| 2.1.1 | 2020-11-12 | 8.9.0 |
| 2.1.0 | 2020-07-28 | 8.9.0 |
| 2.0.0 | 2019-08-12 | 7.23.3 |
| 1.1.5 | 2018-06-13 | 7.5.1 |
| 1.1.4 | 2018-06-05 | 7.5.1 |
| 1.1.3 | 2017-09-14 | 7.5.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 4.0.1 | security | Security vulnerabilities have been identified and fixed |  |  |
| 4.0.0 | requirement | Upgraded to Mx10.21, requiring Mendix 10.21.0 or higher |  |  |
| 3.2.1 | security | Security vulnerabilities have been identified and fixed |  |  |
| 3.2.0 | requirement | Released on Mx v9.24.33, requiring Mendix 9.24.33 or higher |  |  |
| 3.0.0 | requirement | Upgraded to Mendix v9.24.0, requiring Mendix 9.24.0 or higher |  |  |
| 2.1.9 | improvement | Upgraded jars to newer version |  |  |
| 2.1.8 | improvement | Added compatibility with the updated DeepLink module | DeepLink module |  |
| 2.1.6 | security | Upgraded jars for vulnerability fix |  |  |
| 2.1.5 | removal | Removed unwanted jars |  |  |
| 2.1.4 | requirement | Upgraded to Mendix Studio Pro v8.18.10 |  |  |
| 2.1.4 | removal | Removed some unused libs |  |  |
| 2.1.3 | security | Removed few security issues |  |  |
| 2.1.2 | requirement | Upgraded to Mendix Studio Pro version 8.15.1 |  |  |
| 2.1.1 | breaking | Unlinked from MendixSSO module | MendixSSO module |  |
| 2.1.0 | removal | Remove dependency over Administration module | Administration module |  |
| 2.0.0 | requirement | Updated framework to Mendix 7.23.3 to support Mendix 8 |  |  |

## Yaml - JSON Converter <a id="116991"></a>
Module, Emixa, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/116991)

| version | published | min Mendix |
|---|---|---|
| 1.0.0 | 2021-03-24 | 8.14.1 |

## Zuora Connector <a id="114782"></a>
Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/114782)

| version | published | min Mendix |
|---|---|---|
| 3.0.1 | 2024-07-16 | 9.24.24 |
| 3.0.0 | 2024-07-06 | 9.24.23 |
| 2.3.0 | 2024-01-12 | 9.24.14 |
| 2.2.2 | 2024-01-10 | 9.24.14 |
| 2.1.2 | 2023-12-21 | 9.24.12 |
| 2.1.1 | 2023-12-20 | 9.24.12 |
| 2.1.0 | 2023-12-19 | 9.24.12 |
| 2.0.1 | 2023-04-21 | 9.24.1 |
| 2.0.0 | 2023-02-17 | 9.18.4 |
| 1.3.0 | 2022-12-02 | 9.6.14 |
| 1.2.0 | 2021-06-07 | 8.18.6 |
| 1.1.1 | 2021-06-01 | 8.6.9 |
| 1.1.0 | 2020-08-07 | 8.6.5 |
| 1.0.0 | 2020-08-05 | 8.6.5 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 3.0.1 | breaking | zObject updated_time and created_time are now date time attributes | zObject.updated_time, zObject.created_time |  |
| 3.0.0 | breaking | Migrated majority of domain model and actions to V2 API with different naming conventions; entities and attributes renamed or deleted |  |  |
| 3.0.0 | requirement | Upgrade to Mendix 9.24.23 |  |  |
| 2.3.0 | migration-step | json-20200518.jar.zuoraconnector.RequiredLib no longer required as of 2.2.0; delete from userlib if unused | json-20200518.jar.zuoraconnector.RequiredLib |  |
| 2.2.2 | breaking | Removed wrapper entities; deleted OrderActions, Subscriptions, CustomField, SubscriptionRatePlan entities | OrderActions, Subscriptions, CustomField, SubscriptionRatePlan |  |
| 2.2.2 | breaking | Renamed OrderActionWrapper entity to Array | OrderActionWrapper | Array |
| 2.2.2 | breaking | Changed return value for SUB_Contact_Create and SUB_Contact_Update to Contact instead of ZuoraResponse | SUB_Contact_Create, SUB_Contact_Update |  |
| 2.2.2 | breaking | Renamed some microflow actions to better reflect the objects involved |  |  |
| 2.0.1 | requirement | Upgraded to Mendix 9.24.1 |  |  |
| 2.0.0 | breaking | Refactored module and logic; upgrading can break existing implementation |  |  |
| 2.0.0 | requirement | Upgraded to Mendix 9.18.4 |  |  |
| 1.3.0 | security | Added encryption to Authorization Token and removed read access for improved security | Authorization Token |  |
| 1.2.0 | requirement | Upgraded to Mendix 8.18.6 |  |  |
