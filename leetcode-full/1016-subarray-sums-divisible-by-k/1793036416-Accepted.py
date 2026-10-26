class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        

        hh = {}
        res = 0 
        s = 0 

        for i in nums:
            s+=i
            d = s%k
            res += 1 if d == 0 else 0 
            if d in hh:
                res+= hh[d]
                hh[d] +=1
            else:
                hh[d] = 1
        return res
            
            
            
        



