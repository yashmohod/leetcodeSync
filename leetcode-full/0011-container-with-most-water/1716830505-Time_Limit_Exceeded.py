class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lar=0

        for i in range(len(height)):
            for j in range(i+1,len(height)):
                co=0
                if height[i] < height[j]:
                    co = height[i]*abs(j-i)
                else:
                    co =height[j]*abs(j-i)
                if co > lar:
                    lar =co

        return lar
