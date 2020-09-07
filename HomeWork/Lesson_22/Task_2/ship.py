class Ship:
    """This class contains information about the ship."""

    def __init__(self, *, ship_type: str = "Undefined", load_capacity: float = 0.0, speed: float = 0.0):
        """Initialize the object of ship"""
        self.__ship_type = ship_type

        if load_capacity:
            self._load_capacity = load_capacity
        else:
            self._load_capacity = 0.0

        if speed:
            self._speed = speed
        else:
            self._speed = 0.0

    @property
    def ship_type(self) -> str:
        """Returns a representation of the ship type"""
        return self.__ship_type

    @property
    def load_capacity(self) -> float:
        """Returns a value of the load capacity"""
        return self._load_capacity

    @load_capacity.setter
    def load_capacity(self, value: float):
        """Sets the value in the load_capacity field"""
        if value:
            try:
                self._load_capacity = float(value)
            except ValueError:
                print("Error: please enter the load capacity of the ship in float type")
        elif not self._load_capacity:
            self._load_capacity = 0.0

    @property
    def speed(self) -> float:
        """Returns a value of the speed"""
        return self._speed

    @speed.setter
    def speed(self, value: float):
        """Sets the value in the speed field"""
        if value:
            try:
                self._speed = float(value)
            except ValueError:
                print("Error: please enter the speed of the ship in float type")
        elif not self._speed:
            self._speed = 0.0

    def __str__(self) -> str:
        """Returns a representation of the object"""
        return f"~~~~~ Ship ~~~~~\nType: {self.__ship_type}\nLoad capacity: {self._load_capacity}\nSpeed: {self._speed}"


if __name__ == "__main__":
    print("This module for import not for execute!")