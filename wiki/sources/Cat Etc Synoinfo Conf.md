---
tags: [synology, dsm, configuration, synoinfo, source]
sources: [cat etc synoinfo.conf.md]
created: 2026-05-09
updated: 2026-05-09
---

# Cat Etc Synoinfo Conf

**Source:** cat etc synoinfo.conf.md
**Date ingested:** 2026-05-09
**Type:** terminal dump

## Summary

Full dump of `/etc/synoinfo.conf` captured via `cat` on the [[Synology DS212j]].
This file is the central configuration store for [[DSM]] — it defines hardware capabilities,
service limits, enabled services, and runtime flags.

## Key Claims

- Device unique ID: `synology_88f6281_212j` (matches CPU model 88F6281)
- Timezone configured as `Amsterdam`; NTP server `time.google.com`, updated daily
- Disk standby timer (`standbytimer`) is set to `60` (minutes)
- SATA deep sleep enabled: `sata_deep_sleep_en="yes"`, `satadeepsleeptimer="1"`
- Disk wakeup logging enabled: `disk_wakeup_log_en="yes"`
- Hibernation debug currently active: `enable_hibernation_debug="yes"`, `hibernation_debug_level="1"`
- System limits: maxdisks=2, maxaccounts=512, maxgroups=128, maxshares=256
- Package update channel set to `beta`
- Push service registered to `ivanoff.sergey@gmail.com`, serial `C9KON02643`
- SFTP port: 22; FTP port: 21

## Entities Mentioned

- [[Synology DS212j]] — device this config belongs to
- [[DSM]] — OS whose runtime state this file configures

## Concepts Covered

- [[HDD Hibernation]] — `standbytimer`, `sata_deep_sleep_en`, `enable_hibernation_debug` flags present
- [[SSH Key Authentication]] — SFTP/SSH enabled via port 22

## Notable Config Flags

```
# Hibernation
support_disk_hibernation="yes"
standbytimer="60"
standby_force="yes"
sata_deep_sleep_en="yes"
satadeepsleeptimer="1"
disk_wakeup_log_en="yes"
enable_hibernation_debug="yes"
hibernation_debug_level="1"
usb_standbytimer="30"

# Network services
supportNFS="yes"
supportNFSKerberos="yes"
supportssh="yes"
support_iscsi_target="yes"

# System limits
maxdisks="2"
maxaccounts="512"
maxgroups="128"
maxshares="256"

# Misc
package_update_channel="beta"
ntpdate_server="time.google.com"
ntpdate_period="daily"
timezone="Amsterdam"
hostname="DiskStation"
```
