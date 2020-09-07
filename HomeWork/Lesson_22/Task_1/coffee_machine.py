from device import Device


class CoffeeMachine(Device):
    """This class contains information about the coffee machine."""

    def __init__(self, *, manufacturer: str = "Undefined", model: str = "Undefined", power: float = 0.0):
        """Initialize the object of coffee machine"""
        super().__init__(name="Coffee Machine", manufacturer=manufacturer)
        if model:
            self._model = model
        else:
            self._model = "Undefined"

        if power:
            self._power = power
        else:
            self._power = 0.0
    
    @property
    def model(self) -> str:
        """Returns a representation of the model"""
        return self._model

    @model.setter
    def model(self, value: str):
        """Sets the value in the model field"""
        if value:
            self._model = value
        elif not self._model:
            self._model = "Undefined"

    @property
    def power(self) -> float:
        """Returns a value of the power"""
        return self._power

    @power.setter
    def power(self, value: float):
        """Sets the value in the power field"""
        if value:
            try:
                self._power = float(value)
            except ValueError:
                print("Error: please enter the power in float type")
        elif not self._power:
            self._power = 0.0

    def __str__(self):
        """Returns a representation of the object"""
        return f"{super().__str__()}\nModel: {self._model}\nPower: {self._power}"


if __name__ == "__main__":
    print("This module for import not for execute!")