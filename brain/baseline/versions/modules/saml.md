# SAML (Marketplace component 1174)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/1174)

| version | published | min Mendix |
|---|---|---|
| 4.2.3 | 2026-09-01 | 10.21.1 |
| 4.2.2 | 2026-08-20 | 10.21.1 |
| 4.2.1 | 2026-02-12 | 10.21.1 |
| 4.2.0 | 2025-10-22 | 10.21.1 |
| 4.1.2 | 2025-08-13 | 10.21.1 |
| 4.1.1 | 2025-05-29 | 10.21.1 |
| 4.1.0 | 2025-05-07 | 10.21.1 |
| 4.0.4 | 2025-10-22 | 10.12.10 |
| 4.0.3 | 2025-08-13 | 10.12.10 |
| 4.0.2 | 2025-05-07 | 10.12.10 |
| 4.0.1 | 2025-03-07 | 10.12.10 |
| 4.0.0 | 2025-01-09 | 10.12.10 |
| 3.6.27 | 2026-09-01 | 9.24.18 |
| 3.6.25 | 2026-08-20 | 9.24.18 |
| 3.6.23 | 2025-10-22 | 9.24.18 |
| 3.6.21 | 2025-08-07 | 9.24.18 |
| 3.6.19 | 2025-05-07 | 9.24.18 |
| 3.6.17 | 2025-03-07 | 9.24.18 |
| 3.6.15 | 2024-11-15 | 9.24.18 |
| 3.6.13 | 2024-10-09 | 9.24.18 |
| 3.6.11 | 2024-06-04 | 9.24.18 |
| 3.6.9 | 2024-04-11 | 9.24.1 |
| 3.6.8 | 2024-04-11 | 9.24.1 |
| 3.6.7 | 2023-11-09 | 9.24.1 |
| 3.6.6 | 2023-11-09 | 9.24.1 |
| 3.6.5 | 2023-09-25 | 9.24.1 |
| 3.6.4 | 2023-09-25 | 9.24.1 |
| 3.6.3 | 2023-05-25 | 9.24.1 |
| 3.6.2 | 2023-05-25 | 9.24.1 |
| 3.6.1 | 2023-05-10 | 9.24.1 |
| 3.6.0 | 2023-05-10 | 9.24.1 |
| 3.5.1 | 2023-04-27 | 9.22.0 |
| 3.5.0 | 2023-04-27 | 9.22.0 |
| 3.4.1 | 2023-03-30 | 9.22.0 |
| 3.4.0 | 2023-03-30 | 9.22.0 |
| 3.3.15 | 2023-07-12 | 9.12.14 |
| 3.3.14 | 2023-07-12 | 9.12.14 |
| 3.3.13 | 2023-02-20 | 9.12.5 |
| 3.3.12 | 2023-02-20 | 9.12.5 |
| 3.3.11 | 2023-01-19 | 9.12.5 |
| … 88 older versions | | |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 4.2.3 | security | Fixed account hijacking vulnerability in SAML-based authentication. Fixed CVE-2026-80465. |  |  |
| 4.2.2 | improvement | Updated Mobile Auth Token handling to use Mendix Runtime APIs for token and cookie management. | Mobile Auth Token |  |
| 4.2.2 | fix | Fixed TLS connection issue when connecting to DigiD using Artifact Binding. | DigiD, Artifact Binding |  |
| 4.2.2 | security | Fixed CVE-2026-71497. |  |  |
| 4.2.2 | requirement | Upgraded org.bouncycastle:bcpkix-jdk18on to 1.85. | org.bouncycastle:bcpkix-jdk18on |  |
| 4.2.2 | requirement | Upgraded org.bouncycastle:bcprov-jdk18on to 1.85. | org.bouncycastle:bcprov-jdk18on |  |
| 4.2.2 | requirement | Upgraded org.bouncycastle:bcutil-jdk18on to 1.85. | org.bouncycastle:bcutil-jdk18on |  |
| 4.2.2 | requirement | Upgraded org.jsoup:jsoup to 1.23.1. | org.jsoup:jsoup |  |
| 4.2.1 | feature | Enhanced SAML provisioning to support deploy-time population of named-user identifier for consistent multi-app user metering. | SAML provisioning |  |
| 4.2.1 | fix | Fixed SAML configuration issue when react client is enabled. | react client |  |
| 4.2.1 | requirement | SAML 4.2.1 requires UserCommons Module version 2.2.0 or higher. | UserCommons |  |
| 4.2.0 | feature | Enhancement for upgrades where Custom_IdPConfiguration microflow was removed and IdPConfiguration_MicroflowName constant introduced. | Custom_IdPConfiguration, IdPConfiguration_MicroflowName |  |
| 4.2.0 | fix | Fixed TLS connection issue when connected with DigiD via Artifact Binding. | DigiD, Artifact Binding |  |
| 4.2.0 | requirement | Upgraded org.bouncycastle:bcpkix-jdk18on to 1.81. | org.bouncycastle:bcpkix-jdk18on |  |
| 4.2.0 | requirement | Upgraded org.bouncycastle:bcprov-jdk18on to 1.81. | org.bouncycastle:bcprov-jdk18on |  |
| 4.2.0 | requirement | Upgraded org.bouncycastle:bcutil-jdk18on to 1.81. | org.bouncycastle:bcutil-jdk18on |  |
| 4.2.0 | deprecation | Deprecated saml1-post-binding.vm, saml2-post-artifact-binding.vm, saml2-post-simplesign-binding.vm. | saml1-post-binding.vm, saml2-post-artifact-binding.vm, saml2-post-simplesign-binding.vm |  |
| 4.1.2 | fix | Fixed resource path handling for SAML to support ApplicationRootUrl with subpath. | ApplicationRootUrl |  |
| 4.1.2 | security | Fixed CVE-2025-40758. |  |  |
| 4.1.2 | requirement | Upgraded org.apache.commons:commons-lang3 to version 3.18.0. | org.apache.commons:commons-lang3 |  |
| 4.1.0 | requirement | Version 4.1.0 for apps on Mendix 10.21.1 or higher. |  |  |
| 4.1.0 | fix | Fixed SAML20.X509Certificate.SerialNumber length. | SAML20.X509Certificate.SerialNumber |  |
| 4.1.0 | fix | Fixed deprecations to make module compatible with Mendix 10.21.1. |  |  |
| 4.0.4 | fix | Fixed TLS connection issue when connected with DigiD via Artifact Binding. | DigiD, Artifact Binding |  |
| 4.0.4 | requirement | Upgraded org.bouncycastle:bcpkix-jdk18on to 1.81. | org.bouncycastle:bcpkix-jdk18on |  |
| 4.0.4 | requirement | Upgraded org.bouncycastle:bcprov-jdk18on to 1.81. | org.bouncycastle:bcprov-jdk18on |  |
| 4.0.4 | requirement | Upgraded org.bouncycastle:bcutil-jdk18on to 1.81. | org.bouncycastle:bcutil-jdk18on |  |
| 4.0.4 | deprecation | Deprecated saml1-post-binding.vm, saml2-post-artifact-binding.vm, saml2-post-simplesign-binding.vm. | saml1-post-binding.vm, saml2-post-artifact-binding.vm, saml2-post-simplesign-binding.vm |  |
| 4.0.3 | fix | Fixed resource path handling for SAML to support ApplicationRootUrl with subpath. | ApplicationRootUrl |  |
| 4.0.3 | security | Fixed CVE-2025-40758. |  |  |
| 4.0.3 | requirement | Upgraded org.apache.commons:commons-lang3 to version 3.18.0. | org.apache.commons:commons-lang3 |  |
| 4.0.2 | fix | Fixed SAML20.X509Certificate.SerialNumber length. | SAML20.X509Certificate.SerialNumber |  |
| 4.0.1 | fix | Increased SAML20.X509Certificate.SerialNumber length to 1000 to support larger certificates. | SAML20.X509Certificate.SerialNumber |  |
| 4.0.1 | removal | Removed deprecated Model Reflection page. | Model Reflection page |  |
| 4.0.1 | requirement | Removed listenablefuture:9999.0-empty to avoid conflict with guava. | listenablefuture |  |
| 4.0.1 | deprecation | Deprecation for upcoming release: saml1-post-binding.vm, saml2-post-artifact-binding.vm, saml2-post-simplesign-binding.vm. | saml1-post-binding.vm, saml2-post-artifact-binding.vm, saml2-post-simplesign-binding.vm |  |
| 4.0.0 | feature | Allows SSO configurations to be set at design time or deploy time using Application Constants. |  |  |
| 4.0.0 | feature | Java Dependency Management (JDM) is supported. |  |  |
| 4.0.0 | feature | New mechanism for creating custom user-provisioning with enhanced similarity to OIDC SSO module. |  |  |
| 4.0.0 | breaking | evaluateMultipleUserMatches is migrated from SAML to usercommons. | evaluateMultipleUserMatches |  |
| 4.0.0 | requirement | SAML 4.0.0 requires Studio Pro version 10.12.10 or higher. |  |  |
| 4.0.0 | requirement | Added UserCommons Module as dependency for SAML. | UserCommons |  |
| 4.0.0 | migration-step | To resolve UI errors in upgrade scenario, upgrade Atlas Core to latest version. | Atlas Core |  |
| 4.0.0 | deprecation | Previous mechanism for user provisioning is deprecated and will not be supported in next SAML release. |  |  |
| 4.0.0 | breaking | Pre-configured possibility to use InCommon Federation is no longer supported. | InCommon Federation |  |
| 3.6.27 | security | Fixed account hijacking vulnerability in SAML-based authentication. Fixed CVE-2026-80465. |  |  |
| 3.6.25 | security | Fixed CVE-2026-71497. |  |  |
| 3.6.25 | requirement | Upgraded org.bouncycastle:bcpkix-jdk18on to 1.85. | org.bouncycastle:bcpkix-jdk18on |  |
| 3.6.25 | requirement | Upgraded org.bouncycastle:bcprov-jdk18on to 1.85. | org.bouncycastle:bcprov-jdk18on |  |
| 3.6.25 | requirement | Upgraded org.bouncycastle:bcutil-jdk18on to 1.85. | org.bouncycastle:bcutil-jdk18on |  |
| 3.6.25 | requirement | Upgraded org.jsoup:jsoup to 1.23.1. | org.jsoup:jsoup |  |
| 3.6.25 | migration-step | Delete all Java libraries from userlib folder of old SAML module before upgrading to avoid conflicts. |  |  |
| 3.6.23 | fix | Fixed TLS connection issue when connected with DigiD via Artifact Binding. | DigiD, Artifact Binding |  |
| 3.6.23 | fix | Increased SAML20.X509Certificate.SerialNumber length to 1000 to support larger certificates. | SAML20.X509Certificate.SerialNumber |  |
| 3.6.23 | requirement | Upgraded org.bouncycastle:bcpkix-jdk18on to 1.81. | org.bouncycastle:bcpkix-jdk18on |  |
| 3.6.23 | requirement | Upgraded org.bouncycastle:bcprov-jdk18on to 1.81. | org.bouncycastle:bcprov-jdk18on |  |
| 3.6.23 | requirement | Upgraded org.bouncycastle:bcutil-jdk18on to 1.81. | org.bouncycastle:bcutil-jdk18on |  |
| 3.6.23 | migration-step | Delete all Java libraries from userlib folder of old SAML module before upgrading to avoid conflicts. |  |  |
| 3.6.23 | deprecation | Deprecated saml1-post-binding.vm, saml2-post-artifact-binding.vm, saml2-post-simplesign-binding.vm. | saml1-post-binding.vm, saml2-post-artifact-binding.vm, saml2-post-simplesign-binding.vm |  |
| 3.6.21 | fix | Improved URL validation to fix redirect issues during SAML login. |  |  |
| 3.6.21 | security | Fixed CVE-2025-40758. |  |  |
| 3.6.21 | requirement | Upgraded org.apache.commons:commons-lang3 to version 3.18.0. | org.apache.commons:commons-lang3 |  |
| 3.6.21 | migration-step | Delete all Java libraries from userlib folder of old SAML module before upgrading to avoid conflicts. |  |  |
| 3.6.19 | fix | Fixed SAML20.X509Certificate.SerialNumber length. | SAML20.X509Certificate.SerialNumber |  |
| 3.6.17 | deprecation | Deprecation for upcoming release: saml1-post-binding.vm, saml2-post-artifact-binding.vm, saml2-post-simplesign-binding.vm. | saml1-post-binding.vm, saml2-post-artifact-binding.vm, saml2-post-simplesign-binding.vm |  |
| 3.6.15 | improvement | Enhanced XML parsing and improved handling of entity expansion and external entity resolution (Ticket #232023). | XML parsing, entity expansion, external entity resolution |  |
| 3.6.15 | requirement | Upgraded commons-io library to its latest version. | commons-io |  |
| 3.6.15 | migration-step | Delete all Java libraries used by the old SAML module from the userlib folder before upgrading. | userlib |  |
| 3.6.15 | removal | No longer supporting v.3.6.14 for Mx9 apps using Atlas UI v2 (e.g. Mx8 apps upgraded to Mx9). | 3.6.14, Atlas UI v2 |  |
| 3.6.11 | requirement | Upgraded Bouncy Castle version to 1.78.1 (Ticket #217944). | Bouncy Castle |  |
| 3.6.11 | migration-step | Delete all Java libraries used by the old SAML module from the userlib folder before upgrading. | userlib |  |
| 3.6.11 | removal | SAML module no longer supporting Mx9 apps using Atlas UI v2. | Atlas UI v2 |  |
| 3.6.11 | removal | Not planning to release v.3.6.10 for Mx9 apps using Atlas UI v2 (e.g. Mx8 apps upgraded to Mx9). | 3.6.10, Atlas UI v2 |  |
| 3.6.9 | security | Fixed Vulnerability - Cleartext Transmission of Sensitive Information (Ticket #204774). |  |  |
| 3.6.9 | requirement | Upgraded xmlsec library to its latest version. | xmlsec |  |
| 3.6.9 | migration-step | Delete all Java libraries used by the old SAML module from the userlib folder before upgrading. | userlib |  |
| 3.6.8 | security | Fixed Vulnerability - Cleartext Transmission of Sensitive Information (Ticket #204774). |  |  |
| 3.6.8 | requirement | Upgraded xmlsec library to its latest version. | xmlsec |  |
| 3.6.8 | migration-step | Delete all Java libraries used by the old SAML module from the userlib folder before upgrading. | userlib |  |
| 3.6.5 | requirement | Upgraded few libraries to latest versions (Ticket#194306). |  |  |
| 3.6.5 | removal | Removed unused libraries (Ticket#194306). |  |  |
| 3.6.5 | migration-step | Delete all Java libraries used by the old SAML module from the userlib folder before upgrading. | userlib |  |
| 3.6.4 | requirement | Upgraded few libraries to latest versions (Ticket#194306). |  |  |
| 3.6.4 | removal | Removed unused libraries (Ticket#194306). |  |  |
| 3.6.4 | migration-step | Delete all Java libraries used by the old SAML module from the userlib folder before upgrading. | userlib |  |
| 3.6.3 | deprecation | Solved deprecations to make the module Mendix 10 compatible. |  |  |
| 3.6.3 | requirement | Few java libraries updated to latest versions. |  |  |
| 3.6.3 | migration-step | Delete all Java libraries used by the old SAML module from the userlib folder before upgrading. | userlib |  |
| 3.6.2 | deprecation | Solved deprecations to make the module Mendix 10 compatible. |  |  |
| 3.6.2 | requirement | Few java libraries updated to latest versions. |  |  |
| 3.6.2 | migration-step | Delete all Java libraries used by the old SAML module from the userlib folder before upgrading. | userlib |  |
| 3.6.1 | breaking | Renamed ReadOnly role to Admin_ReadSAMLEntities. | ReadOnly | Admin_ReadSAMLEntities |
| 3.6.1 | security | Added fix of CVE-2023-25957 that prevents configuration mistakes when using POST binding on SAML responses. | POST binding, SAML responses |  |
| 3.6.1 | requirement | Upgraded to Studio Pro v9.24.1. | Studio Pro |  |
| 3.6.1 | improvement | SAML Module userlib includes only its dependency libraries (Ticket # 184521). | userlib |  |
| 3.6.1 | migration-step | If ReadOnly role used in App security, then update to Admin_ReadSAMLEntities role. | ReadOnly |  |
| 3.6.0 | breaking | Renamed ReadOnly role to Admin_ReadSAMLEntities. | ReadOnly | Admin_ReadSAMLEntities |
| 3.6.0 | security | Added fix of CVE-2023-25957 that prevents configuration mistakes when using POST binding on SAML responses. | POST binding, SAML responses |  |
| 3.6.0 | requirement | Upgraded to Studio Pro v9.24.1. | Studio Pro |  |
| 3.6.0 | improvement | SAML Module userlib includes only its dependency libraries (Ticket # 184521). | userlib |  |
| 3.6.0 | migration-step | If ReadOnly role used in App security, then update to Admin_ReadSAMLEntities role. | ReadOnly |  |
| 3.5.1 | feature | Support for independent keypairs per IDP that can be uploaded or self-generated; keystore configuration moved to IDP tab with automatic migration. | keypairs, IDP configuration |  |
| 3.5.1 | requirement | Require Encryption module as a dependency for v3.5.0 and above. | Encryption |  |
| 3.5.0 | feature | Support for independent keypairs per IDP that can be uploaded or self-generated; keystore configuration moved to IDP tab with automatic migration. | keypairs, IDP configuration |  |
| 3.5.0 | requirement | Require Encryption module as a dependency for v3.5.0 and above. | Encryption |  |
| 3.4.1 | requirement | Upgraded to Studio Pro v9.22.0. | Studio Pro |  |
| 3.4.1 | requirement | Upgraded com.fasterxml.woodstox:woodstox-core from 6.2.4.jar to 6.5.0.jar (Ticket # 180852). | woodstox-core |  |
| 3.4.1 | migration-step | Delete all Java libraries used by the old SAML module from the userlib folder before upgrading. | userlib |  |
| 3.4.0 | requirement | Upgraded to Studio Pro v9.22.0. | Studio Pro |  |
| 3.4.0 | requirement | Upgraded com.fasterxml.woodstox:woodstox-core from 6.2.4.jar to 6.5.0.jar (Ticket # 180852). | woodstox-core |  |
| 3.4.0 | migration-step | Delete all Java libraries used by the old SAML module from the userlib folder before upgrading. | userlib |  |
| 3.3.15 | breaking | Renamed ReadOnly role to Admin_ReadSAMLEntities. | ReadOnly | Admin_ReadSAMLEntities |
| 3.3.15 | security | Fixed CVE-2023-25957. |  |  |
| 3.3.15 | requirement | Few java libraries updated to latest versions. |  |  |
| 3.3.15 | migration-step | Delete all Java libraries used by the old SAML module from the userlib folder before upgrading. | userlib |  |
| 3.3.15 | migration-step | If ReadOnly role used in App security, then update to Admin_ReadSAMLEntities role. | ReadOnly |  |
| 3.3.14 | breaking | Renamed ReadOnly role to Admin_ReadSAMLEntities. | ReadOnly | Admin_ReadSAMLEntities |
| 3.3.14 | security | Fixed CVE-2023-25957. |  |  |
| 3.3.14 | requirement | Few java libraries updated to latest versions. |  |  |
| 3.3.14 | migration-step | Delete all Java libraries used by the old SAML module from the userlib folder before upgrading. | userlib |  |
| 3.3.14 | migration-step | If ReadOnly role used in App security, then update to Admin_ReadSAMLEntities role. | ReadOnly |  |
| 3.3.13 | requirement | Upgraded commons-io from 2.8.0 to 2.11.0 (Ticket #176198) | commons-io |  |
| 3.3.13 | breaking | Renamed all .Required file names to .RequiredLib in the userlib folder |  |  |
| 3.3.13 | migration-step | Delete all Java libraries used by the old SAML module from userlib folder before upgrading |  |  |
| 3.3.12 | requirement | Upgraded commons-io from 2.8.0 to 2.11.0 (Ticket #176198) | commons-io |  |
| 3.3.12 | breaking | Renamed all .Required file names to .RequiredLib in the userlib folder |  |  |
| 3.3.12 | migration-step | Delete all Java libraries used by the old SAML module from userlib folder before upgrading |  |  |
| 3.3.11 | requirement | Upgraded org.bouncycastle bcpkix-jdk15on-1.69 to jdk15to18-1.70 (Ticket #172523, #173264, #175781) | org.bouncycastle:bcpkix-jdk15on, org.bouncycastle:bcrov-jdk15on, org.bouncycastle:bcutil-jdk15on |  |
| 3.3.11 | requirement | Upgraded org.bouncycastle bcrov-jdk15on-1.69 to jdk15to18-1.70 (Ticket #172523, #173264, #175781) | org.bouncycastle:bcrov-jdk15on |  |
| 3.3.11 | requirement | Upgraded org.bouncycastle bcutil-jdk15on-1.69 to jdk15to18-1.70 (Ticket #172523, #173264, #175781) | org.bouncycastle:bcutil-jdk15on |  |
| 3.3.11 | migration-step | Delete all Java libraries used by the old SAML module from userlib folder before upgrading |  |  |
| 3.3.10 | requirement | Upgraded org.bouncycastle bcpkix-jdk15on-1.69 to jdk15to18-1.70 (Ticket #172523, #173264, #175781) | org.bouncycastle:bcpkix-jdk15on, org.bouncycastle:bcrov-jdk15on, org.bouncycastle:bcutil-jdk15on |  |
| 3.3.10 | requirement | Upgraded org.bouncycastle bcrov-jdk15on-1.69 to jdk15to18-1.70 (Ticket #172523, #173264, #175781) | org.bouncycastle:bcrov-jdk15on |  |
| 3.3.10 | requirement | Upgraded org.bouncycastle bcutil-jdk15on-1.69 to jdk15to18-1.70 (Ticket #172523, #173264, #175781) | org.bouncycastle:bcutil-jdk15on |  |
| 3.3.10 | migration-step | Delete all Java libraries used by the old SAML module from userlib folder before upgrading |  |  |
| 3.3.9 | security | Fixed security vulnerability (9.3 - CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:N/E:P/RL:O/RC:C) affecting v3.3.0 to v3.3.7 |  |  |
| 3.3.8 | security | Fixed security vulnerability (9.3 - CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:N/E:P/RL:O/RC:C) affecting v3.3.0 to v3.3.7 |  |  |
| 3.3.7 | breaking | Moved Authentication related configuration options from Provisioning tab to Request Authn context tab |  |  |
| 3.3.7 | requirement | Upgraded org.slf4j slf4j-api to 2.0.3 (Ticket #167757) | org.slf4j:slf4j-api, org.slf4j:slf4j-simple |  |
| 3.3.7 | requirement | Upgraded org.slf4j slf4j-simple to 2.0.3 (Ticket #167757) | org.slf4j:slf4j-simple |  |
| 3.3.7 | migration-step | Delete all Java libraries used by the old SAML module from userlib folder before upgrading |  |  |
| 3.3.6 | breaking | Moved Authentication related configuration options from Provisioning tab to Request Authn context tab |  |  |
| 3.3.6 | requirement | Upgraded org.slf4j slf4j-api to 2.0.3 (Ticket #167757) | org.slf4j:slf4j-api, org.slf4j:slf4j-simple |  |
| 3.3.6 | requirement | Upgraded org.slf4j slf4j-simple to 2.0.3 (Ticket #167757) | org.slf4j:slf4j-simple |  |
| 3.3.6 | migration-step | Delete all Java libraries used by the old SAML module from userlib folder before upgrading |  |  |
| 3.3.5 | security | Fixed CVE-2022-44457 |  |  |
| 3.3.4 | security | Fixed CVE-2022-44457 |  |  |
| 3.3.1 | requirement | Upgraded to latest LTS/MTS Studio pro v9.12.5 |  |  |
| 3.3.1 | security | Fixed CVE-2022-37011 |  |  |
| 3.3.1 | security | Fixed security vulnerability (9.1 – CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N) |  |  |
| 3.3.1 | requirement | Upgraded org.bouncycastle bcpkix-jdk15on to 1.69 (Ticket #152939) | org.bouncycastle:bcpkix-jdk15on, org.bouncycastle:bcrov-jdk15on, org.bouncycastle:bcutil-jdk15on |  |
| 3.3.1 | requirement | Upgraded org.bouncycastle bcrov-jdk15on to 1.69 (Ticket #152939) | org.bouncycastle:bcrov-jdk15on |  |
| 3.3.1 | requirement | Upgraded org.bouncycastle bcutil-jdk15on to 1.69 (Ticket #152939) | org.bouncycastle:bcutil-jdk15on |  |
| 3.3.1 | migration-step | Delete all Java libraries used by the old SAML module from userlib folder before upgrading |  |  |
| 3.3.0 | requirement | Upgraded to latest LTS/MTS Studio pro v9.12.5 |  |  |
| 3.3.0 | improvement | Improved message validation to better handle different parts of message being signed and/or encrypted |  |  |
| 3.3.0 | security | Fixed CVE-2022-37011 |  |  |
| 3.3.0 | security | Fixed security vulnerability (9.1 – CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N) |  |  |
| 3.3.0 | feature | In-Session Authentication |  |  |
| 3.3.0 | feature | Artifact binding on SAML responses |  |  |
| 3.3.0 | feature | Requesting user attributes at IDP via SAML's AttributeConsumingService concept |  |  |
| 3.3.0 | feature | Separate SP-metadata can be exported per IDP; SP-Metadata download moved from SP Configuration tab to IDP Configuration Overview tab |  |  |
| 3.3.0 | feature | Handling of encrypted nameID |  |  |
| 3.3.0 | requirement | Library upgrade: org.bouncycastle libraries (bcpkix-jdk15on, bcrov-jdk15on, bcutil-jdk15on) to 1.69 | org.bouncycastle:bcpkix-jdk15on, org.bouncycastle:bcrov-jdk15on, org.bouncycastle:bcutil-jdk15on |  |
| 3.3.0 | migration-step | Delete all Java libraries used by old SAML module from userlib folder before upgrading due to potential library conflicts |  |  |
| 3.2.7 | breaking | Renamed ReadOnly role to Admin_ReadSAMLEntities | ReadOnly | Admin_ReadSAMLEntities |
| 3.2.7 | security | Fixed CVE-2023-25957 |  |  |
| 3.2.7 | security | Fixed CVE-2022-37011 |  |  |
| 3.2.7 | requirement | Few Java libraries updated to latest versions |  |  |
| 3.2.7 | migration-step | Delete all Java libraries used by old SAML module from userlib folder before upgrading due to potential library conflicts |  |  |
| 3.2.7 | migration-step | If ReadOnly role used in App security, update to Admin_ReadSAMLEntities role | ReadOnly |  |
| 3.2.6 | breaking | Renamed ReadOnly role to Admin_ReadSAMLEntities | ReadOnly | Admin_ReadSAMLEntities |
| 3.2.6 | security | Fixed CVE-2023-25957 |  |  |
| 3.2.6 | security | Fixed CVE-2022-37011 |  |  |
| 3.2.6 | requirement | Few Java libraries updated to latest versions |  |  |
| 3.2.6 | migration-step | Delete all Java libraries used by old SAML module from userlib folder before upgrading due to potential library conflicts |  |  |
| 3.2.6 | migration-step | If ReadOnly role used in App security, update to Admin_ReadSAMLEntities role | ReadOnly |  |
| 3.2.5 | requirement | Library upgrades: woodstox-core to 6.2.4, stax2-api to 4.2.1 | com.fasterxml.woodstox:woodstox-core, org.codehaus.woodstox:stax2-api |  |
| 3.2.5 | migration-step | Delete all Java libraries used by old SAML module from userlib folder before upgrading due to potential library conflicts |  |  |
| 3.2.4 | requirement | Library upgrades: woodstox-core to 6.2.4, stax2-api to 4.2.1 | com.fasterxml.woodstox:woodstox-core, org.codehaus.woodstox:stax2-api |  |
| 3.2.4 | migration-step | Delete all Java libraries used by old SAML module from userlib folder before upgrading due to potential library conflicts |  |  |
| 3.2.3 | security | Fixed CVE-2022-32285 |  |  |
| 3.2.3 | security | Fixed CVE-2022-32286 |  |  |
| 3.2.2 | improvement | Expiry date for TokenInformation object can be set by overriding HybridAppLoginTimeOutInMinutes constant | TokenInformation, HybridAppLoginTimeOutInMinutes |  |
| 3.2.2 | improvement | Improved creation of mobile tokens to get consistent re-login on iOS devices |  |  |
| 3.2.2 | security | Fixed CVE-2022-32285 |  |  |
| 3.2.2 | security | Fixed CVE-2022-32286 |  |  |
| 3.2.1 | improvement | Logging made consistent with Mx7 version |  |  |
| 3.2.1 | fix | Fixed missing HttpOnly flag on cookies set by SAML Module |  |  |
| 3.2.1 | breaking | Removed library javax.xml.soap-api-1.4.0.jar and upgraded jakarta.xml.soap-api to version 2.0.1 | javax.xml.soap-api-1.4.0.jar, jakarta.xml.soap-api | jakarta.xml.soap-api-2.0.1 |
| 3.2.1 | migration-step | Delete all Java libraries used by old SAML module from userlib folder before upgrading due to potential library conflicts |  |  |
| 3.2.0 | improvement | Logging made consistent with Mx7 version |  |  |
| 3.2.0 | fix | Fixed missing HttpOnly flag on cookies set by SAML Module |  |  |
| 3.2.0 | breaking | Removed library javax.xml.soap-api-1.4.0.jar and upgraded jakarta.xml.soap-api to version 2.0.1 | javax.xml.soap-api-1.4.0.jar, jakarta.xml.soap-api | jakarta.xml.soap-api-2.0.1 |
| 3.2.0 | migration-step | Delete all Java libraries used by old SAML module from userlib folder before upgrading due to potential library conflicts |  |  |
| 3.1.9 | breaking | Increased the Value attribute's character limit in AssertionAttribute Entity | AssertionAttribute |  |
| 3.1.9 | improvement | Added AuthnRequestsSigned and WantAssertionsSigned attributes to SPSSODescriptor in SPMetadata when encryption is enabled | SPSSODescriptor |  |
| 3.1.9 | improvement | Custom provisioning and signing microflows are now configurable on IDP level in IDP Configuration |  |  |
| 3.1.8 | breaking | Increased the Value attribute's character limit in AssertionAttribute Entity | AssertionAttribute |  |
| 3.1.8 | improvement | Added AuthnRequestsSigned and WantAssertionsSigned attributes to SPSSODescriptor in SPMetadata when encryption is enabled | SPSSODescriptor |  |
| 3.1.8 | improvement | Custom provisioning and signing microflows are now configurable on IDP level in IDP Configuration |  |  |
| 3.1.7 | requirement | Library upgrade owasp-java-html-sanitizer from 20200713.1 to version 20211018.2 | owasp-java-html-sanitizer |  |
| 3.1.7 | migration-step | Delete all Java libraries used by old SAML module from userlib folder before upgrading due to potential library conflicts |  |  |
| 3.1.6 | requirement | Library upgrade owasp-java-html-sanitizer from 20200713.1 to version 20211018.2 | owasp-java-html-sanitizer |  |
| 3.1.6 | migration-step | Delete all Java libraries used by old SAML module from userlib folder before upgrading due to potential library conflicts |  |  |
| 3.1.5 | requirement | Library upgrades: org.apache.santuario:xmlsec to 2.2.3, org.apache.velocity:velocity-1.7 to velocity-engine-core 2.3 | org.apache.santuario:xmlsec, org.apache.velocity:velocity-engine-core |  |
| 3.1.5 | migration-step | Delete all Java libraries used by old SAML module from userlib folder before upgrading due to potential library conflicts |  |  |
| 3.1.4 | requirement | Library upgrades: org.apache.santuario:xmlsec to 2.2.3, org.apache.velocity:velocity-1.7 to velocity-engine-core 2.3 | org.apache.santuario:xmlsec, org.apache.velocity:velocity-engine-core |  |
| 3.1.4 | migration-step | Delete all Java libraries used by old SAML module from userlib folder before upgrading due to potential library conflicts |  |  |
| 3.1.3 | requirement | Mx9 New version supports Atlas 3.0 UI for apps newly developed in Mx9, compatible with Studio Pro 9.1.0 through 9.3.0 |  |  |
| 3.1.3 | improvement | Logging confirming to the LogLevel settings and Mendix standard |  |  |
| 3.1.2 | requirement | Mx9 Upgrade version supports Atlas 2.0 UI for apps upgrading from Mx8/Mx7 to Mx9, compatible with Studio Pro 9.1.0 through 9.3.0 |  |  |
| 3.1.2 | improvement | Logging confirming to the LogLevel settings and Mendix standard |  |  |
| 3.1.1 | requirement | Supports Atlas 3.0 UI, compatible with Studio Pro 9.1.0 through 9.3.0 | Atlas 3.0 |  |
| 3.0.5 | requirement | Supports Atlas 2.0 UI, compatible with Studio Pro 9.1.0 through 9.3.0 | Atlas 2.0 |  |
| 2.4.8 | security | Fixed CVE-2025-40758 |  |  |
| 2.4.7 | improvement | Improvement to index file to work with CSP headers (Ticket #240984) | index file |  |
| 2.4.7 | requirement | Upgraded commons-pool to 2.11.1 | commons-pool |  |
| 2.4.7 | requirement | Upgraded cryptacular to 1.2.5 | cryptacular |  |
| 2.4.7 | requirement | Upgraded httpclient to 4.5.14 | httpclient |  |
| 2.4.7 | requirement | Upgraded httpcore to 4.4.16 | httpcore |  |
| 2.4.7 | requirement | Upgraded jakarta.xml.soap-api to 3.0.0 | jakarta.xml.soap-api |  |
| 2.4.7 | requirement | Upgraded java-support to 7.5.2 | java-support |  |
| 2.4.7 | requirement | Upgraded joda-time to 2.12.5 | joda-time |  |
| 2.4.7 | requirement | Upgraded jsoup to 1.16.1 | jsoup |  |
| 2.4.7 | requirement | Upgraded metrics-core to 4.2.18 | metrics-core |  |
| 2.4.7 | requirement | Upgraded opensaml to 3.4.6 | opensaml |  |
| 2.4.7 | requirement | Upgraded slf4j-api to 2.0.7 | slf4j-api |  |
| 2.4.7 | requirement | Upgraded txw2 to 4.0.2 | txw2 |  |
| 2.4.7 | requirement | Upgraded xercesImpl to 2.12.2-sp1 | xercesImpl |  |
| 2.4.7 | migration-step | Delete all Java libraries used by old SAML module from userlib folder before upgrading |  |  |
| 2.4.7 | deprecation | Following files will be deprecated: saml1-post-binding.vm, saml2-post-artifact-binding.vm, saml2-post-simplesign-binding.vm | saml1-post-binding.vm, saml2-post-artifact-binding.vm, saml2-post-simplesign-binding.vm |  |
| 2.4.6 | improvement | Enhanced XML parsing and improved entity expansion and external entity resolution (Ticket #232023) | XML parsing |  |
| 2.4.6 | requirement | Upgraded commons-io library to latest version | commons-io |  |
| 2.4.6 | migration-step | Delete all Java libraries used by old SAML module from userlib folder before upgrading |  |  |
| 2.4.4 | requirement | Upgraded Bouncy Castle version to 1.78.1 (Ticket #217944) | Bouncy Castle |  |
| 2.4.4 | migration-step | Delete all Java libraries used by old SAML module from userlib folder before upgrading |  |  |
| 2.4.3 | improvement | Removed static nonce and inline scripts in SAML Custom Login page (Ticket #207361) | SAML Custom Login page |  |
| 2.4.3 | security | Fixed vulnerability - Cleartext Transmission of Sensitive Information (Ticket #204774) |  |  |
| 2.4.3 | requirement | Upgraded xmlsec library to latest version | xmlsec |  |
| 2.4.3 | migration-step | Delete all Java libraries used by old SAML module from userlib folder before upgrading |  |  |
| 2.4.1 | improvement | Improvement to index file to work with CSP headers (Ticket #184978) | index file |  |
| 2.4.1 | requirement | Upgraded several libraries to latest versions (Ticket #194306) |  |  |
| 2.4.1 | improvement | Removed unused libraries (Ticket #194306) |  |  |
| 2.4.1 | migration-step | Delete all Java libraries used by old SAML module from userlib folder before upgrading |  |  |
| 2.4.0 | breaking | Renamed ReadOnly role to Admin_ReadSAMLEntities | ReadOnly role | Admin_ReadSAMLEntities |
| 2.4.0 | security | Added fix of CVE-2023-25957 preventing configuration mistakes using POST binding on SAML responses | POST binding |  |
| 2.4.0 | migration-step | If ReadOnly role used in App security, update to Admin_ReadSAMLEntities role | ReadOnly role |  |
| 2.3.7 | requirement | Upgraded woodstox-core from 6.2.4 to 6.5.0 (Ticket #180852) | woodstox-core |  |
| 2.3.7 | migration-step | Delete all Java libraries used by old SAML module from userlib folder before upgrading |  |  |
| 2.3.6 | requirement | Upgraded commons-io from 2.8.0 to 2.11.0 (Ticket #176198) | commons-io |  |
| 2.3.6 | migration-step | Renamed all .Required file names to .RequiredLib in userlib folder |  |  |
| 2.3.6 | migration-step | Delete all Java libraries used by old SAML module from userlib folder before upgrading |  |  |
| 2.3.5 | requirement | Upgraded bcpkix-jdk15on from 1.69 to jdk15to18-1.70 (Ticket #172523) | bcpkix-jdk15on |  |
| 2.3.5 | requirement | Upgraded bcrov-jdk15on from 1.69 to jdk15to18-1.70 (Ticket #173264) | bcrov-jdk15on |  |
| 2.3.5 | requirement | Upgraded bcutil-jdk15on from 1.69 to jdk15to18-1.70 (Ticket #175781) | bcutil-jdk15on |  |
| 2.3.5 | migration-step | Delete all Java libraries used by old SAML module from userlib folder before upgrading |  |  |
| 2.3.4 | security | Fixed security vulnerability (9.3 - CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:N/E:P/RL:O/RC:C) |  |  |
| 2.3.3 | breaking | Moved Authentication related configuration options from Provisioning tab to Request Authn context tab | Provisioning tab, Request Authn context tab |  |
| 2.3.3 | requirement | Upgraded slf4j-api to 2.0.3 (Ticket #167757) | slf4j-api |  |
| 2.3.3 | requirement | Upgraded slf4j-simple to 2.0.3 (Ticket #167757) | slf4j-simple |  |
| 2.3.3 | migration-step | Delete all Java libraries used by old SAML module from userlib folder before upgrading |  |  |
| 2.3.2 | security | Fixed CVE-2022-44457 |  |  |
| 2.3.0 | requirement | Upgraded to latest LTS/MTS Studio Pro v8.18.19 |  |  |
| 2.3.0 | improvement | Improved message validation to better handle different parts being signed/encrypted | message validation |  |
| 2.3.0 | security | Fixed CVE-2022-37011 |  |  |
| 2.3.0 | security | Fixed security vulnerability (9.1 – CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N) |  |  |
| 2.3.0 | requirement | Upgraded bcpkix-jdk15on to 1.69 (Ticket #152939) | bcpkix-jdk15on |  |
| 2.3.0 | requirement | Upgraded bcrov-jdk15on to 1.69 (Ticket #152939) | bcrov-jdk15on |  |
| 2.3.0 | requirement | Upgraded bcutil-jdk15on to 1.69 (Ticket #152939) | bcutil-jdk15on |  |
| 2.3.0 | migration-step | Delete all Java libraries used by old SAML module from userlib folder before upgrading |  |  |
| 2.2.3 | requirement | com.fasterxml.woodstox:woodstox-core upgraded to 6.2.4; org.codehaus.woodstox:stax2-api upgraded to 4.2.1 | com.fasterxml.woodstox:woodstox-core, org.codehaus.woodstox:stax2-api |  |
| 2.2.3 | migration-step | Delete all Java libraries from old SAML module in userlib folder before upgrading due to potential conflicts |  |  |
| 2.2.2 | improvement | Expiry date for TokenInformation can be set by overriding HybridAppLoginTimeOutInMinutes constant | TokenInformation, HybridAppLoginTimeOutInMinutes |  |
| 2.2.2 | migration-step | Renamed lognode SAML to SAML_SSO in example microflows to prevent extra unused lognode | SAML, SAML_SSO | SAML_SSO |
| 2.2.2 | security | Fixed CVE-2022-32285 |  |  |
| 2.2.2 | security | Fixed CVE-2022-32286 |  |  |
| 2.2.1 | requirement | Removed javax.xml.soap-api-1.4.0.jar; upgraded jakarta.xml.soap-api to 2.0.1 | javax.xml.soap-api, jakarta.xml.soap-api | jakarta.xml.soap-api-2.0.1 |
| 2.2.1 | migration-step | Delete all Java libraries from old SAML module in userlib folder before upgrading due to potential conflicts |  |  |
| 2.2.0 | improvement | Increased Value attribute character limit in AssertionAttribute Entity | AssertionAttribute |  |
| 2.2.0 | improvement | Added AuthnRequestsSigned and WantAssertionsSigned attributes to SPSSODescriptor in SPMetadata when encryption enabled | SPSSODescriptor, SPMetadata |  |
| 2.2.0 | improvement | Custom provisioning and signing microflows now configurable on IDP level in IDP Configuration |  |  |
| 2.1.9 | requirement | Library upgrade owasp-java-html-sanitizer to version 20211018.2 | owasp-java-html-sanitizer |  |
| 2.1.9 | migration-step | Delete all Java libraries from old SAML module in userlib folder before upgrading due to potential conflicts |  |  |
| 2.1.8 | requirement | Library upgrade org.apache.santuario:xmlsec to version 2.2.3 | org.apache.santuario:xmlsec |  |
| 2.1.8 | requirement | Upgraded org.apache.velocity:velocity-1.7 to org.apache.velocity:velocity-engine-core version 2.3 | org.apache.velocity:velocity-engine-core | org.apache.velocity:velocity-engine-core-2.3 |
| 2.1.8 | migration-step | Delete all Java libraries from old SAML module in userlib folder before upgrading due to potential conflicts |  |  |
| 2.1.6 | requirement | Library upgrades bcpkix-jdk15on and bcprov-jdk15on to version 1.67 | bcpkix-jdk15on, bcprov-jdk15on |  |
| 2.1.6 | migration-step | Delete all Java libraries from old SAML module in userlib folder; especially BountyCastle libraries may conflict |  |  |
| 2.1.5 | improvement | MxSAMLAssertion ValidationLevel configuration always considered as ValidationLevel.Strict as security measure | MxSAMLAssertion, ValidationLevel |  |
| 2.1.5 | migration-step | Delete all Java libraries from old SAML module; especially opensaml-2.6.6.jar may cause conflicts |  |  |
| 2.1.4 | requirement | Library update commons-lang to version 2.6 | commons-lang |  |
| 2.1.4 | requirement | Library update jakarta.xml.soap-api to version 1.4.1 | jakarta.xml.soap-api |  |
| 2.1.3 | requirement | Update to xercesImpl-2.12.1-sp1 | xercesImpl |  |
| 2.1.2 | security | SAML20 JAR library upgrade fixing multiple important vulnerabilities |  |  |
| 2.1.2 | requirement | requiredLib folder updates | requiredLib |  |
| 2.1.2 | requirement | Library upgrade Gauva from version 27 to 31 | Gauva |  |
| 2.0.0 | requirement | Converted module to Mendix 8.0.0.56467 |  |  |
| 1.18.0 | breaking | Renamed ReadOnly role to Admin_ReadSAMLEntities; update in App security if used | ReadOnly | Admin_ReadSAMLEntities |
| 1.18.0 | security | Fixed CVE-2023-25957 preventing configuration mistakes when using POST binding on SAML responses |  |  |
| 1.17.5 | requirement | Library upgrade com.fasterxml.woodstox:woodstox-core from 6.2.4 to 6.5.0 | com.fasterxml.woodstox:woodstox-core |  |
| 1.17.5 | migration-step | Delete all Java libraries from old SAML module in userlib folder before upgrading due to potential conflicts |  |  |
| 1.17.3 | security | Fixed security vulnerability CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N |  |  |
| 1.17.3 | requirement | Library upgrade commons-io from 2.8.0 to 2.11.0 | commons-io |  |
| 1.17.3 | migration-step | Renamed all .Required file names to .RequiredLib in userlib folder |  |  |
| 1.17.3 | migration-step | Delete all Java libraries from old SAML module in userlib folder before upgrading due to potential conflicts |  |  |
| 1.17.2 | security | Fixed CVE-2022-44457 |  |  |
| 1.17.2 | improvement | Added Force Authentication as configurable option in Request Authn context tab |  |  |
| 1.17.2 | breaking | Moved Authentication configuration options from Provisioning tab to Request Authn context tab |  |  |
| 1.17.2 | requirement | Library upgrade org.slf4j:slf4j-api and slf4j-simple to 2.0.3 | org.slf4j:slf4j-api, org.slf4j:slf4j-simple |  |
| 1.17.2 | migration-step | Delete all Java libraries from old SAML module in userlib folder before upgrading due to potential conflicts |  |  |
| 1.17.0 | requirement | Upgraded to latest LTS/MTS Studio Pro v7.23.32 |  |  |
| 1.17.0 | security | Fixed CVE-2022-37011 |  |  |
| 1.17.0 | requirement | Library upgrade org.bouncycastle:bcpkix-jdk15on, bcprov-jdk15on, bcutil-jdk15on to 1.69 | org.bouncycastle:bcpkix-jdk15on, org.bouncycastle:bcprov-jdk15on, org.bouncycastle:bcutil-jdk15on |  |
| 1.17.0 | migration-step | Delete all Java libraries from old SAML module in userlib folder before upgrading due to potential conflicts |  |  |
| 1.16.7 | migration-step | Delete all Java libraries from userlib folder before upgrading due to potential conflicts between old and new versions. | Java libraries |  |
| 1.16.7 | improvement | Upgraded com.fasterxml.woodstox:woodstox-core to 6.2.4 and org.codehaus.woodstox:stax2-api to 4.2.1. | com.fasterxml.woodstox:woodstox-core, org.codehaus.woodstox:stax2-api |  |
| 1.16.6 | breaking | Renamed lognode SAML to SAML_SSO in example microflows to prevent unused lognode. | lognode, SAML | SAML_SSO |
| 1.16.6 | security | Fixed CVE-2022-32285. |  |  |
| 1.16.6 | security | Fixed CVE-2022-32286. |  |  |
| 1.16.5 | migration-step | Delete all Java libraries from userlib folder before upgrading due to potential conflicts. | javax.xml.soap-api-1.4.0.jar |  |
| 1.16.5 | improvement | Removed javax.xml.soap-api-1.4.0.jar and upgraded jakarta.xml.soap-api-1.4.1.jar to 2.0.1. | javax.xml.soap-api, jakarta.xml.soap-api |  |
| 1.16.4 | breaking | Increased character limit in AssertionAttribute Entity's Value attribute. | AssertionAttribute, Value |  |
| 1.16.3 | improvement | Upgraded owasp-java-html-sanitizer to version 20211018.2. | owasp-java-html-sanitizer |  |
| 1.16.3 | migration-step | Delete all Java libraries from userlib folder before upgrading due to potential conflicts. | Java libraries |  |
| 1.16.2 | improvement | Upgraded org.apache.santuario:xmlsec to 2.2.3 and org.apache.velocity:velocity-engine-core to 2.3. | org.apache.santuario:xmlsec, org.apache.velocity:velocity-engine-core |  |
| 1.16.2 | migration-step | Delete all Java libraries from userlib folder before upgrading due to potential conflicts. | Java libraries |  |
| 1.16.0 | improvement | Upgraded bcpkix-jdk15on and bcprov-jdk15on to v1.67 to fix Eclipse environment issues. | bcpkix-jdk15on, bcprov-jdk15on |  |
| 1.16.0 | migration-step | Delete all Java libraries from userlib folder before upgrading; BountyCastle versions may conflict. | Java libraries, BountyCastle |  |
| 1.15.5 | migration-step | Delete all Java libraries from userlib folder; opensaml library conflicts may occur. | Java libraries, opensaml |  |
| 1.15.4 | improvement | Updated commons-lang to 2.6 and jakarta.xml.soap-api to 1.4.1. | commons-lang, jakarta.xml.soap-api |  |
| 1.15.3 | improvement | Updated xercesImpl to 2.12.1-sp1. | xercesImpl |  |
| 1.15.2 | security | Upgraded SAML20 JAR library to fix multiple vulnerabilities. | SAML20 JAR library |  |
| 1.15.2 | improvement | Updated requiredLib folder. | requiredLib folder |  |
| 1.15.2 | improvement | Upgraded Guava library from 27 to 31. | Guava |  |
| 1.13.0 | migration-step | Domain model update requires migration: click migration button on Request Authn Context tab for all IdP settings. | Request Authn Context, IdP Configuration |  |
| 1.12.0 | requirement | Upgraded to Mx7.9; Atlas UI requires at least Mx7.9. | Mendix |  |
| 1.11.0 | improvement | Updated to OpenSAML version 2.6.6. | OpenSAML |  |
| 1.11.0 | improvement | Updated various JAR libraries with known vulnerabilities to more recent versions. | Java libraries |  |
| 1.10.1 | requirement | Upgraded to Mx7.5.1. | Mendix |  |
| 1.10.0 | security | Two security fixes implemented; all customers recommended to update. |  |  |
| 1.9 | requirement | Updated to Mendix 7.0.2. | Mendix |  |
