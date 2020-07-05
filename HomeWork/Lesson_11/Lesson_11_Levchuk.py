def make_multiplier_of(n):
    """Enclosing function return the nested function"""
    def multiplier(x):
        """Nested function"""
        return x * n
    return multiplier

def helper_for_map(x):
    """This function is a replacement of lambda x: x ** 2"""
    return x ** 2

def helper_for_filter(x):
    """This function is a replacement of lambda x: type(x) == int and x % 2 == 0"""
    if type(x) == int and x % 2 == 0:
        return True
    else:
        return False

def square(x):
    """This function is a replacement of lambda x: x ** 2"""
    return x ** 2

if __name__ == "__main__":
    while True:
        print("~~~~~~~~~~~~Menu~~~~~~~~~~~~")
        print("Closure  -> enter 1")
        print("map()    -> enter 2")
        print("filter() -> enter 3")
        print("lambda   -> enter 4")
        print("Exit     -> enter 5")
        choice = input("-> ")
        if choice == '1':
            print("\nClosure")
            print("make_multiplier_of(3)(2)")
            print("Mult =", make_multiplier_of(3)(2))
            print("\nmult_3 = make_multiplier_of(3)")
            mult_3 = make_multiplier_of(3)
            print("mult_3(2)")
            print("Mult =", mult_3(2))
            input()
        elif choice == '2':
            print("\nmap()")
            lst = [1, 2, 3, 4, 5, 6]
            print("List before execute map() ->", lst)
            print("map(lambda x: x ** 2, lst)")
            print("List after execute map() ->", list(map(lambda x: x ** 2, lst)))
            print("\nList before execute map() ->", lst)
            print("map(helper_for_map, lst)")
            print("List after execute map() ->", list(map(helper_for_map, lst)))
            input()
        elif choice == '3':
            print("\nfilter()")
            lst = [1, 2, 3, 4, 5, 6, True, False, "Hello", "World", 6, 12]
            print("List before execute filter() ->", lst)
            print("filter(lambda x: type(x) == int and x % 2 == 0, lst)")
            print("List after execute filter() ->", list(filter(lambda x: type(x) == int and x % 2 == 0, lst)))
            print("\nList before execute filter() ->", lst)
            print("filter(helper_for_filter, lst)")
            print("List after execute filter() ->", list(filter(helper_for_filter, lst)))
            input()
        elif choice == '4':
            print("\nlambda")
            print("square(3)")
            print("Result =", square(3))
            print("\nsquare_2 = lambda x : x ** 2")
            square_2 = lambda x : x ** 2
            print("square_2(3)")
            print("Result =", square_2(3))
            input()
        elif choice == '5':
            break
        else:
            print("Entered wrong data. Please try again.")
            input()