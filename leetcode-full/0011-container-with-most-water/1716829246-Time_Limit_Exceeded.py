class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lar=0
        counti=0
        for i in height:
            countj=0
            for j in height:
                co=0
                if i < j:
                    co = i*abs(counti-countj)
                else:
                    co =j*abs(counti-countj)
                if co > lar:
                    lar =co
                countj+=1
            counti+=1
        return lar
