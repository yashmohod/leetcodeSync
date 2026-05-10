class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        l,r = 0,0
        res = 0
        som = 0
        while l < len(nums):
            if som < k and r < len(nums):
                som += nums[r]
                r+=1
            else:
                if som == k:
                    res+=1
                som -= nums[l]
                l+=1

                
        return res
