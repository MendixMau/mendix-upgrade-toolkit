---
title: Migrating userlib JARs to managed dependencies (vendorlib)
topic: upgrade
domain: [devops-cloud, delivery-process]
kind: procedure
applies_to: company-standard
versions: "Mx10+"
keywords: ["userlib migration", "vendorlib", "managed dependencies", "dependency-analysis script", "Java Dependencies", "ClassNotFound error", "com.mendix.databroker", "Marketplace module userlib", "transitive dependencies", "userlib to vendorlib"]
layer: field
sources:
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed
---
**When**
- An Mx10+ app still has JARs in `userlib`.

**Steps**
1. Find each module's direct dependencies.
   - Preferred: a dependency-analysis script that maps each JAR to its Maven coordinates. It can run locally, in Docker, or in CI.
2. By hand: collect imports per module (Actions and implementation classes). Ignore:
   - JVM: `java.*`, `javax.*`, `jdk.*`, `org.w3c.*`, `org.xml.sax.*`, `sun.*`;
   - runtime: `com.mendix.core.*`, `.logging.*`, `.systemwideinterfaces.*`, `.webui.*`, `.m2ee.api.*`, `.datastorage.*`, `.externalinterface.*`, `.http.*`, `.thirdparty.*`;
   - your own code.
3. Map packages to JARs. Check `META-INF/MANIFEST.MF` or `META-INF/maven/**/pom.xml` for Maven coordinates, or the JAR's folder structure.
4. In each module's Settings, add Java Dependencies. Sync.
5. Move `userlib` contents out of the project; do not delete yet.
6. Build. A missing direct dependency shows as a compile error.
7. Full regression test. Wrong versions and missing transitive dependencies only show at runtime; check logs for stack traces.

**Checks**
- Compiles; regression passes; no ClassNotFound-type errors in logs.

**Watch out**
- `com.mendix.databroker.*` is NOT in the runtime; it comes with the Business Events module.
- Some modules need a reinstall to find their dependencies (Mendix SSO on Mx10).
- Marketplace modules still shipping JARs to `userlib`: the source prefers converting them anyway. On each update:
  1. update from Marketplace (JARs land in `userlib`);
  2. analyse direct dependencies with the script;
  3. configure them in module settings;
  4. empty `userlib`;
  5. test.
  Mark such modules as customized (knowledge base or folder name).
- [[vendorlib-out-of-git-ci-sync]]
