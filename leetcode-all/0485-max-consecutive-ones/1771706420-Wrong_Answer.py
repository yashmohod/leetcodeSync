class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        l,r=0,0
        lg = 0 

        while r<len(nums):
            if nums[r] == 0:
                l,r = r+1,r+1
            r+=1
            lg = max(lg,r-l)

        return lg
