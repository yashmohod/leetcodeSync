class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def bfs(x,y,visited):
            dirs=[[0,1],[0,-1],[1,0],[-1,0]]
            q = deque([(x,y)])
            while(q):
                cx,cy = q.popleft()
                grid[cy][cx] = "0"
                for dx,dy in dirs:
                    if  dx+cx < len(grid[0]) and dy+cy < len(grid) and ((dx+cx,dy+cy) not in visited) and grid[dy+cy][dx+cx] =="1":
                        
                        visited.add((dx+cx,dy+cy))
                        q.append((dx+cx,dy+cy))
        visited = set()
        res = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "1":
                    visited.add((x,y))
                    bfs(x,y,visited)
                    res += 1
        return res





         
