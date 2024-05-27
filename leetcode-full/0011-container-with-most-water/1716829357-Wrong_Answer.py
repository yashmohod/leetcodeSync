class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lar=0
        counti=0
        for i in range(len(height)):
            countj=0
            for j in range(i,len(height)):
                co=0
                if height[i] < height[j]:
                    co = height[i]*abs(counti-countj)
                else:
                    co =height[j]*abs(counti-countj)
                if co > lar:
                    lar =co
                countj+=1
            counti+=1
        return lar
