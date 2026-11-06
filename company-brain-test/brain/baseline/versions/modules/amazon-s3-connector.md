# Amazon S3 Connector (Marketplace component 120340)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/120340)

| version | published | min Mendix |
|---|---|---|
| 5.2.0 | 2026-04-28 | 10.21.0 |
| 5.1.0 | 2026-02-12 | 10.21.0 |
| 5.0.2 | 2025-11-06 | 10.21.0 |
| 4.2.1 | 2025-04-09 | 9.24.2 |
| 4.1.0 | 2024-09-27 | 9.24.2 |
| 4.0.1 | 2024-08-08 | 9.18.0 |
| 3.1.0 | 2024-07-23 | 9.18.0 |
| 3.0.0 | 2024-03-08 | 9.18.0 |
| 2.0.2 | 2024-01-23 | 9.18.0 |
| 1.1.1 | 2023-04-07 | 9.18.0 |
| 1.0.1 | 2022-09-15 | 9.12.1 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 5.2.0 | breaking | Client-side encryption upgraded to AWS V4 algorithm; not backwards compatible with V3 encryption. Check AWS documentation for migration scenarios. | client-side encryption |  |
| 5.2.0 | fix | Bugfix in client-side encryption when using AWS temporary credentials. | client-side encryption, AWS temporary credentials |  |
| 5.2.0 | security | Fixed vulnerabilities in dependencies of client-side encryption. | client-side encryption dependencies |  |
| 5.1.0 | feature | Created ClientsideEncryptionConfig object that enables KMS Clientside Encryption for S3 files. | ClientsideEncryptionConfig |  |
| 5.1.0 | improvement | GetObject updated to look for ClientsideEncryptionConfig and use KMS encryption if it exists. | GetObject |  |
| 5.1.0 | improvement | PutObject updated to look for ClientsideEncryptionConfig and use KMS encryption if it exists. | PutObject |  |
| 5.0.2 | breaking | Renamed HeadObject caption in Toolbox from "Head Bucket" to "Head Object". | HeadObject |  |
| 5.0.2 | fix | Bug fix: file reading from Mendix core API now uses BufferedInputStream for better retry and buffering support. | file reading |  |
| 5.0.2 | requirement | Upgraded to Mendix version 10.21.0. | Mendix |  |
| 5.0.2 | migration-step | Third party jar dependencies now configured in module; removed from user lib. Manual cleanup of user lib required. | jar dependencies |  |
| 4.2.1 | improvement | HeadBucket action updated to use up-to-date AWS regions from Authentication module. | HeadBucket, Authentication module |  |
| 4.1.0 | improvement | Upgraded S3 SDK to version 2.27.17. | S3 SDK |  |
| 4.0.1 | migration-step | Migration file added for Mendix 10 support. | Mendix 10 |  |
| 3.1.0 | feature | Added HeadBucket operation. | HeadBucket |  |
| 3.0.0 | breaking | Connector updated to work with Authentication Connector 3.0+. Region must be specified as input for CreateBucket. | Authentication Connector, CreateBucket |  |
| 2.0.2 | migration-step | Migration file added for Mendix 10.3+ to rebuild dependencies with Mendix Java Dependency Management feature. | Mendix 10.3+, Java Dependency Management |  |
| 1.1.1 | requirement | Module upgraded to Mendix Studio Pro 9.18.0. | Mendix Studio Pro |  |
| 1.1.1 | improvement | Upgraded json-smart Java library from version 2.4.8 to 2.4.10. | json-smart |  |
| 1.0.1 | security | Security fix: updated userlib and removed unused jar files. | userlib |  |
