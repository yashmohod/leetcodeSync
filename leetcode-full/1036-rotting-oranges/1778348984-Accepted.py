class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        q = deque([])
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 2:
                    q.append((x,y,0))
        dirs = [[0,-1],[0,1],[-1,0],[1,0]]
        res = 0
        while q:
            x,y,c = q.popleft()
            res = max(res,c)
            for dx,dy in dirs:
                if 0<= dx+x< len(grid[0]) and 0<= dy+y< len(grid) and grid[dy+y][dx+x]==1:
                    grid[dy+y][dx+x]= 2
                    q.append((dx+x,dy+y,c+1))

        for i in grid:
            if 1 in i:
                return -1
        return res 
