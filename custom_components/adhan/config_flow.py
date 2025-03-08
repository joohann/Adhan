from homeassistant import config_entries
import voluptuous as vol

from .const import DOMAIN, CONF_API_KEY, CONF_LOCATION

class AdhanConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Adhan."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}
        
        if user_input is not None:
            # Validatie toevoegen als nodig
            return self.async_create_entry(title="Adhan", data=user_input)

        schema = vol.Schema({
            vol.Required(CONF_API_KEY): str,
            vol.Required(CONF_LOCATION): str,
        })
        return self.async_show_form(step_id="user", data_schema=schema, errors=errors)
