import os
import sys
from planet import Planet
from outpost import Outpost
from building import Building
from import_data import import_data
from output_data import output_to_terminal

os.chdir(os.path.dirname(os.path.realpath(sys.argv[0])))


def get_build_list():
    try:
        with open("./build_list.txt", "r") as txtf:
            return txtf.readlines()
    except FileNotFoundError:
        open("./build_list.txt", "w").close()
        raise FileNotFoundError(
            "Build List txt file not found. A new one has been created, please intput your list and try again."
        )


def get_build_price(outpost: Outpost, data: dict, build_list: list):
    for line in build_list:
        build_with_amount = line.split(" ")

        if len(build_with_amount) != 2:
            raise ValueError(
                f"idk wtf {build_with_amount} is.. but try again and type it better this time."
            )

        input_buildings(
            outpost, data, build_with_amount[0], int(build_with_amount[1].strip())
        )


def input_buildings(outpost: Outpost, data: dict, ticker: str, amount_tobe_built: int):
    for item in data["buildings"]:
        if item["Ticker"] == ticker:
            amount: int = amount_tobe_built

            building: Building = Building(ticker, amount, outpost)
            building.work_data(item)
            building.add_planet_data()

            outpost.buildings[ticker] = building
            return


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

    if not os.path.isfile(file_path):
        print("Local Data file Not Found.")
        new_data: bool = True
    else:
        new_data: bool = (input("Import new data? (y/n) (default: y): ") or "y") == "y"

    data: dict = import_data(new_data, file_path)

    planet: Planet = Planet(
        input("Planet Name? (default: Harmonia) (Gas Planets not supported): ")
        or "Harmonia"
    )
    planet.calculate_materials()
    outpost: Outpost = Outpost(planet)

    is_done: bool = False

    build_list: list = get_build_list()
    get_build_price(outpost, data, build_list)

    outpost.calculate_data(data)

    output_to_terminal(outpost)
