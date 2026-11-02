class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        
        res = 0 
        a = {}
        s = 0
        for num in nums:

            s+=num
            r = s%k
            if r ==0:
                res+=1
            if r in a:
                res+= a[r]
            
            a[r] = a.get(r,0)+1
        return res
