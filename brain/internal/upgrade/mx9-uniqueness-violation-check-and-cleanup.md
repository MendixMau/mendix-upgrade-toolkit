---
title: Check and clean up uniqueness violations before moving an app to Mx9
topic: upgrade
domain: [data-modeling, delivery-process]
kind: procedure
applies_to: mendix-general
versions: "Mx8 -> Mx9 (apps with Uniqueness validation = Runtime)"
keywords: ["uniqueness validation", "Mx9 upgrade", "Detected unique constraint violation", "runtime uniqueness", "DataStorage.EnableDiagnostics", "StartAttributeMigrationPage", "StartAssociationMigrationPage", "1-1 association violation", "cleanup tool Postgres", "Mx8 to Mx9"]
layer: field
sources:
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed
---
**When**
- Before the Mx8→9 upgrade. Mx9 checks uniqueness in the database; if production data breaks a rule, the app will not start on Mx9.
- Bad data arises when, with Runtime validation, a unique rule was added after data existed, or an association was narrowed to 1 (e.g. 1-* → 1-1) after data existed. Runtime just returned the first associated object.
- Apps built before 7.13 are most at risk (default Runtime before 7.13, Database from 7.13).
- Fixing data is slow; plan early.

**Steps**
1. In the Mx8 app, check runtime setting "Uniqueness validation". Database → done. Runtime → continue.
2. Detect bad data, with a DB as close to prod as possible (a snapshot can miss offending rows):
   - a. set custom setting `DataStorage.EnableDiagnostics = true` and restart; or
   - b. set Uniqueness validation to Database and try to start.
   - Look for `An error occurred while initializing the Runtime: Detected unique constraint violation…`
3. Request the cleanup tool from Mendix Support.
4. Add it to the Mx8 app. Put `StartAttributeMigrationPage` and `StartAssociationMigrationPage` in navigation, admin-only.
5. Run on a prod-like test DB with Uniqueness validation = Runtime.
6. Open each page and click an object to see its conflicts:
   - attribute page: objects with the same value; edit (e.g. "Mark" → "Mark2") or delete;
   - association page: objects linked to one side of a 1-1 or *-1 association; keep one link, remove the rest.
7. Fixed objects drop out of the grids. Empty grids mean the data is clean.
8. Repeat step 2 to confirm.
9. Deploy the Mx8 version with the tool to production and repeat steps 5–8 there (manual prod data edits).

**Checks**
- Step 2 gives no violation logs.
- The app starts with Uniqueness validation = Database.

**Watch out**
- Tool instructions say Postgres only. It was tested on SQL Server and it worked. It does not work on HSQL.

**Release notes**
- 9.0.5: runtime uniqueness validation removed (https://docs.mendix.com/releasenotes/studio-pro/9.0/#905)
- 10.0.0: the custom setting was removed; database validation is mandatory (https://docs.mendix.com/releasenotes/studio-pro/10.0/#1000)
