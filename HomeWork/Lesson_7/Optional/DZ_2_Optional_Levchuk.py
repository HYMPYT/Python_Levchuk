from random import randint
# Пользователь вводит с клавиатуры арифметическое
# выражение. Например, 23+12.
# Необходимо вывести на экран результат выражения.
# В нашем примере это 35. Арифметическое выражение
# может состоять только из трёх частей: число, операция,
# число. Возможные операции: +, -,*,/
def execute_task1():
    string = input("Enter arithmetic expression -> ")
    try:
        if '+' in string:
            lst = string.split('+')
            res = int(lst[0]) + int(lst[1])
        elif '-' in string:
            lst = string.split('-')
            res = int(lst[0]) - int(lst[1])
        elif '*' in string:
            lst = string.split('*')
            res = int(lst[0]) * int(lst[1])
        elif '/' in string:
            lst = string.split('/')
            res = int(lst[0]) / int(lst[1])
        else:
            raise Exception("Entered wrong operation. Example: +, -, *, /")

        print(f"Result: {res}")

    except ValueError as e:
        print(f"Error: {e}\nEntered wrong data.")
    except Exception as e:
        print(f"Error: {e}")

# В списке целых, заполненном случайными числами,
# определить минимальный и максимальный элементы,
# посчитать количество отрицательных элементов, посчитать
# количество положительных элементов, посчитать
# количество нулей. Результаты вывести на экран.
def execute_task2():
    lst = list()
    lst = fill_list(lst)
    print_list(lst)
    negative_count = 0
    positive_count = 0
    zero_count = 0
    for i in lst:
        if i > 0:
            positive_count += 1
        elif i < 0:
            negative_count += 1
        else:
            zero_count += 1

    print(f"Max: {max(lst)}\nMin: {min(lst)}\nCount of negative numbers: {negative_count}\nCount of postive numbers: {positive_count}\nCount of zero: {zero_count}")

def fill_list(lst):
    i = 0
    while i < 20:
        lst.append(randint(-5, 5))
        i += 1
    return lst

def print_list(lst):
    print("List: ", end='')
    for i in lst:
        print(i, end=' ')
    print()

if __name__ == "__main__":
    execute_task2()