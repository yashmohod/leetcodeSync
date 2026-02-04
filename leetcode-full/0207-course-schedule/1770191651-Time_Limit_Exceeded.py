class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        al = {a:[] for a in range(numCourses)}
        for a,b in prerequisites:
            al[a].append(b)


        def dfs(c,seen):
            r = True
            for j in al[c]:
                if j in seen:
                    return False
                else:
                    seen.add(j)
                    r = r and dfs(j,seen)
                    seen.remove(j)
            return r
        for i in range(numCourses):
            if not dfs(i,set()):
                return False
        return True
        

