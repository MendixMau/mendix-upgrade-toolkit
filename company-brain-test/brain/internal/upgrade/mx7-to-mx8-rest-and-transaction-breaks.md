---
title: Mx7 to Mx8 breaks REST Services module use and changes transaction/error-handler behavior
topic: upgrade
domain: [integration, delivery-process]
kind: pitfall
applies_to: mendix-general
versions: "Mx7 -> Mx8 (obsolete path, still relevant for legacy apps)"
keywords: ["REST Services module", "Mx7 to Mx8 migration", "Call REST Service", "transaction behavior change", "custom error handler", "HttpRequest HttpResponse", "commit errors", "microflow transaction", "REST module deprecated", "published REST GET", "query path parameters", "upgrade Mx8"]
layer: field
sources:
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed
---
**Symptom**
- The REST Services module does not work in Mx8.
- Some microflows that worked in Mx7 fail at runtime or behave differently. This can surface during hypercare or much later.

**Root cause**
- The REST Services module is not supported in Mx8.
- Microflow transaction execution changed from 7 to 8.
- Objects created before a custom error handler (or committed in another transaction) now cause commit errors.

**Fix**
- Replace every REST Services module activity with "Call REST Service" plus the System entities `HttpRequest`, `HttpResponse` and `HttpHeader`.
- Effort grows with the number of operations.
- Published REST GET microflows now need one primitive parameter per query/path parameter. Before, they took an entity.
- Re-assert in the microflow any defaults, constraints and validations the Mx7 entity used to impose.
- Refactor to best practice these typical offenders:
  - request logging that creates a log object before a "Custom with…" handler and commits it on the OK or error leg;
  - commits, changes with commit, or deletes inside published REST handling and flat file import/export.

**Status**
- The source is a field upgrade guide. It lists these as hallmark Mx7 → Mx8 considerations. It does not say they are confirmed in the field or fixed in any version.
- The workaround is the refactoring described above.
- The source's theme-conversion section is empty ("TBC").
