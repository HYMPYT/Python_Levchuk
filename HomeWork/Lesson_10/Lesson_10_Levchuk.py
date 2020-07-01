"""This module it's my homework

Functions:
execute_task1(lst):
lst -> list integer.
The function return the multiplication of items in the list.

execute_task2(lst):
lst -> list integer.
The function return the minimal number in the list.

execute_task3(lst):
lst -> list integer.
The function return the number of prime numbers in the list.

is_prime(number):
number -> integer.
The function checks whether the prime number. Returns True or False.

execute_task4(lst, number):
lst -> list integer.
number -> the number you want to remove from the list.
The function return the number of removed items.

execute_task5(lst1, lst2):
lst1 -> list integer.
lst2 -> list integer.
The function return third list created with unique items from lst1 and lst2.

execute_task6(lst, power):
lst -> list integer.
power -> the power to which each item in the list will be elevated.
The function return list."""

from random import randint

def execute_task1(lst):
    print("List:", lst)
    mult = 1
    for i in lst:
        mult *= i
    return mult

def execute_task2(lst):
    print("List:", lst)
    min_elem = lst[0]
    for i in range(1, len(lst)):
        if lst[i] < min_elem:
            min_elem = lst[i]
    return min_elem

def execute_task3(lst):
    print("List:", lst)
    count = 0
    for i in lst:
        if is_prime(i):
            count += 1
    return count

def is_prime(number):
    if number % 2 == 0 or number < 2:
        return number == 2
    d = 3
    while d * d <= number and number % d != 0:
        d += 2
    return d * d > number 

def execute_task4(lst, number):
    print("List:", lst)
    count = 0
    amount = lst.count(number)
    while amount != 0:
        lst.remove(lst[lst.index(number)])
        count += 1
        amount -= 1
    return count

def execute_task5(lst1, lst2):
    print("List1:", lst1)
    print("List2:", lst2)
    lst3 = list(set(lst1 + lst2))
    return lst3

def execute_task6(lst, power):
    print("List:", lst)
    for i in range(len(lst)):
        lst[i] **= power
    return lst


if __name__ == "__main__":
    while True:
        print("~~~~~~~~~~~~Menu~~~~~~~~~~~~")
        print("Execute task 1 -> enter 1")
        print("Execute task 2 -> enter 2")
        print("Execute task 3 -> enter 3")
        print("Execute task 4 -> enter 4")
        print("Execute task 5 -> enter 5")
        print("Execute task 6 -> enter 6")
        print("Exit           -> enter 7")
        choice = input("-> ")
        try:
            if choice == '1':
                print("\nTask 1")
                print("Mult:", execute_task1([i + randint(-5, 5) for i in range(5)]))
                input()
            elif choice == '2':
                print("\nTask 2")
                print("Min:", execute_task2([randint(-5, 5) for i in range(10)]))
                input()
            elif choice == '3':
                print("\nTask 3")
                print("Amount prime number:", execute_task3([randint(1, 20) for i in range(10)]))
                input()
            elif choice == '4':
                print("\nTask 4")
                number = int(input("Enter the number in range(1, 6) -> "))
                print("Amount removed items:", execute_task4([randint(1, 5) for i in range(15)], number))
                input()
            elif choice == '5':
                print("\nTask 5")
                print("List3:", execute_task5([i + randint(-5, 5) for i in range(5)], [i + randint(6, 10) for i in range(5)]))
                input()
            elif choice == '6':
                print("\nTask 6")
                power = int(input("Enter the power -> "))
                print("List after execute function:", execute_task6([randint(-5, 5) for i in range(5)], power))
                input()
            elif choice == '7':
                break
            else:
                print("Entered wrong data. Please try again.")
                input()
        except ValueError as ex:
            print("Error:", ex)
            input()