from builder import Builder
from house import House


class HouseBuilder(Builder):
    """Concrete builder that worh with the concrete object. Implements all abstract methods from Builder"""

    def __init__(self):
        self.reset()

    def reset(self) -> None:
        self.__house = House()
    
    def build_walls(self, value: int = 4) -> None:
        self.__house.add(f"Walls: {value}")

    def build_doors(self, value: int = 1) -> None:
        self.__house.add(f"Doors: {value}")

    def build_windows(self, value: int = 2) -> None:
        self.__house.add(f"Windows: {value}")

    def build_roof(self) -> None:
        self.__house.add("Roof: 1")

    def build_garage(self, value: int = 1) -> None:
        self.__house.add(f"Added {value} garage")

    def build_swimming_pool(self, value: int = 1) -> None:
        self.__house.add(f"Added {value} swimming pool")

    def build_garden(self, value: int = 1) -> None:
        self.__house.add(f"Added {value} garden")

    def build_fancy_statues(self) -> None:
        self.__house.add("Added fancy statues")

    @property
    def house(self) -> House:
        result = self.__house
        self.reset()
        return result


if __name__ == "__main__":
    print("This module for import not for execute!")