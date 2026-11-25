# LDAP Synchronization module (Marketplace component 24)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Module, Mendix, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/24)

| version | published | min Mendix |
|---|---|---|
| 8.0.0 | 2020-01-21 | 7.23.4 |
| 7.2.1 | 2018-11-29 | 7.16.0 |
| 7.1.0 | 2017-09-25 | 7.1.1 |
| 7.0 | 2017-06-12 | 7.1.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 8.0.0 | requirement | Upgraded LDAP module to be Mendix 8 compatible. Minimum Mendix version is now 7.23.4. |  |  |
| 8.0.0 | migration-step | Updated all Java libraries to latest versions. Delete old libraries from userlib folder if compilation or runtime errors occur. | spring-beans-4.3.9.RELEASE.jar, spring-core-4.3.9.RELEASE.jar, spring-ldap-core-2.3.1.RELEASE.jar, spring-tx-4.3.9.RELEASE.jar, org.slf4j.slf4j-api-1.7.25.jar, commons-lang-2.5.jar |  |
| 7.2.1 | requirement | Upgraded to Mendix 7.16.0 or later. Minimum Mendix version is now 7.16.0. |  |  |
| 7.2.1 | migration-step | Cleanup included Java libraries from userlib folder after importing this update. |  |  |
| 7.0 | requirement | Upgraded to Mendix 7 for compatibility. Minimum Mendix version is now 7.1.1. |  |  |
| 7.0 | migration-step | Remove old Java libraries from userlib folder after importing this update as they are no longer needed. | spring-beans-4.0.4.RELEASE.jar, spring-core-4.0.4.RELEASE.jar, spring-ldap-core-2.0.1.RELEASE.jar, spring-tx-4.0.4.RELEASE.jar |  |
