class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        if len(nums) == 1:
            if nums[0] == val:
                return 0 
            else:
                return 1

        if len(nums) == 2:
            if nums[0] == val and nums[1] != val:
                nums[0],nums[1] = nums[1],nums[0]
                return 1
            elif nums[0] != val and nums[1] == val:
                return 1
            elif nums[0] == val and nums[1] == val:
                return 0
            else:
                return 2

        l,r=0,0
        while r < len(nums):
            if nums[r] == val and nums[l] != val:
                l = r 
            if nums[r] != val and nums[l] == val:
                nums[l],nums[r] = nums[r],nums[l]
                l +=1 
            r+=1

        return l
                
            
            
            





