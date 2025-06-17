class Solution:
    def mySqrt(self, x: int) -> int:
        
        c = 1 

        while c**2 <= x:
            c+=1 

        if c**2 - x > (c-1)**2 - x:
            return c-1
        else: 
            return c
