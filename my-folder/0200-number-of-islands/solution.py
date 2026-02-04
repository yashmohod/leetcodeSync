class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def bfs(x,y):
            dirs = [[0,1],[0,-1],[-1,0],[1,0]]
            for dx,dy in dirs:
                xx = x+dx
                yy = y+dy
                if xx in range(len(grid[0])) and yy in range(len(grid))  and grid[yy][xx] == "1":
                    grid[yy][xx] = "0"
                    bfs(xx,yy)
                    
        res = 0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    bfs(j,i)
                    res+=1
        return res
