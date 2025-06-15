class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        l,r = 0,1

        while r < len(nums):
            if nums[r] > nums[l] and r-l != 1 :
                nums[l+1],nums[r] = nums[r],nums[l+1]
                l+=1
            r+=1
        # print(l)
        # print(nums)
        return l+1

