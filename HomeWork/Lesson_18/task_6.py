
#! CONSTS
PUNCTUATION = [',', '.', '!', '?', ':', ';']

def replace(file_name: str, old_word: str, new_word: str) -> None:
    '''This function replaces all occurrences of the old word in the file with the new one.'''
    with open(file_name, "r") as f:
        lines = f.readlines()
        for index in range(len(lines)):
            lines[index] = lines[index].split()
        for line in lines:
            for index in range(len(line)): 
                if line[index] == old_word:
                    line[index] = new_word
                elif line[index][-1] in PUNCTUATION and line[index][:-1] == old_word:
                    line[index] = new_word + line[index][-1]
    with open(file_name, "w") as f:
        for line in lines:
            f.write(f"{' '.join(line)}\n")

if __name__ == "__main__":
    print("This module for importing not for execute.")