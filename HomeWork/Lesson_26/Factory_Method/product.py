from abc import ABC, abstractmethod


class Product(ABC):
    """Abstract class that implements some logic for all classes which inheritence Product"""

    @abstractmethod
    def operation(self) -> str:
        pass


if __name__ == "__main__":
    print("This.module for import not for execute!")