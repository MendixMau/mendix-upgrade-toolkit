---
title: "Mx11: S3 client-side encryption now supports only AES"
topic: upgrade
keywords: ["S3 encryption", "AES only", "client-side encryption", "Mendix 11", "S3 client-side", "encryption algorithm", "AWS SDK v2", "MX11-STORAGE-S3-ENCRYPTION-AES-ONLY", "non-AES algorithm", "S3 configuration"]
domain: [upgrade, data-modeling]
kind: pitfall
applies_to: mendix-general
versions: "11.6.0 and later"
layer: field
sources:
  - {title: "Upgrading from Mendix Studio Pro 10 to 11", url: "https://docs.mendix.com/refguide/upgrading-from-10-to-11/", date: "2026-09-19"}
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed

---
**What changes:** S3 client-side encryption now supports only AES. Category: behaviour change. Severity in the catalog: high.

**Applies:** from Mendix 11.6.0 on. Affects: project.

**Status:** will break (catalog: certain).

**How to find it:** manual review (cannot be detected automatically); detection confidence high.

**Fix:** If S3 client-side encryption is configured with a non-AES algorithm, switch it to AES before upgrading -- part of the same AWS SDK v1-to-v2 migration as MX11-STORAGE-S3-SDK-V2.

**Source quotes:**

- "only AES is supported" ([Upgrading from Mendix Studio Pro 10 to 11](https://docs.mendix.com/refguide/upgrading-from-10-to-11/))

**Related catalog entries:** MX11-STORAGE-S3-SDK-V2.
