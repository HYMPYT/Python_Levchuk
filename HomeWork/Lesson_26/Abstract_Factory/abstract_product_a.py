from abc import ABC, abstractmethod


class AbstractProductA(ABC):
    """
    Each distinct product of a product family should have a base interface. All
    variants of the product must implement this interface.
    """

    @abstractmethod
    def useful_function_a(self) -> str:
        pass


if __name__ == "__main__":
    print("This module for import not for execute!")