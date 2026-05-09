---
tags: [synology, hibernation, hdd, concept]
sources: [System info.md]
created: 2026-05-09
updated: 2026-05-09
---

# HDD Hibernation

Disk sleep (hibernation) mode on [[Synology DS212j]] NAS devices — the ability to spin down hard drives after a period of inactivity to reduce power consumption and noise.

## How It Works

[[DSM]] monitors disk activity. When no reads or writes occur for a configured standby period, the drives spin down. On next access, DSM spins them back up (adds a few seconds of latency).

Key config flags in `/etc/synoinfo.conf`:

```
support_disk_hibernation="yes"
standby_force="yes"
enable_hibernation_debug="yes"
hibernation_debug_level="1"
```

The standby timer (in minutes) is also set in this file.

## Services That Block Hibernation

Background DSM services frequently write to disk, preventing hibernation:

| Service | Process | Cause |
|---|---|---|
| File sharing (SMB) | `smbd` | Stateful connections keep disk active |
| System logging | `syslog-ng` | Continuous log writes |
| Account statistics | `synologaccd` | Periodic writes to `.SYNOACCOUNTDB` |

Even with no user activity, these processes can wake or keep drives active.

## Debugging

Hibernation events are logged to:
- `/var/log/hibernation.log` — summary log
- `/var/log/hibernationFull.log` — verbose debug log

The `syno_hibernation_debug` process can be enabled for deeper diagnostics via `enable_hibernation_debug="yes"` in `/etc/synoinfo.conf`.

## Related Pages

- [[DSM]] — OS configuration and key services
- [[Synology DS212j]] — the device where this issue was investigated
