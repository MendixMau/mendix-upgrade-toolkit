# Encryption (Marketplace component 1011)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/1011)

| version | published | min Mendix |
|---|---|---|
| 11.1.2 | 2026-08-18 | 10.24.0 |
| 11.1.1 | 2026-05-21 | 10.24.0 |
| 11.1.0 | 2025-11-19 | 10.24.0 |
| 11.0.3 | 2025-09-08 | 10.21.0 |
| 11.0.2 | 2025-07-08 | 10.21.0 |
| 11.0.1 | 2025-05-12 | 10.21.0 |
| 11.0.0 | 2025-04-10 | 10.21.0 |
| 10.0.9 | 2026-08-18 | 9.24.18 |
| 10.0.8 | 2026-05-21 | 9.24.18 |
| 10.0.7 | 2025-09-08 | 9.24.18 |
| 10.0.6 | 2025-05-12 | 9.24.18 |
| 10.0.5 | 2025-04-03 | 9.24.18 |
| 10.0.4 | 2025-03-18 | 9.24.18 |
| 10.0.3 | 2024-10-14 | 9.24.18 |
| 10.0.2 | 2024-06-21 | 9.24.18 |
| 9.0.3 | 2024-05-29 | 9.18.0 |
| 9.0.2 | 2023-08-23 | 9.18.0 |
| 9.0.1 | 2023-07-14 | 9.18.0 |
| 9.0.0 | 2023-04-19 | 9.18.0 |
| 8.0.6 | 2024-05-22 | 8.12.0 |
| 8.0.5 | 2023-07-14 | 8.12.0 |
| 8.0.4 | 2023-02-15 | 8.12.0 |
| 8.0.3 | 2022-10-24 | 8.12.0 |
| 8.0.2 | 2022-02-28 | 8.12.0 |
| 8.0.1 | 2022-02-16 | 8.12.0 |
| 8.0.0 | 2022-02-10 | 8.12.0 |
| 7.0.3 | 2023-07-14 | 7.23.22 |
| 7.0.2 | 2023-02-15 | 7.23.22 |
| 7.0.1 | 2022-02-28 | 7.23.22 |
| 7.0.0 | 2022-02-10 | 7.23.22 |
| 2.5.0 | 2022-01-12 | 8.12.0 |
| 2.4.0 | 2022-01-03 | 8.12.0 |
| 2.3.0 | 2021-09-01 | 8.12.0 |
| 2.2.0 | 2021-07-22 | 8.12.0 |
| 2.1.3 | 2021-07-02 | 8.12.0 |
| 2.1.1 | 2020-12-23 | 8.12.0 |
| 2.1.0 | 2020-12-18 | 8.12.0 |
| 2.0.1 | 2020-03-03 | 7.23.0 |
| 2.0.0 | 2019-06-14 | 7.23.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 11.1.2 | requirement | Upgraded BouncyCastle dependency to 1.85 | BouncyCastle |  |
| 11.1.1 | requirement | Upgraded BouncyCastle dependency to 1.84 | BouncyCastle |  |
| 11.1.0 | requirement | Upgraded module to Mendix 10.24.0 | Mendix |  |
| 11.1.0 | fix | Fixed issue where module could not be used when Gradle synchronization was disabled | Gradle synchronization |  |
| 11.0.3 | requirement | Upgraded Bouncy Castle dependency to 1.81 | BouncyCastle |  |
| 11.0.2 | fix | Fixed issue where 'not flagged for encryption' error occurred reading public key (Ticket 253606) | public key encryption |  |
| 11.0.1 | fix | Fixed issue where document encryption did not clean up temporary files (Ticket #247796) | document encryption |  |
| 11.0.0 | requirement | Upgraded Encryption module to Mendix 10.21.0 | Mendix |  |
| 10.0.9 | requirement | Upgraded BouncyCastle dependency to 1.85 | BouncyCastle |  |
| 10.0.8 | requirement | Upgraded BouncyCastle dependency to 1.84 | BouncyCastle |  |
| 10.0.7 | requirement | Upgraded Bouncy Castle dependency to 1.81 | BouncyCastle |  |
| 10.0.6 | fix | Fixed issue where document encryption did not clean up temporary files (Ticket #247796) | document encryption |  |
| 10.0.3 | requirement | Updated Apache Commons IO dependency to 2.17.0 (Tickets 230717, 230797) | Apache Commons IO |  |
| 10.0.3 | breaking | Changed AES/GCM/PKCS5PADDING to AES/GCM/NoPadding for Java 21 compatibility (Ticket 225806) | AES/GCM encryption |  |
| 10.0.2 | requirement | Upgraded Mendix version to 9.24.18 | Mendix |  |
| 10.0.2 | requirement | Upgraded Bouncy Castle version to 1.78.1 | BouncyCastle |  |
| 10.0.2 | breaking | Removed default value for EncryptionKey that was mistakenly introduced in 10.0.0 | EncryptionKey |  |
| 9.0.3 | requirement | Upgraded Bouncy Castle version to 1.78.1 | BouncyCastle |  |
| 9.0.2 | migration-step | Included migration file for Java dependencies for Studio Pro 10 compatibility | Java dependencies |  |
| 9.0.1 | requirement | Updated Bouncy Castle from version 1.70 to 1.75 | BouncyCastle |  |
| 9.0.0 | requirement | Updated module to Studio Pro 9.18 for use in Studio Pro 10 | Mendix |  |
| 8.0.6 | requirement | Upgraded Bouncy Castle version to 1.78.1 | BouncyCastle |  |
| 8.0.6 | migration-step | Remove jar files from userlib: bcpg-jdk18on-1.75.jar, bcpkix-jdk18on-1.75.jar, bcprov-jdk18on-1.75.jar | bcpg-jdk18on-1.75.jar, bcpkix-jdk18on-1.75.jar, bcprov-jdk18on-1.75.jar |  |
| 8.0.5 | requirement | Updated Bouncy Castle from version 1.70 to 1.75 | BouncyCastle |  |
| 8.0.4 | requirement | Updated Bouncy Castle from version 1.69 to 1.70 | BouncyCastle |  |
| 8.0.4 | migration-step | Remove jar files from userlib: bcpg-jdk15on-1.69.jar, bcpkix-jdk15on-1.69.jar, bcprov-jdk15on-1.69.jar | bcpg-jdk15on-1.69.jar, bcpkix-jdk15on-1.69.jar, bcprov-jdk15on-1.69.jar |  |
| 8.0.3 | requirement | Updated Apache Commons IO from version 2.8.0 to 2.11.0 | Apache Commons IO |  |
| 8.0.3 | migration-step | Remove jar file from userlib: commons-io-2.8.jar | commons-io-2.8.jar |  |
| 8.0.2 | requirement | Updated Apache Commons IO from version 2.7 to 2.8.0 | Apache Commons IO |  |
| 8.0.2 | migration-step | Remove jar file from userlib: commons-io-2.7.jar | commons-io-2.7.jar |  |
| 7.0.3 | requirement | Updated Bouncy Castle from version 1.69 to 1.75 | BouncyCastle |  |
| 7.0.2 | requirement | Updated Apache Commons IO from version 2.8.0 to 2.11.0 | Apache Commons IO |  |
| 7.0.2 | migration-step | Remove jar file from userlib if it exists: commons-io-2.8.0.jar | commons-io-2.8.0.jar |  |
| 7.0.1 | requirement | Updated Apache Commons IO from version 2.7 to 2.8.0 | Apache Commons IO |  |
| 7.0.1 | migration-step | Remove jar file from userlib if it exists: commons-io-2.7.jar | commons-io-2.7.jar |  |
| 7.0.0 | removal | Removed PGP document signing; removed SigningCertificate and SigningPrivateKey_Optional parameters | SigningCertificate, SigningPrivateKey_Optional, PGPEncryptDocument, Encrypt_Document |  |
| 7.0.0 | feature | Added new encryption algorithm with {AES3} prefix; encryption key now required to be 32 characters |  |  |
| 7.0.0 | migration-step | Decrypt and re-encrypt all database values; set LegacyEncryptionKey to 16-char key, EncryptionKey to 32-char key | EncryptionKey, LegacyEncryptionKey |  |
| 7.0.0 | improvement | Made encryption module stricter to disallow legacy encryption; legacy algorithms still decryptable |  |  |
| 7.0.0 | requirement | Updated dependencies |  |  |
| 7.0.0 | migration-step | Remove jar files from userlib if they exist: bcpg-jdk15on-164.jar, bcpkix-jdk15on-164.jar, bcprov-jdk15on-164.jar, commons-io-2.6.jar | bcpg-jdk15on-164.jar, bcpkix-jdk15on-164.jar, bcprov-jdk15on-164.jar, commons-io-2.6.jar |  |
| 2.4.0 | removal | Removed PGP document signing; removed SigningCertificate and SigningPrivateKey_Optional parameters | SigningCertificate, SigningPrivateKey_Optional, PGPEncryptDocument, Encrypt_Document |  |
| 2.3.0 | breaking | Reverted change where already-encrypted strings were encrypted again | Encrypt |  |
| 2.2.0 | feature | Added new encryption algorithm with {AES3} prefix; encryption key now required to be 32 characters |  |  |
| 2.2.0 | migration-step | Decrypt and re-encrypt all database values; set LegacyEncryptionKey to 16-char key, EncryptionKey to 32-char key | EncryptionKey, LegacyEncryptionKey |  |
| 2.2.0 | improvement | Strings now encrypted even if starting with prefix; legacy algorithms still decryptable |  |  |
| 2.2.0 | migration-step | Remove jar file from userlib: commons-io-2.6.jar | commons-io-2.6.jar |  |
| 2.1.3 | breaking | Made encryption module stricter to disallow legacy encryption |  |  |
| 2.1.3 | requirement | Updated dependencies |  |  |
| 2.1.1 | requirement | Upgraded BouncyCastle dependency | BouncyCastle |  |
| 2.1.1 | migration-step | Remove jar files from userlib if they exist: bcpg-jdk15on-164.jar, bcpkix-jdk15on-164.jar, bcprov-jdk15on-164.jar | bcpg-jdk15on-164.jar, bcpkix-jdk15on-164.jar, bcprov-jdk15on-164.jar |  |
| 2.1.0 | requirement | Updated Encryption module to Mendix 8.12.0 | Mendix |  |
| 2.0.1 | security | Updated dependencies fixing various vulnerabilities (Ticket 96070) |  |  |
| 2.0.1 | migration-step | Remove jar files from userlib: bcpg-jdk15on-150.jar, bcpkix-jdk15on-150.jar, bcprov-jdk15on-150.jar | bcpg-jdk15on-150.jar, bcpkix-jdk15on-150.jar, bcprov-jdk15on-150.jar |  |
| 2.0.0 | requirement | Updated to Mendix Studio Pro 7.23.0 for use in Mendix 7.23 and Mendix 8 projects | Mendix |  |
