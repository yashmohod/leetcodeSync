class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        

        points.sort()

        s = deque([])

        for x,y in points:

            if len(s) <1:
                s.append([x,y]) 
            else:
                px,py = s.pop()

                if py>=x:
                    s.append([max(x,px),min(y,py)])
                else:
                    s.append([px,py])
                    s.append([x,y])
        print(s)
        return len(s)


