---
title: Upgrading a platform app from Mx9 to Mx10.24
topic: upgrade
domain: [delivery-process, devops-cloud]
kind: procedure
applies_to: company-standard
versions: "9.24.latest -> 10.24.latest"
keywords: ["Mx9 to Mx10 upgrade", "9.24 to 10.24", "SVN to Git migration", "Java 21 upgrade", "Community Commons update", "Workflow Commons 3.0.0", "MPR v2 conversion", "Dojo widgets deprecated", "Copy to Clipboard widget", "LoginAction OData REST", "Native app store rebuild", "Post-upgrade triage"]
layer: field
sources:
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed
---
**Status:** Steps 1–5 and 7 follow a platform migration guide. Step 6 and the Workflow Commons, `LoginAction` and native rebuild advice come from one upgrade triage checklist. They are not independently confirmed.

**When**
- Any app still on Mx9.
- Target 10.24, then keep taking patch versions for fixes and security updates.
- Do not stay on old Mx10 minors. Many fixes landed in 10.6.x and 10.12.x MTS.

**Steps**
1. Upgrade to 9.24.latest.
2. Fix model and Java deprecations (Mx9 runtime deprecated list).
3. Migrate from SVN to Git if not done yet.
   - Known issues exist for Mx9 SVN projects moving to Mx10 Git.
   - Large repos may hit Team Server limits.
   - GitLab is the eventual target but not required for Mx10.
4. Upgrade to 10.24.latest.
5. Switch to Java 21. Update the Dockerfile and pipeline if they came from an older platform app template; the DevOps team can help.
6. The triage skill gives these module updates:
   - Community Commons and Object Handling: update to latest.
   - Workflow Commons: update to 3.0.0 or later, if used.
   - Atlas Core: update to the minimum version required for the target Mendix version.
   - Commit right after the Atlas Core upgrade.
7. Test and fix.

**Checks**
- The MDA builds. Overlooked Mx9-deprecated Java APIs cause errors when building the MDA.
- The runtime starts. Legacy scheduled events make it fail to start in Mx10.
- Deeplinks work from a logged-out state.
- No CE errors from [[mx10-post-upgrade-ce-error-codes]].

**Watch out**
- You do not have to replace all Dojo widgets for Mx10. Replace only where needed.
- The Copy to Clipboard widget (`ClipboardTextCopy.mpk`) broke in the Catalog. It was replaced with a nanoflow and a JavaScript action.
- Models opened in versions above 10.22 are converted to MPR v2 automatically.
- Workflows: the triage skill says Workflow Commons must be ≥ 3.0.0 (multi-assignee).
  - Run `ACT_Assignee_Migration`, or add `ASu_Assignee_Migrate` to after-startup.
  - Fix visibility expressions that assumed a single assignee.
- The same skill says a custom `LoginAction` on OData/REST/web services is ignored in Mx10. Use authentication microflows.
- The same skill says native apps need a full store rebuild, because OTA updates fail across major versions.
- Adopt new features (React client, Strict mode, direct associations, etc.) in a separate epic.
- [[mx10-scheduled-events-minimum-interval]], [[mx10-dom-wrapper-breaks-css-selectors]], [[mx10-java-action-final-params-rollbacktransaction]], [[community-commons-pdfbox3-userlib-mismatch]], [[mx10-dart-sass-mixed-unit-arithmetic]], [[mx10-24-generated-html-ids-changed]], [[git-node-modules-and-mass-deletions-crash-studio-pro]], [[mx10-direct-association-migration-downtime]]

**Release notes**
- 10.21.0: Java 11/17 support removed; use Java 21 (https://docs.mendix.com/releasenotes/studio-pro/10.21/#10210)
- 10.0.0: SVN support removed (https://docs.mendix.com/releasenotes/studio-pro/10.0/#1000)
- 10.0.0: legacy scheduled events no longer supported; runtime fails to start if they exist (https://docs.mendix.com/releasenotes/studio-pro/10.0/#1000)
