# Напишите функцию, которая отображает на экран
# форматированный текст, указанный ниже:
def execute_task1():
    print('"Don\'t compare yourself with anyone in this world...\nif you do so, you are insulting yourself."\n\t\t\t\t\t   Bill Gates')

# Напишите функцию, которая принимает два числа
# в качестве параметра и отображает все четные числа
# между ними.
def execute_task2(first, second):
    print("Even numbers: ", end="")
    for i in range(first + 1, second):
        if i % 2 == 0:
            print(i, end=" ")
    print() 

# Напишите функцию, которая отображает пустой или
# заполненный квадрат из некоторого символа. Функция
# принимает в качестве параметров: длину стороны ква-
# драта, символ и переменную логического типа:
# ■■ если она равна True, квадрат заполненный;
# ■■ если False, квадрат пустой.
def execute_task3(length, symbol, flag):
    if flag:
        for i in range(length):
            print(symbol * length)
    else:
        for i in range(length):
            if i == 0 or i == length - 1:
                print(symbol * length)
            else:
                print(symbol + ' ' * (length - 2) + symbol)

# Напишите функцию, которая возвращает минимальное
# из пяти чисел. Числа передаются в качестве параметров.
def execute_task4(*params):
    min_elem = params[0]
    for i in params[1:]:
        if min_elem > i:
            min_elem = i
    return min_elem

# Напишите функцию, которая возвращает произве-
# дение чисел в указанном диапазоне. Границы диапазона
# передаются в качестве параметров. Если границы диапа-
# зона перепутаны (например, 5 — верхняя граница, 25 —
# нижняя граница), их нужно поменять местами.
def execute_task5(first, second):
    if first > second:
        first, second = second, first
    mult = 1
    for i in range(first, second):
        mult *= i
    return mult

# Напишите функцию, которая считает количество
# цифр в числе. Число передаётся в качестве параметра. Из
# функции нужно вернуть полученное количество цифр.
def execute_task6(number):
    count = 0
    while number:
        count += 1
        number //= 10
    return count

# Напишите функцию, которая проверяет является ли
# число палиндромом. Число передаётся в качестве пара-
# метра. Если число палиндром нужно вернуть из функции
# true, иначе false.
def execute_task7(number):
    lst = []
    while number:
        lst.append(number % 10)
        number //= 10
    for a, b in zip(lst, reversed(lst)):
        if not a == b:
            return False
    else:
        return True

if __name__ == "__main__":
    while True:
        print("~~~~~~~~~~~~Menu~~~~~~~~~~~~")
        print("Execute task 1 -> enter 1")
        print("Execute task 2 -> enter 2")
        print("Execute task 3 -> enter 3")
        print("Execute task 4 -> enter 4")
        print("Execute task 5 -> enter 5")
        print("Execute task 6 -> enter 6")
        print("Execute task 7 -> enter 7")
        print("Exit           -> enter 8")
        choice = input("-> ")
        try:
            if choice == '1':
                print("\nTask 1")
                execute_task1()
                input()
            elif choice == '2':
                print("\nTask 2")
                first = int(input("Enter the start of range -> "))
                second = int(input("Enter the end of range -> "))
                execute_task2(first, second)
                input()
            elif choice == '3':
                print("\nTask 3")
                length = int(input("Enter the length of the square -> "))
                symbol = input("Enter some symbol -> ")
                flag = bool(int(input("Enter 1 - filled square 0 - empty -> ")))
                execute_task3(length, symbol, flag)
                input()
            elif choice == '4':
                print("\nTask 4")
                a = int(input("Enter the number -> "))
                b = int(input("Enter the number -> "))
                c = int(input("Enter the number -> "))
                d = int(input("Enter the number -> "))
                e = int(input("Enter the number -> "))
                print(f"Min: {execute_task4(a, b, c, d, e)}")
                input()
            elif choice == '5':
                print("\nTask 5")
                first = int(input("Enter the start of range -> "))
                second = int(input("Enter the end of range -> "))
                print(f"Mult: {execute_task5(first, second)}")
                input()
            elif choice == '6':
                print("\nTask 6")
                num = int(input("Enter the number -> "))
                print(f"Number of digits: {execute_task6(num)}")
                input()
            elif choice == '7':
                print("\nTask 7")
                num = int(input("Enter the number -> "))
                print(f"Number: {num} is palindrome? {execute_task7(num)}")
                input()
            elif choice == '8':
                break
            else:
                print("Entered wrong data. Please try again.")
                input()
        except ValueError as ex:
            print(f"Error: {ex}")
            input()