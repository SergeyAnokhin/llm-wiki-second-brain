---
tags: [proxmox, virtualization, backup, entity]
sources: [Расследование проблемы сна Synology DS212j.md, NFS solution.md]
created: 2026-05-09
updated: 2026-05-09
---

# Proxmox

Proxmox VE — open-source hypervisor and virtualization platform.
Used in this home lab as the primary VM/container host, with [[Synology DS212j]] as backup storage.

## Role in This Setup

- Backs up VMs to the NAS via SMB (share `dump`, `VMware`) or NFS
- Held a persistent SMB session to the NAS (PID 6069) for 2+ days continuously
- The persistent connection prevented [[HDD Hibernation]] on the NAS
- IP address of Proxmox in LAN: 192.168.1.99 (conflicted with NAS IP — check exact values)

## Wake-on-LAN Integration

To allow the NAS to sleep and be woken before backup:
- Use `etherwake` utility to send a WOL magic packet
- Configure as a pre-backup hook in `/etc/vzdump.conf`
- NAS MAC address: `00:11:32:16:b0:6b`

## NFS Migration

Migration from SMB to NFS for backup storage is proposed to allow NAS hibernation:
- NFS is stateless — no persistent session kept between backups
- See [[NFS]] for configuration details

## Related Pages

- [[Synology DS212j]] — NAS device used for backup storage
- [[HDD Hibernation]] — why persistent SMB from Proxmox prevents NAS sleep
- [[Wake-on-LAN]] — solution for waking NAS before Proxmox backups
- [[NFS]] — stateless protocol proposed as SMB replacement
