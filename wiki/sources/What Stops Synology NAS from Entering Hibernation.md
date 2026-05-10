---
tags: [synology, hibernation, troubleshooting, official-docs]
sources: [What stops my Synology NAS from entering Hibernation- - Synology Bilgi Merkezi.url]
created: 2026-05-10
updated: 2026-05-10
---

# What Stops Synology NAS from Entering Hibernation

**Source:** raw/urls/What stops my Synology NAS from entering Hibernation- - Synology Bilgi Merkezi.url
**URL:** https://kb.synology.com/en-us/DSM/tutorial/What_stops_my_Synology_NAS_from_entering_System_Hibernation
**Last updated (by Synology):** Mar 25, 2026
**Date ingested:** 2026-05-10
**Type:** official troubleshooting article

## Summary

Official Synology article listing every known factor that prevents a NAS from entering hibernation or causes unintended wake-ups. Organized into three categories: Volume Status, Services, Packages, and Others. Also provides two energy-saving alternatives for users who cannot disable the blocking services.

## Key Claims

- Numerous factors influence hibernation; this article is the authoritative Synology reference
- Categories: Volume Status, Services, Packages, Others
- Alternatives if you cannot disable blocking services: Power Schedule or Auto Poweroff + WOL

## Volume Status Blockers

- Volume is degraded or crashed
- No volume has been created

## Services That Block Hibernation

| Service / Setting | Location |
|---|---|
| DSM update auto-check running | Control Panel > Update & Restore > Update Settings > Check Schedule |
| Collect debug logs (SMB) | Control Panel > File Services > SMB > Advanced Settings > Others |
| DDNS enabled | Control Panel > External Access > DDNS |
| Data scrubbing schedule | Storage Manager > Storage Pool > Data Scrubbing |
| DHCP (auto network config) | Control Panel > Network > Network Interface |
| IP conflict detection | Control Panel > Network > General > Advanced Settings |
| Recycle Bin scheduled task | Control Panel > Task Scheduler |
| Resource Monitor usage history | Resource Monitor > Settings |
| File Services (SMB/AFP/FTP/NFS) active | Any active file transfer or SMB/CIFS broadcast (incl. Windows Explorer) |
| IPv6 enabled | Control Panel > Network > Network Interface > Edit > IPv6 |
| Domain/LDAP client | (since DSM 6.0.1) |
| Local Master Browser | Control Panel > File Services > SMB > Advanced Settings > Others |
| NTP service (sync with other devices) | Control Panel > Regional Options > NTP Service |
| QuickConnect enabled | Control Panel > External Access > QuickConnect |
| Remote Access enabled | Support Center > Support Services > Remote Access |
| Port forwarding (Router Configuration) | Control Panel > External Access > Router Configuration |
| Security Advisor scheduled scan | Security Advisor > Advanced > Scan Schedule |
| Share Network Location (Web Assistant) | Control Panel > Info Center > Device Analytics |
| S.M.A.R.T. test / IronWolf Health test | Storage Manager > HDD/SSD > Settings > Test Scheduler |
| Space Reclamation schedule | Storage Manager > Storage Pool > Global Settings > Set Time Grid |
| System Log Tools enabled | Support Center > Support Services > System Log Tools |
| SSD Cache in use | Resource Monitor continuously records cache hit rate |
| Thumbnails and indexing (synoindexd) | Resource Monitor > Task Manager > Processes |
| VPN clients | Control Panel > Network > Network Interface |
| Windows Media Player Network Sharing Service | (enabled on LAN) |
| WriteOnce shared folders | Writes time to drives once per day (Tamper-Proof Clock) |
| Memory swap (RAM exceeded) | HDDs used temporarily when RAM capacity is exceeded |

## Packages That Block Hibernation

- Synology Directory Server / Active Directory Server
- Active Backup for Business
- Active Backup for Business Agent (DSM) — if connected to another NAS
- Active Insight (if service is enabled)
- Audio Station — if logging is enabled (Audio Station > Settings > Advanced > General Settings)
- Calendar
- Cloud Station Server
- **Cloud Sync** — monitors changes to sync with public cloud; may prevent or interrupt hibernation
- Cloud Station ShareSync
- Central Management System (CMS) — if managing other NAS servers
- Container Manager
- LDAP Server
- Log Center — if devices are connected
- DNS Server
- Download Station — when running eMule, RSS downloads, or other active tasks
- Docker-Discourse, Docker-GitLab, Docker-LXQt, Docker-Redmine, Docker-Spree
- Document Viewer
- MailPlus Server / Mail Server / Mail Station / MailPlus
- Media Server — if DMA logging is enabled
- Plex Media Server
- PetaSpace
- Proxy Server
- Surveillance Station — if devices installed or tasks enabled
- Synology Contacts
- Synology AI Console — if token limits are enabled on any API integration
- Synology Drive Server — if devices are connected
- Synology Tiering / Tiering Vault
- Virtual Machine Manager
- VPN Server
- WebDAV Server

## Others

- Third-party packages — if any third-party package is running
- USB devices — if any USB device is attached
- Synology Photos app

## Alternatives If You Cannot Disable Services

1. **Power Schedule:** Control Panel > Hardware & Power > Power Schedule — set scheduled startup and shutdown times
2. **Auto Poweroff + WOL:** Enable auto poweroff (Control Panel > Hardware & Power > Drive Hibernation) and configure WOL (Control Panel > Hardware & Power > General > Power Recovery) to wake up remotely

## Entities Mentioned

- [[DSM]] — Synology NAS OS; all settings paths reference DSM Control Panel

## Concepts Covered

- [[HDD Hibernation]] — the primary subject; official complete list of blockers
- [[Wake-on-LAN]] — used with Auto Poweroff as an energy-saving alternative
- [[CloudSync]] — listed as a package that blocks hibernation
- [[NFS]] — mentioned indirectly: NFS is stateless and not listed as a blocker (only SMB/AFP/FTP block via file services)
