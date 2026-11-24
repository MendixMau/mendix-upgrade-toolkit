---
title: Java API rewrites needed to compile on Mx11
topic: upgrade
domain: [integration, delivery-process]
kind: reference
applies_to: mendix-general
versions: "Mx10 -> Mx11 (field runs on 11.9.1 and 11.12)"
keywords: ["Mx10 to Mx11 upgrade", "Java API rewrite", "retrieveXPathQuery", "createXPathQuery", "isSubClassOf", "IMendixIdentifier", "getEntityId", "getContext", "CustomJavaAction", "UserAction", "RuntimeVersion", "Core.getRuntimeVersion"]
layer: field
sources:
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed
---
| Old (Mx10) | Mx11 |
|---|---|
| `Core.retrieveXPathQuery(ctx, xp)` | `Core.createXPathQuery(xp).execute(ctx)` |
| `Core.isSubClassOf(name, obj.getType())` | `obj.getMetaObject().isSubClassOf(name)`, or `Core.getMetaObject(a).isSubClassOf(b)`. `IMetaObject.isSubClassOf(String)` takes an entity name; see MendixSSO 10.6.0 source. |
| `obj.getId().getEntityId()` (Short) | `obj.getId()` (`IMendixIdentifier`); change `List<Short>` to `List<IMendixIdentifier>` |
| `context()` / `this.context()` | `getContext()` |
| `com.mendix.webui.CustomJavaAction<T>` | `com.mendix.systemwideinterfaces.core.UserAction<T>` (see conflict below) |
| `RuntimeVersion.getInstance()` / `com.mendix.core.conf.RuntimeVersion` | `Core.getRuntimeVersion()`. Remove unused imports. |
| Business Events `schedulePublish` | Signature changed. Update the module. |

Field run (one app, 10.24 → 11.9.1):
- 45 Java errors across 8 modules. All were fixed by hand patches.
- The most common fix was `this.context()` → `getContext()`, done as a bulk replace.
- Marketplace updates did not help:
  - Modules packaged for older versions cannot be imported into Mx11 until opened in 10.21–10.24.99. The TcConnector case also had to go through 10.21–10.24.
  - Some publishers (JWT, ValidationFeedback) still used `this.context()` in their latest versions.
- Lesson: on Mx11, patching the Java source directly is faster than waiting for module updates.
- Incompatible widgets may throw errors. For a first run, turning off the React client got the project running.

Conflict:
- The same-day triage report said to move `CustomJavaAction` to `...core.JavaAction`.
- The journal's applied fix used `UserAction`. That is kept here as better evidenced.

**Release notes**
- 11.0.0 removed `Core.retrieveXPath…`, `Core.isSubClassOf`, `IMendixIdentifier#getEntityId`, `UserAction#context()` and `RuntimeVersion` (https://docs.mendix.com/releasenotes/studio-pro/11.0/#1100-general-availability)
