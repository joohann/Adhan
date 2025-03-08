from homeassistant import config_entries
import voluptuous as vol

from .const import DOMAIN, CONF_CITY, CONF_COUNTRY, CONF_METHOD

class AdhanConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Adhan."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}
        
        if user_input is not None:
            # Controleer of alle invoer geldig is
            if not user_input[CONF_CITY] or not user_input[CONF_COUNTRY]:
                errors["base"] = "invalid_location"
            else:
                # Sla de configuratie op
                return self.async_create_entry(title="Adhan", data=user_input)

        # Formulier voor gebruiker
        schema = vol.Schema({
            vol.Required(CONF_CITY, default="Breukelen"): str,
            vol.Required(CONF_COUNTRY, default="Netherlands"): str,
            vol.Optional(CONF_METHOD, default="3"): str,
        })
        return self.async_show_form(step_id="user", data_schema=schema, errors=errors)
