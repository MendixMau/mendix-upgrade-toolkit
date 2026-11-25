# Forgot Password module (Marketplace component 1296)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/1296)

| version | published | min Mendix |
|---|---|---|
| 6.5.1 | 2026-07-14 | 10.21.1 |
| 6.5.0 | 2026-04-30 | 10.21.1 |
| 6.4.0 | 2025-09-29 | 10.21.1 |
| 6.3.0 | 2025-05-15 | 10.21.1 |
| 6.2.0 | 2025-05-15 | 10.12.10 |
| 6.1.0 | 2024-11-28 | 10.12.10 |
| 6.0.0 | 2024-04-11 | 10.6.0 |
| 5.6.1 | 2025-09-29 | 9.24.2 |
| 5.6.0 | 2025-05-15 | 9.24.2 |
| 5.5.0 | 2024-01-18 | 9.24.2 |
| 5.4.1 | 2023-12-13 | 9.24.2 |
| 5.4.0 | 2023-09-20 | 9.24.2 |
| 5.3.1 | 2023-06-15 | 9.24.2 |
| 5.3.0 | 2023-05-15 | 9.24.2 |
| 5.2.0 | 2023-03-15 | 9.22.0 |
| 5.1.1 | 2023-03-09 | 9.12.7 |
| 5.1.0 | 2023-01-19 | 9.12.7 |
| 5.0.0 | 2022-10-19 | 9.12.7 |
| 4.1.3 | 2023-09-20 | 8.18.22 |
| 4.1.2 | 2023-05-15 | 8.18.22 |
| 4.1.1 | 2023-03-09 | 8.18.22 |
| 4.1.0 | 2023-01-19 | 8.18.22 |
| 4.0.0 | 2022-10-19 | 8.18.21 |
| 3.7.3 | 2023-09-20 | 7.23.33 |
| 3.7.2 | 2023-05-15 | 7.23.33 |
| 3.7.1 | 2023-03-09 | 7.23.22 |
| 3.7.0 | 2023-01-19 | 7.23.33 |
| 3.6.0 | 2022-10-19 | 7.23.33 |
| 3.5.1 | 2022-02-26 | 8.18.13 |
| 3.2.2 | 2022-03-04 | 7.23.19 |
| 3.2.1 | 2021-01-14 | 7.23.19 |
| 3.2.0 | 2019-11-08 | 7.23.3 |
| 3.1.0 | 2019-05-15 | 7.3.0 |
| 3.0.0 | 2019-03-26 | 7.3.0 |
| 2.0.0 | 2017-11-17 | 7.3.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 6.5.1 | fix | Fixed the LoginContext reference for validation messages in ACT_Login | ACT_Login, LoginContext |  |
| 6.5.0 | improvement | Added org.apache.velocity:velocity-engine-core to version 2.4.1 | org.apache.velocity:velocity-engine-core |  |
| 6.5.0 | improvement | Anonymous userrole no longer needed for password reset functionality to mitigate unintended access risk |  |  |
| 6.4.0 | requirement | Added Community Commons module as dependency if Email Connector module is upgraded to v6.3.0 and above | Community Commons |  |
| 6.3.0 | requirement | v.6.3.0 version for apps on Mx10.21.1 or higher |  |  |
| 6.1.0 | requirement | v.6.1.0 version for apps on Mx10.12.10 or higher |  |  |
| 5.5.0 | fix | Fixed Mendix 10 compatibility issue |  |  |
| 5.4.0 | security | Fixed security vulnerability (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N) |  |  |
| 5.2.0 | requirement | Upgraded to Mendix Studio Pro v9.22.0 |  |  |
| 5.1.1 | security | Fixed security vulnerability (5.3 - CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N) |  |  |
| 5.1.0 | breaking | Replaced Email Module with Templates with Email connector (Ticket #169522, #169643, #170709, #169160) | Email Module with Templates | Email connector |
| 5.1.0 | fix | Fixed issue related to cookies in Mendix studio pro-9.20 (Ticket #174456, #173282) |  |  |
| 5.1.0 | migration-step | Changed License to MIT |  |  |
| 5.0.0 | fix | Fixed issues related to Deep Link module. Now compatible with latest Deep Link module from Marketplace (Ticket #149147, #152032) | Deep Link module |  |
| 4.1.3 | security | Fixed security vulnerability (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N) |  |  |
| 4.1.1 | security | Fixed security vulnerability (5.3 - CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N) |  |  |
| 4.1.0 | breaking | Replaced Email Module with Templates with Email connector (Ticket #169522, #169643, #170709, #169160) | Email Module with Templates | Email connector |
| 4.1.0 | migration-step | Changed License to MIT |  |  |
| 4.0.0 | fix | Fixed issues related to Deep Link module. Now compatible with latest Deep Link module from Marketplace (Ticket #149147, #152032) | Deep Link module |  |
| 3.7.3 | security | Fixed security vulnerability (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N) |  |  |
| 3.7.1 | security | Fixed security vulnerability (5.3 - CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N) |  |  |
| 3.7.0 | migration-step | Changed License to MIT |  |  |
| 3.6.0 | fix | Fixed issues related to Deep Link module. Now compatible with latest Deep Link module from Marketplace (Ticket #149147, #152032) | Deep Link module |  |
| 3.5.1 | requirement | Upgrade to Studio 8.18.13 |  |  |
| 3.5.1 | security | Fixed CVE-2022-26313 and CVE-2022-26314 |  |  |
| 3.2.2 | security | Fixed CVE-2022-26314 |  |  |
| 3.2.1 | security | Fixed security exploit |  |  |
| 3.2.0 | requirement | Upgrade to 7.23.3 |  |  |
| 3.1.0 | fix | Fixed issue where ValidUntil and IsSignUp attributes would be empty due to user lacking entity access | ValidUntil, IsSignUp |  |
| 3.0.0 | security | This release includes an important security fix. All users strongly advised to update to latest release |  |  |
