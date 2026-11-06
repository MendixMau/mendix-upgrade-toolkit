# Multi-factor Authentication For Mendix (MFA/2FA) (Marketplace component 116892)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Module, Emixa, Community, [marketplace](https://marketplace.mendix.com/link/component/116892)

| version | published | min Mendix |
|---|---|---|
| 7.0.0 | 2026-08-06 | 11.12.1 |
| 6.0.0 | 2026-01-23 | 11.6.2 |
| 5.1.0 | 2026-08-06 | 11.6.2 |
| 5.0.0 | 2025-12-24 | 9.24.0 |
| 4.0.0 | 2025-07-08 | 9.24.0 |
| 3.1.1 | 2025-01-09 | 9.18.6 |
| 3.1.0 | 2025-01-08 | 9.18.6 |
| 3.0.0 | 2023-09-06 | 9.18.4 |
| 2.1.0 | 2023-09-06 | 8.18.8 |
| 2.0.0 | 2022-12-29 | 8.18.8 |
| 1.5.0 | 2021-12-24 | 8.18.8 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 7.0.0 | requirement | Minimum Mendix version raised to 11.12.1 | Mendix |  |
| 6.0.0 | requirement | Minimum Mendix version raised to 11.6.2 for Mendix 11 compatibility | Mendix |  |
| 6.0.0 | breaking | Several Java actions changed | Java actions |  |
| 5.0.0 | requirement | Minimum Mendix version raised to 9.24.0 | Mendix |  |
| 4.0.0 | breaking | Module architecture redesigned. Configure required microflows via ASU_SetMicroflows and ASU_v2 in after startup | ASU_SetMicroflows, ASU_v2 |  |
| 3.1.0 | security | Security fix for After startup: Access rights removed | After startup |  |
| 3.1.0 | migration-step | Check changed microflows SUB_MFA_CreateCode, SUB_MFA_UserDisabledCheck, SUB_MFA_ValidateCode to avoid startup errors | SUB_MFA_CreateCode, SUB_MFA_UserDisabledCheck, SUB_MFA_ValidateCode |  |
| 2.0.0 | breaking | Removed capability to use MFA from login.html due to complexity | login.html |  |
| 2.0.0 | migration-step | Remove MFA directory from resources directory | MFA directory |  |
| 2.0.0 | fix | BlockSince attribute on User entity fixed for Mendix 9 compatibility | BlockSince |  |
