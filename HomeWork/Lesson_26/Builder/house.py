from typing import Any


class House:
    """This class initializes the object House"""
    def __init__(self):
        """initializes the object field"""
        self.__parts = []

    def add(self, part: Any) -> None:
        """Add a new part to the object"""
        self.__parts.append(part)

    def __str__(self) -> str:
        """Returns the representation of the object"""
        return f"House parts: {', '.join(self.__parts)}"


if __name__ == "__main__":
    print("This module for import not for execute!")