from product import Product


class ConcreteProduct2(Product):
    """ConcreteProduct1 implements all abstract class methods"""

    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"


if __name__ == "__main__":
    print("This.module for import not for execute!")