def outer(par):
    loc = par
    def inner():
        return loc
    return inner()

var = 1
a = outer(var)
print(a)