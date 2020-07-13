from random import randint

def bubble_sort(nums):
    sorted = True
    while sorted:
        sorted = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                sorted = True  
    return nums

lst = [randint(-5, 5) for i in range(10)]
print(lst)
print(bubble_sort(lst))