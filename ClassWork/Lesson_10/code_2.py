import sys
import builtins

def power_factory(exp):
    def power(base):
        return base ** exp
    return power

# def outer_foo():
#     var = 100
#     def inner_foo():
#         print("var =", var)

#     inner_foo()
#     print("var =", var)

# def foo(i):
#     for i in range(5):
#         print(i)

if __name__ == "__main__":
    square = power_factory(2)
    print(square(10))

    # print(dir(__builtins__))
    
    # outer_foo()

    # print(dir(sys))
    # print(sys.__dict__.keys())

    # i = 10
    # print(i)
    # foo(i)
    # print(i)