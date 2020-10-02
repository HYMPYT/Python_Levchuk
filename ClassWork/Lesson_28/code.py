class UserList:
    def __init__(self):
        self.__user_list = []

    def add_num(self, num):
        if self.__approve_number(num):
            self.__user_list.append(num)

    def __approve_number(self, num) -> bool:
        if num not in self.__user_list:
            return True
        answer = input("Do yo want to add this number? (y/n): ")
        return True if answer.lower() == 'y' else None

    def edit_number(self, old_value, new_value):
        pass

    def __str__(self) -> str:
        return f"List: {self.__user_list}"


if __name__ == "__main__":
    #! CONSTS
    USER_LIST = UserList()
    ADD_NUMBER = 'add'
    EDIT_NUMBER = 'edit'
    SHOW_LIST = 'show'
    EXIT = 'q'


    while True:
        print(f"""
        Choices:
            ADD_NUMBER = {ADD_NUMBER}
            EDIT_NUMBER = {EDIT_NUMBER}
            SHOW_LIST = {SHOW_LIST}
            EXIT = {EXIT}
        ---------------------------

        """)
        choice = input("Your choice: ")

        if choice == EXIT:
            break

        elif choice == ADD_NUMBER:
            num = int(input("Enter the number: "))
            USER_LIST.add_num(num)
            print(USER_LIST)

        elif choice == EDIT_NUMBER:
            num_1 = int(input("Enter the old number: "))
            num_2 = int(input("Enter the new number: "))

        elif choice == SHOW_LIST:
            print(USER_LIST)


