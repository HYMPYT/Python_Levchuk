from person import Person


class Student(Person):
    """This class contains information about the student."""
    def __init__(self, *, name: str = "Undefined", age: int = 1, university: str = "Undefined"):
        """Initialize the object of student"""
        super().__init__(name=name, age=age)
        self._university = university

    @property
    def university(self) -> str:
        """Returns a representation of the university"""
        return self._university

    @university.setter
    def university(self, value: str):
        """Sets the value in the university field"""
        if value:
            self._university = value
        elif not self._university:
            self._university = "Undefined"

    def display_info(self):
        """Function print info about student"""
        print(f"Student: {self._name}\nAge: {self._age}\nStudying in {self._university}")


if __name__ == "__main__":
    print("This module for import not for execute.")