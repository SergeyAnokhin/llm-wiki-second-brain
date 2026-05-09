---
tags: [nfs, networking, protocol, storage, concept]
sources: [NFS solution.md]
created: 2026-05-09
updated: 2026-05-09
---

# NFS

Network File System (NFS) — a distributed file system protocol for sharing directories over a network.
Unlike SMB/CIFS, NFS is **stateless**: there is no persistent session between client and server.

## Key Property: Stateless vs Stateful

| Aspect | SMB/CIFS | NFS |
|---|---|---|
| Session | Persistent, authenticated | Stateless — each request independent |
| Disk writes when idle | Session DB, smbpasswd, logs | None |
| Hibernation impact | Keeps NAS active | Allows NAS to sleep |
| Proxmox support | Yes | Yes (native) |

## Why This Matters for NAS Hibernation

SMB mounts from [[Proxmox]] prevented [[HDD Hibernation]] on [[Synology DS212j]] because
each persistent connection caused `smbd`, `synologaccd`, and `syslog-ng` to write continuously.
NFS eliminates this: between backup runs there is no session to maintain, so the NAS can sleep.

## Setup on Synology DSM

1. **Enable NFS service:** Control Panel → File Services → NFS → Enable
2. **Grant access to a share:** Shared Folders → [share name] → NFS Permissions → add client IP (rw)
3. **Client IP for Proxmox:** 192.168.1.99

## Combined Workflow with Wake-on-LAN

```
NAS sleeps (HDDs spun down)
  ↓
Proxmox backup job starts
  ↓
pre-backup.sh: etherwake -i vmbr0 00:11:32:16:b0:6b → sleep 90
  ↓
NAS wakes, NFS mounts automatically
  ↓
Backup runs
  ↓
post-backup.sh: unmount NFS
  ↓
NAS idles → sleeps again in 10 min (standbytimer)
```

## Related Pages

- [[HDD Hibernation]] — problem NFS solves by eliminating persistent sessions
- [[Wake-on-LAN]] — companion mechanism to wake NAS before backup
- [[Proxmox]] — the NFS client being migrated from SMB
- [[Synology DS212j]] — NFS server
- [[DSM]] — configures NFS service
- [[NFS Solution]] — implementation guide source
