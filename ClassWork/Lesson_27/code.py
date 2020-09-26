from datetime import datetime

t = datetime.now()
l = [i for i in range(100_000_000)]
t2 = datetime.now()
print(f"List: {t2 - t}")

t = datetime.now()
g = (i for i in range(100_000_000))
t2 = datetime.now()
print(f"Generator: {t2 - t}")





#! def fibo(n):
#     p = pp = 1
#     for i in range(n):
#         if i in (0, 1):
#             yield 1
#         else:
#             n = p + pp
#             pp, p = p, n
#             yield n

# if __name__ == "__main__":
#     fibs = list(fibo(10))
#     print(fibs)
        



#! class Fibo:
#     def __init__(self, num):
#         print("__init__")
#         self.__n = num
#         self.__i = 0
#         self.__p1 = self.__p2 = 1

#     def __iter__(self):
#         print("__iter__")
#         return self

#     def __next__(self):
#         print("__next__")
#         self.__i += 1
#         if self.__i > self.__n:
#             raise StopIteration
#         if self.__i in (1, 2):
#             return 1
#         r = self.__p1 + self.__p2
#         self.__p1, self.__p2 = self.__p2, r
#         return r

# if __name__ == "__main__":
#     for i in Fibo(20):
#         print(i)