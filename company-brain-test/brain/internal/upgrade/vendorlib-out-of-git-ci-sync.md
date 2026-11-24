---
title: Removing vendorlib JARs from Git and syncing dependencies in CI
topic: upgrade
domain: [devops-cloud]
kind: procedure
applies_to: company-standard
versions: "Mx10.20+ (mx sync-java-dependencies)"
keywords: ["mx sync-java-dependencies", "vendorlib gitignore", "init.gradle", "custom repositories CI", "GitLab CI dependency sync", "Sigrid analysis", "private Maven repository pipeline", "JARs in version control", "Gradle home init script", "managed dependencies CI"]
layer: field
sources:
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed
---
**When**
- Only for teams experienced with dependency management and GitLab CI. Otherwise the source advises keeping JARs in version control (the default).
- Motive: JARs are not source code; they use GitLab space and slow checkouts/commits.

**Steps**
1. Add the `vendorlib` contents (at least the JARs) to `.gitignore`.
2. If you use custom repositories (e.g. a private Maven repository), create an init script in the pipeline before syncing:
```
- mkdir -p "$HOME/.gradle"
- |
    cat > "$HOME/.gradle/init.gradle" << 'EOF'
    allprojects {
        repositories {
            gradlePluginPortal()
            mavenCentral()
            maven { url '<your-maven-repository-url>' }
        }
    }
    EOF
```
3. Run `mx sync-java-dependencies ${MPR_FILENAME}` before the app is built or analysed (e.g. Sigrid).
4. Locally, Studio Pro's sync still populates `vendorlib`.

**Checks**
- Pipeline build and analysis find all JARs.

**Watch out**
- The CLI ignores Studio Pro's IDE-level custom repository config; without `init.gradle` it cannot resolve from a private repository.

