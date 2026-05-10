---
tags: [synology, hibernation, hdd, concept]
sources: [System info.md, cat etc synoinfo.conf.md, Расследование проблемы сна Synology DS212j.md, Управление hibernation debug.md, nas-hibernation-settings.png, nas-hibernation-log.png, Drive Hibernation - DSM - Synology Knowledge Center.url, What stops my Synology NAS from entering Hibernation- - Synology Bilgi Merkezi.url]
created: 2026-05-09
updated: 2026-05-10
---

# HDD Hibernation

Disk sleep (hibernation) mode on [[Synology DS212j]] NAS devices — the ability to spin down hard drives after a period of inactivity to reduce power consumption and noise.

## DSM UI Settings

The hibernation timeout is configured in **DSM Control Panel → Hardware & Power → HDD Sleep Mode** (screenshot: [[NAS Hibernation Settings Screenshot]]):

| Setting | Value |
|---|---|
| Internal HDD / SATA standby | **10 minutes** |
| Enhanced sleep mode | **Enabled** |
| USB HDD standby | **30 minutes** |
| Sleep logs | **Enabled** |

These UI values correspond 1-to-1 with `/etc/synoinfo.conf` flags: `standbytimer="10"`, `sata_deep_sleep_en="yes"`, `usb_standbytimer="30"`, `disk_wakeup_log_en="yes"`.

## How It Works

[[DSM]] monitors disk I/O. When no reads or writes occur for a configured standby period, the drives spin down. On next access, DSM spins them back up (5–15 seconds latency).

**Key rule:** A single disk write resets the idle counter to zero.

Key config flags in `/etc/synoinfo.conf`:

```
support_disk_hibernation="yes"
standbytimer="10"          # timeout in minutes (was 10 during investigation)
standby_force="yes"
sata_deep_sleep_en="yes"   # SATA deep sleep
satadeepsleeptimer="1"
disk_wakeup_log_en="yes"   # log each wakeup event
usb_standbytimer="30"      # USB device standby (minutes)
enable_hibernation_debug="yes"
hibernation_debug_level="1"
```

> **Note:** The current synoinfo.conf dump shows `standbytimer="60"`, but the investigation
> captured `standbytimer="10"` (600 sec). The value was changed during or after the investigation.
> Default in `/etc.defaults/synoinfo.conf` was `standbytimer="20"`.

When debug is active, `syno_hibernation_debug` logs idle duration to `/var/log/hibernation.log`
approximately every 20 seconds.

## Investigation Results (DS212j)

Full investigation documented in [[Расследование Проблемы Сна Synology DS212j]].

**Required idle:** 600 seconds (10 minutes)
**Maximum idle achieved with SMB clients:** 23 seconds
**Maximum idle achieved without SMB clients:** 57 seconds
**Write rate with SMB clients:** 8–9 writes/second
**Write rate without SMB clients:** 1.4 writes/second

Conclusion: HDD hibernation is **not achievable** in the current configuration.
Core [[DSM]] services write continuously regardless of network activity.

## Official List of Hibernation Blockers

Source: [[What Stops Synology NAS from Entering Hibernation]] (Synology KB, last updated Mar 25, 2026).

### Volume Status

- Volume is degraded or crashed
- No volume has been created

### System Services

| Service / Setting | Notes |
|---|---|
| DSM auto-update check running | Scheduled check wakes the system |
| SMB "Collect debug logs" enabled | Writes continuously |
| DDNS enabled | Periodic external calls |
| Data scrubbing schedule | Wakes disks during scrub |
| DHCP on any LAN | Periodic broadcast traffic |
| IP conflict detection | Periodic checks |
| Recycle Bin scheduled task | Wakes system on schedule |
| Resource Monitor usage history | Continuous write to disk |
| **File Services (SMB/AFP/FTP/NFS) active** | Any active transfer or SMB/CIFS broadcast — even Windows Explorer on the LAN |
| IPv6 enabled | Background IPv6 traffic |
| Domain/LDAP client (DSM ≥ 6.0.1) | Continuous directory polling |
| Local Master Browser | SMB browsing broadcasts |
| **NTP service** (syncing other devices) | Periodic NTP server activity |
| QuickConnect enabled | Relay keepalive traffic |
| Remote Access enabled | Persistent tunnel |
| Port forwarding rules configured | Periodic router communication |
| Security Advisor scheduled scan | Wakes system on schedule |
| Share Network Location (Web Assistant) | Beacon traffic |
| S.M.A.R.T. / IronWolf Health test scheduled | Wakes system on schedule |
| Space Reclamation scheduled | Wakes system on schedule |
| System Log Tools enabled | Continuous write |
| SSD Cache in use | Resource Monitor records hit rate continuously |
| Thumbnails / indexing (synoindexd) | Active when re-indexing after updates |
| VPN clients | Persistent tunnel keepalives |
| Windows Media Player Network Sharing | WMP broadcasts on LAN |
| WriteOnce shared folders | Writes timestamp to drives once per day |
| RAM exceeded → memory swap | HDD used as swap when RAM full |

### Packages That Block Hibernation

