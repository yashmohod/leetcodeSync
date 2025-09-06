class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        c = {}
        for i in prerequisites:
            crs,pre = i
            if crs in c:
                c[crs].append(pre)
            else:
                c[crs] = [pre]
            
        def dfs(crs,vs):
            if crs in vs:
                return False
            if crs not in c or c[crs] == []:
                return True
            vs.append(crs)
            for i in c[crs]:
                if not dfs(i,vs): return False
            # vs.remove(crs)
            c[crs]=[]
            return True
        
        res = []

        for i in range(numCourses):
            vss = []
            if i not in c:
                res += [i]
                vss = [i]
            
            if not dfs(i,vss): return []
            print(vss)
            res += vss

        return res
        

        
        
