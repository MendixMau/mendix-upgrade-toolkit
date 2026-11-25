---
title: Choosing a starting Studio Pro version and when to upgrade
topic: upgrade
domain: [delivery-process]
kind: decision
applies_to: company-standard
versions: "all (examples from 9.24 / 10.x era)"
keywords: ["Studio Pro upgrade", "LTS release", "MTS release", "version selection", "production deployment", "go-live", "major version", "regression testing", "supported release", "Marketplace dependencies", "upgrade strategy"]
layer: field
sources:
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed
---
**Rule**
- Production apps run on an LTS or MTS release, preferably the latest one.
- Upgrade to the latest LTS/MTS before every go-live, and run a regression test.

**Why**
- It avoids a major upgrade mid-project while still landing on a supported release at launch.
- Very early majors (x.0) may still have startup issues.

**How to apply**
- If the next MTS will ship before go-live (about 4 months or more of development), start on a recent non-MTS of the new major. Example: 10.2, with 10.6 MTS expected before launch.
- If development is shorter than that, start on the current LTS. Example: 9.24.5.
- If the newest version is not a new major, start on the latest LTS/MTS and upgrade before go-live if a new one ships.
- Exceptions:
  - a needed feature exists only in a non-MTS release;
  - the current version is going out of support;
  - Marketplace module dependencies force it.
- This is a proposed way of working; teams or customers may differ.
