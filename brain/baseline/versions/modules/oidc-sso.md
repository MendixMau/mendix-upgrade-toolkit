# OIDC SSO (Marketplace component 120371)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/120371)

| version | published | min Mendix |
|---|---|---|
| 4.7.0 | 2026-08-24 | 10.24.0 |
| 4.6.0 | 2026-07-10 | 10.24.0 |
| 4.5.0 | 2026-06-11 | 10.24.0 |
| 4.4.0 | 2026-04-13 | 10.24.0 |
| 4.3.0 | 2026-03-09 | 10.24.0 |
| 4.2.1 | 2026-01-26 | 10.24.0 |
| 4.2.0 | 2025-10-17 | 10.21.1 |
| 4.1.2 | 2025-08-05 | 10.21.1 |
| 4.1.1 | 2025-05-29 | 10.21.0 |
| 4.1.0 | 2025-05-15 | 10.21.1 |
| 4.0.1 | 2025-05-21 | 10.12.10 |
| 4.0.0 | 2024-12-24 | 10.12.10 |
| 3.6.0 | 2026-07-14 | 9.24.18 |
| 3.5.1 | 2026-06-24 | 9.24.18 |
| 3.5.0 | 2026-04-13 | 9.24.18 |
| 3.4.0 | 2026-03-09 | 9.24.18 |
| 3.3.1 | 2026-01-26 | 9.24.18 |
| 3.3.0 | 2025-10-20 | 9.24.18 |
| 3.2.1 | 2025-05-21 | 9.24.18 |
| 3.2.0 | 2024-11-05 | 9.24.18 |
| 3.1.0 | 2024-07-29 | 9.24.2 |
| 3.0.1 | 2024-06-11 | 9.24.2 |
| 3.0.0 | 2024-05-14 | 9.24.2 |
| 2.4.0 | 2024-03-27 | 9.24.2 |
| 2.3.2 | 2023-12-19 | 9.24.2 |
| 2.3.1 | 2023-11-15 | 9.24.2 |
| 2.3.0 | 2023-09-07 | 9.24.2 |
| 2.2.0 | 2023-07-13 | 9.24.2 |
| 2.1.1 | 2023-05-10 | 9.22.0 |
| 2.1.0 | 2023-03-15 | 9.22.0 |
| 2.0.0 | 2022-12-23 | 9.12.7 |
| 1.1.1 | 2022-12-02 | 9.12.5 |
| 1.1.0 | 2022-08-19 | 9.12.5 |
| 1.0.1 | 2022-06-15 | 9.8.1 |
| 1.0.0 | 2022-05-17 | 9.8.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 4.7.0 | requirement | Upgraded org.bouncycastle:bcpg-jdk18on, bcpkix-jdk18on, bcprov-jdk18on to version 1.85 | org.bouncycastle:bcpg-jdk18on, org.bouncycastle:bcpkix-jdk18on, org.bouncycastle:bcprov-jdk18on |  |
| 4.6.0 | removal | Dependency on netty library removed to reduce risk of transitive CVEs (Tickets #280205, #280754, #281745, #282429) | netty |  |
| 4.6.0 | improvement | Improved microflow call chain and dependencies to separate configuration business logic from UI actions |  |  |
| 4.5.0 | breaking | PKCE now enabled by default to improve security, without dependency on IdP's well-known endpoint | PKCE |  |
| 4.5.0 | breaking | Removed Anonymous user-role and related artifacts to simplify security model and reduce configuration dependencies | Anonymous user-role |  |
| 4.5.0 | requirement | Upgraded netty-codec-http to version 4.2.14.Final | netty-codec-http |  |
| 4.5.0 | security | Fixed CVE-2026-3505 |  |  |
| 4.4.0 | removal | Removed dependencies on Encryption module and Nanoflow. See documentation for migration | Encryption module, Nanoflow |  |
| 4.4.0 | removal | Ready-to-use token view page removed; UI snippet provided as template for custom implementations | token view page |  |
| 4.4.0 | breaking | Admins can only view decrypted content of their own token (Tickets #275225, #275311, #275327, #275656) |  |  |
| 4.4.0 | security | Fixed CVE-2025-40571. See Siemens Security Advisory SSA-726617 (Ticket #243660) |  |  |
| 4.4.0 | requirement | Upgraded netty-codec-http to version 4.2.12.Final | netty-codec-http |  |
| 4.2.1 | removal | MxReflection module dependency removed for better developer/upgrade experience | MxReflection module |  |
| 4.2.1 | removal | UserCommons migration logic removed | UserCommons migration logic |  |
| 4.2.1 | breaking | Translations removed; custom translations not overwritten when upgrading |  |  |
| 4.2.1 | improvement | AuthAttempt clean up logic refactored | AuthAttempt |  |
| 4.2.1 | breaking | Unlimited entity attributes lengths lowered down |  |  |
| 4.2.1 | breaking | Admin and User role Token entity access revised | Token entity |  |
| 4.2.1 | requirement | Upgraded io.netty:netty-codec-http to version 4.2.9.Final | io.netty:netty-codec-http |  |
| 4.2.1 | requirement | Upgraded com.nimbusds:nimbus-jose-jwt to version 10.5 | com.nimbusds:nimbus-jose-jwt |  |
| 4.2.1 | requirement | Upgraded commons-codec to version 1.19.0 | commons-codec |  |
| 4.2.0 | improvement | Easier to upgrade: ASU_STARTUP microflow moved under _USE ME folder and no longer includes automated user commons migration | ASU_STARTUP |  |
| 4.2.0 | migration-step | Migration logic for upgrading from versions below v3.0.0 moved to dedicated microflow under _USE ME → Migration |  |  |
| 4.2.0 | requirement | Upgraded org.apache.velocity:velocity-engine-core to version 2.4.1 | org.apache.velocity:velocity-engine-core |  |
| 4.2.0 | requirement | Upgraded com.nimbusds:nimbus-jose-jwt to version 10.4.1 | com.nimbusds:nimbus-jose-jwt |  |
| 4.2.0 | requirement | Upgraded org.apache.commons:commons-lang3 to version 3.19.0 | org.apache.commons:commons-lang3 |  |
| 4.2.0 | requirement | Added io.netty:netty-codec-http version 4.2.5.Final | io.netty:netty-codec-http |  |
| 4.2.0 | removal | Removed com.auth0:jwks-rsa and com.auth0:java-jwt dependencies | com.auth0:jwks-rsa, com.auth0:java-jwt |  |
| 4.2.0 | migration-step | Delete all Java libraries from userlib folder of old OIDC SSO module version before upgrading to avoid conflicting Java libraries |  |  |
| 4.1.1 | requirement | Version 4.1.1 for apps on Mendix 10.21.0; ensures compatibility with Mendix 11 |  |  |
| 4.1.0 | requirement | Version 4.1.0 for apps on Mendix 10.21.1 or higher |  |  |
| 4.1.0 | breaking | Anonymous user access no longer required; end-users can authenticate via /oauth/v2/login endpoint with multiple IdPs support | Anonymous user |  |
| 4.1.0 | breaking | Removed dependency on Administration module by replacing Administration.Account references with System.User (Ticket #229453) | Administration module |  |
| 4.1.0 | improvement | Improved ASU_OIDC_Startup to auto-create UserProvisioning objects for ClientConfigurations with empty UserProvisioningFlow (Ticket #238161) | ASU_OIDC_Startup |  |
| 4.1.0 | breaking | Fixed ReturnURL length in ClientConfig to 2048 characters to resolve login errors (Ticket #240374) | ReturnURL |  |
| 4.1.0 | security | Fixed CVE-2025-40571. See Siemens Security Advisory SSA-726617 (Ticket #243660) |  |  |
| 4.0.1 | breaking | Removed dependency on Administration module by replacing Administration.Account references with System.User (Ticket #229453) | Administration module |  |
| 4.0.1 | improvement | Improved ASU_OIDC_Startup to auto-create UserProvisioning objects for ClientConfigurations with empty UserProvisioningFlow (Ticket #238161) | ASU_OIDC_Startup |  |
| 4.0.1 | breaking | Fixed ReturnURL length in ClientConfig to 2048 characters to resolve login errors (Ticket #240374) | ReturnURL |  |
| 4.0.1 | security | Fixed CVE-2025-40571. See Siemens Security Advisory SSA-726617 (Ticket #243660) |  |  |
| 4.0.0 | requirement | Version 4.0.0 for apps on Mendix 10.12.10 or higher |  |  |
| 4.0.0 | removal | Removed OIDC.ACT_Account_RetrieveAccount microflow from _USE ME folder; now handled within module | OIDC.ACT_Account_RetrieveAccount |  |
| 3.6.0 | removal | Dependency on netty library removed to reduce risk of transitive CVEs (Tickets #280205, #280754, #281745, #282429) | netty |  |
| 3.5.1 | requirement | Upgraded io.netty:netty-codec-http to version 4.2.15.Final | io.netty:netty-codec-http |  |
| 3.5.0 | removal | Ready-to-use token view page removed; UI snippet provided as template for custom implementations | token view page |  |
| 3.5.0 | breaking | Admins can only view decrypted content of their own token (Tickets #275225, #275311, #275327, #275656) |  |  |
| 3.5.0 | security | Fixed CVE-2025-40571. See Siemens Security Advisory SSA-726617 (Ticket #243660) |  |  |
| 3.5.0 | requirement | Upgraded netty-codec-http to version 4.2.12.Final | netty-codec-http |  |
| 3.5.0 | requirement | Upgraded jackson-core to version 2.21.2 | jackson-core |  |
| 3.5.0 | migration-step | Delete all Java libraries from userlib folder of old OIDC SSO module version before upgrading to avoid conflicting Java libraries |  |  |
| 3.4.0 | requirement | Upgraded jackson-annotations to version 2.21.0 | jackson-annotations |  |
| 3.4.0 | requirement | Upgraded jackson-core to version 2.21.1 | jackson-core |  |
| 3.4.0 | migration-step | Delete all Java libraries from userlib folder of old OIDC SSO module version before upgrading to avoid conflicting Java libraries |  |  |
| 3.3.1 | improvement | AuthAttempt clean up logic refactored | AuthAttempt |  |
| 3.3.1 | breaking | Admin and User role Token entity access revised | Token entity |  |
| 3.3.1 | breaking | Translations removed; custom translations not overwritten when upgrading |  |  |
| 3.3.1 | breaking | Unlimited entity attributes lengths lowered down |  |  |
| 3.3.0 | feature | Token Encryption support has been added for compliance (Ticket #258462) |  |  |
| 3.3.0 | improvement | Improved XPath constraint for admin access to persisted tokens (Ticket #243660) |  |  |
| 3.3.0 | improvement | Improved implementation of nonce features |  |  |
| 3.3.0 | requirement | Upgraded com.nimbusds:nimbus-jose-jwt to version 10.4.1 | com.nimbusds:nimbus-jose-jwt |  |
| 3.3.0 | requirement | Added io.netty:netty-codec-http:4.2.5.Final | io.netty:netty-codec-http |  |
| 3.3.0 | migration-step | Delete all Java libraries used by old OIDC SSO module from userlib folder before upgrading |  |  |
| 3.2.1 | improvement | Improved ASU_OIDC_Startup to auto-create UserProvisioning objects for ClientConfigurations with empty UserProvisioningFlow (Ticket #238161) | ASU_OIDC_Startup |  |
| 3.2.1 | fix | Fixed ReturnURL length in ClientConfig to 2048 characters to resolve login errors (Ticket #240374) | ReturnURL |  |
| 3.2.0 | feature | Support of Microflow URLs with Query Parameters for continuation after login redirection |  |  |
| 3.2.0 | improvement | Enhanced user login by preventing logins for inactive users |  |  |
| 3.2.0 | feature | Supporting apps with subpath routing |  |  |
| 3.2.0 | fix | Fixed issue related to selected scope in deploytime Configuration (Ticket #224987) |  |  |
| 3.2.0 | requirement | Upgraded to Studio Pro version 9.24.18 |  |  |
| 3.2.0 | improvement | Improved MxModelReflection handling by refreshing modules to ensure backward compatibility | MxModelReflection |  |
| 3.2.0 | feature | New Cookie to clear cached session data during user login (Ticket #201728) |  |  |
| 3.2.0 | fix | Fixed issue related to Progressive Web App offline (Ticket #229872) |  |  |
| 3.2.0 | requirement | Upgraded com.nimbusds:nimbus-jose-jwt to version 9.41.2 (Ticket #224507,#224508,#224815,#229247) | com.nimbusds:nimbus-jose-jwt |  |
| 3.2.0 | requirement | Upgraded com.auth0:jwks-rsa to version 0.22.1 | com.auth0:jwks-rsa |  |
| 3.2.0 | migration-step | Delete all Java libraries used by old OIDC SSO module from userlib folder before upgrading |  |  |
| 3.1.0 | feature | Capability to validate Access Tokens (OAuth bearer tokens, JWT tokens) issued via OAuth Client Credential grant |  |  |
| 3.1.0 | feature | Configurations can be done from CI/CD pipeline at deploy-time using Application Constants or via Admin configuration UI at runtime |  |  |
| 3.1.0 | breaking | Renamed OIDC.Startup microflow as OIDC.ASU_OIDC_Startup | OIDC.Startup, OIDC.ASU_OIDC_Startup | OIDC.ASU_OIDC_Startup |
| 3.0.1 | security | Enhanced security by resolving weak sha1 algorithm detection in package-lock.json (Ticket#215455) |  |  |
| 3.0.1 | fix | Fixed base64 decoding issue in AzureRoleParse to handle JWT payloads with underscores (Ticket#217222) | AzureRoleParse |  |
| 3.0.1 | fix | Fixed auto-commit issue in OIDC.CodeChallengeMethodsSet during Automated Deploy-time SSO Configuration (Ticket#217387) | OIDC.CodeChallengeMethodsSet |  |
| 3.0.1 | removal | Removed Snip_Login_Automatic snippet from module; recommend using Snip_Login_Button snippet instead | Snip_Login_Automatic | Snip_Login_Button |
| 3.0.0 | feature | Users can be provisioned to Custom user entity without customizing the module |  |  |
| 3.0.0 | feature | When using Entra ID, default attribute mapping can be used; no need to configure attribute mapping |  |  |
| 3.0.0 | feature | User provisioning can set user_type (internal/external) based on IdP-level configuration |  |  |
| 3.0.0 | feature | User provisioning allows setting user's preferred language and timezone based on SSO response |  |  |
| 3.0.0 | feature | User provisioning can set default userrole, regardless of Access Token |  |  |
| 3.0.0 | feature | JIT user provisioning can be disabled, e.g. when users provisioned only via Administration module |  |  |
| 3.0.0 | feature | Select any custom microflow prefixed with 'OIDC_CustomUserParsing' for user provisioning |  |  |
| 3.0.0 | feature | Forward-compatible with Upcoming SCIM Module |  |  |
| 3.0.0 | requirement | Added UserCommons Module as new dependency for OIDC SSO | UserCommons |  |
| 3.0.0 | requirement | Mandatory to Set OIDC.Startup microflow as After Startup within settings | OIDC.Startup |  |
| 3.0.0 | fix | Fixed issue related to access token parsing microflow (Ticket#177243) |  |  |
| 3.0.0 | fix | Fixed issue related to Scope Value Attribute |  |  |
| 2.4.0 | feature | Support of Progressive Web App (PWA) |  |  |
| 2.4.0 | feature | Support of Page and Microflow URLs |  |  |
| 2.4.0 | feature | Support for Additional Scopes on deploytime Configuration |  |  |
| 2.4.0 | fix | Fixed issue with Token expires_in attribute (Ticket#206386) |  |  |
| 2.4.0 | requirement | Upgraded com.nimbusds:nimbus-jose-jwt to version 9.37.3 | com.nimbusds:nimbus-jose-jwt |  |
| 2.4.0 | migration-step | Delete all Java libraries used by old OIDC SSO module from userlib folder before upgrading |  |  |
| 2.3.2 | fix | Encoded the escaping special characters in URL for OIDC |  |  |
| 2.3.2 | requirement | Upgraded com.fasterxml.jackson.core:jackson-databind to 2.16.0 | com.fasterxml.jackson.core:jackson-databind |  |
| 2.3.2 | requirement | Upgraded com.fasterxml.jackson.core:jackson-annotations to 2.16.0 | com.fasterxml.jackson.core:jackson-annotations |  |
| 2.3.2 | requirement | Upgraded com.fasterxml.jackson.core:jackson-core to 2.16.0 | com.fasterxml.jackson.core:jackson-core |  |
| 2.3.2 | migration-step | Delete all Java libraries used by old OIDC SSO module from userlib folder before upgrading |  |  |
| 2.3.1 | fix | Fixed Java dependency issue in migration file for Mendix 10 compatibility |  |  |
| 2.3.1 | requirement | Upgraded org.json:json from 20230227 to 20231013 | org.json:json |  |
| 2.3.1 | migration-step | Delete all Java libraries used by old OIDC SSO module from userlib folder before upgrading |  |  |
| 2.3.0 | feature | Automation of SSO configuration via Application Constants set in CI/CD pipeline at deploytime |  |  |
| 2.3.0 | feature | Influence authentication at IDP using ACR feature |  |  |
| 2.3.0 | feature | Out-of-the-box microflow for standardized access token parsing for interaction with OIDC Provider module |  |  |
| 2.3.0 | requirement | Included migration file for Java dependencies for Studio Pro 10 compatibility |  |  |
| 2.3.0 | improvement | Enhanced error handling messages for authorized API calls (Ticket#173297) |  |  |
| 2.3.0 | removal | Dependency on 'Native Mobile Resources' module has been removed | Native Mobile Resources |  |
| 2.2.0 | improvement | Improvement for redirect URLs which may or may not have trailing slash '/' |  |  |
| 2.2.0 | fix | Fixed Mendix 10 compatibility issue (Ticket#190175) |  |  |
| 2.2.0 | requirement | Upgraded to Studio Pro v9.24.2 |  |  |
| 2.2.0 | requirement | Upgraded com.nimbusds:nimbus-jose-jwt to version 9.31 | com.nimbusds:nimbus-jose-jwt |  |
| 2.2.0 | migration-step | Delete all Java libraries used by old OIDC SSO module from userlib folder before upgrading |  |  |
| 2.1.1 | requirement | Upgraded org.json:json from 20220924 to 20230227 | org.json:json |  |
| 2.1.1 | migration-step | Delete all Java libraries used by old OIDC SSO module from userlib folder before upgrading |  |  |
| 2.1.0 | requirement | Upgraded to Mendix Studio Pro v9.22.0 |  |  |
| 2.0.0 | feature | Added support for authorizing access to Mendix back-end app using access token |  |  |
| 2.0.0 | breaking | Simplified structure for access token parsing microflows; breaking change for custom access token parsing microflows | ACT_Token_CustomATPRetrieveRoles |  |
| 2.0.0 | feature | Added introspection of Access Tokens and introspection endpoint field on OIDC configuration screen |  |  |
| 2.0.0 | feature | Added two out-of-the-box microflows for access token parsing (PIB and AzureAD) |  |  |
| 2.0.0 | improvement | Improved conditional check of handleAuthorizationCode microflow (Ticket#170579) |  |  |
| 2.0.0 | fix | Fixed issue related to cookies in Mendix studio pro-9.20 (Ticket#173282) |  |  |
| 1.1.1 | feature | Automatic Redirect to login page of Client if only one OIDC Client configured |  |  |
| 1.1.1 | requirement | Replaced org.json with org.json:json-20220924 | org.json:json |  |
| 1.1.1 | requirement | Upgraded com.fasterxml.jackson.core:jackson-core to 2.14.1 | com.fasterxml.jackson.core:jackson-core |  |
| 1.1.1 | requirement | Upgraded com.fasterxml.jackson.core:jackson-databind to 2.14.1 (Ticket #169884,#171349) | com.fasterxml.jackson.core:jackson-databind |  |
| 1.1.1 | requirement | Upgraded com.fasterxml.jackson.core:jackson-annotations to 2.14.1 | com.fasterxml.jackson.core:jackson-annotations |  |
| 1.1.1 | migration-step | Delete all Java libraries used by old OIDC SSO module from userlib folder before upgrading |  |  |
| 1.1.0 | feature | Added support for 'client_secret_basic' client authentication method; preferred over 'client_secret_post' |  |  |
| 1.1.0 | removal | Removed beta implementation of private_key_jwt client authentication | private_key_jwt |  |
| 1.1.0 | improvement | Configuration experience improved; now enforces mandatory fields: client_id and client_secret |  |  |
| 1.1.0 | feature | Added support for OIDC nonce parameter; usage mitigates replay attacks |  |  |
| 1.1.0 | removal | Removed PKCE configuration from UI; module auto-detects PKCE support through well-known endpoint |  |  |
| 1.1.0 | requirement | Upgraded url-parse package to 1.5.10 (Ticket #152019) | url-parse |  |
| 1.1.0 | requirement | Upgraded querystringify to 2.2.0 | querystringify |  |
| 1.0.1 | requirement | Jackson libraries upgraded to version 2.13.3 (Ticket #150849) | com.fasterxml.jackson.core: jackson-databind, com.fasterxml.jackson.core: jackson-annotations, com.fasterxml.jackson.core: jackson-core |  |
| 1.0.1 | migration-step | Delete all Java libraries used by old OIDC SSO module from userlib folder before upgrading |  |  |
| 1.0.0 | requirement | OIDC SSO supported for Mendix 9 onwards; no version available for Mendix 8 or 7 |  |  |
| 1.0.0 | known-issue | Usage with native mobile apps is not yet supported |  |  |
