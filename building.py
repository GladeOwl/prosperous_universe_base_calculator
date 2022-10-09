from material import Material
from outpost import Outpost


class Building:
    def __init__(self, ticker: str, amount: int, outpost: Outpost) -> None:
        self.ticker: str = ticker
        self.amount: int = amount
        self.outpost: Outpost = outpost

    def work_data(self, data: dict):
        """Get Building Data from the JSON data"""

        self.name: str = data["Name"]
        self.area_cost: int = data["AreaCost"]
        self.outpost.add_area(self.area_cost * self.amount)

        self.pioneers: int = data["Pioneers"]
        self.settlers: int = data["Settlers"]
        self.technicians: int = data["Technicians"]
        self.engineers: int = data["Engineers"]
        self.scientists: int = data["Scientists"]

        self.materials = {}
        for material in data["BuildingCosts"]:
            ticker: str = material["CommodityTicker"]
            amount: int = material["Amount"]
            self.add_material(ticker, amount)

    def add_planet_data(self):
        """Get Planet specific building materials from the Planet Object"""

        self.planet = self.outpost.planet
        for material in self.planet.required_materials:
            ticker: str = material["ticker"]
            amount: int = (
                material["amount"]
                if not material["area_cost"]
                else material["amount"] * self.area_cost
            )
            self.add_material(ticker, amount)

    def add_material(self, ticker: str, amount: int):
        if ticker not in self.outpost.materials.keys():
            material_object: Material = Material(ticker)
            self.outpost.add_material(ticker, amount, self.amount, material_object)
        else:
            material_object: Material = self.outpost.materials[ticker]["info"]
            self.outpost.add_material_amount(ticker, amount)

        self.materials[ticker] = {
            "info": material_object,
            "amount": amount,
        }
