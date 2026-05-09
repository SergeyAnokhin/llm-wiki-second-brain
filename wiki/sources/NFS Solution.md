---
tags: [synology, nfs, smb, proxmox, hibernation, source]
sources: [NFS solution.md]
created: 2026-05-09
updated: 2026-05-09
---

# NFS Solution

**Source:** NFS solution.md
**Date ingested:** 2026-05-09
**Type:** technical guide / architecture proposal

## Summary

Proposes migrating [[Proxmox]] backup storage from SMB to [[NFS]] to enable [[HDD Hibernation]]
on [[Synology DS212j]]. The core argument: NFS is stateless and creates no persistent session,
so the NAS can sleep between backups. Combined with [[Wake-on-LAN]], this creates an
energy-efficient backup workflow.

## Key Claims

- NFS is stateless — no persistent session, no authentication DB writes when idle
- SMB maintains a session database, writes to disk continuously even with no file transfers
- Proposed workflow: NAS sleeps → Proxmox sends WOL → wait 90 sec → NFS mounts → backup → unmount → NAS sleeps after 10 min
- WOL sent on Proxmox interface `vmbr0`; NAS MAC: `00:11:32:16:b0:6b`

## SMB vs NFS Comparison

| Aspect | SMB/CIFS | NFS |
|---|---|---|
| Connection | Stateful session with auth | Stateless — no session |
| Disk writes when idle | session DB, smbpasswd, transfer log | None |
| Impact on hibernation | Strong — keeps sync active | Minimal |
| Proxmox support | Yes | Yes (native) |

## Implementation Steps

1. **Enable NFS on DSM:** Control Panel → File Services → NFS → Enable
2. **Grant share permissions:** Shared Folders → Backup → NFS Permissions → add `192.168.1.99` (rw)
3. **Add NFS storage in Proxmox:** Datacenter → Storage → Add → NFS → IP 192.168.1.99
4. **Add WOL pre-backup hook** in `/etc/vzdump/pre-backup.sh`:

```bash
#!/bin/bash
if [ "$PHASE" = "job-start" ]; then
    etherwake -i vmbr0 00:11:32:16:b0:6b
    sleep 90
fi
```

## Entities Mentioned

- [[Proxmox]] — the backup host being migrated from SMB to NFS
- [[Synology DS212j]] — NAS storage target
- [[DSM]] — configures NFS service and share permissions

## Concepts Covered

- [[NFS]] — proposed protocol replacement
- [[HDD Hibernation]] — the goal this migration serves
- [[Wake-on-LAN]] — pre-backup wakeup mechanism
