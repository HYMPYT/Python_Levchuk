class Book:
    """This class represents book"""

    def __init__(self, *,
        title: str = "Undefined",
        year: int = 0,
        publisher: str = "Undefined",
        genre: str = "Undefined",
        author: str = "Undefined",
        price: float = 0.0):
        """Initialize object fields"""
        self._title = title
        self._year = year
        self._publisher = publisher
        self._genre = genre
        self._author = author
        self._price = price

    @property
    def title(self) -> str:
        """Returns the book title"""
        return self._title

    @title.setter
    def title(self, value: str):
        """Sets the book title"""
        self._title = value

    @property
    def year(self) -> int:
        """Returns the year of the book"""
        return self._year

    @year.setter
    def year(self, value: int):
        """Sets the year of the book"""
        try:
            self._year = int(value)
        except ValueError:
            print("\nError: please enter a year in integer type\n")

    @property
    def publisher(self) -> str:
        """Returns the publisher of the book"""
        return self._publisher

    @publisher.setter
    def publisher(self, value: str):
        """Sets the publisher of the book"""
        self._publisher = value

    @property
    def genre(self) -> str:
        """Returns the genre of the book"""
        return self._genre

    @genre.setter
    def genre(self, value: str):
        """Sets the genre of the book"""
        self._genre = value

    @property
    def author(self) -> str:
        """Returns the author of the book"""
        return self._author

    @author.setter
    def author(self, value: str):
        """Sets the author of the book"""
        self._author = value

    @property
    def price(self) -> float:
        """Returns the price of the car"""
        return self._price

    @price.setter
    def price(self, value: float):
        """Sets the price of the car"""
        try:
            self._price = float(value)
        except ValueError:
            print("\nError: please enter the price in float type\n")

    def __str__(self) -> str:
        """Returns the representation of object"""
        return f"""
        ~~~~~~ Book ~~~~~~
        Model: {self._title}
        Year: {self._year}
        Publisher: {self._publisher}
        Genre: {self._genre}
        Author: {self._author}
        Price: {self._price}
        """

    def __repr__(self) -> str:
        """Returns the admin representation of object"""
        return f"{self._title} {self._year} {self._publisher} {self._genre} {self._author} {self._price}"


if __name__ == "__main__":
    print("This module for import not for execute")