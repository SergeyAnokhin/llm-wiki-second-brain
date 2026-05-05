---
tags: [home-assistant, custom-integration, debugging, vscode, devcontainer]
sources: [Building a Home Assistant Custom Component Part 5 Debugging.md]
created: 2026-05-05
updated: 2026-05-05
---

# Building a HA Custom Component Part 5: Debugging

**Source:** `Building a Home Assistant Custom Component Part 5 Debugging.md`
**Author:** [[Aaron Godfrey]]
**Published:** 2020-12-28
**URL:** https://aarongodfrey.dev/home%20automation/building_a_home_assistant_custom_component_part_5/
**Type:** tutorial article (part 5 of 5)

## Summary

Final part of the series. Covers using the VS Code devcontainer from the HA core repository to run and debug a custom component locally without touching the production HA instance.

## Key Claims

- HA core repo ships a devcontainer — use it instead of modifying production instance
- Prerequisites: VS Code + Docker + Dev Containers extension
- Clone `home-assistant/core`, open in VS Code — it detects and offers to open in devcontainer (first build takes a few minutes)
- Copy custom component to `<cloned-core>/config/custom_components/<domain>/`; docker creates files owned by root, use built-in terminal for correct permissions
- Config flow components need no `configuration.yaml` entry — configure via UI at `http://localhost:8123`
- Run panel: `Ctrl+Shift+D` → select "Home Assistant" → click green triangle to start debugger
- Logs appear in Terminal panel; HA UI available at `http://localhost:8123`
- Debug toolbar: Pause/Resume, Step over, Step into, Step out, Restart, Stop
- Set breakpoints by clicking to the left of line numbers — red dot appears
- When breakpoint is hit: program pauses, local/global variables visible in Run panel
- Resume with the continue button in debug toolbar
- Restart HA after Python code changes using the Restart button

## Entities Mentioned

- [[Aaron Godfrey]] — author

## Concepts Covered

- [[Debugging Devcontainer]] — full setup and usage guide
- [[Custom Component Structure]] — where to place files in devcontainer
