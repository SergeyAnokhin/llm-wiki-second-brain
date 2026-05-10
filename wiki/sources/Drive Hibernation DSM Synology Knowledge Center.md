---
tags: [synology, hibernation, dsm, official-docs]
sources: [Drive Hibernation - DSM - Synology Knowledge Center.url]
created: 2026-05-10
updated: 2026-05-10
---

# Drive Hibernation DSM Synology Knowledge Center

**Source:** raw/urls/Drive Hibernation - DSM - Synology Knowledge Center.url
**URL:** https://kb.synology.com/en-global/DSM/help/DSM/AdminCenter/system_hardware_hibernation?version=7
**Date ingested:** 2026-05-10
**Type:** official documentation (DSM 7 inline help)

## Summary

Official Synology DSM 7 inline help page for the Drive Hibernation control panel section. Explains the three hibernation-related features available in Control Panel → Hardware & Power → Drive Hibernation: standard drive hibernation, Deep Sleep (for expansion units), and Auto Poweroff.

## Key Claims

- Drive hibernation stops disk spinning to reduce power consumption and extend drive lifespan
- Separate idle time settings for internal drives and external eSATA/USB drives
- All hibernation modes (including deep sleep) stop immediately when the system is accessed
- Only certain external USB drives support drive hibernation
- To disable hibernation: Control Panel > Hardware & Power > Drive Hibernation > select "none" in the first drop-down
- If NAS does not enter hibernation, Synology references a separate troubleshooting article

### Deep Sleep (Expansion Units Only)

- Deep Sleep applies to expansion units connected to a paired Synology NAS
- The expansion unit and the paired NAS can have **different idle time settings**
- The expansion unit can enter deep sleep while the paired NAS remains online
- While in deep sleep: all LEDs turn off, power to drives is cut, fan stops running
- Requires the Auto/Manual switch on the back of the expansion unit to be set to **Auto**

### Auto Poweroff

- NAS automatically powers off after drives have been in hibernation for a configured duration
- Requires internal drive hibernation to be enabled first
- To remotely power up after auto poweroff: must enable Wake on LAN (WOL) service first

## Entities Mentioned

- [[DSM]] — the NAS operating system; this is a DSM 7 inline help page
- [[Synology DS212j]] — home-lab NAS device this wiki was created for (not mentioned in the article but is the context)

## Concepts Covered

- [[HDD Hibernation]] — the main subject of this article; official definitions and behavior
- [[Wake-on-LAN]] — required to wake NAS after Auto Poweroff
