from ship import Ship


class Frigate(Ship):
    """This class contains information about the frigate."""

    def __init__(self, *, load_capacity: float = 0.0, speed: float = 0.0, name: str = "Undefined", housing_material: str = "Undefined"):
        """Initialize the object of frigate"""
        super().__init__(ship_type="Frigate", load_capacity=load_capacity, speed=speed)
        if name:
            self._name = name
        else:
            self._name = "Undefined"

        if housing_material:
            self._housing_material = housing_material
        else:
            self._housing_material = "Undefined"

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
    def housing_material(self) -> str:
        """Returns a representation of the housing material"""
        return self._housing_material

    @housing_material.setter
    def housing_material(self, value: str):
        """Sets the value in the housing_material field"""
        if value:
            self._housing_material = value
        elif not self._housing_material:
            self._housing_material = "Undefined"

    def __str__(self) -> str:
        """Returns a representation of the object"""
        return f"{super().__str__()}\nHousing material: {self._housing_material}\nName: {self._name}"


if __name__ == "__main__":
    print("This module for import not for execute!")