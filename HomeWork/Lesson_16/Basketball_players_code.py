from pprint import pprint

def print_result(*args) -> None:
    """This function prints the elements that are passed as a parameter."""
    for element in args:
        pprint(element, width=1)
        input('Press Enter to continue...')

def add_basketball_player(first_name: str, surname: str, middle_name: str, height: float) -> dict:
    """This function is for adding basketball player."""
    global BASKETBALL_PLAYERS
    basketball_player = {
        "First name": first_name,
        "Surname": surname,
        "Middle name": middle_name,
        "Height": height
    }
    BASKETBALL_PLAYERS.append(basketball_player)
    return basketball_player

def del_basketball_player(surname: str) -> dict:
    """This function is for deleting basketball player.
    The key to the search is the surname of the basketball player."""
    global BASKETBALL_PLAYERS
    deleted_basketball_player = {}
    for index, basketball_player in enumerate(BASKETBALL_PLAYERS):
        if basketball_player['Surname'] == surname:
            deleted_basketball_player = basketball_player
            del(BASKETBALL_PLAYERS[index])
            return deleted_basketball_player

def update_basketball_player(surname: str) -> dict:
    """This function is for editing the basketball player information fields.
    The key to the search is the surname of the basketball player."""
    global BASKETBALL_PLAYERS
    for basketball_player in BASKETBALL_PLAYERS:
        if basketball_player['Surname'] == surname:
            first_name = basketball_player['First name']
            surname = basketball_player['Surname']
            middle_name = basketball_player['Middle name']
            height = basketball_player['Height']
            new_first_name = input(f"Enter first name ({first_name} - default): ")
            new_surname = input(f"Enter surname ({surname} - default): ")
            new_middle_name = input(f"Enter middle name ({middle_name} - default): ")

            try:
                new_height = float(input(f"Enter height ({height} - default): "))
                basketball_player['Height'] = new_height
            except ValueError as e:
                print(f'\nError: {e}.\nField "Height" not changed.\n')
                input('Press Enter to continue...')

            if new_first_name:
                basketball_player['First name'] = new_first_name
            if new_surname:
                basketball_player['Surname'] = new_surname
            if new_middle_name:
                basketball_player['Middle name'] = new_middle_name

            return basketball_player

def search_basketball_player(surname: str) -> dict:
    """This function for search basketball player.
    The key for search is the surname of basketball player."""
    global BASKETBALL_PLAYERS
    for basketball_player in BASKETBALL_PLAYERS:
        if basketball_player['Surname'] == surname:
            return basketball_player
    return f"Basketball_player {surname} does not exist\n"
    
if __name__ == "__main__":
    # ! CONSTS
    BASKETBALL_PLAYERS_LIST = 'list'
    ADD_BASKETBALL_PLAYER = 'add'
    DEL_BASKETBALL_PLAYER = 'delete'
    UPDATE_BASKETBALL_PLAYER = 'update'
    SEARCH_BASKETBALL_PLAYER = 'search'
    EXIT = 'q'
    BASKETBALL_PLAYERS = [
        {
            "First name": "Michael",
            "Surname": "Jordan",
            "Middle name": "Jeffrey",
            "Height": 198
        },
        {
            "First name": "Jerry",
            "Surname": "Lucas",
            "Middle name": "Ray",
            "Height": 203
        }
    ]

    while True:
        print(f'''
        Choices:
        BASKETBALL_PLAYERS_LIST -> {BASKETBALL_PLAYERS_LIST}
        ADD_BASKETBALL_PLAYER -> {ADD_BASKETBALL_PLAYER}
        DEL_BASKETBALL_PLAYER -> {DEL_BASKETBALL_PLAYER}
        UPDATE_BASKETBALL_PLAYER -> {UPDATE_BASKETBALL_PLAYER}
        SEARCH_BASKETBALL_PLAYER -> {SEARCH_BASKETBALL_PLAYER}
        EXIT -> {EXIT}
        ---------------------
        ''')

        choice = input('Enter choice: ')
        if choice == EXIT:
            break

        elif choice == BASKETBALL_PLAYERS_LIST:
            if len(BASKETBALL_PLAYERS) > 1:
                print("\n~~~~~~ Basketall players ~~~~~~")
            else:
                print("\n~~~~~~ Basketall player ~~~~~~")
            print_result(BASKETBALL_PLAYERS)

        elif choice == ADD_BASKETBALL_PLAYER:
            first_name = input('Enter first name: ')
            surname = input('Enter surname: ')
            middle_name = input('Enter middle name: ')
            try:
                height = float(input('Enter height: '))
            except ValueError as e:
                height = 0.0
                print(f'\nError: {e}.\nFor height was used default value: 0.\nIf you want to change it use the command "update"\n')
                input("\nPress Enter to continue...")
            
            basketball_player = add_basketball_player(
                first_name=first_name,
                surname=surname,
                middle_name=middle_name,
                height=height
            )
            print("\n~~~~~~ Basketall player ~~~~~~")
            print_result(basketball_player)

        elif choice == DEL_BASKETBALL_PLAYER:
            surname = input("Enter surname: ")
            basketball_player = del_basketball_player(surname=surname)
            print("\n~~~~~~ Basketall player ~~~~~~")
            print_result(basketball_player)

        elif choice == UPDATE_BASKETBALL_PLAYER:
            surname = input("Enter surname: ")
            basketball_player = update_basketball_player(surname=surname)
            print("\n~~~~~~ Basketall player ~~~~~~")
            print_result(basketball_player)

        elif choice == SEARCH_BASKETBALL_PLAYER:
            surname = input("Enter surname: ")
            basketball_player = search_basketball_player(surname=surname)
            print("\n~~~~~~ Basketall player ~~~~~~")
            print_result(basketball_player)

        else:
            print("Entered wrong data. Please try again.")
            input("Press Enter to continue...")