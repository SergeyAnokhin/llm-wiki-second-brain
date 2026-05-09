---
tags: [synology, cloudsync, package, cloud-backup, entity]
sources: [terminal 1.md, terminal 2.md]
created: 2026-05-09
updated: 2026-05-09
---

# CloudSync

CloudSync (v2.7.0) — a Synology [[DSM]] package for syncing files between the NAS
and cloud storage providers (Dropbox, OneDrive, Google Drive, Baidu Cloud, etc.).

## Status on DS212j

**Uninstalled** — removed 2026-05-08 during the [[HDD Hibernation]] investigation.

CloudSync was installed but its cloud accounts had expired OAuth tokens:
- **Dropbox:** `invalid_request` — `refresh_token` was empty
- **OneDrive:** `invalid_grant` — refresh token no longer valid

The failed token refresh attempts added extra disk activity (retries, logging),
contributing to the pool of processes preventing disk sleep.

## Removal

Stopped and uninstalled via DSM package manager (the `synopkg uninstall CloudSync` path).

## Related Pages

- [[DSM]] — package management and the OS where CloudSync ran
- [[Synology DS212j]] — the device where it was installed and uninstalled
- [[HDD Hibernation]] — why CloudSync was uninstalled (extra disk I/O)
