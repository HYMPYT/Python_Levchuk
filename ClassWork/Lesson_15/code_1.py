from random import choice

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

def get_randome_string(lenght):
    result = ""
    for i in range(lenght):
        result += choice(alphabet)
    return result

lst_1 = [get_randome_string(len(alphabet)) for i in range(100)]
lst_2 = [get_randome_string(len(alphabet)) for i in range(100)]

A = set(lst_1)
B = set(lst_2)

text = input("Enter text: ")

if text in (A | B):
    print("Found")
else:
    print("Not found")