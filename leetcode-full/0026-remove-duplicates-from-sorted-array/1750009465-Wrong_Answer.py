class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if len(nums) <=1:
            return len(nums)
        if len(nums) ==2:
            if nums[0] != nums[1]:
                return 2
            else:
                return 1
        l,r = 0,1

        while r < len(nums):
            if nums[r] > nums[l+1] and r-l != 1 :
                nums[l+1],nums[r] = nums[r],nums[l+1]
                l+=1
            r+=1
        # print(l)
        # print(nums)
        return l+1

