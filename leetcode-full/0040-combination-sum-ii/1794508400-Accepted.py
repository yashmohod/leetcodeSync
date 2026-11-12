class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        
        candidates.sort()
        res = []
        def dd(i,s,ss):


            if s == target:
                res.append(ss.copy())
                return 
            
            if s >target :
                return 

            if i >= len(candidates): 
                return

            ss.append(candidates[i])
            dd(i+1,s+candidates[i],ss)
            ss.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            dd(i+1,s,ss)

        dd(0,0,[])
        return res
        



        
