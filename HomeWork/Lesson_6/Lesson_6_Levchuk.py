# Пользователь вводит с клавиатуры два числа (начало и конец диапазона).
# Требуется проанализировать все
# числа в этом диапазоне по следующему правилу: если
# число кратно 7, его надо выводить на экран.
def execute_task1():
    try:
        first = int(input("Enter the start of range -> "))
        second = int(input("Enter the end of range -> ")) + 1
        print("Numbers are multiples of 7: ", end="")
        for i in range(first, second):
            if i % 7 == 0:
                print(f"{i} ", end="")
        print()
    except ValueError:
        print("Error. Incorrect data entered in execute_task1()")
    

# Пользователь вводит с клавиатуры два числа (начало и конец диапазона).
# Требуется проанализировать все числа в этом диапазоне. Нужно вывести на экран:
# 1. Все числа диапазона;
# 2. Все числа диапазона в убывающем порядке;
# 3. Все числа, кратные 7;
# 4. Количество чисел, кратных 5.
def execute_task2():
    try:
        first = int(input("Enter the start of range -> "))
        second = int(input("Enter the end of range -> ")) + 1
        print("All numbers in the range: ", end="")
        for i in range(first, second):
            print(f"{i} ", end="")
        print()

        print("All numbers in the range(reverse): ", end="")
        for i in range(second - 1, first - 1 , -1):
            print(f"{i} ", end="")
        print()

        print("Numbers are multiples of 7: ", end="")
        for i in range(first, second):
            if i % 7 == 0:
                print(f"{i} ", end="")
        print()

        count = 0
        for i in range(first, second):
            if i % 5 == 0:
                count += 1
        print(f"Count of numbers are multiples of 5: {count}")
    except ValueError:
        print("Error. Incorrect data entered in execute_task2()")


# Пользователь вводит с клавиатуры два числа (начало
# и конец диапазона). Требуется проанализировать все числа
# в этом диапазоне. Вывод на экран должен проходить по
# правилам, указанным ниже.
# Если число кратно 3 (делится на 3 без остатка) нужно
# вывести слово Fizz. Если число кратно 5 нужно вывсти слово Buzz.
# Если число кратно 3 и 5 нужно вывести
# Fizz Buzz. Если число не кратно не 3 и 5 нужно вывести само число.
def execute_task3():
    try:
        first = int(input("Enter the start of range -> "))
        second = int(input("Enter the end of range -> "))
        for i in range(first, second):
            if i % 3 == 0 and i % 5 == 0:
                print(f"{i} -> Fizz Buzz. ")
            elif i % 3 == 0:
                print(f"{i} -> Fizz. ")
            elif i % 5 == 0:
                print(f"{i} -> Buzz. ")
    except ValueError:
        print("Error. Incorrect data entered in execute_task3()")



if __name__ == "__main__":
    print("Task 1")
    print("=================================")
    execute_task1()
    print("=================================")
    input()

    print("\nTask 2")
    print("=================================")
    execute_task2()
    print("=================================")
    input()
        
    print("\nTask 3")
    print("=================================")
    execute_task3()
    print("=================================")