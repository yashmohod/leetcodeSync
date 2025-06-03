class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def hours( k, p):
            a=0
            for i in p:
                if i%k > 0 :
                    a += i//k +1
                else:
                    a += i//k
            return a

        l = 1
        r = max(piles)
        
        while l < r:
            m = (l+r)//2

            if hours(m,piles) > h :
                l = m +1
            else:
                r  = m 
               
        return l
