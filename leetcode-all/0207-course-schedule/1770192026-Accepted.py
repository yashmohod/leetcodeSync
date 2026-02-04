class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        al = {a:[] for a in range(numCourses)}
        for a,b in prerequisites:
            al[a].append(b)
            if b in al and a in al[b]:
                return False


        def dfs(c,seen):
            if c in seen:
                return False
            if al[c] ==[]:
                return True
            seen.add(c)
            for j in al[c]:
                if not dfs(j,seen): return False
            seen.remove(c)
            al[c] = []
            return True
        for i in range(numCourses):
            if not dfs(i,set()):
                return False
        return True
        

