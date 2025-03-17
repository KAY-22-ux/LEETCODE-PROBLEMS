#leetcode problem 136 - Single Number
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            var = nums[0]
            if nums.count(nums[i]) <= 1 :
                var = nums[i]
                return var 
                                     