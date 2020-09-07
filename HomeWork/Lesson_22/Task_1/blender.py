from device import Device


class Blender(Device):
    """This class contains information about the blender."""

    def __init__(self, *, manufacturer: str = "Undefined", blender_type: str = "Undefined"):
        """Initialize the object of blender"""
        super().__init__(name="Blender", manufacturer=manufacturer)
        if blender_type:
            self._blender_type = blender_type
        else:
            self._blender_type = "Undefined"

    @property
    def blender_type(self) -> str:
        """Returns a representation of the blender type"""
        return self._blender_type

    @blender_type.setter
    def blender_type(self, value: str):
        """Sets the value in the blender_type field"""
        if value:
            self._blender_type = value
        elif not self._blender_type:
            self._blender_type = "Undefined"

    def __str__(self) -> str:
        """Returns a representation of the object"""
        return f"{super().__str__()}\nBlender type: {self._blender_type}"

if __name__ == "__main__":
    print("This module for import not for execute!")