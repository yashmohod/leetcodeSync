class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        q = deque([])
        fresh = 0
        rows,cols = len(grid), len(grid[0])
        for y in range(row):
            for x in range(cols):
                if grid[y][x] == 1:
                    fresh +=1
                if grid[y][x] == 2:
                    q.append((x,y,0))
        dirs = [[0,-1],[0,1],[-1,0],[1,0]]
        res = 0
        while q:
            x,y,c = q.popleft()
            res = max(res,c)
            for dx,dy in dirs:
                if 0<= dx+x< cols and 0<= dy+y< rows and grid[dy+y][dx+x]==1:
                    grid[dy+y][dx+x]= 2
                    fresh-=1
                    q.append((dx+x,dy+y,c+1))

        return res if fresh <=0 else -1
