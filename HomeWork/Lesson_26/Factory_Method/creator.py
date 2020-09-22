from abc import ABC, abstractmethod


class Creator(ABC):
    """Abstract class that implements some logic for all classes which inheritance Creator"""

    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self) -> str:
        product = self.factory_method()
        return f"Creator: The same creator's code has just worked with {product.operation()}"


if __name__ == "__main__":
    print("This module for import not for execute!")