class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0 or len(nums) == 1:
            return 
        l,r = 0,0

        while r<len(nums) and l<len(nums):
            while l < len(nums) and nums[l]!=0:
                l+=1
                r=l
            if nums[r]==0:
                r+=1
            else:
                nums[l],nums[r] = nums[r],nums[l]
                l+=1
            
            

