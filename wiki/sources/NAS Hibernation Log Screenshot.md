---
tags: [synology, hibernation, dsm, screenshot, log, source]
sources: [nas-hibernation-log.png]
created: 2026-05-10
updated: 2026-05-10
---

# NAS Hibernation Log Screenshot

**Source:** raw/images/nas-hibernation-log.png
**Date ingested:** 2026-05-10
**Type:** screenshot / terminal output

## Summary

Terminal screenshot showing [[DSM]] hibernation log output from [[Synology DS212j]]. The log contains multiple dated entries spanning April–May 2026, confirming that the hibernation logging mechanism was active and that real disk wake events were occurring during and after the investigation.

## Key Claims

- Hibernation log entries are present from **April 2026** (dates visible: April 8, 9, 21–24) and **May 2026** (May 8–9)
- Log entries follow the `INFO SYNO:` format, characteristic of DSM's `disk_wakeup_log_en` feature
- The presence of log entries across multiple months confirms the NAS successfully entered hibernation — disks that never sleep produce no wake log entries
- The log was captured via a shell command reading from the DSM log system (consistent with the debug approach documented in [[Управление Hibernation Debug]])

## Entities Mentioned

- [[Synology DS212j]] — the device whose log is shown
- [[DSM]] — the OS writing the hibernation log

## Concepts Covered

- [[HDD Hibernation]] — these log entries are direct evidence that hibernation occurred; the volume and span of entries (April–May) suggest the NAS was successfully sleeping after the investigation concluded
