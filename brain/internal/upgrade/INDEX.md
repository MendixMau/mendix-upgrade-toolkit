# Upgrade field notes

Short notes from real Mendix upgrades: pitfalls, procedures and version facts. Every note is `draft-unreviewed`;
check the cited Mendix documentation before acting on one. Grep an error code or keyword: `grep -rli "CE0463" .`

| kind | note |
|---|---|
| decision | [Keep the Dojo client when upgrading to Mx11; switch to React as a separate project](mx11-keep-dojo-client-during-upgrade.md) |
| decision | [Choosing a starting Studio Pro version and when to upgrade](studio-pro-version-choice.md) |
| pitfall | [Agents Kit 2 upgrade blocked for OpenAI apps; Agent Editor supports only Mendix Cloud GenAI](agents-kit-2-agent-editor-provider-limit.md) |
| pitfall | [Community Commons update needs PDFBox 3.x and commons-io 2.12+ JARs in userlib](community-commons-pdfbox3-userlib-mismatch.md) |
| pitfall | [Design property oldNames migration fails on direct 10.24 to 11.12 jump](design-property-oldnames-mx11-path.md) |
| pitfall | [Docker Buildpack upgrade changes the mendix user UID and breaks NFS permissions](docker-buildpack-uid-change-breaks-nfs.md) |
| pitfall | [Tracked node_modules and huge change sets crash Studio Pro version-control panels](git-node-modules-and-mass-deletions-crash-studio-pro.md) |
| pitfall | [Xcode duplicate symbols linker error after upgrading to 9.24](ios-duplicate-symbols-after-9-24.md) |
| pitfall | [SQL Server connection fails with PKIX error after the JDBC driver upgrade](mssql-jdbc-tls-pkix-after-upgrade.md) |
| pitfall | [Mx10.24 changed generated widget HTML IDs, breaking ID-based CSS and test selectors](mx10-24-generated-html-ids-changed.md) |
| pitfall | [Mx10 Dart Sass rejects LibSass-era mixed-unit arithmetic (CE6093)](mx10-dart-sass-mixed-unit-arithmetic.md) |
| pitfall | [Switching to direct association storage runs startup migrations and extends downtime](mx10-direct-association-migration-downtime.md) |
| pitfall | [Mx10 data-widget-wrapper div and reference selector class move break custom CSS selectors](mx10-dom-wrapper-breaks-css-selectors.md) |
| pitfall | [Mx10 Java compile errors from final action parameters and removed rollbackTransAction](mx10-java-action-final-params-rollbacktransaction.md) |
| pitfall | [LibGit2Sharp 'repository path is not owned by current user' when opening in Mx10](mx10-libgit2sharp-repo-ownership-error.md) |
| pitfall | [Mx10 scheduled events have a 1-minute minimum interval](mx10-scheduled-events-minimum-interval.md) |
| pitfall | [Mx11: Client date formatting changed to support genitive and abbreviated month names](mx11-client-date-format-change.md) |
| pitfall | [Mx11: Dojo client is deprecated and will be removed in Mendix 12](mx11-client-dojo-deprecated.md) |
| pitfall | [Mx11: mx.ui.downloadFile and mx.data.getFileUrl are now asynchronous](mx11-client-downloadfile-async.md) |
| pitfall | [Mx11: DynamicValue types for web file/image properties are deprecated, removal planned for Mendix 12](mx11-client-dynamicvalue-deprecated.md) |
| pitfall | [Mx11: JavaScript actions must not use the Dojo-era client APIs](mx11-client-forbidden-dojo-apis.md) |
| pitfall | [Mx11: Generated HTML IDs lost their numeric part and gained l or p prefixes](mx11-client-html-id-prefix.md) |
| pitfall | [Mx11: Client API mx.logger removed](mx11-client-mx-logger.md) |
| pitfall | [Mx11: Offline PWA storage migrates from IndexedDB to OPFS on first load, delaying startup](mx11-client-pwa-offline-storage-migration.md) |
| pitfall | [Mx11: The scope parameter was removed from subscribe in mx-api/data](mx11-client-subscribe-scope.md) |
| pitfall | [Mx11: Apps with unmigrated pre-5.12 local file documents are blocked from starting](mx11-data-legacy-file-docs-blocked.md) |
| pitfall | [Mx11: Offline sync now rejects changes from entities with Online/Nothing/Never sync modes](mx11-data-offline-sync-stricter.md) |
| pitfall | [Mx11: DataStorage.OptimizeSecurityColumns now defaults to true](mx11-data-security-columns.md) |
| pitfall | [Mx11: The sql_mode driver parameter is no longer set for MySQL and MariaDB](mx11-data-sql-mode.md) |
| pitfall | [Mx11: Strict mode for offline apps can break code still using retrieve_by_xpath](mx11-data-strict-mode-offline-xpath.md) |
| pitfall | [Mx11: The XPath API now uses limited XPath by default](mx11-data-xpath-api-limited.md) |
| pitfall | [Mx11: Downgrading a database deployed with a newer Mendix version is disallowed](mx11-db-downgrade-disallowed.md) |
| pitfall | [Mx11: jdbc:mysql: is no longer accepted as a database protocol](mx11-db-mysql-protocol.md) |
| pitfall | [Mx11: Support was dropped for MariaDB 10.5, SQL Server 2019 and MySQL 8.0](mx11-db-version-dropped-11-4.md) |
| pitfall | [Mx11: Support was dropped for PostgreSQL 13 and MariaDB 10.6](mx11-db-version-support-dropped.md) |
| pitfall | [Mx11: Document Templates is deprecated](mx11-docgen-templates-deprecated.md) |
| pitfall | [Mx11: Extensions can no longer obtain the studioPro object directly](mx11-extension-studiopro-access.md) |
| pitfall | [Mx11 refuses to start with unmigrated pre-5.12 file documents](mx11-file-orphans-block-start.md) |
| pitfall | [Mx11: Multi-dimensional arrays from WSDL can no longer be selected in Import/Export Mapping](mx11-integration-wsdl-multidim-array.md) |
| pitfall | [Mx11: Deprecated ActionListener and EventActionInfo API surface was removed](mx11-java-actionlistener-api-removed.md) |
| pitfall | [Mx11: ICore#addSessionCookies removed](mx11-java-add-session-cookies.md) |
| pitfall | [Mx11: Consumer<IMendixObject> overloads are deprecated, to be removed in Mendix 12](mx11-java-consumer-overload-deprecated.md) |
| pitfall | [Mx11: Deprecated Core.*Async methods were removed](mx11-java-core-async-methods-removed.md) |
| pitfall | [Mx11: Core.retrieveXPath Java APIs removed](mx11-java-core-retrieve-xpath.md) |
| pitfall | [Mx11: Core scheduling methods lost their generic type parameter](mx11-java-core-schedule-type-param-removed.md) |
| pitfall | [Mx11: Deprecated low-level Core SPI methods were removed](mx11-java-core-spi-methods-removed.md) |
| pitfall | [Mx11: The CoreAction class was removed](mx11-java-coreaction-removed.md) |
| pitfall | [Mx11: Development servlets now require authentication](mx11-java-dev-servlet-auth.md) |
| pitfall | [Mx11: com.mendix.modules.email.EmailModule was removed](mx11-java-email-module.md) |
| pitfall | [Mx11: Error message and exception-cause nesting depth changed](mx11-java-exception-nesting-changed.md) |
| pitfall | [Mx11: The IMxRuntime interface was removed](mx11-java-imxruntime.md) |
| pitfall | [Mx11: Core.isSubClassOf was removed](mx11-java-is-sub-class-of.md) |
| pitfall | [Mx11: Low-level m2ee runtime-extension API surface was removed](mx11-java-m2ee-extension-api-removed.md) |
| pitfall | [Mx11: MendixEnum#isValid(IContext, String) was removed](mx11-java-mendixenum-isvalid-removed.md) |
| pitfall | [Mx11: Deprecated Metrics API methods were removed](mx11-java-metrics-api-removed.md) |
| pitfall | [Mx11: Several other deprecated Java APIs were removed](mx11-java-misc-deprecated-api-removed.md) |
| pitfall | [Mx11: com.mendix.core.conf.RuntimeVersion class was removed](mx11-java-runtime-version-class-removed.md) |
| pitfall | [Mx11: Core.getRuntimeVersion no longer includes the build number](mx11-java-runtime-version-format.md) |
| pitfall | [Mx11: The Java Security Manager is deprecated and non-functional under Java 21](mx11-java-security-manager-deprecated.md) |
| pitfall | [Mx11: The tcpjson log subscriber was removed](mx11-java-tcpjson-subscriber.md) |
| pitfall | [Mx11: UserAction#context() was removed](mx11-java-useraction-context-removed.md) |
| pitfall | [Mx11: Java 21 support is deprecated, to be removed in Mendix 12](mx11-java-version-21-deprecated.md) |
| pitfall | [Mx11: Java 21 is required](mx11-java-version-21.md) |
| pitfall | [Mx11: DataSetAccess and DataSet Object parameter constraints were removed](mx11-model-dataset-constraints-removed.md) |
| pitfall | [Mx11: Entities with AutoNumber or calculated attributes can no longer be instantiated on offline navigation profiles](mx11-model-offline-autonumber-restricted.md) |
| pitfall | [Mx11: ShowHomePage microflow now enforces entity access](mx11-model-show-home-page.md) |
| pitfall | [Mx11: Comparing an association to empty or false() is now a consistency error](mx11-model-xpath-assoc-compare.md) |
| pitfall | [Mx11: Element helper methods were removed from the Model API types](mx11-modelapi-elements-helpers.md) |
| pitfall | [Mx11: Atlas 3 to Atlas 4 migration is optional but recommended](mx11-module-atlas-4.md) |
| pitfall | [Mx11: The Deep Link module is deprecated and no longer actively supported](mx11-module-deep-link-deprecated.md) |
| pitfall | [Mx11: OQL COALESCE result type and alias-dot rules changed](mx11-oql-misc-changes.md) |
| pitfall | [Mx11: SELECT * in OQL now always returns the same columns regardless of optimistic locking](mx11-oql-select-star-locking.md) |
| pitfall | [Mx11: ORDER BY in a UNION OQL query must reference aliased columns only](mx11-oql-union-order-by.md) |
| pitfall | [Mx11: OQL UPDATE with a multi-row SET expression now throws a different exception](mx11-oql-update-exception-type.md) |
| pitfall | [Mx11: Several deprecated custom runtime settings and behaviors were removed](mx11-platform-deprecated-settings-removed.md) |
| pitfall | [Mx11: Studio Pro itself now requires .NET 10](mx11-platform-dotnet-10-required.md) |
| pitfall | [Mx11: Intel-based Macs are no longer supported](mx11-platform-intel-mac.md) |
| pitfall | [Mx11: An invalid time zone setting now blocks the runtime from starting](mx11-platform-invalid-timezone-blocks-start.md) |
| pitfall | [Mx11: Hebrew and Indonesian language codes were replaced](mx11-platform-language-codes.md) |
| pitfall | [Mx11: React 19 removed findDOMNode, breaking older widget builds](mx11-react19-find-dom-node.md) |
| pitfall | [Mx11: Automatic encoding of Send REST request parameters was removed](mx11-rest-param-encoding.md) |
| pitfall | [Mx11: Published REST services now always send JSON](mx11-rest-published-json.md) |
| pitfall | [SCSS @import only warns on Mx11 (Dojo); migrate to @use later](mx11-scss-import-deprecation-non-blocking.md) |
| pitfall | [Mx11: Cookies lose the secure attribute under forwarded-proto/scheme headers](mx11-security-cookie-secure-attr.md) |
| pitfall | [Mx11: S3 client-side encryption now supports only AES](mx11-storage-s3-encryption-aes-only.md) |
| pitfall | [Mx11: S3 storage moved to AWS SDK v2 and now requires an explicit region](mx11-storage-s3-sdk-v2.md) |
| pitfall | [Mx11: String concatenation in expressions changed for empty and null values](mx11-string-concat-null.md) |
| pitfall | [Mx11: Empty values are no longer converted to empty strings in the client](mx11-string-empty-client.md) |
| pitfall | [Mx11: Curly braces in placeholder text must be escaped with an extra opening brace](mx11-string-placeholder-brace.md) |
| pitfall | [Mx11: The Task Queue System context tasks setting was removed](mx11-taskqueue-system-context.md) |
| pitfall | [Mx11: Widget uses the Dojo-era package layout](mx11-widget-dojo-package.md) |
| pitfall | [Mx11: Built-in widget is not supported in the React client](mx11-widget-react-unsupported.md) |
| pitfall | [Mx11: Apps still using the deprecated Reporting widgets will not start](mx11-widget-reporting-removed.md) |
| pitfall | [Mx7 to Mx8 breaks REST Services module use and changes transaction/error-handler behavior](mx7-to-mx8-rest-and-transaction-breaks.md) |
| pitfall | [Mx9 renders pages before nested data views load and loads them sequentially](mx9-nested-dataview-load-order.md) |
| pitfall | [SAML module encryption became per-configuration around 3.5.0](saml-encryption-per-config-since-3-5.md) |
| procedure | [Upgrading an app from Mx10 to Mx11](mx10-to-mx11-upgrade-procedure.md) |
| procedure | [Migrating custom styling from Mx7 to Mx9 via 7.23.4 and 8.18](mx7-to-mx9-styling-migration.md) |
| procedure | [Three-phase Mx8 to Mx9 upgrade through the latest Mx8 MTS](mx8-to-mx9-phased-upgrade.md) |
| procedure | [Upgrading a platform app from Mx9 to Mx10.24](mx9-to-mx10-upgrade-procedure.md) |
| procedure | [Check and clean up uniqueness violations before moving an app to Mx9](mx9-uniqueness-violation-check-and-cleanup.md) |
| procedure | [Replacing the Deeplink module with page/microflow URLs while keeping OIDC SSO](page-urls-with-oidc-replacing-deeplink.md) |
| procedure | [Rolling back an accidental model version upgrade committed to SVN](rollback-accidental-version-upgrade-svn.md) |
| procedure | [Clean userlib before and after each Marketplace module update (pre-managed-deps)](userlib-cleanup-on-module-update.md) |
| procedure | [Migrating userlib JARs to managed dependencies (vendorlib)](userlib-to-managed-dependencies.md) |
| procedure | [Removing vendorlib JARs from Git and syncing dependencies in CI](vendorlib-out-of-git-ci-sync.md) |
| procedure | [Migrating a custom pluggable widget from Webpack (tools 8.x) to Rollup](widget-webpack-to-rollup.md) |
| reference | [Mx9 -> Mx10/11: differences an old-vs-new comparison shows that are not regressions](expected-differences-old-vs-new-compare.md) |
| reference | [CE error codes seen after an Mx9 to Mx10 upgrade and their fixes](mx10-post-upgrade-ce-error-codes.md) |
| reference | [Upgrade catalog: Dojo widget to React replacement map](mx11-dojo-widget-map-catalog.md) |
| reference | [Java API rewrites needed to compile on Mx11](mx11-java-api-rewrites.md) |
| reference | [Upgrade catalog: Marketplace module advisories for Mendix 11](mx11-marketplace-module-advisories.md) |
| reference | [Measured Mx10.24 to Mx11.12 upgrade — warnings by type and how they were handled](mx11-upgrade-measured-warning-triage.md) |
