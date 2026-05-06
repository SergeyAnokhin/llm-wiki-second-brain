"""Toggle Counter sensor platform."""
from homeassistant.components.sensor import SensorEntity, SensorStateClass
from homeassistant.core import Event, HomeAssistant, callback
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
    _attr_should_poll = False

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
        self._count = self._hass.data[DOMAIN]["count"]
        self.async_write_ha_state()

    @property
    def native_value(self) -> int:
        return self._count
