class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        p = {c:[] for c in range(numCourses) }

        for crs,pre, in prerequisites:
            p[crs].append(pre)


        def dfs(cur,vis,pset):

            if cur in vis:
                return []
            vis.add(cur)
            curRes = []
            for i in pset[cur]:
                curRes += dfs(i,vis,pset)
                pset[cur].remove(i)
            curRes.append(cur)

            return curRes

        res = []
        visited = set()
        for i in range(numCourses):
            res += dfs(i,visited,p)

        return res
