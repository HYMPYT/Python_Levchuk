from abstract_product_a import AbstractProductA


class ConcreteProductA2(AbstractProductA):
    """
    Concrete Products are created by corresponding Concrete Factories.
    """

    def useful_function_a(self) -> str:
        return "The result of the product A2."


if __name__ == "__main__":
    print("This module for import not for execute!")