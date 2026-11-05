from collections import deque
class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        

        q = deque([])
        o,z=0,0
        N= len(grid)
        for y in range(N):
            for x in range(N):
                if grid[y][x] ==1 :
                    q.append((x,y))
                    o+=1
                else:
                    z+=1
        if z == N*N or o == N*N:
            return -1
        
        d = 0
        c = 1
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        
        while q : 
            a = len(q)

            while a >0:
                x,y = q.popleft()
                for dx,dy in dirs:
                    xx,yy = dx+x,dy+y
                    if 0<=xx<N and 0<=yy<N and grid[yy][xx] ==0:
                        grid[yy][xx] = c
                        q.append((xx,yy))
                        d = max(c,d) 
                a-=1
            c+=1
        return d






