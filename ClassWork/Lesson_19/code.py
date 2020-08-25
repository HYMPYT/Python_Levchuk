from contextlib import contextmanager

def global_try(func):
    def wrapper():
        try:
            func()
        except FileNotFoundError as e:
            print(f"ERROR:: {e}")
    return wrapper 

@contextmanager
def read_file(filename: str):
    file = open(filename, "r")

    try:
        print(f"File {filename} is opened")
        yield file
    finally:
        print(f"File {filename} is closed")
        file.close()

@global_try
def read_my_file():
    with read_file('my_file_3.txt') as f:
        a = f.readlines()
        print(a)

read_my_file()

#! import pickle

# my_list = [1, 2, 3, 4, 5]

# with open('my_file.bin', 'wb') as f:
#     pickle.dump(my_list, f)

# with open('my_file.bin', 'rb') as f:
#     new_list = pickle.load(f)

# print(new_list)


#! import struct

# ls = [1, 3, 9, 12]

# obj = struct.pack('>4i', ls[0], ls[1], ls[2], ls[3])
# size = struct.calcsize('>3f')

# print('obj: ', obj)
# print('size: ', size)