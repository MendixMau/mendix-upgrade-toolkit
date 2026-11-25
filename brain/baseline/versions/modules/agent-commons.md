# Agent Commons (Marketplace component 240371)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

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
