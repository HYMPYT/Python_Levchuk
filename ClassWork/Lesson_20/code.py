from random import choice


class Car:
    COLORS = (
        (0, 'RED'),
        (1, 'GREEN'),
        (2, 'YELLOW'),
        (3, 'BLUE')
    )

    def __init__(
        self,
        brand: str = '',
        engine_volume: float = 0.0,
        color: int = 0,
        price: float = 0.0
    ):
        self.brand = brand
        self.engine_volume = engine_volume
        self.color = color
        self.price = price

    def __str__(self):
        return f"""
        brand: {self.brand}
        engine_volume: {self.engine_volume}
        color: {Car.COLORS[self.color][1]}
        price: {self.price}
        """

    def change_engine_volume(self, volume: float) -> None:
        try:
            self.engine_volume = float(volume)
        except ValueError:
            print("Error: please enter a number of float")

    def change_color(self, color: str) -> None:
        if not color:
            self.color = choice(Car.COLORS)[0]
        else:
            try:
                for index, car_color in Car.COLORS:
                    if color == car_color:
                        self.color = index
                        break
                else:
                    raise ValueError("Error: Enter correct color!")
            except ValueError as e:
                print(e)

    @property
    def car_color(self):
        return Car.COLORS[self.color][1]


if __name__ == "__main__":
    renault = Car()
    engine_volume = input("Enter engine volume: ")
    renault.change_engine_volume(engine_volume)
    color = input("Enter the color (RED, YELLOW, GREEN, BLUE): ")
    renault.change_color(color)
    print(renault)