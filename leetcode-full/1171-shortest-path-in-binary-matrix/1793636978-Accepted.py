from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        N = len(grid) 
        dirs = [
            [0,1],[0,-1],[1,0],[-1,0],
            [1,1],[-1,1],[1,-1],[-1,-1]
            ]

        if grid[0][0] != 0 or grid[N-1][N-1] != 0:
            return -1
        q = deque([(0,0,0)])

        while q:
            x,y,c = q.popleft() 
            if x == N-1 and y == N-1:
                return  c+1
            
            for dx,dy in dirs:
                xx = x+dx
                yy = y+dy
                if 0<=xx<N and 0<=yy<N and grid[yy][xx] == 0:
                    grid[yy][xx] = 1
                    q.append((xx,yy,c+1)) 
            
        
        return -1


