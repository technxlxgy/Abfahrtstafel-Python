import json

import requests

from objects import StationboardResponse

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

print(decoded.stationboard)