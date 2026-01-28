class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def ch(k):
            s = 0
            for i in piles:
                s += math.ceil(i/k)
            return s <= h 
        
        l = 1 
        r = max(piles)
        res = r
        while l <r:
            m = math.floor((l+r)/2)
            if ch(m):
                r = m-1
                res = min(res,m)
            else:
                l = m +1
        return res

