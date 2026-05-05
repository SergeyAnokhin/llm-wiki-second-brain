---
tags: [home-assistant, custom-integration, manifest]
sources: [Building a Home Assistant Custom Component Part 1 Project Structure and Basics.md, Creating a custom component for home assistant.md]
created: 2026-05-05
updated: 2026-05-05
---

# manifest.json

Every Home Assistant integration (built-in or custom) must include a `manifest.json` file in its root directory. HA reads this file to understand the integration's metadata, dependencies, and capabilities.

## Required Fields

| Field | Description |
|---|---|
| `domain` | Unique identifier (lowercase, underscores). Cannot be changed after release. |
| `name` | Human-readable display name |
| `version` | Semantic version string (required for HACS) |
| `documentation` | URL to docs or GitHub repo |
| `requirements` | List of pip dependencies with pinned versions |
| `codeowners` | List of GitHub usernames (prefixed with `@`) |

## Optional Fields

| Field | Description |
|---|---|
| `iot_class` | Communication model (see below) |
| `config_flow` | `true` to enable UI setup via Add Integration |
| `dependencies` | Other HA integrations this one depends on |
| `after_dependencies` | Integrations that should load before this one |
| `quality_scale` | `silver`, `gold`, `platinum` |
| `single_config_entry` | `true` if only one instance is allowed |

## iot_class Values

| Value | Meaning |
|---|---|
| `cloud_polling` | Polls a cloud API on a schedule |
| `cloud_push` | Cloud service pushes updates |
| `local_polling` | Polls a local device |
| `local_push` | Local device pushes updates |
| `assumed_state` | State is guessed (e.g. IR remotes) |
| `calculated` | Derived from other entities |

## Requirements

Pin versions to avoid breaking changes:
```json
"requirements": ["gidgethub[aiohttp]==4.1.1", "pyserial==3.4"]
```

For packages with optional async extras, include the extra in brackets.

## Example

```json
{
  "domain": "github_custom",
  "name": "Github Custom",
  "version": "1.0.0",
  "documentation": "https://github.com/boralyl/github-custom-component-tutorial",
  "requirements": ["gidgethub[aiohttp]==4.1.1"],
  "codeowners": ["@boralyl"],
  "iot_class": "cloud_polling",
  "config_flow": true
}
```

## Validation

The [[GitHub Actions CI]] `hassfest` action validates `manifest.json` on every push — catches missing fields, invalid `iot_class` values, etc.

## Related

- [[Custom Component Structure]]
- [[GitHub Actions CI]]
