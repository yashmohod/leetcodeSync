class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        

        for l in range(len(nums)):
            r = l+1

            while r < len(nums):
                if nums[l] == nums[r]:
                    return nums[r]
                r +=1
        

