class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        

        p = set()

        som = 0
        res = 0
        for i in nums:
            som +=i
            if som == k:
                res+=1 
            if som-k in p:
                res+=1    
            p.add(som)
        return res
