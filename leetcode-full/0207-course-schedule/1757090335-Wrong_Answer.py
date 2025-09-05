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
        
        return True
