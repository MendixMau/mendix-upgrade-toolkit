# Conversational UI (Marketplace component 239450)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

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
