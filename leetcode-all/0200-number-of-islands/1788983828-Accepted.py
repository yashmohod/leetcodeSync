class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R = len(grid)
        C = len(grid[0])
        def bfs(r,c):
            q = deque([(r,c)])
            dirs = [[0,1],[0,-1],[1,0],[-1,0]]
            while q:
                pr,pc = q.popleft()
                if grid[pr][pc] =="1":
                    grid[pr][pc] = "0"
                    for dr,dc in dirs:
                        rr = dr+pr
                        cc = dc+pc
                        if 0<=rr <R and 0<=cc <C and grid[rr][cc] =="1":
                            q.append((rr,cc))

        qq = []
        for row in range(R):
            for col in range(C):
                if grid[row][col] == "1":
                    qq.append((col,row))
        
        count = 0

        for col,row in qq:
            if grid[row][col] == "1":
                count+=1
                bfs(row,col)
        return count






         
