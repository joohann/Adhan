import logging
from homeassistant.util.json import json_loads

from .const import DOMAIN, PRAYER_TIMES

_LOGGER = logging.getLogger(__name__)

def load_prayer_times():
    try:
        # In plaats van json.loads gebruiken we nu json_loads
        with open("path/to/your/prayer_times.json", "r") as f:
            data = json_loads(f.read())  # Nieuwe functie
        return data
    except Exception as e:
        _LOGGER.error(f"Error loading prayer times: {e}")
        return None
