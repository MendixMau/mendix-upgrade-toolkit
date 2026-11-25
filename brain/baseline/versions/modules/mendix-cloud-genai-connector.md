# Mendix Cloud GenAI Connector (Marketplace component 239449)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

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
