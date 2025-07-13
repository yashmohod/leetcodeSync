class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        cur = 0 

        while cur < len(nums):
            if nums[cur] == 0 and cur != len(nums):
                return False
            cur += nums[cur]
        
        return True
