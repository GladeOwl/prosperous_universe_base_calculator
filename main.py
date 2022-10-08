import os
import sys
from planet import Planet
from outpost import Outpost
from building import Building
from import_data import import_data
from output_data import output_to_terminal


def input_buildings(outpost: Outpost, data: dict):
    ticker: str = input("Building Ticker?: ")

    if ticker == "":
        print("Please input a building name.")
        return

    for item in data["buildings"]:
        if item["Ticker"] == ticker:
            amount: int = int(input("Build Amount? (default: 1): ") or 1)

            building: Building = Building(ticker, amount, outpost)
            building.work_data(item)
            building.add_planet_data()

            outpost.buildings[ticker] = building

            print(f"Building Added: {item['Name']}, {amount}x.")
            return

    print("Bad Ticker.")


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

    planet: Planet = Planet(input("Planet Name? (default: Harmonia): ") or "Harmonia")
    planet.calculate_materials()
    outpost: Outpost = Outpost(planet)

    is_done: bool = False

    while not is_done:
        input_buildings(outpost, data)

        is_done_input = input("Done? (y/n) (default: n): ")
        if is_done_input == "y":
            is_done = True

    outpost.calculate_data(data)

    output_to_terminal(outpost)
