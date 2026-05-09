---
tags: [synology, terminal, disk-io, monitoring, source]
sources: [terminal 1.md]
created: 2026-05-09
updated: 2026-05-09
---

# Terminal 1 Disk IO Monitoring

**Source:** terminal 1.md
**Date ingested:** 2026-05-09
**Type:** terminal session log

## Summary

Terminal session monitoring disk I/O on [[Synology DS212j]] using `/proc/diskstats`.
Captures the initial phase of the [[HDD Hibernation]] investigation before any changes were made.

## Key Claims

- Disk write counters increment continuously: ~59 ops in 5 sec, ~85 in 10 sec, ~258 in 30 sec
- `lsof` not available on DSM — cannot use it to track open file handles
- Crontab entries show scheduled tasks via `/tmp/synoschedtask` (disk health, scheduled backups)
- Enabled packages at time of capture: SynoFinder 1.0.13, FileStation 1.1.6, CloudSync 2.7.0, HyperBackupVault 2.2.9
- RAID-1 visible as `md0_raid1`, `md1_raid1` kernel threads

## Entities Mentioned

- [[Synology DS212j]] — device being monitored
- [[DSM]] — OS running the services
- [[CloudSync]] — one of four enabled packages found

## Concepts Covered

- [[HDD Hibernation]] — disk counters show why hibernation cannot occur
