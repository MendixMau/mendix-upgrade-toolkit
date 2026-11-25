# LDAP (Marketplace component 210270)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/210270)

| version | published | min Mendix |
|---|---|---|
| 2.2.2 | 2026-09-24 | 10.21.1 |
| 2.2.1 | 2026-08-13 | 10.21.1 |
| 2.2.0 | 2026-04-30 | 10.21.1 |
| 2.1.2 | 2026-02-25 | 10.21.1 |
| 2.1.1 | 2025-05-28 | 10.21.1 |
| 2.1.0 | 2025-05-05 | 10.21.1 |
| 2.0.1 | 2025-05-05 | 10.12.10 |
| 2.0.0 | 2025-01-20 | 10.12.10 |
| 1.2.2 | 2026-09-24 | 9.24.35 |
| 1.2.1 | 2026-08-13 | 9.24.35 |
| 1.2.0 | 2026-04-30 | 9.24.35 |
| 1.1.3 | 2025-05-05 | 9.24.8 |
| 1.1.2 | 2025-01-08 | 9.24.8 |
| 1.1.1 | 2024-01-18 | 9.24.8 |
| 1.1.0 | 2023-09-25 | 9.24.8 |
| 1.0.0 | 2023-04-28 | 9.22.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.2.2 | requirement | Added io.micrometer:micrometer-core to 1.17.1 | io.micrometer:micrometer-core |  |
| 2.2.2 | requirement | Upgraded org.springframework:spring-core to 7.0.9 | org.springframework:spring-core |  |
| 2.2.2 | requirement | Upgraded org.springframework:spring-tx to 7.0.9 | org.springframework:spring-tx |  |
| 2.2.2 | requirement | Upgraded org.springframework:spring-beans to 7.0.9 | org.springframework:spring-beans |  |
| 2.2.2 | requirement | Upgraded org.springframework.ldap:spring-ldap-core to 4.1.1 | org.springframework.ldap:spring-ldap-core |  |
| 2.2.1 | improvement | Improved LDAP synchronization performance and prevented duplication when group or user names change |  |  |
| 2.2.1 | requirement | Upgraded org.springframework:spring-core to 7.0.8 | org.springframework:spring-core |  |
| 2.2.1 | requirement | Upgraded org.springframework:spring-tx to 7.0.8 | org.springframework:spring-tx |  |
| 2.2.1 | requirement | Upgraded org.springframework:spring-beans to 7.0.8 | org.springframework:spring-beans |  |
| 2.2.1 | requirement | Upgraded org.springframework.ldap:spring-ldap-core to 4.0.4 | org.springframework.ldap:spring-ldap-core |  |
| 2.2.1 | migration-step | Remove unique constraint on ObjectGUID attribute of LDAP Group entity, run Ldap.MF_DeleteDuplicateGroups, add constraint back, refresh groups | LDAP Group |  |
| 2.2.1 | known-issue | Duplicate LDAP Group records may exist during upgrade. Role mappings may break if groups deleted or renamed | LDAP Group, LDAP role mappings |  |
| 2.2.0 | improvement | Improved LDAP synchronization to prevent duplication when group or user names change |  |  |
| 2.2.0 | requirement | Upgraded org.springframework:spring-core to 6.2.18 | org.springframework:spring-core |  |
| 2.2.0 | requirement | Upgraded org.springframework:spring-tx to 6.2.18 | org.springframework:spring-tx |  |
| 2.2.0 | requirement | Upgraded org.springframework:spring-beans to 6.2.18 | org.springframework:spring-beans |  |
| 2.2.0 | breaking | Module now uses objectGUID as primary identifier for users and groups instead of name | objectGUID |  |
| 2.2.0 | known-issue | Upgrade from earlier versions may create duplicates if legacy data inconsistent. Role mappings break if LDAP group deleted or renamed | LDAP Group, LDAP role mappings |  |
| 2.2.0 | known-issue | Version 2.2.0 may create duplicate LDAP group records during upgrade. Use version 2.2.1 or later. Version will be removed from marketplace soon |  |  |
| 2.1.2 | requirement | Upgraded org.springframework:spring-core to 6.2.16 | org.springframework:spring-core |  |
| 2.1.2 | requirement | Upgraded org.springframework:spring-tx to 6.2.16 | org.springframework:spring-tx |  |
| 2.1.2 | requirement | Upgraded org.springframework:spring-beans to 6.2.16 | org.springframework:spring-beans |  |
| 2.1.1 | improvement | Ensures compatibility with Mendix 11 |  |  |
| 2.1.0 | requirement | Version 2.1.0 for apps on Mendix 10.21.1 or higher |  |  |
| 2.1.0 | requirement | Upgraded org.springframework:spring-core to 6.2.2 | org.springframework:spring-core |  |
| 2.1.0 | requirement | Upgraded org.springframework:spring-tx to 6.2.2 | org.springframework:spring-tx |  |
| 2.1.0 | requirement | Upgraded org.springframework:spring-beans to 6.2.2 | org.springframework:spring-beans |  |
| 2.0.0 | requirement | Version 2.0.0 for apps on Mendix 10.12.10 or higher |  |  |
| 2.0.0 | requirement | Upgraded org.springframework.ldap:spring-ldap-core to 2.4.4 | org.springframework.ldap:spring-ldap-core |  |
| 2.0.0 | migration-step | Delete all Java libraries used by old LDAP module from userlib folder before upgrading to avoid conflicts |  |  |
| 1.2.2 | requirement | Upgraded org.springframework:spring-core to 7.0.9 | org.springframework:spring-core |  |
| 1.2.2 | requirement | Upgraded org.springframework:spring-tx to 7.0.9 | org.springframework:spring-tx |  |
| 1.2.2 | requirement | Upgraded org.springframework:spring-beans to 7.0.9 | org.springframework:spring-beans |  |
| 1.2.1 | requirement | Upgraded org.springframework:spring-core to 7.0.8 | org.springframework:spring-core |  |
| 1.2.1 | requirement | Upgraded org.springframework:spring-tx to 7.0.8 | org.springframework:spring-tx |  |
| 1.2.1 | requirement | Upgraded org.springframework:spring-beans to 7.0.8 | org.springframework:spring-beans |  |
| 1.2.1 | requirement | Upgraded org.springframework.ldap:spring-ldap-core to 4.0.4 | org.springframework.ldap:spring-ldap-core |  |
| 1.2.0 | requirement | Upgraded to Studio Pro v9.24.35 |  |  |
| 1.2.0 | requirement | Upgraded org.springframework:spring-core to 6.2.17 | org.springframework:spring-core |  |
| 1.2.0 | requirement | Upgraded org.springframework:spring-tx to 6.2.17 | org.springframework:spring-tx |  |
| 1.2.0 | requirement | Upgraded org.springframework:spring-beans to 6.2.17 | org.springframework:spring-beans |  |
| 1.2.0 | requirement | Recommended to set runtime to Java 21 for compatibility |  |  |
| 1.1.2 | security | Fixed LDAP injection vulnerability. CVSS v3.1: 7.4 (Ticket #235264) |  |  |
| 1.1.2 | requirement | Upgraded org.springframework.ldap:spring-ldap-core to 2.4.4 | org.springframework.ldap:spring-ldap-core |  |
| 1.1.2 | migration-step | Delete all Java libraries used by old LDAP module from userlib folder before upgrading to avoid conflicts |  |  |
| 1.1.1 | requirement | Upgraded org.springframework:spring-core to 5.3.31 (Ticket #202474) | org.springframework:spring-core |  |
| 1.1.1 | requirement | Upgraded org.springframework:spring-tx to 5.3.31 | org.springframework:spring-tx |  |
| 1.1.1 | requirement | Upgraded org.springframework:spring-beans to 5.3.31 | org.springframework:spring-beans |  |
| 1.1.1 | migration-step | Delete all Java libraries used by old LDAP module from userlib folder before upgrading to avoid conflicts |  |  |
| 1.1.0 | requirement | Upgraded to Studio Pro v9.24.8 |  |  |
| 1.1.0 | fix | Fixed Mendix 10 compatibility issue |  |  |
| 1.1.0 | migration-step | Included migration file for Java dependencies for Studio Pro 10 compatibility |  |  |
| 1.0.0 | requirement | Added org.slf4j:slf4j-api to 2.0.5 | org.slf4j:slf4j-api |  |
| 1.0.0 | requirement | Added org.springframework:spring-core to 5.3.24 | org.springframework:spring-core |  |
| 1.0.0 | requirement | Added org.springframework.ldap:spring-ldap-core to 2.4.1 | org.springframework.ldap:spring-ldap-core |  |
| 1.0.0 | requirement | Added org.springframework:spring-tx to 5.3.23 | org.springframework:spring-tx |  |
| 1.0.0 | requirement | Added org.springframework:spring-beans to 5.3.24 | org.springframework:spring-beans |  |
| 1.0.0 | migration-step | Delete all Java libraries used by old LDAP module from userlib folder before upgrading to avoid conflicts |  |  |
