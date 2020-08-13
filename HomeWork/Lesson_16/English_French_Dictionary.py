from pprint import pprint

def print_result(*args) -> None:
    """This function prints the elements that are passed as a parameter."""
    for element in args:
        pprint(element, width=1)
        input('Press Enter to continue...')

def add_word(english: str, french: str) -> dict:
    """This function is for adding new word to the dictionary."""
    global WORDS
    word = {
        "English": english,
        "French": french
    }
    WORDS.append(word)
    return word

def del_word(english: str) -> dict:
    """This function is for deleting word.
    The key to the search is a word from dictionary in english."""
    global WORDS
    deleted_word = {}
    for index, word in enumerate(WORDS):
        if word['English'] == english:
            deleted_word = word
            del(WORDS[index])
            return deleted_word

def update_word(english: str) -> dict:
    """This function is for editing the word information fields.
    The key to the search is a word from dictionary in english."""
    global WORDS
    for word in WORDS:
        if word['English'] == english:
            english = word['English']
            french = word['French']
            new_english = input(f"Enter english word ({english} - default): ")
            new_french = input(f'Enter translation of "{english}" in french ({french} - default): ')
            if new_english:
                word['English'] = new_english
            if new_french:
                word['French'] = new_french

            return word

def search_word(english: str) -> dict:
    """This function for search word.
    The key to the search is a word from dictionary in english."""
    global WORDS
    for word in WORDS:
        if word['English'] == english:
            return word
    return f"Word {english} does not exist\n"
    
if __name__ == "__main__":
    # ! CONSTS
    WORDS_LIST = 'list'
    ADD_WORD = 'add'
    DEL_WORD = 'delete'
    UPDATE_WORD = 'update'
    SEARCH_WORD = 'search'
    EXIT = 'q'
    WORDS = [
        {
            "English": "Father",
            "French": "Père"
        },
        {
            "English": "Pencil",
            "French": "Crayon"
        },
        {
            "English": "Pen",
            "French": "Stylo"
        },
        {
            "English": "Flower",
            "French": "Fleur"
        }
    ]

    while True:
        print(f'''
        Choices:
        WORDS_LIST -> {WORDS_LIST}
        ADD_WORD -> {ADD_WORD}
        DEL_WORD -> {DEL_WORD}
        UPDATE_WORD -> {UPDATE_WORD}
        SEARCH_WORD -> {SEARCH_WORD}
        EXIT -> {EXIT}
        ---------------------
        ''')

        choice = input('Enter choice: ')
        if choice == EXIT:
            break

        elif choice == WORDS_LIST:
            if len(WORDS) > 1:
                print("\n~~~~~~ Words ~~~~~~")
            else:
                print("\n~~~~~~ Word ~~~~~~")
            print_result(WORDS)

        elif choice == ADD_WORD:
            english = input('Enter english word: ')
            french = input(f'Enter translation of "{english}" in french: ')
            
            word = add_word(
                english=english,
                french=french
            )
            print("\n~~~~~~ Word ~~~~~~")
            print_result(word)

        elif choice == DEL_WORD:
            english = input("Enter english word: ")
            word = del_word(english=english)
            print("\n~~~~~~ Word ~~~~~~")
            print_result(word)

        elif choice == UPDATE_WORD:
            english = input("Enter english word: ")
            word = update_word(english=english)
            print("\n~~~~~~ Word ~~~~~~")
            print_result(word)

        elif choice == SEARCH_WORD:
            english = input("Enter english word: ")
            word = search_word(english=english)
            print("\n~~~~~~ Word ~~~~~~")
            print_result(word)

        else:
            print("Entered wrong data. Please try again.")
            input("Press Enter to continue...")