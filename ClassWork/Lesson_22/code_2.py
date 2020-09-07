class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}"


class Dog(Animal):
    def __init__(self, name: str, age: int, breed: str):
        super().__init__(name, age)
        self.breed = breed

    def say_hello(self, sound: str):
        print(f"{sound} {sound}")

    def __str__(self):
        return f"{super().__str__()}\nBreed: {self.breed}"


class Fish(Animal):
    def __init__(self, name: str, age: int, species: str):
        super().__init__(name, age)
        self.species = species

    def __str__(self):
        return f"{super().__str__()}\nSpecies: {self.species}"


bob = Dog("Bob", 5, "Labrador")
golden_fish = Fish("Korosta", 3, "Plitka")

print(bob)
print()
print(golden_fish)

