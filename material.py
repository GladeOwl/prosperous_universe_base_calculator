import json


class Material:
    def __init__(self, ticker: str) -> None:
        self.ticker = ticker

    def get_price(self, data: dict):
        if self.ticker not in data["prices"].keys():
            raise NameError(
                f"Bad Ticker for the {self.ticker} Material. Something is wrong."
            )

        with open("./override.json", "r", encoding="utf-8") as jsonf:
            override_data = json.load(jsonf)
            if self.ticker in override_data:
                self.o_price: float = float(override_data[self.ticker])

        self.price: float = float(data["prices"][self.ticker])
