# leetcode problem 35 - search insert position
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            for i in range(0 , len(nums)):
                if nums[i] == target:
                    return i 
                
        if target < nums[0]:
            return 0 
        
        for n in range(1 , len(nums)):
            if nums[n-1] < target < nums[n]:
                return n

        return len(nums)
        
    