---
tags: [home-assistant, custom-integration, python, camera-archiver, entity, coordinator, sensor, camera]
sources: [Entities examples from old project.md]
created: 2026-05-05
updated: 2026-05-05
---

# Camera Archiver — Entity Code Examples

**Source:** `Entities examples from old project.md`
**Type:** personal project code (Sergey Anokhin's Camera Archiver integration)

## Summary

Entity implementation examples from Camera Archiver: `camera.py`, `binary_sensor.py`, `sensor.py`. Shows advanced patterns: `CoordinatorEntity` mixin, event-driven sensor updates, multi-inheritance for Camera entities, `_attr_*` shorthand properties.

## Key Claims

### camera.py
- `ToCamera` inherits from both `CoordinatorEntity` and `Camera` — must call `__init__` for each parent explicitly
- `camera_image()` returns `bytes` directly (synchronous); async version `async_camera_image()` is commented out
- `_handle_coordinator_update` callback fires when coordinator has new data — check `enabled` before reading
- `device_info` property returns dict with name, model, etc. — links entity to a device in the device registry

### binary_sensor.py
- `ActivityBinarySensor` extends `BinarySensorEntity`
- Uses `_attr_name` shorthand (no need to define `name` property explicitly) — modern `_attr_*` pattern
- Coordinator-based: different `EventType` (REPOSITORY, READ, SAVE) mapped to different sensor instances

### sensor.py (most complex)
- `ConnectorSensor` base class: holds a `SensorConnector`, adds listener, dispatches events to typed handlers
- `_attr_*` pattern used throughout: `_attr_native_value`, `_attr_extra_state_attributes`, `_attr_icon`, `_attr_unit_of_measurement`
- `set_attr(key, value)` helper: sets or deletes from `_attr_extra_state_attributes` based on truthiness
- Event dispatch: `callback()` uses `isinstance` to route `FileEventObject`, `RepositoryEventObject`, `StartEventObject`, `SetSchedulerEventObject`
- `TimerCoordinatorSensor`: `should_poll = True`, computes time delta to next run dynamically in `state` property
- `TransferCoordinatorSensor`: aggregates file transfer stats (count, size, extensions, last image/video/time)
- `ComponentRepoSensor` / `ComponentFileSensor`: event-driven, extend `TransferCoordinatorSensor`
- `_SENSOR_TYPES` dict maps type string → sensor class — factory pattern for sensor construction
- `SensorBuilder` class wraps construction logic

## Entities Mentioned

- [[Camera Archiver]] — the project

## Concepts Covered

- [[Data Update Coordinator]] — CoordinatorEntity pattern, _handle_coordinator_update
- [[Entity Types]] — _attr_* shorthand, Camera, BinarySensorEntity, SensorEntity
- [[Async Patterns]] — event-driven vs coordinator-driven updates
