import json
import requests
from rich import box
from rich.console import Console
from rich.table import Table
from objects import StationboardResponse, Stationboard, Stop

# make sure the station is string
flag = True

while flag:
    station_var = input("Departure Station: ").strip() or "Zürich"
    try:
        int(station_var)
        print("Departure Station cannot be an integer!")
    except ValueError:
        flag = False

# make sure the limit is integer
limit_var = ""

while type(limit_var) == str:
    limit_var = input("How many departures would you like to see?: ")
    try:
        limit_var = int(limit_var)
    except ValueError:
        print("Please enter a valid number.")

# fetch data
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

    # send GET request to API URL with specified parameters
    return requests.get(api_url, params)

# response with decoded data
response = get_request(station_var, limit_var)
data = json.loads(response.content)
decoded = StationboardResponse(**data)

# create table with columns
table = Table(title=f"Abfahrtstafel von {station_var}", box=box.ROUNDED)
table.add_column("Departure", justify="left", no_wrap=True)
table.add_column("Vehicle", justify="left", no_wrap=True)
table.add_column("Destination", justify="left", no_wrap=True)

# check whether the is delay or not
def check_delay(delay):
    if delay is None or delay == 0 or delay == "0":
        delay_min = ""
    else:
        delay_min = f" +{delay}min"
    return delay_min

# iterate over data and make rows
def load_data():
    for sb in decoded.stationboard:
        departure = sb.stop.departure.strftime("%H:%M")
        delay_min = check_delay(sb.stop.delay)
        vehicle = f"{sb.category}{sb.number}"
        destination = sb.to
        table.show_lines = True
        table.add_row(f"{departure}{delay_min}", vehicle, destination)

# call table with data inside
load_data()
console = Console()
console.print(table)


