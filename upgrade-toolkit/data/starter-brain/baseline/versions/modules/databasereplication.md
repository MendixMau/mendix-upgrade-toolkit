# DatabaseReplication (Marketplace component 160)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/160)

| version | published | min Mendix |
|---|---|---|
| 9.3.2 | 2026-09-24 | 10.24.11 |
| 9.3.1 | 2026-02-18 | 10.24.11 |
| 9.3.0 | 2025-12-10 | 10.24.11 |
| 9.2.1 | 2025-11-07 | 10.21.0 |
| 9.2.0 | 2025-08-05 | 10.21.0 |
| 9.1.0 | 2025-04-16 | 10.21.0 |
| 9.0.0 | 2025-02-10 | 10.18.0 |
| 8.2.2 | 2025-04-04 | 9.18.4 |
| 8.2.1 | 2024-11-25 | 9.18.4 |
| 8.2.0 | 2024-07-26 | 9.18.4 |
| 8.1.4 | 2024-05-24 | 9.18.4 |
| 8.1.3 | 2023-08-31 | 9.18.4 |
| 8.1.2 | 2023-07-10 | 9.18.4 |
| 8.1.1 | 2023-06-01 | 9.18.4 |
| 8.1.0 | 2023-04-18 | 9.18.4 |
| 8.0.2 | 2023-03-17 | 9.0.5 |
| 8.0.1 | 2021-08-10 | 9.0.5 |
| 8.0.0 | 2021-07-19 | 9.0.5 |
| 7.1.5 | 2024-05-27 | 8.18.23 |
| 7.1.4 | 2023-07-10 | 8.18.23 |
| 7.1.3 | 2023-06-01 | 8.18.23 |
| 7.1.2 | 2023-03-17 | 8.18.23 |
| 7.1.1 | 2021-08-10 | 8.12.4 |
| 7.1.0 | 2021-07-19 | 8.12.4 |
| 7.0.1 | 2021-05-05 | 8.12.4 |
| 7.0.0 | 2020-12-22 | 8.12.4 |
| 6.1.1 | 2020-11-19 | 7.23.7 |
| 6.1.0 | 2020-08-28 | 7.23.7 |
| 6.0.2 | 2020-04-10 | 7.23.7 |
| 6.0.1 | 2019-08-19 | 7.23.7 |
| 6.0.0 | 2019-06-20 | 7.23.5 |
| 4.13.0 | 2019-02-11 | 7.1.1 |
| 4.11.0 | 2018-01-05 | 7.1.1 |
| 4.10.1 | 2017-02-24 | 7.0.2 |
| 4.10 | 2017-02-22 | 7.0.2 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 9.3.2 | security | Fixed CVE 2026-54291 by upgrading postgresql version to 42.7.12 | postgresql |  |
| 9.3.0 | requirement | Upgraded module to Mendix version 10.24.11 | Mendix |  |
| 9.2.1 | improvement | Upgraded widgets in TableMapping_Edit page to pluggable widgets using React | TableMapping_Edit, widgets |  |
| 9.2.0 | improvement | Upgraded all widgets to pluggable widgets using React | widgets |  |
| 9.1.0 | requirement | Upgraded module to Mendix version 10.21.0 for compatibility with future versions | Mendix |  |
| 9.1.0 | improvement | Removed usages of deprecated methods in com.mendix.core.Core from implementation | com.mendix.core.Core |  |
| 9.1.0 | improvement | Updated replication library to version 1.0.6 without deprecated com.mendix.core.Core methods | replication library |  |
| 9.0.0 | requirement | Upgraded module to Mendix version 10.18.0 for compatibility with future versions | Mendix |  |
| 8.2.2 | breaking | Removed usages of enum values for Float and Currency data types no longer supported with mx model reflection module 8.0.3+ | Float, Currency, mx model reflection module |  |
| 8.2.1 | fix | Fixed issue with Oracle DB template imports where unlimited string comparison threw database error | Oracle DB, template imports |  |
| 8.2.0 | breaking | Now explicitly disallow adding object parameters when manually executing import calls using Import and Run scheduled events buttons | object parameters, Import call, Planned import action |  |
| 8.1.4 | improvement | Updated replication library to 1.0.4; fixes rollback failure in Mendix 10 due to rollbackTransAction rename | replication library, MFValueParser, rollbackTransAction |  |
| 8.1.3 | migration-step | Included migration file for Java dependencies for Studio Pro 10 compatibility | Java dependencies |  |
| 8.1.2 | fix | Updated replication library to 1.0.3; fixes reference sets with Overwrite being overwritten multiple times, accidentally deleting imports | replication library, reference sets, Overwrite setting |  |
| 8.1.1 | breaking | Renamed URL to Host on database creation form to avoid confusion | URL, Host, database creation form | Host |
| 8.1.0 | requirement | Upgraded module to Mendix version 9.18.4 for compatibility with future versions | Mendix |  |
| 8.0.2 | improvement | Refactored replication library shared with Excel Importer to version 1.0.2 | replication library |  |
| 8.0.2 | improvement | Updated drivers: SQL Server 9.4.0, PostgreSQL 42.5.4, Oracle JDBC 21.9.0.0 | SQL Server, PostgreSQL, Oracle JDBC |  |
| 8.0.0 | requirement | Upgraded module to Mendix 9.0.5 and made compatible with Atlas 3. Version 8 only for Mendix 9; Version 7 for Mendix 8 and 9 | Mendix, Atlas UI |  |
| 7.1.5 | improvement | Updated replication library to 1.0.4; fixes rollback failure in Mendix 10 due to rollbackTransAction rename | replication library, MFValueParser, rollbackTransAction |  |
| 7.1.4 | fix | Updated replication library to 1.0.3; fixes reference sets with Overwrite being overwritten multiple times, accidentally deleting imports | replication library, reference sets, Overwrite setting |  |
| 7.1.3 | breaking | Renamed URL to Host on database creation form to avoid confusion | URL, Host, database creation form | Host |
| 7.1.2 | improvement | Refactored replication library shared with Excel Importer to version 1.0.2 | replication library |  |
| 7.1.2 | improvement | Updated drivers: SQL Server 9.4.0, PostgreSQL 42.5.1, Oracle JDBC 21.5.0.0 | SQL Server, PostgreSQL, Oracle JDBC |  |
| 7.1.0 | improvement | Wrapped all pop-up windows in Layout Grid containers to prepare for Atlas 3 support | pop-up windows, Layout Grid, Atlas 3 |  |
| 7.0.1 | security | Fixed CVE-2021-31341 |  |  |
| 7.0.0 | requirement | Updated to Mendix framework 8.12.4, SQL Server drivers to JRE11 variant, and Atlas UI | Mendix, SQL Server, Atlas UI |  |
| 6.1.1 | improvement | Updated replication.jar to latest version | replication.jar |  |
| 6.1.0 | improvement | Improved memory use: separate context skips user session reuse; load data in batches instead of all at once | memory use, database-replication, session, user context |  |
| 6.1.0 | improvement | Upgraded JDBC driver for PostgreSQL | PostgreSQL, JDBC driver |  |
| 6.0.1 | requirement | Updated to Mendix Studio Pro 7.23.7 | Mendix |  |
| 6.0.0 | removal | Removed deprecated APIs | deprecated APIs |  |
| 6.0.0 | removal | Removed Float and Currency data types; Decimal is used instead | Float, Currency | Decimal |
| 4.13.0 | improvement | Upgraded ojdbc6-11.2.0 to ojdbc8-12.2.0.1 and sqljdbc4-4.0 to mssql-jdbc-7.0.0 | ojdbc8, mssql-jdbc |  |
| 4.13.0 | improvement | Removed axis2-kernel-1.0.jar and use Java 8 API for encoding and decoding instead | axis2-kernel, Java 8 API |  |
| 4.10 | requirement | Made DatabaseReplication module compatible with Mendix 7 release | Mendix |  |
