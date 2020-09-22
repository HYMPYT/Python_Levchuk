from singleton_meta import SingletonMeta


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        """
        Finally, any singleton should define some business logic, which can be
        executed on its instance.
        """

if __name__ == "__main__":
    print("This module for import not for execute!")