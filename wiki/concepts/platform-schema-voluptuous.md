---
tags: [home-assistant, custom-integration, python, config, voluptuous, validation]
sources: [Building a Home Assistant Custom Component Part 1 Project Structure and Basics.md, Creating a custom component for home assistant.md, Code examples from Camera Archiver (old project).md]
created: 2026-05-06
updated: 2026-05-06
---

# Platform Schema (Voluptuous)

HA uses the `voluptuous` library for YAML configuration validation. Two schema objects are commonly extended in custom components: `CONFIG_SCHEMA` (integration-level) and `PLATFORM_SCHEMA` (platform-level).

## PLATFORM_SCHEMA

Used in platform files (`sensor.py`, `switch.py`, etc.) to validate `configuration.yaml` entries for that platform:

```python
import voluptuous as vol
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.helpers import config_validation as cv

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_ACCESS_TOKEN): cv.string,
    vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
    vol.Optional(CONF_PATH, default=[]): vol.All(cv.ensure_list, [cv.string]),
})
```

## CONFIG_SCHEMA

Used in `__init__.py` for integration-level YAML config (older pattern, pre-config-flow):

```python
CONFIG_SCHEMA = vol.Schema({
    DOMAIN: vol.Schema({
        vol.Required(CONF_HOST): cv.string,
        vol.Optional(CONF_PORT, default=8080): cv.port,
    })
}, extra=vol.ALLOW_EXTRA)
```

`extra=vol.ALLOW_EXTRA` is required so HA's own config keys are not rejected.

## Common Voluptuous Helpers

| Helper | Use |
|---|---|
| `vol.Required(key)` | Mandatory config key |
| `vol.Optional(key, default=x)` | Optional with default |
| `cv.string` | Validates as string |
| `cv.boolean` | Validates as bool |
| `cv.port` | Integer 1–65535 |
| `vol.All(...)` | Chain validators |
| `vol.Any(...)` | Accept any of the validators |
| `cv.ensure_list` | Wrap scalar in list |
| `vol.Schema({...})` | Nested schema |

## Advanced: Schema Composition (Camera Archiver Pattern)

Complex integrations can use `.extend()` to build hierarchical schemas:

```python
COMPONENT_DEFAULT = vol.Schema({
    vol.Required(CONF_TYPE): vol.In(COMPONENT_TYPES),
    vol.Optional(CONF_NAME): cv.string,
})

FTP_SCHEMA = COMPONENT_DEFAULT.extend({
    vol.Required(CONF_HOST): cv.string,
    vol.Required(CONF_USERNAME): cv.string,
})
```

## Note on Modern HA

`PLATFORM_SCHEMA` / `CONFIG_SCHEMA` are the **YAML-based** configuration pattern. Modern integrations use [[Config Flow]] (UI-based) instead, which makes YAML schemas unnecessary. Legacy integrations still use them; [[Camera Archiver]] demonstrates advanced composition.

## Related

- [[Config Flow]] — modern UI-based alternative to YAML config
- [[Custom Component Structure]] — where schema definitions live
- [[Camera Archiver]] — example of advanced schema composition
