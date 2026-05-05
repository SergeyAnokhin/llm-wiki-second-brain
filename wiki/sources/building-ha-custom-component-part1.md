---
tags: [home-assistant, custom-integration, python, entity, sensor, manifest]
sources: [Building a Home Assistant Custom Component Part 1 Project Structure and Basics.md]
created: 2026-05-05
updated: 2026-05-05
---

# Building a HA Custom Component Part 1: Project Structure and Basics

**Source:** `Building a Home Assistant Custom Component Part 1 Project Structure and Basics.md`
**Author:** [[Aaron Godfrey]]
**Published:** 2020-06-14
**URL:** https://aarongodfrey.dev/home%20automation/building_a_home_assistant_custom_component_part_1/
**Type:** tutorial article (part 1 of 5)

## Summary

First part of a 5-part tutorial series. Covers building a barebones HA custom component that queries the GitHub API and exposes sensor entities. Goal is to reach at least Silver on the Integration Quality Scale by the end of the series.

Uses a [cookiecutter template](https://github.com/boralyl/cookiecutter-homeassistant-component) to scaffold the project.

## Key Claims

- Custom component lives in `<config>/custom_components/<domain>/`
- `manifest.json` is required — declares domain, name, docs URL, requirements, codeowners, iot_class
- `__init__.py` at minimum must exist; for platform-based integrations the `async_setup` can be removed
- External Python deps go in `requirements` array in manifest.json with pinned versions
- `PLATFORM_SCHEMA.extend({...})` validates configuration.yaml entries for the platform
- `async_setup_platform` is the entry point for platform setup (async version preferred)
- `async_add_entities(sensors, update_before_add=True)` triggers an immediate data fetch on startup
- Entity class extends `homeassistant.helpers.entity.Entity` and must implement `state` property
- `device_state_attributes` returns a dict of extra attributes (note: renamed to `extra_state_attributes` in modern HA)
- `async_update` method is called on `SCAN_INTERVAL` (defined as `datetime.timedelta`)
- Default `SCAN_INTERVAL = timedelta(minutes=10)`

## Entities Mentioned

- [[Aaron Godfrey]] — author of the tutorial series
- [[GitHub]] — API used as data source for the example component

## Concepts Covered

- [[Custom Component Structure]] — file layout, required files
- [[manifest.json]] — integration metadata file
- [[Platform Schema (Voluptuous)]] — config validation
- [[Async Patterns]] — async_setup_platform, async_update
- [[Entity Types]] — SensorEntity basics, state, attributes
- [[SCAN_INTERVAL]] — polling interval mechanism
