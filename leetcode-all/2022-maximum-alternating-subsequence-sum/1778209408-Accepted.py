class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:

        odd,even = 0,0

        for i in range(len(nums)-1,-1,-1):
            odd,even= max(even-nums[i],odd),max(odd+nums[i],even)
        return even
