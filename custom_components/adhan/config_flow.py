from homeassistant import config_entries
from .const import DOMAIN, CONF_CITY, CONF_COUNTRY, CONF_METHOD

class AdhanConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow for Adhan integration."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}

        if user_input is not None:
            # Validatie
            city = user_input[CONF_CITY]
            country = user_input[CONF_COUNTRY]
            method = user_input[CONF_METHOD]

            # Eventueel validatie of de input correct is
            if not city or not country:
                errors["base"] = "invalid_location"
            else:
                # Sla configuratie op en voltooi
                return self.async_create_entry(
                    title=f"Adhan ({city}, {country})",
                    data=user_input,
                )

        return self.async_show_form(
            step_id="user",
            data_schema=self.add_data_schema(),
            errors=errors,
        )

    def add_data_schema(self):
        """Voeg schema toe voor UI."""
        from homeassistant.helpers import config_validation as cv
        import voluptuous as vol

        return vol.Schema(
            {
                vol.Required(CONF_CITY, default="Breukelen"): cv.string,
                vol.Required(CONF_COUNTRY, default="Netherlands"): cv.string,
                vol.Required(CONF_METHOD, default=3): vol.All(vol.Coerce(int), vol.Range(min=1, max=12)),
            }
        )
