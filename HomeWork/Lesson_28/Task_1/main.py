from user_list import Data, UserList


if __name__ == "__main__":
    """Program entrypoint"""
    try:
        user_data_input = [int(i) for i in input("Enter numbers with a space: ").split(' ')]
        USER_LIST = UserList(*user_data_input)

        while True:
            print(f"""
            ~~~~~~~~~~~~~~~~~~
            SHOW: {Data.SHOW}
            ADD: {Data.ADD}
            EDIT: {Data.EDIT}
            DELETE: {Data.DELETE}
            FIND: {Data.FIND}
            EXIT: {Data.EXIT}
            ~~~~~~~~~~~~~~~~~~
            """)

            user_choise = int(input("Enter your choise: "))
            if user_choise == Data.EXIT:
                break

            elif user_choise == Data.SHOW:
                print(USER_LIST)
                input("Press Enter to continue...")

            elif user_choise == Data.ADD:
                user_input = int(input("Enter a number: "))
                USER_LIST.add(user_input)
                input("Press Enter to continue...")
                
            elif user_choise == Data.EDIT:
                user_input_a = int(input("Enter the number you want to replace: "))
                user_input_b = int(input("Enter the number to replace: "))
                USER_LIST.edit(a=user_input_a, b=user_input_b)
                input("Press Enter to continue...")

            elif user_choise == Data.DELETE:
                user_input = int(input("Enter the number to delete: "))
                USER_LIST.delete(user_input)
                input("Press Enter to continue...")

            elif user_choise == Data.FIND:
                user_input = int(input("Enter the number to find: "))
                res = USER_LIST.find(user_input)
                if res:
                    print(f"Number {user_input} is found at the position: {res}")
                input("Press Enter to continue...")

            else:
                print("Enter correct data!")
                input("Press Enter to continue...")
    except ValueError:
        print("Numbers only")
        input("Press Enter to continue...")