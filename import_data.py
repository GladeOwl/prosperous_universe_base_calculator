import os
import sys
import csv
import json
import requests


def import_data(new_data: bool):
    file_path: str = os.path.join(sys.path[0], "./data.json")

    if new_data or not os.path.isfile(file_path):
        print("Importing new data.")
        return get_new_data(file_path)
    print("Working with old data")
    return get_old_data(file_path)


def get_old_data(file_path):
    try:
        with open(file_path, "r") as jsonf:
            data: dict = json.load(jsonf)
            return data
    except Exception:
        raise FileNotFoundError("Could not access the existing data!")


## Currently only supports AI1 AIC Prices
def get_price_data():
    response = requests.get("https://rest.fnar.net/csv/prices")
    with open("./prices.txt", "w") as txtf:
        txtf.write(response.text)

    with open("./prices.txt", "r") as txtf:
        stripped = (line.strip() for line in txtf)
        lines = (line.split(",") for line in stripped if line)

        with open("./prices.csv", "w") as csvf:
            writer = csv.writer(csvf)
            writer.writerows(lines)

    with open("./prices.csv", "r", encoding="utf-8") as csvf:
        csv_data = csv.DictReader(csvf)
        prices = {}
        for rows in csv_data:
            key = rows["Ticker"]
            prices[key] = (
                round(float(rows["AI1-AskPrice"]), 2)
                if rows["AI1-AskPrice"] != ""
                else 0
            )

    return json.dumps(prices, indent=4)


def get_new_data(file_path):
    try:
        building_response = requests.get("https://rest.fnar.net/building/allbuildings")
        material_response = requests.get("https://rest.fnar.net/material/allmaterials")

        with open(file_path, "w") as jsonf:
            json_data: dict = {
                "buildings": json.loads(building_response.text),
                "materials": json.loads(material_response.text),
                "prices": json.loads(get_price_data()),
            }
            jsonf.write(json.dumps(json_data, indent=4))

            print("New Data Imported")
            return json_data

    except ConnectionError:
        print("Internet Issue! Could not grab data. Using existing data.")
        return get_old_data(file_path)
