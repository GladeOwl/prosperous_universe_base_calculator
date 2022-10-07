class Building:
    def __init__(self, ticker: str) -> None:
        self.ticker = ticker

    def get_data(self, data: dict):
        for building in data["buildings"]:
            if self.ticker == building["ticker"]:
                self.name = building["Name"]
                self.area_cost = building["AreaCost"]

                self.add_pop(building)
                self.add_materials(building)

    def add_pop(self, building: dict):
        self.pioneers = building["Pioneers"]
        self.settlers = building["Settlers"]
        self.technicians = building["Technicians"]
        self.engineers = building["Engineers"]
        self.scientists = building["Scientists"]

    def add_materials(self, building: dict):
        self.materials = []
        for material in building["BuildingCosts"]:
            self.materials.append(
                {"ticker": material["CommodityTicker"], "amount": material["Amount"]}
            )
