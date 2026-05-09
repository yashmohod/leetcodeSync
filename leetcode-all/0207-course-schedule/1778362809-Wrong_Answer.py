class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        z ={}
        
        for a,b in prerequisites: 
            if a not in z:
                z[a] = []
            if b not in z:
                z[b] = []
            z[a].append(b)
            if a in z[b]:
                return False
        visited=set()

        def dfs(c): 
            for i in z[c]:
                if dfs(i):
                    z[c].remove(i)
            if len(z[c]) == 0:
                return True
            
        for k in z.keys():
            if not dfs(k):
                return False  

        return True

            



