class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if not len(nums):
            return 0
        
        l=0
        for r in range(len(nums)):
            if nums[r] > nums[l]:
                nums[l+1],nums[r] = nums[r], nums[l+1]
                l+=1
        return l+1
