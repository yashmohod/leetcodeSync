class Solution:
    def rob(self, nums: List[int]) -> int:
        l,r=0,0

        for i in range(len(nums)):
            if i %2 == 0:
                l+=nums[i]
            else:
                r+=nums[i]

        return max(l,r)
