def pow_2(func):
    def wrapper(num):
        return func(num) ** 2
    return wrapper

@pow_2
def func(num):
    return num

if __name__ == "__main__":
    print('Result:', func(10))
    print('Result:', func(6))
    print('Result:', func(4))