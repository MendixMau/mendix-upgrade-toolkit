# External Database Connector (Marketplace component 219862)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/219862)

| version | published | min Mendix |
|---|---|---|
| 6.3.3 | 2026-09-23 | 11.12.0 |
| 6.3.2 | 2026-09-09 | 11.12.0 |
| 6.3.1 | 2026-08-11 | 11.12.0 |
| 6.3.0 | 2026-07-01 | 11.12.0 |
| 6.2.5 | 2026-05-21 | 11.4.0 |
| 6.2.4 | 2026-04-06 | 11.4.0 |
| 6.2.3 | 2026-02-18 | 11.4.0 |
| 6.2.2 | 2026-01-27 | 11.4.0 |
| 6.2.1 | 2025-11-27 | 11.4.0 |
| 6.2.0 | 2025-11-04 | 11.4.0 |
| 6.1.0 | 2025-09-30 | 11.3.0 |
| 6.0.0 | 2025-08-29 | 11.0.0 |
| 5.4.0 | 2026-09-23 | 10.24.0 |
| 5.3.9 | 2026-09-09 | 10.24.0 |
| 5.3.8 | 2026-08-12 | 10.24.0 |
| 5.3.7 | 2026-05-21 | 10.24.0 |
| 5.3.6 | 2026-04-03 | 10.24.0 |
| 5.3.5 | 2026-01-09 | 10.24.0 |
| 5.3.4 | 2025-11-24 | 10.24.0 |
| 5.3.3 | 2025-11-04 | 10.24.0 |
| 5.3.2 | 2025-10-20 | 10.24.0 |
| 5.3.1 | 2025-07-30 | 10.23.0 |
| 5.3.0 | 2025-05-29 | 10.23.0 |
| 5.2.0 | 2025-05-05 | 10.22.0 |
| 5.1.2 | 2025-06-05 | 10.21.0 |
| 5.1.1 | 2025-02-26 | 10.20.0 |
| 5.1.0 | 2025-01-28 | 10.19.0 |
| 5.0.1 | 2025-02-04 | 10.18.0 |
| 5.0.0 | 2024-12-18 | 10.18.0 |
| 4.1.1 | 2024-11-11 | 10.16.0 |
| 4.1.0 | 2024-10-30 | 10.16.0 |
| 4.0.2 | 2024-09-24 | 10.15.0 |
| 4.0.1 | 2024-08-28 | 10.14.0 |
| 4.0.0 | 2024-07-30 | 10.13.0 |
| 3.0.2 | 2024-11-13 | 10.12.4 |
| 3.0.1 | 2024-08-27 | 10.12.4 |
| 3.0.0 | 2024-06-25 | 10.12.0 |
| 2.0.1 | 2024-04-29 | 10.9.0 |
| 2.0.0 | 2024-03-27 | 10.9.0 |
| 1.0.2 | 2024-08-16 | 10.6.12 |
| … 2 older versions | | |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 6.3.3 | security | Resolved CVE-2026-85525 by upgrading snowflake jar to 4.3.4 | snowflake jar |  |
| 6.3.2 | security | Resolved CVE-2026-55856 through CVE-2026-55860 and CVE-2026-61700 by upgrading mariadb to 2.7.14 | mariadb |  |
| 6.3.2 | security | Resolved CVE-2026-59645 by upgrading Bouncy Castle libraries to 1.85 | Bouncy Castle libraries |  |
| 6.3.1 | security | Fixed CVE 2026-54291 by upgrading postgresql version to 42.7.12 | postgresql |  |
| 6.3.0 | breaking | Implementation of AdminAction is now replaced with HttpServelet | AdminAction | HttpServelet |
| 6.2.5 | security | Resolved CVE-2026-42198 by upgrading PostgreSQL JDBC driver to version 42.7.11 | PostgreSQL JDBC driver |  |
| 6.2.5 | improvement | Upgraded Bouncy Castle libraries (bcprov-jdk18on and bcpkix-jdk18on) to 1.84 | Bouncy Castle libraries |  |
| 6.2.5 | improvement | Now we use JVM-managed TLS versions | TLS |  |
| 6.2.4 | security | Resolved CVE-2026-3293 by upgrading Snowflake jar to version 4.0.2 | Snowflake jar |  |
| 6.2.1 | security | Resolved CVE-2025-59250 by upgrading Microsoft SQL Server JDBC driver to version 12.10.2.jre11 | Microsoft SQL Server JDBC driver |  |
| 6.2.0 | improvement | Upgraded Bouncy Castle libraries (bcprov-jdk18on and bcpkix-jdk18on) to 1.81 | Bouncy Castle libraries |  |
| 6.0.0 | security | Fixed CVE-2025-8916 by upgrading Bouncy Castle libraries (bcprov-jdk18on and bcpkix-jdk18on) to 1.79 | Bouncy Castle libraries |  |
| 5.4.0 | security | Fixed CVE-2026-85525 by upgrading snowflake-jdbc version to 4.3.4 | snowflake-jdbc |  |
| 5.3.9 | security | Resolved CVE-2026-55856 through CVE-2026-55860 and CVE-2026-61700 by upgrading mariadb to 2.7.14 | mariadb |  |
| 5.3.9 | security | Resolved CVE-2026-59645 by upgrading Bouncy Castle libraries to 1.85 | Bouncy Castle libraries |  |
| 5.3.8 | security | Fixed CVE 2026-54291 by upgrading postgresql version to 42.7.12 | postgresql |  |
| 5.3.7 | security | Resolved CVE-2026-42198 by upgrading PostgreSQL JDBC driver to version 42.7.11 | PostgreSQL JDBC driver |  |
| 5.3.7 | improvement | Upgraded Bouncy Castle libraries (bcprov-jdk18on and bcpkix-jdk18on) to 1.84 | Bouncy Castle libraries |  |
| 5.3.7 | improvement | Now we use JVM-managed TLS versions | TLS |  |
| 5.3.6 | security | Resolved CVE-2026-3293 by upgrading Snowflake jar to version 4.0.2 | Snowflake jar |  |
| 5.3.4 | security | Resolved CVE-2025-59250 by upgrading Microsoft SQL Server JDBC driver to version 12.10.2.jre11 | Microsoft SQL Server JDBC driver |  |
| 5.3.3 | improvement | Upgraded Bouncy Castle libraries (bcprov-jdk18on and bcpkix-jdk18on) to 1.81 | Bouncy Castle libraries |  |
| 5.3.2 | security | Fixed CVE-2025-8916 by upgrading Bouncy Castle libraries (bcprov-jdk18on and bcpkix-jdk18on) to 1.79 | Bouncy Castle libraries |  |
| 5.3.1 | security | Fixed CVE-2025-27496: Upgraded Snowflake to 3.24.2 | Snowflake |  |
| 5.3.1 | improvement | Upgraded GSON to 2.13.1 | GSON |  |
| 5.1.2 | requirement | Updated the module to Studio-Pro version 10.21.0 | Studio-Pro |  |
| 5.1.0 | feature | v5.1.0 introduces new feature using updated approach for connecting to databases during design time. Run app locally with latest connector before connecting |  |  |
| 5.0.1 | security | Fix CVE-2025-24789, Upgrade net.snowflake:snowflake-jdbc to version 3.22.0 | snowflake-jdbc |  |
| 5.0.0 | feature | External Database Connector introduces new beta feature using different approach for connecting to databases during design time with --enable-live-preview flag |  |  |
| 4.1.1 | security | Fix CVE-2024-43382: Upgrade net.snowflake:snowflake-jdbc to version 3.20.0 | snowflake-jdbc |  |
| 3.0.2 | security | Fix CVE-2024-43382: Upgrade net.snowflake:snowflake-jdbc to version 3.20.0 | snowflake-jdbc |  |
| 1.0.1 | security | Fixed CVE-2024-1597: Upgraded to postgresql@42.4.4 | postgresql |  |
