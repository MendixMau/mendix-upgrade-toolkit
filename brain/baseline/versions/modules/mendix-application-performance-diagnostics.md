# Mendix Application Performance Diagnostics (Marketplace component 6127)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Module, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/6127)

| version | published | min Mendix |
|---|---|---|
| 3.77.92 | 2026-01-13 | 11.0.0 |
| 3.76.92 | 2026-01-13 | 10.0.0 |
| 3.75.92 | 2026-01-13 | 9.0.5 |
| 3.74.91 | 2025-05-14 | 10.0.0 |
| 3.73.91 | 2025-05-14 | 9.0.5 |
| 3.72.91 | 2025-05-14 | 8.0.0 |
| 3.71.90 | 2025-02-07 | 10.0.0 |
| 3.70.90 | 2025-02-07 | 9.0.5 |
| 3.69.90 | 2025-02-07 | 8.0.0 |
| 3.68.89 | 2024-10-02 | 10.0.0 |
| 3.67.89 | 2024-10-02 | 9.0.5 |
| 3.66.89 | 2024-10-02 | 8.0.0 |
| 3.65.88 | 2024-02-08 | ? |
| 3.64.88 | 2024-02-08 | 9.0.5 |
| 3.62.88 | 2024-02-08 | 8.0.0 |
| 3.61.87 | 2024-01-10 | 10.0.0 |
| 3.60.87 | 2024-01-10 | 9.0.5 |
| 3.59.87 | 2024-01-10 | 8.0.0 |
| 3.58.86 | 2023-07-27 | 10.0.0 |
| 3.57.86 | 2023-07-27 | 9.0.5 |
| 3.56.86 | 2023-07-27 | 8.0.0 |
| 3.45.82 | 2022-03-16 | 9.0.5 |
| 3.44.82 | 2022-03-16 | 8.0.0 |
| 3.43.82 | 2022-03-16 | 7.0.2 |
| 3.41.81 | 2022-02-23 | 9.0.5 |
| 3.40.81 | 2022-02-23 | 8.0.0 |
| 3.39.81 | 2022-02-23 | 7.0.2 |
| 3.37.80 | 2022-02-22 | 9.0.5 |
| 3.36.80 | 2022-02-22 | 8.0.0 |
| 3.33.80 | 2022-02-22 | 7.0.2 |
| 3.33.79 | 2021-10-25 | 9.0.5 |
| 3.32.79 | 2021-10-25 | 8.0.0 |
| 3.31.79 | 2021-10-25 | 7.0.2 |
| 3.25.77 | 2021-10-06 | 9.0.5 |
| 3.24.77 | 2021-10-06 | 8.0.0 |
| 3.23.77 | 2021-10-06 | 7.0.2 |
| 3.0.54 | 2023-02-26 | 9.0.5 |
| 3.0.53 | 2023-02-26 | 8.0.0 |
| 3.0.52 | 2023-02-26 | 7.0.2 |
| 3.0.51 | 2022-09-13 | 9.0.5 |
| … 33 older versions | | |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 3.77.92 | fix | Mendix 11.6.0 compatibility |  |  |
| 3.76.92 | fix | Mendix 11.6.0 compatibility |  |  |
| 3.75.92 | fix | Mendix 11.6.0 compatibility |  |  |
| 3.71.90 | fix | Mx 10.18 compatibility |  |  |
| 3.71.90 | deprecation | Database profiler is deprecated in Mx 10.18 and is now disabled in the APD Agent. Use AdvancedSettings 'useprofiler=true' to re-enable. | Database profiler |  |
| 3.71.90 | removal | Browser agent has been discontinued. Please remove the widget 'Mansystems.APDBrowserAgent.mpk' from the project 'widgets' folder. | Browser agent |  |
| 3.70.90 | removal | Browser agent has been discontinued. Please remove the widget 'Mansystems.APDBrowserAgent.mpk' from the project 'widgets' folder. | Browser agent |  |
| 3.69.90 | removal | Browser agent has been discontinued. Please remove the widget 'Mansystems.APDBrowserAgent.mpk' from the project 'widgets' folder. | Browser agent |  |
| 3.68.89 | improvement | Agent now logs running microflows, when memory protection lock is initially set. |  |  |
| 3.67.89 | improvement | Agent now logs running microflows, when memory protection lock is initially set. |  |  |
| 3.66.89 | improvement | Agent now logs running microflows, when memory protection lock is initially set. |  |  |
| 3.61.87 | improvement | Improved capturing and linking of submicrolfows, when using the same context. |  |  |
| 3.61.87 | improvement | Client API calls for microflow now also capture and specify the time needed before and after microflow execution. |  |  |
| 3.61.87 | fix | Added Mx 10.6 compatibility |  |  |
| 3.60.87 | improvement | Improved capturing and linking of submicrolfows, when using the same context. |  |  |
| 3.60.87 | improvement | Client API calls for microflow now also capture and specify the time needed before and after microflow execution. |  |  |
| 3.60.87 | fix | Added Mx 10.6 compatibility |  |  |
| 3.59.87 | improvement | Improved capturing and linking of submicrolfows, when using the same context. |  |  |
| 3.59.87 | improvement | Client API calls for microflow now also capture and specify the time needed before and after microflow execution. |  |  |
| 3.59.87 | fix | Added Mx 10.6 compatibility |  |  |
| 3.58.86 | security | Updated dependencies for security fixes |  |  |
| 3.58.86 | fix | Added Mx 9.24 compatibility |  |  |
| 3.57.86 | security | Updated dependencies for security fixes |  |  |
| 3.57.86 | fix | Added Mx 9.24 compatibility |  |  |
| 3.56.86 | security | Updated dependencies for security fixes |  |  |
| 3.56.86 | fix | Added Mx 9.24 compatibility |  |  |
| 3.37.80 | breaking | Renamed snippet to be inline with ACR naming convention |  |  |
| 3.36.80 | breaking | Renamed snippet to be inline with ACR naming convention |  |  |
| 3.33.80 | migration-step | Renamed snippet to align with ACR naming convention. | snippet |  |
| 3.31.79 | fix | Fixed deprecation warnings due to usage of logger object instead of mx.logger in Mx9. | Mx 9 agent, logger, mx.logger |  |
| 3.23.77 | improvement | Separate channel for manual statistics from hourly statistics prevents one blocking process queue. | manual statistics, hourly statistics |  |
| 3.0.49 | fix | Log node DataStorage_QueryPlan excluded by default for trap collection to prevent 'explain analyze' queries. | Log node DataStorage_QueryPlan |  |
| 3.0.49 | fix | Fix loop iterations not linked to microflow due to missing type for Loop actions in Mx9. | APD Agent, Loop actions, Mendix 9.17.0 |  |
| 3.0.48 | feature | Added option to use a microflow to return the API key instead of a constant. |  |  |
| 3.0.47 | feature | Added option to use a microflow to return the API key instead of a constant. |  |  |
| 3.0.20 | fix | A VerifyError was thrown when using the APD agent and Datadog agent together. | Datadog agent |  |
| 3.0.19 | fix | Fixed VerifyError thrown when using APD agent and Datadog agent together. | APD agent, Datadog agent |  |
| 3.0.17 | security | Admin features to execute queries and create heap dumps disabled by default. |  |  |
| 3.0.17 | breaking | Load test recording default disabled. |  |  |
| 3.0.16 | requirement | Admin features to execute queries and create heap dumps disabled by default. | Admin features |  |
| 3.0.16 | requirement | Load test recording default disabled. | Load test recording |  |
| 3.0.16 | fix | Log levels set from Mx Modeler/Studio/Cloud no longer affect APD agent log level. | log levels, APD agent |  |
| 3.0.2 | breaking | Renamed components to match the APD name. |  |  |
| 3.0.2 | breaking | Advanced settings should now be lowercase. This mainly affects 'proxy' settings, as these were camel case. |  |  |
| 3.0.2 | breaking | Advanced setting behavior changed for 'Memory Protection Time' to no longer stop the agent after the defined time. Instead it will repeat the sleep. |  |  |
| 3.0.1 | migration-step | Renamed components to match APD name. | component names |  |
| 3.0.1 | breaking | Advanced settings should now be lowercase; affects camel case proxy settings. | advanced settings, proxy |  |
| 3.0.1 | breaking | Memory Protection Time behavior changed: no longer stops agent; repeats sleep until memory reduced. | Memory Protection Time |  |
| 2.0.21 | improvement | Added check on startup to detect if proper agent jar file has been loaded. | agent jar file |  |
| 2.0.19 | breaking | Changed behavior for advanced setting 'memoryagentstoplimit'; stops processing log messages/recording for a set timeframe instead of instantly. |  |  |
| 2.0.18 | breaking | Advanced setting memoryagentstoplimit behavior changed: agent stops processing for set timeframe. | memoryagentstoplimit |  |
| 2.0.16 | breaking | Removed CORS headers from 'apm'-request handler |  |  |
| 2.0.15 | removal | Removed CORS headers from 'apm' request handler. | CORS headers, apm request handler |  |
| 2.0.13 | improvement | Merged statistics and recording collecting, reducing overhead and resource usage. | Browser agent, Runtime agent |  |
| 2.0.13 | improvement | Improved support for Mendix 7.6 and newer. | Browser agent |  |
| 2.0.13 | migration-step | JSON Logging set behind advanced setting. | JSON Logging, Runtime agent |  |
| 2.0.12 | improvement | Merged statistics and recording collecting, reducing overhead and resource usage. | Browser agent, Runtime agent |  |
| 2.0.12 | improvement | Improved support for Mendix 7.6 and newer. | Browser agent |  |
| 2.0.12 | migration-step | JSON Logging set behind advanced setting. | JSON Logging |  |
| 2.0.10-beta | migration-step | JSON Logging set behind advanced setting. | JSON Logging |  |
| 2.0.9 | migration-step | JSON Logging set behind advanced setting. | JSON Logging |  |
| 2.0.7 | improvement | Memory improvement: default 80% heap clear buffers, 90% stops agent; configurable via advanced settings. | memory |  |
| 2.0.7 | improvement | Performance improvement: max depth for microflow statistics with manual created loop reduced. | microflow statistics |  |
| 2.0.6 | improvement | Memory improvement: default 80% heap clear buffers, 90% stops agent; configurable via advanced settings. | memory |  |
| 2.0.6 | improvement | Performance improvement: max depth for microflow statistics with manual created loop reduced. | microflow statistics |  |
| 2.0.5 | known-issue | Buffer limit between Mendix log thread and APM threads; fast delivery causes message drops. | buffer, APM threads |  |
| 2.0.5 | feature | Advanced settings added for profiler, recorder, maxtrap, maxstatistics to tune agent. | profiler, recorder, maxtrap, maxstatistics |  |
| 2.0.5 | requirement | Hard-coded maximum for messages accepted by APM Agent/manager from Mendix log thread. | message, stack trace |  |
| 2.0.5 | improvement | Hourly purge of performance tool memory structures during statistics snapshot to prevent OOM. | memory |  |
| 2.0.5 | improvement | Extra clearing of memory structures to faster release memory and ease garbage collection. | memory |  |
| 2.0.3 | improvement | When connection lost with APM Manager, agent delays subsequent calls; max delay 5 min. | APM Manager connection |  |
| 2.0.3 | improvement | Performance optimizations. |  |  |
| 2.0.1 | improvement | Reduced logging from Agent; full JSON messages logging on error default disabled. | Agent logging |  |
| 2.0.1 | improvement | When Browser Agent disabled per APM Manager config, agent no longer logs error. | Browser Agent |  |
| 1.12.0 | improvement | Protection in logtool to configure 'Max messages to store' default 100.000 records. | logtool, Max messages |  |
| 1.12.0 | improvement | Fallback level protection sets logging to INFO when logtool notices excessive data processing. | logtool, Fallback level |  |
| 1.12.0 | fix | Fixed behavior preventing application from running out of heap memory on excessive INFO logging. | heap memory |  |
| 1.12 | fix | Upgrade function on low-memory environments now commits statistics, measurements, and traps data in chunks to prevent out of memory. |  |  |
| 1.12 | removal | Removed fixed duration function from trap and statistics tool as unused and not fitting module scope. | fixed duration function |  |
| 1.12 | improvement | Default trap tool buffer setting in production now stops tool to prevent continuous load from high error volumes. | trap tool buffer default settings |  |
| 1.12 | fix | Fixed incorrect default JDBC settings for MSSQL after installation. | JDBC settings for MSSQL |  |
| 1.12 | fix | Renamed Java action parameters to prevent errors from Mendix generating different names across versions. | Java action parameters |  |
| 1.10.1 | requirement | First version fully available for Mendix 7 with separate package; Mendix 6 package available on All Versions tab. |  |  |
