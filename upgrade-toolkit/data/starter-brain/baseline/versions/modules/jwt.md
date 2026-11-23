# JWT (Marketplace component 106447)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Module, Ciphix, Community, [marketplace](https://marketplace.mendix.com/link/component/106447)

| version | published | min Mendix |
|---|---|---|
| 3.4.0 | 2026-06-09 | 11.6.6 |
| 3.3.3 | 2025-12-19 | 10.24.0 |
| 3.3.2 | 2024-03-13 | 9.18.4 |
| 3.3.1 | 2024-02-20 | 9.18.4 |
| 3.3.0 | 2023-07-26 | 8.12.5 |
| 3.2.2 | 2023-01-13 | 8.12.5 |
| 3.2.1 | 2021-06-04 | 8.12.5 |
| 3.2.0 | 2019-11-20 | 8.1.1 |
| 3.1.0 | 2019-10-30 | 8.1.1 |
| 3.0.0 | 2019-09-11 | 8.1.1 |
| 2.0.0 | 2019-05-29 | 7.13.1 |
| 1.6.0 | 2019-04-11 | 7.13.1 |
| 1.5.0 | 2018-11-02 | 7.13.1 |
| 1.4.1 | 2018-10-31 | 7.13.1 |
| 1.4.0 | 2018-10-26 | 7.13.1 |
| 1.3.0 | 2018-10-24 | 7.13.1 |
| 1.2.2 | 2018-06-12 | 7.13.1 |
| 1.2.1 | 2018-06-08 | 7.13.1 |
| 1.2.0 | 2018-06-08 | 7.13.1 |
| 1.1.0 | 2018-05-04 | 7.13.1 |
| 1.0.0 | 2018-04-05 | 7.13.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 3.4.0 | requirement | Minimum Mendix version raised to 11.6.6 | Mendix |  |
| 3.3.3 | requirement | Minimum Mendix version raised to 10.24.0 | Mendix |  |
| 3.3.2 | fix | Fixed hardcoded 3-year validity in generated public certificate; now respects specified years validity variable | public certificate validity |  |
| 3.3.1 | requirement | Updated to Mendix 9.18.4 minimum for Mendix 10 compatibility | Mendix |  |
| 3.3.1 | security | Resolved vulnerabilities |  |  |
| 3.3.0 | security | Upgraded Guava due to vulnerability | Guava |  |
| 3.2.2 | security | Updated JARs to fix security threat |  |  |
| 3.2.1 | requirement | Updated to Mendix 8.12.5 minimum for Mendix 9 compatibility | Mendix |  |
| 3.2.0 | improvement | Updated all dependencies to latest versions |  |  |
| 3.0.0 | requirement | Mendix 8 compatibility | Mendix |  |
| 2.0.0 | breaking | Fixed incomplete public key specification; now incompatible with public keys generated in previous versions | public keys |  |
| 2.0.0 | fix | Fixed import of X.509 public key certificates in key generation and key imports using signed certificates | X.509 public key certificates |  |
| 1.6.0 | improvement | Updated dependencies |  |  |
| 1.6.0 | known-issue | Jackson Core dependency uses system property; incompatible with Mendix free sandbox; disable Emulate Cloud security feature | Jackson Core |  |
| 1.4.1 | fix | Solved stream handling issues when reading RSA key pairs from S3 object store | S3 object store |  |
| 1.4.0 | breaking | Changed private key specification from PKCS8 to PKCS1 for JWT RS algorithms compatibility; added bouncycastle dependencies | private key specification |  |
| 1.2.2 | migration-step | Renamed public and private key entities for compatibility with Mendix Encryption module | public key entities, private key entities |  |
