---
title: Community Commons update needs PDFBox 3.x and commons-io 2.12+ JARs in userlib
topic: upgrade
domain: [integration, devops-cloud]
kind: pitfall
applies_to: mendix-general
versions: "Mx9 -> Mx10 with userlib (not managed dependencies)"
keywords: ["Community Commons upgrade", "PDFBox 3.x", "commons-io 2.12", "userlib JARs", "pdfbox-2.0.24", "pdfbox-3.0.3", "fontbox", "commons-io 2.11.0", "cannot be converted to List", "RandomAccessRead InputStream", "BOMInputStream builder", "Mx9 Mx10 upgrade"]
layer: field
sources:
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed
---
**Symptom**
- Compile errors after updating Community Commons:
  - `List<RandomAccessRead> cannot be converted to List<InputStream>`;
  - `cannot find symbol: method builder()` on `BOMInputStream`.

**Root cause**
- The newer Community Commons uses the PDFBox 3.x and commons-io 2.12+ APIs.
- `userlib` still held `pdfbox-2.0.24`, `fontbox-2.0.24` and `commons-io-2.11.0`.
- Per the triage skill, Marketplace module upgrades in Studio Pro replace the Java source but do not update the JARs in `userlib`.

**Fix**
- Remove `pdfbox-2.0.24.jar` and `fontbox-2.0.24.jar`. Add `pdfbox-3.0.3.jar` and `fontbox-3.0.3.jar`.
- Add `pdfbox-io-3.0.3.jar`, which is new in 3.x.
- Replace commons-io with `2.16.1`.
- Add `.RequiredLib` markers (content `CommunityCommons`) and delete the stale ones.
- Better long term: [[userlib-to-managed-dependencies]].

**Status**
- Workaround: the fix steps come from an upgrade triage checklist. No source confirms them.
- In one later Mx10.24 -> Mx11.9.1 upgrade, PDFBox 3.0.3 and commons-io 2.16.1 were already in `userlib` from the Mx10 upgrade.
