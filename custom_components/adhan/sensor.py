from homeassistant.components.sensor import SensorEntity
from .const import DOMAIN, PRAYER_TIMES, CONF_API_KEY, CONF_LOCATION
import requests

class AdhanSensor(SensorEntity):
    """Representation of a prayer time sensor."""

    def __init__(self, prayer, api_key, location):
        self._prayer = prayer
        self._state = None
        self._api_key = api_key
        self._location = location
        self._name = f"Adhan {prayer.capitalize()}"

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    async def async_update(self):
        """Fetch prayer times from the API."""
        url = f"https://api.aladhan.com/v1/timingsByCity?city={self._location}&key={self._api_key}"
        response = requests.get(url).json()
        if response.get("code") == 200:
            timings = response["data"]["timings"]
            self._state = timings[self._prayer.capitalize()]
