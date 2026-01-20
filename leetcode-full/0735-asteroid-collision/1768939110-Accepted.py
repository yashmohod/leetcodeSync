class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        s = deque([])

        for i in asteroids:
            while s and i < 0 < s[-1]:
                if -i  > s[-1]:
                    s.pop()
                    continue
                elif  -i == s[-1]:
                    s.pop()
                break
            else:
                s.append(i)
        
        return list(s)

