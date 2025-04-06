#leetcode problem #66 - Plus one


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        List = []
        number = 0 
        for i in digits:
            number = number * 10 + i
        number +=1

        
        var = str(number)
        digits = List  
        for i in range(len(var)):
            digits.append(int(var[i]))
        return digits
           