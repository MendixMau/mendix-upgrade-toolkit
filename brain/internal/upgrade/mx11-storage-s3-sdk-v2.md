---
title: "Mx11: S3 storage moved to AWS SDK v2 and now requires an explicit region"
topic: upgrade
keywords: ["S3 storage region required", "AWS SDK v2 upgrade", "com.mendix.storage.s3.Region", "UseV2Auth deprecated", "Mendix 11.6.0 S3", "Signature v2 not supported", "S3 configuration", "AWS SDK migration", "storage region setting", "Mendix 11 upgrade"]
domain: [upgrade, data-modeling]
kind: pitfall
applies_to: mendix-general
versions: "11.6.0 and later"
layer: field
sources:
  - {title: "Upgrading from Mendix Studio Pro 10 to 11", url: "https://docs.mendix.com/refguide/upgrading-from-10-to-11/", date: "2026-09-15"}
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed

---
**What changes:** S3 storage moved to AWS SDK v2 and now requires an explicit region. Category: platform or configuration change. Severity in the catalog: blocker.

**Applies:** from Mendix 11.6.0 on. Affects: project.

**Status:** will break (catalog: certain).

**How to find it:** manual review (cannot be detected automatically); detection confidence high.

**Fix:** Set com.mendix.storage.s3.Region to the bucket's region in every environment, and stop relying on the UseV2Auth signature-v2 setting.

**Source quotes:**

- "In Mendix 11.6.0 we upgraded the AWS SDK used for accessing S3 storage from version 1 to version 2." ([Upgrading from Mendix Studio Pro 10 to 11](https://docs.mendix.com/refguide/upgrading-from-10-to-11/))
- "The `com.mendix.storage.s3.Region` setting must always be set to the region matching the region of the bucket." ([Upgrading from Mendix Studio Pro 10 to 11](https://docs.mendix.com/refguide/upgrading-from-10-to-11/))
- "SDK version 2 does not support AWS Signature v2 which is enabled by `UseV2Auth` setting." ([Upgrading from Mendix Studio Pro 10 to 11](https://docs.mendix.com/refguide/upgrading-from-10-to-11/))
