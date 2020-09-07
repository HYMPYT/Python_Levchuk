class A:
    __count = 0

    def __init__(self):
        A.__count += 1

    def __del__(self):
        A.__count -= 1

    def obj_quantity():
        return A.__count

a = A()
a2 = A()

print(A.obj_quantity())
del a

print(A.obj_quantity())