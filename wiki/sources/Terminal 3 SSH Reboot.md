---
tags: [synology, terminal, ssh, reboot, hibernation, source]
sources: [terminal 3.md]
created: 2026-05-09
updated: 2026-05-09
---

# Terminal 3 SSH Reboot

**Source:** terminal 3.md
**Date ingested:** 2026-05-09
**Type:** terminal session log

## Summary

Terminal session covering: re-enabling hibernation debug, network cable disconnect/reconnect test,
system reboot, and final cleanup (disable debug permanently). SSH sessions shown with verbose
output confirming [[SSH Key Authentication]] via key `claude-synology`.

## Key Claims

- Debug re-enabled and process manually started: `sudo /bin/sh /usr/syno/sbin/syno_hibernation_debug &`
- Network cable disconnected mid-session; SSH connection dropped; reconnected after cable restored
- After cable reconnect: diskstats show some writes even with no SMB clients (debug process + synologaccd)
- System rebooted; reconnected post-reboot; debug successfully disabled and killed
- Backup share contents confirmed: `dump`, `HomeAssistant`, `#recycle`, `vmSynology_Data.hbk`, `vmSynology_MyScan.hbk`, `vmSynology_Obsidian.hbk`
- Post-reboot state: clean (no SMB clients yet), but disk activity still present from core services

## Entities Mentioned

- [[Synology DS212j]] — device
- [[DSM]] — OS

## Concepts Covered

- [[HDD Hibernation]] — debug lifecycle: enable → test → reboot → disable
- [[SSH Key Authentication]] — used throughout; `claude-synology` ED25519 key confirmed working
