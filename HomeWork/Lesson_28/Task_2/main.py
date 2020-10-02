from string_stack import StringStack


if __name__ == "__main__":
    # ! CONSTS
    ADD_STRING = 'add'
    DEL_STRING = 'del'
    STRING_COUNT = 'count'
    IS_EMPTY = 'empty'
    IS_FULL = 'full'
    CLEAR = 'cls'
    GET_STRING = 'get'
    EXIT = 'q'
    STACK = StringStack()

    while True:
        print(f'''
        ADD_STRING = {ADD_STRING}
        DEL_STRING = {DEL_STRING}
        STRING_COUNT = {STRING_COUNT}
        IS_EMPTY = {IS_EMPTY}
        IS_FULL = {IS_FULL}
        CLEAR = {CLEAR}
        GET_STRING = {GET_STRING}
        EXIT = {EXIT}
        -------------------------
        ''')
        choice = input("Your choice: ")
        try:
            if choice == EXIT:
                break

            elif choice == ADD_STRING:
                string = input("Enter string: ")
                print(f"Message: {STACK.push(string)}")
                input("Press Enter to continue...")

            elif choice == DEL_STRING:
                res = STACK.pop()
                print(f'Result: {res[0]}\nMessage: {res[1]}')
                input("Press Enter to continue...")

            elif choice == STRING_COUNT:
                print(f"Amount of strings: {len(STACK)}")
                input("Press Enter to continue...")

            elif choice == IS_EMPTY:
                if STACK.is_empty():
                    print("Message: stack is empty")
                else:
                    print("Message: stack is not empty")
                input("Press Enter to continue...")

            elif choice == IS_FULL:
                if STACK.is_full():
                    print("Message: stack is full")
                else:
                    print("Message: stack is not full")
                input("Press Enter to continue...")

            elif choice == CLEAR:
                print(f"Message: {STACK.clear()}")
                input("Press Enter to continue...")

            elif choice == GET_STRING:
                key = int(input("Enter index: "))
                res = STACK[key]
                print(f'Result: {res[0]}\nMessage: {res[1]}')
                input("Press Enter to continue...")

            else:
                print("Entered wrong data. Please try again.")
                input("Press Enter to continue...")

        except ValueError:
            print("The number must be an integer type")
            input("Press Enter to continue...")

        except IndexError as e:
            print(f"Error: {e}")
            input("Press Enter to continue...")
