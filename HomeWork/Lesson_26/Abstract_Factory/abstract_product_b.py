from abc import ABC, abstractmethod


class AbstractProductB(ABC):
    @abstractmethod
    def useful_function_b(self) -> str:
        pass


if __name__ == "__main__":
    print("This module for import not for execute!")