def palindrome(string: str) -> bool:
    """This function checks whether the string is entered by the palindrome."""
    if ' ' in string:
        string = "".join(string.split())

    if string.lower() == string[::-1].lower():
        return True
    else:
        return False

def edit_text(text: list, words: list) -> str:
    """This function translates to uppercase all reserved words in the text."""
    for i in range(len(text)):
        for j in words:
            if text[i].lower() == j.lower():
                text[i] = text[i].upper()
    return " ".join(text)

def number_of_sentences_in_text(text: str) -> int:
    """This function returns the number of sentences in the text."""
    return text.count('. ') + text.count('! ') + text.count('? ')


if __name__ == "__main__":
    #! CONSTS
    TASK_1 = "1"
    TASK_2 = "2"
    TASK_3 = "3"
    EXIT = "q"

    while True:
        print(f'''
        Choices:
        TASK_1 -> {TASK_1}
        TASK_2 -> {TASK_2}
        TASK_3 -> {TASK_3}
        EXIT -> {EXIT}
        ------------------
        ''')

        choice = input('Enter choice: ')
        
        if choice == EXIT:
            break
        
        elif choice == TASK_1:
            string = input("Enter the string -> ")
            if palindrome(string):
                print(f'\nString "{string}" is palindrome')
            else:
                print(f'\nString "{string}" isn\'t palindrome')
            input("\nPress Enter to continue...")

        elif choice == TASK_2:
            text = input("Enter some text separated by spaces -> ").split()
            words = input("Enter a list of reserved words separated by spaces -> ").split()
            print(f"\nYour text: {edit_text(text, words)}")
            input("\nPress Enter to continue...")

        elif choice == TASK_3:
            text = input("Enter some text ending with space. Example: (Qwerty. ) -> ")
            print(f"\nNumber of sentences -> {number_of_sentences_in_text(text)}")
            input("\nPress Enter to continue...")

        else:
            print("Entered wrong data. Please try again.")
            input("Press Enter to continue...")