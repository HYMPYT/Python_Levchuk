def get_length_of_the_longest_line(file_name: str) -> int:
    '''This function returns the length of the longest line in the file.'''
    with open(file_name, "r") as f:
        lines = f.readlines()
    return len(max(lines, key=len))

if __name__ == "__main__":
    print("This module for importing not for execute.")