- Synology Directory Server / Active Directory Server
- Active Backup for Business (and Agent)
- Active Insight (if enabled)
- Audio Station (if logging enabled)
- Calendar
- Cloud Station Server / Cloud Station ShareSync
- **[[CloudSync]]** — monitors changes continuously; well-known hibernation blocker
- Central Management System (CMS)
- Container Manager
- LDAP Server / DNS Server
- Log Center (if devices connected)
- Download Station (during active tasks)
- Docker-based packages (Discourse, GitLab, LXQt, Redmine, Spree)
- Document Viewer
- Mail Server / Mail Station / MailPlus / MailPlus Server
- Media Server (if DMA logging enabled)
- Plex Media Server
- PetaSpace / Proxy Server
- Surveillance Station (if devices or tasks configured)
- Synology Contacts / Synology AI Console / Synology Drive Server
- Synology Tiering / Tiering Vault
- Virtual Machine Manager / VPN Server / WebDAV Server

### Other Blockers

- Any third-party package running
- USB device attached to the NAS
- Synology Photos app

## Services That Block Hibernation (Investigation Data)

Observed write rates on [[Synology DS212j]] during the hibernation investigation:

| Process | Writes to | Frequency | Can disable? |
|---|---|---|---|
| `synologaccd` | `.SYNOACCOUNTDB` | every 2 sec | **No** (core DSM) |
| `syslog-ng` | `.SYNOCONNDB` | every 2–3 sec | **No** (core DSM) |
| `smbd` | session DB, logs | every 4 sec | Only by removing SMB clients |
| `jbd2/md0-8` | ext4 journal | every 10 sec | No (follows above) |
| `syno_hibernation_debug` | hibernation log | every 20 sec | Yes — disable in synoinfo.conf |

**Paradox:** The hibernation debug process itself prevents hibernation by writing every 20 seconds.

## SMB Sessions Blocking Sleep

Two persistent SMB sessions kept the NAS awake indefinitely:
- [[Proxmox]] (192.168.1.99) → share `Backup` — connected for 2+ days without interruption
- Home Assistant (192.168.1.92) → share `Backup`

Each active SMB session causes `smbd`, `synologaccd`, and `syslog-ng` to write continuously.

## Debugging

Hibernation events are logged to:
- `/var/log/hibernation.log` — summary log (idle periods, wakeup reasons)
- `/var/log/hibernationFull.log` — verbose debug log

Enable debug mode:
```bash
sudo synosetkeyvalue /etc/synoinfo.conf enable_hibernation_debug yes
sudo /bin/sh /usr/syno/sbin/syno_hibernation_debug &
```

Disable:
```bash
sudo synosetkeyvalue /etc/synoinfo.conf enable_hibernation_debug no
sudo kill $(ps aux | grep syno_hibernation_debug | grep -v grep | awk '{print $2}')
```

Monitor in real-time:
```bash
tail -f /var/log/hibernation.log | grep 'Idle'
grep '======Idle' /var/log/hibernation.log | sed 's/[^0-9]//g' | sort -n | tail -5
```

Config changes via `synosetkeyvalue` **survive reboots** — DSM reads the flag on next start.
See [[Управление Hibernation Debug]] for the full command reference.

## Resolution

The hibernation log screenshot ([[NAS Hibernation Log Screenshot]]) shows real wake events recorded across **April–May 2026** — disks that never sleep produce no wake entries. This confirms that [[Synology DS212j]] was successfully entering hibernation after the investigation concluded.

The most likely cause of the fix: migration from SMB to [[NFS]] for [[Proxmox]] backups (see [[NFS Solution]]). NFS is stateless — no persistent session is maintained between accesses — allowing the NAS to sleep between backup runs.

> The conclusion "HDD hibernation is **not achievable**" reflected the state during the SMB-based configuration. After the NFS migration, hibernation became functional.

## Recommended Alternatives

Since hibernation is not achievable with many common configurations, these alternatives are available (confirmed by both investigation and official Synology docs):

**Option A — Power Schedule (recommended):**
DSM → Hardware & Power → Power Schedule. Configure scheduled shutdown and power-on.
Works reliably regardless of SMB sessions or background processes.

**Option B — Auto Poweroff + [[Wake-on-LAN]]:**
Enable Auto Poweroff in Control Panel → Hardware & Power → Drive Hibernation.
NAS powers off after drives have been in hibernation for a configured time.
Enable WOL in Control Panel → Hardware & Power → General → Power Recovery to wake remotely.
MAC address: `00:11:32:16:b0:6b`.

**Option C — Temporary SMB mounts:**
Configure [[Proxmox]] and Home Assistant to mount SMB only during backup, not permanently.
Would raise idle from 23 sec to ~57 sec — still not enough for hibernation.

**Option D — [[NFS]] instead of SMB:**
NFS is stateless; no persistent session is maintained between accesses.
This allows the NAS to sleep between backup runs. See [[NFS]] for implementation.
NFS is **not listed** in the official hibernation blockers article, unlike SMB/AFP/FTP.

## Related Pages

- [[DSM]] — OS configuration and key services
- [[Synology DS212j]] — the device where this issue was investigated
- [[Proxmox]] — backup host whose SMB session blocks NAS hibernation
- [[Wake-on-LAN]] — proposed alternative to auto-sleep
- [[NFS]] — stateless protocol proposed as SMB replacement
- [[Расследование Проблемы Сна Synology DS212j]] — full investigation source
- [[Drive Hibernation DSM Synology Knowledge Center]] — official DSM 7 UI help (Drive Hibernation panel)
- [[What Stops Synology NAS from Entering Hibernation]] — official complete blockers list (Synology KB)
