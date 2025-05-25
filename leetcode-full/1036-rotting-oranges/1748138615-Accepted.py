class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        layers =[]
        q = deque()
        for x in range(len(grid[0])):
            for y in range(len(grid)):
                if grid[y][x] == 2 :
                    q.append((x,y,0))

        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        while q :
            x,y,t = q.popleft()
            for xn,yn in directions:
                xx = x+xn
                yy = y+yn
                if (xx in range(len(grid[0])) and 
                    yy in range(len(grid))    and
                    grid[yy][xx] == 1          
                    ):
                    q.append((xx,yy,t+1))
                    grid[yy][xx] = 2
                    if t +1. not in layers:
                        layers.append(t+1)
        found = True
        for i in grid:
            # print(i)
            if 1 in i :
                found = False

        if found :
            if len(layers) == 0 :
                return 0
            return max(layers)
        

        return -1 

