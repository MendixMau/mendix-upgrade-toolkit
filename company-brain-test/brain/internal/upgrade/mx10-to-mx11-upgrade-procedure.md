---
title: Upgrading an app from Mx10 to Mx11
topic: upgrade
domain: [delivery-process]
kind: procedure
applies_to: mendix-general
versions: "10.24.latest -> 11.x (11.9.1 and 11.12 field runs)"
keywords: ["Mx10 to Mx11 upgrade", "10.24 to 11.x migration", "Deeplink replacement", "userlib JAR eviction", "module incompatibility", "string behavior runtime", "Dojo client replacement", "native app store rebuild", "Document Templates conflict", "java-version conversion"]
layer: field
sources:
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed
---
**When**
- An app on Mx10.
- Scope the migration to required changes only. Adopt new features in a separate epic.

**Steps**
1. Convert to 10.24.latest. Run, click through, and commit.
2. Replace Deeplink with page/microflow URLs.
3. Fix model and Java deprecations. Two ways to find them:
   - A widget compatibility scan. Scanners of this kind are experimental and give false positives.
   - A trial Mx11 build, to see the compile errors.
   - For errors in Marketplace modules, try the latest module version first. In one run that did not help; see [[mx11-java-api-rewrites]].
4. Check widgets with a compatibility scan and replace Dojo widgets that have no React version.
5. Create a branch with a clean 10.24 snapshot. Conversion is irreversible.
6. Convert to 11.x. Record every error before fixing anything.
7. Remove `userlib` JARs that duplicate `vendorlib`.
8. Fix errors in order: model, then Java, then SCSS.
9. Test and fix.

**Checks**
- Private constants have values. In one run, `MyModule.CLIENT_SECRET` gave an error on conversion.
- Enable "Use new string behavior" in runtime settings. The old behavior is removed in Mx12.
- Module incompatibility warnings are resolved. Example: NanoflowCommons 5.2.0 was flagged incompatible; upgrade to 7.2.0.
- Java: the 11.9.1 run stayed on Java 21, and the `java-version` file survived conversion.
- Deployment config: the `-Djava.security.manager` JVM parameter is removed in Mx11. This comes from research, not a field run.

**Watch out**
- Order module pick-ups by dependency.
- Decide the client mode up front: [[mx11-keep-dojo-client-during-upgrade]].
- Native apps need a full store rebuild and resubmission. OTA updates do not work across majors.
- Document Templates: sources conflict. The stub says removed in 11; the plan and its table say unconfirmed. Check usage and verify before upgrading.
- [[mx11-java-api-rewrites]], [[mx11-file-orphans-block-start]], [[mx11-scss-import-deprecation-non-blocking]], [[git-node-modules-and-mass-deletions-crash-studio-pro]]

**Release notes**
- 11.0.0: apps must be ≥ 10.21.0 to open and convert (https://docs.mendix.com/releasenotes/studio-pro/11.0/#1100-general-availability)
- 11.0.0: string concatenation of empty/null values changed (https://docs.mendix.com/releasenotes/studio-pro/11.0/#1100-general-availability)
