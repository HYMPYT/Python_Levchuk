from random import randint

def selection_sort(nums):
    for i in range(len(nums) - 1):
        min_elem_pos = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_elem_pos]:
                min_elem_pos = j
        nums[i], nums[min_elem_pos] = nums[min_elem_pos], nums[i]

def insertion_sort(nums):
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = item_to_insert
            
nums = [randint(-5, 5) for i in range(10)]
print(nums)
selection_sort(nums)
print(nums)