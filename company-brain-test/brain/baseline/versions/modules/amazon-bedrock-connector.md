# Amazon Bedrock Connector (Marketplace component 215042)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

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
