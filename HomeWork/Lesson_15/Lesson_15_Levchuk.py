from random import randint

def execute_task_1(A, B):
    """This function return the symmetric difference of two sets"""
    return A ^ B

def execute_task_2(A, C):
    """This function return the intersection of two sets"""
    return A & C

def execute_task_3(A, B, C):
    """This function return the union of three sets"""
    return A | B | C

if __name__ == "__main__":
    A = {randint(1, 20) for i in range(10)}
    B = {randint(1, 20) for i in range(10)}
    C = {randint(1, 20) for i in range(10)}
    print("~~~~~~~~~~ Sets ~~~~~~~~~~")
    print(f"A = {A}")
    print(f"B = {B}")
    print(f"C = {C}")
    input("Please press enter to continue")
    while True:
        print("~~~~~~~~~~~~ Menu ~~~~~~~~~~~~")
        print("Symmetric difference of A and B -> enter 1")
        print("Intersection of A and C         -> enter 2")
        print("Union of A, B and C             -> enter 3")
        print("Change sets                     -> enter 4")
        print("Exit                            -> enter 5")
        choice = input("-> ")
        if choice == '1':
            print("\nSymmetric difference of A and B")
            print(f"A = {A}")
            print(f"B = {B}")
            print(f"Result = {execute_task_1(A, B)}")
            input()
        elif choice == '2':
            print("\nIntersection of A and C")
            print(f"A = {A}")
            print(f"C = {C}")
            print(f"Result = {execute_task_2(A, C)}")
            input()
        elif choice == '3':
            print("\nUnion of A, B and C")
            print(f"A = {A}")
            print(f"B = {B}")
            print(f"C = {C}")
            print(f"Result = {execute_task_3(A, B, C)}")
            input()
        elif choice == '4':
            A = {randint(1, 20) for i in range(10)}
            B = {randint(1, 20) for i in range(10)}
            C = {randint(1, 20) for i in range(10)}
            print("~~~~~~~~~~ New Sets ~~~~~~~~~~")
            print(f"A = {A}")
            print(f"B = {B}")
            print(f"C = {C}")
            input("Please press enter to continue")
        elif choice == '5':
            break
        else:
            print("Entered wrong data. Please try again.")
            input()
