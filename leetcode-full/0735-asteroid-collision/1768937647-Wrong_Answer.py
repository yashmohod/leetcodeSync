class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        s = deque([])

        for i in asteroids:
            if s :
                if s[-1]>0 and i < 0:
                    t = True
                    while s and (s[-1]>0 and i < 0) and abs(s[-1]) <= abs(i):
                        t = not (abs(s[-1]) == abs(i))
                        s.pop()
                    if not s or (s[-1]>0 and i >0) and (s[-1]<0 and i <0):
                        if t:
                            s.append(i)
                else:
                    s.append(i)
            else:
                s.append(i)
        
        return list(s)

