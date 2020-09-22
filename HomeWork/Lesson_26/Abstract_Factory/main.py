from concrete_factory_1 import AbstractFactory, ConcreteFactory1
from concrete_factory_2 import ConcreteFactory2

def create_products(factory: AbstractFactory) -> None:
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f"{product_a.useful_function_a()}")
    print(f"{product_b.useful_function_b()}")

if __name__ == "__main__":
    print("Testing code with the first factory type:")
    create_products(ConcreteFactory1())
    print("\n")
    print("Testing code with the second factory type:")
    create_products(ConcreteFactory2())