---
tags: [project, home-assistant, custom-integration, camera, pipeline]
sources: [Code examples from Camera Archiver (old project).md, Entities examples from old project.md]
created: 2026-05-05
updated: 2026-05-05
---

# Camera Archiver

A personal Home Assistant custom integration by Sergey Anokhin for automating camera footage archiving. Copies video/images from cameras (via FTP, MQTT, local directory, IMAP) to archive destinations (FTP, local directory, Elasticsearch) using a configurable pipeline architecture.

**Status:** Old/legacy project (code used as reference examples)

## Architecture

The integration uses a **pipeline** model:
- **Components**: pluggable source/sink nodes (FTP, DIRECTORY, MQTT, IMAP, ELASTICSEARCH, API, SCHEDULER, FILTER, METADATA, SERVICE, SERVICE_CALLER)
- **Sensors**: diagnostic entities (transfer stats, repository stats, timer, last file, last time, camera)
- **Pipelines**: a tree of components connected via `listeners` — data flows from sources through processors to sinks

### Pipeline Example

```yaml
pipelines:
  - id: yi-camera
    component: scheduler        # trigger
    listeners:
      - component: ftp-source   # read from camera
        listeners:
          - component: ftp-dest # write to archive
            listeners:
              - component: elasticsearch  # index metadata
```

## Key Technical Patterns

- `Platform` enum for multi-platform registration (modern HA API)
- `hass.config_entries.async_setup_platforms()` — bulk platform setup
- Dual setup support: `async_setup_entry` (config entries) + `async_setup` (YAML)
- `discovery.async_load_platform()` for dynamic platform loading in YAML mode
- `ConnectorSensor` base class with event-driven updates (no DataUpdateCoordinator)
- `SensorBuilder` factory pattern for sensor construction from config

## Entity Examples

- `ToCamera` — `CoordinatorEntity + Camera` multi-inheritance
- `ActivityBinarySensor` — `BinarySensorEntity` with `_attr_name` shorthand
- `TimerCoordinatorSensor` — polls dynamically, shows countdown to next run
- `TransferCoordinatorSensor` — aggregates file transfer statistics
- `ComponentRepoSensor` / `ComponentFileSensor` — event-driven file tracking

## Sources

- [[Camera Archiver — Init Code Examples]]
- [[Camera Archiver — Entity Code Examples]]

## Related Concepts

- [[Custom Component Structure]]
- [[Entity Types]]
- [[Async Patterns]]
- [[Data Update Coordinator]]
