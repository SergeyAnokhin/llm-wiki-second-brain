---
tags: [synology, hibernation, debug, commands, source]
sources: [Управление hibernation debug.md]
created: 2026-05-09
updated: 2026-05-09
---

# Управление Hibernation Debug

**Source:** Управление hibernation debug.md
**Date ingested:** 2026-05-09
**Type:** technical guide / command reference

## Summary

Step-by-step command reference for managing the hibernation debug process on [[Synology DS212j]].
Covers enabling, disabling, status checking, and log monitoring.

## Key Claims

- Config changes via `synosetkeyvalue` survive reboots — [[DSM]] reads the flag on startup and auto-starts/stops the process
- If flag is `yes` but process is not running, start manually with `/bin/sh /usr/syno/sbin/syno_hibernation_debug &`
- `/var/log/hibernation.log` — brief log (idle periods, who writes)
- `/var/log/hibernationFull.log` — verbose log (all I/O operations)

## Commands

### Check Status
```bash
echo "=== Config ===" && \
grep enable_hibernation_debug /etc/synoinfo.conf && \
echo "=== Process ===" && \
ps aux | grep syno_hibernation_debug | grep -v grep || echo "process NOT running"
```

### Enable Debug
```bash
sudo synosetkeyvalue /etc/synoinfo.conf enable_hibernation_debug yes
sudo /bin/sh /usr/syno/sbin/syno_hibernation_debug &
ps aux | grep syno_hibernation_debug | grep -v grep
```

### Disable Debug
```bash
sudo synosetkeyvalue /etc/synoinfo.conf enable_hibernation_debug no
sudo kill $(ps aux | grep syno_hibernation_debug | grep -v grep | awk '{print $2}')
ps aux | grep syno_hibernation_debug | grep -v grep || echo "process stopped"
```

### Monitor Logs
```bash
# Idle periods only
tail -f /var/log/hibernation.log | grep 'Idle'

# Full log with write sources
tail -f /var/log/hibernation.log

# Find maximum idle period
grep '======Idle' /var/log/hibernation.log | sed 's/[^0-9]//g' | sort -n | tail -5
```

## Entities Mentioned

- [[Synology DS212j]] — device these commands run on
- [[DSM]] — OS that manages the debug process lifecycle

## Concepts Covered

- [[HDD Hibernation]] — debug tooling for diagnosing hibernation failures
