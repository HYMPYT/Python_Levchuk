class Dog:
    total_count = 0

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Dog.total_count += 1

    def say_wof(self):
        print('-WOF-')

    def say_name(self):
        print(f"--WOF, my name is {self.name}--")


if __name__ == "__main__":
    barbos = Dog(name = 'Barbos', age = 4)
    tuzik = Dog(name = 'Tuzik', age = 7)

    barbos.say_wof()
    barbos.say_name()

    tuzik.say_wof()
    tuzik.say_name()

    print(tuzik.total_count)