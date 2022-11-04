from material import Material
from planet import Planet


class Outpost:
    def __init__(self, planet: Planet) -> None:
        self.planet: Planet = planet
        self.buildings: dict = {}
        self.materials: dict = {}

        self.total_area: int = 0
        self.pioneers: int = 0
        self.settlers: int = 0
        self.technicians: int = 0
        self.engineers: int = 0
        self.scientists: int = 0

    def add_material(
        self,
        ticker: str,
        material_amount: int,
        building_amount: int,
        material_object: Material,
    ):
        self.materials[ticker] = {
            "info": material_object,
            "amount": material_amount * building_amount,
        }

    def add_material_amount(self, ticker, amount, building_amount):
        self.materials[ticker]["amount"] += amount * building_amount

    def calculate_data(self, data: dict):
        self.calculate_prices(data)
        self.calculate_population()

    def calculate_prices(self, data: dict):
        self.total_price: float = 0
        self.override_total_price: float = 0
        self.final_price: float = 0

        for ticker in self.materials:
            material_object: Material = self.materials[ticker]["info"]
            material_object.get_price(data)

            price = material_object.price * self.materials[ticker]["amount"]
            self.total_price += price

            if hasattr(material_object, "o_price"):
                price = material_object.o_price * self.materials[ticker]["amount"]
                self.override_total_price += price

            self.final_price += price

    def calculate_population(self):
        for ticker in self.buildings:
            building = self.buildings[ticker]
            self.pioneers += building.pioneers * building.amount
            self.settlers += building.settlers * building.amount
            self.technicians += building.technicians * building.amount
            self.engineers += building.engineers * building.amount
            self.scientists += building.scientists * building.amount

    def add_area(self, area_cost):
        self.total_area += area_cost
