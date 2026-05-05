---
tags: [home-assistant, custom-integration, python, switch, entity]
sources: [Creating a custom component for home assistant.md]
created: 2026-05-05
updated: 2026-05-05
---

# Creating a Custom Component for Home Assistant (TheStaticTurtle)

**Source:** `Creating a custom component for home assistant.md`
**Author:** TheStaticTurtle
**URL:** https://blog.thestaticturtle.fr/creating-a-custom-component-for-homeassistant/
**Type:** blog article

## Summary

Beginner-friendly walkthrough of creating a custom component for a 433MHz RF switch board (open433). Uses synchronous, non-async approach. Good contrast to modern async patterns. Shows integration lifecycle with HA start/stop events, data sharing via `hass.data[DOMAIN]`, and a `SwitchEntity` platform.

## Key Claims

- Create `custom_components/<domain>/` in HA config directory
- `manifest.json` requires: `domain`, `name`, `documentation`, `requirements`, `codeowners`
- Constants defined in `__init__.py`: `DOMAIN`, config key names, `CONFIG_SCHEMA`
- `CONFIG_SCHEMA` wraps `DOMAIN` key: `vol.Schema({DOMAIN: vol.Schema({...})}, extra=vol.ALLOW_EXTRA)`
- Synchronous `setup(hass, config)` function — older pattern, prefer `async_setup` or config entries
- Store shared objects in `hass.data[DOMAIN]` for use by platform files
- HA lifecycle events: `EVENT_HOMEASSISTANT_START`, `EVENT_HOMEASSISTANT_STOP` — listen with `hass.bus.listen_once()`
- Platform file (`switch.py`) extends `SwitchEntity` — must implement `name`, `is_on`, `turn_on`, `turn_off`
- `should_poll = False` when the entity updates itself via callbacks (push model)
- Call `self.schedule_update_ha_state()` to push state change to HA after turn_on/turn_off
- `PLATFORM_SCHEMA.extend({...})` in platform file adds platform-specific config keys
- `setup_platform(hass, config, add_entities, discovery_info=None)` — synchronous platform setup

## Concepts Covered

- [[Custom Component Structure]] — basic file layout
- [[manifest.json]] — required fields
- [[Platform Schema (Voluptuous)]] — CONFIG_SCHEMA, PLATFORM_SCHEMA
- [[Entity Types]] — SwitchEntity, synchronous pattern
- [[Async Patterns]] — contrast: synchronous setup vs async
