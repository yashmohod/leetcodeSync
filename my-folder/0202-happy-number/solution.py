class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = {}

        while n != 1:
            sum = 0

            while n >0:
                sum += (n % 10) **2
                n //= 10
            
            if sum in seen : 
                return False
            else:
                seen[sum] = 1
            n = sum
        return True

