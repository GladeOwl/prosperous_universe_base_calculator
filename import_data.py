from itertools import tee
import json
import requests


def get_old_data(file_path):
    try:
        with open(file_path, "r") as jsonf:
            data: dict = json.load(jsonf)
            return data
    except Exception:
        raise FileNotFoundError("Could not access the existing data!")


def get_new_data(file_path):
    try:
        building_response = requests.get("https://rest.fnar.net/building/allbuildings")
        material_response = requests.get("https://rest.fnar.net/material/allmaterials")

        with open(file_path, "w") as jsonf:
            json_data: dict = {
                "buildings": json.loads(building_response.text),
                "materials": json.loads(material_response.text),
            }
            jsonf.write(json.dumps(json_data, indent=4))

            print("New Data Imported")
            return json_data

    except ConnectionError:
        print("Internet Issue! Could not grab data. Using existing data.")
        return get_old_data(file_path)
