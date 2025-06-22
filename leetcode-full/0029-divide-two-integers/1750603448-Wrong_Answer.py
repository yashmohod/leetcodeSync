class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

         
        cur = 0 
        sdd = dividend >0
        svd = divisor >0
        dividend = abs(dividend)
        divisor = abs(divisor)
        if divisor == 1:
            cur = dividend
        else:
            while dividend >= divisor:
                if cur > 2**31 -1:
                    cur  = 2**31 -1
                    break 
                cur +=1
                dividend -= divisor

        if (sdd and svd) or (not sdd and not svd):
            return cur
        elif  (sdd and not svd) or (not sdd and svd):
            return -cur

