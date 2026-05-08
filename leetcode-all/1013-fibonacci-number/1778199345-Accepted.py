class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        
        l,r = 0,1
        
        for _ in range(n-1):
            l,r = r,r+l
        return r
        
