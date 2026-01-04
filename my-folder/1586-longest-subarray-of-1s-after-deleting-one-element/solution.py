class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        

        res = 0
        l = 0
        r = 0
        kk = 0
        while r < len(nums):
            
            if kk < 1 or nums[r]:
                if not nums[r]: 
                    kk +=1
                r+=1
            else:
                if not nums[l]:
                    kk -=1
                l+=1
            
            res = max(res,r-l)

        
        return res-1
