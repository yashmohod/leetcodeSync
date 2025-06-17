class Solution:
    def climbStairs(self, n: int) -> int:
        s=1
        prev = 0
        for i in range(n):
            s,prev= prev+s,s

        return s
