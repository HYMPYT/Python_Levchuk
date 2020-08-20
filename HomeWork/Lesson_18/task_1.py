def compare_string(line_1: str, line_2: str) -> bool:
    '''This function is for string comparison.'''
    if line_1 == line_2:
        return True
    return False

def sequence_of_comparison(first_file_name: str, first_lines: list, second_file_name: str, second_lines: list) -> None:
    '''This function is for the correct comparison sequence.'''
    for current_index in range(len(first_lines)):
        if not compare_string(first_lines[current_index], second_lines[current_index]):
            print(f"Line from {first_file_name}: {first_lines[current_index]}")
            print(f"Line from {second_file_name}: {second_lines[current_index]}")
    
    for index in range(current_index + 1, len(second_lines)):
        print(f"Line from {second_file_name}: {second_lines[index]}")

def task_1_execute(first_file_name: str, second_file_name: str) -> None:
    '''This function implements the logic to perform the first task.'''
    with open(first_file_name, "r") as f1, open(second_file_name, "r") as f2:
        lines_1 = f1.readlines()
        lines_2 = f2.readlines()
    if len(lines_1) < len(lines_2):
        sequence_of_comparison(first_file_name, lines_1, second_file_name, lines_2)
    else:
        sequence_of_comparison(second_file_name, lines_2, first_file_name, lines_1)

if __name__ == "__main__":
    print("This module for importing not for execute.")