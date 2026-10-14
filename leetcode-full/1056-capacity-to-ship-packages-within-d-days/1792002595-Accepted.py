class Solution:
    def d(self,weights:list[int],cap):
        days = 0
        som = 0
        for i in weights:
            if som+i <= cap:
                som+=i
            else:
                som = i
                days+=1
        return days+1

    def shipWithinDays(self, weights: list[int], days: int) -> int:
       
        l = max(weights)
        r = sum(weights)
        while l <= r:
            m = (l+r)//2
            j = self.d(weights,m)
            if j <= days:
                r = m-1
            elif j > days:
                l = m+1

        return l
