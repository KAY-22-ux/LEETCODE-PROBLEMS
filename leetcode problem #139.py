#leetcode problem #169 - Majority Element
from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = Counter(nums)
        for num in count:
            if count[num] > len(nums)/2:
                return num
           