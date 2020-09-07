from device import Device


class MeatGrinder(Device):
    """This class contains information about the meat grinder."""

    def __init__(self, *, manufacturer: str = "Undefined", meat_grinder_type: str = "Undefined"):
        """Initialize the object of meat grinder"""
        super().__init__(name="Meat Grinder", manufacturer=manufacturer)
        if meat_grinder_type:
            self._meat_grinder_type = meat_grinder_type
        else:
            self._meat_grinder_type = "Undefined"

    @property
    def meat_grinder_type(self) -> str:
        """Returns a representation of the meat grinder type"""
        return self._meat_grinder_type

    @meat_grinder_type.setter
    def meat_grinder_type(self, value: str):
        """Sets the value in the meat_grinder_type field"""
        if value:
            self._meat_grinder_type = value
        elif not self._meat_grinder_type:
            self._meat_grinder_type = "Undefined"

    def __str__(self) -> str:
        """Returns a representation of the object"""
        return f"{super().__str__()}\nMeat grinder type: {self._meat_grinder_type}"


if __name__ == "__main__":
    print("This module for import not for execute!")