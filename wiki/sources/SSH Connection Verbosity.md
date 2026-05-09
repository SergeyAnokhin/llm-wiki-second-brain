---
tags: [ssh, synology, verbose-log, source]
sources: [ssh connection verbosity.md]
created: 2026-05-09
updated: 2026-05-09
---

# SSH Connection Verbosity

**Source:** ssh connection verbosity.md
**Date ingested:** 2026-05-09
**Type:** terminal log (ssh -v output)

## Summary

Verbose SSH handshake log (`ssh -v -i ~/.ssh/claude-synology firstuser@192.168.1.99`)
showing the complete cryptographic negotiation and authentication flow between
a Windows client and [[Synology DS212j]].

## Key Claims

- Client: OpenSSH 10.0p2, OpenSSL 3.2.4 (from Windows/MINGW64)
- Server: OpenSSH 6.8p1-hpn14v6 ([[DSM]] 6.x)
- Key exchange algorithm: `curve25519-sha256@libssh.org`
- Host key: ED25519 `SHA256:iOki/McmfxwUzITQ3Mlr8CiyXeYrUTBwmh0yO26fGfk`
- Client key: `claude-synology` ED25519 `SHA256:R9EP0Q0aKchVLQs8mlUFsOkjMafzK+p4WUIrlu9/SvU`
- Cipher: `chacha20-poly1305@openssh.com` in both directions
- Authentication successful via public key (`publickey`)
- Host was found in `known_hosts` at line 21

## Entities Mentioned

- [[Synology DS212j]] — SSH server
- [[DSM]] — OS providing the SSH service

## Concepts Covered

- [[SSH Key Authentication]] — primary source for key fingerprints and handshake details
