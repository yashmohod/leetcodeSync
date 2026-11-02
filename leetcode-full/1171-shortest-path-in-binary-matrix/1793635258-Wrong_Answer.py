from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        N = len(grid) 
        dirs = [ [0,1],[0,-1],[1,0],[-1,0]]
        dirs2=[[1,1],[-1,1],[1,-1],[-1,-1]]

        def dfs(x,y):

            if x == N-1 and y == N-1:
                return 0
            
            for dx,dy in dirs:
                xx = x+dx
                yy = y+dy
                if 0<=xx<N and 0<=yy<N and grid[yy][xx] == 0:
                    grid[yy][xx] = 1
                    r = dfs(xx,yy) 
                    if r >-1:
                        return r+1
            for dx,dy in dirs2:
                xx = x+dx
                yy = y+dy
                if 0<=xx<N and 0<=yy<N and grid[yy][xx] == 0:
                    grid[yy][xx] = 1
                    r = dfs(xx,yy) 
                    if r >-1:
                        return r+2
            return -1 
        
        return dfs(0,0) if grid[0][0] == 0 and grid[N-1][N-1] == 0 else -1


