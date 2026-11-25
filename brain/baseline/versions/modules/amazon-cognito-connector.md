# Amazon Cognito Connector (Marketplace component 203363)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Module, Mendix, Community, [marketplace](https://marketplace.mendix.com/link/component/203363)

| version | published | min Mendix |
|---|---|---|
| 2.0.0 | 2023-03-24 | 9.14.0 |
| 1.0.2 | 2023-01-16 | 9.13.0 |
| 1.0.0 | 2022-11-02 | 9.13.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 2.0.0 | removal | AWS Services module dependency removed. | AWS Services module | AWSAuthentication module |
| 2.0.0 | removal | AWS Services module related .Jar files removed. | AWS Services module .Jar files |  |
| 2.0.0 | requirement | AWSAuthentication module is now required as a dependency. | AWSAuthentication module |  |
| 2.0.0 | requirement | Cognito related .Jar files now included with the module. | Cognito related .Jar files |  |
| 2.0.0 | breaking | Static credentials storage in AWS Services module removed. Update breaks existing AWS credentials configuration. | AWS credentials configuration, Static credentials storage |  |
| 2.0.0 | feature | App configuration extended with credential choice (Static/Session) and storage capability. | App configuration |  |
| 2.0.0 | migration-step | Reconfigure AWS credentials following documentation guidance due to breaking changes. | AWS credentials configuration |  |
