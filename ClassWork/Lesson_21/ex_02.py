class Robot:
    """Цей клас представляє робота для прибирання з іменем"""

    # Змінна класу, яка містить кількість роботів в цілому
    population = 0

    def __init__(self, name: str):
        """Ініціалізація даних"""
        self.name = name
        print(f"Ініціалізація робота {self.name}")

        # При створенні робота збільшуємо загальну кількість на 1
        Robot.population += 1

    def __del__(self):
        """Виклик деструктора {Коли видаляється об'єкт робота}"""
        Robot.population -= 1
        print(f"Робот {self.name} помер!")

        if Robot.population == 0:
            print("Ви винищили всіх роботів")
        else:
            print(f"Залишилося {Robot.population} роботів")

    def say_hi(self):
        """Привітання окремого робота"""
        print(f"Привіт, мене звати {self.name}")

    def how_many():
        """Виводить на екран кількість роботів"""
        print(f"У нас тут {Robot.population} роботів")


if __name__ == "__main__":
    droid_1 = Robot("R2-D2")

    droid_2 = Robot("Walley")
    del droid_1
    del droid_2
    Robot.how_many()