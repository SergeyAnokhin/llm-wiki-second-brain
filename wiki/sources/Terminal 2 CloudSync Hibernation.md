---
tags: [synology, terminal, cloudsync, hibernation, source]
sources: [terminal 2.md]
created: 2026-05-09
updated: 2026-05-09
---

# Terminal 2 CloudSync Hibernation

**Source:** terminal 2.md
**Date ingested:** 2026-05-09
**Type:** terminal session log

## Summary

Terminal session focused on disabling [[HDD Hibernation]] debug and uninstalling [[CloudSync]]
from [[Synology DS212j]]. System log revealed CloudSync was failing with expired auth tokens
for both Dropbox and OneDrive.

## Key Claims

- CloudSync had expired refresh tokens for Dropbox (`invalid_request`) and OneDrive (`invalid_grant`) since 2026-05-08
- CloudSync was stopped, then uninstalled via `synopkg uninstall CloudSync`
- Hibernation debug disabled via `synosetkeyvalue enable_hibernation_debug no`
- SynoFinder package stopped to reduce disk I/O
- `syno_hibernate_debug_tool` does not exist — correct command is `synosetkeyvalue` + manual process start
- After disabling debug and CloudSync: disk write counters show slower growth (visible in comparison)
- System log: `/var/log/messages` (requires `sudo` to read)

## CloudSync Errors (from /var/log/messages)

```
# Dropbox
[ERROR] dropbox-wrapper.cpp: Failed to refresh token,
  err '{"error": "invalid_request", "error_description": "\"refresh_token\": must not be empty"}'

# OneDrive  
[ERROR] onedrive-v1-proto.cpp: Error: http code (400),
  error message (The provided value for the input parameter 'refresh_token' or 'assertion' is not valid.),
  error code (invalid_grant)
```

## Entities Mentioned

- [[Synology DS212j]] — device
- [[DSM]] — OS and package management
- [[CloudSync]] — package uninstalled; was causing extra disk I/O with failed auth retries

## Concepts Covered

- [[HDD Hibernation]] — debug disabled to reduce self-inflicted disk writes
