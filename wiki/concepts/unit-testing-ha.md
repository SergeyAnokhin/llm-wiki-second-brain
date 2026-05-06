---
tags: [home-assistant, custom-integration, testing, pytest, ci]
sources: [Building a Home Assistant Custom Component Part 2 Unit Testing and Continuous Integration.md, Building a Home Assistant Custom Component Part 3 Config Flow.md, Building a Home Assistant Custom Component Part 4 Options Flow.md]
created: 2026-05-05
updated: 2026-05-05
---

# Unit Testing HA

Unit tests catch bugs before users do. The HA ecosystem provides dedicated tooling that makes testing integrations much easier than general Python testing.

## Setup

Install the pytest plugin:

```bash
pip install pytest-homeassistant-custom-component
```

If using the [[Aaron Godfrey]] cookiecutter template, this is already in `requirements.test.txt`.

Create `tests/__init__.py` (empty) and `tests/conftest.py`.

## Key Fixtures

Provided by `pytest-homeassistant-custom-component` — pytest finds them automatically, no import needed.

### hass

A fully initialized `HomeAssistant` instance for tests:

```python
async def test_something(hass):
    # hass is ready to use
    assert hass is not None
```

### MockConfigEntry

Create mock config entries without going through the UI flow:

```python
from pytest_homeassistant_custom_component.common import MockConfigEntry

config_entry = MockConfigEntry(
    domain=DOMAIN,
    data={"api_key": "test-key", "repos": [{"path": "home-assistant/core"}]},
)
config_entry.add_to_hass(hass)
assert await hass.config_entries.async_setup(config_entry.entry_id)
await hass.async_block_till_done()
```

## Mocking Async Functions

```python
from unittest.mock import AsyncMock, patch

async def test_async_update_failed(hass):
    with patch("custom_components.my_integration.MyAPI.fetch") as mock_fetch:
        mock_fetch.side_effect = Exception("Connection failed")
        sensor = MySensor(config)
        await sensor.async_update()
        assert sensor.available is False
```

## Testing Config Flow

```python
async def test_config_flow_valid(hass):
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_USER}
    )
    assert result["type"] == "form"
    assert result["step_id"] == "user"

    result = await hass.config_entries.flow.async_configure(
        result["flow_id"],
        user_input={"api_key": "valid-key"},
    )
    assert result["type"] == "create_entry"
    assert result["data"] == {"api_key": "valid-key"}

async def test_config_flow_invalid_auth(hass):
    with patch("custom_components.my_integration.config_flow.validate_auth",
               side_effect=ValueError):
        result = await hass.config_entries.flow.async_init(
            DOMAIN, context={"source": "user"}
        )
        result = await hass.config_entries.flow.async_configure(
            result["flow_id"], user_input={"api_key": "bad"}
        )
        assert result["errors"] == {"base": "auth"}
```

## Testing Options Flow

```python
async def test_options_flow(hass):
    config_entry = MockConfigEntry(domain=DOMAIN, data={...})
    config_entry.add_to_hass(hass)
    await hass.config_entries.async_setup(config_entry.entry_id)
    await hass.async_block_till_done()

    result = await hass.config_entries.options.async_init(config_entry.entry_id)
    result = await hass.config_entries.options.async_configure(
        result["flow_id"], user_input={"poll_interval": 5}
    )
    assert result["type"] == "create_entry"
    assert result["data"] == {"poll_interval": 5}
```

## Testing Entities Directly

For `async_update` tests:

```python
async def test_sensor_update(hass):
    with patch("custom_components.my_integration.sensor.MyAPI") as MockAPI:
        instance = AsyncMock()
        instance.get_data.return_value = {"temperature": 22.5}
        MockAPI.return_value = instance

        sensor = MySensor({"api_key": "key"})
        await sensor.async_update()

        assert sensor.native_value == 22.5
        assert sensor.available is True
```

## CI with GitHub Actions

### hassfest (validates component structure)

`.github/workflows/hassfest.yaml`:

```yaml
name: Validate with hassfest
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: home-assistant/actions/hassfest@master
```

### Python Tests

`.github/workflows/tests.yaml`:

```yaml
name: Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install -r requirements.test.txt
      - run: pytest tests/ -v
```

## Pre-commit Hooks

`.pre-commit-config.yaml` checks run before each commit:
- `pyupgrade` — upgrade Python syntax
- `black` — auto-format
- `isort` — sort imports
- `flake8` — linting
- `mypy` — type checking
- `codespell` — spell check
- `bandit` — security checks
- `check-json` — validate JSON files

Install: `pip install pre-commit && pre-commit install`

## Reference Components for Test Patterns

Study tests from platinum-quality HA core integrations:
- `tests/components/hue/`
- `tests/components/wled/`
- `tests/components/ipp/`

## Related

- [[Config Flow]] — testing config flow steps
- [[Options Flow]] — testing options flow
- [[GitHub Actions CI]]
- [[Debugging Devcontainer]]
