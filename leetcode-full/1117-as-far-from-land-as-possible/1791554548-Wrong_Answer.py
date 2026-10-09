class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        

        q = deque([])
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 1:
                    q.append((x,y))
        
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        d = 0
        r = 0
        while q:
            d+=1
            c = len(q)
            while c > 0:
                x,y = q.popleft()
                for dx,dy in dirs:
                    xx,yy = x+dx, y+dy

                    if 0<=xx<len(grid[0]) and 0<=yy<len(grid) and grid[yy][xx] ==0:
                        grid[yy][xx]=d
                        r = max(d,r)
                        q.append((xx,yy))
                c-=1
        for i in grid:
            if 0 in i:
                return -1
        return r


                
