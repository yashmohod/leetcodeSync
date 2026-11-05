class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        s = 0
        j = {}
        res = 0 

        for i in nums:
            s+=i

            if s == k :
                res+=1
            d = s-k

            if d in j:
                res+= j[d]
            
            j[s] = j.get(s,0)+1
        
        return res

