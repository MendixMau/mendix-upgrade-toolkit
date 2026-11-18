# Push Notifications Connector (Marketplace component 3003)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/3003)

| version | published | min Mendix |
|---|---|---|
| 8.0.6 | 2026-10-05 | 10.21.0 |
| 8.0.5 | 2026-08-21 | 10.21.0 |
| 8.0.4 | 2026-06-12 | 10.21.0 |
| 8.0.3 | 2026-04-17 | 10.21.0 |
| 8.0.2 | 2025-11-21 | 10.21.0 |
| 8.0.1 | 2025-07-01 | 10.21.0 |
| 8.0.0 | 2025-05-01 | 10.21.0 |
| 7.4.4 | 2026-04-17 | 9.24.0 |
| 7.4.3 | 2025-11-21 | 9.24.0 |
| 7.4.2 | 2025-04-11 | 9.24.0 |
| 7.4.1 | 2024-10-23 | 9.24.0 |
| 7.4.0 | 2024-07-26 | 9.24.0 |
| 7.3.0 | 2024-06-11 | 9.24.0 |
| 7.2.4 | 2024-05-15 | 9.18.0 |
| 7.2.3 | 2024-01-09 | 9.18.0 |
| 7.2.2 | 2023-12-20 | 9.18.0 |
| 7.2.1 | 2023-09-26 | 9.18.0 |
| 7.2.0 | 2023-09-22 | 9.18.0 |
| 7.1.3 | 2023-07-17 | 9.18.0 |
| 7.1.2 | 2023-07-04 | 9.18.0 |
| 7.1.1 | 2023-06-27 | 9.18.0 |
| 7.1.0 | 2023-01-18 | 9.18.0 |
| 7.0.0 | 2022-11-30 | 9.18.0 |
| 6.3.1 | 2023-06-27 | 9.6.0 |
| 6.3.0 | 2023-01-18 | 9.6.0 |
| 6.2.0 | 2022-06-27 | 9.0.5 |
| 6.1.2 | 2022-05-25 | 9.0.5 |
| 6.1.1 | 2022-03-03 | 9.0.5 |
| 6.1.0 | 2022-02-02 | 9.0.5 |
| 6.0.1 | 2022-01-10 | 9.0.5 |
| 6.0.0 | 2021-12-16 | 9.0.5 |
| 5.4.4 | 2025-04-11 | 8.18.0 |
| 5.4.3 | 2024-10-23 | 8.18.0 |
| 5.4.2 | 2024-05-15 | 8.18.0 |
| 5.4.1 | 2024-01-09 | 8.18.0 |
| 5.4.0 | 2022-06-27 | 8.18.0 |
| 5.3.3 | 2022-05-31 | 8.18.0 |
| 5.3.2 | 2022-01-10 | 8.18.0 |
| 5.3.1 | 2021-12-16 | 8.18.0 |
| 5.3.0 | 2021-11-22 | 8.18.0 |
| … 14 older versions | | |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 8.0.6 | improvement | Updated static images to image widgets for React client compatibility. | images |  |
| 8.0.5 | fix | Fixed issue where Push Notifications was using wrong Pushy library introduced in v8.0.4 | Pushy library |  |
| 8.0.4 | fix | Updated dependencies to fix direct APNS push notifications. netty libraries to 4.1.133.Final, pushy to 0.15.4 | io.netty:netty-codec-http2, io.netty:netty-handler-proxy, io.netty:netty-resolver-dns, com.eatthepath:pushy |  |
| 8.0.3 | improvement | Updated netty dependencies to version 4.2.12.Final | io.netty:netty-codec-http2, io.netty:netty-handler-proxy, io.netty:netty-resolver-dns |  |
| 8.0.2 | improvement | Updated netty dependencies to version 4.2.5.Final | io.netty:netty-codec-http2, io.netty:netty-handler-proxy, io.netty:netty-resolver-dns |  |
| 8.0.0 | requirement | Upgraded module to Mendix version 10.21.0 for compatibility with Mendix 11 |  |  |
| 8.0.0 | improvement | Updated Atlas Core compatibility to version 3.17.0 | Atlas Core |  |
| 8.0.0 | improvement | Updated Atlas Web Content compatibility to version 3.8.0 | Atlas Web Content |  |
| 8.0.0 | improvement | Updated Data Widgets compatibility to version 2.31.0 | Data Widgets |  |
| 8.0.0 | improvement | Updated Combo Box widget compatibility to version 2.3.0 | Combo Box widget |  |
| 7.4.4 | improvement | Updated netty dependencies from 4.2.5.Final to 4.2.12.Final | netty-buffer, netty-codec-base, netty-codec-compression, netty-codec-dns, netty-codec-http2, netty-codec-http, netty-codec-socks, netty-common, netty-handler, netty-handler-proxy, netty-resolver, netty-resolver-dns, netty-transport, netty-transport-native-unix-common |  |
| 7.4.4 | migration-step | After upgrading, remove old versions of updated libraries and their '.PushNotifications.RequiredLib' from userlib folder | netty libraries |  |
| 7.4.3 | improvement | Updated netty dependencies from 4.2.0.Final to 4.2.5.Final | netty-buffer, netty-codec-base, netty-codec-compression, netty-codec-dns, netty-codec-http2, netty-codec-http, netty-codec-socks, netty-common, netty-handler, netty-handler-proxy, netty-resolver, netty-resolver-dns, netty-transport, netty-transport-native-unix-common |  |
| 7.4.3 | migration-step | After upgrading, remove old versions of updated libraries and their '.PushNotifications.RequiredLib' from userlib folder | netty libraries |  |
| 7.4.3 | removal | Deleted netty-codec, netty-codec-marshalling, and netty-codec-protobuf 4.2.0.Final files | netty-codec-4.2.0.Final.jar, netty-codec-marshalling-4.2.0.Final.jar, netty-codec-protobuf-4.2.0.Final.jar |  |
| 7.4.2 | improvement | Updated netty dependencies to version 4.2.0.Final | netty-buffer, netty-codec, netty-codec-dns, netty-codec-http, netty-codec-http2, netty-codec-socks, netty-common, netty-handler, netty-handler-proxy, netty-resolver, netty-resolver-dns, netty-transport, netty-transport-native-unix-common |  |
| 7.4.2 | migration-step | After upgrading, remove old versions of updated libraries and their '.PushNotifications.RequiredLib' from userlib folder | netty libraries |  |
| 7.4.2 | improvement | Added new netty libraries: codec-base, codec-compression, codec-marshalling, codec-protobuf 4.2.0.Final | netty-codec-base, netty-codec-compression, netty-codec-marshalling, netty-codec-protobuf |  |
| 7.4.0 | feature | Added support for Web Push notifications for progressive web apps |  |  |
| 7.3.0 | requirement | Upgraded module to Mendix 9.24.0 |  |  |
| 7.3.0 | feature | Added support for React client introduced as public beta in Mendix 10.7.0 |  |  |
| 7.3.0 | improvement | Updated all dropdown widgets to new Combo Box widget | dropdown widgets | Combo Box widget |
| 7.3.0 | improvement | Updated Atlas Core module compatibility to v3.12.3 replacing Static image widget with Image widget | Atlas Core |  |
| 7.3.0 | improvement | Updated Data Widgets module compatibility to v2.19.1 | Data Widgets |  |
| 7.3.0 | improvement | Updated Switch widget compatibility to v4.2.1 | Switch widget |  |
| 7.3.0 | removal | Excluded snippets related to hybrid mobile as deprecated in Mendix 9 and incompatible with React client | hybrid mobile snippets |  |
| 7.2.4 | improvement | Updated netty dependencies to version 4.1.109.Final | netty-buffer, netty-codec, netty-codec-dns, netty-codec-http2, netty-codec-http, netty-codec-socks, netty-common, netty-handler, netty-handler-proxy, netty-resolver, netty-resolver-dns, netty-transport, netty-transport-native-unix-common |  |
| 7.2.4 | migration-step | After upgrading, remove old versions of updated libraries and their '.PushNotifications.RequiredLib' from userlib folder | netty libraries |  |
| 7.2.3 | migration-step | Migrated from legacy FCM APIs to HTTP v1 for hybrid device notifications. Update before 2024-06-20 | FCM APIs |  |
| 7.2.2 | improvement | Updated netty dependencies to 4.1.101.Final and slf4j-api to 2.0.7 | netty-buffer, netty-codec, netty-codec-dns, netty-codec-http2, netty-codec-http, netty-codec-socks, netty-common, netty-handler, netty-handler-proxy, netty-resolver, netty-resolver-dns, netty-transport, netty-transport-native-unix-common, slf4j-api |  |
| 7.2.2 | migration-step | After upgrading, remove old versions of updated libraries and their '.PushNotifications.RequiredLib' from userlib folder | netty libraries |  |
| 7.2.0 | migration-step | Included migration file for Java dependencies for Studio Pro 10 compatibility | Java dependencies |  |
| 7.1.3 | improvement | Updated netty dependencies to version 4.1.94.Final | netty-buffer, netty-codec, netty-codec-dns, netty-codec-http2, netty-codec-http, netty-codec-socks, netty-common, netty-handler, netty-handler-proxy, netty-resolver, netty-resolver-dns, netty-transport, netty-transport-native-unix-common |  |
| 7.1.3 | migration-step | After upgrading, remove old versions of updated libraries and their '.PushNotifications.RequiredLib' from userlib folder | netty libraries |  |
| 7.1.2 | improvement | Updated dependencies: checker-qual to 3.33.0, j2objc-annotations to 2.8, error_prone_annotations to 2.18.0 | checker-qual, j2objc-annotations, error_prone_annotations |  |
| 7.1.2 | removal | Removed checker-compat-qual-2.5.5 | checker-compat-qual-2.5.5 |  |
| 7.1.2 | migration-step | After upgrading, remove old versions of updated libraries and their '.PushNotifications.RequiredLib' from userlib folder | libraries |  |
| 7.1.1 | improvement | Updated guava library to 32.0.1-android, remove old version 31.0.1-android from userlib | guava |  |
| 7.1.0 | improvement | Updated all netty libraries from version 4.1.78 to 4.1.86, delete older versions with '.PushNotifications.RequiredLib' | netty libraries |  |
| 7.1.0 | improvement | Added index on DeviceID attribute in Device entity | Device entity |  |
| 7.1.0 | improvement | Updated Pop-up Menu widget compatibility to v3.3.0 | Pop-up Menu widget |  |
| 7.1.0 | improvement | Updated Data Widgets compatibility to v2.5.9 | Data Widgets |  |
| 7.0.0 | requirement | Updated module to Mendix 9.18.0 |  |  |
| 7.0.0 | improvement | Switched to task queue implementation for sending notifications in background |  |  |
| 7.0.0 | fix | Fixed issue where notifications were sent multiple times in multi-instance deployment scenario |  |  |
| 6.3.1 | improvement | Updated guava library to 32.0.1-android, remove old version 31.0.1-android from userlib | guava |  |
| 6.3.0 | improvement | Updated all netty libraries from version 4.1.78 to 4.1.86, delete older versions with '.PushNotifications.RequiredLib' | netty libraries |  |
| 6.3.0 | improvement | Added index on DeviceID attribute in Device entity | Device entity |  |
| 6.3.0 | improvement | Updated Pop-up Menu widget compatibility to v3.3.0 | Pop-up Menu widget |  |
| 6.3.0 | improvement | Updated Data Widgets compatibility to v2.5.9 | Data Widgets |  |
| 6.2.0 | breaking | Removed all write access to Device entity for User/Anonymous roles (restricted to owner only). | Device |  |
| 6.2.0 | requirement | Updated dependencies: auto-value-annotations 1.8.2→1.9, commons-codec 1.13→1.15, google-auth-library-credentials 1.4.0→1.7.0, google-http-client 1.41.0→1.41.8, gson 2.8.9→2.9.0, netty 4.1.74→4.1.78, opencensus-api 0.28.0→0.31.0, pushy 0.13.9→0.13.10, slf4j-api 1.7.28→1.7.36, and others. | auto-value-annotations, commons-codec, google-auth-library-credentials, google-auth-library-oauth2-http, google-http-client, google-http-client-gson, gson, netty-buffer, netty-codec, netty-codec-dns, netty-codec-http, netty-codec-http2, netty-codec-socks, netty-common, netty-handler, netty-handler-proxy, netty-resolver, netty-resolver-dns, netty-transport, opencensus-api, opencensus-contrib-http-util, pushy, slf4j-api |  |
| 6.2.0 | migration-step | Review userlib folder after updating due to dependency changes: removed netty-tcnative-classes-2.0.48.Final.jar, added netty-transport-native-unix-common-4.1.78.Final.jar. | userlib |  |
| 6.1.2 | requirement | Updated dependencies: deleted 5 libraries, added checker-qual-3.12.0, guava-31.0.1-android, netty-tcnative-classes-2.0.48.Final. | animal-sniffer-annotations, guava, jackson-core, netty-all, netty-tcnative, checker-qual, netty-tcnative-classes |  |
| 6.1.2 | migration-step | Review userlib folder after updating due to dependency changes. | userlib |  |
| 6.1.1 | requirement | Updated all netty libraries to 4.1.74.Final. Delete netty libraries marked with .PushNotifications.RequiredLib below 4.1.74.Final from userlib. | netty |  |
| 6.1.1 | migration-step | Delete old netty libraries from userlib marked with .PushNotifications.RequiredLib below 4.1.74.Final. | userlib |  |
| 6.1.0 | breaking | Switched from deprecated google-oauth-client to google-auth-library. | google-oauth-client, google-auth-library | google-auth-library |
| 6.1.0 | requirement | Updated dependencies: added auto-value-annotations-1.8.2, google-auth-library-credentials-1.4.0, google-auth-library-oauth2-http-1.4.0, google-http-client-gson-1.41.0; updated multiple others; removed google-api-client, google-http-client-jackson2, google-oauth-client. | auto-value-annotations, google-auth-library-credentials, google-auth-library-oauth2-http, google-http-client-gson, error_prone_annotations, google-http-client, grpc-context, gson, httpclient, httpcore, opencensus-api, opencensus-contrib-http-util |  |
| 6.1.0 | migration-step | Review userlib folder after updating due to dependency changes. | userlib |  |
| 6.0.0 | requirement | Upgraded module to Mendix 9 and Atlas 3. |  |  |
| 5.4.4 | requirement | Updated netty dependencies to version 4.2.0.Final. Added 4 new codecs, updated 15 existing libraries. | netty-buffer, netty-codec, netty-codec-dns, netty-codec-http, netty-codec-http2, netty-codec-socks, netty-common, netty-handler, netty-handler-proxy, netty-resolver, netty-resolver-dns, netty-transport, netty-transport-native-unix-common, netty-codec-base, netty-codec-compression, netty-codec-marshalling, netty-codec-protobuf |  |
| 5.4.4 | migration-step | Remove old versions of updated libraries and corresponding .PushNotifications.RequiredLib from userlib folder. | userlib |  |
| 5.4.2 | requirement | Updated netty dependencies to version 4.1.109.Final. | netty-buffer, netty-codec, netty-codec-dns, netty-codec-http, netty-codec-http2, netty-codec-socks, netty-common, netty-handler, netty-handler-proxy, netty-resolver, netty-resolver-dns, netty-transport, netty-transport-native-unix-common |  |
| 5.4.2 | migration-step | Remove old versions of updated libraries and corresponding .PushNotifications.RequiredLib from userlib folder. | userlib |  |
| 5.4.1 | breaking | Migrated from legacy FCM APIs to HTTP v1 for hybrid devices. Update before 2024-06-20. |  |  |
| 5.4.1 | breaking | Switched from deprecated google-oauth-client to google-auth-library. | google-oauth-client, google-auth-library | google-auth-library |
| 5.4.1 | requirement | Updated dependencies: removed 6 libraries, added 6, updated 22 others including netty to 4.1.101.Final, slf4j-api to 2.0.7. | animal-sniffer-annotations, checker-compat-qual, google-api-client, google-http-client-jackson2, google-oauth-client, netty-all, auto-value-annotations, checker-qual, google-auth-library-credentials, google-auth-library-oauth2-http, google-http-client-gson, netty-transport-native-unix-common, commons-codec, error_prone_annotations, google-http-client, grpc-context, gson, guava, httpclient, httpcore, j2objc-annotations, netty-buffer, netty-codec, netty-codec-dns, netty-codec-http, netty-codec-http2, netty-codec-socks, netty-common, netty-handler, netty-handler-proxy, netty-resolver, netty-resolver-dns, netty-transport, opencensus-api, opencensus-contrib-http-util, pushy, slf4j-api |  |
| 5.4.1 | migration-step | Remove old versions of updated libraries and corresponding .PushNotifications.RequiredLib from userlib folder. | userlib |  |
| 5.4.0 | breaking | Removed all owner write access to device entity for User/Anonymous roles (restricted to owner only). | Device |  |
| 5.2.0 | requirement | Upgrade to Mendix 8.18.0 to ensure compatibility with Mendix 9. |  |  |
| 5.0.0 | requirement | Requires Studio Pro 8.0.0 for native mobile push notification support. |  |  |
| 4.0.4 | improvement | Notifications now play default sound when application is in background. |  |  |
| 4.0.0 | requirement | Requires Modeler Version 7.23.4 or higher to be used in 8.00. |  |  |
| 4.0.0 | breaking | Layouts now based on AtlasUI instead of NavigationsLayout Module. | Layouts, AtlasUI, NavigationsLayout | AtlasUI |
| 4.0.0 | breaking | Removed default actions for snippets to prevent errors on first imports. | snippets |  |
| 4.0.0 | improvement | Updated all dependent modules to latest versions. |  |  |
| 4.0.0 | fix | Fixed missing SLF4j library when using APNS. | SLF4j, APNS |  |
