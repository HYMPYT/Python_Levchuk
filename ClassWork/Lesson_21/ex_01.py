class Temperature:
    def __init__(self, *, celsius=0):
        self.celsius = celsius

    @property
    def kelvines(self):
        return self.celsius + 273

    @kelvines.setter
    def kelvines(self, value):
        self.celsius = value - 273

    @property
    def fahrenheit(self):
        return self.celsius * 1.8 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) / 1.8


if __name__ == "__main__":
    t = Temperature(celsius=12)
    t.fahrenheit = 50
    print(t.celsius)
