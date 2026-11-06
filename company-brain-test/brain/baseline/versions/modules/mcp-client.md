# MCP Client (Marketplace component 244893)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

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
