# Upgrade proposal: 10.6.3.26585 -> 10.24.0.73019 -> 11.12.5

<!-- proposal inputs-hash: 764f15a3e42ebe33aa66a5a0e2fd0b839081d871adcc664b016136bf0bbfa5bc -->

Written by bin/proposal.py from the triage outputs. Nothing in the app model changes before section 6 is signed. Every line starting with `- ` is an item; sub-lines are evidence.

## 1. Summary

- From 10.6.3.26585 to 10.24.0.73019 and 11.12.5 (rung 1 10.6.3.26585 -> 10.24.0.73019, rung 2 10.24.0.73019 -> 11.12.5). App size: 30 modules, 70 pages, 786 microflows, 292 actions.
- 13 items the toolkit expects to handle, 18 need your decision, 4 need a person anyway.

## 2. Done by the toolkit

Module updates and predicted repairs only. A kept module, a stranded module, a RED local edit and a widget with no successor are never here; they are in section 3.

- module update Atlas_Core ? -> 3.15.0 (before the convert)
- module update CommunityCommons 10.0.5 -> 10.4.2 (before the convert)
- module update DataWidgets 2.13.0 -> 2.27.9 (before the convert)
- module update NanoflowCommons 4.0.2 -> 4.0.4 (after the convert)
- module update WebActions 2.10.0 -> 2.11.2 (after the convert)
- module update ZipHandling 4.5.1 -> 5.1.1 (after the convert)
- Dojo to React on the 11.12.5 rung: 4 x Data grid (legacy, core) -> Data Grid 2 (Data Widgets 116540)
- Dojo to React on the 11.12.5 rung: 4 x Drop-down (core) -> Combo box
- Dojo to React on the 11.12.5 rung: 25 x Dynamic Image (core) -> Image widget (com.mendix.widget.web.image.Image, Marketplace 118579)
- Dojo to React on the 11.12.5 rung: 6 x Reference Selector (core) -> Combo box (Marketplace 219304)
- Dojo to React on the 11.12.5 rung: 12 x Static Image (core) -> Image widget
- Dojo to React on the 11.12.5 rung: 1 x Template grid (core) -> Gallery (Data Widgets 116540)
- predicted repair R32 (OQL version 2 app setting off (UseOQLVersion2)) -> repair row 21 (CE6779)

## 3. Needs your decision before we start

Answer each item in chat (steps/decide.md options); the toolkit records it in DECISIONS.md as the P-n line. Signing section 6 without an answer accepts the recommendation of that item.

