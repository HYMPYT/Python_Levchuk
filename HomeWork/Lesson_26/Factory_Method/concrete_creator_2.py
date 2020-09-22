from creator import Creator
from concrete_product_2 import ConcreteProduct2


class ConcreteCreator2(Creator):
    """ConcreteCreator2 to create a ConcreteProduct2"""

    def factory_method(self) -> ConcreteProduct2:
        return ConcreteProduct2()


if __name__ == "__main__":
    print("This.module for import not for execute!")