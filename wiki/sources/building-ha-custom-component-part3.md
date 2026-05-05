---
tags: [home-assistant, custom-integration, config-flow, python]
sources: [Building a Home Assistant Custom Component Part 3 Config Flow.md]
created: 2026-05-05
updated: 2026-05-05
---

# Building a HA Custom Component Part 3: Config Flow

**Source:** `Building a Home Assistant Custom Component Part 3 Config Flow.md`
**Author:** [[Aaron Godfrey]]
**Published:** 2020-11-23
**URL:** https://aarongodfrey.dev/home%20automation/building_a_home_assistant_custom_component_part_3/
**Type:** tutorial article (part 3 of 5)

## Summary

Adds UI-based configuration to the component via Config Flow. The user can now add and configure the integration through the HA integrations UI instead of `configuration.yaml`. Demonstrates multi-step flow with validation, error handling, and translations.

## Key Claims

- Set `"config_flow": true` in `manifest.json` to enable UI setup
- Create `config_flow.py` extending `ConfigFlow` class
- `async_step_user` is the entry point when user clicks Add Integration — `user_input` is `None` on first call, populated on submit
- Validate input inside the step, set errors on the schema field name, return `self.async_show_form()` with errors on failure
- Store intermediate data in `self.data` and call next step's method to chain steps
- `async_create_entry(title=..., data=...)` finalizes config entry creation
- For variable-length lists (repos), use a looping step with an "Add another" checkbox
- In `__init__.py`, define `async_setup_entry` to forward platform setup: `hass.config_entries.async_forward_entry_setup(entry, "sensor")`
- Store entry data in `hass.data[DOMAIN][entry.entry_id]` to support multiple instances
- `strings.json` defines field labels and error messages; copy to `translations/en.json` for English
- Translation files named with ISO 639-2 language codes (e.g. `nb.json` for Norwegian)
- Hard-refresh browser when modifying config flow files during development — browser caches flow data

## Entities Mentioned

- [[Aaron Godfrey]] — author

## Concepts Covered

- [[Config Flow]] — full implementation: steps, validation, entry creation
- [[manifest.json]] — config_flow field
- [[Async Patterns]] — async_setup_entry pattern
- [[Custom Component Structure]] — config_flow.py, strings.json, translations/
