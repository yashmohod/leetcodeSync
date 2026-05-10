class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        

        p = {}

        som = 0
        res = 0
        for i in nums:
            som +=i
            if som == k:
                res+=1 
            if som-k in p:
                res+=p[som-k]    
            p[som] = p.get(som,0)+1
        return res
