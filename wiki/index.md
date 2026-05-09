# Index

Master catalog of all wiki pages. Updated on every ingest.

## Sources

- [[Synology DS212j System Info]] — DSM Control Panel snapshot: hardware specs, firmware version, uptime, NTP config
- [[Cat Etc Synoinfo Conf]] — Full dump of /etc/synoinfo.conf: system flags, service limits, hibernation config
- [[Расследование Проблемы Сна Synology DS212j]] — Full investigation: why DS212j cannot hibernate; write sources and alternatives
- [[Управление Hibernation Debug]] — Command reference: enable/disable debug, monitor logs, find max idle period
- [[Terminal 1 Disk IO Monitoring]] — Baseline disk I/O measurement; installed packages list
- [[Terminal 2 CloudSync Hibernation]] — CloudSync uninstall; auth token errors; debug disabled
- [[Terminal 3 SSH Reboot]] — Debug lifecycle, network test, system reboot, final cleanup
- [[NFS Solution]] — SMB→NFS migration guide for Proxmox; WOL pre-backup hook implementation
- [[SSH Connection Verbosity]] — Verbose SSH handshake log; confirms key fingerprints and cipher suite
- [[NAS Hibernation Settings Screenshot]] — DSM Control Panel: HDD Sleep Mode tab; 10 min SATA, enhanced sleep enabled, 30 min USB
- [[NAS Hibernation Log Screenshot]] — Terminal hibernation log; dated wake events April–May 2026 confirm hibernation is working
## Entities

- [[Synology DS212j]] — Home-lab NAS device: MARVELL 1.2 GHz, 256 MB RAM, DSM 6.1.7, serial C9KON02643
- [[DSM]] — Synology DiskStation Manager 6.1.7: OS, key services, config flags, package management
- [[Proxmox]] — Home-lab hypervisor; backup client whose persistent SMB session blocks NAS hibernation
- [[CloudSync]] — DSM package (uninstalled 2026-05-08); Dropbox/OneDrive sync with expired tokens

## Concepts

- [[HDD Hibernation]] — Synology NAS disk sleep mechanism; full investigation, write sources, and alternatives
- [[Wake-on-LAN]] — Network power-on via magic packet; proposed as NAS hibernation alternative
- [[SSH Key Authentication]] — ED25519 key-based SSH login; configured for DS212j during investigation
- [[NFS]] — Stateless network file protocol; proposed to replace SMB for Proxmox→NAS backups

## Synthesis
