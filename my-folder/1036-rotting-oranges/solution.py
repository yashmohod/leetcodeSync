class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        d = 0
        q = deque([])
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 2:
                    q.append((x,y,0))
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        while q :
            x,y,dd = q.popleft()
            d = max(dd,d)
            for dx,dy in dirs:
                xx = dx+x
                yy = dy+y
                if xx in range(len(grid[0])) and yy in range(len(grid)) and grid[yy][xx] == 1:
                    grid[yy][xx] = 2
                    q.append((xx,yy,d+1))
        for i in grid:
            if 1 in i :
                return -1
        return d
        
