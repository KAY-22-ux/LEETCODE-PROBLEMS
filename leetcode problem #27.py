# leetcode problem 27 - remove element 

nums = [0, 1, 2, 2, 3, 0, 4, 2]

def remove_element(nums):
    k = 0
    for  n in range(len(nums)):
        if nums[n] != 2:
            nums[k] = nums[n]
            k += 1
        return n 


print(remove_element(nums))



















# while i < len(nums):  
#     if nums[i] == 2:
#         nums.pop(i)  # Remove the element at index i
#     else:
#         i += 1  # Only increment if no removal occurs

# print(nums)  # Output: [0, 1, 3, 0, 4]














# def removeduplicates(nums):
#     i = 0
#     for j in (1, len(nums)):
#         if nums[i] != nums[j]:
#             i += 1
#             nums[i] = nums[j]
#     return i + 1


# h = removeduplicates(nums)
# print(h)
