- [P-1] Java: R18 Runtime Java API removals (10, 11)
  - evidence: replacements.md row R18 HIT: /\bCore\.retrieveXPath\w*|\bcom\.mendix\.core\.conf\.RuntimeVersion\b|\bRuntimeVersion\.getInstance\b|\bCore\.isSubClassOf\b|\.getEntityId\s*\(\s*\)|\b(changeAsync|commitAsync|addSessionCookies)\b|com\.mendix\.modules\.email|com\.mendix\.m2ee\b|\bCore\.metrics\(\)\s*\.\s*(counters|gauges|timers|sets)\s*\(/ in javasource/communitycommons/Misc.java (4), javasource/communitycommons/ORM.java (2), javasource/communitycommons/XPath.java (3), javasource/deeplink/actions/ReadMicroflows.java (1) ... (16 files)
  - options: documented replacements; Java Migration Tool (jmt rewrite --to-version 11.x --dry-run) (replacements.tsv row R18)
  - recommendation: follow replacements.tsv row R18: documented replacements; Java Migration Tool (jmt rewrite --to-version 11.x --dry-run); effort S; risk: most hits are Marketplace modules' Java: update those first; a module with no 11
  - answer: follow replacements.tsv row R18: documented replacements; Java Migration Tool (jmt rewrite --to-version 11.x --dry-run) (ASSUMED (unattended))
- [P-2] Java: R30 System attributes changedDate and changedBy read in logic...
  - evidence: replacements.md row R30 HIT: /(?i)/changed(Date|By)\b|\bSystem\.changed(Date|By)\b/ in MendixSSO.RS_NotifyUserRolesChanged (Marketplace): MendixSSO.RS_NotifyUserRolesChanged Microflows$ExpressionSplitCondition: 'addSeconds($User/changedDate, 2) < [%CurrentDateTime%]'; /\b(getChangedDate|getChangedBy|hasChangedMemberValue)\b|MemberNames\.changed(Date|By)\b/ in javasource/communitycommons/ORM.java (1)
  - options: keep the module (S, until it leaves the Marketplace) | OIDC SSO with the IdP (M-L) | SAML / LDAP / local credentials (M) | OIDC Provider for custom SSO
  - recommendation: OIDC with the IdP once the IdP decision is made; keep until then. [RA-16, idea, playbooks/rearchitecture.md]; effort L; risk: SILENT data risk, the build stays green: a value derived from changedDate before
  - answer: OIDC with the IdP once the IdP decision is made; keep until then. [RA-16, idea, playbooks/rearchitecture.md] (ASSUMED (unattended))
- [P-3] check: Release notes
  - evidence: the release-note check did not run: release_impact: no brain version tables under <company-brain>/baseline/versions
  - options: run the check first: give the run the company brain (its version tables), then rerun triage | go on without it: a named person reads the Mendix release notes for every version on the route before go-live | pause the upgrade
  - recommendation: run the check first: give the run the company brain (its version tables), then rerun triage; effort S; risk: a change in the new Mendix versions is only found at the build or the test, or after go-live
  - answer: run the check first: give the run the company brain (its version tables), then rerun triage (ASSUMED (unattended))
- [P-4] module: AmazonTranslateConnector
  - evidence: RED local edit (data-bearing): CHANGED entity AmazonTranslateConnector.ListLanguagesRequest; CHANGED entity AmazonTranslateConnector.TranslateTextRequest (localedits.json / kept.txt)
  - options: update to the latest version and carry the edits over (diagram-only dropped, UI and constants replayed, vendor drops checked) | update, move the edits to AmazonTranslateConnector_Ext by hand | keep old version for now (a reason and an end date) | replace with the Marketplace equivalent (replacements.tsv row) | hand to a named person
  - recommendation: update to the latest version and carry the edits over (diagram-only dropped, UI and constants replayed, vendor drops checked); a real logic edit is held until it is moved to AmazonTranslateConnector_Ext; effort M; risk: data loss if a RED edit is replaced
  - answer: update to the latest version and carry the edits over (diagram-only dropped, UI and constants replayed, vendor drops checked); a real logic edit is held until it is moved to AmazonTranslateConnector_Ext (ASSUMED (unattended))
- [P-18] module: Atlas_Web_Content
  - evidence: kept at its version by the update step: idcheck REVIEW (persistence loss or removal: accept it in approved.txt with a reason, or keep), see .stepupdate/step2-Atlas_Web_Content.idcheck (localedits.json / kept.txt)
  - options: update to the latest version and carry the edits over (diagram-only dropped, UI and constants replayed, vendor drops checked) | update, move the edits to Atlas_Web_Content_Ext by hand | keep old version for now (a reason and an end date) | replace with the Marketplace equivalent (replacements.tsv row) | hand to a named person
  - recommendation: update to the latest version and carry the edits over (diagram-only dropped, UI and constants replayed, vendor drops checked); a real logic edit is held until it is moved to Atlas_Web_Content_Ext; effort M; risk: behaviour of local edits is lost on update
  - answer: update to the latest version and carry the edits over (diagram-only dropped, UI and constants replayed, vendor drops checked); a real logic edit is held until it is moved to Atlas_Web_Content_Ext (ASSUMED (unattended))
- [P-19] module: DeepLink
  - evidence: kept at its version by the update step: local edits refuse the update (localedits.json / kept.txt)
  - options: update to the latest version and carry the edits over (diagram-only dropped, UI and constants replayed, vendor drops checked) | update, move the edits to DeepLink_Ext by hand | keep old version for now (a reason and an end date) | replace with the Marketplace equivalent (replacements.tsv row) | hand to a named person
  - recommendation: update to the latest version and carry the edits over (diagram-only dropped, UI and constants replayed, vendor drops checked); a real logic edit is held until it is moved to DeepLink_Ext; effort M; risk: behaviour of local edits is lost on update
  - answer: update to the latest version and carry the edits over (diagram-only dropped, UI and constants replayed, vendor drops checked); a real logic edit is held until it is moved to DeepLink_Ext (ASSUMED (unattended))
- [P-5] module: R14 Encryption module key, prefix and cipher changes
  - evidence: replacements.md row R14 HIT: module Encryption 9.0.2 (Marketplace)
  - options: same module, newer major; LegacyEncryptionKey for old values (replacements.tsv row R14)
  - recommendation: follow replacements.tsv row R14: same module, newer major; LegacyEncryptionKey for old values; effort S; risk: HIGH data risk: a wrong key makes stored secrets (SMTP, API credentials) unreada
  - answer: follow replacements.tsv row R14: same module, newer major; LegacyEncryptionKey for old values (ASSUMED (unattended))
- [P-6] module: R21 Platform behaviour changes 10 to 11: REST encoding, jdbc:mysql:,...
  - evidence: replacements.md row R21 HIT: Microflows$RestCallAction: 5 in AWSAuthentication.AssumeRole (Marketplace), MendixSSO.GetEmailAddressOfUserFromApp (Marketplace), MendixSSO.RetrieveUserRoles (Marketplace), MendixSSO.SUB_GetUserInfoFromIdentityProvider (Marketplace) ... (5 documents)
  - options: keep the module (S, until it leaves the Marketplace) | OIDC SSO with the IdP (M-L) | SAML / LDAP / local credentials (M) | OIDC Provider for custom SSO
  - recommendation: OIDC with the IdP once the IdP decision is made; keep until then. [RA-16, idea, playbooks/rearchitecture.md]; effort L; risk: SILENT behaviour risk: empty strings no longer concatenate as null, REST paramet
  - answer: OIDC with the IdP once the IdP decision is made; keep until then. [RA-16, idea, playbooks/rearchitecture.md] (ASSUMED (unattended))
- [P-7] module: R3 MendixSSO module
  - evidence: replacements.md row R3 HIT: module MendixSSO 4.2.0 (Marketplace)
  - options: keep the module (S, until it leaves the Marketplace) | OIDC SSO with the IdP (M-L) | SAML / LDAP / local credentials (M) | OIDC Provider for custom SSO
  - recommendation: OIDC with the IdP once the IdP decision is made; keep until then. [RA-16, idea, playbooks/rearchitecture.md]; effort L; risk: user-data migration of the MendixSSO user specialisation; the IdP decision is ou
  - answer: OIDC with the IdP once the IdP decision is made; keep until then. [RA-16, idea, playbooks/rearchitecture.md] (ASSUMED (unattended))
- [P-8] module: R34 SSL certificate algorithm SunX509 (SslCertificateAlgorithm)
  - evidence: replacements.md row R34 HIT: setting Settings$ModelSettings.SslCertificateAlgorithm is absent (its default applies)
  - options: App Settings > Runtime > SSL Certificate Algorithm = PKIX (recommended): the PKIX validator / trust manager (replacements.tsv row R34)
  - recommendation: follow replacements.tsv row R34: App Settings > Runtime > SSL Certificate Algorithm = PKIX (recommended): the PKIX validator / trust manager; effort S; risk: outgoing HTTPS (REST, web services, client certificates) is validated by another
  - answer: follow replacements.tsv row R34: App Settings > Runtime > SSL Certificate Algorithm = PKIX (recommended): the PKIX validator / trust manager (ASSUMED (unattended))
- [P-9] page: R4 Deep Link module
  - evidence: replacements.md row R4 HIT: module DeepLink 10.0.8 (Marketplace)
  - options: page URLs and microflow URLs (10.6+; microflow URL query parameters from 10.9) (replacements.tsv row R4)
  - recommendation: follow replacements.tsv row R4: page URLs and microflow URLs (10.6+; microflow URL query parameters from 10.9); effort M; risk: the deep-link configuration is DATABASE rows (T6: new GUIDs lost all deep links)
  - answer: follow replacements.tsv row R4: page URLs and microflow URLs (10.6+; microflow URL query parameters from 10.9) (ASSUMED (unattended))
- [P-10] page: R6 Document Templates / Generate Document action
  - evidence: replacements.md row R6 HIT: DocumentTemplates$DocumentTemplate: 1 in Shopapp_Reporting.ShopappReport_Template (own); Microflows$GenerateDocumentAction: 1 in Shopapp_Reporting.Report_GenerateShopappReport (own)
  - options: keep on 10.24 (S) | PDF Document Generation from pages (M-L) | partner module for Word/RTF/ODT (M) | hand off
  - recommendation: PDF Document Generation per template; compare output with the old documents. [RA-17, idea, playbooks/rearchitecture.md]; effort L; risk: layout is redone per template; compare output with the old documents; PDF Docume
  - answer: PDF Document Generation per template; compare output with the old documents. [RA-17, idea, playbooks/rearchitecture.md] (ASSUMED (unattended))
- [P-11] theme: R7 Atlas 3 theme (SASS variables) to Atlas Core 4 (CSS variables)
  - evidence: replacements.md row R7 HIT: module Atlas_Core 3.14.0 (Marketplace) is <4.0.0
  - options: Atlas Core 4.x with CSS variables ($use-css-variables: true, var(--x), color-mix()) (replacements.tsv row R7)
  - recommendation: follow replacements.tsv row R7: Atlas Core 4.x with CSS variables ($use-css-variables: true, var(--x), color-mix()); effort M; risk: look, not data; forced by WorkflowCommons 4.3+ (71 CE6083 on Atlas 3) and Data W
  - answer: follow replacements.tsv row R7: Atlas Core 4.x with CSS variables ($use-css-variables: true, var(--x), color-mix()) (ASSUMED (unattended))
- [P-12] widget: R11 Data grid 1 / Data Widgets 2 to Data Widgets 3
  - evidence: replacements.md row R11 HIT: module DataWidgets 2.13.0 (Marketplace) is <3.0.0
  - options: Data grid 2, Gallery and filter widgets of Data Widgets 3.x (replacements.tsv row R11)
  - recommendation: follow replacements.tsv row R11: Data grid 2, Gallery and filter widgets of Data Widgets 3.x; effort S; risk: look and filter behaviour; re-baseline screenshots (paging text)
  - answer: follow replacements.tsv row R11: Data grid 2, Gallery and filter widgets of Data Widgets 3.x (ASSUMED (unattended))
- [P-13] widget: R25 Language Selector widget (com.mendix.widget.web.LanguageSelector 1.x)
  - evidence: replacements.md row R25 HIT: widget /com\.mendix\.widget\.web\.languageselector\.LanguageSelector/ on Atlas_Core.LanguageSelectorWidget (Marketplace)
  - options: a Combo Box acting as language selector, as the Atlas Core 3.20.0+ layouts do (replacements.tsv row R25)
  - recommendation: follow replacements.tsv row R25: a Combo Box acting as language selector, as the Atlas Core 3.20.0+ layouts do; effort S; risk: the layout header and the language-switch logic change; an Atlas Core below 3.20
  - answer: follow replacements.tsv row R25: a Combo Box acting as language selector, as the Atlas Core 3.20.0+ layouts do (ASSUMED (unattended))
- [P-14] widget: R26 Deprecated Dojo-era Mendix web widgets: Microflow Timer, Bootstrap...
  - evidence: replacements.md row R26 HIT: widget /(MicroflowTimer\.widget\.MicroflowTimer|BootstrapTooltip\.widget\.BootstrapTooltip(Context)?)/ on Shopapp_Template.Group_NewEdit (own), Mobile_Inspector.Dashboard_Inspector (own), Mobile_Inspector.InstanceShopapp_ViewSummary (own)
  - options: Microflow Timer: Events widget (timer); Bootstrap Tooltip: Tooltip widget; List View Controls: Data grid 2 or Gallery with their filter widgets; Format String: HTML Element or text with parameters; Google Maps: Maps; Radiobutton List: radio buttons; checkbox and label selectors: Combo box (multiple selection) (replacements.tsv row R26)
  - recommendation: follow replacements.tsv row R26: Microflow Timer: Events widget (timer); Bootstrap Tooltip: Tooltip widget; List View Controls: Data grid 2 or Gallery with their filter widgets; Format String: HTML Element or text with parameters; Google Maps: Maps; Radiobutton List: radio buttons; checkbox and label selectors: Combo box (multiple selection); effort M; risk: a Dojo widget blocks the switch to the React client and dies with Dojo in 12; ea
  - answer: follow replacements.tsv row R26: Microflow Timer: Events widget (timer); Bootstrap Tooltip: Tooltip widget; List View Controls: Data grid 2 or Gallery with their filter widgets; Format String: HTML Element or text with parameters; Google Maps: Maps; Radiobutton List: radio buttons; checkbox and label selectors: Combo box (multiple selection) (ASSUMED (unattended))
- [P-15] widget: R35 A widget package that calls a React 19 removed API (findDOMNode,...
  - evidence: replacements.md row R35 HIT: widgets/mendix.DropdownContainer.mpk 1.2.0 runs /\bfindDOMNode\b|\bunmountComponentAtNode\b|\bReactDOM\.(render|hydrate)\(/ in its JavaScript and widget mendix.dropdowncontainer.DropdownContainer is used 2 time(s) on Shopapp_Template.Group_NewEdit (own) x2
  - options: keep on the source version (S, ends with its support window) | replace by Pop-up menu where the container opens a list of actions (M) | replace by Combo box where it only offers one choice (M) | ask the owner for a React 19 build (S, date not ours) | rebuild as a small pluggable widget (M)
  - recommendation: Pop-up menu per instance, driven by a script, not by hand. [RA-2, proven, playbooks/rearchitecture.md]; effort M; risk: breaks at runtime only, the build stays green: 'Could not render widget' on ever
  - answer: Pop-up menu per instance, driven by a script, not by hand. [RA-2, proven, playbooks/rearchitecture.md] (ASSUMED (unattended))
- [P-16] widget: R9 React 19 (Studio Pro 11.6): every widget at its latest version
  - evidence: replacements.md row R9 HIT: widgets/: AnyChart.mpk, Badge.mpk, BadgeButton.mpk, Charts.mpk ... (43 files)
  - options: current pluggable widget versions (mx update-widgets on the 10.24 rung) (replacements.tsv row R9)
  - recommendation: follow replacements.tsv row R9: current pluggable widget versions (mx update-widgets on the 10.24 rung); effort S; risk: breaks at runtime only: the build stays green
  - answer: follow replacements.tsv row R9: current pluggable widget versions (mx update-widgets on the 10.24 rung) (ASSUMED (unattended))

## 4. Needs a person anyway

- key-user confirmation of the user processes (status: confirmed is set only by a person)
  - templates/process-interview.md; the number of processes is unknown at this point
- visual sign-off of the changed screens (shotdiff REVIEW pairs)
  - the number of changed screens is known only after the gate
- real test systems for external APIs: unclassified
  - 9 endpoints in apimock-inventory.json; the stand-in gives at best PASS (on stand-in APIs)
- go-live actions (deployment, data migration window, rollback decision)
  - outside the toolkit

## 5. Human effort

- decision touchpoints: Java 2, check 1, module 7, page 2, theme 1, widget 5
- person-anyway touchpoints: 4
- range for the decisions alone: 49.5 to 230 hours (toolkit assumption per item: S 0.5-2 h, M 2-8 h, L 8-40 h; not measured). Key-user time, screen review and go-live are not in it.
- unknown at this point:
  - not measured: stranded.md: steps/triage.md item 3 lists stranded modules and add-on modules built before 10.21 there
  - not measured: release-impact.md: steps/triage.md item 10
  - not measured: widgetcover.py: it judges which widget packages the walks render; the walks of the new app exist only at the gate (widgets rung)
  - not measured: theme_clash.py: it compares the app's styling with the NEW Atlas, which exists only after the update
  - not measured: rolecheck.py: it compares the OLD and the NEW model; module roles are checked after each module update
  - not measured: usercode.py: it compares a module's Java user code per module, after the update step (.stepupdate/step<n>-<module>.usercode); Java edits that exist now are the localedits.json FILES-EDITED rows

## Testing plan

What the gate tests, what it cannot test in a sandbox, and how each gap is closed. Numbers come from the inputs named in section 5.

### What is tested and how

- build: mx check and mxbuild of the converted app, errors listed per code (30 modules, 70 pages, 786 microflows)
- data: the old and the new app each start on a copy of the same database; every table is compared row by row (a row that differs is FAIL until accepted with a written reason)
- journeys: one browser journey per action (292 actions in the inventory), per role, run on the old app and the new app; a difference is a regression
  - journeys in scope: 234 reachable, 58 out of scope (unreachable 13, marketplace 36, no-role 9)
  - testability work: 0 reachable actions have no click path yet (record a click path, or test at deploy); each of these stays INVALID in the gate until it has a path
- external calls on a stand-in: 9 endpoints and constants found, 3 can be answered by the stand-in (apimock.py), 6 are UNKNOWN; the apis rung checks that the stand-in was asked what the model says it should be asked

### What cannot be tested in the sandbox

- 6 of 9 external endpoints are UNKNOWN: no stand-in route exists, so a journey that needs one is INVALID, not PASS (examples: AWSAuthentication.AssumeRole, DeepLink.LoginLocation, DeepLink.SSOHandlerLocation, MendixSSO.OpenIdConnectProvider, MendixSSO.SUB_GetUserInfoFromIdentityProvider)
- the real behaviour of an external system (answers, limits, errors): a stand-in only returns shaped data, so a pass on it is reported as PASS (on stand-in APIs), never plain PASS
- single sign-on and any login through an identity provider: the sandbox uses local smoke users
- data the sandbox database does not hold (an action that needs rows of a kind that does not exist yet): the heal step seeds identical rows in both databases where it can, the rest stays INVALID

### How each gap is closed

- classify every UNKNOWN endpoint (static, data-driven or add-on) in apimock-classify.txt; owner: the person who knows the integration
- seed the data that data-driven endpoints need, in the old and the new database alike; owner: the app owner
- run the apis rung against a real test system before go-live and compare with the stand-in run; owner: a named person on the customer side
- go-live decision on every INVALID journey that remains: accept in writing or test by hand; owner: a named person

## 6. Sign-off

A person writes exactly one of these two lines below (an agent never does):

`Signed-off: <name> <yyyy-mm-dd>`   or   `Status: PAUSED <reason>`

Status: open
