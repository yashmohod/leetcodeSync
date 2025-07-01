class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        count = 0 
        while n >= 3**count:
            if n ==3**count:
                return True
            count+=1

        return False
