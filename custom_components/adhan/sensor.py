from homeassistant.components.sensor import SensorEntity
from .const import DOMAIN, PRAYER_TIMES, CONF_CITY, CONF_COUNTRY, CONF_METHOD
import requests

class AdhanSensor(SensorEntity):
    """Representation of a prayer time sensor."""

    def __init__(self, prayer, city, country, method):
        """Initialize the sensor."""
        self._prayer = prayer
        self._city = city
        self._country = country
        self._method = method
        self._state = None
        self._name = f"Adhan {prayer.capitalize()}"

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    async def async_update(self):
        """Fetch prayer times from the API."""
        try:
            url = (
                f"https://api.aladhan.com/v1/timingsByCity?"
                f"city={self._city}&country={self._country}&method={self._method}"
            )
            response = requests.get(url).json()
            if response.get("code") == 200:
                timings = response["data"]["timings"]
                self._state = timings[self._prayer.capitalize()]
            else:
                self._state = "API Error"
        except Exception as e:
            self._state = f"Error: {str(e)}"

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up Adhan sensors from a config entry."""
    city = config_entry.data[CONF_CITY]
    country = config_entry.data[CONF_COUNTRY]
    method = config_entry.data[CONF_METHOD]

    entities = [AdhanSensor(prayer, city, country, method) for prayer in PRAYER_TIMES]
    async_add_entities(entities, update_before_add=True)
