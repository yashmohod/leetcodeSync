class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        z ={s:[] for s in range(numCourses)}
        
        for a,b in prerequisites: 
            z[a].append(b)
        
        visited = set()
        def dfs(c): 
            if len(z[c]) == 0:
                return True
            if c in visited:
                return False
            visited.add(c)    
            for i in z[c]:
                if not dfs(i):
                    return False
            visited.remove(c)
            z[c] = []
            return True
            
            
        for k in range(numCourses):
            if not dfs(k):
                return False  

        return True

            



