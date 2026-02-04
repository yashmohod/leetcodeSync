class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        al = {a:[] for a in range(numCourses)}
        for a,b in prerequisites:
            if a in al:
                al[a].append(b)
            else:
                al[a]=[b]

        done = set([])
        def dfs(c,seen):
            r = True
            for j in al[c]:
                if j in seen:
                    return False
                else:
                    seen.add(j)
                    r = r and dfs(j,seen)
            return r
        for i in range(numCourses):
            if not dfs(i,set([i])):
                return False
        return True
        

