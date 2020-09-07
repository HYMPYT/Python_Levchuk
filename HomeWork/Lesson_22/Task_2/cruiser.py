from ship import Ship


class Cruiser(Ship):
    """This class contains information about the cruiser."""

    def __init__(self, *, load_capacity: float = 0.0, speed: float = 0.0, name: str = "Undefined", classification: str = "Undefined"):
        """Initialize the object of cruiser"""
        super().__init__(ship_type="Cruiser", load_capacity=load_capacity, speed=speed)
        if name:
            self._name = name
        else:
            self._name = "Undefined"

        if classification:
            self._classification = classification
        else:
            self._classification = "Undefined"

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
    def classification(self) -> str:
        """Returns a representation of the classification"""
        return self._classification

    @classification.setter
    def classification(self, value: str):
        """Sets the value in the classification field"""
        if value:
            self._classification = value
        elif not self._classification:
            self._classification = "Undefined"

    def __str__(self) -> str:
        """Returns a representation of the object"""
        return f"{super().__str__()}\nName: {self._name}\nClassification: {self._classification}"


if __name__ == "__main__":
    print("This module for import not for execute!")