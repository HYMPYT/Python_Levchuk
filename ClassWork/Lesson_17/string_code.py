import string

leet = str.maketrans('abegiloprstz', '463611092572')
s = "The quick brown fox jumped over the lazy dog"
print(s.translate(leet))

# pattern = 'This is my favourite job!!! IT Step!'
# print(repr(pattern))
# print(string.capwords(pattern))

# def foo(a: int) -> int:
#     print(repr(a))
#     print(type(a))
#     return a ** 2

# for n in dir(string):
#     if n.startswith('_'):
#         continue
#     v = getattr(string, n)
#     if isinstance(v, str):
#         print(f"{n} = {repr(v)}")

# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)

# print(string.digits)
# print(string.hexdigits)
# print(string.octdigits)

# print(string.punctuation)
# print(string.whitespace)
# print(string.printable)