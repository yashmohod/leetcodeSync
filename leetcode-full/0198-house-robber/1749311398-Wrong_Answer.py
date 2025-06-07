class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(sum(nums[::2]),sum(nums[1::2]))

        
