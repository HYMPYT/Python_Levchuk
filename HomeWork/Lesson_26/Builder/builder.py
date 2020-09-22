from abc import ABC, abstractmethod


class Builder(ABC):
    """Abstract class that implements logic for the builder"""
    
    @abstractmethod
    def build_walls(self, value: int = 4) -> None:
        pass

    @abstractmethod
    def build_doors(self, value: int = 1) -> None:
        pass

    @abstractmethod
    def build_roof(self) -> None:
        pass

    @abstractmethod
    def build_windows(self, value: int = 2) -> None:
        pass

    @abstractmethod
    def build_garage(self, value: int = 1) -> None:
        pass

    @abstractmethod
    def build_swimming_pool(self, value: int = 1) -> None:
        pass

    @abstractmethod
    def build_garden(self, value: int = 1) -> None:
        pass

    @abstractmethod
    def build_fancy_statues(self) -> None:
        pass


if __name__ == "__main__":
    print("This module for import not for execute!")