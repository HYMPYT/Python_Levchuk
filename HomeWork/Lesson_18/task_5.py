def get_number_of_a_given_word(file_name: str, word: str) -> int:
    '''This function returns the number of times a given word occurs in a file.'''
    with open(file_name, "r") as f:
        text = f.read()
    return [w.rstrip(',.!?:;') for w in text.split()].count(word)

if __name__ == "__main__":
    print("This module for importing not for execute.")