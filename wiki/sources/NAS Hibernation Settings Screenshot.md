---
tags: [synology, hibernation, dsm, screenshot, source]
sources: [nas-hibernation-settings.png]
created: 2026-05-10
updated: 2026-05-10
---

# NAS Hibernation Settings Screenshot

**Source:** raw/images/nas-hibernation-settings.png
**Date ingested:** 2026-05-10
**Type:** screenshot

## Summary

DSM Control Panel screenshot showing the **"Спящий режим жёсткого диска"** (HDD Sleep Mode) tab under Hardware & Power. Captures the exact hibernation configuration active on [[Synology DS212j]] during the investigation period.

## Key Claims

- Internal HDD and external SATA disk standby timeout: **10 minutes**
- **Enhanced HDD sleep mode is enabled** (DSM-specific option to further reduce DS212j power consumption)
- USB HDD standby timeout: **30 minutes** (only applies to USB devices that support sleep)
- **Sleep logging is enabled** — DSM records timestamps of each disk wake-up event

## DSM UI Panel Description

The panel has four sections:

1. **Internal / SATA timeout** — a dropdown set to "10 Минут" (10 Minutes)
2. **Enhanced sleep mode checkbox** — "Включите расширенный спящий режим жёсткого диска для снижения потребления энергии устройством DS212j" (checked)
3. **USB timeout** — a dropdown set to "30 Минут" (30 Minutes), with a note that USB devices must support sleep mode
4. **Sleep log checkbox** — "Включить журналы спящего режима" (checked), which records wake-up times for internal, external SATA, and USB disks

## Entities Mentioned

- [[Synology DS212j]] — the device whose settings are shown
- [[DSM]] — the operating system providing this Control Panel

## Concepts Covered

- [[HDD Hibernation]] — the 10-minute timeout here corresponds to `standbytimer="10"` in `/etc/synoinfo.conf`
