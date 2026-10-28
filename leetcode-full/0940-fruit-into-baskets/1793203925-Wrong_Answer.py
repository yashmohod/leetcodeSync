class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        
        h ={}
        l,r=0,0
        N = len(fruits)
        res = 0  
        while l< N: 
            if r < N:
                h[fruits[r]] = h.get(fruits[r],0)+1
            r+=1
            if len(h.keys()) >2 or r >=N:
                h[fruits[l]] = h[fruits[l]] -1
                if h[fruits[l]] == 0:
                    h.pop(fruits[l])
                l+=1

            res = max(r-l+1,res)

        return res



