# OpenAI Connector (Marketplace component 220472)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

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
