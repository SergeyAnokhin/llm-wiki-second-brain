---
tags: [synology, dsm, software, entity]
sources: [System info.md]
created: 2026-05-09
updated: 2026-05-09
---

# DSM

DiskStation Manager — Synology's Linux-based operating system for NAS devices.
Provides a web GUI (Control Panel), package management, and all core storage services.

## Version in Use

- **DSM 6.1.7-15284 Update 3** — running on [[Synology DS212j]]
- DSM 6.x is the legacy branch; the current major version as of 2024 is DSM 7.x
- The DS212j (88F6281 CPU) is not supported by DSM 7, so the device is capped at DSM 6.x

## Key System Services

| Service | Process | Function |
|---|---|---|
| File sharing (SMB) | `smbd` | Windows/Linux file share; stateful connections that block [[HDD Hibernation]] |
| Logging | `syslog-ng` | System log daemon; causes continuous disk writes |
| Account statistics | `synologaccd` | Tracks share access; writes to `.SYNOACCOUNTDB` |
| Hibernation debug | `syno_hibernation_debug` | Optional debug process for diagnosing sleep issues |
| CloudSync | (package) | Cloud backup sync; was uninstalled due to auth failures |

## Configuration File

Core system configuration lives in `/etc/synoinfo.conf` (key-value format).
Important hibernation-related flags:

```
support_disk_hibernation="yes"
enable_hibernation_debug="yes"
hibernation_debug_level="1"
standby_force="yes"
```

The standby timer can be set here (e.g., `60` minutes).

## Log Files

- `/var/log/hibernation.log` — summary hibernation log
- `/var/log/hibernationFull.log` — verbose hibernation debug log

## Package Management

Packages are managed via `synopkgctl`. Example:
```bash
synopkgctl stop CloudSync
synopkgctl uninstall CloudSync
```

## Related Pages

- [[Synology DS212j]] — the device running this DSM instance
- [[HDD Hibernation]] — hibernation mechanism and the investigation into why it fails
