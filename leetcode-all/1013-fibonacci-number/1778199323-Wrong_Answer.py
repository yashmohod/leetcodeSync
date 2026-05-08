class Solution:
    def fib(self, n: int) -> int:
        
        l,r = 0,1
        
        for _ in range(n-1):
            l,r = r,r+l
        return r
        
