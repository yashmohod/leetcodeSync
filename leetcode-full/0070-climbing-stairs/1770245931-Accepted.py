class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1
        if n == 2:
            return 2
        
        r=[1,2]
        for i in range(n-2):
            r[0],r[1] = r[1],r[0]+r[1]
        
        return r[1]
