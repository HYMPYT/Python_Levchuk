from random import randint
class Enemy:
    def __init__(self):
        self.hp = 100
    def kick(self):
        self.hp -= 10
        def critical(self):
            self.hp -= 5
        some_damage(self)

if __name__ == "__main__":
    e = Enemy()
    print(e.hp)
    e.kick()
    print(e.hp)