# Support-ticket sweep: what breaks in real Mendix upgrades, and what the toolkit does not see yet

**From:** ZD (sweep of Mendix Support tickets, 2025-06 to 2026-11; code name only, no ticket ids or customer names)
**Date:** 2026-11-25
**Kind:** pitfall | playbook-row | error-code (many; one section per issue)
**Upgrade:** mostly 9 to 10.24 and 10 to 11.12, some 10.x/11.x patch jumps
**Field evidence:** 484 tickets with "upgrade" in the subject; 242 were app upgrades (not infra, licensing or
announcements); the comments of about 104 were read for the root cause and the fix that worked. Counts below are
tickets per issue. Evidence per issue says **confirmed** (the customer or R&D confirmed the fix), **proposed**
(support's advice, outcome not stated) or **open** (no fix yet). Everything here is a lead for triage, not a verified
row: a row promoted from this file stays `UNVERIFIED` until a control or a field run proves it.
**Proposed target:** per section; four structural items at the end

Upgrade paths seen in the 242: 9→10 (34), 10→10 patch (19), 9→9 patch (11), 10→11 (9), 9→11 (6), 8→9/10 (5), 11→11 (2).

---

## Headline

Most production outages in the tickets come from things outside the app model: database size, the file-storage
backend, reverse-proxy headers, phones still running the old build, and bad patch releases. The toolkit scans the
model, Java and modules, so it is blind to these. Sections 1, 3, 5 and 6 are that kind.

---

## 1. Native: in-place store update of the app breaks the offline database (~13 tickets)

- **Path:** 9→10.24, 10.18→10.24.x, 10.24→11.12.
- **Symptoms:** `[op-sqlite] SQL prepare error: table mx…$_guidToTable has no column named inaccessibleAttrs`;
  `no such table: mx…$System$UserRoles` (or `$Administration$Account`); "Your changes cannot be synchronised at this
  moment"; every launch, until reinstall. Separately: all users logged out once after the 9→10 store update.
- **Cause:** the local offline schema is not migrated across versions (the OP-SQLite switch in 11.12 is one case).
  A 10.24.17–10.24.19 runtime breaks clients still on an older bundle. The cookie-encryption default changed in 10.21,
  so sessions of old builds are lost. Token storage changed 9→10 (forced re-login is expected behaviour).
- **Fix:** offline schema fixed in 10.24.15; old-bundle compatibility fixed in 10.24.20 (both **confirmed** by R&D).
  11.12 OP-SQLite: a native-template change forcing a full local reset on first launch of the new build
  (**confirmed** workaround; platform fix pending). Otherwise reinstall or clear data, which loses unsynced data.
  Support advised against enabling DB encryption as a workaround (it also wipes local data).
- **Toolkit:** partial. R23 flags native risk in general; `10-to-11.md` covers 11.12.5 StorageGuids only.
- **Proposed:** R23 `unchecked` additions (old bundle against new runtime, 10.21 cookie default, 9→10 forced
  re-login as a report item for end-user comms). remedies key `native-installed-client-sync`,
  match `(?i)(could (temporarily )?not synchroni[sz]e|inaccessibleAttrs|_guidToTable|op-sqlite.{0,40}no such (table|column))`,
  options: A target ≥10.24.20 (or the fixed 11.12 patch), B forced local reset / reinstall (HUMAN), D stay.

## 2. Java and jars (~12 tickets)

- **Removed runtime APIs on 10→11**, in own code and in Marketplace/community modules:
  `Core.retrieveXPathQuery(...)` paging/sort overloads, `Core.isSubClassOf(String,String)`,
  `ICoreAction.getMetaInfo()`, `OQL.executeOQL(...)` with 6 args (5 expected), `Export.buildExportFile(...)` (needs an
  `MxTemplate` arg), `com.mendix.webui.CustomJavaAction`, `context()`,
  `com.mendix.systemwideinterfaces.core.UserBlockedException`, `Configuration.RUNTIME_VERSION` (Document Generation).
  Fixes (**proposed** by support): `Core.createXPathQuery(String)`, `IMetaObject.isSubClassOf` /
  `IMendixObject.isInstanceOf`, `getMetaInfoJsonString()`.
  Note: the Java Migration Tool dry run reported "Files would be changed: 0" on an app where support's own run then
  applied the `retrieveXPathQuery` recipe. So 0 changes from that tool does not prove there are no hits.
- **Module minimums on 11:** Advanced Audit Trail below 4.0.0 is not 11-compatible. OIDC SSO 5.0.0 on 11.12.4 calls
  `JWK.getExpirationTime()`, which the nimbus-jose-jwt bundled with 11 no longer has (**open** bug). Excel Exporter
  Template Manager (community) is stranded on 11.
- **Stale jars after a SAML20 update (9.x→9.24, 9→10):**
  `Unknown configuration property http://javax.xml.XMLConstants/property/accessExternalDTD` from an old
  `xalan-2.7.1.jar` in userlib, and `cannot find symbol SessionManager.getInstance(getContext()).setAfterSigninMicroflowName`.
  Fix: remove userlib jars the module's .mpk no longer ships (**confirmed** for xalan).
- **Toolkit:** partial. R18 covers `retrieveXPath*` / `isSubClassOf`; BACKLOG #144 names `CustomJavaAction` and
  `context()`; jardedupe/jarclash cover duplicate jars; nothing names xalan / accessExternalDTD.
- **Proposed:** extend the R18 detect with
  `\bICoreAction\b.*\.getMetaInfo\s*\(|\bOQL\.executeOQL\s*\(|\bExport\.buildExportFile\s*\(|com\.mendix\.webui\.CustomJavaAction|\bConfiguration\.RUNTIME_VERSION\b|\bUserBlockedException\b`.
  New rows: Advanced Audit Trail `modver:AdvancedAuditTrail:<4.0.0` `->11`; OIDC `modver:OIDC:>=5.0.0` `->11.12`
  (until the fixed version is published); `module:SAML20 && jar:(?i)^(xalan|xercesImpl|xml-apis)-`.
  remedies key `stale-xml-jar`, match `(?i)accessExternalDTD|Unknown configuration property http://javax\.xml`.
  Template Manager on the `deprecated-components.md` "no successor" list. A note in `10-to-11.md` about the
  Java Migration Tool's 0 changes.

## 3. Production cutover: database update time, disk, and the way back (~11 tickets, all production outages)

- **Large database, long schema update:** `ConnectionBus: Executing 839 database synchronization command(s)...` with
  no progress logged, then the container is killed at the 15-minute startup limit. Variants:
  `PSQLException: ERROR: could not extend file ... No space left on device` (16 of 40 GB in use, still ran out);
  10→11 with millions of workflow instances: hours of `Actuating workflow instances`, one `System.QueuedTask` per
  InProgress instance (R&D: cannot be skipped).
  Fix (**confirmed**, 2 cases): support disables the Mendix Cloud readiness check, or raises the startup threshold
  (60 min), for the deploy window; or temporarily upsize the plan for disk and memory, then downsize. Workflow volume
  case: **open**.
- **No way back by redeploying:** `Unsupported pre-analysis migration version: 4.4.0. You are trying to synchronize a
  Mendix application database from an unsupported Mendix version.` when the 9.x package is redeployed after a failed
  10.x deploy. An early migration step commits before the main sync (version-downgrade protection).
  Fix: restore the backup taken before the 10.x deploy, then deploy (**confirmed**).
- **Half-applied schema:** a retry after a failed deploy fails with `ALTER TABLE ... ADD (... BOOLEAN NULL)` /
  `execute_ddl_commands did not succeed` because an earlier attempt already applied part of the update. Fix: restore,
  deploy the old version once, then the new one once (**confirmed**, partly).
- **Oracle 9→10:** `ORA-01408: such column list already indexed` creating
  `IDX_SYSTEM$WORKFLOWUSERTASK_ASSIGNEES_...`. Fix: drop the conflicting index before deploying (**confirmed**, 1 ticket).
- **Toolkit:** new. `steps/report.md` lists "backup and way back" as a grey, unchecked item.
- **Proposed:** a "Production cutover" section in `9-to-10.md` and `10-to-11.md`: rehearse on a full-size production
  copy and time it; the way back is a backup restore, never a package redeploy; after any failed deploy that reached
  the database update, restore before retrying. The pre-deploy backup as a gate item. Baseline/gate records the
  number of update commands and the seconds from "Executing N database synchronization" to finished. Triage probe:
  `count(*)` of InProgress workflow instances. remedies keys:
  `ddl-sync-timeout` match `(?i)Executing \d{3,} database synchronization command|No space left on device|Actuating workflow instances`;
  `db-downgrade` match `(?i)pre-analysis migration version`;
  `ddl-half-applied` match `(?i)execute_ddl_commands did not succeed`;
  `oracle-ora01408` match `ORA-01408`.

## 4. SSO module chain (~10 tickets)

- **SAML20 3.6.x → 4.2.x:** new unique attribute `SAMLRequest.AssertionId`. Existing rows get NULL and the app does
  not start, or logins fail on SQL Server (**confirmed** workaround: delete old SAMLRequest rows before deploy; R&D
  is removing the rule). 4.2.x reads NameID unconditionally:
  `Cannot invoke "org.opensaml.saml.saml2.core.NameID.getValue()" because the return value of "...Subject.getNameID()" is null`
  (**confirmed** fix: an IdP claim rule that always sends NameID). 4.2.3: `KeyNotFoundException: Could not find object
  of type 'SAML20.NameIDFormat'`, fixed in 4.2.4.
- **UserCommons 3.0.0** with current SAML/OIDC: `The selected snippet 'Configuration_Overview' expects an object of
  type 'UserCommons.UserProvisioningHelper'` (**open**: stay on 2.x).
- **OIDC behind a custom domain or reverse proxy:** 4.2.0 lands users on `error-page.html`; NPE in
  `SUB_GetNonceFromCookieAndHash` / `OIDC.CheckNonceValue (JavaAction : 'GenerateSHA256')`. "Get application URL"
  returns the platform URL, not the custom domain, so the nonce cookie and the callback differ (**confirmed** fix: a
  constant with the custom URL). 3.5.0 / 4.4.0 build the redirect URI from `X-Forwarded-*` headers.
- **OIDC 4.1.2 → 4.3.0** loses the configuration: 4.2.1 dropped the UserCommons migration, so going through 4.2.0 is
  required. Already covered by RA-20.
- **Login loop behind a proxy, 10.18 → 10.24.x:** `/xas/` POST returns 401 in a loop, works in incognito.
  10.18.0 takes the cookie `Secure` flag from ApplicationRootUrl; from 10.24.7, `X-Forwarded-Proto: http` sets
  cookies without `Secure` (no `__Host-` prefix) and old cookies collide (**proposed**; 1 ticket).
- **Toolkit:** partial. R1/R2/RA-20 cover up to SAML 4.x / UserCommons 2.x; RA-20 notes the UserCommons 3.0.0 and
  OIDC 5.0.0 notes are unread.
- **Proposed:** a SAML20 4.2.x row (purge `SAML20.SAMLRequest` before deploy; NameID required); a UserCommons 3.0.0
  row `modver:UserCommons:>=3.0.0 && (module:SAML20 || module:OIDC)`; RA-20 `why` addition on X-Forwarded headers.
  remedies matches: `(?i)AssertionId|SAMLRequest.{0,40}(unique|null)`, `(?i)Subject\.getNameID\(\)" is null`,
  `(?i)GetNonceFromCookie|CheckNonceValue|GenerateSHA256.{0,120}NullPointer`.

## 5. Patch releases to avoid (~10 tickets)

| bad from | bad to | fixed in | applies if | symptom | evidence |
|---|---|---|---|---|---|
| 10.24.7 | 10.24.7 | 10.24.8 | project created below 10.17 | `value already present: frn_system$filedocument_system$changedby` at runtime start | confirmed (retracted release) |
| 11.6.0 | 11.6.0 | 11.6.1 | any (wrong build distributed for two weeks) | `No model property found for Java field 'EnableNewStringBehavior'` on Cloud/on-prem | confirmed |
| 11.6.0 | 11.6.2 | 11.6.3 | external (consumed) entity with a Decimal key | `Change of data type or length for key attribute ... is not supported in external entity key` | confirmed by R&D |
| 10.24.14 | 10.24.18 | 10.24.19 | S3 file storage | `Data read has a different checksum than expected` (see 6) | confirmed |
| 10.24.17 | 10.24.19 | 10.24.20 | native, old bundles in the field | sync failures (see 1) | confirmed |
| 11.12.5 | 11.12.5 | 11.12.6 | outgoing client certificates | client certificate not sent | confirmed |

Also: `error: release version 21 not supported` on 11.12 cloud builds was a platform incident in 3 tickets
(**confirmed** resolved); a second cause is a stale `java-version` file (see 9).

- **Toolkit:** partial. SKILL.md LTS-1 / NR2-1 says take the newest patch and read the notes for "do not upgrade",
  but no script checks it, and a source already on 10.24.7 is not flagged.
- **Proposed:** a `playbooks/patch-windows.tsv` with the columns above (`applies_if` as a detect clause), read by
  the target picker (`mxversion.py`): refuse a target inside a window whose condition fires, and flag a source that
  sits in one. remedies match `(?i)value already present: frn_system\$`.

## 6. S3 file storage after the AWS SDK v2 change (4 tickets, all confirmed)

Lands with 10.24.14, and the 11.6 and 9.24 lines (fix versions 11.6.6 / 11.10.0 / 9.24.43).

- `SdkClientException: Unable to load region from any of the providers in the chain` at start: set
  `com.mendix.storage.s3.Region` (Mendix Cloud on Kubernetes sets it, Cloud Foundry does not).
- OCI: `S3Exception: AWS chunked encoding not supported. (Service: S3, Status Code: 501)`: a runtime setting that
  turns chunked encoding off, from 10.24.17 / 11.6.6 / 11.10.0 / 9.24.43 (setting name: take it from the 10.24.17
  release notes, UNVERIFIED here).
- NetApp: `x-amz-content-sha256 must be UNSIGNED-PAYLOAD, ...` (400): environment variables
  `AWS_REQUEST_CHECKSUM_CALCULATION=WHEN_REQUIRED` and `AWS_RESPONSE_CHECKSUM_VALIDATION=WHEN_REQUIRED`.
- `RetryableException: Data read has a different checksum than expected` reading a file in the microflow that created
  it: fixed in 10.24.19.
- **Toolkit:** new (no hits for S3 or storage).
- **Proposed:** triage asks for the storage backend (the model does not hold it); a deploy-environment checklist item;
  remedies key `s3-sdk-v2`, match `(?i)Unable to load region|aws-chunked|x-amz-content-sha256|different checksum than expected`.

## 7. CE1707 in a protected module (4 tickets)

- `CE1707 Internal error in hidden document in protected module 'AdvancedAuditTrail'. This is most likely due to
  changes in its dependencies: ... custom icon identifier 'Atlas_Core.Atlas.trash-can'` with AAT 4.1.1 and Atlas_Core
  4.7.x (R&D-confirmed module bug, fix in release test). The forum workaround "downgrade AAT Core to 3.0.2" leads
  into section 2 on 11.
- The same error for another protected add-on: update the modules its dependency list names (Administration, AAT),
  then rebuild (**confirmed**).
- Advanced Audit Trail with the React client switched on (10.24.15): same error, because its widgets are still Dojo
  (R&D-confirmed): keep the Dojo client.
- **Toolkit:** partial. `steps/repair.md` and `10-to-11.md` cover CE1707 "layout not found" after an add-on swap only.
- **Proposed:** remedies key `ce1707-protected-deps`,
  match `(?i)CE1707.*protected module '([^']+)'.*changes in its dependencies`; a specific key for AAT + Atlas_Core
  icons; a `dojo-successors.tsv` row for Advanced Audit Trail as `module-not-ready` (keep the Dojo client).

## 8. Data Widgets 3 (5 tickets)

- The Data grid 2 configuration attribute (personalisation JSON) is no longer filled on page load in 3.8.1 (it was in
  2.28.1). Intended change; R&D will revert it, no ETA (**confirmed**).
- Others: grids stop rendering as a table after a Data Widgets update; flicker with virtual scrolling plus a
  horizontal scrollbar; updating OIDC pulled in UserCommons, which pulled in Data Widgets and broke grids (mostly
  **open**).
- `dojo-successors.tsv` Signature row says a swap to 2.0.0+ is needed, while a ticket was fixed by signature-web
  1.0.8 without changing the widget id. Recheck that row.
- **Proposed:** remedies key `dw3-config-attr-onload`,
  match `(?i)configurationAttribute|personali[sz]ation.{0,60}(empty|null|not (set|filled))`.

## 9. Single-ticket findings with a confirmed fix

| finding | path | fix | proposed target |
|---|---|---|---|
| Stale `java-version` file in the project root still says 11; cloud build fails though the model says 21 | 10.18→10.24 | delete the file (from 10.8 the model setting rules) | replacements row, detect `file:^java-version$` (needs the new `file:` kind) |
| `deployment/sass` committed to git: `Can't find stylesheet to import ... @use "Atlas_Core.Atlas.scss"` | 9.24→10.24 | delete `deployment/`, on every branch | triage check `git:^deployment/` (needs the new `git:` kind) |
| `parseDateTime` strict from 10.0: `Unparseable date` (patterns with `YYYY`, `DD`) | 9→10 | correct the pattern; bridge with `com.mendix.core.LenientDateTimeParsing = true` | replacements row, detect `expr:parseDateTime(UTC)?\([^)]*'[^']*(YYYY\|\bDD\b)` |
| Published REST returns 401 without `WWW-Authenticate` when basic auth is off; challenge-first clients (PowerShell `-Credential`) stop authenticating | crossing 10.22 | callers send `Authorization: Basic` up front | behaviour list in 9-to-10 / 10-to-11 |
| FileDocuments created before 5.12 block the 11 start: `There are still file documents on the local file system which are created before Mendix 5.12` | 10.24→11.12 | finish the migration on 10.24 (placeholder files for rows without `__UUID__`) or delete obsolete FileDocuments | triage SQL probe on the frozen baseline DB; remedies `to:>=11.0` |
| Atlas_Core 3.19: topbar submenu opens but cannot be clicked in a custom layout without class `layout-atlas` | Atlas 3.18→3.19 | add the `.region-topbar` z-index rule to own SCSS | replacements row `modver:Atlas_Core:>=3.19.0` |
| Upgrade-added `_scroll-container-react.scss` block (`.region-content { display:flex ...}`) breaks the Pop-up Menu position; absent in a fresh app | 10.19→10.24 React | remove the block | widget-render row; theme grep |
| Text-template parameter still points at `$currentObject` after the container became a data grid: `Did not expect an argument to be undefined.` | →11.12 | re-select the parameter source | remedies match on the console error |
| Email Connector rich-text links URL-encode placeholders (`{%1%}` → `%7B%25`) | →11.12 | update the Rich Text widget | replacements risk on Email Connector |
| Document Templates: `The entity "nbsp" was referenced, but not declared` (external entities forbidden since 9.10) | 9.6→9.24 | numeric entities (`&#160;`) | R6 `unchecked` |
| Native Gallery blank with Data Widgets latest on 11.12.2 | →11.12 | Gallery size "Maximum space"; fixed in Native Mobile Resources 12.5.1 | R23 detect `modver:NativeMobileResources:<12.5.1` |
| Runtime uniqueness data blocks the 9 start: `Since Mendix 9, only Database Uniqueness Validation is supported` | 7→9 | go via 8, clean data there | out of scope (9+) unless a pre-9 playbook is planned |

Open or weak, not proposed as rows: import mapping leaves attributes empty and skips conversion microflows from
9.24.35 (2 tickets, silent data risk, worth an R30-style behaviour row even while open); Reporting widgets removed
in 10 with no direct replacement (2 tickets); OIDC `401 access_denied` at `handleAuthorizationCode` after
9.24.16→10.24 (3 tickets, no root cause).

## 10. A finding against mxcli itself

A model written by mxcli crashed Studio Pro 11.9 on save and on MPK export:
`System.InvalidOperationException: Null value found in primitive property 'ImageDataStorage' of object of type
'Mendix.Modeler.CodeActions.MicroflowActionInfo'` (mendixlabs/mxcli#656; the customer found the cause). This
toolkit writes the model with mxcli too. **Proposed:** a `steps/repair.md` row, and a gate check after any mxcli
write that the target `mx` can still save and export the MPK.

---

## Four structural changes the sweep points to

1. **`playbooks/patch-windows.tsv`** read by the target picker (section 5). Turns the "read the notes" rule into a
   check and serves sections 1 and 6 too.
2. **A deploy-environment triage step** for what the model cannot show: database size and rows to update, the
   file-storage backend, proxy headers (`X-Forwarded-*`), whether old native builds are in the field, and the
   pre-deploy backup as a gate item (sections 1, 3, 4, 6).
3. **Two new detect kinds** in `bin/replacement_check.py`: `file:REGEX` (a path relative to the project) and
   `git:REGEX` (`git ls-files`) (section 9).
4. **remedies rows matched on runtime log strings** (`pre-analysis migration version`, `value already present:
   frn_system$`, `Unable to load region`, `op-sqlite`, ...), so a failed start maps straight to the right row.

## How to verify (proposed experiments, cheapest first)

1. **Backtest the remedies regexes against the ticket corpus.** Run each proposed `match` over all 242 ticket texts;
   it must fire on its own issue's tickets and stay quiet on the rest. Gives precision and recall per row before
   anything ships. The corpus stays outside the repo (internal data).
2. **Static detect controls.** One fixture per new detect rule (removed Java API calls, `java-version` file,
   committed `deployment/`, `parseDateTime` with `YYYY`, module minimums), run through `replacement_check.py`: a catch
   case and a pass case, as every existing control.
3. **Runtime reproductions on the local Docker stack** (FSM example or GAMI):
   - start 10.24 on a 9.24 DB copy, then 9.24 on the same DB: expect `pre-analysis migration version`;
   - seed with `seed_pg` at 10×, 100×, 1000× rows and record update commands and seconds: a size-to-time curve to
     warn on;
   - insert a FileDocument row with `__FileName__` set and `__UUID__` NULL, start 11.12: expect the 5.12 error;
   - SAML20 4.2.4 with existing `SAMLRequest` rows: expect the unique-constraint failure;
   - S3 against a local MinIO without Region, then behind a proxy that rejects chunked uploads;
   - the target picker refuses each `patch-windows.tsv` row whose condition holds.
4. **Native upgrade-over-install on an emulator:** install the source-version build, create offline data, install
   the target build over it without uninstalling, sync, grep the device log for `op-sqlite`. A MANUAL gate item until
   automated.
5. **Field confirmation:** `FIELD-RUNS.md` records which new rows fired on a run and whether the hit was real. A row
   stays `UNVERIFIED` until a reproduction or a field run confirms it.
