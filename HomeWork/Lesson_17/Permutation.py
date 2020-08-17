from itertools import permutations
from string import ascii_lowercase

def union_of_permutations() -> dict:
    """This function returns a dictionary with all possible combinations of one to three letters of the English alphabet."""
    words = list(map("".join, permutations(ascii_lowercase, 1)))
    words += list(map("".join, permutations(ascii_lowercase, 2)))
    words += list(map("".join, permutations(ascii_lowercase, 3)))
    return { index + 1: word for index, word in enumerate(words)}

if __name__ == "__main__":
    print(f"The number of elements in the dictionary: {len(union_of_permutations())}")

    #! Uncomment if you want to see the output
    # dictionary = union_of_permutations()
    # for index, word in dictionary.items():
    #     print(f"{index}: {word}")