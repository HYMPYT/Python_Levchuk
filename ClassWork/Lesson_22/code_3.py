class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name}"


class SubSuper(Super):
    def __init__(self, name):
        super().__init__(name)


obj = SubSuper("Dima")

print(obj)