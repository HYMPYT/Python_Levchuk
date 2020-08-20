def write_analytics(file_name: str, number_of_chars: int, number_of_lines: int, number_of_digits: int) -> None:
    with open(file_name, "w") as f2:
        f2.write(f"Number of chars: {number_of_chars}\n")
        f2.write(f"Number of digits: {number_of_digits}\n")
        f2.write(f"Number of lines: {number_of_lines}\n")

def get_number_of_chars() -> int:
    with open("./f1.txt", "r") as f1:
        text = f1.read()
    return len(text)

def get_number_of_lines() -> int:
    with open("./f1.txt", "r") as f1:
        number_of_lines = 0
        lines = f1.readlines()
        for line in lines:
            if line != '\n':
                number_of_lines += 1
    return number_of_lines

def get_number_of_digits() -> int:
    with open("./f1.txt", "r") as f1:
        text = f1.read()
        digits = [char for char in text if char.isdigit()]
    return len(digits)
    
if __name__ == "__main__":
    number_of_chars = get_number_of_chars()
    number_of_lines = get_number_of_lines()
    number_of_digits = get_number_of_digits()
    write_analytics("f2.txt", number_of_chars, number_of_lines, number_of_digits)
