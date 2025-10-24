class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l,r = 0,0

        while r<len(nums):
            while nums[l]!=0 and l < len(nums):
                l+=1
                r=l
            if nums[r]==0:
                r+=1
            else:
                nums[l],nums[r] = nums[r],nums[l]
                l+=1
            
            

