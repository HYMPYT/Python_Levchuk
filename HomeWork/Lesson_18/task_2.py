
#! CONSTS
VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']
CONSONANT =['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']

def write_analytics(file_name: str, number_of_chars: int, number_of_lines: int, number_of_digits: int, number_of_vowels: int, number_of_consonant: int) -> None:
    '''This function writes the transmitted analytical data to a file.'''
    with open(file_name, "w") as f:
        f.write(f"Number of chars: {number_of_chars}\n")
        f.write(f"Number of digits: {number_of_digits}\n")
        f.write(f"Number of lines: {number_of_lines}\n")
        f.write(f"Number of vowels: {number_of_vowels}\n")
        f.write(f"Number of consonant: {number_of_consonant}\n")

def get_number_of_chars(file_name: str) -> int:
    '''This function returns the number of chars in the file.'''
    with open(file_name, "r") as f:
        text = f.read()
    return len(text)

def get_number_of_lines(file_name: str) -> int:
    '''This function returns the number of lines in the file.'''
    with open(file_name, "r") as f:
        number_of_lines = 0
        lines = f.readlines()
        for line in lines:
            if line != '\n':
                number_of_lines += 1
    return number_of_lines

def get_number_of_digits(file_name: str) -> int:
    '''This function returns the number of digits in the file.'''
    with open(file_name, "r") as f:
        text = f.read()
        digits = [char for char in text if char.isdigit()]
    return len(digits)

def get_number_of_vowels(file_name: str) -> int:
    '''This function returns the number of vowels in the file.'''
    with open(file_name, "r") as f:
        text = f.read()
        vowels = [char for char in text if char in VOWELS]
    return len(vowels)

def get_number_of_consonant(file_name: str) -> int:
    '''This function returns the number of consonants in the file.'''
    with open(file_name, "r") as f:
        text = f.read()
        consonant = [char for char in text if char in CONSONANT]
    return len(consonant)

def task_2_execute(file_name: str) -> None:
    '''This function implements the logic to perform the second task.'''
    number_of_chars = get_number_of_chars(file_name)
    number_of_lines = get_number_of_lines(file_name)
    number_of_digits = get_number_of_digits(file_name)
    number_of_vowels = get_number_of_vowels(file_name)
    number_of_consonant = get_number_of_consonant(file_name)
    write_analytics(
        file_name="./Files/answer_for_task_2.txt", 
        number_of_chars=number_of_chars, 
        number_of_lines=number_of_lines, 
        number_of_digits=number_of_digits,
        number_of_vowels=number_of_vowels,
        number_of_consonant=number_of_consonant)
    
if __name__ == "__main__":
    print("This module for importing not for execute.")
