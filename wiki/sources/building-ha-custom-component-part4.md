---
tags: [home-assistant, custom-integration, options-flow, config-flow, python]
sources: [Building a Home Assistant Custom Component Part 4 Options Flow.md]
created: 2026-05-05
updated: 2026-05-05
---

# Building a HA Custom Component Part 4: Options Flow

**Source:** `Building a Home Assistant Custom Component Part 4 Options Flow.md`
**Author:** [[Aaron Godfrey]]
**Published:** 2020-12-27
**URL:** https://aarongodfrey.dev/home%20automation/building_a_home_assistant_custom_component_part_4/
**Type:** tutorial article (part 4 of 5)

## Summary

Adds an Options Flow to allow reconfiguring the integration after initial setup — without re-entering credentials. The implementation allows adding and removing GitHub repositories from the config entry via a multi-select + text input form.

## Key Claims

- Add `async_get_options_flow(config_entry)` static method to the config flow class to enable Options button in UI
- `OptionsFlowHandler` extends `config_entries.OptionsFlow`; override `__init__` to receive `config_entry`
- Options flow always uses single step named `init` (unlike config flow which can have multiple steps)
- Use `entity_registry` (`async_get_registry`) to populate multi-select with currently registered entities
- `self.config_entry.options` holds previously saved options — use for default values in the form
- `async_create_entry(title="", data={...})` saves options; data is stored in `config_entry.options` (not `config_entry.data`)
- Options update listener only fires if data actually changed
- Register listener in `async_setup_entry`: `entry.add_update_listener(options_update_listener)` — returns unsubscribe function, store it for cleanup
- Update listener typically calls `hass.config_entries.async_reload(config_entry.entry_id)` to re-setup platforms
- In `async_setup_entry`, merge `config_entry.options` into config dict before creating entities
- Removing entities: call `entity_registry.async_remove(entity_id)` before removing from config data
- Define options strings under `"options"` key in `strings.json` (separate from `"config"`)

## Entities Mentioned

- [[Aaron Godfrey]] — author

## Concepts Covered

- [[Options Flow]] — full implementation
- [[Config Flow]] — relationship between config flow and options flow
- [[Entity Types]] — entity registry queries
- [[Async Patterns]] — update listener, async_reload
