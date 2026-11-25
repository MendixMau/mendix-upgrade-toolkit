# Unit Testing (Marketplace component 390)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/390)

| version | published | min Mendix |
|---|---|---|
| 10.0.8 | 2026-09-16 | 10.21.0 |
| 10.0.7 | 2026-08-06 | 10.21.0 |
| 10.0.6 | 2026-04-10 | 10.21.0 |
| 10.0.5 | 2025-10-15 | 10.21.0 |
| 10.0.4 | 2025-08-14 | 10.21.0 |
| 10.0.3 | 2025-08-07 | 10.21.0 |
| 10.0.2 | 2025-06-20 | 10.21.0 |
| 10.0.1 | 2025-05-16 | 10.21.0 |
| 10.0.0 | 2025-04-24 | 10.21.0 |
| 9.6.6 | 2026-09-16 | 9.24.0 |
| 9.6.5 | 2026-08-06 | 9.24.0 |
| 9.6.4 | 2025-10-15 | 9.24.0 |
| 9.6.3 | 2025-08-14 | 9.24.0 |
| 9.6.2 | 2025-08-07 | 9.24.0 |
| 9.6.1 | 2025-05-16 | 9.24.0 |
| 9.6.0 | 2025-03-21 | 9.24.0 |
| 9.5.2 | 2024-10-15 | 9.18.0 |
| 9.5.1 | 2024-07-04 | 9.18.0 |
| 9.5.0 | 2024-05-28 | 9.18.0 |
| 9.4.3 | 2024-05-01 | 9.18.0 |
| 9.4.2 | 2024-02-07 | 9.18.0 |
| 9.4.1 | 2023-11-14 | 9.18.0 |
| 9.4.0 | 2023-09-20 | 9.18.0 |
| 9.3.0 | 2023-04-14 | 9.18.0 |
| 9.2.0 | 2023-01-04 | 9.0.5 |
| 9.1.0 | 2022-11-07 | 9.0.5 |
| 9.0.5 | 2022-11-01 | 9.0.5 |
| 9.0.4 | 2022-03-10 | 9.0.5 |
| 9.0.3 | 2021-07-09 | 9.0.5 |
| 9.0.2 | 2021-07-07 | 9.0.5 |
| 9.0.1 | 2021-05-10 | 9.0.5 |
| 9.0.0 | 2021-05-03 | 9.0.5 |
| 8.0.6 | 2022-11-01 | 8.12.0 |
| 8.0.5 | 2022-04-13 | 8.12.0 |
| 8.0.4 | 2020-12-21 | 8.12.0 |
| 8.0.3 | 2020-12-21 | 8.1.0 |
| 8.0.1 | 2020-03-13 | 8.1.0 |
| 8.0.0 | 2019-09-26 | 8.1.0 |
| 7.0.2 | 2022-12-21 | 7.0.2 |
| 7.0.1 | 2022-12-21 | 7.0.2 |
| … 1 older versions | | |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 10.0.8 | requirement | Updated httpclient5 dependency to 5.6.4 | httpclient5 |  |
| 10.0.7 | requirement | Updated httpclient5 dependency to 5.6.2 | httpclient5 |  |
| 10.0.6 | migration-step | Migrated from SASS to CSS variables for Atlas 4 compatibility | Atlas 4 |  |
| 10.0.5 | breaking | Increased length of Name, DisplayName, Module, and TestName attributes to align with platform limits | UnitTest.Name, UnitTest.DisplayName, TestSuite.Module, UnitTestContext.TestName |  |
| 10.0.3 | requirement | Updated commons-lang3 dependency to 3.18.0 | commons-lang3 |  |
| 10.0.0 | requirement | Upgraded module to Mendix version 10.21.0 for compatibility with Mendix 11 | Mendix |  |
| 10.0.0 | requirement | Updated Atlas Core compatibility to version 3.17.0 | Atlas Core |  |
| 10.0.0 | requirement | Updated Atlas Web Content compatibility to version 3.8.0 | Atlas Web Content |  |
| 10.0.0 | requirement | Updated Data Widgets compatibility to version 2.31.0 | Data Widgets |  |
| 9.6.6 | requirement | Updated httpclient5 dependency to 5.6.4 | httpclient5 |  |
| 9.6.5 | requirement | Updated httpclient5 dependency to 5.6.2 | httpclient5 |  |
| 9.6.4 | breaking | Increased length of Name, DisplayName, Module, and TestName attributes to align with platform limits | UnitTest.Name, UnitTest.DisplayName, TestSuite.Module, UnitTestContext.TestName |  |
| 9.6.2 | requirement | Updated commons-lang3 dependency to 3.18.0 | commons-lang3 |  |
| 9.6.0 | requirement | Upgraded module to Mendix version 9.24.0 | Mendix |  |
| 9.6.0 | requirement | Added Accordion widget as dependency, compatible with v2.3.4 | Accordion |  |
| 9.6.0 | requirement | Updated Atlas Core module compatibility to v3.12.5 | Atlas Core |  |
| 9.6.0 | requirement | Added Atlas Web Content module as dependency, compatible with v3.4.2 | Atlas Web Content |  |
| 9.6.0 | requirement | Added Data Widgets module as dependency, compatible with v2.27.3 | Data Widgets |  |
| 9.5.2 | requirement | Updated Apache Commons IO dependency to 2.17.0 | commons-io |  |
| 9.5.0 | improvement | Updated unit test details page for React client compatibility, introduced in Mendix 10.7.0 |  |  |
| 9.4.3 | breaking | Changed Name attribute in UnitTest entity length to limited (#213295) | UnitTest.Name |  |
| 9.4.2 | requirement | Updated slf4j-api from 1.7.36 to 2.0.9; review userlib and match other slf4j library versions | slf4j-api |  |
| 9.4.1 | requirement | Updated httpclient5 from 5.0.3 to 5.2.1 | httpclient5 |  |
| 9.4.1 | requirement | Updated httpcore5 from 5.0.2 to 5.2 | httpcore5 |  |
| 9.4.1 | requirement | Updated httpcore5-h2 from 5.0.2 to 5.2 | httpcore5-h2 |  |
| 9.4.1 | requirement | Updated slf4j-api from 1.7.25 to 1.7.36 | slf4j-api |  |
| 9.4.1 | removal | Removed dependency on commons-codec-1.13; review userlib after upgrade | commons-codec-1.13 |  |
| 9.4.0 | migration-step | Switched from hamcrest-2.2.jar to hamcrest-core-1.3.jar and downgraded httpcore5 to 5.0.2; remove old files from userlib | hamcrest-2.2.jar, httpcore5-5.0.3.jar |  |
| 9.4.0 | requirement | Included Java dependency migration file for Studio Pro 10 compatibility | Mendix |  |
| 9.3.0 | requirement | Upgraded module to Mendix version 9.18.0 for compatibility with Mendix 10 | Mendix |  |
| 9.3.0 | breaking | Replaced IContext.rollbackTransAction with IContext.rollbackTransaction |  | IContext.rollbackTransaction |
| 9.2.0 | removal | Removed dependency on Community Commons module; review userlib and remove if unused | Community Commons |  |
| 9.2.0 | requirement | Updated commons-lang3 dependency from 3.11 to 3.12.0; remove old 3.11 jar files from userlib | commons-lang3 |  |
| 9.1.0 | requirement | Replaced Object Handling module dependency with Community Commons module; download from marketplace | Community Commons | Community Commons |
| 9.0.5 | requirement | Updated commons-io dependency from 2.8.0 to 2.11.0 to align with Community Commons | commons-io |  |
| 9.0.4 | migration-step | Fixed file naming conventions in userlib folder |  |  |
| 9.0.4 | requirement | Updated commons-lang from 3.7 to 3.11 to align with Mendix Community Commons | commons-lang |  |
| 9.0.1 | security | Updated commons-io to 2.8.0 due to directory traversal vulnerability in 2.6 | commons-io |  |
| 9.0.0 | requirement | Mendix 9.0.0 support | Mendix |  |
| 8.0.6 | requirement | Updated commons-io dependency from 2.8.0 to 2.11.0 to align with Community Commons | commons-io |  |
| 8.0.5 | requirement | Updated dependencies/userlib folder for Mendix 8 to sync with v9.0.4 |  |  |
| 8.0.4 | requirement | Mendix 8.12.0 support | Mendix |  |
| 8.0.0 | requirement | Updated module to Mendix 8 | Mendix |  |
| 7.0.2 | requirement | Updated commons-io dependency from 2.8.0 to 2.11.0 to align with Community Commons | commons-io |  |
| 7.0.1 | requirement | Updated dependencies/userlib folder for Mendix 7 to sync with v9.0.4 |  |  |
