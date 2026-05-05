---
tags: [home-assistant, custom-integration, entity, sensor, switch, camera, python]
sources: [Building a Home Assistant Custom Component Part 1 Project Structure and Basics.md, Creating a custom component for home assistant.md, Entities examples from old project.md]
created: 2026-05-05
updated: 2026-05-05
---

# Entity Types

Entities are the building blocks of Home Assistant — each one represents a single piece of state (a sensor reading, a switch, a camera feed). Custom components create entities by subclassing HA base classes.

## Modern _attr_* Pattern

Since HA 2021.4, you can use `_attr_*` class attributes instead of defining properties. This is now the **preferred** approach:

```python
class MySensor(SensorEntity):
    _attr_name = "My Sensor"
    _attr_native_unit_of_measurement = "°C"
    _attr_device_class = SensorDeviceClass.TEMPERATURE
    _attr_state_class = SensorStateClass.MEASUREMENT
    _attr_icon = "mdi:thermometer"
```

No need to define `name`, `unit_of_measurement`, etc. as properties.

## SensorEntity

```python
from homeassistant.components.sensor import SensorEntity, SensorDeviceClass, SensorStateClass

class MySensor(SensorEntity):
    _attr_name = "Temperature"
    _attr_native_unit_of_measurement = "°C"
    _attr_device_class = SensorDeviceClass.TEMPERATURE
    _attr_state_class = SensorStateClass.MEASUREMENT

    def __init__(self, config):
        self._config = config
        self._value = None

    @property
    def native_value(self):
        return self._value

    async def async_update(self) -> None:
        self._value = await fetch_temperature(self._config)
```

> **Deprecation note:** Old tutorials use `state` property and `device_state_attributes`. In modern HA, use `native_value` and `extra_state_attributes` (or `_attr_extra_state_attributes`).

## SwitchEntity

```python
from homeassistant.components.switch import SwitchEntity

class MySwitch(SwitchEntity):
    _attr_name = "My Switch"

    def __init__(self):
        self._is_on = False

    @property
    def is_on(self) -> bool:
        return self._is_on

    async def async_turn_on(self, **kwargs) -> None:
        await device.turn_on()
        self._is_on = True

    async def async_turn_off(self, **kwargs) -> None:
        await device.turn_off()
        self._is_on = False
```

Use `should_poll = False` when the device pushes state updates (call `self.async_write_ha_state()` from callbacks).

## BinarySensorEntity

```python
from homeassistant.components.binary_sensor import BinarySensorEntity, BinarySensorDeviceClass

class MyBinarySensor(BinarySensorEntity):
    _attr_name = "Motion"
    _attr_device_class = BinarySensorDeviceClass.MOTION

    @property
    def is_on(self) -> bool:
        return self._state
```

## Camera

```python
from homeassistant.components.camera import Camera

class MyCamera(Camera):
    _attr_name = "My Camera"

    async def async_camera_image(self, width=None, height=None) -> bytes | None:
        return await fetch_image()
```

Multi-inheritance with `CoordinatorEntity` is possible but requires explicit `__init__` calls for each parent.

## CoordinatorEntity Pattern

For coordinator-based entities (see [[Data Update Coordinator]]):

```python
from homeassistant.helpers.update_coordinator import CoordinatorEntity

class MySensor(CoordinatorEntity, SensorEntity):
    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._attr_name = "My Sensor"

    @property
    def native_value(self):
        return self.coordinator.data["temperature"]
```

## Device Info

Link entities to a logical device (shows up in device registry):

```python
from homeassistant.helpers.device_registry import DeviceInfo

@property
def device_info(self) -> DeviceInfo:
    return DeviceInfo(
        identifiers={(DOMAIN, self._device_id)},
        name="My Device",
        manufacturer="Acme",
        model="v1.0",
    )
```

All entities with the same `identifiers` are grouped under the same device card in HA UI.

## Unique ID

Set `unique_id` to allow entities to be renamed/customized in HA UI:

```python
@property
def unique_id(self) -> str:
    return f"{DOMAIN}_{self._device_id}"
```

Without a `unique_id`, the entity cannot be customized through the UI.

## Availability

```python
@property
def available(self) -> bool:
    return self._last_update_successful
```

When `available = False`, HA shows the entity as "Unavailable" and stops polling.

## Update Methods

| Method | When to use |
|---|---|
| `async_update()` | Async polling (preferred) |
| `update()` | Synchronous polling (legacy) |
| `async_write_ha_state()` | Push update from callback (no polling) |
| `schedule_update_ha_state()` | Push update from sync callback |

## Platform Enum

Use `Platform` enum instead of string literals:

```python
from homeassistant.const import Platform
PLATFORMS = [Platform.SENSOR, Platform.SWITCH, Platform.CAMERA]
```

## Related

- [[Async Patterns]]
- [[Data Update Coordinator]]
- [[Custom Component Structure]]
- [[SCAN_INTERVAL]]
