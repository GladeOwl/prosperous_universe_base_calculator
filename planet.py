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
            self.required_materials.append(
                {"ticker": "MCG", "amount": 4, "area_cost": True}
            )
        else:
            self.required_materials.append(
                {"ticker": "AEF", "amount": 4, "area_cost": True}
            )

    def check_temperature(self, temperature: float):
        if temperature > 75:
            self.required_materials.append(
                {"ticker": "TSH", "amount": 1, "area_cost": False}
            )
        elif temperature < -25:
            self.required_materials.append(
                {"ticker": "INS", "amount": 10, "area_cost": True}
            )

    def check_gravity(self, gravity: float):
        if gravity > 2.5:
            self.required_materials.append(
                {"ticker": "BL", "amount": 1, "area_cost": False}
            )
        elif gravity < 0.25:
            self.required_materials.append(
                {"ticker": "MGC", "amount": 1, "area_cost": False}
            )

    def check_pressure(self, pressure: float):
        if pressure > 2:
            self.required_materials.append(
                {"ticker": "HSE", "amount": 1, "area_cost": False}
            )
        elif pressure < 0.25:  ## TODO: It can't handle Gas planets
            self.required_materials.append(
                {"ticker": "SEA", "amount": 1, "area_cost": True}
            )
