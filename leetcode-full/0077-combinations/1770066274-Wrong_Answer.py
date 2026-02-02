class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []
        
        def bt(start,comb):
            if len(comb) == k:
                res.append(comb.copy())
                return 
            
            for i in range(start,n+1):
                comb.append(i)
                bt(i,comb)
                comb.pop()
        bt(1,[])
        return res
