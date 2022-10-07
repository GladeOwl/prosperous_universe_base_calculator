from material import Material
from outpost import Outpost


class Building:
    def __init__(self, ticker: str, amount: int, outpost: Outpost) -> None:
        self.ticker = ticker
        self.amount = amount
        self.outpost = outpost
        self.outpost.buildings.append(self)

    def work_data(self, data: dict):
        """Get Building Data from the JSON data"""

        self.name = data["Name"]

        self.area_cost = data["AreaCost"]
        self.outpost.add_area(self.area_cost * self.amount)

        self.pioneers = data["Pioneers"]
        self.settlers = data["Settlers"]
        self.technicians = data["Technicians"]
        self.engineers = data["Engineers"]
        self.scientists = data["Scientists"]

        self.materials = []
        for material in data["BuildingCosts"]:
            new_material = Material(material["CommodityTicker"])
            self.materials.append(
                (f"{material['CommodityTicker']}", material["Amount"], new_material)
            )
            self.outpost.add_material(
                material["CommodityTicker"],
                material["Amount"],
                self.amount,
                new_material,
            )

    def add_planet_data(self):
        self.planet = self.outpost.planet
        for material in self.planet.required_materials:
            new_material = Material(material["ticker"])
            amount = (
                material["amount"]
                if not material["area_cost"]
                else material["amount"] * self.area_cost
            )
            self.materials.append((material["ticker"], amount, new_material))
            self.outpost.add_material(
                material["ticker"], amount, self.amount, new_material
            )
