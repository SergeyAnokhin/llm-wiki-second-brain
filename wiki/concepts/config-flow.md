---
tags: [home-assistant, custom-integration, config-flow, python, ui]
sources: [Building a Home Assistant Custom Component Part 3 Config Flow.md, Building a Home Assistant Custom Component Part 2 Unit Testing and Continuous Integration.md]
created: 2026-05-05
updated: 2026-05-05
---

# Config Flow

Config Flow is the mechanism that lets users configure a Home Assistant integration through the UI (Settings → Integrations → Add Integration), instead of editing `configuration.yaml` manually. All modern HA integrations should use Config Flow.

## Enabling Config Flow

In `manifest.json`:
```json
{ "config_flow": true }
```

## File: config_flow.py

```python
from homeassistant import config_entries
from homeassistant.data_entry_flow import FlowResult
import voluptuous as vol

AUTH_SCHEMA = vol.Schema({
    vol.Required("api_key"): str,
})

class MyConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow."""
    VERSION = 1

    async def async_step_user(self, user_input=None) -> FlowResult:
        errors = {}
        if user_input is not None:
            try:
                await validate_auth(user_input["api_key"], self.hass)
            except ValueError:
                errors["base"] = "auth"
            if not errors:
                return self.async_create_entry(title="My Integration", data=user_input)
        return self.async_show_form(step_id="user", data_schema=AUTH_SCHEMA, errors=errors)
```

## Flow Lifecycle

1. User clicks "Add Integration" → selects your integration
2. `async_step_user` called with `user_input=None` → return form via `async_show_form`
3. User fills and submits form → `async_step_user` called with `user_input` dict
4. HA validates against `data_schema` first — then your custom validation runs
5. On success: `async_create_entry(title=..., data=...)` → creates `ConfigEntry`, triggers `async_setup_entry`
6. On error: set `errors` dict and return form again

## Multi-Step Flows

For complex flows (e.g., auth step then resource selection step):

```python
async def async_step_user(self, user_input=None):
    if user_input is not None and not errors:
        self.data = user_input
        self.data["repos"] = []
        return await self.async_step_repo()  # advance to next step
    return self.async_show_form(step_id="user", ...)

async def async_step_repo(self, user_input=None):
    if user_input is not None:
        self.data["repos"].append(...)
        if user_input.get("add_another"):
            return await self.async_step_repo()  # loop same step
        return self.async_create_entry(title="...", data=self.data)
    return self.async_show_form(step_id="repo", ...)
```

## Error Handling

Errors are keyed by field name or `"base"` for general errors:
```python
errors["base"] = "auth"          # general error
errors["api_key"] = "invalid"    # field-level error
```

Error keys map to messages in `strings.json`.

## strings.json Structure

```json
{
  "config": {
    "step": {
      "user": {
        "title": "Set Up Integration",
        "data": { "api_key": "API Key" },
        "description": "Enter your API credentials."
      }
    },
    "error": {
      "auth": "Invalid API key. Please check and try again.",
      "invalid_path": "Path must be in format user/repo-name."
    },
    "abort": {
      "already_configured": "Integration is already configured."
    }
  }
}
```

Copy `strings.json` to `translations/en.json`. Add other languages as `translations/<iso_639_2>.json`.

## Setting Up Platforms from Config Entry

In `__init__.py`:

```python
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = entry.data
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True
```

In `sensor.py`:

```python
async def async_setup_entry(hass, config_entry, async_add_entities):
    config = hass.data[DOMAIN][config_entry.entry_id]
    async_add_entities([MySensor(config)])
```

## Testing Config Flow

```python
async def test_flow_invalid_auth(hass):
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": "user"}
    )
    result = await hass.config_entries.flow.async_configure(
        result["flow_id"], user_input={"api_key": "bad"}
    )
    assert result["errors"] == {"base": "auth"}
```

Requires `pytest-homeassistant-custom-component` — see [[Unit Testing HA]].

## Development Tips

- Hard-refresh browser (`Ctrl+Shift+R`) after modifying config flow files — HA caches flow data
- Use `async_abort` to prevent duplicate entries: `await self.async_set_unique_id(unique_id)`

## Related

- [[Options Flow]] — for post-install reconfiguration
- [[Custom Component Structure]] — where config_flow.py lives
- [[Unit Testing HA]] — how to test config flow
- [[manifest.json]] — config_flow field
