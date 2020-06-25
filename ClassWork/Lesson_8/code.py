from random import randint
lst1 = []
for i in range(20):
    lst1.append(randint(-5, 5))
print("Before =", lst1)

for i in range(len(lst1)):
    for j in range(i, len(lst1)):
        if lst1[i] > lst1[j]:
            lst1[i], lst1[j] = lst1[j], lst1[i]

print("After =", lst1)



# lst = [1, 2, 3, 4, 5]
# price = 0
# for i in lst:
#     price += i
# print("Price =", price)



# lst = []
# for i in range(4, -1, -1):
#     lst.append(i)
# print(lst)