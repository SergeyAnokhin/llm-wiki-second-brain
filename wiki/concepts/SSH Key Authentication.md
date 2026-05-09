---
tags: [ssh, security, authentication, concept]
sources: [Расследование проблемы сна Synology DS212j.md, ssh connection verbosity.md]
created: 2026-05-09
updated: 2026-05-09
---

# SSH Key Authentication

SSH public-key authentication — passwordless login to a remote host using a cryptographic key pair.
The private key stays on the client; the public key is registered on the server.

## Key Pair Used

| Parameter | Value |
|---|---|
| Key name | `claude-synology` |
| Algorithm | ED25519 |
| Client fingerprint | `SHA256:R9EP0Q0aKchVLQs8mlUFsOkjMafzK+p4WUIrlu9/SvU` |
| Server host key | ED25519 `SHA256:iOki/McmfxwUzITQ3Mlr8CiyXeYrUTBwmh0yO26fGfk` |

This key was generated and configured during the [[HDD Hibernation]] investigation on [[Synology DS212j]].

## Setup on Synology

Public key added to `~/.ssh/authorized_keys` on the NAS (first user account).
[[DSM]] must have SSH enabled (port 22, SFTP port 22).

## Connection Details

- **Client:** OpenSSH 10.0p2
- **Server:** OpenSSH 6.8p1-hpn14v6 (old DSM 6.x version)
- **Key exchange:** Curve25519-sha256
- **Cipher:** chacha20-poly1305@openssh.com
- **Target host:** 192.168.1.99 (user: `firstuser`)

## Related Pages

- [[Synology DS212j]] — the SSH server
- [[DSM]] — OS that manages SSH access on the NAS
