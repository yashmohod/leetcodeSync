class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        cur = 0 

        while cur < len(nums):
            print(cur)
            if cur != len(nums)-1 
                if nums[cur] == 0:
                    return False
            else:
                return True
            cur += nums[cur]
        
        return True
