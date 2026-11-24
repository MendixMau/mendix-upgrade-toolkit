# Community Commons (Marketplace component 170)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/170)

| version | published | min Mendix |
|---|---|---|
| 11.5.1 | 2026-05-19 | 10.24.0 |
| 11.5.0 | 2026-01-13 | 10.24.0 |
| 11.4.0 | 2025-11-19 | 10.24.0 |
| 11.3.0 | 2025-07-24 | 10.21.0 |
| 11.2.0 | 2025-07-03 | 10.21.0 |
| 11.1.0 | 2025-04-28 | 10.21.0 |
| 11.0.0 | 2025-04-10 | 10.21.0 |
| 10.4.2 | 2026-05-19 | 9.24.36 |
| 10.4.1 | 2026-01-15 | 9.24.36 |
| 10.4.0 | 2025-07-25 | 9.24.36 |
| 10.3.0 | 2025-07-18 | 9.24.36 |
| 10.2.0 | 2025-04-28 | 9.18.0 |
| 10.1.3 | 2025-04-10 | 9.18.0 |
| 10.1.2 | 2025-03-27 | 9.18.0 |
| 10.1.1 | 2025-03-18 | 9.18.0 |
| 10.1.0 | 2025-01-06 | 9.18.0 |
| 10.0.7 | 2024-10-14 | 9.18.0 |
| 10.0.6 | 2024-07-04 | 9.18.0 |
| 10.0.5 | 2024-01-04 | 9.18.0 |
| 10.0.2 | 2023-08-22 | 9.18.0 |
| 10.0.1 | 2023-06-30 | 9.18.0 |
| 10.0.0 | 2023-04-14 | 9.18.0 |
| 9.0.4 | 2023-12-06 | 8.12.0 |
| 9.0.3 | 2023-06-30 | 8.12.0 |
| 9.0.2 | 2022-10-10 | 8.12.0 |
| 9.0.1 | 2022-06-22 | 8.12.0 |
| 9.0.0 | 2022-01-12 | 8.12.0 |
| 8.8.2 | 2023-07-11 | 7.23.22 |
| 8.8.1 | 2023-02-16 | 7.23.22 |
| 8.8.0 | 2022-01-13 | 7.23.22 |
| 8.7.0 | 2021-11-08 | 8.12.0 |
| 8.6.0 | 2021-09-27 | 8.12.0 |
| 8.5.0 | 2021-06-28 | 8.12.0 |
| 8.4.0 | 2021-05-24 | 8.12.0 |
| 8.3.1 | 2020-12-21 | 8.12.0 |
| 8.3.0 | 2020-12-18 | 8.12.0 |
| 8.2.1 | 2021-07-01 | 7.23.22 |
| 8.2.0 | 2019-12-20 | 7.23.6 |
| 8.1.0 | 2019-08-29 | 7.23.6 |
| 8.0.1 | 2019-06-27 | 7.23.4 |
| … 12 older versions | | |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 11.5.1 | improvement | Upgraded pdfbox to 3.0.7 | pdfbox |  |
| 11.5.0 | improvement | Upgraded guava to 33.5.0-jre | guava |  |
| 11.5.0 | improvement | Upgraded owasp-java-html-sanitizer to 20260101.1 | owasp-java-html-sanitizer |  |
| 11.5.0 | improvement | Upgraded commons-io to 2.21.0 | commons-io |  |
| 11.5.0 | improvement | Upgraded pdfbox to 3.0.6 | pdfbox |  |
| 11.5.0 | improvement | Upgraded commons-lang3 to 3.20.0 | commons-lang3 |  |
| 11.5.0 | improvement | Upgraded commons-text to 1.14.0 | commons-text |  |
| 11.5.0 | feature | Added the pdfbox-io 3.0.6 dependency | pdfbox-io |  |
| 11.4.0 | requirement | Upgraded the module to 10.24.0 |  |  |
| 11.3.0 | security | Upgraded Commons-lang3 library to version 3.18.0 to resolve CVE-2025-48924 | commons-lang3 |  |
| 11.1.0 | improvement | Upgraded Guava dependency to 33.4.7, removes jsr305 version 3.0.2 dependency causing code quality scanning issues | guava, jsr305 |  |
| 11.0.0 | requirement | Upgraded the Community Commons module to Mendix version 10.21.0 |  |  |
| 11.0.0 | deprecation | Deprecated Misc.getRuntimeVersion Java method, use Core.getRuntimeVersion instead | Misc.getRuntimeVersion | Core.getRuntimeVersion |
| 11.0.0 | deprecation | Deprecated Misc.getModelVersion Java method, use Core.getModelVersion instead | Misc.getModelVersion | Core.getModelVersion |
| 10.4.2 | improvement | Upgraded pdfbox to 2.0.36 | pdfbox |  |
| 10.4.1 | improvement | Upgraded owasp-java-html-sanitizer to 20260101.1 | owasp-java-html-sanitizer |  |
| 10.4.0 | security | Upgraded Commons-lang3 library to version 3.18.0 to resolve CVE-2025-48924 | commons-lang3 |  |
| 10.3.0 | requirement | Upgraded the Community Commons module to Mendix version 9.24.36 |  |  |
| 10.2.0 | improvement | Upgraded Guava dependency to 33.4.7, removes jsr305 version 3.0.2 dependency causing code quality scanning issues | guava, jsr305 |  |
| 10.1.0 | deprecation | Deprecated the 'length' parameter of the StringUtils Hash java action. Hash length will always be 32 bytes, 64 hex characters | StringUtils Hash |  |
| 10.0.7 | improvement | Updated the Apache Commons IO dependency to 2.17.0 | commons-io |  |
| 10.0.5 | improvement | Updated the Apache PDFBox dependency to 2.0.30 | pdfbox |  |
| 10.0.2 | migration-step | Included a migration file for the Java dependencies for Studio Pro 10 compatibility |  |  |
| 10.0.1 | improvement | Updated the Guava dependency to 32.0.1 | guava |  |
| 10.0.0 | requirement | Updated the module to Studio Pro 9.18, so it can be used in Studio Pro 10 |  |  |
| 10.0.0 | improvement | Updated the Apache Commons Lang dependency to version 3.12.0 | commons-lang |  |
| 10.0.0 | feature | Added a dependency on Apache Commons Text version 1.10.0 because some Apache Commons Lang functionality moved there | commons-text |  |
| 9.0.4 | improvement | Updated the Apache PDFBox dependency to 2.0.30 | pdfbox |  |
| 9.0.3 | improvement | Updated the Guava dependency to 32.0.1 | guava |  |
| 9.0.1 | improvement | Upgrade commons-io dependency from 2.8.0 to 2.11.0 | commons-io |  |
| 9.0.0 | removal | Removed encrypt/decrypt functionality. Java Actions EncryptString, DecryptString, and encryptMembersIfChanged have been removed | EncryptString, DecryptString, encryptMembersIfChanged |  |
| 8.8.2 | improvement | Updated the Guava dependency to 32.0.1 | guava |  |
| 8.8.1 | improvement | Updated Apache Commons from 2.8.0 to 2.11.0 | commons-io |  |
| 8.8.0 | improvement | Updated the OWASP Java HTML Sanitizer dependency | owasp-java-html-sanitizer |  |
| 8.7.0 | improvement | Updated owasp-java-html-sanitizer to 20211018.2 | owasp-java-html-sanitizer |  |
| 8.7.0 | deprecation | Deprecated all encryption related functionality. Use the encryption-module instead |  |  |
| 8.5.0 | improvement | Updated Guava to 30.1.1 to be the same version as used by the SSO module | guava |  |
| 8.5.0 | security | Updated PDFBox to 2.0.24 because of a vulnerability in that library | pdfbox |  |
| 8.4.0 | improvement | Updated library dependencies. Community Commons ships with Apache Commons IO 2.8, Apache Commons Lang 3.11, Guava 30.0 | commons-io, commons-lang, guava |  |
| 8.3.1 | requirement | Updated the Community Commons module to support Mendix Studio Version 9 |  |  |
| 8.3.0 | requirement | Updated the Community Commons module to Mendix Studio Pro 8.12.0 |  |  |
| 8.2.1 | improvement | Updated library dependencies. Community Commons ships with Apache Commons IO 2.8, Apache Commons Lang 3.11, Guava 30.0, PDFBox 2.0.24 | commons-io, commons-lang, guava, pdfbox |  |
| 8.1.0 | requirement | Minimum required Mendix version is 7.23.6 |  |  |
| 8.1.0 | breaking | Changed Logging.java so TimerEnd now returns the time taken in milliseconds | Logging.TimerEnd |  |
| 8.0.1 | removal | Removed the deprecated RegexTest action. Use the isMatch() function in microflow expressions instead | RegexTest | isMatch() |
| 8.0.1 | breaking | Changed Java references to the LogNodes.CommunityCommons enum to point to the name instead of the caption |  |  |
| 8.0.0 | requirement | Converted to Mendix 7.23.4 |  |  |
| 7.4.0 | security | Updated Guava dependency to 27.0 in order to fix a security vulnerability warning | guava |  |
| 7.4.0 | migration-step | Delete all jar files that have a `.CommunityCommons.Required` flag before upgrading |  |  |
| 7.3.0 | removal | Removed deprecated Log action | Log |  |
| 7.3.0 | removal | Removed deprecated SimpleLog action | SimpleLog |  |
| 7.3.0 | removal | Removed deprecated StringLength action | StringLength |  |
| 7.3.0 | improvement | Upgraded PDFBox dependency to 2.0.13. Delete pdfbox-2.0.11.jar and fontbox-2.0.11.jar from userlib before upgrading | pdfbox |  |
| 7.2.0 | migration-step | Delete all `.jar` files from userlib with accompanying `.CommunityCommons.RequiredLib` file before upgrading |  |  |
| 7.2.0 | improvement | Updated and reduced dependencies on third-party libraries to mitigate potential security vulnerabilities |  |  |
| 7.2.0 | breaking | Re-implemented the XSSSanitize action which will require you to re-implement the call if you use it | XSSSanitize |  |
| 7.1.0 | removal | Removed session based locking mechanism as it has become obsolete in Mx7 |  |  |
| 6.3.1 | fix | Added Batik library not provided by Mendix Runtime for Mendix 7. Fixes NoClassDefined error when using Sanitize function. | Batik library |  |
| 6.3.0 | requirement | Module converted to Mendix 7.1.0. |  |  |
| 6.3.0 | migration-step | Added jar which is not provided by runtime anymore in Mendix 7. |  |  |
