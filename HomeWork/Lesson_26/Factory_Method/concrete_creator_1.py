from creator import Creator
from concrete_product_1 import ConcreteProduct1


class ConcreteCreator1(Creator):
    """ConcreteCreator1 to create a ConcreteProduct1"""
    
    def factory_method(self) -> ConcreteProduct1:
        return ConcreteProduct1()


if __name__ == "__main__":
    print("This.module for import not for execute!")