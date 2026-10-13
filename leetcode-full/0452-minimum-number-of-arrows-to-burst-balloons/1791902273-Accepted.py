class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        

        points.sort()

        s = []

        for x,y in points:

            if len(s) <1:
                s.append([x,y]) 
            else:
                px,py = s[-1]
                if py>=x:
                    s[-1]=[max(x,px),min(y,py)]
                else:
                    s.append([x,y])
        return len(s)


