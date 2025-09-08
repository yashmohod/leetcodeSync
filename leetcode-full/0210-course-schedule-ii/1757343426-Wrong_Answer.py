class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        p = {c:[] for c in range(numCourses) }

        for crs,pre, in prerequisites:
            p[crs].append(pre)


        def dfs(cur,viste,curPath,pset):

            if cur in curPath:
                return [],True
            if cur in viste:
                return [],False
            curPath.add(cur)
            viste.add(cur)
            curRes = []
            for i in pset[cur]:
                t,c = dfs(i,viste,curPath,pset)
                if c :
                    return [],True
                curRes += t
                # pset[cur].remove(i)
            curRes.append(cur)

            return curRes,False

        res = []
        visited = set()
        for i in range(numCourses):
            t,c = dfs(i,visited,set(),p)
            if c :
                return []
            res += t

        return res
