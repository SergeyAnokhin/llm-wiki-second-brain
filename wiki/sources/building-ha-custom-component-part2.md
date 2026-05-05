---
tags: [home-assistant, custom-integration, testing, ci, github-actions, pytest]
sources: [Building a Home Assistant Custom Component Part 2 Unit Testing and Continuous Integration.md]
created: 2026-05-05
updated: 2026-05-05
---

# Building a HA Custom Component Part 2: Unit Testing and CI

**Source:** `Building a Home Assistant Custom Component Part 2 Unit Testing and Continuous Integration.md`
**Author:** [[Aaron Godfrey]]
**Published:** 2020-06-21
**URL:** https://aarongodfrey.dev/home%20automation/building_a_home_assistant_custom_component_part_2/
**Type:** tutorial article (part 2 of 5)

## Summary

Covers adding unit tests and continuous integration to a custom component. Uses `pytest-homeassistant-custom-component` plugin for HA-specific fixtures, GitHub Actions for CI, and pre-commit hooks for code quality.

## Key Claims

- `pytest-homeassistant-custom-component` provides `hass` fixture and `AsyncMock` — install with pip, pytest finds it automatically
- `hass` fixture provides a properly initialized HomeAssistant instance for tests
- Use `AsyncMock` from the plugin to mock async functions (e.g. `github.getitem`)
- Testing config flow: call `hass.config_entries.flow.async_init()` then `async_configure()` and assert on result
- Testing `async_update`: instantiate entity directly, await update, assert `available` and `attrs`
- Reference platinum quality components in HA core for test patterns (Brother, Hue, WLED, etc.)
- **Hassfest** GitHub Action validates component structure on every push — use `home-assistant/actions/hassfest@master`
- Python CI workflow: checkout → setup Python 3.7+ → `pip install -r requirements.test.txt` → `pytest`
- **pre-commit**: runs before each commit — checks pyupgrade, black, codespell, flake8, bandit, isort, JSON, mypy
- `--no-verify` flag bypasses pre-commit (use sparingly)

## Entities Mentioned

- [[Aaron Godfrey]] — author
- [[HACS]] — mentioned via ludeeus who created hassfest action

## Concepts Covered

- [[Unit Testing HA]] — pytest fixtures, AsyncMock, testing patterns
- [[GitHub Actions CI]] — hassfest workflow, python build workflow
- [[Pre-commit Hooks]] — code quality checks before commit
- [[Config Flow]] — testing config flow steps
