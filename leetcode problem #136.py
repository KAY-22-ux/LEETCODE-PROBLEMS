#leetcode problem 136 - Single Number

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        var = 0   
        for i in nums:   
            var ^= i   
        return var 
                                                      

       