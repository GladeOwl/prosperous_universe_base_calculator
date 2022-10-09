from material import Material
from outpost import Outpost
from building import Building


def output_to_terminal(outpost: Outpost):
    for buidling_ticker in outpost.buildings:
        building: Building = outpost.buildings[buidling_ticker]
        print(buidling_ticker, building.amount)

        for material_ticker in building.materials:
            material: Material = building.materials[material_ticker]
            print(
                material_ticker,
                material["amount"],
                material["info"].price * material["amount"],
            )
        print("")

    print("--")

    for ticker in outpost.materials:
        material: Material = outpost.materials[ticker]
        print(
            ticker,
            material["amount"],
            material["info"].price,
            round(material["info"].price * material["amount"], 2),
        )

    print("--")
    print(outpost.total_price)
