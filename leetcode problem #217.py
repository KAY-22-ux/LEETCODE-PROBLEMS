#leetcode problem #217 - Contains Duplicate
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_set = set()
        for i in nums:
            if i in num_set:
                return True
            num_set.add(i)
        return False 
       