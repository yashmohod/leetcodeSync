class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        z = {d:[] for d in range(numCourses)}
        
        for a,b in prerequisites: 
            z[a].append(b)
            if a in z[b]:
                return False
        
        for i in range(numCourses):
            if len(z[i])>0:
                q = deque(z[i])
                while q:
                    c = q.popleft()
                    if c == i:
                        return False
                    for n in z[c]:
                        q.append(n)
        return True

            



