import json
import requests


class Planet:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.required_materials: list = []
        self.import_data()

    def import_data(self):
        try:
            response = requests.get(f"https://rest.fnar.net/planet/{self.name}")
            self.data = json.loads(response.text)
        except Exception:
            raise ConnectionError("Couldn't Get Planet Data")

    def calculate_materials(self):
        self.check_type(self.data["Surface"])
        self.check_temperature(self.data["Temperature"])
        self.check_gravity(self.data["Gravity"])
        self.check_pressure(self.data["Pressure"])

    def check_type(self, is_rocky: bool):
        if is_rocky:
            self.required_materials.append({"MCG": 4, "area_cost": True})
        else:
            self.required_materials.append({"AEF": 4, "area_cost": True})

    def check_temperature(self, temperature: float):
        if temperature > 75:
            self.required_materials.append({"TSH": 1, "area_cost": False})
        elif temperature < -25:
            self.required_materials.append({"INS": 10, "area_cost": True})

    def check_gravity(self, gravity: float):
        if gravity > 2.5:
            self.required_materials.append({"BL": 1, "area_cost": False})
        elif gravity < 0.25:
            self.required_materials.append({"MGC": 1, "area_cost": False})

    def check_pressure(self, pressure: float):
        if pressure > 2:
            self.required_materials.append({"HSE": 1, "area_cost": False})
        elif pressure < 0.25:
            self.required_materials.append({"SEA": 1, "area_cost": True})


planet = Planet("Harmonia")
planet.get_data()
