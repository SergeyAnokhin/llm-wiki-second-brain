---
tags: [synology, nas, hardware, entity]
sources: [System info.md, nas-hibernation-settings.png, nas-hibernation-log.png]
created: 2026-05-09
updated: 2026-05-10
---

# Synology DS212j

A Synology DiskStation NAS (Network Attached Storage) device from the 2012 product line.
Used as a personal home-lab backup server and file storage device.

## Hardware Specifications

| Parameter | Value |
|---|---|
| Model | DS212j |
| Serial | C9KON02643 |
| CPU | MARVELL Kirkwood 88F6281 |
| CPU Speed | 1.2 GHz |
| CPU Cores | 1 |
| RAM | 256 MB |
| Max Disks | 2 |
| Disk Config | RAID-1 (mirrored) |

## Software

- **OS:** [[DSM]] 6.1.7-15284 Update 3
- **NTP Server:** time.google.com
- **Timezone:** GMT+01:00 (Amsterdam/Berlin/Rome/Stockholm/Vienna)

## Network

- **IP:** 192.168.1.99
- **WOL MAC:** 00:11:32:16:b0:6b
- **SSH key:** claude-synology (ED25519)
- **SSH server:** OpenSSH 6.8p1-hpn14v6
- **Pushservice account:** ivanoff.sergey@gmail.com

## Connected Hosts

| Host | IP | Protocol | Purpose |
|---|---|---|---|
| Proxmox | 192.168.1.99 | SMB → NFS | VM backups |
| Home Assistant | 192.168.1.92 | SMB | HA backups |

## Backup Shares

- `dump` — VM dumps from Proxmox
- `HomeAssistant` — HA backup files
- `Obsidian` — Obsidian vault sync
- `VMware` — VMware snapshots

## Notes

The device is constrained by its 2012-era hardware (256 MB RAM, single-core 1.2 GHz CPU),
which limits which DSM packages can run and affects background write load.
See [[HDD Hibernation]] for the full investigation. The HDD Sleep Mode panel (screenshot: [[NAS Hibernation Settings Screenshot]]) was configured with a 10-minute internal standby and enhanced sleep enabled. Post-investigation hibernation logs ([[NAS Hibernation Log Screenshot]]) confirm the NAS was successfully entering sleep after the [[NFS]] migration resolved the blocking SMB sessions.
