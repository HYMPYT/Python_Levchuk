# Пользователь вводит с клавиатуры строку. Проверьте
# является ли введенная строка палиндромом. Палиндром — слово
# или текст, которое читается одинаково слева
# направо и справа налево. Например, кок; А роза
# упала на лапу Азора; доход; А буду я у дуба.

def execute_task1():
    string = input("Enter the string -> ")
    if ' ' in string:
        lst = string.split()
        res = is_palindrome("".join(lst))
    else:
        res = is_palindrome(string)
    
    if res == True:
        print(f'String "{string}" is palindrome')
    else:
        print(f'String "{string}" isn\'t palindrome')
   
def is_palindrome(string):
    if string.lower() == string[::-1].lower():
        return True
    else:
        return False

# Пользователь вводит с клавиатуры некоторый текст,
# после чего пользователь вводит список зарезервированных
# слов. Необходимо найти в тексте все зарезервированные
# слова и изменить их регистр на верхний. Вывести на
# экран измененный текст.

def execute_task2():
    text = input("Enter some text separated by spaces -> ").split()
    words = input("Enter a list of reserved words separated by spaces -> ").split()

    for i in range(len(text)):
        for j in words:
            if text[i].lower() == j.lower():
                text[i] = text[i].upper()
    
    text = " ".join(text)
    print(f"Your text: {text}")

# Есть некоторый текст. Посчитайте в этом тексте 
# количество предложений и выведите на экран полученный
# результат.

def execute_task3():
    text = input("Enter some text -> ")
    res = text.count('.') + text.count('!') + text.count('?')
    print(f"Number of sentences -> {res}")


if __name__ == "__main__":
    print("Task 1")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
    execute_task1()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
    input()
    print("\nTask 2")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
    execute_task2()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
    input()
    print("\nTask 3")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
    execute_task3()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")

    