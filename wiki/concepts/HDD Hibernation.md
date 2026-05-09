---
tags: [synology, hibernation, hdd, concept]
sources: [System info.md, cat etc synoinfo.conf.md, Расследование проблемы сна Synology DS212j.md, Управление hibernation debug.md]
created: 2026-05-09
updated: 2026-05-09
---

# HDD Hibernation

Disk sleep (hibernation) mode on [[Synology DS212j]] NAS devices — the ability to spin down hard drives after a period of inactivity to reduce power consumption and noise.

## How It Works

[[DSM]] monitors disk I/O. When no reads or writes occur for a configured standby period, the drives spin down. On next access, DSM spins them back up (5–15 seconds latency).

**Key rule:** A single disk write resets the idle counter to zero.

Key config flags in `/etc/synoinfo.conf`:

```
support_disk_hibernation="yes"
standbytimer="10"          # timeout in minutes (was 10 during investigation)
standby_force="yes"
sata_deep_sleep_en="yes"   # SATA deep sleep
satadeepsleeptimer="1"
disk_wakeup_log_en="yes"   # log each wakeup event
usb_standbytimer="30"      # USB device standby (minutes)
enable_hibernation_debug="yes"
hibernation_debug_level="1"
```

> **Note:** The current synoinfo.conf dump shows `standbytimer="60"`, but the investigation
> captured `standbytimer="10"` (600 sec). The value was changed during or after the investigation.
> Default in `/etc.defaults/synoinfo.conf` was `standbytimer="20"`.

When debug is active, `syno_hibernation_debug` logs idle duration to `/var/log/hibernation.log`
approximately every 20 seconds.

## Investigation Results (DS212j)

Full investigation documented in [[Расследование Проблемы Сна Synology DS212j]].

**Required idle:** 600 seconds (10 minutes)
**Maximum idle achieved with SMB clients:** 23 seconds
**Maximum idle achieved without SMB clients:** 57 seconds
**Write rate with SMB clients:** 8–9 writes/second
**Write rate without SMB clients:** 1.4 writes/second

Conclusion: HDD hibernation is **not achievable** in the current configuration.
Core [[DSM]] services write continuously regardless of network activity.

## Services That Block Hibernation

| Process | Writes to | Frequency | Can disable? |
|---|---|---|---|
| `synologaccd` | `.SYNOACCOUNTDB` | every 2 sec | **No** (core DSM) |
| `syslog-ng` | `.SYNOCONNDB` | every 2–3 sec | **No** (core DSM) |
| `smbd` | session DB, logs | every 4 sec | Only by removing SMB clients |
| `jbd2/md0-8` | ext4 journal | every 10 sec | No (follows above) |
| `syno_hibernation_debug` | hibernation log | every 20 sec | Yes — disable in synoinfo.conf |

**Paradox:** The hibernation debug process itself prevents hibernation by writing every 20 seconds.

## SMB Sessions Blocking Sleep

Two persistent SMB sessions kept the NAS awake indefinitely:
- [[Proxmox]] (192.168.1.99) → share `Backup` — connected for 2+ days without interruption
- Home Assistant (192.168.1.92) → share `Backup`

Each active SMB session causes `smbd`, `synologaccd`, and `syslog-ng` to write continuously.

## Debugging

Hibernation events are logged to:
- `/var/log/hibernation.log` — summary log (idle periods, wakeup reasons)
- `/var/log/hibernationFull.log` — verbose debug log

Enable debug mode:
```bash
sudo synosetkeyvalue /etc/synoinfo.conf enable_hibernation_debug yes
sudo /bin/sh /usr/syno/sbin/syno_hibernation_debug &
```

Disable:
```bash
sudo synosetkeyvalue /etc/synoinfo.conf enable_hibernation_debug no
sudo kill $(ps aux | grep syno_hibernation_debug | grep -v grep | awk '{print $2}')
```

Monitor in real-time:
```bash
tail -f /var/log/hibernation.log | grep 'Idle'
grep '======Idle' /var/log/hibernation.log | sed 's/[^0-9]//g' | sort -n | tail -5
```

Config changes via `synosetkeyvalue` **survive reboots** — DSM reads the flag on next start.
See [[Управление Hibernation Debug]] for the full command reference.

## Recommended Alternatives

Since hibernation is not achievable, three alternatives are proposed:

**Option A — Power Schedule (recommended):**
DSM → Hardware & Power → Power Schedule. Configure scheduled shutdown and power-on.
Works reliably regardless of SMB sessions or background processes.

**Option B — [[Wake-on-LAN]]:**
NAS shuts down on schedule; backup hosts send a WOL magic packet to wake it before backup.
MAC address: `00:11:32:16:b0:6b`.

**Option C — Temporary SMB mounts:**
Configure [[Proxmox]] and Home Assistant to mount SMB only during backup, not permanently.
Would raise idle from 23 sec to ~57 sec — still not enough for hibernation.

**Option D — [[NFS]] instead of SMB:**
NFS is stateless; no persistent session is maintained between accesses.
This allows the NAS to sleep between backup runs. See [[NFS]] for implementation.

## Related Pages

- [[DSM]] — OS configuration and key services
- [[Synology DS212j]] — the device where this issue was investigated
- [[Proxmox]] — backup host whose SMB session blocks NAS hibernation
- [[Wake-on-LAN]] — proposed alternative to auto-sleep
- [[NFS]] — stateless protocol proposed as SMB replacement
- [[Расследование Проблемы Сна Synology DS212j]] — full investigation source
