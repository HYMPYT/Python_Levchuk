def parabola(x):
    return x ** 2

def get_point(y, x):
    return y(x)

print(get_point(parabola, 2))

# def make_closure(par):
#     loc = par
#     def power(var):
#         return var ** loc
#     return power

# cube = make_closure(3)
# print(cube(3))