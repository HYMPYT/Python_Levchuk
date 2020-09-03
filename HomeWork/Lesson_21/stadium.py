from datetime import date


class Stadium:
    """This class represents stadium"""

    def __init__(self, *,
        name: str = "Undefined",
        opening_date: date = date(1, 1, 1),
        country: str = "Undefined",
        city: str = "Undefined",
        capacity: int = 0):
        """Initialize object fields"""
        self._name = name
        self._opening_date = opening_date
        self._country = country
        self._city = city
        self._capacity = capacity

    @property
    def name(self) -> str:
        """Returns the stadium name"""
        return self._name

    @name.setter
    def name(self, value: str):
        """Sets the stadium name"""
        self._name = value

    @property
    def opening_date(self) -> date:
        """Returns the opening date of the stadium"""
        return self._opening_date

    @opening_date.setter
    def opening_date(self, value: date):
        """Sets the opening date of the stadium"""
        try:
            if isinstance(value, date):
                self._opening_date = value
            else:
                raise ValueError("Please enter the date")
        except ValueError as e:
            print(f"\nError: {e}\n")

    @property
    def country(self) -> str:
        """Returns the country of the stadium"""
        return self._country

    @country.setter
    def country(self, value: str):
        """Sets the country of the stadium"""
        self._country = value

    @property
    def city(self) -> str:
        """Returns the city of the stadium"""
        return self._city

    @city.setter
    def city(self, value: str):
        """Sets the city of the stadium"""
        self._volume = value

    @property
    def capacity(self) -> int:
        """Returns the capacity of the stadium"""
        return self._capacity

    @capacity.setter
    def capacity(self, value: int):
        """Sets the capacity of the stadium"""
        try:
            self._capacity = int(value)
        except ValueError:
            print("\nError: please enter stadium capacity in integer type\n")

    def __str__(self) -> str:
        """Returns the representation of object"""
        return f"""
        ~~~~~~ Stadium ~~~~~~
        Name: {self._name}
        Opening date: {self._opening_date}
        Country: {self._country}
        City: {self._city}
        Capacity: {self._capacity}
        """

    def __repr__(self) -> str:
        """Returns the admin representation of object"""
        return f"{self._name} {self._opening_date} {self._country} {self._city} {self._capacity}"


if __name__ == "__main__":
    print("This module for import not for execute")