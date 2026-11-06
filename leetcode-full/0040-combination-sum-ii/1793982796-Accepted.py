class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        candidates.sort() 
        N = len(candidates)
        def dfs(i,cur,s):

            if s == target: 
                res.append(cur.copy())
                return
            if i >= N or s > target:
                return 

            cur.append(candidates[i])
            dfs(i+1,cur,s+candidates[i])
            cur.pop()

            while i < N-1 and candidates[i] == candidates[i+1]:
                i+=1
            dfs(i+1,cur,s)
        
        dfs(0,[],0)
        return res
