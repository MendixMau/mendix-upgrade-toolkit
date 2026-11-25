# Mendix Service Console (Marketplace component 223425)

Source: marketplace-api.mendix.com per-version release notes, layer baseline. Versions newest first; 'min Mendix' is the lowest Studio Pro version the module version supports.

Service, Mendix, Platform, [marketplace](https://marketplace.mendix.com/link/component/223425)

| version | published | min Mendix |
|---|---|---|
| 4.8.3 | 2026-04-14 | 8.18.34 |
| 4.8.2 | 2025-11-28 | 8.18.34 |
| 4.8.1 | 2025-03-20 | 8.18.34 |
| 4.8.0 | 2024-06-27 | 7.0.2 |
| 4.7.4 | 2024-03-01 | 7.0.2 |
| 4.7.3 | 2024-03-01 | 7.0.2 |
| 4.7.2 | 2024-03-01 | 7.0.2 |
| 4.7.1 | 2024-03-01 | 7.0.2 |
| 4.7.0 | 2024-03-01 | 7.0.2 |
| 4.6.1 | 2024-03-01 | 7.0.2 |
| 4.6.0 | 2024-03-01 | 7.0.2 |
| 4.5.1 | 2024-03-01 | 7.0.2 |
| 4.5.0 | 2024-03-01 | 7.0.2 |
| 4.4.0 | 2024-03-01 | 7.0.2 |
| 4.3.0 | 2024-03-01 | 7.0.2 |
| 4.2.1 | 2024-03-01 | 7.0.2 |
| 4.2.0 | 2024-03-01 | 7.0.2 |
| 4.1.1 | 2024-03-01 | 7.0.2 |
| 4.1.0 | 2024-03-01 | 7.0.2 |
| 4.0.0 | 2024-03-01 | 7.0.2 |
| 3.0.0 | 2024-03-01 | 7.0.2 |
| 2.2.0 | 2024-03-01 | 7.0.2 |
| 2.1.1 | 2024-03-01 | 7.0.2 |
| 2.1.0 | 2024-03-01 | 7.0.2 |
| 2.0.0 | 2024-03-01 | 7.0.2 |
| 1.0.7 | 2024-03-01 | 7.0.2 |

| version | type | change | affected | replaced by |
|---|---|---|---|---|
| 4.8.2 | fix | Fixed issue that updating an app via Update-MxApp cmdlet was slower than via Service Console UI. (Ticket 250362) | Update-MxApp |  |
| 4.8.1 | removal | Removed 'Import old app...' button from Service Settings window for importing apps configured with Mendix Service Console 3.0 and earlier. | Import old app button |  |
| 4.8.1 | breaking | Replaced 'DotNetZip' library by official .NET functionality as it isn't maintained and has vulnerability. | DotNetZip |  |
| 4.8.0 | requirement | Now require at least Microsoft .NET Framework version 4.7.2 instead of 4.6.2 to fix 'netstandard' assembly loading error. | Microsoft .NET Framework |  |
| 4.8.0 | breaking | Installer file name now contains underscores instead of spaces due to Marketplace restrictions. |  |  |
| 4.8.0 | fix | Fixed problem that error occurs when opening window to set levels for log file. Service must be reinstalled. (Ticket 219042) |  |  |
| 4.8.0 | improvement | Updated YamlDotNet library from version 15.1.1 to 15.3.0. | YamlDotNet |  |
| 4.7.4 | improvement | Updated Newtonsoft Json.NET library from version 13.0.2 to 13.0.3. | Newtonsoft Json.NET |  |
| 4.7.4 | improvement | Updated YamlDotNet library from version 12.3.1 to 15.1.1. | YamlDotNet |  |
| 4.7.3 | breaking | Changed default installation directory to 64-bit program files (C:\Program Files) instead of 32-bit directory. | installation directory |  |
| 4.7.1 | improvement | Replaced modified YAML parser YamlSerializer 0.9.0.2 with YamlDotNet 12.3.1. | YamlSerializer, YamlDotNet | YamlDotNet |
| 4.7.1 | improvement | Updated Newtonsoft Json.NET library from version 13.0.1 to 13.0.2. | Newtonsoft Json.NET |  |
| 4.7.0 | requirement | Now requires Microsoft .NET Framework version 4.6.2 instead of 4.5.2. | Microsoft .NET Framework |  |
| 4.7.0 | removal | Removed license ID check in Service Console; this check is done by server. | license ID check |  |
| 4.7.0 | improvement | Updated DotNetZip library from version 1.13.3 to 1.16.0. | DotNetZip |  |
| 4.7.0 | improvement | Updated Newtonsoft Json.NET library from version 12.0.2 to 13.0.1. | Newtonsoft Json.NET |  |
| 4.7.0 | improvement | Updated Tulpep.ActiveDirectoryObjectPicker library from version 2.3.133 to 3.0.11. | Tulpep.ActiveDirectoryObjectPicker |  |
| 4.7.0 | improvement | Replaced old Ookii.Dialogs source code with Ookii.Dialogs.Wpf 5.0.1 library. | Ookii.Dialogs | Ookii.Dialogs.Wpf |
| 4.6.1 | breaking | Update-MxApp cmdlet no longer applies file access rights automatically. Use checkbox on Update App form instead. | Update-MxApp cmdlet |  |
| 4.6.0 | feature | Added support for Studio Pro 8. |  |  |
| 4.6.0 | improvement | Updated Newtonsoft Json.NET library from 5.0.3 to 12.0.2. | Newtonsoft Json.NET |  |
| 4.6.0 | improvement | Updated DotNetZip library from version 1.11.0 to 1.13.3. | DotNetZip |  |
| 4.6.0 | improvement | Replaced old Active Directory Common Dialogs library with Tulpep.ActiveDirectoryObjectPicker 2.3.133. | Tulpep.ActiveDirectoryObjectPicker |  |
| 4.6.0 | known-issue | Oracle Java 8 selected by default for Mendix 8 apps. Select JRE/JDK 11 from Oracle or OpenJDK. Fixed in 4.6.1. |  |  |
| 4.5.1 | requirement | Upgraded target Microsoft .NET Framework version from 4.5 to 4.5.2. |  |  |
| 4.5.1 | improvement | Updated DotNetZip library from version 1.10.1 to 1.11.0. | DotNetZip |  |
| 4.5.1 | removal | Removed dependency on Microsoft.VisualBasic.PowerPacks library. | Microsoft.VisualBasic.PowerPacks |  |
| 4.5.0 | feature | Added support for Mendix 7. |  |  |
| 4.4.0 | breaking | Old app no longer copied to backup file when updated with deployment archive; checkbox enables backup. |  |  |
| 4.4.0 | feature | Added DB2 and MariaDB as database types, useful when supported by app server version. |  |  |
| 4.4.0 | improvement | Updated DotNetZip library from version 1.9.1.8 to 1.10.1. | DotNetZip |  |
| 4.3.0 | feature | Added support for Mendix 6.3. Service must be reinstalled if app upgraded from earlier version. |  |  |
| 4.3.0 | requirement | .NET Framework 4.5 now required. Dropped support for Windows Server 2003/2003 R2/XP. |  |  |
| 4.2.1 | fix | Prevented shared runtime mxclientsystem folder from being emptied when app removed. |  |  |
| 4.2.1 | feature | Added MySQL as new database type, supported since Mendix 5.12. |  |  |
| 4.2.0 Beta 1 | removal | Disabled possibility to set environment to deprecated 'Acceptance' runtime configuration mode for Mendix 5+ apps. |  |  |
| 4.2.0 | migration-step | All service user passwords and database passwords will be encrypted in settings files after opening Mendix Service Console for first time. |  |  |
| 4.2.0 | breaking | Service must be reinstalled with this version for Start service button to handle database synchronizations. |  |  |
| 4.2.0 | security | Deployment packages and server distribution files now checked on directory traversal attacks. |  |  |
| 4.0.0 | feature | Mendix Service Console 4 manages all Mendix 3 and 4 apps in one application with unified left bar. |  |  |
| 4.0.0 | requirement | Execute new installer to install Mendix Service Console; do not use old ZIP extraction locations. |  |  |
| 4.0.0 | migration-step | Import old apps one by one; all files remain in old locations, settings saved to new location. |  |  |
| 4.0.0 | migration-step | Must reinstall service after confirming app runs successfully with normal start. |  |  |
| 4.0.0 | migration-step | Remove old Mendix Service Console after service reinstall succeeds. | old Mendix Service Console |  |
| 4.0.0 | breaking | Each app now has its own license, even under same user account; old imports limited to first per user. |  |  |
| 4.0.0 | feature | Added possibility to manage all Mendix 3 and 4 apps in one Service Console instance. |  |  |
| 4.0.0 | feature | Ticket 9960, 11133: Each app now has its own license on one machine. |  |  |
| 4.0.0 | breaking | Symbolic link to runtime's mxclientsystem folder always created/updated; checkbox removed. | mxclientsystem |  |
| 4.0.0 | migration-step | Moved settings to Advanced Settings form via Configuration, Advanced. | project path, log path, backup path, custom Mendix settings, Jetty settings |  |
| 4.0.0 | breaking | Two Jetty options configurable by textboxes instead of custom key-value list. | Jetty options |  |
| 4.0.0 | breaking | Changed new default M2EE admin server passwords to 32 character length. | M2EE admin server passwords |  |
| 4.0.0 | breaking | Changed database type choice text 'Oracle 10.2 and later' to 'Oracle 11.2 and later'. | Oracle |  |
| 4.0.0 | breaking | Set SQL Server as default database type. |  |  |
| 3.0.0 | improvement | Improved support for Mendix 4. | Mendix 4 |  |
| 2.2.0 | requirement | Service cannot be uninstalled when service is running. | service |  |
| 2.1.0 | requirement | UAC administrator level now required to prevent UAC requests on service installation/uninstallation. |  |  |
| 2.1.0 | removal | Removed Informix database type as it is no longer supported by Mendix. | Informix database type |  |
| 2.1.0 | breaking | Removed Stop button. Start button changes to Stop after starting the project. | Stop button |  |
| 2.1.0 | migration-step | Moved Service panel content, Project path, and Mendix path to Management panel. | Service panel, Project path, Mendix path |  |
| 2.1.0 | requirement | Application always started under specific service user account; mandatory before project can run. | service user account |  |
| 2.1.0 | breaking | Removed setting for user account type; system accounts like Local System no longer supported. | user account type, system accounts |  |
| 2.1.0 | breaking | Default folder of project path changed from 'Application' to 'Project'. | project path |  |
| 2.1.0 | breaking | Changed PostgreSQL database type option text from '8.2 and later' to '8.3 and later'. | PostgreSQL |  |
