class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        ssf = 0
        count = 0 
        hm={}
        for i,num in enumerate(nums):
            ssf += num
            if ssf - k in hm:
                count += hm[ssf-k]
            
            hm[ssf] = 1 + hm.get(ssf, 0)
        return count
