---
tags: [home-assistant, custom-integration, python, async, asyncio]
sources: [Building a Home Assistant Custom Component Part 1 Project Structure and Basics.md, Building a Home Assistant Custom Component Part 3 Config Flow.md, Code examples from Camera Archiver (old project).md]
created: 2026-05-05
updated: 2026-05-05
---

# Async Patterns

Home Assistant is built on Python's `asyncio`. Custom components must follow async conventions to integrate correctly. Blocking the event loop (even briefly) can freeze the entire HA instance.

## Core Rule

**Never use blocking I/O in the async event loop.** If a library is synchronous (blocking), run it in an executor:

```python
result = await hass.async_add_executor_job(blocking_library.fetch_data, arg1)
```

## Setup Entry Points

### async_setup (YAML-based, legacy)

Called when HA loads the integration from `configuration.yaml`:

```python
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    # Read config[DOMAIN], store shared objects in hass.data[DOMAIN]
    hass.data.setdefault(DOMAIN, {})
    return True
```

### async_setup_entry (config-entry-based, modern)

Called when HA loads a config entry (from UI or after restart):

```python
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = entry.data
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True
```

> **Modern API:** Use `async_forward_entry_setups` (plural, awaitable). The old pattern `hass.async_create_task(hass.config_entries.async_forward_entry_setup(entry, "sensor"))` is deprecated.

### async_unload_entry

Called when removing/disabling an integration:

```python
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)
    return unload_ok
```

### async_setup_platform (legacy platform setup)

For platforms loaded from YAML (without config entries):

```python
async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    async_add_entities: AddEntitiesCallback,
    discovery_info=None,
) -> None:
    session = async_get_clientsession(hass)
    entities = [MySensor(session, config)]
    async_add_entities(entities, update_before_add=True)
```

### async_setup_entry (platform-level)

For platforms loaded via config entries:

```python
async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    config = hass.data[DOMAIN][config_entry.entry_id]
    async_add_entities([MySensor(config)], update_before_add=True)
```

## update_before_add

```python
async_add_entities(entities, update_before_add=True)
```

`True` means HA calls `async_update()` on each entity immediately during setup, so sensors have data before the first `SCAN_INTERVAL`. Without it, sensors show "Unknown" until the first scheduled update.

## aiohttp Client Session

Never create your own `aiohttp.ClientSession`. Use HA's shared session:

```python
from homeassistant.helpers.aiohttp_client import async_get_clientsession

session = async_get_clientsession(hass)
```

HA manages the session lifecycle — including closing it on shutdown.

## hass.data Pattern

Use `hass.data[DOMAIN][entry.entry_id]` to store per-entry shared objects:

```python
# In async_setup_entry:
hass.data.setdefault(DOMAIN, {})
hass.data[DOMAIN][entry.entry_id] = {
    "client": MyAPIClient(config["api_key"]),
    "unsub_listener": unsub,
}

# In async_unload_entry:
data = hass.data[DOMAIN].pop(entry.entry_id)
data["unsub_listener"]()  # cleanup
```

## HA Event Bus

Listen for HA lifecycle events:

```python
hass.bus.async_listen_once(EVENT_HOMEASSISTANT_START, my_startup_callback)
hass.bus.async_listen_once(EVENT_HOMEASSISTANT_STOP, my_cleanup_callback)
```

## Callbacks and Thread Safety

All HA state mutations must happen on the event loop thread. Use `@callback` decorator for synchronous functions called from async context:

```python
from homeassistant.core import callback

@callback
def handle_event(event):
    entity.async_write_ha_state()
```

## SCAN_INTERVAL

Controls polling frequency when using the `async_update` method:

```python
from datetime import timedelta
SCAN_INTERVAL = timedelta(minutes=10)
```

See [[SCAN_INTERVAL]] for details.

## Related

- [[Entity Types]]
- [[Data Update Coordinator]] — preferred alternative to manual polling
- [[Custom Component Structure]]
- [[SCAN_INTERVAL]]
