from typing import *
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        N = len(nums)
        res = N
        l,r = 0,0
        som = 0 
        if sum(nums) < target:
            return 0

        while l < N:
            res = min(res,r-l) if som >= target else res
            if som > target or r >= N:
                som -= nums[l]
                l+=1
            else:
                som += nums[r]
                r+=1
        return res
