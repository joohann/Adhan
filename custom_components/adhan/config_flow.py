import secrets
from homeassistant import config_entries
from .const import DOMAIN, NAME

class AdhanConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow for Adhan."""

    VERSION = "1.0.0"
    CONNECTION_CLASS = config_entries.CONN_CLASS_LOCAL_POLL

    async def async_step_user(self, user_input=None):
        """Handle a flow initialized by the user."""
        
        errors = {}

        if user_input is not None:
            city = user_input.get("city")
            country = user_input.get("country")
            
            # Save the entered city and country in configuration file
            self._async_abort_entries_match({"city": city, "country": country})

            # Proceed to create the entry
            return self.async_create_entry(title=NAME, data={"city": city, "country": country})

        # Only a single instance of the integration
        if self._async_current_entries():
            return self.async_abort(reason="single_instance_allowed")

        id = secrets.token_hex(6)

        await self.async_set_unique_id(id)
        self._abort_if_unique_id_configured()

        # Display the form for the user to input city and country
        return self.async_show_form(
            step_id="user",
            data_schema=config_entries.CONFIG_SCHEMA.extend(
                {
                    vol.Required("city"): str,
                    vol.Required("country"): str,
                }
            ),
            errors=errors,
        )
