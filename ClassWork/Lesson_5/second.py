from random import choice, sample

lst = [1, 2, 3, 4, 5, 6]
print(choice(lst))
print(sample(lst, 2))
print(sample(lst, 6))

#for i in range(10):
#    print(str(i) + ". " + str(random()))