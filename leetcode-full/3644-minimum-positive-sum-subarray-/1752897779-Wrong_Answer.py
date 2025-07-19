class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        # if len(nums) < r-l:
        #     return -1
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        ans = float('inf')
        while r < len(nums):
            s = nums[r]- nums[l]
            ans = s if s<ans else ans
            r +=1
            l +=1
        
        if ans >0:
            return ans
        else:
            return -1

