from abstract_product_a import AbstractProductA


class ConcreteProductA1(AbstractProductA):
    """
    Concrete Products are created by corresponding Concrete Factories.
    """

    def useful_function_a(self) -> str:
        return "The result of the product A1."


if __name__ == "__main__":
    print("This module for import not for execute!")