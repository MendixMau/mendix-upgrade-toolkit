---
title: Docker Buildpack upgrade changes the mendix user UID and breaks NFS permissions
topic: upgrade
domain: [devops-cloud]
kind: pitfall
applies_to: mendix-general
versions: "docker-mendix-buildpack < 2.4.0 -> 2.4.0+ (options tested against 5.0.4 / CF buildpack 5.0.15)"
keywords: ["Docker Buildpack upgrade", "mendix user UID change", "NFS permissions broken", "UID 1001", "UID 999", "useradd -r", "USER_UID build arg", "fsGroupChangePolicy", "NFS ID mapper", "Dockerfile.rootfs.ubi8", "buildpack 2.4.0", "rootfs image"]
layer: field
sources:
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed
---
**Symptom**
- After upgrading the buildpack from 2.x to 5.x, the container loses access to mounted NFS shares.

**Root cause**
- Before 2.4.0 the Dockerfile created the user with `useradd -r`, so the OS assigned a UID dynamically. In the customer's image that was 999.
- That dynamic UID was then hard-coded in the NFS share authorization. The source calls this an anti-pattern.
- From 2.4.0 the image runs as static `USER 1001`: reproducible, in the regular user range, non-root.

**Fix** (pick one)
- A. Move to Mendix for Private Cloud (supported by Mendix).
- B. Align NFS with UID 1001:
  - Support: fix permissions with a root init-container or `fsGroupChangePolicy`, on the `latest` branch.
  - Or remap UID/GID with the NFS ID mapper, then change the owner of all files on the share.
- C. Force UID 999:
  - Add `ARG USER_UID=999` / `ENV USER_UID=${USER_UID}` to `Dockerfile.rootfs.ubi8`, `Dockerfile.rootfs.bionic` and the app `Dockerfile`.
  - Use `${USER_UID}` in the `chown` lines, `/etc/passwd` entry and `USER`.
  - Build the rootfs images (app and builder) before building the app image.
- For B and C, also follow "Upgrading from Docker Mendix Buildpack v4". There was never a v4; it went v3 → v5.

**Status**
- Seen at one customer.
- Option C was tried only in a development environment, not for production. No support or guarantee.
- The Docker Buildpack is not supported by Mendix; it is used as-is.
