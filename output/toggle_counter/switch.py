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
        self._is_on = True
        self._increment_counter()
        self.async_write_ha_state()

    async def async_turn_off(self, **kwargs) -> None:
        self._is_on = False
        self._increment_counter()
        self.async_write_ha_state()

    def _increment_counter(self) -> None:
        self._hass.data[DOMAIN]["count"] += 1
        self._hass.bus.async_fire(f"{DOMAIN}_count_updated")
