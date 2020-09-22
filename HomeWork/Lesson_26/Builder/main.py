from director import Director, House, HouseBuilder


if __name__ == "__main__":
    builder = HouseBuilder()
    director = Director(builder)

    print("\nBuild house with garden and garage")
    director.build_house_with_garden_and_garage()
    print(builder.house)
    print("~" * 50)
    print("\nBuild house with swimming pool")
    director.build_house_with_swimming_pool()
    print(builder.house)