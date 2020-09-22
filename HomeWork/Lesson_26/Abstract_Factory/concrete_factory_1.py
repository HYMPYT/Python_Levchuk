from abstract_factory import AbstractFactory
from concrete_product_a_1 import ConcreteProductA1
from concrete_product_b_1 import ConcreteProductB1


class ConcreteFactory1(AbstractFactory):
    """
    Concrete Factories produce a family of products that belong to a single
    variant. The factory guarantees that resulting products are compatible. Note
    that signatures of the Concrete Factory's methods return an abstract
    product, while inside the method a concrete product is instantiated.
    """

    def create_product_a(self) -> ConcreteProductA1:
        return ConcreteProductA1()

    def create_product_b(self) -> ConcreteProductB1:
        return ConcreteProductB1()


if __name__ == "__main__":
    print("This module for import not for execute!")