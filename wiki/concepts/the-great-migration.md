---
tags: [home-assistant, custom-integration, architecture, history]
sources: [The Great Migration  Home Assistant Developer Docs.md]
created: 2026-05-05
updated: 2026-05-05
---

# The Great Migration

The architectural change introduced in Home Assistant 0.87 (February 2019) that defines the current integration file structure standard. Authored by [[Paulus Schoutsen]].

## What Changed

| Before 0.87 | After 0.87 |
|---|---|
| `custom_components/light/hue.py` | `custom_components/hue/light.py` |
| `custom_components/switch/zwave.py` | `custom_components/zwave/switch.py` |

The file **content** did not change — only the **path**.

## Why It Happened

Large integrations like Z-Wave had platforms scattered across many entity component folders:
- `light/zwave.py`
- `switch/zwave.py`
- `cover/zwave.py`
- `binary_sensor/zwave.py`

This made custom component distribution difficult (users had to create files in multiple folders) and made maintenance painful.

## Rules Introduced

1. All integration files live in a single `<domain>/` directory
2. Platform files named after the entity component: `<domain>/sensor.py`, `<domain>/light.py`
3. All platforms must be loaded from the **same source** as the component — no partial overrides
4. If overriding a built-in integration: copy ALL its files, not just the one you want to change
5. Use relative imports (`from . import DATA_BRIDGE`) to avoid breakage during HA core upgrades

## Impact on Custom Components

If you have an old custom component using the pre-0.87 layout, it will not work in modern HA. The fix is straightforward — move platform files into the domain folder.

## Related

- [[Custom Component Structure]] — the current standard this migration established
