class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def bfs(x,y):
            dirs=[[0,1],[0,-1],[1,0],[-1,0]]
            q = deque([(x,y)])
            while(q):
                cx,cy = q.popleft()
                for dx,dy in dirs:
                    if  0<=dx+cx < len(grid[0]) and 0<= dy+cy < len(grid)  and grid[dy+cy][dx+cx] =="1":   
                        grid[dy+cy][dx+cx] = "0"
                        q.append((dx+cx,dy+cy))
        res = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "1":
                    grid[y][x] == "0"
                    bfs(x,y)
                    res += 1
        return res





         
