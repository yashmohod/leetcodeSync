class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:

        r = []
        points.sort()
        for x,y in points:

            if len(r)>0 and x <= r[-1][1]:
                xx = max(x,r[-1][0])
                yy = min(y,r[-1][1])
                r[-1][0] = xx
                r[-1][1] = yy
            else:
                r.append([x,y])

            
        return len(r)

