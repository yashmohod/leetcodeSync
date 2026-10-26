class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        if len(nums) <1:
            return 0
        
        def dfs(s,idx):
            if idx >= len(nums) :
                return 1 if s%k ==0 and s !=0 else 0
            l = dfs(s,idx+1)
            r = dfs(s+nums[idx],idx+1)
            return l+r

        return dfs(0,0)

        



