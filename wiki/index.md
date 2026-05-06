# Index

Master catalog of all wiki pages. Updated on every ingest.

## Sources

- [[Building a HA Custom Component Part 1: Project Structure and Basics]] — Project structure, manifest.json, platform schema, sensor entity, async_update
- [[Building a HA Custom Component Part 2: Unit Testing and CI]] — pytest-homeassistant-custom-component, hassfest, GitHub Actions, pre-commit
- [[Building a HA Custom Component Part 3: Config Flow]] — UI-based config, multi-step flow, strings.json, translations
- [[Building a HA Custom Component Part 4: Options Flow]] — Post-install reconfiguration, OptionsFlowHandler, update listener
- [[Building a HA Custom Component Part 5: Debugging]] — VS Code devcontainer, breakpoints, local HA instance
- [[Creating a Custom Component for Home Assistant (TheStaticTurtle)]] — Beginner walkthrough, synchronous setup, SwitchEntity
- [[HA Example Custom Config Repository]] — Official HA example custom components reference repo
- [[The Great Migration — HA Developer Blog]] — HA 0.87 file structure change: light/hue.py → hue/light.py
- [[Contributing to Home Assistant]] — PR process, dev branch, issue tracker
- [[Camera Archiver — Init Code Examples]] — Pipeline architecture, voluptuous schemas, Platform enum
- [[Camera Archiver — Entity Code Examples]] — CoordinatorEntity, _attr_* pattern, event-driven sensors

## Entities

- [[Aaron Godfrey]] — Author of the 5-part custom component tutorial series, cookiecutter template
- [[GitHub]] — Web platform / REST API used as data source in Aaron Godfrey's tutorial
- [[Paulus Schoutsen]] — HA founder, authored The Great Migration (0.87 file structure change)
- [[HACS]] — Home Assistant Community Store, de-facto distribution platform for custom integrations
- [[Camera Archiver]] — Sergey's personal HA integration for camera footage archiving (pipeline architecture)

## Concepts

- [[Custom Component Structure]] — Required files, directory layout, manifest.json, platform files, setup patterns
- [[manifest.json]] — Integration metadata: domain, requirements, iot_class, config_flow, codeowners
- [[Config Flow]] — UI-based integration setup: steps, validation, entry creation, translations
- [[Options Flow]] — Post-install reconfiguration without re-entering credentials
- [[Entity Types]] — SensorEntity, SwitchEntity, Camera, BinarySensorEntity, _attr_* pattern, device_info
- [[Async Patterns]] — async_setup_entry, async_forward_entry_setups, aiohttp session, executor jobs
- [[Data Update Coordinator]] — Shared polling coordinator for multi-entity integrations
- [[Unit Testing HA]] — pytest fixtures, MockConfigEntry, testing config/options flows, CI setup
- [[Debugging Devcontainer]] — VS Code + Docker devcontainer, breakpoints, logging config
- [[SCAN_INTERVAL]] — Module-level polling interval constant for platform files
- [[The Great Migration]] — HA 0.87 architectural change establishing current file layout convention
- [[GitHub Actions CI]] — hassfest + Python CI workflows for custom component validation
- [[Platform Schema (Voluptuous)]] — PLATFORM_SCHEMA / CONFIG_SCHEMA YAML config validation
- [[Pre-commit Hooks]] — Local code quality checks: black, flake8, mypy, isort, bandit

## Synthesis

- [[Sync vs Async Setup]] — Side-by-side comparison of old sync and modern async component patterns
