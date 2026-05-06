"""Toggle Counter integration."""
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

from .const import DOMAIN


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the Toggle Counter component."""
    hass.data.setdefault(DOMAIN, {"count": 0})
    return True
