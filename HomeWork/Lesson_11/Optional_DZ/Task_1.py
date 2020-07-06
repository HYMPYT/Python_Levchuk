def gcd(a, b):
    """This function return the largest common divisor"""
    if a != 0 and b != 0:
        if a > b:
            return gcd(a % b, b)
        else:
            return gcd(a, b % a)
    else:
        return a + b

if __name__ == "__main__":
    a = 30
    b = 18
    print("Number_1 =", a)
    print("Number_2 =", b)
    print("Result =", gcd(30, 18))