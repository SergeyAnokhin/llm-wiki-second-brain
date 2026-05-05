---
tags: [home-assistant, custom-integration, python, polling]
sources: [Building a Home Assistant Custom Component Part 1 Project Structure and Basics.md]
created: 2026-05-05
updated: 2026-05-05
---

# SCAN_INTERVAL

`SCAN_INTERVAL` is the module-level constant that controls how often HA calls `async_update()` on entities in a platform. HA looks for it by name in the platform's module.

## Usage

```python
from datetime import timedelta
SCAN_INTERVAL = timedelta(minutes=10)
```

Place this at the top of your platform file (e.g. `sensor.py`).

## Behavior

- HA polls `async_update` every `SCAN_INTERVAL`
- If not defined, HA uses a default (30 seconds for most platforms)
- `async_add_entities(entities, update_before_add=True)` triggers an immediate update at startup regardless of `SCAN_INTERVAL`
- Without `update_before_add=True`, entities show "Unknown" state until the first scheduled poll

## When NOT to Use

`SCAN_INTERVAL` (and `async_update`) is the **simple polling approach**. For production integrations with multiple entities sharing data from the same source, prefer [[Data Update Coordinator]] — it fetches data once and distributes it, avoids redundant API calls, and handles errors centrally.

## Related

- [[Data Update Coordinator]] — preferred alternative for multi-entity setups
- [[Entity Types]] — async_update method
- [[Async Patterns]]
