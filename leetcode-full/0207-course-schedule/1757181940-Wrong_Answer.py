class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        c = {}

        for i in prerequisites:
            course,prec = i
            if course not in c:
                c[course] = [prec]
            else:
                 c[course].append(prec)
            if prec in c and course in c[prec]:
                return False
        
        def dfs(crs,vs):
            if crs in vs:
                return False
            if crs not in c or c[crs] == []:
                return True
            vs.add(crs)
            for i in c[crs]:
                if not dfs(i,vs): return False
            c[crs]=[]
            return True
        for i in range(numCourses):
            if not dfs(i,set()): return False
            # if i not in c:
            #     c[i] = []
        
        return True
        

            
