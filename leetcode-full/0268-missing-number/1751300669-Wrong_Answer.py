class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        if len(nums) ==1:
            return 0
        for i in range(1,len(nums)+1):
            if i not in nums:
                return i
        

