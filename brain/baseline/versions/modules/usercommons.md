# UserCommons (Marketplace component 223053)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/223053)

| version | published | min Mendix |
|---|---|---|
| 2.4.0 | 2026-07-10 | 10.24.0 |
| 2.3.0 | 2026-06-11 | 10.24.0 |
| 2.2.1 | 2026-02-09 | 10.24.0 |
| 2.2.0 | 2025-11-20 | 10.21.1 |
| 2.1.3 | 2025-07-02 | 10.21.1 |
| 2.1.2 | 2025-05-29 | 10.21.1 |
| 2.1.1 | 2025-05-29 | 10.21.0 |
| 2.1.0 | 2025-05-07 | 10.21.1 |
| 2.0.2 | 2025-06-30 | 10.12.10 |
| 2.0.1 | 2025-05-07 | 10.12.10 |
| 2.0.0 | 2024-12-24 | 10.12.10 |
| 1.0.4 | 2026-01-26 | 9.24.2 |
| 1.0.3 | 2025-05-07 | 9.24.2 |
| 1.0.2 | 2024-07-29 | 9.24.2 |
| 1.0.1 | 2024-03-07 | 9.24.2 |
| 1.0.0 | 2024-02-22 | 9.24.2 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.4.0 | improvement | Forward compatibility improved for usage in Mendix 11.12 applications with react client enabled |  |  |
| 2.3.0 | requirement | Updated for compatibility with v4.5.0 of the OIDC SSO module | OIDC SSO module |  |
| 2.3.0 | removal | Removed dependency on Nanoflow module | Nanoflow module |  |
| 2.2.0 | feature | New user-related entity introduced for storing named user identifier consistently across multiple apps for correct multi-app user metering |  |  |
| 2.1.2 | requirement | Ensures compatibility with Mendix 11 |  |  |
| 2.1.1 | requirement | Ensures compatibility with Mendix 11 |  |  |
| 2.1.1 | known-issue | Compatibility Warning for Mendix 10.21.1 Users: v2.1.1 is for Mendix 10.21.0 only, use v2.1.0 or upgrade to v2.1.2 |  |  |
| 2.1.0 | requirement | v.2.1.0 version for apps on Mx10.21.1 or higher |  |  |
| 2.0.0 | requirement | v.2.0.0 version for apps on Mx10.12.10 or higher |  |  |
| 2.0.0 | improvement | Language and timezone now set to user based on default App settings when not provided by IDP (Ticket #231488) |  |  |
| 1.0.3 | improvement | Language and timezone now set to user based on default App settings when not provided by IDP (Ticket #231488, #241569) |  |  |
| 1.0.3 | improvement | Enhanced UserProvisioning to eliminate redundant return value (Ticket #230774) | UserProvisioning |  |
| 1.0.2 | breaking | Extended length of UserClaim.Value attribute to be unlimited | UserClaim.Value |  |
| 1.0.1 | feature | Support of FriendlyName in CustomClaims Configuration |  |  |
| 1.0.1 | feature | Support of TimeZone in UserProvisioning |  |  |
| 1.0.1 | feature | Support of Language in UserProvisioning |  |  |
| 1.0.0 | requirement | UserCommons supported for Mendix 9.24.2 onwards |  |  |
| 1.0.0 | feature | Introduces ability to utilize custom user entities alongside default Administration.Account entity |  |  |
| 1.0.0 | feature | Facilitates accurate synchronization of Identity Provider attributes with entity attributes for enhanced data integrity |  |  |
| 1.0.0 | feature | Introduces possibility to configure UserType for provisioned users from same IdP source without custom microflow |  |  |
| 1.0.0 | feature | Facilitates setting default user role for any user created in app |  |  |
| 1.0.0 | feature | Empowers administrators with runtime configuration options for default user roles, types, and custom provisioning logic |  |  |
