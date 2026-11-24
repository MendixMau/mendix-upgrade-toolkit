---
title: Measured Mx10.24 to Mx11.12 upgrade — warnings by type and how they were handled
topic: upgrade
domain: [delivery-process]
kind: reference
applies_to: company-standard
versions: "10.24.13 -> 10.24.22 -> 11.12.0"
keywords: ["upgrade warnings", "Mendix 10.24 to 11.12", "exposed action image not optimized", "error handler with rollback", "feedback widget App ID", "microflow url show page action", "potential conflict page URL", "NanoflowCommons not compatible", "old string behavior deprecated", "private constant value", "HTMLSnippet React"]
layer: field
sources:
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed
---
One app's run (10.24.13 → 10.24.22 → 11.12.0):

| Step | Finding | Handling |
|---|---|---|
| →10.24.22 | 0 errors; 48 changes (jackson 2.22.0→2.22.1 auto-updated, vendorlib-sbom.json, widgets) | Commit |
| →10.24.22 | 3 deprecations: StringUtils exposed-action image not optimized | "Optimize all images for exposed actions in the app" |
| →10.24.22 | 237 warnings | Suppress Marketplace module warnings (updates overwrite local changes); 128 remain |
| own | Error-handler-with-rollback flow returns to main flow (32) | Suppress; flows merge into an error flow |
| own | Variable never used (45); empty caption (11); empty title (2); design property excluded by the app's design system (10) | Fix |
| own | Microflow has roles but not used from nav/page/service (7) | Remove roles (security) |
| own | Client side-effect in data source microflow/nanoflow (2 + 1) | Remove refresh, or accept the risk |
| own | Feedback widget App ID differs / set without app ID (2) | Give all feedback widgets the same App ID |
| own | Microflow with URL should end with show page (2) | Suppress; show page is in the last sub-microflow |
| own | Module role in no user role (3); unused page param (5); no on-click (6) | Fix |
| →11.12.0 | 1 error: private constant needs a value | Enter a value |
| →11.12.0 | 46 deprecations (data grid, drop-down etc. removed in Mx12); old string behavior | Enable new string behavior now; widgets later |
| →11.12.0 | NanoflowCommons 5.2.0 not compatible | Upgrade to 7.2.0 |
| →11.12.0 | Page URL "potential conflict" with microflow URL (3) | Unclear if real (source asks) |
| →11.12.0 | HTMLSnippet with Context not supported in React client | Ignored |

The whole app was clicked through after 10.24.22; nothing broke.

