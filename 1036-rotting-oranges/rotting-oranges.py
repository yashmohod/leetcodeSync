class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        q = deque([])
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]==2:
                    q.append((row,col,0))
        
        res = 0 
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        while q :
            r,c,t = q.popleft()

            if grid[r][c] == 1:
                t +=1
                res = max(res,t)
                grid[r][c] = 2
            
            if grid[r][c] == 2:
                for dr,dc in dirs:
                    rr = dr+r
                    cc = dc+c
                    if 0<=rr < len(grid) and 0<= cc < len(grid[0]) and grid[rr][cc] == 1:
                        q.append((rr,cc,t))
        
        for row in range(len(grid)):
            if 1 in grid[row]:
                return -1
        return res 