# GenAI For Mendix (Mx 9) (Marketplace component 227931)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

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
