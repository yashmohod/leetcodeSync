class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        if sum(candidates) < target:
            return []
        candidates.sort() 
        res = {}
        
        def fff(idx,c):
            s = sum(c)
            result = ", ".join(map(str, c))
            if s == target and result not in res:
                res[result] = c.copy()
            
            if idx < len(candidates):
                c.append(candidates[idx])
                fff(idx+1,c)
                c.remove(candidates[idx])
                fff(idx+1,c)
        
        fff(0,[])
        return list(res.values())
                
                

