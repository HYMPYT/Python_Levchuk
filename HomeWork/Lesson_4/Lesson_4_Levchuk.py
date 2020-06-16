def main():
    print("Task 1")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    execute_task1()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    input()
    print("\nTask 2")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    execute_task2()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    input()
    print("\nTask 3")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    execute_task3()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# Користувач вводить 3 числа. 
# Далі в залежності від вибору користувача потрібно знайти суму або добуток цих чисел. 
# (Тобто програма запитує в користувача, що потрібно зробити)
def execute_task1():
    first = float(input("Enter the first number -> "))
    second = float(input("Enter the second number -> "))
    third = float(input("Enter the third number -> "))
    choice = ""
    print('\nIf you want to perform multiplication, enter "mult"\nIf you want to find the sum, enter "sum"')
    while True:
        choice = input("Your choice -> ")
        if choice.lower() == "mult":
            print("\nMult:", first * second * third)
            break
        elif choice.lower() == "sum":
            print("\nSum:", first + second + third)
            break
        else:
            print("Wrong data. Please try again")

# Користувач вводить 3 числа. 
# Далі в залежності від вибору користувача потрібно знайти найбільше з 3-х, 
# найменше, або середнє арифметичне. (Подібно до 1-го)
def execute_task2():
    first = float(input("Enter the first number -> "))
    second = float(input("Enter the second number -> "))
    third = float(input("Enter the third number -> "))
    choice = ""
    print("\n\tMenu\n1.Max number press 1\n2.Min number press 2\n3.Average press 3")
    while True:
        choice = input("Your choice -> ")
        if choice == "1":
            print("\nMax =", max(first, second, third))
            break
        elif choice == "2":
            print("\nMin =", min(first, second, third))
            break
        elif choice == "3":
            print("\nAvarage =", round((first + second + third) / 3, 3))
            break
        else:
            print("Wrong data. Please try again")

# Користувач вводить з клавіатури кількість метрів. 
# В залежності від вибору - програма конвертує їх в сантиметри, міліметри, або кілометри.
def execute_task3():
    value = float(input("Enter the number of meters -> "))
    choice = ""
    print("\n\tMenu\n1.In centimeters press 1\n2.In millimeters press 2\n3.In kilometers press 3")
    while True:
        choice = input("Your choice -> ")
        if choice == "1":
            print("\nCentimeters =", value * 100)
            break
        elif choice == "2":
            print("\nMillimeters =", value * 1000)
            break
        elif choice == "3":
            print("\nKilometers =", value * 0.001)
            break
        else:
            print("Wrong data. Please try again")

# Функція для знаходження максимального числа з трьох  
def max(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

# Функція для знаходження мінімального числа з трьох
def min(a, b, c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    else:
        return c

# Виклик функції main()
main()