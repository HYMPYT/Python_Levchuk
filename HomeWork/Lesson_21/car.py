class Car:
    """This class represents car"""

    def __init__(self, *,
        model: str = "Undefined",
        year: int = 0,
        manufacturer: str = "Undefined",
        volume: float = 0.0,
        color: str = "Undefined",
        price: float = 0.0):
        """Initialize object fields"""
        self._model = model
        self._year = year
        self._manufacturer = manufacturer
        self._volume = volume
        self._color = color
        self._price = price

    @property
    def model(self) -> str:
        """Returns the car model"""
        return self._model

    @model.setter
    def model(self, value: str):
        """Sets the car model"""
        self._model = value

    @property
    def year(self) -> int:
        """Returns the year of the car"""
        return self._year

    @year.setter
    def year(self, value: int):
        """Sets the year of the car"""
        try:
            self._year = int(value)
        except ValueError:
            print("\nError: please enter the year in integer type\n")

    @property
    def manufacturer(self) -> str:
        """Returns the manufacturer of the car"""
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, value: str):
        """Sets the manufacturer of the car"""
        self._manufacturer = value

    @property
    def volume(self) -> float:
        """Returns the volume of the car"""
        return self._volume

    @volume.setter
    def volume(self, value: float):
        """Sets the volume of the car"""
        try:
            self._volume = float(value)
        except ValueError:
            print("\nError: please enter the engine volume in float type\n")

    @property
    def color(self) -> str:
        """Returns the color of the car"""
        return self._color

    @color.setter
    def color(self, value: str):
        """Sets the color of the car"""
        self._color = value

    @property
    def price(self) -> float:
        """Returns the price of the car"""
        return self._price

    @price.setter
    def price(self, value: float):
        """Sets the price of the car"""
        try:
            self._price = float(value)
        except ValueError:
            print("\nError: please enter the price in float type\n")

    def __str__(self) -> str:
        """Returns the representation of object"""
        return f"""
        ~~~~~~ Car ~~~~~~
        Model: {self._model}
        Year: {self._year}
        Manufacturer: {self._manufacturer}
        Volume: {self._volume}
        Color: {self._color}
        Price: {self._price}
        """

    def __repr__(self) -> str:
        """Returns the admin representation of object"""
        return f"{self._model} {self._year} {self._manufacturer} {self._volume} {self._color} {self._price}"


if __name__ == "__main__":
    print("This module for import not for execute")
