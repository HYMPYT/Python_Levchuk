from ship import Ship


class Destroyer(Ship):
    """This class contains information about the destroyer."""

    def __init__(self, *, load_capacity: float = 0.0, speed: float = 0.0, name: str = "Undefined", count_of_mines: int = 0):
        """Initialize the object of destroyer"""
        super().__init__(ship_type="Destroyer", load_capacity=load_capacity, speed=speed)
        if name:
            self._name = name
        else:
            self._name = "Undefined"

        if count_of_mines:
            self._count_of_mines = count_of_mines
        else:
            self._count_of_mines = 0

    @property
    def name(self) -> str:
        """Returns a representation of the sname"""
        return self._name

    @name.setter
    def name(self, value: str):
        """Sets the value in the name field"""
        if value:
            self._name = value
        elif not self._name:
            self._name = "Undefined"

    @property
    def count_of_mines(self) -> int:
        """Returns a value of the count of mines"""
        return self._count_of_mines

    @count_of_mines.setter
    def count_of_mines(self, value: int):
        """Sets the value in the count_of_mines field"""
        if value:
            try:
                self._count_of_mines = int(value)
            except ValueError:
                print("Error: please enter the count of mines in integer type")
        elif not self._count_of_mines:
            self._count_of_mines = 0

    def __str__(self) -> str:
        """Returns a representation of the object"""
        return f"{super().__str__()}\nName: {self._name}\nCount of mines: {self._count_of_mines}"


if __name__ == "__main__":
    print("This module for import not for execute!")