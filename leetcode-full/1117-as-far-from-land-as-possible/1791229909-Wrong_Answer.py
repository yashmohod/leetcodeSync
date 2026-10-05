class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        q = deque([])
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 1:
                    q.append((x,y))

        if not q or len(q) == len(grid) * len(grid[0]): return -1
        res = -1
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q:
            size = len(q)
            res +=1
            while size:
                size -= 1
                x,y = q.popleft()
                for dx,dy in dirs:
                    xx,yy = x+dx,y+dy
                    if 0 <= xx < len(grid[0]) and 0 <= yy < len(grid) and grid[yy][xx] ==0:
                        grid[y][x] = 1
                        q.append((xx,yy))
        return res


                
