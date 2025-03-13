# remove duplicates from sorted Array

    
nums = [0,1,2,2,3,0,4,2]
def removeduplicate(nums):
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i]=nums[j]
    return i + 1

h = removeduplicate(nums)

print(h)





    




