# AI Bot Starter App (Marketplace component 227926)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

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
