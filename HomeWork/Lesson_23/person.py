class Person:
    """This class contains information about the person."""

    def __init__(self, *, name: str = "Undefined", age: int = 1):
        """Initialize the object of person"""
        self._name = name
        self._age = age

    @property
    def name(self) -> str:
        """Returns a representation of the name"""
        return self._name

    @name.setter
    def name(self, value: str):
        """Sets the value in the name field"""
        if value:
            self._name = value
        elif not self._name:
            self._name = "Undefined"

    @property
    def age(self) -> int:
        """Returns a value of the age"""
        return self._age

    @age.setter
    def age(self, value: int):
        """Sets the value in the age field"""
        if value:
            if value > 0:
                try:
                    self._age = int(value)
                except ValueError:
                    print("Error: please enter age in the integer type")
            else:
                print("Error: age must be positive")
        elif not self._age:
            self._age = 1

    def display_info(self):
        """Function print info about person"""
        print(f"Name: {self._name}\nAge: {self._age}")


if __name__ == "__main__":
    print("This module for import not for execute.")