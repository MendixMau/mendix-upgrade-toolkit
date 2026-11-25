# OpenIDConnect Single Sign-on Community Support (OIDC, OAuth2, SSO) (Marketplace component 117529)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Module, Mendix, Deprecated, [marketplace](https://marketplace.mendix.com/link/component/117529)

| version | published | min Mendix |
|---|---|---|
| 3.3.3 | 2023-01-25 | 9.8.1 |
| 3.3.1 | 2022-05-02 | 9.8.1 |
| 3.3.0 | 2022-04-27 | 9.8.1 |
| 3.2.0 | 2022-04-16 | 9.8.1 |
| 3.1.0 | 2021-11-29 | 8.18.0 |
| 2.2.0 | 2021-07-30 | 8.12.0 |
| 2.1.0 | 2021-07-23 | 8.12.0 |
| 1.0.0 | 2021-05-24 | 8.12.0 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 3.3.3 | requirement | Added support for Mendix 9.20+ | Java dependencies |  |
| 3.3.3 | migration-step | Updated Java dependencies - CLEAN UP YOUR USERLIB FOLDER | userlib |  |
| 3.3.1 | fix | Fix for race condition bug during native mobile login | native mobile login |  |
| 3.3.0 | fix | Fix for native login error | native login |  |
| 3.2.0 | requirement | Added support for Mendix 9.8 and up, where AuthTokens are now encrypted | AuthTokens |  |
| 3.1.0 | feature | Added support for the DeepLink module | DeepLink module |  |
| 2.2.0 | fix | Scopes were getting double-url-encoded causing errors during login | scopes |  |
| 2.1.0 | removal | Removes dependency on Administration module by moving OIDC.Token association from Administration.Account to System.User | Administration module |  |
| 2.1.0 | breaking | Replaces configuration pages with snippets to improve portability and dependency on specific page layouts | configuration pages |  |
| 2.1.0 | removal | Removes Native Mobile Resources widgets from package - correct version installed from Marketplace for Mendix 8 or 9 | Native Mobile Resources widgets |  |
