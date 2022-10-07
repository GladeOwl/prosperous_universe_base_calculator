from outpost import Outpost


class Building:
    def __init__(self, ticker: str, amount: int, outpost: Outpost) -> None:
        self.ticker = ticker
        self.amount = amount

    def get_data(self, data: dict):
        """Get Building Data from the JSON data"""

        self.name = data["Name"]
        self.area_cost = data["AreaCost"]

        self.pioneers = data["Pioneers"]
        self.settlers = data["Settlers"]
        self.technicians = data["Technicians"]
        self.engineers = data["Engineers"]
        self.scientists = data["Scientists"]

        self.materials = []
        for material in data["BuildingCosts"]:
            self.materials.append(
                {"ticker": material["CommodityTicker"], "amount": material["Amount"]}
            )
