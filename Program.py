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
    departure = Stop.departure(sb)
    delay = " +" + Stop.delay(sb)
    vehicle = Stationboard.category(sb) + Stationboard.number(sb)
    destination = Stationboard.to(sb)





#print(decoded.stationboard)