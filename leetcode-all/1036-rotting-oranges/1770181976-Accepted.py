class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        q = deque([])
        res = 0
        fresh = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 2:
                    q.append((x,y,0))
                elif grid[y][x] == 1:
                    fresh +=1
        
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        while q :
            x,y,c = q.popleft()
            res = max(res,c)

            for dx,dy in dirs:
                xx = dx+x
                yy = dy+y
                if xx in range(len(grid[0])) and yy in range(len(grid)) and grid[yy][xx] == 1 :
                    grid[yy][xx] = 2
                    q.append((xx,yy,c+1))
                    fresh-=1

        return res if fresh == 0 else -1



