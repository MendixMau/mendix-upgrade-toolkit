# GenAI Commons (Marketplace component 239448)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

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
