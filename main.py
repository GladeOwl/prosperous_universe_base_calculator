import os
import sys
from import_data import get_old_data, get_new_data
from compile_input import input_buildings


def get_resource_cost(buildings: list, resources: dict):
    for building in buildings:
        for item in building["info"]["BuildingCosts"]:
            name = item["CommodityTicker"]

            if name in resources:
                resources[name] += item["Amount"] * building["amount"]
            else:
                resources[name]: int = item["Amount"] * building["amount"]


if __name__ == "__main__":
    file_path: str = os.path.join(sys.path[0], "./data.json")
    get_data: str = input("Import new data? (y/n) (default: y): ") or "y"

    if get_data == "y" or not os.path.isfile(file_path):
        print("Importing new data.")
        data: dict = get_new_data(file_path)
    else:
        data: dict = get_old_data(file_path)

    total_area: int = 0
    buildings: list = []
    resources: dict = {}
    population: dict = {
        "Pioneers": 0,
        "Settlers": 0,
        "Technicians": 0,
        "Engineers": 0,
        "Scientists": 0,
    }

    is_done: bool = False

    while not is_done:
        total_area += input_buildings(buildings, data, population)

        is_done_input = input("Done? (y/n) (default: n): ")
        if is_done_input == "y":
            is_done = True

    get_resource_cost(buildings, resources)
    print(resources)

    # TODO: This guy is pretty much done. Just need a way to combine all the info into a good terminal output
