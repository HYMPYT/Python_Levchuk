from house_builder import HouseBuilder, Builder, House


class Director:
    """Director knows which object to build and what parameters"""

    def __init__(self, builder: Builder):
        self.__builder = builder

    def build_house_with_garden_and_garage(self) -> None:
        self.__builder.build_walls(6)
        self.__builder.build_doors(2)
        self.__builder.build_windows(4)
        self.__builder.build_roof()
        self.__builder.build_garden(1)
        self.__builder.build_garage(1)

    def build_house_with_swimming_pool(self) -> None:
        self.__builder.build_walls()
        self.__builder.build_doors()
        self.__builder.build_windows(3)
        self.__builder.build_roof()
        self.__builder.build_swimming_pool()


if __name__ == "__main__":
    print("This module for import not for execute!")