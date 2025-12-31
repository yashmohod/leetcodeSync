import numpy as np

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        
        if len(nums) < 2:
            return len(nums)
        
        nums = np.array(nums)

        d = np.abs(nums[0]-nums[1])

        ds = abs(nums[:-1] - nums[1:])
        curRes= len(nums)
        print(ds)
        if abs(np.mean(ds)) == d:
            return curRes
        else:
            curRes = -1

        ress= []
        for i in range(len(nums)):
            nums = list(nums)
            ress.append(self.longestArithSeqLength(nums[:i]+nums[i+1:]))
        
        return max(max(ress),curRes)

