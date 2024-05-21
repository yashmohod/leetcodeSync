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
        ans=[]
        for i in candies:
            if i+extraCandies >=g:
                ans.append(True)
            else:
                ans.append(False)
        return ans        
