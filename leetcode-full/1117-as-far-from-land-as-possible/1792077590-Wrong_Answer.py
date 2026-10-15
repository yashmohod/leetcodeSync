class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
       
        q = deque([])
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x]:
                    q.append((x,y))
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        m=0
        while q:
            c = len(q)
            m+=1
            while c>0:
                x,y = q.popleft()
                for dx,dy in dirs:
                    xx,yy = x+dx,y+dy
                    if 0<= xx < len(grid[0]) and 0<= yy <len(grid) and grid[yy][xx] ==0:
                        q.append((xx,yy))
                        grid[yy][xx] = m
                c-=1

        return m-1
