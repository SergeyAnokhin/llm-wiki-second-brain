---
tags: [home-assistant, custom-integration, python, coordinator, entity]
sources: [Entities examples from old project.md]
created: 2026-05-05
updated: 2026-05-05
---

# Data Update Coordinator

`DataUpdateCoordinator` is the preferred pattern for HA integrations that poll external data sources. It fetches data once and distributes it to all related entities — preventing N separate API calls when N entities all need the same data.

## When to Use

- Multiple entities share data from the same API endpoint
- You want centralized error handling and backoff logic
- You want HA to manage the polling schedule automatically

For single-entity integrations, a simple `async_update` method may be sufficient.

## Basic Usage

```python
from datetime import timedelta
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
import logging

_LOGGER = logging.getLogger(__name__)

class MyCoordinator(DataUpdateCoordinator):
    def __init__(self, hass, client):
        super().__init__(
            hass,
            _LOGGER,
            name="My Integration",
            update_interval=timedelta(minutes=5),
        )
        self._client = client

    async def _async_update_data(self):
        """Fetch data from API. Called on every update interval."""
        try:
            return await self._client.get_all_data()
        except ApiAuthError as err:
            raise ConfigEntryAuthFailed from err  # triggers reauthentication
        except ApiError as err:
            raise UpdateFailed(f"Error fetching data: {err}") from err
```

## Setup in async_setup_entry

```python
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    client = MyAPIClient(entry.data["api_key"])
    coordinator = MyCoordinator(hass, client)
    
    # Fetch initial data — raises ConfigEntryNotReady if it fails
    await coordinator.async_config_entry_first_refresh()
    
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = coordinator
    
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True
```

`async_config_entry_first_refresh()` raises `ConfigEntryNotReady` on failure — HA will retry setup automatically.

## CoordinatorEntity

Entities that use a coordinator should extend `CoordinatorEntity`:

```python
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.components.sensor import SensorEntity

class MySensor(CoordinatorEntity, SensorEntity):
    def __init__(self, coordinator: MyCoordinator, sensor_id: str):
        super().__init__(coordinator)
        self._sensor_id = sensor_id
        self._attr_unique_id = f"{DOMAIN}_{sensor_id}"
        self._attr_name = f"My Sensor {sensor_id}"

    @property
    def native_value(self):
        """Return value from coordinator's data."""
        return self.coordinator.data[self._sensor_id]["value"]

    @property
    def available(self) -> bool:
        return super().available and self._sensor_id in self.coordinator.data
```

`CoordinatorEntity` automatically:
- Subscribes to coordinator updates
- Calls `async_write_ha_state()` when data changes
- Sets `available = False` when coordinator raises `UpdateFailed`

## In Platform Setup

```python
async def async_setup_entry(hass, config_entry, async_add_entities):
    coordinator = hass.data[DOMAIN][config_entry.entry_id]
    sensors = [MySensor(coordinator, sid) for sid in coordinator.data.keys()]
    async_add_entities(sensors)
```

Note: no `update_before_add=True` needed — coordinator already fetched data in `async_config_entry_first_refresh`.

## _handle_coordinator_update

Override to react to coordinator updates with custom logic:

```python
@callback
def _handle_coordinator_update(self) -> None:
    """Called when coordinator fetches new data."""
    if not self.coordinator.data:
        return
    # do custom processing here
    self._processed = process(self.coordinator.data)
    super()._handle_coordinator_update()  # calls async_write_ha_state()
```

## Error Handling

| Exception | Effect |
|---|---|
| `UpdateFailed` | Entity shows as "Unavailable" until next successful update |
| `ConfigEntryAuthFailed` | Triggers re-authentication flow |
| `ConfigEntryNotReady` | Delays config entry setup (HA retries) |

## Manual Refresh

Trigger an immediate refresh (e.g. after a user action):

```python
await coordinator.async_request_refresh()
```

## Camera Archiver Pattern

[[Camera Archiver]] uses a different pattern — instead of `DataUpdateCoordinator`, it uses a custom event-driven `ConnectorSensor` that subscribes to a `SensorConnector` object. The connector pushes `EventObject` subclasses (FileEventObject, RepositoryEventObject, etc.) to registered callbacks. This is suitable for push-based data sources where polling is not ideal.

## Related

- [[Entity Types]] — CoordinatorEntity, _attr_* pattern
- [[Async Patterns]] — async_setup_entry
- [[SCAN_INTERVAL]] — alternative manual polling
