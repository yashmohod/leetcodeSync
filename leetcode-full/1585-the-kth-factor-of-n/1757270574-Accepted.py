class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        c = 0

        while k > 0:

            if c >= n:
                return -1
            c+=1
            if n % c == 0 :
                k-=1
        
        return c
            
