class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        fb=flowerbed
        if n == 0:
            return True
        else:
            for i in range(len(fb)):
                if i ==0:
                    if fb[i+1] ==0 and fb[i] ==0:
                        n-=1
                else:
                    if fb[i-1] == 0 and fb[i] ==0:
                        if i <  len(fb)-1:
                            if fb[i+1] == 0 :
                                n -=1
                        else:
                            n -=1
                if n==0:
                    return True
            return False
