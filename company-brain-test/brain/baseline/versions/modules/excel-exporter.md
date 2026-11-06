# Excel Exporter (Marketplace component 726)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/726)

| version | published | min Mendix |
|---|---|---|
| 8.3.2 | 2026-07-29 | 10.24.11 |
| 8.3.1 | 2026-06-09 | 10.24.11 |
| 8.3.0 | 2026-05-18 | 10.24.11 |
| 8.2.3 | 2026-04-27 | 10.24.11 |
| 8.2.2 | 2026-03-16 | 10.24.11 |
| 8.2.1 | 2026-01-28 | 10.24.11 |
| 8.2.0 | 2025-12-15 | 10.24.11 |
| 8.1.3 | 2025-11-07 | 10.21.0 |
| 8.1.2 | 2025-07-15 | 10.21.0 |
| 8.1.1 | 2025-06-06 | 10.21.0 |
| 8.1.0 | 2025-04-28 | 10.21.0 |
| 8.0.0 | 2025-01-31 | 10.12.10 |
| 7.5.9 | 2026-06-09 | 9.24.11 |
| 7.5.8 | 2026-04-27 | 9.24.11 |
| 7.5.7 | 2025-11-07 | 9.24.11 |
| 7.5.6 | 2025-07-21 | 9.24.11 |
| 7.5.5 | 2025-06-12 | 9.24.11 |
| 7.5.4 | 2025-01-15 | 9.24.11 |
| 7.5.3 | 2025-01-07 | 9.24.11 |
| 7.5.2 | 2024-11-22 | 9.24.11 |
| 7.5.1 | 2024-08-09 | 9.24.11 |
| 7.5.0 | 2024-08-02 | 9.24.11 |
| 7.4.1 | 2024-03-07 | 9.24.11 |
| 7.4.0 | 2023-11-08 | 9.24.11 |
| 7.3.0 | 2023-09-27 | 9.18.4 |
| 7.2.0 | 2023-08-02 | 9.18.4 |
| 7.1.1 | 2023-05-30 | 9.18.4 |
| 7.1.0 | 2023-04-07 | 9.18.4 |
| 7.0.5 | 2022-11-29 | 9.0.5 |
| 7.0.4 | 2022-05-27 | 9.0.5 |
| 7.0.3 | 2022-02-09 | 9.0.5 |
| 7.0.2 | 2021-11-02 | 9.0.5 |
| 7.0.1 | 2021-09-20 | 9.0.5 |
| 7.0.0 | 2021-06-01 | 9.0.5 |
| 6.1.6 | 2025-07-09 | 8.12.5 |
| 6.1.5 | 2023-05-30 | 8.12.5 |
| 6.1.4 | 2022-06-01 | 8.12.5 |
| 6.1.3 | 2021-09-20 | 8.12.5 |
| 6.1.2 | 2021-02-05 | 8.12.5 |
| 6.1.1 | 2020-12-31 | 8.12.0 |
| … 11 older versions | | |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 8.3.1 | requirement | Updated log4j-api to latest 2.25.+ version. | log4j-api |  |
| 8.3.1 | requirement | Upgraded Data Widgets to v3.10.0. | Data Widgets |  |
| 8.3.0 | security | Added sanitization for formula injection in excel/csv export to prevent security vulnerabilities [#277915]. |  |  |
| 8.2.2 | requirement | Update log4j-api v2.24.3 to v2.25.3 [#271452]. | log4j-api |  |
| 8.2.0 | requirement | Upgraded module to Studio Pro v10.24.11. |  |  |
| 8.1.2 | requirement | Upgraded opencsv jar to v5.11.2. | opencsv |  |
| 8.1.0 | requirement | Updated studio pro minimum version to 10.21.0 to support Mendix 11. |  |  |
| 8.1.0 | requirement | Updated Atlas core, Data widgets, Nanoflow commons to latest version. | Atlas Core, Data Widgets, Nanoflow Commons |  |
| 8.0.0 | requirement | Upgraded the module to Mendix version 10.12.10. |  |  |
| 8.0.0 | breaking | Replaced old UI components with new ones compatible with the React Client. |  |  |
| 8.0.0 | requirement | Upgraded the Combobox widget to v2.1.3. | Combobox |  |
| 8.0.0 | requirement | Upgraded Data Widgets to v2.29.1. | Data Widgets |  |
| 7.5.8 | security | Fix vulnerability CVE-2025-68161 log4j-api jar [#275070]. | log4j-api |  |
| 7.5.6 | requirement | Upgraded opencsv jar to v5.11.2. | opencsv |  |
| 7.5.6 | requirement | Upgraded commons-lang3 jar to v3.18.0. | commons-lang3 |  |
| 7.5.5 | requirement | Upgraded Apache poi ooxml jar version to v5.4.0. | poi-ooxml |  |
| 7.5.5 | requirement | Upgraded combo box to v1.7.1. | Combobox |  |
| 7.5.2 | requirement | Updated the Apache Commons IO dependency to 2.17.0. | Apache Commons IO |  |
| 7.5.0 | requirement | Apache poi library update to 5.3.0 mitigate vulnerabilities in 5.2.5 due to commons-compress. | Apache poi |  |
| 7.5.0 | improvement | Improved performance for exporting Excel (2007 and higher) including Macro enabled files. |  |  |
| 7.4.1 | security | Mitigated CVE-2024-25710 by updating third-party dependencies. |  |  |
| 7.4.0 | requirement | Upgraded module to Mendix version 9.24.11. |  |  |
| 7.3.0 | migration-step | Introduction of migration file for JDM. |  |  |
| 7.2.0 | breaking | Sheet name is now a mandatory field during template creation. |  |  |
| 7.2.0 | breaking | Naming of JARs in userlib is aligned to only have JAR name without prefix of package. |  |  |
| 7.1.1 | requirement | Upgraded MxModelReflection module from version 6.2.0 to 7.0.0. | MxModelReflection |  |
| 7.1.0 | requirement | Updated module to Mendix version 9.18.4. |  |  |
| 7.0.5 | security | Upgraded opencsv-5.7.1.jar to fix CVE-2022-42889. | opencsv |  |
| 7.0.4 | removal | Removed unused attribute NameAsHeader from MxColumn entity. | MxColumn |  |
| 7.0.4 | requirement | Upgraded poi-ooxml from 4.1.2 to 5.2.2 to fix common vulnerabilities and exposures. | poi-ooxml |  |
| 7.0.2 | requirement | Upgraded joda-time from 2.10.9 to 2.10.10. | joda-time |  |
| 7.0.2 | requirement | Upgraded opencsv from 5.3 to 5.4. | opencsv |  |
| 7.0.1 | requirement | Using commons-compress 1.21 and updated dependencies. | commons-compress |  |
| 7.0.1 | breaking | Removed Excel Importer, re-imported Atlas Core. | Excel Importer |  |
| 7.0.0 | requirement | This version supports Mendix 9.0.5 and higher. |  |  |
| 7.0.0 | requirement | This version is compatible with Atlas Core 3.0.2. | Atlas Core |  |
| 6.1.6 | requirement | Upgraded opencsv jar to v5.11.2. | opencsv |  |
| 6.1.6 | requirement | Upgraded poi-ooxml to v5.4.0. | poi-ooxml |  |
| 6.1.5 | security | Upgraded opencsv JAR to version 5.7.1 to fix CVE-2022-42889. | opencsv |  |
| 6.1.4 | requirement | Upgraded poi-ooxml from 4.1.2 to 5.2.2 to fix common vulnerabilities and exposures. | poi-ooxml |  |
| 6.1.4 | requirement | Related dependencies were also upgraded. |  |  |
| 6.1.4 | removal | Removed unused attribute NameAsHeader from MxColumn entity. | MxColumn |  |
| 6.1.3 | requirement | Jars updated. |  |  |
| 6.1.2 | requirement | Upgraded apache poi from 4.1.1 to 4.1.2. | poi |  |
| 6.1.2 | requirement | Upgraded joda time from 2.10.5 to 2.10.9. | joda-time |  |
| 6.1.2 | requirement | Upgraded opencsv from 5.0 to 5.3. | opencsv |  |
| 6.1.2 | breaking | Renamed userlib jars: commons-codec-1.13.jar to commons-codec.commons-codec-1.13.jar. |  |  |
| 6.1.2 | breaking | Renamed userlib jars: commons-collections4-4.4.jar to org.apache.commons.commons-collections4-4.4.jar. |  |  |
| 6.1.2 | breaking | Renamed userlib jars: commons-compress-1.19.jar to org.apache.commons.commons-compress-1.19.jar. |  |  |
| 6.1.2 | breaking | Renamed userlib jars: commons-math3-3.6.1.jar to org.apache.commons.commons-math3-3.6.1.jar. |  |  |
| 6.1.1 | requirement | Upgraded replication.jar. |  |  |
| 6.1.0 | requirement | This version is compatible with Mendix 8.12.0 and later versions. |  |  |
| 6.0.6 | requirement | Jars updated. |  |  |
| 6.0.5 | requirement | Updated commons-codec 1.11 to 1.13 (used by poi 4.1.1). | commons-codec |  |
| 6.0.5 | requirement | Updated commons-collections4 4.2 to 4.4 (used by poi 4.1.1). | commons-collections4 |  |
| 6.0.5 | security | Updated commons-compress 1.18 (CVE) to 1.19. | commons-compress |  |
| 6.0.5 | requirement | Updated commons-io 2.3 to 2.6. | commons-io |  |
| 6.0.5 | requirement | Updated commons-lang3 3.1.0 to 3.9 (used by commons-codec and commons-collections4). | commons-lang3 |  |
| 6.0.5 | requirement | Updated joda-time 2.9.6 to 2.10.5. | joda-time |  |
| 6.0.5 | requirement | Updated opencsv 4.6 to 5.0. | opencsv |  |
| 6.0.5 | requirement | Updated poi 4.0.0 to 4.1.1 (used by poi-ooxml 4.1.1). | poi |  |
| 6.0.5 | security | Updated poi-ooxml 4.0.0 (CVE) to 4.1.1. | poi-ooxml |  |
| 6.0.5 | requirement | Updated poi-ooxml-schemas 4.0.0 to 4.1.1 (used by poi-ooxml 4.1.1). | poi-ooxml-schemas |  |
| 6.0.5 | requirement | Updated xmlbeans 3.0.1 to 3.1.0 (used by poi-ooxml-schemas 4.1.1). | xmlbeans |  |
| 6.0.5 | requirement | Updated MxModelReflection 5.6.2 to 6.1.1. | MxModelReflection |  |
| 6.0.5 | requirement | Use Atlas UI Resources. | Atlas UI Resources |  |
| 6.0.1 | requirement | Includes the required commons-compress.jar. | commons-compress |  |
| 6.0.0 | breaking | Migrate to Mx 7.23 and fix deprecated warnings including FileDocuments and Float/Currency usages for Mx 8 compatibility. |  |  |
| 6.0.0 | breaking | Use non-deprecated CSVWriter. |  |  |
| 5.2.1 | requirement | Now it includes the required commons-compress.jar. | commons-compress |  |
| 5.2.0 | requirement | Update opencsv from version 2.3 to version 4.6. | opencsv |  |
| 5.2.0 | requirement | Make compatible with Excel Importer 8.0.0. | Excel Importer |  |
| 5.1.0 | requirement | Upgraded poi, poi-ooxml, and poi-ooxml-schemas to 4.0.0. | poi, poi-ooxml, poi-ooxml-schemas |  |
| 5.1.0 | requirement | Upgraded commons-codec to 1.11. | commons-codec |  |
| 5.1.0 | requirement | Upgraded commons-collections4 to 4.2. | commons-collections4 |  |
| 5.1.0 | requirement | Upgraded commons-math to 3.6.1. | commons-math |  |
| 5.1.0 | requirement | Upgraded replication to 7. |  |  |
| 5.1.0 | requirement | Upgraded xmlbeans to 3.0.1. | xmlbeans |  |
