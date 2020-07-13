from random import randint, shuffle

def bubble_sort(nums):
    sorted = True
    while sorted:
        sorted = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                sorted = True  

def quick_sort(nums, L, R):
    x = nums[int((L + R) / 2)]
    i = L
    j = R
    while i <= j:
        while nums[i] < x:
            i += 1
        while nums[j] > x:
            j -= 1
        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
    if L < j:
        quick_sort(nums, L, j)
    if i < R:
        quick_sort(nums, i, R)


if __name__ == "__main__":
    size = int(input("Enter the size of list -> "))
    nums = [randint(-10, 10) for i in  range(size)]

    print("~~~~~~~~~~ Quick sort ~~~~~~~~~~")
    print("List before sorting ->", nums)
    quick_sort(nums, 0, size - 1)
    print("List after sorting ->", nums)

    shuffle(nums)

    print("\n~~~~~~~~~~ Bubble sort ~~~~~~~~~~")
    print("List before sorting ->", nums)
    bubble_sort(nums)
    print("List after sorting ->", nums)