from os import path, walk


def get_file_names(directory_path: str):
    """This function is a generator. It generates a path to the file."""
    for dir_path, dir_names, file_names in walk(directory_path):
        for file_name in file_names:
            yield path.join(dir_path, file_name)

def get_all_lines_from_file(file_path: str):
    """This function is a generator. It generates a line from the file."""
    for line in open(file_path):
        yield line


def emit_lines(path: str, pattern: str = None):
    """This function returns all lines from all files in the specified directory.
    If a filter is set, only the filtered lines will be returned."""
    lines = []
    for file_name in get_file_names(path):
        for line in get_all_lines_from_file(file_name):
            if pattern and line.startswith(pattern):
                lines.append(line[0:-1])
            elif not pattern:
                lines.append(line[0:-1])
    return lines


if __name__ == "__main__":
    print("This module for import not for execute!")
