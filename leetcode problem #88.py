#leetcode problem #88 - Merge sorted Array


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        i = 0
        for j in range(len(nums1)):
            if i < len(nums2):    
                nums1[-n] = nums2[i]
                i += 1
                n -=1

        nums1.sort()
                