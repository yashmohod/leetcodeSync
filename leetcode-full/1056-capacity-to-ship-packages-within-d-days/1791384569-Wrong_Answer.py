class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        
        def calcap(cap):
            su = 0 
            count = 0
            for i in weights:
                if su+i <= cap:
                    su += i
                else:
                    su = i 
                    count+=1
            return count+1
        
        l = max(weights)
        r = sum(weights)
        while l<=r:
            ii = (l+r)//2
            m = calcap(ii)
            print(ii,m)
            if m < days:
                r = ii-1
            elif m > days:
                l = ii+1
            else:
                return ii
        
        return l
