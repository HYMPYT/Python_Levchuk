def execute_task_1():
    """ Task 1
    There are three tuples of integers you need to find
    elements that are in all tuples."""
    t1 = (1, 2, 6, 4, 12)
    t2 = (3, 5, 6, 17, 12)
    t3 = (6, 5, 2, 4, 12)
    print("Tuple 1:", t1)
    print("Tuple 2:", t2)
    print("Tuple 3:", t3)
    print("Elements that are in all tuples:", end=" ")
    for i in t1:
        if i in t2 and i in t3:
            print(i, end=" ")

def execute_task_2():
    """ Task 2
    There are three tuples of integers you need to find
    items that are unique to each list."""
    t1 = (1, 2, 6, 8, 12)
    t2 = (3, 5, 6, 17, 12)
    t3 = (6, 5, 2, 4, 9)
    print("Tuple 1:", t1)
    print("Tuple 2:", t2)
    print("Tuple 3:", t3)
    print("Unique elements for t1:", end=" ")
    for i in t1:
        if i not in t2 and i not in t3 and t1.count(i) == 1:
            print(i, end=" ")

    print("\nUnique elements for t2:", end=" ")
    for i in t2:
        if i not in t1 and i not in t3 and t2.count(i) == 1:
            print(i, end=" ")

    print("\nUnique elements for t3:", end=" ")
    for i in t3:
        if i not in t1 and i not in t2 and t3.count(i) == 1:
            print(i, end=" ")

def execute_task_3():
    """ Task 3
    There are three tuples of integers, you need to find the elements that are in each of the tuples and are
    in each tuple at the same position."""
    t1 = (1, 2, 6, 8, 12)
    t2 = (1, 2, 6, 17, 12)
    t3 = (1, 5, 2, 4, 12)
    print("Tuple 1:", t1)
    print("Tuple 2:", t2)
    print("Tuple 3:", t3)
    print("Same elements at the same position:", end=" ")
    for i in range(len(t1)):
        if t1[i] == t2[i] and t1[i] == t3[i]:
            print(t1[i], end=" ")

if __name__ == "__main__":
    while True:
        print("~~~~~~~~~~~~Menu~~~~~~~~~~~~")
        print("Task 1 -> enter 1")
        print("Task 2 -> enter 2")
        print("Task 3 -> enter 3")
        print("Exit   -> enter 4")
        choice = input("-> ")
        if choice == '1':
            print("\nTask 1")
            execute_task_1()
            input()
        elif choice == '2':
            print("\nTask 2")
            execute_task_2()
            input()
        elif choice == '3':
            print("\nTask 3")
            execute_task_3()
            input()
        elif choice == '4':
            break
        else:
            print("Entered wrong data. Please try again.")
            input()