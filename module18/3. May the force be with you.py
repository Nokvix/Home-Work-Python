import json
import requests
from pprint import pprint
from typing import List, Dict, Union


def get_pilots(starship: Dict[str, str]) -> List[Dict[str, str]]:
    pilots_link_list = starship["pilots"]
    pilots = []
    for link in pilots_link_list:
        pilots_req = requests.get(link)
        pilot_data = json.loads(pilots_req.text)

        homeworld_req = requests.get(pilot_data["homeworld"])
        homeworld = json.loads(homeworld_req.text)["name"]

        pilots.append({
            "height": pilot_data["height"],
            "homeworld": homeworld,
            "homewordl_url": pilot_data["homeworld"],
            "mass": pilot_data["mass"],
            "name": pilot_data["name"]
        })

    print("Получил пилотов")
    return pilots


def get_starships_list() -> List[Dict[str, str]]:
    req = requests.get("https://swapi.dev/api/starships/")
    data = json.loads(req.text)
    starships_list = data["results"]

    print("Получил список кораблей")
    return starships_list


def get_starship(starships_list: List[Dict[str, str]]) -> Dict[str, str]:
    starship = list(filter(lambda ship: ship["name"] == "Millennium Falcon", starships_list))[0]

    print("Получил корабль")
    return starship


def prepare_data_to_be_entered_into_json(starship: Dict[str, str], pilots: List[Dict[str, str]]) -> (
        Dict)[str, Union[str, List[Dict[str, str]]]]:

    result = {
        "max_atmosphering_speed": starship["max_atmosphering_speed"],
        "pilots": pilots,
        "ship_name": starship["name"],
        "starship_class": starship["starship_class"]
    }

    print("Создал словарь для записи в файл")
    return result


starships_list = get_starships_list()
starship = get_starship(starships_list)
pilots = get_pilots(starship)
result = prepare_data_to_be_entered_into_json(starship, pilots)

with open("Millennium Falcon.json", "w") as file:
    json.dump(result, file, indent=4)

with open("Millennium Falcon.json", "r") as file:
    data = json.load(file)

pprint(data)
