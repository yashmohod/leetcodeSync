class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        q = deque([])
        fresh,time = 0,0
        rows,cols = len(grid), len(grid[0])
        for y in range(rows):
            for x in range(cols):
                if grid[y][x] == 1:
                    fresh +=1
                if grid[y][x] == 2:
                    q.append((x,y))
        dirs = [[0,-1],[0,1],[-1,0],[1,0]]
        res = 0
        while q and fresh> 0:
            for _ in range(len(q)):
                x,y = q.popleft()
                for dx,dy in dirs:
                    if 0<= dx+x< cols and 0<= dy+y< rows and grid[dy+y][dx+x]==1:
                        grid[dy+y][dx+x]= 2
                        fresh-=1
                        q.append((dx+x,dy+y))
            time+=1

        return time if fresh <=0 else -1
