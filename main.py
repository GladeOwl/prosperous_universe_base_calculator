import os
import sys
from outpost import Outpost
from building import Building
from import_data import import_data


def input_buildings(outpost: Outpost, data: dict):
    ticker: str = input("Building Ticker?: ")

    if ticker == "":
        print("Please input a building name.")
        return

    for item in data["buildings"]:
        if item["Ticker"] == ticker:
            amount: int = int(input("Build Amount? (default: 1): ")) or 1

            building: Building = Building(ticker, amount)
            building.get_data(item)

            outpost.buildings.append(building)

            print(f"Building Added: {item['Name']}, {amount}x.")

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
    get_data: str = input("Import new data? (y/n) (default: y): ") or "y"

    need_new_data = get_data == "y" or not os.path.isfile(file_path)
    data: dict = import_data(need_new_data, file_path)

    planet: str = input("Planet Name?: ")
    outpost: Outpost = Outpost(planet)

    is_done: bool = False

    while not is_done:
        input_buildings(outpost, data)

        is_done_input = input("Done? (y/n) (default: n): ")
        if is_done_input == "y":
            is_done = True
