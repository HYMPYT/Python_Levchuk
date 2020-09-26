def mult_2_generator(start: int, stop: int):
    """This function is a generator. It generates a number multiplied by 2 from the range."""
    for i in range(start, stop):
        yield i * 2
        

if __name__ == "__main__":
    print("This module for import not for execute!")
