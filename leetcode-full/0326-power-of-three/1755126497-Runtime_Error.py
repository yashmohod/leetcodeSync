class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        l,r = 0,n/2

        while l<=r:

            m = (l+r)//2

            if 3**m ==n:
                return True
            elif 3**m < n:
                l = m +1
            elif 3**m >n:
                r = m-1


        return False
