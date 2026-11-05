from collections import deque
class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        

        q = deque([])

        for y in range(len(grid)):
            for x in range(len(grid)):
                if grid[y][x] ==1 :
                    q.append((x,y))
        

        d = 0
        c = 1
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        
        while q : 
            a = len(q)

            while a >0:
                x,y = q.popleft()
                for dx,dy in dirs:
                    xx,yy = dx+x,dy+y
                    if 0<=xx<len(grid) and 0<=yy<len(grid) and grid[yy][xx] ==0:
                        grid[yy][xx] = c
                        q.append((xx,yy))
                        d = max(c,d) 
                a-=1
            c+=1
        return d






