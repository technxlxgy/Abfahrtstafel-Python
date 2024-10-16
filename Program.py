import urllib.parse
import urllib.request

url = "http://transport.opendata.ch/v1/stationboard"
params = {
    "station": "Zurich",
    "limit": 3,
    "fields[]": "stationboard/stop/departure",
    "fields[]": "stationboard/stop/delay",
    "fields[]": "stationboard/category",
    "fields[]": "stationboard/number",
    "fields[]": "stationboard/to"
}

query_string = urllib.parse.urlencode(params)

url = url + "?" + query_string

with urllib.request.urlopen(url) as response:
    response_text = response.read()
    print(response_text)