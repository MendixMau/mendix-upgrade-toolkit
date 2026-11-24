---
title: SQL Server connection fails with PKIX error after the JDBC driver upgrade
topic: upgrade
domain: [devops-cloud, integration]
kind: pitfall
applies_to: mendix-general
versions: "Mx8 -> 9.24.25+ and Mx10 (newer MS SQL JDBC driver)"
keywords: ["PKIX path building failed", "SQL Server connection fails", "encrypt false trustServerCertificate", "SQLState 08S01", "MS SQL JDBC driver upgrade", "TLS handshake certificate", "hostNameInCertificate", "DatabaseUseSsl", "encrypt connection string", "certificate not trusted"]
layer: field
sources:
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed
---
**Symptom**
- The app retries the DB connection and fails with SQLState 08S01.
- The message says `"encrypt" property is set to "false" and "trustServerCertificate" … PKIX path building failed`.

**Root cause**
- The upgraded driver attempts a TLS handshake whenever the SQL Server supports SSL and presents a certificate.
- The runtime's "encryption off" default only works when the server has no SSL certificate.
- The certificate was not issued by a trusted authority.

**Fix**
- If SSL is required:
  - import each SQL Server certificate into the trust store (in this case, the Private Cloud operator's);
  - use FQDNs in the DB plan.
- That failed in prod behind an HA pair, because the hostname did not match the certificate. Add a wildcard domain via `hostNameInCertificate` in the connection string.
- If SSL is not required, turn it off. This avoids recurring certificate-expiry maintenance.

**Status**
- Confirmed in the field. The team chose "SSL off"; the `hostNameInCertificate` option is documented for later use.

**Release notes**
- 9.24.25: MS SQL JDBC 12.6.3 (https://docs.mendix.com/releasenotes/studio-pro/9.24/#92425)
- 10.0.0: JDBC 12.2.0 uses TLS by default; `DatabaseUseSsl=false` / `encrypt=false` turns it off (https://docs.mendix.com/releasenotes/studio-pro/10.0/#1000)
