---
tags: [home-assistant, custom-integration, python, architecture, manifest]
sources: [Building a Home Assistant Custom Component Part 1 Project Structure and Basics.md, Building a Home Assistant Custom Component Part 3 Config Flow.md, Creating a custom component for home assistant.md, The Great Migration  Home Assistant Developer Docs.md, Code examples from Camera Archiver (old project).md]
created: 2026-05-05
updated: 2026-05-05
---

# Custom Component Structure

A Home Assistant custom component lives inside the HA config directory. Understanding the required files and their roles is the first step to building a working integration.

## Directory Layout

```
<config>/
└── custom_components/
    └── <domain>/
        ├── __init__.py          # required — integration entry point
        ├── manifest.json        # required — integration metadata
        ├── const.py             # recommended — all constants (DOMAIN, keys, etc.)
        ├── config_flow.py       # required for UI setup (config_flow: true)
        ├── strings.json         # required for config flow — field labels and errors
        ├── sensor.py            # platform file (one per entity type)
        ├── switch.py
        ├── camera.py
        ├── binary_sensor.py
        └── translations/
            └── en.json          # copy of strings.json for English
```

After [[The Great Migration]] (HA 0.87), the convention is `<domain>/sensor.py` — NOT `sensor/<domain>.py`.

## manifest.json

Every integration must have this file. Minimum required fields:

```json
{
  "domain": "my_integration",
  "name": "My Integration",
  "version": "1.0.0",
  "documentation": "https://github.com/you/my_integration",
  "requirements": [],
  "codeowners": ["@your_github_username"],
  "iot_class": "cloud_polling",
  "config_flow": true
}
```

Key fields:
- `domain` — unique short name, lowercase with underscores, cannot be changed after release
- `requirements` — list of pip packages with pinned versions: `["gidgethub[aiohttp]==4.1.1"]`
- `iot_class` — describes how the integration communicates: `cloud_polling`, `cloud_push`, `local_polling`, `local_push`, `assumed_state`
- `config_flow: true` — enables "Add Integration" button in UI
- `version` — required for HACS-distributed components

See [[manifest.json]] for full field reference.

## __init__.py

The integration entry point. For modern config-entry-based integrations:

```python
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant

PLATFORMS = [Platform.SENSOR, Platform.SWITCH]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up from a config entry (UI configuration)."""
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = entry.data
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)
    return unload_ok
```

> **Modern API note:** Use `async_forward_entry_setups` (plural, awaitable) instead of the older `async_create_task(async_forward_entry_setup(...))` pattern. The old pattern from the 2020 tutorial is deprecated.

For YAML-based setup (legacy), also add `async_setup(hass, config)`.

## Platform Files (sensor.py, switch.py, etc.)

Each platform file must define `async_setup_entry`:

```python
async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up sensors from a config entry."""
    config = hass.data[DOMAIN][config_entry.entry_id]
    entities = [MySensor(config)]
    async_add_entities(entities, update_before_add=True)
```

For YAML-based platforms, use `async_setup_platform` instead.

## const.py Pattern

```python
DOMAIN = "my_integration"
CONF_SOME_KEY = "some_key"
DEFAULT_SCAN_INTERVAL = 10  # minutes
```

Never hardcode the domain string in multiple places — always import from `const.py`.

## config_flow.py

Required when `config_flow: true`. See [[Config Flow]] for full details.

## strings.json and translations/

```json
{
  "config": {
    "step": {
      "user": {
        "title": "Set up My Integration",
        "data": {
          "api_key": "API Key"
        }
      }
    },
    "error": {
      "auth": "Invalid API key."
    }
  }
}
```

Copy to `translations/en.json`. Add other languages as `translations/<lang_code>.json`.

## Scaffolding Tools

- **cookiecutter template** by [[Aaron Godfrey]]: `cookiecutter https://github.com/boralyl/cookiecutter-homeassistant-component`
- Generates project skeleton with pre-commit config, test structure, GitHub Actions workflows

## Key Rules

1. Always create at least an empty `__init__.py` in the domain folder
2. Use relative imports: `from . import DOMAIN` or `from .const import DOMAIN`
3. All platforms must live in the same folder as `__init__.py`
4. Use `Platform` enum from `homeassistant.const` instead of string literals for platform names
5. Store per-entry data in `hass.data[DOMAIN][entry.entry_id]` to support multiple instances

## Related Concepts

- [[manifest.json]]
- [[Config Flow]]
- [[Options Flow]]
- [[Entity Types]]
- [[Async Patterns]]
- [[The Great Migration]]
