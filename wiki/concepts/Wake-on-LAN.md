---
tags: [wake-on-lan, wol, networking, power-management, concept]
sources: [Расследование проблемы сна Synology DS212j.md, NFS solution.md]
created: 2026-05-09
updated: 2026-05-09
---

# Wake-on-LAN

Wake-on-LAN (WOL) is a network standard that allows a powered-off or sleeping device to be
turned on remotely by sending a "magic packet" to its MAC address.

## How It Works

1. Target device must have WOL enabled in BIOS/firmware and a wired network connection
2. Sender broadcasts a magic packet containing the target's MAC address
3. The network card (which stays powered) detects the packet and powers on the device

## Use in This Setup

WOL is proposed as **Option B** for [[HDD Hibernation]] on [[Synology DS212j]]:
- NAS is powered off on a schedule (DSM Power Schedule)
- Before each backup, the backup host sends a WOL magic packet to wake the NAS
- After backup, NAS shuts down again

**NAS MAC address:** `00:11:32:16:b0:6b`

## Implementation

### From Proxmox

```bash
# Install etherwake
apt install etherwake

# Send magic packet
etherwake 00:11:32:16:b0:6b
```

Add as a pre-backup hook in `/etc/vzdump.conf`.

### From Home Assistant

Use the `wake_on_lan` integration:
```yaml
# configuration.yaml
wake_on_lan:

# automation: wake NAS before backup
service: wake_on_lan.send_magic_packet
data:
  mac: "00:11:32:16:b0:6b"
```

### With NFS (combined solution)

The [[NFS]] solution document proposes a full workflow:
1. Proxmox pre-backup script sends WOL → waits for NAS to come online
2. Backup runs via NFS mount
3. Post-backup: NAS sleeps (NFS is stateless, no persistent session)

## Related Pages

- [[HDD Hibernation]] — why WOL is needed as an alternative to auto-sleep
- [[Synology DS212j]] — target device for WOL
- [[Proxmox]] — backup host that wakes the NAS
- [[NFS]] — stateless protocol that works well with the WOL workflow
