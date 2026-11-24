---
title: Agents Kit 2 upgrade blocked for OpenAI apps; Agent Editor supports only Mendix Cloud GenAI
topic: upgrade
domain: [ai-agents]
kind: pitfall
applies_to: mendix-general
versions: "Agents Kit 1 -> 2 (as of 2026-08)"
keywords: ["Agents Kit 2", "Agent Editor", "Mendix Cloud GenAI only", "OpenAI provider", "AgentCommons 4.0.0", "GenAICommons 7.0.0", "SingleMCPTool migration", "MCPServerConfiguration renamed ConsumedMCPService", "Agents Kit 1 migration flows", "knowledge base migration"]
layer: field
sources:
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed
---
**Symptom**
- An app on OpenAI could not take Agents Kit 2 (AgentCommons, ConversationalUI, GenAICommons, MCPClient, MCPServer, OpenAIConnector) during its Mx11 upgrade.

**Root cause**
- Agents Kit 2 includes the Agent Editor. Per its docs, it currently supports only Mendix Cloud GenAI as provider; others such as OpenAI are planned.

**Fix**
- Stay on Agents Kit 1 and keep the Agents Kit 2 upgrade out of the Mx11 scope.
- Before Kit 2, check whether the Kit 1 migration flows are needed:
  - only if agent definitions contain Single MCP tools (`MCPServerConfiguration` renamed to `ConsumedMCPService`, new `SingleMCPTool_ConsumedMCPService` association);
  - or if the app uses knowledge bases from the affected modules.

**Status**
- Decision in one app's upgrade plan, based on docs at the time. Not tested.
