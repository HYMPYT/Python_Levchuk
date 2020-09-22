from abstract_factory import AbstractFactory
from concrete_product_a_2 import ConcreteProductA2
from concrete_product_b_2 import ConcreteProductB2


class ConcreteFactory2(AbstractFactory):
    """
    Each Concrete Factory has a corresponding product variant.
    """

    def create_product_a(self) -> ConcreteProductA2:
        return ConcreteProductA2()

    def create_product_b(self) -> ConcreteProductB2:
        return ConcreteProductB2()


if __name__ == "__main__":
    print("This module for import not for execute!")