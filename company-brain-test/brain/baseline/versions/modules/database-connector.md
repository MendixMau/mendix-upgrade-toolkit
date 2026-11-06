# Database Connector (Marketplace component 2888)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/2888)

| version | published | min Mendix |
|---|---|---|
| 7.0.5 | 2026-09-09 | 10.24.11 |
| 7.0.4 | 2026-08-12 | 10.24.11 |
| 7.0.3 | 2026-05-11 | 10.24.11 |
| 7.0.2 | 2025-12-12 | 10.24.11 |
| 7.0.1 | 2025-07-30 | 10.21.0 |
| 7.0.0 | 2025-04-02 | 10.21.0 |
| 6.0.3 | 2024-02-26 | 9.18.4 |
| 6.0.2 | 2023-12-27 | 9.18.4 |
| 6.0.1 | 2023-09-21 | 9.18.4 |
| 6.0.0 | 2023-03-24 | 9.18.4 |
| 5.0.7 | 2024-05-14 | 8.18.29 |
| 5.0.6 | 2022-12-13 | 8.18.20 |
| 5.0.5 | 2022-11-23 | 8.18.20 |
| 5.0.4 | 2022-10-31 | 8.18.20 |
| 5.0.3 | 2022-09-15 | 8.18.19 |
| 5.0.2 | 2022-03-22 | 8.12.4 |
| 5.0.1 | 2022-03-08 | 8.12.4 |
| 5.0.0 | 2021-08-03 | 8.12.4 |
| 4.0.0 | 2020-12-21 | 8.12.4 |
| 3.1.0 | 2020-04-07 | 8.8.0 |
| 3.0.0 | 2020-04-07 | 8.6.0 |
| 2.3.0 | 2019-11-21 | 7.23.8 |
| 2.2.1 | 2019-07-25 | 7.23.7 |
| 2.2.0 | 2019-07-24 | 7.23.7 |
| 2.1.0 | 2019-07-24 | 7.0.2 |
| 2.0.0 | 2019-06-11 | 7.23.5 |
| 1.0.2 | 2017-06-20 | 7.0.2 |
| 1.0.1 | 2017-03-13 | 7.0.2 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 7.0.5 | security | Resolved CVE-2026-55856 through CVE-2026-55860 and CVE-2026-61700 by upgrading mariadb to 2.7.14 | mariadb |  |
| 7.0.4 | security | Fixed CVE 2026-54291 by upgrading postgresql version to 42.7.12 | postgresql |  |
| 7.0.3 | security | Resolved CVE-2026-42198 by upgrading postgresql to 42.7.11 | postgresql |  |
| 7.0.2 | security | Resolved CVE-2025-59250 by upgrading the Microsoft SQL Server JDBC driver to version 12.10.2.jre11 | Microsoft SQL Server JDBC driver |  |
| 7.0.2 | fix | Fixed issue where Callable Statement failed to process null DATE values in cursor result set, causing query execution errors [#241877] | Callable Statement |  |
| 7.0.1 | security | Fixed CVE-2024-1597, upgraded to PostgreSQL 42.4.4 | PostgreSQL |  |
| 7.0.0 | requirement | Updated the module to Studio-Pro version 10.21.0 |  |  |
| 6.0.3 | security | Fixed CVE-2024-1597, upgraded to postgresql@42.4.4 | postgresql |  |
| 6.0.2 | security | Fixed CVE-2014-8314, upgraded ngdbc to 2.19.15 | ngdbc |  |
| 6.0.2 | improvement | Upgraded slf4j to 2.0.7 | slf4j |  |
| 6.0.1 | migration-step | Included a migration file for the Java dependencies for Studio Pro 10 compatibility | Java dependencies |  |
| 6.0.0 | requirement | Updated module to Framework version 9.18.4 |  |  |
| 5.0.7 | security | Fixed CVE-2024-1597, upgraded PostgreSQL jar to 42.4.4.jar | PostgreSQL |  |
| 5.0.6 | security | Fixed CVE-2022-41946, upgraded postgresql to 42.4.3 | postgresql |  |
| 5.0.5 | migration-step | Removed unwanted jar files from the userlib [#169589] | userlib |  |
| 5.0.4 | security | Fixed CVE-2022-41853, updated hsqldb (HyperSQL DataBase) to 2.7.1 | hsqldb |  |
| 5.0.3 | security | Upgraded to postgresql-42.4.1 to fix high severity vulnerability in 42.3.3 | postgresql |  |
| 5.0.2 | fix | Fixed issue where some database drivers would not load [#144326] | database drivers |  |
| 5.0.2 | improvement | Upgraded some database drivers | database drivers |  |
| 5.0.1 | improvement | Upgraded module dependencies |  |  |
| 4.0.0 | requirement | Updated module to Framework version 8.12.4 |  |  |
| 4.0.0 | improvement | Updated drivers to match those of Framework version 8.12.4 | drivers |  |
| 4.0.0 | breaking | Removed calls to deprecated methods |  |  |
| 3.1.0 | requirement | Updated to Mendix 8.8.0 |  |  |
| 3.0.0 | requirement | Updated to Mendix 8.6.0 |  |  |
| 2.3.0 | requirement | Updated to be compatible with Mendix Studio Pro version 7.23.8 |  |  |
| 2.2.1 | requirement | Minor update to be compatible with 7.23.7 (Build 55882) |  |  |
| 2.2.0 | requirement | Updated to be compatible with Mendix 7.23.7 |  |  |
| 2.2.0 | removal | Removed unused jackson libraries: jackson-core-2.6.6.jar, jackson-databind-2.6.6.jar, jackson-annotations-2.6.0.jar | jackson-core-2.6.6.jar, jackson-databind-2.6.6.jar, jackson-annotations-2.6.0.jar |  |
| 2.1.0 | removal | Removed unused jackson libraries: jackson-core-2.6.6.jar, jackson-databind-2.6.6.jar, jackson-annotations-2.6.0.jar | jackson-core-2.6.6.jar, jackson-databind-2.6.6.jar, jackson-annotations-2.6.0.jar |  |
| 2.0.0 | breaking | Removed references to Float and Currency, as they are deprecated | Float, Currency |  |
| 2.0.0 | removal | Removed support to HashedString as an attribute type | HashedString |  |
| 2.0.0 | removal | Removed support for testing against Redshift | Redshift |  |
| 2.0.0 | requirement | Supported for Mendix 7 LTS (from 7.23.5) and Mendix 8 |  |  |
| 1.0.2 | fix | HikaryCP no longer requires to write into System Properties, fixing java.security.AccessControlException [#4] | HikaryCP |  |
| 1.0.1 | fix | Fixed Mendix 7 compatibility by adding org.slf4j.slf4j-api.jar (dependency of HikariCP) | org.slf4j.slf4j-api.jar |  |
| 1.0.1 | improvement | Upgraded HikariCP database connection pooling library to version 2.6.1 (was 2.4.6) | HikariCP |  |
