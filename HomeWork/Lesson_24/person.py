class Person:
    """This class implements the object of the person"""

    def __init__(self, name, surname, age):
        """Initialize the object fields"""
        self._name = name
        self._surname = surname
        self._age = age

    @property
    def name(self) -> str:
        """Returns the representation of name field"""
        return self._name

    @name.setter
    def name(self, value: str):
        """Sets the value of name field"""
        self._name = value

    @property
    def surname(self) -> str:
        """Returns the representation of surname field"""
        return self._surname

    @surname.setter
    def surname(self, value: str):
        """Sets the value of surname field"""
        self._surname = value

    @property
    def age(self) -> int:
        """Returns the value of age field"""
        return self._age

    @age.setter
    def age(self, value: int):
        """Sets the value of age field"""
        self._age = value

    def __str__(self) -> str:
        """Returns the representation of object"""
        return f"Name: {self._name}, Surname: {self._surname}, Age: {self._age}\n"

    def __repr__(self) -> str:
        """Returns the admin representation of object"""
        return f"{self._name} ~ {self._surname} ~ {self._age}"


if __name__ == "__main__":
    print("This module for import not for execute")