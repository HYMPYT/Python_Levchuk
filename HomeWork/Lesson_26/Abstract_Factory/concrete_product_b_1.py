from abstract_product_b import AbstractProductB


class ConcreteProductB1(AbstractProductB):
    """
    Concrete Products are created by corresponding Concrete Factories.
    """

    def useful_function_b(self) -> str:
        return "The result of the product B1."


if __name__ == "__main__":
    print("This module for import not for execute!")