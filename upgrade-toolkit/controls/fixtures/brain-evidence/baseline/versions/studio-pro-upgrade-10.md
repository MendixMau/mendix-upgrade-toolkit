# Studio Pro 10 upgrade notes (synthetic control fixture for release_impact.py --evidence)

Six rows, one per verdict: open with evidence, a hit only in a Marketplace module, two environment rows, a row with no
name to search, and a deprecation the app uses.

| version | date | type | area | change | affected | source |
|---|---|---|---|---|---|---|
| 10.1.0 | Mar 2 | removal | runtime | No longer support custom reason phrases in HTTP responses. | ReasonPhrase | [notes](https://docs.mendix.com/releasenotes/studio-pro/10.1/) |
| 10.1.0 | Mar 2 | removal | runtime | Fixture: removed the FixtureLegacyHookQq setting. | FixtureLegacyHookQq | [notes](https://docs.mendix.com/releasenotes/studio-pro/10.1/) |
| 10.1.0 | Mar 2 | removal | data-storage | Dropped support for MariaDB 10.3, no longer supported by the vendor. | MariaDB 10.3 | [notes](https://docs.mendix.com/releasenotes/studio-pro/10.1/) |
| 10.1.0 | Mar 2 | requirement | runtime | Fixture: the runtime now needs Java 21. | Java 21 | [notes](https://docs.mendix.com/releasenotes/studio-pro/10.1/) |
| 10.1.0 | Mar 2 | breaking | client-web | Fixture: changed the order in which a page loads its parts. | page loading | [notes](https://docs.mendix.com/releasenotes/studio-pro/10.1/) |
| 10.1.0 | Mar 2 | deprecation | java-actions | Deprecated Core.executeVoid; use Core.execute instead. | Core.executeVoid | [notes](https://docs.mendix.com/releasenotes/studio-pro/10.1/) |
