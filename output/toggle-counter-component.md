# Toggle Counter — Custom Component для Home Assistant

Тестовая компонента: переключатель + сенсор, считающий количество переключений.

## Структура файлов

```
custom_components/
└── toggle_counter/
    ├── __init__.py
    ├── manifest.json
    ├── const.py
    ├── switch.py
    └── sensor.py
```

---

## manifest.json

```json
{
  "domain": "toggle_counter",
  "name": "Toggle Counter",
  "version": "1.0.0",
  "documentation": "https://github.com/example/toggle_counter",
  "requirements": [],
  "codeowners": [],
  "iot_class": "local_push",
  "config_flow": false
}
```

> `config_flow: false` — компонента настраивается через `configuration.yaml`, без UI. Это проще для тестового примера.

---

## const.py

```python
DOMAIN = "toggle_counter"
```

---

## __init__.py

```python
"""Toggle Counter integration."""
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

DOMAIN = "toggle_counter"


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the Toggle Counter component."""
    hass.data.setdefault(DOMAIN, {"count": 0})
    return True
```

Ключевая идея: `hass.data[DOMAIN]["count"]` — общий счётчик. Переключатель инкрементирует его, сенсор читает.

---

## switch.py

```python
"""Toggle Counter switch platform."""
from homeassistant.components.switch import SwitchEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

from .const import DOMAIN


async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    async_add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    """Set up the switch platform."""
    async_add_entities([ToggleCounterSwitch(hass)])


class ToggleCounterSwitch(SwitchEntity):
    """A switch that increments a counter on each toggle."""

    _attr_name = "Toggle Counter Switch"
    _attr_unique_id = "toggle_counter_switch"
    _attr_icon = "mdi:toggle-switch"

    def __init__(self, hass: HomeAssistant) -> None:
        self._hass = hass
        self._is_on = False

    @property
    def is_on(self) -> bool:
        return self._is_on

    async def async_turn_on(self, **kwargs) -> None:
        """Turn the switch on and increment counter."""
        self._is_on = True
        self._increment_counter()
        self.async_write_ha_state()

    async def async_turn_off(self, **kwargs) -> None:
        """Turn the switch off and increment counter."""
        self._is_on = False
        self._increment_counter()
        self.async_write_ha_state()

    def _increment_counter(self) -> None:
        self._hass.data[DOMAIN]["count"] += 1
        # Notify all listeners that shared data changed
        self._hass.bus.async_fire(f"{DOMAIN}_count_updated")
```

Каждый `turn_on` и `turn_off` — это одно переключение. Счётчик растёт при каждом вызове. После изменения стреляем событием в event bus, чтобы сенсор мог обновиться без поллинга.

---

## sensor.py

```python
"""Toggle Counter sensor platform."""
from homeassistant.components.sensor import SensorEntity, SensorStateClass
from homeassistant.core import HomeAssistant, Event, callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

from .const import DOMAIN


async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    async_add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    """Set up the sensor platform."""
    async_add_entities([ToggleCounterSensor(hass)])


class ToggleCounterSensor(SensorEntity):
    """Sensor that shows how many times the switch was toggled."""

    _attr_name = "Toggle Counter"
    _attr_unique_id = "toggle_counter_sensor"
    _attr_native_unit_of_measurement = "toggles"
    _attr_state_class = SensorStateClass.TOTAL_INCREASING
    _attr_icon = "mdi:counter"
    _attr_should_poll = False  # push-based, no polling needed

    def __init__(self, hass: HomeAssistant) -> None:
        self._hass = hass
        self._count = 0

    async def async_added_to_hass(self) -> None:
        """Subscribe to counter update events."""
        self.async_on_remove(
            self._hass.bus.async_listen(
                f"{DOMAIN}_count_updated", self._handle_count_update
            )
        )

    @callback
    def _handle_count_update(self, event: Event) -> None:
        """Handle counter update event from the switch."""
        self._count = self._hass.data[DOMAIN]["count"]
        self.async_write_ha_state()

    @property
    def native_value(self) -> int:
        return self._count
```

Сенсор подписывается на событие `toggle_counter_count_updated` через `async_added_to_hass`. `async_on_remove` автоматически отпишет при выгрузке. Нет поллинга — обновление мгновенное.

---

## configuration.yaml

Добавь в свой `configuration.yaml`:

```yaml
switch:
  - platform: toggle_counter

sensor:
  - platform: toggle_counter
```

---

## Как установить

1. Скопируй папку `toggle_counter/` в `<config>/custom_components/`
2. Добавь блоки в `configuration.yaml` (см. выше)
3. Перезапусти Home Assistant
4. В UI появятся:
   - `switch.toggle_counter_switch`
   - `sensor.toggle_counter`

---

## Как это работает

```
User clicks switch
        │
        ▼
async_turn_on() / async_turn_off()
        │
        ├─── hass.data["toggle_counter"]["count"] += 1
        │
        └─── hass.bus.async_fire("toggle_counter_count_updated")
                    │
                    ▼
        _handle_count_update() в сенсоре
                    │
                    ├─── self._count = hass.data[...]["count"]
                    └─── self.async_write_ha_state()  →  HA UI обновляется
```

---

## Паттерны из wiki

- [[Custom Component Structure]] — структура директорий и `__init__.py`
- [[Entity Types]] — `SwitchEntity`, `SensorEntity`, `_attr_*` паттерн
- [[Async Patterns]] — `async_write_ha_state()`, `async_on_remove`, event bus
- `_attr_should_poll = False` + event-driven update — вместо polling через `async_update()`
- `SensorStateClass.TOTAL_INCREASING` — правильный state class для монотонно растущих счётчиков (история, статистика)
