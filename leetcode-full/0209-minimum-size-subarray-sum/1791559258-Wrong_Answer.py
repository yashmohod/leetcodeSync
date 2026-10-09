from typing import *
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        
        s = nums[0] 
        l,r = 0,0
        res = float("inf")
        while r < len(nums): 
            if s < target: 
                r+=1
                if r >= len(nums):
                    break
                s += nums[r]
            elif s >= target:
                res = min(r,r-l+1)
                s-= nums[l]
                l+=1
        
                
        return res if res != float("inf") else 0



