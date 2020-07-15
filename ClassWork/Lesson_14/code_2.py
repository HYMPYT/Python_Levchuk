def factorial(x, n = 1):
    return n if x == 1 else factorial(x - 1, n * x)

print(factorial(5))