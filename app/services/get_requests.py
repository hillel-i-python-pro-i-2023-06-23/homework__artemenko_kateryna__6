import requests


def get_astronaut_count():
    url = "http://api.open-notify.org/astros.json"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        astronaut_count = data["number"]
        return astronaut_count


def print_count(count):
    if count is not None:
        print(f"{count} astronauts on the station.")
