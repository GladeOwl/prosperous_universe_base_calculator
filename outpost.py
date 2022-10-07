from planet import Planet


class Outpost:
    def __init__(self, planet: Planet) -> None:
        self.planet: Planet = planet
        self.buildings: list = []
        self.required_materials: list = []

        self.total_area: int = 0
        self.pioneers: int = 0
        self.settlers: int = 0
        self.technicians: int = 0
        self.engineers: int = 0
        self.scientists: int = 0
