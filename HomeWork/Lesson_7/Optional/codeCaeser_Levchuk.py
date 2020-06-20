def menu():
    choice = "0"
    while True:
        print("\n\n\n\n~~~~~~~~~~~~~~~MENU~~~~~~~~~~~~~~~")
        print("1. Encrypting the text enter 1")
        print("2. Deciphering the text enter 2")
        print("3. Exit enter 3")
        choice = input("Your choice -> ")
        try:
            if choice == '3':
                break
            else:
                string = input("\nEnter your text -> ")
                key = int(input("Enter the key [-4; 4] -> "))
                if choice == '1':
                    result = encrypt(string, key)
                elif choice == '2':
                    result = decipher(string, key)
                else:
                    print("Entered wrong data. Please try again.")

            print(f"Your text after working program: {result}")
            input()
        except ValueError as e:
            print(f"Error: {e}\nTry again anter all data")


def encrypt(string, key):
    string = list(string)
    for i in range(len(string)):
        if string[i] == ' ':
            string[i] = '_'
            continue
        string[i] = chr(ord(string[i]) + key)
    string = "".join(string)
    return string

def decipher(string, key):
    string = list(string)
    for i in range(len(string)):
        if string[i] == '_':
            string[i] = ' '
            continue
        string[i] = chr(ord(string[i]) - key)
    string = "".join(string)
    return string

if __name__ == "__main__":
    menu()
