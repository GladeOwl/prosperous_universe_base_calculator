from outpost import Outpost
from building import Building


def output_to_terminal(outpost: Outpost):
    for ticker in outpost.buildings:
        building: Building = outpost.buildings[ticker]
        print(ticker)
        for material in building.materials:
            print(material, building.materials[material]["amount"])
        print("")

    print("--")

    for ticker in outpost.materials:
        print(ticker, outpost.materials[ticker]["amount"])
    print(outpost.materials)
