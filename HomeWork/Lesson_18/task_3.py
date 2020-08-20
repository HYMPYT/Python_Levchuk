def write_result(file_name: str, string: str) -> None:
    '''This function is used to write the result of the third task to a file.'''
    with open(file_name, "w") as f:
        f.write(string)

def delete_last_line_from_file(file_name: str) -> str:
    '''This function removes the last line from the file and returns it.'''
    with open(file_name, "r") as f:
        lines = f.readlines()
    if len(lines) > 0:
        with open(file_name, "w") as f:
            f.writelines(lines[:-1])
        return lines[-1]
    else:
        return ''

if __name__ == "__main__":
    print("This module for importing not for execute.")