class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        

        p = set([0])

        som = 0
        res = 0
        for i in nums:
            som +=i
            if som == k or som-k in p:
                res+=1 
            p.add(som)
        return res
