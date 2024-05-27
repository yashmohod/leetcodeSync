class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lar=0
        larh=0
        lari=0
        count=0
        for i in height:
            if i > larh:
                larh=i
                lari=count
            count+=1
        count=0
        for i in height:
            co=i*abs(count-lari)
            if co >lar:
                lar=co
            count+=1


        return lar
