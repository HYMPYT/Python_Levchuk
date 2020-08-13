from pprint import pprint

def get_footballers(footballers: list) -> list:
    """This function return the list of footballers."""
    return footballers

def print_result(*args) -> None:
    """This function prints the elements that are passed as a parameter."""
    for element in args:
        pprint(element, width=1)
        input('Press Enter to continue...')

def add_footballer(first_name: str, surname: str, middle_name: str) -> dict:
    """This function is for adding football player."""
    global FOOTBALLERS
    footballer = {
        "First name": first_name,
        "Surname": surname,
        "Middle name": middle_name
    }
    FOOTBALLERS.append(footballer)
    return footballer

def del_footballer(surname: str) -> dict:
    """This function is for deleting football player.
    The key to the search is the surname of the football player."""
    global FOOTBALLERS
    deleted_footballer = {}
    for index, footballer in enumerate(FOOTBALLERS):
        if footballer['Surname'] == surname:
            deleted_footballer = footballer
            del(FOOTBALLERS[index])
            return deleted_footballer

def update_footballer(surname: str) -> dict:
    """This function is for editing the football player information fields.
    The key to the search is the surname of the football player."""
    global FOOTBALLERS
    for footballer in FOOTBALLERS:
        if footballer['Surname'] == surname:
            first_name = footballer["First name"]
            surname = footballer["Surname"]
            middle_name = footballer["Middle name"]
            new_first_name = input(f"Enter first name ({first_name} - default): ")
            new_surname = input(f"Enter surname ({surname} - default): ")
            new_middle_name = input(f"Enter middle name ({middle_name} - default): ")
            if new_first_name:
                footballer['First name'] = new_first_name
            if new_surname:
                footballer['Surname'] = new_surname
            if new_middle_name:
                footballer['Middle name'] = new_middle_name
            return footballer

def search_footballer(surname: str) -> dict:
    """This function for search footballer.
    Key for search is the surname of footballer."""
    global FOOTBALLERS
    for footballer in FOOTBALLERS:
        if footballer['Surname'] == surname:
            return footballer
    return f"Footballer {surname} does not exist\n"
    
if __name__ == "__main__":
    # ! CONSTS
    FOOTBALLERS_LIST = 'list'
    ADD_FOOTBALLER = 'add'
    DEL_FOOTBALLER = 'delete'
    UPDATE_FOOTBALLER = 'update'
    SEARCH_FOOTBALLER = 'search'
    EXIT = 'q'
    FOOTBALLERS = []

    while True:
        print(f'''
        Choices:
        FOOTBALLERS_LIST -> {FOOTBALLERS_LIST}
        ADD_FOOTBALLER -> {ADD_FOOTBALLER}
        DEL_FOOTBALLER -> {DEL_FOOTBALLER}
        UPDATE_FOOTBALLER -> {UPDATE_FOOTBALLER}
        SEARCH_FOOTBALLER -> {SEARCH_FOOTBALLER}
        EXIT -> {EXIT}
        ---------------------
        ''')

        choice = input('Enter choice: ')
        if choice == EXIT:
            break

        elif choice == FOOTBALLERS_LIST:
            footballers = get_footballers(FOOTBALLERS)
            print_result(footballers)

        elif choice == ADD_FOOTBALLER:
            first_name = input('Enter first name: ')
            surname = input('Enter first name: ')
            middle_name = input('Enter first name: ')
            footballer = add_footballer(
                first_name=first_name,
                surname=surname,
                middle_name=middle_name
            )
            print_result(footballer)

        elif choice == DEL_FOOTBALLER:
            surname = input("Enter footballers surname: ")
            footballer = del_footballer(surname=surname)
            print_result(footballer)

        elif choice == UPDATE_FOOTBALLER:
            surname = input("Enter surname: ")
            footballer = update_footballer(surname=surname)
            print_result(footballer)

        elif choice == SEARCH_FOOTBALLER:
            surname = input("Enter surname: ")
            footballer = search_footballer(surname=surname)
            print_result(footballer)

        else:
            print("Entered wrong data. Please try again.")
            input("Press Enter to continue...")