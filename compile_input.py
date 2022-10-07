def add_pop(info: dict, population: dict, amount: int):
    for type in population:
        population[type] += info[type] * amount


def input_buildings(buildings: list, data: dict, population: dict):
    ticker: str = input("Building Ticker?: ")

    if ticker == "":
        print("Please input a building name.")
        return

    for item in data["buildings"]:
        if item["Ticker"] == ticker:
            amount: int = int(input("Build Amount? (default: 1): ")) or 1
            buildings.append({"info": item, "amount": amount})
            add_pop(item, population, amount)

            print(f"Building Added: {item['Name']}, {amount}x.")
            return item["AreaCost"] * amount

    print("Bad Ticker.")
    return 0
