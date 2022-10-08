from xml.dom import NotFoundErr


class Material:
    def __init__(self, ticker: str) -> None:
        self.ticker = ticker

    def get_price(self, data: dict):
        if self.ticker not in data["prices"].keys():
            raise NotFoundErr(
                f"Bad Ticker for the {self.ticker} Material. Something is wrong."
            )

        self.price = data["prices"][self.ticker]
