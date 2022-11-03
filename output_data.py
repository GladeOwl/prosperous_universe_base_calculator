from tabulate import tabulate
from material import Material
from outpost import Outpost
from building import Building


def output_to_terminal(outpost: Outpost):
    print("")
    for buidling_ticker in outpost.buildings:
        building: Building = outpost.buildings[buidling_ticker]
        print(
            tabulate(
                [[buidling_ticker, building.name, f"{building.amount:3}"]],
                ["Ticker", "Name", "Amount"],
                tablefmt="pretty",
            )
        )

        material_data = []
        for material_ticker in building.materials:
            material: Material = building.materials[material_ticker]
            material_data.append(
                [
                    material_ticker,
                    f"{material['amount']:3}",
                    f"{material['info'].price * material['amount']:8}",
                ]
            )
            # print(
            #     f"{material_ticker} {material['amount']:3}  {material['info'].price * material['amount']:8}"
            # )
        print(
            tabulate(
                material_data, ["Ticker", "Amount", "Total Price"], tablefmt="psql"
            )
        )
        print("")
        print("---")

    print("MRP: Market Price; CRP: Corporation Price")

    table_data = []
    for ticker in outpost.materials:
        material: Material = outpost.materials[ticker]

        amount = f"{material['amount']}"

        mrp = f"{material['info'].price:.2f}"
        mrp_total = f"{material['info'].price * material['amount']:.2f}"

        if hasattr(material["info"], "o_price"):
            crp = f"{material['info'].o_price:.2f}"
            crp_total = f"{material['info'].o_price * material['amount']:.2f}"
        else:
            crp = 0
            crp_total = 0

        string = [ticker, amount, mrp, mrp_total, crp, crp_total]
        table_data.append(string)

    headers = ["Ticker", "Amount", "MRP", "MRP Total", "CRP", "CRP Total"]
    print(tabulate(table_data, headers, tablefmt="psql"))

    print("")
    print(
        tabulate(
            [
                [
                    f"{outpost.total_price} AIC",
                    f"{outpost.override_total_price} AIC",
                    f"{outpost.final_price} AIC",
                ]
            ],
            ["MRP Total", "CRP Total", "Combined Total*"],
            tablefmt="pretty",
        )
    )
    print("*Combined Total uses MRP for any missing CRP.")
    print("")
