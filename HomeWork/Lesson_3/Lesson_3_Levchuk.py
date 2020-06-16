def main():
    print("Task1")
    print("==========================")
    execute_task1()
    input()
    print("==========================")

    print()
    print("Task2")
    print("==========================")
    execute_task2()
    input()
    print("==========================")

    print()
    print("Task3")
    print("==========================")
    execute_task3()
    input()
    print("==========================")

    print()
    print("Task4")
    print("==========================")
    execute_task4()
    input()
    print("==========================")

    print()
    print("Task5")
    print("==========================")
    execute_task5()
    print("==========================")


# Пользователь вводит с клавиатуры три цифры. 
# Необходимо создать число, содержащее эти цифры. Например,
# если с клавиатуры введено 1, 5, 7, тогда нужно сформировать число 157.
def execute_task1():
    first = input("Enter the first number -> ")
    second = input("Enter the second number -> ")
    third = input("Enter the third number -> ")
    result = int(first + second + third)
    print("Result:", result)


# Пользователь вводит с клавиатуры число, состоящее
# из четырех цифр. Требуется найти произведение цифр.
# Например, если с клавиатуры введено 1324, тогда результат 
# произведения 1*3*2*4 = 24.
def execute_task2():
    value = int(input("Enter the number -> "))
    mult = 1
    while value:
        mult *= value % 10
        value = int(value / 10)
    print("Mult:", mult)


# Пользователь вводит с клавиатуры количество метров.
# Требуется вывести результат перевода метров в сантиметры,
# дециметры, миллиметры, мили.
def execute_task3():
    value = float(input("Enter the number of meters -> "))
    print("Meters -> Centimeters:", value * 100)
    print("Meters -> Decimeters:", value * 10)
    print("Meters -> Millimeters:", value * 1000)
    print("Meters -> Miles:", round(value * 0.000621371192, 5))


# Напишите программу, вычисляющую площадь треугольника.
# Пользователь с клавиатуры вводит размер
# основания треугольника и размер высоты.
def execute_task4():
    height = float(input("Enter the height of the triangle -> "))
    osnova = float(input("Enter the base of the triangle -> "))
    print("Square of the triangle:", height * osnova / 2)


# Пользователь с клавиатуры вводит четырёхзначное
# число. Необходимо перевернуть число и отобразить
# результат. Например, если введено 4512, результат 2154.
def execute_task5():
    value = int(input("Enter the number -> "))
    num = ""
    while value:
        num += str(value % 10)
        value = int(value / 10)
    print("Result:", num)    


# Виклик функції main()
main()
