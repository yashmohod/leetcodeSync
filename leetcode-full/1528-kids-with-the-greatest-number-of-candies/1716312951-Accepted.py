import numpy as np

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        g=0
        for i in candies:
            if i > g:
                g=i
        ans=np.array(candies)+extraCandies
        ans = ans >=g

        return ans        
