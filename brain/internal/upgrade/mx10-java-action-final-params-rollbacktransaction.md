---
title: Mx10 Java compile errors from final action parameters and removed rollbackTransAction
topic: upgrade
domain: [integration, delivery-process]
kind: pitfall
applies_to: mendix-general
versions: "Mx9 -> Mx10"
keywords: ["cannot assign final variable", "final action parameters", "rollbackTransAction", "rollbackTransaction", "Java compile errors", "Mx10 upgrade", "Community Commons", "Object Handling", "IContext method", "cannot find symbol"]
layer: field
sources:
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed
---
**Symptom**
- After converting to Mx10, Java fails to compile with:
  - `cannot assign a value to final variable`;
  - `cannot find symbol: method rollbackTransAction()`.
- Typically seen in old Community Commons and Object Handling versions.

**Root cause**
- Mx10 generates Java action parameters as `final`. Old code reassigns them.
- `IContext.rollbackTransAction()` is gone. Use `rollbackTransaction()`.

**Fix**
- Update Community Commons and Object Handling to the latest versions.
- In custom Java, copy parameters into local variables before changing them.
- Rename calls to `rollbackTransaction()`.

**Status**
- Workaround: update the Marketplace modules and adjust custom Java as above. Listed as a known Mx9 → Mx10 breaking change in an upgrade triage checklist. No specific field run or version pair is recorded.
