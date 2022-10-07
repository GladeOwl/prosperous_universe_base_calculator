from material import Material
from planet import Planet


class Outpost:
    def __init__(self, planet: Planet) -> None:
        self.planet: Planet = planet
        self.buildings: list = []
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
        if self.materials[ticker]:
            self.materials[ticker]["amount"] += material_amount * building_amount
        else:
            self.materials[ticker] = {
                "info": material_object,
                "amount": material_amount * building_amount,
            }
