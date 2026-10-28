class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        res = 0 
        l,r=0,0
        s = 0
        N=len(nums) 

        while l < N:

            if s > k or r >= N:
                s -= nums[l]
                l+=1
            
            res +=1 if s == k else 0

            s +=nums[r] if r <N else 0
            r+=1
        return res
