---
tags: [home-assistant, custom-integration, python, camera-archiver, pipeline, voluptuous]
sources: [Code examples from Camera Archiver (old project).md]
created: 2026-05-05
updated: 2026-05-05
---

# Camera Archiver — Init Code Examples

**Source:** `Code examples from Camera Archiver (old project).md`
**Type:** personal project code (Sergey Anokhin's old Camera Archiver integration)

## Summary

`__init__.py` and `configuration.yaml` examples from Camera Archiver — a personal HA integration for automating camera footage archiving. Uses a sophisticated pipeline architecture with pluggable source/sink components. Demonstrates advanced voluptuous schema composition, dual setup modes (YAML + config entries), and multi-platform registration.

## Key Claims

- Uses `Platform` enum (`from homeassistant.const import Platform`) — modern approach, replaces string literals
- `PLATFORMS = [Platform.CAMERA, Platform.SENSOR, Platform.SWITCH, "timer"]` — registers multiple platforms at once
- `hass.config_entries.async_setup_platforms(entry, PLATFORMS)` — modern bulk platform setup (replaces individual `async_forward_entry_setup` calls)
- Dual setup: `async_setup_entry` for config entries, `async_setup` for YAML — supports both modes
- Complex nested voluptuous schemas: `COMPONENT_DEFAULT.extend(...)` for each component type (FTP, MQTT, DIRECTORY, IMAP, API, etc.)
- YAML anchor (`&diskstation_and_elasticsearch_listeners`) and alias (`<<: *...`) reuse in `configuration.yaml`
- `discovery.async_load_platform()` used to load platforms dynamically in YAML setup mode
- Pipeline architecture: each pipeline has components (sources/sinks) connected via a `listeners` tree
- Schema for pipeline supports 5 levels of listener nesting (LEVEL 1-5 schemas)
- Uses `Builder` class pattern to construct components and sensors from config

## Key Architecture Patterns

- **Pipeline tree**: `scheduler → [component → [listener_components...]]`
- **Component types**: FTP, DIRECTORY, MQTT, IMAP, API, ELASTICSEARCH, SCHEDULER, SERVICE, FILTER, METADATA, SERVICE_CALLER
- **Sensor types**: repository_stat, transfer_stat, timer, last_file, last_time, camera

## Entities Mentioned

- [[Camera Archiver]] — the project itself

## Concepts Covered

- [[Custom Component Structure]] — advanced multi-platform setup
- [[Platform Schema (Voluptuous)]] — complex schema composition patterns
- [[Async Patterns]] — async_setup_platforms, async_setup_entry, async_setup
- [[Entity Types]] — Platform enum, multi-platform registration
