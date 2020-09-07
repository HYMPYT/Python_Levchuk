from person import Person


class Employee(Person):
    """This class contains information about the employee."""
    def __init__(self, *, name: str = "Undefined", age: int = 1, position: str = "Undefined"):
        """Initialize the object of employee"""
        super().__init__(name=name, age=age)
        self._position = position

    @property
    def position(self) -> str:
        """Returns a representation of the position"""
        return self._position

    @position.setter
    def position(self, value: str):
        """Sets the value in the position field"""
        if value:
            self._position = value
        elif not self._position:
            self._position = "Undefined"

    def display_info(self) -> str:
        """Function print info about employee"""
        super().display_info()
        print(f"Position: {self._position}")


if __name__ == "__main__":
    print("This module for import not for execute.")