class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        l,r = 0,0
        som = 0 

        while r < len(nums):
            if r+1 < len(nums):
                while nums[r+1] in nums[l:r]:
                    l +=1
            r +=1
            som = max(som, sum(nums[l:r]))
        
        return som
