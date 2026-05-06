---
tags: [home-assistant, custom-integration, python, async, patterns, comparison]
sources: [Creating a custom component for home assistant.md, Building a Home Assistant Custom Component Part 1 Project Structure and Basics.md, Code examples from Camera Archiver (old project).md]
created: 2026-05-06
updated: 2026-05-06
---

# Sync vs Async Component Setup

Comparison of the two approaches for setting up HA custom component platforms: the older synchronous pattern and the modern async pattern.

## Side-by-Side Comparison

| Aspect | Synchronous (old) | Async (modern) |
|---|---|---|
| Entry point | `setup_platform(hass, config, add_entities, discovery_info)` | `async_setup_entry(hass, entry, async_add_entities)` |
| Config source | `configuration.yaml` via [[Platform Schema (Voluptuous)]] | UI via [[Config Flow]] |
| Setup function | `setup(hass, config)` in `__init__.py` | `async_setup_entry(hass, entry)` in `__init__.py` |
| Entity update | `update()` — blocking | `async_update()` — non-blocking |
| Data sharing | `hass.data[DOMAIN]` | `entry.runtime_data` or `hass.data[DOMAIN][entry.entry_id]` |
| Blocking calls | Direct I/O allowed | Must use `hass.async_add_executor_job()` |
| Source | [[Creating a Custom Component for Home Assistant (TheStaticTurtle)]] | [[Building a HA Custom Component Part 1: Project Structure and Basics]] |

## Synchronous Pattern (Older)

```python
# __init__.py
def setup(hass, config):
    hass.data[DOMAIN] = MyClient(config[DOMAIN][CONF_HOST])
    return True

# sensor.py
def setup_platform(hass, config, add_entities, discovery_info=None):
    client = hass.data[DOMAIN]
    add_entities([MySensor(client)])

class MySensor(Entity):
    def update(self):
        self._state = self._client.fetch()   # blocking I/O — freezes event loop!
```

**When to use:** Never in new code. Only when maintaining very old components that have no config entries.

## Async Pattern (Modern)

```python
# __init__.py
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    client = MyClient(entry.data[CONF_HOST])
    await client.async_connect()
    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = client
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True

# sensor.py
async def async_setup_entry(hass, entry, async_add_entities):
    client = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([MySensor(client)])

class MySensor(SensorEntity):
    async def async_update(self):
        self._attr_native_value = await self._client.async_fetch()
```

## Key Differences to Watch

1. **Blocking I/O in async context** — if a library doesn't support async, wrap it:
   ```python
   result = await hass.async_add_executor_job(blocking_lib.fetch)
   ```

2. **Entry lifecycle** — async setup must have a matching `async_unload_entry` to clean up:
   ```python
   async def async_unload_entry(hass, entry):
       unloaded = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
       if unloaded:
           hass.data[DOMAIN].pop(entry.entry_id)
       return unloaded
   ```

3. **`async_add_entities` vs `add_entities`** — use the async variant in async context. The `update_before_add=True` parameter triggers an immediate fetch on startup.

## Recommendation

Always use the **async pattern** for new components. The synchronous pattern:
- Blocks the HA event loop during I/O
- Doesn't support config entries (no UI setup)
- Cannot be reloaded without restarting HA

## Related

- [[Async Patterns]] — detailed async utilities and patterns
- [[Config Flow]] — the UI-based config system that async pattern uses
- [[Entity Types]] — `_attr_*` pattern works with both but is async-native
- [[Custom Component Structure]] — file layout for both patterns
