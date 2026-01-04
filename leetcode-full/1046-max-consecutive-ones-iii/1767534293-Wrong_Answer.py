class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        res = 0
        l = 0
        r = 0
        kk = 0
        while r < len(nums):
            
            if kk <= k:
                if not nums[r]: 
                    kk +=1
                r+=1
            else:
                if not nums[l]:
                    kk -=1
                l+=1
            
            res = max(res,r-l-1)
            print(r,l,kk,k,res)
        
        return res



