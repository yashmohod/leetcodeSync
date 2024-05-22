class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        s = sum(flowerbed)
        l = len(flowerbed)
        if l %2 ==0:
            if int(l/2) >= s+n:
                return True
            else:
                return False
        else:
            if int(l/2)+1 >= s+n:
                return True
            else:
                return False
        
