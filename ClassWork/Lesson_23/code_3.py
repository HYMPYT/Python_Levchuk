class Base:
    def __init__(self, n):
        self.n = n

    def out(self):
        print(self.n)


class One(Base):
    def multi(self, m):
        self.n *= m

    
class Two(Base):
    def inlist(self):
        self.lst = list(str(self.n))

    def out(self):
        i = 0
        while i < len(self.lst):
            print(self.lst[i])
            i += 1

if __name__ == "__main__":
    obj_1 = One(45)
    obj_2 = Two('abc')

    obj_1.multi(2)
    obj_1.out()

    obj_2.inlist()
    obj_2.out()
