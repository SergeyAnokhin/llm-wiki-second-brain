---
tags: [home-assistant, custom-integration, architecture, history]
sources: [The Great Migration  Home Assistant Developer Docs.md]
created: 2026-05-05
updated: 2026-05-05
---

# The Great Migration

**Source:** `The Great Migration  Home Assistant Developer Docs.md`
**Author:** [[Paulus Schoutsen]]
**Published:** 2019-02-19
**URL:** https://developers.home-assistant.io/blog/2019/02/19/the-great-migration
**Type:** developer blog post

## Summary

Explains the HA 0.87 architectural migration that changed where integration platform files live. This is why modern integrations use `hue/light.py` instead of `light/hue.py`. Critical background for understanding the current file structure convention.

## Key Claims

- **Before 0.87:** platforms stored as `<entity_component>/<integration>.py` — e.g. `light/hue.py`, `switch/zwave.py`
- **After 0.87:** platforms stored as `<integration>/<entity_component>.py` — e.g. `hue/light.py`, `zwave/switch.py`
- File content stays exactly the same — only the path changed
- Motivation: large integrations (like Z-Wave) had files scattered across many entity component folders — unmaintainable and hard to distribute
- Custom components that override built-in platforms must now use the new `<integration>/light.py` format
- New rule: all platforms loaded from the **same source** as the component — prevents partial overrides
- If you override a built-in integration, copy ALL its files (not just the one you need to change)
- Use relative imports (`from . import DATA_BRIDGE`) to avoid breakage during HA upgrades

## Entities Mentioned

- [[Paulus Schoutsen]] — HA founder, authored this migration

## Concepts Covered

- [[Custom Component Structure]] — current file layout standard and its historical origin
- [[The Great Migration]] — architectural change in HA 0.87
