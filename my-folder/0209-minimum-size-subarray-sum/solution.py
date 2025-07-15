class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        ssf=0
        l,r=0,0
        count = float('inf')
        for r in range(len(nums)):
            ssf += nums[r]
            
            while ssf >= target:
                count = min(count,r-l+1)
                ssf -= nums[l]
                l+=1
            
            r+=1
        
        return count if count != float('inf') else 0
