class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 2:
            return 2
        l,r=1,1
        for _ in range(n-1):
            l,r = r,r+l
        return r



