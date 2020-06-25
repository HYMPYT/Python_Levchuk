from random import randint

def fill_list(lst, size):
    i = 0
    while i < size:
        lst.append(randint(-10, 10))
        i+=1
    return lst

def display_list(lst, list_name):
    print(f"{list_name}: ", end="")
    for i in lst:
        print(f"{i} ", end=" ")
    print()

# Сформировать третий список, содержащий элементы
# обоих списков;
def execute_task_exercise1(lst1, lst2):
    lst3 = lst1 + lst2
    display_list(lst3, "lst3")

# Сформировать третий список, содержащий элементы
# обоих списков без повторений;
def execute_task_exercise2(lst1, lst2):
    lst3 = lst1 + lst2
    i = 0
    while i < len(lst3):
        if lst3.count(lst3[i]) > 1:
            del lst3[i]
        else:
            i += 1
    display_list(lst3, "lst3")

# Сформировать третий список, содержащий элементы
# общие для двух списков;
def execute_task_exercise3(lst1, lst2):
    lst3 = []
    for i in lst1:
        if i in lst2 and i not in lst3:
            lst3.append(i)
    display_list(lst3, "lst3")

# Сформировать третий список, содержащий только
# уникальные элементы каждого из списков;
def execute_task_exercise4(lst1, lst2):
    lst3 = []
    for i in lst1:
        if lst1.count(i) == 1:
            lst3.append(i)
    for i in lst2:
        if lst2.count(i) == 1:
            lst3.append(i)
    display_list(lst3, "lst3")

# Сформировать третий список, содержащий только
# минимальное и максимальное значение каждого из
# списков.
def execute_task_exercise5(lst1, lst2):
    lst3 = []
    lst3.append(min(lst1))
    lst3.append(max(lst1))
    lst3.append(min(lst2))
    lst3.append(max(lst2))
    display_list(lst3, "lst3")

if __name__ == "__main__":
    try:
        size1 = int(input("Enter the size of first list -> "))
        size2 = int(input("Enter the size of second list -> "))
        lst1 = []
        lst2 = []
        # Два списка целых заполняются случайными числами.
        lst1 = fill_list(lst1, size1)
        lst2 = fill_list(lst2, size2)
        
        display_list(lst1, "lst1")
        display_list(lst2, "lst2")

        print("\nExercise 1")
        print('-' * 40)
        execute_task_exercise1(lst1, lst2)
        print('-' * 40)
        print("\nExercise 2")
        print('-' * 40)
        execute_task_exercise2(lst1, lst2)
        print('-' * 40)
        print("\nExercise 3")
        print('-' * 40)
        execute_task_exercise3(lst1, lst2)
        print('-' * 40)
        print("\nExercise 4")
        print('-' * 40)
        execute_task_exercise4(lst1, lst2)
        print('-' * 40)
        print("\nExercise 5")
        print('-' * 40)
        execute_task_exercise5(lst1, lst2)
        print('-' * 40)
    except ValueError:
        print("Entered incorrect value")