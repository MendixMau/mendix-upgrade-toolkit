# PgVector Knowledge Base (Marketplace component 225063)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

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
