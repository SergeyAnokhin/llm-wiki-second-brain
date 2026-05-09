---
tags: [synology, dsm, software, entity]
sources: [System info.md, cat etc synoinfo.conf.md, terminal 1.md, terminal 2.md]
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
| CloudSync | (package) | Cloud backup sync; **uninstalled 2026-05-08** — Dropbox/OneDrive tokens expired |
| SynoFinder | (package) | Universal Search / file indexing; stopped to reduce disk I/O |
| HyperBackupVault | (package) | Receives Hyper Backup jobs from remote Synology devices |

## Configuration File

Core system configuration lives in `/etc/synoinfo.conf` (key-value format).
Important hibernation-related flags:

```
support_disk_hibernation="yes"
standbytimer="60"            # standby timeout in minutes (currently 60)
standby_force="yes"
sata_deep_sleep_en="yes"
satadeepsleeptimer="1"
disk_wakeup_log_en="yes"
enable_hibernation_debug="yes"
hibernation_debug_level="1"
```

Other notable runtime flags: `package_update_channel="beta"`, `ntpdate_server="time.google.com"`,
`ntpdate_period="daily"`, `dsmtimeout="3600"` (session timeout 1 hour).

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
