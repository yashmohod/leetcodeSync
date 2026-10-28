class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        p = {}
        s = 0 
        r = 0 

        for i in nums:
            p[s] = p.get(s,0)+1
            s+=i
            d = s-k
            r +=p[d] if d in p else 0 
        return r

