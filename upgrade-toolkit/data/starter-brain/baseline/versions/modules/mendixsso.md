# MendixSSO (Marketplace component 111349)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Module, Mendix, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/111349)

| version | published | min Mendix |
|---|---|---|
| 10.6.2 | 2026-08-25 | 10.24.0 |
| 10.6.1 | 2026-05-11 | 10.24.0 |
| 10.6.0 | 2026-02-26 | 10.24.0 |
| 10.5.0 | 2025-07-21 | 10.21.0 |
| 10.4.0 | 2025-06-27 | 10.21.0 |
| 10.3.0 | 2025-04-28 | 10.21.0 |
| 10.2.0 | 2025-03-07 | 10.6.15 |
| 10.1.0 | 2025-02-04 | 10.6.15 |
| 10.0.0 | 2024-10-03 | 10.6.15 |
| 9.4.2 | 2026-08-26 | 9.24.0 |
| 9.4.1 | 2026-05-11 | 9.24.0 |
| 9.4.0 | 2025-10-08 | 9.24.0 |
| 9.3.0 | 2025-07-21 | 9.24.0 |
| 9.2.0 | 2025-03-07 | 9.24.0 |
| 9.1.0 | 2025-02-04 | 9.24.0 |
| 9.0.0 | 2024-03-20 | 9.24.0 |
| 4.2.0 | 2023-10-25 | 9.24.0 |
| 4.1.0 | 2023-04-17 | 9.24.0 |
| 4.0.2 | 2023-03-27 | 9.20.0 |
| 4.0.1 | 2023-01-24 | 9.20.0 |
| 4.0.0 | 2023-01-24 | 9.18.3 |
| 3.4.0 | 2025-03-10 | 8.18.28 |
| 3.3.0 | 2025-02-04 | 8.18.28 |
| 3.2.0 | 2024-03-20 | 8.18.28 |
| 3.1.1 | 2022-10-20 | 8.18.11 |
| 3.1.0 | 2022-08-10 | 8.18.11 |
| 3.0.0 | 2021-10-19 | 8.18.11 |
| 2.4.0 | 2021-05-27 | 8.12.5 |
| 2.3.1 | 2021-03-19 | 8.12.5 |
| 2.3.0 | 2020-12-23 | 8.12.5 |
| 2.2.2 | 2020-12-23 | 7.23.19 |
| 2.2.1 | 2020-06-19 | 7.23.3 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 10.6.2 | requirement | Upgraded io.netty:netty-codec-http to 4.2.17.Final and org.apache.httpcomponents.client5:http-client-version to 5.6.3 | io.netty:netty-codec-http, org.apache.httpcomponents.client5:http-client-version |  |
| 10.6.1 | requirement | netty-codec-http library upgraded to version 4.2.12.Final | netty-codec-http |  |
| 10.6.1 | removal | decryptUsingLegacyAlgorithm method removed to improve module security posture | decryptUsingLegacyAlgorithm |  |
| 10.6.1 | improvement | Multi domain platform session support improved |  |  |
| 10.6.0 | requirement | Mendix runtime upgraded to 10.24.0 | Mendix runtime |  |
| 10.6.0 | requirement | Netty codec-http library upgraded to version 4.2.5.Final | netty codec-http |  |
| 10.6.0 | requirement | Apache commons-lang3 library upgraded to version 3.18.0 | Apache commons-lang3 |  |
| 10.6.0 | requirement | Nimbus oauth2-oidc-sdk library upgraded to version 11.28 | Nimbus oauth2-oidc-sdk |  |
| 10.6.0 | requirement | Nimbus nimbus-jose-jwt library upgraded to version 10.4.2 | Nimbus nimbus-jose-jwt |  |
| 10.4.0 | improvement | Deprecated runtime methods replaced to ensure full compatibility with Mendix 11 |  |  |
| 10.3.0 | requirement | Mendix runtime upgraded to 10.21.0 for Mendix 11 support | Mendix runtime |  |
| 10.3.0 | requirement | Apache commons-text library upgraded to version 1.13.1 | Apache commons-text |  |
| 10.3.0 | requirement | Netty codec-http library upgraded to version 4.2.0.Final | Netty codec-http |  |
| 10.2.0 | requirement | Nimbus oauth2-oidc-sdk library upgraded to version 11.23.1 | Nimbus oauth2-oidc-sdk |  |
| 10.1.0 | migration-step | Page URLs support added. Replace login.html with resources/mendixsso/templates/login-with-mendixsso-automatically.html | login.html |  |
| 10.1.0 | requirement | Nimbus oauth2-oidc-sdk library upgraded to version 11.21 | Nimbus oauth2-oidc-sdk |  |
| 10.1.0 | requirement | Nimbus nimbus-jose-jwt library upgraded to version 10.0.1 | Nimbus nimbus-jose-jwt |  |
| 10.1.0 | known-issue | Module contains vulnerable version of nimbus-jose-jwt library. Update to v10.2.0 or higher | Nimbus nimbus-jose-jwt |  |
| 10.0.0 | fix | Stale data cleanup logic refactored and fixed based on Mendix 10 behavioral/structural changes |  |  |
| 10.0.0 | known-issue | Module contains vulnerable version of nimbus-jose-jwt library. Update to v10.2.0 or higher | Nimbus nimbus-jose-jwt |  |
| 9.4.2 | security | Fixed CVE-2026-42584, CVE-2026-42579, CVE-2026-42581 |  |  |
| 9.4.2 | requirement | Upgraded io.netty:netty-codec-http to 4.2.17.Final and org.apache.httpcomponents.client5:http-client-version to 5.6.3 | io.netty:netty-codec-http, org.apache.httpcomponents.client5:http-client-version |  |
| 9.4.1 | requirement | netty-codec-http library upgraded to version 4.2.12.Final | netty-codec-http |  |
| 9.4.1 | removal | decryptUsingLegacyAlgorithm method removed to improve module security posture | decryptUsingLegacyAlgorithm |  |
| 9.4.1 | improvement | Multi domain platform session support improved |  |  |
| 9.4.0 | requirement | Netty codec-http library upgraded to version 4.1.125.Final | Netty codec-http |  |
| 9.4.0 | requirement | Apache commons-lang3 library upgraded to version 3.18.0 | Apache commons-lang3 |  |
| 9.4.0 | requirement | Nimbus oauth2-oidc-sdk library upgraded to version 11.28 | Nimbus oauth2-oidc-sdk |  |
| 9.4.0 | requirement | Nimbus nimbus-jose-jwt library upgraded to version 10.4.2 | Nimbus nimbus-jose-jwt |  |
| 9.2.0 | requirement | Nimbus oauth2-oidc-sdk library upgraded to version 11.23.1 | Nimbus oauth2-oidc-sdk |  |
| 9.1.0 | requirement | Nimbus oauth2-oidc-sdk library upgraded to version 11.21 | Nimbus oauth2-oidc-sdk |  |
| 9.1.0 | requirement | Nimbus nimbus-jose-jwt library upgraded to version 10.0.1 | Nimbus nimbus-jose-jwt |  |
| 9.1.0 | known-issue | Module contains vulnerable version of nimbus-jose-jwt library. Update to v9.2.0 or higher | Nimbus nimbus-jose-jwt |  |
| 9.0.0 | requirement | Nimbus oauth2-oidc-sdk library upgraded to version 11.10.1 | Nimbus oauth2-oidc-sdk |  |
| 9.0.0 | requirement | Nimbus nimbus-jose-jwt library upgraded to version 9.37.3 | Nimbus nimbus-jose-jwt |  |
| 9.0.0 | breaking | Cipher algorithm changed to AES/GCM/NoPadding to support Mendix 10.6.0 or newer |  |  |
| 9.0.0 | known-issue | Module contains vulnerable version of nimbus-jose-jwt library. Update to v9.2.0 or higher | Nimbus nimbus-jose-jwt |  |
| 4.2.0 | breaking | ContinuationURL parameter now validated before redirecting. Custom domains require MendixSSO_AllowedContinuationURLs environment variable | ContinuationURL |  |
| 4.2.0 | breaking | EmailAddress and OpenID removed from UserProfile entity. EmailAddress available as $EmailAddress parameter, OpenID via GetLegacyOpenIDForSSOUser | UserProfile, EmailAddress, OpenID |  |
| 4.2.0 | migration-step | Update customized MendixSSO_CreateUser and MendixSSO_UpdateUser microflows to add $EmailAddress parameter | MendixSSO_CreateUser, MendixSSO_UpdateUser |  |
| 4.2.0 | breaking | User UUID and EmailAddress now parsed from ID token subject and email claims instead of Mendix profile claim |  |  |
| 4.2.0 | migration-step | Internal microflow GetSignupHint renamed to GetDefaultSignupHint | GetSignupHint | GetDefaultSignupHint |
| 4.2.0 | known-issue | Module contains vulnerable version of nimbus-jose-jwt library. Update to v9.0.0 or higher | Nimbus nimbus-jose-jwt |  |
| 4.1.0 | requirement | Solved deprecations to make module Mendix 10 compatible |  |  |
| 4.1.0 | requirement | Nimbus oauth2-oidc-sdk library updated to 10.7.1 including json-smart 2.4.10 | Nimbus oauth2-oidc-sdk |  |
| 4.1.0 | migration-step | Updated pom.xml dependency manager file | pom.xml |  |
| 4.1.0 | known-issue | Module contains vulnerable version of nimbus-jose-jwt library. Update to v9.0.0 or higher | Nimbus nimbus-jose-jwt |  |
| 4.0.2 | security | Solved security concern where regular user role had access to decrypted access tokens via XAS request access rules |  |  |
| 4.0.2 | requirement | Nimbus oauth2-oidc-sdk library upgraded to 10.7 | Nimbus oauth2-oidc-sdk |  |
| 4.0.2 | requirement | json-smart library upgraded to 2.4.10, resolving CVE-2023-1370 | json-smart |  |
| 4.0.2 | known-issue | Module contains vulnerable version of nimbus-jose-jwt library. Update to v9.0.0 or higher | Nimbus nimbus-jose-jwt |  |
| 4.0.1 | requirement | Module upgraded to Mendix version 9.20.0 | Mendix version |  |
| 4.0.1 | improvement | Module prepends __Host parameter to cookie names if app uses HTTPS connection |  |  |
| 4.0.1 | known-issue | Module contains vulnerable version of nimbus-jose-jwt library. Update to v9.0.0 or higher | Nimbus nimbus-jose-jwt |  |
| 4.0.0 | requirement | Module upgraded to Mendix version 9.18.3 | Mendix version |  |
| 4.0.0 | requirement | Nimbus oauth2-oidc-sdk library upgraded to 10.5 | Nimbus oauth2-oidc-sdk |  |
| 4.0.0 | requirement | Nimbus nimbus-jose-jwt library upgraded to 9.24.4 | Nimbus nimbus-jose-jwt |  |
| 4.0.0 | known-issue | Module contains vulnerable version of nimbus-jose-jwt library. Update to v9.0.0 or higher | Nimbus nimbus-jose-jwt |  |
| 3.4.0 | requirement | Nimbus oauth2-oidc-sdk library upgraded to version 11.23.1 | Nimbus oauth2-oidc-sdk |  |
| 3.2.0 | requirement | Nimbus oauth2-oidc-sdk library upgraded to version 11.10.1 | Nimbus oauth2-oidc-sdk |  |
| 3.2.0 | requirement | Nimbus nimbus-jose-jwt library upgraded to version 9.37.3 | Nimbus nimbus-jose-jwt |  |
| 3.1.1 | requirement | Updated commons-text to version 1.10 and commons-lang3 to version 3.12 | commons-text, commons-lang3 |  |
| 3.1.0 | improvement | Updated /userlib/ folder jar libraries, readded utility functions, improved error pages, tightened security rules, bug fixes |  |  |
| 3.0.0 | removal | All UI pages and snippets for displaying OIDC token details were removed. Move them from previous versions before upgrading. | UI pages, snippets |  |
| 3.0.0 | breaking | Updated jar libraries incompatible with previous versions. Clean /userlib/ folder, remove old .jar.MendixSSO.RequiredLib versions, keep only .jar.MendixSSO.3.0.0. | userlib, jar libraries |  |
| 3.0.0 | known-issue | Silent Authentication feature is not compatible with the Deeplink module. | Silent Authentication, Deeplink module |  |
| 2.4.0 | requirement | Made module compatible with Mendix 9.1.1. | Mendix |  |
| 2.3.0 | requirement | Converted to Mendix 8.12.5. | Mendix |  |
| 2.3.0 | fix | Fixed deprecated Core.execute() calls in Java logic for Mendix 9 compatibility. | Core.execute() |  |
| 2.2.2 | requirement | Converted to Mendix 7.23.19. | Mendix |  |
| 2.2.2 | improvement | Updated commons-text and oauth2-oidc-sdk module libraries and sub-dependencies. | commons-text, oauth2-oidc-sdk |  |
| 2.2.2 | migration-step | Updated NotifyRolesChanged API published location to avoid conflict with old REST module implementation. | NotifyRolesChanged API |  |
| 2.2.1 | breaking | DS_GetForeignIdentity microflow now accepts generic System.User object as input. | DS_GetForeignIdentity |  |
| 2.2.1 | breaking | Renamed GetOpenIDForSSOUser microflow to GetLegacyOpenIDForSSOUser. | GetOpenIDForSSOUser | GetLegacyOpenIDForSSOUser |
| 2.2.1 | improvement | Refactored some microflows in Identity Propagation default implementation for consistency between REST and oData. | Identity Propagation |  |
| 2.2.1 | known-issue | Deprecated Rest Services module is incompatible with MendixSSO 2.2.0+. | Rest Services module |  |
