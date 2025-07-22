class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        som=l=r=0

        while r < len(nums):
            while r+1< len(nums) and nums[r+1] in nums[l:r+1]:
                print(l,r,nums[r+1],nums[l:r+1])
                l+=1
            r+=1
            som = max(som,sum(nums[l:r+1]))

        
        return som
