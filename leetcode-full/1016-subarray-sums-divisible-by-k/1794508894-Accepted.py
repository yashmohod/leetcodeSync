class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        
        res = 0
        j = {}
        s = 0
        for i in nums:

            s+=i
            r = s%k
            if r ==0:
                res+=1
            if r in j :
                res+=j[r]

            j[r] = j.get(r,0)+1
            
        return  res





