a = ('ab', 'abcd', 'cde', 'abc', 'def')
string = input("Enter the string -> ")
if string in a:
    print(f"String {string} is in the tuple")
else:
    print(f"String {string} isn't in the tuple")

# from random import randint

# lst = []
# for i in range(5):
#     lst.append(randint(0, 10))
# t = tuple(lst)
# print(t)