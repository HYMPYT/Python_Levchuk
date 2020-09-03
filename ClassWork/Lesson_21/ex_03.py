class Robot:
    def __init__(self, name=""):
        self.name = name

    def __str__(self):
        return f"My name is {self.name}"

    def __eq__(self, other):
        return self.name == other.name

    def __add__(self, other):
        return [
            self,
            other
        ]

    def __sub__(self, other):
        if self.name > other.name:
            return self
        return other

    def __div__(self, other):
        pass

    def __pow__(self, other):


if __name__ == "__main__":
    walley = Robot("Walley")
    walley2 = Robot("Walley 2")
    r2_d2 = Robot("R2 D2")

    # robot_c = walley == r2_d2
    # robot_c = walley + r2_d2
    robot_c = walley - r2_d2

    print(robot_c)