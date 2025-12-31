import numpy as np

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        
        if len(nums) <= 2:
            return len(nums)
        
        d =  [{} for _ in range(len(nums))]
        res = -1
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i]-nums[j]
                d[i][diff] = d[j].get(diff,1) +1
                res = max(d[i][diff],res)
        return res
