"""The Adhan integration."""
from .const import DOMAIN

async def async_setup(hass, config):
    """Set up the Adhan component."""
    return True

async def async_setup_entry(hass, entry):
    """Set up Adhan from a config entry."""
    hass.data.setdefault(DOMAIN, {})
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(entry, 'sensor')
    )
    return True

async def async_unload_entry(hass, entry):
    """Unload a config entry."""
    await hass.config_entries.async_forward_entry_unload(entry, 'sensor')
    return True
