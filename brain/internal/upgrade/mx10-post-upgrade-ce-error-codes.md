---
title: CE error codes seen after an Mx9 to Mx10 upgrade and their fixes
topic: upgrade
domain: [delivery-process]
kind: reference
applies_to: mendix-general
versions: "Mx9 -> Mx10.24"
keywords: ["CE6911 cachebust", "CE9803 java-version", "CE6093 Dart Sass SCSS math", "CE9500 feedback widget App ID", "CE0091 validation feedback", "CE0557 navigation page roles", "Mx9 Mx10 upgrade", "cache-bust index.html", "Java dependency sync failed", "SCSS mixed unit arithmetic"]
layer: field
sources:
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed
---
Status: Codes and fixes come from an upgrade triage checklist's list of common post-upgrade errors. The `java-version` survival was seen in one later run. The sources give no fix for CE0091 or CE0557.

| Code | Cause | Fix |
|---|---|---|
| CE6911 | `theme/web/index.html` has hardcoded cache-bust values | Use `{{cachebust}}` tags everywhere. Otherwise deployed changes don't invalidate the browser cache. |
| CE9803 | Java dependency sync failed, often because the root `java-version` file is missing | Create `java-version` containing `21` |
| CE6093 | Dart Sass rejects mixed-unit SCSS arithmetic (px + rem) that LibSass allowed | [[mx10-dart-sass-mixed-unit-arithmetic]] |
| CE9500 | Feedback widget has an old App ID (changes after migration/rename) | Right-click the error → "Update the App ID of all feedback widgets" |
| CE0091 | Empty validation feedback message | Not given in sources |
| CE0557 | Navigation page with no allowed roles | Not given in sources. The lint rule MPR007 flags it. |

Notes:
- A later upgrade plan predicted that Studio Pro might delete `java-version`. On an Mx10.24 → 11.9.1 conversion, the file was still present.
- The skill's fix order is:
  1. CE9803
  2. CE6911
  3. CE9500
  4. Marketplace module updates
  5. `userlib` JARs
  6. SCSS (CE6093)
  7. git state
  8. Validate with `mx check`
