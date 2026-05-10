# Log

Chronological record of all operations.

## [2026-05-10] ingest | What Stops Synology NAS from Entering Hibernation
Processed raw/urls/What stops my Synology NAS from entering Hibernation- - Synology Bilgi Merkezi.url. Created 1 new page: [[What Stops Synology NAS from Entering Hibernation]]. Updated: [[HDD Hibernation]] (added official complete blockers list: 25+ services, 30+ packages), [[DSM]] (frontmatter sources).

## [2026-05-10] ingest | Drive Hibernation DSM Synology Knowledge Center
Processed raw/urls/Drive Hibernation - DSM - Synology Knowledge Center.url. Created 1 new page: [[Drive Hibernation DSM Synology Knowledge Center]]. Updated: [[HDD Hibernation]] (sources), [[DSM]] (Drive Hibernation UI section expanded with Deep Sleep and Auto Poweroff details).

## [2026-05-10] ingest | NAS Hibernation Settings Screenshot
Processed raw/images/nas-hibernation-settings.png. Created 1 new page: [[NAS Hibernation Settings Screenshot]]. Updated: [[HDD Hibernation]] (DSM UI section), [[DSM]] (HDD Sleep Mode UI section), [[Synology DS212j]] (notes).

## [2026-05-10] ingest | NAS Hibernation Log Screenshot
Processed raw/images/nas-hibernation-log.png. Created 1 new page: [[NAS Hibernation Log Screenshot]]. Updated: [[HDD Hibernation]] (Resolution section — confirmed hibernation working after NFS migration).

## [2026-05-09] lint | Fix broken wikilinks
Renamed 13 kebab-case files to Title Case with spaces so Obsidian resolves [[wikilinks]] correctly.

## [2026-05-09] ingest | SSH Connection Verbosity
Processed ssh connection verbosity.md. Created 1 new page: sources/ssh-connection-verbosity.
No new entities/concepts — all covered by [[SSH Key Authentication]].

## [2026-05-09] ingest | NFS Solution
Processed NFS solution.md. Created 2 new pages: sources/nfs-solution, concepts/nfs.
New concept: [[NFS]] (stateless protocol as SMB replacement for Proxmox backups; WOL workflow).

## [2026-05-09] ingest | Terminal 1, 2, 3 (disk I/O monitoring sessions)
Processed terminal 1.md, terminal 2.md, terminal 3.md. Created 4 new pages:
sources/terminal-1-disk-io-monitoring, sources/terminal-2-cloudsync-hibernation, sources/terminal-3-ssh-reboot, entities/cloudsync.
Updated: [[DSM]] (package list with HyperBackupVault, SynoFinder, CloudSync uninstall date).
New entity: [[CloudSync]] (uninstalled 2026-05-08, Dropbox/OneDrive tokens expired).

## [2026-05-09] ingest | Управление hibernation debug
Processed Управление hibernation debug.md. Created 1 new page: sources/upravlenie-hibernation-debug.
Updated: [[HDD Hibernation]] (full command reference for enable/disable/monitor).

## [2026-05-09] ingest | Расследование проблемы сна Synology DS212j
Processed Расследование проблемы сна Synology DS212j.md. Created 4 new pages: sources/rassledovanie-problemy-sna-synology-ds212j, entities/proxmox, concepts/wake-on-lan, concepts/ssh-key-authentication.
Updated: [[HDD Hibernation]] (major rewrite with investigation data, write frequency table, alternatives).
Note: standbytimer contradiction — investigation shows "10", current synoinfo.conf shows "60".

## [2026-05-09] ingest | Cat Etc Synoinfo Conf
Processed cat etc synoinfo.conf.md. Created 1 new page: sources/cat-etc-synoinfo-conf.
Updated existing: [[HDD Hibernation]] (standbytimer value, sata_deep_sleep_en), [[DSM]] (full flag list).

## [2026-05-09] lint | Fix filename-wikilink mismatch
Renamed 4 files from kebab-case to Title Case with spaces so Obsidian resolves [[wikilinks]] correctly: DSM.md, Synology DS212j.md, HDD Hibernation.md, Synology DS212j System Info.md.

## [2026-05-09] lint | Fix broken wikilinks
Found 1 error ([[HDD Hibernation]] broken in 3 places), 1 warning (empty Concepts index). Created wiki/concepts/hdd-hibernation.md and added index entry.

## [2026-05-09] ingest | Synology DS212j System Info
Processed System info.md. Created 3 new pages: sources/synology-ds212j-system-info, entities/synology-ds212j, entities/dsm.
New entities: [[Synology DS212j]], [[DSM]].

## [2026-05-05] setup | Vault initialized
Created vault "llm-wiki-second-brain" для разработки custom integrations и плагинов для Home Assistant.
Agent configs: CLAUDE.md, GEMINI.md, .github/copilot-instructions.md.
