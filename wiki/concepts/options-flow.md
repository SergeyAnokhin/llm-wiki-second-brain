---
tags: [home-assistant, custom-integration, options-flow, config-flow, python]
sources: [Building a Home Assistant Custom Component Part 4 Options Flow.md]
created: 2026-05-05
updated: 2026-05-05
---

# Options Flow

Options Flow lets users reconfigure an integration after the initial setup — without re-entering credentials or creating a new config entry. Accessed via Settings → Integrations → (your integration card) → Configure / Options.

Use it for settings that can change over time: adding/removing entities, adjusting polling intervals, toggling features.

## Enabling Options Flow

Add a static method to your config flow class:

```python
@staticmethod
@callback
def async_get_options_flow(config_entry):
    return OptionsFlowHandler(config_entry)
```

## OptionsFlowHandler

```python
from homeassistant import config_entries
import voluptuous as vol

class OptionsFlowHandler(config_entries.OptionsFlow):
    def __init__(self, config_entry: config_entries.ConfigEntry) -> None:
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        errors = {}
        if user_input is not None:
            if not errors:
                return self.async_create_entry(title="", data=user_input)
        
        schema = vol.Schema({
            vol.Optional("poll_interval",
                         default=self.config_entry.options.get("poll_interval", 10)): int,
        })
        return self.async_show_form(step_id="init", data_schema=schema, errors=errors)
```

Key differences from Config Flow:
- Always has a single step named `init`
- `async_create_entry(title="", data=...)` — empty title, data goes to `config_entry.options`
- Access previous values from `self.config_entry.options.get("key", default)`

## Update Listener

To react when options change, register a listener in `async_setup_entry`:

```python
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    hass_data = dict(entry.data)
    unsub = entry.add_update_listener(options_update_listener)
    hass_data["unsub_options_update_listener"] = unsub
    hass.data[DOMAIN][entry.entry_id] = hass_data
    ...
    return True

async def options_update_listener(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Called when options change — reload the entry to apply new options."""
    await hass.config_entries.async_reload(entry.entry_id)
```

**Important:** The listener only fires if the submitted options differ from the previously stored ones.

Store the unsubscribe function so it can be cleaned up during `async_unload_entry`:

```python
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    hass.data[DOMAIN][entry.entry_id]["unsub_options_update_listener"]()
    ...
```

## Using Options in Platform Setup

In `sensor.py` (or any platform), merge options with config data:

```python
async def async_setup_entry(hass, config_entry, async_add_entities):
    config = dict(hass.data[DOMAIN][config_entry.entry_id])
    if config_entry.options:
        config.update(config_entry.options)
    # now config has both initial data and updated options
```

## Managing Entities via Options Flow

To allow adding/removing entities in the options flow:

```python
from homeassistant.helpers.entity_registry import async_get as async_get_entity_registry

async def async_step_init(self, user_input=None):
    entity_registry = async_get_entity_registry(self.hass)
    entries = entity_registry.entities.get_entries_for_config_entry_id(
        self.config_entry.entry_id
    )
    all_entities = {e.entity_id: e.original_name for e in entries}
    
    schema = vol.Schema({
        vol.Optional("entities", default=list(all_entities.keys())):
            cv.multi_select(all_entities),
    })
    ...
```

To remove an entity from the registry:
```python
entity_registry.async_remove(entity_id)
```

> **API note:** `async_get_registry` (used in the 2020 tutorial) is deprecated. Use `async_get` from `homeassistant.helpers.entity_registry`.

## strings.json for Options

Options strings go under a separate `"options"` key:

```json
{
  "config": { ... },
  "options": {
    "step": {
      "init": {
        "title": "Options",
        "data": { "poll_interval": "Poll interval (minutes)" }
      }
    },
    "error": {
      "invalid_value": "Value must be positive."
    }
  }
}
```

## Related

- [[Config Flow]] — initial configuration
- [[Custom Component Structure]]
- [[Unit Testing HA]] — testing options flow
