class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        z = {d:[] for d in range(numCourses)}
        
        for a,b in prerequisites: 
            z[a].append(b)
        
        for i in range(numCourses):
            q = deque(z[i])
            while q:
                c = q.popleft()
                if c == i:
                    return False
                for n in z[c]:
                    q.append(n)
        return True

            



