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

        seen={}

        q = deque([])
        q.append(0)

        while q :
            cur = q.popleft()
            # print(cur)
            if cur in seen:
                return False
            else:
                if cur in c:
                    for i in c[cur]:
                        if i not in seen:
                            q.append(i)
                else:
                    q.append(cur+1)
                    seen[cur] =1


        return True
