---
title: "Mx11: com.mendix.modules.email.EmailModule was removed"
topic: upgrade
keywords: ["com.mendix.modules.email.EmailModule", "EmailModule removed", "Mendix 11 email module", "MX11-JAVA-EMAIL-MODULE", "email module removed", "Email Connector", "Mx11 upgrade email", "runtime email module", "removed EmailModule", "email breaking change"]
domain: [upgrade, architecture]
kind: pitfall
applies_to: mendix-general
versions: "11.1.0 and later"
layer: field
sources:
  - {title: "Studio Pro 11.1 release notes", url: "https://docs.mendix.com/releasenotes/studio-pro/11.1/", date: "2026-09-15"}
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed

---
**What changes:** com.mendix.modules.email.EmailModule was removed. Category: removed in Mendix 11. Severity in the catalog: blocker.

**Applies:** from Mendix 11.1.0 on. Affects: java.

**Status:** will break (catalog: certain).

**How to find it:** automatic, by a pattern search over the app's code; detection confidence high.

**Fix:** Replace the removed runtime email module with a supported Marketplace email module such as the Email Connector.

**False positives:** Matches the fully qualified runtime class only, so an app's own EmailModule class or a Marketplace module of the same name will not trigger it.

**Source quotes:**

- "We removed `com.mendix.modules.email.EmailModule` as it is no longer supported." ([Studio Pro 11.1 release notes](https://docs.mendix.com/releasenotes/studio-pro/11.1/))
