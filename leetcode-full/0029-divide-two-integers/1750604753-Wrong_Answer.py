class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

         
    
        sdd = dividend >0
        svd = divisor >0
        dividend = abs(dividend)
        divisor = abs(divisor)
        ans = 0
        if divisor == 1:
            ans = dividend
        else:
            hi = 0
            while dividend >= divisor *2**(hi+1):
                hi += 1
            
            while dividend >= divisor *2**hi:
                dividend -= divisor *2**hi
                ans += 2**hi
                if dividend < divisor *2**hi:
                    hi -= 1
        
        if (sdd and svd) or (not sdd and not svd):
            return ans
        elif  (sdd and not svd) or (not sdd and svd):
            return -ans

