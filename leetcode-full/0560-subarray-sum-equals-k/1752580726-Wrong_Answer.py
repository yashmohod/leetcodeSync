class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        ssf = 0
        count = 0 
        hm={}
        for i,num in enumerate(nums):
            ssf += num
            hm[ssf] = ssf

            if (ssf > k and ssf - k in hm) or ssf == k:
                count+=1

        return count
