class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid :
            return 0

        islands = 0 
        rows = len(grid)
        cols = len(grid[0])
        # visited = set()

        def bfs (r,c):
            q = collections.deque()
            q.append((r,c))
            # visited.add((r,c))
            grid[r][c]="0"
            
            while q:
                r,c = q.pop()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in directions:
                    rn = dr +r
                    cn = dc +c
                    if(
                        rn in range(rows)and 
                        cn in range(cols)and
                        grid[rn][cn] == "1"
                    ):
                        q.append((rn,cn))
                        grid[rn][cn]="0"



        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r,c)
                    islands+=1
        return islands

