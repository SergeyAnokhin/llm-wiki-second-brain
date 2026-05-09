---
tags: [synology, hibernation, investigation, nas, source]
sources: [Расследование проблемы сна Synology DS212j.md]
created: 2026-05-09
updated: 2026-05-09
---

# Расследование Проблемы Сна Synology DS212j

**Source:** Расследование проблемы сна Synology DS212j.md
**Date ingested:** 2026-05-09
**Type:** technical investigation report

## Summary

Full technical investigation into why [[Synology DS212j]] fails to enter [[HDD Hibernation]].
The device never achieves the 600-second (10-minute) idle period required for disk sleep.
Root cause: DSM core services write continuously to disk; even disconnecting the network cable
did not help because `synologaccd` and `syslog-ng` write independently of network activity.

## Key Claims

- Target goal: NAS sleeps for ~23 hours/day, active only 1 hour
- Required idle for hibernation: 600 seconds (10 minutes) — `standbytimer="10"` at the time of investigation
- Maximum idle achieved with SMB clients connected: **23 seconds**
- Maximum idle achieved without SMB clients (after reboot): **57 seconds**
- Disk write rate with SMB clients: 8–9 writes/second; without: 1.4 writes/second
- `synologaccd` and `syslog-ng` are core DSM services — **cannot be disabled**
- The hibernation debug process `syno_hibernation_debug` itself writes every 20 sec, preventing sleep (paradox)
- Two persistent SMB sessions found: Proxmox (PID 6069, connected 2+ days) and Home Assistant (PID 27182)
- Hibernation was working before because Proxmox/HA were not continuously mounted, CloudSync was inactive, and debug was off
- Standbytimer conflict: investigation shows `standbytimer="10"`, but current synoinfo.conf shows `standbytimer="60"` — value changed during/after investigation

## Disk Write Sources

| Process | Writes to | Frequency | Can disable? |
|---|---|---|---|
| `synologaccd` | `.SYNOACCOUNTDB` | every 2 sec | No (core) |
| `syslog-ng` | `.SYNOCONNDB` | every 2–3 sec | No (core) |
| `smbd` | session DB, logs | every 4 sec | Only by removing SMB clients |
| `jbd2/md0-8` | ext4 journal | every 10 sec | No (follows above) |
| `syno_hibernation_debug` | hibernation log | every 20 sec | Yes — disable in synoinfo.conf |

## Recommendations

- **Option A (recommended):** Power Schedule — configure hardware on/off times in DSM
- **Option B:** [[Wake-on-LAN]] — NAS off by schedule, woken by magic packet before backup
  - [[Proxmox]] hook: `etherwake` in `/etc/vzdump.conf`; MAC: `00:11:32:16:b0:6b`
  - Home Assistant: `wake_on_lan` integration automation
- **Option C:** Temporary SMB mounts — mount only during backup, not permanently

## Entities Mentioned

- [[Synology DS212j]] — the device investigated
- [[DSM]] — OS whose core processes block hibernation
- [[Proxmox]] — backup server holding persistent SMB session
- Home Assistant — holding persistent SMB session (192.168.1.92)

## Concepts Covered

- [[HDD Hibernation]] — full investigation of why it fails
- [[Wake-on-LAN]] — proposed solution B
- [[SSH Key Authentication]] — ED25519 key `claude-synology` set up during investigation
