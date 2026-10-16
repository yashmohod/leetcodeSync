from typing import *
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        N = len(nums)
        res = N
        s = 0
        l,r = 0,0

        while l < N:
            res = min(res,r-l) if s == target else res
            if s > target or r >= N:
                s-=nums[l]
                l+=1
            else:
                s+=nums[r]
                r+=1
                

        return res if res < N else 0 
