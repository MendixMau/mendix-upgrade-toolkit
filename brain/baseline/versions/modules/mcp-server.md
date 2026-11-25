# MCP Server (Marketplace component 240380)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/240380)

| version | published | min Mendix |
|---|---|---|
| 5.3.0 | 2026-09-25 | 11.12.4 |
| 5.2.0 | 2026-08-31 | 11.12.3 |
| 5.1.0 | 2026-07-22 | 11.12.1 |
| 5.0.0 | 2026-07-02 | 11.12.0 |
| 4.1.1 | 2026-04-28 | 10.24.13 |
| 4.0.0 | 2026-01-19 | 10.24.13 |
| 3.2.0 | 2026-01-02 | 10.24.13 |
| 3.1.0 | 2025-10-15 | 10.24.0 |
| 3.0.0 | 2025-08-13 | 10.24.0 |
| 2.1.1 | 2025-07-22 | 10.21.1 |
| 2.0.0 | 2025-06-26 | 10.21.1 |
| 1.0.0 | 2025-04-25 | 10.21.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 5.3.0 | breaking | Integer parameters of tools now declared as integers in automatic schema creation (previously: numbers). | tools, schema creation |  |
| 5.3.0 | security | Fixed bug where unauthorized requests came through without user context. Smaller request handling changes implemented. | request handling, user context |  |
| 5.3.0 | requirement | MCP Server path validation: no support for additional path segments (no / allowed in path). | MCP Server path |  |
| 5.2.0 | requirement | Upgraded to Mendix 11.12.3. | Mendix |  |
| 5.2.0 | improvement | Setting Authentication Microflow during server initialization is now optional (previously required). | Authentication Microflow |  |
| 5.1.0 | requirement | Upgraded to Mendix 11.12.1. | Mendix |  |
| 5.1.0 | fix | Fixed bug affecting MCP Server creation during after-startup logic due to Root URL fetch failure. | MCP Server, Root URL |  |
| 5.0.0 | requirement | Module upgraded to Mendix 11.12. | Mendix |  |
| 5.0.0 | feature | MCP Server endpoint is now part of object and gets logged in console. | MCP Server, endpoint |  |
| 4.1.1 | security | Changed jackson library dependency declaration for automatic updates, fixing severe vulnerability. | jackson library |  |
| 4.0.0 | breaking | Added Streamable HTTP transport support. Legacy HTTP+SSE transport v2024-11-05 no longer available. | HTTP transport, protocol version |  |
| 4.0.0 | fix | Fixed issue where Mendix/MCP session was not reused with authentication enabled, causing session limit errors. | Mendix session, MCP session, authentication |  |
| 4.0.0 | fix | Fixed bug blocking multiple servers running in same Mendix app; last started server no longer overwrites previous tools. | multiple servers |  |
| 4.0.0 | requirement | MCP server paths validated; path cannot be 'mcp'. | MCP server path |  |
| 3.2.0 | requirement | MCP SDK version upgraded to 0.16.0. | MCP SDK |  |
| 3.2.0 | improvement | Thread sleep setting removed from request handler; now handled by Studio Pro Runtime. | request handler |  |
| 3.1.0 | feature | User and session now in scope of tool and prompt microflows for role/user-based access control. | tool microflows, prompt microflows, user, session |  |
| 3.0.0 | requirement | MCP Java SDK version upgraded to 0.11.1. | MCP Java SDK |  |
| 3.0.0 | requirement | Module upgraded to Mendix Studio Pro version 10.24. | Mendix |  |
| 2.1.0 | feature | Schema input for AddTool action now optional; auto-created from microflow input or overwritten if provided. | AddTool, schema |  |
| 2.0.0 | feature | MCP Server now accepts optional authentication microflow executed on client connection for custom auth methods. | MCP Server, authentication microflow |  |
| 2.0.0 | requirement | MCP Server creation now requires specifying MCP version; currently only 2024_11_05 allowed. | MCP Server, MCP version |  |
