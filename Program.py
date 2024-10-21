import json
import requests
from unicodedata import category

from objects import StationboardResponse, Stationboard, Stop

DEFAULT_STATION = "Romanshorn"
DEFAULT_LIMIT = 3


def get_request(station, limit):
    api_url = "http://transport.opendata.ch/v1/stationboard"
    params = {
        "station": station,
        "limit": limit,
        "fields[]": [
            "stationboard/stop/departure",
            "stationboard/stop/delay",
            "stationboard/category",
            "stationboard/number",
            "stationboard/to"
        ]
    }

    return requests.get(api_url, params)

response = get_request(DEFAULT_STATION, DEFAULT_LIMIT)
data = json.loads(response.content)
decoded = StationboardResponse(**data)
decoded.stationboard

for sb in decoded.stationboard:
    departure = sb.stop.departure
    delay = sb.stop.delay
    # in care the is/is no delay
    if delay is not None:
        delay_min = f" + {delay} min"
    else:
        delay_min = ""
    vehicle = f"{sb.category}{sb.number}"
    destination = sb.to

print(f"Departure: {departure}, Delay: {delay_min}, Vehicle: {vehicle}, Destination: {destination}")