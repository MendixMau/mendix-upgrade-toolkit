---
title: "Mx9 -> Mx10/11: differences an old-vs-new comparison shows that are not regressions"
topic: upgrade
keywords: ["openapi.json", "swagger.json", "rest-doc", "LicenseService", "trial license", "ClusterManagerActionInterval", "SessionKeepAliveUpdatesInterval", "SessionTimeout", "MendixSSO", "MxModelReflection", "data compare", "regression test", "false positive"]
domain: [upgrade, testing]
kind: reference
applies_to: mendix-general
versions: "9.24 -> 10.24 -> 11.12 (observed); likely any 9.x -> 10.x"
layer: field
sources:
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed
---
**Use:** when you compare an app before and after an upgrade (start log, published endpoints, database contents), these rows
showed up on a 9.24 app and are platform or tooling changes, so expect them on others. They are expected. List them as notes, do not file them as regressions.

| what the compare shows | why it is expected | how to tell it apart from a real problem |
|---|---|---|
| `/rest-doc/<service>/openapi.json` was 404, is 200 now | 10.x serves the published REST docs in the OpenAPI 3 format next to the existing `swagger.json` | the same service's `swagger.json` answered 2xx on the old app. Without that, it is a new endpoint |
| start-log WARNING `LicenseService: The runtime has been started using a trial license...` is new | 9.24 logs the same line under the logger `Core`; only the logger name changed | the message text is identical to an old WARNING. Other text under a renamed logger is not covered |
| start-log WARNING `Using derived value for ClusterManagerActionInterval ... based on SessionTimeout` (and `SessionKeepAliveUpdatesInterval ... based on ClusterManagerActionInterval`) | the newer runtime derives these intervals when `SessionTimeout` is short. A test harness that starts the app with a short session timeout causes it | the app (or the harness) sets a short `SessionTimeout`. On production settings, check the real value |
| data: `MendixSSO` or `MxModelReflection` entity attributes gone or with other values | those Marketplace modules change their own entities when they are updated to the version the new Mendix needs; `MxModelReflection` also refills its tables at start | the change is limited to the module that was updated, and no rows of your own entities are lost |
| data: the admin user's `changedDate` or password columns differ | any test tool that signs in as the admin resets the password at start | only the one admin row differs; other `System.User` rows are equal |

**Rule:** a failure only counts as a regression when it worked on the old app and broke on the new one. A check that
fails on both apps is a note for the owner, not an issue.

The upgrade toolkit applies these rules itself (`diff.py`, `logdiff.py`, `heal.py`, `gate.sh`) and prints each as PASS*
with its reason.
