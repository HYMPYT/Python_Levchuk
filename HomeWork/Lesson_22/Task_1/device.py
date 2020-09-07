from string import ascii_uppercase
from random import randint, choice


class Device:
    """This class contains information about the device."""

    def __init__(self, *, name: str = "Undefined", manufacturer: str = "Undefined"):
        """Initialize the object of device"""
        self.__name = name

        if manufacturer:
            self._manufacturer = manufacturer
        else:
            self._manufacturer = "Undefined"

        self.__serial_number = self.__create_serial_number()

    @property
    def name(self) -> str:
        """Returns a representation of the name"""
        return self.__name

    @property
    def manufacturer(self) -> str:
        """Returns a representation of the manufacturer"""
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, value: str):
        """Sets the value in the manufacturer field"""
        if value:
            self._manufacturer = value
        elif not self._manufacturer:
            self._manufacturer = "Undefined"

    @property
    def serial_number(self) -> str:
        """Returns a representation of the serial number"""
        return self.__serial_number

    def __create_serial_number(self) -> str:
        """Returns a randomly generated serial number"""
        serial_number = ""
        for i in range(10):
            if i % 2 == 0:
                serial_number += choice(ascii_uppercase)
            serial_number += str(randint(0, 9))
        return serial_number

    def __str__(self):
        """Return a representation of object"""
        return f"~~~~~ Device ~~~~~\nName: {self.__name}\nThe serial number: {self.__serial_number}\nManufacturer: {self._manufacturer}"


if __name__ == "__main__":
    print("This module for import not for execute!")